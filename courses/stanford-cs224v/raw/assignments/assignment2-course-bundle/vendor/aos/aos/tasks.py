"""Task records: ``tasks/task-NNN/task.json``.

A task is the user's goal plus the plain sequence of steps AOS ran for it,
each with its worker, instructions, workspace inputs and produced outputs.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .workspace import TASKS_DIR, Workspace, now


def _alive(pid) -> bool:
    """Whether the process that started a task is still around (same machine, as the workspace is)."""
    if not pid:
        return False  # a record from before pids were kept: nothing to check, treat as orphaned
    try:
        os.kill(int(pid), 0)
    except ProcessLookupError:
        return False
    except (PermissionError, OverflowError, ValueError):
        return pid != 0 and isinstance(pid, int) and pid < 2 ** 22  # exists but not ours, or nonsense
    return True



@dataclass
class Step:
    """One unit of work handed to a worker."""

    worker: str
    instructions: str
    reason: str = ""
    inputs: list[str] = field(default_factory=list)
    output_dir: str = "generated"


class Task:
    def __init__(self, ws: Workspace, data: dict):
        self.ws = ws
        self.data = data

    @classmethod
    def new(cls, ws: Workspace, goal: str) -> "Task":
        numbers = [
            int(m.group(1))
            for p in (ws.root / TASKS_DIR).glob("task-*")
            if (m := re.fullmatch(r"task-(\d+)", p.name))
        ]
        task_id = f"task-{max(numbers, default=0) + 1:03d}"
        task = cls(ws, {"id": task_id, "goal": goal, "created": now(), "status": "running", "pid": os.getpid(),
                        "steps": [], "result": None})
        task.save()
        return task

    @classmethod
    def load(cls, ws: Workspace, task_id: str) -> "Task":
        path = ws.root / TASKS_DIR / task_id / "task.json"
        return cls(ws, json.loads(path.read_text()))

    @classmethod
    def mark_interrupted(cls, ws: Workspace) -> list[str]:
        """Tasks marked running whose process is gone (the record carries the pid of the process that
        started them; a run in progress from another process, such as the CLI, is left alone)."""
        interrupted = []
        for task in cls.list(ws):
            if task.data["status"] == "running" and not _alive(task.data.get("pid")):
                for step in task.steps:
                    if step["status"] == "running":
                        step.update(status="failed", error="interrupted: the process running this step stopped", finished=now())
                task.finish("interrupted", "The run stopped before the task finished (process ended or crashed)")
                interrupted.append(task.id)
        return interrupted

    @classmethod
    def list(cls, ws: Workspace) -> list["Task"]:
        paths = sorted((ws.root / TASKS_DIR).glob("task-*/task.json"))
        return [cls(ws, json.loads(p.read_text())) for p in paths]

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def goal(self) -> str:
        return self.data["goal"]

    @property
    def steps(self) -> list[dict]:
        return self.data["steps"]

    @property
    def dir(self) -> Path:
        return self.ws.root / TASKS_DIR / self.id

    def save(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        (self.dir / "task.json").write_text(json.dumps(self.data, indent=2) + "\n")

    def log_path(self, n: int) -> Path:
        return self.dir / f"step-{n:02d}.log"

    def start_step(self, step: Step) -> dict:
        n = len(self.steps) + 1
        record = {
            "n": n,
            **asdict(step),
            "status": "running",
            "started": now(),
            "finished": None,
            "outputs": [],
            "summary": "",
            "error": None,
            "commit": None,
            "usage": None,
            "log": self.log_path(n).relative_to(self.ws.root).as_posix(),
        }
        self.steps.append(record)
        self.save()
        return record

    def finish_step(self, record: dict, *, status: str, outputs: list[str], summary: str,
                    error: str | None = None, usage: dict | None = None) -> None:
        record.update(status=status, outputs=outputs, summary=summary, error=error, usage=usage, finished=now())
        self.save()

    def finish(self, status: str, result: str | None, usage: dict | None = None) -> None:
        self.data.update(status=status, result=result, finished=now())
        if usage is not None:
            self.data["usage"] = usage
        self.save()

    def summary_text(self, max_outputs: int = 15) -> str:
        """Compact history of the task for prompts and status output."""
        if not self.steps:
            return "(no steps yet)"
        lines = []
        for s in self.steps:
            lines.append(f"Step {s['n']} [{s['status']}] {s['worker']}: {s['reason'] or s['instructions'][:120]}")
            if s["inputs"]:
                lines.append(f"  inputs: {', '.join(s['inputs'])}")
            if s["outputs"]:
                shown = s["outputs"][:max_outputs]
                extra = f" (+{len(s['outputs']) - max_outputs} more)" if len(s["outputs"]) > max_outputs else ""
                lines.append(f"  outputs: {', '.join(shown)}{extra}")
            if s["summary"]:
                lines.append(f"  summary: {s['summary'][:800]}")
            if s["error"]:
                lines.append(f"  error: {s['error'][:800]}")
        return "\n".join(lines)
