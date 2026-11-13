# MCP Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/ork9uptXB4T) · [Raw file](../../raw/videos/ork9uptXB4T.html)

Retrieved: 2026-11-13T16:57:39.225040+00:00

[00:00] **Speaker**: In this lab, we connect an agent to the LangChain documentation server. The server is remote, maintained by LangChain, and we reach it over HTTP using MCP.

[00:10] **Speaker**: Let's walk through the file

[00:12] **Speaker**: the key new import is MultiServerMCPClient from LangChain MCP Adapters. That's the class that handles the MCP connection. Everything else we've seen before

[00:23] **Speaker**: MultiServerMCPClient takes a dictionary. Each key is a name you give the server, and here we're calling ours  docstring chain. Inside, there are two fields  Transport  and URL

[00:34] **Speaker**: The transport  is HTTP because this is a remote server. The lesson covered three transport types, stdout for local subprocesses, HTTP for remote servers, and SSE for older servers.  For any public MCP endpoint, you'll use HTTP, and the URL is the actual MCP endpoint LangChain mentions for their docs

[00:55] **Speaker**: get_tools connects to every server in the configuration, discovers the tools it exposes, and returns them as a flat list of standard LangChain base tool objects. It's asynchronous,  so we await it

[01:07] **Speaker**: before doing anything with these tools, we print each one's name and the first 90 characters of its description. This is a useful habit. You'll see what you're actually getting before you commit to a tool list. Note that this print loop runs before the filter, so it shows everything the server exposes.

[01:23] **Speaker**: Now everything below this is the filter

[01:27] **Speaker**: Allowed is defined right here

[01:30] **Speaker**: above the list comprehension that uses it. Only tools whose names appear in allowed  pass through. Everything else is dropped before the agent is created. This is an allowlist pattern. The lesson also mentioned a denylist form, but you use an allowlist when you want a strict, stable subset.

[01:47] **Speaker**: You'll use a denylist when you want most tools and just need to exclude a few

[01:51] **Speaker**: the second print block runs after the filter  So we can see exactly what the agent is going to get.

[02:00] **Speaker**: Now, this is the same pattern as every other lab. The only difference is where tools come from, an MCP server here rather than local Python functions

[02:09] **Speaker**: the prompt explicitly asks the agent to use the MCP tool. Without that instruction, the model might answer from training data and skip the tool call entirely.

[02:18] **Speaker**: With this phrasing, it should call search docs by LangChain at least once, read the result, and synthesize an answer

[02:25] **Speaker**: this just pulls the final assistant message out of the message list. Same as always. Now let's run it

[02:40] **Speaker**: so this is before the filter ran, and we can see there are three tools here  Search docs by LangChain is a semantic search over the docs  query_docs_filesystem docs by LangChain is a read-only file system interface to the same content.  And submit_feedback is for reporting doc issues. All three are wrapped as base tool objects, and the agent cannot tell them apart from tools defined locally in Python

[03:03] **Speaker**: But here we can see that only one tool is left after filtering.  Search docs by LangChain.    LangChain, query docs file system docs by LangChain,  and submit feedback are gone

[03:14] **Speaker**: And this down here  is the final message. The agent called search docs by LangChain, read back the doc's content, and synthesized this answer. The two filtered out tools never appeared in the agent's context at all
