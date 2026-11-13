# Lab 2 (LangSmith Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/WzWmCkZHosD) · [Raw file](../../raw/videos/WzWmCkZHosD.html)

Retrieved: 2026-11-13T16:57:38.056408+00:00

[00:01] **Speaker**: We ran the extra posh butler agent twice back to back. So here we see two runs in LangSmith. Now this bottom run is the first call, and it took five point six three seconds, four thousand eight hundred and thirty-one tokens at a cost of zero point zero zero seven five dollars. This run up here is the second call, and it took six point seven two seconds, four thousand eight hundred and sixty-five tokens at a cost of zero point zero zero two six dollars.

[00:28] **Speaker**: This is about a sixty-five percent decrease from zero point zero zero seven five.  Let's start with the first call. Let's go into the model call, then attributes  And then under metadata, if we open up cache control We can see here that the type is ephemeral

[00:48] **Speaker**: And the TTL is five minutes.  TTL stands for time to live, which is essentially how long this cache block stays valid before it has to be written again. And here,  that's five minutes. That's the Anthropic prompt caching middleware default applied automatically, and nothing in this script sets that manually

[01:06] **Speaker**: Now under Usage metadata  and input token details.

[01:10] **Speaker**: Cache_read is zero

[01:13] **Speaker**: But the ephemeral input tokens are four thousand four hundred and twenty-six. So that's the system prompt and the summon_tea tool definition. Four thousand four hundred and twenty-six tokens getting written into a five-minute cache for the first time. There's nothing to read yet, so cache_read is zero.

[01:31] **Speaker**: Now if we go into the second call

[01:39] **Speaker**: The cash rat is now 4,426

[01:42] **Speaker**: and the ephemeral input tokens drops to zero. So it's the same exact four thousand four hundred and twenty-six tokens,  but now they're read out of cache instead of reprocessed.

[01:53] **Speaker**: So you'll notice this run actually took a bit longer than the first at six point seven two versus five point six three, and it also took more tokens at four thousand eight hundred and sixty-five versus four thousand eight hundred and thirty-one. That's not a caching regression.  Caching saves you money, not necessarily time. The total latency here is dominated by how many tokens the model generates in its reply. And this run's answer happened to run a little longer. So reading from cache shaves a bit off how long the model spends processing the prompt itself, but that's a small slice of the total request time next to output generation

[02:27] **Speaker**: Now writing to cache costs a premium. It's roughly 1.25 times the normal input rate. Reading from it is a steep discount, though, about a tenth of the normal rate.
