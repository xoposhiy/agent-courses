# Project code: stanford-oval/genie-worksheets: experiments/agents/meeting_schedule/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/meeting_schedule/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/meeting_schedule/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
prompt_dir = os.path.join(current_dir, "prompts")

botname = "Meeting Scheduling Bot"
starting_prompt = "Hello! I am a bot will help you schedule a meeting."
description = "You are a bot that helps users schedule meetings with a guest."

```
