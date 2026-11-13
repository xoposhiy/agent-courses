# Lab (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/LqdM9KRzLX7) · [Raw file](../../raw/videos/LqdM9KRzLX7.html)

Retrieved: 2026-11-13T16:57:37.450734+00:00

[00:00] **Speaker**: So here we have three runs. This first one is thread A, turn one. This is thread A, turn two.  And this is thread B's only turn. Let's start with thread A, turn one

[00:12] **Speaker**: So LangSmith groups runs by thread ID,  clicking on this run opens the full thread A view. We can see turn one and turn two together.

[00:20] **Speaker**: So for turn one,  Our input message is to remember that our favorite color is blue. There's no prior history, and this is the first call on this thread

[00:29] **Speaker**: In the output, the agent acknowledges it  this message  and the agent's acknowledgement both get saved by the checkpointer under the same thread ID. Now let's look at turn two   we can see it's got the full accumulated history

[00:42] **Speaker**: so that when you get asked the new question, everything was passed to the model

[00:46] **Speaker**: The model answered correctly.

[00:51] **Speaker**: Now let's look at thread B. Only one turn, and as you can see,  no prior history

[00:57] **Speaker**: The checkpointer looked up the thread ID for thread B and found nothing, so it gave the model a clean slate  Therefore, it doesn't know. Not because the model forgot. The information was just never in the thread's history. Same agent, same checkpointer, different thread ID, completely separate state
