# Project code: stanford-oval/genie-worksheets: src/worksheets/__init__.py

[Course index](../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/src/worksheets/__init__.py) · [Raw file](../../../../../raw/repositories/stanford-oval-genie-worksheets/src/worksheets/__init__.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from worksheets.agent.builder import AgentBuilder
from worksheets.agent.config import AzureModelConfig, Config, OpenAIModelConfig
from worksheets.knowledge.parser import (
    DatatalkParser,
    SUQLKnowledgeBase,
    SUQLReActParser,
)
from worksheets.utils.interface import conversation_loop
from worksheets.llm.prompts import init_llm

import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

init_llm(
    prompt_dir=os.path.join(CURRENT_DIR, "prompts"),
    dotenv_path=os.path.join(CURRENT_DIR, "..", ".env"),
)


__all__ = [
    "SUQLKnowledgeBase",
    "SUQLReActParser",
    "DatatalkParser",
    "conversation_loop",
    "AgentBuilder",
    "Config",
    "AzureModelConfig",
    "OpenAIModelConfig",
]

```
