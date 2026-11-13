# celebrity-agent: celebrity_agent/src/guardrails.py

[Course index](../../../../../README.md) · [Original source](https://designing-agents.github.io/assets/celebrity_agent.zip#archive-member=celebrity_agent/src/guardrails.py) · [Raw file](../../../../../raw/assignments/celebrity-agent/celebrity_agent/src/guardrails.py)

Retrieved: 2026-11-13T16:41:03.995785+00:00

```python
"""Guardrails: decline questions the celebrity would not know about."""


def out_of_scope(user_message: str, history: list[dict]) -> bool:
    """Return True if the message asks about events after the knowledge cutoff or outside the celebrity's expertise."""
    raise NotImplementedError

def decline(user_message: str) -> str:
    """Return an in-character response saying the celebrity doesn't know."""
    raise NotImplementedError

```
