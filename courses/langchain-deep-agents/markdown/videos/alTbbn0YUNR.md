# Sub-Agents

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/alTbbn0YUNR) · [Raw file](../../raw/videos/alTbbn0YUNR.html)

Retrieved: 2026-11-13T16:57:38.172564+00:00

[00:00] **Speaker**: Long-running agents need coordination.  A big task can span many steps, tool calls, files, and intermediate results. Without an explicit way to track the plan and isolate specialized work, the main agent can drift or overload its context.

[00:14] **Speaker**: Deep Agents gives the main agent two coordination tools to address this:  planning and delegation.  Planning keeps the main agent organized, and it's opt-in. You turn it on with to-do list middleware

[00:26] **Speaker**: Now delegation moves specialized or context-heavy work out of the main agent's context entirely.

[00:32] **Speaker**: A capable model can draft a solid plan for a multi-step job.  The hard part is follow through. As the conversation grows and the agent juggles tool calls and intermediate results, it tends to drift, losing track of what's done and what isn't.

[00:47] **Speaker**: Deep Agents addresses this with an opt-in write-to-dos tool

[00:50] **Speaker**: Just add the todo list middleware to the agent's middleware list, and the model gets a tool for writing out its plan as a structured list

[00:57] **Speaker**: It updates each item's status as it works:  pending,  in progress

[01:01] **Speaker**: or complete it

[01:03] **Speaker**: That list is saved in the agent state, and it persists across turns when you use the same thread with a checkpointer, which is the same thread pattern introduced earlier in the course on a long task, the agent always has an explicit up-to-date plan to check against instead of trying to hold the whole thing in its head.

[01:19] **Speaker**: Think of it as writing the steps on a whiteboard and ticking them off as it goes

[01:23] **Speaker**: So planning is not delegation. It is the main agent's task list, a way for the main agent to keep itself organized before, during, and after tool calls.

[01:32] **Speaker**: Now let's look at how people handle a project that's too big for one person. You bring in a team. So the supervisor breaks out the work into subtasks and hands each one out. There's a researcher, a writer, a data analyst, and a designer. Each brings their own expertise, and they work in parallel, finishing in a fraction of the time a single person would take And each person only needs to focus on their own piece.

[01:55] **Speaker**: The writer doesn't need to hold the entire project plan in their head.  They just do their assignment and report back

[02:01] **Speaker**: Subagents give an agent exactly the same capability.  A subagent is a full agent the main agent can call to do a focused task and report back.  The main agent splits the work and aggregates the results.  Say the job is writing a newsletter summarizing this week's news on a topic.

[02:17] **Speaker**: The main agent hands each subtopic to a different subagent, And each one searches and summarizes what it finds, and the main agent stitches the results into the final newsletter. Each subagent is a full agent in its own right, with its own system prompt, its own skills, its own tools, and it can even run on a different model.

[02:35] **Speaker**: And subagents run in parallel.  In deep agents, a subagent is invoked like a tool, so the main agent can fire off as many as it needs at the same time, and each subagent focuses only on its own task and its own isolated context, which is what makes subagents a context engineering tool

[02:54] **Speaker**: The main agent doesn't do anything special to delegate. It calls a built-in task tool with an assignment the same way it would call any other tool. It picks which subagent to use from each one's description. From the main agent's perspective, delegation is just a tool call
