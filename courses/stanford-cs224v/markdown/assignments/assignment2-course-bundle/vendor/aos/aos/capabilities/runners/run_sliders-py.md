# Homework 2 bundle: vendor/aos/aos/capabilities/runners/run_sliders.py

[Course index](../../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/capabilities/runners/run_sliders.py) · [Raw file](../../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/capabilities/runners/run_sliders.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""Run SLIDERS (sliders-new) over workspace documents and leave tables + answer in --output-dir.

Executed with external/sliders-new/.venv/bin/python. Reads API_KEY, BASE_URL and
AOS_MODEL from the environment.
"""

import argparse
import asyncio
import csv
import json
import os
from pathlib import Path

TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".rst", ".text"}


def collect_docs(paths):
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(f for f in p.rglob("*") if f.is_file() and f.suffix.lower() in TEXT_SUFFIXES))
        elif p.is_file():
            files.append(p)
    return files


def usage_from_trace(trace_json, model):
    """Find the usage totals in the trace summary (input/output tokens, calls, cost if priced)."""
    found = {}

    def walk(node):
        if isinstance(node, dict):
            if "input_tokens" in node and "output_tokens" in node and not found:
                found.update(node)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(trace_json.get("summary", trace_json))
    cost = found.get("cost_usd")
    return {"model": model, "calls": found.get("llm_calls"), "input_tokens": found.get("input_tokens", 0),
            "output_tokens": found.get("output_tokens", 0), "cost_usd": cost if cost else None}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", nargs="+", required=True, help="text/markdown files or directories")
    ap.add_argument("--question", required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()

    from sliders.config import SlidersConfig
    from sliders.corpus import load_corpus
    from sliders.pipeline import ask, build_table
    from sliders.table import to_records
    from sliders.trace import Trace

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    model = os.environ.get("AOS_MODEL", "gemini-3.6-flash")
    # The proxy routes by model name; OPENAI_API_KEY is what the SDK reads.
    os.environ["OPENAI_API_KEY"] = os.environ["API_KEY"]
    os.environ["OPENAI_BASE_URL"] = os.environ["BASE_URL"]

    cfg = SlidersConfig(cache_dir=out / ".sliders", glob="**/*.{md,markdown,txt,rst,text}")
    for role in type(cfg.models).model_fields:
        spec = getattr(cfg.models, role)
        setattr(cfg.models, role, spec.model_copy(update={"model": model}))
    cfg = cfg.via_proxy(os.environ["BASE_URL"])

    files = collect_docs(args.docs)
    if not files:
        raise SystemExit(f"no text/markdown documents found in {args.docs}")
    docs = load_corpus([str(f) for f in files], config=cfg)
    print(f"SLIDERS: {len(docs)} document(s), model {model}")

    trace = Trace()

    # One event loop for both stages: sliders memoizes its OpenAI client per process,
    # and reusing it across two asyncio.run() loops leaves stale connections that
    # error at shutdown.
    async def _run():
        ref = await build_table(args.question, docs, config=cfg, trace=trace)
        return ref, await ask(args.question, ref, config=cfg, trace=trace)

    ref, result = asyncio.run(_run())
    tables = ref.load()
    (out / "tables").mkdir(exist_ok=True)
    evidence_rows = []
    for table in tables.tables:
        records = to_records(table)
        columns = ["row_id"] + [f.name for f in table.spec.fields] + ["document"]
        with open(out / "tables" / f"{table.spec.name}.csv", "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(records)
        for row in table.rows:
            for field, cell in row.cells.items():
                if cell.value_raw is None:
                    continue
                span = cell.span
                evidence_rows.append({
                    "table": table.spec.name, "row_id": row.row_id, "field": field,
                    "value": cell.value_raw, "quote": cell.quote or "", "document": row.doc_name,
                    "path": row.doc_path or "", "start_line": span.start_line if span else "",
                    "end_line": span.end_line if span else "", "quote_verified": cell.quote_verified,
                })
        print(f"SLIDERS: table {table.spec.name}: {len(table.rows)} rows")
    with open(out / "evidence.csv", "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["table", "row_id", "field", "value", "quote", "document",
                                                "path", "start_line", "end_line", "quote_verified"])
        writer.writeheader()
        writer.writerows(evidence_rows)
    (out / "table.json").write_text(tables.model_dump_json(by_alias=True, indent=2))

    (out / "answer.json").write_text(result.model_dump_json(indent=2))
    lines = [f"# {args.question}", "", result.answer, ""]
    if not result.grounded:
        lines.append("_Note: the extracted table did not support this answer (ungrounded)._\n")
    if result.citations:
        lines.append("## Citations")
        for c in result.citations:
            lines.append(f"- {c.locator or c.doc_name} ({c.table}.{c.field}): {c.quote or ''}")
    (out / "answer.md").write_text("\n".join(lines) + "\n")
    trace_json = trace.to_json()
    (out / "trace.json").write_text(json.dumps(trace_json, indent=2, default=str))
    (out / "usage.json").write_text(json.dumps(usage_from_trace(trace_json, model), indent=2))
    print(f"SLIDERS finished; table id {ref.table_id}; {len(tables.tables)} table(s); grounded={result.grounded}")


if __name__ == "__main__":
    main()

```
