# Lab 1 (accept/edit/reject)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/FXc8O0Aoa62) · [Raw file](../../raw/videos/FXc8O0Aoa62.html)

Retrieved: 2026-11-13T16:57:37.020149+00:00

[00:01] **Speaker**: This lab puts a human checkpoint between the agent and a side-effecting tool. The agent can propose to send an email, but it cannot actually send it until a person approves. Let's go through the file  Here we have two new imports, Command from langgraph types and MemorySaver from langgraph checkpoint memory. We saw MemorySaver in the last lab. Command is new.

[00:21] **Speaker**: We use it to resume a paused run

[00:24] **Speaker**: Here's our send email tool

[00:27] **Speaker**: it takes a recipient, subject, and body and returns a confirmation string. This is a mock. It doesn't contact a real email service, so the lab is safe to run

[00:36] **Speaker**: And here's our system prompt. The first three rules are standard behavior. Use the tool when asked, keep emails professional, and don't claim the email was sent until the tool result confirms it.

[00:46] **Speaker**: This last rule is just for the edit path  When confirming, quote the subject and body from the tool result, not the original request. You'll see this later in the terminal

[00:58] **Speaker**: create_deep_agent has two new arguments

[01:00] **Speaker**: interrupt on

[01:01] **Speaker**: With send_email true means that if the model decides to call send_email, to pause before the tool executes and surface the pending call for review  The checkpointer is required because when the agent pauses, it needs somewhere to save its current state so the run can be resumed later from exactly the same point.

[01:17] **Speaker**: Here's a stable thread ID. The checkpointer uses this to find the paused run when we resume. If you pass a different thread ID  AKA  you change this the agent won't be able to find the save state

[01:30] **Speaker**: The first invoke. This sends the user's request and runs the agent until it hits the interrupt. It doesn't return a final answer.  It returns a result with  __interrupt__ set containing the pending tool call for your review.

[01:44] **Speaker**: Here's the review loop. It checks whether the result contains an interrupt, prints the pending tool call, and asks for a decision

[01:51] **Speaker**: There are three options here

[01:53] **Speaker**: Approve runs the tool exactly as the model proposed  Edit lets you replace the email body before the tool runs

[02:00] **Speaker**: And reject cancels the tool call entirely. The agent receives a cancellation result and never sends the email

[02:06] **Speaker**: After collecting the decision, this line calls agent.invoke again

[02:11] **Speaker**: With this  and the same configuration.  That continues the paused run

[02:15] **Speaker**: Once the loop exits, the run is complete and we print the final message. Let's take a look

[02:24] **Speaker**: There we go  The agent paused, and here are the arguments it proposed  the recipient,  the subject

[02:31] **Speaker**: and the body

[02:33] **Speaker**: Let's approve

[02:36] **Speaker**: So the tool ran and the agent confirmed the content from the tool result.
