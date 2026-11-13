# Project code: stanford-oval/genie-worksheets: experiments/agents/hotel_book/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/hotel_book/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/hotel_book/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.hotel_book import api
from worksheets.agents.hotel_book.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.hotel_book.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "11yI3uFOw1tGCLZWvofvdTyforQZsKDArjWt_DkNt0DM"
suql_prompt_selector = None

```
