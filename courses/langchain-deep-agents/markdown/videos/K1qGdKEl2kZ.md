# Lab 1 (LangSmith Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/K1qGdKEl2kZ) · [Raw file](../../raw/videos/K1qGdKEl2kZ.html)

Retrieved: 2026-11-13T16:57:37.261625+00:00

[00:01] **Speaker**: When you build with Deep Agents, a lot is happening under the hood,  and LangSmith lets you see all of that and understand this black box. So every time your application runs, LangSmith captures a trace,  which is the full record of what happens step by step from input to output.  Let's look at the trace for the Butler agent  On the left-hand side, this is what we call a run tree.

[00:22] **Speaker**: At the top, I can see the latency and a detailed breakdown of token usage. This is one of my favorite parts  because it gives you insight into where the tokens are being used. So this costs three point seven thousand tokens at zero point zero zero five one dollars.

[00:35] **Speaker**: Now, the stack of steps right here  is our middleware, and it's wrapping around the actual model call.  But we'll get back to that later. Let's look into the model call itself first

[00:47] **Speaker**: So this part here is our system prompt

[00:50] **Speaker**: Down here is our user request,  and this is that question we asked, "What is an LLM?" And our answer is down here in the output.  But first, let's take a look at the system prompt again

[01:02] **Speaker**: This defines the agent's behavior, and here we've assigned our agent the persona

[01:06] **Speaker**: of a posh British butler  Right below that persona is the suffix,  which is a short model-specific block covering things like  use parallel tool calls

[01:16] **Speaker**: Investigate before answering

[01:19] **Speaker**: and reflecting on tool results.  This isn't a persona or behavior prompt. It's just some tactical tool use guidance that Deep Agents appends automatically for Claude models

[01:29] **Speaker**: And the answer to our question, what is an LLM?

[01:33] **Speaker**: is answered with the butler persona.

[01:36] **Speaker**: And it has a lot of personality, as we can see here

[01:40] **Speaker**: I dare say
