# Homework 2 bundle: vendor/aos/aos/capabilities/datastorm.py

[Course index](../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/capabilities/datastorm.py) · [Raw file](../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/capabilities/datastorm.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""DataSTORM: analysis and insight generation over a database."""

from __future__ import annotations

from pathlib import Path

from ..tasks import Step
from ..worker import StepFailed, run_command
from ..workspace import Workspace
from .base import ExternalCapability


class DataStorm(ExternalCapability):
    name = "datastorm"
    repo = "datastorm"
    required_env = ("SERPER_API_KEY",)
    description = (
        "DataSTORM: analysis and insight generation over a database by an LLM-driven tree search "
        "of questions answered with SQL. instructions = the research question or topic to "
        "investigate in the data; inputs = one SQLite database (.db/.sqlite) or one or more CSV "
        "files (each CSV becomes a table). Produces in output_dir: report.md (an analyst-style "
        "report whose claims cite the queries that produced them), staged_report_*.json, tree.json "
        "(the explored question tree with answers), sql_results/*.csv (query results) and the "
        "SQLite database used. Slow (10-30 minutes)."
    )

    def run(self, ws: Workspace, step: Step, log: Path) -> str:
        if not step.inputs:
            raise StepFailed("datastorm needs a SQLite database or CSV files as inputs")
        out = ws.abspath(step.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        inputs = [ws.abspath(i) for i in step.inputs]
        run_command(
            [self.python, self.runner(ws, "run_datastorm.py"), "--topic", step.instructions,
             "--output-dir", out, "--sources-dir", ws.root / "sources" / "webpages" / out.name,
             "--inputs", *inputs],
            cwd=self.repo_dir, log=log, env=self.env(), timeout=3 * 3600,
        )
        self.report_usage(out)
        report = out / "report.md"
        if not report.is_file():
            raise StepFailed("DataSTORM finished but produced no report.md; see the step log")
        return f"DataSTORM wrote {ws.relpath(report)} ({len(report.read_text().split())} words) with query results in {step.output_dir}/sql_results/"

```
