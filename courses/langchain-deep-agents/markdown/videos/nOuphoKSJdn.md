# Deploying Your Agent (without Slack)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/nOuphoKSJdn) · [Raw file](../../raw/videos/nOuphoKSJdn.html)

Retrieved: 2026-11-13T16:57:39.073618+00:00

[00:00] **jess**: Let's start by going into the directory

[00:06] **Speaker**: Then we need to add our API keys in our .env

[00:12] **Speaker**: I've added my LangSmith API key and my existing Anthropic API key. Now we can run MDA deploy

[00:25] **Speaker**: now, this can take up to five minutes, so don't worry if it feels like it's taking a while

[00:30] **Speaker**: One eternity later

[00:36] **Speaker**: So these two links are the agent server URL and the dashboard URL

[00:42] **Speaker**: You'll want to copy the dashboard URL and then paste it into your browser

[00:47] **Speaker**: So pasting that link in opens up LangSmith, and if you click on this blue Connect button over here, you can open in Studio And here you have your agent. So because it's a DVD rental store analyst agent, we can ask it some questions related to that What were our top five categories by revenue last quarter?

[01:07] **Speaker**: Now, the first message will always take a little longer because the sandbox is running before the agent's first turn, and this is installing Pandas and Matplotlib and then downloading the Sakila schema and data and building the database from them. Any follow-up questions in this same thread will reuse that sandbox and will be much faster.

[01:27] **Speaker**: Great. So all the info you see here is the agent writing Python in the sandbox against the database. It doesn't have its own SQL tool. It wrote that code

[01:37] **Speaker**: Let's try another question Which store is doing better and by how much?

[01:47] **Speaker**: as you can see, that was a lot quicker  Now, if we want to edit the system prompt, which remember, in Manage Deep Agents, it's instructions.md, all we have to do is go over to Context Hub over here Click into our agent And click into instructions.md. If you want to edit it, just click on Edit over here.

[02:11] **Speaker**: Great. Let's say we wanted to add a persona

[02:15] **Speaker**: Let's make our agent respond as a dramatic woe is me Victorian era child. This will be fun

[02:23] **Speaker**: Now after saving, all we have to do is go back and connect our agent again. No need to redeploy

[02:34] **Speaker**: i've opened up that same conversation we were just in

[02:37] **Speaker**: and let's ask that same question

[02:41] **Speaker**: Oh, woe betide me!" We have our dramatic agent. Here we go. "' Tis store two that fares the better." All right, store one needs to step it up. Anyways this is how you'd edit your system prompt through instructions.md, and you don't need to redeploy with Context Hub

[02:57] **Speaker**: Now, if you wanted to change agent.py by adding a tool or switching the model, you would have to run MDA deploy again. ContextHub covers instructions.md and skills, but code is still code in agent.py Speaking of skills, let's take a look at that

[03:17] **Speaker**: Here we have a quarterly business report skill.md

[03:22] **Speaker**: It generates a quarterly business review report for the DVD rental business.

[03:35] **Speaker**: Let's get it to use the skill to generate the QBR.

[03:42] **Speaker**: I forgot I left the,  the persona in, but gather close  our stores rung 62,000 in revenue. but you get the gist of it

[03:54] **Speaker**: They sorted revenue by language, revenue by category, and top actors by revenue. So if I were to go back, let's remove that   dramatic persona here

[04:09] **Speaker**: Save. And let's actually edit the skill.   Instead of this format, let's say I want it to  respond only in poetry. Do not create any... I can't spell, any tables   Great. Let's leave it at that

[04:41] **Speaker**: Let's get it to generate the QBR again

[04:49] **Speaker**: There you go. No tables and just some...   wonderful poetry. Tongues that spoke the loudest coin. It seems to be English. Anyways, you get the gist of it. It's very easy to edit live in ContextHub both your instructions.md and your skill files  In addition to that,  we didn't set up any LangSmith tracing.  However The deployment created its own project automatically, so we can see all of our traces here.   We can see what tools it called, and so on and so forth.
