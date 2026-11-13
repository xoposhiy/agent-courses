# Programmatic Tool Calling (PTC)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/ma8zcRLkFWk) · [Raw file](../../raw/videos/ma8zcRLkFWk.html)

Retrieved: 2026-11-13T16:57:39.035017+00:00

[00:01] **jess**: There are three patterns where interpreters shine.  The first is data transformation

[00:06] **Speaker**: When the agent has data and context and needs to sort, group, aggregate, or reformat it, eval is faster and more reliable than asking the LLM to do arithmetic in prose. Here, the agent finds the best month from a list of invoices using Reduce

[00:21] **Speaker**: One eval call, one result back to the LLM. The reason this matters is because LLMs are good at deciding what to compute, but unreliable at actually doing it. Eval hands computation to code, which is what code is for

[00:35] **Speaker**: The second pattern is the most powerful, programmatic tool calling or PTC. When PTC is enabled, JavaScript code can call the agent's tools directly without intermediate results ever entering the LLM's context window.

[00:48] **Speaker**: So without PTC

[00:50] **Speaker**: Each tool result is returned to the LLM as a new message. The LLM has to examine it and decide on the next call, incurring latency and token costs with every turn. If you're chaining three queries where each result feeds the next, that's a minimum of three separate LLM turns.

[01:05] **Speaker**: Now with PTC, the LLM writes the JavaScript once. The interpreter handles the chaining internally, and only the final result crosses back to the LLM. One turn total.  here's what that looks like in practice. There are three calls

[01:20] **Speaker**: To query Chinook

[01:23] **Speaker**: that's how Python tools are exposed inside eval, as tools. Each result comes back as a string

[01:29] **Speaker**: So JSON.parse unwraps it into a JavaScript object.  The intermediate result sets are just local variables

[01:38] **Speaker**: Only this string at the very bottom gets returned to the LLM. Three intermediate result sets never become the messages. And one important constraint

[01:48] **Speaker**: Only tools explicitly listed in the ptc argument are callable from JavaScript. Keep that allowlist narrow.

[01:55] **Speaker**: If you put something broad in there, you've given LLM-written code direct access to it

[02:01] **Speaker**: this table is for quick comparison.  For the interpreter,  JavaScript via QuickJS.  It's embedded in the agent process

[02:08] **Speaker**: with no direct file system  or network  State persists within the thread  and it's best for computation, loops, and PTC orchestration.

[02:18] **Speaker**: Now shell-capable backends and sandboxes

[02:21] **Speaker**: uses any shell command or installed runtime

[02:24] **Speaker**: has full file system  and network access,  depending on configuration

[02:28] **Speaker**: And packages are available in the environment

[02:31] **Speaker**: It's best for scripts, packages, file input/output, builds, tests, and arbitrary shell work . The rule of thumb the page gives us is to use the interpreter  for logic and orchestration  and a shell-capable backend when you need packages or file input/output from code

[02:49] **Speaker**: Configuration is one line

[02:52] **Speaker**: Add code interpreter middleware

[02:53] **Speaker**: to middleware. To enable PTC, pass the list of allowed tool names to PTC

[02:59] **Speaker**: the middleware injects the eval tool and adds instructions to the system prompt automatically, describing how to use it and which tools are available via PTC.
