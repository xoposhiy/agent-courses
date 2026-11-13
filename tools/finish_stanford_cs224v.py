"""Complete CS224V homework inputs and one-level project background sources."""

import base64
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, unquote, urldefrag, urlparse, urlunparse
import zipfile

from bs4 import BeautifulSoup
import fitz
from markdownify import markdownify
import requests

from corpus import Corpus, code_block, map_prose, slug
from collect_stanford_cs224v import BASE, DOC_ID, DOC_URL, finish, reuse_pilot_pdf


def update_markdown(corpus, item, content):
    saved_id = item["id"]
    if item.get("markdown_path"):
        item["id"] = Path(item["markdown_path"]).relative_to(Path("markdown") / item["category"]).with_suffix("").as_posix()
    corpus.write_markdown(item, content)
    item["id"] = saved_id


def add_snapshot(corpus, url, title, category, name, body, extension, method, content):
    existing = next((item for item in corpus.data["materials"] if item["url"] == url and item.get("markdown_path")), None)
    if existing:
        return existing
    path = corpus.root / "raw" / category / (name + extension)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    item = {"id": name, "title": title, "url": url, "category": category,
            "retrieved_at": datetime.now(timezone.utc).isoformat(), "raw_path": path.relative_to(corpus.root).as_posix(),
            "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body), "download_status": "downloaded",
            "conversion_status": "converted", "conversion_method": method, "notes": []}
    corpus.data["materials"].append(item)
    update_markdown(corpus, item, content(item) if callable(content) else content)
    corpus.save()
    return item


def homework_notebooks(corpus):
    attempts = json.loads((corpus.root / "notebook-attempts.json").read_text(encoding="utf-8"))
    names = {"1gl9cYgOLZvKMaMTMo_GRrNomOPspjair": "hw1-rare-disease-diagnosis", "1imjDe4sDvjtLW8tFz12nNCPWV0TDk28C": "hw2-react-aos", "1YwmG0Nn9_XUiMmJltLnC4zjzzvcJHBwz": "hw2-satir-verdict"}
    for attempt in attempts:
        file_id = attempt["file_id"]
        source = "https://colab.research.google.com/drive/" + file_id
        if any(source == item["url"] for item in corpus.data["materials"]):
            continue
        binary = (corpus.root / attempt["raw_path"]).read_bytes()
        if attempt["valid_notebook"]:
            notebook = json.loads(binary)
            item = add_snapshot(corpus, source, names[file_id], "notebooks", names[file_id], binary, ".ipynb", "notebook-cells-and-text-outputs", lambda item: corpus.notebook_content(item, notebook))
            item["cell_count"] = len(notebook["cells"])
            item["download_url"] = attempt["download_url"]
            item["aliases"] = [source + "?usp=sharing", source + "?authuser=1"]
        else:
            item = corpus.record_gap(source, "Homework 1 original Colab notebook", "notebooks", "Connected Drive metadata returned 404 and the public raw-download request redirected to Google Drive Sign-in. A public teaching-repository copy is checked separately.", "requires_login")
            item.update(raw_path=attempt["raw_path"], bytes=len(binary), sha256=hashlib.sha256(binary).hexdigest(), http_status=attempt["http_status"], aliases=[source + "?authuser=1"])
    corpus.save()


def import_bundle(corpus):
    file_id = "1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z"
    source_url = "https://drive.google.com/file/d/" + file_id + "/view"
    if any(item["url"] == source_url and item.get("markdown_path") for item in corpus.data["materials"]):
        return
    response = corpus.request("https://drive.google.com/uc?export=download&id=" + file_id)
    response.raise_for_status()
    if not response.content.startswith(b"PK"):
        raise ValueError("Homework course bundle is not a ZIP")
    path = corpus.root / "raw" / "assignments" / "assignment2-course-bundle.zip"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(response.content)
    parent = {"id": "assignment2-course-bundle", "title": "Homework 2 Colab support files and precomputed inputs", "url": source_url, "category": "assignments",
              "retrieved_at": datetime.now(timezone.utc).isoformat(), "raw_path": path.relative_to(corpus.root).as_posix(), "bytes": len(response.content), "sha256": hashlib.sha256(response.content).hexdigest(),
              "download_status": "downloaded", "conversion_status": "converted", "conversion_method": "course-archive-with-text-files", "notes": ["Public 3958608-byte course ZIP is linked by the homework-2 notebook. Source code and saved inputs are archived without execution; no packages were installed from the bundle."]}
    children, raw_only = [], []
    extracted = path.parent / "assignment2-course-bundle"
    with zipfile.ZipFile(path) as bundle:
        for member in bundle.infolist():
            if member.is_dir():
                continue
            rel = Path(member.filename)
            if ".." in rel.parts or "__MACOSX" in rel.parts or rel.name == ".DS_Store":
                continue
            dest = extracted / rel
            if not dest.resolve().is_relative_to(extracted.resolve()):
                raise ValueError("Unsafe archive member")
            binary = bundle.read(member)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(binary)
            try:
                text = binary.decode("utf-8")
            except UnicodeDecodeError:
                raw_only.append(dest)
                continue
            if rel.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".woff", ".woff2", ".ttf", ".pyc"):
                raw_only.append(dest)
                continue
            child = {"id": "assignment2-course-bundle/" + rel.as_posix().replace(".", "-"), "title": "Homework 2 bundle: " + rel.as_posix(), "url": source_url + "#archive-member=" + quote(rel.as_posix()),
                     "container_url": source_url, "archive_member": rel.as_posix(), "category": "assignments", "retrieved_at": parent["retrieved_at"], "raw_path": dest.relative_to(corpus.root).as_posix(),
                     "bytes": len(binary), "sha256": hashlib.sha256(binary).hexdigest(), "download_status": "downloaded", "conversion_status": "converted", "notes": []}
            if rel.suffix == ".ipynb":
                text = corpus.notebook_content(child, json.loads(text))
                child["conversion_method"] = "notebook-cells-and-text-outputs"
            elif rel.suffix in (".md", ".mdx"):
                child["conversion_method"] = "source-markdown"
            elif rel.suffix in (".html", ".htm"):
                page = BeautifulSoup(text, "html.parser")
                for element in page.select("script, style, nav, footer"):
                    element.decompose()
                text = markdownify(str(page.select_one("main") or page.body or page), heading_style="ATX")
                child["conversion_method"] = "html-to-markdown"
            else:
                text = code_block(text, "python" if rel.suffix == ".py" else rel.suffix.lstrip(".") or "text")
                child["conversion_method"] = "source-code-fence"
            corpus.write_markdown(child, text)
            children.append(child)
    by_raw = {str((corpus.root / item["raw_path"]).resolve()): corpus.root / item["markdown_path"] for item in children}
    for child in children:
        converted, raw = corpus.root / child["markdown_path"], corpus.root / child["raw_path"]
        header, body = converted.read_text(encoding="utf-8").split("\n\nRetrieved:", 1)
        def repair(match):
            label, url = match.groups()
            if urlparse(url).scheme or url.startswith("#"):
                return match.group(0)
            target = (raw.parent / unquote(urldefrag(url)[0])).resolve()
            if not target.exists():
                return match.group(0)
            dest = by_raw.get(str(target), target)
            return f"[{label}]({os.path.relpath(dest, converted.parent).replace(chr(92), '/')})"
        converted.write_text(header + "\n\nRetrieved:" + map_prose(body, lambda line: re.sub(r"(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)", repair, line)), encoding="utf-8")
    body = "## Converted contents\n\n" + "\n".join(f"- [{item['archive_member']}]({os.path.relpath(corpus.root / item['markdown_path'], corpus.root / 'markdown' / 'assignments').replace(chr(92), '/')})" for item in children)
    if raw_only:
        body += "\n\n## Original assets\n\n" + "\n".join(f"- [{file.name}]({os.path.relpath(file, corpus.root / 'markdown' / 'assignments').replace(chr(92), '/')})" for file in raw_only)
    parent["file_count"] = len(children) + len(raw_only)
    parent["raw_only_files"] = [file.relative_to(corpus.root).as_posix() for file in raw_only]
    corpus.write_markdown(parent, body)
    corpus.data["materials"].extend(children + [parent])
    corpus.save()


def project_sources(corpus):
    links = json.loads((corpus.root / "project-links.json").read_text(encoding="utf-8"))
    excluded = []
    for original_url in links:
        url = original_url.split("?utm_source=", 1)[0]
        parsed = urlparse(url)
        if parsed.netloc in ("arxiv.org", "www.arxiv.org") and parsed.path in ("", "/"):
            excluded.append({"url": original_url, "reason": "Generic arXiv index"})
            continue
        if DOC_ID in url:
            excluded.append({"url": original_url, "reason": "Internal project-document navigation"})
            continue
        known = next((item for item in corpus.data["materials"] if url in [item["url"], *item.get("aliases", [])]), None)
        if known:
            known.setdefault("linked_from", []).append(DOC_URL)
            if original_url != url:
                known.setdefault("aliases", []).append(original_url)
            continue
        print("Project reference", url, flush=True)
        if "arxiv.org/abs/" in url:
            paper_id = parsed.path.rsplit("/", 1)[-1]
            name = "arxiv-" + paper_id
            reused = reuse_pilot_pdf(corpus, "https://arxiv.org/pdf/" + paper_id, name)
            item = corpus.add("https://arxiv.org/pdf/" + paper_id, "Project background: arXiv " + paper_id, "readings", name, expected="pdf")
            item["aliases"] = [url, original_url]
            if reused:
                item["reused_snapshot"] = reused
        elif parsed.netloc == "github.com":
            if parsed.path.strip("/") == "harbor-framework/terminal-bench-science":
                item = corpus.add("https://raw.githubusercontent.com/harbor-framework/terminal-bench-science/main/README.md", "Terminal-Bench Science: project background README", "project-references", "terminal-bench-science-readme")
                item["aliases"] = [url, original_url]
                item["notes"].append("The linked external benchmark repository has about 1.2 GB of history/data. The assigned README and repository link are retained at one level; benchmark task datasets and execution environments are not course teaching files and are not recursively mirrored.")
                corpus.data["notes"].append(item["notes"][-1])
            else:
                item = corpus.add_repo(url, "Project code: " + parsed.path.strip("/"))
                item["aliases"] = [original_url]
        elif parsed.netloc == "drive.google.com":
            file_id = parsed.path.split("/d/", 1)[-1].split("/", 1)[0]
            if file_id == "1wtyjSiZ6lNN7ffCZSX8e1wsKMdDAQpv0":
                item = corpus.add("https://drive.google.com/uc?export=download&id=" + file_id, "General Coding Agents vs Custom SOTA Agents", "project-references", "general-coding-agents-vs-custom", expected="pdf")
                item["aliases"] = [url, original_url]
            else:
                item = corpus.record_gap(url, "Project background Drive document " + file_id, "project-references", "Connected Drive metadata returned 404; the linked document is not accessible to the connected account. The public source URL remains in the project proposals.", "requires_login")
                item["aliases"] = [url, original_url, url + "?usp=sharing"]
        elif parsed.netloc == "aclanthology.org":
            identifier = parsed.path.strip("/")
            item = corpus.add("https://aclanthology.org/" + identifier + ".pdf", "Project background: " + identifier, "readings", "acl-" + identifier, expected="pdf")
            item["aliases"] = [url, original_url]
        elif parsed.path.endswith(".pdf"):
            item = corpus.add(url, "Project background: " + parsed.path.rsplit("/", 1)[-1], "readings", slug(Path(parsed.path).stem), expected="pdf")
        else:
            item = corpus.add(url, "Project background: " + parsed.netloc + parsed.path, "project-references", slug(parsed.netloc + parsed.path))
        item.setdefault("linked_from", []).append(DOC_URL)
        item.setdefault("reading_requirement", "project-background")
        corpus.save()
    (corpus.root / "project-coverage.json").write_text(json.dumps({"discovered_links": len(links), "excluded_links": excluded, "scope": "One level of linked project background and project starting-code repositories. Generic index/self-navigation links excluded."}, indent=2), encoding="utf-8")


def recover_readings(corpus):
    for failed_url, paper_id, title in [
        ("https://openreview.net/pdf?id=EIc3yin1Eo", "2604.06474", "DataSTORM: Deep Research on Large-Scale Databases using Exploratory Data Analysis and Data Storytelling"),
        ("https://oval.cs.stanford.edu/local-papers/semnani-local.pdf", "2305.14292", "WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia"),
    ]:
        item = corpus.add("https://arxiv.org/pdf/" + paper_id, title, "readings", "arxiv-" + paper_id, expected="pdf")
        item.setdefault("aliases", []).extend([failed_url, "https://arxiv.org/abs/" + paper_id])
        original = next(record for record in corpus.data["materials"] if record["url"] == failed_url)
        if "/openreview.net/" in failed_url:
            item["aliases"].append(failed_url.replace("/pdf?", "/forum?"))
        item["reading_requirement"] = original["reading_requirement"]
        item["notes"].append("Recovered from the author/project-document linked arXiv source. The failed original URL remains separately recorded.")
        original["recovered_by"] = item["markdown_path"]
        corpus.save()


def normalize_inventory(corpus):
    path = corpus.root / "reading-inventory.json"
    inventory = json.loads(path.read_text(encoding="utf-8"))
    mandatory_urls = {
        "https://arxiv.org/abs/2408.08435", "https://arxiv.org/abs/2408.15232", "https://arxiv.org/abs/2407.05674", "https://arxiv.org/abs/2604.22294",
        "https://doi.org/10.1145/3397271.3401075", "https://openreview.net/forum?id=EIc3yin1Eo", "https://doi.org/10.18653/v1/2024.findings-naacl.283",
        "https://doi.org/10.18653/v1/2024.naacl-long.347", "https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf",
        "https://arxiv.org/abs/2201.11903", "https://arxiv.org/abs/2609.03366", "https://arxiv.org/abs/2604.08849", "https://arxiv.org/abs/2407.11417",
    }
    for entry in inventory["readings"]:
        entry["reading_requirement"] = "mandatory" if entry["url"] in mandatory_urls else "recommended"
        if "Mcpverse:" in entry["title"]:
            entry["citation"] = "Fei Lei, Yibo Yang, Wenxiu Sun, and Dahua Lin. 2025. " + entry["citation"]
        for record in corpus.data["materials"]:
            if entry["url"] in [record["url"], *record.get("aliases", [])]:
                record["reading_requirement"] = entry["reading_requirement"]
    inventory["unresolved_citations"] = [entry for entry in inventory["unresolved_citations"] if not entry["citation"].startswith("Fei Lei,")]
    inventory["mandatory_readings"] = len(mandatory_urls)
    path.write_text(json.dumps(inventory, indent=2, ensure_ascii=False), encoding="utf-8")


def extract_project_image(corpus):
    item = next(record for record in corpus.data["materials"] if record.get("category") == "projects")
    path = corpus.root / item["markdown_path"]
    content = path.read_text(encoding="utf-8")
    def replace(match):
        binary = base64.b64decode(match[1])
        asset = corpus.root / "raw" / "assets" / "project-proposals-diagram.png"
        asset.parent.mkdir(parents=True, exist_ok=True)
        asset.write_bytes(binary)
        item.setdefault("assets", []).append({"raw_path": asset.relative_to(corpus.root).as_posix(), "bytes": len(binary), "sha256": hashlib.sha256(binary).hexdigest(), "source": "Embedded image in the original Markdown export"})
        return os.path.relpath(asset, path.parent).replace("\\", "/")
    content = re.sub(r"data:image/png;base64,([A-Za-z0-9+/=]+)", replace, content)
    path.write_text(content, encoding="utf-8")


def main():
    corpus = Corpus("courses/stanford-cs224v", "stanford-cs224v", "Stanford CS224V: Agentic AI", BASE)
    recover_readings(corpus)
    normalize_inventory(corpus)
    homework_notebooks(corpus)
    print("Teaching repository", flush=True)
    repo = corpus.add_repo("https://github.com/stanford-oval/cs224vf26-assignment1-public", "Homework 1 public teaching repository", "cs224vf26-assignment1-public")
    original_notebook = next(record for record in corpus.data["materials"] if record["url"] == "https://colab.research.google.com/drive/1gl9cYgOLZvKMaMTMo_GRrNomOPspjair")
    replacement = next((record for record in corpus.data["materials"] if record.get("raw_path", "").endswith("/rare_disease_diagnosis.ipynb")), None)
    if replacement:
        original_notebook["recovered_by"] = replacement["markdown_path"]
        replacement.setdefault("aliases", []).extend(original_notebook["aliases"] + [original_notebook["url"]])
        replacement["notes"].append("The original Colab URL requires access; this complete notebook is recovered from the course's public teaching repository, named by the homework-2 notebook.")
    corpus.save()
    print("Homework support bundle", flush=True)
    import_bundle(corpus)
    project_sources(corpus)
    extract_project_image(corpus)
    corpus.data["notes"].append("The original Homework 1 Colab URL is restricted, but rare_disease_diagnosis.ipynb and all public precomputed runs were recovered from the course's public teaching repository. Homework 2 notebooks and their linked support ZIP are included. The assignment-disease spreadsheet requires separate access if not publicly exported.")
    discovered = {entry["url"]: entry for entry in json.loads((corpus.root / "discovered-links.json").read_text(encoding="utf-8"))}
    excluded = json.loads((corpus.root / "coverage.json").read_text(encoding="utf-8"))["excluded_links"]
    finish(corpus, discovered, excluded)


if __name__ == "__main__":
    main()
