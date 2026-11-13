"""Reconvert four archived HTML pages while keeping their source snapshots stable."""

from datetime import datetime, timezone
import hashlib
import json
import mimetypes
from pathlib import Path

import requests

from collect_cmu_colorado import ROOT, SnapshotCorpus, finish_cmu


class ArchivedAssetsCorpus(SnapshotCorpus):
    def __init__(self, *args):
        super().__init__(*args)
        self.archived_assets = {asset['url']: asset for item in self.data['materials'] for asset in item.get('assets', []) if asset.get('url') and asset.get('raw_path')}

    def request(self, url):
        asset = self.archived_assets.get(url)
        if asset and (self.root / asset['raw_path']).is_file():
            path = self.root / asset['raw_path']
            response = requests.Response()
            response.status_code = 200
            response.url = url
            response._content = path.read_bytes()
            response.headers['Content-Type'] = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
            return response
        return super().request(url)


def main():
    report = []
    selections = {
        'cmu-11768': ['ref-68c75debbb7b', 'ref-6fa32b7c7361', 'ref-77bc037fa503'],
        'colorado-csci7000': ['ref-b6a2e9797c3f'],
    }
    for source_id, identifiers in selections.items():
        root = ROOT / 'courses' / source_id
        manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
        corpus = ArchivedAssetsCorpus(root, source_id, manifest['title'], manifest['source_url'])
        for identifier in identifiers:
            item = next(x for x in corpus.data['materials'] if x['id'] == identifier)
            raw_path = root / item['raw_path']
            original = raw_path.read_bytes()
            checksum = hashlib.sha256(original).hexdigest()
            assert checksum == item['sha256']
            retrieved_at = item['retrieved_at']
            markdown_path = item['markdown_path']
            before_chars = len((root / markdown_path).read_text(encoding='utf-8'))
            content = corpus.html_content(item, original, item.get('final_url', item['url']))
            corpus.write_markdown(item, content, target_path=markdown_path)
            unique_assets = {}
            for asset in item.get('assets', []):
                unique_assets.setdefault((asset.get('url'), asset.get('raw_path')), asset)
            item['assets'] = list(unique_assets.values())
            available_images = {asset['url'] for asset in item['assets'] if asset.get('url')}
            item['notes'] = [note for note in item['notes'] if not any(note == 'Image remains remote: ' + url for url in available_images)]
            if any(note.startswith('Image remains remote:') for note in item['notes']):
                item['conversion_status'] = 'converted_with_limitations'
            item['converted_at'] = datetime.now(timezone.utc).isoformat()
            assert item['retrieved_at'] == retrieved_at and item['markdown_path'] == markdown_path
            assert hashlib.sha256(raw_path.read_bytes()).hexdigest() == checksum
            entry = dict(source_id=source_id, id=identifier, title=item['title'], raw_sha256=checksum,
                         retrieved_at=retrieved_at, converted_at=item['converted_at'], markdown_path=markdown_path,
                         before_markdown_chars=before_chars, after_markdown_chars=len((root / markdown_path).read_text(encoding='utf-8')),
                         assets=len(item['assets']))
            report.append(entry)
            corpus.save()
            print(json.dumps(entry), flush=True)
        if source_id == 'cmu-11768':
            finish_cmu(corpus)
        else:
            corpus.finalize()
    (ROOT / 'tmp' / 'cmu-colorado-html-reconversion.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
