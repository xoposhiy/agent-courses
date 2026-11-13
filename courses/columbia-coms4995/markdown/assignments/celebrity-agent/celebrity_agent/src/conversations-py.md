# celebrity-agent: celebrity_agent/src/conversations.py

[Course index](../../../../../README.md) · [Original source](https://designing-agents.github.io/assets/celebrity_agent.zip#archive-member=celebrity_agent/src/conversations.py) · [Raw file](../../../../../raw/assignments/celebrity-agent/celebrity_agent/src/conversations.py)

Retrieved: 2026-11-13T16:41:03.995785+00:00

```python
"""Conversation store: create, list, load, and save conversations."""

from dataclasses import dataclass, field


@dataclass
class Conversation:
    """One conversation between a user and the agent."""

    conversation_id: str
    turns: list[dict] = field(default_factory=list)
    ended: bool = False


def create_conversation(store_dir: str = "data/conversations") -> Conversation:
    """Start a new, empty conversation and save it."""
    raise NotImplementedError

def list_conversations(store_dir: str = "data/conversations") -> list[Conversation]:
    """Return every saved conversation."""
    raise NotImplementedError

def load_conversation(conversation_id: str, store_dir: str = "data/conversations") -> Conversation:
    """Load one saved conversation."""
    raise NotImplementedError

def save_conversation(conversation: Conversation, store_dir: str = "data/conversations") -> None:
    """Write a conversation to disk."""
    raise NotImplementedError

```
