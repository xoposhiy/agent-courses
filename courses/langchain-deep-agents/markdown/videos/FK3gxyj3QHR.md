# Lab 1 [Sandbox Agent]

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/FK3gxyj3QHR) · [Raw file](../../raw/videos/FK3gxyj3QHR.html)

Retrieved: 2026-11-13T16:57:36.973935+00:00

[00:00] **Speaker 3**: This lab uses a LangSmith sandbox,  so these commands run in an isolated environment, not on your local machine

[00:08] **Speaker**: These lines provision the sandbox

[00:10] **Speaker**: Sandbox client connects to LangSmith Sandbox service

[00:14] **Speaker**: And create_sandbox spins up a fresh isolated workspace with a unique name

[00:18] **Speaker**: This random hex suffix means no collision if you run this multiple times.

[00:23] **Speaker**: Then LangSmith Sandbox wraps up that sandbox as a backend that the agent can use This is the same backend slot that we've seen before, just a different implementation. The agent sees the same file system tools plus execute. It has no idea whether it's talking to a local file, AgentState, or remote sandbox

[00:42] **Speaker**: The agent is wired up the usual way  model  Backend   and system prompt. The system prompt adds one instruction that matters here

[00:51] **Speaker**: Write the script  to a file first

[00:54] **Speaker**: then execute it. This primes the agent to do writefile before execute rather than trying to run code inline

[01:00] **Speaker**: The invoke is inside a try finally block

[01:07] **Speaker**: This  line always runs, even if the agent raises. That's because sandboxes are billed resources, and if you don't delete them, they keep running. This finally  guarantees cleanup regardless of what happens.

[01:19] **Speaker**: Now here we print the last message, which will be the agent's final answer, including the script output        here we can see the sandbox name and ID printed first, and then the agent ran with the results

[01:36] **Speaker**: So the agent wrote the script to the sandbox file system, ran it, got stdout back as a tool result, and included it in the final answer

[01:47] **Speaker**: The reason execute is available here is this backend. StateBackend and FileSystemBackend don't have it. LangSmith Sandbox does. If you swap the backend, you change what tools the agent has, and everything else in the agent stays the same
