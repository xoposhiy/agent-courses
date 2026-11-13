# Project code: stanford-oval/genie-worksheets: src/worksheets/core/dialogue.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/src/worksheets/core/dialogue.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/src/worksheets/core/dialogue.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from dataclasses import dataclass
from typing import List, Optional

from worksheets.core.context import GenieContext


@dataclass
class CurrentDialogueTurn:
    """Represents a single turn in the dialogue."""

    # User's utterance in natural language
    user_utterance: Optional[str] = None

    # User's target semantic representation
    user_target_sp: Optional[str] = None

    # Final user target after rewrites
    user_target: Optional[str] = None

    # System's response to the user
    system_response: Optional[str] = None

    # System's target action
    system_target: Optional[str] = None

    # System Dialogue acts
    system_action: Optional[List[str]] = None

    # Flag to indicate if the user is asking a question
    user_is_asking_question: bool = False

    # Context for the current dialogue turn
    context: Optional["GenieContext"] = None

    # Global context for the dialogue
    global_context: Optional["GenieContext"] = None

    # User's target SUQL query
    user_target_suql: Optional[str] = None

```
