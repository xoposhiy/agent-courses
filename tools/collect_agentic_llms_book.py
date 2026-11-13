"""Archive the Agentic Large Language Models textbook and linked chapter text."""

import hashlib
import json
import tarfile
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup

from corpus import Corpus


def main():
    corpus = Corpus("courses/agentic-large-language-models", "agentic-large-language-models", "Agentic Large Language Models", "https://arxiv.org/abs/2610.13455")
    corpus.data["authors"] = ["Max van Duijn", "Michiel van der Meer", "Aske Plaat", "Niki van Stein"]
    corpus.add("https://arxiv.org/abs/2610.13455", "arXiv record and version history", "metadata", "arxiv-record")
    for url, title, name in [
        ("https://arxiv.org/html/2610.13455v1", "Full book HTML", "book.html"),
        ("https://arxiv.org/src/2610.13455v1", "Original TeX source archive", "book-source.tar.gz"),
    ]:
        if any(item["url"] == url and item.get("download_status") == "downloaded" for item in corpus.data["materials"]):
            continue
        item = {"id": "originals/" + name, "title": title, "url": url, "category": "originals", "retrieved_at": datetime.now(timezone.utc).isoformat(), "notes": []}
        corpus.data["materials"].append(item)
        try:
            response = corpus.request(url)
            item.update(http_status=response.status_code, final_url=response.url, content_type=response.headers.get("Content-Type", ""))
            response.raise_for_status()
            raw = corpus.root / "raw/originals" / name
            raw.parent.mkdir(parents=True, exist_ok=True)
            raw.write_bytes(response.content)
            item.update(raw_path=raw.relative_to(corpus.root).as_posix(), bytes=len(response.content), sha256=hashlib.sha256(response.content).hexdigest(), download_status="downloaded", conversion_status="pending")
            if name.endswith(".tar.gz"):
                target = corpus.root / "raw/source"
                target.mkdir(parents=True, exist_ok=True)
                with tarfile.open(raw, "r:*") as archive:
                    for member in archive.getmembers():
                        dest = target / member.name
                        if not dest.resolve().is_relative_to(target.resolve()) or not member.isfile():
                            continue
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        dest.write_bytes(archive.extractfile(member).read())
                item.update(conversion_status="not_applicable", conversion_method="original-source-archive")
                item["notes"].append("All original TeX and figure files are preserved in raw/source. Downloaded code was not executed.")
        except Exception as error:
            item.update(download_status="failed", conversion_status="failed")
            item["notes"].append(type(error).__name__ + ": " + str(error))
        corpus.save()
    corpus.add("https://arxiv.org/pdf/2610.13455v1", "Full book PDF: 472 pages", "book", "full-book-pdf", expected="pdf")
    corpus.finalize()
    page = BeautifulSoup((corpus.root / "raw/originals/book.html").read_bytes(), "html.parser")
    article = page.select_one("article")
    print("Article children:", [(child.name, child.get("class"), child.get("id")) for child in article.children if getattr(child, "name", None)], flush=True)
    print("Chapter sections:", [(section.get("id"), section.find(["h1", "h2", "h3"]).get_text(" ", strip=True) if section.find(["h1", "h2", "h3"]) else "") for section in page.select(".ltx_chapter")], flush=True)
    print("Images:", [(img.get("src"), img.get("alt", "")[:60]) for img in page.select("img")][:10], flush=True)
    print("Math:", str(page.select_one("math"))[:300], flush=True)


if __name__ == "__main__":
    main()
