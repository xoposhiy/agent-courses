# Lecture 4 transcript: Tool Use & Function Calling

[Course index](../../README.md) · [Original source](https://youtu.be/s0S38lz6O7M) · [Raw file](../../raw/videos/s0S38lz6O7M.json)

Retrieved: 2026-11-13T16:19:38.327577+00:00

[00:05] Today our topic is going to be around

[00:07] the two years.

[00:09] With that, let's go to our content

[00:12] today.

[00:13] First, I'm going to wrap up a rag that

[00:15] we covered the last week in 5 minutes

[00:18] and then we are going to move towards

[00:20] two years

[00:22] particular around the why we need to

[00:24] consider two years for agents.

[00:27] What are tools and how to get a model to

[00:30] learn what type of tool to use.

[00:33] And then how can we actually scale to

[00:36] many many different type of tools we

[00:37] have.

[00:39] We will then shift from how to teach

[00:41] model to do it to how to have a standard

[00:44] that people can use different type of

[00:47] tools from a standard interface aspect

[00:50] where we'll cover rest,

[00:52] function calling and MCP.

[00:55] The last part of this lecture will cover

[00:58] many different type of function call and

[01:00] the two years data sets and evaluations.

[01:03] So hopefully by the end of this lecture

[01:05] you understand why we need tools,

[01:08] how model learn to call them and how

[01:11] tools are exposed through standard

[01:13] interface and how to use is validated.

[01:17] So with that, let's um

[01:20] coming back to what we were talking

[01:21] about the last week.

[01:23] So I talked about the rag. Rag is more

[01:26] from a design principle perspective

[01:29] where

[01:30] in the process of answering a question

[01:32] or um

[01:34] working on a task, we can actually do

[01:36] retrieval and then use those retrieved

[01:38] content to better facilitate the current

[01:41] task. So that's rag and in addition to

[01:45] many of the algorithm we have learned, I

[01:47] want you all to pay attention to issues

[01:49] with rag because this is where rag

[01:52] actually fail.

[01:54] On the retrieval side, as we mentioned,

[01:56] um

[01:57] maybe

[01:58] um agents actually some information

[02:01] which they should not have access to.

[02:04] So, that's called a permission leak.

[02:06] On the reader side, um, there is this

[02:08] phenomenon called a lost in the middle,

[02:10] which I will cover in the next few page.

[02:13] Uh, distraction. Agents get distracted

[02:15] by very similar but irrelevant content.

[02:19] The real world also has a lot of like

[02:22] conflicting knowledge. So, agents may,

[02:25] uh, fetch information that cover

[02:27] different aspects. For queries such as,

[02:30] is drinking milk good for my health? You

[02:33] may get articles that talk about the

[02:35] benefits. There are also a lot of

[02:37] articles talk about,

[02:39] um, drawbacks. So, how would the agent

[02:42] actually take care of this conflicting

[02:44] evidence? It's actually a big challenge.

[02:47] On the loop side, so, um, if you think

[02:49] about the rag, it's like retrieve and

[02:51] then read and then generate. So, this is

[02:54] actually a compound system. Uh, some of

[02:57] the errors or mistakes agents made

[02:59] earlier may also lead to, um,

[03:03] issues in the later stage.

[03:05] And then, more importantly, we will

[03:07] cover this detailedly later this

[03:09] quarter, is around the prompt injection.

[03:12] That is, what if, um, bad actors

[03:14] actually decided to inject something,

[03:18] uh,

[03:18] negative or malicious in the retrieved

[03:21] documents. And this actually will

[03:23] destroy or influence your rag system.

[03:27] So, I want to go deep into one part here

[03:30] called the lost in the middle, which is

[03:32] actually a very, uh, big issue rag used

[03:35] to suffer from.

[03:38] So, let's get it started.

[03:40] Uh, so, this is a very simple setup. Uh,

[03:44] if you read this example, the prompt

[03:46] basically says that, let's write a

[03:48] high-quality answer for the given

[03:51] question using only the provided search

[03:53] results.

[03:54] And then, what we are going to do is

[03:56] that we give you many documents here.

[03:58] Document one, document two, document

[04:00] three. And then, the question is

[04:02] supposed to read all these content and

[04:05] then

[04:06] retrieve the right document and then do

[04:08] the question answering.

[04:10] So here you can see that a document two

[04:12] is correct as I bolded them here.

[04:15] So the question now is

[04:17] if this is how we do it, why don't we

[04:20] just give

[04:22] a

[04:22] question answering system a lot a lot of

[04:25] documents? We can literally give the

[04:26] internet here if the context window

[04:29] permits.

[04:31] And also what happens if we have instead

[04:34] of three but many many many documents?

[04:37] And also what if the position of the

[04:40] correct document is not the two, it's

[04:42] actually 13, 43 or just like somewhere

[04:46] in the sequence?

[04:48] Would that change the rag results?

[04:52] So the answer is yes, and this is a very

[04:55] kind of classic lost in the middle

[04:58] results. So if you look at this trend,

[05:01] many of them is more like this kind of

[05:03] like U-shape.

[05:05] Where if the correct document is in the

[05:08] top or in the

[05:10] in the most recent or the last position

[05:13] of your sequence, models are very likely

[05:15] to use them well. But if the correct

[05:19] document is somewhere in the middle of

[05:21] the sequence, you actually get worse the

[05:24] performance here.

[05:26] So this is actually very surprising.

[05:28] This is also what we call a position

[05:29] bias when we think about rag.

[05:32] In the bottom I show you some numbers.

[05:35] So basically if you just without a rag,

[05:37] you just do close book

[05:40] QA,

[05:41] GPT-3 turbo here got a result like 56.

[05:45] And then if you could have given them

[05:47] the relevant document, you can actually

[05:49] boost this number to 88, which is pretty

[05:51] high. This is why rag is useful. But

[05:54] then if you look at the in the middle

[05:56] part, we actually really just like

[05:59] degraded to even without a search. So

[06:02] this is quite a surprising and uh

[06:06] the answer the correct answer is

[06:08] actually in the context.

[06:11] But models actually ignore it.

[06:14] So, this is the very classic uh um

[06:17] lost-in-the-middle phenomena.

[06:20] Um so, the same paper, but I'm going to

[06:23] instead of thinking about the positions,

[06:25] let's look at how many documents we can

[06:28] retrieve and how does that affect the

[06:30] results.

[06:31] So, the yellow line here is uh the

[06:34] system the authors built, that is um how

[06:37] often the answer is somewhere in the

[06:40] retrieved set. And you can see that it

[06:42] is slowly grow to about 90%

[06:46] at around the 50 documents here. And I

[06:49] think the other lines here are reader

[06:52] accuracy.

[06:53] Uh most of the reader actually saturates

[06:55] after 10 to 20 documents. And around the

[06:59] like 50 to 60% here, and some even like

[07:02] go down here.

[07:04] So, the gap between the yellow and the

[07:06] rest is the evidence that models

[07:08] actually cannot use. So, more retrieved

[07:11] documents do not mean better results.

[07:15] So, you need to pick this kind of like K

[07:17] carefully and then re-rank etc. So, all

[07:21] of this is trying to share with you that

[07:23] even for a algorithm or design principle

[07:26] as simple as rag, it may suffer from

[07:29] certain issues such as

[07:31] lost-in-the-middle or such as they

[07:34] cannot actually use all the retrieved

[07:37] documents there.

[07:40] If we go this a little bit uh deeper, um

[07:43] the reason why people like rag is uh

[07:46] earlier days as model hallucinates, we

[07:49] want the evidence, we want the

[07:50] citations.

[07:52] Um if they tell us that coffee is not

[07:54] good for our health, they may need to

[07:57] give us the article that supports that.

[07:59] This is a mechanism called a citation,

[08:02] and this is actually a earlier approach

[08:04] to deal with hallucination.

[08:06] But uh the interesting part here is that

[08:10] because citation is also generated by

[08:13] LLMs, citation itself can also be

[08:16] hallucinated. That is, you were supposed

[08:19] to get a citation to support your um

[08:22] answer, but your citation itself is also

[08:25] wrong. This is why you probably have

[08:27] heard the uh lawyer situation where they

[08:30] use LLMs to write a court case where

[08:33] they were presented with very convincing

[08:36] um instance, but it turned out to be a

[08:39] hallucination.

[08:41] Um if you kind of quantify this from a

[08:44] rigorous perspective, uh so on my screen

[08:47] those two tables

[08:49] um actually are are from the original

[08:51] Lost in the Middle paper. And they

[08:54] actually look at the different uh search

[08:55] engines uh being um

[08:58] Perplexity and UChat here. If you look

[09:01] at the perceived utility from users

[09:04] um from a 1 to 5, it's actually pretty

[09:06] high. 4.5, 4.48.

[09:09] So, users think of the results from RAG

[09:13] uh of high quality and fluent.

[09:17] If you look at the citation correctness

[09:20] here, um so the left side is the

[09:22] citation precision and then right side

[09:24] is the citation recall. So, this is a

[09:26] number from 1 to 100. You can see that

[09:30] well, the precision is only 75, which

[09:34] means that the other 25, other one

[09:37] quarter is actually fake or hallucinated

[09:40] content. Which means that if you get a

[09:43] four reference there, one of them is

[09:45] wrong.

[09:46] And same is if you look at the recall.

[09:48] This is also pretty like low here.

[09:51] Um and I think that this actually reveal

[09:53] a big issue of a lot of the RAG. Uh that

[09:57] is, even we can get the right content,

[10:00] um the generation may still indicates

[10:03] issues.

[10:05] Uh this is also a phenomenon that I want

[10:07] to connect with uh research community.

[10:10] So,

[10:11] LLM citations and hallucinations is

[10:14] actually a big topic. Uh last year,

[10:17] uh a team was looking at NeurIPS, which

[10:20] is a big machine learning conference. A

[10:22] lot of the papers

[10:24] like getting accepted there, and they

[10:26] check um how many of those papers

[10:29] actually contain hallucinated citations.

[10:33] And turns out that there was at least

[10:35] 100 new hallucinations in NeurIPS

[10:38] proceedings. And this is the paper many

[10:40] of us read to get to know algorithms, to

[10:43] know a field, but uh we start to see

[10:46] this.

[10:47] Not only with research papers, we also

[10:49] start to see this hallucination of

[10:51] citations in student research project

[10:54] and course project. So, make sure

[10:56] whatever you submit represents your

[10:58] standard and the quality.

[11:01] Uh this year, uh

[11:03] I clear conference, which I served as a

[11:05] program chair, uh we also encounter a

[11:08] lot a lot of hallucinated reference. Uh

[11:11] so, as a result, there was a conference

[11:13] level uh action to do desk reject based

[11:17] on um hallucinated reference.

[11:20] So, uh all of this is just to let you

[11:22] know that those content may look very

[11:25] authoritative, may have a citation or

[11:27] link, uh but it's a little bit unclear

[11:30] whether they are correct.

[11:34] So, the last piece of information I want

[11:36] to present here, um because this is a

[11:38] really neat algorithm. It's called a

[11:41] needle in a haystack here.

[11:43] Uh so, if you look at this figure, um

[11:46] the x-axis is actually the context

[11:48] length. So, here it's a range from uh 1

[11:52] to 200 K contexts.

[11:54] Uh the model being tested here is a very

[11:56] earlier model, Cloud 2.1.

[11:59] And then you can see on the y-axis,

[12:02] um imagine we have one correct fact, one

[12:06] just like one, one correct fact in a

[12:08] long document. And then, what if we are

[12:11] going to vary the document lengths along

[12:13] the x-axis, where the facts actually

[12:16] sits somewhere in the middle? And then,

[12:19] we can ask it for that from a QA

[12:21] perspective.

[12:22] A good rag system is supposed to read

[12:25] all the documents and tell me the

[12:28] correct answer.

[12:29] And then, I think that the interesting

[12:31] thing happens is that as the context

[12:34] gets longer, you can see that the first

[12:36] from a color perspective, we seem to

[12:38] have more red color here. Redder means

[12:41] the model got it wrong. Green means that

[12:43] the model got the results.

[12:45] And then, uh you can see that shorter

[12:47] context here are almost green. As the

[12:50] context get along, red spreads. And most

[12:54] of those actually focused on the top or

[12:57] the middle here. The bottom seems to be

[12:59] pretty good. That is, as long as the

[13:02] correct answer is what I just read, then

[13:05] I can get it right. But if it happens

[13:07] like several decades ago or like a

[13:10] several document away from me, uh I

[13:12] cannot get it right. So, uh this is

[13:14] actually very surprising because

[13:17] for the first the time, we see that

[13:19] despite the model can handle a 200k

[13:22] token context,

[13:23] it cannot reliably use it.

[13:28] So, if we do the same kind of a needle

[13:31] in a haystack test with GPT-4,

[13:35] uh this is actually a very performative

[13:36] model.

[13:38] Um and here, the context window is 128k

[13:41] here.

[13:42] So, first, we see that seems great

[13:45] because the color we see here is mostly

[13:47] green here.

[13:49] Uh but you also see that we there are

[13:51] some kind of

[13:53] degrade here,

[13:55] uh especially around like 73k, we start

[13:58] to see some kind of a red yellow color

[14:00] here.

[14:01] Uh and if you look at this box that we

[14:04] highlighted, I think most of those uh

[14:06] facts, they are around like 10 to 15%

[14:10] during the during that range.

[14:13] And same story as before, the facts at

[14:16] the top and the bottom survive. But in

[14:19] the middle at the longer context is

[14:21] actually where this kind of rag systems

[14:24] fail. So, it is the same story. Lost in

[14:27] the middle.

[14:30] Okay. So, this is a quick overview of

[14:33] many of the issues with rag. Despite

[14:35] that, I think it's still a very cool

[14:37] design principle because it gave model

[14:40] the capability to use external knowledge

[14:43] that's not memorized by the model. So,

[14:46] still a very good principle for us to

[14:48] think about when building agents.

[14:51] Any quick questions before we move to to

[14:54] use?

[14:56] >> Sorry, I might have missed it, but is

[14:58] there any intuition for why that

[15:01] happens?

[15:05] >> Yes. So, um

[15:07] I think there um

[15:09] uh several reasons if you think about

[15:12] this. First is that uh um

[15:15] from like if you think about it from

[15:17] like attention perspective, especially

[15:20] when some information is in the very

[15:23] middle or just like in the

[15:25] um in the uh like sorry, in a earlier

[15:28] stage of the sequence, it's just a

[15:30] little bit harder to take care of this

[15:31] kind of long-range dependency. Uh

[15:34] second, I think it's that uh

[15:37] this seems to be a artifact or a

[15:39] position bias that we have observed that

[15:42] uh maybe when there are a lot of

[15:43] information um

[15:45] just as shortcut that humans may make,

[15:48] we tend to put uh put a lot of attention

[15:50] on what happened yesterday, but tend to

[15:52] forget what happened earlier

[15:54] uh last week. So, you still to you seem

[15:57] to observe this. And I think this is

[15:59] indeed uh indication that models cannot

[16:02] actually reliably use the context. We'll

[16:05] see more and more of those when we go to

[16:07] the memory um component as well.

[16:12] Yes.

[16:12] >> So, if you want to like retrieve

[16:14] external knowledge, is there any

[16:16] alternative

[16:17] to rag or like you have to use rag?

[16:21] >> Uh I didn't hear your first sentence. If

[16:23] you have to

[16:24] >> If you have to

[16:25] use external knowledge, is there any

[16:27] alternative?

[16:28] >> Yes. So, um this is what I was trying to

[16:31] summarize. So, uh I showed you a

[16:34] artifact or issue with RAG, but that

[16:37] does not mean that the RAG is not good

[16:39] on its own. So, I think as a overall

[16:42] general principle, especially if you

[16:43] have external knowledge, doing like

[16:45] retrieval, fact sheet. This is actually

[16:47] one type of tool use as well. So,

[16:49] retrieval in itself is also a tool use.

[16:53] Um so, it's still a very powerful

[16:55] approach, and when you need external

[16:56] data, I would still recommend that to go

[16:59] ahead with RAG. However, just as large

[17:02] language model being a very uh

[17:04] interesting technology, there are

[17:06] promises of it. There are also issues

[17:08] that we need to pay attention to. So,

[17:10] what I would recommend is that the for

[17:12] your task, you go ahead with RAG, and

[17:14] then you do a lot of the validations, or

[17:16] just like uh

[17:18] validity check, just to make sure that,

[17:20] okay, I do not suffer from this, and the

[17:22] sense seems to be not only correct, but

[17:25] also I'm not influenced by this kind of

[17:28] position bias, or in the process, all

[17:31] the retrieved content are secure, and

[17:34] there's no like bad actors injection of

[17:37] bad content.

[17:40] Okay, um with that, let's continue.

[17:43] Uh so, uh

[17:45] we need to talk about tools. And as I

[17:47] just mentioned, retrieval is also one

[17:49] type of tool use.

[17:51] Um before that, I want to give you more

[17:54] examples of of earlier days. This is

[17:56] again around the GPT-4 stage. So, at

[17:59] that time, um if you ask questions such

[18:02] as, "Who is the current president of

[18:05] United States?" the model will be like,

[18:07] "I don't know." Um

[18:09] if you ask them like, "What day of the

[18:11] week is it today?" it cannot help you

[18:14] answer that. Despite that they can solve

[18:16] very hard math problems.

[18:19] Um something interesting occurred, that

[18:21] is um as Professor Yejin Choi mentioned

[18:24] in her talk, uh when it comes to

[18:26] multiplication. So here, let's just ask

[18:29] GPT-4 a very simple question. Uh

[18:32] multiply 999 by 867.

[18:36] And then you get a correct answer.

[18:38] Sorry, you get a answer here, but it's

[18:40] not a correct.

[18:42] Um so

[18:43] overall you start to notice that it's so

[18:46] interesting like this this very capable

[18:48] technology, but then their accuracy for

[18:51] multiplication is only uh 59% accuracy.

[18:55] Their their performance on AMI or other

[18:57] kind of score is probably much higher

[18:59] than this.

[19:01] If you argue like, "Okay, maybe GPT-4

[19:03] was not a very capable." Uh this figure

[19:06] is using O1, which is a pretty strong

[19:09] reasoning model that's supposed to be

[19:11] much smarter and capable with math. So

[19:14] let's do the same task. But then you

[19:17] also see this trend. When we increase

[19:20] the number of digits in the

[19:21] multiplication, even when it's only like

[19:24] four,

[19:25] you start to observe that things start

[19:27] to get red here. Redder means uh

[19:31] like failure.

[19:32] So you see that we start to have worse

[19:35] and worse performance in multiplication.

[19:38] Multiplication is not a harder task. I

[19:40] mean, as long as you learn how to do A *

[19:43] B, um you're already humans can actually

[19:46] do the generalization to multiple digits

[19:48] easily, but this seems to be an issue

[19:50] with with earlier models.

[19:54] And this trend is actually um very

[19:57] general. Like here on my screen, similar

[20:00] web, you see that not only for

[20:02] multiplication, for puzzles like solving

[20:05] puzzles, or even doing like a dynamic

[20:07] programming, as the situation get more

[20:10] complex, model performance start to get

[20:14] worse. That is

[20:16] maybe models only know how to solve easy

[20:18] problems, not harder problems.

[20:21] This is not a bug in one particular

[20:24] model, and I think of the pattern here

[20:26] is that those models seems pretty good

[20:29] when the problem is small. And then the

[20:31] accuracy actually drop as the number of

[20:34] steps that it needs to uh be used

[20:38] actually grow here.

[20:39] So, this is actually maybe a component

[20:42] that what if we can actually delegate

[20:44] that to someone else? Because the model

[20:47] seems still capable. They just cannot

[20:49] handle very complicated task.

[20:53] Um this actually lead me to uh the

[20:57] introduction of tools here.

[20:59] So, here I summarize why LLMs are its

[21:02] own is actually not a good enough and

[21:04] why we actually needed to use.

[21:07] Uh first, as I showed you, uh for this

[21:10] kind of relatively longer sequence

[21:13] multiplication, models seem to struggle.

[21:16] And this is true with like multi-step

[21:18] logic deduction, uh exact or very

[21:20] verifiable settings.

[21:23] The other thing related to like what's

[21:25] the weather today in uh

[21:27] like in Alto, uh if the model didn't see

[21:30] that in the training coppers, it's

[21:32] really hard for them to get them right.

[21:34] So, you can imagine that the long tail

[21:36] effects or post cutoff events or

[21:40] private, sorry, uh private uh

[21:44] proprietary or external data, models

[21:47] seem to struggle with it.

[21:49] Um the other thing is that um models

[21:52] seems to do well with text, code, math,

[21:55] but we also have a lot of like APIs,

[21:58] database, like non-

[22:00] language interface.

[22:02] Um we also have the physical world. We

[22:04] may also have some kind of like live uh

[22:07] states that we want to get out of.

[22:11] So, this is actually what agents can do

[22:13] for you. Um I mean, if they cannot do

[22:16] like three digits by three digits, maybe

[22:18] we can give them a calculator here. If

[22:21] they cannot write dynamic programming

[22:23] easily, maybe we can get them to write a

[22:26] code instead. Uh we can also give them

[22:29] symbolic solvers, verifier that we have

[22:32] from other research field.

[22:34] In terms of content that they never see

[22:37] in the training coppers, we can give

[22:39] them retrieval, rag, web search. We can

[22:43] let them access newsfeed, uh today's

[22:46] news, live APIs. They can also do some

[22:49] kind of rag over like company specific

[22:52] coppers. This is more like the internal

[22:54] coppers here.

[22:55] Um for a lot of like a non-language

[22:58] interface, maybe we can enable agents to

[23:01] use uh function calls, APIs, MCPs. They

[23:05] can use browsers. They can they can work

[23:08] with robots, etc.

[23:10] So, this is why like having tools is

[23:13] going to really enable agents to do a

[23:15] lot on top of LLMs.

[23:19] I think in earlier days, there was a lot

[23:21] of debate on what a really defines an

[23:24] agent, what is agentic system, and what

[23:26] is not. And one big factor is actually

[23:29] whether the system knows how to use

[23:32] tools. And this is actually a really big

[23:34] a differentiator there.

[23:38] Okay, so what what are tools? Uh

[23:41] we do not need a formal definition here,

[23:43] uh but I just to kind of

[23:45] uh separate this with a lot of the real

[23:48] world tools we have, such as a car. Uh

[23:51] here, uh we are talking about the large

[23:53] language model uh to use. Um you can

[23:56] view with them as a function interface

[23:59] to a computer program that runs

[24:02] externally

[24:03] to the LLM, where the LLM actually

[24:05] generate the function calls and input

[24:08] the parameters, arguments in order to

[24:10] use the tool.

[24:12] This is probably a little bit uh

[24:14] abstract. And I want to mention two

[24:17] words here. Um first, external.

[24:20] For a lot of the tools used, the model

[24:22] does not need to do the task themselves.

[24:25] It only needs to write down the tool use

[24:28] kind of arguments and then some external

[24:31] program will do it.

[24:33] So this is why it's like external. We

[24:35] will see some of the examples later.

[24:37] Um second word that I want to highlight

[24:39] here is function interface. So a lot of

[24:42] the two we are going to see is not like

[24:45] okay here's a car. Um

[24:47] what what we are going to see is that

[24:48] it's a text stream with a name with a

[24:50] signature with some kind of like

[24:52] parameters or arguments. So this is

[24:54] actually what do we want to model those

[24:56] two learn to use. [clears throat]

[24:58] It's actually a very interesting um

[25:00] set up because LLMs

[25:03] in general are trained to deal with

[25:05] text. So if we could have put the two

[25:07] use also in similar textual formats,

[25:10] maybe it would work better.

[25:12] So um this figure uh you can see that

[25:15] one of the two use, if we want to know

[25:17] what's the time uh right now, uh they

[25:20] can actually use get a time to access

[25:22] the real world and figure out that it's

[25:24] 3:00 p.m. right now.

[25:26] And then similarly, um they can do some

[25:29] uh calculations instead of doing this

[25:31] very complicated math that's going to

[25:33] fail, it give it to a external

[25:36] calculator here and then can get it the

[25:38] correct result.

[25:41] So um this table actually give you a a

[25:44] wider range of examples in terms of the

[25:46] two use. Uh I already talked about like

[25:49] knowledge access or computation

[25:51] activities. They can also interact with

[25:53] the uh real world such as get the

[25:56] weather, get the location, uh look at

[25:59] your calendar and uh use your email.

[26:03] Um they can deal with non-text uh

[26:06] non-text modalities uh such as maybe

[26:09] they will call uh image generation tool

[26:12] to generate a

[26:13] um

[26:14] meme for your specific uh task. So

[26:16] otherwise you are going to rely on the

[26:18] model themselves to do image generation,

[26:20] but now you can actually delegate it to

[26:22] external image generation tool.

[26:26] Um so the last uh column here is

[26:28] actually Samsung I think uh

[26:31] open to use to a wider range of domains.

[26:34] Not only this kind of very ready-to-use

[26:37] tools such as calculator

[26:40] or like get the weather API. We also

[26:43] have models that we have trained in the

[26:46] past. We may have really good a machine

[26:48] translation systems. Maybe there's a

[26:50] dictionary that is someone maintains and

[26:52] it's just awesome to explain the meaning

[26:55] of a word in your favorite language. And

[26:57] then a lot of those external tools or

[26:59] systems models that we have built, they

[27:02] can also be used as a tool here. So the

[27:05] definition of tool is actually very

[27:07] broad.

[27:09] Okay. So

[27:10] again, let's look at the one last

[27:12] example here before I go deep into tool

[27:14] use. So our familiar

[27:18] multiplication example here. What is

[27:21] 17,423

[27:24] * 3,892?

[27:26] I do not know the answer, but models

[27:29] also do not. However, they can actually

[27:32] write it down in this format.

[27:35] So the one that I highlighted here in

[27:37] yellow is actually a specific tool call

[27:40] here. So you can see that it's not like

[27:43] some

[27:44] other format. It's actually in text. It

[27:46] uses like a specific indicator to let

[27:50] the models know that here you need to

[27:52] call a calculator

[27:55] here to calculate this kind of digits

[27:59] multiplication.

[28:00] And the same on the right. So you can

[28:02] see that how's the weather today?

[28:05] It's actually pretty hot. And then the

[28:07] model is going to call check weather and

[28:09] then look at the some external dashboard

[28:12] or database and then tells us that oh,

[28:15] it's sunny today. So this is how they do

[28:17] the tool call and then internally it's

[28:20] all this kind of like arguments or

[28:22] string here.

[28:25] Okay.

[28:26] So

[28:28] before we talk about how to really

[28:30] enable models to learn how to use tools.

[28:33] Any questions so far?

[28:36] >> So maybe a decade ago we had all these

[28:38] interface definition languages and all

[28:41] the distributed object stuff, all about

[28:43] type checking

[28:45] in order to make sure that we could get

[28:47] an interface call right.

[28:49] And it seems like all your examples were

[28:51] strings. So now we've blown away type

[28:53] checking

[28:55] and now we're to semantic questions. So

[28:57] how do you deal with versioning of the

[29:00] semantics? Is that all just both sides

[29:03] have to make it right? It doesn't seem

[29:05] like it's caller makes right, it doesn't

[29:06] seem like it's callee makes right.

[29:09] How do you deal with that?

[29:11] >> Yeah, great question. So we will briefly

[29:13] hint about that when we come to the

[29:15] standard interface as well.

[29:17] The short answer is that

[29:20] models suffer from that. So you can

[29:21] imagine because you rely on AI to

[29:24] generate a string with that is specified

[29:27] input arguments, functions, things like

[29:29] that. It's very likely since they can

[29:31] already hallucinate the citations, they

[29:33] can also hallucinate the data string,

[29:36] which means that if you're going to do

[29:37] external type check, things like that,

[29:39] they fail. So this is actually a bigger

[29:41] failure of tool use, which we are going

[29:43] to cover later.

[29:45] Yeah.

[29:46] >> Um so when it calls functions, would it

[29:49] also be possible that it sells like

[29:51] Python code

[29:53] and then creates like these children

[29:54] cells?

[29:57] >> Yeah. So

[29:58] good question. In case I didn't hear you

[30:01] clearly, I think you are asking whether

[30:03] the models actually can come up with

[30:04] tools themselves on the fly. The answer

[30:06] is yes. So in addition to a lot of the

[30:09] widely used

[30:11] tools that I'm going to share, you can

[30:13] also imagine if the model is intelligent

[30:15] enough, they realize that in order to do

[30:17] this task, it will be much easier if I

[30:20] generate an interface so that I can just

[30:22] do everything on the interface. Then

[30:25] that's actually a generated tool on the

[30:27] fly. This is actually very possible and

[30:29] there has been research showing that.

[30:31] But again, since it's going to be a new

[30:33] tool, right? You suffer from all the

[30:35] issues that I talk about it such as

[30:38] hallucinations or maybe this too is

[30:41] actually not the generated by the model

[30:42] but the model memorize someone else too

[30:45] and then as a result give it a here to

[30:47] you.

[30:49] Okay, we are going to continue.

[30:51] In the next 15 minutes we are going to

[30:54] learn a little bit of math. So I want to

[30:56] give a warning first. So the question

[30:59] that I want to share here is so far I

[31:02] tell you why we need a tools and then

[31:05] what a tool is. So if you think about it

[31:08] from a model perspective how does the

[31:10] model know when to use tool? How does

[31:13] the model know what kind of tool to use?

[31:16] It feels like a lot of decisions we need

[31:17] to make.

[31:19] And I think many of us have learned the

[31:20] machine learning. If you figure out that

[31:22] there is a question that we need to

[31:25] like decide whether to do it, which

[31:28] which tool to use. This is actually a

[31:29] very classic kind of machine learning

[31:32] question. So what I'm going to show next

[31:34] is let's teach models to use tools.

[31:39] So the title here is literally what I

[31:42] have been saying that is large language

[31:44] large language models they can teach

[31:47] themselves to use tools.

[31:49] So let's be a little bit of slow here.

[31:52] The system I'm going to share with you

[31:54] is called a tool former

[31:56] earlier from meta.

[31:59] It basically trains large language model

[32:00] to decide which API tool to use, when to

[32:05] use them, what arguments I'm going to

[32:08] generate to pass and how to better

[32:11] incorporate those results. So we have

[32:13] four stage here.

[32:15] On the right this is actually what a

[32:18] tool call look like in earlier days.

[32:21] So I'll just use the

[32:23] a shorter example here. So out of the

[32:27] 14,000 participants 500 sorry 400 or

[32:32] passed the test. So here in order for

[32:36] the model to know that the next token is

[32:39] 29%.

[32:41] They actually need to do some

[32:42] calculation. So, what's happening in a

[32:46] hypothetical string is that we now

[32:48] insert this

[32:50] this like two arguments string here so

[32:53] that the model knows that here I need to

[32:56] do a calculation of 400 divided by 1,400

[33:01] here, which is 29, and then they use the

[33:03] 29 as the next token.

[33:06] And similarly here, if you look at the

[33:08] first one, the New England Journal of

[33:10] Medicine is a registered trademark of

[33:14] So, at this stage, it feels like a good

[33:16] timing for models to use a QA system.

[33:20] The QA system is going to ask, "Who is

[33:23] the publisher?" And then you get a like

[33:25] Massachusetts Medical Society. And then

[33:27] the model generates the MMS here.

[33:31] So,

[33:32] like now let's figure out when should I

[33:35] ask this question? Why is it here, not

[33:38] here?

[33:39] And then why is the QA not a

[33:41] translation? So, those are the questions

[33:44] we need a models to learn.

[33:47] Okay, so before I talk about what's

[33:49] going to happen, I'll share you that in

[33:51] two formers, uh the first system that

[33:54] they kind of learn how to use tools, or

[33:56] maybe the first of many systems, um

[33:59] actually only work with five tools.

[34:01] Today, our agents can actually use

[34:04] thousands of tools. But this is actually

[34:06] a earlier idea. So, uh there was only

[34:09] five systems we provide. A QA system, a

[34:12] cal- calcu- calculator here, a search

[34:15] engine, a translation system, a

[34:17] calendar. And this is all what we have.

[34:20] Okay, only five tools.

[34:22] So, now think about a method. So, what

[34:25] would it be a good training? I already

[34:27] showed you some of the examples earlier,

[34:31] such as this like very

[34:33] slightly different uh format that uh

[34:36] very different than natural language,

[34:38] but it's also certain temp- type of

[34:41] thing that's related to natural

[34:42] language.

[34:43] So, what if we can actually create a

[34:45] data set? The data set is going to be

[34:48] that a kind of um

[34:50] string that I showed you. So, every real

[34:53] sentence will have some kind of

[34:55] augmented format with API calls. And

[34:59] then, what if we can actually train a

[35:01] model on top of that? Then, at inference

[35:04] stage, my model knows when to generate

[35:07] the such uh tokens, when to uh how to

[35:11] parse the results. So, we literally turn

[35:13] that into a learning problem here.

[35:17] On my screen, you probably saw that I

[35:19] showed you this like this is a very

[35:21] earlier model called the GPT-J here.

[35:24] Um so, we are going to kind of fine-tune

[35:26] a small model. Now, I'm going to show

[35:28] you how we actually decide how to really

[35:31] train this kind of system.

[35:33] So,

[35:34] take a many step back. What I want to

[35:36] have is

[35:38] I want to have a regular text string.

[35:40] And I want to insert a few two calls in

[35:43] this string that are making it look like

[35:45] the format I shared earlier.

[35:47] And then, I'm going to train a model on

[35:49] top of that. In the inference stage,

[35:52] whenever they saw this kind of prefix,

[35:55] they are going to generate a two call at

[35:57] a certain position. So, this is this is

[35:59] literally a learning problem.

[36:02] So, as I mentioned, there are many

[36:04] steps. So, let's now kind of like go a

[36:07] little bit of deeper here.

[36:09] First is

[36:11] a sentence has so many words. Like this

[36:13] sentence, Pittsburgh is known as the

[36:15] Steel City here. So, if you need to

[36:18] insert a API call or if you know where

[36:21] to insert the API call, where is

[36:23] actually

[36:25] a design choice.

[36:26] So, we are going to call this magic

[36:29] position I here. So, for any kind of

[36:31] input, uh we first need to select that

[36:34] position I um where if we insert a API

[36:38] call there, that it makes a lot of

[36:40] sense. So, assume we know this. This is

[36:43] actually how we pick where to insert

[36:46] that API call.

[36:48] And where is actually determined by

[36:51] this probability here that is PI equals

[36:54] everything so far. And then the

[36:56] probability of I insert an API here. So

[36:59] we basically want to find those

[37:00] positions that can give us the highest

[37:02] probability of inserting an API call.

[37:06] So this is the first step.

[37:08] Once I decide that okay, this is a

[37:10] position I want to insert an API call.

[37:13] What should I do next?

[37:15] I'm going to just like sample different

[37:17] API call I can use here. Because once I

[37:20] know the position is three, I could have

[37:22] used a QA system. I could have used a

[37:24] math. I could have used a search engine.

[37:26] I can use many many choices here. So

[37:29] which call is going to be great?

[37:32] So here

[37:34] we will have several candidates of API

[37:36] call. And then we literally are going to

[37:38] execute those API calls.

[37:40] On the figure here you can see that

[37:43] while I know that I need a QA call here,

[37:47] I got the answer that it's called a

[37:48] steel city. And then I execute that and

[37:51] I get the answer. So all the execution

[37:54] actually happened externally.

[37:57] So that's the execution part.

[38:00] But now like imagine I tried to find

[38:03] different APIs and they all give me some

[38:05] kind of execution outcome. Which one

[38:07] should I use as my ground truth here? So

[38:10] this is what we call a filtering

[38:12] process.

[38:13] The process is also very kind of

[38:16] straightforward. So we are going to make

[38:17] this as a learning problem as I

[38:19] mentioned. First I'm going to share you

[38:22] the loss function here. This is a very

[38:24] classic a cross entropy loss

[38:27] on the tokens from

[38:30] position I and onwards. So basically J

[38:34] starts from I. So everything that I'm

[38:36] going to generate from the current token

[38:38] till the end.

[38:40] One minor thing different from the

[38:42] classic cross entropy is that we also

[38:45] add this W

[38:47] um

[38:48] like weight here. Uh this basically

[38:50] decays with distance. So, tokens right

[38:53] after the call actually count a more,

[38:55] but tokens like really for further away

[38:59] actually does not count a lot.

[39:02] So, then what does model does to kind of

[39:04] filter this is literally a comparison.

[39:07] Okay. So, we have LI plus. This is that

[39:11] we are going to give not only the

[39:13] current prefix, but also the tool call

[39:16] and the execution output. So, this is a

[39:18] complete package. This is our LI plus.

[39:22] LI minus is like two baselines.

[39:25] What if I just do not do API call?

[39:27] What's the loss function? What if I did

[39:30] API call, but I do not have output?

[39:32] What's the What's the loss function? And

[39:35] I take whichever is the better and then

[39:38] compare it with my like finished tool

[39:41] call loss. If this is bigger than a

[39:44] threshold, then I'm going to keep this

[39:47] specific API call. So, this is actually

[39:50] what's happening here.

[39:53] Um let's look at a one example. Um so,

[39:56] the loss function that I mentioned to

[39:58] you that weighted decay cross entropy.

[40:01] So, let's see we use it to calculate my

[40:03] example of Pittsburgh is known by

[40:07] uh what? And then the prefix is

[40:09] Pittsburgh is known by. And then um

[40:12] let's see we got a Steel City on this

[40:14] kind of like QA API call.

[40:17] So, the condition is that I'm not going

[40:19] to do any API call. I will just have

[40:22] this prefix and then you get your loss

[40:24] 2.5 here.

[40:26] If I get in the QA call, but I didn't

[40:29] give them the answer.

[40:32] This is what I like one of the stronger

[40:34] baseline there. You can see that my loss

[40:36] is only 2.1.

[40:39] If I executed this QA API call and also

[40:42] give them the answer. And then this give

[40:45] me a loss of 0.8.

[40:47] Loss in general is lower the better. So,

[40:49] here if I look at the usefulness of this

[40:52] API call for the current situation, it's

[40:55] actually 1.3. It seems pretty good. So,

[40:58] I'm going to keep QA call as a choice

[41:02] here.

[41:03] Of course, you can do this for many

[41:05] other API calls and select whichever

[41:07] give you the smallest loss.

[41:12] >> My question is you're being very clear

[41:14] with why.

[41:15] So, it's not just a textual comparison.

[41:19] You are actually executing the call,

[41:21] getting the response. So, if it was

[41:22] caching the answer to these questions

[41:26] uh

[41:27] cuz you don't have any control over what

[41:28] the server's doing.

[41:30] Um

[41:31] I guess my question is how robust will

[41:33] this be

[41:35] uh cuz you could easily just get cached

[41:37] answers.

[41:38] >> Yes. So, um a few things. First, you are

[41:41] right that here everything need to be

[41:44] executed by a external system, right?

[41:47] And then when they execute that, you

[41:49] fetch back the results and then you see

[41:52] how good is this fetched back result.

[41:54] This is what's happening here. And it's

[41:56] totally plausible that I called this QA

[41:59] server, but the QA server was down. So,

[42:02] I get a nothing back. So, you just use

[42:04] whatever has been produced here. Or

[42:07] uh you you you you give it, but then

[42:09] because your format is wrong or

[42:11] whatever, you didn't get anything. You

[42:13] get a error or the number is wrong. And

[42:15] then that's also the cost that you would

[42:17] have to pay here. So, this is why this

[42:19] learning-based approach may not be the

[42:21] best and then we'll see the evolution of

[42:23] how things go.

[42:26] Okay. I hope that part is clear like in

[42:28] terms of how they determine uh where to

[42:31] insert API call and then how to

[42:34] determine which API call to use.

[42:37] And overall like if you just look at a

[42:39] more examples, um so uh I give you the

[42:42] usefulness score that is the loss

[42:44] comparison. So, you can see that the

[42:46] first the one um

[42:49] the WIO be open on Friday, uh March

[42:52] 10th. So actually they can figure out

[42:55] this with a right API call. And then the

[42:58] useful this score of this one versus the

[43:00] last one is not very useful. So you can

[43:02] see the score is pretty low. So this is

[43:04] actually how you are going to determine

[43:06] whether a particular API call is useful

[43:09] in a position or not.

[43:12] So two formers actually work pretty well

[43:14] when it was first introduced. So on my

[43:17] screen you see five different type of

[43:19] task, fact checking, question answering,

[43:22] math, temporal, multilingual. Uh you can

[43:25] see that models are doing extremely

[43:28] well, especially like two former is

[43:30] probably like many times smaller than

[43:33] GPT-3. Um you can see that

[43:36] uh two former is actually trained on

[43:38] GPT-J here. So it's much smaller than uh

[43:41] GPT-3. Uh you can see that at least the

[43:43] two former results on math

[43:46] uh is just like so much better on

[43:48] temporal information, even on factor uh

[43:52] completion, on multilinguality. So it's

[43:55] just like a much better if the model

[43:57] actually know how to use tools, and they

[43:59] can actually outperform a very big

[44:02] model.

[44:03] >> Okay, so I think this is this actually

[44:04] like how model agents system actually

[44:07] work? That basically inside of an output

[44:10] token stream the model decides to switch

[44:12] to a tool or is it more like like after

[44:14] one agent turn the agent decides okay I

[44:16] want to use these tools and then another

[44:18] agent turn it does the output. Like uh

[44:21] do you understand my question?

[44:22] >> Yes. So here the fashion uh again I'm

[44:25] going to show you a evolution of how the

[44:27] agent the tool use evolve. At what I'm

[44:29] covering right now is actually like uh

[44:32] when you generate each token, one of the

[44:34] token may trigger the tool use, and then

[44:36] you put it that as part of your

[44:38] generation. So this is the current

[44:40] fashion. Later when we go to the very

[44:42] agentic systems today it's more like

[44:45] agents actually decided that okay I need

[44:46] to use a tool for this particular

[44:48] question. And then they uh retrieve one

[44:51] tool, and maybe it didn't work, and then

[44:53] they go to another tool, etc. So you get

[44:55] a trace of how agent use tools.

[44:59] Okay, let's continue. Since this is a

[45:02] very classic work and the people are

[45:03] already eager to ask a modern questions.

[45:06] Um so

[45:08] even for a model like a GPT-2 size with

[45:12] and without two formers, the change is

[45:14] actually

[45:16] a lot. So the blue curve is actually

[45:18] when we have two former and then the

[45:20] right is without a two former. And the

[45:22] dash line here GPT-3. So you can see

[45:24] that this is actually a very important

[45:27] design.

[45:29] Um going back to some of the earlier

[45:31] question that is oh, this is a fashion

[45:33] where the model is generating next token

[45:36] and then suddenly we let them to do this

[45:39] kind of tool use.

[45:41] And apparently since this has a lot of

[45:43] connection to words, tokens,

[45:46] there was a lot of work talking about

[45:49] what if we just view tools as words.

[45:52] And then there's this study called a

[45:54] token GPT. So you basically view each

[45:58] tool as a token. And then you can

[46:00] actually learn a embedding for it.

[46:02] So whenever in the generation process a

[46:05] token, not token, a token is triggered,

[46:08] large language model will complement the

[46:11] arguments and then for the tool to

[46:13] execute. So now we actually really use

[46:15] it in

[46:16] token-based fashion.

[46:19] So I'll give you a quick example. We'll

[46:21] be very fast here. So imagine you are

[46:24] solving a kind of like a math problem

[46:26] here and then at this point

[46:30] the model needs to generate the answer

[46:31] for this math question. And then they

[46:33] decided that I need to use GCD function

[46:36] here. And then they they trigger that.

[46:38] They use the embedding like that

[46:40] embedding get triggered and then they do

[46:42] this kind of calculation.

[46:44] So

[46:45] as a result you can see that there is

[46:47] this reasoning mode. There is this tool

[46:49] mode. There is this kind of plugging

[46:51] back mode.

[46:55] We have talked about like wording

[46:56] bearings briefly. Um so wording bearing

[46:59] the key idea is that okay, uh how can I

[47:02] get a dense representation for each

[47:04] word? So here, we also want to just view

[47:07] token like token as a regular token.

[47:11] Um this is a process of how it got

[47:14] triggered. First, you predict a token

[47:17] here. And then once the model see that I

[47:19] need to use the tool, they stop the

[47:21] generation and they're going to switch

[47:23] to

[47:24] uh something else.

[47:26] Um they look at the available tools and

[47:29] to decide which tool I want to use. What

[47:31] is the arguments, the parameter I need

[47:33] to give to my tool? And then they will

[47:36] give this tool to a external model like

[47:39] um in-context learning or others. And

[47:41] then they get the results, ask you that,

[47:43] and then bring the results back. And

[47:46] then it goes back to the original

[47:48] generation. So you can view this as

[47:50] whenever they they realize they need to

[47:52] do a tool call, they pause, they do the

[47:54] tool calculation. Once they get the

[47:56] results, then they continue. So this is

[47:59] the process of Tool Chain GPT.

[48:02] Um very briefly, um they do a lot of

[48:06] synthetic data to kind of uh construct

[48:09] this training coppers and then they can

[48:11] actually train uh the specific uh token

[48:15] embeddings.

[48:18] Um this kind of Tool Chain GPT also

[48:21] works well.

[48:23] Uh one thing I do want you to notice is

[48:25] that um you see here I have one hop

[48:28] versus multi-hop here.

[48:30] Multi-hop means that the agent asked to

[48:32] use a sequence of tools.

[48:35] It's not like enough if they only use

[48:37] one. And then if you look at the numbers

[48:39] like one hop is 0.7, 0.5, it's pretty

[48:43] high. But then if it's multi-hops, this

[48:45] is literally like 0.03,

[48:48] 0.09, it's pretty bad. So this is

[48:51] actually a big challenge earlier for

[48:53] tool use. That is, if the agent needs to

[48:55] use a sequence of tools, this is

[48:57] actually much harder.

[49:01] Okay, I'll stop here. You all just

[49:03] finished the most math heavy part of

[49:05] this class. Any questions?

[49:09] Okay.

[49:11] Yes.

[49:12] >> Why are multi-cops why is multi-cops

[49:17] like really bad? Like is it is it on the

[49:20] two-sided problem or is it the

[49:22] positional embedding problem?

[49:24] >> Yeah, I think there are many reasons of

[49:26] why multi-cop is more challenging. First

[49:29] is that if you just view this as

[49:32] like each step is a degree of freedom.

[49:35] Many steps, you just have so many

[49:37] choices there, right? Like the

[49:38] combination of possible sequences is

[49:41] just huge. This is the one. Second is

[49:43] that I think in a lot of the like what I

[49:46] was talking about how they train the

[49:47] model, they do have some kind of ground

[49:49] truth data. If you look at a ground

[49:51] truth data, a lot of them is actually

[49:52] just like a single tool call. The

[49:54] reality is that as AI gets better and

[49:56] better, we expect them to do a lot. And

[49:59] that a kind of sequence of tool use is

[50:01] just not a very well like represented in

[50:04] the natural world. So that's another

[50:07] thing. But I think the major reason is

[50:08] just like the search space is huge.

[50:13] Yes.

[50:14] >> I wonder

[50:15] every day there are new new tools out

[50:17] there being created.

[50:18] How does

[50:19] how does it even know

[50:21] what are the new tools out there and how

[50:23] do you explain and which ones are

[50:25] >> Okay, great question. We will talk about

[50:27] that in 10 minutes. Okay. Um so I will

[50:30] continue. So what I shared here is

[50:32] really just like how two cop get

[50:35] introduced to us, like two years ago.

[50:38] And then a lot of things have changed.

[50:40] First is that you probably noticed that

[50:42] in the

[50:43] uh two-former, they only use five tools.

[50:46] But we actually have a lot of tools. How

[50:48] can we actually scale this to many many

[50:50] tools here?

[50:52] Um the first the work that I want to

[50:54] share with you is actually called a tool

[50:56] LM. They actually enable AI to use over

[51:00] 16,000

[51:02] APIs.

[51:03] Uh the way how they do it is actually

[51:05] very um straightforward. You can also

[51:08] view this as a modern fashion of self

[51:12] self-supervised

[51:14] or like uh like a synthetic data

[51:16] construction. So, what it does is that

[51:19] it first just crawl a lot of APIs

[51:21] because those are available online.

[51:23] And then they come to ChatGPT.

[51:26] They ask ChatGPT like, "Okay, uh here is

[51:29] a tool use. Pretend that you are a user

[51:31] asking for something that would trigger

[51:33] this tool call. Give me the input and

[51:36] output." So, they actually work with AI

[51:38] with our arms to generate this kind of

[51:40] synthetic data.

[51:42] Okay, once they generated this kind of

[51:44] input request and then which kind of

[51:46] tools to potentially use, they can then

[51:49] ask ChatGPT again like, "Okay, now

[51:52] pretend that you have this question and

[51:55] you may want to use this kind of tools.

[51:57] Just try to solve it." Then the ChatGPT

[52:00] is going to

[52:02] like use this tool solve it and if it

[52:04] didn't uh

[52:05] like succeed, uh try different tool etc.

[52:07] So, there is actually a tree series of

[52:09] how AI solve this kind of complicated

[52:12] user query.

[52:14] Okay, so that's actually the data uh

[52:17] data set that called a tool bench.

[52:20] This is literally a self or machine

[52:22] constructed uh data sets where we use AI

[52:26] to simulate user queries. We use AI to

[52:28] solve how to do it. Okay, now you have a

[52:32] ChatGPT h solution trees of how to do

[52:36] tool use.

[52:38] Well, then we can do the simulation. We

[52:40] take a llama, which is a earlier model

[52:42] from uh Meta, and then we'll just do SFT

[52:46] on this like ChatGPT reasoning tree

[52:48] series. We can then have a pretty

[52:51] capable tool llama that uh knows how to

[52:53] do uh tool call.

[52:56] Okay, so this is a key idea of two LLMs.

[53:00] And then at inference stage, what the

[53:02] model does is that um they get a

[53:04] instruction from the user, Um they look

[53:07] for different APIs,

[53:10] then they give it a tool the tool llama

[53:12] and the tool llama will produce the

[53:13] final answer. So, this is actually how

[53:16] it works. This is a constructed data set

[53:19] to give them over 16,000 APIs.

[53:24] Yeah.

[53:47] >> [laughter]

[54:06] >> Okay, so this kind of like distillation.

[54:09] So, first I want to make a claim that

[54:11] this is not the classic like Jeff Hinton

[54:14] H knowledge distillation. This is a new

[54:16] wave of distillation where we have a

[54:18] very capable model

[54:21] and we know if we know their reasoning

[54:23] traces or if we know how they solve the

[54:25] problems, we can actually do SFT to

[54:28] enable a much smaller model to have

[54:31] similar capabilities here.

[54:33] Um if you pay attention to news, you

[54:36] actually see a lot of discussions about

[54:38] distillation these days between

[54:40] different the frontier model providers.

[54:43] Going back here,

[54:45] so I know this may seem like, oh wow,

[54:48] this is even like is this even possible?

[54:51] Like the data seems not even not a very

[54:54] high quality or reliable or whatever.

[54:57] The reality is that you can actually do

[54:59] this kind of synthetic data generation

[55:01] where you you pretend a user is going to

[55:04] ask some question that it involve this

[55:06] set of tools. So, you then try GPT can

[55:09] help you write a search a question

[55:11] because this is a very clear task. Not

[55:13] the tool ask them for their reasoning

[55:15] choices, but ask them to do a specific

[55:17] task, right? Once they did that, and

[55:19] then you frame it as, "Okay, now this is

[55:21] a question. You may could use this set

[55:24] of tools. How would you solve it?"

[55:26] Again, the how is actually a process.

[55:29] They are going to describe like, "Okay,

[55:30] I'm going to do this and do that." Uh

[55:32] still we are not attaching the internal

[55:35] reasoning choices. So, slightly

[55:37] different here.

[55:38] Um and then once you have this kind of

[55:40] synthetic data, your training set, you

[55:42] can train a much smaller model on top of

[55:44] that.

[55:54] >> Exactly.

[55:57] >> Yeah. So, you basically use them to do

[55:59] very specific user instruct task. And

[56:02] then maybe you need a multiple steps to

[56:04] construct a training set.

[56:06] Okay, I'm going to continue. Um so, this

[56:09] is about the two arms. And then um one

[56:12] thing actually occurred in this process.

[56:14] So, this is again even at the GPT-4 like

[56:17] more recent at Cloud stage.

[56:19] Um if you want the model to help you

[56:21] with speech-to-text,

[56:23] they need to call certain type of models

[56:25] to do this, right? And then on the left

[56:27] side you can see that uh here a

[56:29] particular model they call it from

[56:31] TorchHub is actually ASR and the source

[56:35] equals local. Those two are actually

[56:37] wrong. Like it does not exist. So, the

[56:39] model actually hallucinate certain type

[56:42] of parameters in the process.

[56:44] In the middle, um Cloud was also trying

[56:47] to do the same task. And then they said

[56:49] that, "Okay, you are going to use

[56:51] translation here." The user wanted

[56:53] speech-to-text. So, they actually called

[56:55] a translation model here, uh which is a

[56:58] wrong library. So, the model actually

[56:59] used a wrong API here. Uh especially

[57:02] when they are so similar to each other,

[57:04] uh this is where issues may occur. And

[57:06] then um what do you really want is

[57:08] actually speech to text. Go to torch hub

[57:11] and load this particular

[57:14] transcribable model here. So, now like

[57:17] how could we really teach models to use

[57:19] a lot of those tools and especially have

[57:22] a way to quantify hallucination in the

[57:24] process. So far, we haven't talked

[57:27] anything about how to quantify

[57:29] hallucination in two years. It's only

[57:31] like correct or incorrect, but is there

[57:33] a way for us to even do this?

[57:36] So, the Gorilla is actually a system

[57:38] from Berkeley where they are trying to

[57:41] connect LLMs with a lot of APIs. By a

[57:45] lot, I mean 1.6 thousand here which is

[57:48] actually 10 times smaller than 2 LLM.

[57:51] So, what they do is very similar to the

[57:53] construction I just mentioned.

[57:56] You are going to

[57:58] scan a lot of the

[58:00] APIs. So, here they actually

[58:03] focus on a lot of the modern AI tool

[58:06] use, hugging face, the model hub,

[58:09] PyTorch hub, the TensorFlow hub, and

[58:12] then they get a lot of API calls in JSON

[58:14] format. And then they use GPT-4 to

[58:17] generate a synthetic instruction data.

[58:19] So, here's a query, here's what kind of

[58:22] tool you should use, etc.

[58:25] On top of this synthetic data, just like

[58:27] how I mentioned with 2 LLMs, they are

[58:30] going to train a model.

[58:32] But the training here may not always be

[58:35] trivial because if you only train the

[58:37] model with correct docs in the prompt,

[58:40] then the model only learns to copy

[58:43] whatever it's given and a wrong doc

[58:46] actually will lead it to the wrong call.

[58:49] So, the way how they deal with it is to

[58:51] do this kind of retrieval aware training

[58:54] where they introduce both correct and

[58:57] incorrect retrieval during the

[58:59] instruction fine-tuning process with the

[59:01] goal that this kind of setup will teach

[59:04] the model to first to recognize what is

[59:06] correct, what is incorrect retrieval,

[59:08] and then do a lot of the generation on

[59:10] top of that.

[59:12] So, at inference stage, like here, let's

[59:15] say you can do a zero-shot inference. If

[59:17] the user says that I want to see some

[59:19] cats dancing. Um the model is going to

[59:23] look at all the available API database

[59:26] and decided that, "Okay, I can actually

[59:28] call stable diffusion pipeline here."

[59:31] And then you call stable diffusion by

[59:33] giving them this query. And then you get

[59:36] a specific result. And then

[59:39] Gorilla actually return that. And then

[59:41] from a user side, what do you see is

[59:43] only this execution results. Everything

[59:45] that I just described are just like in

[59:47] the middle.

[59:48] Today, that in the middle just means

[59:50] that a lot of token, a lot of like cost

[59:54] produced.

[59:56] Um so, how would you evaluate an API

[59:59] call? If you are going to do string

[60:01] matching, it's going to be very strict,

[60:03] very hard because those two call, like

[60:06] here, it's actually very detailed, like

[60:08] 1.1 version is very different than

[60:12] 10.1, etc.

[60:14] Um so, what this work produced is that

[60:18] we can actually pass the generated call

[60:21] into a syntax tree.

[60:23] For many of us, when we learn

[60:25] programming earlier days

[60:27] or like computer computer graph, you can

[60:29] actually turn many of them into a graph

[60:31] representation here. So, on the left,

[60:33] this is actually a syntax tree of what

[60:36] do we have here for this particular API

[60:38] call.

[60:40] And then

[60:41] we are going to check whether this is a

[60:43] subtree of the tree that we are going to

[60:46] build from a real API database.

[60:49] So, if it match, then at least it means

[60:52] that this is a valid

[60:54] valid

[60:55] API call.

[60:56] Um so, you will also get us some other

[60:59] numbers. First, if the tree does the

[61:01] subtree does not match, then you know

[61:04] that the model probably hallucinated an

[61:06] API that it does not exist in my

[61:08] database, right? So, it give you a very

[61:10] intuitive idea.

[61:11] Or Um, maybe it a

[61:14] but it give you a wrong node or

[61:17] something like that, then that's a

[61:19] error. You know that this is a error,

[61:21] not a hallucination.

[61:23] Um, to show you the results, uh, first,

[61:26] uh, definitely they are better, uh, than

[61:28] a lot of the baselines they compare.

[61:30] What I want you to see is actually this

[61:32] figure. So, the zero shot here, you can

[61:35] see that if we quantify hallucination of

[61:37] API call uh, versus accuracy on a like a

[61:41] parental analysis figure here, uh,

[61:44] Gorilla, because of this like AST-based

[61:47] uh,

[61:48] like setup, they're actually having a

[61:50] much lower, um, hallucination and a much

[61:53] higher accuracy compared to many of the

[61:55] other models.

[61:57] So, this is actually one way to teach

[61:59] models to use certain type of tools.

[62:03] Okay, so now I I actually shared a lot.

[62:05] Those are actually four classic learning

[62:08] frameworks to think about how to get let

[62:11] the models use tools.

[62:13] And then, again, like take a many steps

[62:15] back. Um, this is again like a a

[62:18] learning approach, which means that we

[62:20] want models to know what a kind of API

[62:22] to use, where to use, what type of

[62:25] things to use, and they need to know how

[62:28] to fetch back the results. So, this is

[62:30] actually a very different thinking.

[62:34] Um, but the issue here is that

[62:38] if, let's say, as some of the question

[62:40] asked earlier, like today, different API

[62:43] and the tools come out every day. Uh,

[62:45] whenever someone introduce a new API, if

[62:48] you train the model before, now you need

[62:49] to retrain your model. This is actually

[62:51] very costly. Or, uh, you need to retrain

[62:54] your word embedding, which is not going

[62:55] to be very flexible as well. So, um,

[63:00] what if what if instead of training the

[63:03] model, we are going to change how those

[63:05] tools are described, so that any model

[63:08] can actually use them at runtime?

[63:11] That is, I'm not going to uh, get my

[63:14] model to know what a kind of things to

[63:16] use as a intrinsic capability. I'm going

[63:19] to make sure those tools are specified

[63:22] in some kind of

[63:24] like universal format so that as long as

[63:27] I can have a conversation with the tool,

[63:29] I know what kind of tool to use, what

[63:31] are the functions they have, etc. So,

[63:33] this is what I I'm going to share next.

[63:35] That is it's actually a not a from a

[63:38] learning perspective, but more from a

[63:40] industry or like a easy-to-use

[63:42] perspective. This is what we call

[63:44] standard interface.

[63:48] Um so, just to kind of recap what I have

[63:51] said or like why we need a standard

[63:52] interface. Um what I have covered so far

[63:56] is

[63:57] um we are changing the model to fit the

[64:00] tools. And then basically every new API

[64:03] means that we need to do another

[64:04] training.

[64:05] But now what I want to share is that in

[64:07] practice, what it

[64:09] works better is that we are going to

[64:11] change how the tools are described so

[64:13] that any model know how to use that.

[64:17] So, this is going to be a mindset shift.

[64:20] Also means that no more math for the

[64:22] next 15 minutes.

[64:24] Okay, so I'm going to share you three

[64:25] generations that we have.

[64:28] Um so,

[64:29] this is also where a lot of debates

[64:31] about tool use happen. Like there was

[64:33] also even a lot of debate on whether we

[64:35] should redesign the internet so that

[64:38] um the internet is going to be

[64:39] agent-friendly because a lot of the APIs

[64:41] we have were human-facing.

[64:44] Okay, so the very last thing I said is

[64:46] this is actually a human-facing uh tool

[64:48] called the REST API.

[64:50] Um

[64:51] a lot of details that you can um learn

[64:54] about that. I will have examples next

[64:56] page. But this is literally um you uh

[65:00] give like the model or like something

[65:03] uh uh string and then they are going to

[65:06] read it or ask you that. And then um

[65:09] this is this this is what's happening.

[65:12] And then you can see that the process is

[65:13] also very human-readable. So, it's like

[65:16] get and then weather CT equals SF here.

[65:21] So, function call is slightly different.

[65:23] It's designed for developers or like

[65:27] designed for the model. So, each tool is

[65:29] going to get a JSON format and then the

[65:31] model every time just emits the name and

[65:34] arguments. And you can also have a

[65:36] harness around it to validate whether

[65:39] the call is is specified correctly.

[65:42] Um

[65:43] and here again, if the tool change, the

[65:47] function call needs to change as well.

[65:50] Okay. So, that's probably also not a

[65:52] very

[65:53] like very easy to use. So, what if we

[65:56] just have a lot of agents now and they

[66:00] all want to use different type of tools.

[66:01] So, this is actually from an ecosystem

[66:03] facing perspective

[66:05] of MSCP.

[66:07] Uh model context protocol is designed

[66:09] for the ecosystem. We will have a server

[66:11] that expose its tools. I'll show you the

[66:14] tool list discovery.

[66:17] Then others or any client can actually

[66:20] discover that at the run time with like

[66:22] tool list or or invoke them with like

[66:25] tool use to call. And then the server is

[66:28] only need to be written once and then

[66:30] reused across many different host.

[66:33] So, I guess like plain language summary

[66:36] here is that rest those are more like

[66:39] English docs like written for humans.

[66:42] Function calls are written in a JSON

[66:44] schema. So, that the models can read.

[66:47] And MSCP, they are written in a protocol

[66:49] format that every model, every

[66:52] application can reuse.

[66:55] So, let's just look at some examples to

[66:56] make it a very clear. So, this is a very

[66:58] classic REST API.

[67:02] A lot of them is actually over like HTTP

[67:04] request. So, here if I want to know the

[67:07] weather at a Stanford today, you just

[67:09] use a get and then give them this kind

[67:12] of URL query. And then you get a code

[67:15] 200 means that

[67:18] success. And then it give you the

[67:20] specific temperature.

[67:22] This is actually what it will look like.

[67:26] Um there are four different actions or

[67:28] even more.

[67:30] Um

[67:31] I think this is the whole vocabulary.

[67:32] Like get, um post, uh put, delete. So,

[67:35] those are very limited actions you can

[67:37] do.

[67:38] So, the limitation for a lot of the REST

[67:40] APIs that the model must know the URL

[67:43] parameter names and response shape. So,

[67:45] you need to get all of those information

[67:47] there.

[67:50] Um the second generation, as I was

[67:52] talking about, is like a function call.

[67:54] That is, what if we actually could uh

[67:56] get those tools in this kind of very

[67:58] structured JSON schema?

[68:00] This is actually a concept, I think uh

[68:03] OpenAI introduced in around uh 2023 in

[68:06] the summer. And then after that, uh many

[68:09] companies follow this tradition. So, the

[68:11] key idea here is that we give tools to

[68:14] the model as some kind of JSON schema.

[68:17] Since like JSON is just much easier to

[68:19] work with. Um and then the model is

[68:21] going to answer with a tool name and

[68:23] type of typed arguments. Uh instead of

[68:26] some kind of free text here. And then

[68:28] the code is going to run the call and

[68:30] then return the results. So, here for

[68:33] the same query, uh instead of a URL, we

[68:36] actually give them a schema. And then

[68:37] the model is going to give us some kind

[68:39] of output also in JSON format. This is

[68:42] just like a much easier.

[68:44] Very earlier days, actually this kind of

[68:45] JSON schema is a great way to do prompt

[68:48] uh engineering because if you just ask

[68:50] the question, it's really hard to get it

[68:52] correct. But if you let them to return

[68:54] the output in a JSON format, uh you get

[68:58] a a little bit more luck with it.

[69:01] Um so, again, the limitation here is

[69:04] that uh since this is a tool call, there

[69:06] is a tool schema, etc.

[69:08] Um if I have a new tool, then

[69:10] um the API or this kind of JSON schema

[69:13] needs to be rewritten, which is not a

[69:15] very uh scalable.

[69:18] Uh this is why like the third generation

[69:20] we are talking about MCP. Um so, it's

[69:23] one protocol between any AI applications

[69:27] and any tools or data source. So on the

[69:30] left you can see that we can have chat,

[69:32] cloud desktop, IDE, cloud code, or other

[69:36] AI applications here. And then MCP sits

[69:39] in the middle and then on the right

[69:41] those are different data sources. This

[69:43] could have be data on the file systems

[69:46] or even your Slack or developer tools

[69:49] such as Git here.

[69:51] And then this is just like a very

[69:54] interesting setup because with function

[69:56] call or function calling we need to do

[69:59] this kind of JSON schemas. Here it seems

[70:02] that we just need to figure out how to

[70:04] do this standardized protocol.

[70:09] Um so if we go a little bit deeper here

[70:11] and there are a few terms that you will

[70:13] encounter. So MCP host is the is the app

[70:17] that you tap into such as like cloud

[70:19] desktop. And then a server is like a

[70:23] tool provider.

[70:25] Um so your local files, your database,

[70:27] remote service. And then client is

[70:30] actually the connection object the host

[70:33] actually creates for each server. So you

[70:35] will have one per server.

[70:37] It would does the handshaking, um deal

[70:40] with the tool list protocols, return

[70:42] results, etc.

[70:44] So you can see that here we actually

[70:46] have four clients here. Means that there

[70:49] are four open connections we have, not

[70:52] four users. It's like four connections.

[70:55] Uh you also see that like server A

[70:57] serves file system, server B uh deal

[71:00] with database, and uh both client three

[71:03] and the client four actually link to

[71:05] this specific server C here.

[71:09] So the host never learns anything about

[71:13] a specific file or database format. It

[71:16] only need to know how to speak MCP

[71:18] language and then they talk to it with

[71:22] this kind of MCP protocol.

[71:25] So you can view it as like a one layer

[71:27] abstraction. So,

[71:29] uh let's see uh you just established a

[71:31] connection between the server and the

[71:33] client. And then, how do I know which

[71:36] tools to use?

[71:37] In the past, we need to get you to train

[71:40] a model to figure out which one gave the

[71:42] lowest loss. Here, you are just going to

[71:45] ask, "What are the tools do you have?"

[71:47] And this is like tools/list.

[71:50] The server is going to return you a

[71:52] list.

[71:53] And then, each tool will have a name,

[71:55] description, a JSON input schema. And

[71:58] then, your job is to decide, "Okay,

[72:00] based on the description, is this the

[72:02] tool I want to use or not?"

[72:05] There is another like tool execution

[72:08] that we keep talking about.

[72:10] And this is like the tool/call

[72:12] in MCP.

[72:14] Basically, it tells the model that, "Now

[72:16] I know which tool to use. Run this tool

[72:19] with those arguments."

[72:21] You need to first pick a tool using the

[72:24] name.

[72:25] And the arguments basically just like

[72:27] fulfill all the input schema. And then,

[72:30] you get a certain kind of results. So,

[72:32] this is actually the process.

[72:34] One matter of thing, if you are just

[72:36] reading this or hearing this for the

[72:38] first time, you probably notice that,

[72:40] "Wow, this format is like insane. Like,

[72:42] am I going to write this kind of like

[72:44] code in my

[72:46] in my code?" The answer is no. We are

[72:49] not going to write it. As I was talking

[72:52] about, like MCP being a protocol, we

[72:55] want the models to actually

[72:58] generate those kind of detailed like

[73:01] schema stuff like that. We are only in

[73:03] charge of some kind of a high-level

[73:05] specification.

[73:07] So, let's let's look at a real example.

[73:09] So, let's see our course actually has a

[73:13] like learning management system. And

[73:15] there's an API.

[73:17] You can have like assignments

[73:19] submissions or deal with

[73:22] grade. So, in the MCP fashion, like

[73:25] there is this like a package called a

[73:27] fast MCP. So, you can basically just

[73:29] tell them like, "Uh this is the specific

[73:32] API I want to uh visit. And then what is

[73:35] the specific like

[73:37] specification I want to give?" And then

[73:40] uh you establish this. Then the model is

[73:42] going to let's see if some some of your

[73:45] agent want to access our

[73:47] course uh LMS, and then they are going

[73:50] to see what are the tools

[73:53] do you support? And then our course will

[73:56] tell you like we support to give you the

[73:58] list of assignments, get the

[73:59] submissions, or even post the grade.

[74:02] Okay. This seems fine, right? But then

[74:05] think about any of you can build the

[74:07] agents to access our course website. And

[74:10] then post the grade is probably not a

[74:12] something that everyone will have access

[74:14] to. So, in addition to also enable the

[74:17] connection, we could also control who

[74:20] has access to what kind of tools.

[74:23] So, very

[74:24] simple again, let's using this as an

[74:27] example. You can see that the course MCP

[74:31] server actually sits between your agent

[74:34] and then our kind of like rest API here.

[74:37] And then there is going to be an inbound

[74:38] kind of check whether you have access

[74:40] for a specific thing. But again, there

[74:43] is also outbound here.

[74:45] Uh one interesting thing is that agent

[74:47] never sees my like LMS token here. And

[74:52] likewise, like API you never see the

[74:54] agent token. So, everything is like kind

[74:55] of separate. So, you are only allowed to

[74:59] use whatever tools you are allowed to

[75:01] do. Anything beyond that, we will get it

[75:04] with like access or off here.

[75:08] So, this is actually what do we have in

[75:10] terms of standard interface.

[75:12] Um it may look like a lot of content,

[75:14] but it's really just like protocol

[75:16] change. And

[75:18] people have been using them very often

[75:21] these days. And so, it's a very

[75:22] practical thing that you can play

[75:23] around.

[75:24] So, in the next 3 minutes, I'm going to

[75:26] quickly mention

[75:28] a few tool use data sets just as an

[75:31] information for you to know where to

[75:33] look at.

[75:35] Uh this is actually the live leaderboard

[75:37] from Berkeley called the Berkeley

[75:39] function call leaderboard. So, if you

[75:41] care about the function call, this is

[75:42] actually a great resource to check out.

[75:45] They benchmark different models in terms

[75:47] of the data set.

[75:50] Um so, the evaluation here, we already

[75:52] briefly talked about that. So, you can

[75:54] do this abstract syntax tree matching to

[75:57] quantify hallucination. You can also

[75:59] look at the execution to see whether you

[76:01] get it right or or wrong. Uh you can

[76:04] also do like a lot of like state-based

[76:06] evaluation for multi-step or multi-turn

[76:08] function call here.

[76:10] Their data set is created by looking at

[76:13] a lot of real-world use case established

[76:15] from different taxonomies.

[76:18] Um they also try to insert some

[76:20] situations where um you can also check

[76:23] for a specific query, if the answer is

[76:26] no, there's no not available tool, or

[76:28] no, I cannot deal with this, model knows

[76:31] how to uh fact like factor it back. Not

[76:33] only just to give you a like fixed query

[76:36] or API.

[76:39] Um if you are interested in checking out

[76:40] the data set, I think like this is

[76:42] literally what a function call look

[76:44] like. Um multiplication, parallel

[76:47] function, or even like a relevance

[76:49] detection here. So, a wide range of

[76:52] function call situations.

[76:55] I already talked about the tool bench uh

[76:57] where they use this kind of synthetic

[76:59] data construction to come up with how

[77:02] ChatGPT solve a particular user query,

[77:05] and then you can use it to quantify

[77:07] whether your systems can use tools

[77:10] correctly or not.

[77:13] Um tool bench is actually another uh

[77:15] widely used approach or data set. It

[77:18] basically introduced the role of

[77:20] customer. So, now you have a agent, and

[77:23] then the customer is interacting with

[77:24] the agent. Um the customer may want to

[77:27] cancel their flight or may want to

[77:29] change their flight, and then the agent

[77:31] needs to know which correct tool call to

[77:33] use to make the action happen. So, it's

[77:36] actually this kind of tool agent and

[77:38] user interaction data set.

[77:41] Uh last thing that I want to mention

[77:44] here is if you think about evaluation.

[77:47] For a lot of retrieval we talked about

[77:49] the last class. We use pass at a K that

[77:52] is if you tried it a K times, if you

[77:54] succeed once, then that's good.

[77:57] However, when it comes to this kind of

[78:00] multi-turn interactions, we actually

[78:02] want reliability and the consistency.

[78:05] The user is not going to try your

[78:06] systems eight times and then as long as

[78:09] one time work, they are happy. As long

[78:11] as the user tried it, it didn't work,

[78:12] user is going to be very angry, right?

[78:14] So, this is why we need a new metric

[78:16] called a pass hat at K here.

[78:20] It literally means that if I tried it at

[78:22] K times out of N, I want all my K times

[78:25] to succeed. So, this is actually a much

[78:27] stronger metric.

[78:30] Um Top Bench the first version include

[78:32] the retail and the line. You can see the

[78:34] numbers here.

[78:36] Um what I can share with you especially

[78:38] in the bottom is that pass hat at K and

[78:42] pass at K has a very different trend.

[78:44] So, this is why we need to be very

[78:46] careful in terms of what the metrics we

[78:49] are going to use.

[78:51] Top Bench also has evolved a lot. The

[78:53] one that I've mentioned is from 2024.

[78:56] You can see that over the last the two

[78:58] years, now we just have Top Square

[79:00] Bench, Top Knowledge, Top Voice, a lot

[79:02] of those.

[79:04] So, with that, that's all what I want to

[79:06] cover today and thank you. See you next

[79:09] class.
