# Project code: stanford-oval/genie-worksheets: experiments/agents/tipbot/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/tipbot/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/tipbot/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

from worksheets.agents.tipbot.api import send_tip

current_dir = os.path.dirname(os.path.abspath(__file__))
example_prompt_dir = os.path.join(current_dir, "prompts")

starting_prompt = "Hello! I'm the Stanford Daily. I'm here to help you submit a tip. What would you like to do?"
api_list = [send_tip]
botname = "TipBot"
initial_api = "Tip"

description = """You are an assistant for Stanford Daily. Stanford Daily is a local news organisation that covers news, sports, and events at Stanford University. You are responsible for managing the tip submissions from the community. You need to get the tips from the user, answer their queries and ask follow up questions about events and incidents happening around the campus."""

```
