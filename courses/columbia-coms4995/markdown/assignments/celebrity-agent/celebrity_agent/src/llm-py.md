# celebrity-agent: celebrity_agent/src/llm.py

[Course index](../../../../../README.md) · [Original source](https://designing-agents.github.io/assets/celebrity_agent.zip#archive-member=celebrity_agent/src/llm.py) · [Raw file](../../../../../raw/assignments/celebrity-agent/celebrity_agent/src/llm.py)

Retrieved: 2026-11-13T16:41:03.995785+00:00

```python
"""Gemini client helper for HW3."""

import os
from google import genai

MODEL_NAME = "gemini-3.5-flash-lite"

# Use the following documentation to call the Gemini API:
#
#   sdk:     https://googleapis.github.io/python-genai/
#   api:     https://ai.google.dev/api/generate-content

def query_llm(prompt: str, temperature: float = 0.0) -> str:
    """Send a prompt to Gemini and return the raw string response."""
    api_key = os.getenv("GEMINI_API_KEY")
    raise NotImplementedError

```
