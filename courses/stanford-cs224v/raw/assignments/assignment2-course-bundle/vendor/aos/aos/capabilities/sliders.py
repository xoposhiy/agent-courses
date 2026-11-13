"""SLIDERS: documents -> structured table with provenance -> answer."""

from __future__ import annotations

from pathlib import Path

from ..tasks import Step
from ..worker import StepFailed, run_command
from ..workspace import Workspace
from .base import ExternalCapability


class Sliders(ExternalCapability):
    name = "sliders"
    repo = "sliders-new"
    description = (
        "SLIDERS: turns a set of text/markdown documents into a structured table (schema chosen "
        "for the question, one row per extracted entity/feature, every cell backed by a quote with a "
        "file:line locator) and answers a question over that table. instructions = the question or "
        "what to extract (e.g. 'List the clinical features, symptoms, genetic cause, diagnostic tests "
        "and treatments of X as a table'); inputs = one or more .md/.txt files or directories of "
        "them (required; PDFs and images are not accepted). Produces in output_dir: "
        "tables/<Table>.csv per extracted table, evidence.csv (every value with its quote and "
        "locator), table.json, answer.md and answer.json (grounded answer with citations)."
    )

    def run(self, ws: Workspace, step: Step, log: Path) -> str:
        if not step.inputs:
            raise StepFailed("sliders needs at least one input document or directory")
        out = ws.abspath(step.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        docs = [ws.abspath(i) for i in step.inputs]
        run_command(
            [self.python, self.runner(ws, "run_sliders.py"), "--question", step.instructions,
             "--output-dir", out, "--docs", *docs],
            cwd=self.repo_dir, log=log, env=self.env(), timeout=3 * 3600,
        )
        self.report_usage(out)
        tables = sorted(p.name for p in (out / "tables").glob("*.csv")) if (out / "tables").is_dir() else []
        if not tables:
            raise StepFailed("SLIDERS finished but produced no tables; see the step log")
        return (f"SLIDERS built {len(tables)} table(s) ({', '.join(tables)}) in {step.output_dir}/tables/ "
                f"with evidence.csv and answered the question in {step.output_dir}/answer.md")
