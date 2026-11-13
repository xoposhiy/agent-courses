# Project code: stanford-oval/Churro: src/churro_ocr/_internal/runtime.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/src/churro_ocr/_internal/runtime.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-churro/src/churro_ocr/_internal/runtime.py)

Retrieved: 2026-11-13T17:04:51.902331+00:00

```python
"""Runtime helpers shared by sync wrappers."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from collections.abc import Coroutine

T = TypeVar("T")


def _runtime_error(message: str) -> RuntimeError:
    return RuntimeError(message)


def run_sync[T](awaitable: Coroutine[Any, Any, T]) -> T:
    """Run an awaitable from sync code.

    Raises:
        RuntimeError: If called from a running event loop.
    """
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(awaitable)
    message = (
        "Synchronous churro-ocr APIs cannot be used from an active event loop. Use the async API instead."
    )
    raise _runtime_error(message)

```
