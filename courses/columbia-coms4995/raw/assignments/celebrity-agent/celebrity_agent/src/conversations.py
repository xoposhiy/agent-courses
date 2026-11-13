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
