# Lab (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/KqVlE3klzVJ) · [Raw file](../../raw/videos/KqVlE3klzVJ.html)

Retrieved: 2026-11-13T16:57:37.336643+00:00

[00:01] **Speaker 7**: Here's our sales assistant run.  One turn  with two model calls  Let's go through the three stages: discovery, activation, and execution

[00:12] **Speaker**: The first thing that runs isn't the model.  It's skills middleware, which reads all the skill frontmatter and injects the discovery list into the system prompt before the agent sees anything.

[00:27] **Speaker**: So this part is discovery  Both skill names

[00:31] **Speaker**: and descriptions

[00:33] **Speaker**: are listed here. There's no body content, nothing about the BANT framework And it's just the trigger text. This is what the agent uses to decide which skill to activate   This is what we asked our agent to do to qualify this lead. The agent sees this, matches it to Qualify Lead's description

[00:52] **Speaker**: And declares its intent. They'll use this qualify lead skill to systematically evaluate this prospect

[00:58] **Speaker**: And we can see that it called readfile.

[01:02] **Speaker**: This is activation. The agent called read_file as exactly one skill file.    It called qualify lead followed by the full body.

[01:15] **Speaker**: We can see that draft pitch was never touched. Now let's look at the second model call

[01:21] **Speaker**: This is execution. The model has the full skill body and applies it to the lead details from the user message  the model worked through each BANT criterion and produced a structured output. That structure comes directly from the output section in Qualify Lead

[01:35] **Speaker**: So now we've seen discovery, activation, and execution
