# Homework 2 bundle: vendor/aos/aos/orchestrator.py

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/orchestrator.py) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/orchestrator.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""The orchestration loop: inspect the workspace, decide the next step, run it,
register what it produced, checkpoint, repeat."""

from __future__ import annotations

import inspect
import json
from typing import Callable

from . import prompts, trace
from .llm import ZERO_USAGE, add_usage, parse_json, price_usd
from .tasks import Step, Task
from .capabilities.base import ExternalCapability, install_adapters
from .worker import StepFailed, Worker
from .workspace import INPUTS_DIR, Workspace, WorkspaceError, file_type, is_hidden

PLANNER_SYSTEM = prompts.load("planner_system")
PLANNER_PROMPT = prompts.load("planner")
SUMMARY_PROMPT = prompts.load("summary")

MAX_SUMMARIZED_FILES = 25
HEAD_CHARS = 1500


class Orchestrator:
    def __init__(self, ws: Workspace, llm, workers: dict[str, Worker], max_steps: int = 12,
                 log: Callable[[str], None] = print, budget_usd: float | None = None, spent_usd: float = 0.0):
        self.ws = ws
        self.llm = llm
        self.workers = workers
        self.max_steps = max_steps
        self.log = log
        #: Estimated USD cap for the workspace and what was already spent before this run.
        self.budget_usd = budget_usd
        self.spent_usd = spent_usd

    # ------------------------------------------------------------------- run
    def run(self, goal: str) -> Task:
        task = Task.new(self.ws, goal)
        with trace.context(task.dir / trace.TRACE_FILE, task=task.id):
            return self._run(task, goal)

    def _run(self, task: Task, goal: str) -> Task:
        started = _snapshot(self.llm)
        self.log(f"[{task.id}] goal: {goal}")
        self.register_inputs(task)
        self.ws.checkpoint(f"{task.id}: start")

        while len(task.steps) < self.max_steps:
            if self._over_budget(task, started):
                break
            try:
                self.register_inputs(task)  # files the user dropped in since the last decision
                decision = self.decide(task)
            except StepFailed as exc:
                task.finish("failed", str(exc))
                self.log(f"[{task.id}] failed: {exc}")
                break
            except Exception as exc:  # e.g. the model endpoint rejecting the key: record it, do not hang the task
                task.finish("failed", f"{type(exc).__name__}: {exc}")
                self.log(f"[{task.id}] failed: {type(exc).__name__}: {exc}")
                break
            action = decision["action"]
            if action == "done":
                task.finish("done", decision["summary"])
                self.log(f"[{task.id}] done: {decision['summary']}")
                break
            if action == "rollback":
                self.rollback(task, decision["step"], decision.get("reason", ""))
                continue
            step = Step(
                worker=decision["worker"], instructions=decision["instructions"],
                reason=decision.get("reason", ""), inputs=decision.get("inputs", []),
                output_dir=decision.get("output_dir", "generated"),
            )
            self.run_step(task, step)
        else:
            task.finish("stopped", f"Reached the limit of {self.max_steps} steps")
            self.log(f"[{task.id}] stopped: step limit reached")

        self._record_task_usage(task, started)
        self.ws.checkpoint(f"{task.id}: {task.data['status']}")
        return task

    def run_workflow(self, goal: str, steps: list[Step]) -> Task:
        """Replay a saved sequence of steps without the planner; stops at the first failure."""
        task = Task.new(self.ws, goal)
        with trace.context(task.dir / trace.TRACE_FILE, task=task.id):
            return self._run_workflow(task, goal, steps)

    def _run_workflow(self, task: Task, goal: str, steps: list[Step]) -> Task:
        started = _snapshot(self.llm)
        self.log(f"[{task.id}] workflow: {goal}")
        self.register_inputs(task)
        self.ws.checkpoint(f"{task.id}: start")
        status = "done"
        for step in steps:
            if self._over_budget(task, started):
                status = "stopped"
                break
            record = self.run_step(task, step)
            if record["status"] != "ok":
                status = "failed"
                break
        if status != "stopped":
            task.finish(status, f"Workflow of {len(steps)} steps {status}")
        self._record_task_usage(task, started)
        self.ws.checkpoint(f"{task.id}: {status}")
        return task

    def _over_budget(self, task: Task, started: dict | None) -> bool:
        """Stop before the next step once the estimated spend reaches the workspace's cap."""
        if self.budget_usd is None:
            return False
        so_far = add_usage(_usage_since(self.llm, started),
                           *[(s.get("usage") or {}).get("external") for s in task.steps])["cost_usd"]
        spent = round(self.spent_usd + so_far, 6)
        if spent < self.budget_usd:
            return False
        task.finish("stopped", f"Stopped: the budget cap of ${self.budget_usd:.2f} was reached "
                               f"(about ${spent:.2f} spent, estimated). Raise the cap in settings to continue.")
        self.log(f"[{task.id}] stopped: budget cap ${self.budget_usd:.2f} reached (${spent:.2f} spent)")
        return True

    def _record_task_usage(self, task: Task, started: dict | None) -> None:
        """Task cost = every AOS call made during the task (planning, summaries, coding agent)
        plus what the external systems reported for their steps."""
        internal = _usage_since(self.llm, started)
        external = add_usage(*[(s.get("usage") or {}).get("external") for s in task.steps])
        usage = add_usage(internal, external)
        usage["internal"] = internal
        usage["external"] = external
        task.finish(task.data["status"], task.data.get("result"), usage=usage)

    # ------------------------------------------------------------------ steps
    def run_step(self, task: Task, step: Step) -> dict:
        """Run one step: execute the worker, register what it produced, checkpoint."""
        with trace.context(step=len(task.steps) + 1, worker=step.worker, purpose=step.worker):
            return self._run_step(task, step)

    def _run_step(self, task: Task, step: Step) -> dict:
        worker = self.workers.get(step.worker)
        if isinstance(worker, ExternalCapability):
            refreshed = install_adapters(self.ws)  # missing or outdated pristine copies of the runner scripts
            if refreshed:
                self.log(f"[{task.id}] adapters installed or refreshed: {', '.join(refreshed)}")
        if self.ws.has_changes():
            self.ws.checkpoint(f"{task.id}: checkpoint before step {len(task.steps) + 1}")
        record = task.start_step(step)
        n = record["n"]
        log = task.log_path(n)
        log.parent.mkdir(parents=True, exist_ok=True)
        log.write_text(f"# {task.id} step {n}: {step.worker}\n# reason: {step.reason}\n"
                       f"# inputs: {step.inputs}\n# output_dir: {step.output_dir}\n\n")
        self.log(f"[{task.id}] step {n}: {step.worker} — {step.reason or step.instructions[:100]}")

        before = self.ws.snapshot()
        llm_before = _snapshot(self.llm)
        if worker is not None:
            worker.last_usage = None
        summary, status, error = "", "ok", None
        try:
            if worker is None:
                raise StepFailed(f"unknown worker {step.worker!r}; available: {', '.join(self.workers)}")
            ok, why = worker.available()
            if not ok:
                raise StepFailed(f"worker {step.worker} is not available: {why}")
            self.ws.abspath(step.output_dir).mkdir(parents=True, exist_ok=True)
            summary = _call_worker(worker, self.ws, step, log, task.goal)
        except StepFailed as exc:
            status, error = "failed", str(exc)
        except Exception as exc:  # a broken worker must not take AOS down; the planner sees the error
            status, error = "failed", f"{type(exc).__name__}: {exc}"

        try:
            outputs = self._catalog_outputs(task, step, n, before)
        except Exception as exc:  # a bad path or catalog error must not leave the task stuck as "running"
            outputs = []
            status, error = "failed", error or f"cataloging the outputs failed: {type(exc).__name__}: {exc}"
        usage = self._step_usage(_usage_since(self.llm, llm_before), getattr(worker, "last_usage", None))
        task.finish_step(record, status=status, outputs=outputs, summary=summary, error=error, usage=usage)
        sha = self.ws.checkpoint(f"{task.id} step {n}: {step.worker} ({status}) - {(step.reason or step.instructions)[:60]}")
        record["commit"] = sha or self.ws.head()
        task.save()
        if error:
            self.log(f"[{task.id}] step {n} failed: {error[:500]}")
        else:
            self.log(f"[{task.id}] step {n} ok: {len(outputs)} file(s) — {summary[:300]}")
        return record

    def _catalog_outputs(self, task: Task, step: Step, n: int, before: dict) -> list[str]:
        """Register what the step produced (files under inputs/ are the user's); returns the outputs."""
        changed = self.ws.changed_since(before)
        # inputs/ belongs to the user: whatever appears there mid-step is theirs, not the worker's
        user_added = [p for p in changed if p.startswith(INPUTS_DIR + "/")]
        outputs = [p for p in changed if p not in user_added]
        if user_added:
            self._register_user_files(user_added, task, f"Provided by the user during {task.id} step {n}")
        context = (f"produced by worker '{step.worker}' for task {task.id} step {n}: "
                   f"{step.reason or step.instructions[:300]}")
        summaries = self.summarize_files(outputs, context)
        existing_inputs = [i for i in step.inputs if self.ws.abspath(i).exists()]
        for path in outputs:
            self.ws.register(
                path, source=step.worker, reason=step.reason or step.instructions[:200],
                summary=summaries.get(path, ""), task=task.id, step=n, inputs=existing_inputs,
            )
        self.ws.prune_metadata()
        return outputs

    def _step_usage(self, internal: dict, external: dict | None) -> dict:
        """What a step cost: AOS's own calls during it plus the worker's reported usage."""
        reported = None
        if external:
            cost = external.get("cost_usd")
            if cost is None and external.get("input_tokens") is not None:
                cost = price_usd(external.get("model"), external.get("input_tokens") or 0,
                                 external.get("output_tokens") or 0, getattr(self.llm, "prices", None))
            reported = {
                "model": external.get("model"), "calls": external.get("calls") or 0,
                "input_tokens": external.get("input_tokens") or 0, "output_tokens": external.get("output_tokens") or 0,
                "reasoning_tokens": 0, "cost_usd": cost or 0.0, "unpriced_calls": 0 if cost is not None else 1,
            }
        usage = add_usage(internal, reported)
        usage["internal"] = internal
        usage["external"] = reported
        return usage

    def rollback(self, task: Task, step_number: int, reason: str) -> dict:
        target = task.steps[step_number - 1]["commit"]
        record = task.start_step(Step(worker="rollback", instructions=f"restore state after step {step_number}",
                                      reason=reason))
        sha = self.ws.rollback(target)
        task.finish_step(record, status="ok", outputs=[],
                         summary=f"Workspace restored to its state after step {step_number} ({target[:12]})")
        record["commit"] = sha
        task.save()
        self.log(f"[{task.id}] rolled back to step {step_number}")
        return record

    # --------------------------------------------------------------- planning
    def decide(self, task: Task) -> dict:
        prompt = PLANNER_PROMPT.format(
            goal=task.goal,
            workers="\n".join(f"- {w.name}: {w.description}" for w in self.workers.values()),
            tree=self.ws.tree(),
            history=task.summary_text(),
        )
        messages = [{"role": "system", "content": PLANNER_SYSTEM}, {"role": "user", "content": prompt}]
        problem = ""
        for _ in range(3):
            with trace.context(purpose="planner"):
                reply = self.llm.chat(messages, json_mode=True).content or ""
            try:
                decision = parse_json(reply)
                self._validate(decision, task)
                return decision
            except (ValueError, KeyError, TypeError, json.JSONDecodeError, WorkspaceError) as exc:
                problem = str(exc)
                messages.append({"role": "assistant", "content": reply})
                messages.append({"role": "user", "content": f"Invalid decision: {problem}. Reply again with one valid JSON decision."})
        raise StepFailed(f"planner did not produce a valid decision: {problem}")

    def _validate(self, decision: dict, task: Task) -> None:
        action = decision.get("action")
        if action == "done":
            if not decision.get("summary"):
                raise ValueError("'done' needs a non-empty 'summary'")
            return
        if action == "rollback":
            n = decision.get("step")
            if not isinstance(n, int) or not 1 <= n <= len(task.steps) or not task.steps[n - 1].get("commit"):
                raise ValueError("'rollback' needs the number of a completed step")
            return
        if action != "run":
            raise ValueError("'action' must be run, done or rollback")
        if decision.get("worker") not in self.workers:
            raise ValueError(f"unknown worker {decision.get('worker')!r}; available: {', '.join(self.workers)}")
        if not isinstance(decision.get("instructions"), str) or not decision["instructions"].strip():
            raise ValueError("'instructions' must be a non-empty string")
        if not isinstance(decision.get("reason", ""), str):
            raise ValueError("'reason' must be a string")
        inputs = decision.get("inputs", [])
        if not isinstance(inputs, list) or not all(isinstance(i, str) for i in inputs):
            raise ValueError("'inputs' must be a list of workspace paths")
        missing = [i for i in inputs if not self.ws.abspath(i).exists()]
        if missing:
            raise ValueError(f"these inputs do not exist in the workspace: {', '.join(missing)}")
        out = decision.get("output_dir", "generated")
        if not isinstance(out, str) or not out:
            raise ValueError("'output_dir' must be a workspace-relative directory")
        self.ws.relpath(out)  # raises if it escapes the workspace

    # --------------------------------------------------------------- metadata
    def register_inputs(self, task: Task) -> list[str]:
        """Register files that exist in the workspace but have no provenance yet (user-provided inputs),
        and mark worker files that were edited by hand since the last checkpoint as "mixed"."""
        new = self.ws.unregistered()
        if new:
            self._register_user_files(new, task, f"Provided by the user as input for {task.id}")
        gone = self.ws.prune_metadata()  # files removed from the workspace leave the catalog
        if gone:
            self.log(f"[{task.id}] dropped {len(gone)} deleted file(s) from the catalog: {', '.join(gone[:5])}")
        edited = [p for p in self.ws.modified() if (self.ws.describe(p) or {}).get("source") not in (None, "user")]
        if edited:
            summaries = self.summarize_files(edited, "worker-produced files that the user edited by hand")
            for path in edited:
                self.ws.mark_edited(path, summaries.get(path))
            self.ws.checkpoint(f"User edits before {task.id} step {len(task.steps) + 1}")
            self.log(f"[{task.id}] marked {len(edited)} edited file(s) as mixed: {', '.join(edited[:5])}")
        return new

    def _register_user_files(self, paths: list[str], task: Task, reason: str) -> None:
        summaries = self.summarize_files(paths, "files placed in the workspace by the user as inputs")
        for path in paths:
            self.ws.register(path, source="user", reason=reason, summary=summaries.get(path, ""), task=task.id)
        self.log(f"[{task.id}] registered {len(paths)} user file(s): {', '.join(paths[:5])}")

    def summarize_files(self, paths: list[str], context: str) -> dict[str, str]:
        """One-sentence summaries for a batch of files (best effort; never raises)."""
        if not paths:
            return {}
        visible = [p for p in paths if not is_hidden(p)]
        summaries: dict[str, str] = {}
        for start in range(0, len(visible), MAX_SUMMARIZED_FILES):  # one call per batch of files
            shown = visible[start:start + MAX_SUMMARIZED_FILES]
            blocks = []
            for path in shown:
                p = self.ws.abspath(path)
                size = p.stat().st_size if p.is_file() else 0
                blocks.append(f"--- {path} ({file_type(path)}, {size} bytes) ---\n{_head(p)}")
            try:
                with trace.context(purpose="summary"):
                    reply = self.llm.complete_json(SUMMARY_PROMPT.format(context=context, files="\n\n".join(blocks)))
                summaries.update({k: str(v) for k, v in reply.items() if k in shown})
            except Exception as exc:  # summaries are a convenience; the step outcome does not depend on them
                self.log(f"(file summaries unavailable: {exc})")
                break
        for path in paths:
            kind = "Cache/store file" if is_hidden(path) else "File"
            summaries.setdefault(path, f"{kind} {context}")
        return summaries


def _snapshot(llm) -> dict | None:
    return llm.snapshot() if hasattr(llm, "snapshot") else None


def _usage_since(llm, snapshot: dict | None) -> dict:
    if snapshot is None or not hasattr(llm, "usage_since"):
        return dict(ZERO_USAGE)
    return llm.usage_since(snapshot)


def _call_worker(worker: Worker, ws: Workspace, step: Step, log, goal: str) -> str:
    if "goal" in inspect.signature(worker.run).parameters:
        return worker.run(ws, step, log, goal=goal)
    return worker.run(ws, step, log)


def _head(path, limit: int = HEAD_CHARS) -> str:
    if not path.is_file():
        return "(directory)"
    raw = path.read_bytes()[:limit * 2]
    if b"\0" in raw:
        return "(binary file)"
    text = raw.decode("utf-8", errors="replace")
    return text[:limit] + ("..." if len(text) > limit else "")

```
