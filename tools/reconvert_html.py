"""Rebuild selected Markdown files from their unchanged archived HTML."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from corpus import Corpus


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True)
    parser.add_argument("--material-id", action="append", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    plan = json.loads((root / "collection-plan.json").read_text(encoding="utf-8"))
    source = next(item for item in plan["sources"] if item["id"] == args.source)
    corpus = Corpus(root / source["folder"], source["id"], source["title"], source["url"])
    for material_id in args.material_id:
        item = next(record for record in corpus.data["materials"] if record["id"] == material_id)
        raw = corpus.root / item["raw_path"]
        if raw.suffix.lower() not in (".html", ".htm"):
            raise ValueError("The selected raw file is not HTML")
        binary = raw.read_bytes()
        if hashlib.sha256(binary).hexdigest() != item["sha256"]:
            raise ValueError("The archived HTML checksum does not match its manifest")
        target = item["markdown_path"]
        content = corpus.html_content(item, binary, item.get("final_url", item["url"]))
        item["converted_at"] = datetime.now(timezone.utc).isoformat()
        corpus.write_markdown(item, content, target_path=target)
        corpus.save()
        print(json.dumps({"id": material_id, "markdown_path": target, "content_characters": len(content)}))
    corpus.finalize()


if __name__ == "__main__":
    main()
