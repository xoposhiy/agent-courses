# Lecture 6 recording

[Course index](../../README.md) · [Original source](https://www.youtube.com/watch?v=1BWeH1oOM7k&list=PLSN0qpDfUvTM&index=6) · [Raw file](../../raw/videos/1BWeH1oOM7k.json)

Retrieved: 2026-11-13T16:48:29.623203+00:00

[00:00] Okay. Um, today I'll I'll be talking

[00:02] about agents for coding and software

[00:04] development.

[00:06] So, presumably many or mo most or all uh

[00:10] people here are using coding agents. So,

[00:13] um I I barely need to describe what

[00:16] their underlying functionality is. Um

[00:19] but I would like to talk about um how we

[00:24] can build coding agents and what the

[00:26] necessary things we need to have in

[00:28] order to build coding agents are. And um

[00:32] actually I just realized that the title

[00:33] of this slide is uh maybe uh a little

[00:37] bit of a misnomer. The first thing that

[00:39] I'd like to talk about is what it means

[00:41] to have a language model. Not a not an

[00:43] agent, but a language model that's able

[00:44] to write code. Um, and so

[00:49] there's different uh things you can do.

[00:51] The kind of obvious thing is you say in

[00:54] English um I want you to write a program

[00:57] that uh visualizes this data for me. Um

[01:02] and you give it like a CSV uh file in

[01:05] your prompt and uh creates a bar chart

[01:09] uh for this data. Um, how many people do

[01:12] this sort of query like frequently?

[01:18] Doesn't necessarily need to be a bar

[01:19] chart, but like write write this program

[01:21] for me to do this task.

[01:24] Probably a lot of people uh and you

[01:27] write it in like chat GPT or a coding

[01:29] agent or something like that. Um,

[01:32] however, there's a lot of other tasks

[01:33] that involve generating code that's not

[01:35] just like a oneoff like prompt, but you

[01:40] can also do um you can uh have it modify

[01:45] repositories. So, you can have it modify

[01:47] like multiple files. Um, and so this

[01:50] would be something more like in this

[01:52] repository

[01:53] uh fix this issue or make this

[01:55] improvement or something like that.

[01:58] And then finally, actually developing

[02:01] software is not just writing code and

[02:04] implementing fixing issues and

[02:05] implementing features, but there's also

[02:07] a lot of other stuff involved. So I'd

[02:08] like to talk about some of that other

[02:09] stuff as well.

[02:13] And of course uh like all of our other

[02:16] agents, this will involve us uh writing

[02:20] prompts,

[02:22] providing tools to the agent, and uh

[02:25] having a good LM that's able to solve

[02:27] these tasks. I'm mostly in this lecture

[02:30] going to focus on the second and third

[02:33] parts of this. And the reason why is

[02:35] because we spent the last two lectures

[02:37] talking about like skills and memory uh

[02:40] and you know how we incorporate long

[02:42] context. And so for the prompting I I

[02:45] think many of the things were already

[02:48] covered in the previous lecture.

[02:53] So the first element that we have here

[02:56] is a large language model that has the

[02:59] ability to write code.

[03:02] And so the example is writing code. Uh

[03:07] in order to write code from a prompt,

[03:09] you uh essentially need to be able to

[03:11] cover a few things. Um and sorry, just

[03:15] to clarify, this is this is single step

[03:16] at the moment. It's not agentic codew

[03:18] writing. It's singlestep uh language

[03:20] models. And so in order to have the

[03:24] ability to write code in a single step,

[03:26] you need to be able to understand the

[03:27] language uh the programming language

[03:29] that you're going to be writing in.

[03:31] Another very very important uh topic is

[03:34] editing because usually we don't write

[03:38] code once and then throw it away

[03:40] although we do do that sometimes.

[03:41] Usually we like iteratively improve and

[03:44] that is not something that comes for

[03:46] free from language models. you need to

[03:47] train it into the model. And then the

[03:50] final thing is reasoning. And coding has

[03:54] been one of the more successful

[03:56] applications of reasoning models uh just

[03:58] because um like math which is another uh

[04:01] successful application of reasoning

[04:03] models. You uh can easily verify or at

[04:07] least somewhat easily verify that you

[04:09] did a good job of it. So uh these are

[04:11] the the three things

[04:13] that I'd like to cover.

[04:17] So

[04:19] when you're training recently every

[04:21] language model is a coding model. Um so

[04:25] there there are no language models that

[04:27] don't know how to write code. And the

[04:29] reason why is because coding is one of

[04:30] the most valuable and like widely used

[04:33] use cases for language models, but it's

[04:35] not something you get for free. Um, so

[04:37] may maybe before I go into the like the

[04:39] actual content, what sorts of things do

[04:42] you think are necessary to train a model

[04:46] that is good for uh generating code? Not

[04:49] necessarily for agentic tasks first, but

[04:51] like what what sorts of things do you

[04:52] think you might need to do?

[04:55] >> Any ideas? Yeah.

[04:56] >> First of all,

[05:01] tokens must

[05:04] >> Okay. Yeah. all the tokens uh must

[05:06] exist. Uh so what what are what are the

[05:10] some tokens that must exist for code

[05:11] that wouldn't necessarily need to exist

[05:13] for non-code models.

[05:26] [laughter]

[05:27] >> Yeah. So um there's uh I'll give a few

[05:30] examples of of what these tokens look

[05:32] like. Um any any other things that you

[05:34] might need to do? Um but like sorry just

[05:36] to to summarize. So uh you need to make

[05:39] sure your tokens have the tokens that

[05:41] are going to appear in code. Yeah.

[05:43] >> You just need like a lot of coding.

[05:45] >> You need a lot of coding data to train

[05:46] on. Yeah. Um and so where where would

[05:48] you get that?

[05:50] >> GitHub.

[05:51] >> GitHub. Sure. Okay. Cool. Um any any

[05:55] other ideas? Yeah. For coding there's

[05:57] like special tools like all the

[06:01] OS related

[06:03] >> for coding there's special tools like GP

[06:05] and OS related tools. So yes this is uh

[06:08] very important. Um so that's more

[06:14] that's maybe more important on the

[06:16] agentic side once you start creating an

[06:18] agent that actually like moves around

[06:20] the codebase. But if you were writing

[06:21] bash scripts for instance, you

[06:23] definitely need to know know about those

[06:24] even as in a single step setting. So um

[06:28] yeah, these these are all great points.

[06:30] Uh so pre-training um you need to

[06:32] pre-train on a large corpus. It needs to

[06:35] include code, but it can't be only code

[06:36] because you also need it to understand

[06:38] English or whatever language you're

[06:40] quering in it uh it in. As well, um you

[06:43] need to make sure the tokenization's

[06:45] right, which I'm going to talk about in

[06:46] a bit. Um the next thing uh is

[06:51] mid-training. And I'm going to talk

[06:53] about mid-training and supervised

[06:54] fine-tuning as kind of being the uh the

[06:58] same or mid-training or continual

[07:01] pre-training or supervised fine-tuning

[07:03] is all being part of this step. Um in

[07:06] here you need to train on code mixtures.

[07:08] Another really important thing for

[07:09] coding models is to be able to handle

[07:11] long contexts because you want to pull

[07:13] in lots of context from throughout the

[07:15] codebase. And then uh another thing is

[07:18] uh RL post training. And of course we're

[07:21] going to be talking about uh each of

[07:22] these in more detail later with respect

[07:24] to the specific mechanics of how we

[07:26] train these models. So I want to mostly

[07:29] focus on uh kind of like the coding

[07:31] specific details in this uh task and uh

[07:34] leave the overall

[07:37] overview of how you do supervised

[07:39] fine-tuning or RL postraining for later.

[07:42] So pre-training this is basically we

[07:45] need to learn from code and text and of

[07:49] course we're just optimizing next token

[07:51] prediction at this stage typically as is

[07:53] shown in the equation.

[07:55] So when you're training a coding model

[07:58] in contrast to training a model that

[08:00] only needs to answer questions you want

[08:03] to mix web text of course because every

[08:06] model learns from web text but also

[08:09] technical pros. So this could be

[08:11] explanations of how code works.

[08:15] Uh things like math for improving

[08:18] logical reasoning abilities, source

[08:20] code, documentation, uh many many

[08:22] sources.

[08:25] Another thing, this is before probably

[08:28] any of you started working on language

[08:30] models, but there was a time when we

[08:34] normalized whites space. Uh so basically

[08:38] we would take all of the spaces and like

[08:41] drop them down to a single space or

[08:43] something like that. That would be

[08:45] really bad if you're programming in

[08:46] Python, right? Because whites space is

[08:48] meaning bearing. So you need to be

[08:50] careful about these sorts of things. You

[08:52] also need to be careful about file

[08:54] boundaries and how you express file

[08:55] boundaries. You need to be able to have

[08:58] uh APIs and you need to be able to

[09:01] preserve text and code relationships.

[09:03] Like if you have a markdown uh block

[09:05] within text, you want to make sure it

[09:07] remains in a markdown block.

[09:10] And of course, you will be evaluating

[09:13] while you're doing training. Typically,

[09:14] you'll do this just on a held out loss

[09:17] uh on

[09:20] coding tasks, but uh you need to shape

[09:24] your evaluation so that it covers uh the

[09:27] sorts of things that you want to cover.

[09:31] So choosing and cleaning data is hard

[09:34] when you're training a textbased model.

[09:36] It's even harder when you're training a

[09:38] coding model because code is very

[09:43] uh unique in its distribution.

[09:46] So the first thing you need to do is uh

[09:49] filter by language and source. There is

[09:53] a lot of code online that's completely

[09:55] autogenerated and so it's like less

[09:57] interesting from the point of view of

[09:59] you wanting to train on it. So you can

[10:01] remove that sort of code. Um you can

[10:04] remove things that are in wrong

[10:05] encodings uh and low value repeated

[10:09] codes. So um one example of this is

[10:13] forks or vendored libraries or nearly

[10:16] identical files or copied solutions. So

[10:19] if you look online on GitHub, there are

[10:23] thousands to uh tens of thousands,

[10:26] hundreds of thousands of forks. And so

[10:29] if you just download them and use them

[10:30] as is, then you'll have lots of uh lots

[10:33] of trouble. Oh, sorry. Uh also

[10:35] mentioning this is tiny down here, but

[10:37] I'm taking a lot of this from a paper

[10:39] called Start Coder, which was uh one of

[10:41] the first coders on uh one of the first

[10:44] papers on pre-training models to be good

[10:46] at coding tasks. So if you're interested

[10:48] in all of these details, you can you can

[10:50] take a closer look at that. And I

[10:51] believe Daniel uh you were involved in

[10:54] this. So you can ask Daniel for more uh

[10:56] more details.

[10:58] Um another interesting thing that people

[11:02] uh think about in some cases don't think

[11:04] about things in other cases is recording

[11:07] licenses and uh source dates and optouts

[11:11] and uh sensitive data filtering. So just

[11:14] to give some examples,

[11:16] if you train on code that's in a

[11:18] proprietary license

[11:21] and then release the model and then

[11:25] make a billion dollars on this model,

[11:28] the people who have the proprietary

[11:29] license are going to come around two

[11:30] years later and say, "Hey, you trained

[11:32] on my code. Give me

[11:35] a hundred million because my code is

[11:37] contributing to your model." And you

[11:39] might not want that to happen. Um or you

[11:42] might not care. But you need to decide

[11:44] [laughter]

[11:45] u

[11:47] uh actually US copyright law is a little

[11:49] bit vague about you know uh whe whether

[11:51] you should care about that or not. Um uh

[11:54] source states so if you don't want a

[11:55] whole bunch of old code you might want

[11:56] only new code. Um you can allow people

[12:00] the ability to opt out. also uh

[12:02] sensitive data. Um people upload all

[12:05] kinds of things they should not be

[12:06] uploading uh like their uh API keys

[12:09] which nobody in this class will do,

[12:12] right? Uh please please do not push your

[12:15] API keys to the repository but you know

[12:17] people do this. Um,

[12:20] and I there are tools that allow you to

[12:23] do this sensitive data filtering like I

[12:26] uh I and hugging face use one called

[12:28] truffle hog uh which is uh one that

[12:31] basically identifies all these uh API

[12:33] keys

[12:35] and then uh if you want to build a a

[12:37] training set or a test set you'll uh

[12:39] want to build a training set or a test

[12:40] set

[12:42] but this is also very difficult because

[12:44] of forks and all of the other problems

[12:45] you deal with. So um moving on to the

[12:49] next thing which is tokens. Uh this is

[12:51] something that uh you know kind of

[12:54] needed to evolve as code became more

[12:56] important. But basically

[12:59] uh here I wrote bite level BP on code

[13:02] and pros. But BP is basically just any

[13:04] subword tokenization method. Um I think

[13:07] maybe most people would be familiar with

[13:09] uh with BPE but you can uh

[13:13] substitute in anyone you want. Um the

[13:18] uh thing that you need to be careful

[13:20] about is preserving uh whites space

[13:24] and also uh compressing very frequent

[13:27] things. So up until we started working

[13:30] on code a lot whites space might be like

[13:33] one token. So that would mean that you

[13:35] would if you're generating uh 16

[13:39] indented you know Python code you would

[13:41] have 16 spaces or something like that.

[13:44] And so typically uh what it looks like

[13:48] is it would be um you know compressed

[13:50] into like three spaces and a a return in

[13:54] like a single token. So you start uh

[13:58] tokenizing specifically in a way that's

[14:00] useful for code.

[14:03] Another thing you can do but don't

[14:05] necessarily need to do is um like

[14:08] normalize the code so it becomes in a

[14:09] more normal uh more standard uh setting

[14:12] but uh you you don't necessarily need to

[14:15] do that.

[14:16] So

[14:18] another thing you need to think about is

[14:21] the languages that you want to handle.

[14:24] And so Starcoder uh they took the

[14:26] approach of modeling all the languages

[14:29] or modeling not all the languages but a

[14:32] lot of very popular languages and kind

[14:35] of necessarily the ones that had more

[14:37] training data ended up being better at

[14:39] particular tasks. Another uh other

[14:42] things that you need to be

[14:45] aware of are you know like what

[14:47] languages will the users want to be

[14:49] using and also what languages are easier

[14:51] to write um or supported by you know

[14:56] whatever agentic framework you're using.

[14:58] So for instance, if you ask a model to

[15:03] do something and like you don't specify

[15:07] the language, what language will it it

[15:10] use? Like have you ever said code me up

[15:13] an app to do X? What language will it

[15:16] use for that? Yeah,

[15:18] >> mostly Python. Yeah, I think mostly

[15:20] Python. What uh has anybody seen any

[15:24] other contrary things?

[15:27] typically react. [clears throat]

[15:31] >> Yeah, exactly. So, if you if you ask for

[15:33] like a dashboard, it will do React. If

[15:35] you ask for just about anything else, it

[15:37] will do Python. Um, and of course, you

[15:39] can specify something else. Um, I I had

[15:42] a heavy data processing pipeline uh that

[15:46] I originally wrote in Python and I asked

[15:50] the model to convert it to Rust to make

[15:52] it faster. And so the model did that but

[15:55] then every time it ran another program

[15:57] it ran it again in Python. So [laughter]

[15:59] like I had to say in rust in rust in

[16:02] rust in rust every time until finally it

[16:04] did it. So they have these very strong

[16:06] biases. Um I think the biases are built

[16:11] in for two for two reasons. One is ease

[16:13] of writing the language. So, Python is

[16:15] like relatively concise and easy to

[16:16] write. Popularity and then also like

[16:19] downstream uh what was the model RL

[16:22] trained on? And it was probably RL

[16:25] trained with like a Python interpreter.

[16:27] So, it it's more uh favoring that

[16:30] language.

[16:32] Cool. Any questions about pre-training?

[16:35] >> Yeah.

[16:36] >> Is there a situation where you want to

[16:38] augment your tokenizer specified

[16:42] like space for example? a separate token

[16:46] so that it's easier for the model to

[16:48] internally separate like language tokens

[16:52] and coding tokens even though they're

[16:54] like the same.

[16:56] >> Yeah. Yeah. So this is a great question.

[16:58] I mean like it it does have return space

[17:00] face in here in the example. But um one

[17:04] one interesting thing is um you actually

[17:08] don't need to treat whites space any

[17:09] differently than every other token. um

[17:11] bite pair encoding is like literally

[17:13] meant to merge together bytes. Um and so

[17:18] however in almost all of the cases

[17:20] people do treat whites space

[17:21] differently. Um and so the reason why is

[17:24] because like let's say the model is

[17:27] performing a little bit poorly. It's

[17:28] very weird for it to put out a partial

[17:30] word. And so they want to like

[17:33] essentially bias the model so that it's

[17:35] not outputting like partial words or

[17:37] partial word tokens. And so um typically

[17:42] they will tokenize whites space

[17:44] separately and non-white space

[17:46] separately. But um there are also kind

[17:50] of exceptions to that.

[17:51] >> Yeah.

[17:52] >> Yeah. You can get a more efficient like

[17:54] representation in particular for code if

[17:57] you like tokens across space. So in the

[18:00] encoder paper we did that um you can get

[18:03] like 40% tokens but it can also break

[18:07] things in weird ways like said so like

[18:10] import nump numpy as np would be one

[18:13] token but like the model wouldn't be

[18:15] able to

[18:17] stop like import numpy as you have to

[18:22] like back off and do like

[18:25] and you also have to be really careful

[18:27] if you change your tokenizer can break

[18:29] at scale and you have to be a little bit

[18:32] smart about how you do it. There's some

[18:34] papers on that we can share.

[18:37] >> Yeah. So, so just to um repeat basically

[18:41] uh you can the two of the main points

[18:44] were like you can get a much more

[18:48] compact tokenization if you actually

[18:50] allow it to just tokenize

[18:53] indiscriminately regardless of whites

[18:55] space or not. Um but it can break things

[18:57] in weird ways. So like if you write

[18:59] import numpy is np that could become

[19:01] like a single token in your your code

[19:03] model but then you'd have trouble like

[19:06] doing autocomplete or something like

[19:07] that because it's too long. So, um,

[19:10] cool. Any any other things?

[19:15] Okay. So, uh, now I'd like to go into

[19:18] mid training. And, uh, I have a few

[19:21] examples here. One is from Code Lama.

[19:23] Another one is from, uh, Quen Coder. And

[19:26] so, these are, uh, public papers that

[19:29] explain how they take a previously

[19:31] trained non-code model and adapt it to

[19:34] being a coding model. So this kind of is

[19:37] good for highlighting the uh the

[19:39] difference between a co a non-coding

[19:41] model and a coding model. So um the

[19:44] first thing that you can do is you can

[19:45] increase code exposure. So if you start

[19:47] off with a much uh you know more

[19:50] heterogeneous data set you can increase

[19:52] the exposure of code. Um you could also

[19:55] choose the mixture empirically uh to try

[19:58] to get code gains and uh maintain

[20:01] general capability

[20:03] and um so for example in code llama they

[20:07] took llama 2 and then did 500 billion

[20:09] additional tokens uh for the the

[20:12] additional models and uh there context

[20:16] extension is also uh important here. So

[20:20] here's one empirical uh result from Quen

[20:23] 2.5 coder where basically they said this

[20:26] is a coding model and we're going to

[20:28] make it really good at code and so we'll

[20:31] just add 100% code and and train on 100%

[20:34] code afterwards. But the problem was it

[20:36] got uh quite poor scores on uh other

[20:40] important tasks like math or question

[20:42] answering. Um but if they continued

[20:45] training with not 100% code but but also

[20:48] text and math they were able to have

[20:50] like a tiny drop in the coding

[20:53] performance while maintaining other

[20:54] performance. And this is obviously

[20:56] possible or important because uh you

[20:59] know like nobody's going to use a model

[21:01] like just for coding uh nowadays.

[21:06] So another thing is long context

[21:08] handling. And I already kind of talked

[21:10] about long context handling a lot. So

[21:11] I'm just going to go into this uh in a

[21:13] previous class, but I'm just going to go

[21:15] into this in a little bit of detail. But

[21:19] you basically want to uh come up with

[21:24] coherent sequences

[21:26] of uh to train models on. So a very

[21:30] naive way to create data for a coding

[21:33] model is to say I'm just going to take

[21:35] this repo and I'm going to concatenate

[21:37] all the files together. But

[21:40] concatenating all the files together

[21:42] actually very often will exceed the long

[21:44] context of even the longest context

[21:46] models. Like you only train up to

[21:48] typically 1 million tokens and there's

[21:52] many code bases or like I'd say most

[21:55] reasonable code bases are more than 1

[21:56] million tokens. um like the Google monor

[22:00] repo is allegedly like billions of lines

[22:03] long, right? So that's not even on the

[22:06] same uh order of magnitude. And so but

[22:10] you would like to have a coherent file

[22:12] understanding. So you can do things like

[22:14] take everything in a directory or you

[22:17] can parse the dependency graph and

[22:19] follow the dependencies and concatenate

[22:21] together things that depend on each

[22:22] other. Uh that sort of thing.

[22:26] Um so Quen 2.5 coder just as an example

[22:30] it started training into 8K and then it

[22:32] extended uh up to 128K with yarn uh like

[22:36] like I talked about a couple classes

[22:38] ago. So this is also really important

[22:41] and this sort of context manipulation

[22:44] allows you to do that and you can

[22:47] validate it through tasks like cross

[22:49] file completion and infilling and short

[22:51] context retention which I'm going to

[22:53] talk about in a bit.

[22:57] So next I'll talk about infilling. I

[23:00] feel like actually I shouldn't talk

[23:01] about this because Daniel's the expert

[23:03] and this is mostly about his paper but I

[23:05] I will talk about it anyway and people

[23:06] can ask him questions. Um but he had a

[23:09] paper called encoder. Um it was one of

[23:12] the first papers on training strong

[23:16] coding models with an infilling

[23:18] objective so that they would be able to

[23:19] perform tasks that are not just code

[23:21] completion but also um kind of

[23:24] predicting the uh inner part of code.

[23:27] And so what this means is we get

[23:29] something like this is positive and we

[23:32] want to predict its return type um would

[23:34] be just one example of this. And so the

[23:38] problem is if you just look to the body

[23:40] to the the left in a normal auto

[23:42] reggressive model, you actually have no

[23:44] idea, right? Like there's no information

[23:47] about is positive. I mean, well, maybe

[23:49] you could guess bool from is positive,

[23:51] but it it could also be a string or

[23:53] whatever else or an enum. And so then if

[23:56] you look at this, you could uh you know,

[23:58] tell that it's actually the return type.

[24:03] So how do we do this? Uh the answer is

[24:06] surprisingly

[24:08] is that a question or no? Um okay. So I

[24:11] think the answer is uh surprisingly you

[24:14] know you can do surprisingly simple

[24:16] things to make this work which is

[24:17] basically you turn an infilling task

[24:20] into an auto reggressive task. And so

[24:23] you have like the prefix, you have the

[24:25] suffix and then you infill uh infill the

[24:28] span here. And so this m0 is essentially

[24:32] the the first uh like the first span

[24:36] that you infill and then this is uh that

[24:39] comes after m0 here. Um and so then at

[24:43] inference time you just do you put m0

[24:47] here between the prefix and the suffix

[24:50] and then you put m0 again and then it

[24:52] generates a span.

[24:54] So this also um generalizes to one or

[24:58] more holes. So like if you have multiple

[25:00] holes, you can have an M0 and an M1 and

[25:02] then generate M0 at first and then M1

[25:04] second. So this is a a general way that

[25:07] you can do any sort of infilling task.

[25:11] And this allows you to do all kinds of

[25:14] useful things uh from the point of view

[25:16] of software engineering. So you can

[25:18] complete code in the middle of a large

[25:20] file. You can infer types uh like I did

[25:23] for return types. You can generate

[25:25] comments, rename variables. All of these

[25:27] things are like instances of an

[25:29] infilling task.

[25:33] And here are some of the experimental

[25:35] results from the paper. So

[25:38] there are uh basically left to right

[25:41] inference on uh a number of tasks that

[25:43] they evaluated on single lines and

[25:45] multiple lines was like 48 to 24 uh and

[25:48] 25. Um if you did left to right with 10

[25:51] candidates and reranked them uh using uh

[25:55] the context from the whole file, you

[25:57] would uh get do better uh but still uh

[26:00] would not achieve nearly the improvement

[26:04] of training a model to do this. And this

[26:06] is you know not requiring any reranking

[26:09] at all. That's just uh using the um the

[26:12] infilling based inference

[26:15] and uh you can demonstrate that uh you

[26:18] can train with infilling but still

[26:20] maintain uh standard code completion.

[26:22] And so uh if you did causal masking

[26:25] where you basically uh you know masked

[26:28] the the left to right they still were

[26:30] able to maintain performance. So it's

[26:32] not like really a trade-off between the

[26:34] two.

[26:38] Um, any any questions here or any

[26:40] follow-up comments?

[26:41] >> Yeah.

[26:49] >> Yeah. You apply like a a random

[26:53] selection of like

[26:56] kind of like a long tail distribution.

[26:58] So the majority of the time you're just

[27:00] doing one, but you could do up to I

[27:02] think like 100

[27:05] chance. And then for each one of those

[27:07] you like sample

[27:09] and those are like

[27:11] you just

[27:14] replace

[27:16] the model

[27:18] >> and so the model doesn't predict the

[27:21] mass.

[27:24] >> Okay. So I I'll repeat that for the back

[27:26] but basically um the question was how do

[27:29] you decide how many spans and how big

[27:30] the spans are to sample and the answer

[27:33] was basically you use a longtail

[27:34] distribution so that uh you're doing one

[27:37] most of the time but then you do two

[27:38] some of the time three less of the time

[27:41] uh and and similarly for the uh the

[27:43] length of the outputs and you could

[27:45] probably model that after the infills

[27:47] that you actually see in real life uh if

[27:50] like you wanted to do that. So

[27:51] >> yeah let me just count on scale. Yeah,

[27:55] cool. Okay, so this is one example of an

[27:59] important uh thing that you can do uh

[28:01] for code in filling. Um but you can

[28:04] actually become very creative in

[28:06] learning from code.

[28:08] So there's a bunch of different sources.

[28:11] So, um, you can use commit diffs. And

[28:14] so, if you have the before,

[28:18] uh, if you have the files before the

[28:21] diff and a message, uh, like from a a

[28:25] pull request or something like that, you

[28:27] can then generate the diff or the after

[28:31] output. So, this would allow you to

[28:33] basically learn good code editing

[28:35] models. Um, another thing is learning

[28:38] from diagnostics.

[28:40] So, um, you can get broken code plus an

[28:44] error and generate, uh, repairs. So,

[28:48] does anyone have an idea of where you

[28:50] could get like a ton of this data, uh,

[28:52] nearly for free?

[28:52] >> Stack overflow.

[28:54] >> Stack Overflow uh, is is one good one.

[28:56] That's not the one I was thinking of,

[28:57] though. issues.

[28:58] >> GitHub issues uh maybe a little bit more

[29:01] uh

[29:03] >> yeah, GitHub pull requests uh is is

[29:05] good, but uh like

[29:09] uh if you're a software developer um

[29:12] where where do you see code break? Maybe

[29:13] in in GitHub or something tests. Yeah.

[29:16] So I I specifically was going to talk

[29:18] about continuous integration tests,

[29:20] which are the tests that run when you

[29:22] make a push to a repository or something

[29:24] like this. All of this history is

[29:27] included in GitHub and it's public and

[29:29] so you can see that a particular version

[29:31] of the code ran and generated an error

[29:33] and then a later version of the code

[29:35] eventually passed and got merged in. So

[29:37] this is a very rich uh version of this

[29:39] sort of test data that you don't need to

[29:42] um like generate yourself because

[29:44] generating it yourself would be would be

[29:46] painful.

[29:47] Um,

[29:50] of course, if you start running an

[29:52] agent, you can run an agent and generate

[29:54] the data. Uh, which is what I'll be

[29:55] talking about later. So, um, yeah, the

[30:00] tests is related to that. Um, another

[30:04] thing is execution traces. And so, this

[30:06] is kind of interesting. It's a little

[30:09] bit niche, but there uh you know it it's

[30:12] pretty cool, which is like you can see

[30:14] how the program actually acts by

[30:17] instrumenting it and running it at test

[30:19] time. And you could um for example ask

[30:23] the language model to generate this the

[30:26] stack at a particular point in in

[30:28] program execution or something like

[30:30] that. Um or generate the outputs at a

[30:32] particular point in program execution.

[30:34] And I'm going to talk a little bit about

[30:35] code world models at the very end of

[30:37] this talk which kind of relies on this.

[30:41] Cool.

[30:43] Um any any questions? Good.

[30:47] Okay. So next I'd like to talk about

[30:49] evaluating generated code. Um there's a

[30:52] few paradigms to do this. Um, one of the

[30:57] most obvious ways to do this, um, which

[31:00] actually, uh, we we did in a paper in

[31:03] 2017, I guess, is comparing with a

[31:05] reference solution. And so, um, what

[31:09] this means is you have a human generated

[31:11] output and you compare not the execution

[31:15] results, but you just say, is the

[31:18] machine generated code similar to the

[31:20] human generated code? And so a long time

[31:23] ago, uh, there was a famous metric

[31:26] called blue. Has anybody actually used

[31:28] this anymore?

[31:30] Oh, wow. I'm actually [laughter]

[31:33] surprised by how many people still know

[31:35] uh still know of this, but um there's a

[31:36] metric called blue, which is basically

[31:38] measuring uh token and engram overlap uh

[31:42] between the uh the output code. And so

[31:46] this is uh this would allow you to find

[31:49] code that looks similar on the surface,

[31:52] but the problem with this is that uh it

[31:57] um if you have like more than or equal,

[31:59] this is only one token different, but

[32:01] it's actually very different from the

[32:02] point of view of the behavior of the

[32:04] program. Um, and on the other hand,

[32:07] there's uh things with different

[32:09] expressions that look very different

[32:11] from the point of view of token overlap,

[32:13] but actually are uh are not different.

[32:17] So there's been a few ways to um

[32:20] essentially account for this. So one way

[32:23] of doing it is uh this metric called

[32:26] codeblue. And basically what it does is

[32:28] instead of comparing the surface level

[32:30] similarity uh from the point of view of

[32:32] tokens it compares the abstract syntax

[32:35] tree uh between the uh programs. So one

[32:38] feature of programs is every program can

[32:41] be turned into a tree uh that

[32:43] essentially specifies how uh the model

[32:46] you know exe or how the program will be

[32:49] executed uh according to the logic of

[32:51] the programming language. And so they um

[32:55] they compared based on the syntax tree

[32:57] and they also compared based on a

[32:59] syntactic data flow match um or semantic

[33:02] data flow match which is like which

[33:05] variables are uh kind of come from uh

[33:09] which place and and stuff like that.

[33:13] Um another way that you can compare code

[33:15] similarity is uh using embedding based

[33:18] methods. And so this is um something

[33:21] that we uh created in 2023 called code

[33:24] bert score. And the basic idea is that

[33:28] you uh would take code and this would be

[33:33] one example of uh code. This would be

[33:36] another example of code and you uh embed

[33:39] each token in the code. And then you uh

[33:42] check to make sure that each token has a

[33:44] good other token that corresponds to it

[33:46] in the uh in the other set of code. And

[33:49] this uh this allows you to tell like

[33:52] that all of the code is uh all of the

[33:56] code is essentially reflected um in the

[33:59] other implementation.

[34:04] So um these are good in the case um or

[34:10] actually sorry I'm going to talk about

[34:12] the trade-offs in a few slides. So um

[34:13] may maybe I'll just switch to the other

[34:15] paradigm of evaluating code and this is

[34:17] by far more popular nowadays. Um so

[34:21] nowadays the typical way of evaluating

[34:23] code is by actually running it. And so

[34:26] what you do is you have a candidate um a

[34:29] candidate output and then you have a

[34:31] bunch of test cases and based on the

[34:34] candidate output you run the test cases

[34:37] and um you evaluate and if it passes all

[34:40] the test cases you get a score of one.

[34:42] If it doesn't pass all the test cases

[34:44] you you get a score of zero.

[34:48] Um so each of these have uh benefits and

[34:52] disadvantages. So if you look at the

[34:53] execution checks um the benefit of

[34:57] execution uh executionbased evaluation

[35:01] is that this can accept different

[35:03] correct implementations.

[35:05] The disadvantage is this is really hard

[35:09] to create really good unit tests. And

[35:12] for every famous benchmark that you will

[35:15] find, um there is a paper complaining

[35:18] about how bad the unit tests are and uh

[35:21] saying that they either have false

[35:23] positives uh from the point of view of

[35:26] um allowing incorrect implementations

[35:29] because the tests are not rigorous

[35:30] enough or false negatives which is that

[35:33] the input

[35:36] to the model is um the input given to

[35:40] the agent is not enough to pass all all

[35:43] of the unit tests. And just to give an

[35:45] example of this, um it might say I want

[35:49] a uh I want a nice button on the top

[35:53] right of my interface that uh says learn

[35:57] more or something like that. And that

[36:00] might be great, but the test might also

[36:02] be checking the background color of the

[36:04] the button or something. Um because

[36:06] that's a requirement that wasn't obvious

[36:08] right at the very beginning of the test,

[36:09] but became obvious later. So th this is

[36:12] like the problem uh it's like one of the

[36:15] biggest problems in uh training coding

[36:17] agents nowadays uh because we move we're

[36:20] moving to more and more difficult tasks

[36:22] and um creating tests that both have low

[36:26] false positives and low false negatives

[36:28] is is very hard.

[36:31] Um

[36:33] so the uh the advantage another

[36:37] advantage is detecting semantic errors

[36:40] through uh execution is good but this

[36:43] needs um a

[36:47] essentially good tests dependencies in

[36:50] an isolated environment

[36:52] and uh so for instance um if you need to

[36:57] run the tests it's easy if you're just

[36:59] using the Python standard library but if

[37:01] not you need to install all the

[37:02] dependencies beforehand. Um and so the

[37:06] typical way we do this is we have

[37:08] something like a docker container uh

[37:10] which installs all of the dependencies.

[37:13] Um but you might think you have

[37:15] installed all the dependencies but then

[37:16] you didn't think about the versions of

[37:19] the libraries that you're using. And so

[37:21] the versions get upgraded the tests die.

[37:25] um and uh you're you're giving a newer

[37:28] model a lower score just because the

[37:30] tests are like out of date. So uh this

[37:33] is another another problem we have to

[37:34] deal with. And then the final thing is

[37:37] um you need a stable execution

[37:40] environment in time. And so running the

[37:42] tests for a very big repository can

[37:44] actually be very time consuming. And in

[37:47] a lot of the benchmarks uh that we deal

[37:49] with uh including Sweetbench which I'll

[37:51] talk about in a moment um they you know

[37:53] have come up with ways to fix this but

[37:55] it it's definitely a uh a difficulty.

[38:02] Cool.

[38:04] Um so ju just to give some ideas of

[38:07] benchmarks that are popular in uh like

[38:11] singlestep code generation. Um human

[38:13] develop

[38:25] string and um you need to generate a

[38:29] completion uh and there are hidden unit

[38:31] tests. So, uh, this was actually, I

[38:34] think, just manually created by people

[38:36] at OpenAI. Um, so they came up with a

[38:39] bunch of like kind of tricky Python, uh,

[38:42] functions, uh, to implement. And so it's

[38:45] not necessarily reflective of real world

[38:47] usage. Um,

[38:50] one that's a little bit harder is one

[38:53] called code contests. And basically,

[38:55] this is like code forces uh style uh

[38:58] like more competitive programming

[39:00] things. And there's a bunch of a bunch

[39:03] of other evaluation benchmarks, but they

[39:05] go from kind of like simple to to more

[39:07] complex ones.

[39:20] on the fir on their first attempt can

[39:22] solve a code forces problem with no

[39:24] mistakes and get it 100% correct. But

[39:27] that's kind of what we're asking

[39:28] singlestep language models to do here.

[39:30] And so uh this is actually a pretty

[39:32] pretty difficult task and it requires

[39:35] extensive reasoning.

[39:38] Um so uh this is an example of something

[39:43] from uh a paper from 2021 that

[39:48] introduced humanl

[39:50] and everybody if you know what codeex is

[39:53] nowadays you'll be very confused by the

[39:56] fact that this is also called codeex um

[39:58] but this was the original code

[40:00] completion model that was implemented

[40:02] for uh github in 2021 and basically Um

[40:07] here what they're doing is they are

[40:10] evaluating

[40:11] um

[40:13] how uh how much basically the model

[40:16] passes and so uh you can see that as

[40:20] they scaled up the model the model

[40:22] passed more um at one and what pass one

[40:25] means is you get to generate a single

[40:27] output and that passes but it's also

[40:30] common to report like pass k uh which is

[40:33] like if you generate uh if you generate

[40:36] five outputs. Um, is any one of those

[40:39] correct? And so that's like a slightly

[40:41] more lenient metric that you can

[40:43] evaluate as well.

[40:46] >> Cool. Uh, any questions here?

[40:51] >> Yeah.

[40:58] >> How is code efficiency or complexity

[41:00] factored into training? You read my

[41:02] mind. Uh, thank you. Thank you for

[41:05] introducing my next slide for me. So um

[41:07] the answer is coding efficiency is

[41:12] for non-agentic tasks was mostly not

[41:15] factored into training. Um they mostly

[41:19] did not uh did not consider whether it

[41:21] was faster code or slower code. They

[41:24] mostly just considered whether it was

[41:25] right code. Um there are a few uh

[41:29] exceptions to this. Uh one of them is uh

[41:32] this uh paper no fun of um and the uh

[41:40] the existing um basically the idea here

[41:43] is that you don't just evaluate

[41:45] um like functional requirements which

[41:48] are like that it does the thing it's

[41:50] supposed to do correctly. But you also

[41:52] do um uh runtime things like runtime

[41:55] efficiency uh latency or resource use

[41:58] and maintainability and security um uh

[42:01] based on things like static checks. So

[42:04] there is work to evaluate uh this other

[42:06] stuff as well. For agentic tasks it's uh

[42:09] more common to consider efficiency and I

[42:11] I'll talk about that in a bit.

[42:15] Cool.

[42:17] Okay. So um

[42:20] for singlestep code generation models uh

[42:25] a typical way to learn the models is

[42:28] through RL over the test results. So

[42:31] this is pretty straightforward uh from

[42:33] the point of view of RL tasks which is

[42:35] you just sample responses you run the

[42:38] tests over them and then you update the

[42:40] model. So nothing nothing too uh

[42:45] surprising here. Um but one really

[42:49] important thing is this allows you to

[42:50] train um large language mo uh train uh

[42:54] large reasoning models. So uh as I

[42:57] mentioned solving code forces in you

[43:00] know a single step is quite difficult

[43:02] and so it requires uh you to really

[43:04] think carefully about the uh response

[43:08] and reasoning models are very very

[43:10] helpful in doing this and so um this is

[43:13] uh possible uh possible to do. So like

[43:16] one hint of worrying about efficiency is

[43:18] like if you're doing a code forces thing

[43:20] a lot of competitive coding tasks give

[43:22] you a execution timeout and so like if

[43:25] you go over the execution timeout

[43:27] basically um you won't get uh you won't

[43:29] get any score for it but um yeah that

[43:33] that's uh basically the method that you

[43:35] can use here

[43:38] and um you you can show that this

[43:40] reinforcement learning uh style thing

[43:43] after mid-training can uh you know

[43:46] further improve your uh further improve

[43:50] your results. This is just one example

[43:52] from a paper called deep coder that you

[43:54] can look up. But basically um you know

[43:56] they trained for a while at 16k context

[43:59] uh trained uh for longer at 32k context

[44:02] and eventually um reported on uh like

[44:06] 64k context here.

[44:11] Cool. Um so yeah any any questions?

[44:16] >> Yeah

[44:20] >> is that to provide the single step model

[44:23] context to like code more efficiently

[44:25] for code or is that the reason because

[44:27] it was language model and then

[44:32] >> yeah that's a a great question. So um to

[44:35] repeat the question for the comments

[44:37] that are included in code why do I get

[44:39] you know comments in code when it's

[44:41] actually not necessary um you know to

[44:43] like solve the task.

[44:48] I only have hypothesis here because I I

[44:51] don't I'm not 100% sure about like the

[44:53] models that I use the most. You know

[44:55] what what GPD is doing or what what

[44:57] Claude is doing. Um, so I'd like to go

[45:00] back and and read a little bit more

[45:01] about this, but my guess is that um,

[45:05] number one, the models are trained on

[45:07] existing code and existing code has

[45:09] comments, so they'll fill them out.

[45:11] Number two, they are trained to do

[45:12] reasoning. And I feel like there's

[45:15] probably some implicit incentive to add

[45:18] more comments in your code to buy more

[45:20] tokens so that you can think about what

[45:21] to do next while you're generating the

[45:23] code. Um, so I think there might be an

[45:26] implicit incentive to get models to do

[45:28] comments. And then uh I'm certain now

[45:33] now nowadays

[45:34] uh maybe not like six months ago but now

[45:36] there's also some like non-functional

[45:39] you know classifier or like code quality

[45:42] model that they're incorporating uh that

[45:44] says uh write comments write an

[45:48] appropriate number of comments like not

[45:50] too many not too few because one of the

[45:51] big um complaints about previous coding

[45:55] models was that they would generate like

[45:56] a million comments that nobody would

[45:58] ever read and be super verbose. So, um I

[46:02] remember when uh the more recent version

[46:05] of Codex was released, one of the things

[46:07] they stressed was we will not give you a

[46:10] whole bunch of comment spam and we'll

[46:11] just do it concisely. So, yeah.

[46:22] >> Is there specific training methods for

[46:24] code quality that make it human

[46:25] readable? Um, I mean like I think the

[46:30] the obvious way of doing this is to come

[46:32] up with some model that you know judges

[46:35] code quality and add it to your reward

[46:36] during RL. I don't know of any details

[46:40] of this. Do do you know of any uh

[46:42] >> I think like when people do post

[46:44] training they'll often like collect

[46:46] readability as one particular judgement

[46:50] that

[46:52] >> so yeah okay

[46:54] >> so um to to repeat for the back like

[46:57] when you're doing post training um

[47:00] there's often a kind of like RLHF step

[47:03] where you train a reward model that

[47:04] predicts how good the output is and

[47:07] readability is one of the things that

[47:08] you can collect from human annotator

[47:10] ators and then that will be boosted in

[47:13] like indirectly through the reward.

[47:16] Cool. Um okay so I definitely like to

[47:19] cover aentic coding. So um this is uh

[47:23] the big difference between uh singlestep

[47:25] coding and agentic coding is that we um

[47:29] now are doing iterative tool calls uh

[47:32] like you know all agents and

[47:36] let let's first talk about the most

[47:38] common setting of uh either fixing bugs

[47:43] or implementing new features in GitHub

[47:46] repositories or in code repositories

[47:48] when you want to do something like this

[47:51] typically you uh you have three steps.

[47:54] Uh the first one is localize. Um so this

[47:57] is like if we are talking about uh

[48:03] sorry I think my my running example is

[48:07] now uh a long time ago but basically we

[48:09] had um we had an example of fixing some

[48:11] code uh so that the return value would

[48:14] be uh would be appropriate. And so um

[48:17] localize essentially here is trying to

[48:21] find the place that needs to be

[48:22] modified.

[48:24] Um then uh edit is uh changing the place

[48:29] that needs to be modified. So for

[48:30] example, if we're um setting a default

[48:33] only when the value is none. Um and then

[48:36] verify is checking that you actually did

[48:38] a good job. And then uh typically you

[48:42] will do this in a loop. So if you uh if

[48:45] you find that verification fails, you'll

[48:47] go back and iterate until uh everything

[48:49] passes.

[48:51] So yeah, here here's the the running

[48:53] example. Um so uh

[48:57] if you uh if your job is to find the

[49:00] place where uh retries is not defaulting

[49:03] appropriately when the value is zero, um

[49:07] you uh will first localize the

[49:09] implementation and reproduce the

[49:11] behavior.

[49:13] Um and so uh then you edit and so to uh

[49:19] fix the issues you will then go in and

[49:22] edit the code

[49:24] and then you verify by running all of

[49:26] the tests and if the tests fail uh then

[49:29] you use the failures to uh guide the

[49:32] next step uh that you're performing

[49:33] here.

[49:36] So this is agentic coding. Um and you

[49:40] basically put this in a loop uh using

[49:43] the tools that I'll talk about in a bit.

[49:45] Um I'd just like to point out there's

[49:47] one um alternative way that you could do

[49:50] repo level coding without any iterative

[49:53] agentic workflow. Um there was a paper

[49:57] uh called or there is a paper called

[49:58] agent list which is actually by uh

[50:01] Steven Sha a like new assistant

[50:03] professor here. But um basically what

[50:06] they did is um instead of

[50:12] having the agent be able to call call

[50:14] tools to do localization. It basically

[50:16] split it into a localization step where

[50:21] uh they would first localize um they

[50:24] first predict the files that need to be

[50:25] edited uh then predict the uh classes

[50:29] and functions that need to be edited and

[50:32] then pick specifically the lines that

[50:34] need to be edited. Then they would

[50:36] generate a patch um just using a

[50:39] singlestep language model. So this is an

[50:42] alternative. This was like for a short

[50:44] time like frustratingly effective

[50:48] because I I at this time was building

[50:50] coding agents and uh we saw quite a few

[50:53] language models where this workflow

[50:56] actually worked better than using a

[50:57] coding agent. And the reason why is

[50:59] because um the language models were

[51:02] trained very heavily to be good at like

[51:04] singlestep code resolution and they were

[51:06] not trained very heavily to be good at

[51:08] like agentic tool calling and uh and

[51:11] verification loops. Um

[51:15] and uh so yeah anyway this is an

[51:18] alternative way that you could solve

[51:19] repo level code generation but typically

[51:21] now everybody uh everybody uses agents.

[51:27] So how do you apply agents to this? Um

[51:30] one answer is you give the agent a

[51:33] single tool. Um the one tool that you

[51:36] give to an agent is uh the ability to

[51:39] run bash commands. And so this goes back

[51:41] to, you know, the comment before that

[51:43] being able to use bash commands is

[51:44] really important. And a mini suite agent

[51:48] is uh something that was created by uh

[51:52] the people who created SWUB um which is

[51:56] essentially an agent that only uses bash

[51:58] commands to to solve problems. And so

[52:02] this allows you to localize. So um the

[52:05] way you can localize is using uh things

[52:07] like gp or rip gp which is kind of a a

[52:10] more expressive version of gp um cat and

[52:14] find. Um if you want to edit files you

[52:17] can use things like said or you can run

[52:18] a python oneoff script you can use patch

[52:21] and then to execute checks you can use

[52:23] piest or build commands. So at least in

[52:26] theory this is all that you need to

[52:28] implement a coding agent. Um, can anyone

[52:32] think of some reasons why this might not

[52:33] be might not be ideal?

[52:41] >> Yeah.

[52:52] So, so the answer was there's only a

[52:55] limited number of tools like GDB and

[52:57] other uh and there's other tools like

[52:59] GDB, but you could just run GDB through

[53:02] the bash commands, right? So, like it

[53:05] just just to clarify, I'm not saying you

[53:06] only provide these tools to the agent.

[53:08] I'm saying you provide only one tool to

[53:10] the agent and it's a bash tool.

[53:14] >> Yeah.

[53:19] >> 85 90%. So if you make those explicit

[53:29] just

[53:33] >> Yeah, great uh great point. So um uh

[53:37] just to reiterate what the point was is

[53:40] um these will be most of the tool calls

[53:43] and if these are most of the tool calls

[53:45] if you encapsulate them into a more

[53:47] efficient tool the agent should be able

[53:49] to do a good job here. And so just to

[53:52] give an example if I want to edit files

[53:55] the the agent needs to think every time

[53:59] about whether it uses said or python or

[54:01] patch. Um whereas if you make a standard

[54:05] file editing tool that's specifically

[54:07] tailored to agents doing a good job at

[54:09] it um then it will just mostly rely on

[54:12] that file editing tool and it will get

[54:14] the file edits more correct. And so just

[54:18] to give an example this is what it would

[54:20] look like if you were running with said

[54:22] um and so

[54:26] uh that will you know match the line

[54:29] match the lines and stuff like this. But

[54:31] what if you needed to replace a thing

[54:33] that had lots of backslashes in it or

[54:35] something like that. Then you would be

[54:36] like backslashbackslash all the time.

[54:38] You need to get the number of

[54:38] backslashes exactly correct. Um and so

[54:42] there's just a number of of things that

[54:44] make uh bash not necessarily the best

[54:46] possible interface for um working uh

[54:49] with files for instance. And so the

[54:52] biggest change that most or maybe even

[54:54] all uh you know competitive coding

[54:57] agents use is they uh also add at least

[55:00] one tool for file editing.

[55:03] And so you can um either write a whole

[55:07] file or uh you can search and replace

[55:10] within the file. And typically these are

[55:14] implemented uh from the point of view of

[55:16] like having a tool that allows you to um

[55:18] to perform these operations in a like

[55:21] fixed format uh that the this tool uh

[55:24] uses.

[55:26] So

[55:28] um one one way that has been examined is

[55:32] a unified diff format. So basically you

[55:35] have um like the lines and the change

[55:39] that needs to be made. But um the

[55:41] problem with this is uh if you ask the

[55:44] agent to get the lines, it will mess up

[55:45] the lines all the time and like not

[55:47] apply uh properly. And so instead, uh,

[55:52] the most typical way of doing these

[55:53] things is, um, uh, you have something

[55:57] that looks a lot like a diff, but it's

[56:00] not, uh, it's not purely a diff or it

[56:04] doesn't specify line numbers. So, um,

[56:08] this is probably the most common way of

[56:10] doing it. It's done in a lot of, um,

[56:12] it's done in a lot of, uh, coding

[56:14] agents. Can anyone think of a downside

[56:16] of doing the right one instead of the

[56:18] left one? Any

[56:22] ideas of where this might fall apart?

[56:37] Yeah, exactly. So if there's multiple

[56:39] versions of retries equals 3 anywhere in

[56:42] the file, it won't match and then uh you

[56:46] you won't be able to disambiguate which

[56:48] one should be fixed. So basically what

[56:50] the coding agent needs to do in that

[56:51] case is it needs to write more lines

[56:52] until it becomes unambiguous. But the

[56:57] advantage of doing the thing on the

[56:58] right is much larger than that

[57:00] disadvantage. So almost all coding

[57:02] agents use this. Um

[57:05] so diff format can make a big difference

[57:08] and file editing tool format can make a

[57:10] big difference. Um this is an example

[57:12] from something called the uh the Ader

[57:15] code edit benchmark or code editing

[57:17] benchmark and uh basically it evaluated

[57:20] uh GPT4 Turbo which was a model at the

[57:23] time on uh comparing like search and

[57:26] replace and unified diff format and GPT4

[57:28] Turbo was just like a lot better at

[57:30] unified diff format because it had seen

[57:32] more of that in its training data. Um

[57:35] nowadays uh it's a little bit less

[57:38] prominent but it still is a thing. Like

[57:41] until very recently Gemini uh performed

[57:44] quite poorly on a number of harnesses

[57:46] because Gemini like Gemini was trained

[57:49] on its own edit format that was

[57:50] different than everybody else's and so

[57:52] it was not working well. I think they

[57:54] fixed it in the past like few months or

[57:57] something like this. But this can be a

[57:59] major major major bottleneck uh to

[58:01] getting agents to work well if it's not

[58:03] done properly.

[58:06] Cool. Uh any questions here?

[58:11] Okay. Um so the next thing is finding

[58:15] relevant code. So you start with uh

[58:19] searching for you know whatever

[58:22] information you have. So uh rip gpap is

[58:27] the most uh you know popular tool for uh

[58:30] for doing this but you can also search

[58:33] with uh grap or you know a dedicated

[58:36] code search tool

[58:39] and uh then you follow the values and uh

[58:41] the agent goes and fixes things.

[58:44] There's also more complex methods that

[58:47] people have examined with respect to

[58:49] code localization.

[58:51] And so uh just to give one example, this

[58:54] is a paper called LOK agent where LOK

[58:56] agent what it did is it provided the

[58:59] agent with a special tool that allowed

[59:02] it to follow dependency paths. So if you

[59:06] um found the issue, you found config.py

[59:10] um and then uh once you found config.py,

[59:13] you could automatically jump with this

[59:15] tool to other related uh files if you

[59:18] wanted to.

[59:20] So um this is uh interesting. Uh what I

[59:24] will say is from my experience it's hard

[59:25] to make this work this sort of approach

[59:27] work better uh than the simpler stuff.

[59:30] And I'll I'll give some actual examples

[59:32] of that later.

[59:36] So for coding agent evaluation and

[59:37] training um the most popular uh

[59:40] benchmark for evaluating coding agents

[59:43] is bench. Probably many people have

[59:46] heard of this. Mo most people here.

[59:49] Okay, cool. Um, but anyway, like because

[59:52] I assume that not everybody has heard of

[59:54] it. Basically, the way uh this benchmark

[59:56] was created was it was created from

[59:59] GitHub issues where they take the GitHub

[60:03] issue uh which is the problem. They take

[60:05] the codebase state at the time the

[60:07] GitHub issue was resolved. So, it's

[60:10] basically what happened before the pull

[60:12] request. And they also find the tests

[60:15] that were associated with the GitHub

[60:17] issue. And so the tests are um because

[60:21] they were introduced together with this

[60:24] GitHub issue, these are presumably

[60:27] testing the functionality that needed to

[60:29] be fixed in the GitHub issue. So then

[60:31] based on that um they you know have an

[60:34] agent that generates a patch. um based

[60:38] on the patch they apply the patch they

[60:40] apply the tests and uh they generate

[60:43] results and if all of the relevant tests

[60:46] pass then you get a score of one. If all

[60:48] the relevance tests don't pass they they

[60:51] get a score of zero. Um harness here

[60:54] means actually something different uh

[60:56] than you know what an agentic harness

[60:58] means. It means like the test harness.

[60:59] Um so it's just running the test. But

[61:02] one important thing uh to mention here

[61:04] is that running the whole test suite on

[61:08] some of these GitHub repos would be

[61:10] really expensive. So like some of these

[61:12] repos are Django in NumPy and other

[61:14] things like this and running the test

[61:16] harness would be like 5 minutes or 10

[61:18] minutes for each example that you wanted

[61:20] to evaluate uh possibly even more. And

[61:23] so what they did here is they came up

[61:25] with a smaller subset of tests that need

[61:27] to pass in order for this issue to be

[61:29] considered resolved. And these fall into

[61:32] uh some categories. The first one is

[61:34] failed to failed to pass. And so these

[61:36] are things that failed before the PR and

[61:38] pass after the PR. So they're testing

[61:40] the functionality uh that was actually

[61:42] implemented in the PR. Then there's also

[61:45] pass to pass ones and these are related

[61:48] tests that passed before uh the the PR

[61:52] was filed and then also need to pass

[61:54] after to make sure you didn't break

[61:55] anything and didn't have any

[61:56] regressions.

[62:00] Cool.

[62:01] So um to build runnable benchmark tasks

[62:06] um essentially what and you'll do more

[62:09] of this in the evaluation uh evaluation

[62:12] benchmark place uh assignment but run

[62:16] runnable tasks are basically you need a

[62:18] starting state. So you need uh the files

[62:21] uh you might need the dependencies and

[62:22] you need the test command and the issue

[62:25] is the requested behavior um and the

[62:28] checks are the the tests.

[62:32] So um the good news about agents

[62:36] nowadays is

[62:38] actually evaluation is one of the

[62:39] biggest problems in uh making better

[62:42] agents because if you can generate lots

[62:45] of evaluations um you can actually

[62:47] perform reinforcement learning on these

[62:49] evaluation benchmarks and train an agent

[62:52] to do a good job. And so um if you can

[62:57] go through this process of generating

[62:59] many many of these outputs, you can

[63:02] actually uh train a model. And the way

[63:05] you do this is basically you just run

[63:07] the model to um run the model to

[63:09] generate an output and calculate the

[63:11] reward if uh you know the it did a good

[63:16] job or not.

[63:19] And um one of our uh one of our first

[63:22] papers on doing this was something

[63:24] called sugeim. So the thing with uh sui

[63:27] bench is that uh swbench is only an

[63:31] evaluation data set or they only have

[63:33] configured uh training environments for

[63:35] the evaluation data set. So for uh

[63:38] Swedge uh we basically created uh

[63:41] additional training environments and

[63:42] trained a model on it and demonstrated

[63:44] that a model that was you know quite

[63:46] poor before with about 11% accuracy with

[63:49] even 500 examples could scale up to

[63:51] being uh quite a bit better. And um I'm

[63:54] not going to talk about this a whole lot

[63:56] yet because we're going to be talking

[63:57] about this in a later class. But we also

[63:59] demonstrated that if you generate lots

[64:01] of outputs and rerank them uh you can do

[64:03] inference time scaling and do uh even

[64:05] better.

[64:08] Um

[64:10] so the biggest effort on this uh which I

[64:13] actually just realized I don't have it

[64:14] in the slides um but is worth knowing is

[64:17] something called SU rebench and SU

[64:20] rebench basically what this is is it's

[64:24] constantly creating more SWEBench

[64:25] environments and uh so they've been

[64:28] they've created them from PRs from uh

[64:32] December 2024 to June uh June 30 2026

[64:37] And I actually just discussed with the

[64:40] author recently and I think they're

[64:42] going to up update this in October or

[64:43] so. Um so this is just um creating more

[64:48] and more of these and they have a

[64:49] training set and a development set. So

[64:51] this is probably the best example of a

[64:54] large scale uh large scale publicly

[64:56] available uh coding uh coding agent data

[64:59] in the format of SWEBench.

[65:03] But um

[65:06] there's also more lightweight ways to

[65:08] create this data. So um one of the

[65:11] problems with this is you need a single

[65:12] pull request for each one of these uh uh

[65:16] training examples that you create. And

[65:18] so

[65:21] this is an example from Swissmith um

[65:24] which is not relying on uh pull requests

[65:28] but it's instead relying on artificially

[65:30] injected bugs.

[65:33] And what you do is you prepare an

[65:35] executable baseline and you mutate the

[65:38] code but keep the tests. And so

[65:43] essentially um how many people have

[65:44] heard of like mutation testing?

[65:48] A few people. Okay. This is this is

[65:50] actually a really interesting idea from

[65:52] uh kind of like software engineering or

[65:54] software engineering practice which is

[65:58] if you are not sure if your tests are

[66:02] good like if you have unit tests but

[66:05] you're not sure if your unit test suite

[66:06] is very comprehensive. You can go in and

[66:08] make small mutations to the code that

[66:10] should break the code and then you see

[66:12] if the tests pass or not. And if the

[66:14] tests still pass those tests are like

[66:17] not good tests. they they aren't

[66:19] covering like real breakages. So you

[66:21] should augment your test suite. Um so I

[66:25] think this work was inspired by that

[66:27] idea, but it's not exactly the same in

[66:29] that um they mutate the code in the

[66:33] repository and then they try to find

[66:35] tests that fail afterwards. And so what

[66:38] this essentially allows you to do is um

[66:42] it allows you to create synthetic buggy

[66:44] data that you can then use to train

[66:46] models. uh just by just with the

[66:49] existing uh tests in in codebase.

[66:53] Um so here's a example. So um if you

[66:58] have code where all four of the existing

[67:00] tests pass, you then go in and mutate

[67:03] the code um uh into something like

[67:06] return three if not value instead of uh

[67:09] if value is none. And then um one of the

[67:13] tests may fail now. And so this is a

[67:15] good example where you essentially uh

[67:18] are able to come up with uh something

[67:20] that says please fix this.

[67:25] Um cool. Any any questions here?

[67:30] So the good thing about this is this is

[67:32] very lightweight and you can generate a

[67:34] nearly infinite amount of data by doing

[67:36] this. The bad thing about this is these

[67:38] are not necessarily like natural uh

[67:40] training examples that you might want to

[67:42] tackle for real. Um

[67:46] so you can scale out to different uh

[67:50] programming languages with this

[67:52] framework as well. So there's uh

[67:54] something uh called multisbench and

[67:56] another thing called SWEBench

[67:57] multilingual which basically uh scale

[68:00] out to you know a number of different

[68:02] programming languages.

[68:04] The only logistic difficulty is that the

[68:07] conventions are different between the

[68:08] languages and you need to handle them.

[68:10] Um, the good thing is now coding agents

[68:12] can do this very easily. So it's not

[68:15] that not that hard to change the

[68:17] conventions.

[68:20] Um, a final thing I'd like to talk about

[68:22] is multi-harness training. And so as I

[68:25] mentioned before, um

[68:29] if the edit format is very different

[68:33] between uh what a language model expects

[68:35] and what the harness expects,

[68:38] um most uh most language models will

[68:42] perform worse on the harnesses that

[68:43] they're not trained on. So now it is

[68:46] very common uh for language model

[68:49] providers to train on multiple

[68:50] harnesses. So they'll not just train on,

[68:53] you know, a single harness, but they'll

[68:54] train on like open hands and open code

[68:56] and codecs and um, you know, all of

[68:58] these other harnesses. And to give one

[69:01] example of this, um, you can read the

[69:03] reports of Neotron by Nvidia where they

[69:06] intentionally trained on um, I think

[69:09] five or more uh, five or more harnesses

[69:12] to provide this to provide a model that

[69:15] works with a lot of different harnesses.

[69:19] Cool.

[69:21] Um, we don't have a whole lot of time

[69:23] left. I'm maybe we'll just go quickly

[69:25] through a number of different um a

[69:29] number of different uh tasks other than

[69:32] just like straight up issue resolution.

[69:34] These are less these are less mainstream

[69:37] in research, but they're very important

[69:41] if you want to build a functional model.

[69:42] So, um front-end development of one of

[69:46] is one of them. Um there's a front-end

[69:49] development benchmark called Swebench

[69:51] Multimodal. Um this is a benchmark that

[69:54] focuses only on fixing bugs in frontend

[69:59] uh fixing bugs in uh front-end tasks.

[70:03] And so it is not um it's not focusing on

[70:08] developing like new frontends. It's more

[70:11] uh kind of on the issue resolution

[70:13] thing. And so there's two differences in

[70:17] the in creating a multimodal model. The

[70:20] first difference is typically you would

[70:23] think that you would need a a multimodal

[70:25] model to do um uh to like take in the

[70:31] input and understand the input. So you

[70:33] would need a language model that was

[70:35] trained to be able to ingest images. Um

[70:38] the other thing is you need to verify

[70:40] and so you need to there's a couple ways

[70:43] to verify in the browser. One way is to

[70:45] write tests uh that work in the browser.

[70:48] Um another way is to look at the the

[70:50] output.

[70:52] Um

[70:54] so uh there's kind of two ways that

[70:56] people do this nowadays. Um, one common

[70:59] way of doing this is to take a guey

[71:02] based agent and use it as a component of

[71:04] your coding agent or have a have an

[71:07] agent that can handle both guey based

[71:08] tasks and coding tasks. Next class is

[71:11] going to be about guey agents. So I'm

[71:12] not going to explain at all about how we

[71:14] build guey agents. Um, another way you

[71:17] can do it is by writing a script that

[71:20] tests the guey. And so for instance,

[71:22] Playright is a common uh guey testing

[71:26] library that a lot of people use to do

[71:27] this sort of thing.

[71:30] Um and so basically, you know, you might

[71:33] if you have an issue where you're able

[71:35] to submit with a length of zero input,

[71:38] um you would uh then be able to verify

[71:41] that visually that this happens. or you

[71:43] would be able to write a um a playright

[71:46] script that makes sure that after you

[71:49] add zero it enter an unblink name will

[71:51] appear.

[71:53] Um

[71:55] so yeah and then su bench multimodal is

[71:58] is a way to evaluate that one very

[72:01] shocking result from a couple months ago

[72:03] was there's a popular model called GLM 5

[72:07] uh GLM uh and GLM 5.2 uh was a model

[72:11] that came out. It was not a multimodal

[72:13] model, but it got like number one on

[72:15] front-end design arena. Um, regardless

[72:18] of this, so that kind of shook my

[72:20] assumptions about what you need in order

[72:22] to be a good front-end uh developing uh

[72:26] code coding agent. But uh you know, I I

[72:29] still think multimodal behavior is

[72:31] probably pretty important.

[72:33] Um,

[72:35] so

[72:37] there's a famous idea of inner loops and

[72:40] outer loops in development. And the

[72:43] inner loop of development is kind of

[72:45] what I've been talking up about up until

[72:46] this point. And it's essentially the uh

[72:49] iterative process of doing bug fixes,

[72:52] testing, and these sorts of things. Then

[72:55] the outer loop of development is

[72:56] everything that's not this. And there's

[72:58] a lot of stuff involved in software

[73:00] development that's not this. So for

[73:02] example, code review is one example. Um

[73:04] deployment and monitoring is another

[73:06] example. Maintenance

[73:08] um and also uh planning and coming up

[73:11] with requirements are are other

[73:13] examples. And ideally we'd like to have

[73:16] agents that can help us with all of

[73:17] these things. Um but the hard thing is

[73:19] all of these things are kind of harder

[73:21] to define and also harder to find

[73:23] training data for. Um so this is an

[73:26] interesting survey from Microsoft in

[73:29] 2019. So this might be different uh than

[73:32] it is now but um in 2019 they did a

[73:35] survey of their software developers and

[73:37] asked how much of your time do you spend

[73:39] coding and the answer was uh 15%. Um and

[73:44] this is like the the new uh issue

[73:47] development and and feature new uh

[73:50] feature development and issue

[73:51] resolution. They spent uh 25% of their

[73:54] time on meetings and email uh 14%

[73:58] debugging. uh 8% running tests uh etc

[74:02] etc. So like actually this is a big part

[74:04] of the software development uh work uh

[74:06] as well.

[74:10] So um what we can do is we can compare

[74:14] uh tasks and so um you know if we have

[74:17] repair uh issue repair um I already

[74:20] talked about that but there's also um

[74:23] creating uh things from scratch um

[74:28] creating good tests for your code fixing

[74:30] failing deployments or something and uh

[74:34] developing you know apps over a long

[74:36] period of time. And so a first uh

[74:40] example is um you can train specifically

[74:43] on localization. Um so you can have

[74:46] models that are are particularly good at

[74:48] identifying you know like where to um

[74:52] where to start working on a coding task.

[74:54] We have a RL um uh approach to doing

[74:59] this called code scout. Um, this might

[75:02] be interesting to you uh if you want to

[75:04] do an RL related thing for your project

[75:07] because it's like coding agents uh but

[75:10] it's a little bit more tractable and

[75:12] easier to do with smaller models. So if

[75:14] that sounds interesting to you, you can

[75:15] check out our code scout paper.

[75:18] Um, a second task is uh creating apps uh

[75:22] from scratch. Uh there's something

[75:25] called viench which is evaluating agents

[75:28] for how good they are at kind of vibe

[75:29] coding in general. Um this is very uh

[75:33] hard to do because you need to um you

[75:36] need to be able to evaluate them

[75:38] properly and so uh you need to come up

[75:40] with good verifiers.

[75:44] Another thing is um imp implementing

[75:46] full uh kind of like backend libraries.

[75:49] Uh there's a few benchmarks for this.

[75:50] One older one called commit zero and one

[75:53] newly popular one called program bench.

[75:55] In program bench essentially what you

[75:57] need to do is you need to re reverse

[75:59] engineer a binary and reimplement it

[76:01] from scratch. And so here what you can

[76:04] do is you can run the binary and probe

[76:06] based on inputs and outputs and then you

[76:08] need to create a new implementation. And

[76:10] this is interesting because it's very

[76:12] long horizon and uh you know with

[76:14] shorter horizon tasks becoming easier

[76:16] and easier it's now like one of the new

[76:18] challenges.

[76:22] Another example uh if you're interested

[76:24] in benchmarks is the sui milestone

[76:26] benchmark. And the basic idea here is

[76:29] that you don't want to implement a

[76:30] single issue. You want to implement many

[76:32] issues in kind of an epoch. And make

[76:35] sure that as you um implement the issues

[76:38] one by one, you're not making a huge

[76:40] mess of the codebase and making it

[76:41] harder to maintain uh because that's a

[76:44] big problem with code uh some coding

[76:46] agents. And so uh this is a benchmark

[76:48] that's uh meant to evaluate that.

[76:53] Another really big problem nowadays is

[76:55] uh generating tests that allow you to

[76:57] validate whether you did a good job of

[77:00] fixing an issue. Because I feel like now

[77:03] with coding agents, if you can write

[77:05] really good tests to validate that um

[77:08] the issue is solved, you've kind of

[77:11] solved half of the battle, right? you've

[77:12] like specified what task needs to be

[77:14] done and then agents are just really

[77:16] good at iterating on them. So, SWTB is

[77:19] an example of a benchmark that uh that

[77:21] allows you to do this and it's based on

[77:23] the mutation testing that I mentioned

[77:24] before.

[77:27] A final one is um kind of like more

[77:30] operational

[77:31] uh like tasks like deployment and I

[77:36] don't think there's a really good um

[77:39] there there are really really good

[77:41] benchmarks for this yet and it's kind of

[77:42] harder because you need actual

[77:44] infrastructure to run it but I have a

[77:46] reference for an example um uh that was

[77:49] created by Jet Brains that you can take

[77:51] a look at if you're interested

[77:54] Um, so yeah, we're we're at 50 uh we're

[77:59] at 50 past. Um,

[78:02] I'll I'll maybe just cover this one uh

[78:04] very very briefly. So there's also some

[78:07] um uh some work uh by people uh here at

[78:11] CMU including me uh and Daniel and for

[78:14] the other one called SU playground

[78:18] and um

[78:21] SU playground and hybrid gym which

[78:25] basically are um automatically creating

[78:28] coding benchmarks for things other than

[78:30] just coding uh for other things in

[78:33] software engineering. So, um, sorry I

[78:36] ran out of time and I'm not going to be

[78:37] able to cover code world models, but I'm

[78:39] happy to, uh, talk about that in our,

[78:42] uh, in office hours or something like

[78:44] that. So, uh, yeah, thank you everyone.
