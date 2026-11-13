# Project code: stanford-oval/genie-worksheets: experiments/agents/course_enroll/spreadsheet.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/course_enroll/spreadsheet.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/course_enroll/spreadsheet.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agents.course_enroll import api
from worksheets.agents.course_enroll.common import (
    botname,
    description,
    prompt_dir,
    starting_prompt,
)
from worksheets.agents.course_enroll.custom_suql import (
    suql_prompt_selector,
    suql_runner,
)
from worksheets.specification.from_spreadsheet import gsheet_to_genie

gsheet_id_default = "1ejyFlZUrUZiBmFP3dLcVNcKqzAAfw292-LmyHXSFsTE"

```
