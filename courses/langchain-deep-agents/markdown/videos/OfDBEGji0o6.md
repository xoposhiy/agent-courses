# Lab 1 (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/OfDBEGji0o6) · [Raw file](../../raw/videos/OfDBEGji0o6.html)

Retrieved: 2026-11-13T16:57:37.656005+00:00

[00:00] **jess**: In our run, there were three tool steps, write file, the first execute, and the second execute. Let's look at the first call

[00:11] **Speaker**: So our first tool call was writefile, and the agent wrote the Fibonacci script in fib.py in the sandbox before trying to run anything. That's the system prompt doing its job

[00:23] **Speaker**: Now let's look at the first execute call

[00:26] **Speaker**: The second tool call was to execute  fib.py and the result   came back as an error   command not found. The sandbox doesn't have a Python alias, only Python 3. So this is the self-correction loop in action. The agent got a real error from the shell, read it, and then tried again

[00:46] **Speaker**: Which is why we have the second execute call and the third tool call.  the third tool call was to execute Python 3 slash fib.py.  This time,  it succeeded.  The full sequence of fifteen Fibonacci numbers came back in the tool result, and the agent included them in its final answer. So that's the whole  write,  execute and error, retry, and then success loop. The sandbox made it safe to run these shell commands in isolation.
