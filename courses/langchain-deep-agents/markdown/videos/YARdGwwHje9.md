# Summarization

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/YARdGwwHje9) · [Raw file](../../raw/videos/YARdGwwHje9.html)

Retrieved: 2026-11-13T16:57:38.133453+00:00

[00:01] **Speaker**: As agents grow more capable, tasks span more steps, sessions run longer, and tool results pile up. Token counts climb steadily towards the model's limit and left unchecked, a long-running agent eventually stalls. Deep Agents handles this with two complementary mechanisms. On the left, you can see summarization. It watches the context fill up and compacts old messages into a summary before the model ever sees them. On the right, we have offloading. It intercepts individual inputs that are too large before they even enter context and saves them to the file system, and it leaves a pointer in their place.

[00:37] **Speaker**: These work on different problems. Summarization deals with gradual accumulation across many turns, and offloading deals with singular large spikes

[00:46] **Speaker**: Think of the context window like a thermometer. Every new message adds tokens and the level rises, and when it crosses eighty-five percent of the model's limit, the middleware fires

[00:59] **Speaker**: so these are messages from old to new. Now the middleware picks a cutoff point and keeps the most recent messages intact while it summarizes everything older into a single block. The messages being summarized are appended to the conversation history on the file system, so nothing is truly lost.

[01:20] **Speaker**: The summary the model receives includes a link to that file, so the agent can read it back with read_file if it ever needs all of this detail. Because a summary is far more compact than the messages it replaces, the token count here drops sharply, and the conversation can continue Now on a second summarization event, the prior summary is treated just like any other old message.

[01:41] **Speaker**: It gets folded into a new combined summary along with whatever else has aged past the cutoff. There's no special handling for summaries. The same logic applies every time. Every event produces exactly one summary block, no matter how many rounds have happened before.

[01:59] **Speaker**: So what actually goes into the summary?

[02:02] **Speaker**: The middleware makes a separate LLM call using the same model as the agent with a structured prompt that extracts four things

[02:10] **Speaker**: the session intent, which is what the user is trying to accomplish  key facts and decisions from the conversation

[02:16] **Speaker**: Any artifacts like files that were created or modified  and what still remains to be done

[02:21] **Speaker**: That resulting text is injected as a single human message at the top of the preserved recent messages, so the model picks up context as if it had been there the whole time
