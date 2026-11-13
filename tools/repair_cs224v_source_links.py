"""Repair published route links and label files absent from the source archives."""

import json
import os
from pathlib import Path
import re

from bs4 import BeautifulSoup

from corpus import Corpus, map_prose
from collect_stanford_cs224v import BASE
from qa_stanford_cs224v import update_core_links


def main():
    corpus = Corpus("courses/stanford-cs224v", "stanford-cs224v", "Stanford CS224V: Agentic AI", BASE)
    report = json.loads((corpus.root / "qa-report.json").read_text(encoding="utf-8"))
    broken = report["course"]["broken_local_links"]
    by_markdown = {str((corpus.root / item["markdown_path"]).resolve()): item for item in corpus.data["materials"] if item.get("markdown_path")}
    route = next(item["markdown_path"] for item in corpus.data["materials"] if item.get("raw_path", "").endswith("stanford-oval-genie-worksheets/web/docs/index.html"))
    omissions = []
    grouped = {}
    for link in broken:
        grouped.setdefault(link["file"], set()).add(link["target"])
    for filename, targets in grouped.items():
        converted = Path(filename)
        item = by_markdown[str(converted.resolve())]
        raw = corpus.root / item["raw_path"]
        content = converted.read_text(encoding="utf-8")
        def repair(match):
            image, label, target = match.groups()
            if target not in targets:
                return match.group(0)
            if target == "/docs/" and "genie-worksheets/web/" in item["raw_path"]:
                local = os.path.relpath(corpus.root / route, converted.parent).replace("\\", "/")
                return f"{image}[{label}]({local})"
            expected = (raw.parent / target).resolve()
            if expected.exists():
                return f"{image}[{label}]({os.path.relpath(expected, converted.parent).replace(chr(92), '/')})"
            note = "The published source archive does not contain linked file: " + target
            if note not in item["notes"]:
                item["notes"].append(note)
            item["conversion_status"] = "converted_with_limitations"
            omissions.append({"material_id": item["id"], "markdown_path": item["markdown_path"], "raw_path": item["raw_path"], "missing_target": target})
            prefix = "Image: " if image else ""
            return prefix + label + " (source archive omits `" + target + "`)"
        content = map_prose(content, lambda line: re.sub(r"(?<!\\)(!?)\[([^\]]+)\]\(([^\s)]+)\)", repair, line))
        converted.write_text(content, encoding="utf-8")
    (corpus.root / "source-link-gaps.json").write_text(json.dumps({"scope": "Links in published source files whose targets are absent from the downloaded complete archives.", "omissions": omissions}, indent=2), encoding="utf-8")
    note = "Some vendored AOS/GRILL and Genie Worksheets documents link to files omitted from the published archives. Markdown labels these source omissions. See [source-link-gaps.json](source-link-gaps.json) for the exact documents and missing paths. Original archives and source files preserve the original links."
    if note not in corpus.data["notes"]:
        corpus.data["notes"].append(note)
    for item in corpus.data["materials"]:
        if not item.get("markdown_path") or not item.get("raw_path", "").endswith(".html"):
            continue
        if "ncbi.nlm.nih.gov/geo/" not in item["url"] and "clinicaltrials.gov/about-site/trends-charts" not in item["url"]:
            continue
        page = BeautifulSoup((corpus.root / item["raw_path"]).read_bytes(), "html.parser")
        visible = page.get_text(" ", strip=True)
        if len(visible) < 1000:
            item["rejected_markdown_path"] = item.pop("markdown_path")
            target = corpus.root / item["rejected_markdown_path"]
            if not target.resolve().is_relative_to(corpus.root.resolve()):
                raise ValueError("Generated Markdown path leaves the course folder")
            target.unlink(missing_ok=True)
            item.update(download_status="response_only", conversion_status="failed")
            item["notes"].append("The HTML is a browser-verification page." if "ncbi.nlm.nih.gov/geo/" in item["url"] else "The HTML contains only site glossary controls. The requested trends and charts are loaded by an app and were not present in this response.")
    corpus.save()
    update_core_links(corpus)
    corpus.write_indexes()
    print(json.dumps({"archive_link_omissions": len(omissions), "website_route_repairs": len(broken) - len(omissions)}, indent=2))


if __name__ == "__main__":
    main()
