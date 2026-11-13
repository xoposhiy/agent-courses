# Tools Lab (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/h1InaofLToI) · [Raw file](../../raw/videos/h1InaofLToI.html)

Retrieved: 2026-11-13T16:57:38.480567+00:00

[00:02] **Speaker**: This is what we just ran

[00:04] **Speaker**: You'll see that there are one,  two,  three,  and four model calls. Now, that seems like a lot, but I'll explain what happened. Let's start with the first

[00:18] **Speaker**: So under the Tools tab, we can see Read SQL here, and it was called

[00:22] **Speaker**: The model was given the description text from the docstring, the parameter name query, the type string, and required. This is the complete schema, and that's what it used to decide ReadSQL was the right tool.

[00:34] **Speaker**: It wrote SQL using from genres g, but this is the wrong table name. The Chinook database uses genre with a capital G here. The model didn't know the schema, so it just guessed Let's look at the first ReadSQL node.

[00:54] **Speaker**: There we go  No such table.  But this didn't crash anything. The error was wrapped in a tool message and appended to the conversation. I'll show you in the next model call

[01:07] **Speaker**: So this error message was now put into the input. And if we look at the output

[01:13] **Speaker**: It now checks for the correct table names instead of guessing a different name.

[01:17] **Speaker**: It runs select name from sqlite_master where table equals table, which is a query against SQLite's built-in metadata table that lists everything in the database.  Let's take a look

[01:29] **Speaker**: right here in the output The result came back with all 11 table names.  Genre is right here  with that capital G.  Let's go into the third model call

[01:39] **Speaker**: Where we can see in the input,  it sees this entire list

[01:44] **Speaker**: Everything is in the input

[01:46] **Speaker**: Now in the output

[01:48] **Speaker**: It rewrites the SQL  using the correct genre and calls read_sql again

[01:54] **Speaker**: It only took 1.06 seconds, which is the shortest of the four calls because the model had what it needed and didn't have to reason through uncertainty

[02:04] **Speaker**: Let's look at the third Read SQL node

[02:07] **Speaker**: And we can see the corrected query worked. Results are back. Now, this fourth call

[02:13] **Speaker**: includes that answer.

[02:15] **Speaker**: It received these results as a ToolMessage.

[02:19] **Speaker**: and turned them into a clean final answer. So there were four model calls with two failed attempts, one schema lookup, one correct query. Now, none of this was visible to the user. We just saw our one response with the right answer, and if it weren't for LangSmith, we wouldn't know that all of this was going on behind the scenes.
