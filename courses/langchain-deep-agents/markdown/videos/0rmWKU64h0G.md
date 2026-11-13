# Memory Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/0rmWKU64h0G) · [Raw file](../../raw/videos/0rmWKU64h0G.html)

Retrieved: 2026-11-13T16:57:36.283637+00:00

[00:01] **Speaker 5**: This lab has two invokes that demonstrate the two sides of memory, reading and writing.

[00:07] **Speaker**: The agent is a coding assistant that already knows the project's conventions before you say a word. These conventions live in memories or agents.md, and memory middleware injects the file's contents into the system prompt on every single LLM call. The agent doesn't fetch it on demand. It's always there, and the script has two invocations

[00:28] **Speaker**: In the first, we ask a question the model couldn't answer from general knowledge. What tool should I use for file paths in this project? It answers correctly because that's specified in the agents.md file. That's the read side, memory making the agent context aware from the first message.

[00:45] **Speaker**: The second, we tell the agent to remember that the team switched to Ruff for linting. The agent responds by calling edit_file on agents.md, and that's the write side. Memory isn't read-only. When context should persist across sessions, the agent updates the file itself, and from that point on, the new fact is injected on every call

[01:04] **Speaker 7**: Here's what's in agents.md

[01:09] **Speaker**: code style rules  and workflow conventions. These are things the base model has no way of knowing because they're specific to this project. This is the kind of content Memory is designed for

[01:24] **Speaker 5**: FilesystemBackend roots the agent's file system at the m3 directory, which is what allows the agent to read and write files there

[01:32] **Speaker**: The virtual_mode=True flag means writes are tracked in memory rather than immediately hitting disk, which is useful for demos and testing.

[01:41] **Speaker**: Passing memory is what activates memory middleware. That path resolves relative to the backend route, so it maps to m3/memories/agents.md. From this point on, the file's content is injected into the system prompt on every call

[01:57] **Speaker**: The first question asks

[01:59] **Speaker**: What tool to use for file paths, and the agent answers correctly because agents.md

[02:06] **Speaker**: says to use pathlib.Path, and that content is now in the system prompt

[02:13] **Speaker**: The second message

[02:16] **Speaker**: tells the agent to remember that the team switched to Ruff for linting. Because the middleware injects guidelines about when to write, the agent knows to call edit_file on agents.md to persist this, and that's the memory write

[02:29] **Speaker**: After both invokes, the script prints the updated file so you can see the change directly in the terminal

[02:48] **Speaker 6**: So now you can see agents.md has been altered

[02:52] **Speaker**: This line was not there before, but now it's been added. Let's head over to LangSmith to take a look
