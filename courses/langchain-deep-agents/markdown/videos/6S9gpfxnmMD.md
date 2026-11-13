# Lab 1 (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/6S9gpfxnmMD) · [Raw file](../../raw/videos/6S9gpfxnmMD.html)

Retrieved: 2026-11-13T16:57:36.392915+00:00

[00:01] **Speaker 2**: Here we can see two turns, one for each agent invoke call. This first one is the initial call that pauses. The second is the resume after approval. Let's walk through each

[00:16] **Speaker**: So turn one's input is the user's message. "Send an email to Jane saying I'll be 10 minutes late."  And we can see in the output, the model decided to call send_email and drafted the arguments.  But notice there's no tool result here

[00:30] **Speaker**: Execution stopped at human-in-the-loop middleware, which is what interrupt_on hooks into. So the tool call is proposed but not executed. The checkpointer saved the state at this point and returned control to our code, which is where the terminal printed those pending arguments and asked for a decision

[00:47] **Speaker**: So turn two starts with human-in-the-loop middleware again. This is the resume path

[00:52] **Speaker**: So the agent loaded the safe state and the middleware processed the approval decision.

[00:59] **Speaker**: We can see  that the tool ran this time. The full conversation is here   The original user message, the model's tool call,  the tool result

[01:09] **Speaker**: confirming that the email was sent

[01:11] **Speaker**: and the agent's final response. Everything that was paused in turn one completed here after approval
