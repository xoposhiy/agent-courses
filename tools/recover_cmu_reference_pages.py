"""Convert two browser-recovered reference pages and preserve their public data."""

from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import re
import shutil
from threading import Event, Lock
import time
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup
from markdownify import markdownify
import requests

from collect_cmu_colorado import ROOT, SnapshotCorpus, finish_cmu
from corpus import code_block
from recover_cmu_docent import raw_metadata, register


SOURCE = ROOT / 'tmp' / 'recoveries' / 'reference-pages'


def rendered_page(corpus, source_name, identifier, title, note):
    source = json.loads((SOURCE / source_name).read_text(encoding='utf-8'))
    directory = corpus.root / 'raw' / 'recoveries' / 'reference-pages'
    directory.mkdir(parents=True, exist_ok=True)
    raw = directory / (identifier + '.html')
    raw.write_text(source['html'], encoding='utf-8')
    soup = BeautifulSoup(source['html'], 'html.parser')
    for element in soup.select('script, style, nav, footer, noscript, svg, form, #cookie-consent-banner, #wcpConsentBannerCtrl'):
        element.decompose()
    main = soup.select_one('[role="main"]') or soup.select_one('main') or soup.select_one('article') or soup.body or soup
    for anchor in main.select('a[href]'):
        anchor['href'] = urljoin(source['url'], anchor['href'])
    images = {}
    for image in main.select('img[src]'):
        original = image['src']
        if not original or original.startswith('data:'):
            continue
        url = urljoin(source['url'], original)
        image['src'] = url
        images.setdefault(url, []).append(image)
    assets = []
    notes = [note]
    existing = next((x for x in corpus.data['materials'] if x['id'] == identifier), {})
    prior_assets = {asset.get('original_url', asset['url']): asset for asset in existing.get('assets', [])}
    wikimedia_lock = Lock()
    wikimedia_throttled = Event()

    def request_image(url):
        response = requests.get(url, timeout=(10, 25), headers={'User-Agent': corpus.session.headers['User-Agent']})
        if response.status_code == 429 and 'thumbnail' not in response.text.lower():
            delay = response.headers.get('Retry-After', '10')
            time.sleep(min(int(delay) if delay.isdigit() else 10, 30))
            response = requests.get(url, timeout=(10, 25), headers={'User-Agent': corpus.session.headers['User-Agent']})
            if response.status_code == 429 and urlsplit(url).netloc == 'upload.wikimedia.org':
                wikimedia_throttled.set()
        return response

    def fetch(url):
        lock = wikimedia_lock if urlsplit(url).netloc == 'upload.wikimedia.org' else Lock()
        try:
            prior = prior_assets.get(url)
            if prior and (corpus.root / prior['raw_path']).is_file():
                path = corpus.root / prior['raw_path']
                return url, path, path.read_bytes(), None, prior['url']
            with lock:
                if urlsplit(url).netloc == 'upload.wikimedia.org' and wikimedia_throttled.is_set():
                    raise ValueError('The image host is still rate-limited after a bounded retry; additional requests were deferred')
                response = request_image(url)
                download_url = url
                if response.status_code in (400, 429) and urlsplit(url).netloc == 'upload.wikimedia.org' and '/thumb/' in urlsplit(url).path and 'thumbnail' in response.text.lower():
                    match = re.search(r'/(\d+)px-', urlsplit(url).path)
                    if match:
                        width = int(match.group(1))
                        standard = next((x for x in (20, 40, 60, 120, 250, 330, 500, 960, 1280, 1920, 3840) if x >= width), None)
                        if standard and standard != width:
                            download_url = re.sub(r'/\d+px-', '/' + str(standard) + 'px-', url, count=1)
                            response = request_image(download_url)
            response.raise_for_status()
            content_type = response.headers.get('Content-Type', '').split(';', 1)[0]
            if not content_type.startswith('image/'):
                raise ValueError('The image URL did not return an image')
            extension = Path(urlsplit(response.url).path).suffix.lower()
            if extension not in ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.avif'):
                extension = mimetypes.guess_extension(content_type) or '.img'
            path = directory / (identifier + '-assets') / (hashlib.sha256(url.encode()).hexdigest()[:20] + extension)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(response.content)
            return url, path, response.content, None, download_url
        except Exception as error:
            return url, None, None, type(error).__name__ + ': ' + str(error), url
    with ThreadPoolExecutor(max_workers=4) as pool:
        for future in as_completed([pool.submit(fetch, url) for url in images]):
            url, path, body, error, download_url = future.result()
            if error:
                notes.append('Image remains remote: ' + url + '. ' + error)
            else:
                target = os.path.relpath(path, corpus.root / 'markdown' / 'optional-readings').replace('\\', '/')
                for image in images[url]:
                    image['src'] = target
                asset = dict(url=download_url, raw_path=path.relative_to(corpus.root).as_posix(), bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
                if download_url != url:
                    asset['original_url'] = url
                assets.append(asset)
    if any(asset.get('original_url') for asset in assets):
        notes.append('Wikimedia rejects old nonstandard thumbnail widths. The same source images were archived at the nearest larger permitted thumbnail size, as documented at https://www.mediawiki.org/wiki/Common_thumbnail_sizes. Each asset records its original and downloaded URL.')
    content = markdownify(str(main), heading_style='ATX', bullets='-')
    item = register(corpus, identifier, title, source['url'], raw, content, 'rendered-dom-main-content-to-markdown', notes,
                    final_url=source['url'], assets=assets, rendered_visible_chars=len(source.get('text', '')),
                    image_urls=len(images), downloaded_image_urls=len(assets))
    item['notes'] = notes
    if len(assets) != len(images):
        item['conversion_status'] = 'converted_with_limitations'
    for original in corpus.data['materials']:
        if original is not item and original['url'] == item['url'] and original.get('conversion_status') in ('failed', 'not_available'):
            original['recovered_by'] = item['markdown_path']
            original['notes'].append('The complete public page was recovered after browser rendering; see the recovered copy linked in this report.')
    corpus.save()
    print('Rendered reference recovered:', title, 'images', len(assets), '/', len(images), flush=True)
    return item


def main():
    corpus = SnapshotCorpus(ROOT / 'courses' / 'cmu-11768', 'cmu-11768', 'CMU 11-768: AI Agents', 'https://www.cmu-agents.com/')
    rendered_page(corpus, 'natural-questions-render.json', 'natural-questions-rendered',
                  'Natural Questions: Train Set Examples and Data Browser',
                  'The full publicly rendered Train Set Examples page is archived, including all rendered question/answer tables. This is the exact linked example page, not a recursive download of the Natural Questions corpus or its source Wikipedia articles.')
    advisory = rendered_page(corpus, 'msrc-render.json', 'msrc-cve-2025-32711-rendered',
                             'Microsoft advisory CVE-2025-32711: M365 Copilot Information Disclosure Vulnerability',
                             'The public advisory was captured after its content loaded. The complete official vulnerability, acknowledgement, and affected-product API payloads are preserved below and as raw JSON. No customer action or security operation was performed.')
    directory = corpus.root / 'raw' / 'recoveries' / 'reference-pages'
    network = (SOURCE / 'msrc-network.txt').read_text(encoding='utf-8')
    shutil.copy2(SOURCE / 'msrc-network.txt', directory / 'msrc-network.txt')
    path = corpus.root / advisory['markdown_path']
    content = path.read_text(encoding='utf-8')
    public_payloads = []
    for number, label in [(2444, 'Complete official vulnerability record'), (2445, 'Complete official acknowledgements'), (2446, 'Complete official affected-product record')]:
        match = re.search(str(number) + r'\. \[GET\] (\S+) => \[200\]', network)
        if not match:
            raise ValueError('The original public source URL is missing for API response ' + str(number))
        target = directory / f'msrc-response-{number}.json'
        shutil.copy2(SOURCE / f'msrc-response-{number}.json', target)
        payload = json.loads(target.read_text(encoding='utf-8'))
        if payload.get('@odata.nextLink'):
            raise ValueError('The advisory API response requires another page')
        if '@odata.count' in payload and payload['@odata.count'] != len(payload['value']):
            raise ValueError('The advisory API count does not match the retrieved values')
        meta = raw_metadata(corpus, target, match.group(1))
        meta['http_status'] = 200
        public_payloads.append(meta)
        local = os.path.relpath(target, path.parent).replace('\\', '/')
        content += '\n## ' + label + f'\n\n[Original JSON response]({local})\n\n' + code_block(json.dumps(payload, indent=2, ensure_ascii=False), 'json') + '\n'
    path.write_text(content, encoding='utf-8')
    advisory['source_evidence'] = public_payloads
    advisory['api_payload_counts'] = {'vulnerability_records': 1, 'acknowledgements': 2, 'affected_products': 1, 'next_pages': 0}
    corpus.save()
    finish_cmu(corpus)
    print(json.dumps(corpus.data['counts']), flush=True)


if __name__ == '__main__':
    main()
