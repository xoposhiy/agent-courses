"""Integrate verified public recoveries and finish the CMU and Colorado archives."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys

from collect_cmu_colorado import ROOT, SnapshotCorpus, add_raw, finish_cmu, material
from corpus import Corpus


def integrate_packages(corpus):
    for package_path in sorted((ROOT / 'tmp' / 'recoveries').glob('*/manifest.json')):
        package = json.loads(package_path.read_text(encoding='utf-8'))
        if package.get('source_id') != corpus.data['source_id']:
            continue
        for item in package['materials']:
            if any(x['id'] == item['id'] for x in corpus.data['materials']):
                continue
            paths = [item.get('raw_path'), item.get('markdown_path')]
            paths += [asset['raw_path'] for asset in item.get('assets', [])]
            for relative in paths:
                if not relative:
                    continue
                source = package_path.parent / relative
                destination = corpus.root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
            corpus.data['materials'].append(item)
            for original in corpus.data['materials']:
                if original is not item and original['url'] == item['url'] and original.get('conversion_status') in ('failed', 'not_available'):
                    original['recovered_by'] = item['markdown_path']
                    original['notes'].append('The public source content was recovered after browser rendering. See the recovered copy linked in the gap report.')
            print('Integrated recovery:', item['title'], flush=True)
        corpus.save()


def add_local_pdf(corpus, path, name, title, url, aliases=None, note=None):
    old = next((x for x in corpus.data['materials'] if x['url'] == url and x.get('markdown_path')), None)
    if old:
        return old
    destination = corpus.root / 'raw' / 'optional-readings' / (name + '.pdf')
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, destination)
    result = corpus.add(url, title, 'optional-readings', name, expected='pdf')
    result.setdefault('aliases', []).extend(aliases or [])
    if note:
        result['notes'].append(note)
    for original in corpus.data['materials']:
        if original is not result and original['url'] in (aliases or []) and original.get('conversion_status') in ('failed', 'not_available'):
            original['recovered_by'] = result['markdown_path']
            original['notes'].append('Full text recovered from an official public source; see the recovered copy in the gap report.')
    corpus.save()
    return result


def demote_empty_docent(corpus):
    for item in corpus.data['materials']:
        if 'docent.transluce.org/dashboard/' not in item['url'] or not item.get('markdown_path'):
            continue
        path = corpus.root / item['markdown_path']
        content = path.read_text(encoding='utf-8')
        if '# Unnamed Plan' not in content or len(content) > 3000:
            continue
        saved = corpus.root / 'raw' / 'recoveries' / (item['id'] + '-shell-extraction.md')
        saved.parent.mkdir(parents=True, exist_ok=True)
        if not saved.exists():
            path.rename(saved)
        item['rejected_conversion_path'] = saved.relative_to(corpus.root).as_posix()
        item.pop('markdown_path', None)
        item['conversion_status'] = 'failed'
        item['notes'].append('The HTTP response contains only application navigation, loading text, and an Unnamed Plan heading. It does not contain the referenced analysis; the previous shell extraction is retained as raw evidence, not clean course content.')
        recovered = next((other for other in corpus.data['materials'] if other is not item and other['url'] == item['url'] and other.get('markdown_path') and other.get('conversion_status', '').startswith('converted')), None)
        if recovered:
            item['recovered_by'] = recovered['markdown_path']
    corpus.save()


def preserve_langsmith_evidence(corpus):
    package = ROOT / 'tmp' / 'recoveries' / 'langsmith'
    if not (package / 'outcomes.json').is_file():
        return
    destination = corpus.root / 'raw' / 'recoveries' / 'langsmith'
    destination.mkdir(parents=True, exist_ok=True)
    outcomes = json.loads((package / 'outcomes.json').read_text(encoding='utf-8'))
    shutil.copy2(package / 'outcomes.json', destination / 'outcomes.json')
    for outcome in outcomes:
        item = next((x for x in corpus.data['materials'] if x['url'] == outcome['url']), None)
        if not item:
            continue
        share_id = outcome['url'].split('/public/', 1)[1].split('/', 1)[0]
        for filename, kind, url in [(share_id + '.html', 'rendered-dom', outcome['url']), (share_id + '-response.txt', 'public-query-response', outcome['query_url'])]:
            source = package / filename
            if not source.is_file():
                continue
            target = destination / filename
            shutil.copy2(source, target)
            body = target.read_bytes()
            evidence = dict(kind=kind, url=url, raw_path=target.relative_to(corpus.root).as_posix(), bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
            if kind == 'public-query-response':
                evidence.update(http_status=outcome['http_status'], method='POST', request_body=outcome['query_body'])
            if not any(x.get('raw_path') == evidence['raw_path'] for x in item.setdefault('evidence', [])):
                item['evidence'].append(evidence)
        item['conversion_status'] = 'not_available'
        note = 'The public browser page shows No inputs and No outputs. Its public runs query returns HTTP 200 with an empty items list. No trace content was available to convert. See [browser and response evidence](raw/recoveries/langsmith/outcomes.json).'
        if note not in item['notes']:
            item['notes'].append(note)
    corpus.save()


def mark_retry(corpus, item, name):
    actual = item['url']
    corpus.fetch_cache = [x for x in corpus.fetch_cache if x['actual_url'] != actual]
    result = corpus.add(actual, item['title'] + ' (public retry)', 'optional-readings', name)
    if result.get('markdown_path'):
        item['recovered_by'] = result['markdown_path']
        result.setdefault('aliases', []).append(actual)
    else:
        item['notes'].append('A later bounded public retry was also unsuccessful; the retry response is preserved separately.')
    corpus.save()


def main():
    cmu_root = ROOT / 'courses' / 'cmu-11768'
    corpus = SnapshotCorpus(cmu_root, 'cmu-11768', 'CMU 11-768: AI Agents', 'https://www.cmu-agents.com/')
    integrate_packages(corpus)
    recoveries = cmu_root / 'raw' / 'recoveries'
    add_local_pdf(corpus, recoveries / 'curriculum-learning.pdf', 'curriculum-learning-official',
                  'Curriculum Learning: official ICML 2009 paper', 'https://icml.cc/2009/papers/119.pdf',
                  ['https://doi.org/10.1145/1553374.1553380', 'https://dl.acm.org/doi/10.1145/1553374.1553380'],
                  'The official conference PDF has matching title, authors, and ICML 2009 publication details. It recovers the course DOI target that returned HTTP 403.')
    book_path = recoveries / 'marl-download.html'
    if book_path.exists():
        corrected_path = recoveries / 'marl-book.pdf'
        if not corrected_path.exists():
            book_path.rename(corrected_path)
        book_path = corrected_path
    else:
        book_path = recoveries / 'marl-book.pdf'
    add_local_pdf(corpus, book_path, 'multi-agent-reinforcement-learning-book',
                  'Multi-Agent Reinforcement Learning: Foundations and Modern Approaches (full book)',
                  'https://www.marl-book.com/download/',
                  note='This full public PDF is linked by the explicitly referenced book website. It contains 395 pages. The book bibliography was not collected recursively.')
    for url, title in [
        ('https://github.com/acl-org/acl-style-files', 'Project report: ACL style files'),
        ('https://cmu-l3.github.io/anlp-spring2026/assignments/assignment3&4', 'Project report: referenced Advanced NLP guidance'),
        ('https://www.cmu.edu/hub/calendar/docs/2627-academic-calendar.pdf', 'Official CMU 2026-2027 academic calendar'),
    ]:
        material(corpus, url, title, 'references')
    demote_empty_docent(corpus)
    preserve_langsmith_evidence(corpus)
    for item in list(corpus.data['materials']):
        if item.get('http_status') == 429 and item.get('conversion_status') == 'failed' and not item['title'].endswith('(public retry)'):
            mark_retry(corpus, item, item['id'] + '-retry')
    corpus.data['notes'] = list(dict.fromkeys(corpus.data['notes'] + [
        'All 355 unique optional schedule-reference targets have an explicit outcome. Ten targets overlap assigned readings; the remaining 345 were processed as optional references.',
        'Optional references preserve the exact linked document, source file, model card, public caption track, or website snapshot. External repositories, framework documentation sites, datasets, and bibliography links are not mirrored recursively.',
        'Public source snapshots already collected for another selected course are copied into this course archive with their source collection and original retrieval time recorded.',
        'The supplementary MARL textbook is available in full as a 395-page PDF and page-numbered Markdown; it is an optional reading and is separate from the selected Agentic Large Language Models book.',
        'The optional Fujitsu OpenHands slide folder returned HTTP 404 through the source-file URL and the official GitHub directory API. The course-owned OpenHands lecture slides remain available in this archive.',
    ]))
    finish_cmu(corpus)
    # The Colorado source collection is already complete; refresh indexes after recovery labels.
    colorado_root = ROOT / 'courses' / 'colorado-csci7000'
    data = json.loads((colorado_root / 'manifest.json').read_text(encoding='utf-8'))
    for item in data['materials']:
        for note in item.get('notes', []):
            if 'Full text recovered from [a public alternative](' in note:
                item['recovered_by'] = note.split('](', 1)[1].split(')', 1)[0]
    colorado = Corpus(colorado_root, data['source_id'], data['title'], data['source_url'])
    colorado.data = data
    colorado.write_indexes()
    print(json.dumps({'cmu': corpus.data['counts'], 'colorado': colorado.data['counts']}, indent=2), flush=True)


if __name__ == '__main__':
    main()
