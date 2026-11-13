# LangChain Academy: Introduction to Deep Agents

A hands-on course on configuring and deploying Deep Agents. It covers models, prompts, tools, MCP, thread state, approval, filesystems, sandboxes, interpreters, context, skills, memory, and subagents through a sales-assistant project.

[Archived source](../../courses/langchain-deep-agents/README.md) · [Shared dictionary](../DICTIONARY.md) · [Summary](../README.md)

## Scope and limits

- The analysis uses 29 public lesson documents from the archived course repository.
- Python and TypeScript versions, repeated diagrams, quizzes, and matching code files count once per course.
- Optional advanced sandbox and asynchronous-agent lessons are available and included. Product-specific instructions describe the archived version.

## Concepts and evidence

T = explained or implemented in available teaching content; A = assigned reading; P = schedule only. The evidence is a reviewed selection, not a complete list of occurrences.

| Concept | Type | Coverage | Evidence |
| --- | --- | --- | --- |
| Agent architecture | topic | taught | [m1.1-overview, line 34](../../courses/langchain-deep-agents/markdown/lessons/m1.1-overview.md) |
| Agent as a tool | pattern | taught | [m4.1-delegation, line 35](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md) |
| Agent deployment and service APIs | topic | taught | [m5.2-local-deployment, line 50](../../courses/langchain-deep-agents/markdown/lessons/m5.2-local-deployment.md) |
| Agent evaluation and benchmarks | topic | taught | [m4.3-dynamic-subagents, line 910](../../courses/langchain-deep-agents/markdown/lessons/m4.3-dynamic-subagents.md) |
| Agent filesystem and storage backends | topic | taught | [m2.1-the-deep-agent-environment, line 58](../../courses/langchain-deep-agents/markdown/lessons/m2.1-the-deep-agent-environment.md) |
| Agent frameworks and orchestration | topic | taught | [m1.2-running-a-deep-agent, line 25](../../courses/langchain-deep-agents/markdown/lessons/m1.2-running-a-deep-agent.md) |
| Agent harness design | topic | taught | [m1.1-overview, line 18](../../courses/langchain-deep-agents/markdown/lessons/m1.1-overview.md) |
| Agent memory | topic | taught | [m3.3-memory, line 39](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md) |
| Agent middleware | concept | taught | [m1.5-tools, line 61](../../courses/langchain-deep-agents/markdown/lessons/m1.5-tools.md) |
| Agent safety and guardrails | topic | taught | [m1.4-system-prompt, line 57](../../courses/langchain-deep-agents/markdown/lessons/m1.4-system-prompt.md) |
| Asynchronous agent coordination | pattern | taught | [m5.4-async-subagents, line 44](../../courses/langchain-deep-agents/markdown/lessons/m5.4-async-subagents.md) |
| Checkpointing and resuming | pattern | taught | [m1.7-messages-threads-checkpointers, line 104](../../courses/langchain-deep-agents/markdown/lessons/m1.7-messages-threads-checkpointers.md) |
| CodeAct | pattern | taught | [m2.4-interpreter, line 50](../../courses/langchain-deep-agents/markdown/lessons/m2.4-interpreter.md) |
| Coding and terminal agents | application | taught | [m2.3-sandboxes-and-localshell, line 76](../../courses/langchain-deep-agents/markdown/lessons/m2.3-sandboxes-and-localshell.md) |
| Context engineering | topic | taught | [m3.1-summarization-context-offloading, line 42](../../courses/langchain-deep-agents/markdown/lessons/m3.1-summarization-context-offloading.md) |
| Context isolation | pattern | taught | [m4.1-delegation, line 146](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md) |
| Context offloading | pattern | taught | [m3.1-summarization-context-offloading, line 42](../../courses/langchain-deep-agents/markdown/lessons/m3.1-summarization-context-offloading.md) |
| Context summarization and compaction | pattern | taught | [m3.1-summarization-context-offloading, line 66](../../courses/langchain-deep-agents/markdown/lessons/m3.1-summarization-context-offloading.md) |
| Conversation and execution state | concept | taught | [m1.7-messages-threads-checkpointers, line 77](../../courses/langchain-deep-agents/markdown/lessons/m1.7-messages-threads-checkpointers.md) |
| Deep research agents | application | taught | [m4.2-building-a-subagent-team, line 43](../../courses/langchain-deep-agents/markdown/lessons/m4.2-building-a-subagent-team.md) |
| Durable execution and recovery | pattern | taught | [m1.7-messages-threads-checkpointers, line 119](../../courses/langchain-deep-agents/markdown/lessons/m1.7-messages-threads-checkpointers.md) |
| Dynamic subagent creation and batch delegation | pattern | taught | [m4.3-dynamic-subagents, line 50](../../courses/langchain-deep-agents/markdown/lessons/m4.3-dynamic-subagents.md) |
| Embedded code interpreter | method | taught | [m2.4-interpreter, line 46](../../courses/langchain-deep-agents/markdown/lessons/m2.4-interpreter.md) |
| Human oversight and approval | pattern | taught | [m1.8-hitl, line 40](../../courses/langchain-deep-agents/markdown/lessons/m1.8-hitl.md) |
| Human-agent collaboration | topic | taught | [m1.8-hitl, line 604](../../courses/langchain-deep-agents/markdown/lessons/m1.8-hitl.md) |
| LangGraph | tool | taught | [m5.2-local-deployment, line 52](../../courses/langchain-deep-agents/markdown/lessons/m5.2-local-deployment.md) |
| Long-context modeling | topic | taught | [m4.3-dynamic-subagents, line 799](../../courses/langchain-deep-agents/markdown/lessons/m4.3-dynamic-subagents.md) |
| Long-horizon agent tasks | topic | taught | [m1.1-overview, line 18](../../courses/langchain-deep-agents/markdown/lessons/m1.1-overview.md) |
| Managed agent hosting | tool | taught | [m6.1-what-is-managed-deep-agents, line 12](../../courses/langchain-deep-agents/markdown/lessons/m6.1-what-is-managed-deep-agents.md) |
| Memory maintenance and consolidation | pattern | taught | [m3.3-memory, line 123](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md) |
| Memory scoping and user isolation | pattern | taught | [m3.3-memory, line 194](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md) |
| Model Context Protocol | protocol | taught | [m1.6-mcp, line 49](../../courses/langchain-deep-agents/markdown/lessons/m1.6-mcp.md) |
| Model selection and provider integration | topic | taught | [m1.3-models, line 44](../../courses/langchain-deep-agents/markdown/lessons/m1.3-models.md) |
| Multi-agent systems | topic | taught | [m4.1-delegation, line 42](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md) |
| Natural-language database and graph queries | application | taught | [m2.4-interpreter, line 152](../../courses/langchain-deep-agents/markdown/lessons/m2.4-interpreter.md) |
| Orchestrator and workers | pattern | taught | [m4.1-delegation, line 81](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md) |
| Parallel execution | pattern | taught | [m4.2-building-a-subagent-team, line 43](../../courses/langchain-deep-agents/markdown/lessons/m4.2-building-a-subagent-team.md) |
| Persona and response style control | application | taught | [m1.4-system-prompt, line 55](../../courses/langchain-deep-agents/markdown/lessons/m1.4-system-prompt.md) |
| Personalization and user modeling | topic | taught | [m3.3-memory, line 44](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md) |
| Planning and task decomposition | topic | taught | [m4.1-delegation, line 41](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md) |
| Privacy and user data protection | topic | taught | [m2.3-sandboxes-and-localshell, line 115](../../courses/langchain-deep-agents/markdown/lessons/m2.3-sandboxes-and-localshell.md) |
| Procedural memory and skills | concept | taught | [m3.2-skills, line 35](../../courses/langchain-deep-agents/markdown/lessons/m3.2-skills.md) |
| Programmatic tool composition | pattern | taught | [m2.4-interpreter, line 372](../../courses/langchain-deep-agents/markdown/lessons/m2.4-interpreter.md) |
| Progressive disclosure | pattern | taught | [m3.2-skills, line 83](../../courses/langchain-deep-agents/markdown/lessons/m3.2-skills.md) |
| Prompt design | topic | taught | [m1.4-system-prompt, line 48](../../courses/langchain-deep-agents/markdown/lessons/m1.4-system-prompt.md) |
| Prompt injection | concept | taught | [m5.5-sandbox-async-agent, line 62](../../courses/langchain-deep-agents/markdown/lessons/m5.5-sandbox-async-agent.md) |
| Prompt prefix and KV caching | method | taught | [m1.4-system-prompt, line 74](../../courses/langchain-deep-agents/markdown/lessons/m1.4-system-prompt.md) |
| Recursive and self-modifying agents | pattern | taught | [m4.3-dynamic-subagents, line 904](../../courses/langchain-deep-agents/markdown/lessons/m4.3-dynamic-subagents.md) |
| Sales and business assistants | application | taught | [m5.1-putting-it-all-together, line 21](../../courses/langchain-deep-agents/markdown/lessons/m5.1-putting-it-all-together.md) |
| Sandboxed execution | method | taught | [m2.3-sandboxes-and-localshell, line 100](../../courses/langchain-deep-agents/markdown/lessons/m2.3-sandboxes-and-localshell.md) |
| Shared memory and task coordination | pattern | taught | [m4.1-delegation, line 67](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md) |
| State replay and branching | pattern | taught | [m1.7-messages-threads-checkpointers, line 140](../../courses/langchain-deep-agents/markdown/lessons/m1.7-messages-threads-checkpointers.md) |
| Structured output and constrained decoding | method | taught | [m1.5-tools, line 86](../../courses/langchain-deep-agents/markdown/lessons/m1.5-tools.md) |
| Threat modeling and least privilege | method | taught | [m2.2-filesystem-backends, line 248](../../courses/langchain-deep-agents/markdown/lessons/m2.2-filesystem-backends.md) |
| Tool authentication and credential handling | topic | taught | [m1.6-mcp, line 26](../../courses/langchain-deep-agents/markdown/lessons/m1.6-mcp.md) |
| Tool use and function calling | topic | taught | [m1.5-tools, line 44](../../courses/langchain-deep-agents/markdown/lessons/m1.5-tools.md) |
| Tracing and observability | topic | taught | [m5.2-local-deployment, line 81](../../courses/langchain-deep-agents/markdown/lessons/m5.2-local-deployment.md) |
| Working memory | concept | taught | [m3.3-memory, line 43](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md) |

## Dictionary update

Concepts first registered in this source: 12. Final source inventory after cross-course review: 58 concepts. Later evidence updates are listed in the reconciliation audit.
