# Context Isolation + Sync & Async

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/enqK0nl3XXy) · [Raw file](../../raw/videos/enqK0nl3XXy.html)

Retrieved: 2026-11-13T16:57:38.393128+00:00

[00:00] **Speaker**: Let's look more closely at what actually happens at the handoff boundary between the main agent and a subagent, because this is what makes subagents a context engineering tool  on the left, the main agent has accumulated a long message history across many turns. On the right, the subagent starts with completely fresh context. When the main agent delegates, one message crosses the boundary, the task assignment.

[00:23] **Speaker**: The subagent does not inherit the main agent's history. It just gets its assignment. The subagent then runs autonomously, taking as many steps as it needs, using its own tools, making its own LLM calls until the task is done. Then one message comes back, its final result. There's no back and forth with the main agent mid-task.

[00:43] **Speaker**: One in, one out

[00:46] **Speaker**: There are three things to notice here

[00:48] **Speaker**: First, the subagent gets one message describing its task and nothing else. No history, no accumulated context. It starts fresh every time.

[00:58] **Speaker**: Secondly, the subagent defines its own tool set. Think about a database expert with dozens of specialized tools. Putting those behind a subagent means every one of those tool descriptions stays out of the main agent's context it sends the task and gets back an answer.

[01:13] **Speaker**: Thirdly, the key payoff. A large messy subtask gets compressed into a single clean result. As long as the subagent is told to return a concise summary, none of its internal steps or tool calls land in the main agent's context

[01:26] **Speaker**: The main agent stays focused on coordination even as the work accumulates behind the scenes.

[01:34] **Speaker**: subagents can run in two modes, and the choice comes down to one question.   Does the main agent need the result before it can keep going? In synchronous mode, the main agent blocks and waits until the subagent is finished It's the simpler model, but the conversation pauses while the work happens.

[01:52] **Speaker**: In asynchronous mode, the subagent runs in the background, and the main agent launches the job, stays responsive, and checks back later to collect the result. This course uses synchronous subagents in the hands-on lab. Asynchronous subagents are for production and background workflows where the main agent should stay responsive while longer work continues elsewhere.

[02:14] **Speaker**: A quick guide for when to actually reach for a subagent  you should use a subagent when

[02:18] **Speaker**: A multi-step task would otherwise clutter the main agent's context.

[02:22] **Speaker**: when the work needs specialized tools or instructions  When a subtask is better served by a different model  Or when you want the main agent to stay focused on high-level coordination.  You should skip using a subagent when  The task is simple and a single step.  The overhead just isn't worth it.  Or when you actually need to preserve the intermediate context rather than just the final result
