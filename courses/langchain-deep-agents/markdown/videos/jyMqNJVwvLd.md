# Seeing It In Action

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/jyMqNJVwvLd) · [Raw file](../../raw/videos/jyMqNJVwvLd.html)

Retrieved: 2026-11-13T16:57:38.788084+00:00

[00:00] **Speaker**: The default trigger is roughly 85% of the model's real context window. For Claude Haiku 4.5, that's roughly 170,000 tokens. To actually see it fire in a demo, we override  this to a small value so that the threshold is hit after just a few turns

[00:16] **Speaker**: Notice that we're passing the model object to create Deep Agent, not the string anthropic claude haiku four five. Passing the string would reinitialize the model internally and throw away the profile override.

[00:27] **Speaker**: So on the first two turns  The output shows stored two messages, raw history never trimmed. Four messages, raw history never trimmed. So summarization hasn't fired yet

[00:39] **Speaker**: Now in turn three, we see summary plus the messages and summarized.  From here on, every subsequent turn  shows model saw summary plus messages, meaning the model receives the summary plus only the most recent messages, not the full history  In this conversation, we told them our name, where we worked, asked what two plus two is, and that we've been building a distributed cache for three months.

[01:06] **Speaker**: On turn five

[01:08] **Speaker**: we ask what they remember about us  You mentioned your name is Alex, you work at Acme Corp, and you've been building a distributed cache for three months  The agent correctly recalls the name, company, and project from earlier turns, even though it never directly saw them again.  So the summary did its job

[01:26] **Speaker**: There's one important detail. In the normal summarization path  State messages is preserved, so summarization only changes what gets sent to the model each turn, not what's stored.
