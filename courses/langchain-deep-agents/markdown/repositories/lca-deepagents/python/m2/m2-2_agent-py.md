# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m2/m2.2_agent.py

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m2/m2.2_agent.py) · [Raw file](../../../../../raw/repositories/lca-deepagents/python/m2/m2.2_agent.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
# python/m2/m2.2_agent.py
from pathlib import Path

from deepagents import FilesystemPermission, create_deep_agent
from deepagents.backends import CompositeBackend, FilesystemBackend, StateBackend

from models import model

reference_dir = Path(__file__).parent / "reference"
reference_dir.mkdir(exist_ok=True)
(reference_dir / "chinook-sales.md").write_text("""\
# Chinook Sales Reference

You are a sales representative for Chinook Digital Music Store.

Responsibilities:
- Look up customer accounts and purchase history
- Recommend music based on genre and artist preferences
- Answer questions about artists, albums, tracks, and invoices
""", encoding="utf-8")

agent = create_deep_agent(
    model=model,
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/reference/": FilesystemBackend(
                root_dir=str(reference_dir),
                virtual_mode=True,
            ),
        },
    ),
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/reference/**"],
            mode="deny",
        ),
    ],
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Read /reference/chinook-sales.md, then add this note to it: "
                    "'Current promotion: 20% off all Jazz albums through end of month.'"
                ),
            }
        ]
    },
    config={"configurable": {"thread_id": "lab-m2.2"}},
)

print(result["messages"][-1].text)

```
