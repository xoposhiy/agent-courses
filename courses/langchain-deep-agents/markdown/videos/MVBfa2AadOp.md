# Memory

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/MVBfa2AadOp) · [Raw file](../../raw/videos/MVBfa2AadOp.html)

Retrieved: 2026-11-13T16:57:37.516736+00:00

[00:00] **Speaker 9**: Now, Deep Agents makes memory first class with file system backed memory. The agent reads and writes memory as plain files, and you control where those files are stored using backends.  Memory files are markdown, loaded at agent startup and injected into the system prompt on every LLM call. Skills load on demand when a task matches, but memory's always present regardless of the task.

[00:21] **Speaker**: By convention, memory files live in a memories directory and the main file  is named agents.md  This follows the agents.md specification, a shared format that many tools and frameworks recognize.  So take this as an example  Here we have a Project Guidelines heading  A code style section with a couple of bullet points  and a workflow section noting how to run tests.

[00:44] **Speaker**: There's no required structure and no schema to learn. The agent reads and writes this file with the same file system tools it already knows,  especially edit file

[00:53] **Speaker**: There's no separate memory database API for the agent to learn

[00:57] **Speaker**: to attach memory to your agent

[00:59] **Speaker**: We pass a memory argument with a list of file paths. Without it, memory middleware isn't active and nothing gets surfaced to the model , even if the file persists just fine in the backend . Paths are relative to the backend's root, and multiple files are supported.

[01:14] **Speaker**: Passing memory  creates memory middleware behind the scenes. For every run  The middleware loads each configured memory file from the backend  stores the loaded contents in AgentState

[01:24] **Speaker**: and appends the combined memory to the system prompt  inside an agent memory block on every model call in that run.

[01:31] **Speaker**: That's a meaningfully different loading model from skills. With skills, only names and descriptions are always visible, and full content loads on demand when the agent activates that skill. With memory, the full loaded content is proactively present on every call in the run. Memory holds durable facts and instructions the agent should always have in view, while skills hold reusable workflows the agent only needs when a task calls for them.

[01:54] **Speaker**: So when a user says

[01:56] **Speaker**: Remember this, the agent calls edit_file  directly on one of the paths passed to memory.  If a user says

[02:04] **Speaker**: Remember, the team switched to Ruff for linting

[02:07] **Speaker**: The agent edits

[02:08] **Speaker**: this to add that note.  That  write  updates the backend file, and the updated content shows up in the &lt;agent_memory> block  on subsequent calls  once memory is reloaded in a later run.  The one hard rule is to not store secrets, API keys, credentials, tokens, or passwords.  Now, where does that file actually live? The backend controls where memory files are stored, and a common production pattern

[02:32] **Speaker**: its composite backend.

[02:34] **Speaker**: We keep normal working files in the default backend and route a dedicated  memories directory to durable storage

[02:42] **Speaker**: We import CompositeBackend, StateBackend, and StoreBackend

[02:46] **Speaker**: plus an in-memory store

[02:47] **Speaker**: From LangGraph

[02:49] **Speaker**: we define a memory_namespace function that reads  user ID

[02:52] **Speaker**: and workspace ID off the runtime context and returns a tuple

[02:56] **Speaker**: Then we build the agent

[02:58] **Speaker**: With this

[03:00] **Speaker**: Pass the store in  and pass memory

[03:03] **jess**: This code is doing three different jobs at once, so let's take it row by row down here

[03:08] **Speaker**: StateBackend  is scoped to a single thread,  and it does not persist past the thread,  so it's used for temporary working files.  StateBackend is what you reach for when the agent just needs scratch space for the current run

[03:21] **Speaker**: Now store backend  is scoped to whatever namespace you define, whether it's a workspace, a user, whatever segments you pick,  and it does persist past the thread.  So it's used for persistent long-term memory.  Now composite backend

[03:35] **Speaker**: just routes paths to the backends above  So it sometimes persists past the thread depending on the route  It's used for splitting working files from memory files  So it's not really its own storage tier, it's the dispatcher deciding which of the other two rows a given path lands in

[03:51] **Speaker**: Now, in_memory_store is not a backend itself. It's the base store implementation store backend actually writes to, passed in separately  via this. It plays the same role for cross-thread memory  that in_memory_saver plays for thread history. Both are quick in-process stand-ins for local development, and whatever they hold lives inside the running Python process, so it's gone the moment the process restarts  In production, you'd swap each one out for a persistent version, a database-backed store, and a database-backed checkpointer.

[04:20] **Speaker**: Same interface, but real infrastructure underneath

[04:23] **Speaker**: Now scoping. The store backend namespace on the memories route determines which persistent memory files the agent actually sees. In a real application, you usually derive that namespace from runtime context, the authenticated user, the workspace, the tenant, or the assistant ID

[04:38] **Speaker**: Scope isn't a fixed choice between shared and per user. It comes from which segments you include in the namespace tuple, and any combination is valid

[04:47] **Speaker**: if your namespace factory returns  memory  and assistant ID

[04:51] **Speaker**: For example, every user talking to Support Bot writes to the exact same file

[04:55] **Speaker**: Memory  and support bot

[04:58] **Speaker**: Now if instead it returns  memory

[05:02] **Speaker**: assistant ID  and user ID

[05:05] **Speaker**: User123's memory lives at memory  Support bot  and user123. A completely separate key  that second tuple isn't a subfolder of the first, even though it looks like an extension of it. The store treats them as two unrelated keys. A namespace lookup here is an exact match, not a hierarchical one.

[05:24] **Speaker**: And this isn't something the agent decides per request. You pick one shape when you write the namespace factory, always two segments or three, and every invocation resolves that through the same shape, just with different values slotted in

[05:37] **Speaker**: The memory_namespace function from before already defines a user and workspace scope namespace. Invoke the agent with matching context, and the store resolves to that same namespace

[05:48] **Speaker**: that context dictionary is what flows into the namespace factory.  user ID and workspace ID to build the actual scope for this run.

[05:57] **Speaker**: Here are a few common shapes worth knowing  such as shared assistant memory

[06:01] **Speaker**: which is just the assistant ID

[06:03] **Speaker**: And everyone talking to that assistant shares the same file

[06:06] **Speaker**: For user memory,  it's just the user ID

[06:09] **Speaker**: and it follows one person across every thread

[06:11] **Speaker**: Workspace memory  is just the workspace ID  shared across a team or project

[06:16] **Speaker**: Now userWithinWorkspace  is workspaceId  plus user ID

[06:21] **Speaker**: And it's a private notebook inside a shared team space. Probably the most common real world pattern  As for Assistant Plus user

[06:28] **Speaker**: it's assistant ID  and user ID

[06:31] **Speaker**: It's used for when the same person talks to multiple assistants and shouldn't have memory bleed between them.

[06:36] **Speaker**: So you want to choose the scope deliberately. Getting it wrong has consequences in both directions. If private user memories share a namespace, one user's context can leak into another user's run. That's a privacy problem. If shared team memory gets scoped too narrowly, on the other hand, say per user when it should be per workspace, the agent fails to reuse conventions that should apply across the whole workspace, and you lose the benefit of sharing at all
