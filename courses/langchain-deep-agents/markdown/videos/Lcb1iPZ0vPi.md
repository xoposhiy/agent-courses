# LangSmith Walkthrough

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/Lcb1iPZ0vPi) · [Raw file](../../raw/videos/Lcb1iPZ0vPi.html)

Retrieved: 2026-11-13T16:57:37.415104+00:00

[00:00] **Speaker**: This is what we just ran, and it took three hundred and fifteen point one six seconds, which is roughly five and a half minutes, and cost us two point five dollars.  So a lot happened in this run

[00:15] **Speaker**: And LangSmith captured all of it in detail,  so feel free to go through and take a look yourself

[00:21] **Speaker**: But I'm going to dive into some of the main elements

[00:25] **Speaker**: This is an eval call, which is the interpreter actually running the JavaScript the model wrote. Inside, you'll see a cluster of readfile calls  and then a cluster of task calls

[00:38] **Speaker**: Here's another, and so on and so forth

[00:42] **Speaker**: The reads

[00:44] **Speaker**: Are the interpreter pulling book text out of the manuscript.

[00:48] **Speaker**: Book two   Book three

[00:53] **Speaker**: Now, these tasks are book scanner subagents dispatched together with Promise.all, not one after another. And that's the whole reason this span, despite the size of what's in it, only takes a few seconds. Everything is running at once

[01:10] **Speaker**: So this is one book scanner call on its own

[01:14] **Speaker**: Here we see only one books label, nothing else

[01:19] **Speaker**: This subagent has no idea that another 59 books exist

[01:26] **Speaker**: One more thing to point out with the main agent

[01:30] **Speaker**: you'll see the whole conversation only contains one short human message: " Run a workflow to find every corrupted sentence in the manuscript." That's it. There's no actual manuscript text anywhere in the input So the main agent doesn't see the manuscript itself, just the short verdicts that each subagent scanner sent back.

[01:46] **Speaker**: The interpreter held the file, and the main model never touched it

[01:54] **Speaker**: so this is our final AI message, and it says, "Here's the complete report of every anachronistic sentence found across all sixty books, verified by direct grep against the manuscript."

[02:05] **Speaker**: So the whole manuscript's worth of scanning is reduced to this

[02:10] **Speaker**: So the main agent sees the quote

[02:12] **Speaker**: And the line number. But that's all that makes it back, not the book itself. And that's really the whole pattern here. The interpreter holds the big thing, dispatches a lot of small isolated calls at once, and the main model only ever sees what comes back.
