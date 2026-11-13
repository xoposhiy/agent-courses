# Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/dWsX1UbejTZ) · [Raw file](../../raw/videos/dWsX1UbejTZ.html)

Retrieved: 2026-11-13T16:57:38.335581+00:00

[00:01] **Speaker**: Before you start  Check that your API keys are properly set up in your environment file  And if you kicked off langgraph dev in the previous lesson, you'll want to terminate that now

[00:11] **Speaker**: We're going to be running inside the Python M5 sales assistant directory, and this is how you kick it off.

[00:21] **Speaker**: So this will kick off the mail server and langgraph dev.  Now we have Studio. But we're gonna use the chat user interface

[00:31] **Speaker**: This is a ready-made chat interface with no install required.

[00:36] **Speaker**: Everything's been set up, but if this is missing, just remember to add your LangSmith API key

[00:45] **Speaker**: All right. Our agent's ready to go. Let's ask it some questions

[00:50] **Speaker**: we've already prepared some questions here that you can try, but you can ask any questions that are appropriate for a sales assistant

[00:56] **Speaker**: Let's ask it to check the inbox for any quote requests and then process them  We can hide the tool calls, but seeing them gives you a better insight into what's happening behind the scenes  You can see some write_todos happening as the agent is tracking what it's doing

[01:10] **Speaker**: So it's found mail. It's looking for an RFQ

[01:14] **Speaker**: And it's writing more to-dos.

[01:18] **Speaker**: Great. So it checked the Chinook database  And now it's asking for approval to add a customer to the database.

[01:27] **Speaker**: Since we approved that, it's going to create a mail draft

[01:34] **Speaker**: And here's our mail draft

[01:37] **Speaker**: We'll approve that

[01:39] **Speaker**: And now the draft has been saved.

[01:42] **Speaker**: And here's a quick summary. If we want to get rid of all those messy tool calls We can just hide it. But here we have our summary this is just an example of using Deep Agents.  You could easily modify this for your own applications,  change the playbooks, change the database. We really just intended this to be a template for your own projects.
