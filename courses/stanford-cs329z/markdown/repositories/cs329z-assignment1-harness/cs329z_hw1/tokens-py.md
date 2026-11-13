# HW1 Released: assignment1-harness: cs329z_hw1/tokens.py

[Course index](../../../../README.md) · [Original source](https://github.com/cs329z/assignment1-harness/blob/HEAD/cs329z_hw1/tokens.py) · [Raw file](../../../../raw/repositories/cs329z-assignment1-harness/cs329z_hw1/tokens.py)

Retrieved: 2026-11-13T16:35:03.050392+00:00

```python
"""Course-provided token counter.

Every budget in this assignment (the loop's token budget, the agent's context
budget, the search tools' result budget) is measured with these two
functions. They are a deterministic approximation (4 characters per token),
not the provider's tokenizer, so that the deterministic tests never need the
network and everyone's numbers agree.
"""

from __future__ import annotations

import math
from typing import Sequence

CHARS_PER_TOKEN = 4
MESSAGE_OVERHEAD = 4  # tokens charged per message for its role and framing


def count_tokens(text: str) -> int:
    """Tokens in one string."""
    return math.ceil(len(text) / CHARS_PER_TOKEN)


def count_message_tokens(messages: Sequence[dict]) -> int:
    """Tokens in a list of {"role", "content"} messages, as sent to the LM."""
    return sum(count_tokens(m["content"]) + MESSAGE_OVERHEAD for m in messages)

```
