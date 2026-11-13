# Lab 2 (LS walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/UVi0Mf9NUwx) · [Raw file](../../raw/videos/UVi0Mf9NUwx.html)

Retrieved: 2026-11-13T16:57:37.982419+00:00

[00:00] **Speaker**: This thread shows three runs even though we only sent one message, and that's because every agent invoke call in our script, this first one, plus every resume after an interrupt, shows up here as a separate turn on the same thread  This is the very first call

[00:18] **Speaker**: So the model gets the user's message and decides it needs more information before drafting anything

[00:24] **Speaker**: So then it calls a tool.  AskUser

[00:28] **Speaker**: with a question  And a list of choices. This maps directly to our ask_user tool definition in the code. Now, if you look back over here, this is the middleware step where the graph checks interrupt on

[00:41] **Speaker**: Since ask_user only allows the respond decision, the graph pauses right here instead of letting the tool run, and that's why turn one ends after this node.  It's an interrupt, not a normal finish

[00:53] **Speaker**: Let's look into turn two

[00:55] **Speaker**: So this turn corresponds to the first iteration of the while result.interrupts: loop  In the terminal, questionary.select showed the two choices, and we picked one. The code packaged it as  {"type": "respond", "message": selected}

[01:11] **Speaker**: there's no new user message here, just the resume state. The model receives our answer

[01:16] **Speaker**: as if ask_user had returned it directly, then decides it's ready to send the email

[01:22] **Speaker**: Here's the model calling our send email tool with a subject

[01:27] **Speaker**: and body

[01:29] **Speaker**: And again, we have human-in-the-loop middleware after

[01:33] **Speaker**: So same story, different tool

[01:37] **Speaker**: SendEmail allows approve, edit, and reject, so the graph interrupts again here, waiting for our decision in the terminal.   Let's look into turn three   This is the second loop iteration. We approve the email, so the code sent {"type": "approve"} back through Command(resume={"decisions": decisions}).

[01:55] **Speaker**: So here we see send email under the tools node

[01:59] **Speaker**: This time, the tool actually executes, And you can tell because it's a Live Tools node instead of stopping at the middleware

[02:08] **Speaker**: The model then sees the tool's result  and generates the final confirmation message
