"""Normalize the pilot archive and attempt public lecture captions."""

import json
import re
import hashlib
from pathlib import Path
from urllib.parse import urljoin, urlparse

import fitz
from bs4 import BeautifulSoup
from markdownify import markdownify
from youtube_transcript_api import YouTubeTranscriptApi

from corpus import Corpus, code_block, map_prose, resolve_markdown_urls


def main():
    root = Path("courses/stanford-cs329z")
    data = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    corpus = Corpus(root, data["source_id"], data["title"], data["source_url"])
    corpus.data = data
    corpus.record_gap("https://edstem.org/us/courses/106723/discussion", "Ed Discussion", "restricted", "Private enrolled-student discussion service; not part of the public archive.", "requires_login")
    corpus.record_gap("https://canvas.stanford.edu/courses/233286", "Course Canvas", "restricted", "Enrolled-student course service; not part of the public archive.", "requires_login")
    for url, title in [
        ("https://www.overleaf.com/latex/templates/template-for-iclr-2025-conference-submission/gqzkdyycxtvt", "Project report: ICLR submission format"),
        ("https://iclr.cc/Conferences/2026/AuthorGuide", "Project report: ICLR author guide and LLM policy"),
        ("https://2021.aclweb.org/ethics/Ethics-FAQ/", "Project ethics: ACL guidelines"),
        ("http://blog.pnas.org/iforc.pdf", "Project authorship: PNAS guidance"),
    ]:
        corpus.add(url, title, "references")
    # Rebuild existing PDFs with clean block ordering and preserve URL annotations.
    for item in data["materials"]:
        if item["url"].startswith("https://raw.githubusercontent.com/openclaw/openclaw/"):
            item["aliases"] = ["https://github.com/openclaw/openclaw"]
        if item.get("raw_path", "").endswith(".ipynb") and item.get("markdown_path"):
            notebook = json.loads((root / item["raw_path"]).read_text(encoding="utf-8"))
            item["conversion_method"] = "notebook-cells-and-outputs"
            item["conversion_status"] = "converted"
            corpus.write_markdown(item, corpus.notebook_content(item, notebook))
        if item.get("raw_path", "").endswith(".html") and item.get("markdown_path"):
            page = BeautifulSoup((root / item["raw_path"]).read_bytes(), "html.parser")
            for element in page.select("script, style, nav, footer, noscript, svg, form"):
                element.decompose()
            main_content = page.select_one("article") or page.select_one("main") or page.body or page
            base_url = item.get("final_url", item["url"])
            for anchor in main_content.select("a[href]"):
                anchor["href"] = urljoin(base_url, anchor["href"])
            item["assets"] = []
            for image in main_content.select("img"):
                source = image.get("src") or image.get("data-src")
                if not source or source.startswith("data:"):
                    continue
                image_url = urljoin(base_url, source)
                extension = Path(urlparse(image_url).path).suffix
                if extension.lower() not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"):
                    extension = ".png"
                asset = root / "raw" / "assets" / (hashlib.sha256(image_url.encode()).hexdigest()[:16] + extension)
                if asset.exists():
                    image["src"] = "@@ROOT@@/" + asset.relative_to(root).as_posix()
                    binary = asset.read_bytes()
                    item["assets"].append({"url": image_url, "raw_path": asset.relative_to(root).as_posix(), "bytes": len(binary), "sha256": hashlib.sha256(binary).hexdigest()})
                else:
                    image["src"] = image_url
            corpus.write_markdown(item, markdownify(str(main_content), heading_style="ATX", bullets="-", strip=["button"]))
        if item["category"] != "repositories" and item.get("raw_path", "").endswith((".md", ".mdx")) and item.get("markdown_path"):
            raw_source = root / item["raw_path"]
            corpus.write_markdown(item, resolve_markdown_urls(raw_source.read_text(encoding="utf-8", errors="replace"), item.get("final_url", item["url"])))
        if item.get("conversion_method") == "source-code-fence" and item.get("markdown_path"):
            raw_source = root / item["raw_path"]
            corpus.write_markdown(item, code_block(raw_source.read_text(encoding="utf-8", errors="replace"), "python" if raw_source.suffix == ".py" else raw_source.suffix[1:]))
        if item.get("raw_path", "").endswith(".pdf") and item.get("markdown_path"):
            pdf = fitz.open(root / item["raw_path"])
            pages = []
            for index, page in enumerate(pdf, 1):
                text = "\n\n".join(block[4].strip() for block in page.get_text("blocks", sort=False) if block[6] == 0).strip()
                text = text.replace("[", "\\[").replace("]", "\\]").replace("`", "\\`")
                urls = sorted({link.get("uri") for link in page.get_links() if link.get("uri")})
                if urls:
                    text += "\n\n### Page links\n\n" + "\n".join(f"- [Link {number}]({url})" for number, url in enumerate(urls, 1))
                pages.append(f"## Page {index}\n\n" + (text or "[No extractable text. See the original PDF.]"))
            corpus.write_markdown(item, "\n\n".join(pages))
    # Repair repository links using source files as the reference point.
    by_raw = {str((root / item["raw_path"]).resolve()): root / item["markdown_path"] for item in data["materials"] if item.get("raw_path") and item.get("markdown_path")}
    for item in data["materials"]:
        if item["category"] != "repositories" or not item.get("markdown_path"):
            continue
        import os
        target = root / item["markdown_path"]
        raw = root / item["raw_path"]
        if raw.suffix == ".zip":
            children = [child for child in data["materials"] if child["id"].startswith(item["id"] + "/") and child.get("markdown_path")]
            content = f"Original archive contains {item.get('file_count')} files. Code was not executed.\n\n"
            content += "\n".join(f"- [{child['title'].split(': ', 1)[-1]}]({os.path.relpath(root / child['markdown_path'], target.parent).replace(chr(92), '/')})" for child in children)
            corpus.write_markdown(item, content)
            continue
        content = target.read_text(encoding="utf-8")
        header, body = content.split("\n\nRetrieved:", 1)
        def rewrite(match):
            label, url = match.groups()
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("#"):
                return match.group(0)
            source = (raw.parent / url.split("#", 1)[0]).resolve()
            if not source.exists():
                return match.group(0)
            dest = by_raw.get(str(source), source)
            return f"[{label}]({os.path.relpath(dest, target.parent).replace(chr(92), '/')})"
        body = map_prose(body, lambda text: re.sub(r"(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)", rewrite, text))
        target.write_text(header + "\n\nRetrieved:" + body, encoding="utf-8")
    # A finite request timeout avoids blocking the archive on a video service.
    import requests
    class TimedSession(requests.Session):
        def request(self, *args, **kwargs):
            kwargs.setdefault("timeout", 25)
            return super().request(*args, **kwargs)
    api = YouTubeTranscriptApi(http_client=TimedSession())
    for item in data["materials"]:
        if item["category"] != "videos":
            continue
        video_id = item["url"].rsplit("/", 1)[-1]
        print("Captions", video_id, flush=True)
        try:
            transcript = api.fetch(video_id, languages=("en",))
            raw_path = root / "raw" / "videos" / (video_id + ".json")
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text(json.dumps(transcript.to_raw_data(), indent=2, ensure_ascii=False), encoding="utf-8")
            binary = raw_path.read_bytes()
            item.update(raw_path=raw_path.relative_to(root).as_posix(), bytes=len(binary), sha256=hashlib.sha256(binary).hexdigest(), download_status="downloaded", conversion_status="converted", conversion_method="public-caption-text")
            item["notes"] = ["Video binary excluded. Public English captions archived; machine-generated captions may contain recognition errors."]
            corpus.write_markdown(item, "\n\n".join(f"[{int(snippet.start // 60):02d}:{int(snippet.start % 60):02d}] {snippet.text}" for snippet in transcript))
        except Exception as error:
            item["notes"] = ["Video binary excluded.", "Public English caption attempt failed: " + type(error).__name__ + ": " + str(error)[:1200]]
        corpus.save()
    for item in data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
    corpus.finalize()
    discovered = json.loads((root / "discovered-links.json").read_text(encoding="utf-8"))
    archived_urls = {item["url"] for item in data["materials"]}
    excluded_speakers = {"Ryan Marten", "Alex Shaw", "Andrew Ng", "Carlos Jimenez", "Alexander Wettig"}
    coverage = {"scope": "All unique links in official schedule and deadline tables; speaker personal pages excluded. Linked readings are collected one level, not recursively.",
                "discovered_links": len(discovered), "excluded_links": [], "missing_links": []}
    for url, title in discovered:
        if title in excluded_speakers:
            coverage["excluded_links"].append({"url": url, "title": title, "reason": "Speaker personal page"})
        elif url not in archived_urls and not ("github.com/openclaw/" in url and any("raw.githubusercontent.com/openclaw/" in target for target in archived_urls)):
            coverage["missing_links"].append({"url": url, "title": title})
    (root / "coverage.json").write_text(json.dumps(coverage, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(data["counts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
