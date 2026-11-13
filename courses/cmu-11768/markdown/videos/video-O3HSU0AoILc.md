# Lecture 8 recording

[Course index](../../README.md) · [Original source](https://www.youtube.com/watch?v=O3HSU0AoILc&list=PLSN0qpDfUvTM&index=8) · [Raw file](../../raw/videos/O3HSU0AoILc.json)

Retrieved: 2026-11-13T16:48:32.439604+00:00

[00:00] Hi everyone. I'm really glad to uh give

[00:02] the lecture today. Uh it's on super wise

[00:05] fine tuning for agents. So before I

[00:07] start, I want to ask like how many of

[00:09] you have trained agents before? Like

[00:12] please raise your hand.

[00:14] Okay. Um then how many of you have done

[00:17] SFT on agents?

[00:20] Okay, that's actually more than I

[00:21] expected. Um okay so I will be go over

[00:25] these topics today like uh because this

[00:28] is the first lecture on training of

[00:30] agents. So I will first give a overall

[00:32] introduction of like what is training of

[00:35] agents mean and uh and then go over SFT

[00:39] specific topics and also like

[00:42] transitioning into RL which will be the

[00:44] next three lectures.

[00:49] Okay. Um this is a sample trajectory

[00:53] sampled from sui gym. We can see there

[00:56] are different rows in the trajectory.

[01:02] Um so there are a row of system, row of

[01:06] user, row of assistant and observation.

[01:09] Like among these uh we can see there's

[01:12] only three assistant messages in this

[01:14] trajectory.

[01:17] Um

[01:19] so in the overall setting the agent

[01:22] receives an issue which is like given by

[01:24] the user and a couple of tools in a

[01:27] sandbox like for example in this case

[01:29] this is bash and a file edit tool.

[01:34] So in the process the agent produces ss

[01:38] and generates commands and uh reads the

[01:41] observations that those commands return

[01:46] at eventually the repository's own tasks

[01:49] like unit test will determine whether

[01:51] the run succeeded or not.

[01:55] There are several methods of updating

[01:56] the agent that we already discussed

[01:58] about like first context window. Um

[02:00] there are different pros and cons for

[02:03] different methods like for context

[02:04] window it has high fidelity to what

[02:07] already happened but it is costly noisy

[02:11] and does not decide what matters and for

[02:14] external artifacts it'sable

[02:18] editable retrievable and portable so

[02:20] very easy uh reading by human beings but

[02:23] it must be induced selected and

[02:25] maintained throughout the agent

[02:27] trajectory process. So today we'll be

[02:29] talking about updating model weights.

[02:31] This like could incur faster inferences

[02:34] and broader behavior change but like um

[02:37] because we need to train the model the

[02:39] process of training will be slower and

[02:41] more opaque because it's like blackboxed

[02:44] and model specific because it will incur

[02:46] a model specific behavior after

[02:48] training.

[02:50] So we change the weight like once and

[02:53] every call after that gets a new

[02:55] behavior with nothing extra in the

[02:57] prompt.

[02:59] And the first two things we discussed

[03:01] before like update only in seconds and

[03:04] um these like cost of a training run

[03:07] every time you change it

[03:10] and also you cannot open like the

[03:13] weights to see what's going on within a

[03:15] model or move the change to a different

[03:17] model. So this thing like is like

[03:19] onedirectional and opaque

[03:25] like to train a model we need

[03:27] trajectories. Then what does the

[03:29] trajectory teach? First of all how to

[03:31] write a tool call that this harness can

[03:34] actually run.

[03:35] Second like how to keep going when the

[03:38] conversation gets long because the

[03:40] trajectories in learn from like we're

[03:42] supposed to be long

[03:45] and what a tool call result uh what the

[03:47] tool result should look like. So um it

[03:51] waits for one instead of writing one

[03:53] itself

[03:55] and whatever else was in the data that

[03:58] what we use for training like for

[03:59] example extra commentary repeated

[04:02] commands and one way of solving a

[04:04] problem. There are several work

[04:08] to give a more broad overview of what

[04:11] training looks like in frontier labs or

[04:13] like maybe in academia as well. The full

[04:16] this is the full training pipeline. Um

[04:19] we first start with pre-training which

[04:21] is the largest amount of tokens but like

[04:23] this is the stage where uh where

[04:25] language models learn basic next token

[04:28] prediction and then mid-training this is

[04:30] like the second stage but like people

[04:32] have very different definitions for what

[04:34] mid training is uh like mid training is

[04:37] like anything that happens between

[04:38] pre-training and post- training some

[04:40] people even counts like SFT as

[04:43] mid-training nowadays and then but

[04:45] typically SFT is considered as like

[04:48] post-training stage. Um so after mid

[04:51] training we went to SFT. Uh we are like

[04:54] uh this will be covered today and then

[04:56] the next stage will be RL where it will

[04:59] be mostly rollouts and rewards which

[05:01] will be covered like later. But notice

[05:04] that like for most of pre-training mini

[05:06] training and SFT we can find fixed

[05:09] corpuses that we can uh train the model

[05:11] on. But for RL there's typically no

[05:14] fixed corpuses. it's like learned on the

[05:17] model's own like rollouts.

[05:21] So um I will supervise fine-tuning as a

[05:26] cold start before reinforcement

[05:27] learning. Um like cold start means that

[05:30] this checkpoint RL that begins from

[05:34] today's like uh this represent one of

[05:38] the most common pipeline for post

[05:40] training today. This is like um

[05:43] retrieved from Kim K3's report where the

[05:47] model like after pre-training and

[05:49] mid-training it do supervised finetuning

[05:52] first to initialize a baseline agentic

[05:54] capabilities and the next stage is

[05:56] reinforcement learning where models

[05:59] develop domain experts at varying

[06:02] reasoning efforts. The last stage is on

[06:04] policy distillation which consolidate

[06:06] the expert into like one model. Uh this

[06:09] is the last stage and we will cover the

[06:11] next uh the second and the third topic

[06:13] like in later lectures

[06:17] in Kim K3 the model learns to call tools

[06:20] and finish long tasks during SFT u

[06:24] before any RL

[06:26] and uh but some might ask so why don't

[06:30] we just use RL instead of like SFT why

[06:34] do we still do SFT nowadays um So this

[06:39] question deepseek R1 zero has like tried

[06:42] to seek response again like DeepSc R10

[06:45] run RL directly on the base models. Uh

[06:48] so before any SFT happens

[06:53] and they learned their lesson. So like

[06:55] in their very next model uh they put SFT

[06:58] back in R1 starts from a few thousands

[07:00] created examples of SFT because R10's

[07:04] answers just like mix languages and were

[07:06] hard to read without SFT. Uh I think the

[07:09] SFT stage established a high quality

[07:12] coord policy for the subsequent RL

[07:15] stage.

[07:17] This is a comparison of SFT and RL side

[07:21] by side. Um so for supervised

[07:23] fine-tuning it learns from recorded

[07:25] trajectories of agents whoever produced

[07:28] them like it can be produced by stronger

[07:30] models or even themselves and SF learn

[07:34] the signal of a target for every token

[07:37] and it needs data and GPUs to train a

[07:39] model with. It's good at learning tool

[07:41] calls formats and long tasks but is

[07:44] stuck with the demonstrations that are

[07:46] wrong or narrow or used up. For

[07:49] reinforcement learning, it's like learn

[07:51] from its own rollouts scored by a reward

[07:54] at the design for its domain. And uh it

[07:57] learns the signal of one number per roll

[08:01] out per per long roll out. And it needs

[08:04] a live environment, sandboxes and

[08:06] checkable rewards which are some like uh

[08:10] some interesting facts for our people to

[08:12] solve. And uh is good at sharpening what

[08:16] the model already attempts to. uh but

[08:19] the start is two weeks so the reward

[08:21] might sometimes not be like checked

[08:26] um in our lectures we'll be covering

[08:29] reinforcement learning in the next three

[08:30] lectures

[08:33] and I think next topic I'll be going

[08:35] through is like the trajectories as

[08:37] token sequences

[08:40] we all know from language models that

[08:42] there might be chat template that is

[08:44] different for each different language

[08:47] models So for each token sequence um

[08:51] like every boundary above is a template

[08:54] token and uh let's use the coin example

[08:58] queen template example here where um it

[09:02] has some special tokens like uh IM start

[09:07] and then like have special tokens like

[09:09] to call etc

[09:13] and we feed this trajectories through

[09:15] the template and you get one string

[09:17] string of token that represent the whole

[09:19] trajectory. Like for example, it might

[09:21] be going through multiple tool calls

[09:23] like 10 to calls and reaching a final

[09:26] answer, submitting a final trajectory to

[09:29] like some verifier. But like all of

[09:31] these will be represented as one string

[09:33] that will be fit into the training

[09:36] infrastructure to train a model. And the

[09:40] special tokens markers are single

[09:42] special tokens. The rest is what the

[09:45] agent could actually uh write and see in

[09:49] their trajectory that they output.

[09:54] And um different from a language model

[09:58] for agentic SFT, we might not train all

[10:00] of like the output the all of the

[10:03] trajectory. Like for example, here in

[10:06] the trajectory I represented, the gray

[10:08] boxes are the ones that we consider as

[10:10] context. So these will not be in uh

[10:13] calculated towards loss. Uh but the red

[10:15] boxed ones are where we calculate loss

[10:20] like cross entropy loss is what we

[10:22] usually use. But like we have apply a

[10:26] special mask there to assistant tokens

[10:29] that we only train on assistant tokens

[10:30] but not non-assistant tokens which are

[10:33] considered contexts.

[10:35] So the mask is like one bit per token

[10:38] saying whether the token's prediction

[10:40] like counts towards the final training

[10:43] and we want to minimize it because like

[10:46] minimizing it raises the probability of

[10:48] each recorded action like given

[10:50] everything before it has context. This

[10:53] will help increase uh the agent's

[10:56] capability of mimicking what is like

[10:58] already in the trajectory and um

[11:02] observations here are conditioning

[11:04] context but not prediction targets.

[11:07] Yeah.

[11:08] >> Why don't we try to also train with

[11:10] train like observation? It could result.

[11:17] >> Yeah. The question is like why don't we

[11:18] train models also on observations. Uh I

[11:21] would say like training on assistant

[11:23] messages are the general rule of thumb

[11:26] like in agentic SFT because like

[11:29] observations or user context might be

[11:31] given from the user or the environment

[11:34] instead of like given from predicted by

[11:37] the assistant but like I agree that like

[11:39] there are papers um existing that are

[11:43] training on observations and find it to

[11:45] be useful for predicting the world uh

[11:48] stage uh state. So like what I'm

[11:51] discussing here is like uh the general

[11:53] recipe but like you might do ablation

[11:56] studies or even innovations to see what

[11:59] might be the best option for your

[12:01] scenario.

[12:03] >> Just a quick followup about that there

[12:06] one particular paper that did that is

[12:08] called the computational world model

[12:10] that meta published. So they're training

[12:12] the model to like output the results of

[12:15] tool calls which are executing code. Um

[12:19] So they find that it's like pretty

[12:21] helpful on tasks that are aligned with

[12:23] like understanding execution semantics

[12:25] but like it also you could imagine it

[12:27] like takes up some kind of some of the

[12:30] capacity of the model. So yeah like

[12:33] definitely if your model is too small it

[12:35] might hurt its performance on other

[12:36] things. It's kind of like an open

[12:38] question of could it how does it impact

[12:41] kind of the base agentive abilities of

[12:43] the model but it could be like super

[12:45] useful for like world modeling or

[12:46] planning.

[12:48] So it's a little bit more experimental

[12:50] like

[12:52] >> yeah

[12:54] um to explain more on how the mask is

[12:56] built like first we have a render that

[12:59] the template writes the conversation as

[13:01] like one whole string and knows where

[13:03] each assistant span starts and ends with

[13:06] um some special tokens and then like uh

[13:09] tokenize those character positions

[13:11] become like token positions and then

[13:13] these uh we mask like the tokens inside

[13:15] an assistant as one and everything else

[13:18] get the zero because it's not trained

[13:20] on.

[13:22] And the template does the bookkeeping

[13:25] here because like where a system tax

[13:27] starts where it stops

[13:32] like uh by the time training starts the

[13:35] rows uh of system message of users of uh

[13:39] observations are gone. The trainer sees

[13:41] the string and the bits and nothing

[13:43] else.

[13:47] These are some masking controls across

[13:49] some like SFT frameworks. I really like

[13:52] one specific example is like llama

[13:54] factory where you can specify whether

[13:56] you want to train on the prompt as well,

[13:58] whether you want to mask a history uh

[14:00] when calculating loss. Um, so I can show

[14:05] an example of like real usage of llama

[14:08] factory.

[14:28] Um, this is one of the packages I really

[14:31] like to use when doing agentic SFT. You

[14:33] can like generate roll outs or synthetic

[14:36] trajectories and fit into like this

[14:39] infrastructure and identify your model

[14:42] that you want to train with and then

[14:44] just start training.

[14:46] Um you can specify arguments like uh

[14:49] whether you want to train the whole

[14:51] trajectory or you want to cut it off at

[14:53] some position or like we want to train

[14:56] on the context as well.

[15:08] So um

[15:12] there's another special token like the

[15:14] end of turn token where it's like

[15:17] represented differently for different

[15:19] models like for example for queen models

[15:21] it's represented as um this the uh the

[15:25] red token here of I am end and um for

[15:30] other models uh like like for example

[15:35] um probably Kimi Llama like they all

[15:38] have very different end of token end of

[15:40] turn tokens.

[15:43] So if you want to train a model you

[15:45] might need to take a look at what their

[15:46] chat template is so you don't like

[15:49] confuse the model during post training.

[15:54] And uh one thing I observed like when

[15:58] setting up training trajectories are

[16:00] people often times mixed up uh what to

[16:03] include in

[16:05] um calculating loss and what are like

[16:08] context only. Uh for example, the row

[16:11] header of assistant here is now trained

[16:14] for the agent to produce to generate and

[16:17] the model only produces um the red boxes

[16:21] here instead of the gray box and at last

[16:25] the model produces the stop token. So it

[16:28] has to be also be trained inside within

[16:30] the mask and also end of turn um is like

[16:35] actually a combination of multiple

[16:37] events instead of only one because end

[16:39] of turn means that you need to end this

[16:41] message you need to end this tool and

[16:44] also you need to finish the task. Um so

[16:47] like for example in Kimi K3's template

[16:50] here down here um it actually spells

[16:53] them apart with separate tokens for

[16:55] better for the model to better learn how

[16:57] to stop.

[17:02] Another thing that um might be masked

[17:06] out during a training process is

[17:09] reasoning blocks. As we know reasoning

[17:11] blocks are very long blocks and um

[17:14] sometimes people only train on like

[17:16] non-re reasoning parts. So only the like

[17:20] actual tool calls or actual um

[17:23] trajectories.

[17:24] So there are typical several switches

[17:27] that you can try to experiment with.

[17:30] Does the reasoning stays in the context

[17:32] or do they stay in the system message?

[17:34] Uh if they say in the assistant message

[17:36] whether should it be trained on

[17:40] um in the context reason explain the

[17:42] actions that follows the context uh

[17:44] follows the context and if it is trained

[17:47] on it becomes a style that the model

[17:49] itself writes.

[17:52] For example, Neimotron like Neimotra 3

[17:55] ultra keeps like budget truncated

[17:57] reasoning in the context and mask the

[17:59] artificial cut off of the loss. These

[18:03] are like model specific decisions that

[18:05] are very different across different labs

[18:08] or different frontier model development.

[18:13] Um

[18:15] >> yeah sure

[18:16] >> what's the difference between

[18:27] >> uh are you asking for why like reasoning

[18:29] our mask sometimes? Yeah. Uh I'm

[18:31] actually going over this right now like

[18:34] because reason introjectories could be

[18:35] very very long compared to the actual

[18:37] tool call or the actual task completion

[18:40] stage which might confuse the model to

[18:42] produce like only long reasoning but

[18:44] like mixed up with the final outcome. So

[18:48] uh either reasoning sometimes reasoning

[18:50] is mascal sometimes reasoning is train

[18:53] and there is this paper last year of

[18:55] balanced SFT which it aims to balance

[18:57] like reasoning trajectories alongside

[18:59] with the um execution or tool call

[19:03] trajectory. So uh models can learn both.

[19:06] Um

[19:10] so long if we have very long reasoning

[19:12] trajectories it could dominate the loss

[19:14] and the short like tool call or test

[19:17] completion is what we actually most need

[19:20] for like correctness.

[19:24] For example for a task of software

[19:27] engineering we might want the model to

[19:29] reason on what's its next step is but we

[19:32] don't want the model to not actually

[19:34] perform the next step. So um reasoning

[19:37] and action or execution are both

[19:40] important.

[19:42] So in this paper of balance SFT they

[19:45] introduce like rebalancing of uh

[19:47] reasoning and um tool call which like

[19:50] helps more on multi-turn like execution

[19:53] of agents

[19:59] and uh this is a table from MAI so

[20:02] Microsoft MAI model MAI thinking model

[20:06] um they have very different samples

[20:09] across different capability they're

[20:10] aiming to train. Like for example, they

[20:13] categorize STEM capability and coding as

[20:15] like one category and general agency

[20:18] capability as another and general

[20:21] helpfulness and safety as like another.

[20:23] Uh from their sample weight you can see

[20:27] like uh how different they are

[20:30] considering each agent capability uh

[20:33] capabilities importance. Um but like the

[20:36] results are like the token ways are very

[20:38] different from sample ways because

[20:40] different capabilities might incur

[20:43] different lengths of SF trajectories

[20:45] where STEM and coding trajectories are

[20:47] typically very long compared to uh maybe

[20:50] general helpfulness and safety

[20:54] where um in the MAI paper they tend to

[20:59] uh balance the mixture or chose the

[21:00] mixture by counting the number of

[21:02] samples but like stem and coding traces

[21:06] like are so long. So they nearly take

[21:08] all the tokens they're training on

[21:11] and whatever you balance by counting

[21:14] trajectories you should also so this

[21:16] answer is like you should also check

[21:18] whether it's also balanced in tokens or

[21:21] like whether the distribution in tokens

[21:23] is what you preferred.

[21:27] Um also these are some open problems in

[21:30] supervising trajectories where the first

[21:32] one is that we could not find a

[21:35] published experiment that changes the

[21:36] mask for agent SFT and measures what

[21:39] happens but as uh Benu said there's like

[21:42] a recent paper on uh computation world

[21:45] model that like also trained on

[21:47] observations as well. So I think this is

[21:50] one open question that's like worth uh

[21:53] experimenting on and also the careful

[21:57] masking experiments are mostly single

[21:59] term recently uh on instruction tuning

[22:02] instead of on agents. Um and the one

[22:06] case where unmasking the prompt helped

[22:09] like had long prompts and short answers

[22:11] and little um data like in the paper

[22:15] below I attached like agent trajectories

[22:18] are the opposite on all three. So I

[22:20] still think this is an open question

[22:21] that's like worth discussing.

[22:25] Um also choosing the trajectories are

[22:28] important for agent SFT as well.

[22:32] Um so this is a table of like where

[22:36] typical trajectories come from for agent

[22:38] take SFT

[22:39] on the left column like who run the task

[22:43] like where to collect agent SFT

[22:45] trajectory from either is from a strong

[22:48] model that could run it or from the

[22:50] model that like you are training on like

[22:53] uh for example for MAI they use its own

[22:56] reasoning runs or trajectories for SFT

[23:00] and Um yeah, so like depending on the

[23:03] roles um whether you keep everything you

[23:06] got from the uh the generated trajectory

[23:09] or you keep the runs that only passed

[23:11] some threshold or verifier. So if you

[23:15] keep everything that you generated from

[23:17] a strong model that's like called plain

[23:19] distillation. If you keep the runs that

[23:22] pass some sort of verifiers like most of

[23:25] the SFT falls into this category for

[23:27] example Swimmatron

[23:30] by Nvidia and opensource agent all falls

[23:34] into this category. Um and then like if

[23:37] you keep everything that you generated

[23:39] from the model yourself then like this

[23:42] an example is MAI but they felt like

[23:45] little difference um using like FFTD and

[23:50] uh if you keep the runs that pass the

[23:53] verifier with the model of itself then

[23:56] this is like called expert iteration

[23:59] which should be like teased later.

[24:04] So most agent SFD data sits in the like

[24:06] top right box of like keeping only a

[24:09] subset of filter data generated with a

[24:12] strong model and because the stronger

[24:15] model like writes better trajectories

[24:17] than the student could and the tasks own

[24:20] like task might be good as keeping uh

[24:23] only the good trajectories

[24:27] and uh in the bottom row the model makes

[24:29] its own training data. So repeat the

[24:32] loop like you get S for iteration which

[24:34] will be covered later.

[24:37] This is some results from sweet gym

[24:39] which falls into the upper right like

[24:42] you keep the runs that passed with a

[24:44] stronger model that runs it category. uh

[24:48] where it founds that like it achieves

[24:50] much higher resolution rate after um

[24:54] distilling from models like GT40 and

[24:56] Cloud

[24:58] while only keeping the trajectories that

[25:01] pass um the repository tasks.

[25:07] And um in terms of trajectory count and

[25:12] saturation, scaling the number of

[25:14] training trajectories might um result in

[25:18] an increase in the model performance,

[25:20] but like it might saturate at some point

[25:23] and it's much easier for as uh for

[25:27] saturation if you are using a smaller

[25:29] model for training.

[25:32] So

[25:34] in the plot here like the authors of SGM

[25:39] uses the same task set throughout of

[25:42] software engineering and only the number

[25:44] of sample data like changes. So

[25:46] increased through time and accuracy was

[25:49] still rising when the sampling budget

[25:51] run out

[25:53] and they had task to spare where like

[25:56] what they run out of was compute to

[25:58] sample more uh more runs and every point

[26:02] in this plot uses the same task like

[26:04] what happens when you add new task uh I

[26:07] will be discussing like later

[26:12] um but like not all agentic trajectory

[26:14] might be like helpful. There are some

[26:17] desirable behaviors even in successful

[26:20] rollouts. Uh for successful we mean that

[26:22] the final eventual uh task was

[26:25] successfully completed. But there are

[26:27] something intermediate that we might not

[26:29] be able to measure

[26:32] like this might be teaching undesirable

[26:35] behaviors if we use this directly as SFT

[26:39] data.

[26:41] So let's assume that every run passed

[26:44] its like unit test or like the

[26:46] repositories tests. But look at how like

[26:50] for example one edited and uh the red

[26:52] box there like one edited and rerun test

[26:56] in a loop for most of its turns and

[26:59] another left print statements in the

[27:01] final batch. So although the final

[27:03] answer is wrong but this all might still

[27:05] teach the model some wrong behaviors um

[27:08] that it should not learn from SFT

[27:12] and the loss copies like every action no

[27:16] matter like whether it's good or not. So

[27:18] train on these runs and the model learns

[27:20] the best together with the eventual fix.

[27:26] There are like some filters for uh what

[27:29] counts as good SFT data like one very

[27:33] simple example is like filtering real by

[27:36] uh by length like length of the

[27:38] trajectory u for example in a trajectory

[27:41] with uh less than let's say five turns

[27:46] it's probably likely that it's not very

[27:49] good trajectories because like if it's

[27:52] short there are like different

[27:55] Um you you can say different things

[27:57] about like short trajectories but either

[27:59] is like short because it solve the task

[28:01] correctly like at one try and then it's

[28:05] difficult for agent to learn error

[28:08] recovery abilities uh or it might just

[28:11] like the trajectory is incorrect itself.

[28:14] So it's like being very short or the

[28:16] agent encounter like some errors when

[28:18] generating the trajectory which makes us

[28:20] very short. So like filtering by

[28:23] trajectory lens is one of the useful

[28:25] approaches that people do today. Um this

[28:28] is like uh this ablation study is

[28:30] performed by the paper open s agent.

[28:36] So uh one of their conclusion is that

[28:39] the best filter here is just count the

[28:41] number of turns of agents and drops

[28:44] every run that's shorter than five.

[28:47] And turn count says like how much work a

[28:50] run took uh but not whether the work was

[28:53] any was good.

[28:56] And uh um in this case a four turn clean

[28:59] fix might got dropped um and a 14 turn

[29:03] like messy trajectory might still get

[29:06] kept but on average it still helped.

[29:10] Another thing that's important for SFT

[29:13] is like whether you can choose the best

[29:15] teacher like the model itself being the

[29:18] best model does not mean that that it

[29:20] could be a best teacher. Um for the open

[29:23] source agent paper they evaluated

[29:26] several agents on like several

[29:28] benchmarks and they found that the best

[29:31] agent evaluated at that time which was

[29:33] GPD 5.3 codeex is actually the worst

[29:37] teacher among all of these uh models.

[29:41] You can see that it resulted in like

[29:44] less gain compared to other models or

[29:46] even like some decrease in performances

[29:49] after distilling from 255.3 codeex.

[29:53] So if you want to distill from a

[29:56] stronger model or if you want to

[29:57] generate trajectories from a teacher

[29:59] model uh you might need to choose your

[30:01] teacher model wisely.

[30:05] >> Yeah.

[30:06] >> Teach on calls mainly how Is this

[30:10] possible? So the codeex produces correct

[30:12] tool calls but they are the least

[30:15] efficient for training other models.

[30:19] Is there like a reasoning behind it? How

[30:22] could that be? Um there might be various

[30:25] reasons behind it like for example um

[30:29] GPT 5.3 codeex is good at training good

[30:32] at um solving the task itself but like

[30:36] the generated trajectory might not work

[30:38] for the student model that much like

[30:41] because the thinking mode might be very

[30:43] different or the methods of solving the

[30:46] task might be very different. Um so yeah

[30:50] that's one of the explanations. Um also

[30:54] like leaderboard rank only told like

[30:57] whether um whether the models to run

[31:01] things here and you should like try more

[31:04] teachers and keeping the better student

[31:06] that is cheap like by comparison

[31:16] also for SFT ch like wisely choosing the

[31:20] task sources are important. There are

[31:22] just so many asset data assets out

[31:24] there. Um but not probably not all of

[31:27] them could work for the task you are

[31:29] looking to train on. Um still done by

[31:32] open source agent but like they perform

[31:35] some abolition studies on how much like

[31:38] each different task source of agent

[31:40] trajectories could contribute to

[31:43] different benchmarks. Like for example,

[31:45] Sweet Smith contributed the most to

[31:47] Sweetbench verified but it contribute

[31:49] less to terminal bench.

[31:54] And the choice of task source could

[31:57] change the results the most like change

[31:58] the results of training your model the

[32:00] most.

[32:04] Also different sources might help

[32:06] different benchmarks. So like you should

[32:07] spend your effort here before tuning

[32:10] anything else. So you should try uh

[32:12] which task might works out for your

[32:16] for your particular benchmark and then

[32:18] distill like maybe train on that

[32:20] specific data set instead of training on

[32:23] all you can get.

[32:26] And one of their conclusion or empirical

[32:29] conclusion is that it's best for you to

[32:31] mix like four to eight sources of data

[32:34] sets and because going wider than that

[32:37] might not actually help you for your

[32:39] particular benchmark.

[32:45] Um we might think that scaling up just

[32:49] simply could improve agentic

[32:51] performances on benchmarks. But like um

[32:54] empirical evidence shows the contrary.

[32:57] Like if you only set up sample the same

[33:00] rowouts from the same distribution then

[33:03] performance at might actually drop or be

[33:05] saturated over time as you increase the

[33:08] number of rowouts. But on the other

[33:10] hand, if like you increase the

[33:12] distribution, for example, you add more

[33:15] data through synthetic augmentation,

[33:17] then like um the accuracy might still go

[33:21] up as you add more examples.

[33:25] So as you can see from the three um

[33:28] plots here u both the blue curve

[33:30] represents synthetic augmentation uh

[33:33] with different distribution of the data

[33:35] where the red curve represent up

[33:38] sampling rollouts within the same

[33:40] distribution. Both curves are from the

[33:42] same like 10k data set and differ only

[33:45] in where the extra data come from like

[33:47] whether the extra data distribution is

[33:49] the same with the prior data.

[33:54] Um so the the pink curve adds more runs

[33:57] of the same task and it flattens out

[34:00] through time and the blue curves add new

[34:02] task but it keeps climbing.

[34:07] Um I also want to have a short

[34:10] discussion like let's assume that we

[34:13] have three runs of the same task and you

[34:16] are deciding uh like which ones to use

[34:19] for the training set. Let's say option A

[34:22] where you have a short run that solved

[34:24] the issue in four turns and option B a

[34:27] long long run that made a wrong edit and

[34:30] so this test failed and recovered and

[34:33] option C a run that solved the issue

[34:36] after 11 attempts um that changed

[34:39] nothing.

[34:41] Which of these would you keep in your

[34:43] agent training trajectories?

[34:46] And for the ones that you keep, which

[34:48] actions um should carry the loss and

[34:52] which of your answer would the minimum

[34:55] term computer gets wrong?

[34:59] Any any thoughts?

[35:03] probably the B because we're training

[35:05] only on two columns which means that the

[35:09] context of the test doesn't really

[35:11] matter and the fact that you will able

[35:13] to solve the problem for turns is not as

[35:15] valuable as being able to work on long

[35:17] trajectories observing the tests and

[35:20] recovering and getting the results on

[35:22] like a harder configuration even though

[35:24] it's

[35:27] >> yeah I I think that makes sense

[35:30] um but what we would think could be the

[35:33] potential disadvantage of choosing B

[35:38] >> more data, more computer training

[35:41] and then the model gets smaller goals

[35:44] and like excessive doing excessive goals

[35:47] like

[35:49] >> yeah uh other than that there's also a

[35:51] probability of just learning the wrong

[35:53] edit and not being able to learn the

[35:55] recovery ability. So like there's both

[35:58] sides of keeping this data but like so

[36:01] it will improve the agents like error

[36:04] recovery ability but it might also uh

[36:07] incur wrong behaviors for agents.

[36:11] Yeah.

[36:29] Um any any other answers?

[36:35] >> Yeah, go ahead.

[36:39] >> Uh and what's your reasoning?

[36:42] So like

[36:44] behavior rather than going through

[36:47] that.

[36:50] >> Yeah. But uh on the other hand if like

[36:53] for example it's um first try results in

[36:58] like on the one hand like uh it's a

[37:01] right behavior or the right results from

[37:04] the start. But like on the other hand,

[37:06] if you encounter like a wrong behavior

[37:08] at the first turn, it might not be able

[37:10] to learn like how to recover from it. So

[37:13] like um I would say the best answer is

[37:15] to incorporate both A and B. Um and like

[37:20] so you want to increase or increase

[37:23] number of data that like could cover the

[37:25] most useful abilities towards your

[37:28] benchmark.

[37:31] Um

[37:33] for the next section here I will talk

[37:36] about my own work uh with um with

[37:40] professor Graham Yubik. This is like uh

[37:43] on developing a standardized format for

[37:46] agentic SFT.

[37:50] The paper is called Asian data protocol

[37:52] where like this is motivated by each

[37:55] data set was built each uh there are a

[37:58] lot of agentic SFT data out there but

[38:01] like each of them was built by a

[38:03] different group a different lab like in

[38:05] its own format towards a different

[38:06] target audience. Um like for example for

[38:10] web data sets some might be used HTML

[38:14] for uh observations but my others might

[38:17] be using accessibility tree structures.

[38:19] So uh they are very different in terms

[38:21] of the formatting and tool calls.

[38:25] So for example, if I want to train on

[38:28] both um go browse and mine to web where

[38:32] go browse uses accessibility tree

[38:34] structures for web observations and mind

[38:37] to web uses HTMLs for understanding the

[38:41] web content then it will be difficult

[38:43] for me to incorporate both of them to

[38:46] combine them together because um they

[38:49] have different format and to train on

[38:51] them together we need to write a

[38:52] customized converter from each of them

[38:55] to my specified agent format. So let's

[38:58] say I want to train um open hands agent

[39:01] on both go browse and mine to web. I

[39:04] need to write a converter from go browse

[39:06] to open hands and then mine to web to

[39:08] open hands. So that's like a lot of

[39:10] engineering work.

[39:13] Um so in our paper we represent like a

[39:17] trae we represent a trajectory that was

[39:20] like in very different formats into a

[39:22] standardized and a unique format that

[39:25] could represent like a variety of

[39:27] different agentic tasks

[39:30] where we covered uh like like where you

[39:33] read like each once and convert it to

[39:36] our standardized format and then convert

[39:38] our standardized format to your

[39:40] specified agentic format. So you don't

[39:43] need to write custom converters or uh to

[39:46] be able to use multiple data sets for

[39:48] training.

[39:51] Like for example for the web data sets

[39:54] we just talked about before. Um we keep

[39:58] the HTML and accessibility tree

[40:01] structures in our data structures

[40:03] instead of only picking one. But like

[40:05] you can still pick what you want and

[40:07] convert to whatever format you want like

[40:09] downstream. Uh when you perform agentic

[40:12] training

[40:14] um if like using our standardized format

[40:18] each assets only need to convert itself

[40:20] into our standardized format for once

[40:22] and then convert our standardized format

[40:25] once to your specified agentic format

[40:28] once. So this will reduce the

[40:30] computational overhead.

[40:36] And once the data is in one format um

[40:39] you still need to write it to your agent

[40:42] format. So if I want to train open hands

[40:44] I need to convert a agent uh agent data

[40:47] protocol format into open hands format

[40:50] and uh that's because like different

[40:53] agent takes different actions. So the

[40:56] same trajectory comes out to look

[40:58] different uh for each agent.

[41:01] This is also where you set the system

[41:03] prompt and decide what to do when the

[41:05] context get long.

[41:09] And then you want to check the result

[41:10] like do those who call pars and does

[41:14] each call come from a come with a s a

[41:16] function s and does the conversation end

[41:19] the way it should be.

[41:23] Um this is a analysis that we did

[41:27] analyzing whether we want to train on um

[41:30] diverse data instead of only one task

[41:33] specific data. So like previously with

[41:36] open source Asian that they disc they

[41:38] examined whether um training on each

[41:41] task could improve the performance on

[41:43] different benchmarks but like that's

[41:45] only training one on one of the data

[41:47] sets. So they only examine the

[41:50] effectiveness of training on um each

[41:53] task source. Um but like here we

[41:56] examined whether training on multiple

[41:58] different sources could result in better

[42:00] performance than training on a single

[42:02] source. So we discovered that for almost

[42:06] every different agent task agent

[42:09] benchmark training on multiple different

[42:11] sources will result in higher

[42:12] performance compared to only training on

[42:15] a single source. So improving the

[42:17] diversity of data could help a lot in

[42:20] agent take evaluation.

[42:24] So we control this study using the same

[42:26] harness, the same model and the same

[42:28] evaluation format. Only the training

[42:31] mixture change by incorporating a more

[42:34] diverse set of data.

[42:38] Yeah. And training on the mixture beat

[42:40] the matching single domain set. So uh

[42:43] even on the domain's own benchmark

[42:47] and next I'll be talking about actually

[42:50] running the training pipeline. These are

[42:53] some real supervised fine tuning

[42:55] configurations from the wild. Like for

[42:57] example for Neatron 3 ultra they packed

[43:01] uh 294 case u tokens into sequences with

[43:06] uh 64 batch and their learning rate

[43:10] decays like throughout time. for MEI

[43:14] self distillation they pack like 128K

[43:18] and with like a very large batch and a

[43:21] learning rate um that also decays

[43:24] through time but like uh was what might

[43:27] different that is that like they did a

[43:29] warm-up before starting the full SFT and

[43:33] for a recently released model K2 Horizon

[43:36] they were using 512K

[43:39] um sequences with like three different

[43:42] faces is they haven't released their

[43:43] specific uh numbers yet um for SFD

[43:46] configurations but like um they said

[43:49] that like their learning rate decayed on

[43:51] like high quality subsets

[43:55] >> this is not parameter efficient piping

[43:57] right this is just like full training on

[43:59] trajectory how would you do pre-training

[44:01] essentially except the data is different

[44:03] >> yes but like uh also for pre-training

[44:07] um I think people don't mask out like

[44:09] non-agentic

[44:11] parts also

[44:16] expert routing during SFT.

[44:19] Uh the frontier models that I discussed

[44:22] in this lectures are mostly mix of

[44:24] experts where the models that the public

[44:27] papers fine-tune are dense.

[44:31] uh find a mixture of expert model on

[44:34] narrow agent data and a few experts take

[44:38] most of the tokens like uh what is shown

[44:41] in the right panel here.

[44:44] We can see that um we have the most

[44:47] tokens dense like at the left and as the

[44:51] number of expert increase the token uh

[44:53] the number of token we use like

[44:55] decreases

[44:59] and MAI is like balancing the routing uh

[45:03] hard during the supervised stage and a

[45:07] thousand times harder than during RL and

[45:10] they raise drop to 15 Like I think

[45:15] reading one or two technical reports

[45:17] from Frontier Labs or um public papers

[45:21] are important before you start doing SFD

[45:24] because they provide a lot of

[45:25] interesting insights that you could use

[45:28] for SFT

[45:33] and um packing whole conversations. So

[45:38] um typically we don't want truncations

[45:41] and splitting because we want the full

[45:44] trajectory but uh in reality like each

[45:47] conversation is assigned to the pack

[45:50] whose like remaining capacity uh it most

[45:53] tightly fits

[45:57] and no conversation is actually splitted

[46:00] or truncated which is like a deliberate

[46:03] choice against hallucination. And this

[46:06] this plot is like adapted from Neotron's

[46:08] technical report.

[46:11] And identical problems are kept out of

[46:14] the same pack and packs are shuffled

[46:16] afterwards for better training utility.

[46:21] Another thing I want to cover here is

[46:24] template drift

[46:26] where the template you train with has to

[46:28] be the template that you serve with to

[46:30] ensure this alignment even down to the

[46:34] whites space. So to have the best

[46:37] utility of your model

[46:39] and um you you render the same

[46:43] trajectory twice like once with a tool

[46:45] message after it and once resolved so

[46:47] you can get two different strings.

[46:50] When the two messages appended a

[46:52] conditional thinking block uh changes

[46:55] the earlier assistant turn and the

[46:57] prefix no longer matches. So these are

[47:01] uh like why it is fatal inside a tuloop.

[47:10] Um yeah and also there are some publicly

[47:14] released training artifacts. For

[47:15] example, K2 Horizon's model card has a

[47:18] stage bystage training table like uh for

[47:22] each stem, each token and sequence

[47:24] length and what each phase like was for.

[47:27] That table is where the number on the

[47:29] configuration slide like came from and

[47:33] um I think K2 Horizon might be a good uh

[47:36] way although I don't think their

[47:37] technical report is officially released

[47:40] yet but like if it's released I would

[47:41] recommend taking a look because like

[47:44] it's um it's like fully open containing

[47:47] all the um details of training all the

[47:50] data of training um even the loss like

[47:53] they incurred during training through

[47:55] weights and biases like ways and biases

[47:57] is a common platform you use to monitor

[48:00] loss during training. So you can look at

[48:02] their actual uh enterprise level models

[48:06] training loss curves and it also ships

[48:09] like intermediate checkpoints at each

[48:11] stage of their training that you can

[48:13] continue training or um post train on

[48:16] their pre-training checkpoints.

[48:20] Also Neatron released the post training

[48:22] checkpoints too like together with the

[48:23] training data and their training recipe.

[48:27] Um I would suggest like reading at least

[48:29] one of these um that could like teach

[48:32] you a lot on enterprise level training

[48:34] uh SFT

[48:38] more practically we want to do we want

[48:41] to do is like we want to know whether

[48:43] actually SFT worked after we train a

[48:46] model or before we train a model. So uh

[48:50] there might be mismatches between

[48:52] training and running uh your experiments

[48:55] on on evaluation benchmarks for example

[48:59] um for what it has learned through like

[49:02] trajectories. It might have the same

[49:04] prefix and perform some edits and then

[49:07] the test passed and then it submits the

[49:10] job to a verifier but like in reality it

[49:13] might incur another different edit than

[49:16] the edit that you are trained on and

[49:18] then the test failed. Um and then now

[49:21] what the agent should do is not in SFD

[49:23] data. So this is like very depend on the

[49:27] agents like uh error recovery ability

[49:30] that we just discussed.

[49:35] So training grades only one action at a

[49:38] time. Um always continuing the recorded

[49:41] run

[49:45] and also um

[49:50] when models are deployed there is no

[49:52] recording and every action the model

[49:54] takes change what it might see next.

[49:57] This is the reason why the loss curve of

[49:59] training is not um like you can use it

[50:02] to monitor whether training is going

[50:04] well but you cannot use it to substitute

[50:06] actual evaluation because like training

[50:09] continues the recording and deployment

[50:11] continues itself.

[50:14] Uh one so as shown in example one

[50:17] different addit here um and it is in in

[50:20] a state no training run ever have

[50:22] visited in that case the low loss

[50:25] promise nothing but uh about what

[50:28] happens there. So you need to um so you

[50:32] need to monitor both training loss and

[50:34] evaluation results.

[50:39] Um speaking of evaluation results like

[50:41] before trusting any number you should

[50:43] check that you can um and a rule of

[50:46] thumb is like you can check that you can

[50:48] over fit 20 examples. Um if the loss

[50:51] will not drop then the bug might be like

[50:54] upstream

[50:58] and then you can evaluate by running the

[51:00] model in a harness and on task with

[51:02] check checkable outcomes

[51:06] and you can read you should read publish

[51:09] numbers carefully. Sometimes they are

[51:11] the best of like several harnesses

[51:13] instead of like the results you can get

[51:15] from a single run on single harness.

[51:18] And you should try to match the split to

[51:20] the claim by keeping all runs of one

[51:23] task on the same site and split by

[51:25] repository if you want to say it

[51:27] generalizes to new ones.

[51:32] Um yeah robustness across harnesses like

[51:35] trajectories collected in one system

[51:37] teach systems conventions along with the

[51:40] task.

[51:41] So for example, if I collect

[51:43] trajectories through a agent open hands

[51:46] that it might not like generalize to

[51:49] cloud code or codeex

[51:52] and collecting across like several

[51:54] harnesses is how existing frontier labs

[51:56] or academia labs avoid training a model

[51:59] that only works for uh works in one

[52:02] harness.

[52:07] Um if you want to train uh like outside

[52:10] the target domain, you should train on

[52:13] one capability and move the others

[52:16] whether or not like you want to measure

[52:18] it. So if I want to have a good software

[52:21] engineering model, I should still

[52:22] probably train reasoning capabilities

[52:24] because these capabilities might uh

[52:27] transfer and also your mixture is the

[52:30] control here and balancing it by

[52:32] examples uh is not bal is not the same

[52:35] as balancing it by tokens. This is a

[52:38] lesson we learned from the MAI um MAI

[52:42] technical report.

[52:44] So evaluate the things you were not

[52:46] trying to improve too instead of like

[52:47] benchmaxing on only one domain that you

[52:50] care about.

[52:52] These are some takeaways from SFT. And

[52:56] now moving towards like what SFT could

[52:58] do to help RL.

[53:01] Um yeah so RL provide I think in my

[53:05] opinion RL provides the most gains where

[53:08] uh when the SFT model is selected with

[53:11] RL in mind. um to view the whole

[53:15] training pipeline. I I think SFT is

[53:18] where you can gain the most agent cap

[53:20] general agentic capabilities from. But

[53:23] for RL, you can gain domain specific or

[53:26] better reasoning through RL. um existing

[53:30] frontier labs like Neimotron or um K2

[53:34] Horizon, they they all find that SFT is

[53:37] where agents could gain models could

[53:40] gain the most general agent uh

[53:43] capabilities. Well, RL is um where you

[53:46] want to train for a specific domain.

[53:50] And um like also um the three key uh

[53:55] takeaways from the table here are all

[53:59] applied to no SFT at all barely at all

[54:02] barely moves the base model. This is a

[54:04] takeaway that we get from deepseek R10

[54:09] and SFT alone stops well short of what

[54:12] the pair reaches. So um

[54:17] the winning recipe starts RL from a

[54:19] checkpoint that was deliberately not

[54:21] trained to its own best score but like

[54:23] train towards like later uh for better

[54:26] later RL. So I view SFT as a prior state

[54:30] that could co-start agency capabilities

[54:34] that is like well served for later RL.

[54:39] Okay. Um that's all my lecture today and

[54:43] um I welcome any questions.

[54:46] [applause]

[54:52] >> Yeah, we have time for questions.

[54:56] >> Yeah,

[54:59] >> I have a question regarding where you

[55:02] said that it comes from.

[55:04] What if there's no

[55:07] >> Would you be able to just briefly repeat

[55:09] the questions from the media?

[55:11] >> Yeah, sure. Um, the question was, uh, we

[55:14] were saying distillation happens when

[55:16] you use a better model to generate

[55:17] trajectories of SFT, but what will

[55:20] happen if there's no better models? Um,

[55:26] okay.

[55:29] So what

[55:33] so what MAI chose here is to distill

[55:36] from itself. uh this is one of the

[55:38] solutions and the other solution is like

[55:41] for example for I think for frontiers

[55:43] lab especially proprietary ones that

[55:45] like lead the um

[55:50] research of uh training training models

[55:53] like for example open AI anthropic

[55:56] um they rely more on gaining agentic

[55:59] capabilities through RL um like SFD is

[56:02] mostly on

[56:04] SFD is mostly like I say a cold start

[56:08] that like where the agents learn general

[56:12] abilities but not improving um that much

[56:15] because like if you are using SFT then

[56:18] it's fundamentally limited by the

[56:20] teacher model's capability. So if you

[56:22] don't have better teacher model then you

[56:24] might need to rely on RL for training.

[56:28] That's that's my take.

[56:33] in the first place before

[56:37] >> um they have a lot of data like

[56:39] >> just use

[56:42] >> yeah there's like a huge amount of

[56:43] trajectories out there

[56:46] >> plus reinforcement learning which will

[56:50] lectures

[56:52] >> so for RL we don't rely on existing

[56:54] trajectories but we rely on the model's

[56:56] own like rules

[57:01] >> does anyone use

[57:04] pipeline anymore to adapt agents to

[57:06] specific tasks like if you want to

[57:09] navigate some complicated service you

[57:12] would have like SFP in a sense you

[57:14] explained now and then some smaller

[57:16] cycle to like fine tune it is that

[57:22] system

[57:23] >> uh I think in general especially for the

[57:26] prop priority model they expect you to

[57:29] use like only like one single model but

[57:32] might be after model XO merging uh but

[57:35] like only one single model will be

[57:37] actually be inferenced at like inference

[57:40] time so I'm not sure about like the

[57:45] proprietary ones but for um a recently

[57:48] released open model K2 horizon they did

[57:50] multiple rounds of um like fine-tuning

[57:54] even after an SFT stage and the RL stage

[57:57] so they did like some recurrent um

[58:00] fine-tuning Even after the general

[58:03] training stage,

[58:22] Uh the question is like whether there is

[58:24] still low rank adaptations. Um I think

[58:28] for

[58:30] labs that with sufficient resources

[58:33] um they prefer full fine-tuning but uh

[58:37] like for myself I've done uh low rank

[58:40] adaptation before for better like

[58:43] efficiency.

[58:52] Yeah. Uh.

[59:02] >> Oh, here.

[59:11] model.

[59:15] >> Um is the question do we want to

[59:17] supervise it on wrong answers?

[59:20] Uh I would say maybe we want to

[59:23] supervise it on wrong intermediate

[59:25] answers but we want we still want the

[59:27] eventual results to be right because

[59:29] that's like like for example if you are

[59:31] using a coding agent to write some code

[59:33] you don't want it to be wrong.

[59:36] >> Yeah. For example like do we only like

[59:39] supervise on the

[59:41] >> Oh.

[59:42] Oh well, I think we still need to

[59:45] supervise on the like wrong edit because

[59:47] that's like how we learn from the past

[59:50] wrong behaviors. So um we supervise both

[59:55] the right results and the recovery

[59:56] process.

[59:59] >> Is there a wrong

[60:04] to the right?

[60:07] Um I think it's typically determined

[60:11] empirically like for example as I

[60:14] mentioned you might want to train on a

[60:16] smaller portion of the data but like

[60:19] maybe with the same distribution or the

[60:21] same task and see whether it works on a

[60:23] smaller scale model um before running

[60:26] anything like larger scale or scale up.

[60:30] Um yeah, most of these are determined

[60:32] empirically. Like for example, why does

[60:34] the MAI people choose to um

[60:40] choose to use 56% of STEM and coding? Uh

[60:44] like they determined empirically this

[60:45] might be the best setting for um their

[60:48] model

[60:51] >> for using like correctness to determine

[60:54] um how much to weight an example.

[60:56] Reinforcement learning actually will do

[60:58] this sort of at the

[61:00] level and um the reinforcement learning

[61:03] because like we'll we'll talk about like

[61:05] the way the gradient is set up in the RL

[61:08] but like basically the more reward the

[61:11] model gets on that example the higher

[61:15] the weight of the gradient on that

[61:17] example will be so if you have like

[61:20] correctness as a signal RL will

[61:22] effectively rewe it from you for you um

[61:25] it does that implicitly at the

[61:27] trajectory level So if the model is like

[61:30] making some mistakes and then recovering

[61:32] from them, it's going to reinforce

[61:34] making those same mistakes again. If you

[61:37] know that they're mistakes and have kind

[61:40] of like a smarter way of, you know,

[61:42] supervising the loss, you might be able

[61:44] to do better, but those sorts of

[61:46] approaches can be a little bit tricky to

[61:48] set up. So the most common thing is to

[61:50] um just uh use the overall reward on the

[61:53] trajectory um and either like filter the

[61:56] trajectories out to just choose the

[61:57] correct ones and do SFT like you said or

[62:01] um in reinforcement learning we can um

[62:04] rely on um the algorithm to effectively

[62:08] and we'll see more about that in a few

[62:10] days

[62:13] but yeah for like choosing kind of just

[62:15] based on like you know the knowledge of

[62:18] you know, this instance is a good fit

[62:21] domainwise for your downstream test.

[62:23] That ends up being a lot more empirical.

[62:26] And there's methods people use to kind

[62:28] of like if you have an evaluation set

[62:31] and you can like compute the loss of

[62:34] your model on that evaluation set, you

[62:36] can use that as some signal to select

[62:38] your data mixture. Um, but it's all just

[62:41] sort of approximate because you're not

[62:43] doing training on that data mixture.

[62:51] Any other questions?

[63:02] It's just the same as

[63:07] >> uh do you mean the objective of

[63:09] training?

[63:20] >> Um that's a great question.

[63:25] Do you have a general answer for that?

[63:27] >> Yeah. Uh like you had said before, you

[63:30] can think of SFT as being just like

[63:33] pre-training except you are you're

[63:36] formatting your data.

[63:37] >> Yeah.

[63:38] >> To you know have kind of like the

[63:40] structured tags that put it into a chat

[63:42] format and you're also applying a mask

[63:44] to the loss. So you're not supervising

[63:46] the model to output like you know the

[63:49] results of tool calls typically

[63:51] >> but the loss function that you're using

[63:53] is the same like cross entropy loss that

[63:56] you're using in pre-training you're just

[63:58] applying it to different data and on um

[64:02] just a subset of the

[64:04] >> yeah that's your question

[64:11] >> sorry what kind of imitation

[64:20] Yeah. Yeah. This is like this is

[64:22] imitation learning with with teacher

[64:24] forcing. So like teacher forcing has

[64:26] kind of a fixed context and doesn't uh

[64:29] sample from the model at training time.

[64:31] Um that's what these SF most of these SF

[64:35] are choosing. Yeah. Yeah. Yeah, we'll

[64:38] we'll talk about ones that s we'll talk

[64:40] more about ones that have the model

[64:42] produce the training data in the next

[64:43] few lectures.

[64:46] >> Yeah, good questions.

[64:56] Well, let's thank you a
