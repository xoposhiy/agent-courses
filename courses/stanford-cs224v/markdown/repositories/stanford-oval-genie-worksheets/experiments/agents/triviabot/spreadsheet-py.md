# Project code: stanford-oval/genie-worksheets: experiments/agents/triviabot/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/triviabot/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/triviabot/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.triviabot import api
from worksheets.agents.triviabot.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.triviabot.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "1oo7tasfwNDKQp6HO2BSsXKBKikrX7ubw6qEyzT9bMuM"
suql_prompt_selector = None

```
