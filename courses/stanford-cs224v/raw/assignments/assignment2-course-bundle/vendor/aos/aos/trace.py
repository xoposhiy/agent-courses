"""Per-call records of every LLM request AOS makes (the trace), kept in the workspace.

``LLM.chat`` appends one JSON line per call to the file named by the current trace context:
``tasks/task-NNN/llm-calls.jsonl`` during a task, ``tasks/llm-calls.jsonl`` for calls outside
tasks (assistant, natural-language SQL, upload summaries). Contexts are per thread, so a run in
the UI's background thread and a question answered from a request thread never mix.
"""

from __future__ import annotations

import json
import threading
from contextlib import contextmanager
from pathlib import Path

from .workspace import TASKS_DIR, now

TRACE_FILE = "llm-calls.jsonl"
#: Longest message or reply text kept in a record; the rest is cut with a marker.
MAX_TEXT = 50_000

_local = threading.local()


def workspace_log(root: Path) -> Path:
    """Where calls outside any task are recorded."""
    return Path(root) / TASKS_DIR / TRACE_FILE


@contextmanager
def context(path: Path | None = None, **tags):
    """Record calls made in this thread (within the block) to ``path`` with these tags.

    A nested context inherits the outer path and tags and may add or override tags.
    """
    outer = current()
    inner = {**outer, **tags}
    if path is not None:
        inner["path"] = Path(path)
    stack = _stack()
    stack.append(inner)
    try:
        yield
    finally:
        stack.pop()


def current() -> dict:
    stack = _stack()
    return stack[-1] if stack else {}


def _stack() -> list[dict]:
    if not hasattr(_local, "stack"):
        _local.stack = []
    return _local.stack


def record(messages: list[dict], response: dict | None, *, model: str, duration_ms: int, usage: dict | None,
           error: str | None = None, json_mode: bool = False, tools: list[str] | None = None) -> None:
    """Append one call to the current trace file; a no-op when no context is active."""
    ctx = current()
    path = ctx.get("path")
    if path is None:
        return
    previous = getattr(_local, "last_messages", None)
    continues = previous is not None and len(messages) > len(previous) and messages[:len(previous)] == previous
    new_messages = messages[len(previous):] if continues else messages
    _local.last_messages = list(messages)
    entry = {
        "time": now(), "duration_ms": duration_ms,
        **{k: v for k, v in ctx.items() if k != "path"},
        "model": model, "json_mode": json_mode, "tools": tools or [],
        "messages": len(messages), "continues": continues,
        "new_messages": [_trim_message(m) for m in new_messages],
        "response": response, "usage": usage, "error": error,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False, default=str) + "\n")


def read(path: Path) -> list[dict]:
    """The records in one trace file (missing file: none)."""
    path = Path(path)
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _trim_message(message: dict) -> dict:
    out = dict(message)
    if isinstance(out.get("content"), str):
        out["content"] = trim(out["content"])
    return out


def trim(text: str, limit: int = MAX_TEXT) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n... [{len(text) - limit} characters cut from the trace]"
