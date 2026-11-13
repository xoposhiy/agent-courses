# Homework 2 bundle: vendor/aos/aos/capabilities/grill.py

[Course index](../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/capabilities/grill.py) · [Raw file](../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/capabilities/grill.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""GRILL: scientific deep research with source-verified claims."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

from ..tasks import Step
from ..worker import StepFailed, run_command
from ..workspace import Workspace
from .base import ExternalCapability


class Grill(ExternalCapability):
    name = "grill"
    repo = "graph-search-sliders"
    required_env = ("SERPER_API_KEY",)
    description = (
        "GRILL: academic deep research, the choice for scientific, medical or technical questions "
        "where evidence quality matters (papers, mechanisms, clinical findings, methods, numbers). "
        "A budget-bounded agent explores research directions, forms hypotheses and tests each against "
        "sources it retrieves with Google Scholar and web search (papers with DOI/PMID, web pages), "
        "then writes a ranked, cited report. instructions = one research question (say which aspects "
        "matter); inputs are ignored. Produces in output_dir: report.md (findings with a Sources "
        "section), sources.csv (every evidence item with its DOI/PMID/URL and quote), findings.csv, "
        "metrics.csv (every number reported by a source) and grill_run/ (ledger.json, run.json, "
        "per-call transcripts, searches/ with every query and fetched page). Every hypothesis is "
        "screened and then verified against sources it reads (by default a focused check plus one deliberate "
        "search for contradicting evidence; "
        "AOS_GRILL_VERIFY=deep restores the adversarial counter-evidence hunt, off skips verification; "
        "AOS_GRILL_SCREEN=0 skips the screen so every hypothesis is verified directly). "
        "Slow (tens of minutes), so give it one well-posed question; for a general-audience overview "
        "of a topic use storm instead."
    )

    def available(self) -> tuple[bool, str]:
        ok, why = super().available()
        if not ok:
            return ok, why
        if not shutil.which("codex"):
            return False, "the codex CLI is not on PATH (npm i -g @openai/codex)"
        return True, ""

    def run(self, ws: Workspace, step: Step, log: Path) -> str:
        out = ws.abspath(step.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        cmd = [self.python, self.runner(ws, "run_grill.py"), "--question", step.instructions, "--output-dir", out,
               "--tools", self.runner(ws, "web_search.py")]
        cmd += ["--verify", os.environ.get("AOS_GRILL_VERIFY", "light").strip().lower() or "light"]
        if os.environ.get("AOS_GRILL_SCREEN", "1").strip().lower() in ("0", "false", "no", "off"):
            cmd.append("--no-screen")
        run_command(
            cmd,
            cwd=self.repo_dir, log=log, env=self.env(), timeout=4 * 3600,
        )
        self.report_usage(out)
        report = out / "report.md"
        if not report.is_file():
            raise StepFailed("GRILL finished but produced no report.md; see the step log")
        sources = out / "sources.csv"
        n_sources = max(sum(1 for _ in open(sources)) - 1, 0) if sources.is_file() else 0
        return (f"GRILL wrote {ws.relpath(report)} ({len(report.read_text().split())} words) "
                f"with {n_sources} evidence items in {step.output_dir}/sources.csv")

```
