# Project code: stanford-oval/genie-worksheets: experiments/agents/servicebot/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/servicebot/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/servicebot/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.servicebot import api
from worksheets.agents.servicebot.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.servicebot.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "1aNAG5xh1F_6EmtUAYTmoOBlJBdnpl7lgiZ9YhIW8UxA"

suql_prompt_selector = None

```
