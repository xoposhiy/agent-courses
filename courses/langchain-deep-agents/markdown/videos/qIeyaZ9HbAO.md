# Interpreters

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/qIeyaZ9HbAO) · [Raw file](../../raw/videos/qIeyaZ9HbAO.html)

Retrieved: 2026-11-13T16:57:39.462072+00:00

[00:00] **Speaker**: All righty.  You learned about shell-capable backends,  which are environments where the agent can use execute to run commands, scripts, installs, and tests

[00:11] **Speaker**: interpreters are a lighter weight code execution option. They embed a JavaScript runtime directly in the agent loop, so no cloud infrastructure  and no API calls to spin up a shell environment. The trade-off  is a narrower direct capability set. JavaScript standard library only. No external packages, no direct file system, no direct network.  The word direct matters, and we'll come back to it So you probably remember this diagram, but the client sends a request to the LLM, which then generates a code block and sends it to the interpreter. The interpreter executes it, and the final result comes back to the LLM. Then the LLM sends its final response to the client

[00:53] **Speaker**: Notice that there's no external service in this chain. Unlike shell-capable backends, the interpreter is not a backend at all. It operates in the agent loop like any other tool. That's what embedded means. The JavaScript runtime lives inside the same Python process

[01:11] **Speaker**: When CodeInterpreterMiddleware is added to an agent, it provides a single new tool  eval. The agent calls it with a string of JavaScript, and here it's computing an average price. It reduces a list of prices, formats the result, and returns the last expression as a string

[01:27] **Speaker**: That string comes back as the tool result on the next LLM call. It's the result of the last expression, not a return statement, and the code block is more like a script than a function

[01:40] **Speaker**: The runtime is QuickJS, a lightweight embedded JavaScript engine

[01:44] **Speaker**: available are all the standard array methods along with all of this  What's not available, directly at least

[01:51] **Speaker**: file system

[01:53] **Speaker**: Fetch

[01:53] **Speaker**: Node.js APIs

[01:55] **Speaker**: NPM packages. Directly is the qualifier

[01:59] **Speaker**: With program-- with programmatic tool calling, JavaScript can still reach outside the interpreter through tools you explicitly allow, and that allow list is the safety boundary. So it's not that the interpreter is completely isolated, it's that nothing is reachable unless you deliberately expose it
