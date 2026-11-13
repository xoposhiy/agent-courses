# Lecture 1 transcript: Introduction — What Are Agentic Systems?

[Course index](../../README.md) · [Original source](https://youtu.be/DGI4vucR71w) · [Raw file](../../raw/videos/DGI4vucR71w.json)

Retrieved: 2026-11-13T16:17:39.677947+00:00

[00:05] Welcome, everyone.

[00:06] This is CS329Z--

[00:09] Engineering AI Agents.

[00:11] And today is the introduction
to agentic systems.

[00:15] I'm Diyi Yang, an assistant
professor in computer science

[00:17] here, and I'm
co-teaching this course

[00:20] with Michael Ryan and John Yang.

[00:23] Today, we will cover
logistics and also

[00:26] give you a short history of
agents, what agent is made of

[00:30] and also the open problems
we will work on this quarter.

[00:34] I'll first let Michael and
John introduce themselves.

[00:38] Hi, everyone.

[00:39] I'm Michael.

[00:39] I'm a second year PhD
student here at Stanford,

[00:42] and I'm advised
by Diyi and Percy.

[00:45] So my research is on
open-source human-centered AI.

[00:49] And in the past
agent-related work,

[00:51] I've worked on the DSPy
framework for programming,

[00:56] not prompting language models.

[00:57] So that's my little
claim to agents.

[01:01] Hi, my name is John.

[01:02] I'm a third year
PhD at Stanford.

[01:04] I'm advised by Diyi.

[01:05] And in the past I've worked
on coding agents and coding

[01:09] evaluations.

[01:10] So I created a SWE-bench
SWE-agent, program

[01:14] bench SWE-smith if you've
heard of those works.

[01:17] Yeah.

[01:18] Great.

[01:19] OK, so with the
instructor team, I

[01:23] want to formally welcome
you to this course.

[01:26] The primary contact to reach out
to us is to use Ed Discussion.

[01:30] If you want to be added to
it, just send us an email.

[01:33] We prefer you send
everything to this email list

[01:38] so that we can take care of
your requests very quickly.

[01:41] The website will maintain
all the lectures,

[01:43] slides, and homeworks.

[01:45] So that's your primary
website to check out.

[01:49] If you haven't enrolled
in Ed Discussion,

[01:51] please do since we post a lot
of announcements there as well.

[01:55] So in today's
lecture, in addition

[01:58] to the logistics I'll
mention in a few seconds,

[02:01] we are going to provide
a history of agents.

[02:05] There is actually a really
long history behind agents.

[02:09] We will talk about
agent architecture.

[02:11] This is the core content today.

[02:12] And then compound
the AI systems--

[02:14] RAG, tool use, and MCP.

[02:17] We will end with a brief
highlight of key challenges,

[02:20] including the recent
multi-agent risk and collusion

[02:24] we have been seeing.

[02:26] So let's get started.

[02:29] Why we create CS329Z?

[02:32] So when we think about large
language models, agents

[02:36] these days, there seems to be
very different perspectives

[02:39] involved.

[02:39] You can take a
modeling perspective.

[02:42] You can also take a
system perspective.

[02:44] A lot of what we do is
actually around engineering.

[02:48] And if you think
about that, LLM people

[02:51] I think they know how models
are trained, pretraining,

[02:54] post-training, prompting,
alignment, and evaluation.

[02:58] On the other side,
system people know

[03:01] how to build a
reliable tools systems.

[03:04] More related to agents, we
have tools, APIs, environment,

[03:08] and infrastructure.

[03:10] So the expectation
for this course

[03:12] is that we are going to cover
a lot of the foundations.

[03:16] But more importantly, we want
it to be more hands-on building

[03:20] plus evaluation of agents.

[03:23] A quick glance of the content.

[03:25] So week 1 to week 5, we will
talk about large language models

[03:30] for builders with a highlight of
retrieval augmented generation

[03:35] and its variants in many, many
follow-up agent architectures.

[03:39] Tool use and function call
will be another highlight here.

[03:43] We will slowly move to
agent design, training,

[03:46] and scaffolding, and also
the design of agent memory

[03:50] as well as orchestration
and multi-agent systems.

[03:55] The second half
of this course, we

[03:57] are going to have
optimization, harness, and data

[04:01] for agentic systems, data
quality, data selection, et

[04:05] cetera.

[04:05] The evaluation, the
benchmark design

[04:08] will also be highlighted
in different ways.

[04:11] Agent safety and
guardrail will also

[04:14] have two special
highlights of coding agent

[04:17] and also a more emerging topic
called the proactive agents.

[04:24] We have actually
two special teams

[04:28] who are going to show up
in our class this quarter.

[04:31] First, we will welcome
the terminal bench team

[04:35] to talk about how they
design Terminal-Bench

[04:38] and a lot of questions
you can share with them.

[04:41] We will also welcome
the SWE-bench team

[04:43] to come to chat with us.

[04:45] So for both lectures, it will
be a team reunion from those two

[04:51] teams that created a very
fundamental evaluations

[04:54] in our field.

[04:56] Course policy.

[04:57] First, I think the biggest
message that I want to highlight

[05:01] is that you should
use AI to learn.

[05:06] You may want to get yourself
familiar with the Stanford honor

[05:09] code.

[05:10] And laptop use is only allowed
for taking notes, et cetera,

[05:14] and we strongly discourage
the use during the lecture

[05:19] so that you can be more focused.

[05:22] Prerequisite and compute.

[05:24] So first, we strongly
recommend that you

[05:27] have taken any NLP or large
language model-related training.

[05:32] You are expected to know
basic LLMs since we are not

[05:35] going to cover
fine-tuning or pretraining

[05:38] or alignment, et cetera.

[05:40] In terms of compute, we are very
grateful that Laude Institute

[05:45] gives each student $200
in terms of credits.

[05:48] And the Thinking
Machine will provide

[05:50] a $250 for Tinker credits.

[05:55] I want to switch a little bit to
conclude the logistics section

[05:59] by showing you a figure.

[06:01] This is just a specific instance
of what's happening today.

[06:08] With a lot of data, if
you show on the top,

[06:10] this is actually homework score
from two populations, people

[06:15] who use AI and the
people who do not use AI.

[06:19] Very interestingly,
I think with AI,

[06:22] everyone's homework
score are just so great.

[06:25] But then if you
look at the bottom,

[06:27] this is actually the exam
score for the same population.

[06:30] Before using AI,
this is definitely

[06:33] more shifted towards 100 here.

[06:36] With AI, we have way more
people did worse in their exams.

[06:41] And I think we see this kind
of pattern very frequent

[06:44] these days.

[06:46] The second example that
I want to share with you

[06:48] is actually from Anthropic.

[06:51] They did a study with
their own engineers

[06:54] to figure out how the
use of coding agents

[06:57] actually impact coding.

[07:00] As you can see from the
left side, if you use AI,

[07:03] the task completion
time actually decreased.

[07:06] But then on the right, the quiz
score in terms of your mastery

[07:10] actually significantly
decreased.

[07:13] That is, despite the coding
agent that can give us 1,000

[07:16] lines of code, it's a little
bit unclear whether we fully

[07:19] understand such AI output.

[07:22] So with that, I want to
conclude the logistics

[07:25] by saying that we
really hope that you can

[07:28] use AI to learn how to learn.

[07:30] And this is really just
about you and your CS329Z.

[07:35] With that, any quick
questions for logistics?

[07:40] OK.

[07:41] If there is no question,
we will continue

[07:44] to the history of agents.

[07:46] One thing that I
do want to mention

[07:48] is that the learning
objective today

[07:51] is for you all to get
familiar with agent loop

[07:54] on top of large language
models and the different key

[07:57] components.

[07:59] So let's get started.

[08:01] This is a word that's probably
very, very popular today.

[08:05] And what I'm going to
do next is to trace

[08:08] where this idea
actually came from,

[08:11] how it developed
over the decades,

[08:12] and why it suddenly took off
with large language models.

[08:19] If you look at the more
linguistic side of agents,

[08:23] the word agent actually
comes from Latin,

[08:26] meaning that one who acts.

[08:28] And this term also entered
English in the late 14th

[08:34] century.

[08:35] So in AI, the first
index use of it

[08:38] is in this specific
adjective paper from 1973,

[08:43] where Hewitt and
Bishop and Steiger talk

[08:46] about this architecture called
the ACTOR algorithm, where

[08:50] each actor is an active
agent that wait for a message

[08:54] and then does what the
message tells them to do.

[08:57] So the idea of software
entities that act on their own

[09:02] is older than most
people can think about.

[09:06] And then I think a
few years after that,

[09:10] the contract net
protocol actually

[09:12] talks about how agents
dividing tasks with each other

[09:16] and then negotiating tasks.

[09:19] This trend actually continues.

[09:21] In Marvin Minsky's
Society of Mind,

[09:24] it actually talks about
how a group of subagents

[09:27] actually work together
to get something done.

[09:30] And if you reflect on this, this
is actually the earlier idea

[09:34] of multi-agent orchestration.

[09:38] I think the history
actually continues.

[09:40] Around the 1990s, we actually
see more and more emergence

[09:45] of software systems
that serve as agents,

[09:49] from parties designing
autonomous agents to later

[09:54] people talk about agentized
autonomy, social ability,

[09:59] reactivity, proactivity, trying
to define agents in different

[10:02] ways.

[10:03] The most familiar
definition to many of us

[10:07] is actually from Russell and
Norvig, which defines agents

[10:11] as anything that perceive
through sensors and acts

[10:16] through actuators here.

[10:20] We now enter a different stage,
which we call reinforcement

[10:24] learning era here.

[10:26] This is a classic agent
environment loop that many of us

[10:31] get familiar during RL courses.

[10:33] So what happened
here is that agents

[10:36] take action in the
environment, and such action

[10:39] will receive a reward.

[10:41] And then they do the action
based on specific state

[10:44] and the current reward.

[10:46] So this is a very classic agent
environment loop from Sutton

[10:49] here.

[10:50] And then I think we see more
and more promising from--

[10:55] promises from this
kind of setup.

[10:58] DQN refers to Deep Q-Network.

[11:02] This is actually from
DeepMind earlier days,

[11:05] where they build AI systems to
actually solve specific games.

[11:12] And I think later, you also see
that AlphaGo and OpenAI Five

[11:18] are showing that
this kind of approach

[11:20] actually can reach
superhuman performance in go.

[11:24] And I think this is DOTA 2.

[11:26] So those were agents,
but each of them

[11:29] are actually trained
for a specific task.

[11:34] So what actually changed
is the introduction

[11:37] of large language models.

[11:38] I think the first impressive
capability of LLMs

[11:43] is actually in-context learning.

[11:45] Build upon this kind of
transformer-based architectures.

[11:49] GPT-3 actually showed that
you can just talk about a task

[11:53] and give you a few
demonstrations.

[11:56] Like in this particular
example of few-shot,

[11:59] in order to do translation,
you can offer certain examples.

[12:03] And then the model can
actually follow such examples

[12:06] and then do the task.

[12:08] This entire process, unlike
previous systems I showed you,

[12:12] there is no gradient
update happening here.

[12:18] I think not only in
terms of prompting

[12:21] or in context
learning, prompting

[12:23] could do more than teach
a model on a new task.

[12:28] It turned out that
models themselves,

[12:30] they can also
reason step by step,

[12:32] and then use tools for the
things that they cannot do

[12:36] alone.

[12:37] So this particular
example is called

[12:39] the Chain-of-Thought prompting.

[12:41] You can see that
asking the model

[12:43] to actually work through
a problem step by step

[12:46] actually give more accurate
answers in general.

[12:50] When GPT was proposed
by OpenAI, this

[12:54] actually enables language
model in earlier days

[12:58] to use a web browser so that
it can actually look up things

[13:02] online instead of only rely
on memory or parameters.

[13:07] This actually leads to
a lot of follow-up work

[13:10] in terms of web browser agent.

[13:15] One of the very
interesting architecture

[13:17] is actually called
the modular reasoning

[13:19] knowledge and language.

[13:21] I would view it as one of
the first earlier systems

[13:24] to think about to use.

[13:27] So basically this
architecture actually

[13:29] decides which outside
expert to send a request to.

[13:34] Is this going to be
a weather request?

[13:36] So then I should
use a weather API.

[13:39] If this is a coding
task, maybe I

[13:41] should send it to a Python
programming tool, et cetera.

[13:46] So now the model
actually can think,

[13:48] and it can take
actions through tools.

[13:53] So I think we now have
both important pieces here.

[13:56] That is, models can reason
step by step and models that

[14:00] can use tools.

[14:01] Those are two very, very
important prerequisites

[14:04] for the emergence of agents.

[14:07] I'm going to show you a
very short timeline in what

[14:10] happened in history,
that is, two years ago.

[14:13] So 2022, ReAct was proposed.

[14:19] So the name actually
means Reason plus Act.

[14:24] So instead of thinking
once and then answering

[14:26] the question, what the model
does here is actually a loop.

[14:30] It thinks about what to do
next, take action, and then look

[14:35] at what happen, and then
use that to think again.

[14:38] So it's actually a
loop happening here.

[14:42] After that, I think we see
that more and more models get

[14:46] released.

[14:47] So ChatGPT get
launched, and suddenly I

[14:50] think millions of people start
to talk to LLMs every day.

[14:56] And then GPT-4 was released.

[14:58] And the reason why I
want to mention this

[15:00] is that if you
think about agents,

[15:02] they really rely on the base
model, the strong capability

[15:05] from those base models.

[15:07] So when GPT-4 came out, we
have a much stronger model

[15:10] that could follow
long instructions

[15:14] and plan more reliably.

[15:18] Within two weeks,
there were actually

[15:19] two open source
projects came out

[15:22] that really shape what
we think around agents.

[15:26] The first one is
called the BabyAGI.

[15:29] It basically gives
the model a goal

[15:31] and let it write its own task
list, walk through the task

[15:36] and add new ones as it goes.

[15:40] AutoGPT was released I think in
the same month, two days later.

[15:47] Basically try to connect GPT-4
to tools such as web search,

[15:52] file systems, et cetera.

[15:53] And then likely to
keep going on its own

[15:56] without a person really typing
the next prompt each time.

[16:01] I think, now if you look
back, it was definitely

[16:04] very ahead-of-time ideas.

[16:06] The reality is that none
of them actually really

[16:09] worked very well.

[16:12] But they got people's
attention and really

[16:14] opened our imagination
about what's possible.

[16:18] And I think that that's also
probably the time when the word

[16:21] "agent" really
enters everyday use.

[16:25] So I want to go a
little bit deeper here

[16:29] to share with you the underlying
model and also agents,

[16:33] how they have
improved since 2023.

[16:37] So this page, if
you look at that,

[16:40] I only show the GPT-3,
GPT-4, and GPT-5.

[16:44] The underneath model actually
is getting better and better.

[16:49] If you just contrast
GPT-3 versus GPT-4,

[16:52] we see that on MMLU,
there is a 43% increase.

[16:56] This is actually true for all
the data sets that we have.

[17:01] From GPT-4 to GPT-5, some
of those data sets actually

[17:04] didn't show up here
because they got solved,

[17:07] or they saturated so that they
cannot be used as very reliable

[17:11] signals.

[17:12] Instead, we actually
introduced more evaluations

[17:15] such as GPQA which is a very
challenging QA setting and also

[17:22] harder and harder
math problems here.

[17:25] So the key message here is that
each generation of base model

[17:29] actually made a really big jump
in terms of their performance.

[17:34] And a stronger model
means that the agent now

[17:36] can actually reason better.

[17:39] They can make fewer
mistakes, hallucinate less,

[17:43] and along the way, they can
handle longer and longer tasks.

[17:47] And then let's look
at the agent side.

[17:50] So the agent side is also
improving as well, not only just

[17:55] like the raw model capability.

[17:58] So this page is actually
around like SWE-bench verified.

[18:02] As you can see in
January 2025, I

[18:06] think the performance
is only around 30%.

[18:09] But then over the last
one year and a half,

[18:14] now, all the
numbers are actually

[18:16] reached a very high stage here.

[18:20] And then right side, this
is from actual release.

[18:22] So you can see that
our OS world, which

[18:24] is a computer used for
evaluation, and also

[18:28] on Terminal-Bench, which is a
command line task, the accuracy

[18:33] are just impressive.

[18:35] There is also a
trend that people

[18:36] start to pay attention to the
efficiency of the process.

[18:40] This is why you are seeing
that most of those curves

[18:43] these days actually have
both price and accuracy

[18:46] there together.

[18:48] So this is how we get here.

[18:50] It's a long history
in the last 60 years.

[18:54] So what I'm going to do next
is to really open one up

[18:58] and see what an agent
is actually made of.

[19:03] Any quick questions here?

[19:07] OK.

[19:09] Yes?

[19:10] Do you think models'
capacity or ability

[19:13] is going to saturate
in a few years,

[19:16] or is it going to still develop
for like 10 years or so?

[19:23] First, just to
repeat the question,

[19:25] the question is, will model
capabilities saturate,

[19:28] or will it keep improving?

[19:30] I think in terms of
timeline, it's really hard

[19:32] to make estimation into the
future because a lot of things

[19:36] can actually happen in two
to three months these days.

[19:39] There has been a very
interesting topic on RSI,

[19:43] Recursive Self-Improvement.

[19:45] And it has showed very
interesting patterns

[19:48] on solving OpenMath problems
and many other tasks.

[19:51] I think with RSI, this pattern
will get accelerated a lot.

[19:56] So let's see.

[20:00] Yes?

[20:02] Can you go back
to the last slide.

[20:05] Yeah.

[20:06] So when you see the improvements
on the Terminal-Bench window,

[20:10] we can see that GPT-5.6 is
doing really bad over the period

[20:17] of API calls.

[20:19] As the API cost increase,
the accuracy increase.

[20:26] What are the reasons
for doing better

[20:30] than the API cost increase?

[20:32] Also, what are the reasons for
GPT-6 extra doing much better?

[20:37] Is it algorithmic development?

[20:38] Is it bigger model?

[20:41] Yeah, great question.

[20:42] The question is that why
when the models get better

[20:45] is much more expensive?

[20:48] And also why is extra better
than their earlier models?

[20:51] So in terms of the price
and better performance,

[20:55] the API cost here is
strongly associated

[20:58] with the number of tokens
digested in the process.

[21:02] So if you think longer,
the general pattern

[21:05] is that thinking
longer, thinking longer

[21:08] is actually going to lead
to improved the performance.

[21:10] So this is just a general trend.

[21:12] And then in terms of why
models are getting better

[21:16] than their previous model, I
think there are many reasons.

[21:20] This is also a
topic we are going

[21:21] to go deep later in terms
of open weights models

[21:25] and the openness
of large language

[21:26] models and the
proprietary model aspects.

[21:30] The reality is that we do
not know a lot about how

[21:34] those models are trained.

[21:36] Is it about better data, better
distillation, or other aspects?

[21:42] OK.

[21:44] Let's now move to the
agent architecture.

[21:48] So I think if you
think about agents,

[21:52] it has a really long history.

[21:54] It got really accelerated
with large language models.

[21:58] And this is going to
be the agent that we

[22:00] are going to talk about.

[22:02] And I want to go back to
this example from ReAct

[22:05] that I showed you.

[22:07] So in this particular
example, the agent

[22:10] needs to think about what
they are going to do.

[22:14] So this particular task is to
put a pepper shaker in a jar.

[22:19] And then if you read
the right side top

[22:22] to the bottom, the model
itself is actually a LLM core.

[22:27] This is the foundation
model underneath.

[22:31] And then the thinking
step here, basically, it

[22:34] says things like, I
need to find a pepper

[22:36] shaker more likely in cabinets.

[22:39] Those are what we call
planning and reasoning.

[22:42] And then the traces
so far, everything

[22:46] above the current step
is what we call memory.

[22:50] And then the agent actually take
actions such as go to cabinet 1

[22:54] or take a pepper shaker.

[22:56] Those are what we
call tool calls.

[22:59] And then those
observations, those

[23:02] are literally just
like after each action

[23:05] what the agent sees
from the environment.

[23:08] You can see that at least there
are five components if we just

[23:11] look at this very simple
example from ReAct.

[23:16] So we will now walk
through each of them.

[23:20] So this is meant to be
a conceptual framework

[23:25] just to highlight the
different components.

[23:28] And then if you see
different directions,

[23:29] it actually didn't
carry a lot of weights.

[23:32] When we talk about agents,
I want to just show you

[23:35] some core components here.

[23:38] First, agents is built on
top of large language models.

[23:42] So stronger models in
general means better agents.

[23:46] This is why we also have
a debate in terms of

[23:48] should I think about
training for agents,

[23:50] or should I just
care about better

[23:52] harness or other improvement?

[23:57] On top of LLM core, there is a
very important component called

[24:01] the planning and reasoning.

[24:03] So if you think about asking
agents to do a very big task,

[24:06] they actually need to decompose
them into smaller pieces

[24:09] and then maybe have sub agent
to deal with each of them.

[24:13] We may also want to add some
explicit aspects to improve

[24:17] the reasoning here.

[24:19] And then as you see from
the earlier example,

[24:21] we need to introduce
a memory to make sure

[24:23] that as agents work on the
task for more than two hours,

[24:27] they actually know what
has happened so far

[24:29] and then can use that as
context to do the reasoning.

[24:34] Even in earlier days when
model can solve very hard math

[24:38] problems if you ask
them where is CS329Z

[24:43] happening today on campus?

[24:45] Probably models
cannot answer that.

[24:48] Yes, our systems also
cannot answer that.

[24:53] So in order to really
enable LLMs to do stuff,

[24:58] we actually could
give them tools here.

[25:00] This could be
information retrieval.

[25:02] If they do not know what's
the classroom location,

[25:06] they can actually go to Stanford
website and search for it.

[25:09] If they do not know the
weather today at Stanford,

[25:12] they can actually search for
weather from official database.

[25:16] Similarly, I will show more
examples in a few weeks.

[25:22] There has been a time period in
history where despite the GPT-4

[25:27] was amazing, it actually cannot
solve 3 digits times 3 digits,

[25:32] just like a simple
multiplication problem.

[25:35] So there are a lot
of those scenarios.

[25:37] So tool use really enable
agents to take factual

[25:42] and more consistent actions.

[25:46] And all of those actions
lead to different terms

[25:49] that you may have heard of
such as tool call, interaction,

[25:53] response to users.

[25:54] This is what we
call agent actions.

[25:58] And I think more importantly,
there is this environment part

[26:01] that we haven't talked about.

[26:03] So agent observe what's
happening in the environment

[26:06] and then take actions.

[26:08] So what do you see on
the screen right now,

[26:10] this is actually a
skeleton of an agent.

[26:13] Of course, this is only
one way to draw it.

[26:16] And please do not
take too much weights

[26:19] with these kind of directions.

[26:20] This is really meant to
illustrate the process here.

[26:25] And then on top of
this single agent,

[26:27] you can imagine that you
can have different agents.

[26:30] Even within the same
agent, maybe you

[26:32] can do different configuration
optimization for each box

[26:35] that I listed here.

[26:37] This is why later
harness and optimization

[26:40] become very important
because everyone

[26:43] wants to find the most optimal
configuration for this agent.

[26:49] As I said that this is not the
only way to talk about agents,

[26:54] and our breakdown is not
unique, different researchers

[26:57] actually use different labels.

[27:00] For a long time, I think there
was a lot of debate around what

[27:03] is an agent?

[27:04] What is not an agent?

[27:05] What is agentic systems?

[27:07] What is not agentic systems?

[27:08] We are now going to do
any debate in this class,

[27:12] but I think you can see the
common components showing up

[27:14] here.

[27:16] The left side is from an
OpenAI researcher back in 2023.

[27:20] They talk about that OK,
if you think about agents,

[27:23] they use tools.

[27:24] They have memory,
planning, action.

[27:28] And then on the right side, this
is around the cognitive language

[27:31] agents.

[27:33] You can see that they have
similar pieces such as memory

[27:36] with retrieval to read from
it and also learning to write

[27:40] to it, reasoning, et cetera.

[27:42] Despite those are
different vocabularies,

[27:45] I think it really point to
the same architecture here.

[27:49] That is, an LLM reason,
remember, and use tools and acts

[27:54] in a loop within
its environment.

[27:58] So now I'm going to
go back to the diagram

[28:01] of those different
components and start

[28:03] to share with you different
modules we have here.

[28:07] So if you look at this, I
think the first thing that

[28:10] comes to mind is actually
this planning and reasoning

[28:13] from this particular figure.

[28:16] So then the question
is, what does that

[28:19] mean for LLMs to reason?

[28:21] And why does it help an agent?

[28:25] I want to draw some kind of
metaphor to human reasoning

[28:30] here.

[28:31] This action is probably a
little bit controversial,

[28:33] if you think about that.

[28:35] There has been a
lot of debate to see

[28:37] whether the reasoning of AI
is similar to human reasoning.

[28:41] Again, no debate in this course.

[28:44] But if you look
at this process, I

[28:46] think for humans, what
does reasoning mean?

[28:48] It means that some mental
process, such as deduction,

[28:53] analogy, and planning that we
all do for different tasks.

[28:58] For LLMs, I think you can think
about them as Chain-of-Thought.

[29:02] So in this particular example
here, most of the time

[29:06] we would call this
Chain-of-Thought

[29:08] as a reasoning process.

[29:10] Although one message I
want to share with you

[29:13] all is that this
Chain-of-Thought may not

[29:16] be fearful of what actually
happened within LLMs.

[29:23] For agents, by reasoning, we
mean the internal actions that

[29:26] update the agent's own state.

[29:29] So those are just
a different terms

[29:31] to understand the
reasoning and the planning.

[29:33] So now let's look at
a concrete example.

[29:37] So why is reasoning
helpful for agents?

[29:40] So imagine we have an agent
that's doing actions right now.

[29:44] And at the t step it observes
that you are cooking a dish

[29:49] and seeing salt is out.

[29:51] And then the next step if you
see an action of turn right,

[29:56] if you just look at those
two, I at least get confused.

[29:59] OK, why is the agent actually
turning right here, et cetera?

[30:04] So the observation to action
mapping is actually huge.

[30:08] And then this can be
very hard for audits

[30:11] or just like for
making agents better.

[30:14] So if we could actually
introduce a reasoning model here

[30:17] to let agents to
explicit reason,

[30:20] then this actually help a lot.

[30:23] If you read the reasoning
in the green box,

[30:25] it says that the dish should be
savory, and since salt is out,

[30:29] I should find
something equivalent.

[30:32] It is in the
cabinet to my right.

[30:34] And then when it
turns right, we know

[30:36] why the agent is doing
this particular action.

[30:40] I think the reasoning
helps in two ways.

[30:42] First is from a
generalization perspective,

[30:45] because the same reasoning
could actually work

[30:47] in new, similar situations.

[30:50] It also helps with alignment
because you can see

[30:53] why the agent did what it did.

[30:56] So this is why
reasoning was actually

[30:58] a first important component
we are emphasizing.

[31:04] So now just to understand
why systems like ReAct

[31:07] beats existing
prompting methods,

[31:10] I'm going to give you
another example here.

[31:13] This is an example
from HotpotQA.

[31:17] So it's asking
certain questions.

[31:20] And then standard
prompting fail.

[31:22] And if you just
have a model that

[31:24] can reason like
Chain-of-Thought,

[31:26] it also fail here.

[31:28] Basically we have wrong answer.

[31:31] This is actually more dangerous
because you have a very

[31:34] convincing reasoning trace.

[31:36] That's wrong.

[31:38] So now let's look at if
you have this kind of loop

[31:41] think taking action,
think observation.

[31:46] So in this particular
example, the model

[31:49] thinks that it needs to search
Apple remote, since this

[31:52] is in the query, to find out
what it was originally designed

[31:55] to interact with Apple remote.

[31:58] Such a thought actually
induced search actions

[32:01] and gets a long description of
Apple remote from Wikipedia.

[32:06] In the second step,
the model actually

[32:08] uses reasoning to extract
the key information

[32:10] from that specific page.

[32:12] And they found that
Apple remote was actually

[32:15] designed to interact
with front row here.

[32:18] Then the model thinks
that maybe they

[32:20] should search front row to
find out what controls it.

[32:24] But may be the
specific Wikipedia page

[32:28] does not have such information,
but some other articles have.

[32:32] So this process
actually continues.

[32:34] In the third step,
the model actually

[32:37] uses reasoning to
recover from extraction

[32:40] and then search
front row instead.

[32:43] So when the model thinks that
they have the correct answer,

[32:46] they actually finish
the task and return it.

[32:49] So you can see that here the
reasoning traces actually

[32:52] induce and adjust
agent actions, which

[32:56] help agents obtain new knowledge
to support their own reasoning

[33:00] process.

[33:01] And then one thing
that I want to mention

[33:03] is that if you look at this,
a lot of the trajectory

[33:07] here is very intuitive,
interpretable,

[33:10] and somewhat factual.

[33:14] To show you how
this actually works,

[33:16] Chain-of-Thought is a
very straightforward

[33:18] prompting baseline.

[33:20] And then you can see that
compared to just doing

[33:24] actions which is act here, ReAct
actually perform act constantly.

[33:30] One thing is that if you
look at the failure case

[33:33] from different
reasoning paradigms,

[33:36] let's do a very
detailed breakdown.

[33:38] If you compare
Chain-of-Thought and ReAct

[33:42] in terms of failures
like reasoning error,

[33:45] actually ReAct is very high.

[33:47] Search result error,
ReAct is also very high

[33:50] because CoT does not
have search functions.

[33:53] Hallucination.

[33:55] Hallucinating the reasoning
traces or effects, ReAct is 0.

[33:59] And then Chain-of-Thought
is actually 56 here.

[34:02] So in general, hallucination
is a very serious problem

[34:06] for Chain-of-Thought and many
of those prompting techniques.

[34:09] And then ReAct with this
kind of reasoning module,

[34:11] taking actions actually
mitigate it a lot.

[34:16] So you probably
noticed that there

[34:18] is a term here called SC here.

[34:21] SC refers to self-consistency.

[34:25] This is related to
Chain-of-Thought

[34:27] as a prompting technique, and
it's a very intuitive trick

[34:30] you can use.

[34:32] So apparently you can prompt
the large language model

[34:35] using Chain-of-Thought.

[34:36] And instead of just
getting one of them,

[34:38] you can actually get a diverse
set of reasoning choices.

[34:42] You can aggregate by choosing
the most consistent answer

[34:45] in the final answer set.

[34:47] So this is a majority
voting to some extent,

[34:50] but from a consistency
perspective.

[34:54] So after self-consistency,
the process

[34:59] of actually making agent
better at reasoning

[35:03] happens very, very frequently.

[35:05] One of the very notable
examples is called reflection.

[35:10] Basically, the agents
are going to reflect

[35:13] through natural
language feedback.

[35:15] If you look at the left
figure here, so let's see.

[35:19] We have a current
trajectory generated here.

[35:21] This is the short-term
memory here.

[35:23] And then you can give
that to an evaluator.

[35:26] The evaluator is going to judge.

[35:28] Is this going to be
correct or incorrect?

[35:31] And then with those
feedback, the agent

[35:33] is going to do a
self-reflection.

[35:36] And then with those
self-reflected content

[35:39] together with the
experience, they

[35:40] can actually change what
the actor is going to do

[35:44] or going to see.

[35:45] So this is a very
earlier idea of lighting

[35:49] models do self-reflect.

[35:52] Just to show you that if
you look at all the steps

[35:55] after the evaluation,
the reasoning, sorry,

[35:58] the reflection is actually
quite interesting in terms

[36:01] of why the model
thinks such error

[36:04] occurred or they received this
particular evaluation outcome.

[36:10] So a reflection actually
works pretty well.

[36:13] I think if you reflect
on the process,

[36:15] it actually reduce
errors by using

[36:18] self-reflection to really
distill long field trajectories

[36:22] into relevant
experience or rubrics

[36:25] or reward signals
that can be used

[36:28] as self-hints in the future.

[36:31] So from the figure, you
can see that compared

[36:34] to ReAct only with reflection,
it's definitely doing way better

[36:39] than the ReAct system.

[36:41] And similarly, in terms of the--

[36:43] I think this is the
hallucination-- you can also

[36:46] see that it reduced
hallucination

[36:48] a lot with this kind of
self-reflection technique.

[36:54] How is this behavior
introduced to the model?

[36:57] Is it included as a
part of the problem,

[37:00] or there's some fine-tuning
or training steps

[37:03] to bring them into the weights?

[37:05] Yes.

[37:05] Great question.

[37:07] So reflection and many other
similar self-reflection

[37:10] techniques does not involve
fine-tuning or any kind

[37:13] of gradient updates.

[37:15] Most of them are actually
implemented using a prompt.

[37:20] One minor thing I
want to point out

[37:22] is that if you read
the reflection paper,

[37:25] it actually keep you in
this word called reinforce.

[37:28] But reinforce is
actually not achieved

[37:30] from a reinforcement
learning perspective.

[37:32] It's only from a
self-reflection prompt aspect.

[37:37] In this slide that you showed
where you compared ReAct

[37:40] with Chain-of-Thought, the
results, hallucination was 0.

[37:44] How is that different
from reasoning?

[37:46] If there's a reasoning error
and which is considerably high,

[37:49] how is hallucination 0?

[37:51] Yeah, so there could
be multiple failures.

[37:55] Sometimes you fail not
because of hallucination

[37:57] but because such label
may have ambiguity

[38:01] or because you
need to make sense

[38:07] from the current
context, which is not

[38:10] about getting the right tool or
information or things like that,

[38:15] but more about interpreting
what has happened so far.

[38:19] So they are slightly
different in this process.

[38:21] So the one that you're saying
would be reasoning error.

[38:24] Yes, so that would
be reasoning error.

[38:26] Yeah.

[38:29] So the main difference between
Chain-of-Thought and ReAct

[38:32] is the fact that ReAct
you can act and observe

[38:36] but is generally the
same reasoning strategy.

[38:39] It's just Chain-of-Thought
is just like prompting

[38:41] and there's not much--

[38:42] they can't really
[INAUDIBLE] its work?

[38:45] Yeah.

[38:45] So in Chain-of-Thought,
if you-- we

[38:49] will do a more deep dive
into the reasoning modules

[38:52] in two weeks.

[38:54] So in Chain-of-Thought, it's
literally just like one prompt,

[38:56] one pass.

[38:58] In ReAct, you can think
about it as a loop.

[39:01] So the model think,
look at the observation,

[39:04] think, take action, and then
think, look at that observation,

[39:08] take action.

[39:09] So it's like a multiple step.

[39:11] It's a loop.

[39:11] So in this way,
the model actually

[39:13] can revise its own errors
or getting new information

[39:17] to update themselves.

[39:18] So this kind of
richness is something

[39:20] Chain-of-Thought does not have.

[39:21] [INAUDIBLE] that
loop, it can decide

[39:26] whether to think out of it?

[39:28] Yeah.

[39:30] OK.

[39:30] Maybe last question.

[39:31] Yeah?

[39:33] Do you think the reflection
process is the distillation

[39:38] of the model itself?

[39:40] If so, is the distillation
going to cost--

[39:43] is this a reflection of the cost
of overfitting to its action?

[39:50] Yeah, so one thing I want to
clarify is that I do use the--

[39:55] sorry, not this page.

[39:56] I do use the word
like distill here,

[39:58] but this is actually not a
very classic distillation

[40:01] we are talking about.

[40:02] Here, it's really about you
have a lot of trajectories

[40:05] of what happened so far.

[40:07] And then in general, you
may just rely on models

[40:10] to interpret what
has happened so far

[40:12] and then do actions
based on that.

[40:15] With self-reflection, the
model actually think about that

[40:18] and then try to compress that
into something that's shorter.

[40:22] So in this process, one
word to use is distill.

[40:27] You can also use it as
abstract or synthesize.

[40:30] So this is very different
than the classic distillation

[40:33] technique which is more about
getting output from other models

[40:38] and then do training
on top of them.

[40:41] OK.

[40:42] Let's continue.

[40:43] So in addition to this kind of
reflection, self-consistency,

[40:48] another trend that's
very interesting

[40:49] is actually around
multi-agent debate.

[40:53] So earlier days,
people, researchers

[40:55] used multi-agent debate to
improve reasoning performance.

[41:00] And this literally
means that you

[41:02] are going to have
multiple agents doing

[41:04] the same task solving.

[41:06] And then after
each round, you let

[41:08] them read each other's reasoning
and let them debate just

[41:12] like how you talk about some
decisions with your teammates.

[41:16] And then agents can
actually really leverage

[41:19] those diverse
perspectives and maybe

[41:22] make some final decision here.

[41:25] I think this multi-agent
technique in earlier days

[41:29] is a very useful
prompting method.

[41:34] The assumption at that time
is that each individual model

[41:37] is not strong enough.

[41:39] So we actually use this
kind of multi-agent setup

[41:43] as a way to prompt the model.

[41:45] When models get
very powerful today,

[41:47] if your only goal is to
get a performance boost,

[41:50] I think a multi-agent
is not going

[41:52] to help you a lot in terms
of performance boost.

[41:55] But maybe there are other design
choices or design considerations

[41:59] that we can benefit from
multi-agent, such as efficiency,

[42:03] such as data access control.

[42:05] Maybe this agent is
particularly designed

[42:08] to take care of health
care, and that agent

[42:10] is designed to help you
with sensitive information,

[42:13] et cetera.

[42:16] So after multi-agent,
another way

[42:18] to really improve
this kind of reasoning

[42:22] is actually to
set up many agents

[42:25] and then use an orchestrator to
orchestrate the different agents

[42:29] to work towards the same task.

[42:31] So this is a very earlier
system from Microsoft

[42:34] called Magentic here.

[42:38] Basically, if you
have a bigger task,

[42:40] the orchestrator is
going to break them down

[42:42] into different components.

[42:43] And you can see that the
first part gets assigned

[42:46] to a file server
and then to a coder,

[42:49] and then to a computer
terminal, et cetera.

[42:52] And each agent basically takes
care of each specific task.

[42:55] And then in the end, you can
actually combine all of them

[42:59] and then provide a
final answer to users.

[43:03] So this is about planning
and reasoning module.

[43:06] We will go deep into this
process in week 2 and 3.

[43:11] The next component that
I want to quickly mention

[43:13] is around the memory here.

[43:16] You can actually do a lot
of very creative design

[43:19] in terms of how we want
to make memory work.

[43:23] Just to briefly share
why we need a memory.

[43:28] Two reasons.

[43:29] First is [INAUDIBLE] our context
window for large language models

[43:33] are getting bigger and bigger,
still context window cannot hold

[43:38] all the event stream
happen so far.

[43:41] So if you think about
long horizon task

[43:43] we are talking about today
where agents can actually

[43:45] work on your project for
more than three hours, that's

[43:49] actually a lot of data.

[43:51] And it's really hard to feed
that into context window.

[43:55] The second is that even
if that's possible,

[43:59] it may be really
hard for the agent

[44:01] to figure out what is a relevant
piece of information I should

[44:04] use.

[44:05] Think about that if you
have 1,000 documents there,

[44:08] you store them in your context.

[44:10] And then basically
each time, if you

[44:13] need to find the
right document, this

[44:16] is actually very time-consuming
since you have such a big search

[44:20] space.

[44:22] So the bottom is actually
a very interesting design

[44:25] from the generative agents,
the Smallville project,

[44:29] where they were trying to
build agents that can simulate

[44:32] people living in a small town.

[44:34] And then in their
design, they actually

[44:36] need to use the memory
stream to make sure

[44:38] that we can keep track of what
happened to each individual

[44:43] so that the story can continue.

[44:46] There are different types
of memories you can design.

[44:50] If you think about what
kind of things to store,

[44:54] episodic memory here literally
refers to restore everything,

[44:58] like, raw logs, every
sentence the agent

[45:01] has shared with
users, every sentence

[45:04] that the users have
provided to agents.

[45:08] Semantic memory
means that instead

[45:10] of thinking about
this kind of raw logs,

[45:13] we may want to remember
semantic events,

[45:17] since those may be more useful.

[45:20] Procedural memory,
you store scales.

[45:23] Instead of all the specificity,
you remember, what is the scale?

[45:28] What is the procedure of how
we do certain type of things?

[45:32] So if you go deep
into this process,

[45:35] this is actually an
example of episodic memory.

[45:38] You can see that literally we
are storing every single time

[45:41] step and then what
happened at that time step.

[45:46] With semantic
memory, we actually

[45:48] can do some synthesis of
what happened over the agent

[45:52] trajectories.

[45:53] And then literally you have this
a small summary box as a way

[45:58] to remember what has happened
in the last several minutes.

[46:02] So this is what we mean
by semantic memory.

[46:06] Procedural memory, you can
actually check out this Voyager

[46:09] paper from NVIDIA
where they were

[46:11] trying to teach agents to play,
I think this Minecraft here,

[46:17] where if the agent
figure out how

[46:19] to use a new skill or
new tool, you actually

[46:23] want to abstract
that into a skill

[46:25] and store it in
your skill library.

[46:27] And then whenever you have
a new task, you want to see,

[46:30] do I have a skill that I can
use from a skill library?

[46:33] If so, then I'm going to
retrieve it and use it.

[46:36] So this is more from a
procedural perspective rather

[46:39] than all the logs that
have happened so far.

[46:44] So this is about a memory.

[46:45] And then another very important
thing is about the tool use

[46:48] here.

[46:50] So tool use, I will talk
about this next Wednesday.

[46:54] But just to give you a quick
highlight of what this means,

[46:59] we all know that right
now you can actually

[47:01] enable agents to use different
types of tools such as search,

[47:06] such as coding agent, et cetera.

[47:09] So in earlier days, the
tool use is actually

[47:13] triggered in the actual
decoding process.

[47:16] So if you read the right
part, the sentence--

[47:20] or maybe let's just
read the first one.

[47:23] "The New England Journal
of Medicine is a registered

[47:26] trademark of--" So if you need
to do some kind of information

[47:31] generation, at this point, we
may want to trigger a special

[47:37] token called a QA.

[47:39] And then the QA literally
is, who is the publisher

[47:42] of this journal of medicine?

[47:44] And then you got
the specific answer.

[47:46] And then you use that answer
in the process of generation.

[47:50] So in other words,
earlier when we

[47:53] want to teach model
how to use tools,

[47:56] we are actually
learning where to call

[48:00] an API, when to call it,
which API to call, et cetera.

[48:05] So Toolformer was actually
the first ish work

[48:09] that does this kind of
teaching LLMs to use tools.

[48:14] You probably can enumerate
how many tools they can use.

[48:18] At that time, I think
there are only five tools

[48:21] that we teach to agents.

[48:23] Agents can use a
calculator here.

[48:25] They can use a question
answering system.

[48:27] They can use search engine.

[48:28] They can use a
translation system.

[48:30] They can use calendar.

[48:32] So that's a very
limited set of tools.

[48:35] Today, I think our
agents can actually

[48:38] use a wide range of
tools, but they actually

[48:41] all get inspired on top
of setups like this.

[48:46] More recently,
GORILLA from Berkeley

[48:50] actually tried to teach LLMs
to use solvents of APIs.

[48:55] So what they did is that they
actually look at Hugging Face,

[49:00] Torch Hub, and also
TensorFlow Hub,

[49:03] where there are over 1,600 APIs.

[49:06] And then they basically generate
the synthetic data from that

[49:10] and then trained a 7 billion
parameter model on top of that.

[49:15] At the inference time, if
we look at this example,

[49:17] if the user says that
I want to see some cats

[49:21] dancing in celebration,
then you are

[49:24] going to do a retrieval here.

[49:26] Probably you are going to
use a Stable Diffusion.

[49:28] And then you get
this image out here.

[49:32] Otherwise, if you
think about this,

[49:35] the base model needs
to have the capability

[49:37] to understand this and then
give this kind of output

[49:40] of the image.

[49:41] But now we can
actually delegate that

[49:43] to an external tool such
as Stable Diffusion.

[49:46] Then we can get the task
done without requiring

[49:49] the underneath model to even do
this kind of image generation.

[49:56] With GORILLA, I think the
results are quite impressive.

[49:59] So if you look at the
reduction to hallucination,

[50:02] it's actually pretty good,
very few hallucinations

[50:06] and pretty high accuracy.

[50:09] I think this
actually makes sense

[50:11] because without so many
tools use or understanding,

[50:15] you actually have to rely
on the model themselves

[50:18] to do this task.

[50:19] But now you can actually do
more factual and reasonable

[50:23] generation.

[50:25] So this is around the tool use.

[50:27] I will go deep into
that next Wednesday.

[50:31] So if you put
everything together,

[50:33] this is actually the skeleton
of an agent, LLM Core

[50:37] that a reason and a plan.

[50:38] The memory actually
carries states

[50:41] across steps and different task.

[50:44] Tools to reach out to diverse
APIs, available tools we have,

[50:50] and also an environment that
agents can actually take actions

[50:53] and observe states from.

[50:56] So every agent you
are going to build,

[50:59] whether it's going to write
code or browse the web

[51:02] or run the terminal, it's some
kind of version of this diagram.

[51:06] And what differs is actually
how each box is implemented

[51:10] and how well the
pieces fit together.

[51:13] So that's going to be a
lot of the key aspects we

[51:16] are going to cover later.

[51:20] Any quick questions
until this point?

[51:25] How does anyone
know what memory is?

[51:28] So this is actually related
to the memory design.

[51:33] If you just think about how
to design memory systems,

[51:37] instead of letting them to
decide what to memorize,

[51:41] the episodic memory
literally just

[51:43] tells them to
remember everything.

[51:45] So everything happened so far.

[51:47] So this is more from a
heuristic perspective.

[51:49] And semantic
memory, you may need

[51:51] to have some separate module
to teach them that instead

[51:57] of remember everything,
you may want

[51:59] to remember important
information.

[52:01] Then you can actually give
demonstrations of what

[52:03] is important information.

[52:05] What is the format you want?

[52:07] What is the format you want
to even store in your memory?

[52:11] So those are the
design choices we are

[52:13] going to bring to the process.

[52:16] This is also a
place where things

[52:17] can get a little bit tricky.

[52:20] There was this example I
think-- do I have it today?

[52:24] I don't have it on
my slides today,

[52:26] but earlier this
year, some people

[52:29] are using OpenCloud
to manage their email.

[52:32] And then all of a sudden,
OpenCloud actually started

[52:35] to delete this user's email.

[52:37] Despite the user says
please stop, please

[52:40] do not delete my email,
it is still continuous.

[52:44] The user actually specified
in the very beginning

[52:46] that whenever you do such
actions, please confirm with me.

[52:50] But then it's just
like so interesting,

[52:52] like OK, why it happens and when
the model actually is not even

[52:56] listening to instructions.

[52:58] It turns out that
this is actually

[52:59] a failure in the context
memory compression stage,

[53:03] because you want to
make sure the memory is

[53:05] stored in a very efficient way.

[53:07] So you let the model decided
to just keep track of all

[53:10] the important information.

[53:12] Confirm before you do action
is not perceived as important

[53:17] from the agent perspective.

[53:18] So this actually leads to a
lot of the email deletion.

[53:21] So I think this is a
very good question.

[53:24] It's going to be a very
critical design of how

[53:26] we make sure the
memory is faithful

[53:29] and also can enable very
reasonable inductions.

[53:34] OK.

[53:37] If there is no more
question, we will continue.

[53:41] So next, I want to talk
about compound AI systems.

[53:46] We just put together
different pieces.

[53:48] But now if you think about
this, how real products actually

[53:54] combine with other
components, this

[53:58] is what we call
component AI systems.

[54:00] I'm going to briefly talk
about different modules here,

[54:03] but we have specific
lectures to go deep there.

[54:07] I think one thing
people often get

[54:11] overwhelmed is that when
we think about agents,

[54:13] there seems to be a lot
of components happening.

[54:16] There are LLM core.

[54:17] There are plenty memory to
use, environment, et cetera.

[54:21] And to keep all of
those manageable,

[54:25] it helps to think
about engineering

[54:28] as some more principled
ways of understanding.

[54:32] So we are going to divide
this into three layers.

[54:35] And our course is also
set up in similar order.

[54:39] First, I think this
is the system layer.

[54:41] This is the architecture
which components agent has

[54:45] and how they connect.

[54:47] This is just everything
that I have covered so far.

[54:49] The second layer is the data.

[54:52] That's how the agent actually
learns from or is prompt with.

[54:56] Here you will have training
examples to train agent,

[55:00] such as what we will cover
in Swiss miss, demonstration

[55:04] of the task, or maybe just
the context we give to agents.

[55:09] The third layer here
is the evaluation.

[55:11] That's how we actually evaluate
whether the agent actually

[55:15] works and also includes
the metric itself.

[55:19] Choosing the wrong metric can
make a weak agent look nice.

[55:24] So the metric actually
deserves a lot of care

[55:27] when we think about this.

[55:29] So most of what we are going
to cover in this course

[55:31] will be mapped into
those three layers.

[55:34] And when an agent
is not doing well

[55:37] or your agent is not
working as expected,

[55:40] I think a good first question to
ask is which layer the problem

[55:45] may occur.

[55:46] Is it in the system?

[55:47] Is it in the data, or
is it in the evaluation?

[55:49] This is also a guiding
principle for us

[55:51] to debug how to make
the agents better.

[55:55] So let's just quickly go
through the system layer here.

[56:00] A key design choice
at the system layer

[56:02] is who decides the steps.

[56:05] Who decides like memories,
things like that.

[56:08] Is that going to be
the agents, or is it

[56:12] going to be something else?

[56:14] And I want to make this
differentiation here of workflow

[56:17] versus agents.

[56:19] Both are what people refer
to as compound AI systems.

[56:24] That is a large model
plus other components.

[56:27] You may encounter those two
terms in different contexts.

[56:30] So here, a workflow is going
to be maybe like it's just

[56:36] going to fix certain steps.

[56:39] Examples such as
agent lists which

[56:41] fix a GitHub issue in a
very fixed set of stage,

[56:45] like finding the file,
writing patch and doing

[56:50] tests, et cetera.

[56:51] So the large language model
works inside each stage,

[56:54] but they never
pick the next one.

[56:56] So it's actually a script.

[56:58] It's like a fixed order
of how they do stuff.

[57:01] In the agent side
team, the larger model

[57:04] they set for itself.

[57:06] For example, in three
agent, it actually

[57:08] choose which files to open,
what to run, and when it's done.

[57:13] So you can see that it's
actually more flexible.

[57:16] It also gives more
responsibility

[57:18] to the model underneath it.

[57:22] So workflow-- now if I just
stop here, you probably

[57:26] think about, OK, then why do
we even need a workflow here?

[57:30] So I want to just
share one example here

[57:33] that is workflow agents,
sorry workflow system

[57:37] can actually be
very, very strong.

[57:39] So on my screen, this
is actually AlphaCode2.

[57:42] It actually generates up to
millions of candidate programs

[57:46] and then test and rank them.

[57:48] And then it reached almost
like 87% of human competitors.

[57:55] And this is a huge
jump from AlphaCode1.

[58:00] The next common
workflow pattern I think

[58:04] has been widely used
in industry in the past

[58:07] is called the Retrieval
Augmented Generation, RAG.

[58:10] This has a lot of things to do
with open question answering.

[58:16] Basically, RAG
connects large models

[58:18] to external knowledge
stores in real time.

[58:21] So if you have a specific query
that may rely on the weather API

[58:26] or weather website,
then you go there,

[58:29] read the related
content, use that

[58:31] to augment your current
query as context.

[58:35] And then on top of
that, do generation

[58:38] to give users more factual
and consistent answers.

[58:44] What actually happens
in a single tool call?

[58:48] I mean, previously I mentioned
about the algorithms.

[58:52] If you think about
what actually happens

[58:54] from a system perspective, there
are actually multiple stages.

[58:58] First, the model
needs to select a tool

[59:00] from the schemas it has from
the context and then arguments.

[59:05] It needs to fill in all the
text fields from the task.

[59:10] Validator means
that those arguments

[59:12] need to be checked
against the schema.

[59:15] Sometimes there may be
enforcement with constraint

[59:18] decoding so that the model
actually cannot produce

[59:21] an ill-formed call here.

[59:23] Final step is execution
to gather round and then

[59:28] usually in a sandbox.

[59:29] We'll go to the sandbox
in a few minutes.

[59:32] And then the results
go back to the context.

[59:35] And then the example
in the bottom

[59:37] actually shows you a
specific tool call.

[59:39] So if the user question is,
what does test.py contain?

[59:44] And you can see that the model
actually read file, and then

[59:48] fill in the path information,
and then the path

[59:51] is checked as a string.

[59:53] And then the file contents
actually come back

[59:55] from the model
for users to read.

[59:58] So this is actually what's
happening from an execution

[60:00] perspective.

[60:03] I think the reality is that
if every AI application had

[60:07] to write a very custom
integrations for every tool,

[60:11] then nothing will
really scale up.

[60:14] The Model Context Protocol, MCP,
is actually a standard protocol

[60:18] to make sure such
connection can happen.

[60:22] So on the left side, you can
see that we have different AI

[60:25] applications such as Claude
Desktop, IDE, and code

[60:30] editor such as Claude Code.

[60:33] On the right, those are
different data sources

[60:36] and tools, database such as SQL,
Google Drive; deployment tools,

[60:42] or even like productivity tools
such as Slack, Google Maps, et

[60:45] cetera.

[60:46] So MCP sits in the middle
as a standard protocol

[60:50] with data flowing
in both directions.

[60:54] You can then think
about how to build

[60:56] a tool once MCP server and
any MCP client can be set up

[61:02] and use it.

[61:04] We will go back to
this next class.

[61:08] So in the next five
minutes, I'm going

[61:10] to quickly mention
about the key challenges

[61:12] here, just to share with you
that despite the agent being

[61:16] very impressive,
I think they also

[61:19] create a lot of
emerging challenges

[61:22] for us to be aware of.

[61:25] So to give you a
very quick overview

[61:27] of what we are going
to cover, reliability.

[61:31] If you build agents,
you know that there

[61:34] is going to be a lot of
error compound cascade.

[61:39] To train agents,
the reward signal

[61:41] sometimes can be very sparse.

[61:43] It's usually like a
long horizon task.

[61:45] Very, very expensive
to do rollout.

[61:48] The long-horizon
also gave us a lot

[61:50] of challenge in terms
of context increase.

[61:54] Safety is a big topic.

[61:56] Also, evaluation
is very, very hard.

[61:58] It's probably like I think it's
one of the undervalued aspect

[62:02] when we think about agents.

[62:04] I want to give you a
few quick examples.

[62:06] So reliability
versus evaluation.

[62:10] This is actually an
effort from Princeton.

[62:12] They were really
trying to understand

[62:14] that is the accuracy in the
performance we are seeing,

[62:19] a truthful reflection
of what's happening.

[62:21] And they find the three
dimensions such as consistency.

[62:24] If you let the agent
run multiple times,

[62:28] do they give you
the same outcome?

[62:30] Robustness.

[62:31] What if we add a little
bit of perturbation?

[62:33] How do agents actually respond
to those small, realistic

[62:37] and even irrelevant information?

[62:40] Predictable.

[62:41] When agents fail
to do something,

[62:43] do they feel because some
unpredictable reasons?

[62:47] Or can we actually
understand it,

[62:50] like, legible and recoverable?

[62:54] Just to show you some
of those numbers,

[62:55] if you look at
the accuracy, this

[62:57] is actually ranked
in terms of models.

[63:00] But if you look at
the reliability,

[63:03] those scores do
not have a trend,

[63:06] which means that there is
a gap between capability

[63:10] and reliability.

[63:12] The most powerful agent may
not be the most reliable agent.

[63:16] And this is something we
need to keep in mind when

[63:18] we are doing evaluations.

[63:20] So it's not only just about
the model performance,

[63:22] reliability, efficiency.

[63:25] Similar argument
to hold that when

[63:27] you think about harness audit.

[63:29] Recent work showed that
if you audit those agents,

[63:34] the green bar here refers
to the task completion,

[63:37] and then the colored bar
refers to the harness safety.

[63:41] And you can see that the safety
dimension is just way lower

[63:44] compared to the task completion.

[63:48] There is a very
interesting example

[63:50] that I also want
to share with you.

[63:52] So we talk about the agents.

[63:54] They do stuff, but they
may also have issues.

[63:59] This is an example
from Operator,

[64:01] which is a computer used agent
introduced by OpenAI in January

[64:05] of 2025.

[64:07] The user said that my most
frustrating experience

[64:10] with Operator was my first
one-- trying to order groceries.

[64:14] The user said, help me buy
groceries on Instacart,

[64:16] expecting it to ask
some basic questions,

[64:19] such as where do I leave?

[64:20] What store do I usually
buy groceries from?

[64:22] What kind of things do I want?

[64:24] It didn't ask me any of that.

[64:26] Instead, Operator opened
the Instacart in the browser

[64:29] and begin searching for milk in
grocery stores located in Iowa.

[64:33] So think about this.

[64:35] The agents can actually
navigate the web.

[64:38] They can use your credit
card to make purchases,

[64:42] but in this process, they are
making a lot of assumptions,

[64:46] and they didn't really
have this kind of awareness

[64:48] to collaborate with people.

[64:50] So this is actually a failure
from the interaction side.

[64:55] The next thing I
want to show you

[64:57] is that the robustness
of agents is actually

[65:00] going to face a lot of challenge
when they enter our real world,

[65:04] because we just have
so many dark patterns.

[65:07] In this particular example,
researchers actually

[65:10] just pop up this--

[65:12] I mean, we have a lot of
pop-ups on different websites.

[65:15] So we pop up this
kind of blank box.

[65:19] Nothing adversary or
malicious is there.

[65:22] But then because of
this distraction, agents

[65:24] actually fail to complete
their task 87% of the time.

[65:30] This is what we call
adversary attack.

[65:32] And this is really interesting.

[65:34] If your agent goes to do
shopping for you and then

[65:37] a pop-up from the website
actually could get your agents

[65:40] distracted, and they cannot
finish the original task.

[65:45] The other example that
I want to show you

[65:47] here is actually from a privacy
and security perspective.

[65:50] So this is an agent
that's supposed to write

[65:53] a weekly report for workers.

[65:56] It actually did a great job
of how many lines of code

[65:59] you wrote, how many
features you launched.

[66:01] It also mentioned that you
had lunch with a recruiter

[66:04] from a different company.

[66:06] So this actually highlighted
something that's very critical,

[66:10] that is privacy today.

[66:13] We give information, all
our information to agents,

[66:16] to AI systems.

[66:17] They know everything about us.

[66:19] They probably know that
PII information are not

[66:21] something they
should use, but a lot

[66:23] of the sensitive
personal information

[66:25] can really be consequential.

[66:27] And there's no way
to teach agents

[66:29] about how to handle
different access control.

[66:34] This is another important
topic we will go deep later.

[66:39] Misalignment and synchronous.

[66:41] If you look at the
left side, this

[66:43] is actually called an
insincere [INAUDIBLE].

[66:47] So basically the agent think
your writing is terrible,

[66:52] but they do not want
to hurt your feelings.

[66:55] Instead, the agent
just says that they

[66:56] will give it a 5 out of 5.

[66:58] So this is also a reminder that
you should not only just give

[67:01] your homework to
agents, because they

[67:02] will see great things about
it without really giving you

[67:05] feedback.

[67:07] The second part is actually
about the model hacks

[67:09] its own code.

[67:11] So the model is supposed to
help the user check, reinforce

[67:15] the learning.

[67:16] And then the agent
internal thinking

[67:19] is that oh, I saw there
is this unit test which

[67:22] can check the reward function.

[67:24] And I cannot modify that, but
I could change the unit test

[67:28] first.

[67:28] So they change everything
here so that everything

[67:31] looks good on the surface.

[67:35] I think probably the most
surprising thing, very close

[67:38] to us is what happened in July
around this OpenAI hacking

[67:44] incident.

[67:45] And this is actually a very
interesting demonstration

[67:48] of how we think about agent
safety moving forward.

[67:52] So what happens is that
OpenAI has this sandbox agent,

[67:57] and they are asked to
do an impossible task.

[68:02] They get stuck.

[68:03] And then agents start to
explore its environment

[68:06] and looking for other ways
to maybe get a higher reward

[68:09] or cheat on the task.

[68:11] They find out that there is
actually a message board where

[68:14] over 1,000 agents collaborate
to cheat on their task.

[68:18] And then they just
join with each other.

[68:21] And then basically a lot
of things have happened.

[68:26] Just to show you what happened,
I think within a few days,

[68:30] it actually sent over 17,000
attacks to Hugging Face

[68:34] infrastructure.

[68:36] Here if you show, the blue color
refers to intended solution.

[68:42] And then you can see the
released target which

[68:44] is more about
manipulation, understand

[68:47] the manipulate
error, sorry, logs,

[68:49] and then attack Hugging Face.

[68:51] You can see the volume of
what happened in the process.

[68:55] So I think this is indeed a
very concerning topic for us

[68:59] to reflect, especially
given that agents can now

[69:03] function for so many hours
and maybe even longer.

[69:08] So with that, this is a brief
overview of the introduction

[69:13] to agentic AI.

[69:15] I think we did a
history of agents

[69:18] and then different components
of agent architectures.

[69:21] We talk about the
compound AI systems

[69:24] and a lot of key challenge
we are going to go through.

[69:27] With that, thank you all,
and see you next class.
