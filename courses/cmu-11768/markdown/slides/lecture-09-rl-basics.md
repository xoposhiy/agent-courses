# Lecture 9 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-09-rl-basics.pdf) · [Raw file](../../raw/slides/lecture-09-rl-basics.pdf)

Retrieved: 2026-11-13T16:45:27.918446+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

RL Foundations for Agents

From SFT to policy gradients

Daniel Fried

11-768: AI Agents

1

## Page 2

Running example: Number Search

Four sample trajectories:

τ1
8
higher
12
lower
10
higher
11
correct
R = 1

τ2
4
higher
8
higher
12
lower
11
correct
R = 1

τ3
16
lower
8
higher
9
higher
10
timeout
R = 0

τ4
1
higher
2
higher
3
higher
4
timeout
R = 0

τ₁ and τ₂ different actions · same successful outcome

A hidden integer lies between 1 and 16. The agent has four guesses. After an incorrect guess, the
environment replies higher or lower. Reward is 1 only when it finds the number.

Hidden number for this task instance: 11

2

## Page 3

SFT on demonstrations

SFT trains the agent to maximize the probability of all target actions in a demonstration

history h₀

prompt →

target a₀*

guess 8 →

history h₁

higher →

target a₁*

guess 12→

history h₂

lower →

target a₂*

guess 10→

history h₃

higher →

target a₃*

guess 11

Target actions may come from a person, a stronger model, or (today) a successful trajectory from this agent

L
​ =
SFT
−
​log π
​(a
​ ∣

t
∑
θ
t
∗
h
​)
1:t

3

## Page 4

Task mismatch

SFT maximizes the probability of demonstrated actions. We would like to maximize the

probability that the agent carries out the task. (these are not quite the same!)

DEMONSTRATION

τ1
8
higher
12
lower
10
higher
11
correct

ANOTHER SUCCESS

τ2
higher
8
higher
12
lower
11
correct

There are multiple ways to carry out a task.

Some actions are worse than others (e.g. should never guess "13" after "12 -> lower").

4

4

## Page 5

Data mismatch

We'd like to be able to learn from sub-optimal data, too

DEMONSTRATION

τ1
8
higher
12
lower
10
higher
11
correct

OTHER ALTERNATIVES

τ2
4
higher
8
higher
12
lower
11
correct

τ3
16
lower
8
higher
9
higher
10
timeout

τ4
1
higher
2
higher
3
higher
4
timeout

5

## Page 6

Exposure bias

The agent was not exposed to its own mistakes at training time, and might not be prepared to

handle mistakes when generating

TRAINING
DEMONSTRATION
8
higher
12
lower
10
higher
11
correct

GENERATION
8
higher
?

6

2

## Page 7

Reinforcement learning

Generate actions/trajectories from the agent, evaluate their reward, and adjust the parameters

of the agent to maximize expected reward.

task instance

hidden
number 11

⇢
agent

πθ

Generate

→

τ1
8
higher
12
lower
10
higher
11
correct
R = 1

τ3
16
lower
8
higher
9
higher
10
timeout R = 0

Reward

Task mismatch
We train the agent to maximize expected reward.

Data mismatch
The agent can learn from all trajectories (seek high reward; avoid low reward)

Exposure bias
The agent generates trajectories in training (on-policy), so it learns to recover from errors

Update

Adapted from Sean Welleck · RL Fundamentals ↗
7

### Page links

- [Link 1](../optional-readings/ref-93d9a2493220.md)

## Page 8

Interactions as trajectories

8

## Page 9

The agent–environment loop

AGENT
Policy πθ

action a →

←observation o

←reward r

ENVIRONMENT
task instance x

Task instance x
Observation o
Action a
Reward r

Text generation
the prompt
tokens so far
next token
score from a judge model

Web agent
the task and
website
rendered page
click, type, scroll
number of sub-tasks
completed

Number Search
number (hidden)
higher, lower, or
correct
the next guess
1 on correct; otherwise 0

t

t+1

t+1

t+1
t
t+1

9

## Page 10

Trajectories

The agent conditions only on past actions and observations (not hidden environment state).

a₀
o₁
a₁
o₂

history h₂

what the policy conditions on

environment state s₂

hidden number 11

not visible

prompt →
guess 8
→
higher
→
guess 12 →
lower
→
guess 10 →
higher
→
guess 11 →
correct

a₂
o₃
a₃
o₄

h
​ =
t
(o
​, a
​, o
​, … , o
​)
π
​(a ∣
0
0
1
t
θ
t
h
​)
t

10

## Page 11

Trajectories

Trajectories can also include reward at each step.

a₀
o₁r₁=0
a₁
o₂r₂=0
a₂
o₃r₃=0
a₃
o₄r₄=1

trajectory τ₁

reward R(τ₁) = 1

In number search, 1 for "correct" and 0 otherwise.

prompt →
guess 8
→
higher
→
guess 12 →
lower
→
guess 10 →
higher
→
guess 11 →
correct

τ = (o
​, a
​, r
​, o
​, … , a
​, r
​, o
​)
R(τ) =
0
0
1
1
T−1
T
T

​ r
​
∑t=1

T

t

11

## Page 12

Trajectories

Trajectory probabilities depend on the policy and the environment.

a₀
o₁r₁=0
a₁
o₂r₂=0
a₂
o₃r₃=0
a₃
o₄r₄=1

p(o₀|x)
πθ(8|h₀)
P(o₁,r₁|…)
πθ(12|h₁)
P(o₂,r₂|…)
πθ(10|h₂)
P(o₃,r₃|…)
πθ(11|h₃)
P(o₄,r₄|…)

We don't know P, but we can sample from it by interacting with the environment.

prompt →
guess 8
→
higher
→
guess 12 →
lower
→
guess 10 →
higher
→
guess 11 →
correct

p
​(τ ∣
θ
x) =
​π
​(a
​ ∣

t
∏
θ
t
h
​) (o
​, r
​ ∣
t
t+1
t+1
h
​, a
​, x)
t
t

12

## Page 13

Objective: maximize expected reward

EXPECTED REWARD J OVER FOUR TRAJECTORIES

τ₁
0.30 × 1

τ₂
0.20 × 1

τ₃
0.25 × 0

τ₄
0.25 × 0
= 0.50

Training adjusts θ to maximize expected reward (i.e. the agent has a higher probability of high

reward trajectories)

low reward trajectories
probability mass →
high reward trajectories

J(θ) = E

​\[R(τ)\]
τ∼p
​(⋅∣x)
θ

13

## Page 14

Expert iteration

14

## Page 15

Reinforced self-training

ReST generates data from the policy, and then updates the policy using successful trajectories.

1
Grow
Sample trajectories from the current policy
and compute rewards.

2
Improve
Use rewards to filter the data; augment the
existing datasets; train the policy.

3
Repeat
Use the updated policy.

Gulcehre et al. · ReST, Fig. 1 ↗
Singh et al. · ReST-EM ↗
15

### Page links

- [Link 1](../readings/arxiv-2308-08998.md)
- [Link 2](../readings/arxiv-2312-06585.md)

## Page 16

Reinforced self-training

The loss is the standard SFT loss, on trajectories with high reward

τ1
8
higher
12
lower
10
higher
11
correct
R = 1

KEEP

τ2
4
higher
8
higher
12
lower
11
correct
R = 1

KEEP

sample trajectories

↓

compute rewards

↓

keep τ₁, τ₂

↓

SFT

τ3
16
lower
8
higher
9
higher
10
timeout R = 0

DROP

τ4
1
higher
2
higher
3
higher
4
timeout R = 0

DROP

L
​ =
ReST
−
​
​log π
​(a
​ ∣

τ: R(τ)=1

∑

t
∑
θ
t
h
​)
t

Gulcehre et al. · ReST ↗
Singh et al. · ReST-EM ↗
16

### Page links

- [Link 1](../readings/arxiv-2308-08998.md)
- [Link 2](../readings/arxiv-2312-06585.md)

## Page 17

From rewards to gradients

Policy gradients

17

## Page 18

How to maximize expected reward?

We can't use backpropagation directly: sampling and the environment are non-differentiable

PARAMETERS

θ
→

POLICY
πθ(a|h) ✕

SAMPLE
action a ✕

ENVIRONMENT
obs o, reward r

Sampled action
Changing θ changes the action probabilities, but
actions are discrete and sampled.

Task environment
The world is not (usually!) differentiable. How do you
take the derivative of a unit test w.r.t. code?

pθ(τ|x) changes with θ
R(τ) is observed after the rollout

General solution: policy gradient (REINFORCE, Williams 1992).

J(θ) =
​p
​(τ ∣

τ
∑
θ
x) R(τ)

18

## Page 19

Policy gradient

Maximize expected reward
under the policy.

Take the gradient: only the
probability depends on θ.

Multiply and divide by trajectory
probability.

Use ∇p / p = ∇ log p.

This is an expectation we can
estimate from samples.

J(θ) = E
​\[ R(τ) \] =
τ∼p
​(⋅∣x)
θ

​p
​(τ ∣

τ
∑
θ
x) R(τ)

∇

​J =
θ

​∇
​p

​(τ ∣

τ
∑
θ
θ
x) R(τ)

∇
​J =
θ

​p
​(τ ∣

τ
∑
θ
x) R(τ)
​
p
​(τ ∣x)
θ

∇
​p
​(τ ∣x)
θ
θ

∇
​J =
θ

​p
​(τ ∣

τ
∑
θ
x) R(τ) ∇
​ log p
​(τ ∣
θ
θ
x)

∇
​J =
θ
E
​\[ R(τ) ∇
​ log p
​(τ ∣
τ∼p
​(⋅∣x)
θ
θ
θ
x) \]

REINFORCE (Williams, 1992) ↗
19

### Page links

- [Link 1](../optional-readings/ref-fa03f3992632-pdf.md)

## Page 20

Policy gradient

Replace the expectation by trajectories we sample.

τ ∼ pθ(·|x)

Current-policy trajectories and
histories

obtain by sampling: policy and
environment

R(τ)

Task-level evaluation

obtain from the environment

∇θ log πθ(aₜ|hₜ)

Changes probabilities of sampled
actions

same mechanics as in SFT

∇
​J =
θ
E
​\[ R(τ) ∇
​ log p
​(τ ∣
τ∼p
​(⋅∣x)
θ
θ
θ
x) \]

τ ∼p
​(⋅∣
θ
x),
​ =
∇
​J
θ
R(τ) ∇
​ log p
​(τ ∣
θ
θ
x) = R(τ)
​∇
​ log π
​(a
​ ∣

t
∑
θ
θ
t
h
​)
t

Williams · REINFORCE, 1992 ↗
20

### Page links

- [Link 1](../optional-readings/ref-fa03f3992632-pdf.md)

## Page 21

Trajectory log probability

p(o₀|x) ·
πθ(a₀|h₀) ·
P(o₁,r₁|h₀,a₀,x) ·
πθ(a₁|h₁) ·
P(o₂,r₂|h₁,a₁,x)

Same computation as SFT: sum token log probabilities. Here the tokens were sampled by the policy.

t indexes actions; k indexes tokens within action a .

We can just multiply by R(τ) to get ∇̂θJ.

log p
​(τ ∣
θ
x) =
​log P(o
​, r
​ ∣

t
∑
t
t
h
​, a
​, x) +
t
t

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

= const +
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

∇
​ log p
​(τ ∣
θ
θ
x) =
​∇
​ log π
​(a
​ ∣

t
∑
θ
θ
t
h
​)
t

a
​ =
t
(u
​, … , u
​),
∇
​ log π
​(a
​ ∣
t,1
t,m

​t
θ
θ
t
h
​) =
t

​∇
​ log π
​(u
​ ∣

k=1
∑

m

​t

θ
θ
t,k
h
​, u
​)
t
t,<k

t

21

## Page 22

Computing the policy gradient

Effectively, we just do masking and rescaling of the standard SFT loss computation.

<|im_start|>user
↵
Find·the·number·in·1–16.
↵
<|im_end|>
↵
<|im_start|>assistant
↵

guess(8)
↵
<|im_end|>
↵
<|im_start|>tool
↵
higher
↵
<|im_end|>
↵

<|im_start|>assistant
↵
guess(12)
↵
<|im_end|>
↵
…
↵
<|im_start|>assistant
↵

guess(11)
↵
<|im_end|>

“·” = space, “↵” = newline · colored = sampled by the policy, gray = context only

m  = 1

tokens the policy sampled, including the
end-of-turn token

m  = 0

prompt and observation tokens, which the
policy did not choose

R(τ)

one scalar, shared by every generated
token in the trajectory

L
​ =
PG
−R(τ)
​log π
​(u
​ ∣

t : m
​=1
t
∑
θ
t
u
​)
<t

t
t

22

## Page 23

Policy-gradient training loop

After an update, the new policy collects the next batch.

1
Collect

Sample task
instances; sample
from the agent on
them.

→

2
Evaluate

Compute rewards
for each trajectory. →

3
Form loss

Weight action log
probabilities by
reward.

→

4
Update

Backpropagate,
change θ, collect
again.

↺

L
​ =
PG
−
​R(τ
​)
​log π
​(a
​ ∣

i
∑
i

t
∑
θ
i,t
h
​)
i,t

23

## Page 24

With binary rewards, this looks a lot like ReST

REINFORCE

=

SFT loss on the successful trajectories

(there are some differences, e.g. ReST does batched updates and aggregates datasets)

−
​R(τ
​)
​log π
​(a
​ ∣

i
∑
i

t
∑
θ
i,t
h
​)
i,t
−
​
​log π
​(a
​ ∣

i:R(τ
​)=1
i
∑

t
∑
θ
i,t
h
​)
i,t

Williams · REINFORCE ↗
Singh et al. · ReST-EM ↗
24

### Page links

- [Link 1](../readings/arxiv-2312-06585.md)
- [Link 2](../optional-readings/ref-fa03f3992632-pdf.md)

## Page 25

Better than expected

Baselines and advantages

25

## Page 26

Rewards should be relative

τ₁

All actions get upweighted.

τ₃

In basic REINFORCE, as in ReST, this produces no gradient at all!

The update should depend on how well the policy usually does on this example.

guess 8

← R=1

higher
guess 12

← R=1

lower
guess 10

← R=1

higher
guess 11

← R=1

correct

guess 16

← R=0

lower
guess 8

← R=0

higher
guess 9

← R=0

higher
guess 10

← R=0

timeout

26

## Page 27

Advantages

Advantage: how much better is this action, than the policy's average?

History h: guess 8 / higher · guess 12 / lower — the number is 9, 10 or 11, with two guesses left.

Neither Qπ nor Vπ is known, so we estimate advantage from the sampled reward.

A (h, a) =
π

​ −

expected reward after a

​
Q (h, a)
π

​

expected reward from h

​
V (h)
π

guess 11

if wrong, two candidates and one

guess left

Aπ(h,11) < 0

Vπ(h)

guess 10

if wrong, one candidate and one

guess left

Aπ(h,10) > 0

​ =
A^t
−

trajectory reward

​
R(τ)

​

an estimate of V (h
​)
π
t

​
b(h

​)
t

27

## Page 28

Policy gradients with advantage estimates

Incorporate advantages by recentering the reward.

REINFORCE: one trajectory
reward weights every action.

Subtract a baseline — the weight
is now Âₜ.

Both lines are different ways to estimate the same ∇θJ.

Âₜ = R(τ) − b(hₜ). Different choices for b produce different algorithms

a constant

upcoming bandit example

a running mean of
rewards

adapts as the policy improves

Vφ(hₜ)

a trained value model: actor–critic,
PPO

the group mean

no extra model: GRPO (next
section)

​ =
∇
​J
θ
R(τ)
​∇
​ log π
​(a
​ ∣

t
∑
θ
θ
t
h
​)
t

​ =
∇
​J
θ

​
​ ∇
​ log π
​(a
​ ∣

t
∑

​
A^t

​
(R(τ) −b(h
​))
t
θ
θ
t
h
​)
t

28

## Page 29

Baselines do not bias the gradient estimator

So E\[∇̂θJ\] = ∇θJ for any baseline that conditions only on the history

=
∇
​J
θ

​ (R(τ) −
∑t
b(h
​)) ∇
​ log π
​(a
​ ∣
t
θ
θ
t
h
​)
t

so this is an unbiased estimate of J's gradient if the expectation is 0
E\[
​\] =
∇
​J
θ
∇
​J −
θ
E\[
​ b(h
​) ∇
​ log π
​\]
∑t
t
θ
θ

E
​\[b(h)∇
​ log π
​(a ∣
a∼π
​(⋅∣h)
θ
θ
θ
h)\]

= b(h)
​ π
​(a ∣
∑a
θ
h)∇
​ log π
​(a ∣
θ
θ
h)

= b(h)
​ ∇
​π
​(a ∣
∑a
θ
θ
h)
π∇logπ = ∇π

= b(h)∇
​
​ π
​(a ∣
θ ∑a
θ
h) = b(h)∇
​1 =
θ
0

29

## Page 30

Simple example: two-armed bandit

With one policy parameter and two actions, we can compute gradients exactly.

0.0

0.5

1.0

p = πθ(guess A)

−4
0
2
4

θ

p = 0.25

θ = −1.1

an update moves θ

The sigmoid σ turns the single real number θ into a probability.

guess A
p = σ(θ) = 0.25
reward 1

guess B
1 − p = 0.75
reward 0

Raising θ raises p(guess A) and lowers p(guess B)

sampled guess A · reward 1

reward R(τ)

R = 1
×

slope ∂/∂θ log π (a)

1 − p = +0.75
=

gradient on θ

+0.75

if we sample A, A becomes more likely

sampled guess B · reward 0

reward R(τ)

R = 0
×

slope ∂/∂θ log π (a)

−p = −0.25
=

gradient on θ

0

if we sample B, nothing happens

This gradient is correct, but a baseline/advantage can make it more useful.

θ
θ

30

## Page 31

Simple example: Adding a baseline

Subtracting a baseline says whether a reward was better or worse than expected.

guess A
p = σ(θ) = 0.25
reward 1
guess B
1 − p = 0.75
reward 0

sampled guess A · reward 1

advantage Â = R − b
1 − 0.5 = +0.5
×

slope ∂/∂θ log π (a)

1 − p = +0.75
=

gradient on θ
+0.375

without a baseline: +0.75

increases p(guess A)

sampled guess B · reward 0

advantage Â = R − b
0 − 0.5 = −0.5
×

slope ∂/∂θ log π (a)

−p = −0.25
=

gradient on θ
+0.125

without a baseline: 0

increases p(guess A), so decreases p(guess B)

The baseline adds a learning signal from failure while preserving the expected gradient.

reward 0
baseline b(h₀) = 0.5
reward 1

worse than expected · Â < 0
Â > 0 · better than expected

θ
θ

31

## Page 32

Simple example: varying the baseline

Changing the baseline changes the variance of the gradient estimate, while keeping the

expectation the same

b = 0
b = 0

prob 0.75
ĝ = 0.125

prob 0.25
ĝ = 0.375

0
0.25
0.5
0.75

E\[ĝ\] = 0.1875

one sampled gradient estimate ĝ = (R − b)·∇θ log πθ(a)

baseline b
0.50
SD of ĝ
0.108

32

## Page 33

Simple example: noise in the gradient estimate

Computed a running estimate of the gradient by repeated sampling, with no baseline and with

baseline 0.5.

latest sample
guess B
gives ĝ = no baseline 0.000 with baseline 0.125

gradient estimate ĝ

0

0.125

0.375

0.75

5
10
15
20
samples drawn

true gradient 0.1875

no baseline spread SD 0.325 running average 0.188
baseline b = 0.5 spread SD 0.108 running average 0.188

Draw a sample
Draw 5
Clear
20 of 20 samples

Both averages converge to the same value, but the baseline has lower variance.

33

## Page 34

Baselines and credit assignment

What are the advantages of baselines (so far)?

Helps

Marks a trajectory as better or worse than
expected.

A good baseline reduces gradient variance.

Does not solve

All actions have the same advantage Â.

Estimating Vπ(h) may require a separate value
model.

Â = +0.5
guess 8
guess 12
guess 10
guess 11

34

## Page 35

What if we have intermediate rewards?

If the environment gives rewards before the final step, use reward-to-go to reduce variance.

→
→
action aₜ →
action →
terminal reward +1

included in Rₜ

An action is weighted only by the
rewards that come after it.

Earlier rewards do not depend on
aₜ, so dropping them cuts variance
without adding bias.

Number Search pays out once, at
the end: Rₜ = R(τ) for every action.

R

​ =
t

​r

​

t =t+1
′

∑

T

t′

action
tool reward +0.2

ignored

35

## Page 36

Comparing trajectories

Group-relative advantage estimates

36

## Page 37

Group-relative advantage estimates

Advantages: how much better is this trajectory than expected? We can compute this by

sampling the policy multiple times. No separate model needed!

reward

Rⱼ

centered

Rⱼ−R̄

divide by

σR

advantage

Âⱼ

τ1
8
higher
12
lower
10
higher
11
correct
1
+0.5
÷0.5
+1

τ2
4
higher
8
higher
12
lower
11
correct
1
+0.5
÷0.5
+1

τ3
16
lower
8
higher
9
higher
10
timeout
0
−0.5
÷0.5
−1

τ4
1
higher
2
higher
3
higher
4
timeout
0
−0.5
÷0.5
−1

from the group
R̄ = 0.5
σR = 0.5

b(h
​) =
t
=
Rˉ

​
​ R(τ
​)
for every h
​ in the group
G

1 ∑j=1

G

j
t

​ =
A^j

​,
=
σ
​
R

R(τ
​) −
j
Rˉ

Rˉ
b(h
​),
σ
​ =
t
R
std{R(τ
​), … , R(τ
​)}
1
G

37

## Page 38

The GRPO update

Batches contain multiple task instances, each with its own group.

task instance
rewards of the G rollouts
group mean
advantage estimates Âᵢⱼ

x₁ · hidden 11
1
1
0
0
R̄₁ = 0.50
+1
+1
−1
−1

x₂ · hidden 3
1
0
0
0
R̄₂ = 0.25
+1.73 −0.58 −0.58 −0.58

x₃ · hidden 7
1
1
1
0
R̄₃ = 0.75
+0.58 +0.58 +0.58 −1.73

policy-gradient loss · i indexes the batch

→

GRPO loss · i batch, j group

Each task instance has its
own R̄ᵢ and σᵢ.

Each task instance is normalized
individually.

GRPO supplies group-relative weights to the same
policy-gradient term.

−
​R(τ

​)
​log π

​(a

​ ∣

i
∑
i

t
∑
θ
i,t
h

​)
i,t
−
​
​
​
​
​log π

​(a

​ ∣

i
∑G

1

j=1
∑

G

A^ij

t
∑
θ
ij,t
h

​)
ij,t

Written for current-policy trajectories, without the paper's ratio, clipping, or KL terms.
Shao et al. · DeepSeekMath, §4.1.2 ↗
38

### Page links

- [Link 1](../readings/arxiv-2402-03300.md)

## Page 39

DrGRPO’s two changes

DrGRPO removes the group-standard-deviation and response-length divisions.

GRPO
DrGRPO
Why it changes

Advantage
estimate

is measured inside each group, so it differs from one task

instance to the next. Instances the policy almost always passes
or almost always fails have a small 
, so they count for more.

Response
aggregation

differs from one response to the next. A long incorrect

response is penalized less per token than a short one, so the
policy drifts toward longer wrong answers.

C is a global constant, the same for every response; the paper uses the generation budget.

Rewards stay fixed; the relative weights of task instances and responses change.

​
σ
​
R

R
​ −
j
Rˉ

R
​ −
j
Rˉ

σ
​
R

σ

​
R

​
​(⋅)
∣y
​∣
j

1

t
∑
​
​(⋅)
C

1

t
∑

∣y
​∣
j

Liu et al. · DrGRPO, Fig. 1 and §3.2 ↗
39

### Page links

- [Link 1](../readings/arxiv-2503-20783.md)

## Page 40

Token coefficients in DrGRPO

For one task instance, every generated token in trajectory j shares that trajectory's advantage

estimate.

τ₁

Â₁ = +0.5

<|im_start|>assistant
↵
guess(8)
↵
<|im_end|>
↵
<|im_start|>tool
↵

higher
↵
<|im_end|>
↵
…
↵
<|im_start|>assistant
↵
guess(11)
↵

<|im_end|>

PER TOKEN

+0.5 / C

τ₃

Â₃ = −0.5

<|im_start|>assistant
↵
guess(16)
↵
<|im_end|>
↵
<|im_start|>tool
↵

lower
↵
<|im_end|>
↵
…
↵
<|im_start|>assistant
↵
guess(10)
↵

<|im_end|>

PER TOKEN

−0.5 / C

Âⱼ = R(τⱼ) − R̄, with no division by σR.
Simplified: the paper's objective also has a ratio and clipping.

L
​ =
DrGRPO
−
​
​
​
​
​ log π
​(u
​ ∣
G

1

j=1
∑

G

C

1

t : m
​=1
j,t
∑
A^j
θ
j,t
u
​)
j,<t

Liu et al. · DrGRPO, §3.2 ↗
Shao et al. · DeepSeekMath, Eq. 3 ↗
40

### Page links

- [Link 1](../readings/arxiv-2402-03300.md)
- [Link 2](../readings/arxiv-2503-20783.md)

## Page 41

Equal rewards and zero advantage estimates

When every reward in a group matches, the group is degenerate and contributes no gradient.

ALL TRAJECTORIES FAIL

\[0, 0, 0, 0\]
→
\[0, 0, 0, 0\]

possibly too hard for the current policy

ALL TRAJECTORIES SUCCEED

\[1, 1, 1, 1\]
→
\[0, 0, 0, 0\]

possibly too easy for the current policy

What could we change if every sampled trajectory fails?

Choose different task instances, broaden exploration, add demonstrations, or supply a more

informative reward.

41

## Page 42

GRPO vs PPO

GRPO was proposed as a more efficient alternative to PPO, which uses a separate model to

estimate the advantage baseline.

PPO trains a value model

GRPO computes group-relative advantages

The advanced RL lecture covers ratios, clipping, and reference-model terms.
Shao et al. · DeepSeekMath, Fig. 4 and §4.1.2 ↗
42

### Page links

- [Link 1](../readings/arxiv-2402-03300.md)

## Page 43

Summary

43

## Page 44

Comparing the methods we’ve seen so far

Every method today weights the actions the agent took. They (mainly) differ in the weight.

ReST-EM
wₜ = 1 on a successful trajectory, 0 on the rest (the SFT loss on what was kept)

REINFORCE
wₜ = R(τ), the reward of the trajectory the action came from

GRPO/DrGRPO
wₜ = Â , the reward relative to the other rollouts on the same task instance

τ1
8
higher
12
lower
10
higher
11
correct
R = 1

τ2
4
higher
8
higher
12
lower
11
correct
R = 1

τ3
16
lower
8
higher
9
higher
10
timeout
R = 0

τ4
1
higher
2
higher
3
higher
4
timeout
R = 0

​ =
∇
​J
θ

​ w
​ ∇
​ log π
​(a
​ ∣
∑t
t
θ
θ
t
h
​)
t

j

44

## Page 45

Takeaways

Sampling trajectories from the policy and weighting them by reward addresses the three

problems we started with.

Task mismatch

The objective is expected reward, so any trajectory that succeeds is reinforced.

Data mismatch

The agent can also learn from sub-optimal trajectories, based on their reward.

Exposure bias

The trajectories come from the current policy, so the agent is trained to recover from its own mistakes.

45

## Page 46

Questions?

Upcoming: async RL / off-policy data, importance weighting

46
