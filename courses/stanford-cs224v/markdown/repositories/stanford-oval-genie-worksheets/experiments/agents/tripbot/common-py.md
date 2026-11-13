# Project code: stanford-oval/genie-worksheets: experiments/agents/tripbot/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/tripbot/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/tripbot/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
prompt_dir = os.path.join(current_dir, "prompts")

botname = "Trip Direction Bot"
starting_prompt = "Hello! I am a trip direction bot. I can help you find directions to a location. What is your mode of transportation?"
description = "You are a trip direction bot. You can help users find directions to a location, based on their mode of transportation, time of departure, and other preferences."

```
