# Homework 2 bundle: vendor/aos/aos/workspace.py

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/workspace.py) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/workspace.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""The workspace: a git-backed folder that is the entire state of an AOS run.

Every source document, intermediate result, report, database, script and
answer lives here as a file. ``workspace.db`` (SQLite) is the catalog: one row
per file saying what it is, why it exists, where it came from and how it
relates to the task, plus a link table of the files it was derived from. Git
provides history, diffs and rollback.
"""

from __future__ import annotations

import json
import os
import posixpath
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path

STANDARD_DIRS = ["inputs", "sources", "generated", "tasks", "code", "workflows"]
DB_FILE = "workspace.db"
LEGACY_METADATA_FILE = "metadata.json"

# Directories that are never work products: skipped when discovering files.
IGNORED_DIRS = {".git", "__pycache__", "node_modules", ".pytest_cache"}
# Top-level directory holding AOS's own task records and step logs.
TASKS_DIR = "tasks"
# Top-level directory that belongs to the user: anything appearing there is user-provided input.
INPUTS_DIR = "inputs"

FILE_TYPES = {
    ".md": "markdown", ".txt": "text", ".csv": "csv", ".tsv": "tsv", ".json": "json",
    ".jsonl": "jsonl", ".pdf": "pdf", ".py": "python", ".sh": "shell", ".db": "sqlite",
    ".sqlite": "sqlite", ".png": "image", ".jpg": "image", ".jpeg": "image", ".html": "html",
    ".yaml": "yaml", ".yml": "yaml", ".toml": "toml", ".ipynb": "notebook",
}

SCHEMA = """
CREATE TABLE IF NOT EXISTS workspace (
    key   TEXT PRIMARY KEY,
    value TEXT
);
CREATE TABLE IF NOT EXISTS files (
    path    TEXT PRIMARY KEY,   -- workspace-relative path
    type    TEXT NOT NULL,      -- markdown, csv, json, pdf, python, image, ...
    source  TEXT NOT NULL,      -- worker or system that produced it: user, storm, sliders, coding_agent, ...
    agent   TEXT,               -- agent/module that created it (usually = source)
    task    TEXT,               -- task-NNN it belongs to
    step    INTEGER,            -- step number within that task
    reason  TEXT,               -- why the file exists (the step's purpose)
    summary TEXT,               -- one sentence: what it contains
    tags    TEXT,               -- JSON list
    size    INTEGER,            -- bytes
    created TEXT NOT NULL,      -- ISO timestamps
    updated TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS file_inputs (
    path  TEXT NOT NULL REFERENCES files(path) ON DELETE CASCADE,
    input TEXT NOT NULL,        -- workspace-relative path of a file this one was derived from
    PRIMARY KEY (path, input)
);
"""

FILE_COLUMNS = ("path", "type", "source", "agent", "task", "step", "reason", "summary", "tags",
                "size", "created", "updated")


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def file_type(path: str) -> str:
    suffix = Path(path).suffix.lower()
    return FILE_TYPES.get(suffix, suffix.lstrip(".") or "file")


def is_hidden(rel: str) -> bool:
    """Files under a dot-directory (caches, stores) are kept and registered but not listed."""
    return any(part.startswith(".") for part in rel.split("/")[:-1])


class WorkspaceError(Exception):
    pass


class Workspace:
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()

    # ------------------------------------------------------------------ lifecycle
    @classmethod
    def create(cls, root: str | Path, goal: str | None = None) -> "Workspace":
        ws = cls(root)
        ws.root.mkdir(parents=True, exist_ok=True)
        for d in STANDARD_DIRS:
            (ws.root / d).mkdir(exist_ok=True)
            (ws.root / d / ".gitkeep").touch()
        ws._migrate_legacy_json()
        if not ws.db_path.exists():
            ws._init_db(goal)
        if not (ws.root / ".git").exists():
            ws.git("init", "-q")
            ws.git("config", "user.name", "AOS")
            ws.git("config", "user.email", "aos@localhost")
        ws.checkpoint("Initialize workspace")
        return ws

    @classmethod
    def open(cls, root: str | Path) -> "Workspace":
        ws = cls(root)
        ws._migrate_legacy_json()
        if not ws.db_path.exists() or not (ws.root / ".git").exists():
            raise WorkspaceError(f"{ws.root} is not an AOS workspace (run `aos init` first)")
        return ws

    @property
    def db_path(self) -> Path:
        return self.root / DB_FILE

    def _connect(self, readonly: bool = False) -> sqlite3.Connection:
        if readonly:
            conn = sqlite3.connect(self.db_path.as_uri() + "?mode=ro", uri=True)  # as_uri() escapes # ? %
        else:
            conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def _init_db(self, goal: str | None, created: str | None = None) -> None:
        with self._connect() as conn:
            conn.executescript(SCHEMA)
            conn.execute("INSERT OR REPLACE INTO workspace VALUES ('created', ?)", (created or now(),))
            conn.execute("INSERT OR REPLACE INTO workspace VALUES ('goal', ?)", (goal,))

    def _migrate_legacy_json(self) -> None:
        """Import a metadata.json written by earlier versions into workspace.db."""
        legacy = self.root / LEGACY_METADATA_FILE
        if not legacy.exists() or self.db_path.exists():
            return
        data = json.loads(legacy.read_text())
        self._init_db(data.get("goal"), data.get("created"))
        for entry in data.get("files", {}).values():
            self._upsert(entry)
        legacy.unlink()

    def setting(self, key: str, default=None):
        """A per-workspace setting (JSON value) kept in the catalog database."""
        with self._connect(readonly=True) as conn:
            row = conn.execute("SELECT value FROM workspace WHERE key = ?", (f"setting.{key}",)).fetchone()
        return json.loads(row["value"]) if row and row["value"] is not None else default

    def set_setting(self, key: str, value) -> None:
        with self._connect() as conn:
            conn.execute("INSERT OR REPLACE INTO workspace VALUES (?, ?)", (f"setting.{key}", json.dumps(value)))

    @property
    def goal(self) -> str | None:
        with self._connect(readonly=True) as conn:
            row = conn.execute("SELECT value FROM workspace WHERE key = 'goal'").fetchone()
        return row["value"] if row else None

    # ---------------------------------------------------------------------- paths
    def relpath(self, path: str | Path) -> str:
        """Workspace-relative posix path; rejects anything outside the workspace."""
        p = Path(path)
        p = (p if p.is_absolute() else self.root / p).resolve()
        try:
            return p.relative_to(self.root).as_posix()
        except ValueError:
            raise WorkspaceError(f"{path} is outside the workspace {self.root}") from None

    def abspath(self, path: str | Path) -> Path:
        return self.root / self.relpath(path)

    # -------------------------------------------------------------------- catalog
    def register(
        self,
        path: str | Path,
        *,
        source: str,
        reason: str,
        summary: str = "",
        task: str | None = None,
        step: int | None = None,
        agent: str | None = None,
        inputs: list[str] | tuple[str, ...] = (),
        tags: list[str] | tuple[str, ...] = (),
    ) -> dict:
        """Record what a file is, why it exists and where it came from."""
        rel = self.relpath(path)
        abs_path = self.abspath(rel)
        entry = {
            "path": rel,
            "type": file_type(rel),
            "source": source,
            "reason": reason,
            "summary": summary,
            "task": task,
            "step": step,
            "agent": agent or source,
            "inputs": [self.relpath(i) for i in inputs],
            "tags": list(tags),
            "created": now(),
            "updated": now(),
            "size": abs_path.stat().st_size if abs_path.is_file() else None,
        }
        return self._upsert(entry)

    def _upsert(self, entry: dict) -> dict:
        with self._connect() as conn:
            previous = conn.execute("SELECT created FROM files WHERE path = ?", (entry["path"],)).fetchone()
            created = previous["created"] if previous else entry.get("created") or now()
            conn.execute(
                "INSERT OR REPLACE INTO files (path, type, source, agent, task, step, reason, summary, "
                "tags, size, created, updated) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (entry["path"], entry.get("type") or file_type(entry["path"]), entry["source"],
                 entry.get("agent") or entry["source"], entry.get("task"), entry.get("step"),
                 entry.get("reason", ""), entry.get("summary", ""), json.dumps(entry.get("tags", [])),
                 entry.get("size"), created, entry.get("updated") or now()),
            )
            conn.execute("DELETE FROM file_inputs WHERE path = ?", (entry["path"],))
            conn.executemany("INSERT OR IGNORE INTO file_inputs VALUES (?, ?)",
                             [(entry["path"], i) for i in entry.get("inputs", [])])
        return self.describe(entry["path"])

    def describe(self, path: str | Path) -> dict | None:
        rel = self.relpath(path)
        with self._connect(readonly=True) as conn:
            row = conn.execute("SELECT * FROM files WHERE path = ?", (rel,)).fetchone()
            if row is None:
                return None
            inputs = [r["input"] for r in conn.execute(
                "SELECT input FROM file_inputs WHERE path = ? ORDER BY input", (rel,))]
        return _entry(row, inputs)

    def files(self) -> dict[str, dict]:
        """All registered files, keyed by workspace-relative path."""
        with self._connect(readonly=True) as conn:
            inputs: dict[str, list[str]] = {}
            for r in conn.execute("SELECT path, input FROM file_inputs ORDER BY path, input"):
                inputs.setdefault(r["path"], []).append(r["input"])
            return {row["path"]: _entry(row, inputs.get(row["path"], []))
                    for row in conn.execute("SELECT * FROM files ORDER BY path")}

    def unregistered(self) -> list[str]:
        registered = self.files()
        return sorted(p for p in self.snapshot() if p not in registered)

    def prune_metadata(self) -> list[str]:
        """Drop catalog rows whose file no longer exists. Returns the dropped paths."""
        with self._connect() as conn:
            gone = [r["path"] for r in conn.execute("SELECT path FROM files")
                    if not self.abspath(r["path"]).is_file()]
            conn.executemany("DELETE FROM files WHERE path = ?", [(p,) for p in gone])
        return gone

    def schema(self, preview_rows: int = 25) -> dict:
        """The catalog's tables: columns, row counts, CREATE statements and the first rows of each."""
        tables, preview = [], {}
        with self._connect(readonly=True) as conn:
            for row in conn.execute("SELECT name, sql FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"):
                name = row["name"]
                columns = [{"name": c["name"], "type": c["type"]} for c in conn.execute(f'PRAGMA table_info("{name}")')]
                count = conn.execute(f'SELECT COUNT(*) AS n FROM "{name}"').fetchone()["n"]
                rows = [dict(r) for r in conn.execute(f'SELECT * FROM "{name}" LIMIT ?', (preview_rows,))]
                tables.append({"name": name, "rows": count, "columns": columns, "sql": row["sql"]})
                preview[name] = {"columns": [c["name"] for c in columns], "rows": rows}
        return {"tables": tables, "preview": preview}

    def query(self, sql: str, params: tuple = ()) -> list[dict]:
        """Run a read-only SQL query against the catalog and return rows as dicts."""
        if not sql.lstrip().lower().startswith(("select", "with", "explain")):
            raise WorkspaceError("only SELECT queries are allowed on the catalog")
        try:
            with self._connect(readonly=True) as conn:
                return [dict(r) for r in conn.execute(sql, params).fetchall()]
        except sqlite3.Error as exc:
            raise WorkspaceError(f"query failed: {exc}") from None

    # ------------------------------------------------------------------ discovery
    def snapshot(self) -> dict[str, tuple[int, int]]:
        """Every work-product file with its (mtime_ns, size) signature.

        Skips git internals, the catalog database and the ``tasks/`` records, so
        that diffing two snapshots yields exactly the files a step produced.
        Caches and stores under dot-directories are work products too: everything
        an agent fetched or built stays in the workspace.
        """
        snap: dict[str, tuple[int, int]] = {}
        for dirpath, dirnames, filenames in os.walk(self.root):
            rel_dir = Path(dirpath).relative_to(self.root).as_posix()
            dirnames[:] = sorted(
                d for d in dirnames
                if d not in IGNORED_DIRS and not (rel_dir == "." and d == TASKS_DIR)
            )
            for name in filenames:
                if name == ".gitkeep":
                    continue
                if rel_dir == "." and (name.startswith(DB_FILE) or name == LEGACY_METADATA_FILE):
                    continue
                full = os.path.join(dirpath, name)
                if os.path.islink(full):  # symlinks (a venv's python, say) point elsewhere: not cataloged
                    continue
                rel = name if rel_dir == "." else f"{rel_dir}/{name}"
                st = os.stat(full)
                snap[rel] = (st.st_mtime_ns, st.st_size)
        return snap

    def changed_since(self, before: dict[str, tuple[int, int]]) -> list[str]:
        """Files that are new or modified relative to an earlier snapshot."""
        after = self.snapshot()
        return sorted(p for p, sig in after.items() if before.get(p) != sig)

    def tree(self, limit: int = 300, collapse_after: int = 12) -> str:
        """Human/LLM-readable listing: every file with its registered provenance.

        Directories holding more than ``collapse_after`` files (run transcripts, downloaded
        sources) are shown as a few examples plus a count, and dot-directories (caches,
        stores) as one line with a count, so prompts stay readable.
        """
        registered = self.files()
        by_dir: dict[str, list[str]] = {}
        hidden: dict[str, list[str]] = {}
        for rel in sorted(self.snapshot()):
            if is_hidden(rel):
                parts = rel.split("/")
                top = "/".join(parts[:next(i for i, p in enumerate(parts) if p.startswith(".")) + 1])
                hidden.setdefault(top, []).append(rel)
            else:
                by_dir.setdefault(posixpath.dirname(rel), []).append(rel)
        lines: list[str] = []
        for directory in sorted(by_dir):
            paths = by_dir[directory]
            shown = paths if len(paths) <= collapse_after else paths[:5]
            for rel in shown:
                meta = registered.get(rel)
                desc = f"[{meta['source']}] {meta['summary'] or meta['reason']}" if meta else "(unregistered)"
                lines.append(f"{rel} — {desc}")
            if len(paths) > collapse_after:
                lines.append(f"{directory or '.'}/... — {len(paths) - len(shown)} more files like these")
        for directory in sorted(hidden):
            meta = registered.get(hidden[directory][0])
            source = f"[{meta['source']}] " if meta else ""
            lines.append(f"{directory}/ — {source}{len(hidden[directory])} cache/store files (hidden)")
        if len(lines) > limit:
            lines = lines[:limit] + [f"... and {len(lines) - limit} more entries"]
        return "\n".join(lines) if lines else "(empty workspace)"

    # ------------------------------------------------------------------------ git
    def git(self, *args: str, check: bool = True) -> str:
        result = subprocess.run(["git", *args], cwd=self.root, capture_output=True, text=True)
        if check and result.returncode != 0:
            raise WorkspaceError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
        return result.stdout.strip()

    def head(self) -> str:
        return self.git("rev-parse", "HEAD")

    def has_changes(self) -> bool:
        return bool(self.git("status", "--porcelain"))

    def modified(self) -> list[str]:
        """Committed files whose content changed on disk since the last checkpoint (deleted ones excluded)."""
        return sorted(line for line in self.git("diff", "--name-only", "-z", "HEAD").split("\0")  # -z: no quoting
                      if line and not line.startswith((DB_FILE, TASKS_DIR + "/")) and self.abspath(line).is_file())

    def mark_edited(self, path: str | Path, summary: str | None = None) -> dict:
        """A worker's file was changed by hand: its source becomes "mixed" (the ``agent`` column keeps
        who produced it), it is tagged edited-by-user and its summary can be refreshed."""
        existing = self.describe(path)
        if existing is None:
            raise WorkspaceError(f"{self.relpath(path)} is not in the catalog")
        source = "user" if existing["source"] == "user" else "mixed"
        return self.register(existing["path"], source=source, reason=existing["reason"],
                             summary=summary or existing["summary"], task=existing["task"], step=existing["step"],
                             agent=existing["agent"], inputs=existing["inputs"],
                             tags=sorted(set(existing["tags"]) | ({"edited-by-user"} if source == "mixed" else set())))

    def checkpoint(self, message: str) -> str | None:
        """Commit everything. Returns the new commit sha, or None if nothing changed."""
        self.git("add", "-A")
        if not self.git("status", "--porcelain"):
            return None
        self.git("commit", "-q", "-m", message)
        return self.head()

    def history(self, n: int = 20) -> list[dict]:
        out = self.git("log", f"-{n}", "--format=%H%x1f%aI%x1f%s")
        entries = []
        for line in out.splitlines():
            sha, date, message = line.split("\x1f", 2)
            entries.append({"commit": sha, "date": date, "message": message})
        return entries

    def rollback(self, ref: str) -> str:
        """Return the workspace to the state at ``ref`` as a new commit.

        The task records under ``tasks/`` are kept as they are, so the audit
        trail survives; everything else (files and catalog) is restored.
        """
        self.checkpoint("Checkpoint before rollback")
        previous = self.head()
        self.git("read-tree", "-u", "--reset", ref)
        if self.git("ls-tree", previous, TASKS_DIR):
            self.git("checkout", previous, "--", TASKS_DIR)
        return self.checkpoint(f"Rollback workspace to {ref[:12]}") or self.head()


def _entry(row: sqlite3.Row, inputs: list[str]) -> dict:
    entry = {k: row[k] for k in FILE_COLUMNS}
    entry["tags"] = json.loads(entry["tags"] or "[]")
    entry["inputs"] = inputs
    return entry


def format_rows(rows: list[dict], max_width: int = 60) -> str:
    """Render query results as an aligned text table."""
    if not rows:
        return "(no rows)"
    columns = list(rows[0])

    def cell(value) -> str:
        text = "" if value is None else str(value).replace("\n", " ")
        return text if len(text) <= max_width else text[:max_width - 1] + "…"

    table = [[cell(r.get(c)) for c in columns] for r in rows]
    widths = [max(len(c), *(len(t[i]) for t in table)) for i, c in enumerate(columns)]
    lines = ["  ".join(c.ljust(widths[i]) for i, c in enumerate(columns)),
             "  ".join("-" * w for w in widths)]
    lines += ["  ".join(t[i].ljust(widths[i]) for i in range(len(columns))) for t in table]
    return "\n".join(lines)

```
