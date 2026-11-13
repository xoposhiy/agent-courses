"""Convert the book HTML into linked full text and chapter Markdown files."""

import copy
import hashlib
import html
import json
import os
import fitz
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urldefrag, urljoin, urlparse

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from corpus import Corpus, slug


BASE_URL = "https://arxiv.org/html/2610.13455v1"


class BookMarkdown(MarkdownConverter):
    def __init__(self, output_path, corpus, targets, locations, images, whole=False):
        super().__init__(heading_style="ATX", bullets="-", escape_underscores=False)
        self.output_path = output_path
        self.corpus = corpus
        self.targets = targets
        self.locations = locations
        self.images = images
        self.whole = whole

    def process_tag(self, node, parent_tags=None):
        result = super().process_tag(node, parent_tags)
        anchor = node.get("id")
        if anchor in self.targets:
            return f'<a id="{html.escape(anchor, quote=True)}"></a>\n' + result
        return result

    def convert_math(self, element, text, parent_tags):
        latex = element.get("alttext")
        if not latex:
            annotation = element.select_one("annotation[encoding='application/x-tex']")
            latex = annotation.get_text() if annotation else element.get_text(" ", strip=True)
        return "\n\n$$\n" + latex + "\n$$\n\n" if element.get("display") == "block" else "$" + latex + "$"

    def convert_span(self, element, text, parent_tags):
        classes = element.get("class", [])
        if "ltx_font_bold" in classes:
            return "**" + text + "**"
        if "ltx_font_italic" in classes:
            return "*" + text + "*"
        return text

    def convert_a(self, element, text, parent_tags):
        href = element.get("href", "")
        base, fragment = urldefrag(urljoin(BASE_URL, href))
        if fragment and base == BASE_URL and fragment in self.locations:
            target = self.locations[fragment]
            if self.whole or target.resolve() == self.output_path.resolve():
                element["href"] = "#" + fragment
            else:
                element["href"] = os.path.relpath(target, self.output_path.parent).replace("\\", "/") + "#" + fragment
        elif href:
            element["href"] = urljoin(BASE_URL, href)
        return super().convert_a(element, text, parent_tags)

    def convert_img(self, element, text, parent_tags):
        source = element.get("src", "")
        if source in self.images:
            element["src"] = os.path.relpath(self.images[source], self.output_path.parent).replace("\\", "/")
        else:
            element["src"] = urljoin(BASE_URL, source)
        return super().convert_img(element, text, parent_tags)

    def convert_svg(self, element, text, parent_tags):
        key = "svg:" + element.get("id", "")
        if key in self.images:
            target = os.path.relpath(self.images[key], self.output_path.parent).replace("\\", "/")
            return f"\n\n![Original vector figure]({target})\n\n" + text
        return text


def main():
    corpus = Corpus("courses/agentic-large-language-models", "agentic-large-language-models", "Agentic Large Language Models", "https://arxiv.org/abs/2610.13455")
    root = corpus.root
    source_item = next(item for item in corpus.data["materials"] if item["url"] == BASE_URL)
    source_item.update(id="full-book-html", category="book", conversion_method="arxiv-html-with-latex-and-local-figures", conversion_status="converted")
    raw = root / source_item["raw_path"]
    page = BeautifulSoup(raw.read_bytes(), "html.parser")
    article = page.select_one("article")
    for element in article.select("nav, script, style, button"):
        element.decompose()
    for element in article.select(".ltx_itemize"):
        element.name = "ul"
    for element in article.select(".ltx_enumerate"):
        element.name = "ol"
    for element in article.select(".ltx_item"):
        element.name = "li"
        for label in element.select(".ltx_tag_item"):
            label.decompose()
    chapters = article.select("section.ltx_chapter")
    headings = [(chapter["id"], chapter.find(["h1", "h2", "h3"]).get_text(" ", strip=True)) for chapter in chapters]
    chapter_paths = {identifier: root / "markdown/chapters" / ("chapter-" + identifier[2:].zfill(2) + "-" + slug(title.split(" ", 2)[-1]) + ".md") for identifier, title in headings}
    full_path = root / "markdown/book/full-book-html.md"
    locations = {}
    for element in article.select("[id]"):
        chapter = element if "ltx_chapter" in element.get("class", []) else element.find_parent("section", class_="ltx_chapter")
        locations[element["id"]] = chapter_paths[chapter["id"]] if chapter else full_path
    targets = {urldefrag(urljoin(BASE_URL, a["href"]))[1] for a in article.select("a[href]") if urldefrag(urljoin(BASE_URL, a["href"]))[0] == BASE_URL}
    targets.update(heading["id"] for heading in article.select("h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]"))
    targets.update(identifier for identifier, title in headings)
    # Section IDs occur on the enclosing section rather than the heading itself.
    targets.update(section["id"] for section in article.select("section[id]"))
    images = {}
    missing = []
    for image in article.select("img"):
        source = image["src"]
        if not source:
            if image.get("id") == "Ch3.F1.g1":
                dest = root / "raw/assets/figure-3-1-from-pdf-page-65.png"
                document = fitz.open(root / "raw/book/full-book-pdf.pdf")
                document[64].get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(105, 120, 455, 187)).save(dest)
                images[source] = dest
                source_item["notes"] = ["The experimental HTML omits Figure 3.1. Its graphic was recovered by rendering the figure region from original PDF page 65; the original caption is preserved in Markdown."]
            else:
                missing.append("Empty image source in experimental HTML; see original PDF")
            continue
        relative = unquote(source.split("2610.13455v1/", 1)[-1])
        dest = root / "raw/source" / relative
        if not dest.is_file():
            dest = root / "raw/assets" / Path(relative).name
            if not dest.exists():
                response = corpus.request(urljoin(BASE_URL, source))
                if response.ok and response.headers.get("Content-Type", "").startswith("image/"):
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(response.content)
                else:
                    missing.append(source)
                    continue
        images[source] = dest
    raw_svg = {match.group(1): match.group(0) for match in re.finditer(r'<svg\b[^>]*\bid="([^"]+)"[^>]*>.*?</svg>', raw.read_text(encoding="utf-8"), flags=re.DOTALL)}
    svg_count = 0
    for vector in article.select("figure svg[id]"):
        identifier = vector["id"]
        source = raw_svg[identifier]
        if 'xmlns="http://www.w3.org/2000/svg"' not in source:
            source = source.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
        source = re.sub(r'(<foreignObject[^>]*>\s*)<span(?![^>]*\bxmlns=)', r'\1<span xmlns="http://www.w3.org/1999/xhtml"', source)
        source = re.sub(r'&(?!(?:amp|lt|gt|quot|apos);)([A-Za-z]+);', lambda match: html.unescape(match.group(0)), source)
        ET.fromstring(source)
        dest = root / "raw/assets" / (identifier + ".svg")
        dest.write_text(source, encoding="utf-8")
        images["svg:" + identifier] = dest
        svg_count += 1
    source_item["assets"] = [{"url": BASE_URL + "#" + url[4:] if url.startswith("svg:") else urljoin(BASE_URL, url) if url else "https://arxiv.org/pdf/2610.13455v1#page=65", "raw_path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for url, path in images.items()]
    corpus.write_markdown(source_item, BookMarkdown(full_path, corpus, targets, locations, images, whole=True).convert(str(copy.deepcopy(article))))
    contents = ["# Book contents", "", "[Book index](README.md) · [Full HTML Markdown](markdown/book/full-book-html.md) · [Full PDF text](markdown/book/full-book-pdf.md)", ""]
    records = []
    for index, chapter in enumerate(chapters):
        identifier, title = headings[index]
        path = chapter_paths[identifier]
        record = {"id": "chapters/" + path.stem, "title": title, "url": BASE_URL + "#" + identifier, "category": "chapters", "retrieved_at": source_item["retrieved_at"],
                  "download_status": "downloaded", "conversion_status": "converted", "conversion_method": "arxiv-html-chapter-with-latex-and-local-figures", "raw_path": source_item["raw_path"], "bytes": source_item["bytes"], "sha256": source_item["sha256"], "notes": ["Derived from the full original HTML; raw source contains the whole book."], "source_section": identifier}
        # write_markdown appends the ID to the category path, so use the file stem here.
        record["id"] = path.stem
        navigation = ["[Contents](../../CONTENTS.md)", "[Full book](../book/full-book-html.md)"]
        if index:
            navigation.append(f"[Previous chapter]({chapter_paths[headings[index - 1][0]].name})")
        if index + 1 < len(chapters):
            navigation.append(f"[Next chapter]({chapter_paths[headings[index + 1][0]].name})")
        body = " · ".join(navigation) + "\n\n" + BookMarkdown(path, corpus, targets, locations, images).convert(str(copy.deepcopy(chapter)))
        corpus.write_markdown(record, body)
        record["id"] = "chapters/" + record["id"]
        records.append(record)
        contents += [f"## [{title}]({path.relative_to(root).as_posix()})", ""]
        for section in chapter.find_all("section", recursive=False):
            heading = section.find(["h2", "h3", "h4", "h5"])
            if heading and section.get("id"):
                contents.append(f"- [{heading.get_text(' ', strip=True)}]({path.relative_to(root).as_posix()}#{section['id']})")
        contents.append("")
    corpus.data["materials"] = [item for item in corpus.data["materials"] if item["category"] != "chapters"] + records
    corpus.data["notes"] = [
        "This archive contains the complete 472-page PDF, full experimental arXiv HTML, and original TeX/figure source archive for version 1, submitted October 9, 2026.",
        "Use CONTENTS.md and the 23 chapter files for reading. The full HTML Markdown also preserves part headings and front matter. HTML math is preserved as LaTeX, and internal references link to local chapter anchors.",
        "The HTML is arXiv's experimental source rendering. The original PDF is the reference for exact layout and for any source-to-HTML differences. The bibliography is included in the book text but linked papers were not downloaded.",
    ]
    if missing:
        source_item["conversion_status"] = "converted_with_limitations"
        source_item["notes"].append("Figure assets remain remote: " + ", ".join(missing))
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
    corpus.finalize()
    (root / "CONTENTS.md").write_text("\n".join(contents), encoding="utf-8")
    # The primary arXiv HTML URL belongs to the whole book; chapter sources use fragments.
    metadata = root / "markdown/metadata/arxiv-record.md"
    text = metadata.read_text(encoding="utf-8")
    text = re.sub(r"\[HTML \(experimental\)\]\([^\n]+?\)", "[HTML (experimental)](../book/full-book-html.md)", text)
    metadata.write_text(text, encoding="utf-8")
    readme = root / "README.md"
    text = readme.read_text(encoding="utf-8")
    text = text.replace("[Manifest](manifest.json)", "[Contents and chapters](CONTENTS.md) · [Manifest](manifest.json)", 1)
    readme.write_text(text, encoding="utf-8")
    coverage = {"expected_pdf_pages": 472, "retrieved_pdf_pages": next(item["page_count"] for item in corpus.data["materials"] if item.get("conversion_method") == "pymupdf-text-by-page"), "expected_html_chapters": len(chapters), "converted_chapters": len(records), "html_math_elements": len(article.select("math")), "html_figure_elements": len(article.select("img")), "unique_local_figure_assets": len(images), "local_image_references": sum(image.get("src") in images for image in article.select("img")), "preserved_svg_figures": svg_count, "missing_figures": missing, "source_paragraphs": len(article.select("p")), "bibliography_recursion": False}
    (root / "coverage.json").write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(coverage, indent=2), flush=True)


if __name__ == "__main__":
    main()
