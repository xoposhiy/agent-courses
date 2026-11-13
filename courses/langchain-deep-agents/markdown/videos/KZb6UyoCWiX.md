# Decision Types

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/KZb6UyoCWiX) · [Raw file](../../raw/videos/KZb6UyoCWiX.html)

Retrieved: 2026-11-13T16:57:37.298782+00:00

[00:00] **jess**: Four decision types settle a pause tool call   Approve runs the tool exactly as proposed.  Edit lets the human change the arguments first, then run the tool with those  Reject stops the tool entirely, so the agent gets a message explaining why, but not the file deletion or the email send.  And Respond works differently from the other three   It's not built for tools with a side effect at all.

[00:21] **Speaker**: Some tools exist purely to ask a question and wait for a person to answer it. Think of a tool that pauses the agent and needs the human to pick between two options or supply a missing detail before the agent can continue. That tool doesn't do anything to the outside world.

[00:34] **Speaker**: Its whole output is whatever the human tells it. So instead of running any code, respond takes the human's answer and hands it back to the model as if the tool itself had returned that value. That's also why you shouldn't confuse reject and respond.  Both skip running the tool, but they mean opposite things to the model.

[00:50] **Speaker**: Reject essentially says, " This didn't happen."  But respond basically says, " Here's your answer," as if the tool succeeded. So if you use respond on something like a send_email tool, then the model thinks the email went out. Reserve respond for question-asking tools only

[01:07] **Speaker**: And a word of caution, when editing tool arguments, keep the changes small. A heavy rewrite can make the model reevaluate its whole plan instead of just continuing. A smaller one-field fix will keep it on track

[01:20] **Speaker**: Approve,  edit  Reject

[01:22] **Speaker**: And respond. It's the same interrupt_on_setup, same checkpointer, and same resume call, but four different outcomes.
