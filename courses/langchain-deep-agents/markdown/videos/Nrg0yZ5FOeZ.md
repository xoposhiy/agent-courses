# The Sales Assistant

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/Nrg0yZ5FOeZ) · [Raw file](../../raw/videos/Nrg0yZ5FOeZ.html)

Retrieved: 2026-11-13T16:57:37.600480+00:00

[00:01] **Speaker**: So here's what you'll be running You've got your agent, the Chinook database we've been using all along, the sales playbooks  And you'll have a mock mail MCP server. This will be running locally.  We'll also use  a chat user interface,   the thing to note is that there's not a lot of code to bring this up   You have your agent.py  which is mostly just wiring

[00:25] **Speaker**: langgraph.json tells langgraph dev  where to find the graph

[00:28] **Speaker**: There's a start script

[00:30] **Speaker**: That will kick off the mail server before langgraph dev.

[00:33] **Speaker**: And then the agents.md  and skills are where most of the work is getting done.  we've got some subagents

[00:40] **Speaker**: and some tools  the usual SQL tool,  something to convert Markdown  and some plotting tools.

[00:47] **Speaker**: We also have the MCP server, that's the mail server  and then the Chinook database
