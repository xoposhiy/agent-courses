# Sandbox Security

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/tkngKY1GUnU) · [Raw file](../../raw/videos/tkngKY1GUnU.html)

Retrieved: 2026-11-13T16:57:39.558966+00:00

[00:01] **jess**: This lesson takes the Chinook sales assistant that we previously worked with and improves it

[00:06] **Speaker**: Instead of running agent-generated code directly on your machine, we move code execution into an isolated sandbox

[00:13] **Speaker**: and we hand off newsletter generation to an asynchronous subagent so the main agent isn't blocked waiting on it We're covering this because both patterns, sandboxing untrusted execution and offloading slow work to asynchronous subagents, are what allows deep agents to do more without becoming slower or less safe

[00:30] **Speaker**: to recap, we start on the host, and this is your machine or the server running the agent. So the agent lives here on the host, but when it needs to run code, like plotting a script, it doesn't run it locally. It sends it into a sandbox

[00:44] **Speaker**: And that's this execute path. Code goes from the agent into the sandbox and runs here instead of on the host. Inside the sandbox, the code executes in its own isolated environment. Meanwhile, the host keeps its secrets, such as the LLM API key. They keep it on its own side of the boundary, so the sandbox never sees them.

[01:05] **Speaker**: And that's the core idea. Sandboxes isolate code execution, so AI-generated code can run freely without putting the host at risk

[01:12] **Speaker**: But now say that sandbox code misbehaves and it crashes.

[01:16] **Speaker**: The damage is contained entirely inside the sandbox.  The host remains untouched. But notice, we still do have one concern. Whatever data comes back from the sandbox to the host still has to be trusted. And here's why that return path matters  Say the agent's plotting script is missing an argument

[01:35] **Speaker**: The sandbox sends back a real error, a TypeError with missing argument labels That comes back over standard error from the sandbox  to the agent, and the agent needs this.  Without seeing its own errors, it can't correct its code and retry. This error loop is essential to how coding agents work But look at where that error text originated from.

[01:55] **Speaker**: Inside the sandbox, the same insecure environment the agent's code is running in, and that's a vulnerability waiting to happen  Here it is The same standard error channel that carried a legitimate error can just as easily carry an injected instruction riding along with it. Here's a fake message asking for a Stripe API key Because the agent trusts this channel as its normal correction loop, it cannot tell the difference between a real error and one with a prompt injection stitched in.

[02:23] **Speaker**: If the agent reacted to that and reached for real credentials on the host to authenticate, those secrets could be exfiltrated straight out through the sandbox

[02:32] **Speaker**: So here's the fix. Instead of keeping the file system on the host, we move it inside the sandbox  The agent's code reads and writes files directly inside the sandbox. Critically, that file system only holds outputs, plots, and reports, no API keys and no secrets. There's nothing sensitive in there to leak, even if the sandbox is compromised

[02:53] **Speaker**: This breaks the agent's role as a bridge between a sensitive file system and an insecure execution environment  because now there's no sensitive file system on the other side of that bridge

[03:03] **Speaker**: To actually get a file, like a finished plot,  back out of the sandbox

[03:07] **Speaker**: download runs as a non-agentic path, a middleware hook that pulls the file out directly

[03:12] **Speaker**: And it lands in the host application, the chat UI, for you to download completely outside of the agent's tool calling loop And that's the full picture. Isolate execution, move the sensitive-free file system inside the boundary, and extract results through a path the agent itself never controls
