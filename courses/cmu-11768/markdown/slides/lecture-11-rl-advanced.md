# Lecture 11 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-11-rl-advanced.pdf) · [Raw file](../../raw/slides/lecture-11-rl-advanced.pdf)

Retrieved: 2026-11-13T16:45:30.840310+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Advanced RL Algorithms
for Agents

Graham Neubig

Language Technologies Institute

Improving how agents learn from experience

1

## Page 2

RL lecture map

RL basics

Sample attempts →
score them → update
the policy
→

Today

Useful feedback
Less waiting
Stable updates
Reliable rewards
Learning from a
teacher

→

Next lecture

Memory, parallelism,
and execution at scale

2

## Page 3

An RL task: fixing a bug

We’ll train a coding agent to fix bugs, using tests to judge each attempt.

Prompt

Fix the retry setting: zero should disable retries, but the code returns three. Preserve the other
cases.

Initial state: buggy code

def retry_count(config):

return config.get("retries") or 3

Verifier: tests

Input → expected output

Missing → 3
None → 3

0 → 0
2 → 2

Bug-fix example · Lecture 6: Coding Agents (slides) ↗
3

### Page links

- [Link 1](https://cmu-agents.vercel.app/slides/lecture-06-coding-agents.pdf)

## Page 4

A successful trajectory

A trajectory τ is one attempt: the agent’s actions and the observations they produce.

Final reward: R(τ) = 1 if all four tests pass; 0 otherwise.

1 Inspect

Read the function

0 becomes 3

→2 Edit

Change default
handling

First patch
saved

→3 Test

Run the four tests

One test still
fails

→4 Revise

Change the code
again

Revised patch
saved

→5 Test again

Rerun the four
tests

All four tests
pass

4

## Page 5

The RL training loop

Training repeats the loop to increase average reward over many attempts.

Sample

Run the agent on tasks
and collect trajectories τ.

→

Score

The verifier assigns each
trajectory its reward R(τ).

→

Update

Use the rewards to
change the policy’s
parameters.

Collect new attempts with the updated policy

x is the task (initial state and prompt); θ is the policy’s parameters.
p (τ | x) is the probability of trajectory τ given task x.

Goal J(θ): maximize average reward on task x

θ

J(θ) = E
​\[R(τ)\]
τ∼p
​(⋅∣x)
θ

5

## Page 6

Reward and the policy update

Plain REINFORCE uses the final reward to weight every action in an attempt.

Successful attempt

All four tests pass: R(τ) = 1.

Increase the likelihood of its actions.

Failed attempt

At least one test fails: R(τ) = 0.

This attempt contributes no update.

At step t, action a  follows history h : the task, earlier actions, and observations.
π (a  | h ) is the policy’s probability of that action given the history.

Loss to minimize for one sampled trajectory

How can a failed attempt still provide a learning signal?

t
t

θ
t
t

L

​ =
PG
−R(τ)

​log π

​(a

​ ∣

t
∑
θ
t
h

​)
t

6

## Page 7

Credit assignment and

dense feedback

Which actions deserve credit?

7

## Page 8

Comparing trajectories on the same task

Sample four attempts at the same bug-fix task, then compare their rewards.

Attempt
Final tests
Reward R(τ)
Update weight:
reward − baseline

1
All four pass
1
1 − 0.25 = +0.75

2
At least one fails
0
0 − 0.25 = −0.25

3
At least one fails
0
0 − 0.25 = −0.25

4
At least one fails
0
0 − 0.25 = −0.25

Use the group average as a baseline:
(1 + 0 + 0 + 0) / 4 = 0.25.

Even failed attempts now contribute: their actions get a negative weight.

8

## Page 9

Rewards for individual turns

A successful trajectory can contain a mistake; a failed trajectory can contain a helpful
turn.

Two illustrative trajectories on the same task. Each action a , …, a  represents one agent turn.

Trajectory A

Success
a
a

Mistake
a
a
a
a
R=1

Trajectory B

Failure
a
a
a
a

Helpful
a
a
R=0

The group weight is the same for every turn in a trajectory.

Turn-level rewards could tell us which turns to reinforce within each trajectory.

0
5

0

1

2
3
4
5

0
1
2

3

4
5

9

## Page 10

Reward-to-go from one trajectory

With only a final reward, A receives zero at each step until the task succeeds.

History before

Action

Reward after

h

a

r  = 0

h

a

r  = 0

h

a

r  = 1

Starting just before a , how much reward remains on this trajectory?

Add the three remaining rewards, counting each equally

This sum is the reward-to-go R : the rewards received after h .

h

a

r  = 0

0

0

1

h

a

r  = 0

1

1

2

h

a

r  = 0

2

2

3

3

3

4

4

4

5

5

5

6

3

0 + 0 + 1 = 1

3
3

10

## Page 11

Credit along two trajectories

B receives zero reward at every step. Compare its reward-to-go with A's.

Trajectory A

Success

a

R₀=1

a

R₁=1

a

R₂=1

a

R₃=1

a

R₄=1

a

R₅=1
R=1

Trajectory B

Failure

a

R₀=0

a

R₁=0

a

R₂=0

a

R₃=0

a

R₄=0

a

R₅=0
R=0

Add the remaining rewards: at every action, R  = 1 on A and R  = 0 on B.

How can we estimate which turns helped when we only observe the final reward?

0
1
2
3
4
5

0
1
2
3
4
5

t
t

11

## Page 12

Expected reward-to-go from a history

Imagine continuing ten times from B's history h , using the same rollout policy μ.

Same h
Ten possible continuations →

Reward-to-go from each continuation (illustrative)

0
1
0
0
1
0
0
0
1
0

Three continuations have R  = 1. The average is 3 ÷ 10 = 0.3.

Value: the average over all possible continuations under μ

The bar means “given h .” Ten samples give an estimate of this average.

3

3

3

V (h

​) =
μ
3
E

​\[R

​ ∣
μ
3
h

​\]
3

3

12

## Page 13

Learning the value function

Train a critic to predict reward-to-go from the history, using squared error.

Its prediction is V (h), with learned parameters φ. Reuse the ten outcomes at h : three 1s and seven 0s.

If Vφ(h₃) = 0.6, its average squared error is

The best prediction for these samples is their mean, 0.3 (squared error 0.21).

Minimize over φ; Eₜ averages histories from sampled rollouts

φ
3

​ =
10
3(0.6 −1) + 7(0.6 −0)
2
2

0.30

L (ϕ) =
V
E
​
V
​(h
​) −R
​
t\[(
ϕ
t
t)2\]

Squared-error baseline training · Ranzato et al., ICLR 2016 · §3.2.1 ↗
13

### Page links

- [Link 1](../optional-readings/ref-6e30095785b4.md)

## Page 14

Modeling the value function

A critic can use its own network or read the policy's hidden representation.

Separate value network

History h

↓

Value network φ

Own body and output layer

↓
Prediction V (h )

Value loss trains the whole value network.
Example: InstructGPT.

Value head on policy body

History h

↓
Policy body (part of θ)

↓ stop-gradient

Linear value head φ

↓
Prediction V (h )

Value loss trains only the head.
Example: MIXER (Ranzato et al.).

Stop-gradient blocks the value loss from updating the policy body. The policy loss still trains it.

t

φ
t

t

φ
t

InstructGPT · Ouyang et al., 2022 · App. C.4 ↗
MIXER · Ranzato et al., 2016 · §3.2.1 ↗
14

### Page links

- [Link 1](../optional-readings/arxiv-2203-02155.md)
- [Link 2](../optional-readings/ref-6e30095785b4.md)

## Page 15

One-step change in value

Here, rewards are zero. Compare the critic’s value before and after each action.

Trajectory B · final three actions

a

Before
V (h ) = 0.3

Reward
r  = 0

Next
V (h ) = 0.6

0 + 0.6 − 0.3 = +0.3

a

Before
V (h ) = 0.6

Reward
r  = 0

Next
V (h ) = 0.4

0 + 0.4 − 0.6 = −0.2

a

Before
V (h ) = 0.4

Reward
r  = 0

Next
V (h ) = 0.0

0 + 0.0 − 0.4 = −0.4

B ends after a , so no future reward remains at h : V (h ) = 0.

Temporal-difference (TD) error, with no reward discounting

3

φ
3

4

φ
4

4

φ
4

5

φ
5

5

φ
5

6

φ
6

5
6
φ
6

δ
​ =
t
r
​ +
t+1
V
​(h
​) −
ϕ
t+1
V
​(h
​)
ϕ
t

15

## Page 16

Generalized advantage estimation

How should later errors affect the credit given to B's a ?

Trajectory B · final three actions

a

δ  = +0.3

Weight: 1

a

δ  = −0.2

Weight: 0.5

a

δ  = −0.4

Weight: 0.25

Choose λ = 0.5: each later error gets half the weight of the previous one.

Estimated advantage at a₃: combine the three errors

GAE repeats this backward: Â  = δ  + λÂ
. At the end, no later errors remain.

3

3

3

4

4

5

5

​ =
A^3
0.3 + 0.5(−0.2) + 0.25(−0.4) = 0.1

t
t
t+1

GAE · Schulman et al., ICLR 2016 ↗
16

### Page links

- [Link 1](../optional-readings/arxiv-1506-02438.md)

## Page 17

A surrogate: learning value from annotations

A process reward model (PRM) learns step correctness as a surrogate for value.

Here, 5x = 6x − 14 implies x = 14. The annotator marks “x = 7” as incorrect.

Let’s Verify Step by Step · Lightman et al., 2023 · Figure 1 ↗
17

### Page links

- [Link 1](../optional-readings/arxiv-2305-20050.md)

## Page 18

Synchronous and asynchronous RL

18

## Page 19

Waiting in synchronous RL

Every trajectory in a batch must finish before the policy update starts.

Generate trajectories
Update policy
Waiting

GPU 1

GPU 2

GPU 3

Generate

Generate

Generate

Wait
Update

Update

Update

Generate

Generate

Generate

Time →

The next batch starts after the policy update.

AReaL · Fu et al., 2026 · §3.2 ↗
19

### Page links

- [Link 1](../optional-readings/arxiv-2505-24298.md)

## Page 20

Overlapping rollouts and updates

Async RL lets rollout workers keep generating while the learner updates from completed
trajectories.

Generate trajectories
Update policy

Rollout GPU 1

Rollout GPU 2

Learner GPU

Generate

Generate

Generate

Generate

Update 1

Generate

Generate

Update 2

Time →

Some completed trajectories now come from an earlier policy version.

AReaL · Fu et al., 2026 · §4.1 ↗
20

### Page links

- [Link 1](../optional-readings/arxiv-2505-24298.md)

## Page 21

Stable policy updates

21

## Page 22

Rollouts from an older policy

A rollout can finish after the learner has updated to a newer policy.

Rollout policy μ
Learner policy πθ

Check None explicitly

Use get(..., 3)

Keep the original code

μ: sampled the recorded edit.
πθ: is being updated now.

The rollout is stale: its actions came from μ, while the learner uses πθ.

0.40

0.70

0.40

0.20

0.20

0.10

22

## Page 23

Importance sampling

At a fixed history h, reweight a sampled action a by how likely it is under the current
policy.

At a fixed history h

Correct edit

Behavior: 0.40
Current: 0.70

Weight: 0.70 / 0.40 = 1.75

Incomplete edit

Behavior: 0.40
Current: 0.20

Weight: 0.20 / 0.40 = 0.50

R(a) is the final reward after taking action a in this example.

E

​\[R(a)\] =
a∼π
​θ
E

​
​R(a)
a∼μ\[ μ(a ∣h)

π
​(a ∣h)
θ
\]

23

## Page 24

Long trajectories and stale data

The whole-trajectory ratio w multiplies local mismatches along an agent interaction.

Action a_t follows history h_t; environment dynamics are unchanged

1.05

One action ratio
→

1.05¹⁰⁰ ≈ 132

Product along a
trajectory

→

High variance

A few samples can
dominate

w(τ ∣x) =
​ =
p
​(τ ∣x)
μ

p
​(τ ∣x)
θ

​
​

t
∏μ(a
​ ∣h
​)
t
t

π
​(a
​ ∣h
​)
θ
t
t

CTPO · Zhang et al., 2026 · §3.2 ↗
24

### Page links

- [Link 1](../optional-readings/arxiv-2605-07331.md)

## Page 25

Mismatch grows along a response

The cumulative ratio ρ
 multiplies action ratios through token t.

Its spread grows at later positions in tool-using math rollouts.

tcum

CTPO · Zhang et al., 2026 · Fig. 1 ↗
25

### Page links

- [Link 1](../optional-readings/arxiv-2605-07331.md)

## Page 26

Earlier actions change later histories

The current policy may rarely reach a history that the rollout policy visited.

Earlier edit

Add a None check

μ: 40%   πθ: 10%

→

Recorded history

The code now has that

check
→

Next action

Run tests

μ: 50%   πθ: 50%

The next-action ratio is 1, but reaching this history is 0.10 / 0.40 = 0.25 as likely.

CTPO · Zhang et al., 2026 · §3.1 ↗
26

### Page links

- [Link 1](../optional-readings/arxiv-2605-07331.md)

## Page 27

Which actions enter the weight?

For a response with T actions, ρ  is the probability ratio for action t. Methods use
different parts of the response.

Method
Recorded actions →
Weight uses

PPO / GRPO
a
a
a
a
a
Current action

CTPO
a
a
a
a
a
Actions through t

Full ratio
a
a
a
a
a
All actions

GSPO
a
a
a
a
a
All, length-normalized

DAPO and CISPO also use the current-action ratio; their clipping rules differ.

t

0
1
t
t+1
T−1

0
1
t
t+1
T−1

0
1
t
t+1
T−1

0
1
t
t+1
T−1

CTPO · Zhang et al., 2026 · Table 1 ↗
DAPO · Yu et al., 2025 ↗
CISPO · MiniMax-M1, 2025 ↗
27

### Page links

- [Link 1](../optional-readings/arxiv-2503-14476.md)
- [Link 2](../optional-readings/arxiv-2506-13585.md)
- [Link 3](../optional-readings/arxiv-2605-07331.md)

## Page 28

Clipping policy updates

28

## Page 29

Why limit an update?

Stale rollouts can get large weights, letting a few samples dominate an update.

Image Credit: Aditya Soni ↗
29

### Page links

- [Link 1](http://localhost:12445/images/importance-weights.png)

## Page 30

Clipping a probability ratio

The clip function replaces a ratio outside the chosen bounds with the nearest bound.

Here each action is a generated token u ; u  is its earlier context.

Ratio for one sampled token

Clipped value: ℓ is lower, u is upper

ℓ = 0.8
u = 1.2
ratio ρₜ

0.8

1.2

clipped value cₜ

t
<t

ρ
​ =
t

​
μ(u
​ ∣u
​)
t
<t

π
​(u
​ ∣u
​)
θ
t
<t

c

​ =
t
clip(ρ

​, ℓ, u)
t

PPO · Schulman et al., 2017 ↗
CISPO · MiniMax-M1, 2025 ↗
30

### Page links

- [Link 1](../optional-readings/arxiv-1707-06347.md)
- [Link 2](../optional-readings/arxiv-2506-13585.md)

## Page 31

PPO and CISPO policy objectives

PPO puts c  inside a minimum; CISPO uses it as a fixed weight.

Shared clipped ratio

PPO policy objective to maximize

CISPO policy objective to maximize

E  averages sampled tokens; Â  estimates whether a token helped. sg holds c  fixed for gradients. A loss to
minimize is −J.

t

c

​ =
t
clip(ρ

​, ℓ, u)
t

J

​(θ) =
PPO
E

​ min ρ

​
​, c

​
​
t\[
( tA^t
tA^t)\]

J

​(θ) =
CISPO
E

​ sg(c

​)

​ log π

​(u

​ ∣u

​)
t\[
t A^t
θ
t
<t \]

t
t
t

PPO · Schulman et al., 2017 ↗
CISPO · MiniMax-M1, 2025 ↗
31

### Page links

- [Link 1](../optional-readings/arxiv-1707-06347.md)
- [Link 2](../optional-readings/arxiv-2506-13585.md)

## Page 32

PPO’s clipped objective

PPO stops rewarding increases above the cap and decreases below the floor.

Positive advantage: A = +1

1.2
ratio

No extra gain above the cap

Negative advantage: A = −1

0.8
ratio

No extra gain below the floor

For a helpful action, stop rewarding a ratio above
1 + ε.

For an unhelpful action, stop rewarding a ratio
below 1 − ε.

In this plot, ε = 0.2 is the clipping margin.

Adapted from PPO · Schulman et al., 2017 · Figure 1 ↗
32

### Page links

- [Link 1](../optional-readings/arxiv-1707-06347.md)

## Page 33

Reference-model KL

A KL penalty discourages the policy from drifting far from a fixed reference model.

Policy objective with a reference penalty

Rollout policy μ

Generates the training batch and
supplies the denominator in importance

ratios.

Reference model π

Stays fixed as an anchor while the policy
learns.

J
 is the policy objective; D
 measures distribution difference; β sets the penalty strength.

​ J

​ −
θ
max
policy
β D

​(π

​∥π

​)
KL
θ
ref

ref

policy
KL

DeepSeekMath · Shao et al., 2024 · GRPO objective ↗
33

### Page links

- [Link 1](../readings/arxiv-2402-03300.md)

## Page 34

Entropy for exploration

An entropy bonus rewards a broader next-token distribution.

Policy objective with an entropy bonus

H measures next-token uncertainty; α sets the bonus strength.

A broader distribution can help the agent try other actions.

It does not guarantee that those actions will be useful.

​ J

​ +
θ
max
policy
α H(π

​)
θ

Proximal Policy Optimization · Schulman et al., 2017 · §5 ↗
34

### Page links

- [Link 1](../optional-readings/arxiv-1707-06347.md)

## Page 35

A summary of popular algorithms

Compare how each method assigns credit, weights sampled tokens, and limits updates.

Algorithm
Weight from reward
Learned
critic?
Importance ratio
Clipping

REINFORCE
Reward-to-go R
No
None: fresh rollouts
None

PPO
GAE from a critic
Yes
Current token ρ
Minimum of raw and
clipped terms

GRPO
Group comparison
No
Current token ρ
Same as PPO

CISPO
Group comparison
No
Current token ρ
Clipped ratio as a fixed
weight

GSPO
Group comparison
No
Whole response,
length-normalized

PPO minimum, on the
response ratio

DAPO
Group comparison
No
Current token ρ
PPO minimum;
higher upper bound

Group comparison: subtract the group’s mean reward, then divide by its reward spread.

t

t

t

t

t

PPO ↗
GRPO ↗
CISPO ↗
GSPO ↗
DAPO ↗
35

### Page links

- [Link 1](../optional-readings/arxiv-1707-06347.md)
- [Link 2](../readings/arxiv-2402-03300.md)
- [Link 3](../optional-readings/arxiv-2503-14476.md)
- [Link 4](../optional-readings/arxiv-2506-13585.md)
- [Link 5](../optional-readings/arxiv-2507-18071.md)

## Page 36

Task selection and

reward reliability

36

## Page 37

Uninformative rollout groups

Sample four trajectories per task. Each group below shows their final rewards.

All attempts failed

0
0
0
0

Mean reward: 0
Subtract the mean:

0, 0, 0, 0

Mixed outcomes

0
1
0
1

Mean reward: 0.5
Subtract the mean:

−0.5, +0.5, −0.5, +0.5

All attempts passed

1
1
1
1

Mean reward: 1
Subtract the mean:

0, 0, 0, 0

Recall group advantages: subtract the group's mean reward. Equal rewards all become zero.

An all-zero group gives no outcome comparison. Why did every trajectory fail?

37

## Page 38

Why did every trajectory fail?

Four failed trajectories give the same rewards: 0, 0, 0, 0. Inspect what happened before
choosing a remedy.

Verifier quality

A valid solution might be
rejected.

Check: the requirements and
failed tests.

Current capability

The model may not yet be
able to solve the task.

Check: whether stronger-
model demonstrations
succeed.

Lack of exploration

All attempts may repeat the
same approach.

Check: whether the
trajectories differ.

38

## Page 39

False negatives in the verifier

Return to the bug-fix task. This candidate produces every required output.

Missing → 3 ✓
None → 3 ✓

0 → 0 ✓
2 → 2 ✓

Candidate behavior

All four cases are correct.

Its implementation uses different source
code.

Verifier rule

Require the exact phrase

value is None .

The candidate lacks it: reject.

This is a false negative: a valid solution is rejected. Check behavior instead of an incidental wording
choice.

Related task/test review: SWE-bench Verified · 2024 ↗
39

### Page links

- [Link 1](../optional-readings/ref-e1f512a932de.md)

## Page 40

Result of false negatives

Reward noise

Fitting to spurious changes in the output.

Equivalent solutions receive different rewards because of wording or implementation details.

Benchmark saturation
Scores can flatten below 100% when the evaluator rejects valid solutions.

Benchmark
Plateau / limit
Evidence from the audit

SWE-bench Verified
≈81%
Progress slowed near 80.9%; many remaining
failures had flawed tests.

τ-bench Airline
≈70%
Inconsistent tasks limited achievable scores.

τ-bench Retail
≈92%
Annotation errors limited achievable scores.

Historical versions, audited in 2025–26. These are reported plateaus or limits; τ-bench has since corrected the tasks.

SWE-bench audit · OpenAI, Feb. 2026 ↗
SABER · Cuadron et al., 2025 · §5.1 ↗
τ-bench fixes · Feb. 2026 ↗
40

### Page links

- [Link 1](../optional-readings/arxiv-2512-07850.md)
- [Link 2](../optional-readings/ref-a09fb6fd80e8.md)
- [Link 3](../optional-readings/ref-197ad5ccda9a.md)

## Page 41

False positives and reward hacking

Keep the same task requirements, but suppose training tests only the input retries=0.

def retry_count(config):

return 0

Candidate: always return zero.

Training verifier

The one tested case passes.

Reward: 1

Input
Required output
Candidate output

0
0
0 ✓

Missing / None
3
0 ✗

2
2
0 ✗

A false positive rewards an invalid solution. Training can learn to exploit this gap.

41

## Page 42

Reward hacking in coding agents

A passing score can come from a shortcut that the benchmark was meant to exclude.

Available in the environment
Shortcut

Internet access
→
Find the published solution online.

Git history, including future
commits
→
Find and copy the later bug fix.

A model API key
→
Call a different, stronger model for answers or
training data.

Access to tests or the test
runner
→
Make the tests pass without fixing the bug.

Documented API example: a PostTrainBench agent used a grading key to generate training data, despite an
explicit restriction.

Web, Git, and test exploits · MAI-Thinking-1 · §3.3.1, p.43 ↗
API misuse · PostTrainBench · §5.4, Fig.7 ↗
42

### Page links

- [Link 1](../optional-readings/arxiv-2603-08640.md)
- [Link 2](../optional-readings/ref-1b4125b5ee25.md)

## Page 43

Independent checks of progress

The constant-zero patch earned training reward 1, but passed only one of the four
required cases.

Training reward

Measures success on the
training verifier

Independent success

Check unseen tasks and
behavior the training
verifier missed

Costs and failures

Inspect tool calls,
regressions, and repeated
actions

If reward rises without independent improvement, inspect trajectories for shortcuts.

43

## Page 44

DAPO: dynamic sampling

Identical rewards give zero group advantages. DAPO keeps mixed groups and samples
until the batch is full.

Sample four trajectories per task

Each circle is a reward: 0 = failure, 1 = success.

Task A
0
0
0
0
Skip group
Identical rewards

Task B
0
1
0
1
Keep group
Mixed rewards

Task C
1
1
1
1
Skip group
Identical rewards

Task D
New group
0
0
1
0
Keep group
Mixed rewards

→

Training batch

Example target: 2 groups

2 / 2 groups collected

Task B
0
1
0
1

Task D
0
0
1
0

Batch full → update the policy

Keep every trajectory in a mixed group, including its failures.

DAPO · Yu et al., 2025 · §3.2 Dynamic Sampling ↗
44

### Page links

- [Link 1](../optional-readings/arxiv-2503-14476.md)

## Page 45

Partial and auxiliary rewards

Partial credit is an auxiliary reward: extra feedback for progress before full success.

Illustrative task: pass all 4 checks. Add 0.25 reward per check passed.

Four trajectories on the same task
τ₁
τ₂
τ₃
τ₄

Checks passed
0 / 4
1 / 4
2 / 4
1 / 4

Success reward
0
0
0
0

Subtract the mean: 0
0
0
0
0

Success + partial reward
0
0.25
0.50
0.25

Subtract the mean: 0.25
−0.25
0
+0.25
0

Different partial scores can reduce zero-advantage groups and batches.

45

## Page 46

Risks of auxiliary rewards

The model may learn to increase the added reward without improving the task.

Intended behavior
What the reward favored
Observed behavior

Useful tool use
A bug gave credit for
superficial web-tool calls.

GPT‑5.1 used the browser as a
calculator and acted as though it
had searched.

A playful “Nerdy”
persona

Metaphors with “goblin”
or “gremlin” received
higher scores.

Creature metaphors became
more common, including without
the persona prompt.

Calculator hacking · OpenAI, Dec. 2025 ↗
Where the goblins came from · OpenAI, Apr. 2026 ↗
46

### Page links

- [Link 1](../optional-readings/ref-34e4d5c322dc.md)
- [Link 2](../optional-readings/ref-f36ea610aa8e.md)

## Page 47

Exploration collapse

At one history, training changes the probabilities of three possible actions.

Earlier policy
Later policy

Action A

Action B

Action C

Almost every sample now chooses B, so alternatives are rarely tried.

An entropy bonus encourages alternatives; check whether trajectories differ.

0.20

0.01

0.60

0.98

0.20

0.01

DAPO · Yu et al., 2025 · exploration and entropy collapse ↗
47

### Page links

- [Link 1](../optional-readings/arxiv-2503-14476.md)

## Page 48

Learning from a teacher

Distillation: match a teacher's action probabilities

48

## Page 49

Curricula and warm starts

When the student rarely succeeds, a teacher can provide successful trajectories to learn
from.

Demonstrations

First learn from
successful solutions

A warm start

→

Learnable tasks

Practice tasks where
the model sometimes
succeeds

→

Harder tasks

Increase difficulty as
the model improves

A curriculum

Keep earlier tasks in the mix, and use a fixed evaluation set to measure improvement.

49

## Page 50

Distillation

Train a student to match a teacher’s action probabilities on a fixed set of trajectories.

Saved trajectory from the teacher

h
a  →
h
a  →
h
a  →
h

next action here

At this saved history, the teacher assigns 80% to a  and 20% to the other action. Call
this distribution q(· | h ).

When the student acts, its own mistakes can lead to histories missing from this training set.

0
0
1
1
2
2
3

3

3

Knowledge distillation · Hinton et al., 2015 · §2 ↗
Distillation for language models · Agarwal et al., 2024 · §3 ↗
50

### Page links

- [Link 1](../optional-readings/arxiv-1503-02531.md)
- [Link 2](../optional-readings/arxiv-2306-13649.md)

## Page 51

On-policy distillation

Let the student generate the training histories, then ask the teacher for targets at those
histories.

Student rollout on trajectory B

h
a  →
h
a  →
h
a  →
h

next action here

Example teacher targets at this student history: 80% for a  and 20% for the other
action.

Train the student to match these probabilities. “On-policy” means the histories came from the student's
own rollouts.

0
0
1
1
2
2
3

3

On-Policy Distillation of Language Models · Agarwal et al., ICLR 2024 ↗
51

### Page links

- [Link 1](../optional-readings/arxiv-2306-13649.md)

## Page 52

A dense distillation objective

At the same h , suppose the student assigns equal probability to the two actions.

Next-action probabilities
a
Other action

Student π
0.5
0.5

Teacher q
0.8
0.2

Reverse KL measures probability mismatch (natural logarithms)

Average this KL mismatch over student histories (distribution d ), then minimize:

3

3

θ

0.5 log(0.5/0.8) + 0.5 log(0.5/0.2) ≈0.223

μ

L

​ =
OPD
E

​ D

​ π

​(⋅∣h)∥q(⋅∣h)
h∼d
​μ\[
KL(
θ
)\]

GKD · Agarwal et al., ICLR 2024 · choice of divergence ↗
52

### Page links

- [Link 1](../optional-readings/arxiv-2306-13649.md)

## Page 53

On-policy self-distillation

A verified solution can help a teacher give better targets at the student's own history.

Student rollout on trajectory B

h
a  →
h
a  →
h
a  →
h

next action here

Student input

The task and history h .

Teacher input

The same task and history,

plus a verified solution.

OPSD uses a frozen copy of the starting model as teacher. Its next-action probabilities train the student
as before.

0
0
1
1
2
2
3

3

Self-Distilled Reasoner · Zhao et al., 2026 · OPSD ↗
53

### Page links

- [Link 1](../optional-readings/arxiv-2601-18734.md)

## Page 54

Conclusion

54

## Page 55

RL takeaways

Useful feedback

Use group comparisons, a
critic, or process rewards
to assign credit.

Stable updates

Know the behavior policy;
control how strongly
samples change the
model.

Reliable rewards

Match task difficulty and
verify the behavior you
actually want.

55

## Page 56

Questions?

Next Class: RL Systems

56

## Page 57

Notation: the rollout

Symbol
Meaning

x, τ, T
Task; sampled trajectory; number of actions

h , a
History before step t; action at that step

u , u
Generated token at position t; earlier context

π , μ
Current policy; policy that generated the rollout

p (τ | x), p (τ | x)
Probability of the whole trajectory under each policy

R(τ), r
, R
Final reward; reward after a ; reward-to-go from h

t
t

t
<t

θ

θ
μ

t+1
t
t
t

57

## Page 58

Notation: learning signals

Symbol
Meaning

Â
Estimated advantage: how an action compares with expectation

ρ , c
One-token policy ratio; its clipped value

ρ
, w(τ | x)
Ratio through token t; ratio for the whole trajectory

V (h), V (h)
Expected reward-to-go under μ; the critic's estimate

δ
Reward plus next value, minus current value

γ, λ
Reward discount (examples use γ = 1); weight on later errors in
GAE

q, d
Teacher's target; histories collected by the student

t

t
t

tcum

μ
φ

t

μ

58
