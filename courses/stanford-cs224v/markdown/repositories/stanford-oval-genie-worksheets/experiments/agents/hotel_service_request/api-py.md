# Project code: stanford-oval/genie-worksheets: experiments/agents/hotel_service_request/api.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/hotel_service_request/api.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/hotel_service_request/api.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import random
from uuid import UUID, uuid4


def hotel_service(
    hotel_name: str,
    customer_name: str,
    room_number: int,
    service_request: str,
    time: str,
):
    service_can_be_done = random.choice([True, False])

    if not service_can_be_done:
        return {
            "message": "Sorry, we are not able to provide the service at the moment. Please try again later.",
        }
    else:
        return {
            "hotel_name": hotel_name,
            "customer_name": customer_name,
            "room_number": room_number,
            "service_request": service_request,
            "time": time,
            "success": True,
        }

```
