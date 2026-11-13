"""Validate one collected source without scanning other workers' folders."""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from bs4 import BeautifulSoup

from content_checks import access_page_reason
from validate_corpus import local_links, FENCE


def without_inline_code(line):
    if FENCE.match(line):
        return line
    position = 0
    while position < len(line):
        opening = re.search(r"(?<!\\)(`+)", line[position:])
        if not opening:
            break
        start = position + opening.start()
        end = position + opening.end()
        ticks = opening.group(1)
        closing = re.search(r"(?<!`)" + re.escape(ticks) + r"(?!`)", line[end:])
        if not closing:
            position = end
            continue
        stop = end + closing.end()
        line = line[:start] + " " * (stop - start) + line[stop:]
        position = stop
    return line


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_id")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    plan = json.loads((root / "collection-plan.json").read_text(encoding="utf-8"))
    source = next(item for item in plan["sources"] if item["id"] == args.source_id)
    folder = root / source["folder"]
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    errors = []
    broken = []
    links = 0
    docs = list((folder / "markdown").rglob("*.md")) + [folder / "README.md", folder / "GAPS.md"]
    if (folder / "CONTENTS.md").exists():
        docs.append(folder / "CONTENTS.md")
    for index, path in enumerate(docs, 1):
        text = path.read_text(encoding="utf-8")
        # Reject impossible matches before running the Markdown link expression.
        link_text = "\n".join(without_inline_code(line) if "](" in line or FENCE.match(line) else "" for line in text.splitlines())
        for number, target in local_links(link_text):
            links += 1
            if not (path.parent / target).exists():
                broken.append({"file": path.relative_to(folder).as_posix(), "line": number, "target": target})
        if index % 100 == 0:
            print(f"Checked document paths: {index}/{len(docs)}", flush=True)
    duplicates = [identifier for identifier, count in Counter(item["id"] for item in manifest["materials"]).items() if count > 1]
    if duplicates:
        errors.append("Duplicate IDs: " + str(duplicates))
    hashes = {}
    checked_html = set()
    for item in manifest["materials"]:
        for key in ("raw_path", "markdown_path"):
            if item.get(key) and not (folder / item[key]).is_file():
                errors.append("Missing " + key + ": " + item[key])
        raw = folder / item["raw_path"] if item.get("raw_path") else None
        if raw and raw.is_file() and item.get("sha256"):
            if raw not in hashes:
                hashes[raw] = hashlib.sha256(raw.read_bytes()).hexdigest()
            if hashes[raw] != item["sha256"]:
                errors.append("Checksum mismatch: " + item["raw_path"])
        if raw and raw.suffix == ".html" and item.get("conversion_status", "").startswith("converted") and raw not in checked_html:
            checked_html.add(raw)
            page = BeautifulSoup(raw.read_bytes(), "html.parser")
            reason = access_page_reason(item.get("final_url", item["url"]), page.title.get_text(" ", strip=True) if page.title else "", page.get_text(" ", strip=True))
            if reason:
                errors.append("Access shell marked converted: " + item["url"] + " — " + str(reason))
        if item.get("conversion_method") == "pymupdf-text-by-page" and item.get("markdown_path"):
            numbers = list(map(int, re.findall(r"^## Page (\d+)\s*$", (folder / item["markdown_path"]).read_text(encoding="utf-8"), flags=re.MULTILINE)))
            if numbers != list(range(1, item["page_count"] + 1)):
                errors.append("PDF page coverage mismatch: " + item["markdown_path"])
    if broken:
        errors.append(f"Broken local links: {len(broken)}")
    result = {"source_id": args.source_id, "materials": len(manifest["materials"]), "markdown_files": len(list((folder / "markdown").rglob("*.md"))), "raw_files": sum(path.is_file() for path in (folder / "raw").rglob("*")), "local_links_checked": links, "raw_checksums_checked": len(hashes), "converted_html_checked": len(checked_html), "broken_local_links": broken, "errors": errors}
    (folder / "validation.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
