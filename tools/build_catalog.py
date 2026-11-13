"""Build a common entry point and a machine-readable catalog from course manifests."""

from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]


def source_key(url):
    parsed = urlsplit(url)
    host = parsed.netloc.lower().removeprefix("www.")
    if host in ("arxiv.org", "export.arxiv.org"):
        match = re.match(r"/(?:abs|pdf|html)/(.+?)(?:\.pdf)?$", parsed.path)
        if match:
            return "https://arxiv.org/abs/" + re.sub(r"v\d+$", "", match.group(1))
    return urlunsplit((parsed.scheme, host, parsed.path.rstrip("/"), parsed.query, ""))


def main():
    plan = json.loads((ROOT / "collection-plan.json").read_text(encoding="utf-8-sig"))
    datasets = []
    materials = []
    shared = defaultdict(list)
    for source in plan["sources"]:
        folder = ROOT / source["folder"]
        manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8-sig"))
        records = manifest["materials"]
        index_path = folder / "README.md"
        index_text = index_path.read_text(encoding="utf-8")
        if "[Corpus index](../../README.md)" not in index_text:
            heading, separator, body = index_text.partition("\n")
            navigation = "\n[Corpus index](../../README.md) · [Shared readings](../../SHARED-READINGS.md)\n"
            index_path.write_text(heading + separator + navigation + body, encoding="utf-8")
        counts = Counter(record.get("download_status", "unknown") for record in records)
        dataset = {
            **source,
            "retrieved_at": manifest["retrieved_at"],
            "index_path": source["folder"] + "/README.md",
            "manifest_path": source["folder"] + "/manifest.json",
            "gaps_path": source["folder"] + "/GAPS.md",
            "materials": len(records),
            "downloaded": counts["downloaded"],
            "markdown_files": sum(bool(record.get("markdown_path")) for record in records),
            "gaps": sum(record.get("conversion_status") in ("failed", "not_available") for record in records),
            "download_statuses": dict(counts),
            "categories": dict(Counter(record["category"] for record in records)),
        }
        datasets.append(dataset)
        for record in records:
            normalized = {**record, "source_id": source["id"]}
            for field in ("raw_path", "markdown_path"):
                if record.get(field):
                    normalized[field] = source["folder"] + "/" + record[field]
            materials.append(normalized)
            if record.get("markdown_path") and record.get("category") != "metadata":
                shared[source_key(record["url"])].append(normalized)
    duplicate_groups = []
    for url, group in sorted(shared.items()):
        if len({item["source_id"] for item in group}) > 1:
            duplicate_groups.append({"source_url": url, "materials": [
                {key: item[key] for key in ("source_id", "id", "title", "markdown_path")}
                for item in group
            ]})
    catalog = {
        "schema_version": "1.0",
        "built_at": datetime.now(timezone.utc).isoformat(),
        "purpose": plan["purpose"],
        "datasets": datasets,
        "materials": materials,
        "shared_materials": duplicate_groups,
    }
    (ROOT / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# AI Agent Course Corpus", "",
        "This corpus contains the seven selected courses and one book from the source list. Start with a course index, follow the local Markdown links, and consult the raw source when a conversion has limits.", "",
        "[Collection rules](COLLECTION.md) · [Machine-readable catalog](catalog.json) · [Shared readings](SHARED-READINGS.md) · [Validation results](validation-report.json) · [Original source list](resources.md)", "",
        "## Sources", "",
        "| Source | Markdown files | Downloaded records | Recorded gaps |",
        "| --- | ---: | ---: | ---: |",
    ]
    for dataset in datasets:
        label = dataset.get("institution", "Book") + ": " + dataset["title"]
        number = str(dataset["resource_number"]) + ". " if dataset.get("resource_number") else ""
        lines.append(f"| [{number}{label}]({dataset['index_path']}) | {dataset['markdown_files']} | {dataset['downloaded']} | [{dataset['gaps']}]({dataset['gaps_path']}) |")
    lines += [
        "", "## Read the corpus", "",
        "Counts refer to files and manifest records. Repository files and saved experiment traces count separately; these are not lesson counts.", "",
        "Gap counts include failed original URLs with recovered copies. Read the source's gap report to distinguish unavailable content from a failed request that has an alternative.", "",
        "- Each source has `README.md`, `manifest.json`, `GAPS.md`, `raw/`, and `markdown/`.",
        "- Markdown files contain the full converted source content. Generated indexes and gap reports are labeled separately.",
        "- Each converted file links to its source, raw file, and course index. Links to other archived materials point to local files when a matching source was found.",
        "- PDF extraction keeps page numbers. Diagrams, complex tables, and equations can require the original PDF. Check conversion notes in the manifest.",
        "- Repository archives preserve source files. Notebook Markdown contains cells and available saved text outputs. Downloaded code was not executed.",
        "- Gaps include access restrictions, failed requests, missing transcripts, and unpublished materials. A saved error response is evidence of a failed request, not course content.",
        "- Large video files, model weights, installed dependencies, private course systems, and recursive copies of external sites are outside this archive. Video links and retrieval gaps remain documented.",
        "", "## Search and verify", "",
        "Search the clean text with `rg -n -i 'search term' courses -g '*.md'`. Use `catalog.json` to filter by `source_id`, `category`, `download_status`, or `conversion_status`.", "",
        "Run `python tools/validate_corpus.py --output validation-report.json` to check local links, recorded files, hashes, and PDF page coverage. Run `python tools/build_catalog.py` after a source manifest changes.", "",
        "The collection reflects the dates recorded in each manifest. Fall 2026 courses were still in progress during collection. Preserve the authors' attribution and source license notices when reusing materials.", "",
    ]
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    lines = ["# Shared Readings", "", "[Corpus index](README.md)", "",
             "These documents appear in more than one source. The links connect the local copies and keep each course's context. arXiv records are grouped by work; other documents are grouped by source URL. Different versions can have different text.", ""]
    names = {dataset["id"]: dataset.get("institution", "Book") + ": " + dataset["title"] for dataset in datasets}
    for group in duplicate_groups:
        title = group["materials"][0]["title"]
        lines += [f"## {title}", "", f"Source: [{group['source_url']}]({group['source_url']})", ""]
        lines += [f"- [{names[item['source_id']]}]({item['markdown_path']})" for item in group["materials"]]
        lines.append("")
    if not duplicate_groups:
        lines += ["No exact source URL is shared by converted documents in the current manifests.", ""]
    (ROOT / "SHARED-READINGS.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"datasets": len(datasets), "materials": len(materials), "shared_readings": len(duplicate_groups)}))


if __name__ == "__main__":
    main()
