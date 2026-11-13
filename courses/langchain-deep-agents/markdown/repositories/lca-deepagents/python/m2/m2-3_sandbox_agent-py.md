# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m2/m2.3_sandbox_agent.py

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m2/m2.3_sandbox_agent.py) · [Raw file](../../../../../raw/repositories/lca-deepagents/python/m2/m2.3_sandbox_agent.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
from uuid import uuid4

from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

from models import model

client = SandboxClient()
ls_sandbox = client.create_sandbox(name=f"lca-deepagents-lab-{uuid4().hex[:8]}")
print(f"Sandbox: {ls_sandbox.name}  (id: {ls_sandbox.id})")
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model=model,
    backend=backend,
    system_prompt=(
        "You are a coding assistant. When asked to run code, write the script "
        "to a file first, then execute it. Show the output in your final answer."
    ),
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Write a Python script that prints the first 15 Fibonacci numbers, "
                        "save it to fib.py, and run it."
                    ),
                }
            ]
        }
    )
    print(result["messages"][-1].text)
finally:
    client.delete_sandbox(ls_sandbox.name)

```
