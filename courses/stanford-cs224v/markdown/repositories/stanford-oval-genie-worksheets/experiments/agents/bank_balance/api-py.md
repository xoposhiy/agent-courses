# Project code: stanford-oval/genie-worksheets: experiments/agents/bank_balance/api.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/bank_balance/api.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/bank_balance/api.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from uuid import UUID, uuid4


def bank_fraud_report(full_name, fraud_report, **kwargs):
    return {
        "status": "success",
        "error": None,
        "report_id": str(uuid4()),
    }

```
