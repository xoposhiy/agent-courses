"""Repair links after source recoveries and retry three missing source images."""

from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import os
from pathlib import Path
import re
from urllib.parse import urldefrag, urljoin, urlsplit

from collect_cmu_colorado import ROOT, SnapshotCorpus
from corpus import map_prose


def main():
    corpus = SnapshotCorpus(ROOT / 'courses' / 'cmu-11768', 'cmu-11768', 'CMU 11-768: AI Agents', 'https://www.cmu-agents.com/')
    images = [
        ('ref-6dba8b525a6d', '/images/icons/DeepInfra.webp'),
        ('ref-8c3acf43834d', '/news/introducing-inkling/images/webdev-bua-poster.b1e43fec7e6ea270b760cf764d3f76e2.jpg'),
        ('ref-8c3acf43834d', '/news/introducing-inkling/images/snake-game-poster.d1880cb231040fdcb3acc7abc45c6e04.jpg'),
    ]
    def fetch(spec):
        identifier, old_target = spec
        item = next(x for x in corpus.data['materials'] if x['id'] == identifier)
        url = urljoin(item.get('final_url', item['url']), old_target)
        try:
            response = corpus.request(url)
            response.raise_for_status()
            if not response.headers.get('Content-Type', '').startswith('image/'):
                raise ValueError('The image target did not return an image')
            return item, old_target, url, response.content, None
        except Exception as error:
            return item, old_target, url, None, str(error)
    with ThreadPoolExecutor(max_workers=3) as pool:
        for future in as_completed([pool.submit(fetch, spec) for spec in images]):
            item, old_target, url, body, error = future.result()
            path = corpus.root / item['markdown_path']
            content = path.read_text(encoding='utf-8')
            if body:
                image_path = corpus.root / 'raw' / 'assets' / (hashlib.sha256(url.encode()).hexdigest()[:16] + Path(urlsplit(url).path).suffix)
                image_path.write_bytes(body)
                new_target = os.path.relpath(image_path, path.parent).replace('\\', '/')
                asset = dict(url=url, raw_path=image_path.relative_to(corpus.root).as_posix(), bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
                if not any(x.get('url') == url for x in item.setdefault('assets', [])):
                    item['assets'].append(asset)
                item['notes'] = [note for note in item['notes'] if note != 'Image remains remote: ' + url]
            else:
                new_target = url
                note = 'Image remains remote: ' + url + '. A later public retry also failed: ' + error
                if note not in item['notes']:
                    item['notes'].append(note)
                item['conversion_status'] = 'converted_with_limitations'
            path.write_text(content.replace('](' + old_target + ')', '](' + new_target + ')'), encoding='utf-8')
            print('Image:', url, 'recovered' if body else 'remote fallback', flush=True)
    redirects = {}
    for item in corpus.data['materials']:
        if not item.get('recovered_by'):
            continue
        old_path = corpus.root / 'markdown' / item['category'] / (item['id'] + '.md')
        if not old_path.exists():
            redirects[os.path.normcase(os.path.abspath(old_path))] = corpus.root / item['recovered_by']
    repaired = 0
    for item in corpus.data['materials']:
        if not item.get('markdown_path'):
            continue
        path = corpus.root / item['markdown_path']
        content = path.read_text(encoding='utf-8')
        def rewrite(match):
            nonlocal repaired
            label, target = match.groups()
            if urlsplit(target).scheme or target.startswith('#'):
                return match.group()
            base, fragment = urldefrag(target)
            key = os.path.normcase(os.path.abspath(path.parent / base))
            destination = redirects.get(key)
            if not destination:
                return match.group()
            new_target = os.path.relpath(destination, path.parent).replace('\\', '/')
            if fragment:
                new_target += '#' + fragment
            repaired += 1
            return f'{label}({new_target})'
        updated = map_prose(content, lambda line: re.sub(r'(?<!\\)(!?\[[^\]]+\])\(([^\s)]+)\)', rewrite, line))
        if updated != content:
            path.write_text(updated, encoding='utf-8')
    corpus.write_indexes()
    print('Recovered document links repaired:', repaired, flush=True)


if __name__ == '__main__':
    main()
