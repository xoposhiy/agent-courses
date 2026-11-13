# Lecture 9 recording

[Course index](../../README.md) · [Original source](https://www.youtube.com/watch?v=paAcPaaYZGM&list=PLSN0qpDfUvTM&index=9) · [Raw file](../../raw/videos/paAcPaaYZGM.json)

Retrieved: 2026-11-13T16:48:33.879216+00:00

[00:00] Okay, so let's go ahead and get started.

[00:03] So today is going to be about an intro

[00:06] to reinforcement learning which will

[00:09] build on the SFT for agents uh that we

[00:12] had last week. This is going to be the

[00:14] first of three lectures that we'll have

[00:16] on reinforcement learning. And so in

[00:19] this first one, we're going to be

[00:20] talking about basic poly gradient

[00:22] methods, which are ways where agents

[00:25] interact with the environment and get

[00:27] feedback and then update their weights

[00:29] to make things that were successful that

[00:32] got high reward more likely and things

[00:36] that got low reward less likely. We'll

[00:38] then have a second lecture which will

[00:40] actually be next week on uh more

[00:43] advanced RL algorithms talking about off

[00:46] policy methods about um some of the

[00:48] things that you need to do to stabilize

[00:50] RL and get it to work. And then our

[00:54] third lecture will be on RL systems and

[00:56] going into some of the practical

[00:58] frameworks and you know things that you

[00:59] need to think about and pay attention to

[01:01] in hyperparameters when you're training

[01:03] these agents. And all of these should

[01:05] set you up uh pretty well for assignment

[01:09] three, which is going to be focused on

[01:11] training models with reinforcement

[01:13] learning in two settings. So the first

[01:16] setting is going to be a simple kind of

[01:18] sandboxed setting, which we'll actually

[01:20] use as a running example in this

[01:22] lecture. It's going to be called number

[01:24] search. And the second one is going to

[01:26] be like a simple kind of uh crafting

[01:28] environment that's a little bit like

[01:30] Minecraft. So for these, they're

[01:32] definitely going to require more compute

[01:34] than your previous assignments have. Um

[01:36] so you'll be using the compute credits

[01:38] more heavily, but uh you should have the

[01:41] foundations to get started on those

[01:43] assignments after these first two

[01:45] lectures. And um yeah, and we're looking

[01:48] forward to uh to seeing what you all do

[01:50] for those. We'll also have a guest

[01:52] lecture on Thursday from um Akari Asai

[01:55] who's a faculty here at CMU uh who's an

[01:58] expert on deep research and she'll be

[02:00] talking about that as another domain for

[02:02] agents uh that complements the the ones

[02:05] that we've talked about so far. Cool.

[02:08] Any uh any quick logistic questions

[02:10] before we get started?

[02:14] Okay. Yeah. So uh today we'll have a

[02:17] bridge from uh supervised fine-tuning to

[02:19] policy gradient methods which are kind

[02:22] of the most uh the most basic but also

[02:25] one of the most elegant forms of

[02:26] reinforcement learning.

[02:30] So the running example that we'll use is

[02:32] this task that we'll call number search

[02:34] which is basically like training an

[02:37] agent to guess a number based on

[02:39] feedback about whether you're too high

[02:41] or too low. So this is a pretty simple

[02:43] task but you know easy to understand and

[02:45] easy to come up with a reasonable policy

[02:47] for it. So the setup is there's this

[02:51] number which is part of the environment

[02:53] for this task but isn't known to the

[02:55] agent and it's an integer between 1 and

[02:57] 16. The agent is going to get four

[03:00] attempts to guess the number. And after

[03:02] it makes a guess, the if it got it

[03:05] correct, the environment will say

[03:07] correct. But otherwise, the environment

[03:08] will say, uh, you should go higher or

[03:11] you should go lower. And then the agent

[03:14] can make another guess up to four

[03:15] guesses in total. If at any point the

[03:18] agent gets it correct, the task ends and

[03:20] it gets a reward of one. But if you

[03:24] reach the end of your four guesses and

[03:25] you haven't gotten it correct, then it's

[03:27] a reward of zero.

[03:30] Okay. So, a lot of the trajectories that

[03:33] we'll walk through are from an example

[03:36] of this where the hidden number is 11.

[03:38] So, the agent is going to try to guess

[03:39] that.

[03:41] And here's four possible attempts at

[03:44] this where in the first one the agent

[03:46] says 8, gets feedback, you should go

[03:49] higher. It says 12, gets feedback, you

[03:51] should go lower. uh 10 higher and then

[03:54] 11 so it gets it correct on the last

[03:56] guess.

[03:58] In another attempt we might start with a

[04:00] lower number. So this is actually what's

[04:03] the optimal policy here? What's the best

[04:05] starting number?

[04:07] The middle, right? So it's kind of like

[04:09] 20 questions. You want to like split the

[04:10] space, right? So the best first guess is

[04:13] eight. But uh and actually how many of

[04:17] you folks have played Wordle?

[04:19] you know the guessing game from the New

[04:21] York New York Times. It's a fun game.

[04:22] It's kind of in a similar space and

[04:24] there's like an optimal first guess that

[04:26] you can make which reduces the the the

[04:30] space in an information theoretic way.

[04:33] Similar concept here but simpler. So you

[04:36] could start off with a you know

[04:37] suboptimal first guess of four but you

[04:40] could still succeed in the task right by

[04:43] taking this feedback into account going

[04:45] higher then going higher then going you

[04:47] know lower and eventually getting it

[04:49] correct

[04:51] but you could also go wrong right so we

[04:53] could start with a very bad guess of 16

[04:55] and um unless we got that right the

[04:57] feedback's going to be lower and in this

[05:00] case we might time out so we don't get

[05:02] it within four guesses and similar

[05:05] Similarly, we could have another pretty

[05:06] bad policy of starting with one and then

[05:09] going two and three and four and um and

[05:11] timing out and failing at the task.

[05:14] Everybody clear on the the setup? Okay,

[05:17] great.

[05:19] So,

[05:20] we'll also have rewards for

[05:22] trajectories. And a reward is just a

[05:24] scalar value which tells you how good or

[05:27] bad that trajectory is. So in agentive

[05:30] settings, this might correspond to like

[05:32] did the code that you write pass all of

[05:34] the unit tests in like Swedbench for

[05:37] example and you get a reward of one if

[05:39] it passes all the tests a reward of zero

[05:41] if it doesn't pass all the tests or you

[05:43] could have you know like a value that's

[05:46] not zero or one that's not a binary

[05:48] reward too like what's the fraction of

[05:50] tests that you passed but in a lot of

[05:52] the domains that people are training on

[05:54] these days um in what's called RLVR like

[05:57] reinforcement learning with verified

[05:59] rewards. The rewards will be either zero

[06:02] or one. Um but the methods that we'll be

[06:04] talking about today are more general. Um

[06:06] they also apply to scaler valued

[06:08] rewards.

[06:11] So just a quick reminder of how SFT

[06:14] works. So in supervised fine-tuning, you

[06:16] have a demonstration of a task and

[06:19] you're training the agent to copy that

[06:21] demonstration by maximizing the

[06:24] probability of the demonstrated actions.

[06:26] Right? So if we break down one

[06:28] trajectory into these steps, we have a

[06:31] prompt that's given to the agent. Um we

[06:33] have a guess um feedback from the

[06:35] environment higher. We have another

[06:37] guess more feedback from the uh

[06:39] environment and so on. And our task is

[06:42] going to be given these demonstrated

[06:45] actions which we'll write a star. We

[06:48] want to maximize the probability that

[06:51] the agent assigns to those actions

[06:53] conditioned on all the past history up

[06:55] to that point. Right? And so this will

[06:58] be just you know the supervised

[07:00] fine-tuning loss is maximizing the log

[07:02] of the probability of that sequence

[07:05] which is the sum of the log of the

[07:06] probabilities of the individual actions

[07:09] right and there's a lot of ways we could

[07:11] get these target actions that we're

[07:13] trying to imitate. So they could be from

[07:15] a person who gives a demonstration from

[07:17] the task. They could be from like a

[07:19] stronger model that we're trying to copy

[07:21] to distill from today. They could also

[07:24] be from uh trajectories from the agent

[07:27] itself that we're trying to reinforce in

[07:30] the model.

[07:32] But this should hopefully be a review

[07:33] from you know your previous classes on

[07:35] LLM training and and from the SFT

[07:38] lecture.

[07:40] Okay. But SFT has some problems which

[07:43] reinforcement learning is going to

[07:45] address. So there's roughly like three

[07:48] of these that we'll focus on. The first

[07:50] one of these is what we might call task

[07:52] mismatch. So supervised fine-tuning

[07:55] maximizes the probability of

[07:57] demonstrated actions at each point in

[07:59] time. But what we're really interested

[08:01] in is maximizing the probability that

[08:03] the agent carries out the task

[08:05] successfully.

[08:07] And these are similar to each other, but

[08:09] they're not quite the same. And there's

[08:12] a couple reasons for this. So the first

[08:15] reason is that there are multiple ways

[08:17] to carry out the task successfully,

[08:19] right? So, uh, starting with eight is

[08:22] kind of the best thing to do, um, as a

[08:24] first guess, but, um, it would also be

[08:27] reasonable to start with, you know, four

[08:29] as long as you're able to, uh, take the

[08:32] feedback into account. And for this, you

[08:36] know, here after this first step of

[08:38] feedback, we have various reasonable

[08:41] actions that we could take as well. and

[08:44] a demonstration, whether that's, you

[08:46] know, from a person or another model,

[08:48] only shows one way of solving the task,

[08:50] but we want the agent to be able to um

[08:52] potentially use other ways as well.

[08:56] And a second problem is that some

[08:58] actions that you can take are worse than

[09:01] others, but to SFT, they all look the

[09:03] same. So it would be very bad for us to

[09:07] in response to the feedback you should

[09:10] go higher it would be very bad for us to

[09:12] like output a number below eight right

[09:15] but SFT doesn't make a distinction

[09:17] between the actions that weren't

[09:20] demonstrated

[09:21] and so it would get the same loss if um

[09:24] you know the agent had highest

[09:25] probability on um a lower alternative

[09:30] action rather than a higher alternative

[09:32] action that wasn't the one that was

[09:34] demonstrated.

[09:36] So that's one problem of the mismatch

[09:38] between this SFT loss and the objective

[09:41] that we're actually interested in of

[09:42] maximizing you know expected reward or

[09:46] the probability of success on the task.

[09:49] The second problem is data mismatch. So

[09:53] we'd like to be able to learn from um

[09:55] suboptimal data too. Even if we assume

[09:58] that our demonstrations are the best way

[10:00] to achieve a task, there's, you know, if

[10:04] we had access to other demonstrations

[10:07] that were less optimal or maybe even

[10:10] weren't successful, those could provide

[10:12] useful signal for our models too. So

[10:17] like uh say that we know that this is a

[10:20] bad trajectory like it times out. We

[10:23] wouldn't want to just do SFT on this,

[10:25] right? We wouldn't want to maximize the

[10:26] probability of those actions, but we

[10:28] might want to uh have some learning

[10:31] method that could um have the model not

[10:34] take trajectories like this. And

[10:37] reinforcement learning is going to be

[10:38] one way of doing that.

[10:42] The third problem is what's known as

[10:44] exposure bias. So in SFT, you're

[10:48] training a model to make predictions of

[10:51] the next action given a fixed sequence

[10:53] of past actions, right? And that fixed

[10:56] sequence of actions comes from

[10:58] somewhere.

[11:00] But then at evaluation time, the

[11:03] previous actions are going to be

[11:05] generated by the model itself, right?

[11:07] Because you have to produce actions one

[11:08] at a time. You have the actions you

[11:10] produced in the past. It's this auto

[11:12] reggressive process of interacting with

[11:14] the environment.

[11:16] So

[11:17] if the agent um produces an action that

[11:21] is very out of distribution from the

[11:24] histories that it was trained on, it

[11:27] might just not have the the response

[11:30] that it produces might just not be

[11:31] calibrated because it never saw data

[11:33] like that. So say that we only trained

[11:36] on demonstrations where uh the next

[11:39] integer was, you know, did match the

[11:42] feedback that we got. So it was always

[11:43] higher if the feedback was higher. Now

[11:46] if at generation time the model makes a

[11:48] mistake and samples a lower number, it

[11:50] might just totally throw it off because

[11:51] it didn't see data like that in training

[11:54] time if we only trained on these optimal

[11:56] policies.

[11:58] Does that make sense?

[12:00] So one way of viewing reinforcement

[12:02] learning is it's a way of letting the

[12:04] model generate its own training data and

[12:06] also learn how to recover from the

[12:08] mistakes that it makes so that it's

[12:10] prepared to handle its own mistakes when

[12:13] you generate from it. And um this

[12:16] property of having the model generate

[12:18] its own training data is called being on

[12:20] policy. It's generally a good thing to

[12:22] have um because it prepares the model to

[12:25] you know deal with its own mistakes and

[12:26] the supervision that you get is a good

[12:28] fit for what the model's able to

[12:30] currently predict. Um but it can have

[12:33] some efficiency trade-offs and in

[12:35] Graham's lecture we'll talk a little bit

[12:36] we'll talk a lot actually about um uh

[12:39] methods that relax these assumptions

[12:41] that go more off policy.

[12:43] Cool. So these are three problems with

[12:46] um supervised fine-tuning for agents and

[12:48] for sequential prediction generally. Any

[12:50] questions about them?

[12:55] All right. So, reinforcement learning

[12:57] the general idea is instead of having

[12:59] like a uh trajectory a fixed trajectory

[13:04] which you learn to imitate by you know

[13:07] maximizing the probability of the

[13:08] actions. We're going to have the agent

[13:12] or you know the model um generate its

[13:15] own actions and then we'll evaluate the

[13:18] reward of those actions in the

[13:20] trajectory and um then we'll adjust the

[13:23] parameters of the agent so that um it

[13:26] makes high reward trajectories more

[13:28] likely and lowreward trajectories less

[13:30] likely. So formally and we'll see you

[13:33] know the formulation of this in a little

[13:35] bit we're going to be training the agent

[13:37] to maximize its expected reward you know

[13:41] expectation in probability under the

[13:43] agent and under the environment.

[13:46] So for um just schematically if we have

[13:49] you know a task like this number search

[13:51] game with the underlying goal in the

[13:55] environment B to guess number 11 we

[13:58] would have the agent generate multiple

[14:00] trajectories just by um producing likely

[14:03] actions at each step from the agent. You

[14:06] know just in the way that we would

[14:07] typically evaluate the agent in the

[14:09] environment for each of those

[14:11] trajectories. uh we'll get a reward um

[14:14] by

[14:16] uh by executing these actions in the

[14:19] environment and then we'll use that

[14:21] reward as feedback for the reinforcement

[14:23] learning method which is going to change

[14:26] the parameters of the agent uh to make

[14:28] these highreward trajectories more

[14:30] likely.

[14:33] So this is going to address the three

[14:35] problems that we uh laid out with SFT.

[14:38] So task mismatch is addressed because

[14:41] we're now training the agent directly to

[14:43] maximize expected reward. I haven't

[14:45] shown you how that's done yet. A lot of

[14:47] the first part of the lecture is going

[14:48] to be about how we do that. We'll

[14:50] formulate expected reward. We'll take

[14:52] derivatives of it. We'll optimize it

[14:54] directly.

[14:56] It will also fix data mismatch because

[14:59] as we'll see especially towards the

[15:00] middle and end of the lecture, the agent

[15:02] will now be able to learn from all

[15:03] trajectories. So it will get some signal

[15:06] from these bad trajectories and will

[15:08] avoid taking actions that lead to

[15:11] trajectories like that in the future.

[15:14] And it will also help deal with exposure

[15:16] bias because the agent is now going to

[15:18] be generating these trajectories that

[15:21] are used in training. It's going to be

[15:23] on policy. So if it makes mistakes and

[15:25] sees that those mistakes lead to a bad

[15:27] reward, it will get penalized for that

[15:30] and then learn to avoid those in the

[15:31] future. So it's sort of being prepared

[15:33] to deal with its own errors.

[15:38] Yeah. And um yeah, like a lot of the

[15:41] issues that people had with like

[15:43] language models up to maybe like three

[15:45] or four years ago where they were um

[15:47] being like uh they had kind of

[15:49] repetition biases. They would get stuck

[15:51] in loops. A lot of those issues got

[15:54] fixed once people started doing a final

[15:56] post-training step with reinforcement

[15:58] learning where the models were now able

[16:00] to recover from their own mistakes.

[16:05] Okay. So we'll talk about how we you

[16:08] know formulate interactions with the

[16:10] environment as trajectories which will

[16:12] then let us set up the objectives that

[16:13] we optimize.

[16:19] Okay. So um we won't spend too much time

[16:22] on this because it's should just be a

[16:23] recap from the first part of the course.

[16:25] But we have an agent which is going to

[16:28] be uh represented um as a policy which

[16:32] we'll term um pi theta. Theta are the

[16:35] parameters of the language model that

[16:37] you know that drives the agent

[16:40] and the agent's going to be producing

[16:42] actions um by sampling from the language

[16:45] model and you know then applying those

[16:48] um uh those samples in the harness that

[16:51] it's operating in that will produce

[16:53] actions um which you then take in the

[16:55] environment and the environment gives

[16:57] you back observations and also rewards.

[17:01] A lot of the settings that we'll look at

[17:03] only give you a reward at the end of the

[17:05] task, like when you actually execute the

[17:07] test cases. Um, but pretty much

[17:10] everything that we talk about will also

[17:12] apply to settings that have um

[17:14] intermediate rewards where for

[17:16] individual actions you take, you can

[17:18] also get some reward about um the value

[17:21] of that action. But just some examples

[17:24] of how you can apply this general

[17:25] framework for text generation. Um, the

[17:28] task instance might be the prompt that

[17:30] you're trying to produce a completion

[17:32] to. The observation might be the tokens

[17:35] you have so far. The action might be the

[17:37] next token. And the reward might be the

[17:40] score that you get from a judge model.

[17:42] For example, if you're doing um

[17:44] reinforcement learning from human

[17:45] feedback

[17:47] for a web agent, like the setting we

[17:49] talked about a week or two ago, the task

[17:51] instance might be the task and the

[17:53] website. And here there's a difference

[17:56] between the state of the environment,

[17:58] sort of everything that determines the

[18:00] environment and what the agent gets to

[18:02] observe. There might be some hidden

[18:04] state like what's the content of the

[18:06] backing databases, but the agent only

[18:08] gets to observe the page that it's

[18:10] currently on. And it can take actions

[18:12] like clicking, typing or scrolling. And

[18:15] it might get reward like intermediate

[18:17] reward like what are the number of

[18:19] subtasks from the the task description

[18:23] that it has completed so far. And for

[18:26] number search we've uh seen the task

[18:28] instance is the number that the agent is

[18:31] trying to guess which is going to be

[18:33] hidden from the agent. So in number

[18:34] search every task looks the same to the

[18:36] agent at the start. Um the observation

[18:39] would be high or lower or correct.

[18:41] Action would be the next guess. And the

[18:43] reward is given if the agent gets it

[18:45] correct that's a one or um if it times

[18:48] out then it gets a zero.

[18:53] So given these um these observations and

[18:56] actions and tasks we can start to

[18:59] formulate some notation which will let

[19:00] us derive the um reward terms that we're

[19:04] expected reward terms that we're trying

[19:05] to maximize. So a trajectory is a

[19:08] sequence of interled actions and

[19:10] observations and we'll represent um the

[19:14] sequence of observations and actions up

[19:16] to a given time step as the history h.

[19:20] So the history ht is going to have all

[19:23] of the actions and observations up to

[19:25] that point in time. And our agent policy

[19:29] pi theta remember theta are the

[19:31] parameters of the language model inside

[19:33] the agent. that's going to give us a

[19:35] distribution over the next actions that

[19:38] I would take um g at a particular

[19:41] history. Right? So you take the history,

[19:42] you plug it into your agent framework,

[19:44] you get a distribution over next tokens

[19:47] which correspond to actions in the

[19:49] environment. Any questions about that?

[19:54] Okay. So we also have rewards and in the

[19:57] most general setting you could be

[19:58] getting rewards along the way after each

[20:01] um action or observation that you take.

[20:04] Those formulations whether it's after

[20:06] actions or observations can be

[20:08] equivalent to each other. Um in the

[20:10] number search setting, we only get a

[20:12] reward after you um either time out or

[20:15] get the feedback that it was correct. So

[20:18] in the number search setting, your

[20:19] rewards will be binary and they'll just

[20:21] come at the end of the trajectory.

[20:24] And we'll write the reward of the

[20:27] trajectory as the sum over the rewards

[20:30] at all intermediate time steps. So toao

[20:33] is going to represent trajectory which

[20:35] is you know the sequence of these

[20:37] observations actions and rewards.

[20:41] Okay. So that's the notation and given

[20:44] this we can also you know have

[20:46] probabilities over trajectories and the

[20:50] probability of a trajectory is going to

[20:51] depend on two things. So the first thing

[20:54] is the probabilities assigned by the

[20:56] agent. So we can decompose this into a

[21:00] product of probabilities over time steps

[21:03] where um h sorry I dropped a p here but

[21:07] uh there should be a p before this term

[21:10] which is the probability from the

[21:12] environment of getting this observation

[21:16] and this reward conditioned on this

[21:18] history the action taken by the agent at

[21:21] that time step and the task and that

[21:23] probability from the environment we're

[21:25] going to multiply by the probability

[21:27] ility from the agent policy of producing

[21:30] this next particular action. So this is

[21:33] just the chain rule um decomposing this

[21:36] probability of producing this entire

[21:38] trajectory into the product of its

[21:40] component parts.

[21:43] And a key thing in RL is we don't

[21:46] actually know we we don't have to know

[21:49] anything about the environment. We don't

[21:51] have to know, you know, what's the

[21:53] probability of getting correct as our

[21:56] next observation or what's the

[21:57] probability of getting a next

[21:59] observation as I'm interacting with

[22:01] Amazon.com or something. The key thing

[22:04] about RL is we're going to interact with

[22:06] the environment which will by taking

[22:09] actions which will be a way of sampling

[22:12] from this distribution over observations

[22:15] and rewards. And that's actually going

[22:17] to be enough information for us to be

[22:20] able to learn how to differentiate um

[22:24] an objective that depends on this with

[22:27] respect to our parameters and update the

[22:28] parameters. And that's kind of magic in

[22:31] some sense, but it also makes

[22:32] reinforcement learning algorithms a bit

[22:34] slow because you kind of just have to

[22:36] like try stuff and see what happens. Um,

[22:39] and that's why reinforcement learning

[22:40] takes a lot of compute to run because

[22:42] you have to do these experiments um,

[22:45] experiments with the environment, see

[22:47] what happens, and use that as a somewhat

[22:49] indirect source of feedback about how

[22:52] your reward depends on your parameters.

[22:56] Any questions about this?

[22:59] >> Yeah.

[23:06] Yeah.

[23:09] >> Yeah. So I've uh rewritten this a bit

[23:11] from so the question was in classical RL

[23:14] there's a marov assumption which um says

[23:16] that the transition to the next state

[23:19] depends just on the previous state that

[23:21] you're in and the actions. So we're

[23:24] actually working with um a palm dp here

[23:26] a partially observed marov decision

[23:28] process um where there's a difference

[23:30] between the underlying state which you

[23:32] can't see and the observations that you

[23:34] can. So in a palm dp um your probability

[23:38] of the next observation has to depend on

[23:41] all of the previous observations and

[23:43] actions because you don't have access to

[23:45] the state. Um but for a pom dp these

[23:48] formulations should be equivalent and

[23:49] this one's just a little bit easier to

[23:51] work with for our purposes.

[23:54] Good question.

[23:56] Okay. Yeah, sorry about that P missing.

[24:00] Okay, so our objective is going to be to

[24:02] maximize the expected reward. Um, and so

[24:06] what does this mean? So what we want to

[24:10] do is we want to uh take samples from

[24:13] our agent like we want to have the agent

[24:16] generate trajectories through the

[24:18] environment. Um and

[24:21] like uh we're typically going to be

[24:24] doing that by sampling um actions from

[24:26] the language model and then feeding

[24:28] those actions through the agent

[24:29] framework, right? Um so we can write

[24:32] that um as sampling a trajectory from

[24:36] this distribution which is parameterized

[24:38] by the language model itself. And for

[24:41] each of those trajectories that we get

[24:43] by sampling from that distribution, it's

[24:45] a very complex distribution that depends

[24:47] on the agent, on the language model, and

[24:49] on the environment, we're going to get a

[24:51] trajectory and we're going to evaluate

[24:54] the reward of that trajectory that gives

[24:55] us a number. And we want to maximize our

[24:59] chance of getting a high reward here. So

[25:03] that's going to be maximizing this

[25:04] expectation. And we'll just write that

[25:06] objective as J of theta because it's a

[25:08] function of the parameters of our

[25:10] language model.

[25:12] So in our very simple setting um let's

[25:17] uh you know we have this number search

[25:19] we have say there's only four

[25:21] trajectories which are actually

[25:23] producible by the language model. So

[25:25] it's learned kind of a very sharp

[25:26] policy. Um say that it puts probability

[25:30] of 0.3 on this first trajectory 0.2 on

[25:33] the second and 0.25 25 on the third and

[25:35] fourth. Uh generally blue is going to

[25:38] mean success, a reward of one and red is

[25:40] going to mean failure, a reward of zero.

[25:42] So the expected reward if these are the

[25:45] only four trajectories which the agent

[25:48] can produce is going to be 0.5. Right?

[25:51] So just you know taking a weighted sum

[25:53] of these trajectory rewards weighted by

[25:55] the probability under the agent policy

[26:00] and the objective of training is going

[26:02] to be to optimize this. So we want to

[26:05] adjust the parameters theta to maximize

[26:07] this expected reward. So you can think

[26:09] of this as like this is kind of a bad

[26:12] current agent because it has a pretty

[26:14] high probability 0.5 of producing a

[26:17] trajectory with zero reward. We want to

[26:20] shift some of that probability. We want

[26:22] to shift ideally all of that probability

[26:24] to predicting trajectories that have

[26:27] reward of one. So shifting the

[26:29] probability mass from red to blue.

[26:32] This is obviously simplified because you

[26:34] know really the agent could produce an

[26:37] inf

[26:38] not infinite but like combinatorally

[26:41] exponentially large number of possible

[26:43] trajectories but we're just kind of

[26:45] simplifying the visualization a bit

[26:47] here.

[26:49] So one way that you can do this is a

[26:53] pretty simple modification to SFT that's

[26:55] really well motivated. It's called

[26:57] expert iteration.

[26:59] And um a particular

[27:02] uh type of expert iteration is called

[27:04] reinforced self-training or rest for

[27:07] short. So the idea in rest is going to

[27:10] be that we will just generate data from

[27:13] our current um policy from our current

[27:17] parameters of the language model and

[27:20] then we will choose the trajectories

[27:22] that are successful and use those as

[27:25] fine-tuning data and update the model on

[27:28] those. And so that's where the

[27:30] reinforced term comes from. It's going

[27:32] to sort of reinforce the correct

[27:34] behaviors that the agent is already

[27:35] producing. Um so it has two steps which

[27:39] are going to be iterated. Um rest em is

[27:42] actually named like rest I think

[27:44] expectation maximization because it

[27:46] looks really similar to the em algorithm

[27:49] uh which some of you might have seen in

[27:50] an ML class. But the idea is we will

[27:53] alternate between these two steps. The

[27:55] first step is you sample trajectories

[27:58] from the current policy. You get the

[27:59] rewards of them. The second step is you

[28:02] will um have the model make those uh

[28:05] trajectories very likely by just doing a

[28:08] bunch of SFT on those collected

[28:09] trajectories. Um and then you repeat you

[28:12] will get more trajectories from the

[28:14] current policy and you add those

[28:16] trajectories in to the existing set that

[28:20] you have of good trajectories and then

[28:22] you'll um train your model on all of

[28:24] those. So you have this growing data set

[28:26] which you are having the model um

[28:29] iteratively get very good at producing.

[28:32] Um yeah so that's kind of a high level

[28:34] description

[28:36] and uh the way this works mechanically

[28:39] is you will generate a bunch of

[28:40] trajectories. You will um evaluate the

[28:43] reward of each one. You'll select um

[28:46] using like a threshold and this is easy

[28:48] if your reward is binary. Um, if it's

[28:51] binary, you just keep the trajectories

[28:53] that have a reward of one and throw out

[28:55] the ones that have a reward of zero. And

[28:57] then you combine all of these kept

[28:59] trajectories across your instances. And

[29:02] those are the um those are the next

[29:05] iteration of your training set.

[29:09] And so then the objective is just the

[29:11] SFT objective. We want to maximize the

[29:13] probability of these actions in these

[29:16] cap trajectories. the one where the

[29:18] reward is for binary rewards one.

[29:23] Does that make sense? Any questions

[29:24] about that?

[29:27] So, schematically, this is actually

[29:29] going to look quite a bit like the

[29:31] reinforcement learning methods that we

[29:33] will talk about. Um, this isn't like

[29:35] technically referred to as reinforcement

[29:37] learning. Um, but it really has a lot of

[29:40] similarities to it because you're

[29:42] generating data from the model. um

[29:44] you're updating on that data in a way

[29:47] that is determined by the reward of the

[29:50] trajectories. And um we'll see how

[29:52] reinforcement learning does this in a

[29:54] little bit more of a fine grained way

[29:56] later.

[29:57] But this is a very simple and pretty

[29:59] effective uh baseline that you can start

[30:01] with which reuses all the same machinery

[30:04] of um supervised fine-tuning and is a

[30:06] good fit if you have binarized rewards.

[30:12] >> Yeah. Why is that self?

[30:16] >> So the difference from self distillation

[30:18] is just that you're using the reward to

[30:20] filter. Self-distillation could also

[30:23] refer to um training on all of the

[30:26] trajectories produced by the model.

[30:31] >> Yeah. So self it's called selfraining

[30:33] because it looks a lot like um you know

[30:36] like that but it's reinforced because

[30:38] you're using the reward and so you're

[30:40] reinforcing the good trajectories.

[30:42] Yeah.

[30:43] I mean this is a more basic question but

[30:45] how can you guarantee trajectories that

[30:47] do have a positive reward?

[30:49] >> What if like for example in the worst

[30:51] case you just have a bunch of bad

[30:52] trajectories?

[30:55] >> Yeah. So that's a great question like

[30:56] how do you guarantee that some of your

[30:58] trajectories have good reward? Um if

[31:01] your model can't produce trajectories

[31:03] that have good reward then reinforcement

[31:05] learning and this method um are probably

[31:08] not a great fit. So there's a few things

[31:11] you can do. one is you can um have some

[31:15] demonstrations of good trajectories

[31:17] which you train the model on. So you

[31:20] know like um the R1 paper um and a lot

[31:24] of reasoning models um will have an

[31:26] initial what they call cold start stage

[31:28] where they will train the model on

[31:30] reasoning traces um before they start

[31:33] doing reinforcement learning. So that

[31:34] just makes it easier for RL or something

[31:36] like this to be able to produce

[31:38] trajectories that have high reward. You

[31:40] can also like look at curriculum. So you

[31:43] can um select problems that do have

[31:45] enough trajectories which produce

[31:47] reward. Train on those first and then as

[31:49] the model gets better you're able to

[31:50] tackle harder problems. You can also

[31:53] have like intermediate rewards like if

[31:55] you have some knowledge of the problem

[31:56] and like know it's useful to explore the

[31:58] code repo first. You could give the

[32:01] model reward for doing that and then

[32:03] hopefully like after it learns to do

[32:04] that it'll kind of unlock solving the

[32:06] whole task. But this is a really big

[32:08] kind of issue that RL algorithms have to

[32:10] grapple with and those are a few

[32:12] solutions to it.

[32:14] Yeah. Cool.

[32:16] Okay. So now um let's uh actually get

[32:20] into the policy gradient methods.

[32:23] So we're interested to maximize this

[32:25] quantity uh J of theta the expectation

[32:29] of reward. And we can't just use back

[32:32] propagation to do this uh for two

[32:35] reasons. The first is that we are

[32:37] sampling actions from our policy. And

[32:41] the second reason is that we are then

[32:43] executing these actions in this like

[32:45] blackbox environment which is

[32:48] potentially

[32:50] which is almost always like

[32:51] non-ifferiable.

[32:53] Um and so this breaks our ability to do

[32:56] back propagation to you know directly

[32:59] you know like use the chain rule like

[33:01] you saw in a machine learning class to

[33:03] get the derivative of um your reward

[33:06] with respect to the parameters. So um

[33:10] actions are discrete and they're

[33:11] sampled. So the derivative with respect

[33:14] to um the parameters of a sample is zero

[33:18] almost everywhere because you know the

[33:20] parameters change the probabilities but

[33:22] don't um until you get to kind of a step

[33:25] point don't change the action sampled

[33:27] and the environment is usually not

[33:29] differentiable. So the general solution

[33:32] to this is actually a pretty classic

[33:34] method called reinforce um which was

[33:36] from Williams in 1992 and um it's going

[33:41] to use this uh definition of the

[33:45] expected reward and then basically just

[33:47] some algebra tricks in order to um

[33:50] compute an estimate of this that uses um

[33:55] samples from the model and um the same

[33:58] back propagation procedures that we've

[34:00] looked at before um to get par you know

[34:03] to get partial derivatives with respect

[34:05] to these parameters theta and we'll show

[34:08] you how to do that on the next slide.

[34:13] So this is the objective that we want to

[34:16] optimize. It's this expectation over

[34:18] trajectories from our environment and

[34:21] our policy and the expectation of the

[34:23] reward of those trajectories. So this is

[34:26] a if you recall what an expectation is

[34:29] it's a sum um over these things these

[34:33] trajectories

[34:35] uh of the term in here the reward but

[34:37] weighted by the probability of that

[34:40] trajectory. So this is a sum over a

[34:43] really large space like all possible

[34:45] trajectories from the language model.

[34:47] We're almost never going to be able to

[34:49] compute that exactly,

[34:52] but this is what it would come out to be

[34:54] if we wanted to compute it. Taking the

[34:57] gradient of this. So we just, you know,

[34:59] take the partial derivative with respect

[35:01] to the parameters theta. Um, we can move

[35:04] that uh inside the sum and this uh

[35:10] reward term depends only on the

[35:12] trajectory. So once we know the

[35:14] trajectory, we know what the reward is.

[35:16] it doesn't depend on the parameters

[35:18] anymore. The parameters produce the

[35:19] trajectory. Um but then the reward is

[35:22] just a function of the trajectory. So um

[35:25] this reward term is going to be

[35:26] multiplied by this partial derivative of

[35:29] this probability.

[35:32] But this is still difficult because this

[35:35] is a sum over like a potentially very

[35:38] large number of trajectories. So we're

[35:40] going to do an algebra trick here. And

[35:42] this is called the score ratio trick. um

[35:44] we're going to just uh multiply and

[35:46] divide by this term p of theta. So we

[35:49] have that over here and we also have

[35:51] that in the denominator. Those cancel.

[35:53] So this is the same as that. And then we

[35:57] can use this trick which is um the

[35:59] partial derivative of log p with respect

[36:02] to theta. We can just use the chain rule

[36:05] and it's get it's the partial derivative

[36:07] of um p / p. So we can use that identity

[36:11] here and we get this term. And this is

[36:14] going to be kind of magical because we

[36:17] now have this which is going to be an

[36:20] expectation over trajectories

[36:23] um times a reward term times this term

[36:26] here.

[36:27] And um this term is going to be this is

[36:31] the same computation that we do in SFT.

[36:34] Right? In SFT, we're also taking a

[36:36] partial derivative of the log of a bunch

[36:39] of unit tokens um with respect to the

[36:43] parameters of the language model. And um

[36:47] we're going to be able to uh estimate

[36:50] this quantity by sampling trajectories

[36:54] and then computing this term here. And

[36:57] this will give us an estimate of the um

[37:00] of the gradient of this uh expected

[37:05] reward. Any questions about that?

[37:09] >> So this is really general doesn't make

[37:11] any assumptions about um the language

[37:13] model or about the environment.

[37:17] >> Yeah.

[37:18] >> Are you going

[37:21] the

[37:22] series of states and actions but the

[37:24] actions are generated by large

[37:27] are also sequences of

[37:29] >> yeah

[37:31] normal way to reconcile that

[37:33] >> yeah we'll we'll break that down in a

[37:34] couple slides but yeah it's a good

[37:36] question

[37:38] yeah so um we'll just copy that term

[37:40] here and then we'll um break this into

[37:42] the component pieces so um these

[37:45] trajectories are going to be sampled by

[37:48] having the language model and the agent

[37:50] on top of it interact with the

[37:51] environment

[37:53] um and that's you know the same

[37:55] procedure that you would use when you're

[37:57] just running this agent. That gives you

[37:59] a trajectory. Um and we uh

[38:04] uh this should be um a sum over this

[38:09] should be an average over trajectories

[38:11] because we can estimate an expectation

[38:13] by drawing some number of samples from

[38:15] this distribution and then averaging the

[38:19] quantity inside the expectation. So if

[38:22] we average over a bunch of trajectories

[38:25] drawn from this distribution this

[38:27] quantity here um then we will get an

[38:30] estimate of this gradient.

[38:33] So um what are these uh terms inside

[38:36] here? Well it's um since this is a

[38:40] trajectory we break this up into steps.

[38:42] So it'll be a sum over time steps of um

[38:46] the gradient that's due to that

[38:49] particular action. And we'll see how to

[38:51] compute that in a slide.

[38:54] So yeah, so the three components here

[38:56] are the trajectories. We get those by

[38:58] sampling. Um the task level evaluation

[39:01] which we get from the environment. And

[39:03] then this gradient here which is going

[39:06] to be produced using the same way that

[39:08] we get gradients in in supervised

[39:10] fine-tuning. But the key thing is these

[39:13] actions here are going to be the ones

[39:15] sampled from the agent rather than ones

[39:18] that are demonstrated by uh you know

[39:21] some ground truth.

[39:25] Okay. So yeah, how do we get log

[39:27] probabilities of trajectories? Uh I'll

[39:30] go a little bit quickly through this.

[39:32] The the key thing to keep in mind is

[39:34] that the probability of a trajectory

[39:37] depends both on the probability from the

[39:40] language model plus agent but it also

[39:42] depends on the probability of getting

[39:45] the particular observations and rewards

[39:48] that you did from the environment. But

[39:50] the key thing is is that this

[39:51] probability doesn't depend on the

[39:53] parameters of the language model in any

[39:55] way. So if we differentiate this log

[39:58] probability of you know the uh

[40:02] trajectory with respect to the um

[40:05] parameters this entire term just goes

[40:08] away because it's a constant with

[40:10] respect to the parameters. So we can

[40:12] just ignore it and this um gradient

[40:16] uh for the trajectory is the sum of the

[40:20] gradients for the actions within the

[40:23] trajectory.

[40:25] So this is mostly just kind of like uh

[40:28] bookkeeping for rigor. Um but one thing

[40:31] that is important to think about is

[40:33] these actions that are being produced by

[40:36] the agent um might correspond to

[40:39] multiple tokens from your language

[40:40] model, right? So like maybe you need to

[40:43] say uh you need to say you're you're

[40:46] making a complex tool call and that

[40:49] splits up into multiple tokens. Um, of

[40:51] course, the log probabilities of those

[40:53] tokens are just going to be um summed up

[40:56] to produce the log probability of the

[40:58] entire action.

[41:02] And when you have this uh gradient of a

[41:07] trajectory, the gradient for a

[41:10] trajectory, you can just multiply by the

[41:12] reward, which is a scalar value from the

[41:17] environment to get the contribution of

[41:19] this trajectory that you sampled to the

[41:22] expectation.

[41:28] And how does this uh like actually look

[41:30] if you are running this on a real

[41:32] example. So you would um have your

[41:35] trajectory which is sampled from the

[41:37] agent. And um these blue tokens are the

[41:40] ones that are actually generated by the

[41:42] model. All the gray tokens are ones that

[41:44] are either like part of the prompt or

[41:46] part of the environment or added by the

[41:49] scaffold. But these are the ones that

[41:51] are actually produced by generating from

[41:53] the language model. and those are going

[41:55] to be the ones which um contribute to

[41:59] the loss for policy gradient.

[42:02] So we'll have all of these generated

[42:04] tokens. We'll get um log probabilities

[42:07] for those um of that generated action

[42:12] selected from the distribution of the

[42:15] language model over particular tokens at

[42:18] that point. And then we will just scale

[42:21] all of those um token log props by the

[42:24] reward that corresponds to this

[42:26] trajectory.

[42:28] Does that make sense? And then if you

[42:31] take the gradient of this, the gradient

[42:34] passes inside and gets applied to this

[42:37] log probability here. So that your

[42:40] gradient is going to be the reward times

[42:42] the gradient. So when I first looked at

[42:45] the code that implemented reinforce on

[42:47] like a pretty complex task, it was like

[42:50] using RL to optimize dialogue models

[42:53] from a paper called deal or no deal. It

[42:56] was kind of like really surprising that

[42:58] the implementation is so simple like you

[43:00] just do basically an SFT gradient

[43:02] computation and then multiply that

[43:03] gradient by a reward or multiply the

[43:06] loss by a reward and take the gradient

[43:08] of that. But it it works and the math

[43:10] works out.

[43:13] Yeah. So we'll have a mask here which is

[43:16] going to be you know you mask only to

[43:20] select the tokens that you generate and

[43:22] then you scale all of those by the

[43:24] reward for the trajectory.

[43:27] And that's how you implement the

[43:28] reinforce policy gradient algorithm.

[43:32] And so the training loop is just you

[43:34] sample task instances you evaluate

[43:37] reward on them. um get the loss using

[43:39] that slide that we just showed you and

[43:42] then um uh do an update on all of the

[43:47] instances in your batch of examples

[43:49] here.

[43:51] Later on we'll uh when we cover gpo

[43:54] we'll talk about how you could generate

[43:56] multiple possible trajectories for a

[43:58] given task example I and then use all of

[44:01] those in the update. But if you're doing

[44:03] just like standard reinforce, you would

[44:06] just be using one trajectory for each

[44:08] example and then um computing the update

[44:10] from that. So your um batch size would

[44:13] be the number of task instances that

[44:14] you're training on. Um but when we get

[44:16] to gpo um you will also have multiple

[44:19] samples per task instance. Any questions

[44:23] about this?

[44:29] Okay.

[44:31] Yeah. So um just very quickly with

[44:34] binary rewards this looks a lot like the

[44:36] rest um procedure that we talked about.

[44:39] Both of these are just um scaling log

[44:41] probabilities of actions by a reward.

[44:45] The difference is is that this reinforce

[44:48] method is like fully online. You're like

[44:50] sampling these trajectories and then

[44:52] updating on them directly. Whereas with

[44:54] REST, you build up a very large data set

[44:57] and then train on all of those and maybe

[44:58] do like, you know, a full epoch or

[45:00] multiple epochs on all of those

[45:02] instances. But um the intuition behind

[45:04] them is basically the same.

[45:08] Okay, but this has a lot of issues too.

[45:11] And so it's very rare for people to just

[45:13] run standard reinforce policy gradient

[45:15] out of the box.

[45:17] So the biggest I think the the the way

[45:21] of kind of the strongest motivation for

[45:24] the next methods that we'll talk about

[45:25] is thinking about how rewards should

[45:27] really be the update that you do from

[45:30] rewards should really be relative. So

[45:32] let's look at these two different

[45:33] trajectories. Um this one is successful

[45:38] and so all the actions are going to be

[45:39] upweighted by a reward of one if we use

[45:42] the update rules we've talked about.

[45:44] This one is unsuccessful.

[45:46] So we had a bad first guess, we

[45:49] eventually time out. And if we're just

[45:50] using basic reinforce or arrest, we are

[45:53] not going to do any update based on this

[45:56] example at all. Right? Because it's

[45:57] scaled by the reward. The reward is

[45:59] zero. So but we actually want to be able

[46:02] to learn not to do this, right? Um so

[46:06] the intuition for the next part is going

[46:09] to be about shifting our rewards so that

[46:12] um we still get a correct estimate of

[46:14] the gradient but um we're able to learn

[46:17] from um uh rewards at all different um

[46:20] scales or shifts. Um and another way of

[46:24] thinking about this is that the update

[46:26] that you do should depend on how well

[46:28] the policy uh would be expected to do on

[46:31] this example. So say that this is just

[46:33] like an easy example and um it and the

[46:38] model like 95% of the time gets a reward

[46:41] of one on it. If 5% of the time you make

[46:44] a really dumb mistake and get a reward

[46:47] of zero, you should update very heavily

[46:50] against those um costly but rare

[46:53] mistakes. And um baselines and

[46:56] advantages that we'll talk about next

[46:57] will be a way of doing that which will

[46:59] compare rewards to the reward that you

[47:02] would expect to get from the policy

[47:05] running on this example.

[47:08] And the math for that looks like this.

[47:10] We'll define an advantage which is going

[47:12] to be a function of the history up to a

[47:15] particular time step and an action. And

[47:18] that's going to be um say that you take

[47:21] this action from you take this

[47:23] particular action and then you sample

[47:25] from the language model for the rest of

[47:27] the trajectory

[47:29] that will tell you and you contrast that

[47:32] against if you just sample from the

[47:35] language model including that action and

[47:36] then continue on. This will tell you how

[47:39] good is this particular action um

[47:42] relative to uh how good is the what's

[47:45] the value of this particular action

[47:47] taking into account that the language

[47:49] model is going to take all the rest of

[47:51] the actions in the future.

[47:53] So maybe a concrete example will will

[47:55] help with this. Let's say that we are

[47:58] partway through this uh guessing game

[48:00] and we've guessed eight and gotten

[48:02] feedback higher, guessed 12, gotten

[48:03] feedback lower. So um we know that the

[48:06] numbers have to be between 8 and 12. So

[48:10] they can either be 9, 10 or 11. So we

[48:14] don't know exactly what this uh value

[48:17] function is. It depends on what our

[48:19] policy is. But we can think about um

[48:24] it's probably something like 2/3 or one,

[48:27] right? So like if the policy is is uh

[48:30] does the best thing possible

[48:33] uh always you should be able to just

[48:35] always win from this situation. But if

[48:38] it's a more random policy within the set

[48:40] of things that are valid it might be

[48:41] more like 2/3.

[48:43] But we can think about the advantage

[48:45] functions of particular guesses relative

[48:48] to this baseline. So like a guess of 11

[48:51] would be bad because

[48:54] um it's at one end of this range and if

[48:57] 11 is not correct then we have two

[49:01] candidates and one guess left so this

[49:02] advantage should be low whereas 10 would

[49:05] be good because whether or you know even

[49:09] if this is wrong then we have one guess

[49:11] left and we could go either higher or

[49:12] lower.

[49:16] So a lot of reinforcement learning

[49:18] algorithms are derived from different

[49:20] ways of estimating these advantage and

[49:23] value th this advantage as a function of

[49:27] uh this individual Q value for actions

[49:29] and values and we'll talk about a few of

[49:33] those for the rest of this lecture. But

[49:35] a key idea is that if we don't know um

[49:39] qpi or vpi, we can estimate them uh

[49:44] by we can estimate the expected reward

[49:48] of this particular action just by acting

[49:51] and we can estimate um this value

[49:55] of how well we would expect to do using

[49:57] what we'll call a baseline function.

[50:00] We'll see some examples of baseline

[50:01] functions uh for the next few slides.

[50:07] So a baseline is just a way of um

[50:10] rescaling your rewards.

[50:13] So this is the reinforce estimator of

[50:16] the expected um return here. Um which

[50:20] you know scales uh the reward by um the

[50:24] log probabilities of which uses the

[50:27] reward to rescale this gradient of the

[50:30] log probabilities. And um these

[50:32] advantage-based methods will generally

[50:35] have this form here of um subtracting

[50:38] off a baseline from this reward.

[50:42] And these are different these are not

[50:44] numerically equivalent to each other but

[50:47] they are both different valid ways to

[50:50] estimate the policy gradient. We'll uh

[50:53] have a slide next that shows that this

[50:55] is also a valid unbiased um estimator of

[50:59] this same quantity.

[51:01] But for different like baselines that we

[51:04] can define um we'll get different

[51:06] reinforcement learning algorithms. So

[51:09] we'll have an example coming up which

[51:10] kind of motivates why subtracting a

[51:12] baseline uh can be a good thing to do.

[51:15] Um so and in that example the baseline's

[51:18] just going to be a constant. The

[51:19] baseline could also be a running average

[51:22] of all the rewards that you've gotten so

[51:24] far from all the examples that you've

[51:26] seen. It could also be a trained like

[51:29] neural model and this is the case in

[51:32] actor critic methods or a method called

[51:34] PO which we may cover in the next

[51:36] lecture. Um but you need a separate

[51:38] model from your policy for that that can

[51:41] be expensive. And in the final part of

[51:44] this lecture we'll actually not have a

[51:46] separate model but we will just estimate

[51:49] this expected reward under the policy by

[51:52] sampling from the policy itself. Um, and

[51:55] that'll be the gpo algorithm.

[52:00] Okay. So, any questions about this?

[52:06] We'll see a little bit more motivation

[52:08] for baselines in the next few slides,

[52:10] too.

[52:12] [snorts]

[52:16] So, just a quick uh note about um about

[52:21] uh baselines and bias.

[52:24] So

[52:25] both of these terms are estimates of the

[52:30] underlying expected reward.

[52:33] And um an estimate uh could have a bias.

[52:38] Estimates have bias and variance, right?

[52:40] A bias is like um how much is the mean

[52:44] of this estimate potentially shifted

[52:46] from the true value. And the variance is

[52:49] like how much spread is there in the

[52:51] values that I'm uh drawing for that

[52:54] estimate. So uh you might be worried

[52:57] about bias um in your estimator. And

[53:01] there's this uh this lema that shows

[53:04] that subtracting a baseline which

[53:06] depends only on the history up to this

[53:08] point which all of these baselines that

[53:11] we've defined here do um does not bias

[53:14] the gradient. So the way to see this is

[53:17] this is our advantage our baseline based

[53:20] estimate of the expected um return and

[53:25] we can uh decompose this the expectation

[53:28] of this into these terms here. So um

[53:32] using just the associative property

[53:34] putting this here um that's the

[53:36] definition of uh the uh partial

[53:40] derivative that's the that's the um the

[53:44] gradient for J minus this expectation

[53:47] here of B * this and this is going to be

[53:53] um equal to this if this um expectation

[53:58] of this term here is zero

[54:00] And we can see that by just um taking

[54:03] this term here and uh writing out the

[54:06] expectation like this. Um it's the

[54:08] expectation over um actions uh sampled

[54:12] from this policy. Um and bringing out

[54:15] this baseline term which does not depend

[54:18] on anything other than the history up to

[54:20] this point. We just get the sum over

[54:22] actions of the probability of those

[54:24] actions.

[54:26] And um that's going to uh we can use

[54:30] this same uh log derivative trick and

[54:33] rewrite that as this. And then this will

[54:36] just become one um and it'll be um a

[54:39] bias term times the partial derivative

[54:42] of one which is going to be zero.

[54:46] So this tells you that you can uh

[54:48] subtract um a baseline which depends

[54:51] only on the history of um actions up to

[54:54] that point, actions and observations up

[54:56] to that point without biasing your

[54:58] estimate of the policy gradient.

[55:04] But let's look at an example of how

[55:08] these like baselines can actually reduce

[55:10] the noise in your estimate of the

[55:12] gradient. And this is going to actually

[55:14] be really important because uh a huge

[55:18] amount of the work in reinforcement

[55:19] learning is uh reducing the variance in

[55:22] your estimates of the gradient um so

[55:24] that learning is stable um and robust to

[55:28] all the variation that you have from

[55:29] sampling from the policy and from the

[55:32] environment. But to motivate this we'll

[55:34] look at just a very simple example um

[55:37] where you just have two actions. Uh

[55:39] there's no multiple time steps. There's

[55:42] just a single decision that you make and

[55:44] two actions. You're either guessing a or

[55:47] b. And we'll have just a very simple

[55:50] policy which only has one parameter

[55:53] theta.

[55:54] And we'll get a probabilistic policy

[55:56] from this by applying the sigmoid

[55:58] function to theta. So sigmoid is this

[56:01] squashing function, right? Which um maps

[56:04] a real value from negative infinity to

[56:06] infinity um into a value between 0 and

[56:10] one. and we'll take that value as the

[56:12] probability of choosing a.

[56:15] So say that for our current policy we

[56:18] have this theta is negative 1.1 which

[56:21] will give us these uh very convenient

[56:23] probabilities of 0.25 for guessing a

[56:28] which has reward of one and probability

[56:31] 0.75 of guessing B which has probability

[56:34] zero. Is this a good policy or a bad

[56:37] policy?

[56:40] Think about how the probabilities

[56:41] correspond to the rewards.

[56:48] This is bad, right? Because it puts

[56:51] higher probability on the option that

[56:53] has no reward. So we want our policy

[56:56] gradient to update this parameter theta.

[56:59] Which way do we want theta to get

[57:01] updated?

[57:06] Yeah, we want it to become more

[57:07] positive, right? Because um if theta is

[57:10] larger, we'll be farther up on this

[57:12] curve, we'll get a higher probability

[57:14] for guessing A, which is the option that

[57:16] has higher reward.

[57:18] So let's compute our gradients uh

[57:21] without using a baseline and see if

[57:23] policy gradient tells us the right

[57:25] thing. So um we can compute the um

[57:28] expectation we can compute um the uh

[57:31] values that we we would get um as

[57:34] estimates of the policy gradient from

[57:37] each of the actions that we could take

[57:40] under the policy that we could sample.

[57:43] So if we sample guess A, what's our

[57:45] estimate of the gradient? Well, we get

[57:47] this by multiplying the reward by the

[57:50] partial derivative, which um using

[57:53] properties of sigmoid, the partial

[57:54] derivative here is 75. So the gradient

[57:59] is just the product of those, it's 75.

[58:02] We can do the same thing. Uh what's our

[58:04] estimate of the gradient if instead of

[58:05] sampling A, we sample B? That because

[58:09] the reward is zero actually gives us a

[58:11] zero gradient back. So this is kind of

[58:15] looks like the trajectories that we saw

[58:16] before where we didn't get any gradient

[58:18] from ones with reward zero. Here we're

[58:21] not getting any gradient if we sample

[58:23] this action which has reward zero. But

[58:26] um if you take kind of the exact

[58:29] definition of the policy gradient which

[58:31] is the expectation over all the actions

[58:34] in this setting where there's only two

[58:35] actions we can compute that exactly. we

[58:38] can just uh multiply each of these

[58:40] gradients by the probability of sampling

[58:42] that action and that'll be like we'll

[58:45] see the exact number in a couple slides

[58:47] but I think it's like8

[58:50] so the actual policy gradient the

[58:54] expectation over all the actions is8

[58:57] and um but we will only we'll have kind

[59:01] of a very noisy estimate of that where

[59:05] 0.25% 25% of the time we will get a

[59:08] sample of 75 which is much higher than

[59:10] 0.18 and then 75% of the time we'll get

[59:14] zero as an estimate for it. And what we

[59:18] really want is to have both of those

[59:20] estimates that we could sample be much

[59:22] closer to the true value.18.

[59:26] So a baseline actually does this if um

[59:29] so the modification from the past thing

[59:31] is we're just subtracting a baseline

[59:33] from our reward here and otherwise the

[59:36] computation is the same and it works out

[59:39] to be that if we sample um guess A we

[59:43] now have an estimate for the gradient of

[59:46] 375

[59:47] and if we sample B we have an estimate

[59:49] for the gradient of.125.

[59:52] So the expectation uh multiplied by the

[59:55] probability of these actions is still

[59:57] going to be like.18.

[60:00] So it's going to be the same as what we

[60:01] had before. But these individual samples

[60:04] are much closer to that true value

[60:06] because the baseline actually reduced

[60:08] the variance in the samples that we get.

[60:11] We'll have a visualization of this in

[60:13] another slide. But the key thing here is

[60:15] that that expectation does not change.

[60:17] It just kind of like makes the um the

[60:20] variance in the estimator more narrow,

[60:23] which is a good thing because you're

[60:24] going to be drawing these estimates on

[60:27] real data, doing updates, and you don't

[60:29] want your gradient to bounce you around

[60:31] a bunch more than you need to.

[60:35] Okay. Yeah. So, here's just a

[60:37] visualization of this. Um if we have a

[60:40] baseline of zero, here's our gradient

[60:42] estimates. They have this expected

[60:44] value, which is8.

[60:47] And as we drag the baseline, we can see

[60:50] that um we're more we get these

[60:53] estimates for the gradient which um

[60:56] converge

[60:57] on this uh on this true value for the

[61:01] expectation of the gradient.

[61:04] And in all cases we are going to be

[61:06] doing an update which makes the model

[61:08] more correct. We're going to be doing an

[61:10] update which shifts theta to be more

[61:12] positive which is going to increase the

[61:14] probability of a put more reward or put

[61:17] more probability on the thing with

[61:20] reward one. But um we're just going to

[61:23] be doing that more quickly if we have

[61:26] lower variance here in this estimate.

[61:30] And here's a graph that shows that. So

[61:32] um the purple line here is going to be

[61:34] doing draws of um the estimate for the

[61:37] gradient without using the baseline. So

[61:39] no B term just advantages sorry just

[61:42] scales of one or zero. And then the

[61:46] green line is going to be estimates that

[61:49] subtract a baseline just a very simple

[61:51] baseline of 0.5 which was you know which

[61:55] looked like this on this plot. So it's

[61:58] moved them a little bit closer to this

[62:00] true expectation.

[62:03] So uh we'll just like draw some samples

[62:05] and this simulates like doing steps of

[62:08] policy gradient on the exact same

[62:10] example over and over again.

[62:14] So here are sampling in this case we

[62:17] sampled guess A. So we got positive

[62:20] gradient um and we got a much larger

[62:24] gradient if we weren't using a baseline.

[62:26] So we'll be taking a very large step

[62:29] and we sample A again. And this line

[62:33] here is going to be our running average

[62:35] over all of the samples of the gradient

[62:38] so far. So when we sample B, now we have

[62:41] um a sample of the gradient that is

[62:44] below the true value. So we're going to

[62:46] be closer, our running average is going

[62:48] to be closer to that true value. But you

[62:50] can see here we're um we have less

[62:53] variance when we have the baseline. So

[62:55] our running average is already closer to

[62:57] that true value.

[63:00] And this continues like this. We happen

[63:03] to sample a lot of guess B's in a row.

[63:05] We sample guess A, it goes back up

[63:07] again. And it does converge eventually,

[63:10] but we're generally closer to it when

[63:12] we've reduced the variance with this

[63:13] baseline.

[63:15] Any questions about this?

[63:18] Okay. Hopefully this wasn't too in the

[63:20] weeds, but like um baselines have always

[63:22] been a little bit mysterious for me and

[63:24] I wanted to make these visualizations

[63:26] also to convince myself how they work.

[63:29] Um hopefully they're helpful for you

[63:30] too. The intuitions for this very simple

[63:34] uh two armed bandit setting do um

[63:37] transfer generally to these more complex

[63:40] um you know sequential decision-m

[63:42] settings too.

[63:44] Yeah. So um baselines are helpful

[63:47] because they can mark a trajectory as

[63:49] better or worse than expected. And uh if

[63:52] you've chosen a good baseline, a lot of

[63:54] reinforcement learning is about choosing

[63:56] good ways of representing this advantage

[63:58] function. It can help to reduce gradient

[64:00] variance and and stabilize your

[64:02] learning. Um but you have some downsides

[64:05] too and a lot of choices about what you

[64:07] use for the baseline.

[64:10] So with um and I'll skip over this um

[64:13] other than just to say if you are

[64:15] working in a setting that gives you

[64:17] rewards at intermediate time steps

[64:19] rather than just at the end of the

[64:21] trajectory um you'll you'll replace your

[64:24] reward scaling with um the reward to go

[64:28] like the sum over rewards um over future

[64:31] time steps and this will also help to

[64:34] reduce the variance. Um, we'll have this

[64:37] slide here and I we can also talk about

[64:40] this offline if it's something that's

[64:41] relevant to you. Um, but uh it's um how

[64:45] you would handle not having all of your

[64:47] rewards come at the end of the task.

[64:51] [snorts]

[64:52] Okay. So, with the last um bit of time

[64:54] that we have, we'll cover a simplified

[64:56] version of um GRPO um which is uh group

[65:00] relative uh policy optimization I

[65:03] believe. Um, and it's a way of um e of

[65:06] getting this advantage function of

[65:08] estimating a baseline that uses rollouts

[65:12] from the model itself. Um,

[65:17] and this was um this was actually

[65:19] introduced pretty recently. So it was in

[65:21] one of the papers from deepseek that was

[65:23] training reasoning models um with a big

[65:25] focus on efficiency. So a lot of past

[65:28] work on um applying RL to language

[65:32] models required a separate model to

[65:35] predict this baseline. Predicting

[65:36] baselines to you know reduce the

[65:39] variance is very important but was

[65:40] challenging and people were using

[65:42] separate models for it. But DeepSeek was

[65:45] very interested in efficiency um and

[65:47] training models without using much

[65:49] compute and having a separate model

[65:51] takes a lot of compute. So they proposed

[65:55] this approach which gets rid of the

[65:57] separate model and just uses multiple

[65:59] samples from the model itself to

[66:02] estimate the expected value the expected

[66:05] reward under the policy which is really

[66:07] kind of elegant. Um so the idea is that

[66:11] we can sample multiple times from the

[66:13] model for a given instance and then get

[66:16] the reward on each of those. Um and then

[66:19] we can um center that reward by taking

[66:23] the mean of the reward across all of

[66:25] these instances in the group. We get a

[66:28] mean. We um basically use that mean as

[66:32] our baseline. And this makes sense,

[66:35] right? Because you know the baseline is

[66:36] your expected a good baseline is your

[66:40] expected reward under the policy. And a

[66:43] really good estimate of that is just

[66:45] running the policy multiple times and

[66:47] getting the reward taking the mean of

[66:48] those. So we get our centered reward

[66:51] here. And in the original GRPO paper,

[66:55] they're also standardizing this. Um so

[66:58] they're not just shifting it, they're

[67:00] rescaling it. they compute the standard

[67:02] deviation over the rewards in this group

[67:06] of trajectories and then they divide by

[67:09] that standard deviation um to get the

[67:12] advantage functions. Now there's um like

[67:16] actually it seems like dividing by the

[67:19] reward is not necessary and a lot of

[67:22] implementations of uh that that call

[67:25] themselves GRPO actually get rid of this

[67:28] um division by the standard deviation.

[67:31] So it more closely matches the advantage

[67:33] term. Um there's a paper we'll talk

[67:35] about in a few slides called DRGP uh Dr.

[67:39] gpo or done right gpo um which talks

[67:42] more about the motivations for that um

[67:45] but actually in a lot of implementations

[67:47] of gpo they won't divide by the standard

[67:49] deviation they will just subtract the

[67:51] mean um

[67:54] but yeah the gpo update is very simple

[67:57] looks a lot like policy gradient that we

[67:59] defined before but so you have like a

[68:02] task instance which is you know like one

[68:04] RL problem to solve you will generate

[68:08] multiple rollouts from it. So you will

[68:10] solve the same problem multiple times,

[68:12] resetting the environment, um getting a

[68:15] full trajectory by sampling from your

[68:17] agent and um this will typically uh

[68:21] Aorva in his lecture will give some

[68:23] guidance on like choosing values for

[68:25] this group size I believe, but this is

[68:27] typically something like eight. Um and

[68:31] uh you'll get the mean of rewards over

[68:33] those rollouts and you'll get your

[68:35] advantage estimates from that. Um, we'll

[68:38] show two different ways of getting those

[68:39] advantage estimates in another slide,

[68:41] but that gives you a group of rollouts

[68:44] for one trajectory along with advantages

[68:46] for them. If you have room in your GPU

[68:50] uh to fit in more examples, you can also

[68:54] get groups of the same size for

[68:57] additional instances. And you'll be

[69:00] computing group means um only within

[69:03] each example.

[69:05] So this is important right because the

[69:07] value function should just be an

[69:09] estimate of how um it should be an

[69:12] estimate of the reward on this

[69:13] particular example. Um so our advantages

[69:17] should only look at the reward within

[69:19] this example.

[69:21] But you will get an advantage for each

[69:24] trajectory by um scaling the reward for

[69:27] that trajectory using the um the formula

[69:30] that shifts by the mean and maybe

[69:32] divides by the standard deviation of the

[69:35] rewards within that instance.

[69:39] So for policy gradient loss we were just

[69:41] taking a single sample for each um for

[69:44] each instance and then rescaling. But in

[69:48] gpo we are going to be um having

[69:52] multiple instances in our batch and then

[69:54] multiple trajectories within the group

[69:56] for each instance and we'll get an

[69:59] advantage for each of those. We'll use

[70:01] that to rescale our log probabilities

[70:03] before differentiating.

[70:06] Any questions about this? Yeah.

[70:12] >> Um is this unbiased? Yes, because um you

[70:17] your advantage function here um

[70:21] depends on nothing except the prompt and

[70:25] the model. So your baseline function

[70:27] here um which you're subtracting from

[70:30] the reward is just um rollouts from the

[70:35] language model. So this is unbiased.

[70:40] Okay, cool.

[70:45] Yeah. So, um, Dr. GRPO makes two changes

[70:48] to to GRPO. And I should note too, GRPO

[70:51] also, so what what I wrote here is not

[70:54] the loss for GRPO as defined in the

[70:57] paper. Um the loss in the paper has some

[71:00] additional terms which I think Graham

[71:01] will talk more about in his lecture

[71:03] which also like clip the gradient so

[71:06] that you don't take steps too far in one

[71:08] direction or another and also regularize

[71:11] the policy so that you don't uh deviate

[71:14] too much from the policy that you

[71:16] started with. Both of those are

[71:17] additional things that help stabilize

[71:19] training. We're not going to talk about

[71:21] them today. We're just talking about the

[71:23] advantage functions within GRPO. Um but

[71:27] uh yeah, this will help you uh get

[71:29] started on um assignment three when that

[71:32] comes out.

[71:34] Okay, great. So, we're good on time. Um

[71:37] so, uh DRGRPO um makes two changes to

[71:41] GRPO. Um and you will also do these in

[71:44] your assignment. Um and they seem

[71:46] generally helpful to do um

[71:49] because they help avoid some biases

[71:51] within GRPO. And the two changes are

[71:54] just the first one we've talked about a

[71:55] little bit already. It doesn't divide by

[71:57] a standard deviation. It just subtracts

[71:59] the mean of rewards within the group.

[72:03] And um yeah, the motivation for that is

[72:06] that uh uh if you're dividing by the um

[72:11] standard deviation, your advantages are

[72:14] no longer aware of the difficulty of the

[72:16] problem. um because you're sort of like

[72:19] rescaling all ranges of difficulties to

[72:23] be standardized. Um so that can actually

[72:26] be bad. GRPO also um divided by the

[72:30] number of tokens generated which can

[72:32] bias the model towards um uh towards uh

[72:36] long wrong answers and so DRGRPO just

[72:39] divides by a constant which is the max

[72:41] number of tokens that could be

[72:43] generated.

[72:46] Okay. So, same figure that we saw

[72:49] before. How does this actually look when

[72:51] you're implementing it? You have your

[72:53] generated tokens in blue. Uh, you

[72:55] compute an advantage function which is

[72:58] going to um take your reward for this

[73:00] trajectory and just subtract off the

[73:02] mean uh reward from all of your other

[73:05] trajectories.

[73:06] And then you get a per token reward

[73:08] which just normalizes that by a constant

[73:10] C, which is typically the number of

[73:12] tokens that could have been generated.

[73:16] And um you do this for all of the

[73:17] rewards in your all the trajectories in

[73:19] your group which could have varied

[73:21] rewards positive or negative.

[73:24] And the loss looks like this.

[73:27] Any questions about this?

[73:33] Yeah. And um yeah, so just to note again

[73:36] the original paper also has like a a

[73:39] ratio which helps regularize the policy

[73:42] and clipping, but we won't talk about

[73:43] those for now.

[73:46] Okay, so we had a question before about

[73:48] like what if all of your rewards are

[73:50] zero? Um, that's bad because if all of

[73:54] your trajectories fail, that means it's

[73:56] just probably too hard for the current

[73:58] policy and you're not going to get any

[74:00] signal from that even if you have a

[74:03] baseline. Um, you also have a problem if

[74:07] all of your trajectories succeed because

[74:09] they're too easy for the current policy.

[74:12] So like you know if this is binary

[74:13] rewards and um one is the best that we

[74:16] could possibly do um it's bad um and

[74:20] generally it's bad if we don't have any

[74:22] spread um within our examples because

[74:26] then we won't have any signal from the

[74:28] advantage function as estimated by gRPO.

[74:33] So what could we do if every you know

[74:35] sample trajectory fails? We could choose

[74:38] different task instances. We could um

[74:41] inject some some knowledge into the

[74:43] prompt that encourages the model to

[74:45] produce more guided solutions that might

[74:48] be correct. We could add demonstrations.

[74:50] Um there's ways of doing off policy RL

[74:53] that put like uh correct demonstrations

[74:56] into the group. Um or more simply, you

[74:58] could just fine-tune the model first on

[75:00] those correct demonstrations before

[75:02] running RL. Or you could have a more

[75:04] informative reward which um uh

[75:07] encourages the model to make correct

[75:09] intermediate decisions before producing

[75:12] an entire trajectory. That's called

[75:14] reward shaping. So the like giving a

[75:16] model reward for finding the correct

[75:18] file could be an example of that.

[75:23] Um we'll skip this because we'll uh

[75:25] potentially talk more about PO later on.

[75:28] But PO basically just um instead of

[75:31] using the trajectories to compute the

[75:33] advantage function has a separate model

[75:35] which usually shares a backbone with the

[75:38] policy um to predict the the baseline.

[75:44] Okay. So

[75:48] very quickly just comparing the methods

[75:50] that we've seen so far. every method has

[75:53] the agent take actions in the

[75:55] environment and then we'll just um

[75:58] compute a loss uh using those actions

[76:01] produced by the agent. All of these look

[76:03] like selftraining in some way but they

[76:05] just differ in the way that they rewe

[76:08] those generated actions. So restm um we

[76:13] assume that we have binary rewards of

[76:15] zero or one and we just filter to the

[76:18] trajectories which are correct and then

[76:21] do sftt on those. Um reinforce uses the

[76:25] reward of the trajectory to rewe the

[76:28] loss which corresponds to reweing the

[76:31] gradient which we spent a lot of time

[76:33] showing is correct. And then GRPO uh

[76:36] uses these advantage functions where the

[76:38] reward is um is uh shifted and

[76:42] potentially also rescaled by the reward

[76:45] of other trajectories sampled by the

[76:47] model for the same example.

[76:50] And all of these methods help to address

[76:52] the three problems that we had at the

[76:54] very beginning of the lecture. So um

[76:57] task mismatch uh should now be solved

[77:00] because we're now maximizing reward

[77:02] directly. um expected reward directly

[77:05] data mismatch. We can now learn from

[77:07] trajectories that have reward zero as

[77:09] long as we're doing baselines in the

[77:10] appropriate way. And also um the on

[77:13] policy nature of these methods helps

[77:15] with exposure bias because the model's

[77:17] like essentially driving at training

[77:19] time. So it should be learning to

[77:22] recover from its own errors. um it just

[77:25] comes at the expense of you know you

[77:27] have to actually just try stuff in the

[77:29] environment which can be costly can

[77:31] introduce some noise into your gradients

[77:33] and we've covered some ways of trying to

[77:36] make that process more robust but in the

[77:38] next two lectures starting next week

[77:40] we'll we'll talk about some others too

[77:43] okay that's all we
