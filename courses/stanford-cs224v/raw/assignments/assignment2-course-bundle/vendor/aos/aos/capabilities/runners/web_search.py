#!/usr/bin/env python3
"""Web search, Google Scholar search and page fetching for agents working inside a sandbox.

GRILL's research tasks run in Codex, which has no usable built-in web search through the Gemini
proxy; this script is the replacement, run from the agent's shell:

  python3 web_search.py search "query" [--num 10]     # Google web results (Serper)
  python3 web_search.py search "query" --scholar      # Google Scholar results (Serper)
  python3 web_search.py fetch URL [--max-chars 30000]  # readable text of a page or PDF

Reads SERPER_API_KEY from the environment. Every query and every fetched page is saved under
AOS_SEARCH_LOG_DIR (default: ./searches) so the run keeps its sources inside the workspace, and a
repeated query or fetch is answered from that folder. Standard library only and Python 3.8
compatible, so it runs with whatever python3 the sandbox has.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser

SERPER = os.environ.get("SERPER_ENDPOINT", "https://google.serper.dev").rstrip("/")
LOG_DIR = os.environ.get("AOS_SEARCH_LOG_DIR", "searches")
USER_AGENT = "Mozilla/5.0 (compatible; AOS research agent; +https://github.com/stanford-oval)"
SKIP_TAGS = {"script", "style", "noscript", "nav", "header", "footer", "svg", "iframe", "form"}
BLOCK_TAGS = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "section", "article",
              "table", "blockquote", "pre", "ul", "ol", "dd", "dt", "figcaption", "title"}


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def key_for(*parts):
    return hashlib.sha1("\x1f".join(parts).encode("utf-8")).hexdigest()[:16]


def log_path(*parts):
    path = os.path.join(LOG_DIR, *parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def normalize(item, scholar):
    out = {"title": item.get("title"), "link": item.get("link"), "snippet": item.get("snippet")}
    if scholar:
        out.update({"publication": item.get("publicationInfo"), "year": item.get("year"),
                    "cited_by": item.get("citedBy"), "pdf": item.get("pdfUrl")})
    else:
        out.update({"date": item.get("date"), "position": item.get("position")})
    return {k: v for k, v in out.items() if v not in (None, "")}


def search(query, num=10, scholar=False):
    """Serper results for one query; the full reply is saved and reused for the same query."""
    kind = "scholar" if scholar else "search"
    path = log_path("{}-{}.json".format(kind, key_for(kind, query, str(num))))
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            record = json.load(f)
        record["cached"] = True
        return record
    api_key = os.environ.get("SERPER_API_KEY")
    if not api_key:
        raise SystemExit("SERPER_API_KEY is not set, so web search is unavailable")
    body = json.dumps({"q": query, "num": num}).encode("utf-8")
    request = urllib.request.Request(SERPER + "/" + kind, data=body, headers={
        "X-API-KEY": api_key, "Content-Type": "application/json", "User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = json.load(response)
    except urllib.error.HTTPError as exc:
        raise SystemExit("search failed: HTTP {} from Serper ({})".format(exc.code, exc.reason))
    except (urllib.error.URLError, OSError) as exc:
        raise SystemExit("search failed: {}".format(exc))
    record = {"query": query, "kind": kind, "num": num, "fetched_at": now(),
              "results": [normalize(item, scholar) for item in raw.get("organic", [])]}
    box = raw.get("answerBox")
    if box:
        record["answer_box"] = {k: box[k] for k in ("title", "answer", "snippet", "link") if box.get(k)}
    record["raw"] = raw
    with open(path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=1)
    record["cached"] = False
    return record


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip += 1
        if tag == "title":
            self.in_title = True
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self.skip:
            self.skip -= 1
        if tag == "title":
            self.in_title = False
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif not self.skip:
            self.parts.append(data)

    def text(self):
        text = "".join(self.parts)
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r" *\n *", "\n", text)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def html_to_text(raw):
    parser = TextExtractor()
    parser.feed(raw)
    return parser.title.strip(), parser.text()


def pdf_to_text(path):
    if shutil.which("pdftotext"):
        result = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
    try:
        import pypdf  # optional
    except ImportError:
        return None
    return "\n".join((page.extract_text() or "") for page in pypdf.PdfReader(path).pages)


def fetch(url, max_chars=30000):
    """Readable text of a web page or PDF; the original bytes are kept next to the searches."""
    stem = key_for("page", url)
    meta_path = log_path("pages", stem + ".json")
    if os.path.isfile(meta_path):
        with open(meta_path, encoding="utf-8") as f:
            meta = json.load(f)
        with open(meta["text_file"], encoding="utf-8") as f:
            text = f.read()
        return meta, text, True
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            content_type = (response.headers.get("Content-Type") or "").lower()
            data = response.read(50 * 1024 * 1024)
    except urllib.error.HTTPError as exc:
        raise SystemExit("fetch failed: HTTP {} for {}".format(exc.code, url))
    except (urllib.error.URLError, OSError, ValueError) as exc:
        raise SystemExit("fetch failed: {} ({})".format(url, exc))
    is_pdf = "pdf" in content_type or data[:5] == b"%PDF-" or url.lower().split("?")[0].endswith(".pdf")
    raw_path = log_path("pages", stem + (".pdf" if is_pdf else ".html"))
    with open(raw_path, "wb") as f:
        f.write(data)
    title = ""
    if is_pdf:
        text = pdf_to_text(raw_path)
        if text is None:
            text = "[PDF saved to {}; no PDF text extractor (pdftotext or pypdf) is available]".format(raw_path)
    else:
        title, text = html_to_text(data.decode("utf-8", errors="replace"))
    text_path = log_path("pages", stem + ".txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)
    meta = {"url": url, "title": title, "content_type": content_type, "bytes": len(data), "chars": len(text),
            "fetched_at": now(), "raw_file": raw_path, "text_file": text_path}
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=1)
    return meta, text, False


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    s = sub.add_parser("search", help="web or scholar search")
    s.add_argument("query")
    s.add_argument("--num", type=int, default=10, help="results wanted (max 20)")
    s.add_argument("--scholar", action="store_true", help="Google Scholar instead of the web")
    f = sub.add_parser("fetch", help="readable text of a page or PDF")
    f.add_argument("url")
    f.add_argument("--max-chars", type=int, default=30000)
    args = ap.parse_args(argv)
    if args.command == "search":
        record = search(args.query, num=max(1, min(args.num, 20)), scholar=args.scholar)
        shown = {k: record[k] for k in ("query", "kind", "cached", "results") if k in record}
        if record.get("answer_box"):
            shown["answer_box"] = record["answer_box"]
        print(json.dumps(shown, indent=1, ensure_ascii=False))
    else:
        meta, text, cached = fetch(args.url)
        clipped = text[:args.max_chars]
        print("# {}\n# {} | {} chars{} | text saved at {}{}\n".format(
            meta.get("title") or "(no title)", meta["url"], meta["chars"],
            " (showing the first {})".format(args.max_chars) if len(text) > args.max_chars else "",
            meta["text_file"], " | cached" if cached else ""))
        print(clipped)
    return 0


if __name__ == "__main__":
    sys.exit(main())
