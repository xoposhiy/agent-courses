# Lecture 11: What Data Do Agents Need?

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture11.pdf) · [Raw file](../../raw/slides/lecture11.pdf)

Retrieved: 2026-11-13T16:30:29.346245+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

CS329Z: Engineering AI Agents

CS 329Z:Engineering AI Agents
What Data Do Agents Need?

Diyi Yang, Michael Ryan, John Yang

## Page 2

CS329Z: Engineering AI Agents

Roadmap

## Page 3

CS329Z: Engineering AI Agents

Roadmap

What Data Do Agents Need?

tl;dr: LMs have gotten dramatically better at agent tasks in the past 2 years, nearly 
entirely thanks to the massive inﬂux of creating “agentic” data at scale. In this 
lecture, we’ll talk about what data is “agentic”, how it’s minted, and important tips 
toward sanitizing your data properly for training use.

●
What your data accidentally 
teaches \[15 min\]

●
Motivation \[10 min\]
●
Kinds of Agent Data \[10 min\]
●
Where agent data comes from \[45 min\]

## Page 4

CS329Z: Engineering AI Agents

Motivation

## Page 5

CS329Z: Engineering AI Agents

Motivation

Last lecture, we talked about optimizing the system around an LM. This lecture, 
we’ll be talking about “optimizing” the LM itself.

Last Lecture: Weights stay frozen, tune

components surrounding model

Today: Make the LM itself a better agent,

data is the main lever for it!

## Page 6

CS329Z: Engineering AI Agents

Motivation

Reminder on why data is extremely important. Arguably the key diﬀerentiator today.

From Percy’s CS 336 Lecture 13 (Data) Slides

Popular post 
by James 
Betker, a 
researcher at 
OpenAI.

⬆ Llama 3 report’s section about pre-training 
data. ⬇ No data release despite OSS model

## Page 7

CS329Z: Engineering AI Agents

Motivation

Today’s landscape makes it very clear: frontier LM companies pay a ton for data.

## Page 8

CS329Z: Engineering AI Agents

Motivation

A reminder on the training phases of an LM, and where “agent data” lands.

“Agent data” typically refers to conversations and 
environments. Conversations serve as demonstrations, 
environments are places to practice.

## Page 9

CS329Z: Engineering AI Agents

Motivation

Web crawls show a lot of text. Agents need environments to actually interact.

What’s on the internet
What’s possible in an environment

Q: TypeError in parse_date(). I’m 
running into an issue where I’m calling 
the function and passing in a string, 
which should be a legitimate data type?

A: You’re passing a string. Wrap it in 
strptime() first and it should work.

$ grep -rn parse_date src/
utils.py:42: def parse_date(s):
$ pytest tests/
FAILED: TypeError
$ edit src/utils.py
$ pytest tests/
1 passed

Web crawls show a lot of text. Agents need environments to actually interact.

## Page 10

CS329Z: Engineering AI Agents

Motivation

Much evidence that given same base model, post-train data makes big diﬀerence.

From OT-Agent 
paper (Raoof 
2026), given same 
budget of SFT 
traces (x-axis), 
selecting the most 
eﬀective subset 
leads to better 
performance 
across multiple 
benchmarks.

### Page links

- [Link 1](https://arxiv.org/abs/2606.24855)

## Page 11

CS329Z: Engineering AI Agents

Motivation

Today’s lecture will cover the basics of agent data - what it looks like, where it 
comes from. Next lecture, we’ll talk about how to select which traces/envs to use.

1
Why does 
Agent Data

matter?

2
Two Types
of Agent Data:

Traces, Envs

3
Where does

Agent Data 
come from?

4
What Agent 
Data teaches

on accident

Next Time
Which Agent

Data should 
be trained on?

✅

## Page 12

CS329Z: Engineering AI Agents

Types of Agent Data

## Page 13

CS329Z: Engineering AI Agents

Types of Agent Data

Karpathy talks about “conversations” and “environments”. What do they look like?

🎞 Trajectory

A recording of an agent solving a task 
(issue text + sandbox).

Then perform supervised ﬁne-tuning 
(SFT) on traces. LM imitates behavior.

📦 Environment

A task (issue text + sandbox) along with 
a mechanism for verifying success.

Then perform reinforcement learning 
(RL) against tasks. LM practices ReAct.

Think
Act
Obs
Act
Obs
Submit
Task
Sandbox
Veriﬁer

## Page 14

CS329Z: Engineering AI Agents

Types of Agent Data

Anatomy of a Trajectory; the model’s training objective predicts the actions.

Learned: Agents’ 
thoughts and actions

Context only: System 
prompt, task, and tool 
outputs

The format (e.g., tool 
calls, ReAct text, code 
actions) is dictated by 
system around LM.

## Page 15

CS329Z: Engineering AI Agents

Types of Agent Data

Anatomy of a Post-training Task / Environment

You’ll see this ﬁgure again when we discuss agent benchmarks in 2 weeks! Trajectories can 
be generated by running LMs on an environment and recording its problem solving as a trace

Sandbox / Environment

## Page 16

CS329Z: Engineering AI Agents

Types of Agent Data

For trajectories / SFT, the reward comes from predicting the correct action. Where 
does the reward for environments / RL come from?

Reliable, but narrow
General, but fuzzy

Code Tests
Run a suite of unit

tests that check 
deterministically

Rubrics
Have an LM/human

check whether a 
checklist is satisﬁed

LM-as-a-Judge
Model takes a look 
at 2+ solutions and

ranks the outcome

Human Preference

Run live evaluation

where people 
choose best answer

We’ll talk about reward types and LM-as-a-judge thoroughly in 3 lectures!

## Page 17

CS329Z: Engineering AI Agents

Types of Agent Data

How do we train on trajectories vs. environments?

📦 Environment
Many Rollouts

Curate ⇒ SFT Data
Imitate what’s kept

Score ⇒ RL Update
Weight attempt by reward

## Page 18

CS329Z: Engineering AI Agents

How much data at each stage?

Labs usually don’t disclose it. Deepseek v3 
(2 yrs ago), v3.2 (1 yr) is a data point.

14.8T Pretraining tokens (v3)

1.5M SFT Examples (v3)

85k RL Task Prompts (v3.2)

v3 Compute Comparison
(Measured in H800 GPU Hours)

2,664k

119k

5k

Pre
Mid
Post

1 year later, V3.2: Post-train 
budget exceeds 10% of pre-

## Page 19

CS329Z: Engineering AI Agents

Where does Agent Data come from?

## Page 20

CS329Z: Engineering AI Agents

Where does Agent Data come from?

In this section, we’ll cover strategies for collecting large groups of environments, 
tasks, and trajectories.

For each strategy, consider the cost, realism, and scalability of the approach. 
Consider why \[or why not\] the approach works well for a given domain.

1
Human
Demo’s

2
Mined from

web, world

3
Synthesize

Tasks

4
Synthesize
Trajectories

5
Simulated 
Users, Envs

## Page 21

CS329Z: Engineering AI Agents

Human Demonstrations

## Page 22

CS329Z: Engineering AI Agents

Human Demonstrations

People do the task while a recorder captures every step.

1

Deﬁne

Write task goals 
on real sites or 
apps

2

Perform

An annotator 
completes each 
task by hand

3

Record

Log every 
screen state + 
click, keystroke

4

Filter

Drop failed or 
noisy runs and 
verify success

5

Package

Store as task + 
step pairs, 
optionally with 
reasoning

Output
Trajectory = task  →  (screen₁, action₁)  →  (screen₂, action₂)  →  …  →  (screenₙ, actionₙ)

## Page 23

CS329Z: Engineering AI Agents

Human Demonstrations

Mind2Web \[Web\]: Crowdworkers recorded action sequences for 2,000+ 
open-ended tasks on 137 real websites spanning 31 domains.

Deng, Xiang, et al. "Mind2web: Towards a generalist agent for the web." NeurIPS 2023

## Page 24

CS329Z: Engineering AI Agents

Human Demonstrations

Mind2Web \[Web\]: Crowdworkers recorded action sequences for 2,000+ 
open-ended tasks on 137 real websites spanning 31 domains.

## Page 25

CS329Z: Engineering AI Agents

Human Demonstrations

Mind2Web \[Web\]: Crowdworkers recorded action sequences for 2,000+ 
open-ended tasks on 137 real websites spanning 31 domains.

## Page 26

CS329Z: Engineering AI Agents

Human Demonstrations

OpenCUA \[CUA\]: An app on annotators’ own computers records screen video, 
mouse, and keyboard, yielding 22.6K tasks across Windows, macOS, and Ubuntu.

Wang, Xinyuan, et al. "Opencua: Open foundations for computer-use agents." NeurIPS 2026

## Page 27

CS329Z: Engineering AI Agents

Human Demonstrations

OpenCUA \[CUA\]: An app on annotators’ own computers records screen video, 
mouse, and keyboard, yielding 22.6K tasks across Windows, macOS, and Ubuntu.

## Page 28

CS329Z: Engineering AI Agents

Human Demonstrations

Case Study: Mind2Web versus OpenCUA. What’s the diﬀerence?

Mind2Web
OpenCUA

Who records
Crowdworkers in a recording tool
Annotators on their own computers

Environment
Web only: 137 sites, 31 domains
Desktop: 3 OSes, 200+ apps, sites

Recorded
Actions + page snapshot per step
Video, inputs, accessibility tree

Tasks
2,350
22.6K

Reasoning
None; raw actions only
Synthetic, added for each step

## Page 29

CS329Z: Engineering AI Agents

Mined from the web + world

## Page 30

CS329Z: Engineering AI Agents

Mined from the web + world

Convert online artifacts (issue reports, tutorials) into trajectories, environments.

RAW SOURCES
CONVERSION
OUTPUT

Code history
GitHub issues and the PRs 
that ﬁxed them

Written tutorials
How-to guides turned into 
step lists

Videos
Screen recordings and 
gameplay footage

1

Extract the task
Issue, guide title, or video goal 
becomes the instruction

2

Recover the actions
Parse diﬀs or steps; label video 
with an inverse dynamics model

3

Replay and verify
Rerun in a live environment; keep 
runs that succeed

Trajectory

Task instruction

Observation and 
action steps

Pass or fail signal

## Page 31

CS329Z: Engineering AI Agents

Mined from the web + world

SWE-rebench \[Code\]: A fully automated pipeline mined 21,336 veriﬁable tasks from 
3,468 GitHub repositories, including environment setup and test validation.

Badertdinov, Ibragim, et al. "Swe-rebench: An automated pipeline for task collection and

decontaminated evaluation of software engineering agents." (NeurIPS 2026)

SWE-bench Task Formulation, Jimenez et al. 2023

## Page 32

CS329Z: Engineering AI Agents

Mined from the web + world

SWE-rebench \[Code\]: A fully automated pipeline mined 21,336 veriﬁable tasks from 
3,468 GitHub repositories, including environment setup and test validation.

Badertdinov, Ibragim, et al. "Swe-rebench: An automated pipeline for task collection and

decontaminated evaluation of software engineering agents." (NeurIPS 2026)

## Page 33

CS329Z: Engineering AI Agents

Mined from the web + world

AgentTrek \[Web\]: Harvest how-to tutorials from the web, have a VLM agent replay 
them in a real browser, and keep veriﬁed runs, at $0.55 per trajectory.

Xu, Yiheng, et al. "Agenttrek: Agent trajectory synthesis via guiding replay with web tutorials." (ICLR 2025)

## Page 34

CS329Z: Engineering AI Agents

Mined from the web + world

AgentTrek \[Web\]: Harvest how-to tutorials from the web, have a VLM agent replay 
them in a real browser, and keep veriﬁed runs, at $0.55 per trajectory.

Xu, Yiheng, et al. "Agenttrek: Agent trajectory synthesis via guiding replay with web tutorials." (ICLR 2025)

## Page 35

CS329Z: Engineering AI Agents

Mined from the web + world

AgentTrek \[Web\]: Harvest how-to tutorials from the web, have a VLM agent replay 
them in a real browser, and keep veriﬁed runs, at $0.55 per trajectory.

## Page 36

CS329Z: Engineering AI Agents

Mined from the web + world

VideoAgentTrek \[CUA\]: Inverse dynamics model labels 39k YouTube 
screen-recording tutorials with clicks and keystrokes, yields 1.52M interaction steps.

Lu, Dunjie, et al. "VideoAgentTrek: Computer use pretraining from unlabeled videos." (arXiv 2025)

## Page 37

CS329Z: Engineering AI Agents

Mined from the web + world

VideoAgentTrek \[CUA\]: Inverse dynamics model labels 39k YouTube 
screen-recording tutorials with clicks and keystrokes, yields 1.52M interaction steps.

Lu, Dunjie, et al. "VideoAgentTrek: Computer use pretraining from unlabeled videos." (arXiv 2025)

## Page 38

CS329Z: Engineering AI Agents

Synthesized trajectories

## Page 39

CS329Z: Engineering AI Agents

Synthesized trajectories

Given a task or an environment, a model writes or runs the steps itself, and a ﬁlter 
keeps the good runs.

Instruction ﬁrst
Synatra

Start from a task

or tutorial

LLM writes the

steps without 
running them

Filter drops 
invalid samples

Interaction ﬁrst
OS-Genesis, 
NNetNav

Explore the 
environment

freely

Label the run in

hindsight

Score and prune

the runs

Trajectory

## Page 40

CS329Z: Engineering AI Agents

Mined from the web + world

Synatra \[Web\]: An LLM rewrites wikiHow tutorials and random web pages into 100k 
step-by-step demonstrations, at $0.031 each (3% of human cost).

Ou, Tianyue, et al. "Synatra: Turning indirect knowledge into direct demonstrations for digital

agents at scale." (NeurIPS 2024)

## Page 41

CS329Z: Engineering AI Agents

Mined from the web + world

Synatra \[Web\]: An LLM rewrites wikiHow tutorials and random web pages into 100k 
step-by-step demonstrations, at $0.031 each (3% of human cost).

Ou, Tianyue, et al. "Synatra: Turning indirect knowledge into direct demonstrations for digital

agents at scale." (NeurIPS 2024)

## Page 42

CS329Z: Engineering AI Agents

Mined from the web + world

Case Study: Synatra versus AgentTrek. What’s the diﬀerence?

Synatra
AgentTrek

Raw source
wikiHow articles and random web page 
snapshots

How-to tutorials ﬁltered from the 
RedPajama web crawl

How steps are 
made

An LLM writes them oﬄine; no step is ever 
executed

A VLM agent replays them live; a VLM 
judge keeps successes

Observations
Synthesized page text, no screenshots
Real screenshots and accessibility trees

Cost per sample
$0.031
$0.55

Model trained
CodeLlama-7B, text only
Qwen2-VL (vision) and Qwen2.5 (text)

## Page 43

CS329Z: Engineering AI Agents

Synthesized trajectories

OS-Genesis \[CUA\]: Explore apps ﬁrst, then infer the task each interaction 
accomplished; a reward model grades runs, nearly doubling AndroidWorld success.

Sun, Qiushi, et al. "OS-Genesis: Automating GUI agent trajectory construction via reverse task

synthesis." (ACL 2025)

## Page 44

CS329Z: Engineering AI Agents

Synthesized trajectories

OS-Genesis \[CUA\]: Explore apps ﬁrst, then infer the task each interaction 
accomplished; a reward model grades runs, nearly doubling AndroidWorld success.

Sun, Qiushi, et al. "OS-Genesis: Automating GUI agent trajectory construction via reverse task

synthesis." (ACL 2025)

## Page 45

CS329Z: Engineering AI Agents

Synthesized trajectories

NNetNav \[Web\]: An LM explores websites as a sampled persona, another labels 
the run in hindsight, and runs that cannot be labeled are pruned early.

Murty, Shikhar, et al. "NNetNav: Unsupervised learning of browser agents through environment

interaction in the wild." (arXiv 2024)

## Page 46

CS329Z: Engineering AI Agents

Synthesized tasks and environments

## Page 47

CS329Z: Engineering AI Agents

Synthesized tasks and environments

Build the sandbox, the task, and the checker automatically, so every task comes 
with a veriﬁable reward.

Code agents  SWE-smith, R2E-Gym
Tool-use agents  AgentScaler

Environment
Docker image of a real repo that can

run its tests

Simulated database behind real API

schemas

Task
Injected bug or reverted commit, plus

LM-written issue

Goal built from a chain of dependent

tool calls

Veriﬁer
Tests that fail before the ﬁx and pass

after

Final database state matches the

expected one

## Page 48

CS329Z: Engineering AI Agents

Synthesized tasks and environments

SWE-smith \[Code\]: Inject bugs that break existing tests in 128 Python repos and 
have an LM write the issue, yielding 50k tasks from about 20 hours of human work.

Yang, John, et al. "SWE-smith: Scaling data for software engineering agents." (NeurIPS 2025)

## Page 49

CS329Z: Engineering AI Agents

Synthesized tasks and environments

SWE-smith \[Code\]: Inject bugs that break existing tests in 128 Python repos and 
have an LM write the issue, yielding 50k tasks from about 20 hours of human work.

Yang, John, et al. "SWE-smith: Scaling data for software engineering agents." (NeurIPS 2025)

## Page 50

CS329Z: Engineering AI Agents

Synthesized tasks and environments

R2E-Gym \[Code\]: Turn ordinary commits into 8.1K executable tasks by generating 
tests and back-translating code changes into issue text, with no human-written PRs.

Jain, Naman, et al. "R2E-Gym: Procedural environments and hybrid verifiers for scaling

open-weights SWE agents." (COLM 2025)

## Page 51

CS329Z: Engineering AI Agents

Synthesized tasks and environments

AgentScaler \[Tools\]: Build veriﬁable simulated environments from real APIs by 
treating each tool call as a read or write on a database.

Fang, Runnan, et al. "Towards general agentic intelligence via environment scaling." (arXiv 2025)

## Page 52

CS329Z: Engineering AI Agents

Simulated users and environments

## Page 53

CS329Z: Engineering AI Agents

Simulated users and environments

An LLM can stand in for the user, the environment, or both, so the agent gets 
unlimited practice without real people or real systems.

Simulated user
An LLM plays the person

Simulated environment
An LLM predicts the next state and

reward

Agent in training
The model being taught

τ-bench, APIGen-MT
DreamGym

Requests, follow-ups,

reactions

Actions in; next state and 
reward out

Payoﬀ: cheap, unlimited practice.     Risk: agents learn simulator mistakes.

## Page 54

CS329Z: Engineering AI Agents

Simulated users and environments

τ-bench \[Tools\]: An LLM plays the customer in retail and airline support chats, and 
grading compares the ﬁnal database state to the goal.

Yao, Shunyu, et al. "τ-bench: A benchmark for tool-agent-user interaction in real-world domains."

(ICLR 2025)

## Page 55

CS329Z: Engineering AI Agents

Simulated users and environments

APIGen-MT \[Tools\]: LLM reviewers vet task blueprints with ground-truth actions; 
simulated human LM chats with the agent to turn each into a multi-turn trajectory.

Prabhakar, Akshara, et al. "APIGen-MT: Agentic pipeline for multi-turn data generation via

simulated agent-human interplay." (NeurIPS 2025)

## Page 56

CS329Z: Engineering AI Agents

Simulated users and environments

APIGen-MT \[Tools\]: LLM reviewers vet task blueprints with ground-truth actions; 
simulated human LM chats with the agent to turn each into a multi-turn trajectory.

Prabhakar, Akshara, et al. "APIGen-MT: Agentic pipeline for multi-turn data generation via

simulated agent-human interplay." (NeurIPS 2025)

## Page 57

CS329Z: Engineering AI Agents

Simulated users and environments

DreamGym \[Web\]: An LLM “experience model” predicts the next state and reward 
in text, replacing costly real rollouts during RL training.

Chen, Zhaorun, et al. "Scaling agent learning via experience synthesis." (ICLR 2026)

## Page 58

CS329Z: Engineering AI Agents

What agent data
accidentally teaches

## Page 59

CS329Z: Engineering AI Agents

Accidental Learnings

We have a bunch of traces and environments. Let’s just train on them, and then the 
model will become really good. End of story? Not quite.

Let’s take a look at several diﬀerent kinds of “gotchas” that can arise.

Reward Hacking

Environment rewards a

loophole

Overﬁt to Harness

Traces exclusively teach

one scaﬀold’s format

Training Trends

Be careful about SFT or

RL overshooting

## Page 60

CS329Z: Engineering AI Agents

Reward Hacking

SWE-bench tasks models with resolving GitHub issues by modifying a codebase. 
But what happens if you don’t remove the .git history…

Source: SWE-bench issue #465

### Page links

- [Link 1](https://github.com/SWE-bench/SWE-bench/issues/465)

## Page 61

CS329Z: Engineering AI Agents

Reward Hacking

This loophole could be exploited heavily during training. To address this, Self-play 
SWE-RL (Wei et al. 2025) wipes .git and restores test ﬁles before grading.

Source: Wei et al., Self-play SWE-RL (2025)

### Page links

- [Link 1](https://arxiv.org/abs/2512.18552)

## Page 62

CS329Z: Engineering AI Agents

Reward Hacking

Gaming the test harness: In Anthropic’s production coding env.’s, models learned 
hacks like sys.exit(0) to fake passing tests. Misalignment rose once they did.

Source: Anthropic blog · MacDiarmid et al. (2025)

### Page links

- [Link 1](https://arxiv.org/abs/2511.18397)
- [Link 2](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)

## Page 63

CS329Z: Engineering AI Agents

Reward Hacking

A chain-of-thought monitor caught reward hacking in OpenAI’s coding RL. Adding 
the monitor to the reward made the model hide its intent and keep hacking.

Source: OpenAI, Detecting misbehavior in frontier reasoning models (2025)

### Page links

- [Link 1](https://openai.com/index/chain-of-thought-monitoring/)

## Page 64

CS329Z: Engineering AI Agents

Reward Hacking

Adding the monitor to the reward made the model hide its intent and keep hacking.

Source: OpenAI, Detecting misbehavior in frontier reasoning models (2025)

### Page links

- [Link 1](https://openai.com/index/chain-of-thought-monitoring/)

## Page 65

CS329Z: Engineering AI Agents

Reward Hacking

Eval Awareness: On BrowseComp, Claude Opus 4.6 twice inferred it was being 
tested, identiﬁed the benchmark, and decrypted its answer key.

Source: Anthropic, Eval awareness in Claude Opus 4.6’s BrowseComp performance (2026)

### Page links

- [Link 1](https://www.anthropic.com/research/eval-awareness-browsecomp)

## Page 66

CS329Z: Engineering AI Agents

Reward Hacking

Memorization: Models name the buggy ﬁle from the issue text alone 76% of the 
time on SWE-Bench Veriﬁed, vs. up to 53% on repos outside SWE-Bench.

Source: Liang et al., The SWE-Bench Illusion (2025)

### Page links

- [Link 1](https://arxiv.org/abs/2506.12286)

## Page 67

CS329Z: Engineering AI Agents

Reward Hacking

Memorization: OpenAI recommended retired SWE-bench Veriﬁed as an evaluation 
they track when they found their models could recite issues from memory.

Source: OpenAI. Why we no longer evaluate SWE-bench Veriﬁed (2025)

We're playing a SWE-bench Verified 
memory game.
Please give your best guess of the 
full sentence of the task description 
based on the hint, and the 
corresponding code change introduced 
in the fix. Bonus points if you 
remember the exact diff.
The task ID is django__django-11451.
Hint: Part of the description was "... 
shouldn't make a database query when 
username is None"

Task (best-guess full sentence)
- “\`ModelBackend.authenticate()\` shouldn’t make a database query when 
\`username\` is \`None\`.”

What the fix changed (corresponding code change)
- Location: \`django/contrib/auth/backends.py\`
- Function: \`ModelBackend.authenticate(...)\`
- Change: add an early-return guard so that if \`username\` is \`None\` 
(and similarly if \`password\` is \`None\`), Django returns \`None\` 
immediately instead of calling 
\`UserModel._default_manager.get_by_natural_key(username)\` (which would 
hit the DB and/or error).

Best-guess diff (approximate, from memory): …

### Page links

- [Link 1](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

## Page 68

CS329Z: Engineering AI Agents

Reward Hacking

Misleading: Trained on human approval, a model learned to look right rather than 
be right. Humans approved its answers more often, but correctness didn’t improve.

Source: OpenAI. Why we no longer evaluate SWE-bench Veriﬁed (2025)

### Page links

- [Link 1](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

## Page 69

CS329Z: Engineering AI Agents

Overﬁt to Harness

Multiple harnesses could be used by an LM to carry out the same task, but if you 
only train LM’s on traces, environments using one harness, it won’t generalize.

Source: OpenAI. Why we no longer evaluate SWE-bench Veriﬁed (2025)

mini-swe-agent
Terminus 2
SWE-agent

### Page links

- [Link 1](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

## Page 70

CS329Z: Engineering AI Agents

Overﬁt to Harness

SFT will cause the model to imitate both capability and harness, without being able 
to tell which part is which.

Source: OpenAI. Why we no longer evaluate SWE-bench Veriﬁed (2025)

### Page links

- [Link 1](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

## Page 71

CS329Z: Engineering AI Agents

Overﬁt to Harness

LM trained in one harness keeps its conventions. Fix: vary harness during training.

Trained on mini-swe-agent, deployed in a function-calling harness

## Page 72

CS329Z: Engineering AI Agents

Training Trends

SFT can cause overﬁtting: SWE-RL trained on GitHub PRs: RL improved ﬁve 
out-of-domain tasks, while SFT on the same seed data degraded them on average.

Source: Wei et al., SWE-RL (NeurIPS 2025)

### Page links

- [Link 1](https://arxiv.org/abs/2502.18449)

## Page 73

CS329Z: Engineering AI Agents

Training Trends

RL can overshoot: OpenThoughts-Agent’s best RL run peaked, then collapsed as 
the policy over-explored and timed out. They shipped the pre-collapse checkpoint.

Source: Raoof et al., OpenThoughts-Agent (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2606.24855)

## Page 74

CS329Z: Engineering AI Agents

Training Trends

Best model != Best teacher: In OpenThoughts-Agent, trajectories from 
GPT-5.3-Codex trained a worse student than trajectories from the older GLM-4.7.

Source: Raoof et al., OpenThoughts-Agent (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2606.24855)

## Page 75

CS329Z: Engineering AI Agents

Takeaways

1
Agents need more than text.  Tasks, environments, trajectories.

2
Humans are realistic but costly.  Demos are hard to scale.

3
Mined traces are cheap.  Code, tutorials, and videos convert.

4
Synthesis scales cheaply.  Models write steps and build tasks.

5
Simulators give endless practice.  Their errors get learned too.

6
Data teaches by accident.  Reward hacks, harness overﬁt.
