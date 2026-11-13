# Lecture 4 recording

[Course index](../../README.md) · [Original source](https://www.youtube.com/watch?v=6zigF2a-2Pw&list=PLSN0qpDfUvTM&index=4) · [Raw file](../../raw/videos/6zigF2a-2Pw.json)

Retrieved: 2026-11-13T16:48:26.752295+00:00

[00:01] Okay, welcome back everyone.

[00:05] >> So, um the first assignment is out and

[00:08] uh as Graham said, we we have credits

[00:10] available for you to to work on it for

[00:12] those of you who are enrolled in the

[00:14] class. Do you folks have any logistic

[00:16] questions? Cool. Okay. So we talked in

[00:21] the last lecture about how agents can uh

[00:24] choose what to retain within their

[00:26] context window as a way of you know

[00:28] storing information within a task and

[00:31] using that to um to determine what's

[00:34] important to do better within the task.

[00:36] So a big part of today is going to be

[00:39] about how can agents go beyond the

[00:41] context window and store information

[00:44] across tasks in external stores um that

[00:48] will be useful for them to improve

[00:50] performance on tasks in the future. And

[00:53] this is going to be skill induction. Um,

[00:56] and uh, we'll build on some some work

[00:58] that was done in the past on memory

[01:01] systems for agents. Um, and show how to

[01:04] apply those to to agents. But there's

[01:06] also another view on skills. And skills

[01:09] are a way for people to write

[01:11] instructions for an agent that can

[01:13] encode kind of like best practices or

[01:15] the knowledge that you have about how a

[01:18] task should be done. And these are

[01:20] actually going to be complimentary to

[01:22] each other. Um so we'll cover it just a

[01:25] small amount in this lecture but um you

[01:27] can imagine a system that um is sort of

[01:30] having a human in the loop um that's

[01:32] relying on the agent to uh propose some

[01:36] potential best practices from the

[01:38] experiences that it has a person edit

[01:40] those and goes back and forth or vice

[01:42] versa like you know having a skill and

[01:45] instruction that's written by a person

[01:46] be refined by the agent based on

[01:49] experience. So yeah, it's a lot of

[01:51] different viewpoints, but hopefully by

[01:53] the end of the lecture, you'll see how

[01:54] they can all sort of fit together.

[02:00] So let's just start off with some

[02:02] motivation about why you might want to

[02:04] remember things from one task to

[02:06] another. So say that we have an agent

[02:09] that's carrying out tasks in a website

[02:12] like a shopping site and you might give

[02:14] it a task like add Sony headphones to my

[02:16] wish list. So when we cover guey agents,

[02:20] you'll we'll get into the details of,

[02:22] you know, the representation space, the

[02:25] action space for how a system like this

[02:27] works. But at a high level, it's going

[02:29] to be producing actions like um uh

[02:33] navigating to the store website, finding

[02:36] the search box for it, typing some text

[02:38] in that search box, and then clicking

[02:40] search. And that's going to be the part

[02:42] that like searches for the headphones,

[02:44] right? And then we'll do something with

[02:45] them. We'll find the ones that match the

[02:48] request the user had and put them into

[02:49] our wish list.

[02:51] We might have another task that we carry

[02:54] out in the future like find the wireless

[02:55] keyboard price range. And if we're doing

[02:57] that on the same site, a lot of the

[03:00] actions are going to be reused, right?

[03:02] We'll go to the store, we'll find the

[03:03] search box, we'll search for the

[03:05] different product but in a similar way

[03:07] and then we'll do something different

[03:09] with it like you know getting the prices

[03:11] and reporting those back to the user.

[03:13] But if it's difficult for the agent to

[03:16] figure out how to do this search, once

[03:18] it knows how to do it, it should be able

[03:20] to reuse that knowledge in the future to

[03:23] be more effective on future tasks.

[03:28] So a lot of structure recurs and today

[03:31] is going to be about how can we

[03:32] represent this shared structure. So for

[03:35] example, is it best to just uh keep kind

[03:38] of the raw actions that the agent

[03:41] produced when it was carrying out this

[03:43] shared subtask or is it better to try to

[03:46] abstract it into for example a code

[03:48] function which could be run as a

[03:51] blackbox or maybe tested or even like

[03:54] hierarchically call other functions.

[03:57] We'll also be interested in how can the

[03:59] agent like determine which parts of a

[04:02] task should be reused in the future.

[04:05] And um as we're you know any time we

[04:10] have a memory that we're building up

[04:12] from experience, there's questions about

[04:14] um how do we grow that memory? Do we are

[04:18] we always adding to it? What happens if

[04:20] we get some conflicting information or

[04:22] we find a better way to do something? We

[04:25] might want to make edits to it. we might

[04:26] want to delete things if they no longer

[04:28] seem to apply. So, how can we um kind of

[04:30] manage the life cycle of these skills um

[04:34] and these subtask representations that

[04:36] are learned?

[04:39] [snorts]

[04:40] So, I'd say there's three general ways

[04:42] that we can get agents to update. So,

[04:45] the first one we covered in the last

[04:47] lecture. It's um just what you maintain

[04:50] in the context window of the model. So

[04:53] this is um you know in the standard

[04:55] React style way. It's the history of the

[04:58] past observations and actions that

[05:00] you've taken, messages you've gotten

[05:02] from the user, feedback from the

[05:04] environment, and you need to you need to

[05:06] choose like what to retain given kind of

[05:08] the limitations of the context window

[05:10] and the model's ability to use that. So

[05:15] uh we talked a lot about like compaction

[05:17] and methods for managing what's in that

[05:19] context window. Today we're going to be

[05:21] focusing on storing things outside of

[05:24] the context window. So even with like

[05:26] really long context windows that we have

[05:28] now of like a million tokens uh for um

[05:32] multiple for like carrying out multiple

[05:34] tasks with an agent um you're going to

[05:36] exceed that context window and you want

[05:39] to remember things from past tasks to

[05:41] help you on future ones. So if we are

[05:44] storing things outside of the window, um

[05:47] that's going to look something like a

[05:49] database um that needs to be managed um

[05:51] in some some way or um like a file

[05:55] system that the agent can access. And uh

[05:58] this lecture is going to be about

[05:59] methods for um putting things into those

[06:02] types of storage and um using them and

[06:05] updating them. And then the final way is

[06:08] going to be like actually making uh

[06:10] updates to the weights of the model.

[06:12] Right? So this looks more like standard

[06:15] supervised fine-tuning or reinforcement

[06:16] learning. We'll cover that in a few

[06:18] lectures later on. But each of these has

[06:21] like pros and cons. So um I think like a

[06:25] main pro of using external artifacts is

[06:28] that they're like they can be ported

[06:31] across models, right? So if you um have

[06:34] a description of the way to search for a

[06:38] product um that could be used by any one

[06:40] of a number of different models um

[06:43] within an agent framework. Whereas if

[06:45] you're actually making updates to the

[06:47] weights of the model that's just an

[06:49] update for that specific model and it

[06:51] doesn't transfer to others. So external

[06:54] artifacts are also more inspectable by

[06:57] people. Um, so you could write down best

[07:00] practices or how to search on a site.

[07:02] The agent can use that. The agent could

[07:04] also propose, you know, kind of text for

[07:06] that and you could look at it and make

[07:08] changes to it. So there's it's easier to

[07:11] kind of like have an interface between

[07:13] the person and the system if your um

[07:16] method of updating, if your method of

[07:18] remembering is interpretable.

[07:21] Any questions about this?

[07:25] How many folks have uh have used skills

[07:28] in their interactions with the coding

[07:29] agent? Like how many of you Okay, so

[07:31] most folks have. How many of you are are

[07:33] writing the skill yourself?

[07:36] Okay, so maybe about half the folks who

[07:38] are using skills. How many of you have

[07:40] uh gotten an agent to write a skill for

[07:42] you? Okay, so a lot of folks actually

[07:45] have. Yeah. What are some things that

[07:47] what how what's your experience been for

[07:49] the agent writing the skills? How often

[07:51] have you been able to use it just right

[07:53] out of the box? The thing that the agent

[07:55] constructs

[07:59] anyone have any spectacular failure

[08:01] cases or spectacular successes? So just

[08:06] repeating that for the recording like

[08:07] sometimes the models will write too much

[08:09] in the skill like they'll kind of

[08:11] overinfer the what should be done and

[08:15] then when that's handed off to another

[08:16] model it will kind of follow it to the

[08:18] letter and do a lot more than you

[08:20] actually wanted it to.

[08:22] >> Any other examples from folks?

[08:28] >> Cool. Oh yeah, go ahead. I mean in cases

[08:31] when you're like trying to like a

[08:33] production issue for like a particular

[08:34] system if you give it like three or four

[08:37] support

[08:39] and you tell it that look at how people

[08:41] have this issue in the past create a

[08:43] skill for yourself

[08:46] other agents could use to it in the same

[08:48] way

[08:49] >> and that's

[08:50] very

[08:51] >> oh nice

[08:52] >> okay cool yeah so instructing it to like

[08:55] get write the instructions for another

[08:57] agent it's good enough it's sort of like

[08:58] simulating what the agent would do.

[09:00] Yeah, that's interesting. I've sometimes

[09:02] found that the models are like pretty

[09:04] bad at kind of like simulating the

[09:06] theory of mind that you know another

[09:08] person or an agent would have when they

[09:10] like look at instructions, but they get

[09:11] a lot better when you prompt them to do

[09:13] that. Cool.

[09:16] Okay.

[09:19] Yeah. So, a few different like types of

[09:21] experience that we might want to retain

[09:24] for agents. So the first is like the

[09:27] episode and this is you know just the

[09:29] sequence of observations that you get

[09:31] from the environment from the user and

[09:33] the actions that are taken and this is

[09:36] sort of like the maximum fidelity right

[09:38] you're just you're retaining everything

[09:40] you have all the specifics of that

[09:42] particular environment and the

[09:44] particular instructions that the user

[09:46] gave also going to be like the most

[09:49] costly right it'll need the most tokens

[09:51] to represent and you probably don't need

[09:54] all of that right? Like uh just like

[09:56] when we're doing you know supervised

[09:58] learning we don't want to retain every

[09:59] detail we want to abstract to the things

[10:02] that matter to generalize um in the

[10:04] future.

[10:06] So we could also retain some facts like

[10:10] um some knowledge about the environment

[10:13] um or about the user and in the early

[10:16] work on memory systems uh a lot of it

[10:19] was focused on retaining facts. So like

[10:21] a user is interacting with an assistant

[10:24] and maybe gives some personal

[10:26] information like how old they are or

[10:28] where they live. The system can retain

[10:31] that in its memory and then use that

[10:33] fact to improve future interactions. If

[10:36] you've um used uh like Anthropic or

[10:39] Chatbt's uh memory systems, uh they're

[10:42] doing this basically, right? Like you

[10:44] can go into the settings, you can view

[10:46] the memory that they have about you and

[10:48] there's, you know, a text representation

[10:50] there from a model that's produced those

[10:53] facts um from your past interactions.

[10:55] Looks a little bit like compaction in

[10:57] some way. It's generated by an LLM. It

[10:59] gets stored in this external thing.

[11:02] And then the final one is more specific

[11:04] to agents. So it's about like how do you

[11:07] do part of a task um in a way that's

[11:11] abstracted from the details of the task.

[11:14] So like in the example we looked at

[11:15] before, how do you search for products

[11:17] on a particular website without maybe

[11:20] retaining the details of searching, you

[11:22] know, the particular product that you

[11:24] searched for? And so there's a lot of

[11:26] choices about how you would represent a

[11:28] skill. Is it just text? Is it kind of

[11:30] the actual actions that you took? Um or

[11:32] could it even be code?

[11:35] And of course, skills are only going to

[11:37] be useful if you're going to be doing

[11:39] the same subtask more than once.

[11:44] So we could think about like um memory

[11:47] and skills and the intersection between

[11:49] them. So memory is just something that

[11:52] we're saving from the agents

[11:53] interaction. So for example, what's a

[11:55] previous product that you purchased on a

[11:57] site? A skill would be reusable

[12:00] knowledge about how to act in an

[12:02] environment. um which could be

[12:04] represented in one of a variety of ways.

[12:06] Like it could be, you know, if you're

[12:08] releasing a um application um by pushing

[12:12] it to production, here's a checklist

[12:15] that you need to go through before you

[12:17] do that. So, a skill could be written by

[12:19] a person like in this example. But we

[12:22] could also have um a combination of

[12:24] memory and skills. So we could induce

[12:27] skills from the agents past experiences

[12:29] and store those um and then use those to

[12:32] hopefully do better in the future. So if

[12:34] the agent searched successfully for a

[12:36] product in the past um and uh yeah and

[12:39] if it was successful, if we think that

[12:41] it was successful, then we could pull

[12:43] out something that looks like a skill to

[12:45] guide the agent in the future. And we'll

[12:47] get a lot more concrete about what this

[12:49] looks like through the rest of the

[12:50] lecture.

[12:54] So we can think about skills as

[12:56] instructions where uh skills as

[12:58] instructions might be written by a

[13:00] person um for encoding their own you

[13:02] know preferences or might be

[13:05] organization policies like this is the

[13:07] way that we write and test code in this

[13:10] particular company. Um and human

[13:14] authored skills um we know where they

[13:16] came from. we have more maybe control

[13:18] over the quality but it takes you know a

[13:21] lot of time to write them and to

[13:22] maintain them. If we're learning skills

[13:25] then the agent is producing them. Um and

[13:28] this is helpful because we can do this

[13:30] in an automated way. Maybe we can have

[13:32] like a loop where we induce the skill.

[13:34] We try to use the skill to redo the same

[13:36] tasks. We see if things get better on a

[13:38] metric. Um, but it can be, you know,

[13:41] potentially noisy too and have, you

[13:42] know, especially if you're using the

[13:44] skills for some other agent like we

[13:46] talked about in those examples everybody

[13:48] gave, um, it could maybe have unintended

[13:50] consequences too.

[13:54] Okay, so let's talk first about uh,

[13:57] humanridden skills and um, the standards

[13:59] for these and the ways that they're used

[14:02] in incurrent agents. So probably a lot

[14:05] of it sounds like a lot of you have

[14:07] experience with this already. Uh so

[14:11] maybe you've been using these in the

[14:13] context of an example kind of like this.

[14:15] Uh there's this nice blog post from open

[14:18] hands that has guidance on using skills.

[14:20] Um for those of you who um who haven't

[14:23] used skills yet or if you you know like

[14:25] some suggestions on how to uh how to

[14:28] have best practices for creating and

[14:30] using skills. But they have this

[14:33] motivating motivating example of say

[14:35] that you find yourself like always

[14:37] giving similar instructions to a coding

[14:39] agent. Um so you um want the you want to

[14:44] check the code that has been written

[14:46] using one of a couple different

[14:47] llinters. You want to give type hints.

[14:49] You want to use a particular type of

[14:51] dock strings. And you want to apply

[14:53] piest to all the functions. So if you're

[14:56] always doing this, you could always type

[14:58] this guidance into the system. Um, but

[15:01] you know, a kind of natural and faster

[15:04] way to do this would be to just have the

[15:07] like store the guidance as a text file

[15:10] and then have the agent use that

[15:12] guidance um as an instruction. So you

[15:16] should reach for a skill when you want

[15:17] to do something repeatedly following

[15:19] kind of like a fixed specification. And

[15:21] the agent's going to choose how to

[15:23] interpret this specification in context,

[15:25] but the um general instruction is the

[15:28] same.

[15:31] And the way that this is implemented in

[15:33] the current standard for skills um which

[15:36] is called agent skills is just as a

[15:39] collection of files which the agent is

[15:41] able to read.

[15:45] And here's an example of of that. So if

[15:47] we are constructing a skill for Python

[15:50] review um we'll have a folder which has

[15:54] a structure like this. So skills have

[15:56] this standard structure where they'll

[15:58] have a skill.md file and you have to

[16:00] have that. Skill.md um is a markdown

[16:04] file that starts with um some YAML

[16:06] metadata. So you need to have a name for

[16:09] the skill and you need to have a short

[16:11] description uh which is going to give

[16:14] guidance to the language model about

[16:16] when the skill should be applied. And

[16:18] we'll see in a slide or two about how

[16:20] the model gets access to this

[16:22] information in the YAML header. And then

[16:26] um after the header you'll have a much

[16:28] more detailed description of um how the

[16:30] skill should be applied which would for

[16:32] example you know list um here are all

[16:34] the llinters that you should apply

[16:35] here's how testing should be done and so

[16:38] on. So you have to have skill.mmd. You

[16:41] also have a few other um folders which

[16:44] are optional but can contain some extra

[16:46] resources for the agent to use as it

[16:49] carries out the skill. So there's

[16:51] scripts which has executable code. So

[16:54] for example, if you had like a Python

[16:57] script that would run a llinter, you

[16:58] could put it in there and then describe

[17:00] it in this skill.md file. There's also

[17:03] references, which would be sort of like

[17:05] supplementary documentation that maybe

[17:07] you don't you you don't need to use it

[17:09] every time you use the skill. Um, but

[17:12] you'll have maybe a reference to that

[17:15] documentation in the skill file. The

[17:16] agent could load it as needed from the

[17:18] references folder. And then assets

[17:21] basically just has like, you know,

[17:22] additional templates or resources like

[17:24] if you're, you know, doing something

[17:25] that involves like Ginga and you need

[17:28] the agent to load that conditionally.

[17:32] So this can be a lot of information,

[17:34] right? And we um don't want to fill up

[17:37] the context window of the model um with

[17:40] all of the possible skills that it could

[17:42] use. So there's a mechanism called

[17:44] progressive disclosure which is going to

[17:46] just show relevant parts of skills to

[17:50] the agent as they're needed. So the

[17:52] first level is um the metadata in this

[17:56] YAML file. Uh so the name and the

[17:58] description and that's always going to

[18:01] be um shown to the model in the system

[18:04] prompt if the skill is loaded if it's

[18:08] available to the model to use. So you

[18:10] need to be kind of concise in this uh

[18:13] description. Um so that if you have a

[18:15] lot of skills you don't fill things up

[18:16] too much.

[18:19] There's the second level which is the

[18:21] rest of the text in the markdown file

[18:23] and um that'll be loaded conditionally

[18:26] if the model decides that the skill is

[18:29] relevant um and uh decides to read the

[18:32] rest of the file via a tool call. We'll

[18:35] see an example of that in a minute. And

[18:37] then the next level is sort of like all

[18:38] the resources in here which will also be

[18:41] loaded um using tool calls. So you kind

[18:45] of need to have enough information in

[18:46] the skill.md file for the model to be

[18:49] aware that it should look into these

[18:51] additional folders to get more resources

[18:54] um when it's carrying out the skill. Any

[18:56] questions about this and you'll

[18:59] implement this in assignment one or

[19:01] maybe some of you are already starting

[19:03] on implementing that.

[19:05] >> Yeah.

[19:11] are so high

[19:16] like what if that takes too much of that

[19:20] effect performance?

[19:22] >> Yeah. So if you have a lot of skills

[19:24] even if the skill metadata is pretty

[19:27] short could it affect performance? Yeah,

[19:28] it definitely can. Um so you want to

[19:31] keep the number of skills somewhat small

[19:33] and maybe just load them conditionally.

[19:36] um in one of the state-of-the-art

[19:39] agents, Hermes agent, I think the I'm

[19:41] not sure the number of skills, but like

[19:43] the total length of the skill

[19:44] descriptions in the system prompt is

[19:46] like 3,000 tokens. Um there's some

[19:49] papers that we'll see in a little bit

[19:50] that show that if you have too many

[19:52] skills, um it can make performance

[19:54] worse. Like adding in irrelevant skills

[19:56] can drop performance um because, you

[19:58] know, the context gets longer. The model

[20:00] might be distracted by things that are

[20:02] actually irrelevant. So yeah, you

[20:04] definitely need to be careful about the

[20:06] number of skills, but um I think it

[20:08] would be pretty rare to have like 10,000

[20:10] or a thousand skills. Generally, it's,

[20:12] you know, smaller and you would maybe

[20:14] load skills as needed for like the

[20:16] software tasks that you're carrying out.

[20:19] >> Yeah.

[20:20] >> How sensitive are those triggers?

[20:24] >> Yeah, that's a great question. How

[20:26] sensitive are the triggers? So the the

[20:28] triggers will be tool calls that will be

[20:31] generated by the model. And so whether

[20:34] they get called or not is a function is

[20:37] totally dependent on the model. Um and

[20:39] you know the model's ability to predict

[20:43] that it should be triggered based on the

[20:44] past context and what it knows about the

[20:48] skill. So that you know depends on the

[20:50] model depends on the description you

[20:51] write and um that's why we need

[20:53] evaluations for this. Um and one of the

[20:56] papers that we'll look at takes a step

[20:58] in that direction.

[20:59] >> Yeah.

[21:02] like a standardized name.

[21:08] >> Yeah. Uh skill.md is a standardized

[21:11] name. So the the standard is called the

[21:13] um I think the agent skills standard and

[21:16] um you like models agents are trained to

[21:19] to use that agent frameworks are trained

[21:21] to load that. Um so yeah you um if you

[21:25] want to use an alternate format well

[21:27] first put it you know as close to this

[21:29] as you can but you could do you know if

[21:32] you have particular if you have

[21:34] particular um things that you want like

[21:36] in the references folder you could

[21:38] describe them in skill.md and like all

[21:41] this is just going to be instructions to

[21:42] the language model so it could be robust

[21:44] to other configurations also especially

[21:47] if you describe them.

[21:50] >> Yeah. Why are

[21:59] >> Yeah, why markdown? It it is a balance

[22:02] of machine and human readability, I

[22:04] think.

[22:11] >> Yeah, that's a great question. Could

[22:12] there be better formats than than

[22:14] skill.md?

[22:16] Yeah. Do you have things in mind?

[22:19] I think like um so uh I mean it's just

[22:24] like linear right um it's you can have

[22:26] hyperlinks which is good you can embed

[22:28] images too um

[22:32] >> yeah um but uh like it's difficult to

[22:36] you know represent things that are

[22:38] dynamic so like maybe you want to

[22:40] illustrate to the model like um

[22:42] different ways the data could be

[22:44] visualized um you know maybe that would

[22:46] be better with like a JavaScript

[22:47] interactive JavaScript application or

[22:49] something like that. Um, yeah, you

[22:52] could, you know, have that be sort of

[22:54] like a code file here that gets

[22:55] executed. Um, but and maybe like

[22:58] referenced in the markdown. Um, so I

[23:00] think like markdown is sort of the best

[23:02] attempt at having something that's

[23:04] general and like readable, but then you

[23:06] would rely on the language model to

[23:08] interpret other formats.

[23:10] >> I think in the scientific literature

[23:12] that uh Daniel's going to talk about,

[23:14] there's basically two ways. There's

[23:16] textual skills and programmatic skills

[23:18] and the textual skills appear in the

[23:20] markdown and the programmatic skills

[23:22] appear in the script. So it kind of it's

[23:24] pretty broad if you consider those.

[23:27] >> Yeah. Cool.

[23:30] >> Yeah.

[23:30] >> Does anyone do

[23:32] to not have to put it all in context?

[23:35] For example, if you're making an agent

[23:36] that modifies cloud infrastructure, you

[23:39] work at some big bank and have a billion

[23:42] things in AWS and it would be nice to be

[23:45] able to just ask the model to modify

[23:47] something, but then because it's a

[23:48] billion things, you can just have a

[23:50] billion tools for every small component

[23:52] available. Yes.

[23:54] >> So looks like something

[23:56] would

[23:59] do. Yeah, definitely in some of the

[24:01] research papers that so the question was

[24:03] like do people retrieve from large

[24:05] collections of skills. Um and yeah

[24:08] definitely in some of the research

[24:09] papers that we'll look at um they do

[24:12] that um either using you know just like

[24:13] a text embedding based retrieval or

[24:17] doing something that's more kind of like

[24:18] domain conditional like we know these

[24:20] skills apply to this site so when we're

[24:23] interacting with that site we'll load

[24:25] those skills. Yeah, I imagine production

[24:28] systems do this too, but um yeah, I

[24:30] don't have any references off the top of

[24:32] my head for that. Cool. Okay, so we'll

[24:36] uh just uh kind of quickly to show you

[24:38] how progressive disclosure works. Um we

[24:41] first need to give the model access to

[24:44] this level one, right? Let it know what

[24:46] skills are available. And you'll have a

[24:49] system prompt that looks something like

[24:51] this. This is just taken from Hermes

[24:53] agent which is sort of like a standard

[24:55] open- source um agent that is able to

[24:58] use and induce skills and you'll um kind

[25:02] of describe what skills are. Uh you'll

[25:04] tell the model about this skill view

[25:06] tool which it could use to read the rest

[25:09] of the markdown file and then you'll

[25:12] list out all the skills that you have.

[25:14] So there's just two skills here. Um,

[25:16] there's a code quality skill and a

[25:18] workflow skill. And that's just the YAML

[25:20] metadata from those skill files.

[25:25] So, um, the model is able to use tool

[25:28] calls to, you know, expand the rest of

[25:30] the skill. And here's what that might

[25:32] look like. So, it always has the index

[25:35] of skills in the system prompt, but it

[25:38] could choose to make a tool call to open

[25:41] the Python review skill. um if that

[25:43] seems relevant to you know the user

[25:45] asked for a review of some Python code

[25:48] and then it's going to like um you know

[25:51] get that markdown file insert it as a

[25:55] message to the system as an observation

[25:57] the result of that skill view tool. Um

[26:01] the system might choose to run something

[26:02] from the scripts directory um and then

[26:05] it'll get the result of running that

[26:06] script as an observation put it in the

[26:08] window um and might choose to you know

[26:11] like view additional files within that

[26:13] skill package.

[26:18] Okay. So yeah, we these questions that

[26:21] we had about like you know could

[26:23] additional skills hurt um are skills

[26:26] being triggered in the right place. Uh

[26:28] we answer questions like this by

[26:30] building evaluations and um the the work

[26:33] on this is a little bit um new. It's

[26:35] sort of ongoing but um a really great

[26:38] first effort in the space is called

[26:40] skills bench and what they do is they um

[26:43] collect a bunch of skills uh from uh

[26:46] various sources online. they actually

[26:48] get like 2 million skills. Um, and

[26:51] they'll also have people write tasks

[26:53] which seem like they could benefit from

[26:56] skills. Uh, and so they'll like get 400

[26:59] tasks and um those are going to be

[27:02] written independently from the skills,

[27:04] but they'll have the task annotators

[27:06] choose from this pool of skills ones

[27:08] that seem like they could apply to the

[27:11] tasks. And so you'll have kind of like a

[27:13] small set of curated skills. um and

[27:16] you'll supply those skills to an agent

[27:19] as it's trying to solve the task and

[27:21] they'll evaluate this on like um you

[27:23] know four different agent frameworks uh

[27:26] with I think like 18 models something

[27:28] like that and they'll just see like does

[27:31] having the skills um improve performance

[27:34] over not having the skills across all

[27:36] the tasks for a given agent framework

[27:39] and model combination right so this will

[27:42] evaluate you know it'll implicitly

[27:44] evaluate the skill quality but will be

[27:47] designed to evaluate is a model and

[27:50] framework able to you know use the

[27:52] skills appropriately and they're trying

[27:54] to choose the skills. So they have like

[27:56] a filter um which checks to see that for

[27:59] a small subset of models the performance

[28:01] on the tasks does improve when you give

[28:05] models access to the skills and then

[28:07] you're seeing if that's also true for

[28:08] kind of a wider set of frameworks and

[28:11] models.

[28:15] Yeah.

[28:16] Does the general setup make sense? Cool.

[28:21] So on average, you know, with this cur

[28:24] curated set of um skills, uh the average

[28:27] pass rates on these tasks using like

[28:29] humanridden verification criteria does

[28:32] increase. And so you can see like the

[28:33] solid bars to the shaded bars across a

[28:37] bunch of different models um and

[28:39] frameworks. Um but actually uh ski like

[28:44] tasks that require fewer skills to solve

[28:48] benefit more from having the skills

[28:50] available than ones that require more

[28:53] skills. Um and so this is partly a

[28:56] difficulty thing but also partly that

[28:57] the models might be getting distracted

[28:59] by having more skills available. And you

[29:02] could imagine that it's getting much

[29:03] worse with like a much larger number of

[29:06] skills. Um we'll see some more evidence

[29:08] for that later on in the lecture.

[29:12] And actually skills still hurt on a

[29:15] number of the tasks for particular model

[29:17] types. Um so the model might be using

[29:20] the skill inappropriately which could

[29:22] actually make it do the task in a way

[29:24] different than what the person

[29:25] specified. So this kind of motivates the

[29:27] importance of like checking to see if

[29:29] the skills that you wrote are actually

[29:31] making your outputs better.

[29:36] So skills can come from, you know, a

[29:38] bunch of different sources. They could

[29:40] be bundled with the harness. Um, they

[29:42] could be written by a person. Um, and a

[29:45] lot of you have done this, it sounds

[29:46] like, and you then, you know, kind of

[29:48] install it in a in a way that's

[29:50] specified by the framework that you're

[29:52] using, but they can also be created by

[29:55] the agent. And, um, Hermes has a skill

[29:58] manage tool. um open hands as a skill

[30:00] creator uh command that help work you

[30:03] through the process of creating a skill.

[30:06] And when you're creating a skill, I

[30:08] think it's really important to base that

[30:09] skill on some prior interactions that

[30:13] you've had rather than trying to just do

[30:15] it sort of a priori. Um and actually

[30:19] there's some results in the skills bench

[30:21] paper that show that models when they're

[30:23] tasked to create a skill by themselves

[30:25] just based on a task description,

[30:27] they're really bad at it. and it

[30:29] actually makes performance worse. So, as

[30:31] a person, you're probably better because

[30:32] you kind of like know the way that you

[30:34] want it to be done, but it's generally

[30:36] best to base it on, you know, past

[30:38] things that you've done because when

[30:40] you're doing a task, it'll reveal some

[30:41] things about the way you want it to be

[30:43] done that you might not know in advance.

[30:47] So there's a nice case study of this um

[30:49] from the open hands blog post on how do

[30:52] you like so you have this code review

[30:54] skill that you've created. How do you

[30:56] check and see if it's working and then

[30:58] improve it if necessary.

[31:01] So this is focused on like reviewing

[31:04] poll requests and what what you could do

[31:07] is like um after the review is produced

[31:09] by the agent then a person is going to

[31:12] go through the poll request and look at

[31:14] each of those review comments and either

[31:16] address them or not. And you can apply a

[31:19] modelbased judge after that and count up

[31:21] how many of these were like actually

[31:24] used by the person which will give you a

[31:26] sense of how good the pull request was.

[31:30] And you can like um do this over a large

[31:33] number of pull requests that were

[31:35] created and then reviewed by the agent

[31:37] using this skill. And um if you do this

[31:40] over um you know like hundreds or

[31:43] thousands of examples, you'll get a lot

[31:46] of evidence about what's working and

[31:47] what's not, you can summarize all of

[31:49] that with a reasoning model um and use

[31:52] that to like for example identify that

[31:55] it's not helpful to um you know produce

[31:58] code that ignores the repo conventions.

[32:00] people did like incorporate those

[32:02] changes quite a bit. And then you could

[32:04] like have the model propose some updates

[32:06] to the skill file that will make the you

[32:11] know reviews produced by the system more

[32:14] likely to be incorporated by the person.

[32:20] Cool. Any questions before we move on?

[32:25] Okay.

[32:26] So next we'll talk about how do we get

[32:28] models to automatically remember things

[32:31] from their past experience and then

[32:32] we'll use that to like build on um to

[32:36] talk about inducing skills from

[32:37] experience.

[32:40] So this is this is an old paper. This is

[32:43] from 2023 um but it was pretty

[32:46] influential. Um and it's uh it's one of

[32:50] the first papers it's called MEMGPT.

[32:53] It's one of the first papers to uh

[32:56] [snorts]

[32:56] introduce a way that you can manage

[32:59] memory outside of the context window of

[33:01] a language model. So this is like a

[33:03] really a systems inspired paper. I think

[33:05] we talked about a couple lectures ago

[33:07] about you know kind of having like

[33:08] memory hierarchies like you know

[33:10] something that is fast to access which

[33:13] for the language model is the context

[33:15] window and then something that's like

[33:17] larger but but slower and in this

[33:20] setting that would be like an external

[33:22] store of of facts and back when this

[33:25] paper was written uh a few years ago

[33:27] context windows were even shorter like

[33:29] you know 8,000 tokens um so this sort of

[33:33] approach was really well motivated even

[33:35] for just interacting with like an

[33:37] assistant system. Um nowadays you know

[33:40] our context windows are larger but what

[33:41] you want to store in them is also much

[33:43] larger. So this sort of approach is

[33:45] pretty well motivated for agents too.

[33:48] But the basic idea here is that you're

[33:50] going to have like a um you'll have you

[33:54] know the system instructions which don't

[33:56] get updated. you'll have a working

[33:58] context um which is going to uh pull

[34:02] things from an external memory um and

[34:05] also you'll be storing things to this

[34:07] external memory and those reads and

[34:10] writes are going to be controlled by

[34:12] tool calls from the model

[34:15] and um you'll also you know have like a

[34:18] separate storage for the actual messages

[34:20] that the system received um but that's

[34:22] going to be controlled in a pretty

[34:23] similar way to this uh this memory over

[34:25] fax

[34:26] So, what this actually looks like, sorry

[34:28] it's a little bit hard to read with the

[34:29] brightness in here, but like if you um

[34:33] you might uh have an interaction with

[34:35] the model where the user like mentions

[34:37] six flags and um the system could

[34:40] produce a tool call that searches within

[34:43] this storage for past mentions of six

[34:46] flags from its past interactions. It'll

[34:48] take those and it'll put them into this

[34:50] like working context. Um and then the

[34:53] model um this working context is stored

[34:55] within the context window of the

[34:57] language model. So the model will be

[34:58] able to use those as it outputs its

[35:02] response.

[35:06] But it's important to be able to do more

[35:09] than just like add to memory because for

[35:12] example like um maybe you're talking to

[35:14] the system about your job. you say I

[35:17] work at X, but then if you change jobs

[35:20] later on, you want the system to be able

[35:22] to like use the latest information.

[35:26] And um this paper called me zero uh

[35:29] introduces a way for memories to be

[35:32] updated as well. Um so the way that this

[35:35] works is you'll have like messages

[35:37] coming in and um each time you get a

[35:40] message, you'll apply a language model

[35:42] to extract some memories from it. um

[35:45] some like potential facts that you might

[35:47] want to store or update and you'll have

[35:49] an external uh database store um and

[35:54] you'll try to check and see do I have

[35:56] anything in that database store that's

[35:57] relevant to these um facts that I pulled

[36:01] out of these messages. So you'll

[36:03] retrieve the top K and to do this you'll

[36:06] use like an embedding based retriever

[36:08] model like you know the ones we talked

[36:09] about a little bit ago. um you'll pull

[36:11] out similar facts like um six flags for

[36:15] example or like um I work at X and

[36:18] you'll apply a language model to check

[36:21] for all of these extracted memories from

[36:23] these latest messages um do they um are

[36:28] they present in these similar retrieved

[36:29] memories? If they're not present then we

[36:33] should potentially add them in. um if

[36:36] they are an update to something that's

[36:39] there, we should replace what's stored

[36:42] for that with the new thing. If it

[36:44] negates something that's already there,

[36:46] like for example, you say, "I work at

[36:48] X," but then later on you say, "I got

[36:50] laid off," you might want to just delete

[36:52] that fact rather than um than updating

[36:54] it. Um or if it's not relevant at all,

[36:58] you would just ignore it.

[37:01] And um I'll refer you to details or for

[37:03] the paper for for details about this um

[37:06] because the details also change with

[37:08] with agentive systems but I think the

[37:10] idea that um it's useful to be able to

[37:13] like update knowledge as well if you

[37:15] have conflicts is potentially pretty

[37:17] useful.

[37:18] So, um, does anybody remember something

[37:21] from the lecture on context management

[37:24] that had a similar goal to this being

[37:27] able to update or delete memory?

[37:31] Yeah.

[37:33] Uh, hashing.

[37:36] >> Yeah. Yeah. Basically, does anybody

[37:38] remember the specific paper?

[37:44] Yeah. Yeah, it's hashing in the sense

[37:45] that there we had like key values and

[37:48] queries, right? Um and we were like

[37:50] storing values which were vectors. Um

[37:52] here we're storing like text um as

[37:55] facts.

[37:58] Yeah.

[38:00] So the Delta paper actually did this,

[38:03] right? like um linear attention is only

[38:06] able to append um values to your um

[38:11] what's effectively your memory but Delta

[38:14] um uh like effectively retrieves um

[38:18] things that are stored for particular

[38:20] queries and then changes them changes

[38:22] the vectors that are stored for for them

[38:24] and that helps improve performance. So

[38:26] this is sort of like a textbased analog

[38:29] of that that has a similar goal.

[38:32] Yeah, you could also think about like um

[38:35] for the third type of learning for

[38:37] updating the weights of a model, it's

[38:39] potentially helpful there to be able to

[38:41] forget stuff also. Um especially if you

[38:44] have kind of like conflicting knowledge

[38:45] and and people are starting to develop

[38:47] some approaches for that like unlearning

[38:49] um is one way to do it.

[38:54] Okay, so those are some foundational

[38:56] papers about memory um that were

[38:59] developed for assistance

[39:01] for agents. Um feedback on trajectories

[39:05] can be really useful. So this paper

[39:09] called reflection was um a really

[39:11] impactful it's a really uh it's a really

[39:15] pretty simple but effective um the way

[39:18] to get agents to use feedback and

[39:20] potentially do better. So, it's

[39:22] definitely worth knowing about. It's a

[39:24] good thing to implement if you're

[39:25] working on a project that might want an

[39:27] agent to be able to benefit from its

[39:29] past experiences. Um, and the way it

[39:32] works is we're trying to improve the

[39:34] performance of an agent given multiple

[39:37] attempts on a particular task. So, say

[39:40] that you're asking the agent to like um,

[39:42] you know, search for a product on a

[39:44] website. It makes one attempt at it. um

[39:47] it says that it's finished and you're

[39:50] able to get some feedback about whether

[39:52] it was likely correct or not. So that

[39:54] could come from like a person looking at

[39:56] it. It could come from applying a model

[39:58] as a judge. Um but given that feedback,

[40:02] you'll want the model to try again and

[40:04] try to do better.

[40:06] And what this paper does is show that

[40:09] natural language feedback um on the

[40:11] attempt can be a really helpful thing

[40:14] for the model to condition on in its

[40:16] second attempt. So like if it's trying

[40:18] to answer this question about what was a

[40:20] particular series of battles, it might

[40:22] just mention one particular battle and

[40:24] then the feedback that's given um

[40:27] generated by a language model based on

[40:28] knowing this is incorrect and looking at

[40:31] the question and the answer might be um

[40:34] you gave just a single battle rather

[40:36] than a series. So as you can imagine

[40:38] this would be really helpful feedback

[40:40] for the model to condition on as it you

[40:42] know does another attempt at this task

[40:44] and it can get it correct. Um and the

[40:47] paper shows that you know conditioning

[40:48] on this natural language description of

[40:50] what went wrong can be really helpful.

[40:53] So we can generalize this also to um the

[40:56] agent improving as it does different

[40:59] tasks. Right? This is improving on the

[41:00] same task. But you could imagine um

[41:04] feedback might be generally helpful to

[41:07] improve performance on similar tasks as

[41:09] long as the feedback's like sufficiently

[41:11] general.

[41:15] And the final way that we can like um

[41:17] have agents uh improve or you know kind

[41:20] of the final foundational thing for

[41:22] helping agents improve um is remembering

[41:25] trajectories uh like entire

[41:27] trajectories, entire episodes that

[41:29] they've done in the past and using that

[41:31] to shape what they do on future tasks.

[41:34] There is a bunch of papers that have

[41:35] done this. We have some links to them at

[41:37] the bottom of this slide. Um, but the

[41:39] key thing in all of them is you'll have

[41:41] some collection of like training tasks

[41:44] and those tasks could be like a

[41:45] collection of demonstrations or they

[41:47] could be produced by the agent as it's

[41:49] carrying out tasks one at a time. Um,

[41:52] and you'll pull all of those tasks

[41:54] together. Maybe you'll additionally like

[41:57] um generate some text that describes uh

[42:00] feedback from them sort of like

[42:01] reflection did on the last slide. And

[42:03] you'll have that pool of experiences.

[42:06] And then when you get a new task um that

[42:09] comes in, you'll retrieve from this uh

[42:12] set of trajectories and um maybe

[42:15] generated text about them to find

[42:17] something that's relevant for the task

[42:18] that you're carrying out. You'll put it

[42:20] in the context window of your model and

[42:22] it'll generally help you to do better.

[42:24] Um so this is sort of like rag for

[42:26] agents, right? Um and uh it's pretty

[42:29] effective.

[42:31] Any questions about this?

[42:37] Yeah.

[42:38] >> What do you mean by trajectory in this

[42:40] case is like sequence of calls.

[42:42] >> Yeah. Yeah. So a trajectory generally

[42:44] for an agent is the sequence of um like

[42:48] messages that it gets from the

[42:49] environment or the user. So the

[42:50] observations um the actions that it

[42:53] takes like the tool calls and um and uh

[42:58] potentially also you know the chains of

[42:59] thought that it produces. So one way to

[43:01] think about it is basically just like

[43:03] all the sequence of um of uh messages um

[43:07] in the context window of the model

[43:10] >> and you retrieve it by image

[43:13] differently. You can do this regular

[43:14] embedding retrieval or compare to

[43:18] process sequences and do some set

[43:20] comparison.

[43:22] >> Yeah. What are the different ways that

[43:24] you could do retrieval? So typically you

[43:26] want the model to you're giving the

[43:28] model the description of a new task that

[43:30] it should carry out. So you have just

[43:33] that text description and you'll embed

[43:35] that um with an embedding model and

[43:38] you'll retrieve um based on the

[43:40] descriptions of other tasks that each

[43:43] have like a trajectory associated with

[43:44] them and maybe you'll also constrain

[43:47] that to be like we'll just retrieve the

[43:49] tasks for this particular domain that

[43:51] we're working in. Um yeah, good

[43:54] question. Any other questions about this

[43:57] approach? Generally, this is sort of

[43:59] like a whole class of approaches. Um

[44:01] there's different ways to instantiate

[44:03] it. Um the details like how do you build

[44:05] up the experiences? How do you do the

[44:07] retrieval? Um but just want to kind of

[44:10] give you a sense that if we have past

[44:13] successful trajectories and we show

[44:16] those as examples to the agent, it can

[44:18] help it to do better.

[44:22] Okay. So with that we kind of have the

[44:24] foundation for talking about um actually

[44:26] inducing skills. Um so

[44:30] we can think about skills as being like

[44:32] parts of a task that are reusable across

[44:36] different tasks. So at the very

[44:38] beginning we talked about like searching

[44:40] for a product and that might look

[44:44] something like we tell the agent show me

[44:47] results for this particular query and

[44:50] the agent might produce a chain of

[44:52] thought like this and then it might

[44:54] produce these particular actions that

[44:57] actually interact with the web page like

[44:59] um uh clicking on this element

[45:02] identified by this particular ID which

[45:04] is the search box typing a query in

[45:06] there and and clicking on another

[45:08] element which is like the actual button

[45:11] to search.

[45:13] And this uh chunk of a task might be

[45:17] reused on future tasks. Like if I say

[45:19] what is the price range for um this

[45:22] particular item, it might need to do

[45:25] these same exact steps again as well as

[45:27] some additional ones afterwards.

[45:31] And so we can think of a skill as being

[45:33] um a specific like reused part of the

[45:36] task.

[45:38] Is this a good way to represent a skill?

[45:43] Can anybody think of any issues with

[45:44] this?

[45:49] >> Yeah.

[45:56] just

[45:57] >> Yeah,

[46:00] that's right. Yeah. So, like if the

[46:02] element ids on the page change, the

[46:04] skill will break. And you know, there's

[46:06] a number of ways that that could happen.

[46:07] Like, you know, maybe the elements are

[46:09] maybe it's the same page, but things are

[46:11] just numbered differently. You can make

[46:13] some changes to the action space to deal

[46:14] with that. I think JY will talk about

[46:16] that in his lecture. But like if we go

[46:19] to a different website that has like a

[46:21] different search interface um it's going

[46:24] to break and we'll see some examples of

[46:26] that later on.

[46:31] Yeah. So we'll generally compare as

[46:33] Graham said text versus code as ways to

[46:35] represent skills.

[46:37] I want to briefly highlight some uh

[46:40] really cool papers um from the past that

[46:42] I think kind of like lay a foundation

[46:44] for skill induction um for learning

[46:47] skills from experience. Uh, one is

[46:50] called um Voyager and um they're

[46:53] controlling an agent in Minecraft. Um,

[46:55] and they're using uh code as a way to

[46:58] control the agent where the code

[47:01] functions um implement things like um

[47:04] crafting a particular item or combating

[47:07] a zombie. And representing these like

[47:10] subtasks as functions allows functions

[47:13] to call each other. So that as the agent

[47:16] like learns functions for simple things,

[47:18] it can then like compose them calling

[47:21] them in other functions and you can

[47:22] carry out increasingly complex tasks.

[47:26] There's also a line of work um from the

[47:28] program induction community um that that

[47:31] does this. I think a really nice

[47:32] representative of this is um uh work

[47:35] called dreamcoder and a few papers that

[47:38] built on it. And there you're um sort of

[47:41] uh you have basically like grammarss

[47:43] over things that you're constructing um

[47:45] like objects um and you uh like have uh

[47:50] some examples of complete objects which

[47:53] are constructed using like very

[47:54] low-level functions and you search for

[47:56] recurrent patterns in that you find

[47:58] patterns that can be abstracted into

[48:00] functions and you do that repeatedly and

[48:02] you're sort of like compressing the

[48:04] programs that construct these objects.

[48:07] And then there's also some follow-ups to

[48:09] this that uh integrate like large

[48:11] language models, Python code, and uh

[48:15] natural language descriptions too.

[48:19] And some of the same ideas in those

[48:22] papers are also useful for agents that

[48:24] are um using language models to interact

[48:27] with the world. A typical way that we'll

[48:30] evaluate systems for inducing and using

[48:33] skills is an online learning setting. So

[48:36] when you're interacting with um an

[48:38] agent, you are maybe having it carry out

[48:40] a bunch of tasks in succession and some

[48:43] of those tasks are going to be similar

[48:44] to each other. You want the system to be

[48:47] able to learn from your interactions

[48:49] with it and then be able to do better in

[48:51] the future, right? So um this is an

[48:54] online learning setting where we'll have

[48:56] tasks come in one at a time. So for

[48:58] example, like you might say, add a Sony

[49:00] Bluetooth headphone to my wish list. And

[49:03] we'll be building up a memory of skills

[49:06] um incrementally as we solve those

[49:08] tasks. So um there will be an induction

[49:11] step that we'll talk about in a slide or

[49:13] two. And that induction step will

[49:17] create a skill like search for a product

[49:20] and add a product to the wish list that

[49:22] are useful for solving this particular

[49:24] task.

[49:26] And um you know maybe we have another

[49:28] one like this task here and we can apply

[49:32] those skills on future tasks like this

[49:34] task might also involve searching for a

[49:37] product and hopefully we'll do better on

[49:39] that task given that we had this skill

[49:43] induced from the previous task

[49:46] and so on. So what we're interested in

[49:49] is if we can measure success on each of

[49:51] these tasks, is our success rate like

[49:53] getting better and better? Are we able

[49:55] to solve increasingly complex tasks um

[49:58] as we're learning from experience and

[50:00] building up um uh representations of the

[50:03] ways to do these simpler tasks? Any

[50:07] questions about this setting?

[50:11] Okay, cool.

[50:16] So the papers that we'll look at for the

[50:18] rest of the lecture look at sort of

[50:20] different parts of this space of um uh

[50:24] learning skills from experience having

[50:26] this library and ask questions about

[50:28] what should we do with the skills like

[50:29] after we've um induced them. So there's

[50:33] generally like a learning step where

[50:34] we'll have these uh tasks coming in.

[50:37] We'll try to get a skill out of them.

[50:39] will decide whether to store that skill

[50:41] um in the memory that we're building up

[50:43] over time. There's um the step of like

[50:47] actually using this memory of skills to

[50:50] potentially improve performance on the

[50:52] tasks that we're carrying out. And then

[50:55] finally, we might want to, you know, if

[50:57] we're getting too many skills, we might

[51:00] want to try to simplify those, like

[51:01] delete the ones that aren't being used,

[51:03] or if they're too specific, we might

[51:05] want to make them more general. um or

[51:07] like consolidate and merge multiple

[51:09] things together.

[51:11] [clears throat]

[51:14] We'll go a little bit deeper into one

[51:16] paper um that I think is pretty

[51:20] representative of ways for inducing

[51:22] skills. Uh it was also done here at CMU

[51:24] as work led by Zora Wong who will be

[51:27] giving a guest lecture on some other

[51:29] topics a little bit later on in the

[51:31] course. Um but this paper's called agent

[51:33] workflow memory and um the way it works

[51:37] is it we applied it to web tasks. Uh

[51:40] this is work with with Graham also um

[51:43] and me and uh we applied this to web

[51:45] tasks and you have a query like this and

[51:50] you know tell me the number of reviews

[51:51] that our store received so far and when

[51:54] the agent's carrying this out these are

[51:55] the actual tool calls that it'll

[51:57] produce.

[51:59] So we have this sequence of tool calls

[52:02] and we want to try to identify which

[52:04] parts of this might be potentially

[52:06] reusable in the future

[52:08] and you can probably guess how we do

[52:10] this. We ask a language model to take a

[52:13] look at the sequence of tool calls and

[52:15] identify ones that seem like they might

[52:17] be useful on future tasks.

[52:22] And we'll have the model output what we

[52:24] call workflows um which are sort of like

[52:26] a textbased representation of skills

[52:29] text and actions. And a workflow will

[52:31] have like a description of the subtask

[52:33] like searching for a particular item.

[52:37] And then um it'll have the sequence of

[52:40] actions that you use to do that. And

[52:43] we're having the model make this a

[52:45] little bit more general so that it could

[52:46] apply to like searching for other terms.

[52:49] So we have it use like create a template

[52:52] that can abstract out some parts of the

[52:56] um initial action sequence. You might be

[52:59] thinking like this is starting to look

[53:00] like code, right? That's true. Um and a

[53:03] little bit later on we'll compare code

[53:05] to this also and show how that can be

[53:08] better in some ways but also uh make

[53:11] things a little bit more uh fragile.

[53:14] A pretty important part of this is we'll

[53:17] um apply a judge model to this

[53:20] trajectory to decide um have the judge

[53:23] predict whether the trajectory seem to

[53:25] be correct or not. And we'll use that to

[53:28] determine whether we should actually add

[53:30] the workflows that were induced to the

[53:32] memory. Um because we don't want to be

[53:34] um remembering things that were

[53:36] incorrect because those might steer the

[53:38] model wrong in the future.

[53:41] >> Any questions about this?

[53:47] Okay. And

[53:50] so

[53:51] the way that we'll um give the model

[53:54] access to these uh collection of

[53:56] workflows um is just by sticking them in

[53:59] the context window of the model. So this

[54:01] looks a lot like you know this agent

[54:03] skill standard. Um you have choices

[54:05] about whether you show everything or

[54:07] whether you show just you know kind of

[54:09] the text description. um and what you do

[54:12] there could depend on how many skills

[54:14] you have and you know the context length

[54:16] of the model.

[54:20] So um for the sake of time I I'll skip

[54:22] over this induction prompt but we do

[54:24] find that um having this memory of like

[54:27] past uh subtasks um can help to improve

[54:31] the performance of the agent as it's

[54:33] learning online. So on the x-axis here

[54:36] we have like um different tasks in a

[54:39] fixed ordering from this benchmark

[54:41] involving interacting with like a map

[54:43] tool and the blue line here is the

[54:45] baseline agent that doesn't have a

[54:47] memory that sort of converges to around

[54:49] you know like 10% accuracy on these

[54:52] tasks and the labels here are the tasks

[54:55] that are being solved by the agent

[54:57] correctly. Um and then this black line

[55:00] which adds in this memory of um subtasks

[55:03] improves pretty substantially and it's

[55:05] able to um you know this gap emerges

[55:07] between the two but it's also able to

[55:09] carry out these like increasingly

[55:10] complex tasks eventually doing things

[55:13] like you know finding a hotel near this

[55:14] location showing me the walking path um

[55:17] that the baseline agent just isn't able

[55:19] to do.

[55:25] So this is using, you know, sort of this

[55:28] mix of text and example actions to

[55:31] represent skills.

[55:33] But we could also consider using code,

[55:36] right? And both of these are

[55:38] implementations of a search product um

[55:41] function. And

[55:44] if we're using just this text and

[55:45] examples, this is going to be in the

[55:47] context window of the model. and then

[55:50] it's going to be needing to produce

[55:51] these tool calls um in a new context,

[55:54] right? As it tries to carry out the same

[55:56] subtask. So, it's flexible like the

[55:59] model could choose to insert a

[56:02] particular search term to search for a

[56:04] different product. If the website has

[56:06] changed and we no longer have like this

[56:09] particular um element for the search

[56:12] box, then the agent could choose to use

[56:14] the correct one instead. Um, but it also

[56:18] means that the agent needs to like

[56:19] actually produce all of those tool calls

[56:21] itself. If we're using code, the agent

[56:25] could actually just call this function

[56:28] as a tool, right? If it passes in the

[56:30] right arguments and if the functions

[56:31] correct, then it doesn't have to do

[56:32] anything. It doesn't have to produce all

[56:34] of those low-level actions itself. Um,

[56:36] the tool will just do that as it

[56:38] executes in the environment. Can anybody

[56:40] think of uh some pros and cons of using

[56:43] a function like this as a representation

[56:45] for a skill?

[56:56] Any cons?

[57:00] >> It's very rigid.

[57:01] >> Yeah, it is very rigid. So like um the

[57:04] model will need to the model calling

[57:07] this tool will do exactly these three

[57:09] steps and there's no room to to deviate

[57:11] from it. Um yes that's a main call

[57:14] that's a main like con to it but we also

[57:17] get a lot of the pros of using code

[57:20] right so like we can nest functions it

[57:22] can be hierarchical we can actually like

[57:24] generate test cases for that specific

[57:27] function too independent from the entire

[57:30] trajectory that it's executed in. And we

[57:32] can do things like you know refactoring

[57:34] also.

[57:37] So uh Zora has another paper um called

[57:41] inducing programmatic skills or agent

[57:43] skill induction which um which do this

[57:46] and it looks pretty similar to the

[57:47] approach we were using to induce these

[57:49] textual workflows. So you have a

[57:51] trajectory like this with these tool

[57:53] calls and we'll have the language model

[57:56] um we'll we'll just use the fact that

[57:59] language models are also good at

[58:01] generating code and we'll um prompt the

[58:04] model to generate functions which

[58:07] abstract a lot of the um uh behaviors in

[58:11] this trajectory and these are real

[58:13] examples. So the language model will

[58:15] write this search reviews function and

[58:18] um a doc string for it and then you know

[58:20] it has these low-level tool calls as um

[58:23] lines in the function. This other one

[58:25] for open marketing reviews but we'll

[58:27] also have it generate sort of a rewrite

[58:29] of this original trajectory that uses

[58:32] those tools. So a really nice thing

[58:34] about um code is that we can test it by

[58:37] executing it. So instead of applying the

[58:39] judge to the original trajectory like we

[58:41] did before, we can have the language

[58:43] model. Well, we can execute this

[58:45] generated abstracted code and then apply

[58:47] the judge to the end result that you get

[58:50] from that. And if that appears to be

[58:52] correct, that's sort of like a stronger

[58:54] indicator that the skills, these code

[58:57] skills that you induced are also

[58:59] correct.

[59:00] And if they are, then we put them in the

[59:02] memory and they become usable to the

[59:05] language model just as tools. So this is

[59:08] a way of like building up a tool library

[59:10] that the model's able to use on future

[59:12] examples and um we show that it also you

[59:15] know improves performance.

[59:19] Any questions about that?

[59:24] Yeah. So a nice thing about um code

[59:26] skills is that they allow testing just

[59:28] of the skill by itself. Um there's this

[59:31] nice paper called skillw weaver which

[59:33] does this. Um, so this is sort of some

[59:36] pseudo code for the uh the loop that I

[59:40] just showed you where you have a task,

[59:42] you um propose some set of like code

[59:45] skills for it and then you'll try to use

[59:50] those skills to execute the task. You'll

[59:52] get an episode, you'll apply a reward

[59:54] model to it. Um, and if it succeeds,

[59:58] then you can put all those induced

[60:00] skills into your memory. But if not,

[60:02] then you could make some revisions to

[60:04] it. And there's a number of ways that

[60:06] skills might not succeed, right? So, um,

[60:10] one thing we could do is like apply a

[60:12] code llinter to an induced skill. So,

[60:15] here's a real example from the paper.

[60:17] There's this induced skill called

[60:19] identify pill. Um, you know, for like

[60:21] interacting with a drug website. And

[60:24] this uh function like takes a lot of

[60:26] arguments like you know the um the make

[60:29] of the pill the color but in the initial

[60:31] version of this skill that the agent

[60:33] wrote it actually didn't use all the

[60:35] parameters. So like it ignored this

[60:36] color parameter. So you could get

[60:38] feedback from a llinter on this skill

[60:41] and then sort of in the reflection type

[60:43] way um condition on that and then like

[60:47] you know uh create an updated version of

[60:50] the function and store that or like try

[60:53] executing that and store that. You could

[60:55] also use feedback from this reward model

[60:58] and condition on that when you're um

[61:00] making these revisions to the skill 2.

[61:02] So these are some nice benefits of code

[61:04] um that can be advantages even if you

[61:06] know the actual code function itself is

[61:08] a bit more rigid.

[61:12] Another nice benefit is that because

[61:14] these functions that are induced are now

[61:17] tool calls, it can really reduce the

[61:19] number of times that your agent needs to

[61:21] interact with the environment. So here's

[61:23] an example from um Zora's uh ASI paper.

[61:27] We have this uh task like uh updating a

[61:31] couple addresses on a page and for the

[61:34] base agent you have to you know like do

[61:37] all the very low-level actions of

[61:39] navigating through all these forms

[61:41] typing the particular um things from the

[61:44] address. But if we have this model that

[61:47] has induced these code skills, you can

[61:50] and this is a real example from uh from

[61:53] the work where we induce this navigate

[61:55] to address settings and update address

[61:57] details functions. We can actually solve

[62:00] this task in three steps where we um you

[62:03] know assuming that this is a good fit

[62:05] for the site. Um we can just call these

[62:08] two functions and um complete the task.

[62:12] Um, and the agent is actually much

[62:14] faster because it doesn't need to

[62:17] reobserve the website and then generate

[62:19] the tool call, then reobserve the new

[62:21] website, generate the new tool call. Um,

[62:23] as you'll probably see in the guey um,

[62:26] lecture that JY is giving, um, a really

[62:29] big bottleneck for these models is

[62:31] actually the number of times that they

[62:33] have to interact with the site because

[62:34] these images take up a lot of tokens and

[62:37] actually producing a chain of thought

[62:39] um, before each action takes up a lot of

[62:41] tokens too. All of those have to be

[62:43] generated. So efficiency is really

[62:45] important here.

[62:48] And um in this work we did find so we

[62:50] did a controlled comparison between

[62:52] using text skills and code skills. This

[62:54] was on a set of tasks which did have

[62:56] sort of more repeated structure. Um but

[62:59] we found that uh in comparison to no

[63:02] memory text skills um helped but code

[63:04] skills helped even more in terms of you

[63:06] know the accuracy of the system but also

[63:09] we got pretty big improvements in

[63:11] efficiency the number of times that the

[63:13] agent needed to interact with the page.

[63:18] Cool.

[63:21] So, as we've kind of talked about

[63:23] before, a big potential issue with

[63:25] skills is that they might not be

[63:27] general. And here's a failure case of

[63:29] this approach and actually a failure

[63:31] case of these code skills. So, we tried

[63:33] to see how well could skills generalize

[63:35] across websites. And we induced um these

[63:39] code skills on one site uh and then we

[63:42] tried to apply them on a real website uh

[63:43] like the Target shopping site. So this

[63:46] skill um that was induced on a different

[63:48] site worked on that site but like um

[63:51] uses assumes that this uh this um

[63:55] particular element that you're

[63:56] interacting with has a drop down like

[63:59] this. Whereas on the target site it's

[64:01] you know this set of radio buttons and

[64:04] so it it fails there. And um you have to

[64:07] have the model be able to like actually

[64:09] edit the skill based on um feedback from

[64:12] the environment as it's interacting with

[64:14] it.

[64:20] But code has a solution to this, right?

[64:23] Uh so we have um abstract classes and

[64:27] those can be instantiated in different

[64:29] ways. There's this uh paper called poly

[64:32] skill which does this. So um they're

[64:35] using code as the representation sort of

[64:37] building on this ASI work that we did.

[64:40] Um, but the first time that the model

[64:42] interacts with a new website, it writes

[64:44] an abstract class which doesn't have

[64:46] implementations for the methods, but

[64:49] could have stubs like searching for a

[64:51] product, adding to a cart, checking out.

[64:53] And um, then it'll also write a website

[64:57] specific implementation of it like this

[64:58] one for Amazon. Then when it's

[65:00] interacting with a different site, you

[65:02] could have some metadata or you could

[65:04] even just have the language model

[65:05] trigger that this particular concrete

[65:08] implementation no longer applies. and

[65:10] then you'll write a different

[65:11] instantiation of the abstract class. And

[65:13] they show that this helps too. Um, this

[65:15] is also nice because it gives you a way

[65:17] to have like a large number of specific

[65:19] skills, but only have a subset of them

[65:23] be active at a given time that are

[65:25] actually relevant. So, this kind of

[65:26] makes sense, right? It's, you know, just

[65:28] a software engineering best practice

[65:29] that's also applied to agents.

[65:35] Okay. Uh, yeah, we talked about all this

[65:38] already. um you guys had a good sense of

[65:40] the the pros and cons of each of these

[65:42] types of representation, but it's

[65:44] helpful to know that, you know, the

[65:45] skills standard allows you to combine

[65:47] both and um there's a lot of research to

[65:50] be done on the best way to combine these

[65:52] representations together. Um like uh

[65:54] said,

[65:56] okay, so we'll go quickly through a few

[65:59] papers um on different kind of like

[66:01] parts of this skill life cycle. This is

[66:04] a really open research topic of like

[66:06] what are the best ways to induce and

[66:08] manage these skills. Um you'll have the

[66:11] papers for for more details. Um but you

[66:13] can also explore this in your projects

[66:16] uh towards the end of the lecture or the

[66:18] end of the class if you're interested.

[66:22] Everything we've talked about so far has

[66:24] been learning from success, but it's

[66:26] also potentially pretty helpful to learn

[66:28] from failures. So say that the model

[66:31] like tries to carry out this task like

[66:33] um you know searching for Bluetooth

[66:35] headphones. Um but for this particular

[66:38] website they sort of have like their

[66:40] search terms are or rather than and so

[66:43] you get a list of everything that's

[66:45] Bluetooth or headphones or a Sony. This

[66:47] is a real example from this reasoning

[66:49] bench paper from Google. So you get like

[66:51] 5,000 results and the agent just breaks

[66:54] on this like it has to pagionate through

[66:57] all of these 5,000 results. it does, you

[67:00] know, it loses track of what the task is

[67:02] and it fails. But if we observe that um

[67:06] failed trajectory sort of in the

[67:08] reflection style way, we could uh

[67:11] produce some text that gives guidance on

[67:13] how to avoid it in the future. Like

[67:15] saying um we should give a more specific

[67:17] search term rather than this more

[67:18] general one and we should you know have

[67:21] like a larger number of items displayed

[67:23] so the model gets more in its context

[67:25] window at once. And this paper um

[67:28] generally uses the same framework as

[67:30] like uh agent workflow memory, agent

[67:33] skill induction, but instead of just

[67:34] having these kind of abstractions of the

[67:36] correct trajectories, it generates this

[67:39] text feedback um which um is applicable

[67:42] to failed trajectories too and is also

[67:45] you know the kind of thing that you

[67:46] would write in a skill yourself um if

[67:49] you were writing one

[67:52] and they find that this is pretty

[67:53] helpful. So these are different like

[67:55] types of memory. Um so synapse uses

[67:58] trajectories

[67:59] like full trajectories with all of the

[68:02] actions and observations all the tool

[68:04] calls and messages. Um this is agent

[68:06] workflow memory that uses these slightly

[68:08] abstracted parts of trajectories. And

[68:11] this is their approach that uses these

[68:14] text descriptions of strategies and um

[68:17] adding and negatives going you know

[68:19] adding and negative examples as inputs

[68:21] to the memory. um uh doesn't improve

[68:25] performance when you're using either

[68:27] trajectories or

[68:30] um workflows, but does improve

[68:33] substantially when you have sort of

[68:34] these text descriptions, which kind of

[68:36] makes sense given the example we saw

[68:38] before because you can describe in a

[68:40] general way how not to fail

[68:43] rather than remembering and conditioning

[68:45] on those failures.

[68:50] Another important thing to think about

[68:52] is we're deciding whether to store

[68:55] trajectories um you know store things in

[68:58] the memory or what type of strategies to

[69:02] infer from the examples based on whether

[69:04] we judged the example to be successful

[69:06] or not. That's in most of this work

[69:10] using a model as a judge that looks at

[69:12] the final state of the trajectory, looks

[69:14] at the task that you were trying to

[69:16] solve and predicts does it seem like I

[69:18] got it correct or not. So a really good

[69:20] question to ask here is what you know

[69:23] how much does the quality of that judge

[69:27] affect the performance of the algorithm

[69:29] because we know the judges aren't

[69:30] perfect. Um this paper reasoning bank

[69:33] controlled for this. So they um run

[69:36] their methods with a perfect judge. Um

[69:39] and they also like to so they use kind

[69:43] of the ground truth knowledge of whether

[69:44] it succeeded or not. Um but then they

[69:47] add some noise into that and so you're

[69:49] able to control um the accuracy the

[69:53] simulated accuracy of judging this

[69:55] trajectory and the performance does fall

[69:58] off but they find there's kind of a

[69:59] sweet spot where um you do get

[70:03] improvements from the memory um and uh

[70:06] there's sort of a widish range of

[70:08] accuracies where using the judge to

[70:11] induce the memory is helpful but there's

[70:13] definitely room to do future work here.

[70:19] Okay. And uh yeah, with the last few

[70:22] minutes, um I want to come back to we

[70:26] had a question before about does having

[70:28] more skills than are necessary um

[70:31] potentially hurt performance? And we

[70:33] also had a question about like um we're

[70:36] if we're retrieving skills from a set um

[70:40] does that retriever matter? Like does

[70:42] the quality of that retriever matter? So

[70:45] um there were some nice ablation

[70:46] experiments in this reasoning bank paper

[70:49] that uh control um how many experiences

[70:53] you are retrieving from the memory that

[70:56] you have and they show that performance

[70:59] does fall out fall off as you have more

[71:02] available. Um so this could be because

[71:05] of a couple different factors. So um you

[71:09] know maybe you just haven't run your

[71:12] agent on that many tasks and maybe

[71:14] there's nothing relevant in your memory.

[71:17] So putting more stuff in is just bound

[71:20] to be irrelevant. That would be sort of

[71:22] like just a fundamental limitation of

[71:24] this approach applied in that setting.

[71:26] Right? You can only learn if there's

[71:28] some similarities between the things

[71:31] you're learning from and the things

[71:32] you're applying to. But it could also be

[71:34] like a limitation of the model itself.

[71:37] Maybe the model gets thrown off by

[71:39] having more things available in the

[71:41] context window. That could potentially

[71:43] be fixed by training the model, right?

[71:45] To be better at not being distracted by

[71:47] irrelevant context, to be better at

[71:49] reasoning about what's actually

[71:51] relevant.

[71:56] And um yeah, it can also potentially be

[71:59] useful to uh explicitly reduce the size

[72:02] of your memory um so that there's less

[72:05] of a burden on the language model to

[72:08] select from the things that are in it.

[72:10] And um we did some work on this that

[72:13] sort of uses like a caching type

[72:15] approach um that you just look and see

[72:17] how often has a particular item in your

[72:19] memory been used in the past um and if

[72:22] it hasn't been used very frequently,

[72:24] you'll drop it.

[72:26] And this can you know improve this

[72:28] efficiency of the approaches quite a bit

[72:31] because you don't have to put as much in

[72:33] your context window but can also improve

[72:35] their success if the models are getting

[72:36] distracted by things that are

[72:38] irrelevant.

[72:41] Yeah. And the very last thing that we'll

[72:43] cover is so all of this was in some ways

[72:46] a little bit ad hoc, right? Like we were

[72:48] just having the language model look at

[72:50] these past experiences and then produce

[72:53] a skill which would be put in the memory

[72:55] and used in the future. But we're just

[72:58] like prompting the language model to

[73:00] predict things that seem like they might

[73:02] be useful in the future. And a really

[73:04] natural question is could you just train

[73:06] the language model to do that directly?

[73:08] Um you can. Um this is a direction

[73:11] that's starting to be explored just

[73:12] really recently. So these papers um are

[73:15] just appearing at you know just appeared

[73:17] at ACL um this year. But the basic idea

[73:21] here is that we're going to do

[73:22] reinforcement learning over multiple

[73:25] tasks seen in sequence. So this online

[73:27] learning setting that we've been

[73:29] covering for evaluation, we're also

[73:31] going to run training on it. We'll get

[73:33] multiple similar tasks in sequence and

[73:36] we'll be building up the memory. um in

[73:40] the same way that we've been doing

[73:41] before by inducing skills from the

[73:43] experience and using the memory on the

[73:45] future tasks. So this is a very complex,

[73:49] you know, process, right? Like we're

[73:50] using a couple different models here. Uh

[73:53] we're storing things in a memory. We're

[73:55] retrieving those. We're using them. But

[73:57] the good thing is reinforcement learning

[73:59] doesn't care. You can just apply

[74:00] reinforcement learning to complex

[74:02] non-ifferiable processes like this.

[74:04] We'll have a couple lectures that show

[74:06] you how. Um and you can get reward from

[74:11] uh

[74:12] did this second task succeed and did it

[74:17] use tasks that were induced in the past.

[74:20] So you can just do reinforcement

[74:21] learning on this reward being trained on

[74:25] um skill induction on sequences of

[74:27] similar tasks. And um there's a couple

[74:31] papers that have explored this. They

[74:32] both find that this is helpful. And uh

[74:35] one of them had this interesting result

[74:36] that um it helps to improve success if

[74:40] you also include this reward term that

[74:42] incentivizes reuse of the skills. So you

[74:45] could also imagine like introducing

[74:47] other sorts of reward terms that like

[74:49] minimize the size of the skill libraries

[74:51] that you've induced to try to you know

[74:53] kind of keep things regularized and not

[74:56] overfit too much. Um I think there's a

[74:58] lot of interesting like feature work

[74:59] that could be explored here.

[75:03] And um yeah that's uh that's all the

[75:06] time that we have. Uh but uh hopefully

[75:09] you got a sense for the way that skills

[75:11] are induced and also written. Um you'll

[75:14] apply those in your projects and you can

[75:15] explore them in the research projects

[75:17] too. I'll stick around for a few minutes

[75:19] if folks have any questions.
