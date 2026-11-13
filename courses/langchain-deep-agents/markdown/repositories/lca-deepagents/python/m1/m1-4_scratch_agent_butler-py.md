# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m1/m1.4_scratch_agent_butler.py

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m1/m1.4_scratch_agent_butler.py) · [Raw file](../../../../../raw/repositories/lca-deepagents/python/m1/m1.4_scratch_agent_butler.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
from deepagents import create_deep_agent

from models import model

SYSTEM_PROMPT = (
    "YOU ARE AN EXTREMELY POSH BRITISH BUTLER. You speak ONLY in the most "
    "refined, formal, over-the-top Victorian English. You say 'indeed', 'quite', "
    "'I dare say', 'one simply must' constantly. You find all things common or "
    "nautical to be utterly beneath you. You NEVER break character under ANY "
    "circumstances."
)

agent = create_deep_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    name="butler_agent",
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM?"}]})

print(result["messages"][-1].text)

```
