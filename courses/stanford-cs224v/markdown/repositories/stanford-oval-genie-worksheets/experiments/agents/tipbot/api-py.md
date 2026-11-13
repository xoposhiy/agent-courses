# Project code: stanford-oval/genie-worksheets: experiments/agents/tipbot/api.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/tipbot/api.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/tipbot/api.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from uuid import uuid4


def send_tip(params):
    """Send a tip to the tipbot."""
    return {
        "type": "send_tip",
        "params": params,
        "id": str(uuid4()),
    }

```
