# Homework 2 bundle: vendor/aos/aos/cli.py

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/cli.py) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/cli.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""Command line interface: ``aos <command> ...``."""

from __future__ import annotations

import argparse
import json
import os
import sys

from .api import AOS
from .llm import LLM, load_env
from .tasks import Task
from .workspace import Workspace, WorkspaceError, format_rows


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    if getattr(args, "model", None):
        os.environ["AOS_MODEL"] = args.model  # the external runners read it from their environment
    try:
        return args.func(args) or 0
    except WorkspaceError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aos", description="Agentic Operating System")
    sub = parser.add_subparsers()

    p = sub.add_parser("init", help="create a workspace (folders, workspace.db catalog, git repository)")
    p.add_argument("workspace")
    p.add_argument("--goal", default=None)
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("run", help="pursue a goal: plan and execute steps until done")
    p.add_argument("workspace")
    p.add_argument("goal")
    p.add_argument("--max-steps", type=int, default=12)
    p.add_argument("--model", default=None, help="override AOS_MODEL")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("step", help="run a single step with a chosen worker")
    p.add_argument("workspace")
    p.add_argument("worker")
    p.add_argument("instructions")
    p.add_argument("--inputs", nargs="*", default=[])
    p.add_argument("--output-dir", default="generated")
    p.add_argument("--reason", default="")
    p.add_argument("--model", default=None)
    p.set_defaults(func=cmd_step)

    p = sub.add_parser("workflow-save", help="save a finished task's steps as a reusable workflow")
    p.add_argument("workspace")
    p.add_argument("task_id")
    p.add_argument("name")
    p.set_defaults(func=cmd_workflow_save)

    p = sub.add_parser("workflow-run", help="replay a saved workflow in a workspace")
    p.add_argument("workspace")
    p.add_argument("workflow", help="path to a workflow json (inside or outside the workspace)")
    p.add_argument("--model", default=None)
    p.set_defaults(func=cmd_workflow_run)

    p = sub.add_parser("status", help="show tasks and files with their provenance")
    p.add_argument("workspace")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("add", help="give the workspace a new input file (copied into inputs/ if it is outside), catalog it, commit")
    p.add_argument("workspace")
    p.add_argument("files", nargs="+")
    p.add_argument("--reason", default="Provided by the user", help="what the file is for")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("query", help="query the file catalog (workspace.db) with SQL; default: list every file")
    p.add_argument("workspace")
    p.add_argument("sql", nargs="?", default=DEFAULT_QUERY)
    p.add_argument("--json", action="store_true", help="print rows as JSON")
    p.set_defaults(func=cmd_query)

    p = sub.add_parser("describe", help="show everything recorded about one file")
    p.add_argument("workspace")
    p.add_argument("path")
    p.set_defaults(func=cmd_describe)

    p = sub.add_parser("log", help="show the workspace git history")
    p.add_argument("workspace")
    p.add_argument("-n", type=int, default=20)
    p.set_defaults(func=cmd_log)

    p = sub.add_parser("rollback", help="restore the workspace to an earlier commit (as a new commit)")
    p.add_argument("workspace")
    p.add_argument("ref")
    p.set_defaults(func=cmd_rollback)

    p = sub.add_parser("trace", help="show the LLM calls recorded for a workspace (every prompt, reply, tokens, cost)")
    p.add_argument("workspace")
    p.add_argument("task", nargs="?", default=None, help="task-NNN; default: every task plus calls outside tasks")
    p.add_argument("--step", type=int, default=None, help="only this step of the task")
    p.add_argument("--full", action="store_true", help="print the messages sent and the reply of each call")
    p.add_argument("--json", action="store_true", help="print the raw records")
    p.set_defaults(func=cmd_trace)

    p = sub.add_parser("ask", help="ask the meta-assistant a question about the workspace")
    p.add_argument("workspace")
    p.add_argument("question")
    p.add_argument("--model", default=None)
    p.set_defaults(func=cmd_ask)

    p = sub.add_parser("ui", help="serve the web interface for a folder of workspaces (or one workspace)")
    p.add_argument("path", nargs="?", default="workspaces",
                   help="a workspace, or a folder holding workspaces (default: ./workspaces, created if missing)")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--max-steps", type=int, default=12)
    p.add_argument("--model", default=None)
    p.set_defaults(func=cmd_ui)

    p = sub.add_parser("workers", help="list workers and whether they can run here")
    p.set_defaults(func=cmd_workers)
    return parser


def _aos(args) -> AOS:
    return AOS.open(args.workspace, llm=LLM(model=getattr(args, "model", None)), log=lambda line: print(line, flush=True))


def cmd_init(args) -> int:
    aos = AOS.create(args.workspace, goal=args.goal)
    print(f"initialized workspace at {aos.root} with {len(list((aos.root / 'code' / 'adapters').glob('*.py')))} adapter scripts in code/adapters/")
    return 0


def cmd_run(args) -> int:
    task = _aos(args).run(args.goal, max_steps=args.max_steps)
    print(f"\n{task.id} {task.data['status']}: {task.data['result']}")
    return 0 if task.data["status"] == "done" else 2


def cmd_step(args) -> int:
    try:
        record = _aos(args).step(args.worker, args.instructions, inputs=args.inputs,
                                 output_dir=args.output_dir, reason=args.reason)
    except RuntimeError as exc:  # stopped before running: the budget cap
        print(exc)
        return 2
    print(json.dumps({k: record[k] for k in ("n", "status", "outputs", "summary", "error", "commit")}, indent=2))
    return 0 if record["status"] == "ok" else 2


def cmd_workflow_save(args) -> int:
    aos = AOS.open(args.workspace)
    path = aos.save_workflow(args.task_id, args.name)
    print(f"saved {aos.ws.relpath(path)} with {len(json.loads(path.read_text())['steps'])} steps")
    return 0


def cmd_workflow_run(args) -> int:
    task = _aos(args).workflow(args.workflow)
    print(f"\n{task.id} {task.data['status']}: {task.data['result']}")
    return 0 if task.data["status"] == "done" else 2


DEFAULT_QUERY = "SELECT path, source, task, step, summary FROM files ORDER BY task, step, path"


def cmd_add(args) -> int:
    for file in args.files:
        if not os.path.isfile(file):
            print(f"error: {file} is not a file", file=sys.stderr)
            return 1
    entries = AOS.open(args.workspace).add(*args.files, reason=args.reason)
    print(format_rows([{k: e[k] for k in ("path", "source", "reason", "summary")} for e in entries]))
    return 0


def cmd_query(args) -> int:
    ws = Workspace.open(args.workspace)
    rows = ws.query(args.sql)
    print(json.dumps(rows, indent=2) if args.json else format_rows(rows))
    return 0


def cmd_status(args) -> int:
    ws = Workspace.open(args.workspace)
    print(f"workspace: {ws.root}\ngoal: {ws.goal}\nhead: {ws.head()[:12]}\n")
    tasks = Task.list(ws)
    print(f"tasks ({len(tasks)}):")
    for t in tasks:
        print(f"  {t.id} [{t.data['status']}] {t.goal}")
        for s in t.steps:
            print(f"    step {s['n']} [{s['status']}] {s['worker']}: {s['reason'] or s['instructions'][:80]}")
    print(f"\nfiles ({len(ws.snapshot())}; `aos query` for the full catalog):")
    print(ws.tree())
    return 0


def cmd_describe(args) -> int:
    ws = Workspace.open(args.workspace)
    entry = ws.describe(args.path)
    if entry is None:
        print(f"{args.path}: no metadata recorded")
        return 1
    print(json.dumps(entry, indent=2))
    return 0


def cmd_log(args) -> int:
    ws = Workspace.open(args.workspace)
    for e in ws.history(args.n):
        print(f"{e['commit'][:12]}  {e['date']}  {e['message']}")
    return 0


def cmd_rollback(args) -> int:
    ws = Workspace.open(args.workspace)
    sha = ws.rollback(args.ref)
    print(f"workspace restored to {args.ref} (commit {sha[:12]})")
    return 0


def cmd_trace(args) -> int:
    records = AOS.open(args.workspace).trace(args.task, args.step)
    if args.json:
        print(json.dumps(records, indent=2, ensure_ascii=False))
        return 0
    if not records:
        print("no LLM calls recorded")
        return 0
    rows = []
    for i, r in enumerate(records, 1):
        u, resp = r.get("usage") or {}, r.get("response") or {}
        outcome = (f"error: {r['error']}" if r.get("error")
                   else ", ".join(c["name"] for c in resp.get("tool_calls") or []) or (resp.get("content") or "").strip())
        rows.append({"#": i, "time": r["time"][11:19], "task": r.get("task") or "-", "step": r.get("step") or "-",
                     "purpose": r.get("purpose") or "-", "model": r.get("model"), "msgs": r.get("messages"),
                     "in": u.get("input_tokens"), "out": u.get("output_tokens"), "cost": u.get("cost_usd"),
                     "ms": r.get("duration_ms"), "reply": outcome})
    print(format_rows(rows, max_width=80))
    if args.full:
        for i, r in enumerate(records, 1):
            print(f"\n===== call {i}: {r['time']} task {r.get('task') or '-'} step {r.get('step') or '-'} "
                  f"({r.get('purpose') or '-'}, {r.get('model')}, {r.get('duration_ms')} ms)"
                  + (" continues the previous call's conversation" if r.get("continues") else ""))
            for m in r.get("new_messages") or []:
                print(f"--- {m.get('role')}:\n{m.get('content') or json.dumps(m.get('tool_calls') or m, ensure_ascii=False)}")
            if r.get("error"):
                print(f"--- error: {r['error']}")
            else:
                resp = r.get("response") or {}
                calls = "".join(f"\n[tool call] {c['name']}({c['arguments']})" for c in resp.get("tool_calls") or [])
                print(f"--- assistant ({resp.get('finish_reason')}):\n{resp.get('content') or ''}{calls}")
    return 0


def cmd_ask(args) -> int:
    print(AOS.open(args.workspace, llm=LLM(model=args.model)).ask(args.question))
    return 0


def cmd_ui(args) -> int:
    from .capabilities import available_workers
    from .ui import serve

    llm = LLM(model=args.model)
    serve(args.path, llm, available_workers(llm), host=args.host, port=args.port, max_steps=args.max_steps)
    return 0


def cmd_workers(args) -> int:
    from .capabilities import all_workers

    load_env()
    try:
        llm = LLM()
    except RuntimeError as exc:
        print(f"warning: {exc}")
        llm = None
    for name, worker in all_workers(llm).items():
        ok, why = worker.available()
        print(f"{name:14s} {'available' if ok else 'unavailable: ' + why}")
    return 0

```
