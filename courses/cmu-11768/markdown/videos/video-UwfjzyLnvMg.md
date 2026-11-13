# Lecture 1 recording

[Course index](../../README.md) · [Original source](https://www.youtube.com/watch?v=UwfjzyLnvMg&list=PLSN0qpDfUvTM&index=1) · [Raw file](../../raw/videos/UwfjzyLnvMg.json)

Retrieved: 2026-11-13T16:48:22.297665+00:00

[00:00] Okay. Um, hi everyone. Welcome to 11768,

[00:05] uh, AI agents. We're very excited to be

[00:07] teaching this new course, uh, which is

[00:11] timely as, uh, a lot of people are

[00:13] starting to use agents. Um, my name is

[00:16] Graham Nubig. I'm an associate professor

[00:18] in the school of computer science here.

[00:20] I've been working on agents for maybe

[00:23] uh, several years now. Uh, coding

[00:25] agents, web browsing agents, uh, those

[00:26] sorts of things. and I'll be co-eing

[00:29] together with Daniel who will be kicking

[00:31] off this class. So without further ado,

[00:34] I'll turn it over to him and he can

[00:36] start uh this and I'll I'll do the

[00:38] second part of the class.

[00:40] >> Thanks Graeme.

[00:42] How's this?

[00:45] Cool. Yeah. So um hi everyone. Really

[00:48] excited that you're here. My name is

[00:49] Daniel Freed. Um my research group also

[00:52] works on agents. Um so uh grounded

[00:55] agents and also interaction between

[00:57] people and agents and these days

[00:59] interaction between agent systems. So uh

[01:02] excited to talk about um all these

[01:04] topics with you and um yeah we have a

[01:07] really great core staff too who we will

[01:09] introduce in in a few slides. But yeah

[01:13] so agents are are really timely right

[01:15] now and um the capabilities of agents

[01:18] are advancing pretty quickly. So

[01:20] probably a lot of you are using coding

[01:22] agents in your you know day-to-day work

[01:25] and we've seen some big success cases of

[01:28] agents. So um one example is there was

[01:31] this uh nice experiment um by um Carlini

[01:36] at anthropic that

[01:39] saw could we develop a really complex

[01:42] piece of software using um a multi- aent

[01:45] uh configuration of a a recent coding

[01:48] model. And this was pretty successful.

[01:50] So 16 agents collaborated together over

[01:53] two weeks and constructed a rustbased C

[01:56] compiler which was able to compile the

[01:58] Linux kernel. And you've probably you

[02:01] know been using agents effectively in

[02:02] your own work and and seen how much

[02:04] better they've gotten especially in the

[02:06] last like year or so. There's

[02:08] limitations of current agents too. So

[02:11] how many folks have uh tried uh using an

[02:14] agent that controls your computer like

[02:16] controls applications or Okay. So, a lot

[02:18] of folks have How many uh folks have

[02:20] used OpenClaw?

[02:22] Yeah. So, we have a number of folks,

[02:24] too. Um, there was this pretty

[02:26] high-profile incident involving OpenClaw

[02:29] um which got posted on Twitter by the

[02:31] the person who ran into this where she

[02:34] was asking the model to organize her

[02:36] inbox and the model kind of went out of

[02:39] control and started deleting old emails.

[02:42] And uh so she's trying to intervene. She

[02:44] says, "What's going on? Can you describe

[02:46] what you're doing?" But the model says,

[02:47] "I'm taking the nuclear option. I'm

[02:49] going to trash everything in the inbox

[02:51] that isn't already in my keep list." And

[02:53] the user is trying to intervene, saying,

[02:54] you know, do not do that. Um, but the

[02:57] model goes on to delete a lot of this

[02:59] really valuable information. And at the

[03:02] end, it acknowledges uh that, you know,

[03:05] I learned my lesson. I'm not going to do

[03:07] this in the future. And I do remember

[03:09] that she told me this, um, but I

[03:11] violated it. So, what happened behind

[03:14] the scenes here? Well, it seems that it

[03:16] was the model compacted its past

[03:18] context, which is a way that we'll cover

[03:20] in this class of uh of reducing the past

[03:23] history so that the model is able to

[03:25] take in more um interactions with the

[03:28] environment, but that caused it to lose

[03:29] this instruction to not delete emails.

[03:33] So, models are getting much more

[03:35] capable, but they also still have really

[03:37] rough edges. And a lot of this class is

[03:38] going to be about how do you develop

[03:40] these capabilities and models starting

[03:42] from base language models but also what

[03:44] are the research problems and what are

[03:46] the remaining gaps that we need to fill.

[03:49] So let's just uh try to get a sense of

[03:52] what people think agents are are good at

[03:54] these days. So we have like six

[03:56] different tasks that you might want to

[03:58] try to use an agent for. And these are

[04:00] pretty subjective. I just want to get a

[04:02] sense of like what might you be

[04:03] comfortable with. Um, so let's do a show

[04:05] of hands for a task like say you have an

[04:08] online store like some uh code

[04:11] application that hosts a store for you

[04:13] and it started failing. You want to use

[04:14] an agent to try to diagnose that. How

[04:17] many people would be comfortable with

[04:19] having an agent carry this task out like

[04:21] fully on its own? Can we get a show of

[04:23] hands? Okay. Yeah. Um, how about having

[04:28] the agent like ask first as it's

[04:31] carrying out this task? Maybe asking you

[04:32] for help. How many people think that

[04:34] might be necessary?

[04:37] Okay. And how many folks think that this

[04:39] would just not be something that you

[04:40] would ever want an agent to touch at

[04:42] all?

[04:43] Okay. So, for this one, I think we had

[04:45] more autonomous.

[04:47] How about drafting and sending a product

[04:50] launch email to 50,000 customers? So,

[04:52] how many people are okay with this being

[04:54] fully autonomous?

[04:56] Okay, we got some brave souls. Um, how

[04:59] about asking first?

[05:01] Okay. And how about an agent shouldn't

[05:04] do this at all. I want to be responsible

[05:06] for it. Okay, so I think this one was

[05:08] was asked first. How about um collecting

[05:11] your tax forms and preparing and filing

[05:14] your 2025 tax return? Fully autonomous.

[05:19] Okay. Yeah.

[05:22] How about ask first?

[05:25] And how about never?

[05:27] Okay. Yeah. So I think this had the most

[05:29] never of anybody but ask first probably

[05:32] one migrating a payments API from Python

[05:36] to Rust. Say maybe you have some test

[05:38] cases that were written for the

[05:40] application in Python that you can apply

[05:42] to the Rust version. How many people

[05:44] would be okay with this being

[05:45] autonomous?

[05:47] Okay, how about ask first?

[05:50] Yeah, that was very close. I don't know

[05:52] which one was more and never.

[05:56] Okay. So, we'll uh let's uh have this be

[05:59] one for the agents. Autonomous. Buy

[06:01] concert tickets to my favorite band if

[06:03] they set up a show in an area in my

[06:06] area. Autonomous.

[06:09] So, you'd be okay with the agent buying

[06:10] the tickets, too, if it finds good ones.

[06:13] I think that one probably won. And how

[06:15] about this last one? Adjusting an

[06:16] insulin dose after a week of glucose

[06:19] readings. So, an agent like, you know,

[06:21] has all the like the capabilities to do

[06:24] this. Like if you're feeding it your

[06:26] health information, um it could monitor

[06:28] that. If you give it access to like

[06:30] something that can change a prescribed

[06:32] dosage, it could do that too. How many

[06:34] people would be comfortable with this

[06:35] autonomously?

[06:38] Okay, asking first.

[06:41] And how about never? Okay, so yeah, so

[06:44] that one was never, although I was

[06:45] thinking maybe it would be ask first. So

[06:48] cool. So I think you're all you all kind

[06:50] of have a sense of some of the

[06:52] boundaries that agents have. Although

[06:54] you know there's a lot of these tasks

[06:56] where we might just not be sure. Um but

[06:59] you also have a sense that like trust is

[07:00] important and later on in the class when

[07:03] we talk about like sandboxing and um

[07:06] security and um interaction and

[07:08] oversight by people um we'll get into

[07:10] these a little bit more.

[07:15] Okay. So just to give like a very brief

[07:17] kind of uh tour of how agents have

[07:20] extremely brief. It's just two slides.

[07:22] how agents have progressed over the past

[07:23] few years. Um, and also to motivate some

[07:26] of the things that we'll see later on in

[07:28] the course. Um, so we've been doing some

[07:30] work on guey agents, like agents that

[07:32] can use computer applications here at

[07:34] CMU over the past few years. This is

[07:36] work from a lot of um, faculty. Um, and

[07:40] um, here's a demo that was made by um,

[07:42] one of our students, JY Co, um, two

[07:45] years ago showing an agent in action

[07:47] controlling the browser.

[07:50] And so you give it a task like navigate

[07:52] to the page of a good Thai restaurant in

[07:53] Pittsburgh. It should have at least 200

[07:55] reviews and 4.3 stars. And on the right

[07:58] here you can see, sorry it's a little

[07:59] fuzzy, but you can see the interactions

[08:01] with the language model like the chains

[08:03] of thought that are being produced. And

[08:04] on the left here, the model is

[08:06] controlling the browser um typing in the

[08:09] search box on Yelp and then navigating

[08:11] to this page. Fusidities is a really

[08:13] good Thai restaurant. Um and so that's a

[08:15] success and we've seen um you know

[08:19] frameworks and agents like this really

[08:20] taking off over the past few years with

[08:22] like um Manis and um OpenAI's operator

[08:26] cloud computer use agent and so on.

[08:29] And we've also done a lot of work uh

[08:31] here at CMU on building coding agents.

[08:34] Um uh Graham's group in particular has

[08:36] done a lot on this and also um through

[08:39] open hands which develops um open-

[08:41] source um agents. Um and uh here's a

[08:44] demo video uh from Graham which I'll uh

[08:47] play showing the agent like both writing

[08:50] code um but then also interacting with

[08:52] the application that it's built in the

[08:54] browser to test it out.

[08:56] >> To-do list app in list.

[09:01] >> So this will take a little while for the

[09:02] agent to work. Um, we can watch it work

[09:05] over here and see that it has uh made a

[09:08] directory for static files and templates

[09:12] and it has created the main app file. We

[09:15] can look at the changes it made to the

[09:17] app file uh by clicking over here in the

[09:19] changes tab which shows us all of the

[09:21] things it implemented. So that's kind of

[09:23] nice feature. So you can kind of watch

[09:25] uh what the agent is doing while it's

[09:27] working. and it's [music] editing the

[09:29] index file, the style file to make the

[09:31] app look nice.

[09:34] Uh requirements.ext to make it easy to

[09:36] install and adding a read me. So you can

[09:39] see it's kind of following good uh

[09:41] coding practices. And now it will start

[09:44] up the app. [music] And so it's running

[09:47] uh very very quick. And what I can say

[09:50] is let's run in the background

[09:55] and then [music] test out with your

[09:58] browser.

[10:01] And so if I do this, it will uh run the

[10:04] app in the background.

[10:08] [music]

[10:09] And it checked if the app is running.

[10:10] And now it should navigate there with

[10:12] its browser.

[10:21] uh it's checking the log and saw the

[10:22] port was already in use and it's trying

[10:24] it out. So that that's kind of the nice

[10:26] thing of agents. They can debug their

[10:27] own problems and uh and

[10:30] make sure that things work. So, okay, it

[10:32] should be working now.

[10:37] [music]

[10:41] And you see it browsed to the app. And

[10:42] we can see our tuning list app over

[10:44] here. And it sees that it's running, but

[10:48] now it wants to test the functionality.

[10:50] So, what we can do is we can see that it

[10:52] uh went through and it filled in uh buy

[10:56] groceries and it clicked. And you can

[10:57] see that uh in real time it's testing

[11:00] out your app and then it also is uh

[11:03] testing the delete functionality and

[11:05] other stuff like this. So I find this

[11:07] really exciting. I'm not, you know, the

[11:08] best front-end developer, but it's able

[11:11] to kind of [music] try out the front

[11:12] end, see if the functionality is working

[11:15] and fix any issues on the fly. And I

[11:18] even had one time where the app crashed

[11:20] and the agent realized that the app

[11:22] crashed even before I did and it was

[11:24] able to go in and fix the problems.

[11:26] So this is as simple as just saying, you

[11:28] know, go and develop an app and then

[11:30] test out if it works and you don't

[11:32] really need to do anything else. So now

[11:34] we're done. Uh let me stop this. In a

[11:36] real scenario, what I would do next is

[11:38] I'd ask it to push it to GitHub and uh

[11:42] you know finish it up so that I can

[11:43] continue working on it.

[11:46] >> Yeah. So we're excited to give you

[11:48] hands-on experience building agents um

[11:50] in this class. And in one of the

[11:52] lectures later on in the course, we'll

[11:54] cover open hands and its um SDK and how

[11:58] you can um uh develop agents of your own

[12:01] like this.

[12:03] So we um have a really great core staff.

[12:06] We have uh our our core staff all does

[12:09] research in these areas. um wrote some

[12:12] of the foundational papers and uh we'd

[12:15] love to have you all come up uh and uh

[12:18] introduce yourselves and um at the end

[12:21] of the course you'll be getting to work

[12:23] on a mini research project of your own

[12:25] and um we'll be uh getting guidance from

[12:29] the entire core staff um helping you out

[12:31] with that. So um yeah, if we can just uh

[12:34] go through and have each of you maybe

[12:36] just project uh and introduce

[12:38] yourselves.

[12:39] >> Yeah. So the yeah say it so the people

[12:41] in the back can hear like what what your

[12:44] research is on because uh then the

[12:46] people here can like essentially know

[12:49] what you're working on so they know

[12:50] which TA to talk to when you're working

[12:51] on like a project in that area for

[12:53] instance.

[12:54] >> Yeah.

[12:55] >> Hey everyone I'm a third year PhD

[12:58] student. I'm advised by Grant and Kamar.

[13:01] Um my research areas are focused on

[13:04] training agents to better leverage

[13:06] interest and compute and also organized

[13:08] in multi- aent systems.

[13:11] >> Hi everyone. Uh my name is Adita. I'm a

[13:14] first year Ph student uh working in the

[13:16] professor program. Uh my main research

[13:19] interests are like designing reward

[13:20] functions for like agent reinforcement

[13:22] learning. I particularly work on code

[13:24] generation for for now.

[13:27] Um hi everyone my name is and I'm a

[13:31] second year PhD student working with

[13:34] professor Anna Yeah and my current

[13:37] research focus is [clears throat]

[13:39] learning and

[13:42] research

[13:44] >> hi everyone I'm

[13:47] here working with the previous of

[13:51] working on mobility agents and

[13:54] recently I've been working on

[13:58] Hey uh I'm Sus. I'm a PhD student

[14:01] working with Daniel. Uh I work on how we

[14:03] can train agents to communicate more

[14:05] efficiently with people.

[14:08] >> Hi, I'm Lily. I'm a Syria business

[14:09] student by EMU. So I'm work on training

[14:13] on agents on authorizing coffee and

[14:15] battery.

[14:18] >> Uh hey everyone, I'm Andy. I'm a fourth

[14:20] year PhD. I work with Daniel and Monop.

[14:23] Uh I mainly work on alignment post

[14:25] training and also multi-agent

[14:26] introductions.

[14:28] >> Thanks everyone.

[14:33] [applause]

[14:35] >> Yeah. So uh like Graham said, we

[14:37] definitely encourage you as you're

[14:38] starting to think about your projects

[14:40] later on in the course, uh we'll talk

[14:42] about the course structure towards the

[14:43] end, but as you're starting to think

[14:45] about the projects that you want to do,

[14:46] TAS are going to be a really great

[14:48] resource for you to go to in office

[14:49] hours and get their expertise.

[14:52] So, we're also really grateful to um uh

[14:55] several really awesome startups for uh

[14:57] donating uh compute which you will be

[14:59] able to use in the assignments and

[15:01] projects for the course. Um and uh

[15:04] without their support uh we wouldn't be

[15:06] able to run um this at the scale that we

[15:09] would like to. So, we're really grateful

[15:10] to fireworks AI to modal um to prime

[15:14] intellect and to sale for uh helping to

[15:17] support uh this semester.

[15:22] Okay. So today we'll give a brief

[15:24] overview of what an agent is and um then

[15:27] we'll talk about uh the plan for the

[15:30] class and how things will be structured.

[15:33] So an agent um agents have been around

[15:37] for a long time. The concept of an agent

[15:39] and um work developing agentive

[15:41] capabilities um isn't just you know a

[15:44] two or three year old thing. So, uh,

[15:46] Russell and Norvig in their foundational

[15:49] textbook on AI, um, define an agent as

[15:53] anything that can be viewed as, uh,

[15:54] perceiving its environment and acting

[15:57] upon that environment. And that's really

[16:00] true for the agents that we have now.

[16:01] And um, a lot of the techniques that

[16:03] were developed for agents in the past,

[16:05] not all, but a lot of them will apply to

[16:08] current agents too, especially things

[16:09] like search reinforcement learning. So,

[16:13] uh, how does this pan out for our

[16:15] current agents? So, agents are going to

[16:17] be situated in an environment, which

[16:19] could be something like a code

[16:20] repository, a website, um, some other

[16:23] application on your computer, and

[16:26] they'll be interacting with that

[16:28] environment by getting observations of

[16:30] the current state that they're in in the

[16:33] environment. So that's something like

[16:36] messages from the user they're

[16:38] interacting with, the contents of a file

[16:40] that they're um investigating, the

[16:43] current web page that they're on,

[16:44] screenshots, or as we'll focus on in a

[16:47] few slides, the results of um tools

[16:51] which are you like programmatic

[16:53] functions that they can execute in the

[16:55] environment to interact with it.

[16:58] And they're taking actions at each point

[17:01] in time. um which is going to these

[17:03] actions will update the environment and

[17:05] then change the state that the agent is

[17:07] in. So that could be something like

[17:09] replying to the user or editing a file

[17:12] or running a command in the shell or

[17:14] calling an API that backs the web pages

[17:16] that they're interacting with.

[17:19] And finally, there's also this notion of

[17:21] reward. So how do we define whether the

[17:24] agent was successful or not using a

[17:26] numeric score? And we could define this

[17:29] as like if there are some test cases for

[17:31] a codebase, do those pass? If they do,

[17:34] then you get a one, otherwise you get a

[17:36] zero. Uh for other tasks, it can be

[17:39] difficult to like have sort of a

[17:41] programmatic reward. So we might need to

[17:43] rely on an LLM as a judge to uh evaluate

[17:47] whether this was successful or not. In

[17:49] your second assignment, you'll be

[17:50] developing LLM as a judge based

[17:52] evaluation approaches among other eval.

[17:56] And maybe we're ultimately interested in

[17:58] did we, you know, make the user happy

[17:59] with the task that they asked the agent

[18:01] to do. So we could also use feedback

[18:02] from the user for that. And I think in

[18:05] our uh human interaction lecture that

[18:07] Valerie Chen is going to be giving a

[18:09] guest lecture later on, we'll talk about

[18:11] this.

[18:14] So we asked all of you to have prior

[18:16] experience training language models and

[18:19] um given that experience you should all

[18:21] be familiar with um language models um

[18:24] doing next token prediction right so at

[18:27] each step um the agent is going to

[18:29] predict a distribution over the next

[18:30] token um we'll sample or in some other

[18:34] way choose one of those tokens from that

[18:36] distribution um insert it into the

[18:39] context window of the model and repeat

[18:41] this um over over and over again. And

[18:44] recently we've uh seen a lot of a lot of

[18:48] improvements on uh complex reasoning

[18:51] tasks by introducing chain of thought to

[18:53] these models. So as um as you should

[18:57] remember a chain of thought is um

[18:59] predicting a sequence of tokens um which

[19:02] aren't the final answer that we want the

[19:04] model to output but do allow it to um

[19:06] sort of have a scratch pad um for its

[19:09] intermediate uh reasoning steps which it

[19:12] can then um use um and condition on to

[19:15] predict the final answer. And so this is

[19:19] like a non-aggentive setting, right?

[19:20] This is just the agent um interacting

[19:23] with prompts that you give to it. So how

[19:26] do we go from this to um having models

[19:28] that can take actions in the world?

[19:31] So the main way that we do this is

[19:34] through tools. So a tool is something

[19:37] that's situated in the environment um

[19:40] which will uh provide an interface for

[19:42] the model to interact with that

[19:44] environment. And you could think of this

[19:46] as being like um an API for example like

[19:49] if we want the model to be able to uh uh

[19:52] find out what the weather is so that it

[19:54] could respond to a user asking about

[19:56] that maybe we have um an API for like

[20:00] you know weather.gov which is wrapped in

[20:02] an interface that allows the model to

[20:04] call it. So there's a bunch of different

[20:06] ways to represent this interface. Graham

[20:08] will be covering them in more detail I

[20:10] think in the next lecture but here's one

[20:12] example. This is the open AI um tool

[20:14] specification where um for a given tool

[20:18] aka function that the model can call.

[20:20] You'll have a name for that tool um a

[20:23] natural language description of what it

[20:25] does. So for example, read file might be

[20:28] a tool that a coding agent uses to uh

[20:30] look at files in the repo that it's

[20:33] acting in. We'll also need to tell the

[20:36] model what it can pass to this function.

[20:38] So we'll have a description of um the

[20:40] parameters that it takes like maybe this

[20:43] function just takes a path which is a

[20:45] string you know for the file to open. So

[20:48] we have to uh so we have the name and

[20:50] description we have some structured

[20:51] representation of the interface to the

[20:54] function which here is JSON and um this

[20:58] also needs to get fed into the model in

[21:01] some way. So we'll have um this you know

[21:04] underlying specification of the tool and

[21:07] then the model will view it by applying

[21:10] this template which turns it into a

[21:12] sequence of text which will then be

[21:14] tokenized and read by the OM which uh

[21:17] might look like this and the model will

[21:20] have to be um uh sort of either trained

[21:23] or with few examples um know how to use

[21:26] these tools.

[21:28] So this is how the model becomes aware

[21:30] of the tools that it can use to interact

[21:32] with the environment. But the model will

[21:35] also be needing to use those tools to

[21:38] interact and it does this through tool

[21:41] calls. So for example generating text

[21:44] like this like tool call and then you

[21:47] specify the name of the function that

[21:49] you want to call and the arguments as

[21:51] well if you're using sort of a JSONbased

[21:53] representation. Can anybody make a

[21:56] suggestion for another way that you

[21:58] might have the model call tools?

[22:04] Anyone?

[22:07] Let's Yeah, in the back.

[22:14] >> Yeah, you could just write code

[22:15] directly. for example, bash scripts or

[22:18] if you represented this as a Python

[22:20] function, the model could just, you

[22:22] know, call the function using Python

[22:24] syntax. And we'll see in a couple

[22:25] lectures that that's actually a very

[22:27] effective and often more effective way

[22:29] than generating JSON. Um, but there's

[22:31] some trade-offs, too. So, when the model

[22:34] calls the tool, it'll get back results

[22:36] from executing that tool in the

[22:38] environment. So for example, if we're

[22:40] reading um this test file, maybe that

[22:43] test file has this code for an add

[22:46] function in it and um the environment

[22:48] will return um you know the results of

[22:52] that tool in this content field and then

[22:54] that'll be rendered to the model using a

[22:56] template um which the model will then

[22:58] read in as tokens and get to continue

[23:00] producing output. Any questions about

[23:02] this?

[23:07] Cool. So now that we kind of have like

[23:10] the basic tool interface, we're able to

[23:12] um have the language model use these

[23:14] tools to act in the environment. So the

[23:17] way it does this is just by reading in

[23:19] these token sequences that represent

[23:21] what tools are available um uh that

[23:24] represent uh the results of tools and

[23:27] then um generating token sequences

[23:29] naming the tools which then invokes

[23:31] them.

[23:33] And so this uh we have this distinction

[23:36] between the language model itself which

[23:37] is just you know interacting with tokens

[23:40] um later on we'll talk about multimodal

[23:42] language models which maybe also take in

[23:44] images or other modalities. Um so the

[23:47] language models just tokens in and

[23:49] tokens out maybe multimodal tokens but

[23:51] then there's this harness which is

[23:53] responsible for actually um coordinating

[23:56] um these tool calls um using the

[23:58] language model as an engine for it.

[24:03] And so the agentive loop basically and

[24:06] tool former was a really impactful paper

[24:08] that showed that you can train models to

[24:10] be able to use tool calls and then

[24:12] condition on the results of those to um

[24:15] make future text more likely and showed

[24:18] an early way that you could train these

[24:19] models to use tools um that generalized

[24:22] prior LLM training procedures.

[24:25] So once you have this basic setup that

[24:27] you then can implement an agent by

[24:29] running um a loop um and one of the

[24:32] influential papers here was called react

[24:35] um from 2023 um which stands for

[24:37] reasoning and acting because the model's

[24:39] producing chains of thought and then

[24:40] taking actions afterwards and the way it

[24:43] works is you'll have some uh context um

[24:47] which you know includes maybe a

[24:49] definition of the general task of

[24:51] solving pull requests on GitHub or solve

[24:54] issues on GitHub. We'll see some

[24:55] examples of this in a bit. Then you have

[24:57] a task which is maybe an initial query

[25:00] from the user. Um you'll also have a

[25:03] list of all the tools that are available

[25:05] for the agent to call which will be

[25:06] represented using one of those formats

[25:08] that we showed. And you'll also have a

[25:10] history of the past um observations and

[25:13] actions that the agent um has produced

[25:16] and observed as it's been interacting.

[25:19] And in each uh at each time step um so

[25:22] for a given particular state the agent's

[25:24] in it's going to condition on all of

[25:26] that produce a reasoning chain um you

[25:29] know chain of thought um with a scratch

[25:32] pad about what it should do and then

[25:34] produce um one or more tool calls that

[25:36] will be used to interact with the

[25:38] environment or with the user. So for

[25:40] example reading the file. So that tool

[25:44] call will get executed in the

[25:45] environment. We get the results. We add

[25:47] those results to the history and um the

[25:50] environment is also getting updated as a

[25:53] result of our tool call and then we

[25:55] repeat the process again. So the model's

[25:56] conditioning on this updated history and

[25:59] you know the observations that it gets

[26:01] from this time step and then issues a

[26:03] new tool call and it repeats over and

[26:05] over. We could also have tool calls that

[26:08] end the task that for example send a

[26:10] message to the user um or otherwise

[26:13] signal completion. Um and uh so this is

[26:16] a way that we can you know signal that

[26:18] we are finished. And in the planning

[26:19] lecture we'll talk a little bit about

[26:20] like how might a model determine that

[26:23] it's done.

[26:25] So I won't get into the details of this

[26:27] too much. Um you'll get into it when you

[26:30] do assignment one which asks you to

[26:32] implement a um react style loop to uh

[26:37] implement a small coding agent and use

[26:39] it to solve problems in a repo um a a

[26:42] chess engine repo actually. So there's

[26:44] some fun demos that go with it too. Um

[26:47] so we won't get too much into the

[26:48] details of this and the code that you

[26:50] will write will look different than this

[26:52] but you know at a high level this is a

[26:54] very simple implementation. This is an

[26:57] excerpt from this nice minimal repo

[27:00] called mini sui Asian um which actually

[27:03] gets very high performance um on the

[27:07] bench benchmark which we'll talk about

[27:09] in a few lectures. It's a very standard

[27:12] um benchmark for coding agents. Um but

[27:15] it's a really nice repo that I'd

[27:17] encourage you to take a look at because

[27:19] um it's um effective with recent models,

[27:22] but it's also pretty simple and really

[27:24] kind of distills um you know the the

[27:28] distills the basics down. Um but you'll

[27:31] uh start off by having some messages uh

[27:33] which give the model context about it

[27:35] being an agent and about the task. And

[27:38] then you'll just uh run this loop over

[27:40] and over again that implements what we

[27:42] had on the past slide where the agent

[27:44] will um issue a query to a language

[27:46] model using all of the past u messages

[27:49] which contain the history um and then uh

[27:53] it'll add that message to the history

[27:55] and um execute um the uh execute uh the

[28:02] actions in the environment. And we've

[28:04] left this off, but you can take a look

[28:06] at the code repo if you're interested.

[28:08] Execute the actions, get the

[28:09] observations, and um return them.

[28:14] So, I think it's also instructive to

[28:16] take a look at example agent

[28:17] trajectories. And um one nice thing

[28:20] about the Swebench uh data set or

[28:23] Swebench evaluation task and leaderboard

[28:26] is that they have some example

[28:28] trajectories here. Um so, let's take a

[28:31] look at maybe

[28:34] GPTO OSS.

[28:38] And this can give you a feel for what uh

[28:40] tool calls can look like and what the

[28:42] model is actually seeing um as it's

[28:45] carrying out this task. So let's see if

[28:48] I can zoom in a bit.

[28:52] Yeah. So the model gets some uh context

[28:57] in a system message um which says you

[29:00] are a helpful assistant that can

[29:02] interact with a computer shell. So this

[29:04] is like very generic um but then we'll

[29:07] also have a user message which gives

[29:10] some context about a particular task uh

[29:12] solving this particular um poll request.

[29:16] Um

[29:19] and so the model conditions on all of

[29:21] that and then it needs to um issue a

[29:24] first action and you can see here the

[29:26] chain of thought trace that it

[29:28] generates. So this blue is generated by

[29:30] the model. So you have the chain of

[29:32] thought here and it produces a tool

[29:34] call. This agent is using the um the

[29:37] tool format that you suggested which is

[29:40] just issuing bash commands um by you

[29:43] know writing the uh command that should

[29:45] be run that gets handed off to the

[29:47] environment. The environment executes it

[29:49] and here the result is just an exit code

[29:51] exit code zero showing it succeeded but

[29:54] then we go on to the next turn and the

[29:56] agent uh you know issues a new thought

[29:58] and a new bash command and so on.

[30:02] So hopefully that gives you a sense of

[30:04] you know one possible way of uh

[30:06] instantiating tools and instantiating

[30:09] prompts and you'll experiment with this

[30:11] in your first assignment.

[30:17] Cool. So uh now I'll hand over to

[30:19] Graham.

[30:32] Thanks a lot. Okay. Hi. Uh

[30:36] I guess uh everyone can hear me. So next

[30:39] I'd like to talk about agent

[30:41] capabilities. And what I mean by this is

[30:43] like what makes a good agent. Uh because

[30:47] as uh Daniel pointed out uh it's not

[30:50] very hard to make an agent. uh

[30:52] especially nowadays that there are

[30:54] libraries that you can call to you know

[30:56] do inference with a language model or

[30:58] something like this. The hard part is

[31:00] making one that actually works. Um so

[31:02] I'd like to think a little bit about uh

[31:05] the capabilities that you need to have

[31:07] in an agent. So a fairly large number of

[31:11] people said they use agents in some way

[31:13] you know every day like openclaw or

[31:15] coding agents. Um what are the things

[31:17] that frustrate you when you use an

[31:19] agent? like what what has gone wrong

[31:21] that was a problem? We saw an example of

[31:23] deleting all your email files. That

[31:24] would probably frustrate you, but um any

[31:27] any other things?

[31:29] >> They're too slow.

[31:31] >> Okay. Yeah, that that's a good one.

[31:34] Uh in the backy

[31:38] wordy and verbose. That's a good one. I

[31:40] saw a hand. Yeah.

[31:45] >> Um so they forget things. Yeah. Okay.

[31:55] >> They might misunderstand what you said

[31:57] and make mistakes due to that. Yeah.

[32:03] >> Do doing what was it?

[32:06] >> Like accessing things they shouldn't be

[32:08] accessing. Yeah. Okay. That that's a

[32:10] good one. Um Yeah.

[32:15] random knowledge gaps for very common or

[32:18] normal things. Yeah, that that's a good

[32:19] one. Yeah.

[32:26] >> Yeah. Writing a thousand lines of code

[32:27] when two would do. Yes, that that's a

[32:29] good one. That's kind of a different

[32:31] variety of verbose, but it's also Yeah.

[32:32] verbose. Yeah.

[32:37] >> Yeah. Forgetting previous session

[32:38] interactions. So, um, yeah.

[32:43] >> Not knowing how to push back when you

[32:45] say something, uh, unreasonable. Yeah.

[32:49] >> They may lie to you. Yes, that's a bad

[32:52] one.

[32:56] >> A lot of implicit assumptions. Yeah. So,

[32:59] um, these are all great points. Um, all

[33:02] things that frustrate me, too. So um

[33:05] they're they don't exactly align with

[33:07] what I had on the slide but you know

[33:08] that's a a great uh a great thing. So um

[33:13] a first capability that you need to have

[33:15] uh in agents is accurate tool calling.

[33:18] This is something that actually nobody

[33:20] mentioned uh because a lot of people

[33:22] take it for granted nowadays but this is

[33:25] not something you can take for granted

[33:28] uh if you're starting this class and

[33:31] you're in charge of training the model.

[33:33] Um so uh you know it's kind of bread and

[33:36] butter. If you can't call tools

[33:38] accurately you're going to fail at any

[33:39] task you do. But uh it's something that

[33:43] doesn't come for free. Another thing is

[33:46] coherence over long context. And so

[33:47] somebody said uh it annoys me when they

[33:50] forget things or it annoys me when they

[33:52] forget the previous sessions or

[33:53] something like this. So uh that that's

[33:55] one example of it. Another example of it

[33:58] is uh what the example that Daniel gave

[34:01] where previously the model was told to

[34:03] not do something but then it ended up

[34:05] doing it anyway. So uh that that's

[34:07] another example.

[34:09] Another thing is uh customizability. And

[34:12] so

[34:14] you want the agent to do things your

[34:16] way. Uh everybody has different uh ways

[34:19] of doing things uh different

[34:21] requirements. So our class might have a

[34:22] different requirement than another

[34:24] class. And so you need to make sure that

[34:26] if you're using an agent uh it's going

[34:28] to follow those requirements.

[34:30] Uh complex task management. So breaking

[34:33] down tasks uh being able to handle very

[34:36] long horizon things is a very big uh

[34:38] very big issue.

[34:40] environment understanding and what I

[34:42] mean by this is uh there were like one

[34:46] good example of this is making a

[34:47] thousand line change in a codebase where

[34:49] two lines would do that's an implicit

[34:53] failure of environment understanding to

[34:55] know that you know this is actually a

[34:57] really simple change but it didn't

[34:58] realize that and it goes and does a

[35:00] bunch of other things instead and then a

[35:02] final thing is safety and a lot of

[35:06] people separate safety and capabilities

[35:08] they say I'm a safety researcher or I'm

[35:10] a capabilities researcher. But from my

[35:12] point of view, capability safety is a

[35:15] capability. It's something you need to

[35:17] bake into the model. And if it's not

[35:19] baked into the model, you won't feel

[35:22] like you won't feel comfortable using

[35:24] the model because it might go off and do

[35:26] something that you don't uh want it to

[35:27] do. And so from my point of view, it's a

[35:30] a failure of the model or the agent more

[35:32] broadly.

[35:35] And so there's two ways to build these

[35:37] capabilities. And this is something

[35:38] that's really really important when

[35:40] you're working on agents. Uh the first

[35:43] one is uh training in LLM. The second

[35:47] one is engineering the harness uh so

[35:50] that you put structure around the LLM to

[35:52] get it to uh you know solve uh like

[35:57] solve the problems you want in the way

[35:58] that you want to. So

[36:02] question um which one do you think is

[36:06] more important or effective uh here? So

[36:11] does anyone have an a strong opinion

[36:12] that LLM training is the way to to get

[36:15] your agents to work well?

[36:20] Okay, actually surprisingly large small

[36:24] number of people. What about um train uh

[36:26] engineering the harness around the

[36:27] agents?

[36:29] Okay, that that's a pretty large number

[36:32] of people. I saw Daniel raised his hand

[36:34] twice, so he's not allowed to do that,

[36:36] but [laughter]

[36:38] um he's the instructor. So, of course,

[36:41] both of these uh are important. Um my my

[36:44] personal opinion um or well, first I'll

[36:48] I'll you know talk a little bit about

[36:49] what they entail. So, the first one is

[36:51] changing the model's behavior through

[36:53] pre-training uh supervised fine-tuning

[36:55] or reinforcement learning. Um and then

[36:58] you can teach uh reusable patterns for

[37:00] reasoning, tool use and recovery.

[37:03] The important thing is the capabilities

[37:05] become part of the learn model or the

[37:07] learned uh policy. And so in harness

[37:09] engineering, you change the system

[37:11] around the model. You give it prompts,

[37:12] tools, memories and control flow provide

[37:15] context, validation, retries and safety

[37:17] boundaries. And the capabilities emerge

[37:20] not just from the model, but they emerge

[37:22] from the combination of the harness and

[37:24] the model.

[37:26] So my my answer to this is

[37:30] um they're they're maybe both important

[37:33] but typically what happens is you

[37:36] identify a problem and you solve it here

[37:38] first.

[37:40] Then

[37:42] the people who are training the models

[37:45] uh catch up and realize that this is a

[37:48] big problem. It's a big enough problem

[37:49] that it warrants them training the model

[37:51] in a particular way to solve the

[37:52] problem. it gets solved and you don't

[37:55] need to solve it in the harness side

[37:57] anymore. So that this is a typical flow.

[38:00] Um

[38:02] so from my point of view this is kind of

[38:06] very often the more fundamental solution

[38:08] on the left side but it takes a lot of

[38:09] time and so you eventually you need to

[38:12] start out by solving it on the right

[38:13] side because you don't have the time uh

[38:15] when you're improving your models. So I

[38:17] I personally favor LLM training as a

[38:19] fundamental solution to problems if

[38:21] you're in a situation where you're able

[38:22] to do that. Yeah.

[38:35] >> So, this is a great question. So, what

[38:37] are the capabilities that will survive

[38:40] LLM training? Um, one I can definitively

[38:44] say is long context uh in like

[38:48] maintaining all of your your memories uh

[38:51] in context because

[38:54] there that is not a

[38:57] that's not a model

[39:00] accuracy problem only. It's also a model

[39:02] efficiency problem. So you need to be

[39:04] able to model very long sequences. And

[39:07] sure you might be able to come up with a

[39:09] model that doesn't have like n squ

[39:11] complexity like the transformer does but

[39:15] you know that's uh you know that's kind

[39:19] of a bigger a bigger discussion assuming

[39:20] we're staying in our our current

[39:21] modeling paradigm I'd say uh

[39:29] most of the other stuff I have on here

[39:32] uh

[39:35] most of the other stuff I have on here.

[39:36] Accurate tool calling, uh, coherence

[39:39] within your context window, complex task

[39:42] management, environment understanding,

[39:46] mostly from a capabilities perspective

[39:48] can be and maybe even safety mostly from

[39:50] a capabilities perspective could be

[39:53] theoretically solved through the model,

[39:54] but they're not solved yet. Um, and so

[39:56] we still need uh we still need harness

[39:59] uh engineering. Customizability is a

[40:01] very interesting one because you could

[40:03] train the model on the fly. Um, but

[40:06] there are also cases where you kind of

[40:08] want to give it like a script or you

[40:10] want to give it separate instructions

[40:12] based on the situation that you're in

[40:13] and they're like maybe training it would

[40:15] not be the best solution. But we can

[40:17] talk a lot more about you know all of

[40:18] these details later. Yeah.

[40:28] >> Yeah. So um a follow-up question on when

[40:32] inference uh latency is very important

[40:35] is engineering the harness to fit the

[40:37] problem a good solution. So uh

[40:41] what what I want to point out is all of

[40:42] these capabilities can be handled either

[40:44] through training or through the harness.

[40:46] Um and so I I wouldn't say like one is

[40:50] necessarily always better than the

[40:51] other. They're both uh both solutions.

[40:53] The interesting thing about like

[40:55] inference time uh efficiency is you need

[40:59] often need to use a weaker model or you

[41:01] need to use less compute and because

[41:03] that's the case you often need to put

[41:04] more guard rails around it because

[41:06] you're going to have less su uh success

[41:08] or you need to do like adaptation to the

[41:10] particular task you're interested in. So

[41:12] um the the smaller the model you're

[41:14] using the more careful you need to be

[41:16] because the very big models can often

[41:18] generalize better. Um they're not

[41:19] perfect but they can generalize better.

[41:22] Cool.

[41:23] Uh any others?

[41:26] Okay. So um

[41:30] moving on to uh onto this. So um one of

[41:35] the big goals of this class is to get

[41:38] people to be able get all of you to be

[41:41] able to train a model uh for agentic

[41:44] tasks. And this is uh a big point in

[41:49] that not that many people can do this

[41:52] well. And so we'd like the people in

[41:54] this room to be not that many people,

[41:55] right? We we'd like you to be good at at

[41:57] something that that's hard to do, but uh

[42:00] hard to do, right? But, you know, um

[42:03] like it's a good thing to know how to do

[42:05] if you do know how to do it. Um we're

[42:07] not going to be handling pre-training uh

[42:09] because pre-training uh you know, it's

[42:11] on the scale of the entire internet and

[42:13] that's uh unfortunately not something

[42:16] our our modal credits uh will support.

[42:19] uh but we will be uh thinking about

[42:21] mid-training and supervised fine-tuning

[42:23] and reinforcement learning. And uh the

[42:26] points here are mid-training and

[42:28] supervised fine-tuning is where you

[42:30] already have example demonstrations of

[42:32] how an agent did a task and you're

[42:33] training on those example demonstrations

[42:36] uh usually by optimizing maximum

[42:38] likelihood. Hopefully everybody in this

[42:40] class has done that before because it's

[42:41] a prerequisite for the class. So um uh

[42:45] we'll only be covering that briefly and

[42:47] be focusing more on how you create the

[42:49] data for doing this in indogentic

[42:51] setting. Um and then we're going to

[42:53] focus more uh on reinforcement learning

[42:56] because reinforcement learning for uh

[42:59] like agents is is pretty tricky. So how

[43:02] many people have done reinforcement

[43:03] learning with language models before? I

[43:06] guess maybe not that many people. Yeah.

[43:08] Okay. How many have done it for

[43:10] reasoning

[43:11] reasoning tasks? How many have done it

[43:14] for agents?

[43:17] Okay, maybe about half and half and it's

[43:19] only like maybe 10 10% 10% and 80% have

[43:22] not done it. So yeah, we're going to try

[43:24] to put a lot of effort into making sure

[43:26] that everybody is able to do this by the

[43:27] end of the class.

[43:30] Cool. Um so looking at all the

[43:32] capabilities one by one. Um, accurate

[43:34] tool calling is uh an important

[43:36] capability to have. Uh, we do it through

[43:39] harness engineering and LLM training.

[43:42] Uh, some of the things we're going to

[43:43] talk about in class are grammar

[43:45] constraint decoding, uh, which allows

[43:47] you to make sure that your tool calls

[43:49] are wellformed and match the

[43:50] specification that you have. Um, for LLM

[43:54] training, this is

[43:56] first done through SFT um or through uh

[44:00] through mid training or or whatever you

[44:01] want to call it. Um and this is done by

[44:03] training on tool calling uh tool calling

[44:05] data tool calling traces.

[44:08] Um

[44:12] for coherence uh over long context uh

[44:15] this again can be done through harness

[44:17] engineering or uh or LLM training. For

[44:21] harness engineering, we do this through

[44:22] context compression or compaction which

[44:25] are kind of synonyms um where you take

[44:28] all of the context and you summarize it

[44:30] down uh for the agent to continue

[44:32] working. It also can be done through

[44:35] dynamic memory lookup uh where you have

[44:37] memory over all the context that you

[44:39] want to be handling but you don't pull

[44:40] it all in immediately uh you pull it uh

[44:44] in you know on demand. Um and it can

[44:47] also be done through sub aent

[44:48] delegation. So you delegate some parts

[44:50] of a very long task to an agent. It

[44:53] keeps that context in memory, but then

[44:54] it drops it out of memory when it's done

[44:56] performing that.

[44:58] Um for LLM training, uh you can do that

[45:01] through long context training. We're not

[45:02] going to handle it a lot, but we'll talk

[45:04] about it maybe a little bit. Um

[45:08] then for customizability, this is

[45:10] actually one of the best use cases for

[45:11] harness engineering uh right now, I

[45:14] think. And there's a bunch of methods

[45:16] that you can do this. Uh one is through

[45:17] agent memory. So making sure that the

[45:19] agent continues to learn uh as you

[45:22] interact with it more um through skills

[45:25] uh which are kind of

[45:28] prompts and sometimes scripts about uh

[45:32] the sort of thing that you want to do

[45:33] that you pull in at each uh time peri

[45:36] time time point when you want to use

[45:38] those things. Um also possibly custom

[45:41] tools for a particular task.

[45:44] um for LM training uh this is a nent

[45:48] area. I don't think there's a lot of

[45:50] people who are doing this in uh in a lot

[45:52] of detail. Uh but there are methods

[45:54] where you can learn from user feedback.

[45:56] And so like if a user is is using a tool

[45:59] and they give a thumbs up or a thumbs

[46:01] down, you can learn specifically from

[46:02] them to adapt to them.

[46:06] Complex task management. Uh ways you can

[46:08] do this are through harness uh

[46:10] engineering. So you can provide planning

[46:12] or decomposition tools. You can have a

[46:15] plan mode uh for the model where uh it

[46:18] uh it gets to plan. I this is a little

[46:22] uh thing that I I learned but there was

[46:24] a popular coding harness I think it was

[46:26] uh codeex no sorry maybe it was clog

[46:29] code where they had a plan mode and uh

[46:32] the only thing when people pressed the

[46:33] plan mode button was that it added an

[46:36] extra thing to the prompt that said

[46:37] please plan do not do anything. Um,

[46:40] [laughter]

[46:40] but everybody wanted a plan mode. They

[46:42] wanted a button. So, they made sure that

[46:44] it was done entirely through prompts.

[46:45] But there's also more uh more complex

[46:48] ways uh to do this as well. Um, again,

[46:52] you can do this through sub aent

[46:53] delegation by like breaking down the

[46:54] task and uh delegating it to other

[46:57] agents. And a very good way to do this

[46:59] in training is to train on complex uh

[47:02] long horizon tasks.

[47:05] So for environment understanding, what I

[47:07] mean by this is whatever data format or

[47:11] environment that your agent is uh

[47:12] interacting with, it needs to be able to

[47:14] understand it. And just to give one very

[47:17] good example of this in computer use

[47:19] agents, um you need to be able to

[47:22] understand web pages and or uh you know

[47:26] guey interfaces or something like this.

[47:29] This is not something you get for free.

[47:31] In fact, like agents are actually pretty

[47:33] bad at it right now. Uh even the

[47:35] strongest agents are maybe not, but like

[47:38] um many of the open source models don't

[47:40] even support multimodal uh data and uh

[47:44] like the ones that do are not perfect at

[47:47] understanding it. They make lots of

[47:48] mistakes, many more than when they're

[47:49] understanding text. So this is a failure

[47:53] of uh understanding the environment

[47:55] because they need to understand the

[47:56] multi- modal data in their environment.

[47:58] But now let's put them in a different

[47:59] environment where they need to trade

[48:01] stocks or something like that. Um,

[48:05] they're not very good at understanding

[48:06] time series. They make a lot of mistakes

[48:08] on time series. Or you put them in an

[48:09] environment where they need to

[48:11] understand a picture of a, you know, a

[48:16] petri dish with lots of bacteria in it

[48:18] or something like that. They fail to do

[48:19] that as well. So you kind of need to be

[48:22] able to understand whatever environment

[48:23] you want the agents to uh, you know,

[48:26] interact with. So there's ways you can

[48:29] do this through hardness engineering by

[48:31] like giving skills that correspond to

[48:33] domain knowledge but you can also train

[48:35] on data with the expected observation

[48:38] shape or train in domain specific

[48:40] environments.

[48:41] So right now actually like

[48:46] there's kind of this thing uh that

[48:47] people say which is like oh the models

[48:49] are going to get better uh and then we

[48:51] won't need to worry about that anymore.

[48:53] Um the thing is models don't get better.

[48:57] Uh people make models better. And so one

[49:00] of the things we'd like to teach in the

[49:01] class is like what's actually going on

[49:03] under the hood when suddenly Claude goes

[49:04] from uh 4.7 to 4.8 and it can suddenly

[49:08] like compose music better. Um, and the

[49:12] there's a few things uh that go into

[49:14] this, but one of the really big ones is

[49:17] uh they make an environment to train the

[49:19] model on uh a like compose music

[49:22] environment and suddenly you know they

[49:24] they train on it for you know they add

[49:27] it to the training mix and then the

[49:28] model gets better at composing music or

[49:30] something. So a lot of the uh a lot of

[49:32] the work here is creating domain

[49:34] specific environments that models can

[49:35] work in.

[49:38] Uh then the final thing is safety. And

[49:40] uh we're going to talk about it for uh

[49:43] like a bit because if you don't have a

[49:46] safe model, you're not going to be able

[49:47] to use it in real consequential

[49:49] settings. Um and there's a lot of things

[49:51] with respect to harness engineering that

[49:53] you can do here. You can give it a

[49:54] sandbox. Um you can limit access to cred

[49:57] credentials. You can also monitor the

[49:59] agent as it works. Um and you can also

[50:03] do safetyaware reinforcement learning.

[50:06] Um I I think probably a fair number of

[50:08] people heard about this, but who heard

[50:09] about the OpenAI incident where uh it

[50:13] hacked into hugging face? Okay. Well, so

[50:17] I think most people heard about it, but

[50:19] recently there was a um there was an

[50:22] example where uh the newest open AAI

[50:25] model was in an agentic harness and it

[50:27] was working on a cyber security

[50:30] benchmark and so its instruction was

[50:33] hack into this system and so it was

[50:36] going to hack into a system and that was

[50:38] its task and it wasn't able to hack into

[50:41] the system. So instead it basically

[50:43] hacked into the hugging face website and

[50:46] uh and got the answers from the hugging

[50:47] face website and and did it there. And

[50:50] so there were a bunch of failures that h

[50:52] that happened here. Um the first failure

[50:56] was a failure in sandboxing because they

[50:58] didn't properly contain the agent when

[51:00] it was doing this benchmark.

[51:02] um they

[51:04] they did have limited access to

[51:07] credentials and so it worked around that

[51:09] problem uh by by hacking into something

[51:12] it didn't have credentials for. Um and

[51:14] they also didn't have sufficient

[51:15] monitoring so they weren't able to tell

[51:16] that this happened. Uh they didn't have

[51:19] sufficient safety guardrails on this

[51:20] model because this model was being

[51:22] trained to test uh you know like whether

[51:27] it could hack into systems. So

[51:28] presumably the models that they

[51:30] eventually released to the public did

[51:31] have better guardrails of this model.

[51:33] But like um these are all ways that you

[51:36] can handle safety and we'll be talking

[51:37] about this sort of thing as well.

[51:40] So the final thing um and any questions

[51:43] about the capabilities part. We're going

[51:45] to go into a lot more detail of course.

[51:47] So

[51:49] okay, sounds good. Um so another thing

[51:52] that I we really want to reinforce here

[51:55] is agents are systems. uh they're not

[51:58] just models and they are far more

[52:01] complex than most of the things you've

[52:04] dealt with in any

[52:07] machine learning class that you've taken

[52:09] any you know class here that you've

[52:11] taken before. So you're going to have to

[52:14] be able to handle a bunch of different

[52:16] things. The first thing is a harness.

[52:19] Um, which is a

[52:22] moderate to complex piece of software.

[52:26] Um, and it has a lot of moving parts

[52:28] like you need to deal with the context,

[52:29] you need to deal with the the tools, uh,

[52:32] the guardrails, manage workflows, uh,

[52:35] stuff like that. Um, you need to have a

[52:38] sandbox. So, you need to make sure the

[52:40] agent is working within a contained

[52:42] environment. And, um, there are

[52:45] different ways you can do that. uh it

[52:47] needs to work with a model and you need

[52:49] to do inference. But if you've done

[52:51] inference with language models before,

[52:53] you might have dealt with contexts of

[52:55] like 16 tokens or 32 uh 16k tokens or

[53:00] 32k tokens. Here you need like 256 uh at

[53:05] least they have kind of like a

[53:07] state-of-the-art uh coding agent for

[53:09] instance. And so um the inference

[53:11] problems are harder. You need to deal

[53:12] with caching your inference other things

[53:14] like that. and you need monitoring and

[53:16] training.

[53:18] So um from the point of view of this

[53:21] what we're going to teach in the class

[53:22] is harness engineering. So um how to

[53:25] manage state tools memory control flow

[53:28] um how to validate actions, handle

[53:30] errors, enforce permission and safety

[53:32] boundaries. Um and we're in for each of

[53:36] these systems, we're also going to try

[53:37] to give examples of software uh that you

[53:40] can look at. Um, for harnesses, there's

[53:43] kind of two big varieties of harness

[53:45] that you use for coding agents. Um, some

[53:49] popular ones right now are cloud code,

[53:52] codecs, open hands, open code, and pi.

[53:54] Uh, probably you know you're you have

[53:57] used or have heard of uh at least one of

[54:00] these. Um, I develop open hands so I

[54:03] know it very well. Uh, and so I'll be

[54:05] talking about uh talking about this. I'd

[54:07] also like to give a little bit of my

[54:08] experience and some of the lessons we

[54:10] learned uh in in developing it.

[54:13] Separately from this um there are

[54:16] orchestrators. I I wrote lang chain but

[54:18] maybe I should have written lang graph

[54:20] instead in crew AI and kind of the they

[54:22] have a very different philosophy between

[54:24] these. Um the the coding agents are are

[54:27] generally simpler uh in terms of how

[54:30] different intera uh agents interact with

[54:33] each other but they're more complex in

[54:34] the action space that you give to the

[54:36] agent. So the agent can write code, it

[54:38] can interact with a website, it can do

[54:40] other stuff like this. Um orchestrators

[54:43] are less complex with respect to the

[54:45] individual agent that they have. So the

[54:47] agent might just be able to answer

[54:50] customer service requests or um look

[54:52] something up in a database, but it

[54:54] couldn't write an arbitrary Python

[54:55] program. But on the other hand, you get

[54:57] like these

[54:59] declarative workflows of what the agent

[55:02] workflow is able to do. And so that's

[55:04] like a a different way of building

[55:05] things. It's more guardrail but less

[55:07] expressive. And they both have their

[55:09] place uh in different settings.

[55:12] For sandboxing uh to prevent your agents

[55:14] from uh

[55:18] sharing your API keys without your

[55:19] permission or uh hacking into other

[55:22] websites. Um we need to isolate code and

[55:24] tool execution and limit the compute

[55:27] network and file system access that

[55:29] agents have uh access to. Um another big

[55:32] thing is for evaluation and training.

[55:34] It's a very good way to create

[55:35] reproducible environments. Uh so like

[55:38] for SWEBench for instance each problem

[55:41] has a uh each problem has a sandbox and

[55:44] you start in the sandbox and that's the

[55:46] state of the environment before the

[55:47] agent starts working and so you can run

[55:50] these uh locally. Um some of the uh

[55:54] technologies that we use for this are

[55:55] Docker and Appainer. Um or you can run

[55:58] them on the cloud and uh two of our uh

[56:03] kind of compute partners for this class

[56:04] Modal and sale are uh like cloud uh in

[56:08] uh providers and actually prime

[56:10] intellect for that matter.

[56:13] So the next thing is uh language model

[56:15] inference. And so I I think you know

[56:17] given your previous experience in an in

[56:20] an NLP or like large language model

[56:22] class presumably most people have uh

[56:25] encountered this before but basically um

[56:29] they uh are required to serve model

[56:32] gener generations

[56:34] um batch requests. So if you have like

[56:37] multiple agents hitting your language

[56:38] model at once, it's more efficient but

[56:40] also you need to batch the requests

[56:41] together.

[56:43] An extremely extremely important part of

[56:46] agents is caching previous requests

[56:49] because agents take more and more

[56:51] actions and so the more and more actions

[56:53] they take the more uh kind of context

[56:55] they build up and you need to make sure

[56:57] that you reuse that to do it um uh

[57:00] properly and you know other systems

[57:02] considerations.

[57:04] Uh some example software that we're

[57:06] going to talk about here is uh things

[57:07] like VLM and SGLANG. These are the two

[57:09] most popular ones. And then there is

[57:12] also tons and tons of inference

[57:13] providers. Um if people have not seen

[57:16] open router before, open router is kind

[57:18] of a a general thing that gathers

[57:19] together all the inference providers.

[57:21] And for any model, uh you'll see like 20

[57:25] or 30 different providers serving the

[57:26] models. So there's lots and lots of

[57:28] them. uh one of our compute sponsors

[57:30] fireworks is an example of that and sale

[57:34] um training systems. So here what they

[57:37] do is uh basically they need to update

[57:40] the models weights and so they uh

[57:42] prepare data, collect rollouts um uh

[57:45] they coordinate a whole bunch of workers

[57:47] who are working together uh to to train

[57:49] the models and they can uh checkpoint

[57:52] evaluate and reproduce runs. Um some

[57:55] example pieces of software here are Sky

[57:57] RL and Miles. Um and so uh the these can

[58:01] be used for for training.

[58:04] And finally um observability and

[58:06] monitoring. Uh so this is uh to

[58:08] understand how your agents are working.

[58:10] So these capture the traces or

[58:13] trajectories of the agent, what the

[58:14] agent did um and they gather metrics

[58:17] around them uh such as like how much

[58:19] time it takes, how much cost it was uh

[58:21] track the quality, the cost and the

[58:23] failures. Um and they allow you to

[58:25] compare trajectories and evaluations.

[58:27] And so um uh I'm I'm pretty familiar

[58:31] with one called Laminer because I use it

[58:33] a lot. MLFlow is another example. Um I I

[58:36] just realized that Daniel showed one

[58:37] called transluce uh which is not on my

[58:40] slide here but that's another another

[58:42] popular one.

[58:45] So um by the end of the class what I

[58:48] hope everybody in the class would be

[58:49] able to do is uh implement an agent from

[58:52] scratch uh on top of an open source LLM.

[58:55] So uh this is implement a harness

[58:57] yourself uh design evaluations for

[58:59] multi-step tasks. And so basically uh

[59:02] we'll give you a task that you need to

[59:04] evaluate and you need to create an

[59:06] evaluation for it. This is super super

[59:09] important even if you're not interested

[59:11] in evaluation but you're also interested

[59:13] in training because one of the best ways

[59:15] to do training is to create an

[59:17] evaluation and scale it uh so that you

[59:20] can do reinforcement learning based

[59:22] training. So um very important skill to

[59:25] have uh train agents to improve their

[59:28] capabilities. So we actually run the RL

[59:30] loop, handle all the systems problems

[59:32] and be able to to solve this um reason

[59:35] about safety and reliability trade-offs.

[59:36] So we'll we'll be talking about safety

[59:39] and uh finally we will have a project

[59:41] which I'll I'll talk about on the next

[59:43] slide.

[59:45] So um these are the assignments. Um the

[59:47] first assignments are basically going to

[59:49] be implementation assignments. So you'll

[59:51] be given uh something to do and be asked

[59:54] to do it. And uh the first one is create

[59:56] a harness. Um the second one is

[60:00] evaluation as I measured as I I read

[60:03] measure as I mentioned. Um and then uh

[60:06] training uh where we train with RL. And

[60:09] so these are approximately the first

[60:11] half of the course. Um and then the

[60:14] second half of the course will be to do

[60:16] a project uh using these skills uh to

[60:20] you know do something kind of

[60:21] interesting or novel uh in whatever area

[60:24] you choose. And the project will be

[60:26] group based. So we're going to be uh

[60:29] asking you to form groups of two or

[60:31] three and uh and create a project. And

[60:34] the general schedule is uh we're going

[60:36] to talk about agent capabilities first.

[60:39] Um we're then going to jump into some

[60:41] specific domains like coding and guey

[60:42] agents. Um do uh training uh and uh

[60:48] including SFT and RL. Um we're going to

[60:52] be talking about uh frameworks and

[60:53] safety. And then uh we're going to be

[60:57] talking about interaction and then we

[60:58] have some project hours where everybody

[61:00] uh discusses their projects. And then uh

[61:03] on the end of the class we're going to

[61:05] try to get uh some domain experts from

[61:08] each of the various domains to give a

[61:10] guest lecture um which maybe combines a

[61:12] little bit of overview but also their

[61:13] research. Uh and so uh hopefully you'll

[61:16] be able to learn from uh some pretty

[61:18] exciting people. And I uh Daniel and I

[61:21] tried to brainstorm the best people in

[61:23] the uh in the world to talk about their

[61:25] things and I don't know if anybody said

[61:26] no. Um

[61:29] so I think everybody said yes. So uh we

[61:32] we got our first choice for every every

[61:34] topic. So I'm pretty excited about that.

[61:37] Um

[61:39] so uh before we begin uh we have some

[61:42] prerequisites and this is a heavy course

[61:46] in terms of implementation in machine

[61:48] learning. Uh we want uh we want

[61:50] everybody to be able to train an agent

[61:52] with RL by the end of it. And so our

[61:55] prerequisite is also um we require prior

[61:58] serious experience training a language

[62:00] model. Um the LTI courses on uh language

[62:04] models, language model systems, NLP

[62:06] would all qualify for this prerequisite.

[62:08] So if you took one of those, that's

[62:09] okay. Um some deep learning courses

[62:11] might qualify for it. Uh if you're not

[62:14] sure, um feel free to ask us. Um but we

[62:17] are going to require this and we're

[62:18] going to have everybody have to submit a

[62:20] form for it. So uh please uh please do

[62:23] do that. Um if there's like 30 people

[62:27] who want to know whether their course

[62:28] qualifies, please don't ask me that

[62:31] specific question after the class here

[62:33] because it'd be better to do it through

[62:35] email, but um uh other questions we'll

[62:37] be happy to answer after the class. Um

[62:39] we'll share a Google form on Patza and

[62:42] please submit the form so we can

[62:43] finalize enrollment. Um and uh yeah, I I

[62:47] already um uh I already covered it. If

[62:51] you haven't taken a course, if you've

[62:52] worked in industry and you've trained a

[62:54] model in industry, uh it should be a

[62:57] real one like at least 4 to 7B uh size,

[63:00] not uh not 100 million parameters. Um

[63:03] but we will also accept that.

[63:08] Um and so uh this is the grading policy.

[63:12] Um so assignments one to three will be

[63:14] 40% total uh completed individually. Um

[63:18] we're going to have lecture highlights

[63:21] and so uh basically the idea here is

[63:24] that we want people to uh

[63:27] come to the lecture and

[63:30] uh give a highlight about you know

[63:34] something you learned in the lecture.

[63:36] The idea around this is not to be, you

[63:40] know, not to make people do like undo

[63:42] work or something like this, but if you

[63:44] watch through the entire lecture, you

[63:47] hopefully you came up with something

[63:48] that's interesting. If you said if you

[63:50] could say nothing was interesting, I

[63:52] knew all of this already. I learned it

[63:54] here uh in this previous class that's

[63:56] already in the prerequisite list. That's

[63:58] also useful information for us. So share

[64:00] it with us. But hopefully we'll say at

[64:02] least one interesting thing in every

[64:03] lecture. So uh you can uh you can follow

[64:06] up with that. Um the research project uh

[64:10] is uh 50% of the total um and this will

[64:13] be in teams of two to three uh because

[64:15] it's uh half of the class assignments.

[64:18] Um the proposal is 5%, the check-in is

[64:20] 5%, presentation is 10% and final report

[64:23] is 30%. And if you've taken an LTI uh

[64:26] project based class before, grading will

[64:28] be similar to the LTI project based

[64:30] class uh requirements. Um if you have

[64:33] not then uh we'll we'll be sharing uh

[64:37] details about this.

[64:41] Um so here's the question uh you've all

[64:44] been asking for. This is an AI agent

[64:47] class. Um and we discussed this very

[64:52] um very thoroughly about what we wanted

[64:54] to do here. Um,

[64:58] I'd like to preface this by saying I use

[65:00] agents all the time for nearly

[65:01] everything I do. Um, but at the same

[65:05] time, it's kind of dangerous to use

[65:07] agents for everything because you lose

[65:09] like sight of uh of what you want to uh

[65:12] like of what you're learning. You miss

[65:15] some of the details and other things

[65:16] like this because the goal of this class

[65:19] is learning. Um but we also want

[65:22] everybody to be familiar with the

[65:23] standard practice. Um we uh we want you

[65:28] to keep this in mind and uh AI tools

[65:32] will be permitted um for basically

[65:36] everything in the course unless we say

[65:38] otherwise and we probably won't be

[65:40] saying otherwise very often. Um so uh

[65:44] lecture highlights must be written by

[65:46] you not generated by AI. Um and so these

[65:50] do not need to be long. Uh they can be

[65:52] short, they can be a few sentences, but

[65:54] please uh write them yourself. And uh

[65:57] you are responsible for every submitted

[65:59] claim, citation, result in line of code.

[66:02] And uh we will create quizzes uh for the

[66:06] assignments so that uh you will you may

[66:09] need to explain uh parts of your code.

[66:12] And uh how will we do this? Uh we also

[66:15] know how to use agents. So we will

[66:20] We we are considering having agents read

[66:22] uh read your code and come up with quiz

[66:24] questions tailored to your code. Um so

[66:28] uh we're we're serious about this. Uh

[66:31] and that means that the thousand lines

[66:33] of slop that your agent generated will

[66:36] be a bad idea for you to submit. Um so

[66:38] it's better to submit something concise

[66:40] that you really understand well uh than

[66:42] uh submitting you know more uh

[66:44] basically.

[66:46] Um, so yeah, uh, we're almost done. Uh,

[66:49] deadlines, uh, submissions in Slack. So,

[66:52] all the assignments, uh, include two

[66:54] 24-hour Slack days. Um, they cannot be

[66:57] transferred or shared. After the Slack

[66:59] days are used, the penalty is 5% of the

[67:01] assignment score per additional day or

[67:03] part day. So, what this means is the

[67:06] deadline is the deadline. And, uh, but

[67:09] we're being nice and if you miss the

[67:11] deadline, we'll give you some time to

[67:13] make up for it. uh if you miss the

[67:16] deadline by more than two days um then

[67:20] uh we're not going to take most excuses.

[67:23] If you you were in the hospital or

[67:25] something like that, we uh might ask you

[67:27] to get appropriate acknowledgement of

[67:29] that, but that would be an example uh

[67:31] reason why. Uh but other than that,

[67:33] please try to meet the deadline because

[67:35] we're not going to make many exceptions

[67:36] to this. Um cool, that's all. Uh we're

[67:40] at 441. Um so which means we have nine

[67:44] minutes for questions if people have

[67:46] questions. Um otherwise uh looking

[67:49] forward to having everybody in the

[67:50] class. Any Yes.
