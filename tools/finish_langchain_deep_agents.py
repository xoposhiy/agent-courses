"""Build readable Deep Agents lessons, public walkthrough transcripts, and readings."""

import hashlib
import json
import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import esprima
import requests
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

from corpus import Corpus, code_block, slug


ROOT = Path("courses/langchain-deep-agents")
REPO = ROOT / "raw/repositories/lca-deepagents"


def static_value(node, source):
    kind = node["type"]
    if kind == "Literal":
        return node.get("value")
    if kind == "TemplateLiteral" and not node.get("expressions"):
        return "".join(part["value"]["cooked"] for part in node["quasis"])
    if kind == "ArrayExpression":
        return [static_value(element, source) for element in node["elements"]]
    if kind == "ObjectExpression":
        return {(prop["key"].get("name") or prop["key"].get("value")): static_value(prop["value"], source) for prop in node["properties"]}
    raise ValueError("Dynamic JavaScript expression remains in source: " + kind)


class LessonMarkdown(MarkdownConverter):
    def __init__(self, raw_file, output_file, by_raw, source_url):
        super().__init__(heading_style="ATX", bullets="-")
        self.raw_file = raw_file
        self.output_file = output_file
        self.by_raw = by_raw
        self.source_url = source_url

    def local_target(self, target):
        if not target or target.startswith("#"):
            return target
        parsed = urlparse(target)
        if parsed.scheme:
            if parsed.netloc == "github.com" and parsed.path.startswith("/langchain-ai/lca-deepagents/blob/"):
                parts = parsed.path.split("/")
                source = REPO / "/".join(parts[5:])
            else:
                return target
        else:
            source = self.raw_file.parent / urldefrag(target)[0]
        if not source.exists() and "/tutors/" in self.raw_file.as_posix():
            module = self.raw_file.stem.split(".", 1)[0]
            source = REPO / "thinkific/src" / module / urldefrag(target)[0]
        if source.exists():
            dest = self.by_raw.get(str(source.resolve()), source)
            return os.path.relpath(dest, self.output_file.parent).replace("\\", "/") + ("#" + parsed.fragment if parsed.fragment else "")
        return urljoin(self.source_url, target)

    def convert_a(self, element, text, parent_tags):
        if element.get("href"):
            element["href"] = self.local_target(element["href"])
        return super().convert_a(element, text, parent_tags)

    def convert_img(self, element, text, parent_tags):
        element["src"] = self.local_target(element.get("src", ""))
        return super().convert_img(element, text, parent_tags)

    def convert_iframe(self, element, text, parent_tags):
        target = self.local_target(element.get("src", ""))
        label = element.get("title") or ("Public video walkthrough" if "descript.com" in target else "Interactive lesson material")
        return f"\n\n[{label}]({target})\n\n"

    def convert_pre(self, element, text, parent_tags):
        code = element.find("code")
        classes = code.get("class", []) if code else []
        language = next((entry.removeprefix("language-") for entry in classes if entry.startswith("language-")), "text")
        return "\n\n" + code_block(element.get_text(), language) + "\n\n"

    def process_tag(self, node, parent_tags=None):
        result = super().process_tag(node, parent_tags)
        if node.get("id"):
            return '<a id="' + node["id"] + '"></a>\n' + result
        return result


def lesson_html(source, is_html=False):
    if is_html:
        return BeautifulSoup(source, "html.parser")
    if source.startswith("---\n") and "\n---" in source[4:]:
        front, rest = source[4:].split("\n---", 1)
        source = code_block(front, "yaml") + "\n\n" + rest
    result = subprocess.run(["pandoc", "--from=markdown+raw_html", "--to=html", "--wrap=none", "--no-highlight"], input=source, text=True, capture_output=True, encoding="utf-8", check=True)
    return BeautifulSoup(result.stdout, "html.parser")


def make_readable(source, is_html=False):
    page = lesson_html(source, is_html)
    slides = 0
    source_blocks = 0
    for style in page.select("style, link[rel='stylesheet']"):
        style.decompose()
    for script in list(page.select("script")):
        if script.get("src"):
            script.decompose()
            continue
        program = script.get_text()
        converted = False
        try:
            tree = esprima.parseScript(program, {"range": True}).toDict()
            expressions = [node["expression"] for node in tree.get("body", []) if node["type"] == "ExpressionStatement"]
            calls = [node for node in expressions if node["type"] == "CallExpression" and node["callee"].get("name") == "buildSlideshow"]
            if calls and len(calls) == len(expressions):
                block = page.new_tag("section")
                for call in calls:
                    data = static_value(call["arguments"][0], program)
                    heading = page.new_tag("h3")
                    heading.string = "Slideshow: " + str(data.get("title") or data.get("id", ""))
                    block.append(heading)
                    for index, slide in enumerate(data.get("slides", []), 1):
                        heading = page.new_tag("h4")
                        heading.string = str(slide.get("tag") or slide.get("title") or f"Slide {index}")
                        block.append(heading)
                        if slide.get("src"):
                            block.append(page.new_tag("img", src=slide["src"], alt=str(slide.get("tag") or f"Slide {index}")))
                        if slide.get("caption"):
                            fragment = BeautifulSoup("<p>" + slide["caption"] + "</p>", "html.parser")
                            block.append(fragment)
                        extra = {key: value for key, value in slide.items() if key not in ("src", "caption", "tag", "title")}
                        if extra:
                            pre = page.new_tag("pre")
                            pre.string = json.dumps(extra, ensure_ascii=False, indent=2)
                            block.append(pre)
                        slides += 1
                script.replace_with(block)
                converted = True
        except Exception:
            pass
        if not converted:
            pre = page.new_tag("pre")
            code = page.new_tag("code", attrs={"class": "language-javascript"})
            code.string = program
            pre.append(code)
            script.replace_with(pre)
            source_blocks += 1
    return page, slides, source_blocks


def record_download(corpus, url, title, category, name, response, content=None):
    existing = next((item for item in corpus.data["materials"] if item["url"] == url and item.get("download_status") == "downloaded"), None)
    if existing:
        return existing
    binary = response.content if content is None else content
    path = ROOT / "raw" / category / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(binary)
    item = {"id": name.rsplit(".", 1)[0], "title": title, "url": url, "category": category, "retrieved_at": datetime.now(timezone.utc).isoformat(), "http_status": response.status_code, "final_url": response.url, "content_type": response.headers.get("Content-Type", ""), "raw_path": path.relative_to(ROOT).as_posix(), "bytes": len(binary), "sha256": hashlib.sha256(binary).hexdigest(), "download_status": "downloaded" if response.ok else "failed", "conversion_status": "pending" if response.ok else "failed", "notes": []}
    corpus.data["materials"].append(item)
    corpus.save()
    return item


def main():
    corpus = Corpus(ROOT, "langchain-deep-agents", "LangChain Academy: Introduction to Deep Agents", "https://academy.langchain.com/courses/foundation-introduction-to-deepagents")
    # Archive only the course-specific subtree of the official tutor repository.
    response = corpus.request("https://api.github.com/repos/langchain-ai/lca-tutors/git/trees/main?recursive=1")
    response.raise_for_status()
    tree = response.json()
    if tree.get("truncated"):
        raise ValueError("Tutor repository tree is truncated")
    files = [entry for entry in tree["tree"] if entry["type"] == "blob" and entry["path"].startswith("lca-deepagents/")]
    for entry in files:
        url = "https://raw.githubusercontent.com/langchain-ai/lca-tutors/main/" + entry["path"]
        name = entry["path"].removeprefix("lca-deepagents/")
        if any(item["url"] == url for item in corpus.data["materials"]):
            continue
        response = corpus.request(url)
        item = record_download(corpus, url, "Course tutor: " + name, "tutors", name, response)
        item["source_blob_sha"] = entry["sha"]
        item["aliases"] = ["https://github.com/langchain-ai/lca-tutors/blob/main/" + entry["path"]]
        item["conversion_method"] = "source-markdown"
        if response.ok:
            item["conversion_status"] = "converted"
            corpus.write_markdown(item, response.text)
    corpus.save()
    raw_lessons = sorted((REPO / "thinkific/src").glob("m*/*.md"))
    raw_assets = sorted((REPO / "thinkific/src").glob("m*/images/*.html"))
    descriptors = []
    for path in raw_lessons + raw_assets:
        name = path.stem
        category = "lessons" if path in raw_lessons else "lesson-assets"
        source = next(item for item in corpus.data["materials"] if item.get("raw_path") == path.relative_to(ROOT).as_posix())
        record = dict(source)
        record.update(id=name, category=category, title=("Lesson: " if category == "lessons" else "Lesson asset: ") + name, notes=[])
        record.pop("markdown_path", None)
        descriptors.append((path, record))
    corpus.data["materials"] = [item for item in corpus.data["materials"] if item["category"] not in ("lessons", "lesson-assets")]
    by_raw = {str((ROOT / item["raw_path"]).resolve()): ROOT / item["markdown_path"] for item in corpus.data["materials"] if item.get("raw_path") and item.get("markdown_path")}
    for path, record in descriptors:
        by_raw[str(path.resolve())] = ROOT / "markdown" / record["category"] / (record["id"] + ".md")
    videos = set()
    references = set()
    slide_count = 0
    script_count = 0
    for path, item in descriptors:
        source = path.read_text(encoding="utf-8")
        videos.update(re.findall(r"https://share\.descript\.com/embed/[A-Za-z0-9]+", source))
        for match in re.finditer(r"^## References[^\n]*\n(.*?)(?=^#{1,2} |\Z)", source, flags=re.MULTILINE | re.DOTALL):
            block = match.group(1)
            references.update(urldefrag(url)[0] for url in re.findall(r"\]\((https?://[^\s)]+)\)", block))
        page, slides, scripts = make_readable(source, path.suffix == ".html")
        output = by_raw[str(path.resolve())]
        content = LessonMarkdown(path, output, by_raw, item["url"]).convert(str(page))
        item.update(conversion_method="markdown-and-html-with-static-slideshow-data", conversion_status="converted_with_limitations" if scripts else "converted", slideshow_slides=slides, interactive_source_blocks=scripts)
        if scripts:
            item["notes"].append("Interactive JavaScript remains as fenced source where a full static conversion is not safe. The source is complete and was not executed.")
        corpus.write_markdown(item, content)
        corpus.data["materials"].append(item)
        slide_count += slides
        script_count += scripts
    # Keep tutor Markdown source intact while making its image and lesson links local.
    for item in corpus.data["materials"]:
        if item["category"] != "tutors" or not item.get("markdown_path"):
            continue
        path = ROOT / item["raw_path"]
        page, slides, scripts = make_readable(path.read_text(encoding="utf-8"))
        output = ROOT / item["markdown_path"]
        content = LessonMarkdown(path, output, by_raw, item["url"]).convert(str(page))
        item["conversion_method"] = "official-tutor-markdown-with-static-content"
        if scripts:
            item["conversion_status"] = "converted_with_limitations"
            item["notes"].append("Interactive JavaScript is preserved as source, without execution.")
        corpus.write_markdown(item, content)
    corpus.save()
    print("Public videos", len(videos), "assigned reference URLs", len(references), flush=True)
    # Public share pages embed full, timed transcript data; fetch the pages, not media.
    def fetch(url):
        try:
            existing = next((item for item in corpus.data["materials"] if item["url"] == url and item.get("download_status") == "downloaded" and item.get("raw_path")), None)
            if existing:
                response = requests.Response()
                response.status_code = existing.get("http_status", 200)
                response.url = url
                response.headers["Content-Type"] = existing.get("content_type", "text/html")
                response._content = (ROOT / existing["raw_path"]).read_bytes()
                return url, response, None
            response = requests.get(url, timeout=(15, 40))
            return url, response, None
        except Exception as error:
            return url, None, error
    with ThreadPoolExecutor(max_workers=4) as workers:
        results = list(workers.map(fetch, sorted(videos)))
    transcripts = 0
    for url, response, error in results:
        video_id = url.rsplit("/", 1)[-1]
        if error:
            corpus.record_gap(url, "Walkthrough " + video_id, "videos", "Public transcript request failed: " + str(error))
            continue
        item = record_download(corpus, url, "Public walkthrough " + video_id, "videos", video_id + ".html", response)
        try:
            page = BeautifulSoup((ROOT / item["raw_path"]).read_bytes(), "html.parser")
            document = page.select_one("script#document")
            if not document:
                raise ValueError("The public share page has no embedded transcript document")
            data = json.loads(document.string)
            blocks = []
            words = 0
            for segment in data.get("content", []):
                tokens = segment.get("words", [])
                if not tokens:
                    continue
                text = "".join(("" if token.get("omitLeadingSpace") else token.get("leadingNonWordText", {}).get("string", " ")) + token.get("text", "") for token in tokens).strip()
                start = tokens[0].get("startTime", 0)
                speaker = (segment.get("speaker") or {}).get("name", "Speaker")
                blocks.append(f"[{int(start // 60):02d}:{int(start % 60):02d}] **{speaker}**: {text}")
                words += len(tokens)
            if not blocks:
                raise ValueError("The public transcript document has no spoken words")
            item.update(title=page.title.get_text(" ", strip=True).removesuffix(" - Descript") if page.title else item["title"], conversion_status="converted", conversion_method="descript-public-timed-transcript", transcript_words=words, duration_seconds=data.get("duration"))
            item["notes"] = ["Full public transcript extracted from embedded document JSON. Video binary was not downloaded."]
            corpus.write_markdown(item, "\n\n".join(blocks))
            transcripts += 1
        except Exception as problem:
            item["conversion_status"] = "failed"
            item["notes"].append(str(problem))
        corpus.save()
    # References are the explicit lists in lesson source, not a recursive docs crawl.
    examples = {url for url in references if urlparse(url).hostname in ("localhost", "127.0.0.1", "0.0.0.0", "example.com")}
    references -= examples
    for item in corpus.data["materials"]:
        if urlparse(item["url"]).hostname in ("localhost", "127.0.0.1", "0.0.0.0", "example.com"):
            item.update(category="examples", conversion_status="not_applicable", download_status="not_material", notes=["Example URL for a student-run service; not a public teaching resource."])
    for url in sorted(references):
        if any(item["url"] == url and item["category"] == "readings" for item in corpus.data["materials"]):
            continue
        parsed = urlparse(url)
        if parsed.netloc == "github.com":
            # Large framework source trees stay as external references; archive pages or files.
            if "/blob/" in parsed.path:
                raw_url = url.replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/", 1)
                item = corpus.add(raw_url, "Assigned source reference: " + parsed.path, "readings", "github-" + hashlib.sha256(url.encode()).hexdigest()[:12])
                item["aliases"] = [url]
            else:
                corpus.add(url, "Assigned repository reference: " + parsed.path, "readings", "github-" + hashlib.sha256(url.encode()).hexdigest()[:12])
        else:
            corpus.add(url, "Assigned reference: " + parsed.path.rstrip("/").rsplit("/", 1)[-1], "readings", slug(parsed.netloc + parsed.path) + "-" + hashlib.sha256(url.encode()).hexdigest()[:8])
        corpus.save()
        print("Reference", url, flush=True)
    corpus.data["notes"] = [
        "The full official teaching repository is archived, including Python, TypeScript, the agent UI, notebooks, and the public lesson-page source. Code and tutor instructions were saved as source data and were not executed or installed.",
        "Readable lessons include both Python and TypeScript branches. Static slideshow data is converted to steps, figures, and captions. Other interactive programs remain in fenced source blocks so that their content is not silently lost.",
        "Academy access failed for the direct archival request. Public lesson text was recovered from the official teaching repository; the original public curriculum is viewable in web search. Enrolled platform progress, feedback forms, and certificates are not part of this archive.",
        "Official lca-tutors/lca-deepagents files are archived as a separate public snapshot. Tutor references can differ from the current primary course lesson source.",
        "Explicit reference URLs from lesson reference sections were fetched one level only. Framework repositories and documentation sites were not recursively mirrored. Large video binaries, model weights, dependencies, and private course services were not downloaded.",
    ]
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
    corpus.finalize()
    contents = ["# Deep Agents lesson contents", "", "[Course index](README.md)", ""]
    for path, item in descriptors:
        if item["category"] == "lessons":
            contents.append(f"- [{path.stem}]({item['markdown_path']})")
    (ROOT / "CONTENTS.md").write_text("\n".join(contents) + "\n", encoding="utf-8")
    readme = ROOT / "README.md"
    readme.write_text(readme.read_text(encoding="utf-8").replace("[Manifest](manifest.json)", "[Lesson contents](CONTENTS.md) · [Manifest](manifest.json)", 1), encoding="utf-8")
    coverage = {"public_lesson_markdown_sources": len(raw_lessons), "converted_lessons": sum(item["category"] == "lessons" for item in corpus.data["materials"]), "interactive_html_assets": len(raw_assets), "static_slideshow_steps": slide_count, "interactive_programs_preserved_as_source": script_count, "official_tutor_subtree_files": len(files), "public_video_urls": len(videos), "public_video_transcripts": transcripts, "explicit_reference_urls": len(references), "excluded_example_urls": sorted(examples), "repository_files": sum(path.is_file() for path in REPO.rglob("*"))}
    (ROOT / "coverage.json").write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(coverage, indent=2), flush=True)


if __name__ == "__main__":
    main()
