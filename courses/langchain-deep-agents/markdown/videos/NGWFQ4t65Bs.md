# Tools Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/NGWFQ4t65Bs) · [Raw file](../../raw/videos/NGWFQ4t65Bs.html)

Retrieved: 2026-11-13T16:57:37.561096+00:00

[00:00] **jess**: There are three things worth noting here  This is a convenience wrapper. It handles the SQLite connection and gives you a clean run method for executing queries without writing boilerplate SQLite 3 code.

[00:12] **Speaker**: Tool from LangChain core tools is the decorator that turns a regular Python function into something the model can call. You'll remember this from the lesson. It had that little "@"  And dbpath here just resolves the path to the Chinook database relative to the script so that everything works regardless of where you run it from.

[00:30] **Speaker**: here it does two things

[00:32] **Speaker**: it scopes it to its role, a SQL analyst that's read-only.  It's not allowed to modify the database  and only reads

[00:41] **Speaker**: And it gives the model an explicit rule to show its SQL in the final answer. This part isn't about capability, it's about observability. You want to see what query the agent actually ran, not just the result.  This rule,  if a tool returns an error,  revise the SQL and try again, is also doing real work.

[00:59] **Speaker**: Without it, some models would just report the error rather than actually self-correct

[01:04] **Speaker**: read_sql here is a regular Python function  with the tool decorator on top  The decorator reads the function name, type annotation, and docstring to build the tool schema the model sees.

[01:15] **Speaker**: The docstring here, " Run a read-only select query against the Chinook music store database," is what the model reads when it decides whether to reach for this tool. The implementation is deliberately minimal. Run the query, return the result as a string, and surface any exception as a string rather than crashing. This last part matters because the model can read an error message and revise its query.

[01:36] **Speaker**: It can't do anything with a Python exception

[01:39] **Speaker**: here we have our call,  and we've added readSQL to our tools

[01:43] **Speaker**: This doesn't replace anything. Now we have Read SQL alongside the built-in file system tools and Write Todos.

[01:51] **Speaker**: Now, this question being asked, "Which five genres have the most tracks?" gives the model enough context to decide it needs read SQL to write the SQL itself and to use the result to answer in natural language.  Let's run it

[02:06] **Speaker**: There we go. The five genres with the most tracks are rock, Latin, metal, alternative and punk, and jazz

[02:18] **Speaker**: And here's the SQL that it used
