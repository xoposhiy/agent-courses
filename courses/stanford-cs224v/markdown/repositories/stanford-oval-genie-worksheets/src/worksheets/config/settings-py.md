# Project code: stanford-oval/genie-worksheets: src/worksheets/config/settings.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/src/worksheets/config/settings.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/src/worksheets/config/settings.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
"""Genie Worksheets runtime settings.

This module centralises simple runtime configuration switches.  Settings can
be overridden through environment variables so that behaviour can be changed
without code modification or redeploy.
"""

from __future__ import annotations

import os

__all__ = [
    "OPEN_NEW_WORKSHEET_IF_POSSIBLE",
]


def _env_flag(var_name: str, default: str = "1") -> bool:
    """Return ``True`` unless *var_name* is set to an explicit false-y string.

    Accepted false values (case-insensitive): "0", "false", "no".
    Anything else – or unset – is treated as *truthy*.
    """
    return os.getenv(var_name, default).strip().lower() not in {"0", "false", "no"}


# ---------------------------------------------------------------------------
# Feature toggles
# ---------------------------------------------------------------------------

# Whether the agent is allowed to automatically open a new worksheet when it
# still has room for more agent acts.
OPEN_NEW_WORKSHEET_IF_POSSIBLE: bool = _env_flag("GENIE_OPEN_WS", "0")

```
