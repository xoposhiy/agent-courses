"""Check the downloaded course corpus without making network requests."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit
from content_checks import access_page_reason


INLINE_LINK = re.compile(r"(?<!\\)!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")
INLINE_CODE = re.compile(r"(?<![\\`])(`+)(?!`)(.*?)(?<!`)\1(?!`)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def local_links(text: str):
    """Ignore code because downloaded examples can contain sample links."""
    fence = None
    for line_number, line in enumerate(text.splitlines(), 1):
        marker = FENCE.match(line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        if "](" not in line:
            continue
        line = INLINE_CODE.sub("", line)
        for match in INLINE_LINK.finditer(line):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            yield line_number, unquote(parsed.path)


def audit(root: Path, source_ids=None, pending_output=None) -> dict:
    plan = json.loads((root / "collection-plan.json").read_text(encoding="utf-8-sig"))
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "courses": [], "errors": [], "warnings": []}
    selected = set(source_ids) if source_ids else None
    unknown = selected - {source["id"] for source in plan["sources"]} if selected else set()
    if unknown:
        report["errors"].append("Unknown source IDs: " + ", ".join(sorted(unknown)))
    checksums = {}
    pdf_counts = {}
    html_titles = {}
    for source in plan["sources"]:
        if selected and source["id"] not in selected:
            continue
        folder = root / source["folder"]
        entry = {"id": source["id"], "folder": source["folder"]}
        for name in ("README.md", "manifest.json", "GAPS.md"):
            if not (folder / name).is_file():
                report["errors"].append(f"{source['folder']}: missing {name}")
        for name in ("raw", "markdown"):
            if not (folder / name).is_dir():
                report["errors"].append(f"{source['folder']}: missing {name}/")
        raw_files = list((folder / "raw").rglob("*")) if (folder / "raw").is_dir() else []
        entry["raw_files"] = sum(p.is_file() for p in raw_files)
        markdown_files = list((folder / "markdown").rglob("*.md"))
        entry["markdown_files"] = len(markdown_files)
        entry["bytes"] = sum(p.stat().st_size for p in folder.rglob("*") if p.is_file()) if folder.exists() else 0
        broken = []
        checked = 0
        files_to_check = markdown_files + list(folder.glob("*.md"))
        markdown_text = {}
        for path in files_to_check:
            if not path.exists():
                continue
            content = path.read_text(encoding="utf-8-sig")
            markdown_text[path] = content
            if not content.strip():
                report["errors"].append(f"{path.relative_to(root).as_posix()}: empty Markdown")
            for line_number, target in local_links(content):
                checked += 1
                resolved = path.parent / target
                if not resolved.exists():
                    broken.append({"file": path.relative_to(root).as_posix(), "line": line_number, "target": target})
        entry["local_links_checked"] = checked
        entry["broken_local_links"] = broken
        if broken:
            report["errors"].append(f"{source['folder']}: {len(broken)} broken local links")
        manifest_path = folder / "manifest.json"
        if manifest_path.exists():
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
                entry["manifest_type"] = type(manifest).__name__
                records = manifest if isinstance(manifest, list) else manifest.get("materials", manifest.get("resources", manifest.get("items", [])))
                entry["manifest_records"] = len(records)
                if isinstance(manifest, dict) and manifest.get("source_id") != source["id"]:
                    report["errors"].append(f"{source['folder']}: manifest source_id does not match collection plan")
                duplicates = [key for key, count in Counter(record.get("id") for record in records).items() if count > 1]
                if duplicates:
                    report["errors"].append(f"{source['folder']}: duplicate material IDs: {duplicates}")
                statuses = {}
                conversion_statuses = Counter()
                for record in records:
                    required = ("id", "title", "url", "category", "retrieved_at", "download_status", "conversion_status")
                    missing = [key for key in required if not record.get(key)]
                    if missing:
                        report["errors"].append(f"{source['folder']}: {record.get('id')}: missing fields {missing}")
                    status = str(record.get("status", record.get("download_status", "unspecified")))
                    statuses[status] = statuses.get(status, 0) + 1
                    conversion_statuses[record.get("conversion_status", "unspecified")] += 1
                    if record.get("download_status") == "downloaded" and not record.get("raw_path"):
                        report["errors"].append(f"{source['folder']}: {record.get('id')}: downloaded material has no raw path")
                    if record.get("download_status") == "downloaded" and record.get("raw_path"):
                        if not re.fullmatch(r"[a-fA-F0-9]{64}", record.get("sha256", "")) or not isinstance(record.get("bytes"), int):
                            report["errors"].append(f"{source['folder']}: {record.get('id')}: missing raw hash or byte count")
                    for key in ("raw_path", "markdown_path"):
                        relative = record.get(key)
                        if not relative:
                            continue
                        actual = folder / relative
                        relative_path = Path(relative)
                        if relative_path.is_absolute() or ".." in relative_path.parts:
                            report["errors"].append(f"{source['folder']}: {record.get('id')}: {key} is outside its source folder")
                            continue
                        if not actual.is_file():
                            report["errors"].append(f"{source['folder']}: {record.get('id')}: missing {key} {relative}")
                        elif key == "raw_path" and record.get("sha256"):
                            if actual not in checksums:
                                binary = actual.read_bytes()
                                checksums[actual] = (hashlib.sha256(binary).hexdigest(), len(binary))
                            digest, byte_count = checksums[actual]
                            if digest != record["sha256"]:
                                report["errors"].append(f"{source['folder']}: checksum mismatch {relative}")
                            if byte_count != record.get("bytes"):
                                report["errors"].append(f"{source['folder']}: byte count mismatch {relative}")
                    for asset in record.get("assets", []):
                        if not isinstance(asset, dict) or not asset.get("raw_path"):
                            continue
                        relative = Path(asset["raw_path"])
                        if relative.is_absolute() or ".." in relative.parts:
                            report["errors"].append(f"{source['folder']}: asset path is outside its source folder: {relative}")
                            continue
                        actual = folder / relative
                        if not actual.is_file():
                            report["errors"].append(f"{source['folder']}: missing asset {relative}")
                            continue
                        if asset.get("sha256"):
                            if actual not in checksums:
                                binary = actual.read_bytes()
                                checksums[actual] = (hashlib.sha256(binary).hexdigest(), len(binary))
                            digest, byte_count = checksums[actual]
                            if digest != asset["sha256"] or (asset.get("bytes") is not None and byte_count != asset["bytes"]):
                                report["errors"].append(f"{source['folder']}: asset checksum or size mismatch {relative}")
                    if record.get("conversion_status", "").startswith("converted") and not record.get("markdown_path"):
                        report["errors"].append(f"{source['folder']}: {record.get('id')}: converted material has no Markdown path")
                    if record.get("conversion_status", "").startswith("converted") and record.get("markdown_path"):
                        converted_path = folder / record["markdown_path"]
                        if converted_path.is_file() and record.get("raw_path", "").lower().endswith((".html", ".htm")):
                            raw_html = folder / record["raw_path"]
                            if raw_html not in html_titles and raw_html.is_file():
                                with raw_html.open(encoding="utf-8", errors="replace") as stream:
                                    head = stream.read(65536)
                                title_match = re.search(r"<title\b[^>]*>(.*?)</title>", head, re.IGNORECASE | re.DOTALL)
                                html_titles[raw_html] = html.unescape(re.sub(r"<[^>]+>", "", title_match.group(1))) if title_match else ""
                            access_reason = access_page_reason(record.get("final_url", record["url"]), title=html_titles.get(raw_html, ""), text=markdown_text.get(converted_path, ""))
                            if access_reason:
                                report["errors"].append(f"{source['folder']}: {record.get('id')}: access page marked converted: {access_reason}")
                    if record.get("page_count") and record.get("markdown_path"):
                        converted = folder / record["markdown_path"]
                        if converted.is_file() and record.get("conversion_method") == "pymupdf-text-by-page":
                            page_numbers = re.findall(r"^## Page (\d+)\s*$", markdown_text.get(converted, ""), flags=re.MULTILINE)
                            expected_pages = list(range(1, record["page_count"] + 1))
                            if list(map(int, page_numbers)) != expected_pages:
                                report["errors"].append(f"{source['folder']}: page coverage mismatch {record['markdown_path']}")
                            raw_pdf = folder / record.get("raw_path", "")
                            if raw_pdf.is_file():
                                import fitz
                                try:
                                    if raw_pdf not in pdf_counts:
                                        with fitz.open(raw_pdf) as document:
                                            pdf_counts[raw_pdf] = len(document)
                                    if pdf_counts[raw_pdf] != record["page_count"]:
                                        report["errors"].append(f"{source['folder']}: raw PDF page count mismatch {record['raw_path']}")
                                except Exception as error:
                                    report["errors"].append(f"{source['folder']}: invalid raw PDF {record['raw_path']}: {error}")
                entry["statuses"] = statuses
                entry["conversion_statuses"] = dict(conversion_statuses)
                entry["pdf_pages"] = sum(record.get("page_count", 0) for record in records)
            except (ValueError, TypeError, AttributeError) as error:
                report["errors"].append(f"{source['folder']}: invalid manifest: {error}")
        report["courses"].append(entry)
    root_links_checked = 0
    root_broken_links = []
    for name in ("README.md", "COLLECTION.md", "SHARED-READINGS.md"):
        path = root / name
        if not path.is_file():
            continue
        for line_number, target in local_links(path.read_text(encoding="utf-8-sig")):
            root_links_checked += 1
            if not (path.parent / target).exists() and not (pending_output and (path.parent / target).resolve() == Path(pending_output).resolve()):
                root_broken_links.append({"file": name, "line": line_number, "target": target})
    if root_broken_links:
        report["errors"].append(f"Corpus navigation: {len(root_broken_links)} broken local links")
    report["root_navigation"] = {"local_links_checked": root_links_checked, "broken_local_links": root_broken_links}
    report["totals"] = {
        "courses": len(report["courses"]),
        "raw_files": sum(item["raw_files"] for item in report["courses"]),
        "markdown_files": sum(item["markdown_files"] for item in report["courses"]),
        "bytes": sum(item["bytes"] for item in report["courses"]),
        "local_links_checked": root_links_checked + sum(item["local_links_checked"] for item in report["courses"]),
        "broken_local_links": len(root_broken_links) + sum(len(item["broken_local_links"]) for item in report["courses"]),
    }
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--source", action="append", dest="source_ids", help="Validate only this source ID; repeat for several sources.")
    args = parser.parse_args()
    report = audit(args.root.resolve(), source_ids=args.source_ids, pending_output=args.output)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"totals": report["totals"], "errors": report["errors"]}, indent=2))
    raise SystemExit(bool(report["errors"]))


if __name__ == "__main__":
    main()
