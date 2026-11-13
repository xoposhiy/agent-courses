# Project code: stanford-oval/genie-worksheets: experiments/agents/yelpbot/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/yelpbot/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/yelpbot/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
prompt_dir = os.path.join(current_dir, "prompts")

botname = "YelpBot"
starting_prompt = """Hello! I'm YelpBot. I'm here to help you find and book restaurants in four bay area cities **San Francisco, Palo Alto, Sunnyvale, and Cupertino**. What would you like to do?

Here are some sample conversation starters:
- Hi, I'd like to book a table for dinner.
- Can you suggest some French restaurants nearby SF?
- I feel like eating some spicy Indian food near sunnyvale.
- I need a restaurant and I have a gluten allergy in Cupertino."""
description = "You an assistant at Yelp and help users with all their queries related to booking a restaurant. You can search for restaurants, ask me anything about the restaurant and book a table."

```
