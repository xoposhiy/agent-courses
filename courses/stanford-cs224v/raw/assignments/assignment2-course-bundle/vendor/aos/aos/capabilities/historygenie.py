"""HistoryGenie: extraction (OCR to markdown) over image-based documents."""

from __future__ import annotations

from pathlib import Path

from ..tasks import Step
from ..worker import StepFailed, run_command
from ..workspace import Workspace
from .base import ExternalCapability


class HistoryGenie(ExternalCapability):
    name = "historygenie"
    repo = "historygenie"
    description = (
        "HistoryGenie: transcribes image-based documents (scanned PDFs, PNG/JPG/TIFF/WEBP images) "
        "into markdown text with a vision LLM, preserving headings and tables. inputs = the PDF/image "
        "files or directories of them (required); instructions are ignored (fixed transcription "
        "prompt). Produces one <document name>.md per input in output_dir, with one section per "
        "page. Use it first when documents are images rather than text, then hand the markdown to "
        "sliders or coding_agent."
    )

    def run(self, ws: Workspace, step: Step, log: Path) -> str:
        if not step.inputs:
            raise StepFailed("historygenie needs PDF or image files as inputs")
        out = ws.abspath(step.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        inputs = [ws.abspath(i) for i in step.inputs]
        run_command(
            [self.python, self.runner(ws, "run_historygenie.py"), "--output-dir", out, "--inputs", *inputs],
            cwd=self.repo_dir, log=log, env=self.env(), timeout=2 * 3600,
        )
        self.report_usage(out)
        produced = sorted(p.name for p in out.glob("*.md"))
        if not produced:
            raise StepFailed("HistoryGenie finished but produced no markdown; see the step log")
        return f"HistoryGenie transcribed {len(produced)} document(s) into {step.output_dir}/: {', '.join(produced)}"
