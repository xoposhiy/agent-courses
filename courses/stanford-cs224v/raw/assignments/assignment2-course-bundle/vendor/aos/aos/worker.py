"""Workers: the things AOS hands work to.

A worker reads instructions and workspace files and writes workspace files.
It does not know which worker ran before it or which will run after it.
"""

from __future__ import annotations

import json
import os
import signal
import threading
import subprocess
from pathlib import Path

from .tasks import Step
from .workspace import Workspace


class StepFailed(Exception):
    """Raised by a worker when a step did not complete."""


class Worker:
    #: Name the orchestrator uses to select this worker.
    name: str = ""
    #: What the worker does, what ``instructions``/``inputs`` it expects and what it produces.
    #: This is what the planner sees, so it must be precise.
    description: str = ""
    #: Token usage of the last run when the worker can report it:
    #: {"model", "calls", "input_tokens", "output_tokens", "cost_usd"} (any may be None).
    last_usage: dict | None = None

    def available(self) -> tuple[bool, str]:
        """Whether the worker can run here, with a human-readable reason when it cannot."""
        return True, ""

    def run(self, ws: Workspace, step: Step, log: Path) -> str:
        """Perform the step inside ``ws``; append diagnostics to ``log``; return a short summary.

        Outputs are discovered by the orchestrator by diffing the workspace, so a worker
        just has to write its files under ``step.output_dir`` (or wherever instructed).
        Raise :class:`StepFailed` on failure.
        """
        raise NotImplementedError


def run_command(cmd: list[str], *, cwd: Path, log: Path, env: dict | None = None,
                timeout: int = 3600, stdin: str | None = None) -> str:
    """Run a subprocess, tee its output into ``log`` and return the output text.

    Raises :class:`StepFailed` with the tail of the output on a non-zero exit or timeout.
    """
    log.parent.mkdir(parents=True, exist_ok=True)
    full_env = {**os.environ, **(env or {})}
    chunks: list[str] = []
    with open(log, "a") as fh:
        fh.write(f"$ {' '.join(str(c) for c in cmd)}\n")
        fh.flush()
        proc = subprocess.Popen(
            [str(c) for c in cmd], cwd=cwd, env=full_env, text=True, start_new_session=True,
            stdin=subprocess.PIPE if stdin is not None else subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        if stdin is not None:
            proc.stdin.write(stdin)
            proc.stdin.close()

        def pump() -> None:  # every line lands in the log the moment the process writes it
            for line in proc.stdout:
                fh.write(line)
                fh.flush()
                chunks.append(line)

        reader = threading.Thread(target=pump, daemon=True)
        reader.start()
        try:
            returncode = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired as exc:
            _kill_group(proc)
            reader.join(5)
            fh.write(f"[timed out after {timeout}s]\n")
            raise StepFailed(f"{cmd[0]} timed out after {timeout}s") from exc
        reader.join(5)
        fh.write(f"\n[exit {returncode}]\n")
    output = "".join(chunks)
    if returncode != 0:
        raise StepFailed(f"{Path(str(cmd[0])).name} exited with {returncode}:\n{output[-3000:]}")
    return output


def _kill_group(proc: subprocess.Popen) -> None:
    """Stop a runner and the processes it started (they share its session)."""
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except (ProcessLookupError, OSError):
        proc.kill()
    proc.wait()


def read_usage(directory: Path) -> dict | None:
    """The ``usage.json`` a runner leaves in its output directory, or None."""
    path = Path(directory) / "usage.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict):
        return None
    return {
        "model": data.get("model"),
        "calls": _int_or_none(data.get("calls")),
        "input_tokens": _int_or_none(data.get("input_tokens")),
        "output_tokens": _int_or_none(data.get("output_tokens")),
        "cost_usd": float(data["cost_usd"]) if data.get("cost_usd") is not None else None,
    }


def _int_or_none(value) -> int | None:
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None
