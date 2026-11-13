"""Check CS224V source coverage and preserve readable homework data and forms."""

import ast
import base64
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
from urllib.parse import urldefrag
import zlib

from bs4 import BeautifulSoup
from markdownify import markdownify

from corpus import Corpus, code_block, map_prose
from content_checks import access_page_reason
from collect_stanford_cs224v import BASE, finish
from finish_stanford_cs224v import add_snapshot, update_markdown


def embedded_artifacts(corpus):
    source = next(item for item in corpus.data["materials"] if item["url"] == "https://colab.research.google.com/drive/1YwmG0Nn9_XUiMmJltLnC4zjzzvcJHBwz")
    source_url = source["url"] + "#embedded-artifacts"
    if any(item["url"] == source_url for item in corpus.data["materials"]):
        return
    notebook = json.loads((corpus.root / source["raw_path"]).read_text(encoding="utf-8"))
    payload = None
    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue
        try:
            tree = ast.parse("".join(cell.get("source", [])))
        except SyntaxError:
            continue
        for statement in tree.body:
            if isinstance(statement, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "ARTIFACTS" for target in statement.targets):
                payload = ast.literal_eval(statement.value)
    if not isinstance(payload, str):
        raise ValueError("Embedded homework data constant was not found")
    decompressed = zlib.decompressobj().decompress(base64.b64decode(payload), 50_000_000)
    data = json.loads(decompressed)
    binary = (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    item = add_snapshot(corpus, source_url, "Homework 2 SATIR/VERDICT saved evaluation artifacts", "notebooks", "hw2-smt-embedded-artifacts", binary, ".json", "decoded-static-notebook-data", code_block(binary.decode("utf-8"), "json"))
    item["container_url"] = source["url"]
    item["notes"] = ["Decoded a literal base64/zlib data constant with AST literal parsing. No notebook code, model calls, or assignment logic was executed.", "The original compressed constant remains unchanged in the complete notebook and its Markdown conversion."]
    item["source_snapshot_sha256"] = source["sha256"]
    item["data_keys"] = list(data)
    # Keep course notebook links pointed at the notebook, rather than this derived data view.
    corpus.data["materials"].remove(source)
    corpus.data["materials"].append(source)
    corpus.save()


def submission_form(corpus):
    source_url = "https://forms.gle/BD8VXCCkEGKLpMwG8"
    item = next(record for record in corpus.data["materials"] if record["url"] == source_url)
    if item.get("markdown_path"):
        return
    response = corpus.request(source_url)
    raw = corpus.root / "raw" / "projects" / "project-proposal-form.html"
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_bytes(response.content)
    item.update(raw_path=raw.relative_to(corpus.root).as_posix(), http_status=response.status_code, bytes=len(response.content), sha256=hashlib.sha256(response.content).hexdigest(), final_url=response.url)
    page = BeautifulSoup(response.content, "html.parser")
    questions = page.select('[role="listitem"]')
    if response.status_code == 200 and questions and "accounts.google.com" not in response.url:
        for element in page.select("script, style, footer, nav, noscript"):
            element.decompose()
        item.update(category="projects", id="project-proposal-form", title="Project proposal form: questions and instructions", download_status="downloaded", conversion_status="converted", conversion_method="public-form-questions-to-markdown")
        item["notes"] = ["Read-only capture of the public submission form. No form was filled or submitted."]
        text = markdownify(str(page.select_one("form") or page.body or page), heading_style="ATX")
        update_markdown(corpus, item, text)
    else:
        item["download_status"] = "requires_login"
        item["notes"] = ["The public form did not expose questions without sign-in. Its raw response and original URL are retained; no form was submitted."]
    corpus.save()


def disease_sheet(corpus):
    file_id = "1NI2Xk8aolZkuyBXrcy1yKLWc5ADGZvmn-ql8cY4JRyo"
    source = "https://docs.google.com/spreadsheets/d/" + file_id + "/edit?gid=0#gid=0"
    if any(item["url"] == source for item in corpus.data["materials"]):
        return
    url = "https://docs.google.com/spreadsheets/d/" + file_id + "/export?format=csv&gid=0"
    response = corpus.request(url)
    genuine = response.status_code == 200 and "csv" in response.headers.get("Content-Type", "").lower()
    if genuine:
        text = response.content.decode("utf-8-sig")
        rows = list(csv.reader(io.StringIO(text)))
        def escape(cell):
            return cell.replace("|", "\\|").replace("\n", "<br>")
        width = max(map(len, rows), default=0)
        rows = [row + [""] * (width - len(row)) for row in rows]
        markdown = "\n".join("| " + " | ".join(escape(cell) for cell in row) + " |" + ("\n| " + " | ".join("---" for _ in row) + " |" if index == 0 else "") for index, row in enumerate(rows))
        item = add_snapshot(corpus, source, "Homework disease allocation sheet (linked worksheet)", "assignments", "disease-allocation-sheet", response.content, ".csv", "csv-table-to-markdown", markdown)
        item["aliases"] = [source.split("#", 1)[0], url]
    else:
        item = corpus.record_gap(source, "Homework disease allocation spreadsheet", "assignments", "Connected Google Drive metadata returned 404. A public CSV export was also checked and did not return a CSV worksheet; the spreadsheet requires access.", "requires_login")
        raw = corpus.root / "raw" / "assignments" / "disease-allocation-sheet-access-response.html"
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_bytes(response.content)
        item.update(raw_path=raw.relative_to(corpus.root).as_posix(), bytes=len(response.content), sha256=hashlib.sha256(response.content).hexdigest(), http_status=response.status_code, aliases=[source.split("#", 1)[0]])
    corpus.save()


def reading_index(corpus):
    inventory = json.loads((corpus.root / "reading-inventory.json").read_text(encoding="utf-8"))
    original = next(item for item in corpus.data["materials"] if item["url"] == BASE + "CS224V_Readings.pdf")
    identifier = "course-reading-index"
    item = next((record for record in corpus.data["materials"] if record.get("conversion_method") == "generated-reading-navigation"), None)
    if item is None:
        item = {**{key: original[key] for key in ("retrieved_at", "raw_path", "sha256", "bytes")}, "id": identifier, "title": "Course reading index: 13 mandatory and 48 recommended works", "url": original["url"] + "#local-reading-index", "category": "pages", "download_status": "downloaded", "conversion_status": "converted", "conversion_method": "generated-reading-navigation", "notes": ["Generated navigation for the source reading list. The full six-page source conversion remains separately available; this index is not a replacement or summary of the readings."]}
        corpus.data["materials"].append(item)
    output = corpus.root / "markdown" / "pages" / "course-reading-index.md"
    lines = ["This index follows the course's Mandatory labels. Every other curated reading is listed as recommended. The source PDF and full reading-list conversion remain available.", "", "| Reading | Requirement | Local material |", "| --- | --- | --- |"]
    missing = []
    for entry in inventory["readings"]:
        candidates = [record for record in corpus.data["materials"] if entry["url"] in [record["url"], *record.get("aliases", [])]]
        record = next((record for record in candidates if record.get("markdown_path")), None)
        if record is None:
            failed = next(iter(candidates), None)
            if failed and failed.get("recovered_by"):
                target = failed["recovered_by"]
            else:
                target = None
                missing.append(entry["url"])
        else:
            target = record["markdown_path"]
        label = entry["title"].replace("|", "\\|")
        local = f"[Full material]({os.path.relpath(corpus.root / target, output.parent).replace(chr(92), '/')})" if target else "Access gap; see GAPS.md"
        lines.append(f"| {label} | {entry['reading_requirement']} | {local} |")
    update_markdown(corpus, item, "\n".join(lines))
    # The public reading-list URL opens this navigation view; its full source extraction stays linked here.
    source_path = os.path.relpath(corpus.root / original["markdown_path"], output.parent).replace("\\", "/")
    update_markdown(corpus, item, f"[Complete source reading list]({source_path})\n\n" + "\n".join(lines))
    inventory["readings_without_clean_local_content"] = missing
    inventory["captured_scholarly_works"] = len(inventory["readings"]) - len(missing)
    (corpus.root / "reading-inventory.json").write_text(json.dumps(inventory, indent=2, ensure_ascii=False), encoding="utf-8")
    corpus.save()


def reject_access_pages(corpus):
    for item in corpus.data["materials"]:
        if not item.get("markdown_path") or not item.get("raw_path", "").endswith(".html"):
            continue
        page = BeautifulSoup((corpus.root / item["raw_path"]).read_bytes(), "html.parser")
        title = page.title.get_text(" ", strip=True) if page.title else ""
        visible = page.get_text(" ", strip=True)
        reason = access_page_reason(item.get("final_url", item["url"]), title=title, text=visible)
        if "cookies must be enabled" in visible.lower() and len(visible) < 3000:
            reason = "The response is a cookie-access page, not the linked source."
        if reason:
            item["rejected_markdown_path"] = item.pop("markdown_path")
            converted = corpus.root / item["rejected_markdown_path"]
            converted.unlink(missing_ok=True)
            item.update(download_status="response_only", conversion_status="failed")
            item["notes"].append(reason)


def update_core_links(corpus):
    urls = {}
    rejected = {}
    for item in corpus.data["materials"]:
        if item.get("markdown_path"):
            for url in [item["url"], *item.get("aliases", [])]:
                urls[urldefrag(url)[0].rstrip("/")] = item["markdown_path"]
        if item.get("rejected_markdown_path"):
            rejected[str((corpus.root / item["rejected_markdown_path"]).resolve())] = item
    for item in corpus.data["materials"]:
        if not item.get("markdown_path") or item["category"] == "repositories" or item.get("archive_member"):
            continue
        converted = corpus.root / item["markdown_path"]
        before = converted.read_text(encoding="utf-8")
        def rewrite(match):
            label, target = match.groups()
            if label == "Original source":
                return match.group(0)
            base = urldefrag(target)[0]
            local = urls.get(base.rstrip("/"))
            if not local and base and not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", base):
                failed = rejected.get(str((converted.parent / base).resolve()))
                if failed:
                    local = failed.get("recovered_by")
                    if not local:
                        return f"[{label}]({failed['url']})"
            if not local:
                return match.group(0)
            return f"[{label}]({os.path.relpath(corpus.root / local, converted.parent).replace(chr(92), '/')})"
        after = map_prose(before, lambda line: re.sub(r"(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)", rewrite, line))
        if after != before:
            converted.write_text(after, encoding="utf-8")


def main():
    corpus = Corpus("courses/stanford-cs224v", "stanford-cs224v", "Stanford CS224V: Agentic AI", BASE)
    embedded_artifacts(corpus)
    submission_form(corpus)
    disease_sheet(corpus)
    reject_access_pages(corpus)
    reading_index(corpus)
    for item in corpus.data["materials"]:
        item["notes"] = list(dict.fromkeys(item.get("notes", [])))
        if item.get("aliases"):
            item["aliases"] = list(dict.fromkeys(item["aliases"]))
        if item.get("raw_path", "").endswith(".ipynb"):
            notebook = json.loads((corpus.root / item["raw_path"]).read_text(encoding="utf-8"))
            item["cell_count"] = len(notebook.get("cells", []))
    corpus.data["notes"] = list(dict.fromkeys(corpus.data["notes"]))
    seen = set()
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
        if item["id"] in seen:
            raise ValueError("Duplicate material ID: " + item["id"])
        seen.add(item["id"])
    update_core_links(corpus)
    corpus.write_indexes()
    print(json.dumps(corpus.data["counts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
