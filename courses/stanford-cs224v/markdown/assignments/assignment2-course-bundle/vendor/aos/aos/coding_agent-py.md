# Homework 2 bundle: vendor/aos/aos/coding_agent.py

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/coding_agent.py) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/coding_agent.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""A general-purpose coding agent that works directly inside the workspace.

It is a plain tool-calling loop on the configured Gemini model with five tools:
list_files, read_file, write_file, replace_in_file and run_shell. Everything it
touches is a workspace file; AOS commits its work when the step finishes.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from . import prompts
from .tasks import Step
from .worker import Worker
from .workspace import DB_FILE, IGNORED_DIRS, TASKS_DIR, Workspace, WorkspaceError, format_rows

MAX_TOOL_OUTPUT = 12_000
PROTECTED = (DB_FILE, TASKS_DIR + "/", ".git/")

TOOLS = [
    {"type": "function", "function": {
        "name": "query_metadata",
        "description": (
            "Run a read-only SQL SELECT on the workspace catalog (SQLite). Table files(path, type, "
            "source, agent, task, step, reason, summary, tags, size, created, updated) has one row per "
            "workspace file: what it is, why it exists and which worker/task/step produced it (source "
            "'user' = provided by the user, 'mixed' = produced by the worker in `agent` and then edited "
            "by the user, so the user's version is authoritative). Table "
            "file_inputs(path, input) lists the files each file was derived from. Use it to understand "
            "the workspace before reading files, e.g. SELECT path, summary FROM files WHERE source='storm'."),
        "parameters": {"type": "object", "properties": {"sql": {"type": "string"}}, "required": ["sql"]}}},
    {"type": "function", "function": {
        "name": "list_files",
        "description": "List files under a workspace directory (recursively) with their sizes.",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string", "description": "Workspace-relative directory, default '.'"}},
            "required": []}}},
    {"type": "function", "function": {
        "name": "read_file",
        "description": "Read a text file from the workspace. Returns at most max_lines lines starting at start_line.",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"},
            "start_line": {"type": "integer", "description": "1-based first line, default 1"},
            "max_lines": {"type": "integer", "description": "default 300"}},
            "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "write_file",
        "description": "Create or overwrite a workspace file with the given content (parent directories are created).",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"}, "content": {"type": "string"}},
            "required": ["path", "content"]}}},
    {"type": "function", "function": {
        "name": "replace_in_file",
        "description": "Replace one exact, unique occurrence of `old` with `new` in a workspace file.",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"}, "old": {"type": "string"}, "new": {"type": "string"}},
            "required": ["path", "old", "new"]}}},
    {"type": "function", "function": {
        "name": "run_shell",
        "description": "Run a bash command with the workspace root as working directory; returns exit code, stdout and stderr. `python` has the openai and pandas packages and API_KEY/BASE_URL/AOS_MODEL in its environment.",
        "parameters": {"type": "object", "properties": {
            "command": {"type": "string"},
            "timeout": {"type": "integer", "description": "seconds, default 600"}},
            "required": ["command"]}}},
]

SYSTEM_PROMPT = prompts.load("coding_agent_system")
TURN_LIMIT_PROMPT = prompts.load("coding_agent_turn_limit")


class CodingAgent(Worker):
    name = "coding_agent"
    description = (
        "General-purpose coding agent working directly inside the workspace with file and shell "
        "tools (Python available). Use it to inspect or analyze files, write and run small "
        "transformation or analysis scripts, convert formats, connect the outputs of other workers, "
        "write notes/reports/decisions from workspace files, debug failed steps and fix adapter code. "
        "instructions = what to do and what to produce; inputs = files it must read; "
        "output_dir = where its new files go."
    )

    def __init__(self, llm, max_turns: int = 40, shell_timeout: int = 600):
        self.llm = llm
        self.max_turns = max_turns
        self.shell_timeout = shell_timeout

    def run(self, ws: Workspace, step: Step, log: Path, goal: str = "") -> str:
        inputs = ", ".join(step.inputs) if step.inputs else "none specified"
        user = (
            f"Overall goal of the task: {goal or '(not given)'}\n\n"
            f"Instructions for this step:\n{step.instructions}\n\n"
            f"Input files: {inputs}\nOutput directory: {step.output_dir}\n\n"
            f"Workspace files (path — provenance):\n{ws.tree(limit=200)}"
        )
        messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user}]
        self._log(log, f"[coding_agent] {step.instructions}\n")

        for _ in range(self.max_turns):
            msg = self.llm.chat(messages, tools=TOOLS)
            if not msg.tool_calls:
                summary = (msg.content or "").strip()
                self._log(log, f"[coding_agent done]\n{summary}\n")
                return summary or "(coding agent finished without a summary)"
            messages.append(_assistant_message(msg))
            for call in msg.tool_calls:
                result = self._execute(ws, call.function.name, call.function.arguments)
                self._log(log, f"> {call.function.name}({call.function.arguments[:500]})\n{result[:2000]}\n")
                messages.append({"role": "tool", "tool_call_id": call.id, "content": result})

        messages.append({"role": "user", "content": TURN_LIMIT_PROMPT})
        summary = (self.llm.chat(messages, tools=TOOLS).content or "").strip()
        self._log(log, f"[coding_agent stopped: turn limit]\n{summary}\n")
        return f"{summary}\n(stopped: turn limit of {self.max_turns} reached)"

    # ------------------------------------------------------------------ tools
    def _execute(self, ws: Workspace, name: str, arguments: str) -> str:
        try:
            args = json.loads(arguments or "{}")
        except json.JSONDecodeError as exc:
            return f"error: invalid JSON arguments ({exc})"
        handler = getattr(self, f"_tool_{name}", None)
        if handler is None:
            return f"error: unknown tool {name}"
        try:
            return _truncate(handler(ws, **args))
        except WorkspaceError as exc:
            return f"error: {exc}"
        except TypeError as exc:
            return f"error: bad arguments for {name}: {exc}"
        except Exception as exc:  # the model gets the error and decides what to do
            return f"error: {type(exc).__name__}: {exc}"

    def _tool_query_metadata(self, ws: Workspace, sql: str) -> str:
        rows = ws.query(sql)
        shown = rows[:200]
        text = format_rows(shown, max_width=120)
        if len(rows) > len(shown):
            text += f"\n... {len(rows) - len(shown)} more rows"
        return text

    def _tool_list_files(self, ws: Workspace, path: str = ".") -> str:
        root = ws.abspath(path)
        if root.is_file():
            return f"{ws.relpath(root)} ({root.stat().st_size} bytes)"
        if not root.is_dir():
            return f"error: {path} does not exist"
        lines = []
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(d for d in dirnames if d not in IGNORED_DIRS and not d.startswith("."))
            for name in sorted(filenames):
                p = Path(dirpath) / name
                lines.append(f"{ws.relpath(p)} ({p.stat().st_size} bytes)")
                if len(lines) >= 400:
                    lines.append("... (listing truncated)")
                    return "\n".join(lines)
        return "\n".join(lines) or "(empty directory)"

    def _tool_read_file(self, ws: Workspace, path: str, start_line: int = 1, max_lines: int = 300) -> str:
        p = ws.abspath(path)
        if not p.is_file():
            return f"error: {path} is not a file"
        raw = p.read_bytes()
        if b"\0" in raw[:4096]:
            return f"error: {path} is a binary file ({len(raw)} bytes)"
        lines = raw.decode("utf-8", errors="replace").splitlines()
        start = max(start_line, 1)
        chunk = lines[start - 1:start - 1 + max_lines]
        end = start + len(chunk) - 1
        return f"[{path}: lines {start}-{end} of {len(lines)}]\n" + "\n".join(chunk)

    def _tool_write_file(self, ws: Workspace, path: str, content: str) -> str:
        rel = _writable(ws, path)
        p = ws.abspath(rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return f"wrote {len(content.encode())} bytes to {rel}"

    def _tool_replace_in_file(self, ws: Workspace, path: str, old: str, new: str) -> str:
        rel = _writable(ws, path)
        p = ws.abspath(rel)
        if not p.is_file():
            return f"error: {path} is not a file"
        text = p.read_text()
        count = text.count(old)
        if count != 1:
            return f"error: `old` occurs {count} times in {rel}; it must occur exactly once"
        p.write_text(text.replace(old, new))
        return f"replaced in {rel}"

    def _tool_run_shell(self, ws: Workspace, command: str, timeout: int | None = None) -> str:
        env = dict(os.environ)
        env["PATH"] = f"{Path(sys.executable).parent}{os.pathsep}{env.get('PATH', '')}"
        env["PYTHONUNBUFFERED"] = "1"
        try:
            result = subprocess.run(
                ["bash", "-c", command], cwd=ws.root, env=env, capture_output=True, text=True,
                timeout=min(timeout or self.shell_timeout, self.shell_timeout),
            )
        except subprocess.TimeoutExpired:
            return f"error: command timed out after {self.shell_timeout}s"
        out = f"exit code {result.returncode}\n"
        if result.stdout:
            out += f"stdout:\n{result.stdout}"
        if result.stderr:
            out += f"\nstderr:\n{result.stderr}"
        return out

    @staticmethod
    def _log(log: Path, text: str) -> None:
        log.parent.mkdir(parents=True, exist_ok=True)
        with open(log, "a") as fh:
            fh.write(text)


def _writable(ws: Workspace, path: str) -> str:
    rel = ws.relpath(path)
    if rel.startswith(DB_FILE) or any(rel.startswith(p) for p in PROTECTED if p.endswith("/")):
        raise WorkspaceError(f"{rel} is managed by AOS and must not be modified")
    return rel


def _assistant_message(msg) -> dict:
    return {
        "role": "assistant",
        "content": msg.content,
        "tool_calls": [
            {"id": c.id, "type": "function",
             "function": {"name": c.function.name, "arguments": c.function.arguments}}
            for c in msg.tool_calls
        ],
    }


def _truncate(text: str, limit: int = MAX_TOOL_OUTPUT) -> str:
    if len(text) <= limit:
        return text
    half = limit // 2
    return text[:half] + f"\n... [{len(text) - limit} characters truncated] ...\n" + text[-half:]

```
