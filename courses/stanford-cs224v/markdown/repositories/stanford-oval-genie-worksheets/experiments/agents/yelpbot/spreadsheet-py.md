# Project code: stanford-oval/genie-worksheets: experiments/agents/yelpbot/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/yelpbot/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/yelpbot/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.yelpbot import api
from worksheets.agents.yelpbot.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.yelpbot.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "1pCAMsK4xh5QbYD9aPUG66iMOdOJt-xJRVZqZyl23TgI"

suql_prompt_selector = None

```
