# Putting it all together

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/phWZWmbUpx5) · [Raw file](../../raw/videos/phWZWmbUpx5.html)

Retrieved: 2026-11-13T16:57:39.367313+00:00

[00:01] **Speaker**: Alrighty, now you've used all of the major features of Deep Agents. Well, all of the ones available so far. There's always more coming. Now it's time to put them together into a bigger project

[00:12] **Speaker**: We're going to build a sales assistant for Jane Peacock, a sales rep at Chinook, the online music distributor. You may not be in sales, and you may not need an assistant, but here's what I want you to notice as we go

[00:24] **Speaker**: Very little of what we build requires code. It's a little bit of Python and a lot of text files. Most of the programming happens in natural language

[00:34] **Speaker**: an agents.md file that describes how the agent should behave

[00:37] **Speaker**: And a set of skills, which tell it how to get tasks done.  It's one deep agent, but it's a complete realistic application. It reads quote requests out of an inbox, looks things up in a real database, drafts replies for Jane to approve, writes a newsletter, and reports on how her territory is doing

[00:56] **Speaker**: Along the way, we'll lean on just about everything you've built so far

[01:00] **Speaker**: subagents that act like specialists, one for the database, one for the inbox, and one that double checks a quote before it goes out. And when we get to the newsletter part, you'll see subagents running in parallel

[01:11] **Speaker**: one per genre

[01:13] **Speaker**: Now, the file system is where all of this lives

[01:16] **Speaker**: the skills

[01:17] **Speaker**: The agents.md file, the quotes ledger, and the newsletter

[01:21] **Speaker**: The interpreter handles the quote math so numbers are computed instead of guessed.

[01:26] **Speaker**: And human-in-the-loop puts a checkpoint in front of anything consequential, like sending an email or adding a new customer

[01:34] **Speaker**: And mail access comes in through MCP.  So this is everything we've already learned in one agent. Before we build it, we're going to talk about deploying an agent. Head on over to the next lesson
