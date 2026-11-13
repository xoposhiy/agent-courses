# Filesystem Backends Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/q4b8LOnnehl) · [Raw file](../../raw/videos/q4b8LOnnehl.html)

Retrieved: 2026-11-13T16:57:39.405793+00:00

[00:01] **Speaker**: This lab introduces file system backends, which control where the agent's files actually live. The agent always sees the same six tools, ls, readfile, writefile, etcetera, and the backend is what changes underneath.

[00:14] **Speaker**: At the top, we import three backends, CompositeBackend, FileSystemBackend, and StateBackend

[00:20] **Speaker**: We also import FileSystemPermission, which we'll use to restrict what the agent can do

[00:25] **Speaker**: First, we create a local directory called reference sitting next to this file

[00:30] **Speaker**: And this just means it won't error if it already exists

[00:34] **Speaker**: Then we write a file into that reference directory called chinook_sales.md. This is the agent's starting material, A fictional sales rep brief for the Chinook Digital Music Store. We're creating this file in Python so the lab is self-contained. You don't need to create anything manually before running it

[00:52] **Speaker**: Here's where the agent's created, and there are a few things to notice First, the composite backend. It has a default

[00:59] **Speaker**: and a rat's dictionary

[01:01] **Speaker**: The default is state backend, and that means that any file the agent creates outside of a match route goes into the thread state. It's fast, zero configuration, and scoped to the current thread

[01:11] **Speaker**: What this dictionary says is that anything under reference should go to a FileSystemBackend pointing at our local reference directory   Virtual mode being assigned true means the backend translates the agent's virtual path, so the agent can use reference like any other directory, but the backend handles where it actually reads and writes  File system permission. This rule says

[01:33] **Speaker**: To deny  all write operations

[01:35] **Speaker**: on paths matching reference. The important thing here is that this is enforced in code. The model cannot reason around it. If it tries to write to reference, the tool call fails immediately. rules are evaluated in order and first match wins.

[01:49] **Speaker**: Since no other rule matches, reads on reference are still allowed and everything else defaults to allowed

[01:57] **Speaker**: Finally, the request itself. We give the agent two things to do

[02:01] **Speaker**: To read the file

[02:03] **Speaker**: and then add a note to it.  The reading will succeed.

[02:06] **Speaker**: but the writing will be blocked

[02:08] **Speaker**: We also pass a thread ID in configuration. We're not using a checkpointer here, but the thread ID still gets attached to the LangSmith trace so that the runs are grouped together

[02:17] **Speaker**: We print the last message, which will be the agent summary explaining what happened. Let's take a look

[02:26] **Speaker**: There we go

[02:27] **Speaker**: Writes to reference have been denied
