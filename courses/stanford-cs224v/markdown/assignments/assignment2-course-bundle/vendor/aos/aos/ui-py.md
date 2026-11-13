# Homework 2 bundle: vendor/aos/aos/ui.py

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/ui.py) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/ui.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

````python
"""A small web interface: view workspaces, run goals, talk to the meta-assistant.

Standard library only: ``ThreadingHTTPServer`` serving one HTML page and a few JSON
endpoints. The server is pointed at a folder of workspaces (or at one workspace);
the page switches between them, creates new ones and adds files to them. Goals run
in a background thread per workspace; the page polls for progress.
"""

from __future__ import annotations

import json
import sqlite3
import os
import re
import shutil
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import prompts, trace
from .assistant import Assistant
from .capabilities.base import install_adapters
from .llm import ZERO_USAGE, add_usage
from .orchestrator import Orchestrator
from .tasks import Task
from .workspace import DB_FILE, IGNORED_DIRS, LEGACY_METADATA_FILE, Workspace, WorkspaceError, is_hidden, now

INDEX_HTML = Path(__file__).resolve().parent / "static" / "index.html"
DEFAULT_QUERY = "SELECT path, source, task, step, summary FROM files ORDER BY task, step, path"
#: Text files are returned whole up to this many characters (override with AOS_MAX_FILE_CHARS);
#: the page can ask for the rest with ?full=1.
MAX_TEXT_CHARS = int(os.environ.get("AOS_MAX_FILE_CHARS", "2000000"))
MAX_SQL_ROWS = 500

NL2SQL_PROMPT = prompts.load("nl2sql")


def _clean_sql(text: str) -> str:
    text = (text or "").strip()
    fenced = re.search(r"```(?:sql)?\s*(.*?)```", text, re.S)
    if fenced:
        text = fenced.group(1).strip()
    return text.strip().rstrip(";").strip()
#: Bumped whenever the page needs a route the server did not have before; the page compares it
#: with its own copy and asks for a restart when a running server is older than the page.
API_VERSION = 2
WORKSPACE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def is_workspace(path: Path) -> bool:
    return (path / DB_FILE).is_file() or (path / LEGACY_METADATA_FILE).is_file()


def resolve_root(path: str | Path) -> tuple[Path, str | None]:
    """``aos ui PATH``: a workspace serves itself with its parent as the root; anything else is a root."""
    p = Path(path).expanduser().resolve()
    if is_workspace(p):
        return p.parent, p.name
    return p, None


class App:
    """Everything the endpoints need for one workspace; independent of HTTP so it can be tested directly."""

    def __init__(self, ws: Workspace, llm, workers: dict, max_steps: int = 12):
        self.ws = ws
        self.llm = llm
        self.workers = workers
        self.max_steps = max_steps
        self.assistant = Assistant(ws, llm)
        Task.mark_interrupted(ws)  # runs left behind by an earlier process
        self.run: dict | None = None
        #: AOS calls outside tasks in this server session: assistant answers and file summaries.
        self.session_usage: dict = dict(ZERO_USAGE)
        #: The chat as this server session saw it: goals sent and questions answered.
        self.thread: list[dict] = []
        self._thread: threading.Thread | None = None
        self._lock = threading.Lock()

    # ------------------------------------------------------------------ viewing
    def is_running(self) -> bool:
        return bool(self._thread and self._thread.is_alive())

    def state(self) -> dict:
        tasks = []
        for task in Task.list(self.ws):
            steps = []
            for s in task.steps:
                steps.append({
                    "n": s["n"], "worker": s["worker"], "status": s["status"], "reason": s["reason"],
                    "instructions": s["instructions"], "inputs": s["inputs"],
                    "outputs": sorted(s["outputs"], key=lambda p: (is_hidden(p), p))[:8],
                    "output_count": len(s["outputs"]),
                    "summary": (s["summary"] or "")[:600], "error": (s["error"] or "")[:600],
                    "log": s["log"], "commit": s.get("commit"), "started": s["started"],
                    "duration": _seconds(s["started"], s["finished"]), "usage": s.get("usage"),
                })
            tasks.append({
                "id": task.id, "goal": task.goal, "status": task.data["status"],
                "result": task.data.get("result"), "created": task.data["created"],
                "duration": _seconds(task.data["created"], task.data.get("finished")),
                "steps": steps, "usage": task.data.get("usage"),
            })
        files = self.ws.query("SELECT count(*) AS n FROM files")[0]["n"]
        tasks_usage = add_usage(*[t["usage"] for t in tasks])
        total = add_usage(tasks_usage, self.session_usage)
        budget = self.budget()
        return {
            "api_version": API_VERSION,
            "budget_usd": budget,
            "root": str(self.ws.root), "name": self.ws.root.name, "goal": self.ws.goal,
            "head": self.ws.head()[:12], "model": getattr(self.llm, "model", ""), "files": files,
            "models": _models(self.llm), "prices": {m: list(p) for m, p in getattr(self.llm, "prices", {}).items()},
            "cost": {"total_usd": total["cost_usd"], "tasks_usd": tasks_usage["cost_usd"],
                     "session_usd": self.session_usage["cost_usd"], "tokens": total,
                     "unpriced_calls": total["unpriced_calls"], "budget_usd": budget,
                     "remaining_usd": None if budget is None else round(budget - total["cost_usd"], 6)},
            "max_steps": self.max_steps, "workers": sorted(self.workers), "tasks": tasks,
            "history": self.ws.history(30), "run": self.run_status(),
        }

    def tree(self) -> dict:
        """The workspace folder as a tree, each file carrying its catalog source and summary."""
        catalog = self.ws.files()

        def build(directory: Path, rel: str) -> list[dict]:
            nodes = []
            children = sorted(directory.iterdir(), key=lambda c: (not c.is_dir(), c.name.lower()))
            for child in children:
                if child.name in IGNORED_DIRS or child.name == ".gitkeep":
                    continue
                crel = f"{rel}/{child.name}" if rel else child.name
                if child.is_dir():
                    kids = build(child, crel)
                    nodes.append({"name": child.name, "path": crel, "type": "dir",
                                  "hidden": child.name.startswith("."), "children": kids,
                                  "count": sum(k["count"] if k["type"] == "dir" else 1 for k in kids)})
                else:
                    meta = catalog.get(crel)
                    if meta is None and (crel.startswith("tasks/") or crel.startswith("workspace.db")):
                        meta = {"source": "aos", "summary": "AOS record", "task": None, "step": None}
                    nodes.append({"name": child.name, "path": crel, "type": "file", "size": child.stat().st_size,
                                  "source": meta["source"] if meta else None,
                                  "summary": meta["summary"] if meta else "",
                                  "task": meta["task"] if meta else None, "step": meta["step"] if meta else None})
            return nodes

        kids = build(self.ws.root, "")
        return {"name": self.ws.root.name, "path": "", "type": "dir", "children": kids,
                "count": sum(k["count"] if k["type"] == "dir" else 1 for k in kids)}

    def query(self, sql: str) -> list[dict]:
        return self.ws.query(sql or DEFAULT_QUERY)

    def db_overview(self) -> dict:
        """What the database tab shows first: every table with its columns, counts and first rows."""
        overview = self.ws.schema()
        db = self.ws.root / DB_FILE
        overview.update(entry=self.ws.describe(DB_FILE), size=db.stat().st_size if db.is_file() else 0, path=DB_FILE)
        return overview

    def run_sql(self, sql: str, limit: int = MAX_SQL_ROWS) -> dict:
        """Run a read-only query and shape the result for a table: columns in order, rows capped."""
        sql = (sql or "").strip().rstrip(";")
        if not sql:
            raise WorkspaceError("write a SELECT statement first")
        rows = self.ws.query(sql)
        columns = list(rows[0].keys()) if rows else []
        return {"sql": sql, "columns": columns, "rows": rows[:limit], "total": len(rows), "truncated": len(rows) > limit}

    def nl2sql(self, question: str) -> dict:
        """Turn a plain-English question about the catalog into SQL with the configured model, run it,
        and return both; a query that fails to run comes back with its error so it can be edited."""
        if not (question or "").strip():
            raise WorkspaceError("ask a question first")
        schema = self.ws.schema(preview_rows=3)
        before = _snapshot(self.llm)
        with trace.context(trace.workspace_log(self.ws.root), purpose="nl2sql"):
            reply = self.llm.complete(NL2SQL_PROMPT.format(
                schema="\n".join(t["sql"] + ";" for t in schema["tables"]),
                counts=", ".join(f"{t['name']} {t['rows']}" for t in schema["tables"]),
                samples="\n".join(f"{name}: {json.dumps(p['rows'])}" for name, p in schema["preview"].items() if p["rows"]),
                question=question.strip()))
        used = _usage_since(self.llm, before)
        self.session_usage = add_usage(self.session_usage, used)
        sql = _clean_sql(reply)
        result = {"question": question.strip(), "sql": sql, "usage": used, "columns": [], "rows": [], "total": 0, "truncated": False}
        try:
            result.update(self.run_sql(sql))
        except (WorkspaceError, sqlite3.Error) as exc:
            result["error"] = f"{exc}"
        return result

    def tail(self, path: str, lines: int = 20) -> dict:
        """The last lines of a text file (a running step's log, mostly)."""
        p = self.ws.abspath(path)
        if not p.is_file():
            raise WorkspaceError(f"{path} is not a file")
        all_lines = p.read_text(errors="replace").splitlines()
        lines = max(1, min(int(lines), 200))
        return {"path": self.ws.relpath(p), "lines": all_lines[-lines:], "total": len(all_lines), "size": p.stat().st_size}

    def file(self, path: str, full: bool = False) -> dict:
        p = self.ws.abspath(path)
        if not p.is_file():
            raise WorkspaceError(f"{path} is not a file")
        raw = p.read_bytes()
        binary = b"\0" in raw[:4096]
        limit = len(raw) if full else MAX_TEXT_CHARS
        text = None if binary else raw[:limit].decode("utf-8", errors="replace")
        return {"path": self.ws.relpath(p), "entry": self.ws.describe(p), "size": len(raw), "binary": binary,
                "text": text, "truncated": (not binary) and len(raw) > limit, "limit": MAX_TEXT_CHARS}

    # ------------------------------------------------------------------ actions
    def add(self, name: str, data: bytes, reason: str) -> dict:
        """Save uploaded bytes as inputs/<name>, then catalog and commit the file."""
        name = Path(name).name
        if not name:
            raise WorkspaceError("a file name is required")
        dest = self.ws.root / "inputs" / name
        dest.write_bytes(data)
        return self._catalog_user_files([self.ws.relpath(dest)], reason)[0]

    def write(self, path: str, content: str, reason: str) -> dict:
        """Create or overwrite a text file inside the workspace (never AOS's own records), then catalog and commit.

        A new file is the user's. A file some worker produced becomes "mixed": the agent column keeps
        who made it, the edit is noted with a tag, a fresh summary and a commit.
        """
        rel = self.ws.relpath((path or "").strip() or "inputs/untitled.md")
        if rel.startswith((DB_FILE, "tasks/", ".git/")) or rel == "":
            raise WorkspaceError(f"{rel} is managed by AOS; choose a path under inputs/, generated/ or code/")
        existing = self.ws.describe(rel)
        dest = self.ws.abspath(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content or "")
        if existing and existing["source"] != "user":
            summaries = self._summarize([rel], f"file produced by {existing['agent']} and then edited by the user")
            entry = self.ws.mark_edited(rel, summaries.get(rel))
            self.ws.checkpoint(f"Edit {rel}")
            return entry
        return self._catalog_user_files([rel], reason or (existing["reason"] if existing else "Written by the user"))[0]

    def add_path(self, path: str, reason: str) -> dict:
        """Copy a file or folder from this machine into inputs/ (a path already inside the workspace is
        cataloged in place), then catalog and commit."""
        src = Path(path).expanduser()
        if not path.strip() or not src.exists():
            raise WorkspaceError(f"{path} does not exist")
        src = src.resolve()
        try:
            self.ws.relpath(src)
        except WorkspaceError:  # outside the workspace: copy it in
            dest = self.ws.root / "inputs" / src.name
            if src.is_dir():
                shutil.copytree(src, dest, dirs_exist_ok=True)
            else:
                shutil.copyfile(src, dest)
            src = dest
        files = [src] if src.is_file() else sorted(p for p in src.rglob("*") if p.is_file())
        rels = [self.ws.relpath(p) for p in files]
        entries = self._catalog_user_files(rels, reason)
        return {"added": rels, "count": len(entries)}

    def _summarize(self, rels: list[str], context: str) -> dict[str, str]:
        before = _snapshot(self.llm)
        with trace.context(trace.workspace_log(self.ws.root)):
            summaries = Orchestrator(self.ws, self.llm, {}, log=lambda _: None).summarize_files(rels, context)
        self.session_usage = add_usage(self.session_usage, _usage_since(self.llm, before))
        return summaries

    def _catalog_user_files(self, rels: list[str], reason: str) -> list[dict]:
        summaries = self._summarize(rels, "files placed in the workspace by the user as inputs")
        entries = [self.ws.register(rel, source="user", reason=reason or "Provided by the user",
                                    summary=summaries.get(rel, "")) for rel in rels]
        shown = ", ".join(rels[:3]) + (f" (+{len(rels) - 3} more)" if len(rels) > 3 else "")
        self.ws.checkpoint(f"Add {shown}")
        return entries

    def ask(self, message: str) -> str:
        before = _snapshot(self.llm)
        reply = self.assistant.ask(message)
        used = _usage_since(self.llm, before)
        self.session_usage = add_usage(self.session_usage, used)
        self.thread.append({"kind": "ask", "question": message, "reply": reply, "time": now(), "usage": used})
        return reply

    def message(self, text: str, mode: str = "auto") -> dict:
        """One chat box for both kinds of input: a goal starts a run, a question asks the assistant."""
        if not text.strip():
            raise WorkspaceError("a message is required")
        kind = mode if mode in ("run", "ask") else classify(text)
        if kind == "run":
            return {"kind": "run", "run": self.start_run(text)}
        return {"kind": "ask", "reply": self.ask(text)}

    def rollback(self, ref: str) -> dict:
        if self.is_running():
            raise RuntimeError("cannot roll back while a run is in progress")
        sha = self.ws.rollback(ref)
        self.thread.append({"kind": "rollback", "ref": ref, "head": sha, "time": now()})
        return {"head": sha}

    def budget(self) -> float | None:
        return self.ws.setting("budget_usd")

    def set_budget(self, value) -> float | None:
        if value in (None, "", 0, "0"):
            self.ws.set_setting("budget_usd", None)
            return None
        try:
            cap = float(value)
        except (TypeError, ValueError):
            raise WorkspaceError("the budget cap must be a number of US dollars") from None
        if cap <= 0:
            raise WorkspaceError("the budget cap must be positive (or empty for no cap)")
        self.ws.set_setting("budget_usd", cap)
        return cap

    def total_cost(self) -> float:
        """Estimated USD spent in this workspace: every task's usage plus this session's extras."""
        tasks = add_usage(*[t.data.get("usage") for t in Task.list(self.ws)])
        return round(tasks["cost_usd"] + self.session_usage["cost_usd"], 6)

    def start_run(self, goal: str, max_steps: int | None = None) -> dict:
        if not goal.strip():
            raise WorkspaceError("a goal is required")
        budget, spent = self.budget(), self.total_cost()
        if budget is not None and spent >= budget:
            raise RuntimeError(f"budget cap of ${budget:.2f} reached (about ${spent:.2f} spent); raise it in settings")
        with self._lock:
            if self.is_running():
                raise RuntimeError("a run is already in progress")
            limit = max_steps or self.max_steps
            self.run = {"goal": goal, "status": "running", "log": [], "task": None, "started": now(),
                        "max_steps": limit}
            self.thread.append({"kind": "goal", "text": goal, "run": self.run, "time": self.run["started"]})
            self._thread = threading.Thread(target=self._execute, args=(goal, limit), daemon=True)
            self._thread.start()
        return self.run_status()

    def _execute(self, goal: str, max_steps: int) -> None:
        run = self.run
        orch = Orchestrator(self.ws, self.llm, self.workers, max_steps=max_steps, log=run["log"].append,
                            budget_usd=self.budget(), spent_usd=self.total_cost())
        try:
            task = orch.run(goal)
            run.update(status=task.data["status"], task=task.id, result=task.data.get("result"))
        except Exception as exc:  # surface the failure in the UI instead of dying silently
            run["log"].append(f"run failed: {type(exc).__name__}: {exc}")
            run.update(status="failed", result=str(exc))

    def run_status(self) -> dict | None:
        if self.run is None:
            return None
        return _run_view(self.run)

    def thread_view(self) -> list[dict]:
        events = []
        for e in self.thread:
            if e["kind"] == "goal":
                events.append({"kind": "goal", "text": e["text"], "time": e["time"], "run": _run_view(e["run"])})
            else:
                events.append(e)
        return events


class Hub:
    """The folder of workspaces the server manages, with one App per workspace."""

    def __init__(self, root: str | Path, llm, workers: dict, max_steps: int = 12, default: str | None = None):
        self.root = Path(root).expanduser().resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.llm = llm
        self.workers = workers
        self.max_steps = max_steps
        self.default = default
        self.apps: dict[str, App] = {}
        self._lock = threading.Lock()

    def names(self) -> list[str]:
        return sorted(d.name for d in self.root.iterdir() if d.is_dir() and is_workspace(d))

    def app(self, name: str | None = None) -> App:
        names = self.names()
        name = name or self.default or (names[0] if names else None)
        if not name:
            raise WorkspaceError("no workspace yet: create one first")
        if name not in names:
            raise WorkspaceError(f"no workspace named {name!r} under {self.root}")
        with self._lock:
            if name not in self.apps:
                self.apps[name] = App(Workspace.open(self.root / name), self.llm, self.workers, self.max_steps)
            return self.apps[name]

    def list(self) -> list[dict]:
        return [self.info(name) for name in self.names()]

    def info(self, name: str) -> dict:
        ws = self.apps[name].ws if name in self.apps else Workspace.open(self.root / name)
        tasks = Task.list(ws)
        last = tasks[-1] if tasks else None
        history = ws.history(1)
        return {
            "name": name, "path": str(ws.root), "goal": ws.goal, "tasks": len(tasks),
            "files": ws.query("SELECT count(*) AS n FROM files")[0]["n"],
            "last_task": {"id": last.id, "status": last.data["status"], "goal": last.goal} if last else None,
            "running": name in self.apps and self.apps[name].is_running(),
            "updated": history[0]["date"] if history else None,
        }

    def models(self) -> list[str]:
        return _models(self.llm)

    def set_model(self, name: str) -> str:
        """Switch the model for every later call: planner, agents, assistant and the external runners."""
        if name not in self.models():
            raise WorkspaceError(f"unknown model {name!r}; available: {', '.join(self.models())}")
        if any(app.is_running() for app in self.apps.values()):
            raise RuntimeError("cannot switch models while a run is in progress; wait for it to finish")
        self.llm.model = name
        os.environ["AOS_MODEL"] = name
        return name

    def create(self, name: str, goal: str | None = None) -> dict:
        name = (name or "").strip()
        if not WORKSPACE_NAME.match(name):
            raise WorkspaceError("workspace names use letters, digits, dots, dashes and underscores")
        path = self.root / name
        if path.exists():
            raise WorkspaceError(f"{path} already exists")
        ws = Workspace.create(path, goal=(goal or "").strip() or None)
        install_adapters(ws)
        ws.checkpoint("Install adapter scripts")
        if self.default is None:
            self.default = name
        return self.info(name)


class Handler(BaseHTTPRequestHandler):
    server: "UIServer"

    def _app(self, params: dict) -> App:
        return self.server.hub.app(params.get("ws", [None])[0])

    def do_GET(self) -> None:
        url = urlparse(self.path)
        params = parse_qs(url.query)
        hub = self.server.hub
        try:
            if url.path == "/":
                self._send(200, INDEX_HTML.read_bytes(), "text/html; charset=utf-8")
            elif url.path == "/api/workspaces":
                self._json({"root": str(hub.root), "default": hub.default, "workspaces": hub.list()})
            elif url.path == "/api/models":
                self._json({"models": hub.models(), "current": getattr(hub.llm, "model", None)})
            elif url.path == "/api/state":
                self._json(self._app(params).state())
            elif url.path == "/api/query":
                self._json({"rows": self._app(params).query(params.get("sql", [""])[0])})
            elif url.path == "/api/file":
                self._json(self._app(params).file(params["path"][0], full=params.get("full", ["0"])[0] == "1"))
            elif url.path == "/api/tail":
                self._json(self._app(params).tail(params["path"][0], int(params.get("lines", ["20"])[0])))
            elif url.path == "/api/db":
                self._json(self._app(params).db_overview())
            elif url.path == "/api/run":
                self._json({"run": self._app(params).run_status()})
            elif url.path == "/api/tree":
                self._json(self._app(params).tree())
            elif url.path == "/api/thread":
                self._json({"events": self._app(params).thread_view()})
            elif url.path == "/api/assistant":
                self._json({"messages": self._app(params).assistant.history})
            elif url.path == "/api/settings":
                app = self._app(params)
                self._json({"budget_usd": app.budget(), "spent_usd": app.total_cost()})
            else:
                self._json({"error": "not found"}, 404)
        except (WorkspaceError, KeyError, ValueError) as exc:
            self._json({"error": str(exc)}, 400)

    def do_POST(self) -> None:
        url = urlparse(self.path)
        params = parse_qs(url.query)
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        hub = self.server.hub
        try:
            if url.path == "/api/workspaces":
                data = json.loads(body or b"{}")
                self._json({"workspace": hub.create(data.get("name", ""), data.get("goal"))})
                return
            if url.path == "/api/models":
                data = json.loads(body or b"{}")
                self._json({"current": hub.set_model(data.get("model", ""))})
                return
            app = self._app(params)
            if url.path == "/api/run":
                data = json.loads(body or b"{}")
                self._json({"run": app.start_run(data.get("goal", ""), int(data.get("max_steps") or 0) or None)})
            elif url.path == "/api/assistant":
                data = json.loads(body or b"{}")
                self._json({"reply": app.ask(data.get("message", ""))})
            elif url.path == "/api/message":
                data = json.loads(body or b"{}")
                self._json(app.message(data.get("message", ""), data.get("mode", "auto")))
            elif url.path == "/api/rollback":
                data = json.loads(body or b"{}")
                if not data.get("ref"):
                    raise WorkspaceError("a commit is required")
                self._json(app.rollback(data["ref"]))
            elif url.path == "/api/add":
                entry = app.add(params.get("name", [""])[0], body, params.get("reason", [""])[0])
                self._json({"entry": entry})
            elif url.path == "/api/add-path":
                data = json.loads(body or b"{}")
                self._json(app.add_path(data.get("path", ""), data.get("reason", "")))
            elif url.path == "/api/write":
                data = json.loads(body or b"{}")
                self._json({"entry": app.write(data.get("path", ""), data.get("content", ""), data.get("reason", ""))})
            elif url.path == "/api/settings":
                data = json.loads(body or b"{}")
                self._json({"budget_usd": app.set_budget(data.get("budget_usd")), "spent_usd": app.total_cost()})
            elif url.path == "/api/sql":
                try:
                    self._json(app.run_sql(json.loads(body or b"{}").get("sql", "")))
                except sqlite3.Error as exc:
                    self._json({"error": f"SQL error: {exc}"}, 400)
            elif url.path == "/api/nl2sql":
                self._json(app.nl2sql(json.loads(body or b"{}").get("question", "")))
            else:
                self._json({"error": "not found"}, 404)
        except RuntimeError as exc:
            self._json({"error": str(exc)}, 409)
        except (WorkspaceError, KeyError, ValueError) as exc:
            self._json({"error": str(exc)}, 400)

    def log_message(self, format, *args) -> None:  # keep the terminal quiet
        pass

    def _json(self, data, status: int = 200) -> None:
        self._send(status, json.dumps(data, default=str).encode(), "application/json")

    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


class UIServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, hub: Hub, host: str = "127.0.0.1", port: int = 8765):
        super().__init__((host, port), Handler)
        self.hub = hub

    @property
    def url(self) -> str:
        host, port = self.server_address[:2]
        return f"http://{host}:{port}"


def serve(path: str | Path, llm, workers: dict, host: str = "127.0.0.1", port: int = 8765,
          max_steps: int = 12) -> None:
    root, default = resolve_root(path)
    hub = Hub(root, llm, workers, max_steps, default)
    names = hub.names()
    what = f"workspace {default}" if default else (f"{len(names)} workspace(s)" if names else "no workspaces yet")
    server = UIServer(hub, host, port)
    print(f"AOS UI at {server.url} for {root} ({what}); Ctrl-C to stop", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def _models(llm) -> list[str]:
    if hasattr(llm, "available_models"):
        return list(llm.available_models())
    return [getattr(llm, "model", "")]


def _snapshot(llm) -> dict | None:
    return llm.snapshot() if hasattr(llm, "snapshot") else None


def _usage_since(llm, snapshot: dict | None) -> dict:
    if snapshot is None or not hasattr(llm, "usage_since"):
        return dict(ZERO_USAGE)
    return llm.usage_since(snapshot)


def _run_view(run: dict) -> dict:
    view = {k: v for k, v in run.items()}
    if not view.get("task"):  # the orchestrator announces the task id in its first log line
        for line in run["log"][:3]:
            m = re.match(r"\[(task-\d+)\]", line)
            if m:
                view["task"] = m.group(1)
                break
    return view


QUESTION_WORDS = ("what", "why", "how", "which", "where", "when", "who", "is", "are", "does", "do", "did",
                  "can", "could", "should", "would", "explain", "list", "show", "tell", "summarize")


def classify(text: str) -> str:
    """Auto mode: a question goes to the assistant, anything else is a goal to run."""
    t = text.strip()
    first = re.split(r"[\s,:]+", t.lower(), maxsplit=1)[0] if t else ""
    return "ask" if t.endswith("?") or first in QUESTION_WORDS else "run"


def _seconds(start: str | None, end: str | None) -> float | None:
    if not start:
        return None
    try:
        a = datetime.fromisoformat(start)
        b = datetime.fromisoformat(end) if end else datetime.now(a.tzinfo)
    except ValueError:
        return None
    return round((b - a).total_seconds(), 1)

````
