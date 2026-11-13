# Project code: stanford-oval/genie-worksheets: src/worksheets/utils/rumtime.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/src/worksheets/utils/rumtime.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/src/worksheets/utils/rumtime.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from functools import partial


def callable_name(any_callable):
    if isinstance(any_callable, partial):
        return any_callable.func.__name__

    try:
        return any_callable.__name__
    except AttributeError:
        return str(any_callable)

```
