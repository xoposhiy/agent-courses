# Dynamic Subagents

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/u4S3dWlvLnJ) · [Raw file](../../raw/videos/u4S3dWlvLnJ.html)

Retrieved: 2026-11-13T16:57:39.604309+00:00

[00:00] **Speaker**: Previously, delegation meant that the model

[00:02] **Speaker**: called the task tool directly once per subagent.  So a genre researcher call for rock,  another for metal,  and a third for Latin.  And that works fine at this scale, since four genres is a short enough list for the model to enumerate and dispatch itself, even issuing all four as parallel tool calls within the same turn.

[00:20] **Speaker**: But now say the job is a thousand sales transcripts with the same task on every one, to summarize it. That's no longer a short list the model can enumerate in its head, and someone still has to keep track of which ones are done. If you leave that to the model, you've put the exact thing that breaks agents at scale

[00:34] **Speaker**: which is tracking state across a shrinking context window  back to the model. Now, if you leave this to the model,  in practice, it wouldn't just cleanly fail. Depending on the model, it would more likely just refuse outright, saying it cannot process that many in one pass, or try to chunk the work into rough ranges across subagent calls, or try to fire off everything in batches of roughly twenty calls at a time, since that's close to the practical ceiling on how many tool calls a model can issue in parallel

[01:00] **Speaker**: But none of these guarantee every transcript actually gets touched. Each still depends on the model, not the code, for getting the bookkeeping right.

[01:07] **Speaker**: And this is the problem programmatic orchestration solves. Instead of issuing subagent tasks through tool calls turn by turn, the model writes a short script that orchestrates and calls subagents itself, leaning on code patterns it already knows, looping, branching, concurrency, that sort of thing.

[01:24] **Speaker**: That script runs in a lightweight interpreter.  So here's the difference written as code, since that's really what's changing

[01:31] **Speaker**: This version has the model enumerating each transcript itself, one task call per turn, with nothing guaranteeing it actually reaches transcript one thousand.

[01:40] **Speaker**: The second version is a loop written once and run by code for transcript and transcripts and the task.

[01:46] **Speaker**: now task itself didn't change. It's the same subagent call either way. But what did change is where the decision to keep going lives. So in this version, it's in the model, however many calls that takes. In the second version, it's in code, run in an interpreter

[02:02] **Speaker**: Now, dynamic subagents is Deep Agent's name for that programmatic orchestration, subagents dispatched by code and not by the model, one turn at a time. That loop doesn't have to be a literal for loop like I showed earlier. It could be a map over a list, a parallel fan-out, or a branching pipeline. The only thing that matters is that it's a fixed shape written in code, not something the model has to reconstruct from memory on every turn

[02:24] **Speaker**: So this is what you've seen so far. A small fixed N and a main agent fanning out to four subagents at once in a single step. The model enumerating a short list itself. Now this is dynamic subagents. The main agent

[02:39] **Speaker**: writes a loop once, and that loop fans out to however many subagents there are. Could be N, could be 1,000, whatever it is Now, these are both doing the exact same jobs with the same fan-out pattern, but what is different is who enumerated the list. At four items, the model held that list itself. At a thousand, only code can reliably hold it, so the code keeps track instead of the model

[03:04] **Speaker**: And this shift  guarantees two properties  turn by turn delegation can

[03:08] **Speaker**: first is deterministic coverage at scale. A model deciding turn by turn whether it's covered everything can quietly stop at seventy-five of five hundred items and just call it done

[03:18] **Speaker**: a for batch in batches loop  doesn't have that option. It touches every batch

[03:22] **Speaker**: On a long context benchmark called Oolong, a plain agent at 128,000 tokens didn't just answer wrong.  It often gave up outright, reporting it couldn't compute the result

[03:32] **Speaker**: An interpreter-enabled agent on the same benchmark  did dramatically better, and we'll see the actual numbers later in this lesson.

[03:38] **Speaker**: Secondly, we have reliable complex orchestration. Writing orchestration as code is more reliable than having the model reproduce it as a sequence of tool calls, especially for fan-out and synthesize work, multi-phase pipelines, or conditional branching.

[03:51] **Speaker**: The pipeline can branch, run in parallel, or run sequentially, shaped however the task needs instead of being constrained to one tool call per model turn
