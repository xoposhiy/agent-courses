# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m1/m1.6_agent_mcp.py

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m1/m1.6_agent_mcp.py) · [Raw file](../../../../../raw/repositories/lca-deepagents/python/m1/m1.6_agent_mcp.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
import asyncio

from deepagents import create_deep_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

from models import model


async def main():
    client = MultiServerMCPClient({
        "docs-langchain": {
            "transport": "streamable_http",
            "url": "https://docs.langchain.com/mcp",
        }
    })
    tools = await client.get_tools()

    print(f"\ndocs-langchain: {len(tools)} tool(s)")
    for t in tools:
        print(f"  {t.name}")
        print(f"  {t.description[:90]}")

    # filter to allowed tools only
    ALLOWED = {"search_docs_by_lang_chain"}
    tools = [t for t in tools if t.name in ALLOWED]

    print(f"\nfiltered to: {len(tools)} tool(s)")
    for t in tools:
        print(f"  {t.name}")

    agent = create_deep_agent(model=model, tools=tools)

    result = await agent.ainvoke({
        "messages": [{"role": "user", "content": "Use the LangChain docs MCP tool to explain what MCP is and how LangChain uses MCP tools."}]
    })
    print(result["messages"][-1].text)


asyncio.run(main())

```
