# celebrity-agent: celebrity_agent/src/agent.py

[Course index](../../../../../README.md) · [Original source](https://designing-agents.github.io/assets/celebrity_agent.zip#archive-member=celebrity_agent/src/agent.py) · [Raw file](../../../../../raw/assignments/celebrity-agent/celebrity_agent/src/agent.py)

Retrieved: 2026-11-13T16:41:03.995785+00:00

```python
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

```
