"""Reconcile CS224V course, homework, and project links against the saved manifest."""

import hashlib
import json
from pathlib import Path

import fitz

from corpus import Corpus
from collect_stanford_cs224v import BASE


def main():
    corpus = Corpus("courses/stanford-cs224v", "stanford-cs224v", "Stanford CS224V: Agentic AI", BASE)
    response_path = corpus.root / "raw" / "project-references" / "drive-project-document-access-response.html"
    restricted = next(item for item in corpus.data["materials"] if item["url"] == "https://drive.google.com/file/d/1--ypH_6j1oywlikk04ZTFynJxMrHxG7-/view")
    binary = response_path.read_bytes()
    restricted.update(raw_path=response_path.relative_to(corpus.root).as_posix(), bytes=len(binary), sha256=hashlib.sha256(binary).hexdigest(), http_status=200)
    note = "The public raw-download endpoint was checked as well and returned Google Drive Sign-in. The saved response is an access page, not project content."
    if note not in restricted["notes"]:
        restricted["notes"].append(note)
    records = corpus.data["materials"]
    def resolve(url):
        candidates = [item for item in records if url in [item["url"], *item.get("aliases", [])]]
        preferred = next((item for item in candidates if item.get("markdown_path")), next(iter(candidates), None))
        if not preferred:
            return None
        return {"url": url, "material_id": preferred["id"], "download_status": preferred["download_status"], "conversion_status": preferred["conversion_status"], "markdown_path": preferred.get("markdown_path") or preferred.get("recovered_by")}
    project = json.loads((corpus.root / "project-coverage.json").read_text(encoding="utf-8"))
    excluded = {item["url"] for item in project["excluded_links"]}
    expected = [url for url in json.loads((corpus.root / "project-links.json").read_text(encoding="utf-8")) if url not in excluded]
    project["accounted_links"] = [result for url in expected if (result := resolve(url))]
    project["missing_links"] = [url for url in expected if resolve(url) is None]
    project["accounted_link_count"] = len(project["accounted_links"])
    (corpus.root / "project-coverage.json").write_text(json.dumps(project, indent=2), encoding="utf-8")
    homework_links = []
    for item in records:
        if item["category"] == "assignments" and item.get("raw_path", "").endswith(("cs224v-2026-hw1.pdf", "cs224v-2026-hw2.pdf")):
            document = fitz.open(corpus.root / item["raw_path"])
            homework_links.extend(link["uri"] for page in document for link in page.get_links() if link.get("uri"))
    homework_links = list(dict.fromkeys(homework_links))
    coverage = json.loads((corpus.root / "coverage.json").read_text(encoding="utf-8"))
    coverage["homework_links"] = [result for url in homework_links if (result := resolve(url))]
    coverage["missing_homework_links"] = [url for url in homework_links if resolve(url) is None]
    coverage.update(reading_inventory_path="reading-inventory.json", project_coverage_path="project-coverage.json", source_link_gaps_path="source-link-gaps.json")
    (corpus.root / "coverage.json").write_text(json.dumps(coverage, indent=2), encoding="utf-8")
    for item in records:
        replacements = {"PMID39954218": "PMID 39954218", "PMCIDPMC13346298": "PMCID PMC13346298", "DOI10.1007": "DOI 10.1007", "expected1result": "expected 1 result", "retrieved1result": "retrieved 1 result"}
        item["title"] = item["title"].replace("PMID39954218", "PMID 39954218")
        item["notes"] = [note for note in dict.fromkeys(item.get("notes", []))]
        for old, new in replacements.items():
            item["notes"] = [note.replace(old, new) for note in item["notes"]]
        if item.get("markdown_path") and "pubmed-39954218-europepmc" in item["markdown_path"]:
            path = corpus.root / item["markdown_path"]
            path.write_text(path.read_text(encoding="utf-8").replace("PMID39954218", "PMID 39954218"), encoding="utf-8")
    corpus.write_indexes()
    if project["missing_links"] or coverage["missing_homework_links"]:
        raise ValueError("Source links remain unaccounted for")
    print(json.dumps({"project_links": len(expected), "project_links_accounted": project["accounted_link_count"], "homework_links": len(homework_links), "homework_links_accounted": len(coverage["homework_links"])}, indent=2))


if __name__ == "__main__":
    main()
