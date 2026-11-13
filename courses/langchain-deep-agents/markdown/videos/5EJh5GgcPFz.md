# Messages, Threads, and Checkpointers

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/5EJh5GgcPFz) · [Raw file](../../raw/videos/5EJh5GgcPFz.html)

Retrieved: 2026-11-13T16:57:36.328900+00:00

[00:01] **Speaker**: Deep agents keep track of more than one model call, and to do that reliably, three runtime ideas need to work together  Messages, threads, and checkpointers. You've already used all of these in the labs. Now we'll name the pieces and show how they fit

[00:16] **Speaker**: When you invoke a deep agent, you pass in a list of messages. That list is the conversation history the model sees. Here, we're starting with one message

[00:25] **Speaker**: a user message  With the content,  what is an LLM?

[00:29] **Speaker**: Every turn adds more messages to it.  And there are three kinds of messages.  The user message is the human's input.  What you just saw  The AI message is the model's response. It can contain plain text   or tool calls

[00:43] **Speaker**: The ToolMessage is the result returned after a tool runs. Every agent run produces some combination of these three types, building up a list as the conversation progresses.

[00:55] **Speaker**: The final response is usually the last message in that list, which is why you'll see  this negative one index throughout the course. It reaches for the last item without needing to know how many messages were produced

[01:06] **Speaker**: Now, an important mental model is that the agent is not passing one prompt to the model. It is building and updating a message history across the whole run

[01:16] **Speaker**: A thread is one ongoing conversation. To make two separate invoke calls share history, you give them the same thread ID

[01:25] **Speaker**: in the configuration  This config dict is passed as the second argument to each invoke call

[01:32] **Speaker**: Now the first call

[01:33] **Speaker**: tells the agent the user's favorite color is blue,  and this message is saved to the thread  And the second call

[01:41] **Speaker**: asks what the favorite color is,  passing the same thread ID

[01:46] **Speaker**: so that the agent can answer correctly because both calls share the same history

[01:52] **Speaker**: same thread ID, shared history. Different thread ID, a complete separate conversation that starts fresh

[02:01] **Speaker**: But a thread ID alone is not enough. There has to be somewhere to actually store that history between calls. And that's what a checkpointer does. Without one, there's nowhere to save state, and each invoke starts from scratch, regardless of the thread ID

[02:14] **Speaker**: Memory Saver is all you need for local development. It stores checkpoints in the current Python process, and when you deploy agents in production, you swap it for persistent infrastructure so threads survive restarts, but the API stays exactly the same. And this is what ties it together. After each call, the checkpointer saves the current thread state, and the next call with the same thread ID picks that state back up and continues from it.
