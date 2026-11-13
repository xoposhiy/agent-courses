# Lecture 7 recording

[Course index](../../README.md) · [Original source](https://www.youtube.com/watch?v=jwGluLrrqjQ&list=PLSN0qpDfUvTM&index=7) · [Raw file](../../raw/videos/jwGluLrrqjQ.json)

Retrieved: 2026-11-13T16:48:30.997899+00:00

[00:00] Okay, great. So, yeah, today I'm super

[00:03] excited to have JY Code as our guest

[00:06] lecturer. So, um JY is an expert on um

[00:10] on multimodal machine learning um in

[00:13] particular computer use agents. Uh so,

[00:16] JY um has experience both in academia

[00:19] here as a PhD student CMU uh working

[00:22] with uh me and Russ Solakutnav but um

[00:26] also has a lot of industry experience.

[00:28] Uh so he worked at Google research

[00:30] before starting the PhD and um also he

[00:33] led the computer use agent team at

[00:36] Meta's TBD lab for a year and a half.

[00:40] >> Yeah. And so kind of like laid the

[00:42] foundation for um the strong agents that

[00:45] they're releasing now. And yeah, he also

[00:48] um built uh some of the most uh

[00:52] impactful benchmarks in this area and

[00:54] also did work on um search for agents.

[00:58] So he'll also be giving a lecture later

[01:00] on in the course and we've covered some

[01:02] of his work already on multi-agent

[01:04] computer use and looking forward to uh

[01:08] you know hearing about the foundations

[01:09] of KUAS today. Thanks.

[01:12] >> Cool.

[01:15] Uh thanks a lot Daniel for the kind

[01:17] introduction. Um so today I'm very happy

[01:19] to talk about something that I've uh

[01:21] personally been very excited about for

[01:23] for a couple years now. Um I think today

[01:25] it's like taken for granted that we have

[01:27] uh that computer use is a is a core

[01:30] capability in like many frontier models.

[01:32] But uh as we will see by uh kind of

[01:35] stepping a bit through the history of

[01:36] computer use agents, this was not always

[01:38] the case. Uh I think for a long time

[01:40] like um it was not very clear whether we

[01:42] would want computer use agents or how we

[01:44] would build strong computer use agents.

[01:47] Um so I think computer use agents or kas

[01:50] are a little bit different from the

[01:51] agents that you've already covered in

[01:53] this class. Um so I think they're a bit

[01:54] different I think of them as a little

[01:56] bit different from like sui agents and

[01:58] more textbased agents. Um so first of

[02:00] all what is a cooler? Um, a coupa is a

[02:03] model is an agent that observes a

[02:08] sorry, it's actually not. Um,

[02:14] okay, there we go. Here you

[02:17] >> uh I'm I'm think I think it's fine.

[02:19] Yeah, sorry. So, AUA is a computer use

[02:21] agent. Um, it's a little bit different

[02:23] from the agents that you've already seen

[02:25] cuz what they take as input is actually

[02:26] the graphical user interface that you

[02:29] have in most applications. Um, so you

[02:31] might imagine this could be a web

[02:33] browsing agent. It could be an agent

[02:35] that operates on your desktop computer

[02:37] or it could be something that operates

[02:38] on a mobile device such as your phone.

[02:40] Um, so all of these are broadly speaking

[02:42] computer use agents. Um, agents that

[02:44] operate through the same graphical user

[02:47] interface that humans use. Um, so they

[02:49] take in like screenshots as inputs and

[02:51] they execute actions uh of the same type

[02:53] that humans do. So clicking actions,

[02:55] scrolling actions, swiping, tapping and

[02:58] and so on. Um so the key difference here

[03:00] is that they operate in the exact same

[03:01] space as humans which I think is a very

[03:04] uh it allows for very interesting

[03:06] problems and challenges to be solved in

[03:07] the modeling and evaluation space.

[03:12] So broadly speaking uh kers operate in

[03:14] the following fashion. You have a user

[03:15] task um that is provided to your cooler.

[03:19] You also have some environment

[03:20] observations and typically this is a

[03:21] screenshot uh of whatever you have on

[03:24] your current computer screen or mobile

[03:25] device. Um this can also be some other

[03:28] uh like textbased representations but

[03:30] broadly speaking most frontier course uh

[03:33] use like screenshot representations. So

[03:36] this is essentially exactly what the

[03:38] user would see if they were to attempt

[03:39] the same task.

[03:41] Both of these inputs go into your cool

[03:43] which then produces a reasoning uh trace

[03:46] typically. So it's like a chain of

[03:47] thought and it produces an action that

[03:49] it wants to execute next. And this

[03:51] action can be uh any any action that you

[03:54] allow in your um in your environment. So

[03:57] it can be clicking, scrolling, typing

[03:59] and so on.

[04:01] We then process this action and we

[04:03] execute it in in some infrastructure

[04:05] that you have uh in your environment. Um

[04:07] so if it's a click action, you actually

[04:09] execute it on the computer and you uh

[04:11] get some new observation after executing

[04:13] this action.

[04:15] To give you a concrete example, um you

[04:18] might have a task like buy me a bloom

[04:20] map and you might have some initial

[04:22] environment observation for example from

[04:24] your web browser. So these would go into

[04:26] input into your computer use agent model

[04:29] and your model might produce some

[04:30] reasoning trace of the form. I see a

[04:32] blue monk on the center of the screen. I

[04:33] will click it and it will then produce

[04:36] uh some like formatted action to be

[04:38] executed. So in this case it wants to do

[04:40] a left click on the on the environment.

[04:43] um we will execute this action on the

[04:44] environment. So we will actually like

[04:46] click somewhere on the environment and

[04:48] we will get a new observation that

[04:50] happens after we execute this action. So

[04:52] for example over here you get a new

[04:54] screenshot. Um in this case the agent

[04:56] has clicked into the blue mark. So you

[04:58] kind of have a new observation that

[04:59] shows the details of the blue mark. Your

[05:02] model then takes in this new observation

[05:04] and it produces a new action to be

[05:05] executed condition on this updated

[05:07] observation. So it will it might then

[05:09] say like delivery details are below. I

[05:12] will scroll down to find them and it

[05:14] will produce this scroll action that we

[05:15] will again like execute on the

[05:17] infrastructure. Um you then get a new

[05:19] observation and you basically repeat

[05:21] this until um your model decides it's

[05:24] done. Right? So this can go on like for

[05:26] many many iterations depending on how

[05:28] complex your task is.

[05:31] Uh so yeah you start with an observation

[05:33] your model executes an action you get a

[05:35] new observation um and this repeats

[05:37] until the end and um typically you get

[05:40] some reward either from the environment

[05:42] a human user or some other judge telling

[05:44] you whether the model did it

[05:45] successfully or not. Um so typically

[05:47] like this reward is just a 01 uh binary

[05:50] reward but it can also be um a partial

[05:53] reward in some cases.

[05:55] Um so this is broadly speaking how a

[05:57] computer use agent works. It's this like

[05:59] observe, reason, act loop that that

[06:01] repeats until uh your model exhausts its

[06:04] budget or it thinks it has successfully

[06:06] completed the task. Um and today it

[06:08] seems like very simple uh and models are

[06:11] actually very capable as as we'll see in

[06:13] a couple slides. Um but this was not

[06:15] always the case. So um maybe we can have

[06:19] a quick poll. So when do people think

[06:21] like computer use agents were first uh

[06:23] like invented? Um do people think it was

[06:26] like before 2020?

[06:30] Okay, a few hands. Um say like 2020 to

[06:33] 2024 period is when we started building

[06:35] coolers. Cool. And who thinks it was

[06:37] like after 2024?

[06:40] Um so the the answer is actually that um

[06:42] the first cooler paper came out in in

[06:44] 2017. So this was like uh quite ancient

[06:48] in in um AI standards, right? Uh it was

[06:50] actually a paper from OpenAI. So they

[06:52] had this project called um World of Bits

[06:55] where they built this very simplified

[06:57] toy environment. Um as you can see here,

[07:00] it's mostly like synthetic data. It's

[07:02] very simplified environments that look

[07:05] maybe a bit like what you might see on a

[07:06] mobile device, but it's very simplified.

[07:08] Uh not not realistic at all. Um and what

[07:11] they did in this paper is that they

[07:12] actually did like a bunch of RL

[07:14] training. Um so this is not really

[07:17] similar to like modern LLM RL but it's

[07:19] more like similar to RL that we did for

[07:22] um game agents in in the past. Um but

[07:25] this was I think this project was like

[07:27] ahead of its time. All of the models

[07:29] back then could not do this at all. Like

[07:31] even this simplified uh mini world of

[07:33] bits task they were very bad at it. Um

[07:37] so this was the first cooler paper

[07:39] probably. Um in 2022 I think a bit more

[07:42] interest started picking up with the

[07:43] advent of uh language models. Um there

[07:45] was this other paper called web shop

[07:47] that um also did uh kind of like

[07:50] simplified shopping environments but it

[07:52] was a lot more realistic than than mini

[07:54] world of bits as you can see in this

[07:56] visualization here. So it's kind of

[07:57] clicking through this like simulated

[07:59] Amazon site. Um and it's still a bit

[08:02] artificial but it's a lot better than

[08:03] mini world of bits. Um and at this point

[08:06] like language model agents started doing

[08:08] a bit better at these tasks. uh and we

[08:10] weren't really training them in uh in in

[08:13] the way that we were for many world bits

[08:16] in 2022. In 2024 actually um there was

[08:20] this I think of it as a seminal work uh

[08:22] from actually Graham's lab at CMU called

[08:25] web arena. So it was this work that

[08:27] created a lot of simulated environments.

[08:29] Um and as you can see like all of these

[08:31] environments are a lot more realistic

[08:32] than web shop and mini world of bits. um

[08:34] they contain like very realistic data

[08:37] often scripted from real world websites.

[08:39] So these environments were populated

[08:40] with actual data from like Amazon and

[08:42] Reddit and and so on. um so these are

[08:44] like very realistic data and

[08:46] environments. Um and I think they marked

[08:49] a point where uh the models also started

[08:51] getting a bit better at these problems.

[08:54] In 2024 uh there was also this almost

[08:58] concurrent release of this benchmark

[08:59] called OS world. So I think this is one

[09:01] of the most uh standard computer use

[09:03] benchmarks these days. And this was also

[09:05] using uh real apps and kind of like real

[09:09] data but um uh it tackled like desktop

[09:12] use rather than web browsing. So it's a

[09:14] bit more general. You can use a lot of

[09:16] different apps on Linux, Windows uh and

[09:18] so on. Um so this is a bit different

[09:21] from web arena because web arena was web

[09:23] browsing but OS world is uh like fullon

[09:26] desktop use.

[09:29] Um I think things also took a bit of a

[09:31] change like in 2025 to 2026. So this was

[09:33] the point where like coding agents got a

[09:35] lot better and at this point like a lot

[09:36] of people started generating

[09:38] environments uh end to end. Um so for

[09:41] web arena and OS world what they did was

[09:43] they actually took open source

[09:45] implementations of these apps and they

[09:47] filled it with realistic data but all of

[09:49] the all all of the software was already

[09:51] written by humans and open sourced in

[09:53] some manner. um my PC bench and a few

[09:56] other uh benchmarks around the 2025 to

[10:00] 2026 period actually use coding agents

[10:02] to generate uh the entire app and

[10:04] website um end to end. So shown here is

[10:07] actually a Gmail clone. It's not the

[10:09] real Gmail, but it looks very close to

[10:10] it. And this is actually generated

[10:12] completely by an LLM a coding agent. Um

[10:15] all of the data that is seated here is

[10:17] also completely synthetic. So, we've

[10:19] actually gotten to a point where a lot

[10:21] of like frontier cooler environments are

[10:23] completely generated and completely

[10:25] filled with synthetic data and um I

[10:28] think they actually work very well. Uh

[10:29] sometimes they're even better than real

[10:31] applications because um they're a lot

[10:33] cleaner and they're not as as noisy.

[10:37] Ka world was also another project that

[10:39] came from CMU that took like a real

[10:41] world software. So, I think Kool World

[10:43] is very interesting because the software

[10:45] used here is a bit more of the long

[10:47] tail. So you have some software used for

[10:49] like astronomy and biology and other

[10:51] things of that sort. Um so it's a bit it

[10:53] it departs a bit from like just

[10:55] consumerbased apps into very specialized

[10:57] desktop software. Um all of the data

[10:59] here is also uh I think is realistic

[11:02] data. So it's downloaded data from real

[11:04] world use cases um and is loaded onto

[11:06] onto onto these environments.

[11:10] Uh shown here is a demo very recently

[11:12] from this month of GPT6 Astra. So GBT6

[11:16] Astra was a huge leap in computer use. I

[11:19] think it basically like solved most of

[11:21] the computer use benchmarks. Uh it's

[11:23] like better than human baselines at this

[11:24] point. Um it's kind of a lot faster than

[11:27] previous models, but it's still very

[11:29] slow and very expensive. So this demo is

[11:31] showing GPT6 Astra operating like a CAD

[11:34] software. So it's doing like some like

[11:35] 3D modeling. Um it's actually sped up 30

[11:38] times. So in in practice like this model

[11:40] is actually 30 times slower than

[11:42] whatever you see here. Um but but the

[11:44] point is it's very capable but it's

[11:46] still very expensive and and slow. Um so

[11:49] we still have some research problems

[11:50] left but in terms of capabilities I

[11:52] think current models are are very good.

[11:54] Um so you can see like we progress from

[11:57] toy environments with miniw walk uh to

[11:59] today 9 years later where we have GPT6

[12:01] extra that is uh comparable or better

[12:04] than your median human at a lot of

[12:06] computer tasks.

[12:08] Um so very exciting very fast progress

[12:10] and we can think about like how we might

[12:12] measure these problems. Um if you think

[12:13] about them from a research or academic

[12:15] standpoint uh benchmarks are one of the

[12:18] core ways in which we measure how fast

[12:20] these agents have been progressing. Um

[12:22] so we'll go through an overview of like

[12:24] several computer use benchmarks and how

[12:26] they measure different axes of uh agent

[12:29] performance.

[12:30] Um so if we think about how computer use

[12:32] might be measured uh it's actually a bit

[12:34] I think it's a bit more interesting um

[12:37] than some of the other agents that we've

[12:39] already covered in this course. Um so

[12:41] computer use is in some sense a bit less

[12:43] of a verifiable task compared to like

[12:45] software engineering or math. Um in

[12:47] software engineering or math you kind of

[12:49] have unit tests or or um symbolic

[12:52] verifiers that tell you whether you

[12:54] successfully accomplish a task. for

[12:56] computer use is actually a bit different

[12:57] because you can imagine that um

[12:59] successfully accomplishing a problem is

[13:02] not always um people do not even people

[13:05] do not generally agree on it. So it can

[13:07] be challenging to write like

[13:08] programmatic verifiers. Um so we have

[13:10] several ways of evaluating how computer

[13:13] use agents do on some of these

[13:15] benchmarks.

[13:16] Um the most obvious one is whether the

[13:18] action was correct. So you can measure

[13:20] whether a click action was uh done on

[13:23] the correct item. Um you can also

[13:26] measure the outcome which is probably

[13:27] the most endto-end fashion. So you give

[13:29] it a task like buy me a blue mark and

[13:31] you measure the outcome of whether it

[13:33] actually managed to um purchase the item

[13:35] or not. So this can be done through

[13:38] either like um checking the state if you

[13:40] have a simulated environment or you can

[13:42] just look at the trajectory of the agent

[13:44] and decide whether it um provided enough

[13:46] evidence that it did the task.

[13:49] Um, and lastly, I think you also want to

[13:51] measure whether the model respected any

[13:53] constraints that might be inherent or

[13:54] explicit in the task. So, for example,

[13:57] you might want it to navigate to the

[13:58] checkout page but not actually check

[14:00] out. Um, so you also have some other

[14:02] like uh verifiers to make sure that it

[14:04] did the task while respecting any

[14:06] userdefined constraints. So, I think

[14:08] evaluation is generally very challenging

[14:10] for Kas. Um, there's a few broad

[14:13] categories of evals that we'll go

[14:14] through today. Um, so broadly speaking,

[14:16] I've categorized them into four

[14:18] different categories. So the first one

[14:19] that we'll talk about is static

[14:21] evaluations.

[14:23] Um, so let's go back to our task. Add a

[14:25] blue mark under $20 to the cart and do

[14:27] not purchase. Static evaluations measure

[14:30] whether every action along the the

[14:32] trajectory of the agent is correct or

[14:34] not. So for example, you might start off

[14:35] on this screenshot and your agent would,

[14:38] you know, try to attempt to click on

[14:39] this blue mark here. um we might have

[14:42] some ground truth reference rule like we

[14:44] want XY that the agent predicts to be in

[14:46] a target box. If it's if the prediction

[14:49] is within a target box for example this

[14:51] red box here we give it a score of one.

[14:54] Um otherwise we kind of give it a score

[14:55] of zero meaning that it did not perform

[14:57] the correct next action at this point.

[15:01] Um so in this case like for static evals

[15:03] uh we consider it to be correct if the

[15:05] current step produces the correct action

[15:07] or not. Um so this this because it's

[15:10] static you can't really like roll out

[15:11] the agent end to end. Uh we just

[15:13] consider actions at every point um to

[15:16] determine whether it successfully

[15:18] accomplished the current action.

[15:21] One canonical example for benchmarks in

[15:23] this area is known as screen spot pro.

[15:26] Um so screen spot pro is what we call a

[15:27] grounding benchmark. Um it tests the

[15:29] abilities of the models to ground

[15:31] actions in the screenshots and it

[15:33] consists of a variety of applications

[15:35] operating systems and about 1,500

[15:38] different screenshot examples. The

[15:40] evaluation in this case is the perpoint

[15:43] uh accuracy. So for example this task of

[15:46] constructing a UV spear mesh um you have

[15:50] this like uh Blender screenshot here. So

[15:52] this is a screenshot. It's not an actual

[15:54] environment. So the agent does not have

[15:56] access to any interactive environment.

[15:58] is just given this screenshot and the

[16:00] goal is to determine whether it produces

[16:02] an action that falls within this red

[16:04] bounding box over here. So if it if it

[16:07] predicts a click action that falls

[16:08] within this uh bounding box, we consider

[16:11] it to be a correct action. Otherwise, we

[16:13] consider it to be an incorrect action

[16:15] and and we don't give it any any reward.

[16:19] Another example of a static benchmark is

[16:21] mine to web um which tests a bit more of

[16:24] a variety of actions. So um you can

[16:26] think of this as like next action

[16:28] imitation in this case given a current

[16:30] screenshot and a task. Um for example

[16:32] rent a car in Brooklyn central um I'm

[16:35] supposed to predict the next action that

[16:36] my agent will take. Uh so in this case

[16:38] the ground truth action is to click on

[16:40] the car tab and um no actual action is

[16:43] executed on this task. You're given a

[16:45] series of screenshots and your agent has

[16:46] to predict the next action condition on

[16:48] that screenshot. So once it predicts the

[16:50] action we score it and we provide it the

[16:52] next screenshot from our offline data

[16:54] set. So again, this is not actually

[16:56] executing any actions in the

[16:57] environment. There's no environment in

[16:58] this case. It's a series of static

[17:00] screenshots and ground truth actions.

[17:02] Um, so as you can imagine, this kind of

[17:05] evaluation is very fast. It's very cheap

[17:07] to run because you don't actually have

[17:08] to support an environment or simulation.

[17:11] You just have to provide it screenshots

[17:12] and measure whether the resulting

[17:14] predicted actions are within uh the

[17:16] ground truth set. Um but one problem as

[17:20] you can imagine with static evals

[17:22] um is that there's a lot of

[17:26] uh false negatives uh in the sense that

[17:30] for this screenshot and for this task

[17:32] there's a bunch of different actions

[17:33] that you can click that you can perform

[17:35] that would be considered correct uh like

[17:37] for example I don't really have to click

[17:38] the car tab in this case I could adjust

[17:40] the dates um to begin with and that

[17:42] would also be considered a valid action

[17:44] but in static evals because you have a

[17:46] set of ground troop actions um we we

[17:49] actually would mark those as as

[17:50] incorrect. Um so that's one of the main

[17:52] drawbacks of static evals. They are very

[17:54] fast but they don't really measure the

[17:55] thing that you care about uh which is

[17:57] the true end toend performance. So I

[17:59] think what we actually care about is

[18:00] whether the agent successfully did the

[18:02] thing at the end of the day. Um which

[18:05] brings us to our second type of

[18:06] evaluations which are end to end

[18:08] evaluations.

[18:09] Um so again like let's let's look at

[18:11] this example task like add a blue monk

[18:13] under under $20. um we might have an

[18:17] agent execute this task in an

[18:19] environment or on the real web and at

[18:21] the end we can uh check whether the

[18:22] agent did it correctly by using some uh

[18:25] programmatic unit test like checks. So

[18:27] for example um an agent might have

[18:29] attempted attempted this task and at the

[18:32] end of the trajectory we can uh run

[18:34] these like unit test like checks to see

[18:35] whether it actually did it. So this is

[18:37] done in a simulated environment. So we

[18:40] actually have like API access to all of

[18:41] the back end and state of the

[18:43] environment. Um so we can check whether

[18:45] the blue mark is in the cart uh whether

[18:47] the blue mark is less than $20 and

[18:49] whether the agent has not um actually

[18:52] place the order. So we check whether the

[18:54] order is the order count is zero and we

[18:56] only give it a reward of one if all of

[18:58] these individual unit tests pass. Um so

[19:01] this this is actually like a

[19:03] programmatic check. You actually have an

[19:05] environment in this case. So the agent

[19:06] is doing like whatever it needs to do.

[19:08] Um so we don't we don't check for the

[19:10] individual actions that the agent

[19:12] executes at every step but we do a check

[19:14] for uh whether it actually accomplish

[19:16] the task at the end based on these unit

[19:18] tests. So if your unit tests are

[19:21] comprehensive enough you could imagine

[19:22] that this is a very good uh reward

[19:24] signal um because we don't really

[19:26] supervise every single action of the of

[19:29] the model. Uh we just kind of like check

[19:31] whether it did it correctly or not at

[19:32] the end.

[19:34] So web arena was one of the first

[19:36] benchmarks to do this. uh web arena was

[19:39] a simulated um web navigation benchmark

[19:42] consisting of a few environments. Um so

[19:45] you have 800 about 800 tasks on four

[19:47] different uh apps that web arena uh

[19:51] hosts and the agent will execute all of

[19:54] these 800 tasks and at the end you kind

[19:56] of have a pro programmatic verifier as

[19:58] we discussed to check whether the agent

[19:59] did it correctly or not. So this is an

[20:02] example task. Um the goal is to create

[20:04] an empty repository called awesome LLM

[20:06] reading. So the agent will go onto this

[20:08] simulated gitlab uh repo. So importantly

[20:11] this is a simulated environment. It's

[20:13] something that you host locally. Uh you

[20:15] do not go on the real web at any point

[20:17] in time for for web arena. Um the agent

[20:19] has to try and accomplish this goal

[20:21] within the simulated environment and at

[20:23] the end of the task we run this

[20:25] programmatic verifier which basically

[20:27] checks for a bunch of conditions. Uh so

[20:30] you you essentially check whether it

[20:32] managed to create this repository or

[20:34] not. Um and all of these verifiers are

[20:36] handwritten by students uh by grad

[20:38] students at CMU actually. Um so they uh

[20:42] they hand wrote these verifiers for

[20:43] every single task in web arena and um at

[20:46] the end of the assuming you know the

[20:48] students did it correctly uh at the end

[20:50] of the execution um you would have a

[20:52] verifier that tells you whether the

[20:54] agent successfully did it or not. Um

[20:57] there there's still a few like uh false

[20:58] negatives and false positives because

[21:00] the verifiers are not comprehensive

[21:02] enough but on the whole it's a very uh I

[21:05] think it's a very nice benchmark. It

[21:07] definitely like led the way to people

[21:09] taking and evaluating coolers a bit more

[21:11] seriously.

[21:13] Um so I think it's important to contrast

[21:15] this with previous static evals because

[21:17] this actually measures the end to end

[21:19] performance. So you kind of just check

[21:20] for the outcome. you don't care about

[21:22] the individual steps as long as the

[21:23] agent did the task correctly. Um but you

[21:26] could also imagine that these this leads

[21:28] to some reward hacking. So the agent

[21:30] might uh you know try to accomplish the

[21:32] verifiers rather than actually doing the

[21:34] thing which is a common problem across

[21:36] most cool and and agent um evals and

[21:40] training generally. Um but I think this

[21:42] was a huge step up step up in in agent

[21:44] evals. Um so they made sure that you did

[21:47] it in simulated sandboxes and they uh

[21:50] measured like the outcome rather than

[21:52] the individual steps.

[21:55] Uh visual web arena was a an extension

[21:57] of web arena that kind of like treated

[22:00] it as a multimodal problem instead. Um

[22:02] so at this point when web arena was

[22:03] released most models were um handling

[22:06] the cooler problem or web browsing

[22:08] problem using accessibility trees which

[22:10] are kind of a simplified version of HTML

[22:13] and visual web arena actually uh tried

[22:15] to convince people that you kind of want

[22:16] to operate using screenshot based

[22:18] approaches. So visual web arena is an

[22:20] extension of web arena that consists of

[22:21] 910 uh visually grounded tasks. So all

[22:25] of the problems in visual web arena have

[22:26] to be solved using multimodal

[22:28] representations. Um and the evaluation

[22:30] is a bit similar. So you kind of have

[22:32] like programmatic checks as well. Um but

[22:34] you also have some multimodal based uh

[22:36] programmatic checks. So um there's some

[22:39] problems that you can't solve if you

[22:40] rely purely on HTML.

[22:45] Another form of evaluation for these

[22:46] benchmarks is instead of using

[22:48] programmatic verifiers, you kind of use

[22:50] an a different LLM to judge whether the

[22:52] model did the task correctly. So given a

[22:55] trajectory of a model, you prompt a

[22:56] different VLM or LLM. Um so a textbased

[23:00] LLM or multimodal uh vision language

[23:02] model uh you prompt it with the

[23:04] trajectory of the model and you ask it

[23:05] whether it completed the task

[23:07] successfully and this is also a very

[23:09] popular evaluation metric um because

[23:12] it's not always possible to write u

[23:14] verifiers for every single task that you

[23:16] care about. Um so in this case you again

[23:19] have the trajectory that the agent um

[23:21] completed and instead of a programmatic

[23:24] verifier you have a bunch of rubrics or

[23:27] or maybe you just even provide the task

[23:28] to the to the LLM. Um so you provide the

[23:31] trajectory of the agent and you provide

[23:33] the task and the the LLM kind of tells

[23:35] you whether it thinks the agent

[23:36] completed the task successfully or not.

[23:39] Um so typically like these judges they

[23:42] produce a short chain of thought

[23:43] followed by a judgment for example pass

[23:45] or fail or sometimes uh you assign like

[23:48] um floating point scores but typically

[23:50] the judge tells you whether you pass or

[23:52] fail or not. Um so this is a bit more

[23:54] general because you don't need to write

[23:55] verifiers for every single task in your

[23:57] benchmark. Um but it's also a bit more

[24:00] prone to like false uh false positives

[24:02] and negatives because um you can imagine

[24:05] that your LLM judge can be easily fooled

[24:07] into thinking that a task was

[24:09] successfully accomplished when it was

[24:10] not. Um but in general this is a lot

[24:12] more uh flexible

[24:15] and um several benchmarks that use this

[24:17] form of judging include web voyager

[24:19] which was one of the first benchmarks

[24:21] that tested the abilities of coolers to

[24:23] navigate on the real web. Um so this is

[24:25] very different from web arena because um

[24:27] what they did is they actually came up

[24:29] with 15 different websites and 600 tasks

[24:31] on these websites and they told the uh

[24:34] the benchmark is to actually go on the

[24:35] real web on these websites to accomplish

[24:37] certain goals. Um so actually if you go

[24:39] on some of these websites in the

[24:40] benchmark like there's this recipe site

[24:42] called all recipes. If you look at some

[24:44] of the task that the agent is supposed

[24:46] to do you can actually see some traces

[24:48] on the real web of previous agents

[24:49] attempting this task. uh which is

[24:51] actually it's not great but you can um

[24:54] see some evidence of why we might not

[24:56] want to evaluate agents on the real web.

[24:58] Um but nevertheless like web voyager was

[25:01] still quite valuable because it tested

[25:03] the capabilities of these agents on non

[25:05] simulated environments. So it's

[25:07] basically as close to a real world

[25:09] evaluation as you can get. Um it gets

[25:11] agents to go and do these things on the

[25:13] real web. Uh for example like find the

[25:15] most start GitHub project for climate

[25:17] change data visualization. um they they

[25:21] uh deploy like who was to go on the real

[25:22] GitHub and do a bunch of search and uh

[25:25] find the actual most start GitHub repo

[25:27] for this task. Um and in this case

[25:30] because it's going on the real web you

[25:32] can't really have programmatic verifiers

[25:33] because you can't really uh query the

[25:36] real web for its state. Um so the eval

[25:39] here is the VLM judge that we talked

[25:40] about. So the judge which is a different

[25:42] LLM gets the uh series of actions and

[25:46] screenshots that the agent has has taken

[25:48] and observed. Um it gets the original

[25:50] task. So it sees this task. It sees what

[25:53] the agent has done and it kind of

[25:54] predicts whether the agent succeeded or

[25:56] not. So we we evaluate this problem with

[25:59] like VLM judges. Um no programmatic

[26:01] verifiers. Um so this is kind of like

[26:05] you can think of it as quite uh wild

[26:07] wild west evals. you deploy something on

[26:09] the real web, you run a judge and you um

[26:11] you know at the end of the day say

[26:12] whether it's succeeded or not. But I

[26:14] think a lot of people like this because

[26:16] it's in some ways as close to a real

[26:18] world eval as you can get.

[26:22] Online mind to web was a was a different

[26:24] eval that followed up on web voyager. Um

[26:26] so it's a bit more comprehensive. The

[26:28] judge is a bit more stronger. So they

[26:30] show that the judge actually has about

[26:32] 85% agreement with humans. Um so it's

[26:35] very close to uh being uh human level

[26:38] agreement for for judges. Um but

[26:40] essentially uh online Mind2 web also

[26:42] looks at real world evals. Um so they

[26:45] expanded to about 136 websites and 300

[26:47] tasks and they get LLMs to go on these

[26:50] 136 real websites to accomplish certain

[26:53] tasks. Um and they they show that uh it

[26:58] actually um using this judge is a bit

[27:01] more accurate compared to Web Voyagers

[27:02] judge. Um so they they have a bit more

[27:05] of a complicated judge with different

[27:06] rubrics and and criteria. Um but

[27:09] essentially this also goes on the real

[27:10] web and it inherits it inherits a lot of

[27:13] problems that going on the real web um

[27:15] poses similar to web voyager. Um but

[27:19] again it's a very nice eval because it's

[27:22] [snorts] in some ways as close to a real

[27:23] world eval as you can get. Um so this is

[27:26] completely automated but you have an LLM

[27:28] judging the task. You have an LLM

[27:30] attempting the task on the real world.

[27:31] Um and because

[27:34] uh the judge is very close to human eval

[27:36] kind of have this automated pipeline of

[27:38] an LLM going on the real world doing

[27:40] something and you have a human-like

[27:41] judge determining whether it succeeded

[27:43] or not. So I think it's a very nice

[27:45] benchmark um very automated uh but again

[27:48] I think people don't really use this uh

[27:50] recently anymore because it's um

[27:52] essentially solved by modern models and

[27:56] I think as cool words have gotten more

[27:58] popular um people have also become a bit

[28:01] more careful about deploying them on the

[28:02] real world um because these website

[28:04] owners really don't like having like

[28:06] tons of agents ping ping their websites

[28:08] to to do a benchmark um yeah you can

[28:11] imagine that if your website got

[28:12] included in this benchmark and you

[28:14] started getting a lot more traffic, uh

[28:15] you probably also wouldn't be very

[28:17] pleased about it.

[28:20] Yeah. Um so one I think one important

[28:22] thing is that all of these evaluation

[28:24] metrics that we talked about are very um

[28:27] they are programmatic verifiers or they

[28:29] are LLM judges. Um so they are kind of

[28:32] like proxies uh to determine whether we

[28:35] successfully accomplish a task or not.

[28:37] Um but human review meaning uh getting

[28:39] humans to judge whether the agent did

[28:41] something or not is probably still the

[28:42] gold standard. So uh these papers also

[28:46] ran like a human evaluation baseline

[28:48] where they got humans to review the

[28:50] trajectories of agents and um you get a

[28:53] few humans per trajectory to determine

[28:55] whether the agent succeeded or not. Uh

[28:57] and at the end you uh kind of like get

[29:00] humans to vote whether the agent

[29:01] succeeded or not. Um, this is in some

[29:03] ways like still the gold standard of

[29:04] determining whether an agent

[29:06] successfully accomplished a task, but

[29:08] this is very expensive to run. So, it's

[29:10] not really possible to do this for every

[29:12] single task in your benchmark or every

[29:15] single um uh like debug or validation

[29:18] run that you want to do. Um, but this is

[29:20] something that most benchmark creators

[29:21] still do. Uh, get humans to attempt the

[29:24] task or judge the task and and determine

[29:26] whether the agent is doing the right

[29:28] thing. Um, but this is very expensive.

[29:31] So it's typically just done once or

[29:33] twice for ensuring that your agents or

[29:36] your benchmark is uh reasonable.

[29:44] So the other type of evaluation that

[29:45] people typically do is um they're also

[29:48] end to end evaluations but they're done

[29:50] on like desktop computers or mobile

[29:52] devices instead of of the web. Um so the

[29:54] web is quite interesting because you can

[29:56] do a lot of things on the web. Uh I

[29:57] think personally most of my time is

[29:59] spent on Chrome as well. Um but there's

[30:01] a different set of tasks where uh

[30:04] require you to operate an actual virtual

[30:07] machine or an actual desktop and um

[30:09] there's also several benchmarks that

[30:10] measure this in an end toend fashion. Uh

[30:13] we've already talked about OS world

[30:14] which is one of the canonical cua

[30:16] benchmarks. Um so this is a real Linux

[30:20] virtual machine that you can spin up. It

[30:22] consists of about 369 tasks across nine

[30:25] different applications like um uh

[30:28] Libra Office, uh Chrome and and so on.

[30:32] Um it's 369 tasks across nine different

[30:34] applications. And for each of these

[30:36] tasks, they also have programmatic

[30:38] verifiers. So your agent has to um go

[30:41] into these virtual machines, attempt the

[30:43] task across multiple different apps, and

[30:45] at the end, we run some uh unit test

[30:47] like checks to see if it succeeded or

[30:49] not.

[30:51] So some examples of task in OS world are

[30:53] for example uh you might want to update

[30:56] uh this Libra office uh calcul sheet um

[31:00] using receipts in a different folder. So

[31:02] in this case your agent has to navigate

[31:04] to the folder find the receipts it has

[31:06] to enter like the appropriate uh values

[31:09] in this um workbook and it has to save

[31:12] the workbook. So it has to do this uh

[31:14] navigate across different apps um handle

[31:16] like entering items in in this uh Libra

[31:19] office and uh basically like accomplish

[31:21] this task based off just an initial user

[31:24] instruction.

[31:26] After the agent thinks it's done, we run

[31:28] all of these like unit tests that we

[31:29] have. So we check whether the the

[31:31] spreadsheet consists of the items that

[31:33] we think uh should be there and we

[31:35] assign it again a 01 score of whether we

[31:37] think it succeeded or not. So kind of

[31:40] like very similar in spirit to web arena

[31:42] but um in this case it's using uh real

[31:45] world apps. So these are apps that

[31:46] people actually use on a day-to-day

[31:48] basis and it's operating again in a full

[31:51] virtual machine. So it's not just

[31:52] confined to to Chrome or to the web

[31:54] anymore. It's uh operating over this

[31:56] virtual machine that consists of nine

[31:58] different apps. Um so it's a lot more

[32:00] broad and you could imagine that um with

[32:03] desktop agents we can automate a wider

[32:05] variety of tasks than if we just use web

[32:08] browsing agents.

[32:11] Uh Windows agent arena was a different

[32:13] benchmark that is kind of like inspired

[32:14] by OS World. Um but it's a benchmark

[32:17] created by Microsoft to uh test the

[32:19] performance of agents on Windows

[32:20] machines. Um so a lot of a lot of like

[32:23] productive work in the world actually

[32:25] happens on Windows machines and um I

[32:28] think this benchmark was quite nice

[32:29] because it measured the ability of

[32:31] agents to perform some of these tasks

[32:33] that are very common in enterprise

[32:34] workflows or in um other companies.

[32:38] Yeah. So it's uh again like you spin up

[32:41] a Windows virtual machine, you get an

[32:43] agent to attempt a task and at the end

[32:45] you have some uh verifiers to determine

[32:47] whether it did the task correctly or

[32:48] not.

[32:50] And again like because we're using

[32:51] programmatic verifiers um some of these

[32:54] are also very prone to having false

[32:55] positives or false negatives but um you

[32:58] know they have their merits uh as LLM

[33:00] judges do um but these these are

[33:02] essentially some of the core end to end

[33:04] eval benchmarks that that um people have

[33:06] been exploring um from the 2024 to 2025

[33:10] period. Yeah. Um most of these

[33:14] benchmarks are actually quite well

[33:17] solved by modern coolers. So for example

[33:20] the recent GPT6 release I think achieves

[33:22] like much higher than human performance

[33:24] on most of these benchmarks. So um the

[33:27] community has actually um recently

[33:31] [clears throat] um put a bit less

[33:32] attention on these benchmarks that I

[33:34] just mentioned um and they've started to

[33:36] look at a bit more like longer horizon

[33:38] or um uh specialized benchmarks I would

[33:42] say. So long horizon computer use is

[33:44] this other it it's actually the same

[33:46] task but the problems that we care about

[33:48] span uh much longer horizons. So some of

[33:52] these tasks can take actual humans hours

[33:54] or even like two to three hours or even

[33:56] longer to complete. Um so now we're

[33:58] really like stress testing the abilities

[34:00] of kas to complete um things that humans

[34:02] don't actually want to do or we're

[34:04] getting them to complete like longer and

[34:05] longer tasks. A lot of the ones that

[34:07] we've seen in OS world the web arena uh

[34:09] typically take a human about uh 10

[34:12] minutes or 20 minutes or less to

[34:14] complete. Um, but some of the ones that

[34:15] we'll see in the following slides can be

[34:18] several hours operating over potentially

[34:20] specialized software. So, we're really

[34:22] getting to the point where we're trying

[34:24] to get them to be better than like

[34:26] expert human use of the computer.

[34:29] Um, a lot of these long horizon

[34:31] benchmarks, they follow a very similar

[34:33] evaluation strategy. So, you kind of

[34:35] have this action trace which represents

[34:37] what actions the LLM has taken uh on

[34:40] this environment. Um and you have a few

[34:42] different checks because it's long

[34:43] horizon. Um people tend to impose like

[34:46] more rubric based approaches. So the the

[34:48] version where we have a single outcome

[34:50] reward of whether it successfully did it

[34:52] or not is not so useful for long horizon

[34:54] because it's very sparse. Um the rewards

[34:56] are very sparse. Um the agent can be

[34:59] doing a lot of useful work in the

[35:01] interim but fail to achieve a perfect

[35:04] score. Um so we kind of have like a lot

[35:06] more fine grain rewards for long horizon

[35:08] computer use. Um there's a few different

[35:11] checks here. So state check is the

[35:12] interim rewards that I mentioned. Um

[35:14] these are kind of like rubric based

[35:16] rewards where they check whether the

[35:17] agent did um an intermediate task

[35:20] successfully and you kind of have a

[35:22] process reward where um this essentially

[35:24] checks whether the agent completed the

[35:26] entire task successfully end to end. Um

[35:29] so this is kind of like the ultimate

[35:30] reward but we have some intermediate

[35:31] rewards to ensure that we have some

[35:34] non-zero signal for long horizon

[35:36] computer use.

[35:38] Um and of course you can always have a

[35:40] final verdict for whether the agent

[35:41] successfully did it or not. Um but again

[35:44] because we're looking at long horizon

[35:45] computer use uh this is very sparse. So

[35:48] often times like a lot of models get uh

[35:50] a zero on the final reward which is why

[35:52] you kind of want to have intermediate

[35:54] rubrics or um uh process rewards.

[36:00] Yeah. And and importantly um as I

[36:02] mentioned like having a a good

[36:03] deliverable at the end is not always a

[36:06] great evaluation metric for long horizon

[36:08] computer use because it's so long. Um so

[36:10] you kind of want to have some interim uh

[36:12] rewards to ensure that the model was

[36:14] doing productive things in the meantime.

[36:18] Uh Odyssey's was a benchmark that we

[36:20] built here at CMU that measures long

[36:21] horizon uh web browsing. So Odyssey's

[36:24] consists of 200 tasks. Um we have uh

[36:28] rubrics for every task. So, we have a

[36:30] set of um things that we believe the

[36:32] model should complete. Uh so, for

[36:34] example, for this task, um plan a trip

[36:36] to a Palm Springs wedding. Um there's

[36:39] eight rubrics that the model needs to

[36:40] satisfy in order to perfectly accomplish

[36:42] the task. Uh for example, you need to

[36:44] find a a non-stop flight from Pittsburgh

[36:46] to to Los Angeles. Um you need to uh

[36:51] find a drive time within the 9:00 a.m.

[36:53] to 4 p.m. window. and you have a bunch

[36:56] of these criterias that you need to

[36:57] satisfy in order to accomplish the task

[36:59] successfully. Um so Odyssey's kind of

[37:01] like grades performance across many

[37:04] different rubrics um allowing you to

[37:06] have partial rewards instead of just a

[37:07] single binary pass or fail um outcome at

[37:10] the end.

[37:13] Yeah. So um this example I already

[37:14] mentioned we kind of have like eight

[37:16] rubric items um and the model needs to

[37:18] satisfy like each of the rubric items in

[37:20] order to achieve a perfect score idea.

[37:23] Um, so this is kind of an in between of

[37:26] uh like it it's still LLM uh verified

[37:30] for the most part, but you kind of have

[37:31] like fine grain LLM verification because

[37:33] you don't just um produce a single pass

[37:36] or fail uh reward at the end.

[37:39] Um OS World also came up with a

[37:41] follow-up called OS World 2 and in this

[37:44] benchmark they actually tried to tackle

[37:45] like hourlong workflows. So OS World 1.0

[37:48] know was a lot of tasks that require

[37:50] just like minutes of of human time to

[37:52] complete and OS World 2 actually has

[37:54] about 108 tasks that that on on median

[37:57] require a human 1.6 hours to complete.

[37:59] Um so this is very uh the some of these

[38:02] workflows are very complex. Um they

[38:04] require like doing uh CAD modeling or 3D

[38:06] modeling or photo editing. Um so we're

[38:09] getting into the realm of like more

[38:10] specialized um software use. Um

[38:16] uh on average most Frontier agents that

[38:18] they benchmark required about 300 calls

[38:20] to make. Uh so this also um typically

[38:23] it's it's a few hours of like just

[38:25] benchmarking an agent. Uh so I think

[38:27] this gets to a point where it's a lot

[38:29] more interesting because you can see

[38:30] these agents uh even like productively

[38:32] working for hours at a time. Um, so it's

[38:35] very expensive to evaluate, but it's

[38:37] quite magical to like start in Eval,

[38:39] come back an hour later and you see that

[38:40] the agent is still productively making

[38:42] progress on some of these tasks.

[38:45] This is an example task uh from OS World

[38:48] 2 and um I don't know if I don't know

[38:50] about the median human, but I definitely

[38:53] uh would not be able to do this uh

[38:54] easily. So I think we're getting to the

[38:56] point where you have like expert level

[38:58] task. Um, so the task here is to build a

[39:01] a cat support bracket and export a model

[39:03] that matches this drawing. So you're

[39:05] provided with this reference drawing on

[39:07] the left and the goal of the model is to

[39:08] be able to produce this thing on the

[39:10] right uh by operating some like um

[39:12] computer aided design uh software. Um so

[39:15] I think this is this is actually very

[39:17] complex. Uh it requires like navigating

[39:19] 3D space. It requires knowing like what

[39:21] tools you have available in this

[39:22] environment and you need to be able to

[39:24] sustain work over like probably several

[39:26] hours because um a human would also take

[39:29] uh on the order of an hour or at least

[39:31] like half an hour to complete this task.

[39:33] Um so it has a lot of very interesting

[39:36] things. Um this is a visualization of a

[39:39] GPT6 a GPT6 model trying to attempt one

[39:41] of the OS world two tasks. So again like

[39:44] this is sped up 30 times. So it's

[39:46] actually much slower in practice, but

[39:48] you can actually see like navigating

[39:49] between a terminal environment, going

[39:51] back to the CAT software and um actually

[39:54] like doing 3D modeling uh autonomously

[39:56] for for about I think an hour of time.

[39:59] Um so it's actually able to design like

[40:01] these 3D parts quite well. Uh and this

[40:03] is a a very huge leap from the models

[40:06] that we had even like two years ago. Um,

[40:08] so we're getting to the point where

[40:10] these models are are very good at

[40:12] attempting many of these like long

[40:14] horizon paths. Yeah.

[40:19] Um, so I'll mention a few other

[40:20] benchmarks. So cool world long is

[40:22] another benchmark from CMU uh that tried

[40:25] to tackle like long horizon computer

[40:27] use. Um, so again this is uh very

[40:29] specialized environments across a

[40:31] variety of tasks for example healthcare

[40:33] task, engineering tasks or like uh just

[40:35] architecture and design task. um

[40:37] consists of 200 of these types of tasks

[40:40] and most of them require like 500 or

[40:42] more LLM calls. Um so again this is a

[40:44] few hours of human work time. Um and

[40:47] when this benchmark was released early

[40:49] this year most models scored a very very

[40:52] poorly on this benchmark but um I think

[40:55] recent models including GPD6 uh actually

[40:58] um achieved like close to 90%

[40:59] performance on this benchmark. So, uh,

[41:02] long horizon computer use and like

[41:04] computer use in general is very, uh,

[41:06] very close to being solved or some might

[41:08] say even solved because these models can

[41:11] outperform humans at a lot of these, uh,

[41:13] general software use tasks.

[41:17] Um, so hopefully I've convinced you that

[41:19] uh, some of these benchmarks are useful

[41:21] uh, or or most of them were useful at

[41:23] some point in time. Um and uh I think I

[41:27] think hopefully I've convinced you that

[41:29] they are very capable and have very

[41:31] interesting um uh capabilities. Uh they

[41:35] are very good nowadays at automating a

[41:37] lot of different types of tasks. Um so I

[41:39] think the natural next question is like

[41:40] how do we how are these models built?

[41:43] How do we build these models? How do we

[41:44] train them? And how do we introduce

[41:45] these type of capabilities to them? Um,

[41:48] so we'll talk a bit about like how how

[41:50] modeling typically works and also how uh

[41:52] these models are trained. But I think

[41:54] I'll pause for a few seconds for any

[41:56] questions about benchmarks because I

[41:57] know we covered a lot of different

[41:58] things.

[42:05] >> Yeah. So

[42:09] object

[42:12] [clears throat]

[42:20] for something that has a twoar.

[42:23] >> Yeah. So the question is whether any of

[42:24] these benchmarks assign um partial

[42:27] rubric rewards to intermediate steps. So

[42:29] for example, if the task is to add

[42:31] something highly rated to the card and

[42:34] you did do that but you have some like

[42:36] irrelevant items that you added, do you

[42:38] get penalized for that? Um I think

[42:39] that's a good question. Uh I think

[42:41] reward design is very tricky in a lot of

[42:43] these benchmarks. So um some tasks in

[42:46] web arena do have these kind of like

[42:48] penalization uh but a lot of the times

[42:51] like people design these benchmarks so

[42:52] that the answer is kind of unambiguous.

[42:54] So the problems are a bit artificial in

[42:56] a sense. So for example web arena might

[42:58] say add the top rated item to my cart

[43:01] and if you do that then um you kind of

[43:04] get like a perfect score but uh an agent

[43:06] I I've seen like agents reward hack by

[43:08] adding a ton of things to the cart um to

[43:10] try and accomplish the goal. So it

[43:12] depends a lot on the benchmarks. I think

[43:13] typically people don't really penalize

[43:16] it at such a fine grain manner but it's

[43:18] also because at the point where these

[43:20] benchmarks were created the agents were

[43:22] so bad that I think some of the reward

[43:24] scores were a bit more generous to begin

[43:26] with. Um so I think it's some benchmarks

[43:29] do have these things but it's not I

[43:30] wouldn't say it's like super common.

[43:34] Yeah, I think people tend to air on the

[43:37] side of like giving false positives than

[43:39] false negatives.

[43:42] >> Yes,

[43:43] >> this is not exactly like a benchmark

[43:45] question, but do you think there is like

[43:46] benefit in looking at other not?

[43:58] >> Yeah. So the question is whether there's

[44:00] benefits in using other modalities other

[44:02] than just pixelbased representations

[44:04] like screenshots. I think there

[44:06] definitely is. Um open AAI has said that

[44:09] um at least previous models and I assume

[44:12] Astra as well they use like the

[44:14] accessibility representations of the

[44:15] computer when available. So Mac OS has

[44:18] this like uh accessibility

[44:19] representation that essentially is for

[44:21] like visually impaired users. um it's

[44:23] kind of like XML like representations

[44:25] where they determine where they tell you

[44:27] like this area is a description of a

[44:29] certain item like this area is my chrome

[44:31] window and this area is my dock and so

[44:33] on. Um so the models at least GPD6 do

[44:36] use these representations when

[44:37] available. I think there is a lot of

[44:39] value in it um especially for uh if you

[44:43] want your model to be more robust. Um,

[44:45] I'm personally I personally really like

[44:48] the pure like screenshot based

[44:49] representations because it's very I

[44:52] think it's very general. So you train a

[44:53] model that takes in just screenshot

[44:55] representations. You can deploy it on

[44:57] any device without having access to the

[44:59] underlying internals of the of the

[45:01] device. So you can train a model on like

[45:03] Windows and it presumably gen

[45:06] generalizes a bit more easily to like a

[45:07] Linux or Mac computer um because they

[45:10] have different like underlying

[45:12] accessibility representations. for

[45:14] example. Um but yeah, I think models

[45:16] definitely use alternative

[45:17] representations. Yeah. Yes.

[45:20] >> Yeah. My question was around the rubrics

[45:22] itself.

[45:23] >> Yeah.

[45:23] >> I'm assuming rubrics are different for

[45:25] each dots. So are they one is that

[45:28] expert generated rubrics or is that like

[45:30] a synthetic rubric that you generate and

[45:32] then in terms of reward

[45:35] are they how what are ways to mitigate

[45:37] that from the rubrics?

[45:38] >> Yeah. So the question is um whether

[45:40] rubrics are generated by humans or I

[45:42] guess synthetically generated by LLMs

[45:44] and um whether reward hacking happens

[45:46] with rubrics and how you mitigate that.

[45:48] Um so at least for Odysseies most of the

[45:50] rubrics are LLM generated but human

[45:52] verified. Um so one common way of like

[45:55] generating these rubrics is actually uh

[45:57] related to the previous question where

[45:59] you give a model like privilege

[46:00] information. So you give it more

[46:02] information than it has at evaluation

[46:03] time. uh for example like some hints or

[46:06] some uh HTML representation and you kind

[46:09] of get it to do better than it would in

[46:11] a realistic eval scenario and based on

[46:13] that you can uh generate like more

[46:15] accurate rubrics um because you have

[46:17] like privilege information. Um so for

[46:19] Odysseies and I think for a lot of uh

[46:22] industry benchmarks rubrics are

[46:24] typically these days like LLM generated

[46:26] by by human verified. Um sometimes not

[46:28] even human verified but verified by a

[46:30] different LLM uh that that has like

[46:33] potentially different information. But

[46:36] um yeah, I think I think this is quite

[46:38] reasonable these days to do like

[46:40] synthetic generation, but I personally

[46:42] still feel that a human has to uh look

[46:45] at everything that you put into a

[46:46] benchmark at some point in order to make

[46:48] sure that that it's um uh legitimate. Um

[46:51] I think reward hacking definitely

[46:53] happens a lot for um training these

[46:56] models. Um yeah, I think we can talk a

[46:59] bit more about that in the training

[47:00] section, but essentially I think reward

[47:02] hacking is a hu huge problem. I would

[47:04] say that rubric based rewards actually

[47:07] mitigate reward hacking a bit better

[47:08] than outcome based rewards. Um because

[47:10] you kind of have like these different

[47:12] criteria that you need to satisfy. Um if

[47:14] for example like if you just want to buy

[47:16] like the top rated item then you can

[47:18] reward hack by adding every single thing

[47:19] on the site to your cart for example.

[47:21] Whereas you could imagine that rubric

[47:22] based rewards uh check for this.

[47:26] Yeah.

[47:27] >> Yes.

[47:29] >> Do you have any sense about whether

[47:31] these academic benchmarks are used for

[47:34] evaluation or also do people train on

[47:36] them whether academia or industry?

[47:39] >> Yeah. So the question is whether um

[47:40] people train on these benchmarks in

[47:42] academia or industry. Uh well you're not

[47:44] supposed to train on these benchmarks

[47:46] because you're kind of like uh testing

[47:48] on the thing you're training on. But I

[47:50] think uh it's kind of like common in

[47:53] industry to generate tasks that are very

[47:55] similar to your benchmarks. Um so it's

[47:57] very common for people to uh produce

[47:59] tasks that are like OS world like or web

[48:02] arena like and train on those things

[48:03] instead. Um so that it's like in

[48:06] distribution but you're not really

[48:07] training on the same test set. So I

[48:09] think that's very common. Um cool world

[48:11] also actually has an explicit training

[48:13] set. Um so for some benchmarks they have

[48:15] like train validation and and ideally

[48:18] test splits um that people can train on

[48:20] but um you're not supposed to train on

[48:23] the the actual eval but it's uh I think

[48:26] people do find like proxy signals for

[48:28] essentially doing that. Yeah

[48:30] unfortunately

[48:33] cool yeah maybe the last question and we

[48:35] can move on. Yeah

[48:38] >> I was curious what

[48:42] representation What is the action space?

[48:46] >> Yeah. Um,

[48:48] >> yeah. So, the question is what the

[48:50] action space is actually for KUS. Um, I

[48:52] I think we'll cover this very quickly.

[48:54] So, maybe we can just uh do that in a

[48:56] couple slides. Yeah. But essentially,

[48:58] um, it depends on a model by model basis

[49:01] and it also depends like what

[49:02] environment you want to deploy the model

[49:04] in. Um,

[49:07] yeah. So, how how do we um how is a KUA

[49:10] represented? As you might have guessed

[49:11] by now, as is with most models in AI

[49:14] these days, a cool is basically an LLM

[49:17] prompted and accepting inputs in a

[49:20] certain format. Um, so more

[49:22] specifically, it's a it's typically a

[49:24] vision language model because most

[49:25] models take in um screenshot

[49:27] representations. So you have a goal

[49:30] that's typically represented in natural

[49:31] language. Like again um sorry to use the

[49:34] same example multiple times, but the

[49:35] goal might be like buy me a blue monk

[49:37] that's less than $20. And you might have

[49:39] an initial screenshot that is based on

[49:42] what your environment initially has. So

[49:44] you have a goal and a screenshot. Uh

[49:47] this goes into your your policy which is

[49:49] essentially an LLM. Um and your LLM

[49:52] produces an action. Um so typically this

[49:54] is represented as like text. So your LLM

[49:57] produces some structured representation

[49:58] in text of what action it wants to

[50:00] produce. So this might be a click action

[50:02] with X and Y coordinates. Uh again we

[50:05] then execute this action. um we add it

[50:08] to the to the context that we feed into

[50:10] the LLM at the next step. Um we also get

[50:12] a new screenshot after we execute this

[50:14] action. So we get screenshot one after

[50:16] executing action one or screenshot zero.

[50:19] We again concatenate this to the context

[50:21] that we already have. Um we feed this

[50:23] again to the LLM and it produces the the

[50:25] next action that we are supposed to

[50:27] execute. We then execute this action

[50:29] again on screenshot one um and get a new

[50:31] screenshot and we concatenate this to

[50:34] the context and we we we again feed it

[50:35] to the LLM. So, um, you repeat this

[50:38] until until your LLM thinks it's done or

[50:40] until, uh, you run out of budget, I

[50:42] guess. Yeah. Um, so you have this loop.

[50:45] Um, it's typically called a react loop,

[50:48] reasoning and action. Um, and at every

[50:50] step, you add in you you concatenate the

[50:52] action that you produce the new

[50:54] screenshot to your ever growing context

[50:56] and you feed this back into the LLM. Um,

[50:58] so it's an interle like vision language

[51:00] interle uh, action history. you have

[51:03] natural language in the form of goals,

[51:05] actions. You also have like pixel inputs

[51:07] or potentially other metadata. Um, and

[51:10] this essentially is like concatenated

[51:13] into this long sequence, this long

[51:14] multimodel sequence that you feed into

[51:16] your language model. Um, so this grows

[51:19] and grows. Um, there's different ways

[51:21] that people used to handle like longer

[51:23] and longer context, but essentially, uh,

[51:25] you feed in like the context, um, to the

[51:28] LLM at every step and it generates the

[51:30] next action at that point in time.

[51:32] Um, of course, like we don't actually

[51:34] feed in the actual pixel inputs. Uh,

[51:36] typically for most language models, you

[51:37] would tokenize this in some way. So, you

[51:39] would tokenize like your natural

[51:40] language to become uh text tokens. You

[51:43] would convert your screenshots into like

[51:44] visual tokens or or some like pixelbased

[51:47] representations. And the nice thing

[51:49] about modern language models is that um

[51:52] this is typically just like concatenated

[51:54] directly. So, what it looks like to the

[51:56] model is that you have a bunch of

[51:57] embeddings uh that you feed into it at

[52:00] every single step. the model produces an

[52:02] action that you then tokenize and you uh

[52:04] concatenate it to the context. Um so you

[52:07] kind of just repeat this growing the

[52:09] number of tokens that you feed in at

[52:10] every step. Um and the model takes in

[52:13] that uh conditions on the context at

[52:15] every point. Um produces the next action

[52:17] and you kind of repeat this. So it's a

[52:19] very um nice and simple representation I

[52:22] think uh

[52:25] and and it works surprisingly well.

[52:27] Yeah. So you typically have like text

[52:28] that you convert into token embeddings.

[52:30] You have screenshots that you convert

[52:32] into visual embeddings. And all of this

[52:34] is just interled and concatenated and

[52:37] passed to your language model. Um and

[52:39] and these days your language model is a

[52:41] is a transformer. Um obviously that

[52:44] produces actions for the next turn.

[52:48] Yeah. So the question earlier about how

[52:50] like what action space we usually use.

[52:52] Um different models have different

[52:54] action spaces. uh if you squint they

[52:56] like generally look similar. So they

[52:58] typically have a set of actions that

[53:00] they can produce like click actions,

[53:02] scroll actions um or whatever other

[53:05] actions you have in your uh environment,

[53:07] right? Um so different models produce

[53:09] them in slightly different ways. For

[53:11] example, you might produce them as like

[53:12] pi autogy outputs or you might produce

[53:15] them as just like two calls or XML. Um

[53:17] and you would have to like process this

[53:18] and pass it into something that you can

[53:20] actually execute on your environment.

[53:23] Yeah. Um, there's a question in the

[53:24] back.

[53:48] Yeah. So the question is why do we use

[53:50] screenshots rather than HTML? I think

[53:53] HTML is also a valid well HTML is very

[53:56] messy but people have done like

[53:57] simplified versions of HTML as

[53:59] representations. Um I guess one reason

[54:01] that most so most recent models do not

[54:04] use um or they primarily rely on

[54:07] screenshots. They sometimes still use

[54:09] metadata but uh to generalize it broadly

[54:12] most recent models use uh screenshots as

[54:14] inputs. And I think the reason for it is

[54:16] that it's a lot simpler. Um so it's it's

[54:20] a lot simpler to like take a screenshot

[54:21] of your computer rather than trying to

[54:23] process the uh underlying uh like

[54:26] accessibility metadata. um you you can

[54:28] like get HTML easily on the web but you

[54:31] can't really do it as easily for like

[54:33] desktop computer use right um so for

[54:36] that reason I think people like prefer

[54:38] screenshots a lot more because it's a

[54:39] lot uh uh more simplified and I think

[54:43] somewhat surprisingly to some the

[54:45] screenshot based representation has

[54:47] achieved like very very strong

[54:49] performance so it seems almost like

[54:50] unnecessary to use HTML or other

[54:53] structured representations um so I guess

[54:55] that that's kind of like um Why? Uh it's

[54:58] very simple and it and it works somewhat

[55:00] surprisingly well.

[55:03] >> Yeah, great question. I think um this

[55:06] was something that you know people did

[55:07] not really accept as readily even one

[55:10] year ago. Um

[55:13] but yeah, the multimodal models are very

[55:15] good. So it's uh surprisingly

[55:18] easy to do this.

[55:21] >> Uh yes, another question.

[55:23] >> So if

[55:26] it

[55:27] to pick a button

[55:30] or something. So the loading screen as

[55:33] well.

[55:35] >> Yeah. So um there's a bunch of like

[55:37] different design choices you can do with

[55:39] regards to like how you can handle these

[55:41] edge cases. Um sorry the question is to

[55:45] the question is like whether whether you

[55:46] would take a loading screenshot

[55:48] immediately or what do you do when when

[55:50] you execute an action. So I think

[55:52] computer use is annoying and also

[55:54] interesting because it encounter you

[55:56] encounter a lot of these like age cases

[55:58] and infrastructure problems compared to

[56:00] like math or or coding models. Um it

[56:04] this can be resolved in a couple of

[56:05] ways. I think the most common way that

[56:07] people do this is that you typically

[56:09] like sleep or wait for a few seconds

[56:10] after executing an action. So you would

[56:13] execute an action and you sleep for like

[56:14] 3 seconds before you take the screenshot

[56:16] and execute the next thing. Um so if you

[56:19] do see a loading screen at that point in

[56:20] time, models are typically trained to

[56:23] wait again for another um specified

[56:25] amount of time. Um yeah, there's more

[56:29] complex infra infra um there's like more

[56:33] complex ways of designing models where

[56:34] you kind of like wait until the

[56:36] screenshot changes, but I think the most

[56:38] simple and common way to deal with it is

[56:40] you just sleep. Yeah.

[56:47] Yeah. Thanks a lot for the questions. So

[56:49] um this is essentially at a high level

[56:52] like how almost all frontier coolers are

[56:54] trained uh to the best of my knowledge.

[56:57] Um sorry this is not how they're

[56:58] trained. This is how they are modeled

[56:59] and we'll soon like look a bit at how

[57:01] they are actually trained to do these uh

[57:05] um quite amazing things.

[57:11] Cool. So um with training a model uh

[57:15] essentially like most computer use

[57:17] agents are based on pre-trained uh

[57:20] vision language models. So training

[57:22] happens at a few different stages like

[57:25] obviously when you deploy GPD6 as a

[57:28] computer use agent uh you're not

[57:30] deploying I guess it's not obvious but

[57:32] you're not deploying a specialized

[57:33] version of GPD6 that can only do

[57:34] computer use. So it's kind of a general

[57:36] model that can have computer use as one

[57:39] of its capabilities and I think this is

[57:41] like increasingly the way that people do

[57:42] it. Um so computer use specific training

[57:45] happens at a few different stages. Um at

[57:47] the pre-training stage where models are

[57:49] trained uh with like large scale

[57:51] internet um data uh core specific data

[57:55] is typically injected in a few different

[57:56] formats. So you have kind of like your

[57:59] grounding data which is um data that

[58:01] encourages the model to learn to ground

[58:04] information in in screenshots. Um so

[58:06] this data typically looks at like the

[58:08] form of um you have a screenshot and you

[58:11] kind of have like a series of bounding

[58:12] boxes followed by coordinates. So what

[58:14] the model is learning to do here is that

[58:16] it's learning to um uh just like

[58:19] learning grounding abilities. So it's

[58:20] learning like if I want to click on the

[58:22] button I have to produce like these XY

[58:24] coordinates. So it's just learning like

[58:26] the most basic uh capabilities like

[58:28] learning localization, grounding and so

[58:30] on. Um you might also have some data in

[58:34] the form of like immediate actions. So

[58:36] this is actually very similar to the

[58:37] static evals that we talked about. Uh

[58:39] you might have these screenshots, you

[58:40] might have some like highle task and the

[58:43] goal here is to predict the next action

[58:44] that you will you will produce. Um so

[58:46] this is again like very noisy data. It

[58:49] might even be like synthetically

[58:50] generated. But the goal here in

[58:52] pre-training is just to introduce uh

[58:54] some form of like localization and

[58:56] grounding ability which the kua needs to

[58:58] do later on in order to um be able to

[59:00] produce like accurate click and um other

[59:03] types of actions. Yeah.

[59:07] Um after pre-training we typically have

[59:08] a post-training phase. Um so nowadays

[59:12] like this is typically mixed in with

[59:13] other model capabilities but uh to

[59:16] simplify it we can assume that we only

[59:17] care about like cooler for now. Um and

[59:19] in this post- training phase there's

[59:21] there's two different stages. So the

[59:23] first stage is that you typically do

[59:24] supervised fine-tuning um to train the

[59:26] model to mimic a human demonstration of

[59:28] of a computer use task. So you have a

[59:31] bunch of like human demonstrations that

[59:33] you can collect or otherwise like uh

[59:35] scrape from somewhere. Um, and this

[59:37] typically looks a lot like the

[59:39] trajectories that we already have. So

[59:40] the human is given a screenshot, the

[59:42] human does something and you record that

[59:44] action. So it might be a click action

[59:45] that the human does, you record that

[59:47] using some like specialized software

[59:48] that you have. Um, so you have a bunch

[59:50] of these like human demonstrations that

[59:52] essentially uh some humans um record

[59:56] humans doing cool like tasks. Um,

[59:59] nowadays it's also very common to make

[60:00] in synthetic data. So maybe you prompt

[60:02] your agent in a certain way or you

[60:04] prompt a stronger model to attempt the

[60:05] task and you kind of like keep the

[60:07] trajectories that you think are good. Um

[60:09] so this is like synthetically generated

[60:11] by a different model or the same model.

[60:14] Um and you also kind of mix this in. Uh

[60:16] so this is typically a bit lower quality

[60:19] and noisier than human data. But you can

[60:21] generate this at scale. So you don't

[60:22] need humans to actually produce this

[60:24] data. So it's actually generally still

[60:26] quite useful to have um this like

[60:28] synthetically model generated data in

[60:30] your post- training stage.

[60:32] Um the more interesting part I think is

[60:34] after this uh post- training supervised

[60:37] fine-tuning stage your model has some

[60:40] semblance of a cooler uh capability. So

[60:42] you can after after SFT you can

[60:45] typically prompt your model and it will

[60:46] do a decent job at most of these cooler

[60:48] tasks. I think the more interesting

[60:50] stage is um nowadays it's is it wasn't

[60:52] very common like one year ago but

[60:54] nowadays it's very common for kas to

[60:55] undergo an a reinforcement learning

[60:58] stage. So what happens here is that you

[61:00] kind of drop your cooler in a simulated

[61:02] environment or real world and you give

[61:04] it a thing to do. Um it it it will do

[61:06] that thing. So it will like try to buy a

[61:08] blue mark and at the end you will assign

[61:09] a reward to it either from like rubric

[61:11] based rewards, programmatic verifiers or

[61:14] like um just llm as a judge. You assign

[61:16] a reward to it in some way and you kind

[61:18] of do like reinforcement learning to

[61:20] reinforce the successful trajectories.

[61:23] Um so this is kind of interesting

[61:25] because it's like uh there is no human

[61:28] demonstration for these tasks. You kind

[61:29] of just let the model loose in a sandbox

[61:31] and it um tries a bunch of things uh

[61:35] learns from its uh successes and

[61:36] failures and it you you repeat this

[61:38] until until it's able to do this

[61:40] successfully. Um

[61:43] yeah so I think people are very excited

[61:45] about RL these days. Um but the other

[61:47] stages are also very important to ensure

[61:49] that the model has a strong foundation

[61:51] for doing RL.

[61:54] Yeah. So let's talk a bit more in detail

[61:56] about the various stages. So in the

[61:58] pre-training phase as I mentioned you

[62:00] kind of have these like screenshots and

[62:02] the goal of this pre-training data is

[62:03] just to learn uh very basic

[62:05] capabilities. So you probably learn like

[62:07] grounding abilities. um given this

[62:10] screenshot uh typically your model is

[62:12] trained to predict the next token uh for

[62:15] very long description that essentially

[62:18] boils down to like predicting the

[62:20] coordinates of items on the page. So you

[62:22] might have this like car label and the

[62:24] model has to predict the xy coordinates

[62:25] or the xy uh width and height of this

[62:28] bounding box. Um so it's kind of like

[62:31] very noisy data but data that you can

[62:33] imagine getting in very large quantities

[62:35] at scale. Uh so for example like this

[62:37] screenshot data it comes from the United

[62:39] website and you can easily generate like

[62:41] all of the bounding box and grounding

[62:42] data by just running a simple like

[62:45] JavaScript uh script on the website. So

[62:47] you can extract like all the bounding

[62:48] boxes. So you can collect this kind of

[62:50] grounding data very easily at scale

[62:52] which is why it's a great fit for

[62:53] pre-training where you want like a a lot

[62:55] of uh noisy but large volumes of data.

[63:01] The other type of data that people

[63:02] sometimes collect is um action

[63:04] prediction. Uh so you can collect for

[63:07] example in the same way from HTML pages

[63:10] you can get like the element name or

[63:12] element uh meta of certain things on the

[63:15] page and um you can provide this as as

[63:19] the input to the cool and has to predict

[63:21] again the xy coordinates of this. So

[63:23] this is a bit more like semantic

[63:24] understanding where you can provide like

[63:26] a HTML element and it has to predict uh

[63:29] what it wants to do or what it wants to

[63:30] click on. Um so again this is like very

[63:34] low-level capabilities. It's really just

[63:37] teaching the cooler how to understand

[63:38] screenshots and how to ground uh various

[63:40] items on the page.

[63:43] Yeah. So you basically learn like

[63:45] screenshot understanding. Uh you learn

[63:47] localization. So sometimes you learn

[63:49] like where items are on the page. uh you

[63:51] can also learn like the relationship of

[63:53] items with each other. So we know for

[63:55] example like the car button is to the

[63:57] right of the hotel button and uh this

[63:59] might be introduced in your pre-training

[64:00] data in Subway. Um but this is typically

[64:03] generated at scale and mixed into the

[64:05] early stages of frontier model

[64:06] pre-training um just so that our cooler

[64:09] has a bit of an easier time later on in

[64:11] in learning to ground and learning to

[64:13] produce actions.

[64:16] uh after pre-training the next stage is

[64:18] uh I think people typically call it

[64:20] post- trainining um so again like we are

[64:22] ignoring all the other data that goes

[64:23] into post- trainining and focusing on

[64:25] cooler data here um this typically comes

[64:28] in two forms so you have like human data

[64:30] where you pay a bunch of humans uh to

[64:33] annotate trajectories so you might give

[64:34] someone the task like find a birya taco

[64:37] recipe I could make in under three hours

[64:38] and a human here like actually attempts

[64:40] this task by navigating on a web browser

[64:43] um so over here like this example is

[64:44] from momo

[64:45] Momo web mix um where they collected

[64:48] like 36,000 human trajectories. So they

[64:50] collected 36,000 demonstrations of

[64:52] people doing tasks similar to this like

[64:55] going on the web and doing things and

[64:57] and um at every point you get the

[64:59] screenshot observation and you get the

[65:00] thing that the human did. Uh so you end

[65:03] up with a bunch of like screenshot

[65:05] action screenshot action trajectories.

[65:08] They also generated a bunch of um

[65:10] synthetic trajectories that we'll we'll

[65:12] talk about in a bit. Um but some open-

[65:15] source examples of like cooler data are

[65:17] Momo web mix and also agent net. So both

[65:20] of both of these papers essentially like

[65:22] collected human demonstrations uh of

[65:24] these tasks. So it's a very nice way to

[65:27] um train your cooler to like imitate

[65:30] human behavior. Um so condition on

[65:32] screenshot is trained to predict the

[65:34] next action in the sequence.

[65:37] Um, of course, increasingly so these

[65:39] days we can generate some like synthetic

[65:42] data for for this part of the training

[65:44] as well. Um, so Momo Momo web actually

[65:47] did this thing where they uh gave a

[65:50] model the accessibility tree of the

[65:51] website. So I think this was um uh

[65:54] addressed in some of the previous

[65:55] questions but uh some of these models do

[65:57] a lot better when you give them

[65:58] metadata. So they have a model that is

[66:00] trained to use like accessibility trees

[66:03] and they provide the accessibility tree

[66:05] which is essentially a simplified HTML

[66:07] representation uh to the model and they

[66:09] let this model like roll out taking

[66:11] actions in the accessibility tree space

[66:13] and they collect the same set of

[66:15] trajectories. Um so you kind of have

[66:16] this model that is using like privilege

[66:18] information that it might not have at

[66:20] actual eval and inference time. So it's

[66:23] uh doing a lot better than it would have

[66:24] if it just had screenshot inputs. Um, so

[66:27] you roll out this model, you collect

[66:28] like 105,000

[66:30] synthetic traces in this way and you can

[66:32] also um uh not not all traces are

[66:35] retained. So you can kind of like look

[66:36] at the traces and keep just the ones

[66:38] that you think are higher quality based

[66:40] on some metric like using a different

[66:42] LLM to judge it or using a human to

[66:43] filter them out. Um, so traces are

[66:46] collected in this way either with human

[66:48] demonstration or or synthetic data. Um,

[66:51] and one analogy I really like with the

[66:52] synthetic data version where you have

[66:54] privilege information is that um, I

[66:58] actually don't know if it's true, but I

[66:59] heard that Tesla actually deploy deploys

[67:01] their cars um, during training with LA.

[67:04] So they have these cars that have LA

[67:06] installed and they do like self-driving

[67:08] and obviously if you have like 3D LA

[67:10] information, you do a lot better. Um,

[67:11] and they collect those trajectories and

[67:13] they discard like the LAR information

[67:15] and they train their model to just use

[67:16] like the pixelbased information. So you

[67:19] kind of have a teacher that is using a

[67:21] lot better information than you would

[67:23] have at inference time. Um and I think

[67:25] for a lot of cooler applications, people

[67:27] have attempted similar ways of injecting

[67:29] like metadata or extra information um in

[67:32] order to collect better traces. Um so I

[67:35] think it's a very nice way of

[67:36] introducing synthetic data. Yeah.

[67:38] Question in the back.

[67:44] Especially

[67:57] with certain pixel values.

[68:02] >> Yeah. So the question is whether um if

[68:05] you do like pre-training does the

[68:07] coordinate uh representation generalize?

[68:09] So if you train it on a Mac, does it

[68:11] generalize to a tablet or maybe even

[68:13] like computers with other resolutions?

[68:15] Right? Um and I think typically the way

[68:18] that we collect like coordinate data is

[68:19] that it's normalized. So uh coordinates

[68:22] aren't usually represented in absolute

[68:24] uh formats. So they're represented in

[68:26] like um zero to a thousand. Zero zero

[68:29] zero meaning like top left of the screen

[68:31] and thousand thousand meaning like

[68:33] bottom right of the screen. So they're

[68:34] like completely normalized and in my

[68:37] experience it transfers quite well even

[68:38] when the absolute resolutions are

[68:40] different.

[68:42] Yeah. Cool. Um question

[68:46] >> more efficient way of doing it like

[68:48] perhaps

[68:53] a

[68:56] >> Yeah. So the question is whether there's

[68:57] like more efficient ways if you have

[69:01] >> instead of getting the screenshot

[69:06] through it just stoing like values what

[69:09] certain items are in some database

[69:13] you can just

[69:18] >> there are boxes just like a description

[69:21] of what the box does

[69:24] >> yeah I think that's a

[69:26] That's also a reasonable way to do it. I

[69:28] think models these days are not trained

[69:29] as uh like monolithic coolers. Like if

[69:33] you try using like GPD6 Astro, it

[69:35] doesn't always just do computer actions.

[69:37] It will interleaf like bash calls and it

[69:39] will like write code instead. So I think

[69:41] models like typically try to solve it in

[69:42] the most efficient way possible. Um so

[69:45] they definitely like do use that kind of

[69:47] data at training and also at inference.

[69:50] Um

[69:51] yeah.

[69:55] Oh, okay. Okay, cool. Uh, okay. I'll

[69:59] cover a bit more quickly then. Yeah,

[70:01] basically we have a bunch of like um uh

[70:04] open- source data that we can train

[70:05] models on these days. So, a lot of um

[70:08] different examples

[70:10] and the final stage of training is

[70:12] actually uh post- training RL. So as I

[70:14] mentioned in this stage you kind of like

[70:16] deploy the model in a simulated

[70:17] environment or if you are feeling um you

[70:20] know extra spicy you can also deploy on

[70:22] the real web but people don't really do

[70:24] that nowadays. Um so you typically like

[70:26] deploy the model it takes actions in a

[70:28] simulated environment and at the end it

[70:30] produces you get a reward from the

[70:32] environment or from some other judge and

[70:34] you update the policy based on the

[70:36] rewards. So uh broadly speaking like if

[70:39] you get a positive reward you upweight

[70:41] the actions that happen in that

[70:42] trajectory a bit higher and if you get a

[70:44] zero or negative reward you um

[70:46] downweight those actions. So your model

[70:48] essentially is trained to maximize the

[70:50] reward in an environment and in this

[70:52] case it's like doing it completely

[70:54] autonomously. So no human

[70:55] demonstrations. Um the tasks that the

[70:58] model is attempting might come from

[70:59] humans but uh typically it's like

[71:01] operating in an autonomous fashion.

[71:05] Yeah. And um hopefully it's obvious why

[71:07] we need simulated environments for RL. A

[71:10] lot of the tasks that we care about, we

[71:11] don't really want to execute them

[71:12] repeatedly on the real world. For

[71:14] example, you can only book uh an airport

[71:16] ride on Uber so many times before you

[71:18] get banned or you run out of money,

[71:20] right? So you kind of want like

[71:21] simulated environments to do

[71:23] reinforcement learning in.

[71:25] Um and there's several uh benchmarks

[71:27] that uh kind of like tackle the

[71:30] reinforcement learning building uh

[71:32] paradigm. Um so I think I won't go

[71:35] through these in detail but uh you can

[71:37] reference them on the slides. Um but

[71:39] essentially I like to show this graph

[71:41] which shows that the reinforcement

[71:43] learning part of post training is

[71:44] actually very important for uh

[71:46] introducing like strong cooler

[71:47] abilities. Um so you start off with a

[71:50] success rate after SFT of about.5 and if

[71:53] you do like reinforcement learning at

[71:55] the end you climb to about like 6 or or

[71:57] more. Um so it's a very important part

[72:00] of ka training and uh anecdotally it

[72:03] also introduces some abilities that is

[72:05] hard to do through human uh

[72:07] demonstration alone. So it's much easier

[72:09] to train a model to operate over long

[72:11] horizons um using reinforcement learning

[72:14] because you typically don't have human

[72:16] demonstrations of very long uh tasks.

[72:18] It's very expensive to collect those.

[72:22] Yeah. Um so to summarize yeah we covered

[72:26] like how coolers are trained. Uh you

[72:28] typically have a few training stages

[72:29] like pre-training um post- training

[72:31] where you do like behavior cloning on

[72:33] human demonstrations and synthetic data

[72:35] and you also have like the final cherry

[72:37] on top where you do the model uh

[72:39] reinforcement learning phase um of

[72:42] running it in simulation and getting

[72:44] rewards in the environment

[72:47] and hopefully by the end of this you get

[72:49] a strong cool. Um but at a high level

[72:51] this is like the pipeline that most labs

[72:52] use to train cooler models these days.

[72:56] So to summarize um kas are a bit

[72:59] different from other agents. I think

[73:00] they are uh kind of like really nice

[73:02] because they operate directly on the

[73:03] same interface as humans. Um it's very

[73:06] tricky to evaluate coolers and people

[73:08] have been doing it for for a while. Um

[73:10] but essentially we want to target the

[73:11] right metrics and level of behavior.

[73:14] Um cooler models are designed so that

[73:17] they predict actions from interled

[73:19] visual history. So you kind of have this

[73:21] interleaf context of screenshots and

[73:23] actions that you previously took and the

[73:24] model has to condition on this to

[73:26] produce the next action.

[73:28] Uh models these days are trained in

[73:30] multiple stages. So you have

[73:31] pre-training with large scale noisy

[73:32] data. You have SFT where you try to

[73:35] behavior clone human or synthetic

[73:37] demonstrations and you have a final RL

[73:39] phase where you uh let the model um roll

[73:43] out itself in simulated environments and

[73:45] you reward it for good behaviors and

[73:46] penalize it for bad behaviors.

[73:49] Um essentially that's uh probably the

[73:52] summary of all I have time to cover off

[73:55] cover today but I encourage you to visit

[73:56] the slides for some uh remaining takes

[73:59] on what we can still work on for Kers.

[74:02] Um, essentially I think speed is still

[74:03] an issue. Personalization is a very ripe

[74:06] area for research. Uh, infrastructure

[74:09] and UX is a big concern. And, um, I'm

[74:12] also very excited about multi- aent

[74:13] systems.

[74:15] Yeah. Uh, thank you for listening and

[74:20] happy to take questions for remaining

[74:22] time or Yeah. God bless.
