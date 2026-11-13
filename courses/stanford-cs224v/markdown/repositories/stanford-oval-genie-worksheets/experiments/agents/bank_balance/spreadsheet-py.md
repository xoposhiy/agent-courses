# Project code: stanford-oval/genie-worksheets: experiments/agents/bank_balance/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/bank_balance/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/bank_balance/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.bank_balance import api
from worksheets.agents.bank_balance.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.bank_balance.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "1nYcIjJg7SA7hJQwMbfK5II3OmP1VOZX_9gZrwehHO3w"
suql_prompt_selector = None

```
