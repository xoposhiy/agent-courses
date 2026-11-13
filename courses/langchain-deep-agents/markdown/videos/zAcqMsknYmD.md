# task()

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/zAcqMsknYmD) · [Raw file](../../raw/videos/zAcqMsknYmD.html)

Retrieved: 2026-11-13T16:57:39.923633+00:00

[00:00] **Speaker**: The code interpreter you saw in module two exposes  a global task function that bridges straight to the exact same task tool a main agent would call directly. So concretely, in deep agents  task takes a description and a subagent type

[00:15] **Speaker**: When the interpreter, CodeInterpreterMiddleware, has subagents configured, it freezes a task function into its global scope, so calling it from a script inside the interpreter invokes that same underlying tool

[00:25] **Speaker**: Each call still runs a fresh, isolated invocation of that subagent, so clean slate, no memory of prior runs executed end to end.  Nothing  about what gets invoked changes based on who called task, whether it's the model directly or a script running in the interpreter

[00:39] **Speaker**: Task is the subagent side equivalent of programmatic tool calling,  PTC, from module two. So it's the same idea applied to subagents instead of ordinary tools

[00:49] **Speaker**: so first,  a request comes in that reads like an orchestration job, and the main agent decides to write code rather than delegate turn by turn. Then the main agent calls the eval tool and hands it a script.  From here, the script runs inside the interpreter and is in control.  Then the script calls task three times, once per item.

[01:07] **Speaker**: Each call runs a fresh, isolated invocation of that subagent. Now we aggregate. Each subagent runs end to end and returns its result to the script, not to the main agent. The script combines them itself in code. So this is just a little zoom in. That combine step is just an ordinary function the model wrote, not a fourth subagent call.

[01:27] **Speaker**: Code decides how the pieces fit together. This example uses the fan out and synthesize pattern, and we'll see some more patterns later

[01:35] **Speaker**: Now only the combined result crosses back out of the interpreter. The main agent sees one clean result, not three separate subagent transcripts.

[01:44] **Speaker**: interrupt_on pauses a tool call for human approval before it executes, but only for tool calls the model makes directly.  Task calls made from inside an already running eval call don't go through that path, so a per-tool interrupt_on gate on the parent agent's task tool won't catch them. If you need a human-in-the-loop before orchestration runs, gate the eval tool itself, not the individual subagent dispatches inside it.

[02:07] **Speaker**: interrupt_on configured on an individual subagent's own spec still applies, since that gate runs inside the subagent's own invocation, not the parent's dispatch.   now for setup, the interpreter runtime is currently beta and needs this version of Python or later

[02:24] **Speaker**: you import CodeInterpreterMiddleware from LangChain QuickJS and pass it into createDeepAgent  as middleware. Same shape you've seen for other middleware

[02:33] **Speaker**: now dynamic subagent dispatch is on by default

[02:36] **Speaker**: since this is the default. You can disable it  if you assign false to subagents. But what actually triggers it is the word workflow in the prompt

[02:44] **Speaker**: Code interpreter middleware injects a literal instruction into the system prompt on every model call. If the request uses the word workflow, write orchestration code that dispatches subagents with task() and assembles the results instead of delegating one at a time.

[02:58] **Speaker**: So here in this code, we see run a workflow that reviews every file, yada, yada, yada. And for a single direct delegation, phrase the request plainly instead  so you don't trigger orchestration you didn't need.

[03:10] **Speaker**: for seamless zero setup testing  LangChain's Deep Agents code, which is an open source terminal coding agent built on the Deep Agents SDK, it ships with the interpreter pre-enabled

[03:21] **Speaker**: So use this if you want to try this without writing any code yourself
