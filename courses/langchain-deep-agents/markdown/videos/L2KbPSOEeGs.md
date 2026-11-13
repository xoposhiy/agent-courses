# Behaviour and Design

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/L2KbPSOEeGs) · [Raw file](../../raw/videos/L2KbPSOEeGs.html)

Retrieved: 2026-11-13T16:57:37.371447+00:00

[00:00] **Speaker**: launching a task and immediately checking on it defeats the point.  So the model needs to report the task ID  and move on,  not just sit there polling until it's done. Async subagent middleware accepts a system prompt argument to instill that discipline, and this lesson's lab relies on async subagent middleware's built-in default for that prompt,  and it enforces these things

[00:21] **Speaker**: Launch, then stop.  After start_async_task, report the task ID and return control. Don't immediately call check_async_task on it

[00:30] **Speaker**: check only on request by default. Its system prompt tells the model to call check_async_task when the user asks for a status update, not on a timer or in a loop.  Auto-notifying the supervisor when a subagent finishes is possible,  but it needs extra middleware on the subagent side that isn't part of this default setup

[00:47] **Speaker**: And to never trust the status already in the transcript. A task that shows running earlier in the conversation may be done by now. Always call a tool to get the current status rather than repeating a stale one.

[00:58] **Speaker**: And that's because the tool result sitting in the transcript saying running was true at the moment that the message was written, but time keeps passing after that.

[01:05] **Speaker**: So if the main agent just reread its own transcript instead of calling check_async_task again, it could confidently report a task as still running even though it's actually finished

[01:15] **Speaker**: An update_async task isn't a message to a listener.  It interrupts the current run and starts a fresh one on the same thread, so the subagent sees the full history plus the new instructions. The task ID doesn't change.

[01:28] **Speaker**: As of the new Deep Agents update, this default prompt is no longer supplied automatically. You have to pass it explicitly via AsyncSubagentMiddleware   to keep this behavior    if the main agent needs a subagent's answer before it can take its next step, sync is simpler and there's less to manage

[01:48] **Speaker**: You'll want async when the work takes long enough that blocking would be wasteful or when you want several things happening at once without serializing them.

[01:57] **Speaker**: now, this is a different topic from dynamic subagents in module four

[02:00] **Speaker**: Dynamic subagents are about the main agent deciding how many subagent instances to spin up and what to hand each one. This lesson is about whether a given delegation blocks or not. They're independent choices.

[02:13] **Speaker**: A dynamically sized batch of subagents could each run asynchronously too
