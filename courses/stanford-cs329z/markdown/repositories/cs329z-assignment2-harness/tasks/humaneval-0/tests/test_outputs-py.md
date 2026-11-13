# HW2 Released: assignment2-harness: tasks/humaneval-0/tests/test_outputs.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/cs329z/assignment2-harness/blob/HEAD/tasks/humaneval-0/tests/test_outputs.py) · [Raw file](../../../../../../raw/repositories/cs329z-assignment2-harness/tasks/humaneval-0/tests/test_outputs.py)

Retrieved: 2026-11-13T16:35:14.032514+00:00

```python
"""Official HumanEval/0 checks, adapted to run against the Harbor task state."""

import sys

sys.path.insert(0, "/app")

from humaneval_0 import has_close_elements


def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) is True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) is False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) is True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) is False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) is True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) is True
    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) is False


check(has_close_elements)

```
