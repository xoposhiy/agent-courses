# Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/kVx79ZeFLVY) · [Raw file](../../raw/videos/kVx79ZeFLVY.html)

Retrieved: 2026-11-13T16:57:38.837627+00:00

[00:01] **Speaker**: This lesson is about deployment, so we've kept the agent as simple as possible. And here it is  One call to create_deep_agent  using the shared model from the courses_models.py

[00:11] **Speaker**: This is assigned  to a module-level variable named graph because that's the name the server's going to look for. Now here we have langgraph.json. This is the file that turns a Python file into a deployment, and it says a few things

[00:25] **Speaker**: where the dependencies live.  which graph to serve

[00:28] **Speaker**: and which env file to load for things like your model API key. That's the whole deployment. One graph declared in one configuration file     Before we run it, make sure your model API key from setup is available in the environment   If you see this error, it's a very easy fix

[00:50] **Speaker**: Just give it permission

[00:54] **Speaker**: And there you go

[00:56] **Speaker**: This is the graph that's running your Deep Agent. It has the model the tools and some middleware You can have this graph interface or there's also a chat interface  You can converse with the agent

[01:14] **Speaker**: You can ask it questions

[01:19] **Speaker**: the agent remembers your conversation over time because it's storing your conversation in that persistent store  Now in this graph view,  we can see our chat.

[01:29] **Speaker**: We can also look at the trace

[01:33] **Speaker**: This should look familiar to you

[01:35] **Speaker**: It's what we look at in LangSmith. So that's a quick introduction to Studio and langgraph dev
