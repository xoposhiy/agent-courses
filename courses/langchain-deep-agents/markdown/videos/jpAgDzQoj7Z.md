# Models

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/jpAgDzQoj7Z) · [Raw file](../../raw/videos/jpAgDzQoj7Z.html)

Retrieved: 2026-11-13T16:57:38.747914+00:00

[00:01] **Speaker 2**: So what is a model provider?

[00:03] **Speaker**: a model provider is a company or platform that hosts AI models and lets you call them through  an API. Think OpenAI, Anthropic, or Google

[00:12] **Speaker**: LangChain supports over 50 chat model providers, so you're never locked into using a specific model.

[00:18] **Speaker**: And we'll actually go over swapping models

[00:21] **Speaker**: There are roughly three types of models  conversational  Advance reasoning  and open source. Each has different trade-offs around cost, capability, and control, and this table lists a few examples.  Most models across all three categories also accept image inputs and some accept audio.

[00:41] **Speaker**: multimodal support works through the same InitChatModel interface, so no extra setup is needed. For this course

[00:48] **Speaker**: All labs share a single models.py file. That's how every lab imports its model. To swap models, just comment out one line

[00:57] **Speaker**: And uncomment another. Let's head on over to the lab to see how that works
