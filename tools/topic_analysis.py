"""Build course topic reports from reviewed concepts and local source evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis"
ORDER = [
    "stanford-cs329z", "columbia-coms4995", "cmu-11768",
    "langchain-deep-agents", "stanford-cs224v", "dlai-agentic-evals",
    "colorado-csci7000", "agentic-large-language-models",
]


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def save_curation(slug, summary, limits, definitions, sources):
    """Save compact, manually reviewed input as structured data."""
    concepts = []
    for line in definitions.strip().splitlines():
        if not line.strip():
            continue
        key, label, kind, definition, aliases, parent = line.split("|")
        concepts.append(dict(id=key, label=label, kind=kind, definition=definition,
                             aliases=[a.strip() for a in aliases.split(";") if a.strip()],
                             parent_id=parent or None))
    coverage = []
    path = None
    for line in sources.strip().splitlines():
        if not line.strip():
            continue
        if line.startswith("@ "):
            path = line[2:].strip()
            continue
        fields = line.split("|")
        key, needle = fields[:2]
        coverage.append(dict(concept_id=key, source=path, needle=needle,
                             coverage=fields[2] if len(fields) > 2 else "taught"))
    write_json(OUT / "curation" / f"{slug}.json", dict(
        source_id=slug, summary=summary, limitations=limits,
        new_concepts=concepts, coverage=coverage))


def resolve_evidence(slug, record):
    path = ROOT / "courses" / slug / record["source"]
    lines = path.read_text(encoding="utf-8").splitlines()
    needle = record["needle"].casefold()
    matches = [i for i, line in enumerate(lines) if needle in line.casefold()]
    if not matches:
        raise ValueError(f"Missing evidence: {slug}: {record}")
    # Skip the generated conversion title and provenance when content matches exist.
    index = next((i for i in matches if i >= 8), matches[0])
    page = None
    for line in lines[:index + 1]:
        match = re.fullmatch(r"## Page (\d+)", line)
        if match:
            page = int(match[1])
    manifest = json.loads((ROOT / "courses" / slug / "manifest.json").read_text(encoding="utf-8"))
    material = next(m for m in manifest["materials"] if m.get("markdown_path") == record["source"])
    assert material["download_status"] == "downloaded", material
    return dict(source_path=path.relative_to(ROOT).as_posix(), line=index + 1,
                page=page, excerpt=lines[index].strip(), material_id=material["id"],
                category=material["category"], source_url=material["url"],
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def normalized_name(value):
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def validate_dictionary(concepts):
    names = {}
    for key, concept in concepts.items():
        assert concept["id"] == key
        if concept["parent_id"]:
            assert concept["parent_id"] in concepts, (key, concept["parent_id"])
        for name in [concept["label"], *concept["aliases"]]:
            normal = normalized_name(name)
            assert normal not in names or names[normal] == key, (name, key, names.get(normal))
            names[normal] = key
        ancestors = {key}
        parent = concept["parent_id"]
        while parent:
            assert parent not in ancestors, (key, parent)
            ancestors.add(parent)
            parent = concepts[parent]["parent_id"]


def apply_course(slug):
    position = ORDER.index(slug)
    previous = OUT / "checkpoints" / f"{position:02d}.json"
    state = json.loads(previous.read_text(encoding="utf-8")) if position else dict(concepts={}, courses=[])
    assert state["courses"] == ORDER[:position], "Process courses in order."
    curation = json.loads((OUT / "curation" / f"{slug}.json").read_text(encoding="utf-8"))
    added = []
    for concept in curation["new_concepts"]:
        key = concept["id"]
        assert key not in state["concepts"], key
        concept["introduced_in"] = slug
        state["concepts"][key] = concept
        added.append(key)
    validate_dictionary(state["concepts"])
    entries = {}
    for record in curation["coverage"]:
        key = record["concept_id"]
        assert key in state["concepts"], key
        assert record["coverage"] in ("taught", "assigned", "planned")
        entry = entries.setdefault(key, dict(concept_id=key, coverage=record["coverage"], evidence=[]))
        assert entry["coverage"] == record["coverage"], (slug, key)
        evidence = resolve_evidence(slug, record)
        if evidence not in entry["evidence"]:
            entry["evidence"].append(evidence)
    state["courses"].append(slug)
    write_json(OUT / "courses" / f"{slug}.json", dict(
        source_id=slug, summary=curation["summary"], limitations=curation["limitations"],
        new_concept_ids=added, concepts=list(entries.values())))
    write_json(OUT / "checkpoints" / f"{position + 1:02d}.json", state)
    write_json(OUT / "dictionary.json", dict(schema_version="1.0", processed_sources=state["courses"],
                                             concepts=list(state["concepts"].values())))
    print(f"Processed {slug}: {len(entries)} concepts; {len(added)} new; dictionary {len(state['concepts'])}.")


def md(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def reconcile():
    """Apply reviewed cross-course corrections after the sequential first pass."""
    rules = json.loads((OUT / "reconciliation.json").read_text(encoding="utf-8"))
    dictionary = json.loads((OUT / "dictionary.json").read_text(encoding="utf-8"))
    assert dictionary["processed_sources"] == ORDER
    concepts = {c["id"]: c for c in dictionary["concepts"]}
    for rule in rules.get("dictionary_updates", []):
        concepts[rule["concept_id"]].update(rule["fields"])
    validate_dictionary(concepts)
    audit = []
    for rule in rules["coverage_updates"]:
        slug, key = rule["source_id"], rule["concept_id"]
        path = OUT / "courses" / f"{slug}.json"
        course = json.loads(path.read_text(encoding="utf-8"))
        course["concepts"] = [e for e in course["concepts"] if e["concept_id"] != key]
        if rule["action"] != "remove":
            assert key in concepts
            evidence = [resolve_evidence(slug, r) for r in rule["evidence"]]
            course["concepts"].append(dict(concept_id=key, coverage=rule["coverage"], evidence=evidence))
        write_json(path, course)
        audit.append({k: v for k, v in rule.items() if k != "evidence"})
    write_json(OUT / "dictionary.json", dictionary)
    write_json(OUT / "reconciliation-audit.json", audit)
    print(f"Applied {len(audit)} coverage updates and {len(rules.get('dictionary_updates', []))} dictionary updates.")


def build_reports():
    dictionary = json.loads((OUT / "dictionary.json").read_text(encoding="utf-8"))
    assert dictionary["processed_sources"] == ORDER
    concepts = {c["id"]: c for c in dictionary["concepts"]}
    validate_dictionary(concepts)
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    datasets = {d["id"]: d for d in catalog["datasets"]}
    courses = [json.loads((OUT / "courses" / f"{s}.json").read_text(encoding="utf-8")) for s in ORDER]
    labels = dict(zip(ORDER, ["S329", "COL", "CMU", "LC", "S224", "EVAL", "CU", "BOOK"]))
    counts = {}
    for key, concept in concepts.items():
        taught, assigned, planned, book, files = [], [], [], [], set()
        for course in courses:
            entry = next((e for e in course["concepts"] if e["concept_id"] == key), None)
            if not entry:
                continue
            slug = course["source_id"]
            if slug == ORDER[-1]:
                book.append(slug)
            else:
                {"taught": taught, "assigned": assigned, "planned": planned}[entry["coverage"]].append(slug)
                if entry["coverage"] != "planned":
                    files.update(e["source_path"] for e in entry["evidence"])
        counts[key] = dict(concept_id=key, concept=concept["label"], kind=concept["kind"],
                           course_count=len(taught) + len(assigned), taught_course_count=len(taught),
                           assigned_course_count=len(assigned), planned_course_count=len(planned),
                           book_present=bool(book), evidence_file_count=len(files),
                           courses=taught + assigned, taught_courses=taught, assigned_courses=assigned,
                           planned_courses=planned)
    ranked = sorted(counts.values(), key=lambda r: (-r["course_count"], -r["taught_course_count"], r["concept"].casefold()))
    write_json(OUT / "frequency.json", dict(unit="distinct course", denominator=7,
        book_in_denominator=False, parent_counts_inferred=False, rows=ranked))
    with (OUT / "frequency.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(ranked[0]))
        writer.writeheader()
        writer.writerows({k: "; ".join(v) if isinstance(v, list) else v for k, v in row.items()} for row in ranked)
    with (OUT / "course-matrix.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["concept_id", "concept", "kind", *ORDER])
        for row in ranked:
            writer.writerow([row["concept_id"], row["concept"], row["kind"], *[
                next((e["coverage"] for e in c["concepts"] if e["concept_id"] == row["concept_id"]), "not evidenced")
                for c in courses]])
    glossary = ["# Shared Concept Dictionary", "", "Canonical names, scope, aliases, and parent concepts. Parent and child concepts remain separate. A child does not automatically add coverage to its parent.", "",
                "Aliases name the same concept. Related terms are examples or associated systems, not synonyms.", "",
                "| ID | Canonical name | Type | Definition | Aliases | Related terms | Parent |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for c in sorted(concepts.values(), key=lambda c: c["label"].casefold()):
        glossary.append("| " + " | ".join(md(v) for v in [c["id"], c["label"], c["kind"], c["definition"], "; ".join(c["aliases"]), "; ".join(c.get("related_terms", [])), c["parent_id"] or ""]) + " |")
    (OUT / "DICTIONARY.md").write_text("\n".join(glossary) + "\n", encoding="utf-8")
    for course in courses:
        slug = course["source_id"]
        lines = [f"# {datasets[slug].get('institution', 'Book')}: {datasets[slug]['title']}", "", course["summary"], "",
                 f"[Archived source](../../courses/{slug}/README.md) · [Shared dictionary](../DICTIONARY.md) · [Summary](../README.md)", "",
                 "## Scope and limits", "", *[f"- {v}" for v in course["limitations"]], "",
                 "## Concepts and evidence", "", "T = explained or implemented in available teaching content; A = assigned reading; P = schedule only. The evidence is a reviewed selection, not a complete list of occurrences.", "",
                 "| Concept | Type | Coverage | Evidence |", "| --- | --- | --- | --- |"]
        for entry in sorted(course["concepts"], key=lambda e: concepts[e["concept_id"]]["label"].casefold()):
            c = concepts[entry["concept_id"]]
            links = []
            for evidence in entry["evidence"]:
                location = f"p. {evidence['page']}" if evidence["page"] else f"line {evidence['line']}"
                links.append(f"[{Path(evidence['source_path']).stem}, {location}](../../{evidence['source_path']})")
            lines.append(f"| {c['label']} | {c['kind']} | {entry['coverage']} | {'; '.join(links)} |")
        lines += ["", "## Dictionary update", "", f"Concepts first registered in this source: {len(course['new_concept_ids'])}. Final source inventory after cross-course review: {len(course['concepts'])} concepts. Later evidence updates are listed in the reconciliation audit.", ""]
        (OUT / "courses" / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")
    lines = ["# Course Topic Analysis", "", "Analysis of seven downloaded courses. The downloaded book is a separate comparison source.", "",
             "[Category dictionaries](categories/README.md) · [Method and limits](METHOD.md) · [Shared dictionary](DICTIONARY.md) · [Frequency CSV](frequency.csv) · [Course matrix](course-matrix.csv) · [Structured evidence](courses/)", "",
             f"The dictionary contains **{len(concepts)} concepts**. Frequency counts distinct courses with available teaching content or assigned readings. Planned topics and the book do not increase this count.", "",
             "## Sources", "", "| Code | Source | Confirmed concepts | Planned only | New dictionary entries |", "| --- | --- | ---: | ---: | ---: |"]
    for c in courses:
        slug = c["source_id"]
        confirmed = sum(e["coverage"] != "planned" for e in c["concepts"])
        lines.append(f"| {labels[slug]} | [{datasets[slug].get('institution', 'Book')}: {datasets[slug]['title']}](courses/{slug}.md) | {confirmed} | {len(c['concepts']) - confirmed} | {len(c['new_concept_ids'])} |")
    lines += ["", "## Most frequent concepts", "", "The first 30 rows use the same ranking as the full table. Ties use the number of courses with teaching evidence, then the concept name.", ""]
    def table(rows):
        result = ["| Concept | Courses / 7 | Taught | Assigned | Courses | Planned only | Book |", "| --- | ---: | ---: | ---: | --- | --- | --- |"]
        for r in rows:
            result.append(f"| {r['concept']} | {r['course_count']} | {r['taught_course_count']} | {r['assigned_course_count']} | {', '.join(labels[s] for s in r['courses'])} | {', '.join(labels[s] for s in r['planned_courses'])} | {'yes' if r['book_present'] else ''} |")
        return result
    lines += table(ranked[:30])
    lines += ["", "## Most frequent patterns", "", *table([r for r in ranked if r["kind"] == "pattern"][:20])]
    lines += ["", "## Full frequency table", "", *table(ranked), "", "## Interpretation", "",
              "Course frequency shows how widely a concept appears across these sources. It does not measure teaching time, depth, quality, or importance. A broad topic and a specific pattern can both appear in the table; their counts must not be added.", "",
              "A blank course entry means no confirmed evidence was recorded in the selected available materials. It does not prove that the course omits the topic. Read the course reports and archive gap reports before treating a difference as a curriculum gap.", ""]
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    audit = []
    for c in courses:
        slug = c["source_id"]
        manifest_path = ROOT / "courses" / slug / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        audit.append(dict(source_id=slug, manifest_sha256=hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
            material_categories=dict(Counter(m["category"] for m in manifest["materials"])),
            evidence_files=sorted({e["source_path"] for entry in c["concepts"] for e in entry["evidence"]})))
    write_json(OUT / "source-audit.json", audit)
    print(f"Built reports: {len(concepts)} concepts, {sum(len(c['concepts']) for c in courses)} source-concept records.")


def validate_outputs():
    dictionary = json.loads((OUT / "dictionary.json").read_text(encoding="utf-8"))
    concepts = {c["id"]: c for c in dictionary["concepts"]}
    validate_dictionary(concepts)
    total = 0
    for slug in ORDER:
        course = json.loads((OUT / "courses" / f"{slug}.json").read_text(encoding="utf-8"))
        keys = [e["concept_id"] for e in course["concepts"]]
        assert len(keys) == len(set(keys))
        for entry in course["concepts"]:
            assert entry["concept_id"] in concepts and entry["evidence"]
            for evidence in entry["evidence"]:
                path = ROOT / evidence["source_path"]
                assert hashlib.sha256(path.read_bytes()).hexdigest() == evidence["sha256"]
                assert path.read_text(encoding="utf-8").splitlines()[evidence["line"] - 1].strip() == evidence["excerpt"]
                total += 1
    frequency = json.loads((OUT / "frequency.json").read_text(encoding="utf-8"))
    assert {r["concept_id"] for r in frequency["rows"]} == set(concepts)
    for row in frequency["rows"]:
        assert row["course_count"] == len(set(row["courses"])) <= 7
        assert row["course_count"] == row["taught_course_count"] + row["assigned_course_count"]
        assert ORDER[-1] not in row["courses"]
        assert not set(row["courses"]) & set(row["planned_courses"])
        actual = {"taught": [], "assigned": [], "planned": []}
        for slug in ORDER[:-1]:
            course = json.loads((OUT / "courses" / f"{slug}.json").read_text(encoding="utf-8"))
            entry = next((e for e in course["concepts"] if e["concept_id"] == row["concept_id"]), None)
            if entry:
                actual[entry["coverage"]].append(slug)
        for level in actual:
            assert row[f"{level}_courses"] == actual[level], (row["concept_id"], level)
        book = json.loads((OUT / "courses" / f"{ORDER[-1]}.json").read_text(encoding="utf-8"))
        assert row["book_present"] == any(e["concept_id"] == row["concept_id"] for e in book["concepts"])
    book = json.loads((OUT / "courses" / f"{ORDER[-1]}.json").read_text(encoding="utf-8"))
    for entry in book["concepts"]:
        for evidence in entry["evidence"]:
            lines = (ROOT / evidence["source_path"]).read_text(encoding="utf-8").splitlines()
            references = next((i for i, line in enumerate(lines, 1) if line == "### References"), None)
            assert references is None or evidence["line"] < references, entry["concept_id"]
    links = 0
    for path in OUT.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:")):
                continue
            assert (path.parent / target.split("#")[0]).exists(), (path, target)
            links += 1
    result = dict(status="passed", sources=len(ORDER), concepts=len(concepts), evidence_records=total,
                  local_links=links, checks=["canonical names and aliases are unique", "parent graph has no cycles",
                  "evidence excerpts and hashes match local sources", "course frequencies exclude the book and planned topics",
                  "frequencies match the course inventories", "book evidence is outside bibliographies",
                  "source-concept records are unique", "report links exist"])
    write_json(OUT / "validation.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["apply", "reconcile", "build", "validate"])
    parser.add_argument("--course", choices=ORDER)
    args = parser.parse_args()
    if args.action == "apply":
        apply_course(args.course)
    elif args.action == "reconcile":
        reconcile()
    elif args.action == "build":
        build_reports()
    else:
        validate_outputs()
