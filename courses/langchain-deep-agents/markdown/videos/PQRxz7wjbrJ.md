# Lab 2 (Prompt Caching)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/PQRxz7wjbrJ) · [Raw file](../../raw/videos/PQRxz7wjbrJ.html)

Retrieved: 2026-11-13T16:57:37.688071+00:00

[00:01] **Speaker**: This lab is a chunkier version of Lab One so that the caching process is a little more obvious to see

[00:09] **Speaker**: The system prompt here  is much longer ne's Butler, and we've added a custom tool

[00:16] **Speaker**: so that there's real sizable static prefix  for  the  provider to cache between calls

[00:22] **Speaker**: so back to our system prompt. It's the same idea as Lab 1's persona, a posh British butler, but we just cranked it up several times longer, many more  rules of comportment

[00:32] **Speaker**: More forced quirks  like addressing the user as good sir or madam  adjusting your eyewear and et cetera. This whole block is what gets sent and cached on every single call

[00:44] **Speaker**: As for this custom tool

[00:46] **Speaker**: summon_tea. It takes a flavor and an optional temperature and just returns a string describing the tea being summoned in character.

[00:54] **Speaker**: This matters for caching too. Tool definitions are just as much a part of the prefix as the system prompt is,  and Anthropic's caching middleware tags the last tool in the list, which covers this one along with the built-in tools ahead of it.  Don't worry if this doesn't make complete sense just yet.  We cover tools in the next lesson

[01:13] **Speaker**: And the agent gets created here

[01:15] **Speaker**: The system prompt here is our system prompt

[01:20] **Speaker**: Tools includes  the summon_t tool I just showed you

[01:23] **Speaker**: And the name is Extra Posh Butler Agent  and then a single invoke here with one question

[01:30] **Speaker**: What is an LLM?  Then we print the last message.  there's no loop, no multi-turn conversation. We're just going to create the repetition ourselves from the terminal

[01:42] **Speaker**: we're running it twice back to back, completely unchanged

[01:46] **Speaker**: now, these two runs look identical from the terminal, but underneath, the second one didn't pay for the same tokens twice. It's easier to see this in LangSmith, so let's head over
