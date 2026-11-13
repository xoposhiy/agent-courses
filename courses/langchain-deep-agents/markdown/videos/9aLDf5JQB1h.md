# MCP Lab (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/9aLDf5JQB1h) · [Raw file](../../raw/videos/9aLDf5JQB1h.html)

Retrieved: 2026-11-13T16:57:36.504813+00:00

[00:01] **jess**: So here we have our run. Let's go through what happened

[00:07] **Speaker**: The input is exactly what we passed in, and here we asked it to use the LangChain docs MCP tool to explain what MCP is and how LangChain uses MCP tools

[00:18] **Speaker**: now in output, the model responded with, " I'll search the LangChain docs for information about MCP." It immediately called search_docs by LangChain and didn't try to answer from memory. Went straight to the tool, which is exactly what our prompt asked for. Let's take a look at that node

[00:34] **Speaker**: So here's that first tool call, this is the query that the model generated to search the docs, MCP Model Context Protocol

[00:43] **Speaker**: The tool returned relevant documentation content as a string, which gets wrapped in a ToolMessage and added to the conversation history. So let's look at the next tool node, called in parallel

[00:53] **Speaker**: The model issued a second query This is a different query, MCP tools LangChain. Now down here is our final model call that synthesized everything into the answer we saw in the terminal  The core pattern is visible. One model call to decide what to search for, two tool calls to the MCP server, and then a final model call to synthesize.

[01:14] **Speaker**: This was the answer we saw in the terminal From the agent's perspective, SearchDocs by LangChain was just another tool. It had no idea it was calling out to a remote server over HTTP
