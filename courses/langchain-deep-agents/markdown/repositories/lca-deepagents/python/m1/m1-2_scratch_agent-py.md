# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m1/m1.2_scratch_agent.py

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m1/m1.2_scratch_agent.py) · [Raw file](../../../../../raw/repositories/lca-deepagents/python/m1/m1.2_scratch_agent.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
from deepagents import create_deep_agent

from models import model

agent = create_deep_agent(model=model)

result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM?"}]})

print(result["messages"][-1].text)

```
