# Lecture 12: Data Selection & Quality

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture12.pdf) · [Raw file](../../raw/slides/lecture12.pdf)

Retrieved: 2026-11-13T16:30:37.831568+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

CS329Z: Engineering AI Agents

CS 329Z: Engineering AI Agents
Data Selection & Quality

Diyi Yang, Michael Ryan, John Yang

## Page 2

CS329Z: Engineering AI Agents

Announcements

●
HW2 released!

○
Task due 11/23

○
Peer Reviews due 12/2

●
Please sign up for oral exams!! Registration already over due.

●
Midpoint demo + report due this Friday (11/6)

## Page 3

CS329Z: Engineering AI Agents

Recap: Lecture 10

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

## Page 4

CS329Z: Engineering AI Agents

Roadmap

Data Selection & Quality

●
Motivation \[10 min\]
●
Which tasks are worth 
training on? \[25 min\]
●
Which trajectories are worth 
imitating? \[15 min\]

●
More data, or better data? \[25 min\]
●
Takeaways \[5 min\]

tl;dr: Making agent tasks and trajectories is now cheap; deciding what to keep is 
the hard part. In this lecture, we’ll cover which tasks to train on, which trajectories 
to imitate, and whether more data or better data wins.

## Page 5

CS329Z: Engineering AI Agents

Motivation

## Page 6

CS329Z: Engineering AI Agents

Motivation

Making tasks and trajectories is now cheap. Deciding what to keep is hard.

Make tasks + trajectories
Now cheap

Decide what to keep
The hard part

## Page 7

CS329Z: Engineering AI Agents

Motivation

CWM generated 3M agent trajectories, then decided which ones to keep.

3M

agent trajectories from 
10.2k Docker images of

3.15k repos

Dropped near-duplicates

Within each repo, kept trajectories have pairwise 
Jaccard similarity below 0.5.

Kept failed attempts

The goal is a world model of code environments, so 
they don’t ﬁlter by success.

Source: Meta FAIR CodeGen Team, CWM (2025)

### Page links

- [Link 1](https://arxiv.org/abs/2510.02387)

## Page 8

CS329Z: Engineering AI Agents

Motivation

Every stage of the pipeline throws data away.

Candidate tasks

Valid tasks

Learnable tasks

Rollouts

Kept trajectories

Training mix

Section 2
Which tasks?

Section 3
Which trajectories?

Section 4
More or better data?

## Page 9

CS329Z: Engineering AI Agents

Motivation

We select two things: trajectories for SFT, environments for RL.

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

Section 3
Section 2

## Page 10

CS329Z: Engineering AI Agents

Motivation

Training data goes bad in three ways.

Wrong signal

Broken veriﬁers and 
hacked successes.

Sections 2–3

No signal

Tasks too easy or too hard 
to learn from.

Section 2

Redundant signal

More of the same.

Section 4

## Page 11

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

## Page 12

CS329Z: Engineering AI Agents

Motivation

The open tension: is less more, or is more more?

Less is more

LIMI: 78 hand-curated trajectories 
beat 10,000.

More is more

Orchard: at scale, data size 
matters more than how you pick it.
vs

Section 4 looks at when each one holds.

## Page 13

CS329Z: Engineering AI Agents

Which tasks are worth training on?

## Page 14

CS329Z: Engineering AI Agents

Which tasks are worth training on?

Let’s use the mental model of thinking of the task selection process as a loop!

1

Filter out broken 
or unreliable tasks

SWE-bench Veriﬁed

2

Check task validity 
by running them

APIGen, CodeMidas

3

Keep tasks LM 
sometimes solves

DAPO, LEGO-RL

4

Re-select as the 
model improves

WebRL

## Page 15

CS329Z: Engineering AI Agents

SWE-bench Veriﬁed

In sklearn-14520, the test requires an exact deprecation message that was only 
decided in PR discussion the agent never sees.

Source: OpenAI, Introducing SWE-bench Veriﬁed (2024)

Copy param ignored in TfidfVectorizer
I was playing with vectorizers and I found this:

https://github.com/scikit-learn/scikit-learn/blob/ae1631
9626e2ca6ca0e54d4a5b83f73f817232aa/sklearn/feature_extra
ction/text.py#L1669

However that parameter is not used later in the method.

Here \`copy=False\` is used:

https://github.com/scikit-learn/scikit-learn/blob/ae1631
9626e2ca6ca0e54d4a5b83f73f817232aa/sklearn/feature_extra
ction/text.py#L1692

Is there anything I am missing?

### Page links

- [Link 1](https://openai.com/index/introducing-swe-bench-verified/)

## Page 16

CS329Z: Engineering AI Agents

SWE-bench Veriﬁed

93 Python developers annotated 1,699 random SWE-bench samples. Each sample 
was labeled by 3 annotators, keeping the highest-severity label.

Source: OpenAI, Introducing SWE-bench Veriﬁed (2024)

### Page links

- [Link 1](https://openai.com/index/introducing-swe-bench-verified/)

## Page 17

CS329Z: Engineering AI Agents

SWE-bench Veriﬁed

38.3% ﬂagged for underspeciﬁed problem statements, 61.1% for unfair unit tests; 
68.3% ﬁltered out overall.

Source: OpenAI, Introducing SWE-bench Veriﬁed (2024)

### Page links

- [Link 1](https://openai.com/index/introducing-swe-bench-verified/)

## Page 18

CS329Z: Engineering AI Agents

SWE-bench Veriﬁed

Broken tasks hide real ability. In training, they give wrong rewards.

16%

GPT-4o on original SWE-bench
33.2%

GPT-4o on SWE-bench Veriﬁed

Source: OpenAI, Introducing SWE-bench Veriﬁed (2024)

### Page links

- [Link 1](https://openai.com/index/introducing-swe-bench-verified/)

## Page 19

CS329Z: Engineering AI Agents

APIGen

Human review doesn’t scale, so APIGen automates it: a format check, an execution 
check, then an LLM judging whether results match the query’s intent.

Source: Liu et al., APIGen (2024)

### Page links

- [Link 1](https://arxiv.org/abs/2406.18518)

## Page 20

CS329Z: Engineering AI Agents

CodeMidas

CodeMidas builds coding 
RL environments from 
source code alone: no 
issues, PRs, commits, or 
existing tests.

From MiMo model team.

Source: Ye et al., CodeMidas (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2609.22068)

## Page 21

CS329Z: Engineering AI Agents

CodeMidas

Tests should accept any correct solution.

Source: Ye et al., CodeMidas (2026)

Too strict: sklearn-14520
CodeMidas: only what the task states

msg = ("'copy' param is unused and has"
       " been deprecated since version"
       " 0.22. Backward compatibility for"
       " 'copy' will be removed in 0.24.")
with pytest.warns(DeprecationWarning,
                  match=msg):
    tv.transform(train_data, copy=True)

# Task: raise ValueError on bad input.
# The message wording is not specified.

with pytest.raises(ValueError):
    parse_config(bad_input)

The exact message came from PR discussion.
Illustrative test, following the paper’s rule.

### Page links

- [Link 1](https://arxiv.org/abs/2609.22068)

## Page 22

CS329Z: Engineering AI Agents

CodeMidas

Each task runs in six fresh containers.

Starting code × 2
Reference solution × 4

Must fail
Must fail
Must pass
Must pass
Must pass
Must pass

A task is kept only if all six runs come out as expected.

Source: Ye et al., CodeMidas (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2609.22068)

## Page 23

CS329Z: Engineering AI Agents

CodeMidas

After rollouts, three more ﬁlters.

Source: Ye et al., CodeMidas (2026)

Candidate task
Kept task

Leakage probe

Drop if adversarial

rollouts ﬁnd the

solution leaks

Verdict review

Drop if a reviewer

ﬁnds a wrong 
veriﬁer verdict

Outcome ﬁlter

Drop if every 
attempt passes, or 
every attempt fails

### Page links

- [Link 1](https://arxiv.org/abs/2609.22068)

## Page 24

CS329Z: Engineering AI Agents

CodeMidas

Even the ﬁltered 3k subset beats the unﬁltered 8k sample on all three evaluations. 
Full 5k beats 8k by 0.59 / 4.59 / 4.49 points (SWE-bench Pro / DeepSWE / Internal).

Source: Ye et al., CodeMidas (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2609.22068)

## Page 25

CS329Z: Engineering AI Agents

DAPO

If every rollout in a group gets the same reward, RL learns nothing.

Source: Yu et al., DAPO (2025)

advantage  =  (reward − group mean) / group std

Mixed rewards
1
0
1
1
0
0
1
0
→ learns

All correct
1
1
1
1
1
1
1
1
→ no gradient

One prompt, 8 rollouts. Filled = reward 1.

### Page links

- [Link 1](https://arxiv.org/abs/2503.14476)

## Page 26

CS329Z: Engineering AI Agents

DAPO

It gets worse: as the model improves, more prompts become all-correct.

Source: Yu et al., DAPO (2025)

What the y-axis counts

1
1
1
1
1
1
1
1

accuracy 1: every rollout correct

These prompts give zero gradient 
(previous slide). As their share rises, 
each batch carries fewer prompts the 
model can learn from.

### Page links

- [Link 1](https://arxiv.org/abs/2503.14476)

## Page 27

CS329Z: Engineering AI Agents

DAPO

Fix: keep sampling until the batch is full of prompts with mixed rewards.

Source: Yu et al., DAPO (2025)

Keep

1
0
1
1
0
0
1
0

Drop: all correct or all wrong

1
1
1
1
1
1
1
1

0
0
0
0
0
0
0
0

Same accuracy in fewer steps,
even though each step samples more.

### Page links

- [Link 1](https://arxiv.org/abs/2503.14476)

## Page 28

CS329Z: Engineering AI Agents

LEGO-RL

Validity checks cut 36,884 candidate tasks to 21,681.

Source: Du et al., LEGO-RL (2026)

Candidates
36,884

Rule-based screening
22,806

Build + veriﬁer check
21,681

Diﬃculty screen (next)
2,699

About 2.5% of inspected tasks had veriﬁers that wrongly apply the reference patch.

### Page links

- [Link 1](https://arxiv.org/abs/2608.17393)

## Page 29

CS329Z: Engineering AI Agents

LEGO-RL

Keep tasks the model solves 1–3 times out of 4 tries.

Times solved out of 4 tries

0 / 4

never solved

1 / 4

keep

2 / 4

keep

3 / 4

keep

4 / 4

always solved

Final training set: 2,699 tasks.

Source: Du et al., LEGO-RL (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2608.17393)

## Page 30

CS329Z: Engineering AI Agents

LEGO-RL

Without the screen, training improves on neither measure.

In the unscreened pool, 72.7% of tasks are never solved and 13.4% are always solved.

Source: Du et al., LEGO-RL (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2608.17393)

## Page 31

CS329Z: Engineering AI Agents

LEGO-RL

As the policy improves, the task pool goes stale. Must refresh over time.

Under OpenHands SDK, zero-variation groups rise from 44.7% to 51.4%.

Source: Du et al., LEGO-RL (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2608.17393)

## Page 32

CS329Z: Engineering AI Agents

WebRL

Online RL for web agents faces three problems.

1

Scarce training tasks

2

Sparse feedback

3

Policy distribution drift

Source: Qi et al., WebRL (ICLR 2025)

### Page links

- [Link 1](https://arxiv.org/abs/2411.02337)

## Page 33

CS329Z: Engineering AI Agents

WebRL

A self-evolving curriculum generates new tasks from unsuccessful attempts, plus an 
outcome-supervised reward model.

Source: Qi et al., WebRL (ICLR 2025)

### Page links

- [Link 1](https://arxiv.org/abs/2411.02337)

## Page 34

CS329Z: Engineering AI Agents

WebRL

WebRL takes Llama-3.1-8B from 4.8% to 42.4% on WebArena-Lite.

The 70B model reaches 47.3%.

Source: Qi et al., WebRL (ICLR 2025)

Llama-3.1-8B success rate on WebArena-Lite

4.8%

42.4%

### Page links

- [Link 1](https://arxiv.org/abs/2411.02337)

## Page 35

CS329Z: Engineering AI Agents

Which trajectories are worth imitating?

## Page 36

CS329Z: Engineering AI Agents

Which trajectories are worth imitating?

Passing the tests ≠ a good demonstration.

Passed the tests
Failed the tests

Some are cheats

Check how the 
agent got there

Veriﬁcation Horizon

Some are sloppy

Select by process 
quality

SWE-Prime

Labeled failures

Keep them, marked 
as failed

NAT

Good steps

Salvage them from 
failed expert runs

EEF

## Page 37

CS329Z: Engineering AI Agents

The Veriﬁcation Horizon

Generating solutions is no longer the hard part; verifying them is.

Source: Qwen Team, The Veriﬁcation Horizon (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2606.26300)

## Page 38

CS329Z: Engineering AI Agents

The Veriﬁcation Horizon

Agents ﬁnd seven kinds of shortcuts.

1.
Solution-artifact retrieval

2.
External ﬁx lookup

3.
Harness tampering

4.
Test-oracle tampering

5.
Visible-test overﬁtting

6.
Evaluator-aware patching

7.
Git-history mining

Source: Qwen Team, The Veriﬁcation Horizon (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2606.26300)

## Page 39

CS329Z: Engineering AI Agents

The Veriﬁcation Horizon

Shortcuts pay oﬀ: solution-artifact retrieval is rare but eﬀective.

4.32%

of trajectories use solution-artifact 
retrieval

72.34%

of those resolve (+12.35 points vs. 
baseline)

Source: Qwen Team, The Veriﬁcation Horizon (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2606.26300)

## Page 40

CS329Z: Engineering AI Agents

The Veriﬁcation Horizon

Pass rate can stay high while clean performance drops.

Source: Qwen Team, The Veriﬁcation Horizon (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2606.26300)

## Page 41

CS329Z: Engineering AI Agents

The Veriﬁcation Horizon

Fix: monitor the trajectories. Hacking nearly disappears and clean performance 
rises (average over three SWE-bench variants).

28.57% → 0.56%

hacked resolved rate

40.22% → 60.53%

clean resolved rate

Source: Qwen Team, The Veriﬁcation Horizon (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2606.26300)

## Page 42

CS329Z: Engineering AI Agents

SWE-Prime

Successful runs can still contain ineﬀective, redundant, or risky steps.

One successful trajectory

Step
Step

ineﬀective

Step
Step

redundant

Step
Step

risky

Step
Tests pass

Source: Zheng et al., SWE-Prime (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2608.27449)

## Page 43

CS329Z: Engineering AI Agents

SWE-Prime

Two stages: select 
trajectories, then 
select segments.

Stage 1: Pick by 
process quality

Stage 2: Score by 
contribution, risk, 
learnability

Source: Zheng et al., SWE-Prime (2026)

### Page links

- [Link 1](https://arxiv.org/abs/2608.27449)

## Page 44

CS329Z: Engineering AI Agents

SWE-Prime

Training on a 10% subset beats training on all successful trajectories.

Source: Zheng et al., SWE-Prime (2026)

All successful trajectories

10%

selected by SWE-Prime beats
training on all of them.

Relative gains up to 12.2% (SWE-bench Pro) and 24.2% 
(SWE-bench Veriﬁed).

### Page links

- [Link 1](https://arxiv.org/abs/2608.27449)

## Page 45

CS329Z: Engineering AI Agents

NAT

Standard practice trains only on 
successful trajectories.
—
Left: a successful trajectory.

Right: a failed one. Its early steps are 
reasonable, but standard practice 
throws the whole run away.
—

Source: Wang et al., NAT (NAACL 2025)

### Page links

- [Link 1](https://arxiv.org/abs/2402.11651)

## Page 46

CS329Z: Engineering AI Agents

NAT

Tell the model which trajectories succeeded, with a preﬁx or suﬃx.

Source: Wang et al., NAT (NAACL 2025)

### Page links

- [Link 1](https://arxiv.org/abs/2402.11651)

## Page 47

CS329Z: Engineering AI Agents

NAT

Failed trajectories mix useful information with errors.

The label gives a better trade-oﬀ between the useful 
information and the errors in failed trajectories.

NAT’s explanation for why it works.

Source: Wang et al., NAT (NAACL 2025)

### Page links

- [Link 1](https://arxiv.org/abs/2402.11651)

## Page 48

CS329Z: Engineering AI Agents

EEF

Rejection-sampling ﬁne-tuning (RFT) trains only on successful expert runs.

Source: Lan et al., EEF (2025)

Expert runs

RFT keeps

easier subtasks
harder subtasks

The expert mostly succeeds on easy subtasks, so hard ones never enter training.

Filled = success. Illustrative.

### Page links

- [Link 1](https://arxiv.org/abs/2504.13145)

## Page 49

CS329Z: Engineering AI Agents

EEF

A failure may come from mistakes in only the last few steps.

Prior methods treat every action 
in a failed run as negative.

Source: Lan et al., EEF (2025)

### Page links

- [Link 1](https://arxiv.org/abs/2504.13145)

## Page 50

CS329Z: Engineering AI Agents

EEF

EEF beats RFT and GPT-4 on WebShop.

Source: Lan et al., EEF (2025)

WebShop win rate

62%

53.6%

35.6%

### Page links

- [Link 1](https://arxiv.org/abs/2504.13145)

## Page 51

CS329Z: Engineering AI Agents

More data, or better data?

## Page 52

CS329Z: Engineering AI Agents

More data, or better data?

Is less more, or is more more?

More data, unﬁltered

Small, curated

training data size →

Illustrative, not data.

Either way, diversity is what generalizes.

## Page 53

CS329Z: Engineering AI Agents

LIMI

Earlier work got a lot from small curated datasets.

Source: Xiao et al., LIMI (2025)

10
100
1k
10k

LIMI: 78 agent trajectories
LIMA: 1,000 alignment examples

LIMO: 817 math samples
10,000: LIMI’s comparison

Training examples (log scale)

### Page links

- [Link 1](https://arxiv.org/abs/2509.17567)

## Page 54

CS329Z: Engineering AI Agents

LIMI

78 hand-curated trajectories beat 10,000 (128× fewer).

Source: Xiao et al., LIMI (2025)

73.5% on AgencyBench with 78 samples, vs. 47.8% for a model trained on 10,000.

### Page links

- [Link 1](https://arxiv.org/abs/2509.17567)

## Page 55

CS329Z: Engineering AI Agents

LIMI

The 78 training queries came from two sources.

Source: Xiao et al., LIMI (2025)

60
18

from real developer and researcher scenarios
sampled from queries 
synthesized from GitHub PRs

78 training queries in total

### Page links

- [Link 1](https://arxiv.org/abs/2509.17567)

## Page 56

CS329Z: Engineering AI Agents

LIMI

Four PhD students worked with GPT-5 until each task succeeded.

Source: Xiao et al., LIMI (2025)

### Page links

- [Link 1](https://arxiv.org/abs/2509.17567)

## Page 57

CS329Z: Engineering AI Agents

LIMI

The headline comes with ﬁne print.

Source: Xiao et al., LIMI (2025)

●
A small, close benchmark. AgencyBench has 10 tasks and shares many 
authors with LIMI.

●
Small gain without the CLI. Without the CLI environment, generalization is 
50.0% vs. 48.7% for GLM-4.5.

### Page links

- [Link 1](https://arxiv.org/abs/2509.17567)

## Page 58

CS329Z: Engineering AI Agents

Orchard

Same base model and SFT recipe. Only data size and selection strategy vary.

Source: Peng et al., Orchard (2026)

Heuristic
Uses gold-patch properties

Random
Diverse repo

Concentrated

repo
Multi-ﬁle
Large diﬀ
Composite

512 traj.

1,024 traj.

2,048 traj.

Each dot is one SFT run. Base model, recipe, and harness stay ﬁxed.

### Page links

- [Link 1](https://arxiv.org/abs/2605.15040)

## Page 59

CS329Z: Engineering AI Agents

Orchard

Any good SFT helps.

Source: Peng et al., Orchard (2026)

22.0%

+22 points

base model level

Base model
Worst SFT setting

### Page links

- [Link 1](https://arxiv.org/abs/2605.15040)

## Page 60

CS329Z: Engineering AI Agents

Orchard

Scale dominates: more data beats a better selection strategy.

Source: Peng et al., Orchard (2026)

Trajectories
Random
Diverse repo
Concentrated

repo
Multi-ﬁle
Large diﬀ
Composite

512
45.8
44.0
47.9
47.5
49.5
48.1

1,024
50.3
49.0
51.3
51.6
52.2
52.1

2,048
52.8
52.2
53.4
54.2
52.9
53.7

Worst method (Diverse repo), 512 → 2,048 trajectories: +8.2 points.
Spread across all six strategies at 512: 5.5 points.

SFT-only resolve rate (%) on SWE-bench Veriﬁed, Orchard Table 10

### Page links

- [Link 1](https://arxiv.org/abs/2605.15040)

## Page 61

CS329Z: Engineering AI Agents

AgentReﬁne

Existing agent data does well on held-in tasks, not held-out ones.

Source: Fu et al., AgentReﬁne (ICLR 2025)

### Page links

- [Link 1](https://arxiv.org/abs/2501.01702)

## Page 62

CS329Z: Engineering AI Agents

AgentReﬁne

In new environments, most errors fall into three types.

Source: Fu et al., AgentReﬁne (ICLR 2025)

Format error

Action: clik \[Buy Now\]

Illogical reasoning

Thought: mug is in sink.
Action: go to fridge 1

Repeated generation

Action: look
Action: look
Action: look

Illustrative examples of each error type.

### Page links

- [Link 1](https://arxiv.org/abs/2501.01702)

## Page 63

CS329Z: Engineering AI Agents

AgentReﬁne

Synthesize diverse environments, then train the model to ﬁx its mistakes.

Source: Fu et al., AgentReﬁne (ICLR 2025)

### Page links

- [Link 1](https://arxiv.org/abs/2501.01702)

## Page 64

CS329Z: Engineering AI Agents

AgentReﬁne

Self-correction and diversity are what generalize.

Source: Fu et al., AgentReﬁne (ICLR 2025)

●
More robust. Training on self-correction holds up better when the 
environment changes slightly.

●
Diversity drives the gains. Diverse environments and diverse thoughts in the 
data are what make it generalize.

### Page links

- [Link 1](https://arxiv.org/abs/2501.01702)

## Page 65

CS329Z: Engineering AI Agents

SWE-smith

Recap from Lecture 10: one environment per repo, with bugs synthesized into it.

Source: Yang et al., SWE-smith (NeurIPS 2025)

### Page links

- [Link 1](../readings/arxiv-2504-21798.md)

## Page 66

CS329Z: Engineering AI Agents

SWE-smith

Each run uses 700 expert trajectories, drawn from 4 to 100 repositories.

Source: Yang et al., SWE-smith (NeurIPS 2025)

4 repositories
100 repositories

same 700 
trajectories

### Page links

- [Link 1](../readings/arxiv-2504-21798.md)

## Page 67

CS329Z: Engineering AI Agents

SWE-smith

Performance grows roughly logarithmically with repository count.

Source: Yang et al., SWE-smith (NeurIPS 2025)

### Page links

- [Link 1](../readings/arxiv-2504-21798.md)

## Page 68

CS329Z: Engineering AI Agents

Takeaways

Filtering is most valuable when the candidate pool is limited.

Source: Qwen Team, The Veriﬁcation Horizon (2026), Table 10

Fine-tuning score by training set (number of samples)

21.61
23.52
24.75

Filtering beats random at the same size, but the bigger unﬁltered set wins.
This reconciles LIMI and Orchard.

### Page links

- [Link 1](https://arxiv.org/abs/2606.26300)

## Page 69

CS329Z: Engineering AI Agents

Takeaways

A practical checklist for selecting agent data.

1

Verify 
tasks

Section 2

2

Screen 
diﬃculty

Section 2

3

Audit 
successes

Section 3

4

Keep 
failures 
(labeled)

Section 3

5

Scale 
diverse 
sources

Section 4

## Page 70

CS329Z: Engineering AI Agents

Summary

Making agent data is cheap. The work is deciding what to keep.

Candidate tasks

Valid tasks

Learnable tasks

Rollouts

Kept trajectories

Training mix

Tasks. Run each one to check it, keep the ones 
the model sometimes solves, and refresh the 
pool as it improves.

Trajectories. A pass can be a cheat, so check 
how it passed. Failures still teach.

Training mix. Curate when data is scarce;
at scale, size and diversity win.

Next lecture: how do we know the agent actually improved?
