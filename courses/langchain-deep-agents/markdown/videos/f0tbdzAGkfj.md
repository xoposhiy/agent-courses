# Lab 1 (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/f0tbdzAGkfj) · [Raw file](../../raw/videos/f0tbdzAGkfj.html)

Retrieved: 2026-11-13T16:57:38.443628+00:00

[00:00] **Speaker**: So this run took about two seconds and 19,000 tokens. If we compare that to the sandbox run, almost 12 seconds and 34,000 tokens No writefile, no execute, and no retries.

[00:15] **Speaker**: It's the same pattern as skills middleware from the skills lab. The middleware runs before the agent and injects the eval tool and its instructions into the system prompt Here we had one tool call initialize an array, iterate 15 times, and push each value. The code ran inside the embedded QuickJS runtime, not in a shell, not in a sandbox

[00:38] **Speaker**: The result came straight back as the array. One tool call, the correct output, and done CodeInterpreterMiddleware right here means that the middleware also runs a cleanup step after the agent finishes.
