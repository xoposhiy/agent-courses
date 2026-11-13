# Offloading

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/DBjUzgBYFJG) · [Raw file](../../raw/videos/DBjUzgBYFJG.html)

Retrieved: 2026-11-13T16:57:36.590234+00:00

[00:00] **Speaker**: summarization handles gradual accumulation across turns, but there's a different problem. A single tool call that returns an enormous result, a full database export, hundreds of search matches, a long generated file, could be anything. That would spike the token count in one shot before summarization even gets the chance to act.

[00:18] **Speaker**: When a tool result exceeds roughly twenty thousand tokens  File system middleware automatically intercepts it. It writes the full result

[00:25] **Speaker**: to large tool results on the agent's file system and replaces  the inline message  with a short preview    and a file reference

[00:33] **Speaker**: So instead of the full result, the model sees this

[00:36] **Speaker**: It's told the result was too large  and where it was saved.

[00:40] **Speaker**: It's told it can use readfile to retrieve it  but to only read part of the result at a time.

[00:44] **Speaker**: and it gets a head and tail preview,  the first five  and last five lines, so it has enough context to know what the result contains before deciding how to proceed

[00:55] **Speaker**: The file system tools themselves are excluded. They either have their own built-in truncation, return minimal confirmation text, or in the case of readfile  Offloading it would defeat the purpose.

[01:07] **Speaker**: the same mechanism applies when a user message is very large    For example, pasting in a long document or transcript. When a human message exceeds roughly fifty thousand tokens

[01:17] **Speaker**: File system middleware writes the full text  to conversation history and replaces it with a preview and file reference

[01:24] **Speaker**: what the agent sees is identical to a tool result.

[01:27] **Speaker**: Only the threshold  and the storage location differ
