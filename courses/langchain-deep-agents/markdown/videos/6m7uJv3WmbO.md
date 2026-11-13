# Local Deployment

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/6m7uJv3WmbO) · [Raw file](../../raw/videos/6m7uJv3WmbO.html)

Retrieved: 2026-11-13T16:57:36.422938+00:00

[00:00] **Speaker**: So far, you've run every agent as a script. You invoke it at the command line, it runs, and it returns a result. Often, though, an agent wants to be deployed. Consider a chat agent. You have a chat user interface, and that UI calls the agent over an HTTP interface. The agent runs and returns a result. In the next turn, the user makes another request, and they expect the same agent to be there, remembering the conversation they've been having.

[00:27] **Speaker**: So the agent has to run behind a web API, not inside a Python script you invoke by hand. Let's look at what it takes to make that possible

[00:36] **Speaker**: All of this is available locally

[00:38] **Speaker**: With langgraph dev,  which is part of the LangGraph CLI package, It gives you a cloud deployment-like environment right on your laptop

[00:46] **Speaker**: So to reach your agent over HTTP, you need a few things running behind it, and LangGraph Dev wraps your agent in all of them. You'll need an HTTP API for endpoints, persistence, so state is stored between runs, a store for long-term memory, and a task queue that receives runs and schedules your deep agent to execute them

[01:06] **Speaker**: Studio here reaches all of this the same way any chat UI would,  over HTTP

[01:14] **Speaker**: so what is Studio?  It's basically a chat and debug interface. It gives you a chat panel to talk to your agent, plus a graphical debugger, and you'll see both in the lab later

[01:25] **Speaker**: Let's talk a bit more about this API. You've been issuing commands like invoke to run your agent locally. Your UI needs to do the same thing over the network, and since this is a live web service, it documents itself. Once it's running

[01:38] **Speaker**: Open localhost:2024/docs in your browser and you'll see the whole interactive API for your agent.

[01:45] **Speaker**: The assistant is the deployable unit, your graph plus its configuration

[01:50] **Speaker**: A thread holds a conversation's accumulated state across runs. This is what makes the agent remember between turns.

[01:58] **Speaker**: Each message becomes a thread run, one invocation of the agent against that thread. The equivalent of a blocking invoke call

[02:05] **Speaker**: is this. It runs the agent and waits for the result. There's also

[02:10] **Speaker**: So you get output back as it's generated instead of waiting for the whole response.

[02:15] **Speaker**: and there's the store, a long-term key-value memory available from any thread, which is what your agent's file system often reads and writes to.

[02:24] **Speaker**: And if you want to go further, the API opens up into a lot more. Stateless runs, scheduled cron runs, an A2A interface, exposing your agent as an MCP server in its own right, and health and metrics endpoints for keeping an eye on it in production

[02:39] **Speaker**: Deep agents have a lot of deployment options beyond your laptop too. A managed cloud service, a standalone server, or something fully self-hosted click here to find out more,  and check out LangSmith deployment in LangChain Academy if you want to go deeper.  But first, let's go to the lab and try this out
