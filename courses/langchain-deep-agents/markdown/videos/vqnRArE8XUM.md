# Lab + Studio Walkthrough

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/vqnRArE8XUM) · [Raw file](../../raw/videos/vqnRArE8XUM.html)

Retrieved: 2026-11-13T16:57:39.675696+00:00

[00:00] **Speaker**: On to the second half of this lesson, running the newsletter subagent asynchronously. We'll go file by file in the order that they actually connect to each other.  Let's start with langgraph.json

[00:10] **Speaker**: Here's the main agent's graph, same as what you've seen before

[00:14] **Speaker**: And here is a completely separate graph, newsletter agent, pointing at a different file entirely. Registering it here is what makes it launchable as an async subagent, and it's deployed alongside the main agent, not nested inside it

[00:29] **Speaker**: Now newsletter_agent_graph.py

[00:32] **Speaker**: This is the same pattern as the main agent, and it only turns on internet search if a Tavily key is set

[00:39] **Speaker**: This is the system prompt for the subagent itself.

[00:42] **Speaker**: Notice that it's told directly that it's running in the background and the main agent already informed the user. So its job is just to do the work and hand back a result,  not to manage any of that communication itself.

[00:54] **Speaker**: It's instructed to fan out to a genre researcher subagent once per genre,  all in the same turn, so those calls run in parallel.   And it's told to reply with nothing but the HTML because whatever it replies with gets written straight to a file    And here's that genre researcher subagent. A normal subagent dictionary in the same shape you've seen before, with name, description, prompt, tools, and model  This backend namespaces storage  by thread ID,  so each newsletter run's research files don't collide with another run's.   and that all comes together in one create_deep_agent call.  Nothing exotic here, just a standard DeepAgent. This is the graph that langgraph.json pointed at   On to agent.py

[01:38] **Speaker**: Back in the main agent, this import is the hook into the async wiring, and we'll open that file next  this is the same search flag as before, and it's reused here too

[01:50] **Speaker**: inside make_graph, if search is enabled, this line appends the async middleware to the agent's middleware list. That's the only change to the main agent needed to make it async subagent aware. Everything else about the async wiring lives one file over.   onto async_research.py.

[02:07] **Speaker**: This is the actual middleware class

[02:11] **Speaker**: And here's where it's constructed

[02:13] **Speaker**: The name is what the name agent calls when it launches the subagent type

[02:17] **Speaker**: And the description is how the main agent decides when to delegate to it and what to expect back.

[02:22] **Speaker**: graph_id ties it back to the entry we saw in langgraph.json, and that's the actual graph that gets launched

[02:29] **Speaker**: Constructing async subagent middleware this way is what gives the main agent its five async tools: start_async_task, check_async_task, update_async_task, cancel_async_task, and list_async_tasks

[02:44] **Speaker**: Now in the SkillMD  Step two is where the judgment call lives, not in the code so this tells it to launch once with the genre list in the description.

[02:56] **Speaker**: Tell the user it's running, then stop. They're explicitly told not to poll  Step three is the flip side. It only runs when the user actually asks first, it looks up the task ID fresh rather than trusting anything from earlier in the conversation.

[03:11] **Speaker**: Then it checks status

[03:14] **Speaker**: If it's done, the result is the finished HTML ready to save. And that's the whole loop start to finish. Registered as its own graph, launched once by the main agent, worked on in the background, and only checked back in on when the user actually asks

[03:29] **Speaker**: Let's run it and see it in action     before we get into the chat UI,  when you run start.sh,  LangSmith Studio will pop open in a browser tab  automatically.  That's just a side effect of LangGraph Dev starting up.  You can ignore it and close this tab if you want   Now make sure you're on localhost:3000, because that's the self-hosted AgentChat UI that this lesson ships with its own Sandbox Files panel and async task badge

[04:02] **Speaker**: It's not calling a dedicated chart tool. It's writing a Python script with write_file and running it with execute inside the sandbox, and that's the sandbox security change we walked through earlier

[04:21] **Speaker**: Great. So now that it's finished, they're saved under outputs    in the sandbox,  not our local machine

[04:31] **Speaker**: and this is the non-agentic extraction path from the diagram that we saw earlier. It goes through the UI's download, not through the agent

[04:40] **Speaker**: Now to do the second task, the asynchronous one      it just launched start_async task and handed control back. It's not sitting there waiting on the newsletter

[04:53] **Speaker**: and this badge appears showing the newsletter subagent running in the background

[05:02] **Speaker**: This is check async task firing under the hood. If it's done, the agent retrieves the finished HTML and tells you where it's saved under outputs. The same download flow as the chart
