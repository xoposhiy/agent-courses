# Lab (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/CywMBDM59XU) · [Raw file](../../raw/videos/CywMBDM59XU.html)

Retrieved: 2026-11-13T16:57:36.548701+00:00

[00:01] **Speaker**: so we have one turn here. The whole interaction happened in a single invoke. Read, blocked, write, and final response.

[00:09] **Speaker**: Here's the user message going in.

[00:11] **Speaker**: Read the reference file, then add a promotion note to it. The agent will complete the first task but fail the second

[00:19] **Speaker**: So the model decides to read first

[00:22] **Speaker**: and then add the note

[00:24] **Speaker**: This is our first tool call

[00:25] **Speaker**: And the result comes back cleanly, the full file contents

[00:30] **Speaker**: Now for the promotion note It calls edit file And note that it chose editfile instead of writefile. It's doing a targeted patch on the existing content rather than overwriting the entire file.

[00:45] **Speaker**: But here we have the result, permission denied, that's the file system permission rule firing. The rule matches write operations on reference with mode deny.

[00:54] **Speaker**: It doesn't matter which write tool was used. edit_file is still a write operation, and the backend enforced it before the tool could touch the file

[01:03] **Speaker**: And here we have the model's final response. "I don't have write permissions for that file. It's read-only."

[01:09] **Speaker**: There were three model calls in total. Read, attempt to write and summarizing the failure.
