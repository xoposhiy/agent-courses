"""The Python interface: everything the ``aos`` command does, behind one object.

    from aos.api import AOS
    aos = AOS.create("workspaces/review", goal="Find the matching patients")
    aos.add("~/cases/labs.csv", reason="lab results")
    aos.step("historygenie", "", inputs=["inputs/notes"], output_dir="generated/transcripts")
    task = aos.run("Determine which patients ...")
    aos.ask("Which patients were flagged?")

An ``AOS`` holds a workspace, the LLM client, the workers the planner may use and the budget wiring.
The CLI is a thin layer over it; the web UI keeps its own per-session accounting.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Callable

from . import trace
from .assistant import Assistant
from .capabilities import available_workers
from .capabilities.base import install_adapters
from .llm import LLM, add_usage
from .orchestrator import Orchestrator
from .tasks import Step, Task
from .worker import Worker
from .workspace import INPUTS_DIR, Workspace, WorkspaceError


class AOS:
    def __init__(self, ws: Workspace, llm=None, workers: dict[str, Worker] | None = None,
                 log: Callable[[str], None] = print):
        self.ws = ws
        self._llm = llm
        self._workers = workers
        self.log = log
        self._assistant: Assistant | None = None

    @property
    def llm(self):
        """The model client (``aos.llm.LLM`` from ``.env`` unless one was passed); created on first use,
        so inspecting a workspace needs no credentials."""
        if self._llm is None:
            self._llm = LLM()
        return self._llm

    @property
    def workers(self) -> dict[str, Worker]:
        """The workers the planner may choose from, by name (default: every available built-in and
        ``AOS_WORKERS`` worker). Add your own with ``aos.workers["x"] = X(aos.llm)``."""
        if self._workers is None:
            self._workers = available_workers(self.llm)
        return self._workers

    # ---------------------------------------------------------------- lifecycle
    @classmethod
    def create(cls, path: str | Path, goal: str | None = None, **kwargs) -> "AOS":
        """Create (or reopen) a workspace with its folders, catalog, git repository and adapter copies."""
        ws = Workspace.create(path, goal=goal)
        install_adapters(ws)
        ws.checkpoint("Install adapter scripts")
        return cls(ws, **kwargs)

    @classmethod
    def open(cls, path: str | Path, **kwargs) -> "AOS":
        return cls(Workspace.open(path), **kwargs)

    @property
    def root(self) -> Path:
        return self.ws.root

    # ------------------------------------------------------------------ inputs
    def add(self, *paths: str | Path, reason: str = "Provided by the user") -> list[dict]:
        """Give the workspace input files or folders: anything outside it is copied into ``inputs/``,
        anything inside is cataloged in place; each file gets a model-written summary and a commit."""
        files: list[str] = []
        for path in paths:
            src = Path(path).expanduser()
            if not src.exists():
                raise WorkspaceError(f"{path} does not exist")
            src = src.resolve()
            try:
                self.ws.relpath(src)
            except WorkspaceError:  # outside: copy it in
                dest = self.ws.root / INPUTS_DIR / src.name
                if src.is_dir():
                    shutil.copytree(src, dest, dirs_exist_ok=True)
                else:
                    shutil.copyfile(src, dest)
                src = dest
            files += [self.ws.relpath(p) for p in ([src] if src.is_file() else sorted(p for p in src.rglob("*") if p.is_file()))]
        if not files:
            return []
        try:
            with trace.context(trace.workspace_log(self.ws.root)):
                summaries = self._orchestrator().summarize_files(files, "files placed in the workspace by the user as inputs")
        except RuntimeError:  # no LLM configured: catalog them without a summary
            summaries = {}
        entries = [self.ws.register(rel, source="user", reason=reason, summary=summaries.get(rel, "")) for rel in files]
        shown = ", ".join(files[:3]) + (f" (+{len(files) - 3} more)" if len(files) > 3 else "")
        self.ws.checkpoint(f"Add {shown}")
        return entries

    # ------------------------------------------------------------------- doing
    def run(self, goal: str, max_steps: int = 12) -> Task:
        """Pursue a goal: the planner picks a worker per step until it says done."""
        return self._orchestrator(max_steps).run(goal)

    def step(self, worker: str, instructions: str, inputs: list[str] | tuple[str, ...] = (),
             output_dir: str = "generated", reason: str = "") -> dict:
        """Run one step with a worker of your choice (no planner). Returns the step record:
        status, outputs, summary, error, commit, usage."""
        step = Step(worker=worker, instructions=instructions, reason=reason, inputs=list(inputs), output_dir=output_dir)
        task = self._orchestrator().run_workflow(f"manual step: {instructions}", [step])
        if not task.steps:  # stopped before running: the budget cap
            raise RuntimeError(task.data["result"])
        return task.steps[0]

    def workflow(self, workflow: str | Path | list[Step | dict], goal: str | None = None) -> Task:
        """Replay a saved workflow (a path to its JSON) or a list of steps, without the planner."""
        if isinstance(workflow, (str, Path)):
            data = json.loads(Path(workflow).read_text())
            steps, goal = data["steps"], goal or data.get("goal", data.get("name", "workflow"))
        else:
            steps = workflow
        steps = [s if isinstance(s, Step) else Step(**s) for s in steps]
        return self._orchestrator().run_workflow(goal or "workflow", steps)

    def save_workflow(self, task_id: str, name: str) -> Path:
        """Write a finished task's successful steps to ``workflows/<name>.json`` and commit."""
        task = Task.load(self.ws, task_id)
        steps = [{k: s[k] for k in ("worker", "instructions", "reason", "inputs", "output_dir")}
                 for s in task.steps if s["status"] == "ok" and s["worker"] != "rollback"]
        path = self.ws.root / "workflows" / f"{name}.json"
        path.write_text(json.dumps({"name": name, "goal": task.goal, "steps": steps}, indent=2) + "\n")
        self.ws.register(path, source="aos", reason=f"Reusable workflow saved from {task.id}",
                         summary=f"Workflow '{name}': {len(steps)} steps for goal: {task.goal[:120]}")
        self.ws.checkpoint(f"Save workflow {name}")
        return path

    def ask(self, question: str) -> str:
        """Ask the read-only assistant about the workspace; it remembers the conversation."""
        if self._assistant is None:
            self._assistant = Assistant(self.ws, self.llm)
        return self._assistant.ask(question)

    def rollback(self, ref: str) -> str:
        """Restore files and catalog to commit ``ref`` as a new commit (task records are kept)."""
        return self.ws.rollback(ref)

    # -------------------------------------------------------------- inspecting
    def tasks(self) -> list[Task]:
        return Task.list(self.ws)

    def query(self, sql: str, params: tuple = ()) -> list[dict]:
        """A read-only SQL query over the catalog (``files``, ``file_inputs``, ``workspace``)."""
        return self.ws.query(sql, params)

    def describe(self, path: str | Path) -> dict | None:
        return self.ws.describe(path)

    def files(self) -> dict[str, dict]:
        return self.ws.files()

    def history(self, n: int = 20) -> list[dict]:
        return self.ws.history(n)

    def trace(self, task_id: str | None = None, step: int | None = None) -> list[dict]:
        """The LLM calls recorded for one task (or all tasks plus calls outside tasks), in time order."""
        if task_id:
            files = [self.ws.root / "tasks" / task_id / trace.TRACE_FILE]
        else:
            files = sorted((self.ws.root / "tasks").glob(f"task-*/{trace.TRACE_FILE}")) + [trace.workspace_log(self.ws.root)]
        records = [r for f in files for r in trace.read(f) if step is None or r.get("step") == step]
        return sorted(records, key=lambda r: r["time"])

    # ------------------------------------------------------------------ budget
    @property
    def budget_usd(self) -> float | None:
        """Estimated-USD cap for this workspace (None = no cap); runs stop between steps when reached."""
        return self.ws.setting("budget_usd")

    @budget_usd.setter
    def budget_usd(self, value: float | None) -> None:
        if value is not None and value <= 0:
            raise ValueError("the budget cap must be positive, or None for no cap")
        self.ws.set_setting("budget_usd", value)

    @property
    def spent_usd(self) -> float:
        """Estimated USD recorded by every task in this workspace so far."""
        return add_usage(*[t.data.get("usage") for t in self.tasks()])["cost_usd"]

    def _orchestrator(self, max_steps: int = 12) -> Orchestrator:
        return Orchestrator(self.ws, self.llm, self.workers, max_steps=max_steps, log=self.log,
                            budget_usd=self.budget_usd, spent_usd=self.spent_usd)
