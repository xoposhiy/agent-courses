# Homework 2 bundle: vendor/aos/aos/capabilities/base.py

[Course index](../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/capabilities/base.py) · [Raw file](../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/capabilities/base.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""Shared plumbing for wrapping the external research systems.

Each capability is a repo cloned under ``external/`` with its own virtualenv;
AOS drives it through a small runner script executed with that virtualenv's
Python. Instructions and paths go in as arguments, files come out.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
from pathlib import Path

from ..llm import AOS_ROOT, DEFAULT_MODEL, load_prices
from ..worker import Worker, read_usage
from ..workspace import Workspace

RUNNERS_DIR = Path(__file__).resolve().parent / "runners"
#: Where a workspace keeps its own, editable copy of the runner scripts.
ADAPTERS_DIR = "code/adapters"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def install_adapters(ws: Workspace) -> list[str]:
    """Copy the runner scripts into the workspace so agents can inspect, fix and version them.

    Safe to call before any run: a missing copy is installed, a copy nobody changed since AOS
    installed it is refreshed when AOS's version moved on, and a copy edited by the user or by an
    agent (the catalog says so) is left alone. Returns the paths installed or refreshed.
    """
    target = ws.root / ADAPTERS_DIR
    target.mkdir(parents=True, exist_ok=True)
    changed = []
    for script in sorted(RUNNERS_DIR.glob("run_*.py")) + [RUNNERS_DIR / "web_search.py"]:
        dest = target / script.name
        entry = ws.describe(dest) if dest.exists() else None
        if entry is not None:
            if entry["source"] != "aos" or _sha(dest) == _sha(script):
                continue  # edited by someone, or already current
            installed = next((t.split(":", 1)[1] for t in entry["tags"] if t.startswith("adapter-sha:")), None)
            if installed and installed != _sha(dest):
                continue  # changed on disk since AOS installed it: keep that version
        shutil.copyfile(script, dest)
        tags = [f"adapter-sha:{_sha(script)}"]
        if script.name == "web_search.py":
            ws.register(dest, source="aos", reason="Search tool that research agents run inside their sandbox",
                        summary="web_search.py: Serper web and Google Scholar search plus page fetching from the "
                                "shell; results are saved next to the run that made them.", tags=tags)
        else:
            system = script.stem.removeprefix("run_")
            ws.register(dest, source="aos", reason=f"Adapter script that runs {system} inside its own virtualenv",
                        summary=f"Adapter for {system}: instructions and workspace paths in, files out. "
                                "Edit here to fix the integration; the wrapper runs this copy.", tags=tags)
        changed.append(ws.relpath(dest))
    return changed


def external_dir() -> Path:
    return Path(os.environ.get("AOS_EXTERNAL_DIR", AOS_ROOT / "external"))


class ExternalCapability(Worker):
    #: Folder name under ``external/``.
    repo: str = ""
    #: Environment variables the system needs besides the LLM credentials.
    required_env: tuple[str, ...] = ()

    @property
    def repo_dir(self) -> Path:
        return external_dir() / self.repo

    @property
    def python(self) -> Path:
        return self.repo_dir / ".venv" / "bin" / "python"

    def runner(self, ws: Workspace, name: str) -> Path:
        """The workspace's copy of a runner script if it has one, else AOS's own."""
        local = ws.root / ADAPTERS_DIR / name
        return local if local.is_file() else RUNNERS_DIR / name

    def available(self) -> tuple[bool, str]:
        if not self.repo_dir.is_dir():
            return False, f"repository not found at {self.repo_dir}"
        if not self.python.exists():
            return False, f"no virtualenv at {self.python} (run scripts/setup_external.sh {self.repo})"
        missing = [v for v in ("API_KEY", "BASE_URL", *self.required_env) if not os.environ.get(v)]
        if missing:
            return False, f"missing environment variables: {', '.join(missing)}"
        return True, ""

    def env(self) -> dict[str, str]:
        """Environment for the runner: the LLM credentials under both AOS and OpenAI-style names."""
        return {
            "API_KEY": os.environ["API_KEY"],
            "BASE_URL": os.environ["BASE_URL"],
            "AOS_MODEL": os.environ.get("AOS_MODEL", DEFAULT_MODEL),
            "OPENAI_API_KEY": os.environ["API_KEY"],
            "OPENAI_BASE_URL": os.environ["BASE_URL"],
            "PYTHONUNBUFFERED": "1",
            "LD_LIBRARY_PATH": clean_library_path(os.environ.get("LD_LIBRARY_PATH", "")),
            "AOS_PRICES": json.dumps({m: list(p) for m, p in load_prices().items()}),
        }

    def report_usage(self, output_dir: Path) -> dict | None:
        """Pick up the usage.json a runner wrote next to its outputs."""
        self.last_usage = read_usage(output_dir)
        return self.last_usage


def clean_library_path(value: str) -> str:
    """Drop compiler-SDK library directories: their libgomp shadows the one bundled with torch."""
    return os.pathsep.join(p for p in value.split(os.pathsep) if p and "hpc_sdk" not in p)

```
