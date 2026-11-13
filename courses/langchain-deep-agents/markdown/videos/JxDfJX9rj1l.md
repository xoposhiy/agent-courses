# Memory: Short Term vs. Long Term

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/JxDfJX9rj1l) · [Raw file](../../raw/videos/JxDfJX9rj1l.html)

Retrieved: 2026-11-13T16:57:37.208505+00:00

[00:01] **jess**: Agent memory splits into two scopes: short-term and long-term

[00:05] **Speaker**: Short-term memory is the running message history for a single thread. It's tracked automatically by the checkpointer and does not persist beyond that thread Long-term memory is what the agent has learned that should carry over across threads, things like user preferences, project conventions, and recurring facts. It's tracked in a persistent store or file system and separate from any one thread's message history.

[00:27] **Speaker**: The distinction here is scope, not lifetime. A checkpointer can be backed by a real database and outlive the process. It's still short-term though, because that history only exists inside the thread that created it. Long-term memory is visible to any thread that matches its scope, same user, same workspace, whatever you choose, regardless of which thread wrote it

[00:47] **Speaker**: Now, both scopes can technically live in the file system. Deep agents already offload some short-term context to files by default, mainly to keep large tool outputs out of the message history.

[00:57] **Speaker**: This lesson focuses on long-term memory. In deep agents, long-term memory is represented as files in the backend, and any file the agent can read or write can be treated as memory once you configure it that way This is short-term memory,  the message history for one thread. Say the task at hand is write an email to my boss, and here's what it's about, and so on. That's the kind of thing that lives here, specific to this one conversation. Human message, AI message, and so forth, and all of this flows straight down to the LLM.

[01:28] **Speaker**: Now, the checkpointer over here is infrastructure, so not part of the messages, but attached to this thread

[01:34] **Speaker**: Everything from earlier turns in this thread is already sitting in storage with the checkpointer, not here. So at the start of a new run, this load arrow is the checkpointer handing that saved history back over into here, so the conversation picks up right where it left off. Now, this save arrow over here

[01:52] **Speaker**: Once a step happens, the updated history gets saved back out to the checkpointer. Load happens once at the start, but save can happen more than once after each step, so the checkpoint stays current as the run goes. And that's why each thread's history stays isolated. Nothing here gets shared with other threads  now, long-term memory are facts shared across every thread with access. Think of things like your email preferences, always write formally, or how you relate to specific people. Person A is a coworker, Person B is your boss. That's the kind of thing this holds onto, no matter which conversation you're in. So these are facts sitting in a shared store, which then flow down into the LLM One store is shared across every thread

[02:38] **Speaker**: Whatever gets written by one thread is there for the others too.  And here's what it looks like when both are configured together. Now, both paths land on the same LLM. As you can see here, it isn't calling the checkpointer or the store directly. It's just seeing messages and memory land in front of it
