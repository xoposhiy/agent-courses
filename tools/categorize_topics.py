"""Build category frequency dictionaries from the reviewed course analysis."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from topic_analysis import ORDER

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
OUTPUT = ANALYSIS / "categories"
CODES = dict(zip(ORDER, ["S329", "COL", "CMU", "LC", "S224", "EVAL", "CU", "BOOK"]))


def validate_taxonomy(taxonomy, concepts, frequency):
    categories = {c["id"]: c for c in taxonomy["categories"]}
    assert len(categories) == len(taxonomy["categories"]), "Duplicate category IDs."
    ids = [a["concept_id"] for a in taxonomy["assignments"]]
    assert len(ids) == len(set(ids)), "A concept has multiple primary categories."
    assert set(ids) == set(concepts) == set(frequency), "The classification must cover the whole dictionary."
    used = Counter()
    for assignment in taxonomy["assignments"]:
        category = categories[assignment["category_id"]]
        assert assignment["subgroup_id"] in {s["id"] for s in category["subgroups"]}
        related = assignment["related_category_ids"]
        assert len(related) == len(set(related))
        assert set(related) <= set(categories)
        assert assignment["category_id"] not in related
        used[assignment["category_id"]] += 1
    assert set(used) == set(categories), "Empty category."


def category_rows(taxonomy, concepts, frequency):
    """Join classifications without changing any source frequency or definition."""
    categories = {c["id"]: c for c in taxonomy["categories"]}
    rows = {c["id"]: [] for c in taxonomy["categories"]}
    for assignment in taxonomy["assignments"]:
        key = assignment["concept_id"]
        concept = concepts[key]
        category = categories[assignment["category_id"]]
        subgroup = next(s for s in category["subgroups"] if s["id"] == assignment["subgroup_id"])
        rows[assignment["category_id"]].append(dict(
            **frequency[key], category_id=assignment["category_id"],
            category=category["title"], subgroup_id=assignment["subgroup_id"], subgroup=subgroup["title"],
            related_category_ids=assignment["related_category_ids"],
            definition=concept["definition"], aliases=concept["aliases"],
            related_terms=concept.get("related_terms", []), parent_id=concept["parent_id"]))
    for group in rows.values():
        group.sort(key=lambda r: (-r["course_count"], -r["taught_course_count"], r["concept"].casefold()))
    return rows


def category_stats(rows):
    """Count concepts and course coverage without adding concept frequencies."""
    result = []
    for category_id, group in rows.items():
        courses = {slug for row in group for slug in row["courses"]}
        result.append(dict(category_id=category_id, concept_count=len(group),
            confirmed_course_concepts=sum(r["course_count"] > 0 for r in group),
            book_only_concepts=sum(r["course_count"] == 0 and r["book_present"] for r in group),
            covered_course_count=len(courses),
            course_concept_counts={slug: sum(slug in r["courses"] for r in group) for slug in ORDER[:-1]}))
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def input_data():
    taxonomy = read_json(ANALYSIS / "taxonomy.json")
    concepts = {c["id"]: c for c in read_json(ANALYSIS / "dictionary.json")["concepts"]}
    frequency = {r["concept_id"]: r for r in read_json(ANALYSIS / "frequency.json")["rows"]}
    validate_taxonomy(taxonomy, concepts, frequency)
    return taxonomy, concepts, frequency


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_csv(path, records):
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        for record in records:
            writer.writerow({k: "; ".join(v) if isinstance(v, list) else v for k, v in record.items()})


def frequency_table(rows):
    lines = ["| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |",
             "| --- | --- | ---: | ---: | ---: | --- | --- | --- |"]
    for row in rows:
        name = f"[{row['concept']}](#concept-{row['concept_id']})"
        values = [name, row["kind"], row["course_count"], row["taught_course_count"],
                  row["assigned_course_count"], ", ".join(CODES[s] for s in row["courses"]),
                  ", ".join(CODES[s] for s in row["planned_courses"]), "yes" if row["book_present"] else ""]
        lines.append("| " + " | ".join(cell(value) for value in values) + " |")
    return lines


def render_category(category, rows, categories, courses):
    key = category["id"]
    subgroups = {s["id"]: s["title"] for s in category["subgroups"]}
    lines = [f"# {category['title']}", "", category["scope"], "", category["boundary"], "",
             f"[All categories](README.md) · [CSV]({key}.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)", "",
             f"**{len(rows)} concepts**: {sum(r['course_count'] > 0 for r in rows)} confirmed in courses; "
             f"{sum(r['course_count'] == 0 and r['book_present'] for r in rows)} confirmed only in the book.", "",
             "## Frequency dictionary", "",
             "Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.", "",
             *frequency_table(rows), "", "## Course codes", ""]
    lines += [f"- **{code}**: [{courses[slug]['title']}](../courses/{slug}.md)" for slug, code in CODES.items()]
    lines += ["", "## Definitions and evidence", "",
              "Entries follow frequency order. Related categories are navigation links; they do not create additional category membership or frequency.", ""]
    for row in rows:
        lines += [f"<a id=\"concept-{row['concept_id']}\"></a>", "", f"### {row['concept']}", "",
                  f"`{row['concept_id']}` · {subgroups[row['subgroup_id']]} · original type: {row['kind']}", "",
                  row["definition"], ""]
        if row["aliases"]:
            lines += [f"**Aliases:** {'; '.join(row['aliases'])}.", ""]
        if row["related_terms"]:
            lines += [f"**Related terms:** {'; '.join(row['related_terms'])}.", ""]
        if row["related_category_ids"]:
            links = [f"[{categories[c]['title']}]({c}.md)" for c in row["related_category_ids"]]
            lines += [f"**Also relevant to:** {'; '.join(links)}.", ""]
        evidence_links = []
        for slug in ORDER:
            entry = next((e for e in courses[slug]["concepts"] if e["concept_id"] == row["concept_id"]), None)
            if entry:
                evidence = entry["evidence"][0]
                locator = f"p. {evidence['page']}" if evidence["page"] else f"line {evidence['line']}"
                label = f"{CODES[slug]}, {entry['coverage']}, {locator}"
                evidence_links.append(f"[{label}](../../{evidence['source_path']})")
        lines += [f"**Evidence:** {'; '.join(evidence_links)}.", ""]
    return "\n".join(lines)


def build():
    taxonomy, concepts, frequency = input_data()
    rows = category_rows(taxonomy, concepts, frequency)
    stats = category_stats(rows)
    categories = {c["id"]: c for c in taxonomy["categories"]}
    courses = {slug: read_json(ANALYSIS / "courses" / f"{slug}.json") for slug in ORDER}
    catalog = {d["id"]: d for d in read_json(ROOT / "catalog.json")["datasets"]}
    for slug, course in courses.items():
        course["title"] = catalog[slug]["title"]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    all_rows = []
    for key, group in rows.items():
        all_rows.extend(group)
        write_csv(OUTPUT / f"{key}.csv", group)
        (OUTPUT / f"{key}.md").write_text(render_category(categories[key], group, categories, courses), encoding="utf-8")
    write_csv(OUTPUT / "all-concepts.csv", all_rows)
    write_json(OUTPUT / "frequencies.json", dict(unit="distinct course", denominator=7,
        book_in_denominator=False, assignment_rule=taxonomy["assignment_rule"], categories=rows))
    write_json(OUTPUT / "summary.json", stats)
    write_csv(OUTPUT / "summary.csv", [{k: v for k, v in stat.items() if k != "course_concept_counts"} for stat in stats])
    write_csv(OUTPUT / "category-course-counts.csv", [dict(category_id=s["category_id"], **s["course_concept_counts"]) for s in stats])
    lines = ["# Frequency Dictionaries by Category", "",
             f"The shared dictionary contains **{len(concepts)} concepts** in **{len(categories)} primary categories**. "
             f"**{sum(r['course_count'] > 0 for r in frequency.values())}** have confirmed course evidence; "
             f"**{sum(r['course_count'] == 0 and r['book_present'] for r in frequency.values())}** have confirmed evidence only in the book.", "",
             "[Category method and boundaries](METHOD.md) · [All concepts CSV](all-concepts.csv) · [Category summary CSV](summary.csv) · [Course coverage CSV](category-course-counts.csv) · [Original analysis](../README.md)", "",
             "Each concept belongs to one primary category. Related categories are cross-references. This keeps architectural patterns separate from local techniques and named products without repeating concepts in category totals.", "",
             "## Category dictionaries", "", "| Category | All concepts | Confirmed in courses | Book only | Most frequent concepts | CSV |",
             "| --- | ---: | ---: | ---: | --- | --- |"]
    for stat in stats:
        key = stat["category_id"]
        top = "; ".join(f"{r['concept']} ({r['course_count']}/7)" for r in rows[key][:3])
        lines.append(f"| [{categories[key]['title']}]({key}.md) | {stat['concept_count']} | {stat['confirmed_course_concepts']} | {stat['book_only_concepts']} | {top} | [CSV]({key}.csv) |")
    lines += ["", "## How to read the categories", "",
              "Architecture describes how a system is arranged and who controls the next step. A technique describes an operation, such as sampling reasoning paths, summarizing context, or reranking search results. A product or protocol describes an implementation choice. An application describes the work the agent performs.", "",
              "For example, orchestrator and workers is an architectural pattern; self-consistency is a reasoning technique; context compaction is a context technique; MCP is a protocol; and a coding agent is an application area. Human approval is classified as a control-flow pattern and linked to safety. The category method explains other boundary cases.", "",
              "## Course coverage by category", "",
              "Cells count distinct confirmed concepts in the category and course. They do not measure lessons, teaching hours, depth, or course quality. The book is excluded. Category size depends on the dictionary's granularity.", "",
              "| Category | " + " | ".join(CODES[s] for s in ORDER[:-1]) + " |",
              "| --- | " + " | ".join("---:" for _ in ORDER[:-1]) + " |"]
    for stat in stats:
        values = " | ".join(str(stat["course_concept_counts"][s]) for s in ORDER[:-1])
        lines.append(f"| [{categories[stat['category_id']]['title']}]({stat['category_id']}.md) | {values} |")
    lines += ["", "## Course codes", ""]
    for slug in ORDER:
        lines.append(f"- **{CODES[slug]}**: [{catalog[slug].get('institution', 'Book')}: {catalog[slug]['title']}](../courses/{slug}.md)")
    lines += ["", "## Count rules", "",
              "A concept's frequency is unchanged from the original analysis: one count per course with taught or assigned evidence. Schedule-only topics and the book do not raise that frequency. Counts are not inherited from parent concepts. Book-only concepts remain visible at frequency zero.", "",
              "Each category file includes the full frequency ranking, definitions, aliases, related terms, and source evidence. Its CSV preserves the original frequency fields and adds the primary category, subgroup, and related categories.", ""]
    (OUTPUT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    inputs = [ANALYSIS / "taxonomy.json", ANALYSIS / "dictionary.json", ANALYSIS / "frequency.json"]
    write_json(OUTPUT / "inputs.json", {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs})
    print(f"Built {len(categories)} category dictionaries for {len(concepts)} concepts.")


def validate():
    taxonomy, concepts, frequency = input_data()
    expected = category_rows(taxonomy, concepts, frequency)
    actual = read_json(OUTPUT / "frequencies.json")["categories"]
    assert actual == expected, "Category frequencies differ from the source analysis."
    assert read_json(OUTPUT / "summary.json") == category_stats(expected)
    for filename, digest in read_json(OUTPUT / "inputs.json").items():
        assert hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == digest
    csv_records = []
    for key, group in expected.items():
        with (OUTPUT / f"{key}.csv").open(encoding="utf-8-sig", newline="") as stream:
            records = list(csv.DictReader(stream))
        assert len(records) == len(group)
        for record, row in zip(records, group):
            for field, value in row.items():
                text = "; ".join(value) if isinstance(value, list) else "" if value is None else str(value)
                assert record[field] == text, (key, row["concept_id"], field)
        csv_records.extend(records)
    assert len(csv_records) == len(concepts)
    with (OUTPUT / "all-concepts.csv").open(encoding="utf-8-sig", newline="") as stream:
        assert list(csv.DictReader(stream)) == csv_records
    for slug in ORDER[:-1]:
        inventory = read_json(ANALYSIS / "courses" / f"{slug}.json")
        confirmed = sum(entry["coverage"] != "planned" for entry in inventory["concepts"])
        assert sum(s["course_concept_counts"][slug] for s in category_stats(expected)) == confirmed
    links = 0
    for path in OUTPUT.glob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:")):
                continue
            filename, _, anchor = target.partition("#")
            resolved = path.parent / filename if filename else path
            assert resolved.exists(), (path, target)
            if anchor:
                assert f'id="{anchor}"' in resolved.read_text(encoding="utf-8"), (path, target)
            links += 1
    result = dict(status="passed", categories=len(expected), concepts=len(concepts), local_links=links,
        checks=["all concepts have one primary category", "category and subgroup IDs are valid",
                "definitions and frequencies match the original analysis", "CSV files match structured data",
                "category totals match each course inventory", "input hashes match", "local links and concept anchors exist"])
    write_json(OUTPUT / "validation.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["build", "validate"])
    args = parser.parse_args()
    if args.action == "build":
        build()
    else:
        validate()
