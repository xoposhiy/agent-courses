# Project code: stanford-oval/genie-worksheets: experiments/agents/apartment_search/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/apartment_search/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/apartment_search/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.apartment_search import api
from worksheets.agents.apartment_search.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.apartment_search.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "1-j9c6Bg7hz3EglpR0WE6Lip8qSz8y_TsXe_evJTHsIo"
suql_prompt_selector = None

```
