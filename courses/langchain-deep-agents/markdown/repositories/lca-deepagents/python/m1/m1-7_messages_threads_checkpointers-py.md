# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m1/m1.7_messages_threads_checkpointers.py

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m1/m1.7_messages_threads_checkpointers.py) · [Raw file](../../../../../raw/repositories/lca-deepagents/python/m1/m1.7_messages_threads_checkpointers.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
from deepagents import create_deep_agent
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver

from models import model

agent = create_deep_agent(
    model=model,
    checkpointer=MemorySaver(),
)

thread_a: RunnableConfig = {"configurable": {"thread_id": "m1-7-thread-a"}}
thread_b: RunnableConfig = {"configurable": {"thread_id": "m1-7-thread-b"}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Remember that my favorite colour is blue."}]},
    config=thread_a,
)
print("Thread A, turn 1:")
print(result["messages"][-1].text)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is my favorite colour?"}]},
    config=thread_a,
)
print("\nThread A, turn 2:")
print(result["messages"][-1].text)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is my favorite colour?"}]},
    config=thread_b,
)
print("\nThread B, turn 1:")
print(result["messages"][-1].text)

```
