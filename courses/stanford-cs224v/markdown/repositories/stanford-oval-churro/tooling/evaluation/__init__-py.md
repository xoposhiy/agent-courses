# Project code: stanford-oval/Churro: tooling/evaluation/__init__.py

[Course index](../../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/tooling/evaluation/__init__.py) · [Raw file](../../../../../raw/repositories/stanford-oval-churro/tooling/evaluation/__init__.py)

Retrieved: 2026-11-13T17:04:51.902331+00:00

```python
"""Repo-only evaluation utilities for benchmark workflows."""

from tooling.evaluation.evaluate_page import (
    aggregate_results,
    batch_evaluate,
    calculate_metrics,
    calculate_metrics_from_text,
    evaluate_page,
)
from tooling.evaluation.metrics import (
    calculate_language_and_type_metrics,
    compute_metrics,
    to_rounded_percentage,
)

__all__ = [
    "aggregate_results",
    "batch_evaluate",
    "calculate_language_and_type_metrics",
    "calculate_metrics",
    "calculate_metrics_from_text",
    "compute_metrics",
    "evaluate_page",
    "to_rounded_percentage",
]

```
