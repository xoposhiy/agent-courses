"""Collect the CMU AI Agents and CU Boulder Building AI Agents course sources."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import re
from urllib.parse import parse_qs, urldefrag, urljoin, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify
import requests

from corpus import Corpus, map_prose, slug
from network_pacing import paced_host


ROOT = Path(__file__).resolve().parents[1]


class SnapshotCorpus(Corpus):
    def __init__(self, *args):
        super().__init__(*args)
        self.snapshots = {}
        self.cache_hits = {}
        cache_path = self.root / 'optional-fetches.json'
        self.fetch_cache = json.loads(cache_path.read_text(encoding='utf-8')) if cache_path.is_file() else []
        for manifest_path in (ROOT / 'courses').glob('*/manifest.json'):
            if manifest_path.parent.resolve() == self.root.resolve():
                continue
            try:
                data = json.loads(manifest_path.read_text(encoding='utf-8'))
            except (OSError, ValueError):
                continue
            for record in data.get('materials', []):
                if record.get('download_status') != 'downloaded' or not record.get('raw_path'):
                    continue
                path = manifest_path.parent / record['raw_path']
                if not path.is_file():
                    continue
                for url in [record.get('url'), record.get('final_url'), *record.get('aliases', [])]:
                    if url:
                        self.snapshots[url] = (path, record.get('content_type', ''), record.get('retrieved_at'), data['source_id'])
                for asset in record.get('assets', []):
                    if not asset.get('url') or not asset.get('raw_path'):
                        continue
                    asset_path = manifest_path.parent / asset['raw_path']
                    if asset_path.is_file():
                        self.snapshots[asset['url']] = (asset_path, mimetypes.guess_type(asset_path.name)[0] or '', record.get('retrieved_at'), data['source_id'])

    def request(self, url):
        prefetched = next((x for x in self.fetch_cache if x['actual_url'] == url and x.get('raw_path')), None)
        if prefetched:
            response = requests.Response()
            response.status_code = prefetched['http_status']
            response.url = prefetched['final_url']
            response._content = (self.root / prefetched['raw_path']).read_bytes()
            response.encoding = 'utf-8'
            response.headers['Content-Type'] = prefetched['content_type']
            return response
        cached = self.snapshots.get(url)
        if cached:
            path, content_type, retrieved_at, source_id = cached
            response = requests.Response()
            response.status_code = 200
            response.url = url
            response._content = path.read_bytes()
            response.encoding = 'utf-8'
            response.headers['Content-Type'] = content_type or mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
            self.cache_hits[url] = f'Reused the source snapshot from {source_id}, retrieved at {retrieved_at}. The raw bytes are copied into this course archive.'
            return response
        return super().request(url)

    def add(self, *args, **kwargs):
        item = super().add(*args, **kwargs)
        note = self.cache_hits.get(item['url'])
        if note and note not in item['notes']:
            item['notes'].append(note)
            self.save()
        if item.get('download_status') == 'downloaded' and Path(item.get('raw_path', '')).suffix.lower() in ('.gif', '.png', '.jpg', '.jpeg', '.webp', '.svg'):
            markdown_parent = (self.root / item['markdown_path']).parent
            image_path = os.path.relpath(self.root / item['raw_path'], markdown_parent).replace('\\', '/')
            item['conversion_method'] = 'original-image-embedded-in-markdown'
            self.write_markdown(item, f'![{item["title"]}]({image_path})')
            self.save()
        return item

    def gap(self, url, title, category, reason, status='unavailable'):
        old = next((x for x in self.data['materials'] if x['url'] == url and x['category'] == category and x.get('conversion_status') == 'not_available'), None)
        return old or self.record_gap(url, title, category, reason, status)


def add_raw(corpus, url, title, path, category='metadata', notes=None):
    old = next((x for x in corpus.data['materials'] if x['url'] == url and x.get('raw_path') == path.relative_to(corpus.root).as_posix()), None)
    if old:
        return old
    body = path.read_bytes()
    item = dict(id='source-' + slug(path.stem), title=title, url=url, category=category,
                retrieved_at=datetime.now(timezone.utc).isoformat(), download_status='downloaded',
                conversion_status='not_required', raw_path=path.relative_to(corpus.root).as_posix(),
                bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), notes=notes or [])
    corpus.data['materials'].append(item)
    corpus.save()
    return item


def clean_html(corpus, item, selector=None):
    soup = BeautifulSoup((corpus.root / item['raw_path']).read_bytes(), 'html.parser')
    for element in soup.select('script, style, nav, footer, noscript, svg, form'):
        element.decompose()
    main = soup.select_one(selector) if selector else soup.select_one('article') or soup.select_one('main') or soup.body or soup
    for anchor in main.select('a[href]'):
        anchor['href'] = urljoin(item['url'], anchor['href'])
    for image in main.select('img[src]'):
        image['src'] = urljoin(item['url'], image['src'])
    return markdownify(str(main), heading_style='ATX', bullets='-')


def cmu_route_links(text, parent, corpus):
    def replace(match):
        label, url = match.groups()
        if not url.startswith('https://www.cmu-agents.com/#/'):
            return match.group()
        parts = url.split('#/', 1)[1].strip('/').split('/')
        route = parts[0] or 'home'
        if route not in ('home', 'schedule', 'assignments', 'project', 'syllabus', 'staff', 'sponsorship'):
            return match.group()
        dest = corpus.root / 'markdown' / 'pages' / ('page-' + route + '.md')
        target = os.path.relpath(dest, parent).replace('\\', '/')
        if len(parts) > 1:
            target += '#' + '/'.join(parts[1:])
        return f'[{label}]({target})'
    return map_prose(text, lambda line: re.sub(r'(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)', replace, line))


def cmu_pages(corpus):
    data = json.loads((corpus.root / 'discovery.json').read_text(encoding='utf-8'))
    for page in data:
        item = next((x for x in corpus.data['materials'] if x['url'] == page['url']), None)
        raw = corpus.root / 'raw' / 'pages' / (page['route'] + '.html')
        if not item:
            body = raw.read_bytes()
            item = dict(id='page-' + page['route'], title='CMU 11-768: ' + page['route'].title(), url=page['url'], category='pages',
                        retrieved_at=datetime.now(timezone.utc).isoformat(), download_status='downloaded', conversion_status='converted',
                        raw_path=raw.relative_to(corpus.root).as_posix(), bytes=len(body), sha256=hashlib.sha256(body).hexdigest(),
                        conversion_method='rendered-dom-main-content-to-markdown', notes=['The official site is a client-rendered application. This raw file is the fully rendered DOM for the stated route. The HTTP shell and JavaScript bundle are stored separately.'])
            corpus.data['materials'].append(item)
        content = clean_html(corpus, item, '#content')
        parent = corpus.root / 'markdown' / 'pages'
        content = cmu_route_links(content, parent, corpus)
        corpus.write_markdown(item, content)
    # A plain root URL must resolve to the home page when the common finalizer removes a fragment.
    corpus.data['materials'].sort(key=lambda x: x.get('url') == 'https://www.cmu-agents.com/#/')
    corpus.save()
    return data


def material(corpus, url, title, category='readings'):
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    name = ('arxiv-' + parsed.path.rsplit('/', 1)[-1].removesuffix('.pdf')) if 'arxiv.org' in host else 'ref-' + hashlib.sha256(url.encode()).hexdigest()[:12]
    if host.endswith('arxiv.org'):
        identifier = re.sub(r'^/(?:abs|pdf|html)/', '', parsed.path).removesuffix('.pdf')
        result = corpus.add('https://arxiv.org/pdf/' + identifier, title, category, name, expected='pdf')
        result.setdefault('aliases', []).extend(x for x in [url, 'https://arxiv.org/abs/' + identifier] if x not in result.get('aliases', []))
        corpus.save()
        return result
    if host == 'aclanthology.org':
        pdf_url = url if parsed.path.endswith('.pdf') else url.rstrip('/') + '.pdf'
        result = corpus.add(pdf_url, title, category, name, expected='pdf')
        result.setdefault('aliases', []).append(url)
        corpus.save()
        return result
    if host == 'github.com':
        parts = parsed.path.strip('/').split('/')
        if len(parts) >= 4 and parts[2] in ('pull', 'issues'):
            return corpus.add(url, title, category, name)
        if len(parts) >= 5 and parts[2] == 'blob':
            raw_url = 'https://raw.githubusercontent.com/' + '/'.join(parts[:2] + parts[3:])
        elif len(parts) >= 4 and parts[2] == 'tree':
            raw_url = 'https://raw.githubusercontent.com/' + '/'.join(parts[:2] + parts[3:]) + '/README.md'
        else:
            raw_url = 'https://raw.githubusercontent.com/' + '/'.join(parts[:2]) + '/HEAD/README.md'
        result = corpus.add(raw_url, title, category, name)
        result.setdefault('aliases', []).append(url)
        result['notes'].append('Only the explicitly linked source file or repository README is archived for this external reference; this is not a teaching-repository mirror.')
        corpus.save()
        return result
    if host == 'huggingface.co' and '/blob/' in parsed.path:
        raw_url = url.replace('/blob/', '/resolve/')
        result = corpus.add(raw_url, title, category, name)
        result.setdefault('aliases', []).append(url)
        corpus.save()
        return result
    if host == 'huggingface.co' and len(parsed.path.strip('/').split('/')) == 2 and not parsed.path.startswith('/docs/'):
        raw_url = url.rstrip('/') + '/raw/main/README.md'
        result = corpus.add(raw_url, title, category, name)
        result.setdefault('aliases', []).append(url)
        result['notes'].append('The public model card is archived as source Markdown. Model weights are excluded.')
        corpus.save()
        return result
    if host in ('youtube.com', 'www.youtube.com', 'youtu.be'):
        result = captions(corpus, url, title)
        result['course_relation'] = 'optional-reference' if category == 'optional-readings' else 'assigned-recording'
        corpus.save()
        return result
    if host == 'openreview.net':
        pdf_url = url.replace('/forum?', '/pdf?')
        result = corpus.add(pdf_url, title, category, name, expected='pdf')
        result.setdefault('aliases', []).append(url)
        corpus.save()
        return result
    if parsed.path.lower().endswith('.pdf'):
        return corpus.add(url, title, category, name, expected='pdf')
    result = corpus.add(url, title, category, name)
    if result.get('raw_path', '').endswith('.html') and result.get('download_status') == 'downloaded':
        soup = BeautifulSoup((corpus.root / result['raw_path']).read_bytes(), 'html.parser')
        pdf = soup.select_one('meta[name="citation_pdf_url"]')
        if pdf and pdf.get('content'):
            pdf_url = urljoin(url, pdf['content'])
            full = corpus.add(pdf_url, title + ' (PDF)', category, name + '-pdf', expected='pdf')
            if full.get('markdown_path'):
                full.setdefault('aliases', []).append(url)
    corpus.save()
    return result


COLORADO_ALTERNATES = {
    'https://link.springer.com/article/10.1007/s11704-024-40231-1?fromPaywallRec=true': ('https://arxiv.org/abs/2308.11432', 'The arXiv record lists the assigned Springer DOI as a related DOI. This is the public preprint version.'),
    'https://dl.acm.org/doi/epdf/10.1145/3715754': ('https://lingming.cs.illinois.edu/publications/fse2025.pdf', 'Public author-hosted copy of the assigned FSE paper; the first page identifies DOI 10.1145/3715754.'),
    'https://iopscience.iop.org/article/10.1088/2632-2153/ae4b07/pdf': ('https://arxiv.org/abs/2502.09565', 'Public arXiv preprint with matching title and authors. This preprint may differ from the published version.'),
    'https://dl.acm.org/doi/epdf/10.1145/3832783.3834393': ('https://arxiv.org/abs/2605.30777', 'Public arXiv preprint with matching title and authors. This preprint may differ from the published version.'),
    'https://dl.acm.org/doi/10.1145/3832783.3834400': ('https://arxiv.org/abs/2604.12147', 'Public arXiv preprint with matching title and authors. This preprint may differ from the published version.'),
    'https://openreview.net/pdf?id=zj7YuTE4t8': ('https://arxiv.org/abs/2305.14325', 'Public arXiv preprint with matching title and authors. This preprint may differ from the published version.'),
    'https://openreview.net/pdf?id=t32Hgnk7ou': ('https://arxiv.org/abs/2606.17799', 'Public arXiv preprint with matching title and authors. This preprint may differ from the published version.'),
}


def recover_colorado(corpus):
    recoveries = []
    for original_url, (alternate_url, note) in COLORADO_ALTERNATES.items():
        original = next((x for x in corpus.data['materials'] if x['url'] == original_url), None)
        if not original or original.get('page_count'):
            continue
        print('Public alternative', original['title'], alternate_url, flush=True)
        recovered = material(corpus, alternate_url, original['title'] + ' (public alternative)')
        if recovered.get('markdown_path'):
            recovered.setdefault('aliases', []).append(original_url)
            if note not in recovered['notes']:
                recovered['notes'].append(note)
            recovery_note = f"Full text recovered from [a public alternative]({recovered['markdown_path']}). {note}"
            if recovery_note not in original['notes']:
                original['notes'].append(recovery_note)
            recoveries.append(dict(original_url=original_url, alternate_url=alternate_url, markdown_path=recovered['markdown_path'], notes=note))
    (corpus.root / 'public-alternatives.json').write_text(json.dumps(recoveries, indent=2), encoding='utf-8')
    corpus.save()


def colorado():
    base = 'https://danny.cs.colorado.edu/courses/csci7000-009_F26/'
    corpus = SnapshotCorpus(ROOT / 'courses/colorado-csci7000', 'colorado-csci7000', 'CU Boulder CSCI 7000-09: Building AI Agents', base + 'index.html')
    pending = [base + 'index.html']
    seen = set()
    external = {}
    discovered = []
    while pending:
        url = pending.pop(0)
        if url in seen:
            continue
        seen.add(url)
        print('Course page', url, flush=True)
        item = corpus.add(url, 'Course ' + Path(urlparse(url).path).stem, 'pages', 'page-' + Path(urlparse(url).path).stem)
        if item.get('download_status') != 'downloaded':
            continue
        soup = BeautifulSoup((corpus.root / item['raw_path']).read_bytes(), 'html.parser')
        for anchor in soup.select('a[href]'):
            href = urldefrag(urljoin(url, anchor['href']))[0]
            title = re.sub(r'\s+', ' ', anchor.get_text(' ', strip=True))
            if not href or href.startswith('mailto:') or not title:
                continue
            entry = dict(source_page=url, title=title, url=href)
            discovered.append(entry)
            if href.startswith(base):
                path = urlparse(href).path
                if path.endswith('.html'):
                    pending.append(href)
                elif path.endswith('.pdf'):
                    corpus.add(href, title, 'slides' if '/pdfs/' in path else 'assignments', Path(path).stem, expected='pdf')
                continue
            host = urlparse(href).netloc
            if host in ('cuboulder.zoom.us', 'piazza.com'):
                corpus.gap(href, title, 'restricted', 'The course requires enrolled-student authentication for this service.', 'requires_login')
            elif href in ('http://danny.cs.colorado.edu', 'https://danny.cs.colorado.edu/', 'https://twitter.com/githubstatus', 'https://githubstatus.com', 'https://help.github.com/pages/'):
                continue
            else:
                external[href] = title
    corpus.gap(base + 'index.html', 'Agentic Refactoring paper on Canvas', 'restricted', 'The schedule states that the PDF is available in Canvas and provides no public paper title, author list, or download URL. It was not replaced with a guessed paper.', 'requires_login')
    for url, title in external.items():
        category = 'optional-readings' if title in ('article1', 'article2', 'ACM template', 'ACM Proceedings template', 'ACM SIG template') else 'readings'
        print('Reading', title, url, flush=True)
        actual_url = 'https://' + url[len('http://'):] if url.startswith('http://') else url
        result = material(corpus, actual_url, title, category)
        if actual_url != url:
            result.setdefault('aliases', []).append(url)
            result['notes'].append('The original course link used HTTP; the equivalent public HTTPS URL was requested.')
            corpus.save()
    recover_colorado(corpus)
    corpus.data['notes'] = list(dict.fromkeys(corpus.data['notes'] + [
        'Collected while Fall 2026 was in progress. Only one course-owned slide PDF was linked publicly; the schedule also describes sessions without posted materials.',
        'All course-owned HTML links were followed. Future milestone and final-project links that returned HTTP 404 are recorded as failed retrievals, not converted course content.',
        'Publisher or OpenReview failures are retained as retrieval evidence. Where a matching author-hosted paper or preprint was found, the alternative version is recorded separately and linked from the failed request.',
        'The Canvas-only Agentic Refactoring paper has no public identifier in the schedule; no substitute paper was guessed.',
        'The course schedule links no public video recordings or teaching code repositories.',
    ]))
    corpus.finalize()
    present = {x['url'] for x in corpus.data['materials']}
    present.update(alias for x in corpus.data['materials'] for alias in x.get('aliases', []))
    excluded = ('http://danny.cs.colorado.edu', 'https://danny.cs.colorado.edu/', 'https://twitter.com/githubstatus', 'https://githubstatus.com', 'https://help.github.com/pages/')
    relevant = {x['url'] for x in discovered if not x['url'].startswith('mailto:') and x['url'] not in excluded}
    (corpus.root / 'discovery.json').write_text(json.dumps(discovered, indent=2), encoding='utf-8')
    (corpus.root / 'coverage.json').write_text(json.dumps({'scope': 'All course-owned linked pages and PDFs; all explicitly linked readings and teaching guidance, one level only.', 'unique_course_pages_checked': len(seen), 'unique_relevant_links': len(relevant), 'represented': len(relevant & present), 'missing_links': sorted(relevant - present)}, indent=2), encoding='utf-8')
    print(json.dumps(corpus.data.get('counts')), flush=True)


def captions(corpus, url, title):
    old = next((x for x in corpus.data['materials'] if x['url'] == url and x.get('conversion_method') == 'public-caption-text'), None)
    if old:
        return old
    identifier = parse_qs(urlparse(url).query).get('v', [urlparse(url).path.rsplit('/', 1)[-1]])[0]
    item = corpus.gap(url, title, 'videos', 'Large video binary excluded. Public English caption retrieval is attempted.', 'video_not_downloaded')
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        class TimedSession(requests.Session):
            def request(self, *args, **kwargs):
                kwargs.setdefault('timeout', 25)
                return super().request(*args, **kwargs)
        transcript = YouTubeTranscriptApi(http_client=TimedSession()).fetch(identifier, languages=('en',))
        raw = corpus.root / 'raw' / 'videos' / (identifier + '.json')
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text(json.dumps(transcript.to_raw_data(), indent=2, ensure_ascii=False), encoding='utf-8')
        body = raw.read_bytes()
        item.update(id='video-' + identifier, raw_path=raw.relative_to(corpus.root).as_posix(), bytes=len(body), sha256=hashlib.sha256(body).hexdigest(),
                    download_status='downloaded', conversion_status='converted', conversion_method='public-caption-text',
                    notes=['The full public English caption track is archived. Captions may contain recognition errors. The large video binary is excluded.'])
        content = '\n\n'.join(f'[{int(x.start // 60):02d}:{int(x.start % 60):02d}] {x.text}' for x in transcript)
        corpus.write_markdown(item, content)
    except Exception as error:
        item['notes'].append('Caption attempt failed: ' + type(error).__name__ + ': ' + str(error)[:1200])
    corpus.save()
    return item


def prefetch_slides(corpus, entries):
    def fetch(entry):
        url, title = entry['url'], entry['title']
        name = Path(urlparse(url).path).stem
        target = corpus.root / 'raw' / 'slides' / (name + '.pdf')
        if target.is_file() and target.read_bytes()[:5] == b'%PDF-':
            return url, title, name, None
        try:
            response = requests.get(url, timeout=(15, 70))
            response.raise_for_status()
            if not response.content.startswith(b'%PDF-'):
                raise ValueError('Slide URL did not return a PDF')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(response.content)
            return url, title, name, None
        except Exception as error:
            return url, title, name, str(error)
    with ThreadPoolExecutor(max_workers=4) as pool:
        for future in as_completed([pool.submit(fetch, entry) for entry in entries]):
            url, title, name, error = future.result()
            print('Slide', name, error or 'downloaded', flush=True)
            corpus.add(url, title, 'slides', name, expected='pdf')


def optional_target(url):
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    name = 'ref-' + hashlib.sha256(url.encode()).hexdigest()[:12]
    if host.endswith('arxiv.org'):
        identifier = re.sub(r'^/(?:abs|pdf|html)/', '', parsed.path).removesuffix('.pdf')
        return 'https://arxiv.org/pdf/' + identifier, slug('arxiv-' + identifier)
    if host == 'aclanthology.org':
        return (url if parsed.path.endswith('.pdf') else url.rstrip('/') + '.pdf'), name
    if host == 'openreview.net':
        return url.replace('/forum?', '/pdf?'), name
    if host == 'github.com':
        parts = parsed.path.strip('/').split('/')
        if len(parts) >= 4 and parts[2] in ('pull', 'issues'):
            return url, name
        if len(parts) >= 5 and parts[2] == 'blob':
            return 'https://raw.githubusercontent.com/' + '/'.join(parts[:2] + parts[3:]), name
        if len(parts) >= 4 and parts[2] == 'tree':
            return 'https://raw.githubusercontent.com/' + '/'.join(parts[:2] + parts[3:]) + '/README.md', name
        return 'https://raw.githubusercontent.com/' + '/'.join(parts[:2]) + '/HEAD/README.md', name
    if host == 'huggingface.co' and '/blob/' in parsed.path:
        return url.replace('/blob/', '/resolve/'), name
    if host == 'huggingface.co' and len(parsed.path.strip('/').split('/')) == 2 and not parsed.path.startswith('/docs/'):
        return url.rstrip('/') + '/raw/main/README.md', name
    return url, name


def collect_optional(corpus, links):
    assigned = {x['url'] for x in links if x['category'] == 'Readings:'}
    represented = {x['url'] for x in corpus.data['materials']}
    represented.update(a for x in corpus.data['materials'] for a in x.get('aliases', []))
    seen = assigned | represented
    pending = []
    for entry in links:
        if entry['category'] == 'references' and entry['url'] not in seen:
            seen.add(entry['url'])
            pending.append(entry)

    def fetch(entry):
        actual, name = optional_target(entry['url'])
        old = next((x for x in corpus.fetch_cache if x['actual_url'] == actual and x.get('raw_path') and (corpus.root / x['raw_path']).is_file()), None)
        if old:
            return entry, old
        record = dict(original_url=entry['url'], actual_url=actual, retrieved_at=datetime.now(timezone.utc).isoformat())
        try:
            if urlparse(actual).netloc in ('youtube.com', 'www.youtube.com', 'youtu.be'):
                return entry, record
            cached = corpus.snapshots.get(actual)
            if cached:
                source, content_type, retrieved_at, source_id = cached
                body = source.read_bytes()
                status, final_url = 200, actual
                record['reused_snapshot'] = dict(source_id=source_id, retrieved_at=retrieved_at)
            else:
                if urlparse(actual).netloc.endswith('arxiv.org'):
                    with paced_host('arxiv.org'):
                        response = requests.get(actual, timeout=(15, 70))
                else:
                    response = requests.get(actual, timeout=(15, 40))
                body, status, final_url = response.content, response.status_code, response.url
                content_type = response.headers.get('Content-Type', '')
            extension = '.pdf' if body.startswith(b'%PDF-') else '.html' if 'html' in content_type or body.lstrip().startswith((b'<!DOCTYPE', b'<!doctype', b'<html')) else Path(urlparse(final_url).path).suffix or '.txt'
            path = corpus.root / 'raw' / 'optional-readings' / (name + extension)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
            record.update(http_status=status, final_url=final_url, content_type=content_type, raw_path=path.relative_to(corpus.root).as_posix(), sha256=hashlib.sha256(body).hexdigest(), bytes=len(body))
        except Exception as error:
            record['error'] = type(error).__name__ + ': ' + str(error)
        return entry, record

    arxiv_pool = ThreadPoolExecutor(max_workers=1)
    other_pool = ThreadPoolExecutor(max_workers=3)
    try:
        futures = [(arxiv_pool if urlparse(optional_target(x['url'])[0]).netloc.endswith('arxiv.org') else other_pool).submit(fetch, x) for x in pending]
        for index, future in enumerate(as_completed(futures), 1):
            entry, record = future.result()
            corpus.fetch_cache.append(record)
            (corpus.root / 'optional-fetches.json').write_text(json.dumps(corpus.fetch_cache, indent=2), encoding='utf-8')
            print('Optional reference', index, '/', len(pending), entry['title'], entry['url'], flush=True)
            if record.get('error'):
                corpus.gap(entry['url'], entry['title'], 'optional-readings', 'Public request failed: ' + record['error'], 'failed')
            else:
                result = material(corpus, entry['url'], entry['title'], 'optional-readings')
                if record.get('reused_snapshot'):
                    result['notes'].append('Reused an existing source snapshot: ' + json.dumps(record['reused_snapshot']))
                if record.get('raw_path'):
                    result['prefetch_retrieved_at'] = record['retrieved_at']
                    result['prefetch_final_url'] = record['final_url']
                corpus.save()
            if index % 20 == 0:
                finish_cmu(corpus)
    finally:
        arxiv_pool.shutdown(wait=True)
        other_pool.shutdown(wait=True)


def finish_cmu(corpus):
    cmu_pages(corpus)
    corpus.finalize()
    discovery = json.loads((corpus.root / 'discovery.json').read_text(encoding='utf-8'))
    schedule = next(x for x in discovery if x['route'] == 'schedule')
    present = {x['url'] for x in corpus.data['materials']}
    present.update(alias for x in corpus.data['materials'] for alias in x.get('aliases', []))
    links = [link for row in schedule['schedule'] for link in row['links']]
    categories = {}
    for category in ('Slides:', 'Recording:', 'Readings:', 'references'):
        chosen = {x['url'] for x in links if x['category'] == category}
        available = {url for record in corpus.data['materials'] if record.get('conversion_status', '').startswith('converted') or record.get('recovered_by') for url in [record['url'], *record.get('aliases', [])]}
        categories[category] = {'unique_links': len(chosen), 'represented': len(chosen & present),
                                'available_as_markdown': len(chosen & available),
                                'with_recorded_gap': sorted((chosen & present) - available),
                                'not_collected': sorted(chosen - present)}
    (corpus.root / 'coverage.json').write_text(json.dumps({'scope': 'Public course pages, teaching repositories, course-assigned readings, and explicitly course-curated optional references, one level only.',
        'schedule_rows': len(schedule['schedule']), 'categories': categories}, indent=2), encoding='utf-8')
    print(json.dumps(corpus.data.get('counts')), flush=True)


def cmu(phase):
    corpus = SnapshotCorpus(ROOT / 'courses/cmu-11768', 'cmu-11768', 'CMU 11-768: AI Agents', 'https://www.cmu-agents.com/')
    data = cmu_pages(corpus)
    shell = corpus.root / 'raw' / 'pages' / 'http-shell.html'
    if not shell.exists():
        response = corpus.request('https://www.cmu-agents.com/')
        shell.write_bytes(response.content)
    add_raw(corpus, 'https://www.cmu-agents.com/', 'Original HTTP application shell', shell,
            notes=['This shell is not course text. The rendered route pages are converted separately.'])
    soup = BeautifulSoup(shell.read_bytes(), 'html.parser')
    for script in soup.select('script[src]'):
        url = urljoin('https://www.cmu-agents.com/', script['src'])
        path = corpus.root / 'raw' / 'pages' / Path(urlparse(url).path).name
        if not path.exists():
            path.write_bytes(corpus.request(url).content)
        add_raw(corpus, url, 'Original course application bundle', path, notes=['Preserved as source evidence. Compiled application code is not a substitute for the rendered course pages.'])
    schedule = next(x for x in data if x['route'] == 'schedule')
    links = [link for row in schedule['schedule'] for link in row['links']]
    if phase == 'core':
        prefetch_slides(corpus, [x for x in links if x['category'] == 'Slides:'])
        seen = set()
        for entry in links:
            if entry['category'] != 'Readings:' or entry['url'] in seen:
                continue
            seen.add(entry['url'])
            print('Assigned reading', entry['title'], entry['url'], flush=True)
            material(corpus, entry['url'], entry['title'])
        for number in range(1, 4):
            corpus.add_repo(f'https://github.com/cmu-agents/assignment-{number}', f'Assignment {number}', f'cmu-assignment-{number}')
        for entry in links:
            if entry['category'] == 'Recording:':
                print('Captions', entry['title'], flush=True)
                captions(corpus, entry['url'], entry['title'])
        corpus.gap('https://canvas.cmu.edu/courses/55126', 'Course Canvas', 'restricted', 'Private CMU course system for enrolled students; public assignment repositories and project guidance are archived.', 'requires_login')
        corpus.gap('https://piazza.com/cmu/fall2026/11768/home', 'Course Piazza', 'restricted', 'Private enrolled-student discussion and project-hours scheduling service.', 'requires_login')
        corpus.data['notes'] = list(dict.fromkeys(corpus.data['notes'] + [
            'Collected while Fall 2026 was in progress. The schedule publishes 18 slide files and 9 recording links; other rows did not have public slide or video links at retrieval.',
            'The course has three public programming assignment repositories, including assignment 3, beyond the two repositories listed in the initial source selection.',
            'Optional references are explicitly listed in References expanders on the course schedule. Coverage distinguishes assigned readings from optional reference snapshots.',
            'External repositories used as readings are archived as the explicitly linked file or README, not mirrored recursively. Teaching assignment repositories are preserved as complete archives.',
        ]))
    elif phase == 'optional':
        collect_optional(corpus, links)
    finish_cmu(corpus)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('course', choices=['cmu', 'colorado'])
    parser.add_argument('--phase', choices=['core', 'optional', 'finalize'], default='core')
    args = parser.parse_args()
    if args.course == 'cmu':
        cmu(args.phase)
    else:
        colorado()


if __name__ == '__main__':
    main()
