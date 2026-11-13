"""Use the schedule's lecture titles in the pilot index and transcript pages."""

import json
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from corpus import Corpus


def main():
    root = Path("courses/stanford-cs329z")
    data = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    corpus = Corpus(root, data["source_id"], data["title"], data["source_url"])
    corpus.data = data
    page = BeautifulSoup((root / "raw/pages/index.html").read_bytes(), "html.parser")
    titles = {}
    for row in page.select("tr"):
        slide = row.select_one("a[href*='/slides/']")
        title = row.select_one(".lec-title")
        if not slide or not title:
            continue
        number = int(Path(urlparse(slide["href"]).path).stem.removeprefix("lecture"))
        titles[slide["href"]] = f"Lecture {number}: " + title.get_text(" ", strip=True)
        for video in row.select("a.video-link"):
            titles[video["href"]] = f"Lecture {number} transcript: " + title.get_text(" ", strip=True)
    for item in data["materials"]:
        if item["url"] in titles:
            item["title"] = titles[item["url"]]
            path = root / item["markdown_path"]
            content = path.read_text(encoding="utf-8")
            path.write_text("# " + item["title"] + "\n" + content.split("\n", 1)[1], encoding="utf-8")
    corpus.finalize()


if __name__ == "__main__":
    main()
