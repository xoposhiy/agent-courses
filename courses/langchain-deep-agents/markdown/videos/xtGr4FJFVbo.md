# Lab 2 [PTC]

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/xtGr4FJFVbo) · [Raw file](../../raw/videos/xtGr4FJFVbo.html)

Retrieved: 2026-11-13T16:57:39.816699+00:00

[00:00] **jess**: This lab runs the same task through two agents back to back, one with the code interpreter turned on and one without. So it's the same tool, same system prompt, and same database. The only thing that changes is whether the agent can chain its queries together in JavaScript, or it has to make them one at a time and wait for each answer before asking the next question

[00:22] **Speaker**: So this is the question we're going to ask both agents. Who's the top selling artist? What's their best album? What's the top track on that album? And then how many customers bought that track? Each step needs the answer from the step before it. This is exactly the kind of problem where chaining queries in code beats going back and forth with the model one query at a time.

[00:41] **Speaker**: This is the shared system prompt: the database schema, and the revenue formula.  Both agents get this exact same text.

[00:49] **Speaker**: This is our only tool. It takes a SQL string, runs it against the Chinook database, and hands back the rows as JSON. Nothing about this function knows it's going to be used inside the interpreter. It's a normal tool, and that matters because it means any existing tool can be made available to the interpreter without rewriting it

[01:07] **Speaker**: So this is the first agent,

[01:09] **Speaker**: with the interpreter turned on

[01:11] **Speaker**: And this is the line that does it. CodeInterpreterMiddleware with ptc set to a list containing Query Chinook. Adding the middleware gives the agent the eval tool

[01:20] **Speaker**: Listing this

[01:22] **Speaker**: in the ptc list is what makes it callable from inside the JavaScript that runs in eval, not just as a regular tool call

[01:29] **Speaker**: This is what programmatic tool calling means. The model writes a bit of JavaScript, and that JavaScript can read out and call our Python tool as many times as it needs in a loop, in a sequence, however it wants

[01:41] **Speaker**: We take the shared system text and tack on a few extra sentences. We're telling the model two things, that inside eval, it can call query Chinook  And when queries depend on each other like ours do, it should do all of them

[01:54] **Speaker**: inside one eval call instead of one at a time.

[01:58] **Speaker**: So the reason that matters is because anything that happens inside that JavaScript, including every intermediate row it pulls back, stays inside the interpreter.

[02:07] **Speaker**: None of it gets turned into a message and sent back to the model. Only the final result the JavaScript returns shows up in the conversation

[02:15] **Speaker**: We hand the agent the task and run it

[02:17] **Speaker**: The thread ID here is just a random UUID. We're not trying to resume a conversation. We just want every run to be its own clean trace in LangSmith

[02:25] **Speaker**: And then we print the last message, which is the model's final answer

[02:28] **Speaker**: Now our second agent, which has the same tool, the same shared system prompt, but no middleware at all, this is the agent

[02:35] **Speaker**: Without an interpreter

[02:37] **Speaker**: This agent has exactly one way to touch the database, to call query Chinook directly, look at what comes back, and then decide what to ask next  same task and the same pattern. To invoke, and then print the last message.  We write it this way so that by the time we get to the output, the two runs are as close to identical as we can make them, except for that one capability.

[03:00] **Speaker**: Let's run it

[03:04] **Speaker**: Great

[03:06] **Speaker**: so this is with the interpreter  And this is without the interpreter

[03:11] **Speaker**: the top-selling artist  They both return Iron Maiden

[03:17] **Speaker**: Same for the best-selling album

[03:19] **Speaker**: Same thing again

[03:20] **Speaker**: Both agents get the right answer. So the lab isn't about one agent being more correct than the other. It's about how they got there, and we can see this better through LangSmith
