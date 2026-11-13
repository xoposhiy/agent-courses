# Prompt Caching

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/JMJNrFWTAdd) · [Raw file](../../raw/videos/JMJNrFWTAdd.html)

Retrieved: 2026-11-13T16:57:37.119994+00:00

[00:01] **Speaker**: So prompt caching is what makes agent loops cheap to run in production, and the idea is pretty simple. You reuse the work you already did on a prompt instead of paying to reprocess the same tokens every single turn.  Agent loops are an ideal case for this because the system prompt and tool definitions rarely change between turns. A big chunk of every request is identical to the request before it

[00:22] **Speaker**: so here's turn one,  the very first request. We have the prompt stack here with system prompt, tools, and skills at around five thousand two hundred tokens, with another three tokens with this new message, "Good morning." So nothing here has been cached yet. It's a completely fresh request. And because there's nothing to reuse, given that this is our first turn, every token gets charged at the regular rate, the full five thousand two hundred token stack, along with the additional three tokens 'cause of good morning.

[00:48] **Speaker**: This is the only time this stack is ever at a full price, billed at a hundred percent cost.

[00:53] **Speaker**: Right after that response comes back, the provider takes a snapshot

[00:57] **Speaker**: This entire prefix, the system prompt, the tools, the skills, and now also the good morning message, it gets tagged "cached" and stored, ready to be reused on a future call    And for turn two, we have a new message. " What's the weather?" This is another three tokens. But look at what's right above it  The same 5,203 tokens from before are already sitting in the cache from that snapshot.

[01:19] **Speaker**: So here's the payoff.  This cached block, all 5,203 tokens, gets billed at just 10% of cost because it's read from the cache instead of reprocessed. Only the new message, " What's the weather?" which are three fresh tokens, gets billed at full price, the exact same way good morning was back in turn one. And that's the whole mechanism.

[01:40] **Speaker**: Cache the boring repeated part that we've already seen and pay full price only for what's new

[01:46] **Speaker**: Now, Deep Agents doesn't leave this up to you to wire up.  The harness makes a best effort attempt at prompt caching automatically in three ways.

[01:53] **Speaker**: It sets explicit cache breakpoints when the provider supports them

[01:58] **Speaker**: It opts into provider-side implicit caching when explicit breakpoints aren't available  And it structures your prompt to maximize cache reads in general. So first, what is a cache breakpoint?

[02:09] **Speaker**: A cache breakpoint is just a marker placed at a specific point in a request that tells the provider, " Cache everything up to here." Without one, a provider can only cache automatically, usually by matching the longest prefix two requests share, which gives you a lot less control.   and not every provider lets you set one explicitly.

[02:26] **Speaker**: Anthropic and Gemini support explicit breakpoints. OpenAI and Fireworks doesn't, and AWS Bedrock varies per underlying model. That's exactly why caching code written for one provider's API doesn't just carry over to another

[02:40] **Speaker**: to see what caching actually saves, we ran the Deep Agents eval suite across three providers' mid-tier models.

[02:47] **Speaker**: Here we have Claude Haiku   GPT-4o mini

[02:51] **Speaker**: and Gemini 3.5 Flash.

[02:53] **Speaker**: claude Haiku uses Anthropic's explicit breakpoints, and it drops to twenty-three percent of its no-cache cost, a seventy-seven percent reduction. As for GPT, they rely on OpenAI's automatic longest prefix caching with no explicit control at all, but it still drops eighty percent. As for Gemini, it makes no explicit savings guarantee with its implicit caching, but it still lands at a very meaningful forty-nine percent reduction. So across the board, there's real savings from forty-nine percent to eighty percent, and it compounds.  The longer a conversation runs, the more turns get to reuse that same cache prefix, so long-horizon agent tasks benefit the most

[03:31] **Speaker**: Head on over to lab two to see this in a real trace,  where you'll run the same exact request twice and watch the second call read most of its tokens straight out of cache
