# Lecture 3 recording

[Course index](../../README.md) · [Original source](https://www.youtube.com/watch?v=AiwCCvFW1uE&list=PLSN0qpDfUvTM&index=3) · [Raw file](../../raw/videos/AiwCCvFW1uE.json)

Retrieved: 2026-11-13T16:48:25.140161+00:00

[00:07] Okay. Uh hello everyone. Can you hear me

[00:09] in the back?

[00:11] All good. Okay.

[00:15] So, uh well, welcome back everyone.

[00:20] Am I uh echoing? All good. Okay. So, um,

[00:24] today I'd like to talk about context

[00:26] management for long context agents. And

[00:30] I at first thought about titling this as

[00:33] like context management for long context

[00:35] LLMs because most of the stuff I'm going

[00:37] to be talking about today is kind of

[00:38] more general LLM stuff, but long context

[00:42] is super super important for when we're

[00:44] working on agents and it's not

[00:45] necessarily covered uh, very well in all

[00:47] of the LLM prerequisite classes. So, I'm

[00:49] going to cover it in a fair amount of

[00:51] detail today. I'm also going to try to

[00:53] go through kind of the long context

[00:55] architectures that are used in many of

[00:58] the kind of state-of-the-art open uh

[01:00] models so you can kind of see the best

[01:03] practices that everybody is using in

[01:05] order to handle a very long context.

[01:10] So first I'd like to talk a little bit

[01:12] about um how long an agent context can

[01:16] grow.

[01:17] So basically the input is quadratic uh

[01:22] from the uh or the number of token

[01:26] accesses that you do is quadratic uh

[01:29] based on the linear history growth. So

[01:31] um if each call uh you make for an agent

[01:35] takes about you know five tokens and

[01:36] let's say you start out with a an

[01:38] initial system prompt of one token uh

[01:40] you'll get six tokens in the first call

[01:42] 11 16 uh 21 and 26. you know, this will

[01:47] increase and increase and increase. Um,

[01:50] and so by the time you have gotten to

[01:53] the end, you will, if you do things

[01:56] completely naively, you will have had to

[01:59] process ADK tokens uh for these five

[02:02] calls. And you know, this can continue

[02:06] for a very long time. I I don't know the

[02:08] longest anybody has used a single coding

[02:10] agent session or something like that,

[02:11] but I've certainly done them for like

[02:13] multiple days uh where I've been working

[02:15] with it for almost the entire day. So

[02:17] you could imagine this could get uh very

[02:19] very large. Um the actual computational

[02:22] complexity of this is uh is actually

[02:27] even larger than this. Um

[02:30] well no sorry. So yeah the the

[02:33] computational complexity is is quadratic

[02:35] here.

[02:37] So why do agent prompts get so long uh

[02:40] so quickly? I did a little bit of data

[02:43] analysis on uh the composition of

[02:47] prompts that I used in um uh 1,500

[02:52] sessions from our uh coding agent

[02:54] openhands. And

[02:57] each each session was relatively short.

[03:00] These are not like the long multi-day

[03:01] sessions that you do. This is more like

[03:03] solving a single task. But uh each one

[03:06] used about 78,000 tokens on average. Um

[03:10] 23% of this was a system prompt in all

[03:12] of the tool descriptions. Uh this is

[03:14] relatively large for a coding agent. I

[03:16] think our system prompt is somewhere on

[03:18] the order of like 15,000 to 18,000

[03:21] tokens because we're very opinionated.

[03:23] Uh the open ants agent is very

[03:25] opinionated about how people uh do work.

[03:27] Um these tend to vary from like 8,000 to

[03:30] uh 8,000 to 20,000 tokens depending on

[03:33] you know how many tools you uh you pull

[03:35] in and stuff like this. Um separately

[03:38] from this uh 9% were user messages. So

[03:41] this is the user either saying the

[03:42] initial task or following up with uh

[03:45] additional information after that. 9%

[03:48] were reasoning traces um and you know

[03:51] where the model is thinking through

[03:53] things. 2% were model replies. Sorry,

[03:56] this isn't showing on the slide, but 2%

[03:58] were um the model replying directly to

[04:00] the user. So, it's spending about um

[04:03] five times as many tokens freezing as it

[04:05] is spending communicating uh with text

[04:07] to the user. And 20% were tool calls. Uh

[04:10] so, you know, uh you know, writing code,

[04:14] uh reading code, that sort of thing. And

[04:16] 37% were tool results. So, this is uh

[04:19] you know, getting the result of, you

[04:21] know, reading a file or something like

[04:22] this.

[04:23] So you know each step can uh will

[04:27] consist of all of these and that tends

[04:29] to add up uh very quickly.

[04:34] So when you're handling this very long

[04:36] context uh there's two big challenges

[04:38] here. Uh the first one is capacity and

[04:42] so whether your model is able to handle

[04:44] this large amount of uh evidence in the

[04:46] first place and this is a challenge uh

[04:49] because as I'll talk about in a little

[04:50] bit training models to handle very long

[04:52] context is hard

[04:54] um and so in order to manage this you

[04:57] need uh things like architecture

[04:58] position encoding training data uh and

[05:02] uh you also need to be able to evaluate

[05:03] whether you're doing a good job of this.

[05:05] And then the second thing is efficiency

[05:08] uh and whether the system can afford to

[05:10] serve it. And there's a bunch of

[05:12] techniques to do that as well. And I I

[05:16] think some people might be taking this

[05:18] for granted if you're just using, you

[05:19] know, cloud code or codeex or something

[05:20] like this, but they're doing some pretty

[05:23] monumental feats of engineering to take

[05:26] a, you know, multi- trillion parameter

[05:29] model and serve it within seconds uh to

[05:34] uh over and over and over again for mil

[05:36] I don't know codeex has 25 million

[05:38] users. So you can imagine uh 25 million

[05:41] daily users hitting it every few seconds

[05:43] for this huge model. Uh if you want to

[05:46] you can calculate in your head how many

[05:48] flops per uh per second that might be.

[05:51] It's a lot of flops.

[05:55] Cool. Um so any questions or things?

[05:59] Probably pretty straightforward I guess.

[06:01] Okay. So uh let's go into inference. And

[06:06] so in order to make this happen uh the

[06:11] you basically need to be able to um

[06:15] calculate uh prefill and decoding. So uh

[06:19] calculate your inputs and your outputs

[06:21] at each step. And this uh you know I'm

[06:26] sure everybody has done in your previous

[06:28] classes uh for generating from uh you

[06:31] know a language model. some things you

[06:33] may or may not have thought about in

[06:34] your previous classes. If you took how

[06:36] many people took like uh language model

[06:39] systems or deep learning systems or

[06:41] something like that actually more than I

[06:43] thought. So if you took the systems

[06:44] course you you probably handled this. Um

[06:47] but other things you need to think about

[06:48] are how do you schedule uh multiple

[06:51] concurrent queries? Um and also how do

[06:53] you save the results in the KV cache uh

[06:56] so you can reuse them and not have to

[06:59] reuse them over and over again. uh not

[07:01] have to calculate over and over again.

[07:05] So going into a bit more detail here, um

[07:08] we have a few phrase uh phases in

[07:11] inference. The first one is called

[07:12] prefill. Um you could also call it

[07:14] encoding. Um but I think pre prefill is

[07:17] kind of the like preferred term of art

[07:20] nowadays. And so you take in all of your

[07:24] input tokens uh that you don't need to

[07:26] generate and uh you generate the key and

[07:29] value pairs uh from each of them. And

[07:33] then uh when you're decoding you

[07:35] basically uh take the prompt uh and key

[07:38] value pairs um generate an output and

[07:41] append uh the key value pair that you

[07:43] get from the output. So um you do this

[07:46] kind of incrementally whereas this can

[07:48] be done in a batched sequence.

[07:53] And so uh when we think about this as a

[07:55] serving system, there's a bunch of ways

[07:57] we quantify how good a serving system

[08:01] is. Uh the first one is time to first

[08:04] token. So this is how long you need to

[08:07] start um you need to wait between when

[08:10] you start uh

[08:13] entering a query and when you start

[08:15] seeing the first output. And so like I'm

[08:17] sure everybody you know who uses chat

[08:20] GPT or something like that uh you put in

[08:22] a long output you notice it takes longer

[08:24] to start getting a response than if you

[08:25] put in sorry put in a long input you see

[08:28] it takes longer to start getting a

[08:30] response than if you put in a short

[08:31] input and that's like your TTFT is

[08:33] higher. Uh then uh your time per output

[08:37] token is the uh time like the amount of

[08:41] time it takes uh between generating each

[08:43] token. And if you go to a website like

[08:47] open router

[08:51] um

[08:52] t typically uh here this will be your

[08:56] time per output token there I am pretty

[09:00] sure they're not counting prefill here

[09:02] and it's just like the time between uh

[09:04] each of the tokens that might be a

[09:06] little bit small with the black

[09:07] background but you can see that um for

[09:09] GLM 5.2 to uh you have like 63, 48, uh

[09:14] 24, uh that sort of thing. And you know,

[09:17] some providers are drastically better

[09:19] than others. Like this provider,

[09:22] not to pick on Mistl, but they're

[09:24] getting, you know, three three tokens

[09:26] per second and then these other ones

[09:29] like Parasel and Coreweave are getting,

[09:31] you know, hundreds of tokens per second.

[09:32] So um so basically uh you know this

[09:38] makes a huge difference in your

[09:40] experience using um uh using agents. Uh

[09:44] one other interesting thing is um

[09:47] there's different ways people can use

[09:49] agents. And so in some cases you might

[09:52] really hear about this. So like let's

[09:54] say you're working together um with a an

[09:58] agent on a interactive task in your

[10:01] favorite coding CLI. you may really

[10:02] really care about, you know, TTFT and

[10:04] Tapot. Um, if you're running an agent in

[10:08] the background to do some background

[10:10] tasks that run overnight, you might not

[10:12] care at all. Um, and there's trade-offs

[10:15] between them, between like throughput

[10:17] and cost and how fast uh you can get the

[10:20] the tokens. And like I you know also um

[10:24] serve coding agents uh with my company

[10:27] and when I talk to providers they'll

[10:29] often often ask which do you care about

[10:31] more so we can optimize the system uh

[10:33] for the one you care about more and so

[10:35] um there's uh there's ways you can do

[10:37] that and I'll I'll talk about those too.

[10:46] Cool.

[10:48] Um yeah so sorry just to finish the

[10:50] slide. So throughput is um the completed

[10:53] tokens or requests divided by the wall

[10:54] clock time. So this is kind of seen

[10:56] usually on a more holistic level over

[10:58] the whole system. And then uh the cost

[11:01] is you know how much it costs.

[11:04] So as a refresher um I I hopefully

[11:08] everybody should know this already. Um

[11:10] but you have uh the

[11:14] uh query key and value calculation in uh

[11:18] typical attention and this is uh so you

[11:22] have this here and then you take the

[11:24] softmax um divide it by this. You might

[11:26] have some sort of uh you know positional

[11:29] uh bias and then you calculate your

[11:31] output and typical full attention uh

[11:35] looks uh like this. you mask all the

[11:37] previous tokens and and or you consider

[11:40] all the current tokens and you mask all

[11:41] the um the future tokens.

[11:44] Um so this is of course very expensive

[11:48] because it's quadratic in the sequence

[11:50] length. Uh and so a lot of the stuff I'm

[11:53] going to be talking about today is about

[11:54] how to fix that.

[11:56] Um so this is on the efficiency side and

[12:00] then on the effectiveness side just

[12:02] because you have a model or just because

[12:05] you have a serving system that can take

[12:06] in you know a million tokens doesn't

[12:09] necessarily mean that you can use that a

[12:12] million tokens effectively and

[12:15] um this is a very like old school

[12:19] example of this I guess this is a needle

[12:21] in the haststack evaluation how many

[12:23] people have seen this figure for

[12:25] maybe some but not not that many. Okay,

[12:28] so to explain what this looks like,

[12:30] basically what this is saying is um it's

[12:34] a very weird evaluation. Basically, they

[12:36] um they took a whole bunch of Paul

[12:38] Graham essays uh by the like famous

[12:40] entrepreneur and head of Y Combinator

[12:42] Paul Graham and they stuck in uh

[12:45] something about like the best place in

[12:46] San Francisco to eat a sandwich is

[12:48] something or other and then they ask a

[12:50] question where's the best place in San

[12:52] Francisco to eat a sandwich and then the

[12:54] language model has to answer that

[12:55] correctly. um and they made the context

[12:58] longer and longer and longer and then

[13:00] they evaluate uh models with the longer

[13:03] context and eventually the weaker models

[13:06] start getting worse at these very very

[13:08] long contexts and there's a bunch of

[13:10] examples of things like this. Um ruler

[13:13] and helmet are kind of the the common

[13:15] benchmarks that people use here. Um but

[13:18] basically uh the long the summary is

[13:21] that if you have very long context your

[13:24] models might start getting worse at

[13:25] processing them.

[13:28] So has anybody noticed this when you've

[13:29] used a coding agent for a long time like

[13:31] are there common

[13:34] or used any agent for a long time are

[13:36] there common like failure cases that you

[13:38] see?

[13:40] What what kind of things what kind of

[13:42] things have bothered you?

[13:45] Anybody?

[13:48] >> Yeah.

[13:49] >> Forget the previous context.

[13:51] >> Yeah. Forgets the previous context. Did

[13:53] that cause any like problems for you?

[13:58] >> Yeah.

[14:06] with me telling it not to do something

[14:08] in the middle of the conversation and

[14:09] then it goes and does it. Um there there

[14:13] was a really bad example uh where I

[14:16] think actually Daniel talked about it

[14:17] here where the person had said do not

[14:19] delete this and then it went and deleted

[14:21] it anyway because it had forgotten the

[14:22] context. So yeah, this can be a really

[14:25] big problem in agentic settings because

[14:28] you know the user is giving these

[14:30] incremental instructions. So

[14:33] so I'm going to be talking about several

[14:35] different things. I'm going to be

[14:36] talking about architecture. I'm going to

[14:37] be talking about training inference and

[14:40] compaction. So going first into

[14:43] architecture. Um this is both about

[14:46] efficiency and accuracy.

[14:49] And so as I mentioned standard attention

[14:51] is global. So it makes pairwise

[14:53] comparisons across uh all of the tokens

[14:57] here. And um the problem with this is uh

[15:02] like this is quadratic obviously. And

[15:07] does anyone know the like standard

[15:09] length of the of models nowadays of

[15:13] these uh of like state-of-the-art

[15:15] language models?

[15:17] >> 256 to a million.

[15:19] >> 256 to a million. Yeah. And I I'd say

[15:21] most people are aiming for a million now

[15:23] because they don't want to be the, you

[15:24] know, the model that has 256 when

[15:27] everyone else has a million. So very

[15:29] quick math in your head, how many

[15:30] pairwise comparisons is that?

[15:34] >> 10 12

[15:36] >> 10 10^ the 12 or in English.

[15:38] >> A trillion. Yeah, that's a trillion.

[15:41] That's a trillion comparisons every

[15:43] time. uh like when you're uh generating

[15:45] a sequence of a million long and each

[15:49] comparison uh requires you to multiply

[15:53] large vectors by each other over and

[15:55] over and over again. So you're starting

[15:56] to get up into the you know 10 to the

[16:01] I guess it'd probably be 10 to the 20ish

[16:06] uh which is a lot that that's a lot of

[16:08] compute um for a single sequence.

[16:12] So um there there's ways that people

[16:16] solve this and basically almost all of

[16:19] them fall into the category of taking

[16:20] this quadratic computation and putting

[16:23] some sort of constant limit on the

[16:24] number of comparisons that are made uh

[16:27] at each time step. And that brings your

[16:30] uh n squared down to owl where I I wrote

[16:34] w for window but it doesn't necessarily

[16:36] need to be a window. It just needs to be

[16:38] the cap on the number of comparisons

[16:39] that you're making.

[16:43] Um so there's the idea of local models

[16:47] and global models. And so local models

[16:49] are are basically models where this cap

[16:51] on computation happens within a local

[16:54] window. And then global models you have

[16:58] a cap on you might or might not have a

[17:00] cap on computation but that cap on

[17:01] computation is not localized. So you can

[17:03] pass information uh throughout the

[17:05] entire sequence. And the I'd say almost

[17:09] all of the models uh that exist nowadays

[17:12] or are widely popular nowadays are some

[17:14] variety of hybrid model where they have

[17:18] many local computations and then one

[17:20] global computation then many local

[17:21] computations one global computation

[17:25] and specifically I'm going to talk about

[17:27] six uh models that we have here. So uh

[17:31] the most recent Quen model uh has uh

[17:34] local computation of uh gated delta net.

[17:37] I'll explain all of these uh or most of

[17:39] these in a bit. And then um sparse

[17:42] retrieval uh for the global computation

[17:44] and the ratio is 3:1.

[17:46] Uh GLM 5.3 is uh also a variety of delta

[17:51] um and sparse attention uh with 3:1.

[17:56] Um

[17:58] uh Kim K3 is uh a variety of Delta and

[18:03] um this is a dense uh dense attention

[18:07] 3:1.

[18:08] Uh Neimotron is Mamba uh which is uh

[18:12] kind of like recurrent style model

[18:15] and uh dense attention 4:1.

[18:19] um to uh window uh sliding window

[18:22] attention uh dense attention 5 to one

[18:26] and deepseek's a little bit different.

[18:28] It kind of has uh window windowed

[18:31] attention but then some uh sparsity uh

[18:34] sparse stuff with interle branches. So

[18:37] um basically the the standard way of

[18:40] doing things is hybrid model uh with

[18:43] some sort of local thing and uh either

[18:45] sparse or dense uh global attention.

[18:50] So I'm I'm going to be talking about

[18:51] this. I'm not going to go into like a

[18:53] ton of details for all of them, but uh

[18:55] it should be enough that you could be

[18:56] able to look them up later.

[19:00] So the first one is uh sliding window

[19:02] attention. And this is maybe the the

[19:05] simplest conceptually. And what you do

[19:08] is you take chunks or uh you take chunks

[19:12] of the output and basically you're able

[19:15] to attend to your current chunk and um

[19:19] all of the previous chunks and uh

[19:24] or not all of the previous chunks, a

[19:25] fixed number of previous chunks. So if

[19:27] this is your current chunk, um it might

[19:30] be a chunk of like 512 tokens or

[19:32] something like this. You would have an

[19:34] additional 512 and 512 tokens in the

[19:36] previous chunks and you would attend to

[19:38] those. Um so pretty simple, no changes

[19:42] to attention, but you have something

[19:44] like this. But the nice thing about this

[19:46] is on the first layer you're passing

[19:49] information from the previous one or two

[19:51] chunks, but on the next layer the uh

[19:54] previous chunks also have information

[19:55] from their previous chunks. And so you

[19:57] kind of get this gradually expanding

[19:59] window. Um

[20:02] so uh this uh this is pretty widely

[20:05] used.

[20:08] Um but the more popular way of doing

[20:11] things nowadays is using some variety of

[20:14] linear attention.

[20:16] And so the way uh linear attention works

[20:19] is basically we take our uh standard

[20:23] attention and standard attention has

[20:25] this um softmax operation included in

[20:28] it. And this is the reason why it's hard

[20:31] to compute because you're taking the

[20:32] exponent and um and dividing. And

[20:36] because you do this there's you

[20:38] basically have no choice but to expand

[20:41] all of the uh key and query computations

[20:47] uh like key query multiplication

[20:49] computations in and be uh quadratic uh

[20:54] quadratic

[20:55] complexity.

[20:57] What linear attention does is you

[20:59] basically start from this uh kind of

[21:04] standard attention formulation but you

[21:06] take you remove the softmax and the

[21:09] normalization here or I mean the

[21:11] normalization doesn't really matter but

[21:13] you remove the softmax and you get just

[21:16] the key query multiplication

[21:19] and [clears throat]

[21:21] this is definitely less expressive

[21:24] because basically what you're doing is

[21:26] you're moving

[21:27] from something that

[21:29] takes in a bunch of uh like numbers.

[21:52] Anyway, like pretend pretend that this

[21:54] bottom one adds up to one, but you're

[21:56] going from a thing that takes a bunch of

[21:58] real numbers and normalizes them into

[22:00] probability like numbers that are

[22:02] between zero and one and add to one. Um,

[22:06] so this nonlinearity allows you to focus

[22:08] on like only some of the previous uh

[22:12] like tokens. And this is kind of the

[22:14] good point of attention. That's the

[22:15] selling point of attention that allows

[22:16] you to focus on the relevant previous

[22:19] context. And you're basically taking

[22:21] away that ability, right? You're you're

[22:24] removing the relative comparisons and

[22:26] just getting um the the dotproduct

[22:28] between the queries and keys. But it

[22:31] allows you to do something really uh

[22:33] nice which is that you can use uh the

[22:37] associative

[22:38] uh you can use associivity and basically

[22:41] rearrange

[22:43] so that um you can convert the sum of

[22:49] all the key and value uh multiplications

[22:53] before into a single uh state matrix.

[22:56] And so this state matrix is essentially

[22:59] a function that map it's a linear

[23:02] function that maps from a query to a

[23:05] value. So attention is also a linear

[23:08] function that maps from a query to a

[23:10] value. So if I go back to this here

[23:12] you're basically calculating you're

[23:14] taking the query you're calculating the

[23:16] attention over all the keys you're

[23:18] multiplying it by the values and you're

[23:20] getting a value here. Um and this state

[23:24] matrix is also that. But the nice part

[23:27] about it is this state matrix can be

[23:29] decomposed. So you can update it. You

[23:32] can keep this state matrix around and

[23:34] update it in constant time every time

[23:36] you get a new value. So this essentially

[23:38] becomes like a recurrent neural network.

[23:40] So it it allows you to update the state

[23:43] matrix um in linear time without having

[23:47] uh without requiring the quadratic

[23:49] computation.

[23:50] So

[23:52] this basically solves your quadratic

[23:54] problem and it solves it so much

[23:57] that um O of N squ becomes O of N.

[24:00] There's no like there's no even W term

[24:03] in this because uh each time you're uh

[24:06] you're updating based entirely on the

[24:08] previous state. Um but there's there's

[24:11] caveats here. So um is this clear though

[24:14] uh so far?

[24:17] Okay, cool.

[24:19] Um, so the big caveat is exactly the

[24:21] caveat I mentioned before. Like this is

[24:23] just a less expressive function. Um, and

[24:26] it doesn't allow you to make like

[24:28] relative comparisons between the

[24:29] previous tokens, that sort of thing. So

[24:32] there's a bunch of uh workarounds around

[24:35] this to try to make a more expressive

[24:39] function that nonetheless is useful in

[24:42] um in kind of uh doing attention-like

[24:44] calculations. And so um most of these

[24:49] are

[24:50] if you dig deep into the math in them,

[24:53] they're basically trying to become

[24:54] better predictors of the final value

[24:56] that you would get from attention. Um

[24:59] and you you can dig into the papers to

[25:01] see how that works, but I'm going to

[25:02] explain them mostly uh mechanistically

[25:05] here. And so um the first thing is

[25:07] Delta. And the idea behind deltaNet is

[25:11] um you can predict what

[25:16] um

[25:18] you can essentially predict what value

[25:21] you would want to be getting from the uh

[25:26] from the calculation of uh KT

[25:30] um and S. And so you know KT here is uh

[25:36] the key at time step t and you are

[25:40] comparing it with the matrix at time

[25:42] step t uh t minus one and uh you're

[25:46] calculating this v hat t and

[25:52] on the other hand you um so basically

[25:57] this this is the prediction that you

[25:59] would get of kt But on the other hand,

[26:02] you know what the uh output VT should be

[26:07] uh based on um what the query times uh

[26:13] or based on uh what the

[26:17] Hang on one second. [laughter]

[26:20] I don't want to I don't want to get this

[26:21] wrong. So

[26:26] you calculate KT with respect to the

[26:29] matrix. And you can view this matrix as

[26:32] a way of uh calculating the uh the way

[26:38] of calculating the mapping from a query

[26:42] to a value. And you can also get the the

[26:46] actual value and subtract out uh what

[26:50] the value you get when multiplying it

[26:53] from the previous uh together with the

[26:54] previous matrix is. And this is

[26:57] essentially the error uh that you get

[26:59] here. And then you want to reduce the

[27:01] error. And so in order to reduce this

[27:04] error, what you do is you um essentially

[27:07] add in this uh this term which is KT uh

[27:12] times the error term. And after you do

[27:15] this, if you multiply in KT to the new

[27:17] matrix, you will no longer have any

[27:20] error. But you don't want to make an

[27:23] update that is too big. So you add this

[27:25] beta term. This is essentially a

[27:27] learning, it's similar to a learning

[27:28] rate. And this learning rate will make

[27:31] the updates uh smaller. And so uh if you

[27:34] if you do this, this allows you to

[27:37] basically nudge the matrix in the

[27:40] direction of uh the in the direction

[27:44] that will cause a query that looks like

[27:48] the current key to output the value that

[27:50] you want essentially. So it's it's

[27:53] reducing the error uh reducing the error

[27:55] in the prediction of the value that you

[27:57] want.

[28:00] So um as I said this is going to be a

[28:03] little bit high level. Um the the papers

[28:06] are are pretty good uh descriptions of

[28:08] this.

[28:10] Um so after this um this basically what

[28:14] this is doing is this is pushing you in

[28:16] the direction of the uh of making the

[28:20] the matrix a better predictor of the uh

[28:24] the value. But one problem with this is

[28:27] you can build up lots and lots of

[28:29] context uh from the previous uh spots

[28:32] and linear attention doesn't have any

[28:35] mechanism to prevent very far away cont

[28:38] uh context from having a bad

[28:42] influence on your next predictions. And

[28:47] so if you have like a very weird key far

[28:52] back in the future, it might have a very

[28:54] big influence on you in the f uh in the

[28:58] future. And so the way they fix this is

[29:01] basically they have a decay term to make

[29:04] uh to make the

[29:08] matrix decay

[29:10] a little bit at every time step. And by

[29:14] decaying the matrix a little bit at

[29:16] every time step, they're basically

[29:17] discounting the the far in the past

[29:20] context. And so you multiply um the

[29:23] matrix by alpha t and then you add this

[29:27] uh st tilda into uh into your

[29:31] calculation here and update the matrix.

[29:33] And so the stronger you make this decay

[29:36] basically the the more quickly uh it

[29:38] will forget the previous context. And so

[29:41] you can make this more local or or less

[29:43] local.

[29:47] And so this is uh gated delta is used in

[29:50] the Quen models. So it's one of the more

[29:53] uh the more popular methods now. Um but

[29:56] both uh GLM and uh KI which are kind of

[30:00] two of the state-of-the-art models use a

[30:02] slightly more expressive version of this

[30:05] uh where they basically have a per

[30:07] element uh decay term. So each element

[30:10] can decay at a different speed. And uh

[30:13] because each element decays at a

[30:14] different speed, you can have some uh

[30:17] portions of the context that uh you know

[30:20] carry over very long time periods, some

[30:22] portions of the context that carry over

[30:24] very short time periods.

[30:28] Cool. So hopefully this was more or less

[30:33] uh more or less legible. Um

[30:37] any any questions here?

[30:39] Long long story short, it's basically a

[30:41] way to turn uh into

[30:44] um it's a way to turn

[30:48] the idea of attention to something that

[30:50] you can calculate um in context. Mamba

[30:54] is uh something that's very similar um

[30:58] but it's a little bit more

[30:59] mathematically involved um uh and I I

[31:02] decided to skip over it. uh I covered it

[31:04] more in the uh language model uh

[31:07] description course but similar idea but

[31:10] just a bit more complex uh in the math.

[31:14] So the next thing I'd like to talk about

[31:15] is sparse attention. And so sparse

[31:18] attention is uh basically looking up a

[31:25] not attending to everything in the

[31:27] previous context but only attending to

[31:30] some things in the previous context. And

[31:32] essentially you limit the number of

[31:34] things that you look up in the previous

[31:35] context. There's a few ways you can do

[31:37] it. Um originally in there was a sparse

[31:41] attention paper by OpenAI uh quite a

[31:44] while ago like 5 years ago or something

[31:46] like this. Um and basically uh what they

[31:50] did was they had sparse attention every

[31:53] you know uh 512 tokens or something like

[31:57] this. And what this does is it means

[31:58] that you still have a fixed it's still

[32:01] quadratic in the sequence length but

[32:03] it's 512 times less than if you attended

[32:06] to every token and that's like good

[32:08] enough uh that you can manage to

[32:10] calculate it over the context that

[32:12] you're interested in.

[32:14] Another option is to do um content

[32:17] dependent sparse attention. And

[32:19] basically what this does is you have a

[32:21] very cheap way of calculating attention.

[32:23] Like for example, you can down project

[32:25] the attention vectors to be very very

[32:27] small and then you do attention over

[32:30] these very very small uh attention

[32:33] vectors. You pick the top k ones and

[32:35] then you do full attention over the top

[32:36] k. So uh that's uh another way that you

[32:40] can do this

[32:42] and this is what's used in deepseek.

[32:43] Yeah.

[32:43] >> How do we define the metric for which we

[32:46] do the top similarity compared in this

[32:50] in the shrine space we just do like

[32:53] coine distance.

[32:55] >> Yeah.

[32:57] >> Yeah. I I think it's typically not

[32:59] cosine but it's just product but yeah

[33:03] >> I I I think although maybe maybe they're

[33:05] normalizing beforehand. They actually

[33:07] don't know that detail.

[33:10] Any other questions?

[33:13] So basically um these

[33:17] th this is a very very cheap way to

[33:21] achieve global attention because you can

[33:23] just uh write a kernel that will do this

[33:26] for you. Um this over here will uh

[33:30] require you to have two passes, but you

[33:32] know it's potentially uh more accurate.

[33:35] So um I I've seen both of these used

[33:37] pretty widely.

[33:41] So a final um a final thing is KV

[33:44] compression. How many people saw this in

[33:46] a language modeling course?

[33:49] Maybe some people. Okay. Um so I will uh

[33:54] I'll explain this. So basically um this

[33:57] is standard multi head attention. And so

[34:00] in standard multi-head attention, you

[34:01] have a bunch of heads and each one has

[34:04] values and keys and all of these are a

[34:08] certain dimension. So they're like

[34:09] dimension, let's say they're dimension D

[34:12] and you have uh you have like a certain

[34:16] number of heads. Let's say that's H. Um

[34:20] so

[34:23] the two main ways that people solve uh

[34:26] or help uh this problem of having very

[34:29] uh large and expensive KV caches is uh

[34:33] grouped query attention. And grouped

[34:35] query attention basically uh just uses a

[34:38] smaller number than h um you usually h

[34:42] divided by some uh power of two uh

[34:46] number of uh keys and values. And

[34:50] because it's the KV cache, it's not the

[34:52] KVQ cache. Um

[34:55] if you reduce the number of uh keys and

[34:57] values that are used, you reduce the

[34:59] amount of memory that you need to hold

[35:01] the KV cache. This is really important

[35:02] because if it gets very large then um it

[35:06] limits the number you can fit on one GPU

[35:08] and so this can usually be reduced by

[35:11] like four or by eight or something like

[35:13] that. Um multiquery attention is just

[35:17] like grouped query attention with a

[35:19] single one. So you can kind of almost

[35:21] skip over that. You already know what it

[35:22] means. Um multi head latent attention

[35:26] the the um

[35:30] is essentially down projecting uh the

[35:35] size of the keys and values. So it's not

[35:39] reducing the number of heads, it's

[35:40] making each head smaller. And so this is

[35:43] similar to what I talked about with the

[35:45] top K attention. Um and of course you

[35:47] can combine both of these together as

[35:48] well. You could have group query

[35:50] attention with um you know smaller uh

[35:52] keys of values.

[35:57] Uh any any questions here?

[36:02] Okay, cool.

[36:05] Um so the these are the method the

[36:07] architectural methods that people use to

[36:09] handle very long contexts and with these

[36:13] um you can handle up to a million uh

[36:16] tokens. So like this is uh you know this

[36:19] makes the efficiency possible.

[36:22] The next thing is uh training long

[36:25] context models. And this is actually uh

[36:29] pretty hard. And the reason why is

[36:32] because um if we want something to

[36:36] handle 128k tokens or even more, there's

[36:41] actually not that much data on the

[36:44] internet that is 128k coherent tokens.

[36:48] Um it's actually a lot of a lot of data.

[36:51] it's more than most Wikipedia articles,

[36:53] you know, um you're starting to get in

[36:55] the in the order of like having a book

[36:57] uh that you need to have and there's not

[36:59] that many books on the internet. So,

[37:00] typically what you do is you start out

[37:02] with like short pre-training. Um you do

[37:05] more continued training with longer

[37:07] documents and then you do long

[37:08] adaptation.

[37:10] Um I wrote packed sequences here. Um,

[37:14] but packed sequences are are useful can

[37:17] be useful for efficiency, but they're

[37:19] not super useful for learning long

[37:20] contexts because um every time you like

[37:24] let's say you pack 10 documents into a

[37:26] sequence, you're not learning to attend

[37:28] across the documents and in fact you

[37:30] probably should not be. So um you really

[37:33] need coherent uh long sets of data to do

[37:36] adaptation to very long contexts.

[37:41] Um so I'm going to talk about a few

[37:43] things that we do here. Um the first

[37:45] thing I'm going to talk about is uh

[37:47] handling positional encodings. Um so

[37:51] absolute positional encodings uh I I

[37:54] hope everybody has seen in their

[37:56] language modeling class. Um but

[37:59] basically uh each individual

[38:04] entry in the uh

[38:07] each individual word embedding uh gets a

[38:10] position vector and that position vector

[38:12] is typically calculated by uh some sort

[38:15] of function like using signs and

[38:17] cosiness and other stuff like this. So

[38:19] hopefully you know most people have seen

[38:20] this. So I'll I'll kind of skip over

[38:23] that. Also maybe most people have seen

[38:25] rope. Are people generally familiar with

[38:28] rope? Okay, I see a fair number of

[38:32] people. I see actually less people uh

[38:34] than I would have expected, but um uh

[38:36] maybe people are just uh not interested

[38:39] in raising your hand. Um [laughter] but

[38:42] uh but basically um rope rope is pretty

[38:46] elegant mathematically in my opinion. Uh

[38:48] basically the problem they were trying

[38:50] to solve is they wanted to have a

[38:53] positional embedding. um where the

[38:58] positional uh or positional encoding

[39:01] where the positional encoding is

[39:03] entirely

[39:05] determined by the relative distance uh

[39:08] between two tokens.

[39:10] And the

[39:14] reason why they wanted to do this is

[39:16] they didn't they didn't want the

[39:19] absolute position to have an effect on

[39:23] uh they didn't want the absolute

[39:25] position to have an effect on whether

[39:27] two tokens would attend to each other.

[39:30] And so

[39:33] this is this has been quite effective

[39:36] and a lot of uh a lot of models use

[39:41] rope. Um the the math I'm not going to

[39:44] go through here because it's kind of not

[39:45] the main point, but they do some

[39:47] interesting stuff with rotations and

[39:49] imaginary numbers and stuff like this.

[39:51] Um but there's also this like super

[39:55] counterintuitive

[39:57] uh nope.

[40:00] which is uh don't don't use positional

[40:02] encodings at all. Um and if you took

[40:06] your uh class on transformers

[40:09] uh you might have heard this scary stuff

[40:12] which is like you need positional

[40:14] encodings for transformers because

[40:17] otherwise something in position one in

[40:21] position five will have exactly the same

[40:24] representation. So if you have like this

[40:27] this is a cat but this is not a cat it

[40:30] will attend to both of the cats the same

[40:31] amount or something like this. Um

[40:36] theoretically when the transformers were

[40:39] originally created um this might have

[40:41] been true but now actually it's it's not

[40:43] true anymore based on the transformers

[40:45] we use now. Um anybody have an idea

[40:50] why this is the case? I've kind of given

[40:52] a hint in the slide but

[40:55] you might also need to know a little bit

[40:56] of the history of transformers uh which

[40:59] is uh before we were using encoder

[41:00] decoder models uh where the encoders

[41:03] encoded all of the input and then the

[41:04] decoders uh generated the output any

[41:08] idea

[41:11] >> because we're doing causal masking

[41:13] exactly so um to elaborate on that a

[41:16] little bit if I go back to our

[41:18] transformer equation

[41:21] Um, we have the keys um, and the

[41:25] queries. And if we look at the queries,

[41:30] even if you have cat at position two and

[41:32] cat at position five, the cat at

[41:35] position two is only attending to the

[41:36] previous token where the cat at position

[41:39] five is attending to the previous four

[41:41] tokens. Um, and so both of them are like

[41:45] actually different. um starting at least

[41:47] in the first layer of attention. And so

[41:50] you can tell like even if they are

[41:52] exactly the same word, the embeddings

[41:55] starting in the first layer of attention

[41:56] will will not be different. And there's

[41:58] kind of uh this counterintuitive paper

[42:01] that demonstrates that you don't need uh

[42:03] positional encodings at all. And this is

[42:06] especially true um this is in auto

[42:10] reggressive uh transformers. In non-auto

[42:12] reggressive transformers where you're

[42:14] attending all the tokens are attending

[42:15] to each other. You still do need

[42:17] positional encodings. Um

[42:21] this is especially true when we start

[42:22] talking about like gated delta because

[42:25] gated delta has like the decay term and

[42:28] uh other things like this which causes

[42:30] each uh token to be different. So once

[42:33] we start having those sort of local

[42:34] biases, we actually don't need

[42:35] positional uh encodings anymore.

[42:39] Um

[42:41] and

[42:42] if you uh if you look um

[42:46] we uh the first two here have rope uh or

[42:51] at least partial rope. The second two

[42:53] have nope uh no positional attend

[42:55] encodings. Um the the fourth one uh

[42:59] relies entirely on implicit order and

[43:02] mamba and some of them in uh and inkling

[43:05] has relative positional encodings. So

[43:08] you can see that it's kind of like half

[43:10] split between having relative positional

[43:11] encodings and not at all. But like let's

[43:14] say we did have positional encodings. Uh

[43:16] one thing you need to worry about for

[43:17] long context is uh position

[43:20] interpolation or position extension. And

[43:24] what this means is if you have a

[43:25] pre-training range, um, you need to

[43:29] essentially extend your model so that

[43:31] it's able to handle longer sequences.

[43:34] And so the the promise of rope was that

[43:38] rope relied only on the relative

[43:41] position uh between the different tokens

[43:46] in the output. But

[43:49] that that's fine as long as the relative

[43:52] position is only um well okay there

[43:56] there's two reasons why this is not

[43:58] fine. So number one if you're training

[44:00] on

[44:02] sequences of length L and then you

[44:05] extend to sequences uh of length SL then

[44:09] it's never seen two tokens attend to

[44:12] each other over a distance of more than

[44:14] L. So the tokens that are more than L

[44:17] away from each other are going to have

[44:19] problems attending to each other and

[44:20] you're not going to be able to uh manage

[44:22] that very well. Um the other problem is

[44:26] that actually relative positional

[44:28] encodings are only one part of the story

[44:31] and like actually the auto reggressive

[44:32] mask has an effect in all these other

[44:34] things. So you can't just take rope and

[44:37] expect it to work uh really well on

[44:39] longer sequences.

[44:41] And so the typical way you fix this is

[44:45] there's a parameter in rope that

[44:46] basically

[44:48] uh

[44:51] let me see if I have it in my slide.

[44:55] So I I don't I don't really have it in

[44:57] my slide, but there's basically a um a

[44:59] parameter in rope theta that uh tells

[45:02] you how much you rotate at each time

[45:03] step. and you divide this theta by the

[45:08] uh multiplier by which you extended the

[45:10] sequence. And so basically you're

[45:12] stretching the rope position so that the

[45:16] rope uh position at position zero would

[45:19] um or the rope position at position like

[45:22] five would be 5s uh would be equivalent

[45:26] to the position 5s in your uh extended

[45:28] context.

[45:30] And there's also um a more sophisticated

[45:34] way of doing this called yarn uh which

[45:37] basically is uh similar

[45:41] in spirit uh to like the delta uh the ki

[45:47] delta attention

[45:49] um which

[45:51] basically said that we want some of them

[45:54] to be very long distance and some of

[45:56] them to not be very long distance. In

[45:58] yarn essentially you have some of them

[46:00] be uh extended more and some of them be

[46:03] extended less and so you don't um you

[46:06] don't necessarily interpolate all of

[46:08] them at the same frequency.

[46:14] So um yeah in the interest of time I'm

[46:16] not going to go into like a lot of

[46:18] detail about this but basically these

[46:19] are um uh these are the various methods

[46:22] that you can use here.

[46:27] So, um,

[46:29] I'd like to talk a little bit now, um,

[46:31] taking a step back from the detailed

[46:33] modeling stuff and going into the data

[46:35] that you can use to train this. So, um,

[46:39] as I mentioned before, packed examples,

[46:40] you can just pack a whole bunch of stuff

[46:42] in there, um, a whole bunch of documents

[46:45] in into your context length. And this

[46:48] will work at training models to be able

[46:50] to process things near the end of your

[46:52] context window. But what it won't work

[46:54] for is the kind of global coherence. And

[46:58] um so there's a number of different ways

[47:01] that people do this. One way is just to

[47:03] find um very long documents uh like

[47:07] books or something like this. There

[47:09] aren't a lot of these uh but there are

[47:11] books. There are code bases and code

[47:14] bases tend to be coherent. So you can

[47:15] just download a big codebase and that

[47:17] will definitely have more tokens. Um

[47:20] multi-document corpora of some kind. So,

[47:23] you know, like uh you can get a whole

[47:25] bunch of documents that are on the same

[47:26] topic and then at least you'll have

[47:28] topical coherence between them. Um I've

[47:30] also seen people train on patents

[47:32] because patents have like there's lots

[47:34] of public data for them and you can kind

[47:37] of link link them together.

[47:39] A big source nowadays is agent

[47:41] trajectories because you know agents can

[47:45] make very very long trajectories if you

[47:47] just interact with them for a little

[47:48] while. So that's another one. And then

[47:51] you can also create synthetic tasks and

[47:53] a lot of the evaluations are synthetic

[47:55] tasks. So you can do that as well.

[47:59] Um and I I have some examples of how the

[48:03] models do this. Um a lot of the model

[48:06] training companies don't like to share

[48:07] these details with you because this is

[48:09] like if they release their um well so

[48:13] number one the closed models like

[48:14] anthropic open AAI you know those places

[48:18] uh uh Gemini they will not release even

[48:20] their architectural details the open

[48:22] model companies have to release their

[48:23] architectural details otherwise you

[48:25] can't run their model so what do they

[48:27] keep secret they keep their data mixes

[48:29] and their their training strategy secret

[48:31] so um this there's a lot less detailed

[48:34] stuff that we can say. Um, but there's

[48:38] uh all of them explain all of the ones

[48:41] in here explain a little bit about their

[48:42] data mixtures and they are things like

[48:45] uh cleaned up sampled documents and

[48:47] video um documents, repository files,

[48:50] issue, PRs, uh long document QA,

[48:53] scientific papers and technical reports.

[48:56] And then uh they also create a bunch of

[48:58] synthetic tasks. And typically they have

[49:00] a scaling strategy of like 8 64 256 1

[49:03] million uh that that sort of stuff as

[49:05] well.

[49:10] Oh yes. Um [clears throat]

[49:12] one other

[49:14] logistical detail that you might need to

[49:17] deal with um or might not need to deal

[49:19] with depending on the size of the model

[49:20] you're training. like for example for

[49:22] your project if you want to start

[49:23] dealing with um uh larger models is

[49:27] context parallelism and basically what

[49:30] this means is there's a bunch of uh ways

[49:34] to do parallelism when training models I

[49:36] wrote context parallelism up here what

[49:38] are two other ways uh that you can

[49:40] parallelize models during model training

[49:42] or serving

[49:44] >> yes

[49:47] >> data parallelism

[49:50] >> yeah you you said a more specific

[49:52] example of the second one but data

[49:54] parallelism and I would say model

[49:55] parallelism in general and model

[49:57] parallelism can have lots of varieties.

[49:59] It can have uh expert parallelism where

[50:02] you have different experts on different

[50:04] machines uh tensor more generally tensor

[50:06] parallelism where you split um uh the uh

[50:10] the parameters and you can also have

[50:11] pipeline parallelism where you have

[50:12] different layers on different uh

[50:14] different devices. But context

[50:16] parallelism starts becoming import more

[50:18] important for agents because when you

[50:20] train agents you want to train them on

[50:22] very long contexts. And so uh the way

[50:25] this works is you will compute like one

[50:28] part of the context uh the keys and

[50:31] values. So you send it to the next

[50:32] device calculate the keys and values for

[50:35] the next for that part send it to the

[50:37] next device uh and etc etc. So um this

[50:42] is uh very useful. It's really important

[50:44] if you start getting above like 32k

[50:47] 32k context or so. Um, but it's also a

[50:51] pain because

[50:54] you have the

[50:58] um

[51:00] you have all the modeling people saying

[51:02] I want my I want my KI delta attention

[51:05] and then you have all the info people

[51:06] saying but wait I need to implement a

[51:08] context parallel kernel for KI delta

[51:10] attention and make sure it actually

[51:12] works and you can back prop through it

[51:14] and all of these other things. So um I I

[51:19] personally had an experience where I was

[51:20] trying to train uh Quen uh for uh like a

[51:24] smaller quen model like 135 uh 35b and

[51:29] uh I I wanted to go do use context

[51:32] parallelism on it and it's like there's

[51:33] no kernel for gated delta net anywhere

[51:35] on the internet and so um you need to uh

[51:38] you need to either go in and implement

[51:39] that kernel or decide to do something

[51:41] else. So um th those two can conflict

[51:44] some of the times. So be be aware I

[51:46] guess

[51:51] um the the good news is for like

[51:53] standard attention and sliding window

[51:55] attention and stuff like that all of

[51:56] those will have uh kernels more easily

[51:59] implemented. The hard parts are where

[52:00] you're like not doing a standard

[52:02] attention operation.

[52:06] Cool.

[52:09] Okay. So the next part I'd like to talk

[52:11] about is prompt and KV caching. This is

[52:14] uh very important even if you're not the

[52:16] person who's implementing the language

[52:18] model, but also if you're just a person

[52:19] who's um

[52:22] like running agents uh yourself, but I'm

[52:26] going to talk about uh the the technical

[52:28] details of how it's implemented. So, you

[52:30] know, at least you you have a good uh

[52:32] idea about how that works. So um

[52:35] basically

[52:37] when we I I simplified this a little bit

[52:40] but when we're generating an agent call

[52:42] we have an input uh we have an output uh

[52:46] so this could be like the the messages

[52:48] and tool calls and then we have the tool

[52:49] result and so so

[52:55] as we calculate the input we do prefill

[52:59] and as we calculate the output uh we do

[53:02] uh basically decoding Right? And so

[53:04] during prefill and decoding, we have to

[53:06] calculate the KV cache. This is all done

[53:08] in a batch. Uh this is done every time

[53:11] we generate a token. But after we have

[53:13] that, we have the uh key and value uh

[53:16] for each of the positions up until the

[53:18] end of the output. And so what we can do

[53:20] is we can throw that in a cache and then

[53:22] we don't need to calculate it anymore.

[53:24] The tool result is new uh because you

[53:27] know we don't calculate over the tool

[53:29] result. So this becomes a new input and

[53:32] we generate an output and we get another

[53:33] tool result. And so in step two we need

[53:37] to calculate the KV cache over the new

[53:38] input and we uh during prefill and the

[53:41] output but we can reuse the cache

[53:44] and then we do that over and over and

[53:45] over again. And so as you imagine um as

[53:49] you can imagine I just showed steps 1 2

[53:52] 3 but by the time we get to step 50 if

[53:55] we haven't done anything tricky with our

[53:57] output this is going to be 50 times

[53:59] larger than the new input in the in the

[54:02] output right so that's pretty

[54:04] significant savings if we can cache this

[54:06] properly

[54:10] and here are some examples from actual

[54:12] papers uh that you know examine this and

[54:15] basically What we can see is this is

[54:18] like the the token length on uh

[54:20] different GPUs and this is the amount of

[54:25] uh of compute that you need with caching

[54:28] and no caching. And so the upper one of

[54:31] the same color is uh or the lower one

[54:34] with the same color is caching and the

[54:36] the upper one is no caching. So uh

[54:40] basically as the sequence gets longer

[54:42] the non-cashed one becomes quadratic and

[54:44] the cache one is is mostly linear.

[54:50] This also shows up in how much you pay

[54:53] to run an agent. And so I I pulled all

[54:56] of these numbers from uh the official

[54:58] pricing. And basically you can see here

[55:02] that if you go through all of these uh

[55:04] all of these numbers including the

[55:05] commercial ones typically cashed tokens

[55:08] are onetenth of the price of uncashed

[55:10] tokens. And so what this means is you

[55:13] need to be very aware of uh whether your

[55:16] tokens are being cached or not. Uh

[55:18] because if they're not being cached uh

[55:20] you're going to be paying a lot of money

[55:22] to be running your agents. Um,

[55:26] so does anyone have an idea of what a

[55:28] good uh cash hit rate is

[55:31] if you're running an agent? Yeah.

[55:33] >> 80 to 90%.

[55:34] >> 80 to 90%.

[55:37] >> Yeah.

[55:44] >> Um, yeah. So I I heard 80 to 90% I heard

[55:49] like more than 95%. I my my impression

[55:53] is 90 to 95 is everything is fine. Like

[55:56] I'm I'm good with 90 to 95. If it's less

[55:59] than that, you might be fine, but you

[56:01] might be might be losing out somewhere.

[56:03] Um so, uh yeah, so basically you can you

[56:08] can cache most of your tokens. Um one

[56:11] other interesting thing is the output

[56:12] also tends to be five times more than

[56:14] the input. So um this is uh there's a

[56:17] 50x difference between output and cached

[56:19] input which just reflects the amount of

[56:22] uh uh the amount of cost uh savings that

[56:25] you can get from serving it.

[56:28] So why why is caching um so much cheaper

[56:34] is maybe kind of obvious. You just need

[56:36] to look up um you need to look up the

[56:42] outputs. uh you just need to look these

[56:44] up instead of like actually uh

[56:46] performing the calculation over them. Uh

[56:49] especially the feed forward network

[56:50] calculation is pretty expensive in

[56:52] transformers and so being able to skip

[56:54] that is is uh particularly a win. Um but

[56:58] how do we actually manage that? So

[57:02] um the first thing is uh how do you hold

[57:06] it in memory? And there's two like most

[57:10] popular open-source

[57:12] uh two most popular open-source

[57:15] LLM serving libraries VLM and SGLANG and

[57:18] both of them are based on an innovation

[57:22] around the how you manage KV caching. Um

[57:26] so VLM's main technical in innovation

[57:30] and like of course they have a lot more

[57:32] stuff in there now. They're like general

[57:33] purpose serving libraries, but like the

[57:36] main technical innovation that led to

[57:38] VLM was something called page detention.

[57:41] And basically the way it works is you

[57:43] have physical GPU memory blocks and you

[57:46] rear you arrange them like kind of

[57:49] memory blocks or or disk blocks on uh

[57:53] like more typical uh like CPUbased

[57:57] machines. And so you might have uh block

[58:01] zero uh block one block two that you

[58:04] actually need to calculate and they put

[58:08] that you know in like block one and then

[58:10] block seven and then block three or

[58:13] sorry uh block seven block one block

[58:14] three and then you have an index to each

[58:18] one of these uh as you're generating.

[58:20] And the reason why they wanted to do

[58:22] this is they want to be able to generate

[58:23] in parallel many sequences in parallel

[58:26] and when you finish generating um you

[58:29] can like evict that from your memory and

[58:31] so you can uh evict whole blocks at once

[58:34] and this makes the calculation more more

[58:36] efficient. So um this is uh one

[58:39] technical trick that they used to make

[58:40] this uh you know make parallel serving

[58:44] work.

[58:46] Um

[58:48] the technical innovation that kind of

[58:50] led to SG lang in particular uh was

[58:53] something called RAIX attention and this

[58:55] is specifically focused around uh like

[59:00] re reusing already cached uh out uh

[59:04] inputs. And so what they do is they form

[59:08] a a tree basically uh it's a radics tree

[59:13] and they use this to look up prefixes

[59:15] that have been used already. And so this

[59:18] uh when it first came out this was

[59:20] specifically focused around uh chat bots

[59:22] like chatgpt

[59:24] uh because you know you can have

[59:26] somebody start a conversation and then

[59:27] continue the conversation and so you'll

[59:29] be caching some portion of the already

[59:31] done conversation. But for uh now it's

[59:36] like much much more important for agents

[59:38] because agent conversations are much

[59:39] longer and much more frequent. So we

[59:41] need this uh looking up more frequently.

[59:46] Um so another uh another thing that you

[59:50] need to think about um which is handled

[59:52] in uh newer versions of sglang for

[59:55] instance is let's say you're doing

[59:57] multi-achine serving. So you're serving

[60:00] on um you know different machines uh you

[60:05] know maybe you have a data center with

[60:07] like 64 nodes or 128 nodes or something

[60:09] like this. um every time a request comes

[60:12] in, you want to route it to the machine

[60:14] that has your KV cache that has the best

[60:17] KV cache for you um to be accessing and

[60:21] so that you actually have cache aware

[60:23] routing uh route it to the appropriate

[60:25] place and then have the worker with the

[60:27] best uh KV cache match uh process set.

[60:32] And so

[60:34] I love getting all my uh my serving

[60:36] statistics from Open Router um because

[60:39] they have so much data and uh they cover

[60:42] all of the things I want to talk about,

[60:44] but I believe they even have

[60:47] a ranking of providers by cash hit rate.

[60:50] [laughter]

[60:51] I'm sorry mist the data the data doesn't

[60:54] lie but um you can see uh mistrol has

[60:58] the worst cache hit rate and then um you

[61:02] have other one other ones like Alibaba

[61:04] cloud or dicard or silicon flow that

[61:06] have higher cash hit rates um this is

[61:09] not entirely reflective of the provider

[61:12] being bad or something like that it

[61:13] could be just the workloads that they're

[61:15] running but there's a number of things

[61:17] that like actually factor into

[61:20] into this cache hit rate and um one of

[61:24] them one of them is how good is the cash

[61:28] routing. The other one is how fast is

[61:30] the cash eviction. Um so the providers

[61:35] will not hold your cash for you forever.

[61:38] Um they will uh you know evict your cash

[61:42] after a certain amount of time. Does

[61:44] anyone know how long this is for like

[61:47] popular providers? Have you ever taken a

[61:49] look at that

[61:50] >> yet?

[61:52] Close to an hour.

[61:53] >> Close to an hour. I I think the long

[61:56] like I'm not I'm not like super up to

[61:59] date on this, but I know anthropic used

[62:01] to be five minutes. And so it's

[62:03] basically if you have a an active

[62:05] conversation going on with them and you

[62:07] don't pause your conversation, you'll

[62:08] stay in the cache. Otherwise, if you

[62:10] like stop the conversation, you get

[62:11] evicted from the cache. I think you at

[62:14] least have an option to go up to an hour

[62:16] now. Um but I don't know if you um but

[62:19] like it costs a little bit more if you

[62:20] go up to an hour or something. Um but

[62:23] yeah, ba basically they don't want to

[62:24] keep this around because there this is a

[62:26] huge amount of memory uh that they're

[62:28] keeping in memory and so they want to

[62:30] use it if it's working and and evict it

[62:32] if it's not working. So um that that's

[62:35] another policy that could change your

[62:36] cash hit rate. The bad news for us as

[62:39] users is the pricing doesn't change no

[62:41] matter how good the provider is at

[62:42] routing or um or cash eviction. So you

[62:47] uh you might be paying just because they

[62:50] evict you uh evict you too quickly which

[62:52] seems a little bit unfair.

[62:54] >> Um yeah

[62:57] >> do they use like cash layering where you

[62:59] can store it on device in memory that's

[63:02] like adjusted to device and then on this

[63:04] >> yeah so the that's a great question. So

[63:06] the question was, do they use a cache

[63:08] layering where you have like a fast

[63:10] cache that's stored in the device and

[63:12] then uh a slower cache that's stored on

[63:14] disk or something like that? I actually

[63:17] don't know the answer to that question.

[63:18] That'd be a great uh like a great

[63:20] follow-up for us to do. Um the open

[63:23] source libraries also are probably not

[63:26] as sophisticated as the closed libraries

[63:27] because um if you look at all the people

[63:29] on open router their job is to be really

[63:32] good at serving and so you know they're

[63:35] some of them might be using open source

[63:37] libraries but they'll be building stuff

[63:38] on top of them and that's kind of their

[63:40] you know competitive differentiation. So

[63:43] um like I I think

[63:47] the internal solutions that inference

[63:48] providers are likely to be you know a

[63:50] bit better than the ones that are

[63:51] available in open source too with

[63:53] respect to that.

[63:54] >> They usually offload to CPU from GPU.

[63:57] >> They usually offload to CPU from GPU.

[63:59] Yeah.

[64:00] >> Yeah. Because your GPU memory is so

[64:03] precious. So yeah. Yeah.

[64:07] >> Cool. Um so uh yeah. Oh, sorry. I

[64:12] skipped a important part. So, what does

[64:14] this mean? If you're just designing a

[64:16] harness and you're not deploying models

[64:18] or or anything like this, it means you

[64:21] need to be super super careful to not

[64:24] break your cache unintentionally.

[64:27] So, remember that your cache only works

[64:29] if the entire prefix is exactly the

[64:31] same. And so there's a bunch of things

[64:36] that we've thought about

[64:38] uh doing but we decided are a very bad

[64:42] idea because we don't want to break the

[64:44] cache. So one thing that's completely

[64:48] forbidden you should not do is don't

[64:51] change the system message every time you

[64:55] uh you take a step because that means

[64:58] like no caching essentially. uh you

[65:00] don't have a single message that you're

[65:01] able to cache. So one thing one very

[65:04] logical thing that you might think of is

[65:06] okay I want to append the current time

[65:08] and date to the system message uh so

[65:11] that the agent knows what time it is. Do

[65:14] not do this because the time and date

[65:15] changes every step and so that will

[65:18] break your cache. So if you do need to

[65:20] append it, append it to the final user

[65:22] message uh or the final uh tool call

[65:25] result that you get. um and uh like

[65:31] changing your um changing your tools uh

[65:34] dynamically in the middle of the

[65:36] conversation. You can do this. That's

[65:37] okay. Um another thing is a very logical

[65:41] thing that you might think of doing is

[65:43] routing to a different model every time

[65:45] you uh every time you take a step. So

[65:47] it's like this step looks like a really

[65:49] good model for you know a really power a

[65:51] really good step for a really powerful

[65:53] model. um like uh like I want to do this

[65:57] step on Fable and then I want to do the

[65:59] ne next three steps on um on a cheaper

[66:02] model to save money. But the thing is

[66:04] you're still paying

[66:07] you're still paying the you know 10x

[66:09] cost for Fable the next time you use uh

[66:12] Fable. So you really need to be very uh

[66:16] frugal in the amount of switching you're

[66:18] going to be doing if you want to be

[66:19] doing switching to save cost for

[66:20] instance.

[66:23] Cool. Um,

[66:26] so the final thing I'd like to talk

[66:28] about is context compaction. Um, how

[66:31] many people know know about this? Use

[66:33] this in your everyday coding agent use.

[66:37] How many people are really excited when

[66:39] it says compacting context?

[66:42] [laughter]

[66:43] That's nobody good. So um the the basic

[66:48] idea behind context compaction is uh

[66:51] that you have uh before

[66:55] and uh this is you know all your

[66:58] observations and actions that you might

[66:59] have had. Um then after what you tend to

[67:03] do is you tend to take your previous

[67:05] context and you crush it down into just

[67:09] the essence of the previous context. Um,

[67:12] and so the reason why people are

[67:17] like not excited about using this, uh,

[67:19] perhaps obviously is if you do a bad job

[67:21] at this, your agent forgets things. It

[67:24] starts doing something completely

[67:25] different and, uh, maybe deletes your

[67:28] file system.

[67:30] So

[67:33] um we can view compaction as essentially

[67:36] trying to come up with a previous

[67:39] representation where your future action

[67:42] sequence um you take your history, you

[67:45] compact that, you get a working state

[67:48] and you want your future action sequence

[67:50] to be the same or you know similar or

[67:54] possibly better um if uh after

[67:57] compaction than it was before. Um

[68:01] at the same time you also have a

[68:03] constraint which your

[68:06] state needs to be bounded. So it needs

[68:08] to be small enough that you're happy to

[68:10] continue work.

[68:13] Um so if we look at what survives uh

[68:17] compaction um there's different ways of

[68:22] doing this. I'm going to cover the

[68:23] different ways that people do this, but

[68:28] a common strategy is to take some

[68:32] anchors and these can be the very first

[68:35] um like the very first things the user

[68:38] said when they started the session for

[68:39] instance. Um,

[68:42] so, uh, one of the answers to the things

[68:44] that I heard agents forget when I asked

[68:47] the question, what do agents forget was

[68:50] sometimes they forget the things at the

[68:52] very beginning of the session? And

[68:55] that actually might be a design bug in

[68:58] the agent harness that you're using. Um,

[69:01] because uh, some good agent harnesses

[69:03] uh, like kind of intentionally avoid

[69:06] deleting the stuff at the very beginning

[69:07] of the session because they think it's

[69:08] more important. Um, but it could also

[69:12] be, you know, impossible to avoid

[69:14] depending on the situation. Um, also you

[69:17] want the stuff in the middle that's

[69:18] encoded and put back into the context.

[69:21] And then the recent tail is often kept

[69:24] around. So often people will keep around

[69:26] the the most recent actions.

[69:29] Separately from this, I don't see this a

[69:31] whole lot, but um, you can also add the

[69:35] evidence to an evidence store. Actually,

[69:37] no, sorry. I I'll correct this. Um, the

[69:40] evidence is typically added to an

[69:42] evidence store. Um, and at the very

[69:45] least, if you're using a CLI coding

[69:47] agent, usually your full history is

[69:49] saved on disk somewhere. And so, if you

[69:52] know where on disk, your coding agent

[69:54] has saved all of this history. Even if

[69:57] you lose stuff through compaction, you

[69:58] can tell the coding agent to go back and

[70:00] read the history, and it can, you know,

[70:02] uh, read the history for you and find

[70:03] the the previous results. Um but there

[70:06] there are also uh possibly more

[70:09] structured ways of doing this and so

[70:12] then um you know other things can be

[70:13] discarded.

[70:15] Um so there's a few ways to decide uh

[70:19] compaction policy. Um the first one is

[70:21] the trigger and there's

[70:24] um

[70:27] essentially two ways of doing this. Um

[70:30] one is a token threshold. So you limit

[70:35] uh the token threshold. Uh so you can

[70:37] say I'm I'm only going to use up to 200k

[70:39] tokens. Once I go over 200k tokens, I'm

[70:42] I'm going to compact the context.

[70:45] Another thing is um like when you get

[70:48] forced to do that by the provider. Um so

[70:50] that's kind of like a hard limit on the

[70:51] number of tokens you can have. Um

[70:53] finally, you can also have a manual

[70:55] request. And so uh a lot of uh kind of

[70:58] coding agent toolkits for instance have

[71:00] a slashcompact

[71:02] uh like command that you can use to

[71:05] compact the context.

[71:08] Um then based on that uh you'll select

[71:11] you might protect the beginning and keep

[71:12] the recent tail and compact the older

[71:14] region. Um replace it with a summary. Um

[71:17] that summary can be a structured

[71:19] summary. So sometimes uh they require a

[71:23] tool call uh that says this and this and

[71:26] this and this must be in the compaction

[71:27] summary. Sometimes it's just free text.

[71:30] Um there's also uh

[71:34] I think this is only open AI uh

[71:36] possibly. But basically they um they

[71:38] compact into

[71:41] something encrypted uh that you cannot

[71:43] read. So you can't see how they're

[71:45] compacting because they don't want you

[71:46] to steal their uh their precious

[71:48] compaction algorithm. Uh so uh so

[71:51] there's that.

[71:53] Um and then uh yeah, you can you can

[71:57] keep on on working on that.

[71:59] Um

[72:01] so

[72:03] one of the risks here is uh sometimes

[72:06] you can compact over and over and over

[72:08] again and the first time it works uh but

[72:10] as you walk through more um you uh you

[72:14] end up losing more and more. So again

[72:16] this is one of the reasons why people

[72:18] don't like compaction because it can

[72:19] cause the agent to go off the rails.

[72:22] Um so uh ba basically the way we

[72:26] evaluate this is typically in a holistic

[72:28] state. So you can vary the compaction

[72:30] algorithm and evaluate it against

[72:32] whatever benchmarks you're evaluating

[72:33] against. I would like to warn you uh

[72:37] about this. I have a a kind of like

[72:40] story from when we were first developing

[72:42] open hands which is um we actually I

[72:45] think made one of the first like

[72:48] production grade uh compaction

[72:51] algorithms. We called it compression

[72:53] then um and we evaluated it against

[72:56] bbench which is a very common you know

[72:58] benchmark for for coding agents and we

[73:01] worked pretty hard on it like as a

[73:03] research project for about a month or

[73:04] something like that and we were like we

[73:06] found this great compaction strategy. It

[73:08] doesn't reduce our score at all. it's

[73:09] saving us a lot of tokens. And then we

[73:12] actually tried it in our um we tried it

[73:15] in our our system and it made these

[73:18] really silly mistakes like um sending a

[73:21] pull request every time it compacted. So

[73:24] it forgot that it had sent a pull

[73:25] request to GitHub. And so uh you know we

[73:29] would get five pull requests for the

[73:30] same functionality because it had

[73:33] forgotten. Um or you know it would

[73:36] forget

[73:38] user instructions that were sent in the

[73:42] middle of the conversation because we

[73:44] had only evaluated on single turn

[73:46] conversations that had a single user

[73:48] message and we were compacting away the

[73:50] multiple user messages. So it's not just

[73:53] good enough to benchmark uh unless you

[73:55] have really really robust benchmarks

[73:57] that represent every use case. You kind

[73:59] of need to test them in the wild as

[74:00] well.

[74:03] Cool. Um so we're we're getting close to

[74:06] time. Uh but yeah, basically uh what I

[74:08] covered today is uh you know agent loops

[74:10] grow very quickly. Uh we have a lot of

[74:13] inference challenges in doing so. uh we

[74:16] can handle uh efficiency problems

[74:18] through architectures and um and caching

[74:22] and uh compaction is kind of the way we

[74:24] handle this uh once we expand beyond the

[74:27] level that we can handle. So um that's

[74:31] all I have. Uh if there is any questions

[74:34] happy to happy to cover them and next

[74:36] time we're going to be talking about

[74:37] skills and memory. So this is like even

[74:39] longer context over your entire uh your

[74:42] entire time. Um, are there any questions

[74:44] before we all uh all leave or

[74:48] >> Yeah.

[74:52] >> Yeah, great question. Um, the question

[74:55] was, do we consider sub agents as a way

[74:57] to manage context? And yes, but we're

[74:59] going to talk about sub aents later, so

[75:00] I didn't cover them this time. Yeah.
