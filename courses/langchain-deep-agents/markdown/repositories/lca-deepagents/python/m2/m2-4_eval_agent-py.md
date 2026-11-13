# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m2/m2.4_eval_agent.py

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m2/m2.4_eval_agent.py) · [Raw file](../../../../../raw/repositories/lca-deepagents/python/m2/m2.4_eval_agent.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware

from models import model

agent = create_deep_agent(
    model=model,
    middleware=[CodeInterpreterMiddleware()],
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Use the eval tool to compute and return the first 15 Fibonacci numbers.",
            }
        ]
    }
)

print(result["messages"][-1].text)

```
