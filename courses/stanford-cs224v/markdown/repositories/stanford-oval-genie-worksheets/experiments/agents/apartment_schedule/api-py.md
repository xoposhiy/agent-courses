# Project code: stanford-oval/genie-worksheets: experiments/agents/apartment_schedule/api.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/apartment_schedule/api.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/apartment_schedule/api.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import random
from uuid import UUID, uuid4


def check_availability(
    customer_name,
    apartment_name,
    day_of_visit,
    start_time,
    application_fee_paid,
    special_request_from_customer,
):
    if random.random() > 0.5:
        return {
            "status": "success",
            "booking_available": True,
        }
    else:
        return {
            "status": "success",
            "booking_available": False,
        }


def book_apartment_visit(
    customer_name,
    apartment_name,
    day_of_visit,
    start_time,
    application_fee_paid,
    special_request_from_customer,
):
    return {
        "status": "success",
        "booking_id": str(uuid4()),
    }

```
