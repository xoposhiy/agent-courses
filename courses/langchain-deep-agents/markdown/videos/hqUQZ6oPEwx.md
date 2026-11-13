# The System Prompt

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/hqUQZ6oPEwx) · [Raw file](../../raw/videos/hqUQZ6oPEwx.html)

Retrieved: 2026-11-13T16:57:38.526147+00:00

[00:01] **Speaker**: The system prompt guides the model and is part of every model call, so it's resent on every turn ahead of the conversation.

[00:07] **Speaker**: In deep agents, you pass your own instructions

[00:10] **Speaker**: with the system prompt argument.  So this could be things like giving your agent a persona,  such as  answer me only in all caps or emojis, or a constraint that scopes it to one topic domain If you don't pass the system prompt at all, the agent gets no system prompt, and the model falls back to its own generic default behavior with none of the persona, domain scope, or constraints that you'd normally set.  You'll see this yourself in lab one

[00:34] **Speaker**: You'll swap in a pirate, cowboy, or Shakespearean persona and watch the system message change  In your homework, you'll write a constraint that scopes the agent to a single topic domain of your choosing and instructs it to refuse or redirect anything outside that domain.

[00:48] **Speaker**: And this is important because this is how real company chatbots stay on topic. ChatLangChain, which is our own support chatbot, uses that same technique. Its system prompt names the LangChain ecosystem as its scope and instructs the model to decline anything unrelated to keep the conversation scoped to what the product actually supports.

[01:05] **Speaker**: And you can also ensure that the agent responds in the company's voice and branding guidelines.

[01:12] **Speaker**: you may or may not have seen this example before, but some users found that Chipotle's support bot could be used for other things, such as figuring out how to reverse a linked list. Definitely nothing to do with their menu
