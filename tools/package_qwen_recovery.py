"""Prepare a rendered public article for the active CMU collector to merge."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup
from markdownify import markdownify

from corpus import Corpus


def main():
    root = Path("tmp/recoveries/qwen")
    rendered = json.loads((root / "render.json").read_text(encoding="utf-8"))
    corpus = Corpus(root, "cmu-11768", "CMU optional reading recovery", "https://www.cmu-agents.com/")
    if corpus.data["materials"]:
        print("The rendered article package already exists.")
        return
    raw_path = Path("raw/recoveries/qwen3-8-flash-next-rendered.html")
    (root / raw_path).parent.mkdir(parents=True, exist_ok=True)
    binary = rendered["html"].encode("utf-8")
    (root / raw_path).write_bytes(binary)
    item = {
        "id": "qwen3-8-flash-next-rendered", "title": rendered["title"],
        "url": rendered["url"], "final_url": rendered["url"],
        "category": "optional-readings", "published_at": "2026-08-26",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "raw_path": raw_path.as_posix(), "bytes": len(binary),
        "sha256": hashlib.sha256(binary).hexdigest(),
        "download_status": "downloaded", "conversion_status": "converted",
        "conversion_method": "rendered-dom-main-content-to-markdown", "assets": [],
        "notes": ["The ordinary HTTP response is an app shell. This raw file is the public article DOM after browser rendering. The article was archived without following its bibliography or downloading model weights."],
    }
    soup = BeautifulSoup(rendered["html"], "html.parser")
    article = soup.select_one("article")
    if not article or "Introduction" not in article.get_text() or "Citation" not in article.get_text():
        raise ValueError("The rendered snapshot does not contain the complete expected article")
    for element in article.select("script, style, nav, footer, button, svg"):
        element.decompose()
    for anchor in article.select("a[href]"):
        anchor["href"] = urljoin(rendered["url"], anchor["href"])
    for image, discovered in zip(article.select("img"), rendered["images"], strict=True):
        image_url = discovered["src"]
        response = corpus.request(image_url)
        response.raise_for_status()
        if not response.headers.get("Content-Type", "").startswith("image/"):
            raise ValueError("An article image response is not an image")
        suffix = Path(urlsplit(image_url).path).suffix.lower()
        if suffix not in (".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif"):
            suffix = ".png"
        asset_path = Path("raw/recoveries/qwen-assets") / (hashlib.sha256(image_url.encode()).hexdigest()[:20] + suffix)
        (root / asset_path).parent.mkdir(parents=True, exist_ok=True)
        (root / asset_path).write_bytes(response.content)
        item["assets"].append({"url": image_url, "raw_path": asset_path.as_posix(), "bytes": len(response.content), "sha256": hashlib.sha256(response.content).hexdigest()})
        image["src"] = "@@ROOT@@/" + asset_path.as_posix()
    content = "Published: 2026-08-26\n\n" + markdownify(str(article), heading_style="ATX", bullets="-")
    corpus.write_markdown(item, content)
    corpus.data["materials"].append(item)
    corpus.finalize()
    print(json.dumps({"markdown_path": item["markdown_path"], "article_characters": len(rendered["text"]), "images": len(item["assets"])}))


if __name__ == "__main__":
    main()
