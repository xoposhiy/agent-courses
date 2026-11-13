# Project code: stanford-oval/genie-worksheets: experiments/agents/hotel_book/api.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/hotel_book/api.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/hotel_book/api.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import random
from uuid import UUID, uuid4


def check_availability(
    customer_name, hotel_name, start_date, end_date, customer_request
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


def book_hotel_visit(customer_name, hotel_name, start_date, end_date, customer_request):
    return {
        "status": "success",
        "booking_id": str(uuid4()),
    }

```
