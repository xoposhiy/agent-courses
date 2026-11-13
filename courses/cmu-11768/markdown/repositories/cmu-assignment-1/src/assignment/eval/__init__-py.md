# Assignment 1: src/assignment/eval/__init__.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/cmu-agents/assignment-1/blob/HEAD/src/assignment/eval/__init__.py) · [Raw file](../../../../../../raw/repositories/cmu-assignment-1/src/assignment/eval/__init__.py)

Retrieved: 2026-11-13T16:48:10.751888+00:00

```python
"""Instructor-side patch evaluation helpers."""

from assignment.eval.harness import (
    EvaluationSpec,
    Report,
    TestStatus,
    evaluate,
    parse_pytest_report,
    resolve_image,
)
from assignment.task import Task

__all__ = [
    "EvaluationSpec",
    "Report",
    "Task",
    "TestStatus",
    "evaluate",
    "resolve_image",
    "parse_pytest_report",
]

```
