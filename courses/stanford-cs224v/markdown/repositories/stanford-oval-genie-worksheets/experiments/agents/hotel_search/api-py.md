# Project code: stanford-oval/genie-worksheets: experiments/agents/hotel_search/api.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/hotel_search/api.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/hotel_search/api.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import random
from uuid import UUID, uuid4


def hotel_search(
    hotel_name: str,
    location: str,
    cost: str,
    min_rating: str,
    max_rating: str,
):
    min_rating = int(min_rating)
    max_rating = int(max_rating)

    min_rating_limit = 0
    max_rating_limit = 5

    if min_rating < min_rating_limit or min_rating > max_rating_limit:
        return {
            "message": "Couldn't find any hotels with the given rating range. Please try again.",
        }

    return {
        "hotel_name": hotel_name,
        "location": location,
        "cost": cost,
        "rating": random.randint(min_rating, max_rating),
    }

```
