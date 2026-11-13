# Assignment 1: tests/test_smoke.py

[Course index](../../../../README.md) · [Original source](https://github.com/cmu-agents/assignment-1/blob/HEAD/tests/test_smoke.py) · [Raw file](../../../../raw/repositories/cmu-assignment-1/tests/test_smoke.py)

Retrieved: 2026-11-13T16:48:10.751888+00:00

```python
import assignment
import assignment.agent


def test_package_importable():
    assert assignment is not None
    assert assignment.agent is not None

```
