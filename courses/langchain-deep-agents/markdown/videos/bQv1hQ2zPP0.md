# Messages, Threads and Checkpointers Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/bQv1hQ2zPP0) · [Raw file](../../raw/videos/bQv1hQ2zPP0.html)

Retrieved: 2026-11-13T16:57:38.209663+00:00

[00:00] **Speaker**: This lab is about how the agent remembers things across multiple calls. Three concepts make that work: messages, threads, and checkpointers

[00:08] **Speaker**: This new import is MemorySaver from LangGraph checkpoint memory.  Create Deep Agent looks the same as before, but with one new addition

[00:16] **Speaker**: MemorySaver assigned to checkpointer. A checkpointer is what gives the agent somewhere to save thread state between calls, and without it, each invoke starts fresh with no memory of what came before. MemorySaver stores that state in memory, which is fine for local development

[00:30] **Speaker**: Two thread configurations. A thread is an ongoing conversation identified by a thread ID

[00:36] **Speaker**: Pass the same thread ID to continue an existing conversation and pass a different one to start a separate conversation with its own history.  Here we have thread A  and thread B

[00:46] **Speaker**: Thread A, turn one

[00:49] **Speaker**: The user tells the agent their favorite color is blue

[00:53] **Speaker**: And we pass this so the checkpointer knows which thread to save this to.

[00:57] **Speaker**: Thread A, turn two. Same question and same thread. The agent receives the new message

[01:03] **Speaker**: But the checkpointer also loads the saved history from turn one, so the model sees the full conversation,  the original message

[01:10] **Speaker**: The agent's response  And now this new question. It should know the answer is blue

[01:16] **Speaker**: now this is thread B, turn one

[01:19] **Speaker**: same question, but different thread. Thread B has no saved history. It's never been used before, so the checkpointer loads nothing. The model sees only this one message with no context about favorite colors.

[01:31] **Speaker**: Let's see how it runs

[01:37] **Speaker**: so in turn one

[01:39] **Speaker**: It noted our favorite color is blue

[01:41] **Speaker**: In turn two,  they remembered that  But in thread B turn one

[01:45] **Speaker**: It simply doesn't know. It has a different thread ID, so the checkpointer gave it a clean slate. No message history

[01:52] **Speaker**: It's the same agent and the same model, but completely separate state.
