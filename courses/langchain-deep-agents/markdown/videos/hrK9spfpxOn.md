# Async Subagents

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/hrK9spfpxOn) · [Raw file](../../raw/videos/hrK9spfpxOn.html)

Retrieved: 2026-11-13T16:57:38.568057+00:00

[00:01] **jess**: So far, every subagent we've built, dynamic or otherwise, has worked the same way under the hood. The main agent calls it like a tool, and it just waits. If that subagent takes thirty seconds, the main agent is frozen for thirty seconds. It can't answer the user, can't check on anything else, can't do anything but sit there until the tool call returns.

[00:19] **Speaker**: Now, that's fine for quick lookups. It stops being fine once a subagent's job genuinely takes minutes, now, this lesson is about the other option  Asynchronous subagents, which don't block. The main agent kicks one off, gets back an ID immediately, and keeps going.

[00:34] **Speaker**: The official write-up on this pattern calls it fire and steer. The subagent keeps its own persistent state so you can check on it, redirect it, or cancel it while it's still running.

[00:45] **Speaker**: So the supervisor launches the researcher subagent  and gets a task ID back immediately  without waiting for it to finish.  Then it launches a second subagent, the coder, right away as well, without waiting on the researcher at all. Both subagents now run independently at the same time.  The supervisor can check on either one whenever it wants in any order.  Later, on its own schedule, the supervisor checks on the researcher's task and checks on the coder whenever it wants, same as the researcher. So there's no step where the

[01:12] **Speaker**: supervisor sits idle waiting on either subagent

[01:17] **Speaker**: an asynchronous subagent runs differently from a synchronous one in two ways.  With a synchronous subagent, which we saw in Module four,  it's invoked through the built-in task tool,  and it calls create_agent in the same process.  With an asynchronous subagent  It's invoked through a different set of tools that go over the LangGraph SDK.

[01:34] **Speaker**: And it runs on a remote agent protocol server, which is a managed LangGraph platform deployment or a self-hosted one. With a synchronous subagent,  it waits for it to finish and returns the result  For an asynchronous one,  the main agent doesn't wait for that run to finish. It gets a task ID back right away,  so it can check on the task whenever it wants

[01:52] **Speaker**: Now this remote server

[01:54] **Speaker**: It's the same kind of deployment you set up earlier in this module when you ran langgraph dev to serve an agent over HTTP

[02:01] **Speaker**: An async subagent target is just another deployed graph, reachable the same way.

[02:06] **Speaker**: You already have both pieces from the local deployment lesson's homework and configuring an asynchronous subagent looks like configuring a synchronous one, but instead of a system prompt and tools, you point at a deployed graph

[02:19] **Speaker**: So you import AsyncSubagent

[02:21] **Speaker**: Then point at a remote deployment with graph ID and URL.

[02:25] **Speaker**: and you pass that list straight to subagents  on create_deepagent.  there's no middleware to wire in yourself. It's added to the stack automatically once async subagents are configured   And the name is how the main agent refers to the subagent type when launching a task  The description is the main agent's only signal for when to reach for the subagent, so be as specific here as you would with any tool description.

[02:49] **Speaker**: For a LangGraph deployment, the graph ID has to match a graph actually registered in that deployment's langgraph.json.

[02:56] **Speaker**: And for the URL, it's optional. If you leave it out, the SDK talks to the subagent over an in-process ASGI transport, so it runs inside the same process as the main agent. The lab for this lesson sets this field explicitly  since its analyst subagent runs as a genuinely separate deployment on its own port.

[03:13] **Speaker**: And you'll see that concretely once we get to the lab so four tools are documented here. There is a fifth called list_asynchronous_tasks, which shows up in the lab once the middleware is wired in, but here are the main ones

[03:25] **Speaker**: start_asynchronous_task launches a background run on the named async subagent, and it returns a task ID immediately.  It's the only one that creates something new. Everything else operates on a task ID you already have.  check_async_task looks up the current status of a task by task ID. If it's finished, the result comes back too  For update, it sends new instructions to a still-running task on the same thread.

[03:46] **Speaker**: And cancel_async_task stops running the task

[03:50] **Speaker**: Now, synchronous and asynchronous subagents aren't an either/or choice for the whole agent. Either can show up on its own or both together. Configure at least one of each kind, and the main agent ends up with all five tools: task and the other four above. It can reach for a quick in-process subagent one moment and hand off a long remote job the next in the same conversation

[04:11] **Speaker**: So the user asks the supervisor to do something, say research topic X,  and the supervisor calls start_async_task, naming the subagent type and describing the job and behind that single call, the server creates a new thread, then starts a run on it targeting the subagent's graph ID, which is the same key from langgraph.json's graphs mapping.  Then you get the task ID back immediately

[04:33] **Speaker**: And it's the thread ID being reused,  not a separate identifier.  The supervisor reports it without waiting for the subagent to finish.  And it's tracked in state.  The supervisor records this as an async task in its own state, under the

[04:47] **Speaker**: async_tasks key: task_id, thread_id, run_id, and a status of "running."    .  So time passes, and the user keeps talking to the supervisor, and the subagent keeps working unattended on the remote server. So we ask again later And the user checks in. Only now does the supervisor check the task, and it's only happening because the user asked.

[05:06] **Speaker**: Nothing here runs on a timer  this check comes back too early. The run hasn't finished, so check_async_task just reports the status with no result yet.   Then the user checks back in again later,  and the supervisor checks the same task ID a second time. Nothing stops it from checking as many times as it needs to Check_async_task looks up the tracked task by task ID, then asks the server for that run's current status. Only once it's finished does it also fetch the thread's latest values to read out the result. Then we get the result back.

[05:36] **Speaker**: The run's finished, so the supervisor reports it

[05:40] **Speaker**: So this is the reason async subagents work across a long conversation. Every tracked task, task ID, which subagent type launched it, run ID, status, and a few timestamps lives in that dedicated async task slot in the AgentState, not inside the message history

[05:56] **Speaker**: This is what lets it survive context compaction. Concretely, deep agents periodically summarize or prune older messages to keep the context window under control. If a task ID only existed as text inside a tool message, compaction pass could summarize that message away, and the main agent would lose its own reference to a task it's still waiting on.

[06:14] **Speaker**: Keeping tasks in a separate state channel means they're untouched by whatever compaction does to the messages list.

[06:20] **Speaker**: The main agent can always recover its task list, with list_async_tasks,  even after several rounds of summarization  these are the behaviors the main agent is specifically prompted to follow per its own system prompt. It's still a language model deciding what to do turn to turn, so treat this as the intended pattern the model is instructed to follow, not something the surrounding code enforces on its own.

[06:41] **Speaker**: So after starting AsyncTask, report the task ID and return control. Don't immediately call checkAsyncTask on it  and to check only on request by default.  The middleware's own instructions tell the model to call  check_async_task  when the user asks for a status update, not on a timer or in a loop.

[06:57] **Speaker**: Auto-notifying the supervisor when a subagent finishes is possible but needs extra middleware on the subagent side that isn't part of the default setup.  And to never trust the status already in the transcript. A task that shows "running" earlier in the conversation may be done by now. Always call a tool to get the current status rather than repeating a stale one  Now update_async_task isn't a message to a listener.

[07:18] **Speaker**: It interrupts the current run and starts a fresh one on the same thread, so the subagent sees the full history plus the new instructions. The task ID doesn't change.

[07:27] **Speaker**: Now, this comparison table  just helps you see the difference between synchronous and asynchronous subagents side by side If the main agent needs a subagent's answer before it can take its next step,  synchronous is simpler and there's less to manage. You'll want to use asynchronous when the work takes long enough that blocking would be wasteful or when you want several things happening at once without serializing them

[07:48] **Speaker**: Now just to recap, module four's dynamic subagents  are about the main agent deciding how many subagent instances to spin up and what to hand each one. This lesson is about whether a given delegation blocks or not.

[08:00] **Speaker**: They're independent choices.  A dynamically sized batch of subagents could each run asynchronously too,
