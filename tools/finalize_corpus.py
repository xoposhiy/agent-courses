"""Build common indexes and validate all sources after collection finishes."""

from datetime import datetime, timezone
import json
from pathlib import Path

from build_catalog import main as build_catalog
from corpus import Corpus
from validate_corpus import audit


ROOT = Path(__file__).resolve().parents[1]


def main():
    plan = json.loads((ROOT / "collection-plan.json").read_text(encoding="utf-8-sig"))
    for source in plan["sources"]:
        corpus = Corpus(ROOT / source["folder"], source["id"], source["title"], source["url"])
        alternatives = {}
        for item in corpus.data["materials"]:
            if item.get("markdown_path") and item.get("conversion_status", "").startswith("converted") and item["category"] != "metadata":
                for url in [item["url"], *item.get("aliases", [])]:
                    alternatives[url] = item["markdown_path"]
        for item in corpus.data["materials"]:
            if item.get("conversion_status") in ("failed", "not_available") and item["url"] in alternatives:
                item["recovered_by"] = alternatives[item["url"]]
        if source.get("kind") != "book":
            corpus.write_indexes()
        else:
            corpus.save()
    build_catalog()
    output = ROOT / "validation-report.json"
    report = audit(ROOT, pending_output=output)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for entry in report["courses"]:
        path = ROOT / entry["folder"] / "validation.json"
        if path.is_file():
            evidence = json.loads(path.read_text(encoding="utf-8-sig"))
            evidence["course"] = entry
            evidence["structural_checked_at"] = report["checked_at"]
            evidence["errors"] = [error for error in report["errors"] if entry["folder"] in error]
            path.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"finished_at": datetime.now(timezone.utc).isoformat(), "totals": report["totals"], "errors": report["errors"]}, indent=2))
    raise SystemExit(bool(report["errors"]))


if __name__ == "__main__":
    main()
