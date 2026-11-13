# Assigned reference: managed-deep-agents

[Course index](../../README.md) · [Original source](https://docs.langchain.com/langsmith/managed-deep-agents) · [Raw file](../../raw/readings/docs-langchain-com-langsmith-managed-deep-agents-75c0af16.html)

Retrieved: 2026-11-13T17:00:51.980522+00:00

# Managed Deep Agents

Copy pageCopy page

Build your agent as a directory of files while LangSmith runs the harness and runtime.

Copy pageCopy page

Managed Deep Agents (MDA) is the simplest way to build and deploy production agents. You focus on what your agent does. MDA runs it. There are no servers to run and no infrastructure to wire together.

Managed Deep Agents is in **public [beta](https://docs.langchain.com/langsmith/release-stages)** on [LangSmith Cloud](https://docs.langchain.com/langsmith/cloud) and [Bring Your Own Cloud (BYOC)](https://docs.langchain.com/langsmith/byoc). Use Managed Deep Agents CLI and SDK v0.10 or later for BYOC.

You write the agent’s intelligence: its instructions, the tools it can call, the skills it follows, and you select the model that drives it. MDA provides everything underneath:

- **The Deep Agents harness**: The agent loop that plans, calls tools, manages a filesystem, and delegates to subagents. See [Deep Agents](docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md).
- **A managed runtime**: Every deployment runs on [LangSmith Agent Server](https://docs.langchain.com/langsmith/agent-server-overview). You get the Agent Server API, threads, runs, streaming, and the [MCP endpoint](https://docs.langchain.com/langsmith/python/managed-deep-agents-mcp-endpoint) without operating the server yourself.

![Your agent definition runs inside the Deep Agents harness, surrounded by managed Agent Server, channels, memory, sandboxes, schedules, and connections.](../../raw/assets/dfd906820f54cb47.png)
![Your agent definition runs inside the Deep Agents harness, surrounded by managed Agent Server, channels, memory, sandboxes, schedules, and connections.](../../raw/assets/6c529d470e36bc2f.png)

## Example agent

A managed deep agent consists of a project folder that contains the business logic for its behavior:

- Model & configuration
- Instructions
- Skills
- Tools
- Middleware
- MCP Connectors

agent.py

```
from managed_deepagents import define_deep_agent

from middleware.audit import log_tool_calls
from tools.search import internet_search

agent = define_deep_agent(
    name="research-assistant",
    model="openai:gpt-6.1-sol",
    tools=[internet_search],
    middleware=[log_tool_calls],
)
```

instructions.md

```
# Assistant

You are a helpful assistant.
```

skills/research/SKILL.md

```
---
name: research
description: Gather and synthesize context before answering complex questions.
---

# Research

Use this skill when a task needs more than a direct answer.

1. Identify what information is missing.
2. Search LangChain docs when the question is about LangChain, LangGraph, or LangSmith.
3. Summarize findings before responding to the user.
```

tools/search.py

```
from langchain.tools import tool


@tool(parse_docstring=True)
def internet_search(query: str) -> str:
    """Search the internet for relevant sources.

    Args:
        query: The search query.
    """
    return f"Results for: {query}"
```

middleware/audit.py

```
from collections.abc import Awaitable, Callable

from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage
from langchain.tools.tool_node import ToolCallRequest
from langgraph.types import Command


@wrap_tool_call
async def log_tool_calls(
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]],
) -> ToolMessage | Command:
    print(f"Calling tool: {request.tool_call['name']}")
    result = await handler(request)
    print(f"Finished tool: {request.tool_call['name']}")
    return result
```

tools/mcp.py

```
from managed_deepagents import define_mcp

mcp = define_mcp(
    servers={
        "langchainDocs": {
            "transport": "http",
            "url": "https://docs.langchain.com/mcp",
            "include_tools": ["search_docs_by_lang_chain"],
        },
    },
)
```

When you upload this folder with the `mda` CLI, it will automatically run on managed LangSmith infrastructure.
You provide the business logic, and Managed Deep Agents provides the agent harness and production infrastructure.
To get started, see the [Managed Deep Agents quickstart](https://docs.langchain.com/langsmith/python/managed-deep-agents-quickstart).

## Core capabilities

Each part of the agent maps to a file or directory. Add the ones your agent needs:


| Capability | Path | Description |
| --- | --- | --- |
| [Model and configuration](https://docs.langchain.com/langsmith/python/managed-deep-agents-agent-definition) | `agent.py` | The model and core options. Required. |
| [Instructions](https://docs.langchain.com/langsmith/python/managed-deep-agents-instructions) | `instructions.md` | The system prompt that defines how the agent behaves. |
| [Skills](https://docs.langchain.com/langsmith/python/managed-deep-agents-skills) | `skills/` | Task-specific playbooks the agent loads when they are relevant. |
| [Tools](https://docs.langchain.com/langsmith/python/managed-deep-agents-tools) | `tools/` | Functions the agent calls to run your application logic or reach external services. |
| [MCP connectors](https://docs.langchain.com/langsmith/python/managed-deep-agents-mcp-connectors) | `tools/mcp.py` | Remote MCP servers that provide tools to the agent. |
| [Middleware](https://docs.langchain.com/langsmith/python/managed-deep-agents-middleware) | `middleware/` | Custom logic that runs around model and tool calls. |
| [Sandbox](https://docs.langchain.com/langsmith/python/managed-deep-agents-sandboxes) | `sandbox/` | An isolated filesystem and shell for running agent-written code. |
| [Memory](https://docs.langchain.com/langsmith/python/managed-deep-agents-memory) | `memory.py` | Preferences and knowledge that persist across threads. |
| [Identity](docs-langchain-com-langsmith-python-managed-deep-agents-identity-000af9d5.md) | `identity.py` | Per-caller private threads, memory, and credentials for multi-user deployments. |
| [Channels](https://docs.langchain.com/langsmith/python/managed-deep-agents-channels) | `channels/` | Connections to messaging services, such as Slack, that start runs and receive responses. |
| [Schedules](https://docs.langchain.com/langsmith/python/managed-deep-agents-schedules) | `schedules/` | Managed cron schedules that run the agent on a recurring basis. |
| [Evals](https://docs.langchain.com/langsmith/python/managed-deep-agents-evals) | `evals/` | Harbor tasks that test the agent. |

For the full layout, see [Project structure](https://docs.langchain.com/langsmith/python/managed-deep-agents-project-structure). Instructions, skills, and optional durable memory are stored in [Context Hub](https://docs.langchain.com/langsmith/python/managed-deep-agents-context-hub).

## Relationship to Deep Agents

Managed Deep Agents runs the open source [Deep Agents](docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md) harness rather than a second framework. The agent loop, filesystem tools, subagents, and skills are the same, so there is no second API to learn and an agent you already built keeps working.
Managed Deep Agents adds the layer around the agent. The sandbox, durable memory, channels, and schedules above are declarations in a project file rather than services you build and operate. [Connections](https://docs.langchain.com/langsmith/python/managed-deep-agents-connections) run OAuth, so end users authorize their own accounts instead of you provisioning credentials for each one. LangSmith hosts the result on [Agent Server](https://docs.langchain.com/langsmith/agent-server-overview). In the code, the difference is narrower: who compiles the agent.

- [create\_deep\_agent](https://reference.langchain.com/python/deepagents/graph/create_deep_agent) returns a compiled agent. You run it, and you own the backend, store, checkpointer, and server around it.
- `define_deep_agent` returns a definition. The `mda` CLI hands it to the managed runtime, which supplies those pieces along with memory, skills, and the system prompt, then compiles the agent with [create\_deep\_agent](https://reference.langchain.com/python/deepagents/graph/create_deep_agent).

So `define_deep_agent` takes the same parameters minus the managed ones, plus a required static `name`. Every `define_*` function works this way: declare what the agent needs, and leave the lifecycle to the runtime.
Start with Managed Deep Agents to run production agents without having to manage infrastructure. Alternatively, for maximum flexibility while using the same Deep Agents harness, use the [Deep Agents SDK](docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md) and host agents yourself, or run a custom [Agent Server](https://docs.langchain.com/langsmith/deployment). For a side-by-side comparison and steps to convert an agent you already built, see [Move from Deep Agents](docs-langchain-com-langsmith-python-managed-deep-agents-migrate-65bf4db0.md).

## Next steps

## Quickstart

Create and deploy your first Managed Deep Agent with the `mda` CLI.

## Tutorial

Add a custom search tool, durable memory, and a daily schedule.

## Design agent template

Deploy LangChain’s open-source design agent to Slack.

## Paid media agent template

Deploy LangChain’s open-source paid media agent to Slack.

## Agent Server

Explore the runtime that hosts Managed Deep Agents deployments.

## MCP endpoint

Call a deployed agent as a tool from Claude Code or another MCP client.

---

[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo
