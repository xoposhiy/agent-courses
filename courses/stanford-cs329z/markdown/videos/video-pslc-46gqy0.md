# Lecture 3 transcript: Retrieval-Augmented Generation (RAG)

[Course index](../../README.md) · [Original source](https://youtu.be/psLc-46GqY0) · [Raw file](../../raw/videos/psLc-46GqY0.json)

Retrieved: 2026-11-13T16:18:51.886153+00:00

[00:05] Okay, uh welcome to uh lecture three. Uh

[00:08] today we are going to cover rag and

[00:10] agents.

[00:12] So, I will start this lecture by giving

[00:14] you a quick overview of the projects

[00:17] since we already got a lot of questions.

[00:21] Um overall, I think uh the general rule

[00:24] of thumb before projects is that we

[00:26] really hope that you can pick a topic

[00:27] that you are very very excited about

[00:30] yourself. Um so, think about questions

[00:32] such as what a task does your agent do?

[00:36] Um what are research questions drive it?

[00:39] Um what kind of data or API we have to

[00:42] support it? And which agent frameworks

[00:45] you are going to use? And more

[00:47] importantly, how would you evaluate

[00:49] that? So, those are some kind of guiding

[00:52] principles.

[00:54] And then um related to this, just to go

[00:57] a little bit uh deeper here, um the goal

[00:59] of this course or the goal of the course

[01:02] project is to help you to enable you to

[01:06] design, build, and evaluate uh agent

[01:08] systems of your own.

[01:10] And the focus here, uh we encourage you

[01:12] to think about the building agents using

[01:15] retrieval, tool use, memory, multi-agent

[01:17] systems, uh different optimization

[01:20] hardness, the data agents use, uh or the

[01:24] evaluation, and how to make agents safe.

[01:27] So, a lot of topics around that would be

[01:29] really good uh candidates for project.

[01:32] One thing I do want to highlight here is

[01:35] about the rigorous evaluation.

[01:37] Um so, in the end, we are going to see

[01:39] the demo presentation from you all. A

[01:42] demo that works once, just like it only

[01:45] happened to work during the final

[01:47] presentation, will not score highly. Uh

[01:49] we really want you to think about the

[01:51] rigor behind your system.

[01:53] Um think about like the task. Where does

[01:56] your data come from? What counts as

[01:58] success here?

[02:00] Think about

[02:01] uh how to really grade or evaluate your

[02:04] agents. You can think about LLMs a

[02:06] judge, different rubrics, human ratings,

[02:09] feasibility check, or just like a

[02:11] mixture of many of them.

[02:14] In terms of how to report the results,

[02:17] think about different type of task. It

[02:19] shouldn't just work on one single user

[02:21] or one single data point. Baselines you

[02:24] can incorporate and

[02:26] more importantly where your agents are

[02:28] fail. So those are some dimensions to

[02:31] think about.

[02:33] To give you some kind of sample or

[02:35] example topics.

[02:37] So if you read this long list, there are

[02:39] a lot of exciting topics you can look at

[02:43] such as evaluating agents,

[02:45] cost, latency, safety beyond task

[02:48] success.

[02:49] You can think about how to adapt agents

[02:51] to new environments, new tools,

[02:54] new APIs, new UIs.

[02:57] Robustness of agents to prompt

[02:59] injection,

[03:01] adversary attack.

[03:02] Why agents misuse tools,

[03:05] learning to use, learning a lot of

[03:07] capabilities for agents from limited

[03:10] data.

[03:11] Interpreting agent behaviors, long tail,

[03:14] long horizon, edge cases related to

[03:17] agents.

[03:18] Human agent or agent agent teaming, how

[03:21] can we get a group of agents to work

[03:23] well with each other and get agents and

[03:26] human workers to work together.

[03:28] Multi-agent systems around of memory,

[03:30] planning, over set, reward hacking,

[03:33] we'll have some lectures about safety

[03:36] later this quarter.

[03:39] If you read the website, we do offer

[03:42] some kind of example ideas. In the very

[03:44] beginning of designing this course, we

[03:46] really hope that

[03:48] students could build agents to make your

[03:50] life at a Stanford much easier.

[03:53] So you can think about the building

[03:54] agents that could read syllabus and then

[03:57] put the deadlines to your calendar

[03:59] automatically. You can think about

[04:01] course schedule optimizer for next

[04:03] quarter. You can think about research

[04:05] paper discovery and the summarization

[04:07] agent. Campus event aggregator and the

[04:11] recommendation system. Coding agent

[04:13] specialized for one specific coding code

[04:16] base, framework, or language, as well as

[04:20] rigorous evaluations

[04:22] around the figures and artifacts.

[04:26] So, a lot of topics you can choose from.

[04:29] One

[04:30] minor recommendation here, but actually

[04:33] turned out to be very important is you

[04:35] should always consider the availability

[04:38] of data, agentic frameworks,

[04:40] computation, compute, and evaluation.

[04:44] Missing any of them may lead your

[04:46] project to be not as successful.

[04:50] Some final recommendations here.

[04:52] So,

[04:53] start earlier and work on it every week

[04:56] rather than just like a rushing

[04:58] in the final week.

[05:00] Get your data first. Make sure what kind

[05:02] of agentic application you want to focus

[05:05] on, where you should get the data.

[05:07] We recommend that you have a very clear,

[05:09] well-defined research question.

[05:12] Novel, creative questions are highly

[05:15] recommended.

[05:17] You probably see that there is one

[05:19] sentence that I bolded bolded here is

[05:23] results should teach us something. So, I

[05:26] think you should use this as a guiding

[05:27] principle. When you build something,

[05:29] when tears or myself read it,

[05:32] what are we learning from your project?

[05:35] Present and visualize your results very

[05:37] well, and more importantly, come talk to

[05:39] us during office hours,

[05:42] and we will be very happy to help.

[05:45] Okay.

[05:46] Any quick questions about projects?

[05:52] Okay, since the content is very clear,

[05:55] now I'm going to move to

[05:57] the content today. We are going to focus

[06:00] on rag.

[06:01] I will first start with a motivation for

[06:03] rag, and then we will go deep into the

[06:06] rag

[06:07] pipeline. Uh we will talk about some

[06:09] very detailed uh building components

[06:11] such as how you do indexing,

[06:14] um how to do retrieval, and agentic rag,

[06:17] as well as some feeder mode here.

[06:21] Let's get it started. The learning

[06:23] objective uh as I wrote here is by the

[06:27] end of this class, you should know how

[06:29] the pipeline is built, where it breaks,

[06:32] where what to index, and how to index,

[06:34] and how to search it.

[06:36] This lecture is related to your homework

[06:38] one.

[06:40] Let's start with one example here that

[06:43] uh many of you probably uh recognize. Uh

[06:46] if you ask a LM when office hours are

[06:50] least crowded,

[06:52] and I think you'll get something like

[06:54] this, where it tells you that try the

[06:57] Wednesday afternoon sessions. Midweek uh

[07:00] office hours are usually uh quiet.

[07:04] Um and it look fine.

[07:06] Um it's a guess from the prior

[07:08] knowledge. There's nothing behind it.

[07:10] Now, if you give the same model with the

[07:13] the Q log that we have recorded in terms

[07:16] of how many people show up to office

[07:18] hours, it actually read that Tuesday at

[07:21] 4:00 p.m. had a 14 people waiting and

[07:23] the Thursday at 9:00 only had a three.

[07:26] So, it tells you that you should go to

[07:28] Thursday morning uh office hour with

[07:30] those numbers.

[07:32] The difference is here is not about the

[07:34] fluency. Uh I think uh both answers are

[07:36] fluent here. The difference is actually

[07:39] about the evidence. The second uh

[07:41] response here, it actually tell you the

[07:44] actual data uh together with the model

[07:46] response. So, the answer is something

[07:48] that you can actually check.

[07:52] So, the idea behind the rag or the

[07:54] design principle behind the rag is that

[07:57] we do not want a models to memorize

[07:59] everything. Instead, we want them to uh

[08:02] think about finding the relevant

[08:05] information just in time at the moment

[08:08] where the model needed.

[08:10] And retrieval is actually a mechanism

[08:12] that achieve such goal here.

[08:15] Um two things I want you to remember.

[08:18] First is that this is a dynamic process,

[08:21] which means that when the facts change,

[08:24] you update the index, not not the

[08:26] weights.

[08:27] And then um

[08:29] it's also very interpretable because the

[08:31] model can point out like where the

[08:34] document they fetched the information.

[08:36] And this give you like citations. And it

[08:39] means that a human, if we want, we can

[08:41] actually go there and then verify the

[08:44] answer.

[08:46] So um I want to start with a very

[08:49] classic a setup. Uh this is actually uh

[08:52] earlier days, uh people are working on

[08:54] open domain question answering. And

[08:56] there are two stage that's very similar

[08:58] to the rag we are talking about today.

[09:01] Um if you have a question coming in

[09:03] here, um there is going to be a document

[09:06] retriever that runs over all possible

[09:09] Wikipedia pages, and then fetch a

[09:12] handful of articles.

[09:14] And then the document reader takes those

[09:17] articles and extract the answer.

[09:20] Uh so here you can see the particular

[09:22] number here.

[09:23] The division of labor is actually the

[09:26] the whole point here. The retriever

[09:28] basically narrow down millions of

[09:30] articles into a few, and then the reader

[09:33] does the very fine-grained processing on

[09:35] those few candidates.

[09:37] Um you need to have both in order to get

[09:40] the task done here.

[09:44] So if you go a little bit deep into the

[09:47] retriever reader framework, so let's

[09:49] just try to formulate them a little bit.

[09:52] Uh you have a large collection of

[09:53] documents D here. This could have been

[09:56] D1, D2, DN here.

[09:58] Uh N is in general very big. It could

[10:00] have been millions of documents. And you

[10:03] do have a question. We want the model to

[10:05] output a answer here, A.

[10:08] So if you use this formulation, what the

[10:11] retriever does is that it actually try

[10:14] to retrieve key top-ranked passages

[10:17] here. K here is very small, like 100,

[10:21] 50, or 10.

[10:22] >> [clears throat]

[10:23] >> And then your reader is going to read

[10:24] those top passages here and then return

[10:28] you a specific answer.

[10:31] Very earlier days, the way how we

[10:33] implement a retriever is actually a very

[10:36] standard TF-IDF

[10:38] processing.

[10:40] This is through a fixed module.

[10:42] And then the reader is actually where a

[10:44] lot of the earlier neural network

[10:46] efforts were about.

[10:48] So, you can have your reader as a neural

[10:50] reading comprehension model. This could

[10:53] be trained on squad, which refers to

[10:55] Stanford question answering data set, or

[10:58] other type of like question answering

[11:00] data sets.

[11:02] Today, you can also use a zero-shot

[11:03] LLMs, ChatGPT, to do this kind of reader

[11:07] function.

[11:09] So, this is the very classic retriever

[11:12] reader framework.

[11:13] And now this comes

[11:16] to our main focus today called retrieval

[11:19] augmented generation, RAG, here. Let's

[11:22] just walk through this figure from left

[11:24] to right before I unpack many of the

[11:27] components here.

[11:29] So, let's see we have a specific query

[11:31] X. The query X actually goes into

[11:35] what we call a query encoder, QX, here.

[11:39] The vector actually runs against the

[11:41] document index with algorithms such as

[11:44] maximum inner product search, MIPS.

[11:48] This is the non-parametric process.

[11:51] And then you got those like top key

[11:53] documents. The top key documents will

[11:55] then go through this kind of generator,

[11:58] P theta, here, which is what we call a

[12:01] parametric part. And then we can

[12:03] marginalize over the documents to get

[12:05] the output.

[12:07] So, the important detail here is that

[12:09] this is actually a end-to-end training

[12:12] pipeline. The gradient is going to flow

[12:14] back

[12:16] through the generator and to the query

[12:18] encoder.

[12:20] The frozen part of this process is

[12:22] actually the document index because it's

[12:25] huge. We are not going to learn them

[12:26] like all the time.

[12:28] Um this is also the same model behind

[12:31] the many different task. So if you

[12:34] curious about the question answering,

[12:36] fact verification, even generating like

[12:39] Jeopardy-like questions, I think this is

[12:41] a framework to use.

[12:43] A lot of follow-up work was also built

[12:46] on top of ideas of RAG.

[12:49] So this is a very quick intro to RAG.

[12:53] Um

[12:54] having known that why we need a RAG, I'm

[12:57] now going to go through the detailed

[12:59] process. What the retriever does, what

[13:02] the generator does, and then how are we

[13:04] going to train those two components

[13:06] together.

[13:08] So um

[13:10] RAG, you can think about them as two

[13:12] components. As I mentioned, there is

[13:14] this retriever.

[13:15] So basically you have your context X and

[13:18] then um

[13:20] you want to return the top K documents

[13:23] for a specific query X.

[13:25] The generator is going to write the

[13:27] answer one token at a time giving the

[13:30] query X and then what you have retrieved

[13:33] so far that's relevant to the current

[13:35] query.

[13:36] So the high-level idea here can be

[13:38] really decomposed as for my

[13:41] query X, what is the answer Y here? And

[13:45] then you can actually decompose them

[13:47] into two components.

[13:49] First, how can we get a Z PZ giving X?

[13:52] Second component is once you have X and

[13:55] the Z, how should we generate Y here?

[13:58] So this is a very kind of high-level

[14:01] process.

[14:02] One minor thing here that I do want to

[14:04] mention is

[14:06] the actual process of RAG actually had a

[14:09] two variants here. One's called a RAG

[14:12] sequence. That is you pick one passage

[14:15] and then you generate the whole answer

[14:17] with it.

[14:19] Right a token means that

[14:21] every time we are going to re-weight the

[14:23] passage at every token of the answers.

[14:25] So, you do not kind of fix a passage for

[14:27] the entire answer generation.

[14:32] Let's go a little bit of deeper here.

[14:34] So, once you have this kind of retriever

[14:37] and a generator, we need to train this

[14:39] architecture. This is actually done in a

[14:42] joint training fashion where we jointly

[14:44] train the retriever and a generator to

[14:47] really just minimize the negative log

[14:49] likelihood here. This is should be very

[14:52] familiar to many of you.

[14:54] Um

[14:55] Basically, you have a ground truth

[14:56] answer and then you have a generated

[14:58] answer. We are going to see whether they

[15:00] match. That's the key idea here.

[15:05] Now, let's go a little bit of deeper

[15:07] into how retriever is is learned and how

[15:10] to even represent a retriever and a

[15:12] generator.

[15:13] So, in the classic rag fashion, the

[15:17] retriever is

[15:19] dense passage retriever here, DPR.

[15:23] We basically are going to use two BERT

[15:25] encoders here. BERT was used like

[15:28] frequently earlier days.

[15:31] So, basically, what it does is that we

[15:33] are going to

[15:35] pass the passage and question to

[15:38] different BERT encoder here. So, we get

[15:41] a query encoder. We also get a document

[15:44] encoder and then we look at the inner

[15:47] product of their those two vectors. This

[15:51] is basically the score we are going to

[15:53] use to rank documents.

[15:56] Those passage vectors, they can be

[15:59] computed at once and then stored in a

[16:01] index. So, this often is like in

[16:04] offline. So, at the query time, we only

[16:08] like encode the question and then run

[16:10] this

[16:11] MIPS search to gather the top K. So,

[16:14] basically, the document part is what we

[16:16] can actually process offline.

[16:19] Um then this exponential basically just

[16:22] like turns the score into a distribution

[16:25] over different retrieved passages here.

[16:28] And then that's what the sum on the

[16:30] right slice is about.

[16:34] The generator part, again this is a

[16:36] design choice. You can actually try

[16:38] different type of setups. I'm going to

[16:40] use BART which is a earlier

[16:42] encoder-decoder architecture as an

[16:45] illustration here.

[16:46] Um but you can use any kind of sequence

[16:48] to sequence model here.

[16:51] The input is very simple. We basically

[16:53] concatenated the question and then the

[16:55] retrieved passenger. And then we feed

[16:57] them into the encoder. And then we let

[17:00] the decoder write the answer one token

[17:03] at each time.

[17:05] Uh there is no like special architecture

[17:07] for retrieval. And then the retrieved

[17:09] passage is just a actual text in the in

[17:13] the context. And this is also why RAG

[17:16] can easily transferred to modern LLMs

[17:19] where we do the same thing just with a

[17:21] prompt.

[17:24] So let's look at some of the RAG

[17:26] performance. Again, this is a little bit

[17:29] more earlier days. Uh today I think a

[17:31] model performance on those data sets are

[17:34] much higher.

[17:35] Uh there were two there were like two or

[17:37] four

[17:38] data sets that we use frequently.

[17:41] Um natural questions is from Google,

[17:43] TriviaQA, WebQuestions,

[17:46] and Curated Track here. You can see that

[17:49] compared to just simple DPR or the

[17:52] earlier algorithm,

[17:55] RAG based fashion actually lead to a lot

[17:57] of boost here.

[18:00] When you also give the output to humans

[18:02] to let humans read for the for the

[18:05] answers from RAG versus from earlier

[18:08] BART or other systems, which one is

[18:10] better? And you can see that from a

[18:12] factuality factuality or specificity

[18:16] perspective, RAG is written better most

[18:19] of the time.

[18:20] So I think it basically pointed out the

[18:23] the key contribution of rag that is it

[18:26] literally does better grounding compared

[18:29] to a lot of the systems we have because

[18:32] the retrieved the content is really

[18:34] doing the work for us.

[18:37] So, what I just went through is a very

[18:39] classic first rag paper and rag actually

[18:43] has evolved like like significantly in

[18:47] the last few years. The very left side

[18:50] is the naive rag fashion where you can

[18:52] see user query documents, we do index,

[18:56] we do retrieval, and then we can query

[18:59] the model to answer it.

[19:01] You can also add some kind of components

[19:03] there to make rag more more

[19:05] sophisticated and more powerful.

[19:08] In the middle column, you can see that

[19:10] pre-retrieval, you can actually do

[19:13] something like query routing or query

[19:17] rewriting, query expansion. You can

[19:19] actually provide a lot of rich context

[19:21] for your query to make it easily

[19:24] like processable.

[19:26] And then post-retrieval, you can also do

[19:28] maybe you try the different approach to

[19:30] do the retrieval. So, maybe you want to

[19:32] combine them, you want to re-rank them,

[19:34] you want to summarize them, you want to

[19:36] fuse them together. So, there are a lot

[19:38] of like techniques you can actually

[19:40] introduce to make rag better.

[19:44] I think like more recently this kind of

[19:47] more modular rag

[19:49] on the right part actually goes one step

[19:52] further. It break everything into

[19:55] modules, search, routing, rewrite,

[19:57] re-rank, memory, and fusion. And then

[20:00] you can compose them into patterns such

[20:02] as retrieve and then read or iterate

[20:06] iterative retrieve and then read.

[20:09] So, this is just what do we have today?

[20:11] I think you can do a lot of design

[20:13] choices on top of those different

[20:16] components.

[20:18] Before we move to the specific index,

[20:21] any quick question here?

[20:23] >> For the slide where showed that RAG is

[20:25] performing better than the other models.

[20:27] When something like that is sort of

[20:28] proposed for the first time, do we also

[20:30] think of how much faster or is it due to

[20:32] the other reasons?

[20:33] >> Yeah, great question.

[20:35] Um

[20:36] The question is, in addition to

[20:37] performance comparison, do we have any

[20:39] benchmarking of speed and the memory and

[20:42] even cost? Um

[20:44] so uh in later in this lecture, I will

[20:47] mention some of the different components

[20:49] in terms of a latency and others when we

[20:51] compare those methods. I do think that

[20:54] this is a very key

[20:55] uh difference. This is why when I was

[20:57] talking about like for the document

[20:59] index, this is something we can actually

[21:01] process uh like offline. Uh when we have

[21:04] more kind of encoders that I'm going to

[21:06] talk about, you will see that uh some of

[21:08] them you can actually precompute them.

[21:10] Some of the other like BERT encoders,

[21:12] you really cannot precompute them

[21:14] because you need to put in the context

[21:16] and document in the same matrix and then

[21:19] do attention mechanism. So, this is

[21:21] going to be a big consideration as we

[21:23] move along.

[21:26] >> Um

[21:27] When you're using

[21:28] API models on like say ChatGPT or like

[21:32] um more frontier models, um is RAG

[21:36] already implemented within them or

[21:39] do we need to like add on more like

[21:43] like extra RAG instructions within the

[21:45] agent?

[21:46] >> Yeah, uh the question is, for more than

[21:49] models, are we going to still do RAG

[21:52] explicitly or is it already built in

[21:55] with them? Um so, the answer is uh RAG

[21:59] as a principle, uh it can always work

[22:02] even for frontier models. Let me give

[22:04] you one example. Let's say you run a

[22:06] company and the company is for specific

[22:08] financial services. All the data, all

[22:11] the specific database are just not

[22:13] public online. So, in that situation,

[22:15] it's really hard for the model to know

[22:17] everything. Then when you use the model

[22:19] there, you can give them access to

[22:21] certain kind of like local database. In

[22:24] this way, uh RAG still applies there and

[22:27] you can use any kind of frontier models

[22:29] here in in this uh perspective. I think

[22:32] if it's really just about the general

[22:34] internet search, uh I think uh since

[22:36] GPT-4,

[22:38] um many of the models already support

[22:40] that. So, like if you're asking a

[22:41] question of um

[22:43] what's the weather today in in uh Palo

[22:46] Alto, it actually can go fetch some of

[22:48] the existing database and answer you the

[22:50] question.

[22:53] Okay.

[22:53] Maybe last question.

[22:55] >> Uh I was just wondering like

[22:57] uh I'm wondering the retriever inside

[22:59] RAG, like do we still use BERT behind

[23:02] the scenes as a more advanced approach

[23:04] or we are we are we are having better

[23:06] options?

[23:06] >> Yeah. So, I will go um detailed in terms

[23:10] of different approach of how we encode

[23:12] it. Uh so, I used BERT as one example

[23:15] here, but uh we all know that the field

[23:17] has changed dramatically. BERT now is

[23:19] viewed as very historical. Uh so, we are

[23:22] going to move to more modern methods

[23:24] just in a few slides.

[23:27] Okay, I'm going to continue. Um

[23:30] So, uh I always love the questions.

[23:33] Um now I want to go like one layer

[23:36] deeper. Uh this is actually a technique

[23:38] called indexing. Basically, when you

[23:40] want to do retrieval, you need to have

[23:42] the unit where you can

[23:43] like provide embeddings for the unit.

[23:46] And then, how do we make sure that each

[23:48] chunk here uh carries enough context to

[23:51] be found?

[23:53] Um so, going back to what makes a good

[23:56] retriever. Uh

[23:58] so, still embedding is very popular. If

[24:01] you think about a statical word um

[24:04] examples such as word-to-vec or GloVe,

[24:07] which we covered at the CS224N,

[24:10] um here you are going to get embedding

[24:12] for each word for each token.

[24:14] Um you can also get a contextual

[24:16] embedding uh such as using BERT. Uh you

[24:19] can also use different architecture

[24:21] here. Basically, this token

[24:23] representation is going to take care of

[24:25] the context. So, if you have a word like

[24:27] a bank, um in this contextual uh

[24:30] fashion, you are going to encode

[24:33] the financial

[24:35] connotation versus bank

[24:38] its own may have different meanings.

[24:41] You can also use the passage as a unit

[24:43] here. You can do sentence bird. You can

[24:46] do DPR that I mentioned earlier. You can

[24:48] also try different architecture here.

[24:50] Then the unit here is not a word. It's

[24:53] not a token. It's actually a like

[24:56] segment of text.

[24:58] You can also have multimodal information

[25:01] here. For example, clip.

[25:03] This actually provides both encodings

[25:06] for text and image tokens.

[25:09] Here, you put a text and image into the

[25:12] shared space.

[25:14] You can also go towards like multimodal

[25:16] where you have both audio, image, and

[25:20] text.

[25:21] So, this is just one specific example.

[25:24] We can also go a bit deeper. Graph.

[25:28] You can have node to vector, like node

[25:30] to back. You can have like a different

[25:32] graphic neural network graph neural

[25:35] network encoder here, GM. And then you

[25:38] your your like embedding is going to

[25:40] capture the node information or the

[25:42] relation between different node.

[25:45] This page is just to show you that the

[25:47] reason why rag or a lot of the design

[25:50] principles behind the rag are still

[25:52] powerful is because they do apply to a

[25:54] lot of like task as we will see in the

[25:58] next 10 minutes.

[26:01] One thing that I do want to mention here

[26:03] is that in order to make the retrieval

[26:05] good, in addition to have a good

[26:08] embedding representation per chunk, you

[26:11] also need a similarity metric. In

[26:14] general, people just use cosine or like

[26:17] inner product here. And the simple

[26:19] approach actually work very well.

[26:23] So, now let's think about the chunking

[26:25] process here. This is the basic unit in

[26:28] retrieval. And you can imagine if I have

[26:31] a really really long document, how can I

[26:34] segment them into different pieces?

[26:37] The first approach is very simple. Let's

[26:39] just do a fixed size segmentation. You

[26:42] can just segment it based on size. I'm

[26:44] going to have 100 to 500 tokens per

[26:47] segment.

[26:48] If the segment is very small, then the

[26:51] vector does not have enough context.

[26:53] If the segment is very large, then a

[26:57] vector may carry or average many many

[27:00] topics. That's also not good. So we want

[27:02] something in the middle and that in the

[27:05] middle needs to be well configured.

[27:08] You may also want to think about that,

[27:10] okay, if I have this segment and that

[27:12] segment,

[27:13] how should I preserve information shared

[27:16] between them?

[27:17] This is a technique called overlap. In

[27:19] general, we are going to have 10 to 20%

[27:21] of the tokens kind of overlap. So those

[27:25] two two like intervals will have some

[27:27] overlap with each other. In this way, we

[27:29] can actually preserve some of the

[27:31] context or center sentence boundary

[27:34] information.

[27:36] Beyond that, you can also do some kind

[27:38] of semantic segmentation where you can

[27:41] just be like, I'm going to just use this

[27:43] one sentence as one unit or this one

[27:45] paragraph as one unit. Those are

[27:48] different design choices.

[27:50] Beyond that, you can also do something

[27:52] even more sophisticated.

[27:54] For example, people do this context

[27:57] enriched chunking where each segment

[28:00] actually carry additional metadata or

[28:03] summaries from this particular segment.

[28:08] Today, you can also get LLMs to help.

[28:10] This is what we call a AI-driven dynamic

[28:12] chunking. You can use LLMs to detect

[28:15] natural kind of breakpoints. So in this

[28:18] way, you get something that's very very

[28:20] semantically meaningful.

[28:24] Let me show you one example here just to

[28:26] see how that really works. Let's see you

[28:29] are curious about the greeting and uh

[28:33] And then on my screen, this is the

[28:34] example. Uh grading the project

[28:36] milestone is due week six. This is

[28:38] actually wrong information. Check out

[28:40] website for correct information.

[28:42] Um so, if you are going to only do fixed

[28:45] size chunking, this is actually what you

[28:47] have. You will just have this kind of

[28:48] different uh segments of the original

[28:51] document.

[28:53] If you do uh fixed size with overlap,

[28:56] you will see that some of those

[28:58] information are actually overlap with

[29:00] each other. This is the low-level

[29:02] representation behind the scene.

[29:04] And then if you want to do like semantic

[29:07] um segmentation, just based on headings

[29:09] of what our website, then you get the

[29:11] entire block here.

[29:13] So, this example is just to illustrate

[29:16] that different segmentation technique

[29:18] actually matters when it comes to this

[29:21] very low-level representation for your

[29:23] retrieval unit.

[29:27] If you are paying attention to the

[29:28] field, actually um one of the widely

[29:31] used technique today is called a

[29:33] contextual retrieval.

[29:35] Uh so, if you read this query, what was

[29:37] the revenue growth for ACME Corp in Q2

[29:41] 2023?

[29:43] And this is actually the perfect segment

[29:45] we are going to find from the coppers.

[29:47] But if you read this

[29:49] uh result, this is actually not a very

[29:52] intuitive because

[29:54] which company is this the company here?

[29:57] Which quarter are we talking about? This

[30:00] segment does not really carry much

[30:02] information.

[30:04] Um our query actually ask for this

[30:06] specific company, specific quarter,

[30:08] specific year, and all of those

[30:10] information are just not there in my

[30:13] like retrieved the content here.

[30:15] So, how about we can actually have a

[30:17] mechanism to put those words back? So,

[30:20] on the right, what if the retrieved

[30:23] segment for me is actually those words

[30:25] highlighted in yellow here, and then

[30:28] followed by the original segment

[30:30] content? If we can have this, now now we

[30:34] have both the company and timing

[30:36] information in the text. And then mine

[30:39] like vector index or my keyword index

[30:42] can now just like match with each other.

[30:44] So if we could have this, that's

[30:46] amazing.

[30:47] Uh how can we achieve that?

[30:50] Um this is a technique uh proposed by

[30:53] Anthropic. Uh so basically for each

[30:56] segment, we are going to run a prompt

[30:59] over the whole document and get back

[31:02] around 50 to 100 tokens of the context

[31:06] and then pre uh prepend it to the

[31:08] segment themself.

[31:11] And then we can index this

[31:12] contextualized segment twice. Uh first

[31:15] time we'll just run them through a

[31:17] embedding model where we can get their

[31:20] uh vector representation.

[31:22] The other is that we are going to put it

[31:24] into a BM25 here to get their sparse

[31:28] index.

[31:29] Um probably you noticed that we actually

[31:31] did it twice. Why do we need a both of

[31:34] them?

[31:35] In practice, we actually want to use

[31:37] both because embeddings in general give

[31:40] us semantic meaning match. However,

[31:43] TF-IDF BM25, despite it being a very

[31:47] classic traditional metric, they are

[31:50] actually very very powerful. They can

[31:52] help us with exact numbers uh and then

[31:56] you can you can just take the best of

[31:58] both world and then merge them.

[32:02] Um one thing I I do want to mention uh

[32:04] as you can imagine, that is if you are

[32:06] going to give a prompt and then to add

[32:09] this additional context, then you

[32:12] basically need to pay a cost per search

[32:16] per uh segment. And then this is

[32:18] actually something quite uh expensive

[32:21] just to think about.

[32:23] Uh now comes to the uh exciting uh

[32:26] moment. How do you really achieve this

[32:28] kind of uh context?

[32:31] Well, you write a prompt. And this is

[32:33] actually what it would look like. You

[32:35] basically tell the model that here is

[32:38] the chunk we want to um situate within

[32:40] the whole document. Please give a short

[32:44] uh sufficient context to uh situate this

[32:47] chunk with the overall document. So, you

[32:49] basically write a prompt, and then the

[32:51] LM actually scan the entire documents,

[32:53] give you a summary of the context.

[32:57] Uh nothing sophisticated is here, and I

[32:59] think like now you really leverage the

[33:02] overall context, and then you also have

[33:05] the specific segment. You combine both

[33:07] of them. Now we are good.

[33:11] Compared to uh a lot of the classic

[33:13] approach, uh researchers show that uh

[33:16] um contextual embeddings actually reduce

[33:20] uh retrieve failure rate.

[33:22] So, this metric I'm going to mention it

[33:25] uh uh in a few slides later, uh but uh

[33:28] they quantify this failed retrieval at

[33:30] the 20. That is, if you look at the top

[33:33] 20 results, uh how many of them uh fail?

[33:37] And then uh you can see that compared to

[33:40] embedding, contextual embedding actually

[33:42] uh drop the error rate from 5.7 to 3.7.

[33:47] And then this is a combination, the

[33:50] hybrid approach. Uh it also drops from 5

[33:53] to 2.9. So, it's actually pretty um

[33:57] like uh useful. And uh

[34:00] also, I think you already noticed that

[34:03] uh having both embedding, like you use

[34:05] in uh embeddings and also BM25, the

[34:08] combination of them actually give us

[34:10] much better performance.

[34:13] So, this is about uh more kind of like a

[34:15] modern approach of doing uh

[34:18] retrieval.

[34:19] Uh the last thing that I or maybe not

[34:21] the last, one of the last thing I'm

[34:24] going to mention here is this technique

[34:26] called late chunking here.

[34:29] So, let's just look at the picture. The

[34:31] naive uh segmentation I talked so far is

[34:34] that you have a long document, and then

[34:36] we segment them into different

[34:38] components, and then for each component,

[34:40] we are going to gather their embeddings,

[34:43] and that's going to be the unit we use

[34:44] for retrieval. So, late chunking was

[34:47] asking, "Well, if you do this

[34:49] segmentation, you really lose the idea

[34:53] of the entire document, right? Because

[34:55] if you take each of them separately, you

[34:57] only get to see the information there."

[35:00] How can we actually get to know some

[35:02] kind of document-level semantics?

[35:05] So, then you can do this a late

[35:07] chunking, where late chunking means that

[35:09] we do the segmentation later in the

[35:12] process.

[35:13] Uh we got a long document, and we are

[35:16] going to pass it to any embedding model.

[35:19] And then you we are you already got like

[35:21] rich embedding information. And then on

[35:23] top of that, we are going to do

[35:25] segmentation. In this way, the segments

[35:28] actually carry some document-level

[35:30] information.

[35:32] Uh so, this is why you get like a richer

[35:34] information from this kind of uh

[35:36] segmentation.

[35:38] Just to quickly show you, um

[35:41] I think uh if you look at the naive

[35:43] versus late chunking here, uh you

[35:45] definitely see much better performance

[35:47] from this kind of document-level uh

[35:50] enrichment.

[35:52] Uh one thing um that I'm going to point

[35:54] out is um if you notice this trend here,

[35:59] so the improvement from late chunking is

[36:02] actually the largest when your chunk

[36:04] size is small.

[36:07] This makes sense, right? Because uh if

[36:09] the the size the segment size is already

[36:11] very big, then this kind of late

[36:14] chunking is not going to add a lot of

[36:16] information. If the size is very small,

[36:18] then this kind of embedding from the

[36:20] document is going to bring in a lot a

[36:22] lot of value. So, this is something to

[36:25] kind of think about from a practical

[36:26] perspective.

[36:29] Okay, now let's go a step further.

[36:32] Uh

[36:32] this is actually a very interesting

[36:34] topic uh even just for a very specific

[36:36] component uh called uh indexing.

[36:39] Uh well, we all learned data structures,

[36:42] uh algorithms. So, so far it's like a

[36:44] very sequential. We just cut them into

[36:47] smaller pieces.

[36:48] What if we can actually make them more

[36:50] hierarchical, tree-based? We can

[36:53] leverage very nice properties of of

[36:56] structures.

[36:58] So, this is actually a research from

[37:00] Stanford called a PeaKtor here. Uh

[37:03] basically, what we are going to do is

[37:04] that for questions whose answer is kind

[37:08] of spread across the document, a single

[37:11] segment may not be very helpful. So, how

[37:15] about we actually take a hierarchical

[37:17] approach here?

[37:18] We can build a tree bottom-up. First, we

[37:21] will embed each segment, and then we can

[37:24] collapse them. We summarize them, and we

[37:28] can then just embed the summaries and

[37:30] repeat until we have kind of like a

[37:32] root, like a tree here.

[37:35] And then at the query time, we just

[37:37] retrieve across all levels, and a detail

[37:40] of question may match the leaf node, and

[37:43] then a higher-level semantical question

[37:46] will match a summary node

[37:49] summary node that's like one layer up.

[37:54] Um if you read a specific example here,

[37:56] let's see for Cinderella, we have two

[37:58] questions. What is the central theme of

[38:01] the story, and how did she find a happy

[38:03] ending?

[38:05] Okay. So, if you read this kind of like

[38:07] arrows here, DPR, you can see that it

[38:10] only retrieve those specific like a leaf

[38:12] node here.

[38:13] But then in the PeaKtor example, it

[38:16] actually the boxes we highlighted, it

[38:18] actually find those kind of higher-level

[38:21] box to represent the information.

[38:23] Especially for the second question, how

[38:25] did she find a happy ending? I think you

[38:27] need to figure out like who's she, what

[38:30] is a happy ending, etc. So, that

[38:32] requires multiple layer of semantic

[38:35] processing.

[38:38] If you follow this kind of data

[38:40] structure,

[38:41] we we not talk about sequence, we talk

[38:43] about tree.

[38:44] Let's go a step further uh, into graph.

[38:48] So, you can also think about how to uh,

[38:51] really make sure that

[38:53] um,

[38:53] we we really leverage this kind of

[38:55] high-level information since some

[38:57] questions are not about one specific

[39:00] paragraph or even not one document. They

[39:04] need to be synthesized across many

[39:06] documents.

[39:08] Uh, no specific chunk or segment will

[39:11] give you that answer. So, then what if

[39:13] we can actually build a knowledge graph

[39:15] first?

[39:16] Uh, at indexing time we just segment the

[39:19] documents, ask LLMs to get all the

[39:22] entities, and then the relationship

[39:23] between them.

[39:25] Uh, we can then connect them into a

[39:26] graph.

[39:27] >> [snorts]

[39:27] >> So, now you can actually do like graph

[39:29] clusterings, like different community

[39:31] detection algorithm here.

[39:33] At a query time,

[39:35] um, we do not search segments. We are

[39:38] going to ask each community, each

[39:41] cluster summary to answer the question,

[39:43] and then merge those partial answers

[39:45] into a global answer. So, this is

[39:48] actually how you could do graph rag.

[39:51] Um, to kind of summarize, uh, this is

[39:54] the last page here.

[39:56] In terms of graph rag, I think the

[39:59] reason why this is powerful is because

[40:01] you can really index across rich

[40:04] modalities. Not only text, image, uh,

[40:08] you can even apply that to um,

[40:10] like biology structures, uh, molecules,

[40:13] social network, citation network,

[40:15] knowledge graph. So, uh, this is why the

[40:19] design principle behind the rag can be

[40:21] really really generalizable.

[40:24] Okay, I think there was a question.

[40:26] Yeah.

[40:27] >> So, for something with these like more

[40:29] complex structures, where we're actually

[40:32] comparing against every chunk, is like

[40:34] is it does it get harder to answer some

[40:36] questions that are like really specific

[40:37] because it's not actually looking at the

[40:39] level that has actually encoded the

[40:41] information? Does that make sense?

[40:43] >> Yeah, so the question is about why we

[40:46] need this uh, very sophisticated like

[40:48] segmentation approach. Uh, the reason is

[40:51] that if you think about the very earlier

[40:53] kind of chunky segmentation, uh, they

[40:56] are very kind of localized. Uh, they do

[40:58] not take care of the broader document

[41:01] information. This is why we want a

[41:03] contextual retrieval. And then, uh,

[41:05] sometimes you may also need to know

[41:08] multiple, uh, segments in order to

[41:10] derive the answer. This is why we need

[41:12] to put them into a tree structure so

[41:15] that we can get a something higher

[41:16] level.

[41:17] Uh, graph means that maybe it's not even

[41:20] within the same document. You probably

[41:22] need like 10 documents to figure out how

[41:25] the public perceive a specific topic.

[41:28] For question like that, you want to

[41:30] really look over many different

[41:32] documents.

[41:33] It's more from a community perspective.

[41:35] This is why you want to actually maybe

[41:38] segments them based on some kind of

[41:40] themes, topics, and then do, uh, this

[41:43] kind of question answering with that.

[41:45] Um, so as we go more and more

[41:47] sophisticated, it's actually designed to

[41:50] answer like more higher level questions

[41:53] rather than exact answer match.

[41:55] Uh, however, you can imagine going back

[41:57] to some of the earlier question, uh,

[42:00] different the chunking algorithm also

[42:01] carry with cost. This is why, like

[42:05] today, if you think about the commercial

[42:08] or a lot of the large-scale, uh, QA

[42:10] systems, they still prefer some of the

[42:12] earlier technique that I mentioned since

[42:14] it's very fast. It covers majority of

[42:17] the questions we have.

[42:20] Yes.

[42:21] >> Given a query time, how do you choose

[42:23] which communities you need to look at

[42:25] for the question?

[42:26] Or are all of them queried

[42:28] simultaneously?

[42:29] >> Yeah.

[42:29] So, um, this is again, uh, think about

[42:32] it from a The question is how do we

[42:34] choose which community to focus?

[42:36] Um, again, this is going to be a design

[42:38] choice. Uh, you can define like a

[42:40] relevance score here. If my question is,

[42:43] uh, which sport should I look at this

[42:46] weekend? Uh, which game should I look

[42:47] at? And then you may want to fetch those

[42:50] clusters that are talk about sports,

[42:52] talk about games, etc. So, you can

[42:55] define some kind of relevancy

[42:58] estimation and use that. And then,

[43:00] instead of only look at the one cluster

[43:02] output, you can actually aggregate

[43:04] partial answers from multiple clusters

[43:06] to answer your question.

[43:09] >> actual retrieval

[43:11] uh you you need to use that LM to attend

[43:14] the conference. So, here how important

[43:16] is the quality of the LM? So, if you're

[43:18] using a very cheap LM, does that affect

[43:21] the quality a lot?

[43:23] >> Yeah. Um the question is is LM uh

[43:26] like is is the choice of LM sensitive to

[43:29] the setup here and how should we think

[43:31] about that? So, the LM definitely needs

[43:33] to be somewhat capable, but it does not

[43:36] need to be state-of-the-art. Uh you're

[43:38] going to do a parental analysis in terms

[43:41] of the accuracy of the retrieval, the

[43:43] quality of the retrieval, and then the

[43:45] cost of LMs or the speed of LMs, and

[43:48] then you make a design choice based on

[43:50] that. In general, the LM people use here

[43:53] are quite uh I would say small, capable

[43:56] uh rather than like a very large

[43:58] commercial API-based models.

[44:01] Yes.

[44:02] >> So,

[44:03] I'm wondering like is there like an

[44:06] office where it goes back to the

[44:08] original source and actually

[44:11] is that an action like during the whole

[44:13] processing, there might be errors the

[44:16] errors

[44:17] are

[44:18] magnified and also quality.

[44:21] Is there a way to reflect that

[44:23] and then actually is like that?

[44:25] >> Yeah, great question. So, the question

[44:27] is that if you think about the rag, the

[44:29] design pattern may suffer from compound

[44:32] errors where the error may cascade along

[44:35] the pipeline. And then, if we made a

[44:37] wrong, let's say retrieval in the first

[44:39] place, there's no way you are going to

[44:40] get a good answer in the end.

[44:42] So, we this is actually one of the

[44:45] limitation of the rag approach. As we

[44:48] move more towards a generic rag, we will

[44:50] add some additional components such as

[44:53] self-reflection or critique, etc. So,

[44:56] we'll add some additional components to

[44:58] make sure we do not suffer from that,

[45:01] but in practice, this is still a

[45:02] concern.

[45:04] Okay, I will continue. Um so, we we now

[45:07] finish um

[45:09] uh chunking, uh which is a very exciting

[45:11] topic, actually. Uh now, we are going to

[45:14] a little bit higher level to the vector

[45:16] search here.

[45:18] So, if you think about the top K

[45:19] selection for rag, uh you are provided

[45:22] with a query vector, and you want to get

[45:25] the top K

[45:26] >> [clears throat]

[45:26] >> um

[45:26] segments.

[45:28] Um you can definitely do a exact search.

[45:30] This is going to be a very brute force

[45:33] process, where if you have N documents

[45:36] and then D dimension, your complexity is

[45:39] like O N D here. N is in general like, I

[45:43] don't know, like millions of records, so

[45:45] it's going to be very, very expensive if

[45:47] you do exact search.

[45:50] Um again, like uh you can actually use

[45:52] approximate algorithm here. Um people

[45:55] use approximate nearest neighbor, like

[45:57] ANN here. You trade a little bit of

[46:00] recall with a lot of speed. So, we do

[46:02] not need to search everything. We only

[46:04] need to search for a small region.

[46:08] Um different techniques have been

[46:10] proposed, uh such as IVF here. You

[46:13] basically cluster the index, and you

[46:16] only do search probe in a nearest

[46:19] neighbor region.

[46:21] You can also do quantization here. Uh

[46:24] you can compress each vector into a

[46:27] quantized version. So, it's going to be

[46:29] a much shorter code. You reduce the

[46:31] dimension of D here.

[46:33] Uh one approach I'm going to share you

[46:35] here is called uh HNSW.

[46:39] Uh hierarchical navigable small world.

[46:42] This is actually one of the widely used

[46:44] approach. Uh I will share the high-level

[46:47] idea here, uh but I'm happy to talk

[46:48] about the details.

[46:50] So, what this does is that, since it's

[46:53] really hard to do exact search, what if

[46:56] we kind of arrange the information at

[46:59] the different layers?

[47:01] So, different layers, um first all

[47:04] vectors we have will be in layer zero.

[47:06] So, they are all the bottom.

[47:08] As you move a little bit higher level

[47:11] higher level, you have fewer and the

[47:13] fewer samples.

[47:15] So, when we do search, we actually

[47:16] search from the top here. And then you

[47:19] can greedy hope towards the query. Um if

[47:22] you cannot find the answer, let's see at

[47:24] the layer two, you go to layer one. If

[47:26] you cannot find the answer here, you go

[47:28] to layer zero. And at each layer, you

[47:30] are just doing like a nearest neighbor

[47:32] search. So, this kind of hierarchical

[47:34] representation enable us to do very

[47:37] fast. I think here like all n hops here.

[47:41] log n, sorry.

[47:44] This is the HNSW.

[47:46] If you are curious like, "Okay, how is

[47:48] this actually constructed?" Uh I

[47:50] recommend you uh read the algorithm

[47:53] yourself. It's actually a very

[47:54] interesting random uh algorithm here. Uh

[47:58] you basically insert a vector at each

[48:00] time. And then you pick its top layer at

[48:03] random.

[48:04] Uh most of node will stay at layer zero.

[48:07] And then few node will reach the top.

[48:09] And then you basically link it at each

[48:11] layer.

[48:12] Um the nearest neighbors and then the

[48:14] heuristic link across to another

[48:17] cluster. So, that the greedy walk across

[48:20] those different layers can happen. And

[48:22] then you do not trap a specific node in

[48:25] a specific layer. So, you can basically

[48:27] construct a layered representation. And

[48:29] then when you do the search, you go from

[48:31] the top layer to middle layer to the

[48:34] bottom layer.

[48:36] Okay. So, this actually concludes our

[48:38] indexing. Um this is again a very uh

[48:41] kind of like specific component behind

[48:44] the rack.

[48:45] Yeah. And then I'm now going to go

[48:47] towards our retrieval. This is actually

[48:50] uh

[48:51] a component that answers a lot of the

[48:53] questions about why we need a DPR, do we

[48:56] still need a BERT, what are some kind of

[48:58] other choices here?

[49:01] So, first, uh let's talk about different

[49:03] type of retrievers. I already mentioned

[49:06] those terms. You already see DPR. You

[49:09] can do sentence vectors.

[49:11] You can also do word overlap BM25.

[49:15] You can use neural systems. You can use

[49:17] L arms. Those are just like a different

[49:19] type of retrievers we can have.

[49:22] So, let's look at a BM25.

[49:26] This is again the most widely used

[49:28] approach. Very, very classic. It's from

[49:31] 1990s.

[49:33] And it's still the baseline that every

[49:35] retriever paper reports today.

[49:38] I'm going to show you the results. This

[49:40] is literally a TF-IDF-ish

[49:43] setup. So, nothing is very sophisticated

[49:47] here. We are just going to go through

[49:49] this uh

[49:50] one by one.

[49:51] So, if you read this kind of score, BM25

[49:54] score here,

[49:56] it's literally two components. You have

[49:58] IDF, you have the kind of like

[50:02] TF here. So, often a [snorts] specific

[50:05] word in the query QI

[50:09] occurs in the document. And then you do

[50:12] some kind of normalization here.

[50:14] And then IDF is going to look at how

[50:18] like NQI here refers to the docs that

[50:20] contain QI.

[50:22] So,

[50:23] basically, the second piece is just like

[50:25] a term frequency with some kind of like

[50:28] length normalization here.

[50:30] And then

[50:32] with those two terms, we just like get

[50:34] to the BM25.

[50:37] I'm not going to go deep into those

[50:39] different parameter choices here.

[50:41] There are different variants of this.

[50:44] The good thing about BM25 is that

[50:47] there's no training, no vector, and it's

[50:49] very hard to beat exact term

[50:52] representation.

[50:55] So,

[50:56] I want to provide you some kind of

[50:58] intuitions because if you look at this,

[51:01] Uh, definitely feels like, "Okay, this

[51:03] is so complicated. How did they come up

[51:05] with K1 here? What exactly is doing with

[51:08] this kind of IDF? So, instead of walk

[51:11] you through with the terms, let's look

[51:13] at some intuitions behind this.

[51:16] So, IDF, let's just take them as a

[51:18] whole.

[51:19] If you read the left side, so the x-axis

[51:23] is a document frequency.

[51:25] Uh, that is how often a term occurs in

[51:27] document. And then the y-axis, we plot

[51:30] the IDF score. So, as you can see, BM25

[51:35] uh, here, um, this

[51:37] this line.

[51:40] It definitely has two shapes. So, when

[51:44] it

[51:44] when it is like less than 50% of the

[51:47] document, the term has a positive value.

[51:50] When a term occurs more than half of the

[51:53] documents, it actually receive a

[51:54] negative value.

[51:56] Uh, so this is actually what we want. We

[51:58] want to find the sense that's very

[51:59] unique to the query. So, this is the

[52:02] intuition behind the IDF score here.

[52:05] Um, the term frequency, in the earlier

[52:07] thing, you see this kind of like big box

[52:10] here is refers to like term frequency.

[52:12] It has some kind of normalization with

[52:14] K1 here. So, let's just look at what a

[52:17] K1 is doing.

[52:18] If K1 is very small, like 0.5 here, so

[52:22] that's the bottom line, versus K1 is

[52:24] five, which is the top line.

[52:27] Um,

[52:28] this literally tells us about the term

[52:31] frequency saturation. Um, you can see

[52:33] that each term actually starts at one

[52:36] here for a single mention. And then a

[52:38] higher K1 will give more credits uh, for

[52:42] repeats before it flattens. Uh, small

[52:46] uh, K1 here is nearly like a binary. So,

[52:48] the word is there or it is not. So, if

[52:51] you look at this, it kind of converge

[52:53] very earlier. It basically quantify is

[52:55] the word there or is it not? So, IDF

[52:59] decides which words matters, and then

[53:02] the saturation actually stops any word

[53:04] from being dominating in the output.

[53:09] Okay, so this is just a very classic, as

[53:11] I mentioned, like a very fast approach

[53:13] to process information.

[53:16] Now, if we go to this kind of DPR stage,

[53:20] dense passage retrieval here.

[53:22] In the offline, what we do is that for

[53:24] different passages, we pass them through

[53:27] an encoder. This could have been BERT

[53:30] or Roberta or other type of architecture

[53:33] here. You gather different vectors. You

[53:35] store them into your vector index.

[53:39] During the online fashion, whenever we

[53:41] get a query, we pass it to a query

[53:43] encoder. And then we can do the dot

[53:46] product. And then you do the top key

[53:48] here. So this is a neural approach. And

[53:51] then

[53:52] one thing I do want to mention is that

[53:54] the passage encoder and the query

[53:56] encoder, they are two separate BERTs

[53:58] here.

[53:59] Um

[54:00] A quiz you need to answer yourself is

[54:02] which side is expensive.

[54:05] Is it this one or is this one? One's

[54:07] done offline, one's done online.

[54:11] Um one minor thing that I do want to

[54:13] mention is that

[54:15] if you want to go deep, you can also see

[54:17] how we train DPR here.

[54:20] Um so what do we do is that once you get

[54:22] the representation from the question

[54:25] coder, the passage encoder, we do a

[54:27] inner product similarity here. And then

[54:30] you can just pass them into a

[54:32] normalization here.

[54:34] Um so the loss function here is what we

[54:37] call a contrastive loss. That is the

[54:39] negative log soft max of the positive

[54:42] retrievals against the negatives. So

[54:45] that's referred as the P plus here

[54:48] versus P minus.

[54:51] So think about the idea. The idea is

[54:53] that we want to promote those correct

[54:56] search to be closer. And then we want to

[55:00] penalize those incorrect or less

[55:03] relevant search.

[55:05] Um so one of the key design question

[55:07] here is where do the negative come from?

[55:11] I think you can use the other passages

[55:13] in the same batch since you do batch

[55:15] processing.

[55:17] Uh, which This is what we call a

[55:18] in-batch negative. Or you can use BM25

[55:23] hard negatives. That is the passage that

[55:25] the match the questions words, but do

[55:28] not contain the answer. So, you give it

[55:30] a really hard negative here. And those

[55:33] hard negatives are what teach the model

[55:36] to go beyond just like word overlap.

[55:39] Um, so you can see that the right line

[55:41] here, uh, this shows how the gradient

[55:43] updates both encoders.

[55:46] So, this is the architecture behind the

[55:48] DPR.

[55:50] I'm going to show you more equations,

[55:52] but they literally means how we do the

[55:54] evaluation since um, some people may get

[55:57] a confused as we have so many many

[56:00] different metrics whenever it comes to

[56:03] rank.

[56:04] Uh, let's start with a very simple one,

[56:06] hit at K.

[56:08] Again, as the name mentions, it

[56:10] basically means that if I look at the

[56:12] top K positions, uh, is that

[56:15] content relevant or not. So, you

[56:18] basically use this kind of um, index

[56:21] function and then look at the whether

[56:23] uh, the passage is relevant or not and

[56:26] then you do a normalization. So, this is

[56:28] very straightforward, hit at a K K.

[56:32] Uh, field at a K. Again, same. Uh, you

[56:36] just look at is this relevant or is this

[56:38] not. This is the metric we mentioned

[56:41] earlier for contrast retrieval and it

[56:43] basically complements hit at a K here.

[56:48] Okay, [snorts] a much uh, more common

[56:51] metric, but look a little bit uh,

[56:54] uh, scary, but let's unpack them.

[56:57] Uh, so this is called a NC NDCG at K.

[57:00] And then in order to understand this,

[57:03] let's look at the DCG here.

[57:06] It basically means that for the for the

[57:08] current list, if I look at the top key

[57:11] passages, this is their relevance. And

[57:14] then you you basically like discount

[57:16] them by their rank position. So, you

[57:18] basically get like how relevant they are

[57:21] with regarding to their ranking. So,

[57:23] this give you a more accurate

[57:25] description of the relevance.

[57:28] Uh and then since you have ground truth,

[57:30] the IDCG here refers to if you look at

[57:33] your ground truth retrieval and then

[57:36] give them the relevant score and rank

[57:37] key what ideal situation. And then you

[57:40] do a normalization here to refer to the

[57:43] outcome.

[57:44] So, again, nothing is is like really

[57:47] new. We are just trying to walk through

[57:49] the the matrix here.

[57:52] Okay, I have two more metrics before we

[57:53] finish. So, uh the next one is called uh

[57:57] um

[57:58] MRR here. Uh this is also a widely

[58:01] used metric. So, you literally just

[58:03] going to look at the rank of the

[58:06] specific first relevant query and then

[58:09] where is the rank? And then you do the

[58:11] average across all queries.

[58:14] Uh recall the key is also intuitive.

[58:17] Like if you look at the top retrieved

[58:20] content,

[58:21] um

[58:22] did we find those in the top K? And then

[58:25] uh across all the relevant passage we

[58:28] have for that query. So, this is a lot

[58:30] of the metrics. Um you may encounter

[58:33] some of those in your implementation.

[58:36] With those contacts, now let's look at

[58:38] the results. So, DPR is also a very uh

[58:43] powerful technique. Uh when researchers

[58:46] compared with BM25, you can see that it

[58:49] actually outperforms

[58:51] uh four out of five data sets.

[58:54] Uh this is the match I think uh

[58:56] um

[58:58] Yes. So, here um the contrastive loss is

[59:01] actually trained with two parts. The

[59:03] in-batch negative as I mentioned as well

[59:06] as BM25 hard negatives. So, this is a

[59:09] trained DPR and you can see the results

[59:12] uh compared to BM25 and then the

[59:14] combination of both of them.

[59:18] Um so single here refers to training the

[59:21] DPR only use a individual data set and

[59:24] then multi means that you are going to

[59:26] combine different data sets to train the

[59:27] DPR.

[59:30] Um two more interesting things that I

[59:32] want to highlight. So on this figure you

[59:34] can see that with the top key accuracy

[59:38] how it kind of like evolve over

[59:40] different training size here. It turns

[59:43] out that only 1,000

[59:46] annotated pairs you can actually train

[59:49] DPR much better than BM25 here.

[59:53] And then again like more training

[59:55] examples help. So you see this kind of

[59:58] higher line here.

[60:01] Um with no actual pre-training DPR with

[60:05] the 1,000 or like 2,000 QA pairs

[60:08] actually beats like a RAM which is a

[60:10] earlier system from Google that it

[60:12] trains the entire pipeline end-to-end.

[60:15] So this is indeed a very very powerful

[60:18] technique.

[60:21] So last thing that I want to mention

[60:23] here related to this kind of retrieval.

[60:27] The two approach that I mentioned to you

[60:30] so far BM25 they cannot handle semantic

[60:34] paraphrase ish

[60:36] scenarios. And then DPR they will miss

[60:39] the exact match such as specific code,

[60:43] numbers, product IDs, etc.

[60:47] The reality is that we want to take the

[60:50] best of both world. So what if we can do

[60:53] a hybrid search? We can run both

[60:55] retrievers and then fuse them

[60:58] um

[60:59] through their rank list.

[61:01] And then one technique that you will

[61:03] come across is called a reciprocal rank

[61:07] fusion.

[61:08] It give you approach to merge positions

[61:10] instead of raw scores because the score

[61:13] of ranking actually cannot be combined

[61:16] easily. So, we are going to think about

[61:18] how to merge positions here.

[61:21] Um so,

[61:23] again, this approach no per corpus

[61:25] tuning and it works with any number of

[61:28] retrievers.

[61:30] Uh I'll stop here in case there are any

[61:32] questions.

[61:34] >> Um in the slide you just showed where

[61:35] you're doing the dot product between the

[61:37] query vector and the position vectors to

[61:39] retrieve the top K

[61:41] passages,

[61:42] what is the what is the result like? Is

[61:44] it the

[61:44] index of those passages

[61:47] >> Yeah, so purely you look at the index of

[61:50] those passages, but like use the index

[61:52] to gather their actual embeddings,

[61:54] right? A lot of the embeddings for each

[61:56] segment's passage already processed

[61:59] offline. So, you use the index to get

[62:01] their embeddings and then do the inner

[62:03] product there.

[62:08] Any other questions here?

[62:09] I think those are a lot of the metrics,

[62:12] but they literally are more from an

[62:14] illustrative perspective. So, you can

[62:16] use them to understand tables and

[62:18] results.

[62:20] Okay, uh if there is no more question,

[62:23] I'm going to go a little bit deeper here

[62:25] in terms of

[62:26] encode encoder.

[62:28] Uh so, this lecture literally contains

[62:31] everything you need to know about the

[62:32] retrieval. Uh so, it really contains

[62:35] like many many different components.

[62:37] Um so,

[62:39] I would really divide a lot of the um

[62:42] representation process into two parts.

[62:45] First, you can have what do we call a

[62:46] bi-encoder. Uh your query and passage,

[62:50] they are encoded separately. Um you can

[62:53] also think about what if we could have a

[62:56] cross-encoder.

[62:57] That is, instead of these like two

[62:59] separate encoders for my query, for my

[63:02] passage, I'm going to do this

[63:03] cross-encoder. The query and passage go

[63:07] through the model together and we do

[63:09] full attention across both and then we

[63:11] use the results to do some further

[63:13] processing.

[63:16] Similarly to late trunky, we also have

[63:19] late interaction here. And this page is

[63:22] actually very important, so I want to

[63:24] decompose it a little bit.

[63:26] So, the very left side, this is you have

[63:29] a query, you have a document, you do

[63:31] information processing of them

[63:33] separately, and then you look at their

[63:35] inner product.

[63:38] Now, think about what may go wrong in

[63:39] the process. Second is that I'm going to

[63:42] maintain a big matrix here, query and

[63:45] document, and then um I process

[63:48] everything together.

[63:50] Third is that what if I just concatenate

[63:53] the query and document together,

[63:55] pass it through a transformer or any

[63:57] network, and do it together.

[64:00] The last one is I pass the query through

[64:03] a network, I pass the document at

[64:06] through a network, and then I do some

[64:08] kind of inner uh like product there in

[64:12] interesting way, and then I got an

[64:14] output. So, now think about what are the

[64:17] pros and the cons of each setup.

[64:21] Anyone want to give it a try?

[64:23] Yes.

[64:27] >> It's more faster.

[64:29] It's the most It will lost resource. And

[64:32] the

[64:33] uh but it doesn't care about the

[64:34] position.

[64:36] Uh

[64:36] the sequence that's why

[64:38] the second one is going to be uh more uh

[64:42] it's more complex, it take more time.

[64:45] For each

[64:46] query

[64:47] it it's more difficult

[64:49] for

[64:50] attention to care about the positions

[64:53] uh and the selection of the positions.

[64:56] >> Yeah, that that's a that's a beautiful

[64:57] answer. So, just to repeat, uh so, the

[65:00] left side is actually very fast.

[65:02] Actually, the most complicated one is

[65:05] probably B and the C here, especially

[65:07] for C, since you need to put the

[65:08] document and the query together in the

[65:10] same matrix. And then D is actually

[65:13] somewhere in the middle. One thing you

[65:16] do need to remember is that documents,

[65:18] we have a lot of documents. So,

[65:20] documents are representations in

[65:22] general. If we can process them offline,

[65:24] we prefer that. So, you also need to

[65:26] think about decoupling of them. So, the

[65:29] fashion we have in C, you really cannot

[65:32] like pre-compute many of them in

[65:34] advance, right? Versus D and A, you can

[65:37] actually easily just like get this blue

[65:40] part pre-processed,

[65:42] and then later you just do a query at

[65:45] inference time, and then their

[65:47] product calculation there. So, this is

[65:49] actually the key difference here.

[65:52] Uh the later interaction I'm going to

[65:54] mention for this Colbert here refers to

[65:57] that we're going to keep one vector per

[66:00] token, and we'll encode the query and

[66:02] the passage still um

[66:04] independently. But then we do an

[66:06] interaction only at the scoring time.

[66:09] And then this is actually what we call

[66:12] max sim here. For each token in the

[66:15] query, we're going to find the token in

[66:18] the document that match this token the

[66:21] most, and then we take that score, and

[66:24] we add it across all the query terms.

[66:27] So, this is actually the score we used

[66:29] here.

[66:30] Uh

[66:31] just to zoom in a little bit. So, you

[66:34] have both the query encoder, document

[66:37] encoder. The document encoder is

[66:39] something we can process offline. And

[66:41] then each time we're going to take each

[66:43] specific token, find the which token

[66:46] match them first best from the document

[66:49] encoder, and then do this for every

[66:51] single token there in the query.

[66:56] Um so, again, this is

[66:58] a lot of content to remember,

[67:01] um but the high-level idea is that

[67:04] Colbert actually works pretty well.

[67:06] Uh if you can see that compared to a lot

[67:09] of the approach we mentioned earlier,

[67:12] uh it definitely give you much higher

[67:14] number compared to BM25 and a lot of the

[67:17] baselines.

[67:19] Um on this page you can also see latency

[67:21] get a mention here, and the different

[67:24] type of record.

[67:26] Um to summarize this part, um so

[67:30] there are different choices. Uh when you

[67:33] build a rag, especially if your

[67:34] application domain is very diverse, you

[67:37] work with graph data, you work with

[67:39] image data, you work with

[67:41] different documents. A document on

[67:44] social media is going to be very

[67:46] different than a financial document that

[67:48] contains a lot of specific entities.

[67:51] Um so if you look at this, uh we need to

[67:53] think about their pre- pre-compute

[67:56] whether we can do them offline.

[67:58] The query latency.

[67:59] What a situation is best for which

[68:02] specific retriever? And then where do

[68:04] they fail or break? And then this table

[68:08] actually give you some summarizations uh

[68:10] based on the empirical results in the

[68:13] two papers we just mentioned.

[68:16] Okay, any quick questions here?

[68:22] Um if not, we're going to finish um

[68:24] with the agentic rag.

[68:27] Um so so far, if you look at the rag

[68:30] that I've mentioned, it's a lot of kind

[68:32] of probability uh models, encoding,

[68:36] index, etc. But we have AI and agents

[68:41] right now. So

[68:42] um everything so far feels like they are

[68:45] not really have the initiative to do

[68:47] something. Uh because the system cannot

[68:50] decide whether to retrieve, what to ask,

[68:54] and when to stop.

[68:57] Um what if we could actually make a

[68:59] retrieval an action that the agent

[69:01] takes? So there will be three decisions

[69:03] they need to make. Uh retrieve or answer

[69:06] directly. Do I need actual information

[69:08] or not?

[69:09] What a query to issue if I need to

[69:11] search additional information? Whether

[69:13] the result is good enough that I should

[69:15] stop. So this is more from a agentic

[69:18] perspective to leverage rag.

[69:21] And I'll share some of the widely used

[69:24] uh agentic rag system here.

[69:26] Uh the first one is called a self-rag.

[69:29] So, how about we teach one model to

[69:31] retrieve, critique, and then generate

[69:34] here? Uh you can just give them some

[69:37] special reflection tokens along with the

[69:39] text.

[69:40] So, if you look at this specific

[69:41] example,

[69:43] um how did the US states get their

[69:45] names?

[69:46] Uh step one, we're going to retrieve on

[69:48] demand. The model starts writing and um

[69:52] emits uh

[69:54] retrieval token here when it decides

[69:56] that it needs evidence to answer your

[69:58] question.

[70:00] Um step two here,

[70:02] it actually generates a segment for each

[70:05] retrieved passage in parallel.

[70:08] In step three,

[70:09] it actually critique each response or

[70:12] each segment. And is the passage

[70:15] relevant? Is the segment supported? You

[70:17] ask a lot of question here.

[70:19] It then rank the segments and keeps the

[70:22] best.

[70:23] So, decisions um

[70:25] one and the three are actually trained

[70:27] here into a generator itself.

[70:30] Um the cost is the training pipeline

[70:32] with the critique labeled data. So,

[70:34] these are the parts we need to have uh

[70:36] it ready.

[70:38] So, through this process, you basically

[70:40] combine um this kind of rag design

[70:42] principle with a lot of the

[70:44] self-critique, self-reflect

[70:47] uh natures of agentic systems.

[70:51] Um C-rag actually uh push it further or

[70:54] take a very different approach. How

[70:56] about we do not touch the generator, and

[71:00] we put a evaluator between the retriever

[71:02] and the generator?

[71:04] This evaluator is going to grade the

[71:06] retrieved documents and uh give us a

[71:09] score, a confidence score, uh which map

[71:12] to an action. Correct? If the score says

[71:15] this is correct, then we'll keep them.

[71:17] Um we can still refine them, split them

[71:19] into different parts.

[71:21] Um if it tells us that this is

[71:23] incorrect, then we need to throw them

[71:25] away, rewrite the query, and the search

[71:28] the web again. So, there is more like a

[71:30] judge there.

[71:32] If the query is very ambiguous here,

[71:35] then you need to do both.

[71:37] So, this kind of design is really like a

[71:39] plug-play on any kind of rack stack we

[71:42] can we can we can implement. It answers

[71:46] like a decision um tree with a separate

[71:49] very lightweight model, and it does not

[71:52] need to touch the generator at all.

[71:56] So, with more and more like kind of

[71:59] reasoning capabilities, uh people are

[72:01] also looking at it. Can we use like R1

[72:04] uh ish thinking to improve the the

[72:07] search process?

[72:08] So, this is a recent uh work called a

[72:10] search R1. Instead of like hand

[72:12] designing the loop, how about we learned

[72:15] with RL?

[72:17] Uh so, this is actually a real

[72:19] trajectory from a search process. The

[72:21] question is uh who is who is older here?

[72:25] And the model thinks, search, read what

[72:28] comes back, and then um think again,

[72:31] search again, and eventually answer your

[72:33] question. It actually searched three

[72:35] times and refined the query each time.

[72:39] And then um no one needs to write this

[72:41] plan on how the agent should work. So,

[72:44] remember the difference between workflow

[72:46] and agents here.

[72:47] Um so, one thing to point out here is

[72:50] that

[72:51] um

[72:52] a lot of the um the passage we are going

[72:54] to retrieve may get truncated here. So,

[72:57] the trace that uh you see here does not

[72:59] actually reflect the the detailed

[73:02] process.

[73:05] So, how do we train it? Um we are not

[73:07] going to go deep into PPO and the uh

[73:09] GRPO here. We we'll have some lectures

[73:12] later this uh course. But, I only want

[73:15] you to look at the architecture and uh

[73:17] pay attention to the search module.

[73:20] So, the entire process here is very

[73:22] similar to a classic PPO or GRPO.

[73:26] Instead, we only add those two

[73:28] additional components here. So, whenever

[73:30] you are going to uh get a policy, we

[73:34] will do search first. So, that's the

[73:36] only component we added there. Nothing

[73:39] else here. So, basically during a roll

[73:41] out, the policy generates text and every

[73:44] time it will emit a search query and

[73:48] that hit the search engine and then the

[73:49] results come back into the context as

[73:52] some information tokens. The reward is

[73:55] going to be very classic as other type

[73:57] of reward is only the outcome.

[74:00] Is the final answer correct or not?

[74:03] So, this is how you could potentially do

[74:05] it with search R1.

[74:09] The process actually works pretty well.

[74:12] Researchers show that compared to R1 SFT

[74:16] rag, search O1, search R1 actually have

[74:20] much better performance in the process.

[74:24] So, this is actually what do we have for

[74:26] the agentic rag. So, rag as a design

[74:29] principle, you can actually use it in

[74:31] many many settings. This is why when

[74:34] agentic systems come out, we can still

[74:37] use similar principle here.

[74:40] The last two minutes, I'm going to share

[74:42] you some kind of figure mode here.

[74:45] This actually goes back to some of the

[74:47] question asked earlier. Rag is powerful.

[74:51] Some people would see that a rag is out

[74:53] of date today.

[74:54] Others would see that it's really hard

[74:56] to anticipate what may go wrong with

[74:58] rag. So, here we break them into three

[75:02] parts. The retrieval part, how rag would

[75:04] have failed.

[75:05] You can imagine maybe it didn't catch

[75:08] the right evidence. Maybe the embedding,

[75:12] the offline documents we have are just

[75:14] so out of date.

[75:15] Maybe the search actually look at some

[75:19] content which we should not look at. So,

[75:22] all of those questions may happen at the

[75:25] retrieval side.

[75:26] From a reader side, there may be like

[75:29] lost in the middle.

[75:31] Models may get distracted. Evidence we

[75:34] have may conflict with each other. That

[75:36] is, when Ragel go outside to fetch

[75:39] evidence, they actually got two

[75:41] evidence. They do not agree with each

[75:43] other. So, how should we think about

[75:45] that?

[75:46] From a loop like retriever generator

[75:49] perspective, there may be compound

[75:51] errors.

[75:53] Um, that is something

[75:55] some mistake happened earlier may affect

[75:58] later decisions.

[76:00] Um, there may even be prompt injections

[76:03] in the search process. What if bad

[76:06] actors actually added something to your

[76:08] search the documents and then really

[76:10] attack your entire pipeline. So, those

[76:13] are all the issues um, we can or we are

[76:16] going to mention about Ragel later. Uh,

[76:19] with that, this is all what we are going

[76:21] to cover for today's class. Thank you

[76:22] all and happy to take a more questions.
