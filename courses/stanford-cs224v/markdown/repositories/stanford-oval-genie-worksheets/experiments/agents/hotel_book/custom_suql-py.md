# Project code: stanford-oval/genie-worksheets: experiments/agents/hotel_book/custom_suql.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/hotel_book/custom_suql.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/hotel_book/custom_suql.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

from loguru import logger
from suql import suql_execute
from suql.agent import postprocess_suql

from worksheets.llm.basic import llm_generate


def suql_runner(query, *args, **kwargs):
    return []

```
