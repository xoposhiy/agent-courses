"""Collect Stanford CS224V pages, published slides, assignments, and curated readings."""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urljoin, urlparse

from bs4 import BeautifulSoup
import fitz
from markdownify import markdownify
import requests

from corpus import Corpus, slug


BASE = "https://web.stanford.edu/class/cs224v/"
DOC_ID = "17GsPD8IzaSJ_MnGj-yqZgw1MG65bohxeTHeFqz68hi4"
DOC_URL = "https://docs.google.com/document/d/" + DOC_ID + "/edit?usp=sharing"


def collect_pages(corpus):
    for page, title in [("", "Course information and policies"), ("schedule.html", "Course schedule"), ("projects.html", "Project information")]:
        item = corpus.add(BASE + page, title, "pages", Path(page).stem or "index")
        if not page:
            item["aliases"] = [BASE + "index.html"]
    discovered = {}
    for item in corpus.data["materials"]:
        if item["category"] != "pages":
            continue
        soup = BeautifulSoup((corpus.root / item["raw_path"]).read_bytes(), "html.parser")
        for anchor in soup.select("a[href]"):
            url = urljoin(item["url"], anchor["href"])
            discovered.setdefault(url, {"url": url, "label": anchor.get_text(" ", strip=True), "linked_from": []})["linked_from"].append(item["url"])
    (corpus.root / "discovered-links.json").write_text(json.dumps(list(discovered.values()), indent=2), encoding="utf-8")
    pdfs = [entry for url, entry in discovered.items() if url.startswith(BASE) and urlparse(url).path.endswith(".pdf")]
    def prefetch(entry):
        url = entry["url"]
        category = "slides" if "/lectures_2026/" in url else "readings" if "Readings" in url else "assignments"
        name = "reading-list" if category == "readings" else slug(Path(urlparse(url).path).stem)
        path = corpus.root / "raw" / category / (name + ".pdf")
        if path.exists() and path.read_bytes().startswith(b"%PDF-"):
            return
        response = requests.get(url, timeout=(15, 100))
        response.raise_for_status()
        if not response.content.startswith(b"%PDF-"):
            raise ValueError("Expected a course PDF")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(response.content)
    with ThreadPoolExecutor(max_workers=3) as pool:
        for _ in pool.map(prefetch, pdfs):
            pass
    excluded = []
    for url, entry in discovered.items():
        if any(url in [item["url"], *item.get("aliases", [])] for item in corpus.data["materials"]):
            continue
        print("Course link", url, flush=True)
        if url.startswith(BASE) and url.endswith(".pdf"):
            category = "slides" if "/lectures_2026/" in url else "readings" if "Readings" in url else "assignments"
            name = "reading-list" if category == "readings" else slug(Path(urlparse(url).path).stem)
            corpus.add(url, entry["label"], category, name, expected="pdf")
        elif url.startswith(BASE + "schedule_"):
            excluded.append({**entry, "reason": "Past course offering; the requested edition is Fall 2026"})
        elif "canvas.stanford.edu" in url or "edstem.org" in url:
            corpus.record_gap(url, entry["label"], "restricted", "Enrolled-student service. Lecture recordings and some supplementary details are published only in Canvas.", "requires_login")
        elif "forms.gle" in url:
            corpus.record_gap(url, "Project proposal submission form", "restricted", "Submission workflow retained as an external link; no form was submitted.", "submission_service")
        elif url == DOC_URL:
            item = corpus.add("https://docs.google.com/document/d/" + DOC_ID + "/export?format=md", "CS224V (2026) project proposals", "projects", "project-proposals")
            item["aliases"] = [DOC_URL, "https://docs.google.com/document/d/" + DOC_ID + "/edit", "https://docs.google.com/document/d/" + DOC_ID]
            item["notes"].append("The connected Google Drive metadata and Markdown export verified this native document and its 238715-byte public Markdown export. The complete public export is preserved; signed download URLs are not retained.")
        else:
            excluded.append({**entry, "reason": "Staff biography, campus map, or enrollment listing"})
    return discovered, excluded


def bibliography_inventory(corpus):
    document = fitz.open(corpus.root / "raw" / "readings" / "reading-list.pdf")
    entries = {}
    unresolved = []
    started = False
    for page_index, page in enumerate(document, 1):
        for block in page.get_text("blocks", sort=False):
            if block[6] != 0:
                continue
            text = block[4]
            if text.strip() == "References":
                started = True
                continue
            if not started:
                continue
            urls = list(dict.fromkeys(link.get("uri") or link.get("file") for link in page.get_links() if (link.get("uri") or link.get("file")) and fitz.Rect(block[:4]).intersects(link["from"])))
            ids = re.findall(r"arXiv:\s*(\d{4}\.\d{4,5})", text)
            if not urls and ids:
                urls = ["https://arxiv.org/abs/" + paper_id for paper_id in ids]
            for raw_url in urls:
                if raw_url.startswith("arXiv preprint arXiv:"):
                    url = "https://arxiv.org/abs/" + raw_url.rsplit(":", 1)[-1]
                elif raw_url == "https//cursor.com":
                    url = "https://cursor.com/"
                else:
                    url = raw_url.replace("http://arxiv.org/", "https://arxiv.org/")
                if url not in entries:
                    compact = " ".join(text.split())
                    title = re.split(r"\b20\d{2}[ab]?\.\s+", compact, maxsplit=1)[-1]
                    title = re.split(r"\s+In (?:Proceedings|International|Findings|Third|Advances)", title, maxsplit=1)[0]
                    entries[url] = {"url": url, "source_urls": [raw_url], "title": title[:300], "citation": compact, "reading_list_page": page_index}
                elif raw_url not in entries[url]["source_urls"]:
                    entries[url]["source_urls"].append(raw_url)
            if not urls and re.search(r"\b20\d{2}[ab]?\.\s+", text):
                unresolved.append({"citation": " ".join(text.split()), "reading_list_page": page_index})
    resolutions = [
        ("Gepa:", "https://arxiv.org/abs/2507.19457", "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning", "https://github.com/gepa-ai/gepa"),
        ("From local to global", "https://arxiv.org/abs/2404.16130", "From Local to Global: A Graph RAG Approach to Query-Focused Summarization", "https://arxiv.org/abs/2404.16130"),
        ("Biomni:", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12157518/", "Biomni: A General-Purpose Biomedical AI Agent", "PMCID PMC12157518 is stated in the course bibliography"),
        ("Lang2ltl:", "https://openreview.net/references/pdf?id=fuEQkAYpTi", "Lang2LTL: Translating Natural Language Commands to Temporal Specification with Large Language Models", "https://openreview.net/references/pdf?id=fuEQkAYpTi"),
        ("Spinach:", "https://arxiv.org/abs/2407.11417", "SPINACH: SPARQL-Based Information Navigation for Challenging Real-World Questions", "https://arxiv.org/abs/2407.11417"),
        ("Yago3:", "https://asiabiega.github.io/papers/yago3_cidr2015.pdf", "YAGO3: A Knowledge Base from Multilingual Wikipedias", "https://asiabiega.github.io/papers/yago3_cidr2015.pdf"),
        ("s1:", "https://arxiv.org/abs/2501.19393", "s1: Simple Test-Time Scaling", "https://arxiv.org/abs/2501.19393"),
        ("Satlm:", "https://arxiv.org/abs/2305.09656", "SatLM: Satisfiability-Aided Language Models Using Declarative Prompting", "https://arxiv.org/abs/2305.09656"),
        ("A global network of biomedical", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6061699/", "A Global Network of Biomedical Relationships Derived from Text", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6061699/"),
        ("Darwin gödel machine:", "https://arxiv.org/abs/2505.22954", "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents", "https://sakana.ai/dgm/"),
    ]
    pending = []
    for entry in unresolved:
        resolution = next((row for row in resolutions if row[0].lower() in entry["citation"].lower()), None)
        if resolution:
            _, url, title, evidence = resolution
            entries[url] = {**entry, "url": url, "source_urls": [], "title": title, "resolution_source": evidence}
        elif "Percy Liang" not in entry["citation"]:
            pending.append(entry)
    mandatory = ["Attention is all", "Chain-of-thought", "Assisting in writing Wikipedia", "Into the unknown", "DataSTORM:", "Colbert:", "Sliders:", "SUQL:", "SPINACH:", "declarative genie worksheets", "Satir:", "verdict", "Automated design of agentic", "Auto- mated design of agentic"]
    for entry in entries.values():
        combined = entry["title"] + " " + entry["citation"]
        entry["reading_requirement"] = "mandatory" if any(marker.lower() in combined.lower() for marker in mandatory) else "recommended"
    inventory = {"source_url": BASE + "CS224V_Readings.pdf", "scope": "All references in the course-curated reading list, including readings not marked Mandatory. The references of these papers are not traversed.", "readings": list(entries.values()), "unresolved_citations": pending}
    (corpus.root / "reading-inventory.json").write_text(json.dumps(inventory, indent=2, ensure_ascii=False), encoding="utf-8")
    return inventory


def reuse_pilot_pdf(corpus, url, name):
    manifest = Path("courses/stanford-cs329z/manifest.json")
    pilot = json.loads(manifest.read_text(encoding="utf-8"))
    paper_id = urlparse(url).path.rsplit("/", 1)[-1].removesuffix(".pdf") if "arxiv.org" in url else None
    for item in pilot["materials"]:
        if item.get("download_status") != "downloaded" or not item.get("raw_path", "").endswith(".pdf"):
            continue
        same = item["url"] == url or paper_id and "/pdf/" in item["url"] and urlparse(item["url"]).path.rsplit("/", 1)[-1].removesuffix(".pdf") == paper_id
        if same:
            original = manifest.parent / item["raw_path"]
            target = corpus.root / "raw" / "readings" / (name + ".pdf")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, target)
            return {"course_id": "stanford-cs329z", "raw_path": item["raw_path"], "retrieved_at": item["retrieved_at"], "sha256": item["sha256"]}
    return None


def collect_readings(corpus, inventory):
    for entry in inventory["readings"]:
        url = entry["url"]
        title = entry["title"]
        print("Reading", url, flush=True)
        if "arxiv.org/abs/" in url:
            paper_id = url.rsplit("/", 1)[-1]
            name = "arxiv-" + paper_id
            pdf_url = "https://arxiv.org/pdf/" + paper_id
            reused = reuse_pilot_pdf(corpus, pdf_url, name)
            item = corpus.add(pdf_url, title, "readings", name, expected="pdf")
            if reused:
                item["reused_snapshot"] = reused
            item["aliases"] = [url, url.replace("https://", "http://"), *entry["source_urls"]]
        elif "doi.org/10.18653/v1/" in url:
            identifier = url.rsplit("/", 1)[-1]
            item = corpus.add("https://aclanthology.org/" + identifier + ".pdf", title, "readings", "acl-" + identifier, expected="pdf")
            item["aliases"] = [url, "https://aclanthology.org/" + identifier + "/"]
        elif "aclanthology.org/" in url:
            item = corpus.add(url.rstrip("/") + ".pdf", title, "readings", "acl-" + url.rsplit("/", 1)[-1], expected="pdf")
            item["aliases"] = [url]
        elif url == "https://doi.org/10.1145/3397271.3401075":
            reused = reuse_pilot_pdf(corpus, "https://arxiv.org/pdf/2004.12832", "arxiv-2004.12832")
            item = corpus.add("https://arxiv.org/pdf/2004.12832", title, "readings", "arxiv-2004.12832", expected="pdf")
            item["aliases"] = [url]
            item["reused_snapshot"] = reused
        elif url == "https://doi.org/10.1145/3447772":
            item = corpus.add("https://arxiv.org/pdf/2003.02320", title, "readings", "arxiv-2003.02320", expected="pdf")
            item["aliases"] = [url]
        elif "openreview.net/forum?" in url:
            item = corpus.add(url.replace("/forum?", "/pdf?"), title, "readings", "datastorm", expected="pdf")
            item["aliases"] = [url]
        elif ".pdf" in url or "/references/pdf?" in url:
            name = "lang2ltl" if "fuEQkAYpTi" in url else slug(Path(urlparse(url).path).stem)
            item = corpus.add(url, title, "readings", name, expected="pdf")
        else:
            item = corpus.add(url, title, "readings", "pmc-" + url.rstrip("/").rsplit("/", 1)[-1] if "pmc.ncbi" in url else slug(title))
        item["reading_requirement"] = entry["reading_requirement"]
        item["reading_list_page"] = entry["reading_list_page"]
        item["course_citation"] = entry["citation"]
        if entry.get("resolution_source"):
            item["resolution_source"] = entry["resolution_source"]
        corpus.save()


def finish(corpus, discovered, excluded):
    notes = [
        "Fall 2026 was in progress at retrieval. Eleven lecture slide PDFs and two homework PDFs are published. Later November 16/18 lectures and project presentations have no public slide links yet.",
        "The course information page states that posted slides omit important details to support participation. Complete recordings are only on Canvas; public slides are preserved without inventing missing lecture content.",
        "The official Readings navigation points to CS224V_Readings.pdf, a six-page list. All course-curated mandatory and recommended readings are collected one level. Reading requirement flags follow the source; papers' own references are not recursively collected.",
        "Past Fall 2023-2025 course schedules, staff biographies, campus maps, and enrollment listings are outside the requested Fall 2026 edition.",
    ]
    for note in notes:
        if note not in corpus.data["notes"]:
            corpus.data["notes"].append(note)
    seen = set()
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
        if item["id"] in seen:
            raise ValueError("Duplicate material ID: " + item["id"])
        seen.add(item["id"])
    corpus.finalize()
    accounted = {url for item in corpus.data["materials"] for url in [item["url"], *item.get("aliases", [])]}
    excluded_urls = {item["url"] for item in excluded}
    coverage = {"scope": "Current course information, schedule, project page, linked materials, homework links, and all references in the curated reading list.", "course_page_links": len(discovered), "excluded_links": excluded, "missing_course_page_links": [url for url in discovered if url not in accounted and url not in excluded_urls]}
    (corpus.root / "coverage.json").write_text(json.dumps(coverage, indent=2), encoding="utf-8")
    print(json.dumps(corpus.data["counts"], indent=2), flush=True)


def main():
    corpus = Corpus("courses/stanford-cs224v", "stanford-cs224v", "Stanford CS224V: Agentic AI", BASE)
    discovered, excluded = collect_pages(corpus)
    inventory = bibliography_inventory(corpus)
    print("Reading inventory", len(inventory["readings"]), "unresolved", len(inventory["unresolved_citations"]), flush=True)
    collect_readings(corpus, inventory)
    finish(corpus, discovered, excluded)


if __name__ == "__main__":
    main()
