# Assignment 3: scottyrl/agents/__init__.py

[Course index](../../../../../README.md) · [Original source](https://github.com/cmu-agents/assignment-3/blob/HEAD/scottyrl/agents/__init__.py) · [Raw file](../../../../../raw/repositories/cmu-assignment-3/scottyrl/agents/__init__.py)

Retrieved: 2026-11-13T16:48:20.158886+00:00

```python
"""Agent registry (given). Add new agent classes here."""

from __future__ import annotations

from scottyrl.agents.base import Agent, AgentAction
from scottyrl.agents.xml_tool_call import XMLToolCallAgent
from scottyrl.policy import Policy

AGENT_REGISTRY: dict[str, type[Agent]] = {
    "xml_toolcall": XMLToolCallAgent,
}


def make_agent(name: str, policy: Policy) -> Agent:
    if name not in AGENT_REGISTRY:
        raise ValueError(f"Unknown agent '{name}'. Options: {sorted(AGENT_REGISTRY)}")
    return AGENT_REGISTRY[name](policy)


__all__ = ["Agent", "AgentAction", "XMLToolCallAgent", "AGENT_REGISTRY", "make_agent"]

```
