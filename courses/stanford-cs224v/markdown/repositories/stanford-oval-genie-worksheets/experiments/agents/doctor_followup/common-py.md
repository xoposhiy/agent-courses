# Project code: stanford-oval/genie-worksheets: experiments/agents/doctor_followup/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/doctor_followup/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/doctor_followup/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
prompt_dir = os.path.join(current_dir, "prompts")

botname = "Doctor Follow-up bot"
starting_prompt = "Hello! I am a bot that helps you get followup instructions from your doctor."
description = "You are a bot that helps patients get follow-up instructions from their doctors."

```
