# Lab 1 [Fib with eval]

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/wSwgLsOL9uy) · [Raw file](../../raw/videos/wSwgLsOL9uy.html)

Retrieved: 2026-11-13T16:57:39.770641+00:00

[00:00] **Speaker**: This lab has the same task as Lab One in the previous lesson on sandboxes, to compute the first fifteen Fibonacci numbers, but the code is different. In the sandbox lab, we had sandbox provisioning, a try finally, file uploads, backend configuration, and here the whole thing is nine lines.

[00:19] **Speaker**: Super short

[00:22] **Speaker**: One line adds the interpreter

[00:25] **Speaker**: Code Interpreter middleware embeds a QuickJS JavaScript runtime directly in the agent loop and injects a single new tool, eval. There's no cloud environment, no sandbox to spin up, no writefile to execute sequence. The runtime runs in process

[00:41] **Speaker**: The user message explicitly asks for the eval tool

[00:44] **Speaker**: And this is intentional. It tells the agent

[00:48] **Speaker**: To compute the answer rather than just write out the numbers from memory      There we go. We have the first 15 Fibonacci numbers     the trade-off versus the sandbox is scope. Qwik JS gives you the JavaScript standard library, which includes array methods, map, JSON, math, promise. There's no packages, no file system, and no network. For pure computation like this, that's all you need, and the simplicity shows in the code.
