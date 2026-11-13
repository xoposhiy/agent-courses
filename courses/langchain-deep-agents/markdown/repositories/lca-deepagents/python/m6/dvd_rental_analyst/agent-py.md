# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m6/dvd_rental_analyst/agent.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m6/dvd_rental_analyst/agent.py) · [Raw file](../../../../../../raw/repositories/lca-deepagents/python/m6/dvd_rental_analyst/agent.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
from langchain.tools import tool
from managed_deepagents import define_deep_agent


@tool
def email_report(to: str, subject: str, body: str) -> str:
    """Email a report to a stakeholder. This simulates a send, no network call is made."""
    return f"Emailed {to}: {subject}"


agent = define_deep_agent(
    name="dvd-rental-analyst",
    model="anthropic:claude-sonnet-5-5",
    tools=[email_report],
)

```
