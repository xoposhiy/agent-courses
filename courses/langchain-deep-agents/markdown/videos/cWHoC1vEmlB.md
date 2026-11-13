# Recursive Language Models (RLMs)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/cWHoC1vEmlB) · [Raw file](../../raw/videos/cWHoC1vEmlB.html)

Retrieved: 2026-11-13T16:57:38.283659+00:00

[00:01] **Speaker**: Deep Agents implements a documented technique called the recursive language model, or RLM.

[00:06] **Speaker**: Introduced by these MIT researchers  Now their core insight is that instead of a model treating a long context as one monolithic input, to split it into pieces, call each piece, and combine the results, recursing on any piece that's still too big to handle directly

[00:22] **Speaker**: So step one is the context splits into call A and call B,  each handling half

[00:28] **Speaker**: Then both results feed into a third call, C, which combines them.

[00:33] **Speaker**: If half is still too big to handle in one call, that call recurses the same way, splitting into A1 and A2.

[00:41] **Speaker**: A1 and A2 are small enough to answer directly now, so they combine into call A3

[00:47] **Speaker**: A3's result feeds back up into call C and the loop closes. And the recursion bottoms out. It doesn't split forever

[00:55] **Speaker**: Deep agent's dynamic subagents use that same  divide and conquer technique but dispatch full agents rather than recursing on the same model call. The team's more precise term for that

[01:05] **Speaker**: is recursive agents. RLM is the popular shorthand that you'll see used for the pattern generally. Now, the MIT paper reports RLMs handling inputs up to two orders of magnitude beyond a model's context window, with median gains on GPT-5 ranging from thirteen percent versus Claude Code to one hundred thirty percent versus Code Act with subcalls across four long context tasks.

[01:28] **Speaker**: We ran the Oolong long context benchmark ourselves against the interpreter-enabled agent from this lesson, and it agrees with the paper's direction at more than one context length

[01:37] **Speaker**: At 64,000 tokens, the score went from 0.58 without the interpreter to 0.67 with it.  At 128 tokens, it went from 0.44 to 0.79,  a much bigger gap.  So when should you use dynamic subagents versus a plain subagent team?

[01:56] **Speaker**: you'll want to reach for dynamic subagents  when the number of work units is large, fixed, or only known at runtime.  Think pages, rows, files, and transcripts

[02:04] **Speaker**: Or when you need a guarantee that every unit gets covered, not a best effort pass.  Or when orchestration itself is non-trivial.  Branching, parallel fan-out, or a pipeline shape the model would otherwise have to reconstruct every turn.  But you'll want to stick with an ordinary subagent team  when there's a small fixed number of specialized roles, like a researcher per genre, a reviewer, an analyst

[02:26] **Speaker**: and you're delegating by role, not fanning out over a large uniform collection of items.
