# Lab 2 (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/xuBB1zLLUm7) · [Raw file](../../raw/videos/xuBB1zLLUm7.html)

Retrieved: 2026-11-13T16:57:39.872312+00:00

[00:00] **Speaker**: We have two runs here. The one at the top is agent without, so no interpreter, and this one has the interpreter.  Let's look at agent without first  so this is a model call and this is a tool call. You've seen these before. And there are five model calls here. One,  two,  three,  four,  and five Each one is the LLM calling Query Chinook once, reading the result, then deciding what to ask next.

[00:27] **Speaker**: There are five round trips because we had four queries, and then here's our final answer  Let's look at the one with the interpreter

[00:38] **Speaker**: Here we have one model call and then tools with a single eval node and nested inside it, query Chinook fires four times in a sequence. This is the PTC bridge. Four database calls chained together inside one tool call, and then one more model call for the final answer. But two round trips total It was the same task with the same final numbers and answers in both, as we saw in the terminal in the previous video,  both agents get it right,  but the difference is what happened in between. Without the interpreter  Every intermediate result, the artist row, the album row, the track row, became a message the model had to stop and read before it could ask the next question

[01:19] **Speaker**: with the interpreter, these intermediate results stayed inside the eval call as JavaScript variables and never triggered a context switch back to the model.
