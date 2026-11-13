"""Collect the public Columbia Designing LLM Agents course materials."""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, urldefrag, urljoin, urlparse
import zipfile

from bs4 import BeautifulSoup
from markdownify import markdownify
import requests

from corpus import Corpus, code_block, map_prose, slug


BASE = "https://designing-agents.github.io/"


def convert_archives(corpus):
    archives = [item for item in corpus.data["materials"] if item.get("raw_path", "").endswith(".zip")]
    for item in archives:
        if item.get("conversion_method") == "course-archive-with-text-files":
            archive_name = Path(item["raw_path"]).stem
            item["id"] = "archive-" + archive_name
            old = corpus.root / item["markdown_path"]
            children = [child for child in corpus.data["materials"] if child.get("container_url") == item["url"]]
            corpus.write_markdown(item, "## Archive contents\n\n" + "\n".join(f"- [{child['archive_member']}]({os.path.relpath(corpus.root / child['markdown_path'], corpus.root / 'markdown' / 'assignments').replace(chr(92), '/')})" for child in children))
            if old != corpus.root / item["markdown_path"]:
                old.unlink(missing_ok=True)
            continue
        archive = corpus.root / item["raw_path"]
        archive_name = archive.stem
        old_markdown = corpus.root / item["markdown_path"] if item.get("markdown_path") else None
        item.update(category="assignments", id="archive-" + archive_name)
        extracted = corpus.root / "raw" / "assignments" / archive_name
        children = []
        skipped = []
        with zipfile.ZipFile(archive) as bundle:
            for member in bundle.infolist():
                if member.is_dir():
                    continue
                rel = Path(member.filename)
                if "__MACOSX" in rel.parts or rel.name == ".DS_Store":
                    skipped.append(member.filename)
                    continue
                target = extracted / rel
                if not target.resolve().is_relative_to(extracted.resolve()):
                    raise ValueError("Archive member leaves the course folder")
                binary = bundle.read(member)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(binary)
                child = {"id": archive_name + "/" + rel.as_posix().replace(".", "-"), "title": archive_name + ": " + rel.as_posix(),
                         "url": item["url"] + "#archive-member=" + quote(rel.as_posix()), "container_url": item["url"], "archive_member": rel.as_posix(),
                         "category": "assignments", "retrieved_at": item["retrieved_at"], "raw_path": target.relative_to(corpus.root).as_posix(),
                         "sha256": hashlib.sha256(binary).hexdigest(), "bytes": len(binary), "download_status": "downloaded", "conversion_status": "converted",
                         "notes": ["Extracted from the linked course archive; no code was executed."]}
                text = binary.decode("utf-8")
                if rel.suffix == ".ipynb":
                    text = corpus.notebook_content(child, json.loads(text))
                    child["conversion_method"] = "notebook-cells-and-text-outputs"
                elif rel.suffix == ".md":
                    child["conversion_method"] = "source-markdown"
                else:
                    text = code_block(text, "python" if rel.suffix == ".py" else rel.suffix.lstrip("."))
                    child["conversion_method"] = "source-code-fence"
                corpus.write_markdown(child, text)
                children.append(child)
        by_raw = {str((corpus.root / child["raw_path"]).resolve()): corpus.root / child["markdown_path"] for child in children}
        for child in children:
            converted = corpus.root / child["markdown_path"]
            raw = corpus.root / child["raw_path"]
            header, body = converted.read_text(encoding="utf-8").split("\n\nRetrieved:", 1)
            def repair(match):
                label, link = match.groups()
                if urlparse(link).scheme or link.startswith("#"):
                    return match.group(0)
                target = (raw.parent / urldefrag(link)[0]).resolve()
                if not target.exists():
                    return match.group(0)
                destination = by_raw.get(str(target), target)
                return f"[{label}]({os.path.relpath(destination, converted.parent).replace(chr(92), '/')})"
            body = map_prose(body, lambda line: re.sub(r"(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)", repair, line))
            converted.write_text(header + "\n\nRetrieved:" + body, encoding="utf-8")
        item.update(conversion_status="converted", conversion_method="course-archive-with-text-files", file_count=len(children), skipped_archive_metadata=skipped)
        item["notes"] = ["Full archive preserved. macOS resource forks and .DS_Store metadata remain only in the original ZIP."]
        corpus.write_markdown(item, "## Archive contents\n\n" + "\n".join(f"- [{child['archive_member']}]({os.path.relpath(corpus.root / child['markdown_path'], corpus.root / 'markdown' / 'assignments').replace(chr(92), '/')})" for child in children))
        if old_markdown and old_markdown != corpus.root / item["markdown_path"]:
            old_markdown.unlink(missing_ok=True)
        corpus.data["materials"].remove(item)
        corpus.data["materials"].extend(children + [item])
        corpus.save()


def main():
    corpus = Corpus("courses/columbia-coms4995", "columbia-coms4995", "Columbia COMS 4995-15: Designing LLM Agents", BASE)
    home = next((item for item in corpus.data["materials"] if item["url"] == BASE), None)
    if home:
        home["aliases"] = [BASE + "index.html"]
        corpus.data["materials"] = [item for item in corpus.data["materials"] if item["url"] != BASE + "index.html"]
    owned_pages = ["", "syllabus.html", "HW1.html", "HW2.html", "HW3.html", "project.html"]
    for page in owned_pages:
        name = Path(page).stem.lower() if page else "index"
        category = "assignments" if page.startswith("HW") or page == "project.html" else "pages"
        corpus.add(urljoin(BASE, page), {"index": "Course schedule", "syllabus": "Syllabus", "project": "Final project"}.get(name, name.upper()), category, name)
    links = {}
    for item in corpus.data["materials"]:
        if not item.get("raw_path", "").endswith(".html") or not item["url"].startswith(BASE):
            continue
        soup = BeautifulSoup((corpus.root / item["raw_path"]).read_bytes(), "html.parser")
        for anchor in soup.select("a[href]"):
            url = urljoin(item["url"], anchor["href"]).split("#", 1)[0]
            links.setdefault(url, {"url": url, "label": anchor.get_text(" ", strip=True), "linked_from": []})["linked_from"].append(item["url"])
    (corpus.root / "discovered-links.json").write_text(json.dumps(list(links.values()), indent=2), encoding="utf-8")
    pdfs = [entry for url, entry in links.items() if url.startswith(BASE) and urlparse(url).path.endswith(".pdf")]
    def prefetch(entry):
        name = Path(urlparse(entry["url"]).path).stem
        path = corpus.root / "raw" / "slides" / (name + ".pdf")
        if path.exists() and path.read_bytes().startswith(b"%PDF-"):
            return
        response = requests.get(entry["url"], timeout=(15, 90))
        response.raise_for_status()
        if not response.content.startswith(b"%PDF-"):
            raise ValueError("Expected a slide PDF")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(response.content)
    with ThreadPoolExecutor(max_workers=3) as pool:
        for _ in pool.map(prefetch, pdfs):
            pass
    excluded = []
    for url, entry in links.items():
        if url == BASE + "index.html":
            continue
        if any(item["url"] == url for item in corpus.data["materials"]):
            continue
        print("Collecting", url, flush=True)
        host = urlparse(url).netloc
        if url.startswith(BASE):
            path = urlparse(url).path
            name = Path(path).stem
            if path.endswith(".pdf"):
                corpus.add(url, "Lecture slides: " + name, "slides", name, expected="pdf")
            elif path.endswith((".py", ".ipynb", ".zip", ".csv", ".json", ".txt")):
                corpus.add(url, "Course code: " + Path(path).name, "activities", name)
            else:
                corpus.add(url, entry["label"] or Path(path).name, "pages", name)
        elif host == "github.com":
            corpus.add_repo(url, entry["label"] or url.rsplit("/", 1)[-1])
        elif "arxiv.org" in host:
            paper_id = urlparse(url).path.rsplit("/", 1)[-1].removesuffix(".pdf")
            corpus.add(url, entry["label"] + " (metadata)", "metadata", "arxiv-" + paper_id)
            corpus.add("https://arxiv.org/pdf/" + paper_id, entry["label"], "readings", "arxiv-" + paper_id, expected="pdf")
        elif host in ("courseworks2.columbia.edu", "forms.gle", "docs.google.com", "colab.research.google.com"):
            corpus.record_gap(url, entry["label"] or url, "restricted", "Course platform or submission service; availability checked separately where a public notebook export is provided.", "requires_login")
        elif host in ("shreyahavaldar.com", "www.linkedin.com") or url.startswith("mailto:"):
            excluded.append({**entry, "reason": "Staff biography or contact link"})
        else:
            corpus.add(url, entry["label"] or url, "references", slug(entry["label"] or url))
    notes = [
        "The Fall 2026 course was collected while in progress. The schedule publishes eight lecture slide PDFs (weeks 1-7 and week 9), thirteen Python exercise/support/solution files, three homework pages, and final-project instructions.",
        "The schedule has no public recording links or transcripts. Later lecture entries and project presentations have no published material links at retrieval.",
        "External links from assignment and syllabus pages are included one level; websites and paper bibliographies are not recursively mirrored. Courseworks remains an enrolled-student service.",
    ]
    for note in notes:
        if note not in corpus.data["notes"]:
            corpus.data["notes"].append(note)
    convert_archives(corpus)
    for item in corpus.data["materials"]:
        if item["url"] not in (BASE + "HW1.html", BASE + "HW2.html"):
            continue
        soup = BeautifulSoup((corpus.root / item["raw_path"]).read_bytes(), "html.parser")
        for element in soup.select("script, style, nav, footer"):
            element.decompose()
        for anchor in soup.select("a[href]"):
            anchor["href"] = urljoin(item["url"], anchor["href"])
        corpus.write_markdown(item, markdownify(str(soup.select_one("main") or soup.body or soup), heading_style="ATX"))
    ids = set()
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
        if item["id"] in ids:
            raise ValueError("Duplicate material ID: " + item["id"])
        ids.add(item["id"])
    corpus.finalize()
    recorded = {url for item in corpus.data["materials"] for url in [item["url"], *item.get("aliases", [])]}
    coverage = {"scope": "All links on the current course home, syllabus, three homework pages, and final-project page. Staff personal/contact links excluded.", "discovered_links": len(links), "excluded_links": excluded, "missing_links": [url for url in links if url not in recorded and url not in {item["url"] for item in excluded}]}
    (corpus.root / "coverage.json").write_text(json.dumps(coverage, indent=2), encoding="utf-8")
    print(json.dumps(corpus.data["counts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
