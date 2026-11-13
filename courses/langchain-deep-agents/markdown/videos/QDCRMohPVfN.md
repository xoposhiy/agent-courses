# Lab + Studio Walkthrough

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/QDCRMohPVfN) · [Raw file](../../raw/videos/QDCRMohPVfN.html)

Retrieved: 2026-11-13T16:57:37.727487+00:00

[00:00] **jess**: This lab is the first one in the course where the main agent talks to a subagent running as a completely separate deployment, not just a separate configuration in the same process.

[00:09] **Speaker**: Let's go through the files that make that happen  Starting with the deployment that's actually new. So this is the configuration file that tells langgraph dev how to serve this deployment, so what to install and which graph to expose. Every lab so far has had one of these.

[00:24] **Speaker**: This one's configured a little differently, though    every other lab's langgraph.json in this course pointed dependencies at the shared course environment. This one, however  points it here, its own directory. And that's the entire isolation mechanism. Just one line  Now, this is Specialise Agent's own dependency file, separate from the course's shared one.

[00:44] **Speaker**: Whatever's listed here only gets installed into this one deployment.  And here's the dependency list.  Deep Agents, LangGraph, LangChain Anthropic, LangGraph CLI

[00:53] **Speaker**: and pandas. And this is why the isolation from the previous file mattered  Pandas lives only here, never in the shared environment the other labs depend on   this is the agent actually running on the specialized deployment,  the one main agent will delegate to. It's a plain Deep Agent built around one tool and a small Pandas DataFrame

[01:13] **Speaker**: This is a small hard-coded sales DataFrame with six rows

[01:19] **Speaker**: Columns for region, product, units sold, and revenue

[01:23] **Speaker**: And this is the Analyze Sales tool

[01:26] **Speaker**: It takes one argument, group_by,  defaulting to region

[01:30] **Speaker**: Now this forces every call to analyze_sales to take at least twenty seconds, no matter how fast the actual Pandas grouping is. This delay simulates how long a full Pandas analysis over a real dataset would take. The six-row table I showed you above computes instantly.

[01:46] **Speaker**: So without this, every step in the lab would finish before there was anything left to interrupt or check on.

[01:51] **Speaker**: And this groups the six rows by whichever key was passed in. Region collapses them into three rows and product into two, with sum units sold and revenue within each group and sourced by revenue highest first.

[02:03] **Speaker**: That one parameter, region or product, is what lets the main agent kick off more than one independent analysis at the same time later  This deployment only installs its own directory, not the rest of the repo, so it can't reach the shared models.py the way main agent does.  It has to define its own model here instead

[02:24] **Speaker**: Now, this is a plain Deep Agent. Nothing async specific lives on this side at all. As far as this file's concerned, it's just answering tool calls.

[02:34] **Speaker**: Now, this is the agent you'll actually talk to in Studio. It doesn't run any analysis itself. Everything sales related gets handed off to the deployment we just looked at  So we import AsyncSubagent  and  create Deep Agent  from deepagents and model from the course's shared models.py.  Unlike that last file,  this agent doesn't set up its own model. It uses the same one every other lab uses

[02:58] **Speaker**: This is the subagents list with one entry on async subagent

[03:03] **Speaker**: The name is nlist   And the description field  doesn't just say what the subagent does, it explicitly bounds what it returns and tells the model to launch one task per grouping if it needs both regional and product breakdowns

[03:15] **Speaker**: The graph ID here is agent,       the address the second server will be running on  As you can see, there are no tools passed here at all. Main agent never imports pandas and never sees analyze_sales directly. Everything it knows about that capability comes through this one AsyncSubagentEntry

[03:41] **Speaker**: And this is the main agent's own configuration file, the counterpart  to that first file we looked at

[03:48] **Speaker**: It's the same structure but with different settings. dependencies here points to the shared environment, same as every other lab

[03:58] **Speaker**: Remember, this one pointed at just this

[04:02] **Speaker**: Same course environment on this side  fully isolated on this

[04:08] **Speaker**: Now let's run it          Both commands opened a browser tab each. This first tab here is what Specialized Agent opened up, and this is the specialized deployment on port 2025,  the one hosting the Analyze Sales tool, and it opened its own studio automatically as a side effect. We're going to focus on this tab here Because this is what main agent opened up, and it's the one that we actually talk to.

[04:38] **Speaker**: You can see that in the input panel there is an async tasks field, which only shows up because this agent has an async subagent wired in. Now let's open up the messages field.   We'll replace this empty list with this

[04:56] **Speaker**: So we're asking it to analyze sales by region and separately by product at the same time.

[05:01] **Speaker**: This is the main agent deciding what to do with our request

[05:05] **Speaker**: And now here are the two tool calls

[05:06] **Speaker**: that were fired from a single model turn, not two separate turns.

[05:12] **Speaker**: So we see the same tool, start async task, but this is for the regional breakdown

[05:18] **Speaker**: the task ID here

[05:19] **Speaker**: And the task ID here is different. So they're both start async tasks, but this  is for the regional breakdown, and this is for the product breakdown

[05:29] **Speaker**: This is the agent reporting back once both calls returned

[05:33] **Speaker**: And here we see those different task IDs, they're both handed back in seconds while the analyses are still running on the specialized agent server underneath.

[05:42] **Speaker**: let's ask another question

[05:47] **Speaker**: So we asked it, "What's twelve times eight?" And look how quickly the answer came back. The main agent isn't blocked waiting on either analysis. It's answering a completely unrelated question while both jobs are still running underneath.

[05:59] **Speaker**: Now let's change our mind.  Now we want to narrow the regional analysis to just the West region

[06:09] **Speaker**: Now we can see we called update async task, not start async task  This has the same task ID  as the one from step one

[06:20] **Speaker**: So under the hood, this interrupts whatever's currently sitting in that run's sleep and starts a fresh run on the same thread with the new instruction attached.

[06:29] **Speaker**: Now let's cancel something

[06:37] **Speaker**: Here we see cancel_async_task

[06:39] **Speaker**: called on the product task's ID specifically.  Finally

[06:46] **Speaker**: Let's get a status update

[06:53] **Speaker**: Here we see that fifth tool call list_async_tasks

[06:59] **Speaker**: and it came back with just the West region.  And we canceled the product analysis
