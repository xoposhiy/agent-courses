# Project code: stanford-oval/genie-worksheets: experiments/agents/doctor_schedule/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/doctor_schedule/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/doctor_schedule/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.doctor_schedule import api
from worksheets.agents.doctor_schedule.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.doctor_schedule.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "1GXiL_irt_gR1wk4RiJ36nKS6EveyXnH_4O4C9DxFahA"
suql_prompt_selector = None

```
