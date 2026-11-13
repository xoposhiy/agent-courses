"""Run DataSTORM over a SQLite database (or CSV files) and leave its report in --output-dir.

Executed with external/datastorm/.venv/bin/python, cwd = the datastorm repo.
Reads API_KEY, BASE_URL, AOS_MODEL and SERPER_API_KEY from the environment.
"""

import argparse
import asyncio
import csv
import importlib
import json
import logging
import os
import shutil
import sqlite3
import sys
from pathlib import Path


class UsageCounter:
    """LangChain callback summing token usage across every model call."""

    def __init__(self):
        self.calls = 0
        self.input_tokens = 0
        self.output_tokens = 0
        self.ignore_chat_model = False
        self.ignore_llm = False
        self.raise_error = False
        self.run_inline = True

    def totals(self):
        return {"calls": self.calls, "input_tokens": self.input_tokens, "output_tokens": self.output_tokens}

    def on_llm_end(self, response, **kwargs):
        self.calls += 1
        usage = ((response.llm_output or {}).get("token_usage") or {}) if getattr(response, "llm_output", None) else {}
        if not usage:
            for generations in getattr(response, "generations", []) or []:
                for g in generations:
                    meta = getattr(getattr(g, "message", None), "usage_metadata", None) or {}
                    usage = {"prompt_tokens": meta.get("input_tokens", 0), "completion_tokens": meta.get("output_tokens", 0)}
        self.input_tokens += int(usage.get("prompt_tokens", 0) or 0)
        self.output_tokens += int(usage.get("completion_tokens", 0) or 0)

    def __getattr__(self, name):  # every other callback hook is a no-op
        if name.startswith("on_") or name.startswith("ignore_"):
            return (lambda *a, **k: None) if name.startswith("on_") else False
        raise AttributeError(name)


def build_sqlite_from_csvs(csv_files, db_path: Path) -> None:
    import pandas as pd

    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    for f in csv_files:
        pd.read_csv(f).to_sql(Path(f).stem, conn, index=False)
    conn.close()


def write_domain(domain_dir: Path, db_path: Path) -> int:
    """Create the domain folder DataSTORM expects: db details, schema lookup, instructions."""
    domain_dir.mkdir(parents=True, exist_ok=True)
    (domain_dir / "db_details.json").write_text(json.dumps(
        {"db_type": "sqlite", "db_path": str(db_path), "database_name": domain_dir.name,
         "suql_enabled": False}, indent=2))
    conn = sqlite3.connect(db_path)
    tables = conn.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall()
    with open(domain_dir / "_lookup_table.csv", "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["table_name", "id_field_name", "type", "table_CREATE_command"])
        for name, sql in tables:
            columns = [row[1] for row in conn.execute(f'PRAGMA table_info("{name}")')]
            writer.writerow([name, columns[0] if columns else "rowid", "table", sql])
    conn.close()
    with open(domain_dir / "domain_specific_instructions.csv", "w", newline="") as fh:
        csv.writer(fh).writerow(["table_name", "instruction", "report_controller_flag"])
    return len(tables)


def main() -> None:
    logging.basicConfig(level=logging.WARNING, stream=sys.stdout, format="%(name)s: %(message)s")
    logging.getLogger("knowledge_storm").setLevel(logging.INFO)  # stage progress, streamed into the step log
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--inputs", nargs="+", required=True, help="a .db/.sqlite file or CSV files")
    ap.add_argument("--sources-dir", default=None, help="archive of fetched web pages (STORM_FETCH_DIR)")
    ap.add_argument("--db-description", default=None)
    ap.add_argument("--first-level-questions", type=int, default=3)
    ap.add_argument("--max-tree-depth", type=int, default=3)
    ap.add_argument("--population", type=int, default=2)
    ap.add_argument("--max-global-insights", type=int, default=10)
    ap.add_argument("--expansion-max-questions", type=int, default=2)
    args = ap.parse_args()

    out = Path(args.output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    inputs = [Path(p).resolve() for p in args.inputs]
    if len(inputs) == 1 and inputs[0].suffix.lower() in (".db", ".sqlite", ".sqlite3"):
        db_path = inputs[0]
    else:
        csvs = [p for p in inputs if p.suffix.lower() == ".csv"]
        if not csvs:
            raise SystemExit("inputs must be one SQLite database or CSV files")
        db_path = out / "data.sqlite"
        build_sqlite_from_csvs(csvs, db_path)
    domain = "aos_data"
    domains_root = out / ".domains"
    n_tables = write_domain(domains_root / domain, db_path)
    print(f"DataSTORM: {n_tables} table(s) in {db_path}")

    model = os.environ.get("AOS_MODEL", "gemini-3.6-flash")
    os.environ["AZURE_OPENAI_ENDPOINT"] = os.environ["BASE_URL"]
    os.environ["AZURE_OPENAI_API_KEY"] = os.environ["API_KEY"]
    os.environ["DATATALK_DOMAINS_ROOT"] = str(domains_root)
    os.environ["DATASTORM_PROMPT_SOURCE"] = "local"
    os.environ["DATASTORM_SQL_RESULTS_DIR"] = str(out / "sql_results")
    os.environ.setdefault("DATASTORM_DEBUG_LOG", str(out / ".debug_rm.log"))
    os.environ.setdefault("OPENAI_API_TYPE", "openai")
    if args.sources_dir:
        os.environ["STORM_FETCH_DIR"] = str(Path(args.sources_dir).resolve())
    (out / "sql_results").mkdir(exist_ok=True)

    # Several call sites hardcode gpt-5; route every LangChain client to the configured model.
    repo = Path.cwd()
    sys.path.insert(0, str(repo))
    langfuse_llm = importlib.import_module("knowledge_storm.langfuse_llm")
    original_get_llm = langfuse_llm.get_llm
    counter = UsageCounter()

    def get_llm(model_name="gpt-5", *a, **kw):
        llm = original_get_llm(model, *a, **kw)
        try:
            llm.callbacks = [counter]
            if hasattr(llm, "stream_usage"):
                llm.stream_usage = True
        except Exception:
            pass
        return llm

    langfuse_llm.get_llm = get_llm
    entry = importlib.import_module("datatalk_basic_article_generation_costorm")
    # modules imported through the package __init__ already bound the original function
    for module in list(sys.modules.values()):
        if getattr(module, "get_llm", None) is original_get_llm:
            module.get_llm = get_llm
    original_init_storm_runner = entry.init_storm_runner

    def init_storm_runner(*a, **kw):  # the critique phase builds a nested runner with default models
        kw["datastorm_main_model"] = model
        kw.setdefault("datatalk_engine", model)
        return original_init_storm_runner(*a, **kw)

    entry.init_storm_runner = init_storm_runner

    (repo / "display_javascripts").mkdir(exist_ok=True)  # tree_simulator saves a viewer copy of the tree here
    scratch = out / ".datastorm_run"
    result = asyncio.run(entry.process_generation(
        topic=args.topic, output_dir=str(scratch), domain=domain, db_description=args.db_description,
        no_warm_start=True, generate_graphs=False, disable_upload_to_azure=True,
        first_level_questions=args.first_level_questions, max_tree_depth=args.max_tree_depth,
        each_level_population_control_num=args.population, max_global_insights=args.max_global_insights,
        expansion_max_questions=args.expansion_max_questions, append_timestamp_to_output_dir=False,
        generation_module_model=model, datatalk_engine=model, datastorm_main_model=model,
        # the thesis is only formed once the tree reaches depth 3; shallower runs get a thesis-free report
        skip_thesis=args.max_tree_depth < 3,
    ))
    run_dir = Path(result["output_dir"])
    for item in run_dir.iterdir():
        target = out / item.name
        if target.exists():
            shutil.rmtree(target) if target.is_dir() else target.unlink()
        shutil.move(str(item), str(target))
    shutil.rmtree(scratch, ignore_errors=True)
    for name in ("co_storm_report_staged.md", "co_storm_report.txt"):
        if (out / name).is_file():
            shutil.copyfile(out / name, out / "report.md")
            break
    (out / "usage.json").write_text(json.dumps({"model": model, **counter.totals(), "cost_usd": None}, indent=2))
    print(f"DataSTORM finished; artifacts in {out}; {counter.totals()}")


if __name__ == "__main__":
    main()
