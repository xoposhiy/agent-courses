# Patterns

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/w4fw6n6CPp4) · [Raw file](../../raw/videos/w4fw6n6CPp4.html)

Retrieved: 2026-11-13T16:57:39.718778+00:00

[00:00] **Speaker**: Only workflow is actually configured. In a prompt, that word flips on a single instruction.  write dispatch code instead of delegating one call at a time. Everything past that point is the model writing ordinary code, and whether it ends up by branching by category, fanning out in parallel, looping until nothing new turns up, or running an elimination bracket depends on how the model reasons about the shape of the task while it writes the script

[00:24] **Speaker**: and that reasoning tends to settle into a handful of recognizable shapes.

[00:28] **Speaker**: Mixed type inputs often lead to a branch, like a folder with both PDFs and spreadsheets, where the script checks each file's type and routes it differently

[00:36] **Speaker**: A pile of uniform items often leads to a parallel map, like 60 book files that all need the same scan dispatches one call per file.

[00:44] **Speaker**: An open-ended search often leads to a loop, like querying a database repeatedly, stopping only once a query returns no new results

[00:52] **Speaker**: And the model picks the shape fresh each time it writes the script, not from a fixed rule. So the same task can occasionally come out differently between runs.

[01:00] **Speaker**: for more consistent results than relying on the model's own reasoning, steer it directly.

[01:05] **Speaker**: Describe the orchestration shape you want in the system prompt or bundle a worked example into a skill, which is a worked orchestration example the model reads before writing its own.

[01:13] **Speaker**: The model still writes the script itself. It's just working from a pattern that you've handed it instead of one it has to invent from scratch.

[01:20] **Speaker**: So this table lists some patterns as a dropdown

[01:23] **Speaker**: And these are common outcomes of that reasoning, not configuration options that you set anywhere.   For classify and act, you route each item to a specialist by type. It's good for triaging support tickets, error logs, or user feedback. Essentially, any batch of items that needs different handling depending on their type. You configure a sub-agent per role, say, a bug fixer or a feature analyst and a support agent And the model writes code that maps each ticket's category to the right subagent type and dispatches them in parallel.

[01:54] **Speaker**: Here's the code you configure and what the agent writes

[01:58] **Speaker**: For fanout and synthesize, it's the same work across many items in parallel and then combined. It's good for code reviews across a directory, analyzing a batch of documents, or running the same check across many services. You configure one reviewer per subagent, and the model globs the files, dispatches one review call per file, and flattens the result into a single list

[02:19] **Speaker**: for adversarial verification,  you find then independently verify before keeping. It's good for security audits or compliance checks. Anywhere a false positive is costly enough to be worth a second independent pass. One reviewer subagent produces findings

[02:35] **Speaker**: Then each individual finding fans out to its own verifier call, and only the confirmed findings survive.

[02:43] **Speaker**: For generate and filter, you produce several options,  then score them and keep the best. It's good for exploring an idea space where the first attempt might not be the best one Drafting titles, proposing fixes, or brainstorming approaches. Anywhere it's cheaper to generate a few options and score them than to get the right one on the first try. Generator subagents produce the candidates in parallel, and a scorer subagent scores each one. You keep whatever clears your threshold

[03:10] **Speaker**: Now, tournament is head-to-head judging with winners advancing. It's good for picking the best of several candidates when you can't score them independently, and you only compare two at a time.

[03:20] **Speaker**: This is good for style rewrites, competing implementations, or anywhere the criteria is subjective. Writer subagents produce candidates. A judge subagent compares two at a time, and the bracket collapses round by round to one winner

[03:34] **Speaker**: For loop_until_done, you repeat passes until one turns up nothing new. Good for open-ended discovery when you don't know the scope upfront, like finding every bug in a code base or every mention of a topic across a wiki. Anywhere "keep looking" is a better instruction than "look n times". A finder subagent runs pass after pass, and the script tracks what's already been seen and stops once a couple of consecutive passes come back dry.
