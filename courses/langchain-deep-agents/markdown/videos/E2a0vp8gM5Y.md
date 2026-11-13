# Tools

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/E2a0vp8gM5Y) · [Raw file](../../raw/videos/E2a0vp8gM5Y.html)

Retrieved: 2026-11-13T16:57:36.702563+00:00

[00:01] **Speaker**: tools are functions you give an agent so it can act, whether that's looking things up, running queries, or calling APIs. You define what they do, and the agent decides when to call them and what arguments to pass.

[00:13] **Speaker**: Every deep agent ships with a built-in set of tools loaded automatically by the SDK.  You already saw these appear in the LangSmith trace in the previous lesson as file system tools on the model call. Now, these tools are always present

[00:27] **Speaker**: the tools parameter on create_deep_agent is additive. Whatever you pass

[00:31] **Speaker**: And here is merged with the built-in suite, not substituted for it

[00:36] **Speaker**: there's also a write_todos tool for managing a running to-do list, but that's opt-in, so you need to add to-do list middleware to turn it on, and you'll see that in module four

[00:46] **Speaker**: Now, this diagram here shows exactly what happens under the hood when an agent uses a tool

[00:51] **Speaker**: So the model asks for a tool call and tools, the built-in runner inside the agent executes the Python function and returns the result.  First,  the SDK provides tool schemas.  Before every LLM call, the SDK binds all available tools to the model call. The model receives each tool name, description, and argument schema, so it knows what tools exist and how to call them. Then the LLM outputs tool_calls. It decides it needs data and responds with an AI message containing a tool_calls list which is the tool name and the arguments to pass.

[01:22] **Speaker**: The LLM does not run anything.  It produces a structured request. Something else executes it,  and that triggers Tools. The agent runtime detects tool_calls in the AI message and routes them to Tools.

[01:33] **Speaker**: The AI message itself is not passed to Tools. The tool_calls within it are what trigger the routing  Tools executes the call. It reads tool_calls, finds read_sql by name, and calls it with the arguments the LLM supplied. If multiple independent tools were requested, Tools can run them in parallel  Then read_sql runs and returns a string.

[01:53] **Speaker**: Tools wraps it in a ToolMessage, linking the result back to the original request via a tool_call_id.  That ToolMessage feeds back to the LLM. It's appended to the conversation, and the LLM is called again with a full updated history, its original question, its tool call, and the result.

[02:10] **Speaker**: And finally, the LLM either answers or loops. With the result in context, it either responds with a final answer or issues another tool_call if it needs more information, and that's the loop. The LLM never runs tools directly. It only requests them, and Tools handles execution and feeds results back

[02:30] **Speaker**: Now for parallel tool calls

[02:32] **Speaker**: tool_calls is a list because the model can request more than one tool in the same turn. When those calls have no dependency on each other, tools runs them simultaneously.   so if an agent needs both search_web and search_docs, both fire in the same turn

[02:46] **Speaker**: and the LLM sees both results together in the next call.
