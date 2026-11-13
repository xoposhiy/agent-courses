# Project code: stanford-oval/genie-worksheets: experiments/agents/plane_book/api.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/plane_book/api.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/plane_book/api.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import random
from uuid import UUID, uuid4


def check_availability(user_name: str, flight_id: str):
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


def book_hotel_visit(user_name: str, hotel_id: str):
    return {
        "status": "success",
        "booking_id": str(uuid4()),
    }

```
