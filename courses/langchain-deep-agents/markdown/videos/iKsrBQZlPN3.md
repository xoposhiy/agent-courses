# HITL

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/iKsrBQZlPN3) · [Raw file](../../raw/videos/iKsrBQZlPN3.html)

Retrieved: 2026-11-13T16:57:38.697979+00:00

[00:01] **jess**: In the tools lesson, you saw that tools can do more than retrieve information. They can take real actions

[00:07] **Speaker**: And in the previous lesson, you saw how checkpointers let an agent save and resume state  Human-in-the-loop combines those ideas

[00:14] **Speaker**: Pause the agent before a sensitive action happens

[00:17] **Speaker**: and let a person approve, edit, or reject it before the side effect occurs  The main reason is safety.  if an agent is about to send an email, update a database, or delete a file, you may want a human to checkpoint first

[00:30] **Speaker**: Human-in-the-loop is also how an agent suspends execution and waits rather than staying active indefinitely

[00:37] **Speaker**: so the model asks to call a sensitive tool, in this case, send email. But because that tool is listed in interrupt_on, it does not execute yet. The agent stops here and surfaces the pending tool call for review.

[00:50] **Speaker**: The agent pauses and returns the pending tool call to the human. At the same time, the checkpointer saves the full agent state, the thread, the messages, everything, so the run can be resumed later from exactly this point. Nothing is lost

[01:05] **Speaker**: The human sends a resume command with a decision. There are a few options: approve, which means the tool runs as proposed; edit, which means the human supplies revised arguments and the tool runs with those instead; or reject, and the tool never runs, and the agent receives a cancellation result and responds accordingly.

[01:25] **Speaker**: Four things make this work together

[01:27] **Speaker**: InterruptOn names the tools that require review before they execute  The checkpointer saves the pause state. Without it, there is nothing to resume.  The thread ID identifies that save state so the resume call can find it  And command resume is how you pass the human decision back into the pause run.
