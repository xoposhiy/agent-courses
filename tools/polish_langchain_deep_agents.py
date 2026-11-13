"""Normalize duplicate lesson conversions and complete linked public media."""

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

from corpus import Corpus
from finish_langchain_deep_agents import LessonMarkdown, make_readable, REPO, ROOT


def write_existing(corpus, item, content):
    identifier = item["id"]
    if identifier.startswith(item["category"] + "/"):
        item["id"] = identifier[len(item["category"]) + 1:]
    corpus.write_markdown(item, content)
    item["id"] = identifier


def main():
    corpus = Corpus(ROOT, "langchain-deep-agents", "LangChain Academy: Introduction to Deep Agents", "https://academy.langchain.com/courses/foundation-introduction-to-deepagents")
    by_raw = {str((ROOT / item["raw_path"]).resolve()): ROOT / item["markdown_path"] for item in corpus.data["materials"] if item.get("raw_path") and item.get("markdown_path")}
    for item in corpus.data["materials"]:
        path = ROOT / item.get("raw_path", "")
        if item["category"] == "lessons":
            source = path.read_text(encoding="utf-8")
            published = re.search(r"\]\((https://langchain-ai\.github\.io/[^)]+)\)", source)
            if published:
                item["aliases"] = list(set(item.get("aliases", []) + [published.group(1)]))
        if item["category"] == "repositories" and "/thinkific/src/" in item.get("raw_path", "") and path.suffix in (".md", ".html"):
            source = path.read_text(encoding="utf-8")
            page, slides, scripts = make_readable(source, path.suffix == ".html")
            content = LessonMarkdown(path, ROOT / item["markdown_path"], by_raw, item["url"]).convert(str(page))
            item.update(conversion_method="markdown-and-html-with-static-slideshow-data", conversion_status="converted_with_limitations" if scripts else "converted", slideshow_slides=slides, interactive_source_blocks=scripts)
            if scripts:
                item["notes"] = ["Interactive programs are preserved in fenced source blocks without executing downloaded code."]
            write_existing(corpus, item, content)
    # Explicitly assigned paper links must include full text rather than only an abstract.
    papers = [item for item in corpus.data["materials"] if item["category"] == "readings" and "arxiv.org/abs/" in item["url"]]
    full_texts = 0
    for item in papers:
        identifier = item["url"].rsplit("/", 1)[-1]
        page = BeautifulSoup((ROOT / item["raw_path"]).read_bytes(), "html.parser")
        heading = page.select_one("h1.title")
        title = heading.get_text(" ", strip=True).removeprefix("Title:") if heading else "Assigned paper " + identifier
        result = corpus.add("https://arxiv.org/pdf/" + identifier, title, "readings", "arxiv-" + identifier.replace(".", "-") + "-full-text", expected="pdf")
        full_texts += bool(result.get("markdown_path"))
    video_url = "https://www.youtube.com/watch?v=z30BJFWe89c"
    if not any(item["url"] == video_url for item in corpus.data["materials"]):
        try:
            class TimedSession(requests.Session):
                def request(self, *args, **kwargs):
                    kwargs.setdefault("timeout", 25)
                    return super().request(*args, **kwargs)
            transcript = YouTubeTranscriptApi(http_client=TimedSession()).fetch("z30BJFWe89c", languages=("en",))
            path = ROOT / "raw/videos/course-announcement-z30BJFWe89c.json"
            path.write_text(json.dumps(transcript.to_raw_data(), indent=2, ensure_ascii=False), encoding="utf-8")
            binary = path.read_bytes()
            item = {"id": "course-announcement", "title": "Deep Agents course announcement: public English transcript", "url": video_url, "category": "videos", "retrieved_at": datetime.now(timezone.utc).isoformat(), "raw_path": path.relative_to(ROOT).as_posix(), "bytes": len(binary), "sha256": hashlib.sha256(binary).hexdigest(), "download_status": "downloaded", "conversion_status": "converted", "conversion_method": "public-youtube-caption-text", "notes": ["Public captions were archived; video binary was not downloaded."]}
            corpus.data["materials"].append(item)
            corpus.write_markdown(item, "\n\n".join(f"[{int(segment.start // 60):02d}:{int(segment.start % 60):02d}] {segment.text}" for segment in transcript))
        except Exception as error:
            corpus.record_gap(video_url, "Deep Agents course announcement", "videos", "Public caption request failed: " + type(error).__name__ + ": " + str(error)[:900])
    note = "The repository has 29 substantive lesson/setup pages, including both language versions and Module 6. Separate platform welcome, conclusion, module-introduction, feedback, progress, and certificate items are not provided as separate public repository files. Public walkthrough transcripts are archived where linked from the lesson source."
    if note not in corpus.data["notes"]:
        corpus.data["notes"].append(note)
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
    corpus.finalize()
    readme = ROOT / "README.md"
    readme.write_text(readme.read_text(encoding="utf-8").replace("[Manifest](manifest.json)", "[Lesson contents](CONTENTS.md) · [Manifest](manifest.json)", 1), encoding="utf-8")
    coverage_path = ROOT / "coverage.json"
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    coverage["assigned_arxiv_full_texts"] = full_texts
    coverage["announcement_transcripts"] = sum(item["url"] == video_url and bool(item.get("markdown_path")) for item in corpus.data["materials"])
    coverage["example_endpoints_not_teaching_materials"] = [item["url"] for item in corpus.data["materials"] if item["category"] == "examples"]
    coverage_path.write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(corpus.data["counts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
