"""Agent: wire guardrails, content, style, and sign-off into one turn."""

from .content_module import content_step
from .conversations import Conversation
from .guardrails import decline, out_of_scope
from .memory_store import MemoryStore
from .style_module import stylize


def should_end(user_message: str, history: list[dict]) -> bool:
    """Determine if the conversation should end."""
    raise NotImplementedError

def add_signoff(response: str) -> str:
    """Add a signoff to the response."""
    raise NotImplementedError

def respond(memory: MemoryStore, conversation: Conversation, user_message: str) -> str:
    """Run one turn of the agent, add it to the conversation, and mark the conversation ended if it is over."""
    raise NotImplementedError
