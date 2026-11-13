# Code: lecture5-frameworks: tinycal/__init__.py

[Course index](../../../../README.md) · [Original source](https://github.com/cs329z/lecture5-frameworks/blob/HEAD/tinycal/__init__.py) · [Raw file](../../../../raw/repositories/cs329z-lecture5-frameworks/tinycal/__init__.py)

Retrieved: 2026-11-13T16:20:40.422150+00:00

```python
"""tinycal: a tiny, dependency-free calendar app with a Python SDK for agent tool calls.

Run the app:        python -m tinycal
Use from Python:    import tinycal; tinycal.ensure_server(); tinycal.add_event(...)
List the API:       print(tinycal.api())
"""

from .sdk import (  # noqa: F401
    TOOLS,
    CalendarError,
    add_event,
    api,
    clear_calendar,
    delete_event,
    ensure_server,
    find_free_slots,
    list_events,
    today,
    update_event,
)

__all__ = [
    "TOOLS",
    "CalendarError",
    "add_event",
    "api",
    "clear_calendar",
    "delete_event",
    "ensure_server",
    "find_free_slots",
    "list_events",
    "today",
    "update_event",
]

```
