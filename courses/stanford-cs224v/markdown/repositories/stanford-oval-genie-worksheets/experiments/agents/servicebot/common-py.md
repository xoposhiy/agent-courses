# Project code: stanford-oval/genie-worksheets: experiments/agents/servicebot/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/servicebot/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/servicebot/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
prompt_dir = os.path.join(current_dir, "prompts")

botname = "ServiceBot"
starting_prompt = """Hello! I'm ServiceBot. I'm here to help you answer you questions and **generate a help ticket**.

I have the following capabilities:
- Troubleshooting Student Enrollment Issues, such as changing course or joining waitlist 
- Issues with Leave of Absence
- Problems with Test submitting scores or missing credits
"""
description = "You an assistant for Stanford student services. You can help the student with their questions and generate a help ticket if needed."

```
