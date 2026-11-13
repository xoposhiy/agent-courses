# Project code: stanford-oval/genie-worksheets: experiments/agents/doctor_followup/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/doctor_followup/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/doctor_followup/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.doctor_followup import api
from worksheets.agents.doctor_followup.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.doctor_followup.custom_suql import suql_runner
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "1Cb0JC2UtbLCIMRHxFtF8PZGTjANvkGS-wECubAASe64"
suql_prompt_selector = None

```
