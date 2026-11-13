# Project code: stanford-oval/genie-worksheets: src/worksheets/core/__init__.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/src/worksheets/core/__init__.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/src/worksheets/core/__init__.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.core.context import GenieContext
from worksheets.core.dialogue import CurrentDialogueTurn
from worksheets.core.fields import GenieField, GenieResult, GenieValue
from worksheets.core.runtime import GenieRuntime

__all__ = [
    "GenieField",
    "GenieResult",
    "GenieValue",
    "GenieContext",
    "GenieRuntime",
    "CurrentDialogueTurn",
]

```
