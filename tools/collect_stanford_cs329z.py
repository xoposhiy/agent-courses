"""Collect the public Stanford CS329Z course and assigned readings."""

import json
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
import requests

from corpus import Corpus


def main():
    manifest = Path("courses/stanford-cs329z/manifest.json")
    previous = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else None
    corpus = Corpus("courses/stanford-cs329z", "stanford-cs329z", "Stanford CS329Z: Engineering AI Agents", "https://cs329z.stanford.edu/")
    if previous:
        corpus.data = previous
        corpus.save()
    home = corpus.add("https://cs329z.stanford.edu/", "Course schedule and readings", "pages", "index")
    corpus.add("https://cs329z.stanford.edu/logistics.html", "Course logistics", "pages", "logistics")
    corpus.add("https://cs329z.stanford.edu/project.html", "Course project", "pages", "project")
    soup = BeautifulSoup((corpus.root / home["raw_path"]).read_bytes(), "html.parser")
    links = []
    seen = set()
    for anchor in soup.select("table a[href]"):
        url = urljoin("https://cs329z.stanford.edu/", anchor["href"])
        if url in seen:
            continue
        seen.add(url)
        title = anchor.get_text(" ", strip=True)
        row = anchor.find_parent("tr")
        if title == "Slides":
            number = int(Path(urlparse(url).path).stem.removeprefix("lecture"))
            lecture_title = row.select_one(".lec-title")
            title = f"Lecture {number}: " + lecture_title.get_text(" ", strip=True)
        links.append((url, title))
    (corpus.root / "discovered-links.json").write_text(json.dumps(links, indent=2), encoding="utf-8")
    def prefetch(pair):
        url, title = pair
        if "/slides/" not in url or not url.endswith(".pdf"):
            return
        path = corpus.root / "raw" / "slides" / Path(urlparse(url).path).name
        if path.exists() and path.read_bytes()[:5] == b"%PDF-":
            return
        print("Prefetching", url, flush=True)
        try:
            response = requests.get(url, timeout=(15, 70))
            response.raise_for_status()
            if not response.content.startswith(b"%PDF-"):
                raise ValueError("Expected PDF response")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(response.content)
            print("Prefetched", path.name, len(response.content), flush=True)
        except Exception as error:
            print("Prefetch deferred", url, type(error).__name__, flush=True)
    with ThreadPoolExecutor(max_workers=4) as workers:
        list(workers.map(prefetch, links))
    for url, title in links:
        print("Collecting", url, flush=True)
        host = urlparse(url).netloc
        if "youtu" in host:
            if not any(item["url"] == url for item in corpus.data["materials"]):
                corpus.record_gap(url, title + " " + url.rsplit("/", 1)[-1], "videos", "Video binary excluded. Public caption retrieval is attempted separately.", "video_not_downloaded")
        elif host == "github.com":
            if "/cs329z/" in url:
                corpus.add_repo(url, title + ": " + url.rsplit("/", 1)[-1])
            else:
                item = corpus.add(url.replace("https://github.com/", "https://raw.githubusercontent.com/") + "/HEAD/README.md", title, "readings")
                item["aliases"] = [url]
        elif host.endswith("arxiv.org"):
            paper_id = url.rsplit("/", 1)[-1]
            corpus.add(url, title + " (metadata)", "metadata", "arxiv-" + paper_id)
            corpus.add("https://arxiv.org/pdf/" + paper_id, title, "readings", "arxiv-" + paper_id, expected="pdf")
        elif url.lower().endswith(".pdf"):
            category = "slides" if "/slides/" in url else "assignments"
            corpus.add(url, title, category, Path(urlparse(url).path).stem, expected="pdf")
        elif title in ("Ryan Marten", "Alex Shaw", "Andrew Ng", "Carlos Jimenez", "Alexander Wettig"):
            continue
        else:
            result = corpus.add(url, title, "readings")
            if "aclanthology.org/" in url:
                corpus.add(url.rstrip("/") + ".pdf", title + " (full text)", "readings", "acl-2024-emnlp-main-54", expected="pdf")
            elif host == "openreview.net":
                corpus.add(url.replace("/forum?", "/pdf?"), title + " (full text)", "readings", "autolibra-full-text", expected="pdf")
        corpus.finalize()
    corpus.data["notes"] += [
        "The schedule was collected while the Fall 2026 course was in progress. Future lectures have assigned readings but no published slide links.",
        "No slides or video links were published for the November 9 Andrew Ng fireside chat. November 16 SWE-bench, November 18 Safety, November 30 Coding Agents, December 2 Personal Agents, and December 9 final demos had no published slides at retrieval.",
        "The official homework-2 schedule link names assignment2-harness; the preliminary resource list names assignment2-evals. Both names are checked and the official schedule takes precedence.",
        "External readings are collected one level from the syllabus; linked external sites are not recursively mirrored. For OpenClaw, only the assigned repository README is archived."
    ]
    if not any("assignment2-evals" in x["url"] for x in corpus.data["materials"]):
        corpus.add_repo("https://github.com/cs329z/assignment2-evals", "Homework 2 alternate repository from resource list")
    # Course-owned links from the logistics and project pages may contain further handouts.
    for item in list(corpus.data["materials"]):
        if item["category"] != "pages" or not item.get("raw_path"):
            continue
        page = BeautifulSoup((corpus.root / item["raw_path"]).read_bytes(), "html.parser")
        for anchor in page.select("a[href]"):
            url = urljoin(item["url"], anchor["href"])
            if "cs329z" in url and url.lower().endswith(".pdf") and url not in seen:
                seen.add(url)
                corpus.add(url, anchor.get_text(" ", strip=True) or Path(urlparse(url).path).stem, "assignments", expected="pdf")
    corpus.finalize()
    print(json.dumps(corpus.data["counts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
