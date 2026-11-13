# MCP

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/SMCDEu7woKA) · [Raw file](../../raw/videos/SMCDEu7woKA.html)

Retrieved: 2026-11-13T16:57:37.948029+00:00

[00:02] **Speaker**: MCP stands for Model Context Protocol. It's an open protocol that standardizes how applications expose tools and context to LLMs. Instead of writing a custom integration for every service, any MCP-aware client connects to any MCP server using the same interface.

[00:18] **Speaker**: Now, before MCP, you'd write a separate integration for every service you wanted the agent to call. MCP replaces that with a single protocol. Any MCP-aware client connects to any MCP server, and the server handles all of the service specific details.  MCP servers can expose three primitives: tools, resources, and prompts. This course focuses on tools. get_tools retrieves them as BaseTool objects you can pass directly to your agent. Resources and prompts exist in the spec but need separate client calls

[00:48] **Speaker**: Now, this is the key integration point.  LangChain MCP adapters wraps each server tool as a standard base tool.  The agency's MCP tools identically to locally defined tools. Results come back as tool messages in the conversation history exactly the same as any other tool call

[01:06] **Speaker**: Now connecting to an MCP server is just one dictionary entry  and multi-server MCP client

[01:12] **Speaker**: Name the server  Set the transport type

[01:15] **Speaker**: and provide the URL

[01:17] **Speaker**: then call  await client.get_tools() to get the tools as BaseTool objects and pass them to create deep agent    as any other tool list

[01:27] **Speaker**: Now, some MCP servers require the user to sign in. At the agent level, the idea is simple

[01:33] **Speaker**: pass an auth provider in the server dictionary alongside transport and URL. The auth provider handles getting and attaching credentials. The optional OAuth lab at the top walks through a full GitHub example if you want to see that in detail

[01:48] **Speaker**: For now, the key point is that MCP tools arrive in the agent as normal tools, regardless of how the server is authenticated
