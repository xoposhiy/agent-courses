# Lecture 8 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-08-sft.pdf) · [Raw file](../../raw/slides/lecture-08-sft.pdf)

Retrieved: 2026-11-13T16:45:28.201405+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

1 1 - 7 6 8  ·  A I  AG E N TS  |  T RA I N I N G  1
Supervised Fine-Tuning for Agents

Yueqi Song

Language Technologies Institute

Turning recorded trajectories into weights

1

## Page 2

Today

Weight updates as a capability

Trajectories as token sequences

Choosing the trajectories

One format for many datasets

Running the training

Knowing it worked

Handing off to RL

2

## Page 3

A trajectory as recorded data

system

harness prompt

user

issue text

assistant

thought + bash

observation

test output

assistant

thought + edit

observation

diff
…

assistant

submit

The agent received an issue and a couple of tools in a sandbox: bash and a file editor.

It produced thoughts, commands, and the observations those commands returned.

The repository's own tests decided whether the run succeeded.

Pan et al., 2024 · SWE-Gym, §4.2 ↗
3

### Page links

- [Link 1](../optional-readings/arxiv-2412-21139.md)

## Page 4

Methods of updating the agent

LOCATION
PROS
CONS

Context window

SEP 1

high fidelity to what happened
costly, noisy, does not decide what
matters

External artifacts

SEP 3

inspectable, editable, retrievable,
portable

must be induced, selected, and
maintained

Model weights

THIS LECTURE

faster inference, broad behavior
change

slower updates, opaque, model-
specific

Change the weights once and every call after that gets the new behavior, with nothing extra in the
prompt.

The first two rows update in seconds. This row costs a training run every time you change it.

And you cannot open the weights to see what changed, or move the change to a different model.

4

## Page 5

What the trajectories teach

How to write a tool call this harness can actually run.

How to keep going when the conversation gets long, because the trajectories it learned
from were long.

What a tool result looks like, so it waits for one instead of writing one itself.

And whatever else was in the data: extra commentary, repeated commands, one way of
solving a problem where several would work.

5

## Page 6

The full training pipeline

Pre-training
20T tokens· Nemotron 3 Ultra

Mid-training
1.43T· K2 Horizon

SFT · today
332B· K2 Horizon

RL · Sep 22 →
rollouts + rewards
no fixed corpus

Drawn to token scale: every step down is fewer tokens, each one more heavily curated.

Nemotron 3 Ultra ↗
K2 Horizon · Training Overview ↗
6

### Page links

- [Link 1](../optional-readings/ref-64285efd9c4c.md)
- [Link 2](../optional-readings/ref-1e31be6807c5.md)

## Page 7

Cold start before reinforcement learning

Supervised fine-tuning

initialize baseline
agent capabilities

Reinforcement learning

develop domain experts at

varying reasoning effort

On-policy distillation

consolidate the experts

into one model

"The SFT stage establishes a high-quality cold-start policy for the subsequent RL stage."

"Cold start" is the checkpoint RL begins from. Today's stage is how K3 makes that checkpoint good.

In Kimi K3, the model learns to call tools and finish long tasks during SFT, before any RL.

Some might ask: why not just RL, without SFT? DeepSeek-R1-Zero ran RL directly on the
base model, with no SFT at all.

Their very next model put SFT back in: R1 starts from a few thousand curated examples,
because R1-Zero's answers mixed languages and were hard to read.

Kimi Team, 2026 · Kimi K3, §4.1 ↗
DeepSeek-R1 ↗
7

### Page links

- [Link 1](../optional-readings/arxiv-2501-12948.md)
- [Link 2](../optional-readings/arxiv-2607-24653.md)

## Page 8

SFT and RL, side by side

SUPERVISED FINE-TUNING
REINFORCEMENT LEARNING

learns from
recorded trajectories, whoever produced them
its own rollouts, scored by a reward

signal
a target for every token
one number per rollout

needs
data and GPUs
live environments, sandboxes, a checkable reward

good at
learning tool calls, formats, long tasks
sharpening what the model can already attempt

stuck when
the demonstrations are wrong, narrow, or used up
the start is too weak, or the reward cannot be checked

OpenThoughts-Agent, Table 11 ↗
Kimi K3 ↗
Kimi K2, §3.2 ↗
8

### Page links

- [Link 1](../optional-readings/arxiv-2507-20534.md)
- [Link 2](../optional-readings/arxiv-2606-24855.md)
- [Link 3](../optional-readings/arxiv-2607-24653.md)

## Page 9

The training lectures

TOPIC
WHEN

Supervised fine-tuning
today

Reinforcement learning
Sep 22 · Sep 29 · Oct 1

9

## Page 10

Trajectories as token sequences

10

## Page 11

The chat template applied to the trajectory

system

harness prompt

user

issue text

assistant

thought + bash

observation

test output

assistant

thought + edit

observation

diff
…

assistant

submit

one token sequence · every boundary above is a template token

<|im_start|>tool
↵
3·failed,·41·passed
↵
<|im_end|>
↵
<|im_start|>assistant

↵
The·test·compares·floats.·Fix·it.
↵
<tool_call>
↵
str_replace(...)
↵

</tool_call>
↵
<|im_end|>

“·” = space, “↵” = newline

Feed the trajectory through the template and you get one string of tokens.

The <|…|>  markers are single special tokens. The rest is what the agent wrote and saw.

Transformers · chat templating ↗
Kimi K3 · XTML, §4.1.1 ↗
11

### Page links

- [Link 1](../optional-readings/arxiv-2607-24653.md)
- [Link 2](../optional-readings/ref-709061a06780.md)

## Page 12

Which tokens carry the loss

system

harness prompt

user

issue text

assistant

thought + bash

observation

test output

assistant

thought + edit

observation

diff
…

assistant

submit

loss computed
context only

Cross-entropy over the assistant tokens only

L(θ) = −
​log p
​ x
​ ∣x
​

t : m
​=1
t
∑
θ(
t
<t)

Mask: one bit per token, saying whether that token's prediction counts.

Minimizing it raises the probability of each recorded action, given everything before it.

Observations are conditioning context, not prediction targets.

12

## Page 13

How the mask is built

Render

the template writes the conversation as
one string and notes where each assistant

span starts and ends

→

Tokenize

those character positions become token

positions
→

Mask

tokens inside an assistant span get a 1,

everything else a 0

The template does the bookkeeping as it writes: where assistant text starts, where it
stops.

By the time training starts, the roles are gone. The trainer sees the string and the bits,
nothing else.

Transformers · apply_chat_template ↗
13

### Page links

- [Link 1](../optional-readings/ref-9f89693e6e4e.md)

## Page 14

Masking controls across frameworks

FRAMEWORK
WHAT YOU SET
HOW THE MASK IS PRODUCED

TRL
assistant_only_loss=True
the template marks the assistant spans as
it renders

Axolotl
roles_to_train ,

train_on_eos

finds each turn’s role header in the
rendered string

LLaMA-Factory
train_on_prompt ,

mask_history

tags whole turns as train-or-ignore while
encoding

Same decision in all three. Only TRL puts it in the template.

TRL · SFTTrainer ↗
Axolotl · conversation formats ↗
LLaMA-Factory · data args ↗
14

### Page links

- [Link 1](../optional-readings/ref-cc7ce71c1794.md)
- [Link 2](../optional-readings/ref-7e9a41e772dc.md)
- [Link 3](../optional-readings/ref-b5fa93404333.md)

## Page 15

The end-of-turn token

<|im_start|>assistant
↵
I'll·run·the·failing·test.
↵
<tool_call>
↵

bash(cmd="pytest·-q")
↵
</tool_call>
↵
<|im_end|>
↵

“·” = space, “↵” = newline · red = loss computed, gray = context only

The role header is supplied at inference. It is never a
target.

The model produces the stop token, so it has to be inside the
mask.

"End of turn" is three events, not one: end this message, hand off to a tool, or finish the task. Kimi K3's template spells them apart
with separate tokens:

\[open\]message·role=assistant\[sep\]
\[open\]think\[sep\]
…
\[close\]think\[sep\]

\[open\]response\[sep\]
Use·math.isclose.
\[close\]response\[sep\]
\[end_of_msg\]

"the model may not learn to stop."

TRL · training chat templates ↗
TRL · SFTTrainer source ↗
Kimi K3 · XTML, §F ↗
15

### Page links

- [Link 1](../optional-readings/arxiv-2607-24653.md)
- [Link 2](../optional-readings/ref-09763e84d70f.md)
- [Link 3](../optional-readings/ref-b5fa93404333.md)

## Page 16

Masking the reasoning block

<|im_start|>assistant
↵
<think>
↵
The·assert·compares·floats.
↵
</think>
↵

Use·math.isclose.
↵
<|im_end|>

“·” = space, “↵” = newline · red = loss computed, gray = context only

Two switches, set separately: does the reasoning stay in the context, and does it get
trained on.

In the context, the reasoning explains the action that follows. Trained on, it becomes
the style the model itself writes.

Nemotron keeps budget-truncated reasoning in the context, and masks the artificial
cut-off out of the loss.

NVIDIA, 2026 · Nemotron 3 Ultra, §3.1.1 ↗
16

### Page links

- [Link 1](../optional-readings/ref-1e31be6807c5.md)

## Page 17

Weighting inside the assistant turn

Two components from one paper: SSB is a learned weight
that rebalances reasoning tokens against tool-call tokens in
the loss, and HDR resamples the hard examples.

Long reasoning dominates the loss, and the
short tool call is what you actually need
correct.

Rebalancing helps more on multi-turn than on
single-turn, on both base models.

Hao et al., 2025 · BalanceSFT, Table 5 ↗
17

### Page links

- [Link 1](../optional-readings/arxiv-2505-20192.md)

## Page 18

Samples versus tokens

They chose the mixture by counting examples. The loss is computed per token.

The mixture was balanced by counting examples, but STEM and coding traces run far
longer, so they take nearly all the tokens.

Whatever you balance by counting trajectories, check what it turned into in tokens.

Microsoft AI, 2026 · MAI-Thinking-1, Table 10 ↗
18

### Page links

- [Link 1](../optional-readings/ref-1b4125b5ee25.md)

## Page 19

Open problems in supervising a trajectory

We could not find a published experiment that changes the mask for agent SFT and
measures what happens.

The careful masking experiments are single-turn instruction tuning, not agents.

The one case where unmasking the prompt helped had long prompts, short answers,
and little data. Agent trajectories are the opposite on all three.

At 8B scale this experiment is cheap, and it is sitting there unrun.

Chatterjee et al., 2025 · WIT ↗
Shi et al., 2024 · Instruction Modelling ↗
19

### Page links

- [Link 1](../optional-readings/arxiv-2405-14394.md)
- [Link 2](../optional-readings/arxiv-2507-07817.md)

## Page 20

Choosing the trajectories

20

## Page 21

Where the trajectories come from

WHO RAN THE TASK
YOU KEEP EVERYTHING
YOU KEEP THE RUNS THAT PASSED

a stronger model ran it
plain distillation
SWE-Gym · Nemotron · OT-Agent

the model ran it itself
MAI, on its own reasoning runs
expert iteration · Sep 22

Most agent SFT data sits in the top right box: a stronger model writes better trajectories
than the student could, and the task's own tests make keeping the good ones cheap.

In the bottom row the model makes its own training data. Repeat that loop and you get
expert iteration, which will be covered in future lectures.

21

## Page 22

Distillation from a stronger model

SEP 10  GPT-4o and Claude ran the SWE-Gym tasks; 491 runs passed the repository tests.

A 32B Qwen model was fine-tuned on those 491 runs alone.

Its scores on both SWE-Bench splits rose by more than ten points.

Pan et al., 2024 · SWE-Gym, §4.2 and Table 3 ↗
22

### Page links

- [Link 1](../optional-readings/arxiv-2412-21139.md)

## Page 23

Trajectory count and saturation

Same task set throughout. Only the number of sampled
trajectories changes.

Accuracy was still rising when the sampling
budget ran out.

They had tasks to spare. What they ran out of
was compute to sample more runs.

Every point in this plot uses the same tasks.
What happens when you add new tasks comes
a few slides later.

Pan et al., 2024 · SWE-Gym, §5.2 and Figure 5 ↗
23

### Page links

- [Link 1](../optional-readings/arxiv-2412-21139.md)

## Page 24

Undesirable behaviors in successful rollouts

read, never edited
edit–test loop
print( in the patch

system

harness prompt

user

issue text

assistant

thought + bash

observation

test output

assistant

thought + edit

observation

diff
…

assistant

submit

"would teach undesirable behaviors if used directly as SFT data"

Every run on this slide passed its tests.

But look at how: one edited and re-ran tests in a loop for most of its turns, another left
print statements in the final patch.

The loss copies every action, good or not. Train on these runs and the model learns the
mess together with the fix.

NVIDIA, 2026 · Nemotron 3 Ultra, §3.1.1 ↗
24

### Page links

- [Link 1](../optional-readings/ref-1e31be6807c5.md)

## Page 25

Filtering rollouts by shape

The best filter here just counts turns and drops every run shorter than five.

Turn count says how much work a run took, not whether the work was any good.

A four-turn clean fix gets dropped. A forty-turn mess gets kept. On average it still helped.

Raoof et al., 2026 · OpenThoughts-Agent, Table 7 ↗
25

### Page links

- [Link 1](../optional-readings/arxiv-2606-24855.md)

## Page 26

Choosing the teacher

The paper reports GPT-5.3-Codex was the strongest of these five models on the
benchmarks themselves. Its runs produced the weakest student.

Leaderboard rank told them the wrong thing here. Trying two teachers and keeping the
better student is cheap by comparison.

Raoof et al., 2026 · OpenThoughts-Agent, Table 6 ↗
26

### Page links

- [Link 1](../optional-readings/arxiv-2606-24855.md)

## Page 27

Task sources

The choice of task source changed results the most.

Different sources help different benchmarks, so spend your effort here before tuning
anything else.

Mix the best four to eight sources. Going wider than that did not help them.

Raoof et al., 2026 · OpenThoughts-Agent, Table 2 ↗
27

### Page links

- [Link 1](../optional-readings/arxiv-2606-24855.md)

## Page 28

Scaling the data

Both curves start from the same 10K dataset and differ only in where the extra data
came from.

The pink curve adds more runs of the same tasks, and it flattens out. The blue curve
adds new tasks, and it keeps climbing.

Raoof et al., 2026 · OpenThoughts-Agent, Figure 3 ↗
28

### Page links

- [Link 1](../optional-readings/arxiv-2606-24855.md)

## Page 29

Discussion

A. A short run that solved the issue in four turns.

B. A long run that made a wrong edit, saw the test fail, and recovered.

C. A run that solved the issue after eleven attempts that changed nothing.

Three runs of the same task just came back. You are deciding what goes into the training set.

Which of these do you keep?

For the ones you keep, which actions carry the loss?

Which of your answers would a minimum-turns filter get wrong?

29

## Page 30

One format for many datasets

30

## Page 31

Heterogeneity across agent datasets

Each dataset was built by a different group, in its own format.

For a web page, some save the HTML and others save the accessibility tree.

To train on two of them together, you first write two customized converters.

Song et al., 2026 · Agent Data Protocol, Table 1 ↗
31

### Page links

- [Link 1](../optional-readings/arxiv-2510-24702.md)

## Page 32

One representation for a trajectory

You read each dataset once and rewrite it as typed actions and observations.

For the web page we just saw, keep the HTML and the accessibility tree, instead of
picking one.

Each dataset converts once, each harness once, not once per pair.

Song et al., 2026 · Agent Data Protocol, ICLR oral ↗
32

### Page links

- [Link 1](../optional-readings/arxiv-2510-24702.md)

## Page 33

Harness-specific rendering

Once the data is in one format, you still have to write it back out for the harness you are
training for.

OpenHands, SWE-Agent and AgentLab take different actions, so the same trajectory comes out
looking different in each.

This is also where you set the system prompt and decide what to do when the context gets
long.

Then you check the result: do the tool calls parse, does each call come with a thought, does the
conversation end the way it should.

Song et al., 2026 · Agent Data Protocol, §3.3 ↗
33

### Page links

- [Link 1](../optional-readings/arxiv-2510-24702.md)

## Page 34

Diversity versus task-specific data

Same harness, same model, same evaluation. Only the training mixture changes.
Train on the mixture and you beat the matching single-domain set, even on that domain's own
benchmark.

Song et al., 2026 · Agent Data Protocol, cross-task transfer ↗
34

### Page links

- [Link 1](../optional-readings/arxiv-2510-24702.md)

## Page 35

Running the training

35

## Page 36

Real SFT configurations

SEQUENCE
BATCH
LEARNING RATE

Nemotron 3 Ultra
packed 294,912 then 515,000
64
1.5e-5 → 1e-6

MAI self-distillation
packed 128k
2,048
1.7e-5 → 5.2e-6, 2% warmup

K2 Horizon
512K, three phases
—
decayed on a high-quality subset

Nemotron 3 Ultra, §3.1 ↗
MAI-Thinking-1, §3.1.4 and §3.5 ↗
K2 Horizon model card ↗
36

### Page links

- [Link 1](../optional-readings/ref-64285efd9c4c.md)
- [Link 2](../optional-readings/ref-1b4125b5ee25.md)
- [Link 3](../optional-readings/ref-1e31be6807c5.md)

## Page 37

Expert routing during SFT

broad pre-training mix
narrow agent SFT set

tokens per expert
tokens per expert

The frontier models in this lecture are mixtures of experts. The models the public
papers fine-tune are dense.

Fine-tune an MoE on narrow agent data and a few experts take most of the tokens, like
the right panel.

MAI's fix: balance the routing hard during the supervised stage, a thousand times harder
than during RL, and raise dropout to 0.15.

Microsoft AI, 2026 · MAI-Thinking-1, §3.1.5 ↗
37

### Page links

- [Link 1](../optional-readings/ref-1b4125b5ee25.md)

## Page 38

Packing whole conversations

pack 1
19k run
15k run
11k run
8k run
unused

pack 2
29k run
17k run
7k run
unused

Training runs on fixed-length sequences. Packing fills each one with several conversations, instead of padding most of it away.

Each conversation is assigned to the pack whose remaining capacity it most tightly fits.

No conversation is split or truncated, which is a deliberate choice against hallucination.

Identical prompts are kept out of the same pack, and packs are shuffled afterwards.

NVIDIA, 2026 · Nemotron 3 Ultra, §3.1.2 ↗
38

### Page links

- [Link 1](../optional-readings/ref-1e31be6807c5.md)

## Page 39

Template drift

"The chat template should always match the format the model was trained with."

The template you train with has to be the template you serve with, down to the
whitespace.

Render the same trajectory twice, once with a tool message after it and once without,
and you can get two different strings.

When a tool message is appended, a conditional thinking block changes the earlier
assistant turn, and the prefix no longer matches.

Transformers · writing chat templates ↗
TRL · training chat templates ↗
39

### Page links

- [Link 1](https://huggingface.co/docs/transformers/en/chat_templating_writing)
- [Link 2](../optional-readings/ref-09763e84d70f.md)

## Page 40

Released training artifacts

K2 Horizon's model card has a stage-by-stage training table: steps, tokens, sequence
length, and what each phase was for. That table is where the numbers on the
configurations slide came from.

It also links the Weights & Biases run, so you can look at the actual loss curves, and it
ships intermediate checkpoints for every stage.

Nemotron released the post-trained checkpoints together with the training data and the
recipe.

Reading one of these teaches a lot.

Nemotron 3 Ultra ↗
K2 Horizon ↗
40

### Page links

- [Link 1](../optional-readings/ref-64285efd9c4c.md)
- [Link 2](../optional-readings/ref-1e31be6807c5.md)

## Page 41

Knowing it worked

41

## Page 42

The mismatch between training and running

DEMONSTRATED

ITS OWN RUN

same prefix

issue + first edit

edit A

the recorded one

tests pass

expected observation

submit

task complete

edit B

plausible, different

tests fail

unexpected observation

now what

not in the data

Training grades one action at a time, always continuing the recorded run.

Deployed, there is no recording. Every action the model takes changes what it sees next.

One different edit and it is in a state no training run ever visited. Low loss promised
nothing about what happens there.

Ross et al., 2011 · DAgger ↗
42

### Page links

- [Link 1](../optional-readings/ref-93002f771ba6-pdf.md)

## Page 43

Evaluation in the target harness

Before trusting any number, check that you can overfit twenty examples. If the loss will
not drop, the bug is upstream.

Then evaluate by running the model in a harness, on tasks with checkable outcomes.

Read published numbers carefully. Sometimes they are the best of several harnesses.

Match the split to the claim. Keep all runs of one task on the same side, and split by
repository if you want to say it generalizes to new ones.

OpenThoughts-Agent, Table 1 ↗
SWE-Gym, §5.2 ↗
43

### Page links

- [Link 1](../optional-readings/arxiv-2412-21139.md)
- [Link 2](../optional-readings/arxiv-2606-24855.md)

## Page 44

Robustness across harnesses

Trajectories collected in one system teach that system's conventions along with the
task.

Collecting across several harnesses is how labs avoid training a model that only works
in one.

NVIDIA, 2026 · Nemotron 3 Ultra, §3.1.1 ↗
44

### Page links

- [Link 1](../optional-readings/ref-1e31be6807c5.md)

## Page 45

Regressions outside the target domain

Train on one capability and you move the others, whether or not you measure it.

Your mixture is the control here, and balancing it by examples is not the same as
balancing it by tokens.

So evaluate the things you were not trying to improve, too.

Microsoft AI, 2026 · MAI-Thinking-1, §3.5 ↗
45

### Page links

- [Link 1](../optional-readings/ref-1b4125b5ee25.md)

## Page 46

Handing off to RL

46

## Page 47

How much SFT before RL

"RL provides the most gains when the SFT model is selected with RL in mind."

RL applied to no SFT at all barely moves the base model.

SFT alone stops well short of what the pair reaches.

The winning recipe starts RL from a checkpoint that was deliberately not trained to its
own best score.

OpenThoughts-Agent, Table 11 ↗
MAI-Thinking-1, §3.1.4 ↗
47

### Page links

- [Link 1](../optional-readings/arxiv-2606-24855.md)
- [Link 2](../optional-readings/ref-1b4125b5ee25.md)

## Page 48

Questions
Next class · Training 2: Reinforcement Learning Basics

48

## Page 49

Backup · Exact masking flags

FRAMEWORK
FLAG
BEHAVIOR

TRL
assistant_only_loss=True
needs {% generation %}  markers; known

families get patched templates

TRL
completion_only_loss
prompt–completion datasets; on by default
there

Axolotl
roles_to_train:

\["assistant"\]

default; loss on the listed roles only

Axolotl
train_on_eos: turn
the EOS of each trained turn is in the loss

LLaMA-Factory
train_on_prompt: false
default; prompt tokens masked

LLaMA-Factory
mask_history: true
last turn only; truncation keeps the final
turn

49
