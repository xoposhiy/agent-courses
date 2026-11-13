# Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/WxjRmqB2NMI) · [Raw file](../../raw/videos/WxjRmqB2NMI.html)

Retrieved: 2026-11-13T16:57:38.014990+00:00

[00:01] **jess**: manuscript_agent.py defines the agent for the lab, where a mischievous editor spliced a couple strange sentences into a combined public domain translation of the Iliad, Odyssey, and Aeneid. There's sixty books, about two megabytes of text, and the job is to find every single one of those strange lines.

[00:21] **Speaker**: Here are our imports, and there's nothing unusual here except for models, where we import StrongModel   Here, that means we use sonnet instead of our cheaper model haiku.

[00:34] **Speaker**: I'll go back to this in a minute

[00:36] **Speaker**: This line just means that data_directory points at the data folder sitting next to this file, and that's where the corpus and the answer key live.

[00:44] **Speaker**: The answer key is how you'll check to see if you got all of the weird sentences that we added into this lab

[00:50] **Speaker**: This is the system prompt for the subagent that actually reads a single book. It's scoped to proofreading one book, flagging anachronistic sentences, returning them as a JSON array quoted verbatim, and to return an empty list if there's nothing. this last instruction here, "Most books have none. Don't force a match,"  is important. Without it, a model under pressure to find something tends to flag ordinary old-fashioned phrasing as something suspicious instead of the ones that we actually planted there.  This is the book_scanner subagent spec itself

[01:21] **Speaker**: We have the name  and the description

[01:24] **Speaker**: And this is what the main agent sees when deciding which subagent to dispatch to. Same shape as any other subagent configuration that we learned about in earlier modules.

[01:32] **Speaker**: But you'll see here we set model to model, not strong model, but our cheaper one of Haiku 4.5 This call runs up to 60 times  And it's a narrow repeated task where you want to use a cheaper model instead of the more complex one.

[01:49] **Speaker**: Now, this is our main agent system prompt, and here are a few things worth noticing

[01:54] **Speaker**: First, it tells the agent exactly where the file lives and how it's structured.

[01:58] **Speaker**: split into 60 books

[02:00] **Speaker**: with each starting with a line formatted like this

[02:03] **Speaker**: And it tells it to run a workflow that reads the manuscript. " And never read a book's full text into your own context."  Now, workflow here is important  because it's what triggers dynamic subagent dispatch, like we covered in the lesson earlier. Then it tells the agent to batch 30 books per Promise.all round instead of the smaller batch size shown in the interpreter's own tool guidance. Two rounds total instead of six. Now, we do this deliberately because the framework's example code defaults to batches of ten out of caution.

[02:31] **Speaker**: But this workload comfortably fits under the interpreter's hard concurrency cap, and bigger batches mean less time spent waiting on sequential rounds.

[02:39] **Speaker**: finally, it tells the agent to let the interpreter hold the file  and let each subagent hold only its own book

[02:45] **Speaker**: then to collect every subagent's findings into one grouped report. And the corpus itself never touches the main model's context. Only each scanner's short list of findings does.

[02:55] **Speaker**: Here we have two file system permission rules, and the order matters here since rules are evaluated top to bottom.

[03:02] **Speaker**: This first rule allows read on exactly this

[03:07] **Speaker**: The second rule  denies  both read and write  on everything

[03:13] **Speaker**: So together, that's a read-only allowlist of one single file. The agent can read the manuscript

[03:19] **Speaker**: And nothing else. No rights anywhere

[03:23] **Speaker**: Then finally, we have create_deep_agent itself

[03:26] **Speaker**: Here we want the strong model so that the main agent, which is the one orchestrating and reasoning about how to split the work,  run on sonnet while the subagent doing the repetitive scanning runs on haiku The middleware here is what makes the line in the prompt, " The interpreter holds the file," true.

[03:43] **Speaker**: PTC bridges the agent's already configured readfile and grep tools directly into the JS sandbox as tools.readfile and tools.grep. That means the workflow code the model writes can call those functions itself  inside the interpreter to load and split the manuscript,

[03:58] **Speaker**: So the two-megabyte file never has to pass through the main model as a message. Without PTC here, the sandbox would have no way to touch the file system at all

[04:07] **Speaker**: Then we have the subagents book scanner to register the one subagent type

[04:12] **Speaker**: This backend here is what makes epic corpus.txt in the prompt actually resolve

[04:17] **Speaker**: Assigning virtual_mode true anchors every path the agent sees

[04:21] **Speaker**: to this as a virtual route

[04:23] **Speaker**: And combined with the permissions rule, that's a real enforced restriction. The agent can only read that one file and cannot write anywhere. Now let's take a look at run_manuscript.py

[04:34] **Speaker**: This is the short script that actually kicks off a run and grades it against a known answer key.

[04:40] **Speaker**: Here are our imports  And we've imported the agent that we were just looking at

[04:47] **Speaker**: Here we have the same data directory pattern as before, pointing at the local data folder

[04:52] **Speaker**: Now here's the actual invocation

[04:54] **Speaker**: With our user message,  run a workflow to find every corrupted sentence in the manuscript.  Workflow here is doing the same job here as it did in the system prompt, reinforcing that this should be dispatched as code-based orchestration rather than delegated turn by turn.

[05:09] **Speaker**: Now here

[05:10] **Speaker**: We set the recursion limit to 200. So this run dispatches roughly 60 subagent calls plus the orchestration steps around them.  200 gives it room to actually finish  and this just pulls the final content out as a report so that we can actually read it this is a self-check

[05:26] **Speaker**: It loads this answer key

[05:28] **Speaker**: And found_sentences is just a substring check. So for each seeded sentence, is it present verbatim somewhere in the report text?

[05:36] **Speaker**: Missed is whatever's in the key but not in the report,

[05:39] **Speaker**: the model sometimes flags a genuinely odd-sounding phrase from the real nineteenth century translations as a false positive, so the raw total count in the report can come out above fourteen. The orchestration itself, splitting the manuscript and dispatching one scanner call per book, is deterministic code the main agent writes once. What can vary between runs is whether an individual scanner call catches the one sentence planted in its book.

[06:03] **Speaker**: So this is sometimes an ordinary model recall limit on a detection task, not a gap in the workflow and not a sign that we've done something wrong.

[06:15] **Speaker**: There we go

[06:16] **Speaker**: so 14 corrupted sentences were found, which is exactly what we left for you to find

[06:21] **Speaker**: A vending machine did not exist back then,  nor a smartwatch  or a bronze pager

[06:27] **Speaker**: google Maps, and so on and so forth. So these are all the strange little sentences that we left for you to find. And if you run this lab, don't worry about it taking a while. It may take up to five, potentially ten minutes, but it should not take longer than that
