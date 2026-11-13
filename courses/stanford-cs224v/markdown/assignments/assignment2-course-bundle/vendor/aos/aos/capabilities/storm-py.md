# Homework 2 bundle: vendor/aos/aos/capabilities/storm.py

[Course index](../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/capabilities/storm.py) · [Raw file](../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/capabilities/storm.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""STORM: general deep research on a topic from web search."""

from __future__ import annotations

from pathlib import Path

from ..tasks import Step
from ..worker import StepFailed, run_command
from ..workspace import Workspace
from .base import ExternalCapability


class Storm(ExternalCapability):
    name = "storm"
    repo = "storm"
    required_env = ("SERPER_API_KEY",)
    description = (
        "STORM: broad research on any topic for a general audience using web search; writes a long, "
        "Wikipedia-style report with numbered citations (for academic depth with source-verified "
        "claims use grill instead). instructions = the research topic or "
        "question (say what aspects to cover); inputs are ignored. Produces in output_dir: "
        "report.md (the report), url_to_info.json (cited sources with snippets), "
        "raw_search_results.json, storm_gen_outline.txt and conversation_log.json; every search "
        "hit and fetched web page is archived under sources/webpages/<output_dir name>/ "
        "(results/*.json, pages/*.txt and *.html). Takes 5-15 minutes; use a fresh output_dir per topic."
    )

    def run(self, ws: Workspace, step: Step, log: Path) -> str:
        out = ws.abspath(step.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        sources = ws.root / "sources" / "webpages" / out.name
        run_command(
            [self.python, self.runner(ws, "run_storm.py"), "--topic", step.instructions,
             "--output-dir", out, "--sources-dir", sources],
            cwd=self.repo_dir, log=log, env=self.env(), timeout=3 * 3600,
        )
        self.report_usage(out)
        report = out / "report.md"
        if not report.is_file():
            raise StepFailed("STORM finished but produced no report.md; see the step log")
        words = len(report.read_text().split())
        pages = len(list((sources / "pages").glob("*.txt"))) if (sources / "pages").is_dir() else 0
        return (f"STORM wrote {ws.relpath(report)} ({words} words); cited sources in "
                f"{step.output_dir}/url_to_info.json; {pages} fetched pages archived in {ws.relpath(sources)}/")

```
