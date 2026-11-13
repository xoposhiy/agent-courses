# Project code: stanford-oval/genie-worksheets: experiments/agents/tripbot/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/tripbot/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/tripbot/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.tripbot import api
from worksheets.agents.tripbot.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.tripbot.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "12dVJdhCFuIi020r1zgQplfA8He5OxYOzCRWelgCyc0c"
suql_prompt_selector = None

```
