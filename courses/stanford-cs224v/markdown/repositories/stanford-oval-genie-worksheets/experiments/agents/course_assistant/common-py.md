# Project code: stanford-oval/genie-worksheets: experiments/agents/course_assistant/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/course_assistant/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/course_assistant/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
prompt_dir = os.path.join(current_dir, "prompts")

botname = "Course Requirement Assistant"
starting_prompt = "Hello! I'm the Course Requirement Assistant. I can help you with filling submitting the course requirements form, you can ask me anything about the course requirements. What would you like to know?"
description = "You are a couse requirement assistant. You can help students with their course requirements."

```
