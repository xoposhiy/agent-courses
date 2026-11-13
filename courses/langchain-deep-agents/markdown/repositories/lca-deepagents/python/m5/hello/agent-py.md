# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m5/hello/agent.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m5/hello/agent.py) · [Raw file](../../../../../../raw/repositories/lca-deepagents/python/m5/hello/agent.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
# python/m5/hello/agent.py
"""A minimal deep agent, exposed as a graph for `langgraph dev`.

This is the whole agent: a model, nothing else. The point of this lab is the
*deployment*, not the agent — so we keep the agent as small as it gets and let
`langgraph dev` serve it over HTTP.
"""

from deepagents import create_deep_agent

from models import model

# `langgraph.json` points at this module-level variable: "./agent.py:graph".
graph = create_deep_agent(model=model)

```
