"""Download source materials and build a linked Markdown corpus."""

from __future__ import annotations

import hashlib
import base64
import io
import json
import os
import re
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import fitz
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from network_pacing import paced_host
from content_checks import access_page_reason


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:110] or "material"


def code_block(text, language="text"):
    runs = [len(match.group()) for match in re.finditer(r"`+", text)]
    fence = "`" * max(3, max(runs, default=0) + 1)
    return fence + language + "\n" + text + "\n" + fence


def map_prose(text, transform):
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines.append(line)
        else:
            lines.append(line if fence else transform(line))
    return "".join(lines)


def resolve_markdown_urls(text, base_url):
    def rewrite(match):
        label, url = match.groups()
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("#"):
            return match.group(0)
        return f"[{label}]({urljoin(base_url, url)})"
    return map_prose(text, lambda line: re.sub(r"(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)", rewrite, line))


def main_content(soup):
    body = soup.body or soup
    size = lambda element: len(element.get_text(" ", strip=True))
    main = max(soup.select("main, [role='main']"), key=size, default=None)
    if main is not None and size(main) >= 100:
        return main
    article = max(soup.select("article"), key=size, default=None)
    if article is not None and size(article) >= 0.55 * size(body):
        return article
    return body


class Corpus:
    def __init__(self, root, source_id, title, source_url):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "CourseResearchArchive/1.0 (public educational materials)"
        self.data = {"schema_version": "1.0", "source_id": source_id, "title": title,
                     "source_url": source_url, "retrieved_at": datetime.now(timezone.utc).isoformat(),
                     "materials": [], "notes": []}
        manifest_path = self.root / "manifest.json"
        if manifest_path.is_file():
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
            if existing.get("source_id") != source_id:
                raise ValueError("The existing manifest belongs to a different source")
            self.data = existing
        else:
            self.save()

    def save(self):
        (self.root / "manifest.json").write_text(json.dumps(self.data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def request(self, url):
        def get_response():
            if urlparse(url).netloc.endswith("arxiv.org"):
                with paced_host("arxiv.org"):
                    return self.session.get(url, timeout=(15, 70))
            return self.session.get(url, timeout=(15, 70))
        response = get_response()
        if response.status_code in (429, 503):
            wait = response.headers.get("Retry-After", "3")
            time.sleep(min(int(wait) if wait.isdigit() else 3, 30))
            response = get_response()
        return response

    def record_gap(self, url, title, category, reason, status="unavailable"):
        item = {"id": slug(title), "title": title, "url": url, "category": category,
                "retrieved_at": datetime.now(timezone.utc).isoformat(), "download_status": status,
                "conversion_status": "not_available", "notes": [reason]}
        self.data["materials"].append(item)
        self.save()
        return item

    def notebook_content(self, item, notebook):
        cells = []
        def joined(value):
            return "".join(value) if isinstance(value, list) else str(value or "")
        def image_asset(mime, value):
            content = joined(value)
            binary = content.encode("utf-8") if mime == "image/svg+xml" else base64.b64decode(content)
            extension = {"image/png": ".png", "image/jpeg": ".jpg", "image/svg+xml": ".svg", "image/gif": ".gif"}.get(mime, ".bin")
            dest = self.root / "raw" / "assets" / (hashlib.sha256(binary).hexdigest()[:24] + extension)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(binary)
            markdown_parent = (self.root / "markdown" / item["category"] / (item["id"] + ".md")).parent
            return os.path.relpath(dest, markdown_parent).replace("\\", "/")
        for index, cell in enumerate(notebook.get("cells", []), 1):
            source = joined(cell.get("source", []))
            for name, representations in cell.get("attachments", {}).items():
                for mime, content in representations.items():
                    if mime.startswith("image/"):
                        source = source.replace("attachment:" + name, image_asset(mime, content))
                        break
            cells.append(f"## Cell {index}\n\n" + (source if cell.get("cell_type") == "markdown" else code_block(source, "python")))
            for output in cell.get("outputs", []):
                if output.get("text"):
                    cells.append(code_block(joined(output["text"])))
                rich = output.get("data", {})
                images = [mime for mime in rich if mime.startswith("image/")]
                if images:
                    mime = "image/png" if "image/png" in images else images[0]
                    cells.append(f"![Cell {index} output]({image_asset(mime, rich[mime])})")
                elif "text/html" in rich:
                    cells.append(markdownify(joined(rich["text/html"]), heading_style="ATX"))
                elif "text/latex" in rich:
                    cells.append("$$\n" + joined(rich["text/latex"]) + "\n$$")
                elif "text/plain" in rich:
                    cells.append(code_block(joined(rich["text/plain"])))
                if output.get("output_type") == "error":
                    cells.append(code_block(joined(output.get("ename")) + ": " + joined(output.get("evalue")) + "\n" + "\n".join(output.get("traceback", []))))
                unknown = [mime for mime in rich if mime not in ("text/html", "text/latex", "text/plain") and not mime.startswith("image/")]
                if unknown:
                    item["conversion_status"] = "converted_with_limitations"
                    item["notes"].append("Rich notebook output remains in the raw notebook: " + ", ".join(unknown))
        return "\n\n".join(cells)

    def pdf_content(self, item, body):
        document = fitz.open(stream=body, filetype="pdf")
        parts = []
        empty = []
        for index, page in enumerate(document, 1):
            text = "\n\n".join(block[4].strip() for block in page.get_text("blocks", sort=False) if block[6] == 0).strip()
            text = text.replace("[", "\\[").replace("]", "\\]").replace("`", "\\`")
            urls = sorted({link.get("uri") for link in page.get_links() if link.get("uri")})
            if urls:
                text += "\n\n### Page links\n\n" + "\n".join(f"- [Link {number}]({url})" for number, url in enumerate(urls, 1))
            if len(text) < 15:
                empty.append(index)
            parts.append(f"## Page {index}\n\n{text or '[No extractable text on this page. See the original PDF.]'}")
        item["page_count"] = len(document)
        item["conversion_method"] = "pymupdf-text-by-page"
        item["conversion_status"] = "converted_with_limitations"
        item["notes"].append("Text extraction preserves source text block order and page boundaries. Read the original PDF for figures, equations, and exact layout.")
        if empty:
            item["notes"].append("Pages with little or no extractable text: " + ", ".join(map(str, empty)))
        return "\n\n".join(parts)

    def html_content(self, item, body, base_url):
        soup = BeautifulSoup(body, "html.parser")
        access_reason = access_page_reason(
            base_url, soup.title.get_text(" ", strip=True) if soup.title else "",
            soup.get_text(" ", strip=True),
        )
        if access_reason:
            raise ValueError(access_reason)
        for element in soup.select("script, style, nav, footer, noscript, svg, form"):
            element.decompose()
        main = main_content(soup)
        if len(main.get_text(" ", strip=True)) < 100:
            raise ValueError("HTML has too little content; possible app shell or access page")
        for anchor in main.select("a[href]"):
            anchor["href"] = urljoin(base_url, anchor["href"])
        for image in main.select("img, video[poster]"):
            attribute = "poster" if image.name == "video" else "src"
            src = image.get(attribute) or image.get("data-src")
            if not src or src.startswith("data:"):
                continue
            image_url = urljoin(base_url, src)
            image[attribute] = image_url
            cached = next((asset for asset in item.get("assets", []) if asset.get("url") == image_url and asset.get("raw_path") and (self.root / asset["raw_path"]).is_file()), None)
            if cached:
                image[attribute] = "@@ROOT@@/" + cached["raw_path"]
                continue
            try:
                response = self.request(image_url)
                response.raise_for_status()
                if not response.headers.get("Content-Type", "").startswith("image/"):
                    item["notes"].append("Image remains remote: " + image_url + " (the server did not return an image)")
                    continue
                extension = Path(urlparse(image_url).path).suffix
                if extension.lower() not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"):
                    extension = ".png"
                destination = self.root / "raw" / "assets" / (hashlib.sha256(image_url.encode()).hexdigest()[:16] + extension)
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(response.content)
                item.setdefault("assets", []).append({"url": image_url, "raw_path": destination.relative_to(self.root).as_posix(), "bytes": len(response.content), "sha256": hashlib.sha256(response.content).hexdigest(), "retrieved_at": datetime.now(timezone.utc).isoformat()})
                image[attribute] = "@@ROOT@@/" + destination.relative_to(self.root).as_posix()
            except Exception:
                item["notes"].append("Image remains remote: " + image_url)
        item["conversion_method"] = "html-main-content-to-markdown"
        item["conversion_status"] = "converted"
        return markdownify(str(main), heading_style="ATX", bullets="-", strip=["button"])

    def add(self, url, title, category="pages", name=None, expected=None):
        existing = next((x for x in self.data["materials"] if x["url"] == url and x.get("raw_path") and x.get("download_status") == "downloaded" and x.get("conversion_status", "").startswith("converted")), None)
        if existing:
            return existing
        item = {"id": slug(name or title), "title": title, "url": url, "category": category,
                "retrieved_at": datetime.now(timezone.utc).isoformat(), "notes": []}
        self.data["materials"].append(item)
        try:
            cached = self.root / "raw" / category / (item["id"] + ".pdf")
            if expected == "pdf" and cached.is_file() and cached.read_bytes()[:5] == b"%PDF-":
                response = requests.Response()
                response.status_code = 200
                response.url = url
                response.headers["Content-Type"] = "application/pdf"
                response._content = cached.read_bytes()
                item["notes"].append("Reused the already downloaded original PDF from this course archive.")
            else:
                response = self.request(url)
            item.update(http_status=response.status_code, final_url=response.url,
                        content_type=response.headers.get("Content-Type", ""))
            body = response.content
            pdf = body.startswith(b"%PDF-")
            html = "html" in item["content_type"] or body.lstrip().startswith((b"<!DOCTYPE", b"<!doctype", b"<html"))
            extension = ".pdf" if pdf else ".html" if html else Path(urlparse(response.url).path).suffix or ".txt"
            raw = self.root / "raw" / category / (item["id"] + extension)
            raw.parent.mkdir(parents=True, exist_ok=True)
            raw.write_bytes(body)
            item.update(raw_path=raw.relative_to(self.root).as_posix(), bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
            response.raise_for_status()
            if expected == "pdf" and not pdf:
                raise ValueError("Expected a PDF; response is not a PDF")
            item["download_status"] = "downloaded"
            if pdf:
                content = self.pdf_content(item, body)
            elif html:
                content = self.html_content(item, body, response.url)
            else:
                content = response.text
                item["conversion_method"] = "source-text"
                item["conversion_status"] = "converted"
                if extension in (".py", ".sh", ".toml", ".yaml", ".yml", ".json", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".sql", ".tex", ".rst", ".csv", ".css", ".r", ".rs", ".go", ".c", ".cpp", ".h"):
                    content = code_block(content, "python" if extension == ".py" else extension[1:])
                    item["conversion_method"] = "source-code-fence"
                elif extension == ".ipynb":
                    notebook = response.json()
                    content = self.notebook_content(item, notebook)
                    item["conversion_method"] = "notebook-cells-and-outputs"
                elif extension in (".md", ".mdx"):
                    content = resolve_markdown_urls(content, response.url)
                    item["conversion_method"] = "source-markdown-with-resolved-links"
            self.write_markdown(item, content)
        except Exception as error:
            item["download_status"] = "failed" if item.get("http_status", 0) >= 400 or not item.get("raw_path") else item.get("download_status", "response_only")
            item["conversion_status"] = "failed"
            item["notes"].append(f"{type(error).__name__}: {error}")
        self.save()
        return item

    def write_markdown(self, item, content, target_path=None):
        path = self.root / target_path if target_path else self.root / "markdown" / item["category"] / (item["id"] + ".md")
        path.parent.mkdir(parents=True, exist_ok=True)
        raw = os.path.relpath(self.root / item["raw_path"], path.parent).replace("\\", "/")
        home = os.path.relpath(self.root / "README.md", path.parent).replace("\\", "/")
        header = f"# {item['title']}\n\n[Course index]({home}) · [Original source]({item['url']}) · [Raw file]({raw})\n\nRetrieved: {item['retrieved_at']}\n\n"
        if item.get("conversion_method") == "pymupdf-text-by-page":
            header += "> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.\n\n"
        content = re.sub(r"\n{4,}", "\n\n\n", content).strip()
        content = content.replace("@@ROOT@@/", os.path.relpath(self.root, path.parent).replace("\\", "/") + "/")
        path.write_text(header + content + "\n", encoding="utf-8")
        item["markdown_path"] = path.relative_to(self.root).as_posix()

    def add_repo(self, url, title, name=None):
        existing = next((item for item in self.data["materials"] if item["url"] == url and item.get("download_status") == "downloaded" and item.get("markdown_path")), None)
        if existing:
            return existing
        parsed = urlparse(url)
        owner, repo = parsed.path.strip("/").split("/")[:2]
        repo_id = name or slug(owner + "-" + repo)
        item = {"id": repo_id, "title": title, "url": url, "category": "repositories",
                "retrieved_at": datetime.now(timezone.utc).isoformat(), "notes": []}
        self.data["materials"].append(item)
        try:
            archive_url = f"https://api.github.com/repos/{owner}/{repo}/zipball"
            response = self.request(archive_url)
            item.update(http_status=response.status_code, final_url=response.url, archive_url=archive_url)
            response.raise_for_status()
            archive = self.root / "raw" / "repositories" / (repo_id + ".zip")
            archive.parent.mkdir(parents=True, exist_ok=True)
            archive.write_bytes(response.content)
            item.update(raw_path=archive.relative_to(self.root).as_posix(), bytes=len(response.content),
                        sha256=hashlib.sha256(response.content).hexdigest(), download_status="downloaded")
            extracted = self.root / "raw" / "repositories" / repo_id
            count = 0
            docs = []
            raw_only = []
            with zipfile.ZipFile(io.BytesIO(response.content)) as bundle:
                for member in bundle.infolist():
                    rel = Path(*Path(member.filename).parts[1:])
                    if not rel.parts or member.is_dir() or ".." in rel.parts:
                        continue
                    dest = extracted / rel
                    if not dest.resolve().is_relative_to(extracted.resolve()):
                        raise ValueError("Repository archive path leaves the extraction folder")
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    data = bundle.read(member)
                    dest.write_bytes(data)
                    count += 1
                    suffix = rel.suffix.lower()
                    if suffix not in (".md", ".mdx", ".ipynb", ".py", ".txt", ".toml", ".yaml", ".yml", ".json", ".sh", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".sql", ".tex", ".rst", ".csv", ".html", ".htm", ".pdf", ".css", ".r", ".rs", ".go", ".c", ".cpp", ".h") or rel.name in ("package-lock.json", "pnpm-lock.yaml") or any(part in ("node_modules", ".venv", "dist", "build", ".next") for part in rel.parts) or rel.name.endswith(".min.js"):
                        raw_only.append(dest.relative_to(self.root).as_posix())
                        continue
                    child = {"id": repo_id + "/" + rel.as_posix().replace(".", "-"), "title": title + ": " + rel.as_posix(),
                             "url": f"https://github.com/{owner}/{repo}/blob/HEAD/{rel.as_posix()}", "category": "repositories",
                             "retrieved_at": item["retrieved_at"], "raw_path": dest.relative_to(self.root).as_posix(),
                             "download_status": "downloaded", "conversion_status": "converted", "notes": [],
                             "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
                    text = data.decode("utf-8", errors="replace") if suffix != ".pdf" else ""
                    if suffix == ".pdf":
                        text = self.pdf_content(child, data)
                    elif suffix in (".html", ".htm"):
                        page = BeautifulSoup(data, "html.parser")
                        for element in page.select("script, style, nav, footer"):
                            element.decompose()
                        text = markdownify(str(page.select_one("main") or page.body or page), heading_style="ATX")
                        child["conversion_method"] = "html-to-markdown"
                    elif suffix == ".ipynb":
                        notebook = json.loads(text)
                        text = self.notebook_content(child, notebook)
                        child["conversion_method"] = "notebook-cells-and-text-outputs"
                    elif suffix not in (".md", ".mdx"):
                        text = code_block(text, "python" if suffix == ".py" else suffix[1:])
                        child["conversion_method"] = "source-code-fence"
                    else:
                        child["conversion_method"] = "source-markdown"
                    self.write_markdown(child, text)
                    docs.append(child)
            item.update(file_count=count, conversion_status="converted", conversion_method="repository-archive-with-text-files")
            if raw_only:
                item["raw_only_files"] = raw_only
                item["notes"].append("Binary assets, dependency lockfiles, and generated files remain in the raw archive and extracted repository.")
            content = f"Original archive contains {count} files. Code was not executed.\n\n"
            content += "\n".join(f"- [{x['title'].split(': ',1)[-1]}]({os.path.relpath(self.root / x['markdown_path'], self.root / 'markdown' / 'repositories').replace(chr(92), '/')})" for x in docs)
            if raw_only:
                content += "\n\n## Original assets and other files\n\n" + "\n".join(f"- [{Path(path).name}]({os.path.relpath(self.root / path, self.root / 'markdown' / 'repositories').replace(chr(92), '/')})" for path in raw_only)
            self.write_markdown(item, content)
            by_raw_path = {str((self.root / child["raw_path"]).resolve()): self.root / child["markdown_path"] for child in docs}
            for child in docs:
                converted = self.root / child["markdown_path"]
                raw_file = self.root / child["raw_path"]
                def rewrite_relative(match):
                    label, target = match.groups()
                    if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                        return match.group(0)
                    base, fragment = urldefrag(target)
                    source_target = (raw_file.parent / base).resolve()
                    if not source_target.exists():
                        return match.group(0)
                    dest_target = by_raw_path.get(str(source_target), source_target)
                    local = os.path.relpath(dest_target, converted.parent).replace("\\", "/")
                    return f"[{label}]({local})"
                text = converted.read_text(encoding="utf-8")
                # The generated navigation header already points to the correct files.
                header, body = text.split("\n\nRetrieved:", 1)
                body = map_prose(body, lambda text: re.sub(r"(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)", rewrite_relative, text))
                converted.write_text(header + "\n\nRetrieved:" + body, encoding="utf-8")
            self.data["materials"].extend(docs)
        except Exception as error:
            item.update(download_status="downloaded" if item.get("raw_path") else "failed", conversion_status="failed")
            item["notes"].append(f"{type(error).__name__}: {error}")
        self.save()
        return item

    def finalize(self):
        urls = {}
        for item in self.data["materials"]:
            if item.get("markdown_path"):
                for alias in item.get("aliases", []):
                    urls[urldefrag(alias)[0].rstrip("/")] = item["markdown_path"]
                for key in ("url", "final_url"):
                    if item.get(key):
                        urls[urldefrag(item[key])[0].rstrip("/")] = item["markdown_path"]
                        if urlparse(item[key]).path in ("", "/"):
                            urls[item[key].rstrip("/") + "/index.html"] = item["markdown_path"]
                        parsed = urlparse(item[key])
                        if parsed.netloc.endswith("arxiv.org") and parsed.path.startswith("/pdf/"):
                            urls["https://arxiv.org/abs/" + parsed.path.removeprefix("/pdf/").removesuffix(".pdf")] = item["markdown_path"]
        local_redirects = {}
        for item in self.data["materials"]:
            if item.get("markdown_path") and urlparse(item["url"]).netloc.endswith("arxiv.org") and "/abs/" in item["url"]:
                preferred = urls.get(urldefrag(item["url"])[0].rstrip("/"))
                if preferred and preferred != item["markdown_path"]:
                    local_redirects[str((self.root / item["markdown_path"]).resolve())] = preferred
        for item in self.data["materials"]:
            if not item.get("markdown_path"):
                continue
            path = self.root / item["markdown_path"]
            content = path.read_text(encoding="utf-8")
            def rewrite(match):
                label, target = match.groups()
                if label == "Original source":
                    return match.group(0)
                base, fragment = urldefrag(target)
                local = urls.get(base.rstrip("/"))
                if not local and not urlparse(base).scheme and base:
                    local = local_redirects.get(str((path.parent / base).resolve()))
                if local:
                    target = os.path.relpath(self.root / local, path.parent).replace("\\", "/")
                    return f"[{label}]({target})"
                return match.group(0)
            content = map_prose(content, lambda text: re.sub(r"(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)", rewrite, text))
            path.write_text(content, encoding="utf-8")
        self.write_indexes()

    def write_indexes(self):
        index = [f"# {self.data['title']}", "", f"Source: [{self.data['source_url']}]({self.data['source_url']})", "",
                 f"Retrieved: {self.data['retrieved_at']}", "", "[Manifest](manifest.json) · [Gaps and limits](GAPS.md)", "",
                 "Original files are in `raw/`. Full-content Markdown conversions are in `markdown/`. Use the original PDFs for diagrams, formulas, and exact layout.", ""]
        index += ["Repository files and saved traces are linked from each repository archive index. The manifest lists every material.", ""]
        order = ["pages", "chapters", "slides", "assignments", "repositories", "readings", "optional-readings", "references", "videos", "transcripts", "metadata", "restricted"]
        categories = sorted({x["category"] for x in self.data["materials"]}, key=lambda category: (order.index(category) if category in order else len(order), category))
        repository_roots = [str(Path(item["raw_path"]).with_suffix("")).replace("\\", "/") + "/" for item in self.data["materials"] if item["category"] == "repositories" and item.get("raw_path", "").endswith(".zip") and item.get("markdown_path")]
        for category in categories:
            index += ["## " + category.replace("-", " ").title(), ""]
            for item in self.data["materials"]:
                if item["category"] != category:
                    continue
                if item.get("container_url") and item.get("archive_member"):
                    continue
                if category == "repositories" and any(item.get("raw_path", "").startswith(root) for root in repository_roots):
                    continue
                target = item.get("markdown_path") or item.get("raw_path")
                if item.get("conversion_status") in ("failed", "not_available"):
                    if item.get("recovered_by"):
                        index.append(f"- [{item['title']}]({item['recovered_by']}) — recovered from another source; see [gaps](GAPS.md).")
                    else:
                        response_link = f" [Saved response]({item['raw_path']})." if item.get("raw_path") else ""
                        index.append(f"- {item['title']} — {item['download_status']}; conversion {item['conversion_status']}.{response_link} See [gaps](GAPS.md).")
                else:
                    index.append(f"- [{item['title']}]({target})" if target else f"- {item['title']} — {item['download_status']}; see gaps.")
            index.append("")
        (self.root / "README.md").write_text("\n".join(index), encoding="utf-8")
        gaps = ["# Gaps and limits", "", "[Course index](README.md)", "", "PDF Markdown is extracted text. Diagrams, tables, and equations may need the original file. Large video binaries, private services, unpublished materials, dependencies, and model weights are outside this archive.", ""]
        for note in self.data["notes"]:
            gaps += [note, ""]
        for item in self.data["materials"]:
            if item.get("conversion_status") in ("failed", "not_available") or any("Image remains" in x for x in item.get("notes", [])):
                gaps += [f"## {item['title']}", "", f"Source: {item['url']}", "", f"Download: {item['download_status']}; conversion: {item['conversion_status']}.", ""]
                if item.get("recovered_by"):
                    gaps += [f"Full text: [Recovered copy]({item['recovered_by']})", ""]
                gaps += ["- " + note for note in item.get("notes", [])] + [""]
        (self.root / "GAPS.md").write_text("\n".join(gaps), encoding="utf-8")
        self.data["counts"] = {"materials": len(self.data["materials"]), "downloaded": sum(x.get("download_status") == "downloaded" for x in self.data["materials"]),
                               "markdown_files": sum(bool(x.get("markdown_path")) for x in self.data["materials"]), "gaps": sum(x.get("conversion_status") in ("failed", "not_available") for x in self.data["materials"])}
        self.save()
