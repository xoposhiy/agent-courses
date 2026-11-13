"""Preserve anonymous access evidence and complete image provenance."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from corpus import Corpus


def main():
    root = Path("courses/dlai-agentic-evals")
    corpus = Corpus(root, "dlai-agentic-evals", "DeepLearning.AI / Arize: Evaluating and Improving Agentic Applications", "https://www.deeplearning.ai/courses/evaluating-and-improving-agentic-applications")
    snapshot = Path(".playwright-cli/page-2026-11-13T17-22-10-299Z.yml")
    if snapshot.exists():
        target = root / "raw/access/anonymous-reading-snapshot.yml"
        target.parent.mkdir(parents=True, exist_ok=True)
        binary = snapshot.read_bytes()
        target.write_bytes(binary)
        corpus.data["materials"].append({"id": "metadata/anonymous-browser-access", "title": "Anonymous browser access evidence", "url": "https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/bvl0k28r/reading-lab-1%3A-how-tracing-works", "category": "metadata", "retrieved_at": datetime.now(timezone.utc).isoformat(), "raw_path": target.relative_to(root).as_posix(), "bytes": len(binary), "sha256": hashlib.sha256(binary).hexdigest(), "download_status": "downloaded", "conversion_status": "not_applicable", "conversion_method": "anonymous-browser-snapshot", "notes": ["A separate anonymous browser displayed 'Log In to Continue' for the reading. No login, enrollment, or account changes were made."]})
        corpus.data["notes"].append("[Anonymous browser access evidence](raw/access/anonymous-reading-snapshot.yml) records the reading viewer's login requirement. The isolated browser session was closed after inspection.")
    item = next(item for item in corpus.data["materials"] if item["url"] == corpus.data["source_url"])
    page = BeautifulSoup((root / item["raw_path"]).read_bytes(), "html.parser")
    main_content = page.select_one("main") or page.body
    assets = {}
    for image in main_content.select("img"):
        source = image.get("src") or image.get("data-src")
        if not source or source.startswith("data:"):
            continue
        url = urljoin(item["url"], source)
        identifier = hashlib.sha256(url.encode()).hexdigest()[:16]
        target = next((path for path in (root / "raw/assets").glob(identifier + ".*") if path.is_file()), None)
        if target:
            assets[url] = {"url": url, "raw_path": target.relative_to(root).as_posix(), "bytes": target.stat().st_size, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}
    item["assets"] = list(assets.values())
    corpus.finalize()
    readme = root / "README.md"
    readme.write_text(readme.read_text(encoding="utf-8").replace("[Manifest](manifest.json)", "[Course contents](CONTENTS.md) · [Manifest](manifest.json)", 1), encoding="utf-8")
    coverage_path = root / "coverage.json"
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    coverage["transcript_words"] = sum(item.get("transcript_words", 0) for item in corpus.data["materials"])
    coverage["caption_text_matches_timed_cues"] = all(item.get("plain_caption_matches_timed_cues", True) for item in corpus.data["materials"] if item["category"] == "lessons")
    coverage["genuine_account_only_items"] = sum(item["category"] == "restricted" for item in corpus.data["materials"])
    coverage_path.write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
