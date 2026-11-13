"""Recover advertised Discourse attachments from their verified public CDN originals."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

import fitz
from bs4 import BeautifulSoup

from corpus import Corpus


def decoded_sha1(code):
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = 0
    for character in code:
        number = number * 62 + alphabet.index(character)
    return format(number, "040x")


def main():
    root = Path("courses/dlai-agentic-evals")
    corpus = Corpus(root, "dlai-agentic-evals", "DeepLearning.AI / Arize: Evaluating and Improving Agentic Applications", "https://www.deeplearning.ai/courses/evaluating-and-improving-agentic-applications")
    coverage = json.loads((root / "coverage.json").read_text(encoding="utf-8"))
    recovery = []
    links = set()
    for attachment in coverage["attachments"]:
        code = urlparse(attachment["url"]).path.rsplit("/", 1)[-1].removesuffix(".pdf")
        expected = decoded_sha1(code)
        url = f"https://global.discourse-cdn.com/dlai/original/3X/{expected[0]}/{expected[1]}/{expected}.pdf"
        item = corpus.add(url, attachment["title"], "slides", f"module-{attachment['module']}", expected="pdf")
        item["aliases"] = [attachment["url"]]
        item["discovered_from"] = "https://community.deeplearning.ai/t/evals-lecture-notes/896118"
        item["expected_source_sha1"] = expected
        actual = hashlib.sha1((root / item["raw_path"]).read_bytes()).hexdigest() if item.get("raw_path") else None
        item["source_sha1_matches"] = actual == expected
        if actual != expected:
            raise ValueError("Recovered file does not match the published attachment SHA-1")
        item["notes"].append("Recovered from the public CDN original after the published short attachment URL returned 404. The file SHA-1 matches the base62-decoded short-link hash exactly.")
        for attempt in corpus.data["materials"]:
            if attempt["url"] == attachment["url"]:
                attempt.update(category="access-attempts", id=f"access-attempts/module-{attachment['module']}-short-url", title=attachment["title"] + ": original short-URL attempt", recovered_by=item["markdown_path"])
                attempt["notes"].append("Full slide deck recovered from the verified public CDN original: " + item["markdown_path"])
        document = fitz.open(root / item["raw_path"])
        for page in document:
            links.update(link["uri"] for link in page.get_links() if link.get("uri"))
        recovery.append({"module": attachment["module"], "advertised_url": attachment["url"], "recovered_url": url, "expected_sha1": expected, "actual_sha1": actual, "sha1_matches": actual == expected, "pages": item["page_count"], "first_page_text": document[0].get_text().strip()[:700]})
        print("Recovered module", attachment["module"], item["page_count"], "pages", flush=True)
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
    corpus.data["notes"] = [
        "All five advertised module PDFs were recovered from the forum's public CDN originals. The original short attachment URLs return 404, but every recovered PDF has the SHA-1 encoded in its advertised short link. Initial failed responses are retained separately for provenance.",
        "The official lecture-notes post warns that the slide PDFs are not maintained and can omit topics or contain errors. Lecture videos are updated separately. Preserve this warning when using the slides to design teaching material.",
        "PDF Markdown is full page-by-page text extraction. The original PDFs preserve diagrams, tables, and exact mathematical notation.",
        "Only public sources were fetched; no course enrollment, payment, account changes, or downloaded code execution was performed.",
    ]
    corpus.finalize()
    coverage.update(recovered_modules=len(recovery), recovered_pdf_pages=sum(item["pages"] for item in recovery), verified_attachment_sha1=sum(item["sha1_matches"] for item in recovery), pdf_link_targets=sorted(links))
    (root / "coverage.json").write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")
    (root / "recovery.json").write_text(json.dumps({"method": "Discourse base62 SHA-1 decoded to a public 3X CDN original, then verified against downloaded file bytes", "source_topic": "https://community.deeplearning.ai/t/evals-lecture-notes/896118", "encoding_reference": "https://meta.discourse.org/t/converting-short-upload-urls-to-full-urls/131760", "files": recovery}, indent=2) + "\n", encoding="utf-8")
    print("Slide link targets", sorted(links), flush=True)


if __name__ == "__main__":
    main()
