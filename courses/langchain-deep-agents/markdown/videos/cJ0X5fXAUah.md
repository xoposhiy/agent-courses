# Memory Lab (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/cJ0X5fXAUah) · [Raw file](../../raw/videos/cJ0X5fXAUah.html)

Retrieved: 2026-11-13T16:57:38.242127+00:00

[00:01] **Speaker 8**: We have two runs here, both labeled memory agent, one per agent invoke call. Let's look at the first one.

[00:10] **Speaker**: This is when we asked, "What tool should I use for file paths in this project?" Now, if we scroll down here

[00:19] **Speaker**: we find the agent memory block  And this contains the raw contents of agents.md

[00:25] **Speaker**: Injected by memory middleware before the LLM was even called. That's why the agent answered pathlib.Path with zero hesitation  The rule was already in its context. Now let's take a look at the second run

[00:41] **Speaker**: See down here Under tools, we have edit file. The agent used the content it already had in the agent memory block to construct the edit. It didn't need a separate file read.    The edit file call targeting agents.md is the moment the rough note gets written in.  From this point on, every future run would include it in the agent memory block automatically.
