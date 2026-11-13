"""Inspect course-linked notebooks and project references without executing code."""

import json
from pathlib import Path
import re

from bs4 import BeautifulSoup
import requests


root = Path("courses/stanford-cs224v")
project = next((root / "raw" / "projects").glob("project-proposals.*")).read_text(encoding="utf-8")
urls = list(dict.fromkeys(re.findall(r"https?://[^\s<>\)\]\"]+", project)))
(root / "project-links.json").write_text(json.dumps(urls, indent=2), encoding="utf-8")
print("Project document links:", len(urls))
print("\n".join(url for url in urls if any(term in url for term in ("github", "arxiv", "datastorm", "DataSTORM"))))
for url in ["https://george1459.github.io/", "https://cs.stanford.edu/~yuchengj/publications/"]:
    soup = BeautifulSoup(requests.get(url, timeout=30).content, "html.parser")
    for anchor in soup.select("a[href]"):
        if "datastorm" in (anchor.get_text(" ", strip=True) + anchor["href"]).lower():
            print("DataSTORM link:", anchor.get_text(" ", strip=True), anchor["href"])
            print("Context:", str(anchor.parent)[:2000])
records = []
for file_id in ["1gl9cYgOLZvKMaMTMo_GRrNomOPspjair", "1imjDe4sDvjtLW8tFz12nNCPWV0TDk28C", "1YwmG0Nn9_XUiMmJltLnC4zjzzvcJHBwz"]:
    url = "https://drive.google.com/uc?export=download&id=" + file_id
    response = requests.get(url, timeout=40)
    try:
        notebook = response.json()
        valid = isinstance(notebook, dict) and isinstance(notebook.get("cells"), list)
    except ValueError:
        valid = False
    path = root / "raw" / "notebooks" / (file_id + (".ipynb" if valid else ".html"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(response.content)
    record = {"file_id": file_id, "download_url": url, "http_status": response.status_code, "raw_path": path.relative_to(root).as_posix(), "valid_notebook": valid, "bytes": len(response.content)}
    records.append(record)
    print("Notebook attempt:", record)
(root / "notebook-attempts.json").write_text(json.dumps(records, indent=2), encoding="utf-8")
