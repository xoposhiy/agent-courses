# Project code: stanford-oval/genie-worksheets: experiments/agents/doctor_followup/api.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/doctor_followup/api.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/doctor_followup/api.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import random
from uuid import UUID, uuid4


def doctor_followup_instructions(*args, **kwargs):
    outputs = [
        "You must take your medicine 2 times a day before meals.",
        "Take your medicine before you go to sleep. If you experience nausea, please contact your doctor immediately.",
    ]

    return {"message": random.choice(outputs)}

```
