"""Archive the two course-linked public Docent plans and their saved outputs."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from collect_cmu_colorado import ROOT, SnapshotCorpus, finish_cmu
from corpus import code_block


COLLECTION = '9bafeb94-3f6e-4d03-bd01-1ae8476e3f6e'
SOURCE = ROOT / 'tmp' / 'recoveries' / 'docent'


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2)


def relative(root, path, parent):
    return os.path.relpath(root / path, parent).replace('\\', '/')


def raw_metadata(corpus, path, url, method='GET'):
    body = path.read_bytes()
    return dict(url=url, raw_path=path.relative_to(corpus.root).as_posix(), bytes=len(body),
                sha256=hashlib.sha256(body).hexdigest(), http_method=method)


def register(corpus, identifier, title, url, raw, content, method, notes=None, **extra):
    existing = next((x for x in corpus.data['materials'] if x['id'] == identifier), None)
    item = existing or dict(id=identifier, title=title, url=url, category='optional-readings',
                            retrieved_at=datetime.now(timezone.utc).isoformat(), notes=notes or [])
    item.update(download_status='downloaded', conversion_status='converted', conversion_method=method,
                raw_path=raw.relative_to(corpus.root).as_posix(), bytes=raw.stat().st_size,
                sha256=hashlib.sha256(raw.read_bytes()).hexdigest(), **extra)
    corpus.write_markdown(item, content)
    if not existing:
        corpus.data['materials'].append(item)
    corpus.save()
    return item


def copy_json(name, destination):
    source = SOURCE / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        shutil.copy2(source, destination)
    return json.loads(destination.read_text(encoding='utf-8'))


def render_table(payload):
    def cell(value):
        text = json.dumps(value, ensure_ascii=False) if isinstance(value, (list, dict)) else str(value)
        return text.replace('|', '\\|').replace('\n', '<br>')
    columns = payload['columns']
    lines = ['| ' + ' | '.join(map(cell, columns)) + ' |', '| ' + ' | '.join('---' for _ in columns) + ' |']
    lines += ['| ' + ' | '.join(map(cell, row)) + ' |' for row in payload['rows']]
    metadata = {key: value for key, value in payload.items() if key not in ('columns', 'rows')}
    return '\n'.join(lines) + '\n\n## Response metadata\n\n' + code_block(json_text(metadata), 'json')


def render_readings(items, pages, parent, corpus):
    def readable(value, level=4):
        if isinstance(value, dict) and isinstance(value.get('text'), str):
            return value['text'].replace('<', '&lt;').replace('>', '&gt;').replace('[', '\\[').replace(']', '\\]')
        if isinstance(value, dict):
            return '\n\n'.join('#' * min(level, 6) + ' ' + key.replace('_', ' ').title() + '\n\n' + readable(child, level + 1) for key, child in value.items() if key != 'citations')
        if isinstance(value, list):
            return '\n\n'.join('#' * min(level, 6) + f' Item {index}\n\n' + readable(child, level + 1) for index, child in enumerate(value, 1))
        return str(value).replace('<', '&lt;').replace('>', '&gt;').replace('[', '\\[').replace(']', '\\]')
    parts = [f'Complete saved outputs: {len(items)} result groups. No new model evaluation was run.', '', '## Original response pages', '']
    for page in pages:
        parts.append(f"- [Offset {page['offset']}, {page['items']} groups]({relative(corpus.root, page['raw_path'], parent)})")
    for index, item in enumerate(items, 1):
        rollouts = item.get('rollouts', [])
        parts += ['', f'## Result group {index}', '', '### Inputs', '', code_block(json_text(item.get('arguments_dict')), 'json')]
        for rollout in rollouts:
            parts += ['', '### Saved output: ' + rollout['id'], '', readable(rollout.get('output')), '', '### Output data', '', code_block(json_text(rollout.get('output')), 'json')]
        parts += ['', '### Complete result record', '', code_block(json_text(item), 'json')]
    return '\n'.join(parts)


def collect_readings(corpus, reading_id, response_name, network, target):
    observed = re.search(r'\d+\. \[GET\] (https://api\.docent\.transluce\.org/[^\s]*?/reading/' + re.escape(reading_id) + r'/results-page\?[^\s]+)', network)
    if not observed:
        raise ValueError('No observed public source URL for reading ' + reading_id)
    initial_url = observed.group(1)
    original = target / ('reading-' + reading_id + '-offset-0.json')
    initial = copy_json(response_name, original)
    total = initial['total_group_count']
    pages = []
    items = []
    current = initial
    current_path = original
    current_url = initial_url
    while True:
        count = len(current['items'])
        offset = current['offset']
        meta = raw_metadata(corpus, current_path, current_url)
        meta.update(offset=offset, limit=current['limit'], items=count, reported_total=current['total_group_count'])
        pages.append(meta)
        items.extend(current['items'])
        next_offset = offset + current['limit']
        if next_offset >= total:
            break
        parsed = urlsplit(initial_url)
        query = dict(parse_qsl(parsed.query))
        query.update(offset=str(next_offset), limit=str(current['limit']))
        current_url = urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urlencode(query), ''))
        current_path = target / ('reading-' + reading_id + f'-offset-{next_offset}.json')
        if not current_path.exists():
            if reading_id == 'd3e8d144-e03d-46a0-9f22-744dbf8476c8' and next_offset == 20:
                shutil.copy2(SOURCE / 'test-next-page.json', current_path)
            else:
                response = corpus.request(current_url)
                response.raise_for_status()
                current_path.write_bytes(response.content)
        current = json.loads(current_path.read_text(encoding='utf-8'))
        if current['total_group_count'] != total or current['offset'] != next_offset:
            raise ValueError('Reading pagination changed or returned an unexpected offset')
        if not current['items']:
            raise ValueError('Reading pagination stopped before the reported total')
    hashes = [item['cache_key_hash'] for item in items]
    if len(items) != total or len(set(hashes)) != total:
        raise ValueError('Reading group count or uniqueness does not match the public source')
    return items, pages, initial_url


def main():
    corpus = SnapshotCorpus(ROOT / 'courses' / 'cmu-11768', 'cmu-11768', 'CMU 11-768: AI Agents', 'https://www.cmu-agents.com/')
    destination = corpus.root / 'raw' / 'recoveries' / 'docent'
    destination.mkdir(parents=True, exist_ok=True)
    report = []
    specs = [
        ('response-2177.json', 'first-render.json', 'network.txt', {'1': 'response-2188.json', '3': 'response-2190.json', '5': 'response-2192.json', '7': 'response-2194.json'},
         {'2': 'response-2189.json', '4': 'response-2191.json', '6': 'response-2193.json', '8': 'response-2195.json'}),
        ('response-2284.json', 'second-render.json', 'second-network.txt', {'1': 'response-2295.json', '2': 'response-2296.json'}, {}),
    ]
    for plan_file, rendered_file, network_file, dql_files, reading_files in specs:
        plan = json.loads((SOURCE / plan_file).read_text(encoding='utf-8'))
        plan_id = plan['plan_id']
        plan_url = f'https://docent.transluce.org/dashboard/{COLLECTION}/analysis-plan/{plan_id}'
        api_url = f'https://api.docent.transluce.org/rest/reading/{COLLECTION}/reading-plan/{plan_id}'
        raw = destination / ('plan-' + plan_id + '.json')
        copy_json(plan_file, raw)
        rendered = json.loads((SOURCE / rendered_file).read_text(encoding='utf-8'))
        dom_path = destination / ('plan-' + plan_id + '-rendered.html')
        dom_path.write_text(rendered['html'], encoding='utf-8')
        network_path = destination / (plan_id + '-network.txt')
        shutil.copy2(SOURCE / network_file, network_path)
        network = network_path.read_text(encoding='utf-8')
        identifier = 'docent-plan-' + plan_id
        markdown_parent = corpus.root / 'markdown' / 'optional-readings'
        pieces = [
            'This archive contains the complete public plan definition and its saved outputs. No new model evaluation was run. Underlying agent-run transcripts are referenced by source IDs and were not recursively downloaded.', '',
            '## Plan metadata', '', code_block(json_text({key: value for key, value in plan.items() if key != 'steps'}), 'json'), '',
            f'[Rendered browser DOM]({relative(corpus.root, dom_path.relative_to(corpus.root).as_posix(), markdown_parent)})', '',
        ]
        plan_report = dict(plan_id=plan_id, url=plan_url, steps=len(plan['steps']), dql_outputs=[], reading_outputs=[])
        for index, step in enumerate(plan['steps'], 1):
            label = step.get('title') or step.get('name') or step.get('label') or step.get('type')
            pieces += [f'## Step {index}: {label}', '']
            if step.get('markdown'):
                pieces += [step['markdown'], '']
            if step.get('dql_query'):
                pieces += ['### DQL query', '', code_block(step['dql_query'], 'sql'), '']
            if step.get('prompt_template_segments'):
                prompt = ''.join(segment if isinstance(segment, str) else '{{' + segment['param_name'] + '}}' for segment in step['prompt_template_segments'])
                pieces += ['### Prompt template', '', code_block(prompt), '']
            pieces += ['### Complete step definition', '', code_block(json_text(step), 'json'), '']
            alias = step.get('alias')
            if alias in dql_files:
                response_name = dql_files[alias]
                output_path = destination / (plan_id + '-dql-' + alias + '.json')
                payload = copy_json(response_name, output_path)
                if payload['truncated'] or payload['row_count'] != len(payload['rows']):
                    raise ValueError('DQL output is truncated or its row count is inconsistent')
                output_id = identifier + '-dql-' + alias
                endpoint = f'https://api.docent.transluce.org/rest/dql/{COLLECTION}/execute'
                output = register(corpus, output_id, plan['name'] + ': DQL step ' + alias, endpoint, output_path,
                                  f"Saved response rows: {payload['row_count']}.\n\n" + render_table(payload), 'public-dql-response-to-markdown',
                                  ['This response was captured from the public browser query. The query text is preserved in the linked plan. The original request body was not captured. No query was re-executed during this conversion.'],
                                  http_method='POST', plan_url=plan_url, dql_query=step.get('dql_query'), row_count=payload['row_count'])
                pieces += [f"[Complete saved DQL output: {payload['row_count']} rows]({Path(output['markdown_path']).name})", '']
                plan_report['dql_outputs'].append(dict(alias=alias, rows=payload['row_count'], truncated=False, markdown_path=output['markdown_path']))
            if alias in reading_files:
                items, pages, first_url = collect_readings(corpus, step['reading_id'], reading_files[alias], network, destination)
                output_id = identifier + '-reading-' + alias
                output = register(corpus, output_id, plan['name'] + ': saved reading step ' + alias,
                                  first_url, corpus.root / pages[0]['raw_path'],
                                  render_readings(items, pages, markdown_parent, corpus), 'paginated-public-reading-results-to-markdown',
                                  ['All publicly stored result groups and rollouts were copied without running the evaluator. Original response pages are preserved separately; citation metadata and input source IDs remain in each complete record.'],
                                  source_pages=pages, expected_groups=pages[0]['reported_total'], retrieved_groups=len(items), plan_url=plan_url)
                pieces += [f"[Complete saved reading output: {len(items)} groups]({Path(output['markdown_path']).name})", '']
                plan_report['reading_outputs'].append(dict(alias=alias, reading_id=step['reading_id'], expected_groups=pages[0]['reported_total'], retrieved_groups=len(items), pages=len(pages), markdown_path=output['markdown_path']))
        item = register(corpus, identifier, 'Docent: ' + plan['name'], plan_url, raw, '\n'.join(pieces), 'public-plan-definition-and-saved-results-to-markdown',
                        ['The public plan API and stored result pages were retrieved without authentication. The full plan, DQL source, evaluator prompts, output schemas, query results, and saved evaluator outputs are archived. Underlying agent-run transcripts were not downloaded recursively.'],
                        raw_source_url=api_url, source_evidence=[raw_metadata(corpus, dom_path, plan_url), raw_metadata(corpus, network_path, plan_url)])
        for original in corpus.data['materials']:
            if original is not item and original['url'] == plan_url and original.get('conversion_status') in ('failed', 'not_available'):
                original['recovered_by'] = item['markdown_path']
                original['notes'].append('The complete public plan and all stored result pages were recovered from the public source API after browser inspection. See the recovered copy linked in this report.')
        report.append(plan_report)
        corpus.save()
    expected = sum(x['expected_groups'] for plan in report for x in plan['reading_outputs'])
    retrieved = sum(x['retrieved_groups'] for plan in report for x in plan['reading_outputs'])
    if expected != 115 or retrieved != 115:
        raise ValueError('The four public reading outputs do not reconcile to 115 result groups')
    summary = dict(plans=report, expected_reading_groups=expected, retrieved_reading_groups=retrieved,
                   scope='Two course-linked public analysis plans and all saved outputs; no recursive collection of underlying agent-run transcripts.')
    (corpus.root / 'docent-coverage.json').write_text(json_text(summary) + '\n', encoding='utf-8')
    note = 'Both course-linked Docent plans were recovered in full: 14 plan steps, six complete DQL response tables, and all 115 saved reading-output groups. No new evaluator jobs were run; underlying agent-run transcripts were not collected recursively. See docent-coverage.json for count reconciliation.'
    if note not in corpus.data['notes']:
        corpus.data['notes'].append(note)
    finish_cmu(corpus)
    print(json_text(summary), flush=True)


if __name__ == '__main__':
    main()
