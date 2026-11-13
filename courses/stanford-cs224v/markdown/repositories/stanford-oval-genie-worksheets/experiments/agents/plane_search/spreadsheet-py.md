# Project code: stanford-oval/genie-worksheets: experiments/agents/plane_search/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/plane_search/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/plane_search/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.plane_search import api
from worksheets.agents.plane_search.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.plane_search.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "16qRkQgDSq1JtkNSzxv295zSBjq4nFwYarXx1EQsihkI"
suql_prompt_selector = None

```
