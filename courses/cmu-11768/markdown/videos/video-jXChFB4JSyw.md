# Lecture 2 recording

[Course index](../../README.md) · [Original source](https://www.youtube.com/watch?v=jXChFB4JSyw&list=PLSN0qpDfUvTM&index=2) · [Raw file](../../raw/videos/jXChFB4JSyw.json)

Retrieved: 2026-11-13T16:48:23.793991+00:00

[00:00] Okay. So, hi everyone. Uh, welcome to

[00:04] class number two. Today,

[00:07] uh, today I'll be talking about tool use

[00:09] for language model agents. And, uh, this

[00:13] is, you know, the the most fundamental

[00:15] thing about agents that, uh, you know,

[00:17] makes them different from a language

[00:19] model.

[00:23] Um so the basic idea here is uh that

[00:27] we're going to be um a tool is basically

[00:29] an interface through which a language

[00:31] model can invoke an external computer

[00:33] program. And uh this is a language model

[00:38] cannot do this on its own because it's

[00:40] fundamentally a token predicting

[00:42] machine. But this enables you to do you

[00:46] know many many different things. So you

[00:48] know you can search, you can call a

[00:50] calculator, you can call a browser, um

[00:52] you can call Python, you can call

[00:53] arbitrary APIs and so uh the language

[00:58] model kind of as you'll see the method

[01:01] for tool calling is standardized but

[01:04] what you do downstream with the tool

[01:06] call can be very different.

[01:09] So there's basically two uh benefits of

[01:12] tools and all of this is from one of the

[01:15] readings that I I posted on the website

[01:17] if you want to go back and read more

[01:18] about it. Uh this is a survey that uh I

[01:22] we wrote uh together Daniel and I and

[01:25] Zoro Wong, one of our our students. Um

[01:27] and the first thing is extending the

[01:31] ability of language models. So this is

[01:33] giving language models the ability to do

[01:35] something that they fundamentally cannot

[01:37] do. And so this could be like accessing

[01:40] information or actions that are outside

[01:42] the language model's um you know action

[01:45] space. The second thing is uh

[01:47] facilitating the language model. And so

[01:49] what I mean by this is this is something

[01:51] that fundamentally the language model

[01:53] can do but it's just a lot easier if you

[01:58] don't if you don't require the language

[02:00] model to do it.

[02:02] So um can anybody come up with an

[02:05] example or well I guess we already have

[02:08] an example in here. So like one thing

[02:10] the the language model fundamentally

[02:11] cannot do would be get the time four

[02:14] months ago or something like that. So

[02:15] the most recent information it saw is uh

[02:18] from four months ago and then its

[02:20] parameters are frozen. So there's no way

[02:22] it could know that without calling you

[02:24] know an external function. On the other

[02:26] hand, uh something in the realm of

[02:28] facilitating is language models can do

[02:31] math actually quite well nowadays, but

[02:34] they take a lot longer than calling a

[02:36] calculator to do math because they have

[02:38] to do reasoning like you ask them to

[02:40] multiply uh two seven-digit numbers and

[02:43] it will take them a very long time to do

[02:45] it where a calculator can do that really

[02:46] quickly. So those are the two kind of

[02:49] basic categories.

[02:52] So um to go a little bit more deeply

[02:54] into those uh you can do things like

[02:57] look up current information um and the

[03:00] benefit of this is this gives you you

[03:01] know fresh evidence to uh ground your

[03:04] answers uh do exact computation using

[03:07] like calculators or python this gives

[03:09] you the ability to execute more reliably

[03:12] or and quickly than using the language

[03:14] model itself.

[03:15] Um other things is uh access private

[03:18] states. So giving the model access to

[03:20] like information about the user so they

[03:22] can uh respond based on the user state

[03:25] um or uh make a change to your external

[03:27] environment. So this could be like

[03:28] browsing or or calling an API.

[03:33] So to have some examples of these um if

[03:37] we think about chat GPT

[03:39] uh chat GPT used to like literally just

[03:43] be text in and text out when it first

[03:45] came out. it, you know, the the only

[03:48] thing that it could do was give you

[03:49] textual responses to uh your queries.

[03:52] Now, it's kind of an everything app. It

[03:54] allows you to do so many different

[03:56] things. Um,

[03:58] so like what what are some of the

[04:00] examples of things that uh you know are

[04:05] your top use cases of uh of using chat

[04:08] GPD now?

[04:10] >> Yeah.

[04:11] >> Writing code. Okay. So uh what what tool

[04:15] would you need for something like that?

[04:18] uh like cursor or codeex I think they

[04:21] they can invoke like

[04:23] >> okay but that's not chat GPT right

[04:25] that's cursor or codeex yeah I mean chat

[04:27] GPT like in the chat GPT interface

[04:30] >> they can use blender so they they can

[04:32] render blender okay things so that

[04:36] that's an example of um something that

[04:39] requires executing code but also like

[04:41] displaying it in the appropriate format

[04:43] um any any other ones that people do

[04:46] yeah Just the web page generate images.

[04:49] >> Generate images. Yeah. So that that's

[04:51] calling an image generation tool. Any

[04:54] others?

[04:56] >> Yeah.

[05:06] Yeah. So recommend products like a

[05:08] blender or something like this. And for

[05:10] this uh what what sort of tool do you

[05:12] think it would need?

[05:14] >> Some sort of like web searches like

[05:16] Google or Amazon to find.

[05:19] >> Yep. So you might need like arbitrary

[05:21] web search or you might need an API that

[05:23] directly links into Google or Amazon or

[05:25] something like that. Yeah. Any other

[05:27] like weirder weirder ones? Things you

[05:29] were surprised chat GPT was able to do?

[05:31] >> Yeah.

[05:31] >> You can render latex quite nicely.

[05:35] >> Okay. messed up files when I fix you the

[05:38] PDF

[05:39] >> and compile everything which is very

[05:41] handy sometimes.

[05:42] >> Yep. Ren, it can render latex. Well, I

[05:44] actually don't know if this is a tool or

[05:46] if this is just a front-end interface

[05:48] thing, but it might be just that it's

[05:50] rendered in your web browser.

[05:52] >> Oh, it creates a PDF. So, okay. Is a

[05:54] tool. Okay. Very cool. Yeah.

[05:57] >> Interact

[05:59] >> uh interact with like Slack or something

[06:01] like that. So, that's another

[06:02] specialized API. So all kinds of

[06:04] different things. Um I I kind of

[06:07] categorized these into a list of things

[06:09] that I think are um the most uh like

[06:12] typical tools and most of the other

[06:15] tools can kind of be categorized into

[06:17] each of these. So the first one is uh

[06:19] textual responses. So this is kind of

[06:22] the boring one where it just gives you

[06:24] an answer. Um there's two ways you can

[06:27] implement this within an agentic uh like

[06:30] loop. By the way, chat GPT is is an

[06:33] agent now. Uh if you're like if there

[06:35] was any question about it, chat GPD is

[06:37] not just a chat app. It's an agent

[06:38] because it makes uh iterative tool calls

[06:41] to answer your queries. So that's kind

[06:42] of the definition of an agent. Um but uh

[06:46] textual responses, there's two ways you

[06:48] can implement these. One way you can

[06:49] implement these is you can have a finish

[06:53] tool that says, "Okay, I'm done

[06:55] interacting with the user, so I'm just

[06:56] going to finish and and output some

[06:58] text." The other way you can do it is if

[07:00] the agent decides to not call a tool,

[07:02] you can just finish the agentic loop. So

[07:04] that's kind of uh you know the the

[07:06] simple u you know most obvious one.

[07:11] Another extremely common one. Um so all

[07:15] all of these are tools and so like

[07:16] theoretically all of them can be thought

[07:18] of as an API but uh just to break them

[07:20] down a little bit more. Um another one

[07:23] is searching the web and this is you

[07:25] know pulling in information um from all

[07:28] of these uh different settings. Um how

[07:32] many people have heard of retrieval

[07:34] augmented generation? Probably everybody

[07:36] everybody who took the NLP class here uh

[07:39] you know has heard of it but a lot of

[07:41] people. How many people have heard like

[07:43] rag is dead?

[07:46] [snorts and laughter] A fairly large

[07:47] number of people. So there there's been

[07:49] an argument in like language model

[07:50] circles that retrieval augmented

[07:52] generation was so like two years ago and

[07:54] like nobody cares about it anymore. My

[07:56] argument here is a retrieval augmented

[07:59] generation where you retrieve context

[08:00] and then generate answers based on it

[08:02] has become so normal that people don't

[08:04] even realize that they're using it

[08:06] anymore. And so um it's it's so alive

[08:09] that people think it's dead. Um but uh

[08:12] basically you know searching the web and

[08:14] retrieving information and then

[08:16] generating answers based on it is now

[08:18] essentially the norm uh within these uh

[08:21] these applications. Now so uh that's

[08:23] another tool that's provided very very

[08:25] broadly and like any chat uh interface.

[08:29] Another one is code execution and so

[08:32] this is uh throwing in uh you know a set

[08:35] of code to do uh calculations or or

[08:38] something like this. very useful for uh

[08:40] computation all the other stuff we

[08:42] talked about. Another common one is uh

[08:45] having some sort of image generation and

[08:49] uh this this is you know obviously

[08:51] another very popular use case in chat

[08:53] GPT. Um this one's a little bit

[08:56] different because like all of the other

[08:57] ones here uh that I was talking about

[09:00] basically you know mostly interface with

[09:02] text. Um here this is interfacing with

[09:06] uh this is interfacing with images. One

[09:09] interesting thing is uh you'll notice

[09:12] that this is not the same thing is here.

[09:16] So this is like water watercolor robot

[09:19] studying in a library where the query

[09:21] was actually different. And so a big

[09:25] part of calling these images is actually

[09:27] deciding what query to put in there. So

[09:30] the language model will like really

[09:31] really expand the query before it calls

[09:33] an image generation API. I don't know if

[09:35] you can see this anymore in chat GPT,

[09:37] but you used to be able to see in chat

[09:38] GPT when you downloaded the image um

[09:41] that it would have like a very different

[09:42] caption than the caption you gave and

[09:44] you could kind of like latently see what

[09:46] the uh what query the the image

[09:48] generator uh sent to the generate image

[09:50] tool.

[09:53] Then there's all all kinds of uh you

[09:56] know custom functions. So, um, like buy

[10:00] me buy me bananas, uh, milk and coffee.

[10:03] Um, so, you know, this could create a

[10:05] grocery cart, uh, for you and call the

[10:08] like Instacart API to do this. Um, and

[10:12] you can basically go as wild as you want

[10:14] with all these tools and and add

[10:15] whichever ones you want there.

[10:20] Okay, so there's a bunch of different

[10:24] ways you can think about tool calling.

[10:27] Um the first way you can think about

[10:28] tool calling is just

[10:32] you provide a list of uh 50 or 70 API

[10:37] functions that the agent is able to

[10:39] inter interact with and it can call

[10:42] these uh APIs and if you do that

[10:45] basically what you're doing is like

[10:47] every step you're calling one API or if

[10:49] you're doing parallel tool calling

[10:50] you're calling multiple APIs or

[10:51] something like this but code is kind of

[10:55] a special uh API uh because code is

[11:00] extremely

[11:01] uh you know expressive and you can view

[11:04] code as like a meta tool right so within

[11:08] this we have like the bakers baked 200

[11:10] loaves of bread how many loaves of bread

[11:11] did they have left here this is calling

[11:14] an assignment tool an assignment tool

[11:18] this is calling a subtraction tool um

[11:20] this is calling a uh assignment tool you

[11:23] know etc etc so like essentially

[11:27] Um I I imagine that a lot of people have

[11:29] taken like a programming languages

[11:30] course or have some familiar familiarity

[11:33] with programming languages but basically

[11:35] you you can express

[11:38] each piece of code is a tree of these

[11:41] function calls um and these uh the tree

[11:44] can also be have loops and other uh

[11:47] control flow in it. So it's essentially

[11:49] you know a very rich way of calling uh

[11:52] tools. Um and so uh you can also pull in

[11:56] external libraries. So these are now the

[11:59] custom APIs that you pull into your uh

[12:02] pull into your system. So uh you know

[12:05] now if you're calling pandas now you've

[12:07] opened up all of the like tools in

[12:10] pandas right

[12:12] and um you know you can build your own

[12:16] utility functions. So you could call uh

[12:20] special purpose functions that you want

[12:22] uh as well. So

[12:25] code is kind of special. It's like one

[12:27] of the one of the you know special

[12:30] things that uh it's different from other

[12:33] tools in the way that it like opens up

[12:35] your ability to call tools in new ways.

[12:37] And so there's actually uh research work

[12:40] that demonstrates that this is very

[12:41] effective. Uh right now we basically

[12:44] take it for granted but this was not how

[12:46] uh not how we called tools like three or

[12:49] four years ago uh when we first started

[12:52] uh you know building agents with LLMs.

[12:55] And so the the standard then was like if

[12:58] you got a a query sorry this is very

[13:00] small but um it basically says determine

[13:02] the most cost-effective country to

[13:04] purchase the smartphone model Kodak 1.

[13:07] Uh the countries to consider are the US

[13:10] uh Japan, Germany and India. Basically,

[13:12] what this would require you to do was uh

[13:16] you would call your lookup rates tool on

[13:18] Germany. Um you would call your lookup

[13:20] phone price uh tool. You would call uh

[13:23] convert and tax. Then you would call

[13:26] lookup rates again. Then you would call

[13:28] uh look up phone price and you would

[13:30] step over and over and over again uh in

[13:32] order to uh finally get uh finally get

[13:35] the result.

[13:37] But if you write code, you can just

[13:39] write like a single program to perform

[13:41] this. And so uh this makes it like a

[13:44] much richer uh a much more efficient way

[13:46] of calling tools in addition to be being

[13:48] richer. And so this method called uh

[13:51] called Kodak has a paper uh about it and

[13:55] uh some of the core results from the

[13:56] paper are essentially the success rate

[13:58] goes up and the average number of

[14:00] interaction turns goes down. And this is

[14:03] even for tasks that didn't traditionally

[14:06] require code. These are for tasks that

[14:08] were like viewed as regular tool use

[14:10] tasks. Um but like code is just like a

[14:13] good medium uh for how you would do

[14:15] this.

[14:18] Um but there's a reason why people don't

[14:20] use code uh programmatic tool calling

[14:22] for everything. Um and it largely has to

[14:25] do with um with like the level of power

[14:29] that you want to give to the agent. So

[14:32] code is very highowered. So it's

[14:34] expressive. It gives you loop variables

[14:36] and libraries. This is good. But what

[14:38] could be a downside of this?

[14:41] Any ideas? Ju just with respect to loops

[14:44] variables uh loops and variables at

[14:46] first maybe. Yeah.

[14:48] >> Get stuck.

[14:49] >> Yeah, it could get stuck. So it could

[14:50] write an infinite loop and then you need

[14:52] to have something in your system to deal

[14:53] with infinite loops, right? That's uh

[14:56] that's a little bit annoying. Um what

[14:58] about libraries?

[15:01] any problem with that?

[15:03] >> Yeah, security problems would be one

[15:05] thing. Also, maybe just versioning and

[15:07] stuff like this, but um I'm not sure if

[15:09] people are familiar with this, but one

[15:11] of the major issues with agents in cyber

[15:13] security right now is the agents will

[15:15] pull in a library that has been

[15:17] compromised. Um the agent gets

[15:20] compromised and then your whole system

[15:21] gets compromised. So, uh this is

[15:23] something uh something you need to be

[15:25] very careful about.

[15:27] Um they're also uh harder con to

[15:30] constrain because they have the broad

[15:31] action space. So uh it's you know harder

[15:34] to validate and uh get predictable

[15:36] behavior. Um they also have higher

[15:38] impact. So they can you know use more

[15:40] disk uh sorry use more memory, use more

[15:43] disk, use more CPU and stuff like this.

[15:45] And so because of this um we'll talk

[15:47] about this more in the safety lecture,

[15:48] but like once you move to programmatic

[15:51] tool calling, you need to be uh you need

[15:54] to think about sandboxes and how you're

[15:55] going to contain the agent and stuff

[15:56] like that as well.

[15:59] Um any any questions about this?

[16:06] Cool.

[16:09] Okay. So I want to uh talk next about

[16:12] the mech uh mechanics of providing tools

[16:14] and right now uh every language model is

[16:19] basically pretty good at uh like calling

[16:22] tools but this was not you know taken

[16:24] for granted. I I think I mentioned this

[16:26] on Tuesday as well. Um but basically

[16:28] tool calls are um expressed as tokens

[16:32] like this. And so um you know a text

[16:35] continuation is the weather is sunny. A

[16:39] tool continuation is uh like a tool call

[16:43] and then you have get weather or

[16:44] something like this within the the tool

[16:46] call. And very often uh you have both in

[16:50] the same uh output. So if you remember

[16:53] react uh which was talked about before

[16:58] um I can actually draw this on the board

[17:03] but react basically you have your text

[17:06] up here

[17:08] and then you have your uh tool call

[17:12] and then you have your tool call down

[17:14] here.

[17:19] Yeah, this is like the end of the tool

[17:21] call.

[17:24] And so now you have the the model be

[17:27] being uh giving a response to the human

[17:31] uh while it's making the tool call. And

[17:33] then uh in here you have the like actual

[17:35] tool call that it's making. And so the

[17:37] react loop is no longer expressed as

[17:39] like separate code. It's expressed more

[17:42] as like just a single completion. um if

[17:45] you're using one of the reasoning models

[17:49] um

[17:50] that can reason uh like have long

[17:53] reasoning traces and stuff like that. In

[17:56] addition, you might have like the

[17:57] thinking tokens up here and then a

[17:59] message and then the tool calls. And so

[18:02] the thinking is like very verbose

[18:03] thinking that you don't show to the

[18:05] user. The text is the less verbose uh

[18:07] message that you show to the user and

[18:09] then the tool call is like the actual

[18:11] output you have there.

[18:14] Yeah,

[18:15] >> the tool call tokens has to be in the

[18:17] vocabulary of the model during

[18:19] pre-training also, right?

[18:21] >> Yes.

[18:21] >> So all of these service tokens are going

[18:23] to be vocabulary.

[18:26] >> Uh yes. So actually that's a good point.

[18:29] I said yes, but the answer might be no.

[18:31] I'm going to repeat the question first.

[18:32] So the question was um do these tokens

[18:35] have to be in the vocabulary when you do

[18:36] pre-training? Um, typically if you're

[18:40] pre-training on all of the internet, you

[18:41] don't necessarily have to have them in

[18:43] the vocabulary yet. Um we there are

[18:48] cases where you might do that but it's

[18:49] actually more typical to introduce them

[18:51] in a process of mid-training which is

[18:53] like uh between uh it's when you're

[18:56] training on like moderately large

[18:59] amounts of data on things in the format

[19:01] that you like and then uh you might do

[19:03] reinforcement learning after that but

[19:05] you might not necessarily have them when

[19:06] you pre-train on the whole internet.

[19:10] Cool. Um

[19:14] so

[19:15] I think this should likely be familiar

[19:19] to um you know uh people who have

[19:22] implemented things in uh previous

[19:24] natural language processing or or

[19:26] whatever courses. But um if you have the

[19:29] chat format like the open AAI chat

[19:31] format you have things like the system

[19:33] message, the user message, the assistant

[19:35] message and then uh these are

[19:38] represented as something like JSON in

[19:42] uh like in Python when you call the call

[19:44] the model but these get converted into

[19:48] something uh with like a special token

[19:50] here the system uh like this is a system

[19:54] prompt and then be concise and stuff

[19:56] like this. So like each chat message

[19:59] gets its own format and this is an

[20:01] example of the quen format

[20:04] but uh as I'll show later the other uh

[20:07] other functions are in different

[20:08] formats. So

[20:11] tools basically um add a structure to

[20:15] the request and so you have a tool

[20:16] definition like this and uh this tells

[20:19] you that it's a function. The function

[20:22] name might be get weather. Um the

[20:24] parameters are city and the type is a

[20:28] string and this is required. And this

[20:33] schema gets passed to for example the

[20:36] chat completions function that you you

[20:37] would use when calling openAI or

[20:39] something like this.

[20:44] So um when the prompt uh contains

[20:47] something like this, you might have uh

[20:49] this included in the tools section of

[20:51] the prompt and then the output uh ends

[20:54] up being something like name get weather

[20:57] uh with the appropriate arguments like

[20:58] the city of Pittsburgh.

[21:02] So um we we had a question about how you

[21:05] pre-train the models and um you might

[21:08] not be pre-training but at least at

[21:10] mid-training and beyond you will be

[21:12] training the model to fit a particular

[21:13] tool call format. The interesting thing

[21:16] is uh every model has a different tool

[21:17] call format. Maybe not everyone but many

[21:20] of the different ones. And so uh Quen

[21:24] has like im start tool call uh IM end.

[21:29] Uh Mistall has tool calls and then uh

[21:32] all of the tool calls. Deepseek has

[21:34] their like DSML DeepS markup language

[21:38] function calls. They they don't call it

[21:39] tool calls. they call it function calls

[21:41] and then evoke invoke and basically you

[21:44] know any of these works. Um there might

[21:46] be like minor minor differences in uh

[21:49] which one gets better performance or not

[21:50] if you train the same model with the

[21:52] same data. Uh but

[21:54] what you need to know is you need to

[21:56] know that these are different. So you

[21:57] can't just assume that like some parsing

[21:59] code that works with deepseek will

[22:01] suddenly work with quen and vice versa.

[22:03] Yeah.

[22:04] >> You said you add functionality.

[22:09] So need to provide.

[22:17] >> Um, so what do you mean by loose

[22:19] generalizability?

[22:36] >> Yep. fine tuning

[22:38] set of

[22:39] >> Yeah. So when you're when you're

[22:41] fine-tuning, you will want to match like

[22:44] if you're fine-tuning

[22:46] from a model that's already been

[22:48] trained, you 100% want to match the tool

[22:50] call format. You don't want to try to

[22:51] get it to do something it wasn't trained

[22:53] on. Um, and the good news is this is all

[22:57] implemented in like hugging face with

[22:59] the apply chat template uh function. And

[23:02] so you need to apply the chat template

[23:04] for the model you're using, but that's

[23:05] all implemented. If it's not implemented

[23:08] properly, you can go in and um like it

[23:11] you ask them and they'll go in and

[23:13] implement it or you do it yourself or

[23:14] something like that. But yeah, it's it's

[23:16] all standardized now. But I I want to

[23:20] people to know that this is going on

[23:22] under the hood because if you don't know

[23:23] this, you can make mistakes and uh and

[23:25] it will not be happy.

[23:29] Cool. So um once you have done this uh

[23:33] the next thing is um that you

[23:38] do tool call parsing and actually I'm

[23:40] going to talk about tool called kernel

[23:42] parsing in the next section. So um not

[23:45] immediately here but like let's assume

[23:47] that if uh the language model outputs

[23:51] this you have a way of parsing it into

[23:53] uh into the function arguments. you then

[23:56] um like have the you register the tool

[24:00] at initialization and um you uh have a

[24:04] way to resolve it so that you get a map

[24:08] from the name to the tool that you want

[24:10] to execute. So most agentic frameworks

[24:13] basically will will have a way that you

[24:15] can add new tools. Each tool gets its

[24:18] own name and then you have a Python

[24:20] function or something like that. Python,

[24:22] TypeScript, whatever language. And then

[24:24] it uh it will be dispatched to that with

[24:27] the appropriate arguments. And so then

[24:30] at each time you you parse uh you look

[24:32] up the tool, you validate the uh action

[24:35] from the arguments and you execute uh

[24:37] and then you return. But um at

[24:40] validation time, this can fail if the

[24:43] model gave you the wrong uh the wrong

[24:45] tool call. At execution time, this can

[24:47] also fail if there's like not something

[24:50] that was explicitly said is bad uh is

[24:54] like invalid but implicitly is invalid.

[24:57] So like for example, if you have an

[24:58] execute Python tool, it might accept any

[25:01] string as Python, but then when you

[25:03] actually try to run the Python, it it

[25:05] might fail. So that that would be like

[25:06] an execution error. And then if it does

[25:08] if it well whether it uh whether it

[25:11] fails or not, then uh you get an

[25:13] observation out of it.

[25:18] So this is another detail um that that's

[25:21] pretty helpful but also really annoying

[25:24] uh when you're implementing agents if

[25:26] you if you get it wrong. But basically

[25:29] each tool call is assigned an ID uh when

[25:33] you uh when you run it basically by um

[25:37] uh either the language model inference

[25:39] code or the agent code and then you get

[25:42] a result and the result has a matching

[25:45] call ID and this is useful especially in

[25:50] the case of parallel tool calling

[25:51] because I'm going to talk about parallel

[25:53] tool calling in a bit and having the IDs

[25:55] matched lets you know which tool call is

[25:57] associated assiated with with which

[25:59] result. But the uh the problem is uh for

[26:04] instance uh anthropic if you have a tool

[26:08] call with no matched tool result it will

[26:10] die on you and uh so it will tell you

[26:14] this is an invalid history and I'm not

[26:16] going to accept this history and and

[26:18] generate any more outputs for you. And

[26:20] so in my practical experience there's

[26:24] times when for example the assistant

[26:26] makes a tool call then suddenly uh your

[26:29] your program dies or something like that

[26:31] it fails to write out the tool result

[26:32] and then you resume it it doesn't have

[26:34] the result the associated result and uh

[26:37] anthropic fails to fails to work for

[26:40] you. So this is a little bit of a a

[26:42] detail that you need to know.

[26:47] Okay. So, um, any any questions there?

[26:51] Yeah.

[26:55] >> And, uh, great question. Are the tool

[26:57] calls asynchronous? Um, I'm going to

[26:59] talk about that in like the the next

[27:00] next section. Yeah.

[27:03] Cool. Okay. So, now now here's a very

[27:06] technically algorithmically

[27:09] difficult problem. Uh, that may be very

[27:13] interesting to you or maybe not not very

[27:14] interesting to you. But if it's not

[27:16] interesting to you, be glad that other

[27:18] people are solving it for you. Um, so,

[27:21] uh, language models are definitely not

[27:24] guaranteed to generate well-formed tool

[27:26] calls. Um, and this is an example. Uh,

[27:30] you can see that this is JSON that's

[27:32] missing the uh, last closing bracket.

[27:36] So, this is poorly formed JSON. You put

[27:39] this into your JSON parsing program and

[27:40] it will throw an exception and you won't

[27:42] be able to get the uh, the data out of

[27:44] it. So I I've seen a million people go

[27:47] in and try to like figure out if the

[27:49] brackets are missing and like add one

[27:50] post hawk, but you don't want to be

[27:52] doing that. That's not not fun. Um so

[27:56] there's a bunch of constraints uh that

[27:58] you uh could be assigning to each of the

[28:00] tool calls. So the first one is syntax.

[28:04] So it has to be valid JSON. So this is

[28:06] kind of like table stakes, right? So it

[28:08] it needs to parse. Um the second thing

[28:11] is uh shape. So make sure that if you

[28:14] have expected or required fields, you

[28:17] have the required fields. Um the third

[28:19] thing is types. So uh you know if you

[28:22] have city, the city must be a string. Oh

[28:26] sorry. Yeah. Um yeah. So if you have a

[28:29] city, city is a string. Um if you have

[28:32] uh values, uh you know the units are in

[28:34] the appropriate units. So this can all

[28:36] be expressed through um something called

[28:39] JSON schema or basically any schema

[28:41] library. Um so it's like this is a city

[28:46] uh the type is string and the units can

[28:48] be uh Celsius or Fahrenheit and city is

[28:51] required.

[28:54] So um the the good thing about this is

[28:57] this has machine readable validation

[29:00] rules. So you can check if like a call

[29:01] uh follows the schema.

[29:04] But um

[29:07] one way that you can express whether the

[29:09] schema is valid or invalid is by

[29:12] defining a grammar over uh over the

[29:14] schema. And how many people uh did like

[29:18] contextf free grammarss or like context

[29:22] or those sorts of things? Regular

[29:23] grammarss. How many people know regular

[29:26] expressions?

[29:28] Okay. A lot of a lot of people. Okay. So

[29:32] a regular expression is a regular

[29:34] grammar. Um does anybody know how you

[29:37] can parse a regular expression?

[29:42] >> Finite state automaton. Yeah, that's

[29:44] exactly correct. Um so a finite state

[29:48] automaton uh for for those who are less

[29:50] familiar with this is

[30:04] something that looks a little bit like

[30:05] this.

[30:11] Um, so you have a state and every time

[30:15] you take a token as input, uh, you move

[30:19] to a different state. So if you get A,

[30:21] you would move to this state. If you get

[30:22] B or C, you move to this state. And

[30:27] This this works on uh something called

[30:30] uh uh regular grammarss. So regular

[30:34] expressions like the the slashes and dot

[30:36] stars and stuff like this that you might

[30:38] use to search for search text are uh reg

[30:42] are regular expressions and they can be

[30:44] expressed through regular grammars. Um

[30:47] JSON schema cannot be expressed through

[30:49] a regular grammar. um it can be

[30:52] expressed through something called a

[30:53] contextf free grammar and you can uh the

[30:57] context free grammar can basically make

[30:58] a tree that looks a little bit like

[31:00] this. So um every JSON expression can

[31:03] have brackets on the side. It can have

[31:06] commas between its members. Uh this can

[31:08] be a string um and this can be a unit.

[31:12] And if uh the JSON schema is in the

[31:16] correct format, you should be able to

[31:18] create a tree uh that looks like this.

[31:21] If the JSON schema is in the wrong

[31:22] format, you might create a be able to

[31:25] create create most of a tree. But then

[31:27] when you get to a unit, a unit cannot be

[31:29] K. So basically this would uh this would

[31:32] fail even though a unit can be K, but uh

[31:36] we we defined this to not accept Kelvin

[31:38] as our our unit of temperature.

[31:42] So

[31:43] um basically if you can parse uh the

[31:48] tool call with a contextf free grammar

[31:51] uh defined from your JSON schema you can

[31:54] uh you can do this and I'm not going to

[31:56] go into a lot of details but a finite

[31:58] state automaton cannot parse a um a

[32:01] contextf free grammar but there's

[32:02] something called a push down automaton

[32:04] that can allow you to do this. So

[32:06] basically it adds a stack to uh the

[32:10] regular grammar and uh you push things

[32:12] onto the stack uh pop things off of the

[32:14] stack and eventually can um eventually

[32:18] can decide whether it's uh parsible or

[32:20] not. And so what you do is you start out

[32:23] at the very beginning um with uh a state

[32:26] in this push down automaton and you step

[32:28] through and uh validate your output as

[32:34] you um as you generate it from left to

[32:36] right

[32:38] and I'm giving some examples from X

[32:41] grammar uh and X grammar is a thing

[32:43] that's actually pretty widely used in uh

[32:45] all of the LM inference libraries. It's

[32:48] actually developed by people in the

[32:49] machine learning department here. Uh so

[32:52] what you uh what this means is every

[32:54] time you get an LLM predict the logits

[32:59] of the next token, you take a look at

[33:02] your grammar and if the grammar says

[33:05] this is a valid next token, uh you get a

[33:08] score of one and if you have an invalid

[33:10] next token, you get a score of zero. And

[33:13] you set all of the invalid next tokens

[33:15] to negative infinity. um for the output

[33:18] logits and then you renormalize so that

[33:21] you get probability only on the valid

[33:24] tokens. And so what this uh lets you do

[33:27] is this ensures that you generate valid

[33:29] output.

[33:31] Um, and so

[33:36] this is another figure from the Xgrammer

[33:39] paper and they do these uh tricky things

[33:42] where basically there are some

[33:44] vocabulary that are always valid or

[33:47] always invalid and you premputee these

[33:50] and then there what there are those that

[33:52] are valid only in some contexts only in

[33:54] some uh stack context and then you

[33:56] calculate them on the fly. So it's uh

[33:58] very interesting algorithmically if you

[34:01] like algorithmic uh stuff. If you don't

[34:03] like it uh be glad that the people in

[34:05] the machine learning department are

[34:06] doing it for you basically. Um so

[34:09] because of this almost always um if you

[34:12] are uh if you are have this enabled you

[34:17] will uh and set your appropriate JSON

[34:20] schema you will get wellformed to tool

[34:22] calls. So that that's uh that's great.

[34:27] There's one case where you actually

[34:29] can't uh uh get well-formed tool calls

[34:32] despite this. Um may maybe I can give a

[34:36] quick quiz. This is very very difficult.

[34:38] So I don't know if anybody can get it.

[34:39] But any anybody have an idea where even

[34:41] this would not be uh not be enough. Need

[34:44] to be familiar with uh with LMS I guess.

[34:50] >> Yeah.

[34:58] Uh I I think that's close enough to what

[35:00] I I wanted to say. So basically um when

[35:02] you run out of tokens, so models can

[35:04] only generate so many tokens and you

[35:06] might run into a place where you're

[35:08] still on a valid path through the

[35:09] automaton, but you're not at the final

[35:11] state. So you generate like part of a

[35:13] JSON output. So very very good. Um and I

[35:17] I've actually encountered this. There's

[35:19] uh theoretically a way you could do that

[35:21] which is like you count the number of

[35:23] output tokens that you still have left

[35:24] and you you cut them off but that's uh

[35:28] if if somebody wants to implement that

[35:29] in next grammar as a extra credit

[35:31] assignment you know be happy to happy to

[35:34] have that okay so now um let's go to

[35:40] rest API calling um so there's uh two

[35:44] different ways to um there's different

[35:47] ways to Express

[35:49] tools and um I'd say probably most

[35:53] people are familiar with REST APIs. The

[35:55] these are the ways you interact with web

[35:57] services. Um but

[36:01] actually sorry there's one other way to

[36:03] call APIs and one way to call APIs is

[36:05] through programmatic tool calling where

[36:07] basically um you just give the model a

[36:09] Python program and you say use the stuff

[36:12] in this Python program to call tools.

[36:14] And so if you do something like that you

[36:16] might have like weather lib.py pi and uh

[36:19] you have the get weather function in

[36:21] here uh with its city and its units and

[36:25] uh then you just say call this function

[36:26] whenever you need to and you give it the

[36:28] ability to execute Python and it will be

[36:30] able to call that tool. So in

[36:32] programmatic tool calling this uh this

[36:34] works but this is not um callable

[36:37] remotely and it's also not callable from

[36:39] the like standard method of tool calling

[36:41] that you use um that you use when you

[36:47] uh implement this uh not through

[36:49] non-programmatic tool calling.

[36:52] So there's a way to turn this into uh

[36:55] REST APIs. Has anybody used fast API

[36:57] before? It's a pretty common Okay. a lot

[37:00] of people. It's a pretty common library.

[37:02] And basically what this allows you to do

[37:04] is this allows you to create a web uh

[37:07] web backend uh extremely simply by just

[37:11] uh setting up a fast API uh giving an

[37:14] API key so you can get people to

[37:16] validate against the API and then

[37:18] writing a Python decorator where uh

[37:21] weather becomes uh becomes this. And so

[37:26] this is good uh for a couple reasons.

[37:29] The first reason is maybe if you don't

[37:31] want people uh looking at the weather um

[37:34] then uh you can prevent them from

[37:36] looking at the weather. But probably

[37:37] more importantly if you don't want

[37:38] people like getting your personal data

[37:40] or something like that you can require

[37:42] an API key and uh this will uh allow you

[37:45] to block anybody who doesn't have an

[37:47] appropriate API key for instance. Um the

[37:51] other reason why is this gives you a

[37:55] JSON schema for free. uh and when I say

[37:57] for free of course you know this is

[37:59] something that's implemented in in fast

[38:01] API but your entire API can be expressed

[38:03] as a JSON schema and that JSON schema

[38:06] can then be provided as is to a language

[38:08] model and that language model can then

[38:10] use it uh to you know specify which

[38:12] calls are allowed and so then you could

[38:13] go in and process this and um whenever

[38:17] the agent made a tool call you could

[38:19] then send it to your API server and they

[38:21] it could use that on the API server

[38:24] Um,

[38:26] another option for calling these is you

[38:28] can just uh use the curl command. And

[38:31] the curl command um basically allows you

[38:33] to call these APIs uh directly like this

[38:35] as well. And so if you have a a coding

[38:37] agent that has access to bash, it has

[38:40] the ability to um to call like this.

[38:44] So this is maybe maybe reasonably

[38:47] straightforward if you're familiar with

[38:49] uh REST and stuff like this. Any any

[38:51] questions or comments or

[38:55] If you haven't played around with fast

[38:56] API, it's nice. It's very easy to use.

[39:00] But um the reason why I wanted to cover

[39:02] this first is this is kind of like the

[39:04] traditional way of of programming uh you

[39:07] know before agents. Um

[39:11] there's uh something called MCP the

[39:14] model context protocol and this was

[39:16] introduced by anthropic uh maybe twoish

[39:18] years ago or a year and a half ago and

[39:21] the idea was this is was designed to be

[39:24] a standard way to uh give your model

[39:28] additional context.

[39:31] When I first saw this I actually was

[39:34] like why do we need to do this? I don't

[39:36] understand why we need to do this. Let's

[39:38] uh let's just let our uh agents call

[39:40] APIs. Um but there is one uh important

[39:45] point about one one or two important

[39:48] points that make MCP different from just

[39:50] calling a normal API. Uh and I'll I'll

[39:53] explain them here. But um first I'll

[39:56] explain why I didn't real I didn't like

[39:59] I thought this was not actually

[40:00] necessary. And basically the reason why

[40:02] is every time you set up an MCP, what

[40:06] you do is you have your AI application

[40:09] and then you set up a couple MCP

[40:12] clients. So like maybe this is your

[40:14] weather client uh your this is your

[40:16] weather MCP and your uh your GitHub MCP

[40:19] or something like that. So you can ask

[40:21] what the weather is what the weather is

[40:23] and push it to your GitHub. Um uh and

[40:30] the reason why I didn't think this was

[40:32] necessary originally was because like

[40:34] why do you need to run a program to call

[40:36] an API, right? We already have good ways

[40:38] to call APIs. We just, you know, send it

[40:40] to the the REST API server.

[40:43] But um

[40:47] okay. Yeah. So so that's a little bit of

[40:49] an aside. Um, uh, I'll I'll get back to

[40:52] that in a moment, but for a little bit

[40:53] of an aside, uh, there's a really nice

[40:55] library called fast MCP. And fast MCP is

[40:59] basically designed to be fast API for

[41:01] MCP. So if you want to create an MCP

[41:03] server for whatever you want, you can

[41:06] um, just like basically swap out fast

[41:08] MCP and swap it uh, swap out fast API

[41:11] and swap in fast MCP and you can uh,

[41:13] create an MCP server very easily.

[41:16] Um, you can also take in a spec that was

[41:19] generated by like a REST API and just

[41:21] turn it in into an MCP as well.

[41:25] But here here's the main reason why you

[41:28] might want to use MCP uh as opposed to

[41:32] an API. Uh, and the reason why is

[41:36] because it gives you an extra layer of

[41:38] security. And so MCPs have an MCP

[41:43] API key. And this MCP API key uh is

[41:48] something that you need to provide to

[41:50] the process that's running your agent.

[41:53] Separately from this, you have the

[41:54] upstream API key. So like let's say you

[41:56] are getting um getting your agent to

[41:59] connect to your GitHub. The upstream API

[42:01] key would be your GitHub token and you

[42:03] would provide that to the MCP server,

[42:05] but you would not provide it to the

[42:06] agent. And then what you provide to the

[42:09] agent is the MCP API key, which allows

[42:12] you to authenticate into the MCP server.

[42:14] And so the reason why this is important

[42:16] is what happens if you give your agent

[42:18] the GitHub your GitHub token and your

[42:21] agent suddenly decides that it's a good

[42:23] idea to push that to your public GitHub

[42:26] repository.

[42:28] Not good, right? [laughter] Your account

[42:30] gets compromised and uh you get malware

[42:32] installed onto all your repositories or

[42:34] something like this. So you want to give

[42:36] the the agent something that is

[42:40] relatively harmless. Uh so that even if

[42:42] it leaks it for whatever reason like

[42:45] that leak is relatively harmless and

[42:46] then the um the actual credentials get

[42:49] get preserved and so that was basically

[42:51] the reasoning behind it.

[42:55] So um just to go into a summary, they

[42:58] all give you the ability to add a set of

[43:00] APIs into uh into your agent. Like you

[43:04] could do that through a regular JSON

[43:05] schema or through an MCP. Um

[43:09] the uh but a lot of other things are

[43:11] different. So like for discovery um you

[43:13] might need to fetch an open API uh

[43:16] document. For MCP there is a special API

[43:19] that allows you to list all of the

[43:20] tools. Um for invocation um you call an

[43:26] HTTP

[43:27] uh thing here for um MCP there's an MCP

[43:31] transport and this can be through

[43:33] various ways. You connect through

[43:34] standard IO or you connect through an H

[43:36] uh uh a socket or something like that.

[43:39] Uh I already talked about authentication

[43:42] and um MCP actually has a few other um

[43:46] has a few other like conveniences like

[43:48] you can add resources, prompts and

[43:50] extensions, but I'm not going to go into

[43:51] a lot of detail about that.

[43:56] Cool. Um

[43:59] actually, um there's two other things

[44:01] I'd like to mention. um there I don't

[44:03] want to uh I I guess I forgot to add

[44:08] them to my slide. Um so the first thing

[44:11] is um MCP registry. There's an official

[44:16] MCP registry. So if you want to find

[44:20] MCPS uh that allow you to do something

[44:22] like this, you can, you know, go to this

[44:24] registry and find uh any of a very large

[44:27] number of MCPS. There's also like a

[44:30] million and a half uh MCP server like

[44:34] websites that you can go to that are are

[44:36] ranked based on uh popularity and stuff

[44:39] like this. Another thing is um I've been

[44:42] talking a lot about the Pittsburgh

[44:43] weather and uh the funny thing is uh

[44:47] today I prepared all of these slides

[44:49] like earlier of course but today we

[44:52] actually got Pittsburgh weather that was

[44:54] simultaneously rainy and sunny at the

[44:56] same time. And so I managed to break my

[44:59] own API because it cannot return

[45:01] multiple states at the same time. But uh

[45:03] uh yeah, it was uh quite the

[45:05] coincidence. You can see the torrential

[45:06] downpour and the the bright side at the

[45:08] same time. Okay. Uh back back to serious

[45:12] stuff.

[45:16] Cool. Um so another big uh kind of like

[45:20] development pretty recently is parallel

[45:22] tool calling. in parallel tool calling.

[45:25] Um the the basic problem we want to

[45:28] solve is the same problem that I talked

[45:29] about when I talked about like the codec

[45:31] and the programmatic tool calling which

[45:33] is if you call tools one at a time. Um

[45:38] the uh it it could become very long for

[45:41] even a simple operation because you

[45:42] might do a weather and then do a

[45:43] calendar and then do a flight. Um, but

[45:47] if tool calls are independent, you can

[45:49] actually call them at the same time. And

[45:51] this is done pretty simply. You just

[45:54] like add add multiple tool call

[45:59] blocks to a single agent response.

[46:04] The um there's a few nuances about this.

[46:07] The first one is um you can only

[46:09] paralyze tool calls if they don't have

[46:11] dependencies on each other. So, um, like

[46:14] if you were looking up the weather for

[46:15] Pittsburgh and reading today's calendar

[46:16] and looking up flight status, that might

[46:19] be, uh, might be good. Um, but if you

[46:22] need to find a customer ID, use it to

[46:23] fetch orders and refund the selected

[46:25] order. Obviously, you can't do that. So,

[46:27] there's limits to the parallel tool

[46:28] calling you could do. And if your

[46:30] calendar or your flight was dependent on

[46:32] the weather, then you know, obviously

[46:33] that'd be a problem, too.

[46:37] So, there was a question about this. Um,

[46:39] do you execute the tool calls in

[46:40] parallel? And the answer is typically

[46:42] yes. You can just uh use typical Python

[46:46] uh syntax to you know have a whole bunch

[46:48] of tool calls and then execute them and

[46:51] then uh use something like

[46:52] async.io.gather to uh to return the

[46:56] results of them when they run in the

[46:58] same time. So this is uh uh this is

[47:01] pretty common. Another thing I'd like to

[47:03] point out is um this is a major

[47:07] difference between really efficient

[47:10] language models in note efficient

[47:12] language models. And

[47:15] there there's this weird

[47:18] weird paradox in agentic language models

[47:20] nowadays that more expensive models more

[47:25] expensive models can actually be cheaper

[47:27] if you measure them on a taskbytask

[47:29] basis. And there's two major reasons for

[47:31] this.

[47:33] The first major reason is more expensive

[47:35] models can be smarter. So they pick like

[47:37] an appropriate solution more quickly. Um

[47:40] but another thing is um more recent

[47:43] models

[47:45] do parallel tool calling uh a lot

[47:47] better. So they make a whole bunch of

[47:49] calls at the same time. So if you're

[47:52] using a coding agent or something like

[47:53] this, uh you use the the better uh you

[47:57] use the better models and they are doing

[47:59] like a bunch of view images at the same

[48:02] time or they're uh like writing a bunch

[48:05] of different files at the same time or

[48:07] something like that. That's because

[48:08] they're doing parallel tool calling.

[48:09] Well, um does anyone have an idea of

[48:12] like why they got so much better at

[48:14] this? They like this was not a huge

[48:16] thing even though parallel tool calling

[48:18] mechanisms have existed for a long time.

[48:20] This was not a huge thing until maybe

[48:22] like six months ago or something. Yeah.

[48:25] >> Reinforcement learning just forced them

[48:26] to do that.

[48:27] >> Yes. Exactly. So reinforcement learning

[48:29] uh kind of forced them to do that and so

[48:31] the models were very heavily

[48:33] incentivized to fish finish tasks

[48:35] quickly and parallel tool calling is one

[48:37] of the good ways to do that. So if you

[48:40] do reinforcement learning with a very

[48:41] heavy like brevity penalty on on how

[48:44] long uh the task execution is, you can

[48:47] get uh like a lot more parallel tool

[48:50] calling.

[48:53] Cool. So um the final thing I'd like to

[48:57] talk about in this lecture today is

[48:58] evaluating tool use. And so I'm not

[49:02] going to talk about evaluating endto-end

[49:05] agentic tasks immediately yet. um but

[49:08] rather talk about evaluating just the

[49:10] tool usability of language models

[49:12] because it's kind of like a prerequisite

[49:15] for language models to be good at um uh

[49:18] good at agentic tasks. And there's a

[49:22] bunch of data sets for this. The most

[49:24] famous one is the Berkeley function

[49:25] calling leaderboard and this has four

[49:28] versions. Uh it started out with version

[49:31] one which was basically um single turn

[49:35] uh tool calling. Um it's then evolved

[49:38] through the four versions and now it

[49:39] covers um multi-turn tool calling. It

[49:42] also does have aentic tool calling but

[49:44] this is more um not for like endto-end

[49:47] coding agents or something like that.

[49:48] It's uh tool calling agents and they

[49:51] also have tool calling robustness. So

[49:53] they measure um hallucination of

[49:55] arguments. They also measure format

[49:57] sensitivity. So when I talked about like

[49:59] the all the different formats uh they

[50:01] have uh parameters about that as well.

[50:06] So um

[50:09] when you uh go in to evaluate the whole

[50:11] uh stack there's a number of things that

[50:14] you want to uh evaluate. So the first

[50:17] thing is did the language model choose

[50:20] the appropriate tool for the task. So it

[50:22] might have picked like a an

[50:24] inappropriate tool that can't uh allow

[50:27] you to do that uh the task at all. Um

[50:30] the other thing is arguments uh which is

[50:33] uh you know whether you you add the

[50:35] right values. Um if you're talking about

[50:38] agentic tool calling you can talk about

[50:40] whether it did it in the right order and

[50:42] then you can uh measure endto-end task

[50:44] accuracy for if you're doing uh agentic

[50:46] tool calling. And all of these are kind

[50:48] of metrics in this leaderboard.

[50:52] Then separately from that there's also

[50:54] um efficiency. So like uh how quickly

[50:57] can you solve the task? Like um how many

[50:59] tokens did it take? How how much did it

[51:01] cost? Um reliability. So um you know if

[51:06] a tool call times out uh does it retry

[51:10] appropriately? If a tool is out of

[51:12] order, can it choose a a different one?

[51:15] And also um safety. So if you have

[51:17] adversarial outputs where you ask it to

[51:20] use a tool in an inappropriate way, uh

[51:23] can you do this? And all of these are

[51:24] like over the four iterations of this

[51:26] benchmark. It covers uh all of these

[51:28] dimensions.

[51:32] Um yeah, I kind of covered that already

[51:34] actually. So one other uh really

[51:37] interesting benchmark uh for tool

[51:39] calling is uh this open router uh tool

[51:43] call air rate benchmark. I don't know if

[51:45] anybody like uses open router or has

[51:48] seen this before. Maybe no.

[51:51] Okay. So um this is for the same model.

[51:56] All of these are for uh I think this is

[51:58] GLM 5.3. So it's like the same the same

[52:02] model and it's measuring the tool call

[52:04] error rate

[52:07] simply the only thing they varied is who

[52:10] serves the model to you. And this is uh

[52:14] this is pretty important obviously

[52:16] because you think oh I'm going to use

[52:18] this model maybe you know it's going to

[52:20] be the same regardless of who provides

[52:22] it to me but actually the difference is

[52:24] between 15% and like 0.01

[52:28] to 0.05%.

[52:30] Any idea uh why this might be?

[52:40] There were some uh there were some hints

[52:42] in the lecture and some uh not some

[52:44] hints in the lecture

[52:45] >> is decoding algorithms different maybe

[52:47] someone's using

[52:50] like cheaper version of the model or

[52:52] quantized version of the model.

[52:54] >> Yeah, great great points. So I'll I'll

[52:56] repeat it. So number one is the decoding

[52:59] or the inference algorithm could be

[53:00] different and um one very big difference

[53:03] is whether they're using quantization of

[53:05] the model or not or like what level of

[53:07] quantization of the model they're using.

[53:09] So my my personal experience is um uh

[53:14] FP8 models uh FP8 is kind of like the

[53:17] default level of uh quantization for the

[53:19] model um get a lot fewer uh mistaken

[53:23] tool calls than FP4 models because FP4

[53:26] is like compressing it very heavily.

[53:28] It's saving money for the inference

[53:29] provider, but it's it's usually a worse

[53:33] model. There aren't very many FP4

[53:35] quantizations that can allow you to get

[53:37] the same performance. Another one was uh

[53:40] speculative decoding. Um I don't think

[53:42] we're going to talk about speculative

[53:43] decoding a huge amount in this class.

[53:45] Maybe I'll talk about it during long

[53:46] context or actually may there are a few

[53:50] algorithms specifically for agents which

[53:52] are interesting. So maybe we can talk

[53:53] about it. But basically what it is is

[53:55] you have another cheaper model um that

[53:58] predicts what the more expensive model

[54:00] is going to do and then you use that to

[54:02] like speed up your inference.

[54:04] um spec lossless speculative decoding

[54:08] probably shouldn't make a difference

[54:10] because it it's like not changing the

[54:13] underlying result of the model. But if

[54:15] they're doing some sort of like lossy

[54:16] speculative decoding uh then that might

[54:19] might cause it to be different. But then

[54:20] you know calling it the same model is

[54:22] also probably a bad uh a bad idea. Uh

[54:25] there's one other thing um that I

[54:27] mentioned uh and anybody have an idea

[54:31] this was actually mentioned in the uh in

[54:34] the class today.

[54:43] What can you do to make your tool calls

[54:46] more successful?

[54:48] >> Yeah.

[54:50] >> Constraint decoding. Yeah, exactly. So

[54:52] these different providers might be using

[54:54] different constraint decoding

[54:56] algorithms. Um just practically

[55:00] many many of these providers will be

[55:03] implementing their own inference

[55:05] algorithm. So they'll have their own

[55:07] inference algorithm completely

[55:08] implemented from scratch. Um some of the

[55:12] providers will be using an open source

[55:13] one like VLM or SGLANG. And VLM or SG

[55:16] lang support different grammar-based

[55:18] decoding uh algorithms. And so uh some

[55:22] of these providers just might not have

[55:24] that implemented and so they're entirely

[55:26] relying on the language model to do good

[55:28] tool calls. Um otherwise uh they might

[55:31] not. A final kind of like boring reason

[55:33] why tool calls might fail is the

[55:35] inference provider might be unreliable.

[55:37] So it might go down some of the time and

[55:39] then the tool call would fail.

[55:43] Cool. Um so these are the um that that's

[55:47] the main thing that I I had for today.

[55:49] Um so tool use is basically a layered

[55:51] system. Um you know the tools add

[55:54] capabilities such as retrieval,

[55:56] execution, generation, application.

[55:58] They're what make an agent an agent. Uh

[56:01] but we can't get that uh for free. And

[56:04] um you can uh add schemas to the prompt.

[56:08] Uh the models emit calls and then you

[56:10] validate dispatch and match results by

[56:13] ID. And we can add constraints uh like

[56:16] grammar-based decoding. um they don't

[56:18] guarantee semantic correctness. So um if

[56:21] you have like a Python program, the

[56:22] Python program might still be wrong even

[56:24] if you generated uh you know a string

[56:26] that could be parsed as Python. Um and

[56:29] there's a number of uh ways you can

[56:31] interface with them like direct rest

[56:33] calls and MCPS.

[56:35] Uh and then we have a lot of systems

[56:37] that um orchestrate dependencies and

[56:39] concurrency and uh allow us to evaluate.

[56:43] So yeah, that that's uh what I wanted to

[56:46] talk about for tool calling. Uh this

[56:48] will be something that is covered in the

[56:50] harness uh assignment or the first

[56:51] assignment where you build your agent.

[56:53] So you'll need to need to deal with

[56:54] this. Um but and next time we're going

[56:58] to talk about context management for

[56:59] long context in long context LMS. But um

[57:03] any questions

[57:05] to wrap up?

[57:07] Okay. Yeah. Yeah. And I'm going to

[57:08] repeat in case people didn't hear in the

[57:10] back, but the first um uh assignment for

[57:13] reflecting on the lecture and talking

[57:15] about something you learned in the

[57:16] lecture is going to be up on Canvas. So,

[57:18] make sure you uh make sure you submit

[57:20] it. Thank you.
