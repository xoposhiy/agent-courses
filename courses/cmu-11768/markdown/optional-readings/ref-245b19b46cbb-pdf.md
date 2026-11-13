# MaxRL (PDF)

[Course index](../../README.md) · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tajwar26a/tajwar26a.pdf) · [Raw file](../../raw/optional-readings/ref-245b19b46cbb-pdf.pdf)

Retrieved: 2026-11-13T16:59:54.362882+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Maximum Likelihood Reinforcement Learning

Fahim Tajwar * 1 Guanning Zeng * 1 Yueer Zhou 2 Yuda Song 1 Daman Arora 1 Yiding Jiang 1 Jeff Schneider 1

Ruslan Salakhutdinov 1 Haiwen Feng 3 4 Andrea Zanette 1

Abstract

Reinforcement learning (RL) is the method of
choice for training models in setups where the
objective function can only be evaluated by sam-
pling from the model. Our key observation is that
when the feedback is terminal and binary, models
implicitly induce a likelihood over correct roll-
outs. Maximum likelihood would be the natural
framework in such settings, but RL is used in-
stead as a workaround to the non-differentiability.
We prove that the standard, expected-reward RL
formulation is only a first-order approximation
of the likelihood. To remedy this mismatch, we
introduce Maximum Likelihood Reinforcement
Learning (MaxRL), a compute-indexed family
of sample-based objectives that interpolate be-
tween expected-reward RL and maximum like-
lihood as sampling compute is scaled. The re-
sulting objective is a one-line change to standard
RL implementations. MAXRL Pareto-dominates
existing methods in all tested models and tasks,
achieves up to 20× gains in test-time scaling ef-
ficiency over GRPO, and scales more favorably
with additional training data and compute.

1. Introduction

Maximum likelihood (ML) and reinforcement learning (RL)
are two highly successful optimization paradigms that sig-
nificantly shaped the landscape of modern machine learning.
Maximum likelihood training is a foundational principle
behind modern generative and predictive models (Bishop,
2006; Murphy, 2012); in fully differentiable settings, op-
timizing log-likelihood objectives has reliably translated
increases in model capacity, data, and compute into consis-

*Equal contribution
1Carnegie Mellon University 2Stanford
University
3UC Berkeley
4Impossible,
Inc.
Correspon-
dence to:
Fahim Tajwar <ftajwar@andrew.cmu.edu>, Guan-
ning
Zeng
<guanninz@andrew.cmu.edu>,
Andrea
Zanette
<azanette@andrew.cmu.edu>.

Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).

tent performance improvements (Krizhevsky et al., 2012;
Radford et al., 2018). Reinforcement learning, by con-
trast, originated in optimal control and sequential decision-
making (Bertsekas, 1995; Sutton et al., 1998), where learn-
ing proceeds through interaction with an environment and
the objective is to maximize expected return. The gener-
ality of this formulation enables reinforcement learning to
address problems involving non-differentiable intermediate
sampling, and has led to models capable of superhuman
performance in complex domains (Mnih et al., 2015; Silver
et al., 2016; OpenAI et al., 2019; Vinyals et al., 2019).

Many modern learning problems are typically addressed
with reinforcement learning even if they define an im-
plicit likelihood over successes. Examples include navi-
gation (Thrun et al., 2005; Anderson et al., 2018), program
synthesis (Chen et al., 2018; Bunel et al., 2018), structured
prediction (Smith, 2011; Mensch & Blondel, 2018), and
multi-step reasoning in large language models (Wei et al.,
2022; Guo et al., 2025). In these tasks, success is determined
by an external verifier only after a stochastic generation
process, yielding a binary outcome. From an end-to-end per-
spective, the model induces a probability of success for each
input, defining an implicit likelihood over correctness. Max-
imizing this likelihood would be the principled approach,
but non-differentiable intermediate sampling precludes di-
rect optimization. Reinforcement learning is used instead,
not because it offers a better objective, but as a workaround
to this non-differentiability.

Suppose that both maximum likelihood and reinforcement
learning could be applied to a given task, regardless of dif-
ferentiability. Then the two objectives induce markedly
different optimization behavior, as we shall explain below.
To make this distinction precise, we compare the population-
level objectives implied by each framework. Let pθ(x) de-
note the probability that a model with parameters θ produces
a correct output for input x. Moreover, let ρ be the distribu-
tion from which the inputs are sampled. The corresponding
gradients of reinforcement learning, ∇θJRL, and of maxi-
mum likelihood, ∇θJML, take the form

∇θJRL = Ex∼ρ\[∇θpθ(x)\]

∇θJML = Ex∼ρ\[∇θ log pθ(x)\] = Ex∼ρ


1
pθ(x)∇θpθ(x)


1

## Page 2

Maximum Likelihood Reinforcement Learning

The inverse-probability reweighting induced by maximum
likelihood places greater emphasis on hard, low-success
inputs, leading to very different optimization dynamics, as
we empirically demonstrate in this paper (cf. Section 6).

When viewed end-to-end, maximum likelihood emerges as
the principled objective, for the very same reasons it is the
method of choice in differentiable supervised learning with
binary correctness. In non-differentiable problems, however,
this objective is difficult to optimize directly because cor-
rectness is observed only after a non-differentiable stochas-
tic generation process, and the success probability pθ(x)
may be small. This computational challenge motivates a
framework that leverages additional sampling compute to
more faithfully approximate likelihood-based training. We
call this framework Maximum Likelihood Reinforcement
Learning (MaxRL). At a high level, MAXRL bridges stan-
dard reinforcement learning and exact maximum likelihood
by progressively incorporating higher-order correctness in-
formation as more sampling compute is utilized, ultimately
recovering likelihood optimization in the infinite-compute
limit. We discuss the relationship between MAXRL and
recent work in this direction (Xiong et al., 2025b; Davis &
Recht, 2025) in Section 7. Our contributions are threefold:

1. We formalize correctness-based reinforcement learning
as a latent-generation maximum likelihood problem and
show that standard reinforcement learning optimizes only
the first-order approximation of the maximum likelihood
objective (cf. Section 3).

2. We introduce a compute-indexed family of objectives
that interpolates between expected reward and exact max-
imum likelihood via a Maclaurin expansion in pass@k
events (cf. Section 3).

3. We analyze a simple on-policy estimator whose expected
gradient exactly matches the compute-indexed approx-
imation of the likelihood objective, implying that in-
creased sampling improves the optimized objective itself
rather than merely reducing variance.

Empirically, MAXRL Pareto-dominates standard RL objec-
tives (RLOO (Ahmadian et al., 2024), GRPO (Shao et al.,
2024)) on all settings that we tested (cf. Section 6). Specifi-
cally, MAXRL shows better scaling trends when additional
compute and data are available, and on mathematical reason-
ing tasks, it achieves up to 20× test-time scaling efficiency
gains over GRPO with a perfect verifier.

2. Preliminaries

We focus on correctness-based problems which define a
binary success or failure outcome for each input. Formally,
let x ∼ρ be an input drawn from a distribution ρ, and

let y∗(x) denote the correct label or answer for x. Let the
learner be parameterized by θ, inducing a distribution pθ(· |
x) over outputs for each input x. Equality between outputs is
defined up to a task-dependent equivalence relation, so that
y = y∗(x) denotes semantic correctness rather than exact
output equality. For example, in mathematical reasoning,
x is the prompt and y is the final solution produced by the
model. We use natural logarithms unless stated otherwise.

Latent generation models.
In many settings, the model
generates a latent variable z ∈Z (a trajectory, e.g. a chain
of thought) according to a discrete conditional distribution
mθ(z | x) before producing the final answer. The final out-
put y is then obtained via a deterministic decoding function
y = f(z), such as parsing a generated program or extract-
ing a boxed answer from a chain of thought. Correctness is
evaluated only on the decoded output, i.e., z is successful if
f(z) = y∗(x). Decoding pushes mθ forward to the output
distribution pθ(· | x) from above,

pθ(y | x) =
X

z∈Z
mθ(z | x) I{f(z) = y}.
(1)

Throughout the paper, expectations with respect to model
outputs should be understood as expectations over latent
samples z ∼mθ(· | x) followed by deterministic decoding.

Pass rate.
We define the pass rate as the probability that
the model produces the correct answer for a fixed input x:

ppass
θ
(x) := pθ(y∗(x) | x) = Ey∼pθ(·|x)\[I{y = y∗(x)}\] .

Similarly, let y1, . . . , yk
i.i.d.
∼pθ(· | x). We define pass@k
as the probability of at least one correct sample:

pass@k(x) := P(∃i ∈\[k\] s.t. yi = y∗(x)) .

Maximum likelihood (ML).
Maximum likelihood selects
parameters that maximize the log-likelihood of the observed
data under the model. In our setting, the probability of
observing correctness is pθ(y∗(x) | x). Maximizing the
corresponding log-likelihood therefore yields the objective

JML(θ) := Ex∼ρ \[log pθ(y∗(x) | x)\] ,
(2)

which is directly analogous to cross-entropy training in
differentiable supervised learning.

Reinforcement learning (RL).
Typically, reinforcement
learning is applied to correctness-based tasks by defining a
binary reward function r(x, y) = I{y = y∗(x)} indicating
correctness, yielding the RL objective:

JRL(θ) := Ex∼ρ

Ez∼mθ(·|x) \[r(x, z)\]

= Ex∼ρ \[ppass
θ
(x)\] .
(3)
In short, RL maximizes the expectation over pass rate while
ML maximizes the expectation over its logarithm.

2

## Page 3

Maximum Likelihood Reinforcement Learning

3. Maximum Likelihood Reinforcement
Learning (MAXRL)

In this section, we show that reinforcement learning on
expected reward optimizes only a first-order approximation
of the ML objective. Specifically, the maximum likelihood
objective admits a population-level expansion in terms of
pass@k events, with standard RL optimizing only the first-
order term. This suggests a compute-indexed family of
objectives that incorporate higher-order terms, converging
to ML as more compute is allocated.

3.1. Maclaurin Expansion of Maximum Likelihood

For simplicity, let us consider a single task x in the develop-
ment to follow, as the final objective and gradients can be
obtained by taking an expectation over x ∼ρ. Moreover,
we write p := ppass
θ
(x) to simplify our notation. The maxi-
mum likelihood objective admits the Maclaurin expansion
in terms of failure events:

JML(x) = log p = −

∞
X

k=1

(1 −p)k

k
= −

∞
X

k=1

fail@k(x)

k
,

(4)
where fail@k(x) = 1 −pass@k(x) denotes the probability
that all k i.i.d. samples from the model fail. Differentiat-
ing Equation (4) yields the population-level gradient identity

∇θJML(x) =

∞
X

k=1

1
k ∇θpass@k(x).
(5)

Thus, maximum likelihood optimizes an infinite harmonic
mixture of pass@k gradients, with higher-order terms en-
coding rare success which are critical when p is small. In
contrast, the classical reinforcement learning approach is
to optimize only the expected pass@1 objective (Koenig
& Simmons, 1993; Silver et al., 2016; Vecerik et al., 2018;
Guo et al., 2025):

∇θJRL(x) = ∇θpass@1(x),

corresponding to retaining solely the leading term of Equa-
tion (5). From this observation, we can claim:

Reinforcement learning optimizes a first-order
approximation of the maximum likelihood objective.

3.2. MAXRL Objective Function

The maximum likelihood gradient in Equation (5) is difficult
to estimate with a fixed number of samples. In particular,
estimating pass@k gradients for large k requires an increas-
ing number of samples, especially when the pass rate p is
small. This finite-sample difficulty is precisely what moti-
vates Maximum Likelihood Reinforcement Learning. We

define MAXRL as the class of reinforcement-learning meth-
ods that explicitly target the maximum likelihood objective
rather than the pass rate, while remaining implementable
under fixed sampling and non-differentiable generation. We
consider a principled way to do so below.

Consider approximating the maximum likelihood objective
by truncating the Maclaurin expansion (Equation (5)) to a
fixed finite order and then estimating such an objective in-
stead. For a truncation level T ∈N, we define the truncated
maximum likelihood objective for a fixed input x as:

J(T )
MAXRL(x) := −

T
X

k=1

(1 −p)k

k
.
(6)

Differentiating Equation (6) yields the truncated population
gradient:

∇θJ(T )
MAXRL(x) =

T
X

k=1

1
k ∇θpass@k(x).
(7)

This defines a family of objectives: T = 1 recovers rein-
forcement learning, T →∞recovers maximum likeli-
hood, and intermediate T values interpolate between them.
Thus, the truncation level T directly controls the order
of correctness events that contribute to learning. As we
will soon see, it becomes viable to estimate higher-order
∇θJ(T )
MAXRL(x) as more compute is expended in terms of
rollouts. In other words:

MAXRL provides a principled framework for trading
additional compute for higher-fidelity approximations to
the maximum likelihood objective.

The remaining question is whether these truncated objec-
tives admit simple, unbiased estimators under a fixed sam-
pling budget, a question that we answer affirmatively in the
next section.

4. Gradient Estimators for MAXRL

Equation (7) already provides a viable approach for con-
structing an unbiased estimator: approximate each term
in the finite series using a pass@k gradient estimator, as
provided in recent work (Walder & Karkhanis, 2025; Chen
et al., 2025b). Under this strategy, any improvement in
pass@k estimators directly translates into improved estima-
tors for the truncated maximum likelihood objective that we
provided in Equation (7).

In this work, we take an alternate approach. The key insight
is that the maximum likelihood gradient can be expressed as
an expectation under the success-conditioned distribution,
as established by the following theorem (Davis & Recht
(2025) also recently made a similar observation).

3

## Page 4

Maximum Likelihood Reinforcement Learning

Theorem 4.1 (Conditional Form of the Maximum Likeli-
hood Gradient). The gradient of the maximum likelihood
objective admits the following conditional expectation rep-
resentation:

∇θJML(x) = E\[∇θ log mθ(z | x) | f(z) = y∗(x)\] . (8)

We provide the proof of this theorem in Appendix C. The
theorem establishes that the maximum likelihood gradient
is the average gradient from successful trajectories only.
This interpretation naturally leads to a concrete gradient
estimator by replacing the expectation with sample averages
over successful rollouts.

4.1. Empirical Gradient Estimator

Table 1. Comparison of the REINFORCE estimator (∇θJRL(x))
and the conditional estimator (∇θJ(T )
MAXRL(x)). Although they dif-
fer only in normalization (N vs. K), they are unbiased for funda-
mentally different objectives.

REINFORCE
MAXRL

Estimator
1
N
PN
i=1 riSi
1
K
PN
i=1 riSi

Unbiased for
∇θ pass@1(x)
PN
k=1
1
k ∇θpass@k(x)

Theorem 4.1 suggests drawing samples from the success-
conditioned policy. Recent literature has proposed rejection
fine-tuning (Touvron et al., 2023; Yuan et al., 2023; Dong
et al., 2023; Xiong et al., 2025a; Davis & Recht, 2025) and
adaptive sampling (Xiong et al., 2025b) as mechanisms to
sample from this conditional distribution. However, doing
so is computationally demanding when the pass rate is small
or requires a more complex implementation regarding adap-
tive sampling. Instead, we adopt a simpler approach: we
sample from the unconditional policy mθ(· | x) and then
average over only the successful trajectories. Fix an input x
and draw N latent trajectories z1, . . . , zN ∼mθ(· | x). Let
ri := I{f(zi) = y∗(x)} indicates success-based reward,
Si := ∇θ log mθ(zi | x) denote the score function, and
K := PN
i=1 ri be the number of successful samples. We
average score functions only over successful trajectories
and obtain the following REINFORCE-style estimator:

bgN(x) :=








1
K

N
X

i=1
riSi,
K ≥1,

0,
K = 0.

(9)

The estimator constructed in this way is such that some
inputs may receive zero gradient if there are no successes
within N samples, making the resulting estimator no longer
unbiased with respect to the infinite series expansion of
the true ML objective from Equation (5). We show that
this estimator is however unbiased for the gradient of the

truncated maximum likelihood objective in Equation (7),
∇θJ(T )
MAXRL(x), with truncation level T = N:
Theorem 4.2 (Estimator–objective equivalence). The es-
timator bgN(x) is an unbiased estimator for the MAXRL
gradient of order T = N, i.e.,

E\[bgN(x)\] = ∇θJ(N)
MAXRL(x).

We present the proof of this result in Appendix C. Theo-
rem 4.2 reveals an elegant alignment between the estimator
in Equation (9) and the gradient of the truncated Maclaurin
expansion in Equation (7). It is worth highlighting the most
important property of the estimator:

Increasing compute as rollouts N leads to a better
approximation of the maximum likelihood gradient.

Table 1 compares our estimator with the REINFORCE esti-
mator, whose expected value underlies most RL algorithms.
At the estimator level, the difference is simple: both average
score functions over sampled trajectories, but REINFORCE
normalizes by total samples N while MAXRL normalizes
by successful samples K. This difference in normalization
determines the objective each estimator is unbiased for.

Consequently, increasing the number of samples, N, for the
two estimators has different effects: REINFORCE1 reduces
variance of a fixed objective (pass@1), while MAXRL in-
creases the approximation order to maximum likelihood.
Additional compute thus improves the objective itself for
MAXRL, not just estimation quality.

4.2. Variance Reduction via Control Variates

Like REINFORCE, the estimator in Equation (9) can ex-
hibit high variance when the number of successful samples,
K, is small. Policy-gradient baselines are typically intro-
duced to reduce variance without changing the expected
gradient (Sutton, 1988). However, standard arguments for
policy-gradient baselines are not directly applicable in this
setting, as the estimator normalizes by the random variable
K which depends on all samples, making it correlated with
the observed rollouts.

We instead proceed from first principles and use a simple
zero-mean control variate, the unconditional average score:

VN := 1

N

N
X

i=1
∇θ log mθ(zi | x).

1Modern policy-gradient methods such as PPO (Schulman
et al., 2017) introduce additional mechanisms (importance weight
truncation via clipping) that trade bias for robustness. In the fully
on-policy setting, these reduce to REINFORCE, our canonical
baseline. GRPO (Shao et al., 2024) is a notable exception due
to its division by standard deviation in the advantage calculation,
which we discuss further in Section 5.

4

## Page 5

Maximum Likelihood Reinforcement Learning

This satisfies E\[VN\] = 0. Subtracting VN preserves unbi-
asedness while reducing variance in practice:

egN(x) = 1

K

N
X

i=1
riSi −1

N

N
X

i=1
Si =

N
X

i=1

 ri

K −1

N


Si

(10)
with the convention that the first term,
PN
i=1 riSi

/K, is
zero when K = 0.

4.3. On-Policy Implementation

Finally, we present a simple on-policy implementation of
MAXRL that differs from standard REINFORCE-style pol-
icy gradient methods by a single-line modification to the ad-
vantage calculation. We adopt the variance-reduced formula-
tion from Equation (10), and drop both terms when K = 0,
consistent with standard policy-gradient practice (Yu et al.,
2025; Nie et al., 2026) in which no gradient is computed
for tasks with no successful rollouts: this choice is simpler
and performs better empirically. Concretely, the advantage
is normalized by the per-task mean reward, rather than left
unnormalized as in RLOO (Ahmadian et al., 2024) or nor-
malized by the reward standard deviation as in GRPO (Shao
et al., 2024). The modified line is highlighted in blue.

Algorithm 1 On-Policy Implementation of MAXRL

1: Input: Batch of inputs B, number of rollouts N, latent
policy mθ
2: for each input x ∈B do

3:
Sample N rollouts z1, . . . , zN
i.i.d.
∼mθ(· | x)
4:
Compute rewards rj = I{f(zj) = y∗(x)}

5:
Compute mean reward br(x) = 1

N
PN
j=1 rj
6:
Set

eg(x) =










1
N br(x)

N
X

j=1

 
rj −br(x)

Sj,
br(x) > 0,

0,
otherwise.

7: end for
8: Set eg =
1
|B|
P
x∈B eg(x)
9: return eg

We direct the reader to Section M.2 for a study on the effect
of the control variate baseline on gradient variance: Fig-
ure 28 shows that despite having no theoretical guaranties,
baseline subtraction generally reduces gradient variance in
practice, especially when the rollout count is low. Finally, it
should be noted that the practical gradient estimator in Al-
gorithm 1 is an unbiased estimator for the MAXRL gradient
of order T = N −1, as opposed to order T = N from The-
orem 4.2. This is due to the lack of baseline subtraction
for tasks without any positive rollouts, which changes the
expected gradient. See Section D for a detailed analysis.

5. A Unifying Weight-Function View

Maximum likelihood, MAXRL, classical reinforcement
learning, and GRPO all admit population-level gradients of
the following form:

∇θJ = Ex∼ρ\[w(pθ(x)) ∇θpθ(x)\]
(11)

where pθ(x) = ppass
θ
(x) and w(p) is a scalar weight that
depends only on the pass rate. The function w(p) determines
how learning signal is allocated across inputs of varying
difficulty and fully characterizes the differences between
these objectives at the population level. Figure 1 plots the
resulting weight functions for each method; derivations
are provided in Appendix E. The key distinction among
objectives is how strongly they emphasize hard, low-pass-
rate inputs. As T increases, MAXRL uniquely approaches
maximum likelihood weighting in the low-pass-rate regime.

Table 2. Population-level weighting functions w(p).

RL
GRPO
MAXRL (T)
ML

w(p)
1
1
p

p(1 −p)

1 −(1 −p)T

p
1
p

10
3
10
2
10
1
100

Pass rate, p (x)

100

101

102

103

Weight function, w(p (x))

T = 1 (also REINFORCE)

T = 2

T = 4

T = 8

T = 16

T = 32

T = 64

T = 128

T =
 (also Maximum Likelihood)

JML
J(T)
MaxRL
JGRPO

Figure 1. Population-level weighting functions w(p) as a function
of pass rate p. Truncated objectives, J(T )
MAXRL, interpolate between
REINFORCE and maximum likelihood as T increases.

This weight perspective also provides a useful reinterpreta-
tion of GRPO (Shao et al., 2024). Although GRPO is heuris-
tically motivated by Z-normalization using the empirical
standard deviation, such normalization induces a fundamen-
tally different population-level objective from REINFORCE,
a conclusion also reached by recent work (Davis & Recht,
2025; Liu et al., 2025b; Xiong et al., 2025b; Yang et al.,
2026a; Thrampoulidis et al., 2026). Table 2 summarizes the
population-level weighting functions; relative to standard
expected-reward optimization, GRPO upweights low-pass-
rate inputs approximately as 1/√p when p is small, placing
it between classical reinforcement learning and maximum
likelihood. However, increasing compute via additional
sampling under GRPO does not yield a better approxima-
tion to the maximum likelihood objective, as the induced

5

## Page 6

Maximum Likelihood Reinforcement Learning

population loss is fundamentally distinct. Moreover, as
shown in Figure 1, the GRPO weighting function inverts
for sufficiently large pass rates, increasing as p →1, unlike
likelihood-based objectives. Consequently, GRPO assigns
increased weight to very easy inputs when they are present,
in contrast to the other formulations.2

6. Experiments

We now turn to the empirical evaluation of MAXRL. We
begin in Section 6.1 with a controlled setting where exact
maximum likelihood optimization is possible, allowing di-
rect comparison with MAXRL as compute increases. We
then study non-differentiable correctness-based tasks in two
regimes: (i) an effectively infinite-data setting with large
number of novel tasks (Section 6.2), and (ii) a data-scarce
setting with a fixed training dataset where we can scale
compute nonetheless by training for many epochs over the
same dataset (Section 6.3). Finally, in Section 6.4, we train
and evaluate billion-parameter reasoning models on math-
ematical problem-solving, testing whether the benefits of
MAXRL extend to larger-scale LLM training.

Because we compare training objectives rather than algo-
rithms, all methods are trained on-policy. We compare
against RLOO (Ahmadian et al., 2024) and GRPO (Shao
et al., 2024) as primary baselines.

6.1. Comparisons with Exact Likelihood

As a first step, we evaluate how closely MAXRL approxi-
mates exact maximum likelihood in a setting where the latter
can be implemented exactly. We compare three objectives:
(i) reinforcement learning on expected reward, (ii) MAXRL
(a fixed sample-based objective), and (iii) exact maximum
likelihood training. We consider a standard image classifi-
cation task, where the exact ML objective corresponds to
minimizing cross-entropy. The RL reward is defined as 1
if the predicted class matches the ground-truth label and
0 otherwise. We instantiate this comparison on the Ima-
geNet (Deng et al., 2009) dataset using a ResNet-50 (He
et al., 2016) based classifier trained under each objective;
full experimental details are provided in Appendix H. Fig-
ure 2 summarizes the results: REINFORCE (with a standard
baseline) fails to achieve meaningful improvements even
with very high per-input sampling budget, whereas exact
maximum likelihood training yields steady gains on both
average performance (Pass@1) and coverage (Pass@k).

In contrast, MAXRL is trained on the same samples and
observes the same sparse set of successful trajectories as

2We conjecture that this inversion may contribute to distribution
sharpening (Pass@k degradation) (Yue et al., 2025; Wu et al., 2026)
when datasets contain a substantial fraction of overly easy inputs,
and leave a detailed analysis to future work.

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

20

40

60

Validation Pass@1 (
)

Pass@1 (
)

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

25

50

75

100

Validation Pass@128 (
)

Pass@128 (
)

MaxRL (Rollout = 16)
REINFORCE (Rollout = 1024)

MaxRL (Rollout = 128)
Cross Entropy

MaxRL (Rollout = 1024)

Figure 2. (ImageNet) Comparison of training dynamics under
exact maximum likelihood, MAXRL, and REINFORCE in a
controlled image classification setting. With sufficient rollouts,
MAXRL closely matches cross-entropy training, while REIN-
FORCE fails to make progress from low initial pass rates.

REINFORCE, but makes more effective use of this limited
learning signal through likelihood-inspired reweighting. As
the compute increases by means of higher rollout counts,
MAXRL improves consistently and closely tracks exact
maximum likelihood. We also analyze the gradient norm
resulting from different objectives in Figure 8: MAXRL and
cross-entropy concentrate learning signal on harder tasks
and are characteristically similar given sufficient compute
for MAXRL, whereas GRPO and REINFORCE exhibit
very different behavior. For additional experiments such as
comparison to GRPO, we refer the reader to Appendix H.

Takeaway 1
When direct maximum-likelihood optimization is available,
MAXRL converges to it as sampling compute increases.

6.2. Infinite Data Regime

Next, we study MAXRL in non-differentiable settings. For
the first experiment, we study how MAXRL behaves in data-
rich domains. To simulate training with infinite data, we
construct a procedurally generated maze-navigation envi-
ronment with 1 million unique 17 × 17 mazes for training
where multiple valid solution paths might exist for a given
task. We reserve a held-out set of 256 mazes for evaluation
and apply a brief supervised pretraining phase to ensure a
non-zero initial pass rate. The complete details of the task
are provided in the Appendix I.

We train a lightweight transformer model (Vaswani et al.,
2017) with approximately 3M parameters and simulate ex-
tended training by running 9,000 RL steps with a batch size
of 256. We report performance after 9,000 steps in Figure 3
as a function of training compute, implemented as different
number of rollouts per prompt, from 4 to 128, while keep-
ing other hyperparameters the same. Notice that this is a
substantial amount of compute for our particular model size.

All three objectives (RLOO, GRPO, and MAXRL) improve
upon the base model, but the magnitude of improvement dif-
fers markedly across methods. Even at the highest compute
budget (128 rollouts per prompt), RLOO fails to match the
performance achieved by MAXRL at the lowest budget (4

6

## Page 7

Maximum Likelihood Reinforcement Learning

4
8
16
32
64
128
Training Rollouts

10
2

10
1

100

101

log (Pass@k) (
)

k = 1

4
8
16
32
64
128
Training Rollouts

10
2

10
1

100

101
k = 128

4
8
16
32
64
128
Training Rollouts

10
2

10
1

100

101
k = 1024

4
8
16
32
64
128
Training Rollouts

10
2

10
1

100

101
k = 2048

Base
GRPO
RLOO
MaxRL

Figure 3. (Maze) Motivated by Schaeffer et al. (2025), we record −log(pass@k) (lower is better) as a function of training rollouts for
different objectives. We see that across all different inference rollout budgets (k), MAXRL exhibits better scaling compared to GRPO and
RLOO as we increase number of training rollouts.

0
10
20
30
40
50
Epochs

0.1

0.2

0.3

Pass@1 (
)

Pass@1 (
)

0
10
20
30
40
50
Epochs

0.4

0.5

0.6

0.7

Pass@32 (
)

Pass@32 (
)

0
10
20
30
40
50
Epochs

0.5

0.6

0.7

0.8

Pass@128 (
)

Pass@128 (
)

0
10
20
30
40
50
Epochs

0.5

0.6

0.7

0.8

0.9

Pass@256 (
)

Pass@256 (
)

Base
GRPO
RLOO
MaxRL

Figure 4. (GSM8K) Training dynamics on GSM8K with a fixed dataset and increasing training compute in terms of RL steps. MAXRL
shows slower initial gains but ultimately achieves higher performance with substantially less pass@k degradation.

rollouts) across all pass@k metrics. GRPO-trained models
at the highest compute similarly trail MAXRL trained with
only 16 rollouts per prompt at every pass@k evaluation.
These results highlight that MAXRL scales with compute
far more effectively than competing frameworks when large
amounts of unique training data are available. Moreover,
there is almost no gap in pass@k and pass@1 for GRPO
and RLOO despite no repeated data, showing that these
algorithms have lost the ability to improve further, whereas
MAXRL has a substantial gap and potentially can improve
more given additional compute. Comparisons with addi-
tional baselines are provided in Table 3 and Appendix L.

Takeaway 2
In a data-rich training regime, MAXRL scales more favorably
with additional compute compared to existing methods.

6.3. Data-Scarce Regime

We next consider a data-scarce regime where models are
trained for many epochs on a fixed dataset until peak per-
formance is reached, with the goal of identifying which
method extracts the highest attainable performance. Un-
like the infinite-data setting in Section 6.2, longer training
in this regime does not necessarily translate into improved
performance due to the increased risk of overfitting. Specif-
ically, we train a SmolLM2-360M-Instruct model (Allal
et al., 2025) on GSM8K (Cobbe et al., 2021) for up to 50
epochs. Training dynamics is reported in Figure 4, with
additional experimental details provided in Appendix J.

All methods improve on the base model in terms of pass@1
performance; however, only MAXRL consistently exceeds
the base model in pass@k metrics. In contrast, RLOO
and GRPO exhibit massive pass@k degradation with ex-
tended training, mirroring the behavior observed by Yue
et al. (2025) and exacerbated here by prolonged training on
a fixed dataset. RLOO and GRPO reach their peak pass@1
performance faster than MAXRL (around 10 epochs), but
MAXRL overtakes competing methods at approximately 30
epochs and continues to increase through the end of training,
reaching a higher peak. At the same time, pass@k remains
substantially healthier for MAXRL and exceeds the base
model for a large portion of training. This behavior suggests
MAXRL is more resistant to overfitting, particularly with
regard to output diversity. Additional comparisons with
baseline methods are reported in Table 5.

Takeaway 3
In a data-scarce regime, MAXRL can sustain improvement
over a large number of epochs, demonstrating less pass@k
degradation (overfitting) and converging to a higher average
performance.

6.4. Large Reasoning Model Training

We next demonstrate that the benefits of MAXRL extend to
larger-scale LLM reasoning training. We train Qwen3-1.7B-
Base and Qwen3-4B-Base models on POLARIS-53K (An
et al., 2025), a dataset of approximately 50,000 mathe-
matical reasoning prompts, using 256 prompts per batch,

7

## Page 8

Maximum Likelihood Reinforcement Learning

1
16
256
4096
0

20

40

60

Qwen3-1.7B-Base

Coverage (Pass@k)

BeyondAIME

3.9×

1
16
256
4096
0

15

30

45

60

75

AIME 2025

5.0×

1
8
64
512
55

70

85

100
MATH-500

7.9×

1
8
64
512
10

40

70
Minerva

2.3×

1
16
256
4096
k

0

20

40

60

80

Qwen3-4B-Base

Coverage (Pass@k)

16.4×

1
16
256
4096
k

0

15

30

45

60

75

90

7.9×

1
8
64
512
k

60

70

80

90

100

16.0×

1
8
64
512
k

10

40

70

19.2×

Base
GRPO
MaxRL

Figure 5. (Qwen3 training results) Evaluation of final checkpoints from training Qwen3-1.7B-Base and Qwen3-4B-Base models, on 4
benchmarks: AIME 2025, BeyondAIME, MATH-500 and Minerva. MAXRL matches or outperforms GRPO in all 4 evaluation datasets
and shows little to no degradation at coverage (pass@k) for very high k values.

0.0
0.2
0.4
0.6
0.8
1.0
Pass Rate

0

50

100

150

Gradient L2 Norm

MaxRL

0.0
0.2
0.4
0.6
0.8
1.0
Pass Rate

0

50

100

GRPO

0.0
0.2
0.4
0.6
0.8
1.0
Pass Rate

0

25

50
RLOO

Figure 6. (Gradient norm analysis) To compare different objec-
tives qualitatively, we show a scatter plot of gradient L2 norm vs
pass rate over individual prompts. We use Qwen2.5-1.5B-Instruct
on MATH-500 dataset for this analysis. MAXRL generates larger
gradient norms prompts with close to 0 pass rates.

16 rollouts per prompt, and 1000 RL steps. Notice that
this setup utilizes lower rollout counts and RL steps than
prior experiments to allow training larger models within
our compute budget. We evaluate on four standard math
benchmarks: AIME 2025, BeyondAIME (ByteDance-Seed,
2025), MATH-500 (Hendrycks et al., 2021; Lightman et al.,
2024), and Minerva (Lewkowycz et al., 2022). We compare
against GRPO (Shao et al., 2024), a widely used baseline for
large-scale reasoning (Guo et al., 2025; Yang et al., 2025).
Additional details are provided in Appendix K.

Figure 5 summarizes our main results.
Across both
model sizes, MAXRL consistently Pareto-dominates GRPO,
achieving higher pass@1 while simultaneously improving
pass@k. Consistent with prior work (Yue et al., 2025; Wu
et al., 2026), GRPO exhibits pronounced pass@k degrada-
tion at larger k. In contrast, MAXRL improves pass@k
relative to both the pretrained base model and the GRPO-
trained checkpoint in 7 out of 8 evaluation settings. Im-
proved pass@k directly translates into inference efficiency
under repeated sampling. As shown in Figure 5, MAXRL

achieves up to 20× test-time scaling efficiency gains when
using a perfect verifier to filter wrong solutions, yielding
substantial practical savings at inference time. We note
that many settings admit a strong verifier, such as program-
ming (Chen et al., 2021) or Lean (de Moura et al., 2015),
where MAXRL can show strong benefits over other RL
objectives. We provide additional results, such as evalu-
ation on 4 additional benchmarks, and comparisons with
additional baselines, in Appendix Sections K.3 and L.

Takeaway 4
On larger scale mathematical reasoning, MAXRL Pareto-
dominates GRPO, shows little to no diversity degradation with
respect to the base model, and leads to strong (up to 20×)
test-time scaling efficiency gains.

6.5. Behavior Analysis of MAXRL

Finally, we study whether MAXRL shows different charac-
teristics compared to commonly used RL objectives besides
performance metrics. We first study the gradient norms
produced by different objectives: Figure 6 illustrates that
MAXRL generates higher gradient norms on harder prompts
and lower gradient norms on easier prompts. This behavior
matches that of cross-entropy in fully differentiable image
classification setting (Figure 8), showing that MAXRL con-
centrates learning signal on harder problems unlike GRPO
and RLOO. These larger gradient norms on more difficult
prompts then translate into the model’s capability to gener-
ate correct solutions for a larger fraction of problems during
training. Figure 7 illustrates this trend, as MAXRL consis-
tently generates at least one correct rollout for a larger frac-

8

## Page 9

Maximum Likelihood Reinforcement Learning

0
250
500
750
1000
RL Step

70

80

90

100

Non-zero pass rate

prompts(%)

SmolLM-360M-Instruct

on GSM8K

0
250
500
750
1000
RL Step

35

45

55

65

Qwen3-1.7B-Base

on POLARIS-53K

0
250
500
750
1000
RL Step

50

60

70

80

Qwen3-4B-Base 
on POLARIS-53K

GRPO
MaxRL

Figure 7. (Training dynamics comparison) Fraction of prompts
where the model generates at least one correct rollout (out of
128, 16, and 16 rollouts for SmolLM-360M-Instruct, Qwen3-1.7B-
Base, and Qwen3-4B-Base, respectively) during training. MAXRL
consistently produces at least one correct rollout for more prompts.

tion of training prompts, and the gap between MAXRL and
GRPO persists as we train longer. Appendix M.1 further
corroborates these findings in the maze and GSM8K training
settings. In addition, Figure 14 shows that GRPO and RLOO
drive the per-prompt pass-rate distribution to the extremes
of 0 and 1, consistent with the distribution-sharpening narra-
tive, whereas MAXRL maintains a broad pass-rate distribu-
tion throughout training. Finally, the inverse signal-to-noise
ratio (SNR) analysis in Figure 29 shows that MAXRL be-
comes more stable as the rollout budget increases, despite a
stronger amplification of the learning signal from problems
with very-low-success-rate (p →0). Appendix M further
examines how MAXRL and GRPO differ in distribution
sharpening and non-binary reward settings. In general, these
results suggest that MAXRL differs in significant ways from
other RL objectives, and we leave a deeper investigation of
these differences to future work.

Takeaway 5
Besides performance metrics, MAXRL also exhibits different
optimization dynamics. Most notably, it produces stronger
gradients on harder prompts, and also leads to a larger fraction
of prompts with at least one correct rollout during training.

7. Related Work

Supervised training vs reinforcement learning.
Super-
vised learning and reinforcement learning (RL) are com-
plementary but fundamentally different paradigms. Super-
vised training is stable, sample-efficient, and well-calibrated
within the training distribution (Ng & Jordan, 2001), but it is
limited by the quality and scope of available data and cannot
directly optimize non-differentiable objectives such as cor-
rectness or preferences. In contrast, RL can optimize such
objectives directly, typically via policy gradients (Williams,
1992; Sutton et al., 1999; 1998; Schulman et al., 2017; Guo
et al., 2017), and improve performance beyond the avail-
able demonstrations by having access to interactions with
an environment and the resulting reward-based feedback.
Although recent work has reframed RL objectives as su-
pervised ones (Rafailov et al., 2023), on-policy learning,
characteristic of online RL algorithms, appears crucial for
optimal performance (Tajwar et al., 2024; Xu et al., 2024).
Modern foundation model training often combines super-
vised learning on human data with subsequent RL (Ouyang

et al., 2022). Unlike these approaches, we assume no access
to high-quality demonstrations or a stronger model, and in-
stead study a purely interactive RL setting that nonetheless
optimizes an objective that mimics cross-entropy.

Closely related work.
One closely related line of work is
that of Xiong et al. (2025b), which also considers non-linear
functions of the pass rate in reinforcement learning. Both
their work and ours are motivated by the observation that
expected-reward objectives can underweight low-pass-rate
prompts, and that maximizing a log-likelihood-like objec-
tive can mitigate this issue. However, the focus of Xiong
et al. (2025b) is on adaptive rollout budget allocation and
sampling strategies, treating the choice of non-linear weight-
ing as part of an algorithmic design space. In contrast,
we do not employ adaptive sampling, and instead derive a
sampling-based on-policy estimator that approaches max-
imum likelihood as rollout compute budget is increased.
We also empirically focus on demonstrating better data and
compute scaling with our framework, while Xiong et al.
(2025b) focuses on comparing against other adaptive sam-
pling frameworks (Yu et al., 2025). Furthermore, Davis
& Recht (2025) provides a theoretical argument character-
izing the population-level objectives approached by spe-
cific binary-reward reinforcement-learning algorithms in
asymptotic limits, showing that certain procedures induce
log-like weighting of the pass rate. Our work addresses a
complementary question: how finite sampling defines ex-
plicit population-level objectives. We establish an exact
estimator–objective equivalence at each finite rollout count
and empirically evaluate how this objective-level interpola-
tion manifests as compute is increased in both controlled
settings and large-scale LLM post-training experiments. We
discuss additional related work in Appendix B.

8. Conclusion

In this work, we establish Maximum Likelihood Reinforce-
ment Learning as a principled optimization framework for
non-differentiable binary reward settings. We showed that
MAXRL approaches maximum likelihood in differentiable
settings as compute increases and that in non-differentiable
settings it offers key advantages over traditional RL, scaling
more effectively with additional compute and data. More
broadly, our results suggest that some limitations attributed
to reinforcement learning with foundation models arise from
objective choice rather than optimization or sampling. Our
work currently assumes a binary reward setting and does
not extend directly to continuous or arbitrarily valued re-
wards. Moreover, one can also consider objectives other
than maximum likelihood to optimize following our frame-
work. Generalizing MAXRL to continuous rewards, multi-
turn reinforcement learning, and off-policy settings such as
PPO-style training are promising directions for future work.

9

## Page 10

Maximum Likelihood Reinforcement Learning

Acknowledgements

This research used both the DeltaAI advanced computing
and data resource (Bode et al., 2025), which is supported
by the National Science Foundation (award OAC 2320345)
and the State of Illinois, and the Delta advanced computing
and data resource (Gropp et al., 2023), which is supported
by the National Science Foundation (award OAC 2005572)
and the State of Illinois. Delta and DeltaAI are joint efforts
of the University of Illinois Urbana-Champaign and its Na-
tional Center for Supercomputing Applications. Both of
these computing resources were used as part of ACCESS-
approved compute grants (Boerner et al., 2023). The au-
thors also appreciate the computing resources of Bridges-
2 (Brown et al., 2021) at Pittsburgh Supercomputing Cen-
ter through ACCESS allocation CIS240901 from the Ad-
vanced Cyberinfrastructure Coordination Ecosystem: Ser-
vices & Support (ACCESS) program, which is supported by
National Science Foundation grants #2138259, #2138286,
#2138307, #2137603, and #2138296. Overall, this project
used ACCESS grants CIS240901, CIS250216, CIS250428,
CIS250651, CIS250835, CIS250560, CIS251063, and
CIS251385 for its compute resources. The authors also
thank the CMU FLAME center and the CMU Babel Com-
pute Cluster for additional compute support during the early
phases of this project.

This work was supported in part by ONR N000142312368
and ONR MURI N00014-25-1-2116. Moreover, Fahim
Tajwar was partially supported by the U.S. Army Futures
Command under Contract No. W519TC-23-C-0030 during
the project. Yuda Song gratefully acknowledges the support
of the Two Sigma Fellowship. Daman Arora was supported
by the National Science Foundation under Grants CCF-
2106778. Yiding Jiang gratefully acknowledges the support
of the Google PhD Fellowship.

The authors thank Brandon Pusateri, Jillian Lehosky, and
Greg Bauer from ACCESS Support Staff for their incredible
help in approving supplements and renewals for ACCESS
compute grants throughout this project. Moreover, the work
would not have been completed in a timely manner without
the help of Brett Bode from NCSA Delta Support Staff, who
provided the authors with critical help in properly utilizing
the Delta cluster. The authors gratefully acknowledge Qian-
qian Wang, Yifei Zhou, Samuel Sokota, Yutong He, Lili
Chen, Stephan Xie, Haque Ishfaq, Gaurav Rohit Ghosal,
Aakash Lahoti, Kevin Li and other members of the Zanette,
Russ and Auton lab for feedback and suggestions received
on earlier versions of this work.

Impact Statement

Our work can be used to train large language models that
have better reasoning capabilities, which can have potential
impact in the real world as LLM reasoning systems become
widespread. Our experiments are conducted in relatively
simple and controlled settings and it is an open question
what kind of impacts large-scale LLM reasoning systems
will have on society. Other than that, this paper presents
work whose goal is to advance the field of Machine Learn-
ing. There are many potential overall societal consequences
of our work, none of which we feel must be specifically
highlighted here.

References

Afriyie, J. K., Tawiah, K., Pels, W. A., Addai-Henne, S.,
Dwamena, H. A., Owiredu, E. O., Ayeh, S. A., and Eshun,
J. A supervised machine learning algorithm for detecting
and predicting fraud in credit card transactions. Decision
Analytics Journal, 6:100163, 2023. ISSN 2772-6622.
doi:
https://doi.org/10.1016/j.dajour.2023.100163.
URL
https://www.sciencedirect.com/
science/article/pii/S2772662223000036.

Ahmadian, A., Cremer, C., Gallé, M., Fadaee, M., Kreutzer,
J., Pietquin, O., Üstün, A., and Hooker, S. Back to basics:
Revisiting reinforce style optimization for learning from
human feedback in llms. In Proceedings of the 62nd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 2024.

AI, E., :, Shah, D. J., Rushton, P., Singla, S., Parmar, M.,
Smith, K., Vanjani, Y., Vaswani, A., Chaluvaraju, A.,
Hojel, A., Ma, A., Thomas, A., Polloreno, A., Tanwer, A.,
Sibai, B. D., Mansingka, D. S., Shivaprasad, D., Shah, I.,
Stratos, K., Nguyen, K., Callahan, M., Pust, M., Iyer, M.,
Monk, P., Mazarakis, P., Kapila, R., Srivastava, S., and
Romanski, T. Rethinking reflection in pre-training, 2025.
URL https://arxiv.org/abs/2504.04022.

Allal, L. B., Lozhkov, A., Bakouch, E., Blázquez, G. M.,
Penedo, G., Tunstall, L., Marafioti, A., Kydlíˇcek, H.,
Lajarín, A. P., Srivastav, V., Lochner, J., Fahlgren, C.,
Nguyen, X.-S., Fourrier, C., Burtenshaw, B., Larcher, H.,
Zhao, H., Zakka, C., Morlon, M., Raffel, C., von Werra,
L., and Wolf, T. Smollm2: When smol goes big — data-
centric training of a fully open small language model. In
Conference on Language Modeling (COLM), 2025.

An, C., Xie, Z., Li, X., Li, L., Zhang, J., Gong, S., Zhong,
M., Xu, J., Qiu, X., Wang, M., and Kong, L. Polaris: A
post-training recipe for scaling reinforcement learning
on advanced reasoning models, 2025.
URL https:
//hkunlp.github.io/blog/2025/Polaris.

10

### Page links

- [Link 1](https://arxiv.org/abs/2504.04022)
- [Link 2](https://hkunlp.github.io/blog/2025/Polaris)
- [Link 3](https://www.sciencedirect.com/science/article/pii/S2772662223000036)

## Page 11

Maximum Likelihood Reinforcement Learning

Anderson, P., Wu, Q., Teney, D., Bruce, J., Johnson, M.,
Sünderhauf, N., Reid, I., Gould, S., and van den Hengel,
A. Vision-and-language navigation: Interpreting visually-
grounded navigation instructions in real environments. In
Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition (CVPR), 2018.

Anthony, T., Tian, Z., and Barber, D. Thinking fast and
slow with deep learning and tree search. In Proceedings
of the 31st International Conference on Neural Informa-
tion Processing Systems, NIPS’17, pp. 5366–5376, Red
Hook, NY, USA, 2017. Curran Associates Inc. ISBN
9781510860964.

Arora, D., Singh, H. G., and ., M. Have LLMs advanced
enough? a challenging problem solving benchmark for
large language models.
In The 2023 Conference on
Empirical Methods in Natural Language Processing,
2023. URL https://openreview.net/forum?
id=YHWXlESeS8.

Atamuradov, S. Evaluating model-agnostic meta-learning
on metaworld ml10 benchmark: Fast adaptation in robotic
manipulation tasks, 2025.
URL https://arxiv.
org/abs/2511.12383.

Auer, P., Cesa-Bianchi, N., and Fischer, P.
Finite-time
analysis of the multiarmed bandit problem. Machine
learning, 47:235–256, 2002.

Bae, S., Hong, J., Lee, M. Y., Kim, H., Nam, J., and Kwak,
D. Online difficulty filtering for reasoning oriented re-
inforcement learning. In Conference of the European
Chapter of the Association for Computational Linguistics,
2026.

Bagirov, F., Arkhipov, M., Sycheva, K., Glukhov, E., and
Bogomolov, E. The best of n worlds: Aligning reinforce-
ment learning with best-of-n sampling via max@k op-
timisation, 2025. URL https://arxiv.org/abs/
2510.23393.

Belkhale, S., Cui, Y., and Sadigh, D. Data quality in imi-
tation learning. In Advances in Neural Information Pro-
cessing Systems, 2023.

Bellemare, M. G., Srinivasan, S., Ostrovski, G., Schaul, T.,
Saxton, D., and Munos, R. Unifying count-based explo-
ration and intrinsic motivation. In Advances in Neural
Information Processing Systems, 2016.

Bellman, R. A markovian decision process. Journal of
Mathematics and Mechanics, 6(5):679–684, 1957. ISSN
00959057, 19435274.
URL http://www.jstor.
org/stable/24900506.

Bengio, E., Pineau, J., and Precup, D. Interference and gen-
eralization in temporal difference learning. In Proceed-
ings of the 37th International Conference on Machine
Learning, Proceedings of Machine Learning Research.
PMLR, 2020.

Bertsekas, D. Dynamic programming and optimal control:
Volume I, volume 4. Athena scientific, 1995.

Bishop, C. M. Pattern Recognition and Machine Learning.
Springer, 2006. ISBN 978-0387310732.

Bode, B., Bauer, G., Herriott, L., Kindratenko, V., and
Gropp, W.
Deltaai: A national resource for ai/ml
research.
In Practice and Experience in Advanced
Research Computing 2025: The Power of Collabora-
tion, PEARC ’25, New York, NY, USA, 2025. Associa-
tion for Computing Machinery. ISBN 9798400713989.
doi: 10.1145/3708035.3736062. URL https://doi.
org/10.1145/3708035.3736062.

Boerner, T. J., Deems, S., Furlani, T. R., Knuth, S. L.,
and Towns, J. Access: Advancing innovation: Nsf’s
advanced cyberinfrastructure coordination ecosystem:
Services & support.
In Practice and Experience in
Advanced Research Computing 2023: Computing for
the Common Good, PEARC ’23, pp. 173–176, New
York, NY, USA, 2023. Association for Computing
Machinery.
ISBN 9781450399852.
doi: 10.1145/
3569951.3597559.
URL https://doi.org/10.
1145/3569951.3597559.

Bojarski, M., Testa, D. D., Dworakowski, D., Firner, B.,
Flepp, B., Goyal, P., Jackel, L. D., Monfort, M., Muller,
U., Zhang, J., Zhang, X., Zhao, J., and Zieba, K. End to
end learning for self-driving cars, 2016. URL https:
//arxiv.org/abs/1604.07316.

Boucher, R. H., Semeraro, O., and Mathelin, L. Evidence
on the regularisation properties of maximum-entropy re-
inforcement learning. In International Conferences on
Optimization and Learning, 2025.

Brown, S. T., Buitrago, P., Hanna, E., Sanielevici, S.,
Scibek, R., and Nystrom, N. A.
Bridges-2: A plat-
form for rapidly-evolving and data intensive research.
In Practice and Experience in Advanced Research Com-
puting 2021: Evolution Across All Dimensions, PEARC
’21, New York, NY, USA, 2021. Association for Com-
puting Machinery.
ISBN 9781450382922.
doi: 10.
1145/3437359.3465593. URL https://doi.org/
10.1145/3437359.3465593.

Brunskill, E. and Li, L. Sample complexity of multi-task
reinforcement learning. In Proceedings of the 29th Con-
ference on Uncertainty in Artificial Intelligence, 2013.

11

### Page links

- [Link 1](http://www.jstor.org/stable/24900506)
- [Link 2](https://arxiv.org/abs/1604.07316)
- [Link 3](https://arxiv.org/abs/2510.23393)
- [Link 4](https://arxiv.org/abs/2511.12383)
- [Link 5](https://doi.org/10.1145/3437359.3465593)
- [Link 6](https://doi.org/10.1145/3569951.3597559)
- [Link 7](https://doi.org/10.1145/3708035.3736062)
- [Link 8](https://openreview.net/forum?id=YHWXlESeS8)

## Page 12

Maximum Likelihood Reinforcement Learning

Bunel, R., Hausknecht, M., Devlin, J., Singh, R., and Kohli,
P. Leveraging grammar and reinforcement learning for
neural program synthesis. In International Conference
on Learning Representations, 2018.

Burda, Y., Edwards, H., Storkey, A., and Klimov, O. Ex-
ploration by random network distillation. arXiv preprint
arXiv:1810.12894, 2018.

ByteDance-Seed.
Beyondaime:
Advancing
math
reasoning
evaluation
beyond
high
school
olympiads.
\[https://huggingface.co/
datasets/ByteDance-Seed/BeyondAIME\]
(https://huggingface.co/datasets/
ByteDance-Seed/BeyondAIME), 2025.

Casella, G. and Berger, R. L. Statistical Inference. Duxbury,
Pacific Grove, CA, 2nd edition, 2002.

Chan, A., Silva, H., Lim, S., Kozuno, T., Mahmood, A. R.,
and White, M. Greedification operators for policy op-
timization: investigating forward and reverse kl diver-
gences. Journal of Machine Learning Research, 23(1),
January 2022. ISSN 1532-4435.

Chang, J. D., Zhan, W., Oertell, O., Brantley, K., Misra,
D., Lee, J. D., and Sun, W. Dataset reset policy opti-
mization for rlhf, 2024. URL https://arxiv.org/
abs/2404.08495.

Chen, J. C.-Y., Peng, B. X., Choubey, P. K., Huang, K.-H.,
Zhang, J., Bansal, M., and Wu, C.-S. Nudging the bound-
aries of llm reasoning. In The Fourteenth International
Conference on Learning Representations, Proceedings of
Machine Learning Research. PMLR, 2026a.

Chen, M., Tworek, J., Jun, H., Yuan, Q., de Oliveira Pinto,
H. P., Kaplan, J., Edwards, H., Burda, Y., Joseph, N.,
Brockman, G., et al. Evaluating large language models
trained on code, 2021. URL https://arxiv.org/
abs/2107.03374.

Chen, P., Li, X., Li, Z., Yin, W., Chen, X., and Lin, T. Explo-
ration vs exploitation: Rethinking rlvr through clipping,
entropy, and spurious reward. In The Fourteenth Interna-
tional Conference on Learning Representations, Proceed-
ings of Machine Learning Research. PMLR, 2026b.

Chen, X., Liu, C., and Song, D. Towards synthesizing
complex programs from input-output examples. In Inter-
national Conference on Learning Representations, 2018.

Chen, X., Lu, J., Kim, M., Zhang, D., Tang, J., Piché, A.,
Gontier, N., Bengio, Y., and Kamalloo, E. Self-evolving
curriculum for llm reasoning, 2025a. URL https://
arxiv.org/abs/2505.14970.

Chen, Z., Qin, X., Wu, Y., Ling, Y., Ye, Q., Zhao, W. X., and
Shi, G. Pass@k training for adaptively balancing explo-
ration and exploitation of large reasoning models, 2025b.
URL https://arxiv.org/abs/2508.10751.

Cheng, D., Huang, S., Zhu, X., Dai, B., Zhao, W. X., Zhang,
Z., and Wei, F. Reasoning with exploration: An entropy
perspective. In Proceedings of the 40th AAAI Conference
on Artificial Intelligence, 2026.

Cheng, Z., Hao, S., Liu, T., Zhou, F., Xie, Y., Yao, F., Bian,
Y., Zhuang, Y., Dey, N., Zha, Y., Gu, Y., Zhou, K., Wang,
Y., Li, Y., Fan, R., She, J., Gao, C., Saparov, A., Li, H.,
Killian, T. W., Yurochkin, M., Liu, Z., Xing, E. P., and Hu,
Z. Revisiting reinforcement learning for llm reasoning
from a cross-domain perspective. In Advances in Neural
Information Processing Systems, 2025.

Clavier, P., Allassonière, S., and Pennec, E. L. Robust
reinforcement learning with distributional risk-averse for-
mulation, 2022. URL https://arxiv.org/abs/
2206.06841.

Cobbe, K., Hesse, C., Hilton, J., and Schulman, J. Lever-
aging procedural generation to benchmark reinforcement
learning. In Proceedings of the 37th International Con-
ference on Machine Learning, Proceedings of Machine
Learning Research. PMLR, 2020.

Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H.,
Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano,
R., Hesse, C., and Schulman, J. Training verifiers to solve
math word problems, 2021. URL https://arxiv.
org/abs/2110.14168.

Codevilla, F., Müller, M., López, A., Koltun, V., and Doso-
vitskiy, A. End-to-end driving via conditional imitation
learning. In IEEE International Conference on Robotics
and Automation (ICRA), 2018.

Dai, R., Song, L., Liu, H., Liang, Z., Yu, D., Mi, H., Tu, Z.,
Liu, R., Zheng, T., Zhu, H., and Yu, D. Cde: Curiosity-
driven exploration for efficient reinforcement learning in
large language models. In The Fourteenth International
Conference on Learning Representations, Proceedings of
Machine Learning Research. PMLR, 2026.

Dang, X., Baek, C., Kolter, J. Z., and Raghunathan, A.
Assessing diversity collapse in reasoning. In Scaling
Self-Improving Foundation Models without Human Su-
pervision, 2025. URL https://openreview.net/
forum?id=AMiKsHLjQh.

Davis, D. and Recht, B. What is the objective of reasoning
with reinforcement learning?, 2025. URL https://
arxiv.org/abs/2510.13651.

12

### Page links

- [Link 1](arxiv-2107-03374.md)
- [Link 2](https://arxiv.org/abs/2110.14168)
- [Link 3](https://arxiv.org/abs/2206.06841)
- [Link 4](https://arxiv.org/abs/2404.08495)
- [Link 5](https://arxiv.org/abs/2505.14970)
- [Link 6](https://arxiv.org/abs/2508.10751)
- [Link 7](https://arxiv.org/abs/2510.13651)
- [Link 8](https://openreview.net/forum?id=AMiKsHLjQh)

## Page 13

Maximum Likelihood Reinforcement Learning

de Moura, L., Kong, S., Avigad, J., van Doorn, F., and von
Raumer, J. The lean theorem prover (system description).
In Felty, A. P. and Middeldorp, A. (eds.), Automated De-
duction - CADE-25, pp. 378–388, Cham, 2015. Springer
International Publishing. ISBN 978-3-319-21401-6.

Dempster, A. P., Laird, N. M., and Rubin, D. B. Maximum
likelihood from incomplete data via the em algorithm.
Journal of the Royal Statistical Society. Series B (Method-
ological), 39(1):1–38, 1977.
ISSN 00359246.
URL
http://www.jstor.org/stable/2984875.

Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., and
Fei-Fei, L. Imagenet: A large-scale hierarchical image
database. In 2009 IEEE Conference on Computer Vi-
sion and Pattern Recognition, pp. 248–255, 2009. doi:
10.1109/CVPR.2009.5206848.

Dong, H., Xiong, W., Goyal, D., Zhang, Y., Chow, W.,
Pan, R., Diao, S., Zhang, J., Shum, K., and Zhang, T.
Raft: Reward ranked finetuning for generative foundation
model alignment. Transactions on Machine Learning
Research, 2023.

Dong, X., Cheng, J., and Zhang, X. S. Maximum entropy
reinforcement learning with diffusion policy. In Interna-
tional Conference on Machine Learning, Proceedings of
Machine Learning Research. PMLR, 2025.

Duan, Y., Schulman, J., Chen, X., Bartlett, P. L., Sutskever,
I., and Abbeel, P. Rl2: Fast reinforcement learning via
slow reinforcement learning, 2016. URL https://
arxiv.org/abs/1611.02779.

Editya,
A. S.,
Alamin,
M. M.,
Pramana,
A. L.,
and Kurniati, N.
Fraud classification in online
payments using supervised machine learning algo-
rithms.
Green Intelligent Systems and Applications,
5(1):40–50, Mar. 2025.
doi:
10.53623/gisa.v5i1.
552.
URL https://tecnoscientifica.com/
journal/gisa/article/view/552.

Eysenbach, B. and Levine, S. Maximum entropy rl (prov-
ably) solves some robust rl problems. In International
Conference on Learning Representations, 2022.

Eysenbach, B., Gupta, A., Ibarz, J., and Levine, S. Diversity
is all you need: Learning skills without a reward function.
arXiv preprint arXiv:1802.06070, 2018.

Feng, Y., Jain, P., Hartshorn, A., Duan, Y., and Kempe, J.
Don’t waste mistakes: Leveraging negative rl-groups via
confidence reweighting, 2025. URL https://arxiv.
org/abs/2510.08696.

Finn, C., Abbeel, P., and Levine, S. Model-agnostic meta-
learning for fast adaptation of deep networks. In Proceed-
ings of the 34th International Conference on Machine

Learning, Proceedings of Machine Learning Research.
PMLR, 2017.

Fortunato, M., Azar, M. G., Piot, B., Menick, J., Osband, I.,
Graves, A., Mnih, V., Munos, R., Hassabis, D., Pietquin,
O., Blundell, C., and Legg, S. Noisy networks for explo-
ration. In International Conference on Learning Repre-
sentations, 2018.

Gai, J., Zeng, G., Zhang, H., and Raghunathan, A. Differen-
tial smoothing mitigates sharpening and improves LLM
reasoning. In Proceedings of the 43rd International Con-
ference on Machine Learning, Proceedings of Machine
Learning Research. PMLR, 2026.

Gandhi, K., Chakravarthy, A., Singh, A., Lile, N., and
Goodman, N. D. Cognitive behaviors that enable self-
improving reasoners, or, four habits of highly effective
stars. In Conference on Language Modeling (COLM),
2025.

Ged, F. and Veiga, M. H. Matryoshka policy gradient for
entropy-regularized rl: Convergence and global optimal-
ity. Journal of Machine Learning Research, 2024.

Gneiting, T. and Raftery, A. E. Strictly proper scoring
rules, prediction, and estimation. Journal of the American
Statistical Association, 102(477):359–378, 2007. doi:
10.1198/016214506000001437. URL https://doi.
org/10.1198/016214506000001437.

Good, I. J. Rational decisions. Journal of the Royal Statisti-
cal Society: Series B (Methodological), 14(1):107–114,
1952.

Greensmith, E., Bartlett, P. L., and Baxter, J. Variance reduc-
tion techniques for gradient estimates in reinforcement
learning. Journal of Machine Learning Research, 5(Nov):
1471–1530, 2004.

Gropp, W., Boerner, T., Bode, B., and Bauer, G. Delta: Bal-
ancing gpu performance with advanced system interfaces.
Technical report, 2023. URL https://hdl.handle.
net/2142/117179.

Gulcehre, C., Paine, T. L., Srinivasan, S., Konyushkova, K.,
Weerts, L., Sharma, A., Siddhant, A., Ahern, A., Wang,
M., Gu, C., Macherey, W., Doucet, A., Firat, O., and
de Freitas, N. Reinforced self-training (rest) for language
modeling, 2023. URL https://arxiv.org/abs/
2308.08998.

Guo, C., Pleiss, G., Sun, Y., and Weinberger, K. Q. On
calibration of modern neural networks. In Proceedings
of the 34th International Conference on Machine Learn-
ing, Proceedings of Machine Learning Research. PMLR,
2017.

13

### Page links

- [Link 1](http://www.jstor.org/stable/2984875)
- [Link 2](https://arxiv.org/abs/1611.02779)
- [Link 3](../readings/arxiv-2308-08998.md)
- [Link 4](https://arxiv.org/abs/2510.08696)
- [Link 5](https://doi.org/10.1198/016214506000001437)
- [Link 6](https://hdl.handle.net/2142/117179)
- [Link 7](https://tecnoscientifica.com/journal/gisa/article/view/552)

## Page 14

Maximum Likelihood Reinforcement Learning

Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R.,
Zhu, Q., Ma, S., Wang, P., Bi, X., et al. Deepseek-r1: In-
centivizing reasoning capability in llms via reinforcement
learning. arXiv preprint arXiv:2501.12948, 2025.

GX-Chen, A., Prakash, J., Guo, J., Fergus, R., and Ran-
ganath, R. Kl-regularized reinforcement learning for gen-
erative modelling is designed to mode collapse. In The
Fourteenth International Conference on Learning Repre-
sentations, Proceedings of Machine Learning Research.
PMLR, 2026.

Haarnoja, T., Zhou, A., Abbeel, P., and Levine, S. Soft
actor-critic: Off-policy maximum entropy deep reinforce-
ment learning with a stochastic actor. In Proceedings
of the 35th International Conference on Machine Learn-
ing, Proceedings of Machine Learning Research. PMLR,
2018.

Hamid, J. I., Orney, I. H., Xu, E., Finn, C., and Sadigh,
D. Polychromic objectives for reinforcement learning.
In The Fourteenth International Conference on Learning
Representations, 2026. URL https://openreview.
net/forum?id=zzTQISAGUp.

Hao, Z., Wang, H., Liu, H., Luo, J., Yu, J., Dong, H., Lin,
Q., Wang, C., and Chen, J. Rethinking entropy interven-
tions in rlvr: An entropy change perspective, 2025. URL
https://arxiv.org/abs/2510.10150.

He, H. Defeating nondeterminism in LLM inference. Think-
ing Machines Lab Blog, September 2025.

He, K., Zhang, X., Ren, S., and Sun, J. Deep residual learn-
ing for image recognition. In Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition
(CVPR), 2016.

Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart,
S., Tang, E., Song, D., and Steinhardt, J. Measuring
mathematical problem solving with the math dataset.
In Advances in Neural Information Processing Systems,
Datasets and Benchmarks Track, 2021.

Herzog, A., Rao, K., Hausman, K., Lu, Y., Wohlhart, P.,
Yan, M., Lin, J., Arenas, M. G., et al. Deep rl at scale:
Sorting waste in office buildings with a fleet of mobile
manipulators. In Robotics: Science and Systems, 2023.

Hessel, M., Soyer, H., Espeholt, L., Czarnecki, W.,
Schmitt, S., and van Hasselt, H.
Multi-task deep re-
inforcement learning with popart.
In Proceedings of
the Thirty-Third AAAI Conference on Artificial Intelli-
gence and Thirty-First Innovative Applications of Ar-
tificial Intelligence Conference and Ninth AAAI Sym-
posium on Educational Advances in Artificial Intelli-
gence, AAAI’19/IAAI’19/EAAI’19. AAAI Press, 2019.

ISBN 978-1-57735-809-1.
doi: 10.1609/aaai.v33i01.
33013796.
URL https://doi.org/10.1609/
aaai.v33i01.33013796.

Hester, T., Vecerik, M., Pietquin, O., Lanctot, M., Schaul,
T., Piot, B., Horgan, D., Quan, J., Sendonaris, A., Dulac-
Arnold, G., Osband, I., Agapiou, J., Leibo, J. Z., and
Gruslys, A. Deep q-learning from demonstrations. In
Proceedings of the AAAI Conference on Artificial Intelli-
gence, 2018.

Higgins, I., Pal, A., Rusu, A. A., Matthey, L., Burgess, C. P.,
Pritzel, A., Botvinick, M., Blundell, C., and Lerchner,
A. Darla: Improving zero-shot transfer in reinforcement
learning. In Proceedings of the 34th International Con-
ference on Machine Learning, Proceedings of Machine
Learning Research. PMLR, 2017.

Ho, J. and Ermon, S. Generative adversarial imitation learn-
ing. In Advances in Neural Information Processing Sys-
tems, 2016.

Houthooft, R., Chen, X., Chen, X., Duan, Y., Schulman, J.,
De Turck, F., and Abbeel, P. Vime: Variational informa-
tion maximizing exploration. In Lee, D., Sugiyama, M.,
Luxburg, U., Guyon, I., and Garnett, R. (eds.), Advances
in Neural Information Processing Systems, volume 29.
Curran Associates, Inc., 2016.

Hu, J., Liu, M., Lu, X., Wu, F., Harchaoui, Z., Diao, S.,
Choi, Y., Molchanov, P., Yang, J., Kautz, J., and Dong,
Y. BroRL: Scaling reinforcement learning via broadened
exploration. In Proceedings of the 43rd International
Conference on Machine Learning, Proceedings of Ma-
chine Learning Research. PMLR, 2026.

Huang, W., Zhang, Q., Fang, Y., Liang, J., Rong, X., Yao,
H., Wan, G., Liang, K., He, W., Li, M., Rutkowski, L.,
Ye, M., Du, B., and Tao, D. Mapo: Mixed advantage pol-
icy optimization, 2025. URL https://arxiv.org/
abs/2509.18849.

Ishfaq, H., Lan, Q., Xu, P., Mahmood, A. R., Precup, D.,
Anandkumar, A., and Azizzadenesheli, K. Provable and
practical: Efficient exploration in reinforcement learning
via langevin monte carlo. In International Conference on
Learning Representations, 2024a.

Ishfaq, H., Tan, Y., Yang, Y., Lan, Q., Lu, J., Mahmood,
A. R., Precup, D., and Xu, P. More efficient randomized
exploration for reinforcement learning via approximate
sampling. In RLJ, 2024b.

Ishfaq, H., Wang, G., Islam, S. N., and Precup, D. Langevin
soft actor-critic: Efficient exploration through uncertainty-
driven critic learning.
In International Conference
on Learning Representations, Proceedings of Machine
Learning Research. PMLR, 2025.

14

### Page links

- [Link 1](https://arxiv.org/abs/2509.18849)
- [Link 2](https://arxiv.org/abs/2510.10150)
- [Link 3](https://doi.org/10.1609/aaai.v33i01.33013796)
- [Link 4](https://openreview.net/forum?id=zzTQISAGUp)

## Page 15

Maximum Likelihood Reinforcement Learning

Ito, K. and Kashima, K. Risk-sensitive control as infer-
ence with rényi divergence. In The Thirty-eighth Annual
Conference on Neural Information Processing Systems,
2024. URL https://openreview.net/forum?
id=LUIXdWn6Z5.

Iyengar, G. N. Robust dynamic programming. Math. Oper.
Res., 30(2):257–280, May 2005. ISSN 0364-765X. doi:
10.1287/moor.1040.0129. URL https://doi.org/
10.1287/moor.1040.0129.

Jain, T., Garg, P., Chalil, N., Sinha, A., Verma, V. K.,
and Gupta, R. Sms spam classification using machine
learning techniques. In 2022 12th International Confer-
ence on Cloud Computing, Data Science & Engineer-
ing (Confluence), pp. 273–279, 2022.
doi: 10.1109/
Confluence52989.2022.9734128.

Jamil, M., Mihajloska Trpcheska, H., Popovska-Mitrovikj,
A., Dimitrova, V., and Creutzburg, R. Advancing image
spam detection: Evaluating machine learning models
through comparative analysis. Applied Sciences, 15(11),
2025. ISSN 2076-3417. doi: 10.3390/app15116158.
URL https://www.mdpi.com/2076-3417/15/
11/6158.

Jesson, A. and Jiang, Y. Improving generalization on the
procgen benchmark with simple architectural changes
and scale, 2024. URL https://arxiv.org/abs/
2410.10905.

Jia, C. Generalizing reward modeling for out-of-distribution
preference learning. In ECML/PKDD, 2024.

Jiang, Y., Kolter, J. Z., and Raileanu, R. On the importance
of exploration for generalization in reinforcement learn-
ing. In Oh, A., Naumann, T., Globerson, A., Saenko,
K., Hardt, M., and Levine, S. (eds.), Advances in Neural
Information Processing Systems, volume 36, pp. 12951–
12986. Curran Associates, Inc., 2023.

Jiang, Y., Huang, J., Yuan, Y., Mao, X., Yue, Y., Zhao,
Q., and Yan, L. Risk-sensitive reinforcement learning
for alleviating exploration dilemmas in large language
models.
In The Fourteenth International Conference
on Learning Representations, Proceedings of Machine
Learning Research. PMLR, 2026.

Kalashnikov, D., Irpan, A., Pastor, P., Ibarz, J., Herzog,
A., Jang, E., Quillen, D., Holly, E., Kalakrishnan, M.,
Vanhoucke, V., and Levine, S. Qt-opt: Scalable deep
reinforcement learning for vision-based robotic manipu-
lation. In Proceedings of the 2nd Conference on Robot
Learning, Proceedings of Machine Learning Research.
PMLR, 2018.

Khatri, D., Madaan, L., Tiwari, R., Bansal, R., Duvvuri,
S. S., Zaheer, M., Dhillon, I. S., Brandfonbrener, D.,
and Agarwal, R. The art of scaling reinforcement learn-
ing compute for llms. In The Fourteenth International
Conference on Learning Representations, Proceedings of
Machine Learning Research. PMLR, 2026.

Kim, K., Kotha, S., Liang, P., and Hashimoto, T.
Pre-
training under infinite compute. In The Fourteenth In-
ternational Conference on Learning Representations,
2026. URL https://openreview.net/forum?
id=ck0aZTAnwK.

Kingma, D. P. and Ba, J. Adam: A method for stochastic
optimization. In International Conference on Learning
Representations, 2015.

Kirk, R., Mediratta, I., Nalmpantis, C., Luketina, J., Ham-
bro, E., Grefenstette, E., and Raileanu, R. Understanding
the effects of rlhf on llm generalisation and diversity. In
International Conference on Learning Representations,
2024.

Koenig, S. and Simmons, R. G. Complexity analysis of
real-time reinforcement learning. In AAAI, volume 93,
pp. 99–105, 1993.

Kornblith, S., Lee, H., Chen, T., and Norouzi, M. Demystify-
ing loss functions for classification, 2021. URL https:
//openreview.net/forum?id=jNTeYscgSw8.

Kostrikov, I., Yarats, D., and Fergus, R. Image augmentation
is all you need: Regularizing deep reinforcement learning
from pixels. In International Conference on Learning
Representations, 2021.

Krizhevsky, A., Sutskever, I., and Hinton, G. E. Imagenet
classification with deep convolutional neural networks.
Advances in neural information processing systems, 25,
2012.

Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu,
C. H., Gonzalez, J. E., Zhang, H., and Stoica, I. Efficient
memory management for large language model serving
with pagedattention. In Proceedings of the ACM SIGOPS
29th Symposium on Operating Systems Principles, 2023.

Lambert, N., Morrison, J., Pyatkin, V., Huang, S., Ivison,
H., Brahman, F., Miranda, L. J. V., Liu, A., Dziri, N., Lyu,
S., Gu, Y., Malik, S., Graf, V., Hwang, J. D., Yang, J.,
Bras, R. L., Tafjord, O., Wilhelm, C., Soldaini, L., Smith,
N. A., Wang, Y., Dasigi, P., and Hajishirzi, H. Tulu 3:
Pushing frontiers in open language model post-training.
In Conference on Language Modeling (COLM), 2025a.

Lambert, N., Pyatkin, V., Morrison, J., Miranda, L., Lin,
B. Y., Chandu, K., Dziri, N., Kumar, S., Zick, T., Choi, Y.,

15

### Page links

- [Link 1](https://arxiv.org/abs/2410.10905)
- [Link 2](https://doi.org/10.1287/moor.1040.0129)
- [Link 3](https://openreview.net/forum?id=LUIXdWn6Z5)
- [Link 4](https://openreview.net/forum?id=ck0aZTAnwK)
- [Link 5](https://openreview.net/forum?id=jNTeYscgSw8)
- [Link 6](https://www.mdpi.com/2076-3417/15/11/6158)

## Page 16

Maximum Likelihood Reinforcement Learning

Smith, N. A., and Hajishirzi, H. Rewardbench: Evaluat-
ing reward models for language modeling. In Findings of
the Association for Computational Linguistics: NAACL
2025, 2025b.

Laskin, M., Lee, K., Stooke, A., Pinto, L., Abbeel,
P., and Srinivas, A.
Reinforcement learning with
augmented data.
In Larochelle, H., Ranzato, M.,
Hadsell, R., Balcan, M., and Lin, H. (eds.), Ad-
vances in Neural Information Processing Systems,
volume 33, pp. 19884–19895. Curran Associates, Inc.,
2020.
URL https://proceedings.neurips.
cc/paper_files/paper/2020/file/
e615c82aba461681ade82da2da38004a-Paper.
pdf.

Lecun, Y., Bottou, L., Bengio, Y., and Haffner, P. Gradient-
based learning applied to document recognition. Pro-
ceedings of the IEEE, 86(11):2278–2324, 1998.
doi:
10.1109/5.726791.

Lehmann, E. and Casella, G.
Theory of Point Estima-
tion. Springer Texts in Statistics. Springer New York,
2006. ISBN 9780387227283. URL https://books.
google.com/books?id=4f24CgAAQBAJ.

Levine, R. A. and Casella, G.
Implementations of
the monte carlo em algorithm.
Journal of Computa-
tional and Graphical Statistics, 10(3):422–439, 2001.
ISSN 10618600. URL http://www.jstor.org/
stable/1391097.

Levine, S. Reinforcement learning and control as prob-
abilistic inference: Tutorial and review, 2018.
URL
https://arxiv.org/abs/1805.00909.

Levine, S. and Koltun, V. Guided policy search. In Das-
gupta, S. and McAllester, D. (eds.), Proceedings of the
30th International Conference on Machine Learning, vol-
ume 28 of Proceedings of Machine Learning Research,
pp. 1–9, Atlanta, Georgia, USA, 17–19 Jun 2013. PMLR.
URL https://proceedings.mlr.press/v28/
levine13.html.

Lewkowycz, A., Andreassen, A., Dohan, D., Dyer, E.,
Michalewski, H., Ramasesh, V., Slone, A., Anil, C.,
Schlag, I., Gutman-Solo, T., Wu, Y., Neyshabur, B., Gur-
Ari, G., and Misra, V. Solving quantitative reasoning
problems with language models. In Advances in Neural
Information Processing Systems, 2022.

Li, C., Liu, K., and Liu, S. A survey of loss functions
in deep learning. Mathematics, 13(15), 2025. ISSN
2227-7390. doi: 10.3390/math13152417. URL https:
//www.mdpi.com/2227-7390/13/15/2417.

Li, Z., Yi, M., Wang, Y., Cui, S., and Liu, Y. Towards a the-
oretical understanding to the generalization of rlhf, 2026.
URL https://arxiv.org/abs/2601.16403.

Liang, A., Tennenholtz, G., wei Hsu, C., Chow, Y., Bıyık,
E., and Boutilier, C. Dynamite-rl: A dynamic model
for improved temporal meta-reinforcement learning. In
Neural Information Processing Systems, 2024.

Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker,
B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and
Cobbe, K. Let’s verify step by step. In International
Conference on Learning Representations, 2024.

Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T.,
Tassa, Y., Silver, D., and Wierstra, D. Continuous con-
trol with deep reinforcement learning. In International
Conference on Learning Representations, 2016.

Lin, Y., Seto, S., Ter Hoeve, M., Metcalf, K., Theobald,
B.-J., Wang, X., Zhang, Y., Huang, C., and Zhang, T.
On the limited generalization capability of the implicit
reward model induced by direct preference optimization.
In Al-Onaizan, Y., Bansal, M., and Chen, Y.-N. (eds.),
Findings of the Association for Computational Linguis-
tics: EMNLP 2024, pp. 16015–16026, Miami, Florida,
USA, November 2024. Association for Computational
Linguistics.
doi:
10.18653/v1/2024.findings-emnlp.
940. URL https://aclanthology.org/2024.
findings-emnlp.940/.

Liu, B., Zhu, Y., Gao, C., Feng, Y., Liu, Q., Zhu, Y., and
Stone, P. Libero: Benchmarking knowledge transfer for
lifelong robot learning. In Advances in Neural Informa-
tion Processing Systems, 2023.

Liu, M., Diao, S., Lu, X., Hu, J., Dong, X., Choi, Y., Kautz,
J., and Dong, Y. Prorl: Prolonged reinforcement learning
expands reasoning boundaries in large language models.
In Advances in Neural Information Processing Systems
38 (NeurIPS 2025), 2025a.

Liu, Z., Chen, C., Li, W., Qi, P., Pang, T., Du, C., Lee, W. S.,
and Lin, M. Understanding r1-zero-like training: A crit-
ical perspective. In Conference on Language Modeling
(COLM), 2025b.

Liu, Z., Kim, J., Luo, X., Li, D., and Yang, Y.
Ex-
ploratory memory-augmented LLM agent via hybrid
on- and off-policy optimization.
In The Fourteenth
International Conference on Learning Representations,
2026. URL https://openreview.net/forum?
id=UOzxviKVFO.

Loshchilov, I. and Hutter, F. Sgdr: Stochastic gradient
descent with warm restarts. In International Conference
on Learning Representations, 2017.

16

### Page links

- [Link 1](http://www.jstor.org/stable/1391097)
- [Link 2](https://aclanthology.org/2024.findings-emnlp.940/)
- [Link 3](https://arxiv.org/abs/1805.00909)
- [Link 4](https://arxiv.org/abs/2601.16403)
- [Link 5](https://books.google.com/books?id=4f24CgAAQBAJ)
- [Link 6](https://openreview.net/forum?id=UOzxviKVFO)
- [Link 7](https://proceedings.mlr.press/v28/levine13.html)
- [Link 8](https://proceedings.neurips.cc/paper_files/paper/2020/file/e615c82aba461681ade82da2da38004a-Paper.pdf)
- [Link 9](https://www.mdpi.com/2227-7390/13/15/2417)

## Page 17

Maximum Likelihood Reinforcement Learning

Loshchilov, I. and Hutter, F. Decoupled weight decay reg-
ularization. In International Conference on Learning
Representations, 2019.

Lu, M., Zhong, H., Zhang, T., and Blanchet, J. Distribu-
tionally robust reinforcement learning with interactive
data collection: Fundamental hardness and near-optimal
algorithm. In Neural Information Processing Systems,
2024.

Luo, M., Tan, S., Huang, R., Patel, A., Ariyak, A., Wu,
Q., Shi, X., Xin, R., Cai, C., Weber, M., Zhang, C., Li,
L. E., Popa, R. A., and Stoica, I. Deepcoder: A fully
open-source 14b coder at o3-mini level, 2025.

Mahdavi, S., Li, M., Liu, K., Liao, R., and Thrampoulidis,
C.
Beyond accuracy: A policy gradient reweighting
approach for pass@k maximization in LLMs. In 2nd AI
for Math Workshop @ ICML 2025, 2025. URL https:
//openreview.net/forum?id=Dn3gk9auxd.

Mao, A., Mohri, M., and Zhong, Y. Cross-entropy loss func-
tions: Theoretical analysis and applications. In Proceed-
ings of the 40th International Conference on Machine
Learning, Proceedings of Machine Learning Research.
PMLR, 2023.

MathArena.
Hmmt
february
2025.
https:
//huggingface.co/datasets/MathArena/
hmmt_feb_2025, 2025a.

MathArena.
Hmmt
november
2025.
https:
//huggingface.co/datasets/MathArena/
hmmt_nov_2025, 2025b.

McCandlish, S., Kaplan, J., Amodei, D., and OpenAI Dota
Team. An empirical model of Large-Batch training, 2018.
URL https://arxiv.org/abs/1812.06162.

Mensch, A. and Blondel, M. Differentiable dynamic pro-
gramming for structured prediction and attention. In
Proceedings of the 35th International Conference on Ma-
chine Learning, Proceedings of Machine Learning Re-
search. PMLR, 2018.

Millidge, B., Tschantz, A., Seth, A. K., and Buckley, C. L.
On the relationship between active inference and con-
trol as inference. In International Workshop on Active
Inference, 2020.

MiniMax, :, Chen, A., Li, A., Gong, B., Jiang, B., Fei, B.,
Yang, B., Shan, B., Yu, C., Wang, C., Zhu, C., Xiao, C.,
Du, C., et al. Minimax-m1: Scaling test-time compute
efficiently with lightning attention, 2025. URL https:
//arxiv.org/abs/2506.13585.

Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A.,
Antonoglou, I., Wierstra, D., and Riedmiller, M. Play-
ing atari with deep reinforcement learning, 2013. URL
https://arxiv.org/abs/1312.5602.

Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Ve-
ness, J., Bellemare, M. G., Graves, A., Riedmiller, M.,
Fidjeland, A. K., Ostrovski, G., Petersen, S., Beattie,
C., Sadik, A., Antonoglou, I., King, H., Kumaran, D.,
Wierstra, D., Legg, S., and Hassabis, D. Human-level
control through deep reinforcement learning. Nature, 518
(7540):529–533, February 2015. ISSN 00280836. URL
http://dx.doi.org/10.1038/nature14236.

Motwani, S. R., Ivanova, A., Cai, Z., Torr, P., Islam, R.,
Shah, S., Schroeder de Witt, C., and London, C. h1:
Bootstrapping LLMs to reason over longer horizons via
reinforcement learning. In Proceedings of the 43rd Inter-
national Conference on Machine Learning, Proceedings
of Machine Learning Research. PMLR, 2026.

Mroueh, Y. Reinforcement learning with verifiable rewards:
GRPO’s effective loss, dynamics, and success amplifica-
tion. In Proceedings of the 43rd International Conference
on Machine Learning, Proceedings of Machine Learning
Research. PMLR, 2026.

Murphy, K. P. Machine Learning: a Probabilistic Perspec-
tive. MIT Press, 2012. ISBN 978-0262018029.

Nair, A., McGrew, B., Andrychowicz, M., Zaremba, W.,
and Abbeel, P. Overcoming exploration in reinforcement
learning with demonstrations.
In IEEE International
Conference on Robotics and Automation (ICRA), 2018.

Ng, A. and Jordan, M. On discriminative vs. generative
classifiers: A comparison of logistic regression and naive
bayes. In Dietterich, T., Becker, S., and Ghahramani,
Z. (eds.), Advances in Neural Information Processing
Systems, volume 14. MIT Press, 2001.

Nguyen, M. N., Baker, A., Neo, C., Roush, A., Kirsch, A.,
and Shwartz-Ziv, R. Turning up the heat: Min-p sampling
for creative and coherent LLM outputs. In International
Conference on Learning Representations, Proceedings of
Machine Learning Research. PMLR, 2025a.

Nguyen, P. M., La, C. D., Nguyen, D. M. H., Chawla, N. V.,
Nguyen, B. T., and Doan, K. D. The reasoning bound-
ary paradox: How reinforcement learning constrains lan-
guage models, 2025b. URL https://arxiv.org/
abs/2510.02230.

Ni, K., Tan, Z., Liu, Z., Li, P., and Chen, T. Can grpo
help llms transcend their pretraining origin?, 2025. URL
https://arxiv.org/abs/2510.15990.

17

### Page links

- [Link 1](http://dx.doi.org/10.1038/nature14236)
- [Link 2](https://arxiv.org/abs/1312.5602)
- [Link 3](https://arxiv.org/abs/1812.06162)
- [Link 4](arxiv-2506-13585.md)
- [Link 5](https://arxiv.org/abs/2510.02230)
- [Link 6](https://arxiv.org/abs/2510.15990)
- [Link 7](https://huggingface.co/datasets/MathArena/hmmt_feb_2025)
- [Link 8](https://huggingface.co/datasets/MathArena/hmmt_nov_2025)
- [Link 9](https://openreview.net/forum?id=Dn3gk9auxd)

## Page 18

Maximum Likelihood Reinforcement Learning

Niculescu-Mizil, A. and Caruana, R. Predicting good prob-
abilities with supervised learning.
In Proceedings of
the 22nd International Conference on Machine Learning,
ICML ’05, pp. 625–632, New York, NY, USA, 2005. As-
sociation for Computing Machinery. ISBN 1595931805.
doi: 10.1145/1102351.1102430. URL https://doi.
org/10.1145/1102351.1102430.

Nie, W., Wu, J., Liu, J., Li, Z., Lin, Z., Zijian, Z., Fan,
Y., Zheng, H., and Jang, J.-S. R. Gradient starvation
in binary-reward grpo: Why group-mean centering fails
and why the simplest fix works, 2026. URL https:
//arxiv.org/abs/2605.07689.

Nilim, A. and Ghaoui, L. E.
Robust markov deci-
sion processes with uncertain transition matrices, 2004.
AAI3165509.

O’Donoghue, B., Osband, I., and Ionescu, C. Making sense
of reinforcement learning and probabilistic inference. In
International Conference on Learning Representations,
2020.

Olmo, T., :, Ettinger, A., Bertsch, A., Kuehl, B., Graham,
D., Heineman, D., Groeneveld, D., Brahman, F., et al.
Olmo 3, 2025. URL https://arxiv.org/abs/
2512.13961.

OpenAI, :, Berner, C., Brockman, G., Chan, B., Che-
ung, V., D˛ebiak, P., Dennison, C., Farhi, D., Fischer,
Q., Hashme, S., Hesse, C., et al.
Dota 2 with large
scale deep reinforcement learning, 2019. URL https:
//arxiv.org/abs/1912.06680.

OpenAI, Jaech, A., Kalai, A., Lerer, A., Richardson, A., El-
Kishky, A., Low, A., Helyar, A., Madry, A., Beutel, A.,
Carney, A., et al. Openai o1 system card. arXiv preprint
arXiv:2412.16720, 2024.

Orney, I. H., Hamid, J. I., Ramanujam, S. S., Wu, S.,
Hu, H., Goodman, N., Sadigh, D., and Finn, C. Poly-
epo: Training exploratory reasoning models, 2026. URL
https://arxiv.org/abs/2604.17654.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright,
C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K.,
Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L.,
Simens, M., Askell, A., Welinder, P., Christiano, P., Leike,
J., and Lowe, R. Training language models to follow
instructions with human feedback. In Advances in Neural
Information Processing Systems, 2022.

Pang, R. Y., Yuan, W., Cho, K., He, H., Sukhbaatar, S., and
Weston, J. Iterative reasoning preference optimization. In
Neural Information Processing Systems, 2024.

Pathak, D., Agrawal, P., Efros, A. A., and Darrell, T.
Curiosity-driven exploration by self-supervised predic-
tion. In International conference on machine learning,
pp. 2778–2787. PMLR, 2017.

Pathak, D., Gandhi, D., and Gupta, A. Self-supervised
exploration via disagreement. In International conference
on machine learning, pp. 5062–5071. PMLR, 2019.

Peng, X. B., Kumar, A., Zhang, G., and Levine, S.
Advantage-weighted regression: Simple and scalable
off-policy reinforcement learning, 2019. URL https:
//arxiv.org/abs/1910.00177.

Peters, J. and Schaal, S.
Reinforcement learning by
reward-weighted regression for operational space con-
trol. In Proceedings of the 24th International Confer-
ence on Machine Learning, ICML ’07, pp. 745–750,
New York, NY, USA, 2007. Association for Comput-
ing Machinery.
ISBN 9781595937933.
doi:
10.
1145/1273496.1273590. URL https://doi.org/
10.1145/1273496.1273590.

Petrenko, A., Lipkin, B., Chen, K., Wijmans, E., Cusumano-
Towner, M. F., Giryes, R., and Kraehenbuehl, P. Entropy-
preserving reinforcement learning. In The Fourteenth
International Conference on Learning Representations,
2026. URL https://openreview.net/forum?
id=E8MR8jgEeZ.

Pomerleau, D. A. Alvinn: an autonomous land vehicle in a
neural network. In Proceedings of the 2nd International
Conference on Neural Information Processing Systems,
NIPS’88, pp. 305–313, Cambridge, MA, USA, 1988.
MIT Press.

Prim, R. C. Shortest connection networks and some gen-
eralizations. The Bell System Technical Journal, 36(6):
1389–1401, 1957.

Qu, Y., Setlur, A., Smith, V., Salakhutdinov, R., and
Kumar, A.
Pope: Learning to reason on hard prob-
lems via privileged on-policy exploration, 2025. URL
https://arxiv.org/abs/2601.18779.

Qu, Y., Singh, A., Lee, Y., Setlur, A., Salakhutdinov, R.,
Finn, C., and Kumar, A. Rlad: Training llms to dis-
cover abstractions for solving reasoning problems. In The
Fourteenth International Conference on Learning Repre-
sentations, Proceedings of Machine Learning Research.
PMLR, 2026.

Qwen, :, Yang, A., Yang, B., Zhang, B., Hui, B., Zheng,
B., Yu, B., Li, C., et al. Qwen2.5 technical report, 2025.
URL https://arxiv.org/abs/2412.15115.

Radford, A., Narasimhan, K., Salimans, T., and Sutskever,
I. Improving language understanding by generative pre-
training. 2018.

18

### Page links

- [Link 1](https://arxiv.org/abs/1910.00177)
- [Link 2](https://arxiv.org/abs/1912.06680)
- [Link 3](https://arxiv.org/abs/2412.15115)
- [Link 4](https://arxiv.org/abs/2512.13961)
- [Link 5](https://arxiv.org/abs/2601.18779)
- [Link 6](https://arxiv.org/abs/2604.17654)
- [Link 7](https://arxiv.org/abs/2605.07689)
- [Link 8](https://doi.org/10.1145/1102351.1102430)
- [Link 9](https://doi.org/10.1145/1273496.1273590)
- [Link 10](https://openreview.net/forum?id=E8MR8jgEeZ)

## Page 19

Maximum Likelihood Reinforcement Learning

Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and
Sutskever, I. Language models are unsupervised multitask
learners. 2019.

Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning,
C. D., and Finn, C. Direct preference optimization: Your
language model is secretly a reward model. In Advances
in Neural Information Processing Systems, 2023.

Raileanu, R., Goldstein, M., Yarats, D., Kostrikov, I., and
Fergus, R. Automatic data augmentation for general-
ization in deep reinforcement learning. In Advances in
Neural Information Processing Systems, 2021.

Rawlik, K., Toussaint, M., and Vijayakumar, S. On stochas-
tic optimal control and reinforcement learning by approx-
imate inference. Proceedings of Robotics: Science and
Systems VIII, 2012.

Rosenblatt,
F.
The
perceptron:
a
probabilistic
model for information storage and organization in
the brain.
Psychological review,
65 6:386–408,
1958.
URL https://api.semanticscholar.
org/CorpusID:12781225.

Ross, S. and Bagnell, D. Efficient reductions for imita-
tion learning. In Teh, Y. W. and Titterington, M. (eds.),
Proceedings of the Thirteenth International Conference
on Artificial Intelligence and Statistics, volume 9 of
Proceedings of Machine Learning Research, pp. 661–
668, Chia Laguna Resort, Sardinia, Italy, 13–15 May
2010. PMLR. URL https://proceedings.mlr.
press/v9/ross10a.html.

Ross, S., Gordon, G. J., and Bagnell, J. A. A reduction of
imitation learning and structured prediction to no-regret
online learning. In Proceedings of the 14th International
Conference on Artificial Intelligence and Statistics, Pro-
ceedings of Machine Learning Research. PMLR, 2011.

Rumelhart, D. E., Hinton, G. E., and Williams, R. J. Learn-
ing representations by back-propagating errors. Nature,
323(6088):533–536, 1986. doi: 10.1038/323533a0.

Russo, D. Success-conditioning as policy improvement:
The optimization problem solved by imitating success.
In Proceedings of the 43rd International Conference on
Machine Learning, Proceedings of Machine Learning
Research. PMLR, 2026.

Ruth, W. A review of monte carlo-based versions of the em
algorithm, 2024. URL https://arxiv.org/abs/
2401.00945.

Savage, L. J.
Elicitation of personal probabilities
and expectations.
Journal of the American Statis-
tical Association, 66(336):783–801, 1971.
ISSN
01621459, 1537274X.
URL http://www.jstor.
org/stable/2284229.

Schaeffer, R., Kazdan, J., Hughes, J., Juravsky, J., Price,
S., Lynch, A., Jones, E., Kirk, R., Mirhoseini, A., and
Koyejo, S. How do large language monkeys get their
power (laws)? In International Conference on Machine
Learning, Proceedings of Machine Learning Research.
PMLR, 2025.

Schaul, T., Borsa, D., Modayil, J., and Pascanu, R. Ray
interference: a source of plateaus in deep reinforcement
learning, 2019. URL https://arxiv.org/abs/
1904.11455.

Schmidhuber, J. Curious model-building control systems. In
Proc. international joint conference on neural networks,
pp. 1458–1463, 1991.

Schmidhuber, J. Gödel machines: Fully self-referential
optimal universal self-improvers. In Artificial general
intelligence, pp. 199–226. Springer, 2007.

Schulman, J., Levine, S., Moritz, P., Jordan, M. I., and
Abbeel, P. Trust region policy optimization. In Proceed-
ings of the 32nd International Conference on Machine
Learning, Proceedings of Machine Learning Research.
PMLR, 2015.

Schulman, J., Wolski, F., Dhariwal, P., Radford, A.,
and Klimov, O.
Proximal policy optimization algo-
rithms, 2017.
URL https://arxiv.org/abs/
1707.06347.

Setlur, A., Yang, M. Y. R., Snell, C. V., Greer, J., Wu, I.,
Smith, V., Simchowitz, M., and Kumar, A. e3: Learning
to explore enables extrapolation of test-time compute
for LLMs. In The Fourteenth International Conference
on Learning Representations, 2026. URL https://
openreview.net/forum?id=aID0dZmMmM.

Shafayat, S., Tajwar, F., Salakhutdinov, R., Schneider,
J., and Zanette, A. Can large reasoning models self-
train?, 2025.
URL https://arxiv.org/abs/
2505.21444.

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X.,
Zhang, H., Zhang, M., Li, Y. K., Wu, Y., and Guo,
D.
Deepseekmath: Pushing the limits of mathemat-
ical reasoning in open language models, 2024. URL
https://arxiv.org/abs/2402.03300.

Sharma, A., Gu, S., Levine, S., Kumar, V., and Hausman, K.
Dynamics-aware unsupervised discovery of skills. arXiv
preprint arXiv:1907.01657, 2019.

Sheng, G., Zhang, C., Ye, Z., Wu, X., Zhang, W., Zhang,
R., Peng, Y., Lin, H., and Wu, C. Hybridflow: A flexi-
ble and efficient rlhf framework. arXiv preprint arXiv:
2409.19256, 2024.

19

### Page links

- [Link 1](http://www.jstor.org/stable/2284229)
- [Link 2](https://api.semanticscholar.org/CorpusID:12781225)
- [Link 3](arxiv-1707-06347.md)
- [Link 4](https://arxiv.org/abs/1904.11455)
- [Link 5](https://arxiv.org/abs/2401.00945)
- [Link 6](../readings/arxiv-2402-03300.md)
- [Link 7](https://arxiv.org/abs/2505.21444)
- [Link 8](https://openreview.net/forum?id=aID0dZmMmM)
- [Link 9](https://proceedings.mlr.press/v9/ross10a.html)

## Page 20

Maximum Likelihood Reinforcement Learning

Shi, L., Li, G., Wei, Y., Chen, Y., Geist, M., and Chi, Y. The
curious price of distributional robustness in reinforcement
learning with a generative model. In Advances in Neural
Information Processing Systems, 2023.

Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L.,
Van Den Driessche, G., Schrittwieser, J., Antonoglou, I.,
Panneershelvam, V., Lanctot, M., et al. Mastering the
game of go with deep neural networks and tree search.
nature, 529(7587):484–489, 2016.

Smith, N. A.
Linguistic Structure Prediction.
Mor-
gan & Claypool Publishers, 1st edition, 2011. ISBN
1608454053.

Song, Y., Kempe, J., and Munos, R.
Outcome-based
exploration for llm reasoning, 2025.
URL https:
//arxiv.org/abs/2509.06941.

Srinivas, A., Laskin, M., and Abbeel, P. Curl: Contrastive
unsupervised representations for reinforcement learning.
In Proceedings of the 37th International Conference on
Machine Learning, Proceedings of Machine Learning
Research. PMLR, 2020.

Stojanovski, Z., Stanley, O., Sharratt, J., Jones, R., Adefioye,
A., Kaddour, J., and Köpf, A. Reasoning gym: Reasoning
environments for reinforcement learning with verifiable
rewards. In Advances in Neural Information Processing
Systems, 2025.

Strehl, A. L., Li, L., and Littman, M. L.
Reinforce-
ment learning in finite mdps:
Pac analysis.
Jour-
nal of Machine Learning Research, 10(84):2413–2444,
2009.
URL http://jmlr.org/papers/v10/
strehl09a.html.

Su, J., Lu, Y., Pan, S., Murtadha, A., Wen, B., and Liu,
Y. Roformer: Enhanced transformer with rotary position
embedding. Neurocomputing, 2024.

Sutton, R. S. Learning to predict by the methods of temporal
differences. Machine Learning, 1988.

Sutton, R. S., Barto, A. G., et al. Reinforcement learning:
An introduction, volume 1. MIT press Cambridge, 1998.

Sutton, R. S., McAllester, D., Singh, S., and Mansour, Y.
Policy gradient methods for reinforcement learning with
function approximation. Advances in neural information
processing systems, 12, 1999.

Tajwar, F., Singh, A., Sharma, A., Rafailov, R., Schneider,
J., Xie, T., Ermon, S., Finn, C., and Kumar, A. Preference
fine-tuning of llms should leverage suboptimal, on-policy
data. In International Conference on Machine Learn-
ing, Proceedings of Machine Learning Research. PMLR,
2024.

Tajwar, F., Jiang, Y., Thankaraj, A., Rahman, S. S., Kolter,
J. Z., Schneider, J., and Salakhutdinov, R. Training a
generally curious agent. In International Conference on
Machine Learning, Proceedings of Machine Learning
Research. PMLR, 2025.

Tang, Y., Zheng, K., Synnaeve, G., and Munos, R. Optimiz-
ing language models for inference time objectives using
reinforcement learning. In International Conference on
Machine Learning, Proceedings of Machine Learning
Research. PMLR, 2025.

Tarbouriech, J., Lattimore, T., and O’Donoghue, B. Prob-
abilistic inference in reinforcement learning done right.
In Advances in Neural Information Processing Systems,
2023.

Team, K., Du, A., Gao, B., Xing, B., Jiang, C., Chen, C.,
Li, C., Xiao, C., Du, C., et al. Kimi k1.5: Scaling re-
inforcement learning with llms, 2025. URL https:
//arxiv.org/abs/2501.12599.

Terven, J., Cordova-Esparza, D.-M., Romero-González,
J.-A., Ramírez-Pedraza, A., and Chávez-Urbiola, E. A.
A comprehensive survey of loss functions and metrics
in deep learning.
Artificial Intelligence Review, 58
(7), April 2025.
ISSN 1573-7462.
doi: 10.1007/
s10462-025-11198-7. URL http://dx.doi.org/
10.1007/s10462-025-11198-7.

Thompson, W. R. On the likelihood that one unknown
probability exceeds another in view of the evidence of
two samples. Biometrika, 25(3-4):285–294, 1933.

Thrampoulidis, C., Mahdavi, S., and Deng, W. Advan-
tage shaping as surrogate reward maximization: Unifying
pass@k policy gradients. Transactions on Machine Learn-
ing Research, 2026. ISSN 2835-8856. URL https:
//openreview.net/forum?id=R1RhBFUk8t.

Thrun, S., Burgard, W., and Fox, D. Probabilistic Robotics
(Intelligent Robotics and Autonomous Agents). The MIT
Press, 2005. ISBN 0262201623.

Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi,
A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P.,
et al. Llama 2: Open foundation and fine-tuned chat mod-
els, 2023. URL https://arxiv.org/abs/2307.
09288.

Tuyls, J., Foster, D. J., Krishnamurthy, A., and Ash, J. T.
Representation-based exploration for language models:
From test-time to post-training. In The Fourteenth Inter-
national Conference on Learning Representations, Pro-
ceedings of Machine Learning Research. PMLR, 2026.

van der Vaart, A. W. Asymptotic Statistics. Cambridge
Series in Statistical and Probabilistic Mathematics. Cam-
bridge University Press, 1998.

20

### Page links

- [Link 1](http://dx.doi.org/10.1007/s10462-025-11198-7)
- [Link 2](http://jmlr.org/papers/v10/strehl09a.html)
- [Link 3](https://arxiv.org/abs/2307.09288)
- [Link 4](https://arxiv.org/abs/2501.12599)
- [Link 5](https://arxiv.org/abs/2509.06941)
- [Link 6](https://openreview.net/forum?id=R1RhBFUk8t)

## Page 21

Maximum Likelihood Reinforcement Learning

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones,
L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. At-
tention is all you need. Advances in neural information
processing systems, 30, 2017.

Vecerik, M., Hester, T., Scholz, J., Wang, F., Pietquin, O.,
Piot, B., Heess, N., Rothörl, T., Lampe, T., and Riedmiller,
M. Leveraging demonstrations for deep reinforcement
learning on robotics problems with sparse rewards, 2018.
URL https://arxiv.org/abs/1707.08817.

Vendrow, J., Vendrow, E., Beery, S., and Madry, A. Do large
language model benchmarks test reliability?, 2025. URL
https://arxiv.org/abs/2502.03461.

Vinyals, O., Babuschkin, I., Czarnecki, W. M., Mathieu, M.,
Dudzik, A., Chung, J., Choi, D. H., Powell, R., Ewalds,
T., Georgiev, P., et al. Grandmaster level in starcraft ii
using multi-agent reinforcement learning. nature, 575
(7782):350–354, 2019.

Waghmare, K. and Ziegel, J. Proper scoring rules for estima-
tion and forecast evaluation. Annual Review of Statistics
and Its Application, 2025.

Walder, C. and Karkhanis, D. Pass@k policy optimiza-
tion: Solving harder reinforcement learning problems. In
Advances in Neural Information Processing Systems 38
(NeurIPS 2025), 2025.

WANG, K., Kang, B., Shao, J., and Feng, J. Improving
generalization in reinforcement learning with mixture
regularization. In Larochelle, H., Ranzato, M., Hadsell,
R., Balcan, M., and Lin, H. (eds.), Advances in Neural
Information Processing Systems, volume 33, pp. 7968–
7978. Curran Associates, Inc., 2020.

Wang, Q., Ma, Y., Zhao, K., and jie Tian, Y. A comprehen-
sive survey of loss functions in machine learning. Annals
of Data Science, 9:187 – 212, 2020.

Wang, S., Yu, L., Gao, C., Zheng, C., Liu, S., Lu, R., Dang,
K., Chen, X.-H., Yang, J., Zhang, Z., Liu, Y., Yang, A.,
Zhao, A., Yue, Y., Song, S., Yu, B., Huang, G., and Lin,
J. Beyond the 80/20 rule: High-entropy minority tokens
drive effective reinforcement learning for LLM reason-
ing. In The Thirty-ninth Annual Conference on Neural
Information Processing Systems, 2025. URL https:
//openreview.net/forum?id=yfcpdY4gMP.

Wang, X., Lian, L., and Yu, S. X. Unsupervised visual
attention and invariance for reinforcement learning. In
Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), 2021.

Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang,
S., Chowdhery, A., and Zhou, D. Self-consistency im-
proves chain of thought reasoning in language models. In

International Conference on Learning Representations,
2023a.

Wang, Y., Ivison, H., Dasigi, P., Hessel, J., Khot, T., Chandu,
K. R., Wadden, D., MacMillan, K., Smith, N. A., Beltagy,
I., and Hajishirzi, H. How far can camels go? exploring
the state of instruction tuning on open resources. In Ad-
vances in Neural Information Processing Systems, 2023b.

Watkins, C. J. C. H. and Dayan, P.
Q-learning.
Ma-
chine Learning, 8(3–4):279–292, 1992. doi: 10.1007/
BF00992698. URL https://doi.org/10.1007/
BF00992698.

Wei, G. C. G. and Tanner, M. A.
A monte carlo im-
plementation of the em algorithm and the poor man’s
data augmentation algorithms. Journal of the American
Statistical Association, 85(411):699–704, 1990. ISSN
01621459, 1537274X.
URL http://www.jstor.
org/stable/2290005.

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B.,
Xia, F., Chi, E., Le, Q., and Zhou, D. Chain-of-thought
prompting elicits reasoning in large language models.
In Advances in Neural Information Processing Systems,
2022.

Williams, R. J. Simple statistical gradient-following algo-
rithms for connectionist reinforcement learning. Machine
learning, 8:229–256, 1992.

Wu, F., Xuan, W., Lu, X., Liu, M., Dong, Y., Harchaoui, Z.,
and Choi, Y. The invisible leash: Why rlvr may or may
not escape its origin, 2026. URL https://arxiv.
org/abs/2507.14843.

Xiong, W., Yao, J., Xu, Y., Pang, B., Wang, L., Sahoo,
D., Li, J., Jiang, N., Zhang, T., Xiong, C., and Dong, H.
A minimalist approach to llm reasoning: from rejection
sampling to reinforce, 2025a. URL https://arxiv.
org/abs/2504.11343.

Xiong, W., Ye, C., Liao, B., Dong, H., Xu, X., Monz,
C., Bian, J., Jiang, N., and Zhang, T. Reinforce-ada:
An adaptive sampling framework under non-linear rl ob-
jectives, 2025b. URL https://arxiv.org/abs/
2510.04996.

Xu, S., Fu, W., Gao, J., Ye, W., Liu, W., Mei, Z., Wang,
G., Yu, C., and Wu, Y. Is dpo superior to ppo for llm
alignment? a comprehensive study. In International Con-
ference on Machine Learning, Proceedings of Machine
Learning Research. PMLR, 2024.

Yang, A., Yang, B., Hui, B., Zheng, B., Yu, B., Zhou, C., Li,
C., Li, C., Liu, D., Huang, F., Dong, G., Wei, H., Lin, H.,
Tang, J., Wang, J., et al. Qwen2 technical report, 2024a.
URL https://arxiv.org/abs/2407.10671.

21

### Page links

- [Link 1](http://www.jstor.org/stable/2290005)
- [Link 2](https://arxiv.org/abs/1707.08817)
- [Link 3](https://arxiv.org/abs/2407.10671)
- [Link 4](https://arxiv.org/abs/2502.03461)
- [Link 5](https://arxiv.org/abs/2504.11343)
- [Link 6](https://arxiv.org/abs/2507.14843)
- [Link 7](https://arxiv.org/abs/2510.04996)
- [Link 8](https://doi.org/10.1007/BF00992698)
- [Link 9](https://openreview.net/forum?id=yfcpdY4gMP)

## Page 22

Maximum Likelihood Reinforcement Learning

Yang, A., Zhang, B., Hui, B., Gao, B., Yu, B., Li, C., Liu,
D., Tu, J., et al. Qwen2.5-math technical report: Toward
mathematical expert model via self-improvement, 2024b.
URL https://arxiv.org/abs/2409.12122.

Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B.,
Yu, B., Gao, C., et al. Qwen3 technical report, 2025. URL

https://arxiv.org/abs/2505.09388.

Yang, F., Chen, Z., Wang, X., Lu, X., Chai, J., Yin, G., Lin,
W., Ma, S., Zhuang, F., Wang, D., Yang, Y., Li, J., and
Ban, Y. Your group-relative advantage is biased, 2026a.
URL https://arxiv.org/abs/2601.08521.

Yang, K., Tao, J., Lyu, J., and Li, X. Exploration and
anti-exploration with distributional random network dis-
tillation. In International Conference on Machine Learn-
ing, Proceedings of Machine Learning Research. PMLR,
2024c.

Yang, Z., Guo, Z., Huang, Y., Wang, Y., Xie, D., Li, H.,
Wang, Y., Liang, X., and Tang, J. Depth-breadth syn-
ergy in rlvr: Unlocking llm reasoning gains with adaptive
exploration. In Proceedings of the 43rd International
Conference on Machine Learning, Proceedings of Ma-
chine Learning Research. PMLR, 2026b.

Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai,
W., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma,
B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang,
W., Zhu, H., Zhu, J., Chen, J., Chen, J., Wang, C., Yu, H.,
Song, Y., Wei, X., Zhou, H., Liu, J., Ma, W.-Y., Zhang,
Y.-Q., Yan, L., Qiao, M., Wu, Y., and Wang, M. Dapo: An
open-source llm reinforcement learning system at scale.
In Advances in Neural Information Processing Systems
38 (NeurIPS 2025), 2025.

Yu, T., Quillen, D., He, Z., Julian, R., Narayan, A., Shively,
H., Bellathur, A., Hausman, K., Finn, C., and Levine,
S. Meta-world: A benchmark and evaluation for multi-
task and meta reinforcement learning. In Proceedings of
the 3rd Conference on Robot Learning, Proceedings of
Machine Learning Research. PMLR, 2019.

Yu, Z., Su, W., Tao, L., Wang, H., Singh, A., Yu, H., Wang,
J., Gao, H., Yuan, W., Weston, J., Yu, P., and Xu, J.
Restrain: From spurious votes to signals — self-driven rl
with self-penalization. In The Fourteenth International
Conference on Learning Representations, Proceedings of
Machine Learning Research. PMLR, 2026.

Yuan, L., Chen, W., Zhang, Y., Cui, G., Wang, H., You, Z.,
Ding, N., Liu, Z., Sun, M., and Peng, H. From f(x) and
g(x) to f(g(x)): Llms learn new skills in rl by composing
old ones. In The Fourteenth International Conference
on Learning Representations, Proceedings of Machine
Learning Research. PMLR, 2026.

Yuan, Z., Yuan, H., Li, C., Dong, G., Lu, K., Tan, C., Zhou,
C., and Zhou, J. Scaling relationship on learning math-
ematical reasoning with large language models, 2023.
URL https://arxiv.org/abs/2308.01825.

Yue, Y., Chen, Z., Lu, R., Zhao, A., Wang, Z., Yue, Y., Song,
S., and Huang, G. Does reinforcement learning really
incentivize reasoning capacity in llms beyond the base
model? In Advances in Neural Information Processing
Systems 38 (NeurIPS 2025), 2025.

Zelikman, E., Wu, Y., Mu, J., and Goodman, N. D. Star:
Bootstrapping reasoning with reasoning. In Advances in
Neural Information Processing Systems, 2022.

Zeng, G., Zhou, Z., Arora, D., and Zanette, A. Shrinking the
variance: Shrinkage baselines for reinforcement learning
with verifiable rewards. In Proceedings of the 43rd Inter-
national Conference on Machine Learning, Proceedings
of Machine Learning Research. PMLR, 2025a.

Zeng, W., Huang, Y., Liu, Q., Liu, W., He, K., Ma, Z.,
and He, J. Simplerl-zoo: Investigating and taming zero
reinforcement learning for open base models in the wild.
In Conference on Language Modeling (COLM), 2025b.

Zhang, A., Ballas, N., and Pineau, J. A dissection of over-
fitting and generalization in continuous reinforcement
learning, 2018a. URL https://arxiv.org/abs/
1806.07937.

Zhang, A., McAllister, R., Calandra, R., Gal, Y., and Levine,
S. Learning invariant representations for reinforcement
learning without reconstruction. In International Confer-
ence on Learning Representations, 2021.

Zhang, C., Vinyals, O., Munos, R., and Bengio, S. A study
on overfitting in deep reinforcement learning, 2018b.
URL https://arxiv.org/abs/1804.06893.

Zhang, C., Sheng, G., Liu, S., Li, J., Feng, Z., Liu,
Z., Liu, X., Jia, X., Peng, Y., Lin, H., and Wu,
C.
A framework for training large language mod-
els for code generation via proximal policy optimiza-
tion, 2024. URL https://i.cs.hku.hk/~cwu/
papers/gmsheng-NL2Code24.pdf.
PDF avail-
able online.

Zhang, C., Neubig, G., and Yue, X. On the interplay of
pre-training, mid-training, and RL on reasoning language
models. In Proceedings of the 43rd International Con-
ference on Machine Learning, Proceedings of Machine
Learning Research. PMLR, 2026.

Zhang, L., Wang, S., and Liu, B. Deep learning for senti-
ment analysis : A survey. Wiley Interdisciplinary Reviews:
Data Mining and Knowledge Discovery, 2018c.

22

### Page links

- [Link 1](https://arxiv.org/abs/1804.06893)
- [Link 2](https://arxiv.org/abs/1806.07937)
- [Link 3](https://arxiv.org/abs/2308.01825)
- [Link 4](https://arxiv.org/abs/2409.12122)
- [Link 5](https://arxiv.org/abs/2505.09388)
- [Link 6](https://arxiv.org/abs/2601.08521)
- [Link 7](https://i.cs.hku.hk/~cwu/papers/gmsheng-NL2Code24.pdf)

## Page 23

Maximum Likelihood Reinforcement Learning

Zhang, S., Dong, L., Li, X., Zhang, S., Sun, X., Wang, S.,
Li, J., Hu, R., Zhang, T., Wu, F., and Wang, G. Instruc-
tion tuning for large language models: A survey. ACM
Computing Surveys, 2023.

Zhang, T. Statistical analysis of some multi-category large
margin classification methods. J. Mach. Learn. Res., 5:
1225–1251, December 2004. ISSN 1532-4435.

Zhao, R., Meterez, A., Kakade, S., Pehlevan, C., Jelassi, S.,
and Malach, E. Echo chamber: Rl post-training ampli-
fies behaviors learned in pretraining. In Conference on
Language Modeling (COLM), 2025.

Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C.,
Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J., and
Lin, J. Group sequence policy optimization, 2025. URL
https://arxiv.org/abs/2507.18071.

Ziebart, B. D., Maas, A., Bagnell, J. A., and Dey, A. K.
Maximum entropy inverse reinforcement learning. In
Proceedings of the 23rd National Conference on Artificial
Intelligence - Volume 3, AAAI’08, pp. 1433–1438. AAAI
Press, 2008. ISBN 9781577353683.

23

### Page links

- [Link 1](arxiv-2507-18071.md)

## Page 24

Maximum Likelihood Reinforcement Learning

Appendix

A Public Code Release
26

B
Extended Related Work
26

C Theoretical Results
30

D Analysis of the Practical Gradient Estimator
31

E
More on Unifying Weight-Function View on RL Objectives
33

F
RL Implementation Details for LLM Experiments
35

G Pass@k Calculation
36
G.1
Closed-form Calculation for Differentiable Settings . . . . . . . . . . . . . . . . . . .
36
G.2
Sampling-based Estimator
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36

H ImageNet Experiments
37
H.1 Training Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
H.2 Training Hyperparameters
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
H.3
Equivalence of Validation Top-1 Accuracy and Majority Voting Accuracy . . . . . . .
38
H.4
Gradient Norm Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
H.5
Comparison with GRPO and Additional Metrics . . . . . . . . . . . . . . . . . . . . .
39

I
Maze Experiments
40
I.1
Model Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
I.2
Task Description
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
I.3
Training Setups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
I.4
Training Dynamics in Our Highest Compute Budget Setting
. . . . . . . . . . . . . .
41
I.5
Comparison Table with Additional Baselines
. . . . . . . . . . . . . . . . . . . . . .
42

J
GSM8K Experiments
43
J.1
Prompt template . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
J.2
Hyperparameters
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
J.3
Effect of Additional Compute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
J.4
Comparison with Additional Baselines . . . . . . . . . . . . . . . . . . . . . . . . . .
44
J.5
Per-Prompt Pass-Rate Distribution During Training . . . . . . . . . . . . . . . . . . .
44

K Qwen3 Experiments
46
K.1
Prompt template . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46
K.2
Hyperparameters
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46
K.3 Additional Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46

L
Comparison with Additional Baselines
49

24

## Page 25

Maximum Likelihood Reinforcement Learning

L.1
PKPO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
L.2
ZPD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
L.3
Power Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51

M Additional Analyses
53
M.1 Non-Zero Gradient Signal Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . .
53
M.2 Policy Gradient Variance Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
M.3 On the Distribution Sharpening Narrative
. . . . . . . . . . . . . . . . . . . . . . . .
54
M.4 Non-Binary Reward Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55

25

## Page 26

Maximum Likelihood Reinforcement Learning

A. Public Code Release

We provide sufficient details about our implementation, hyperparameters, environment design, and datasets in the main paper
and the appendix to effectively reproduce the results in this paper. The assets required to reproduce the results in our paper can
be found through our website: https://zanette-labs.github.io/MaxRL/. In particular, the code and scripts
to reproduce the results in this paper has been open-sourced at https://github.com/tajwarfahim/maxrl.

B. Extended Related Work

Cross-entropy objective.
Maximizing log-likelihood via optimizing cross-entropy is a widely used framework in machine
learning due to its simplicity and favorable theoretical properties. In particular, cross-entropy is a strictly proper scoring rule,
meaning that the expected loss is uniquely minimized by the true probability distribution, which encourages statistically
calibrated predictions (Good, 1952; Savage, 1971; Gneiting & Raftery, 2007; Waghmare & Ziegel, 2025). Moreover, it
yields statistically efficient estimators under standard assumptions (van der Vaart, 1998; Casella & Berger, 2002; Lehmann
& Casella, 2006), and induces gradients that concentrate learning signal on low-probability or uncertain outcomes through
logarithmic weighting (Wang et al., 2020). As a result, cross-entropy (or log-loss) often yields consistent estimators for
classification and tends to generalize well in practice (Ng & Jordan, 2001; Zhang, 2004). However, more recent work
has shown that models trained to maximize log-likelihood can still overfit and exhibit miscalibration, motivating post-hoc
techniques such as temperature scaling (Niculescu-Mizil & Caruana, 2005; Guo et al., 2017). Moreover, the unbounded
nature of cross-entropy and its sensitivity to small perturbations in the predicted distribution suggest that alternative strictly
proper scoring rules may be more suitable in certain settings (Kornblith et al., 2021). Because cross-entropy is extensively
studied, we refer interested readers to Mao et al. (2023); Li et al. (2025); Terven et al. (2025) for a comprehensive review.

Supervised training vs reinforcement learning.
Supervised learning has been the go-to training paradigm in machine
learning, beginning with early “learning with a teacher” neural-network-based systems such as the perceptron (Rosenblatt,
1958) and later becoming practical with backpropagation-based neural network training (Rumelhart et al., 1986). It has
been used to tackle a broad range of problems, from financial fraud detection (Afriyie et al., 2023; Editya et al., 2025), to
sentiment analysis (Zhang et al., 2018c) and spam detection (Jain et al., 2022; Jamil et al., 2025). More recently, supervised
training has been used in modern image classification systems (Lecun et al., 1998; Krizhevsky et al., 2012) to achieve
strong performance. In modern foundation models, “pretraining” is typically done by supervised learning via minimizing
cross-entropy over next-token prediction (Radford et al., 2018; 2019) on a large corpus of text, followed by additional
supervised training on high-quality, human-written demonstrations (Ouyang et al., 2022; Zhang et al., 2023) to teach models
how to respond to prompts, often known as instruction-tuning. In sequential decision-making domains, supervised training
appears as behavior cloning from expert demonstration, used in early autonomous driving and robotic systems (Pomerleau,
1988; Bojarski et al., 2016; Codevilla et al., 2018). However, supervised learning in sequential decision-making breaks the
i.i.d. assumption since the learned policy’s actions affect which states it visits during execution, causing compounding errors
over time (Ross & Bagnell, 2010; Belkhale et al., 2023). The classic no-regret reductions line (DAgger) makes this explicit
and addresses drift by iteratively querying the expert on states visited by the learner, turning the sequential problem into an
online supervised learning loop with improved guarantees (Ross et al., 2011).

In such scenarios, reinforcement learning is an attractive alternative paradigm that formalizes learning under delayed, sparse,
and evaluative feedback in Markov decision processes (MDPs), with foundational roots in dynamic programming and MDP
theory (Bellman, 1957). Mechanistically, the key contrast with supervised learning / behavior cloning is that supervised
learning assumes (or benefits strongly from) an i.i.d. dataset of correct targets under a fixed data distribution, whereas RL’s
data distribution is policy-induced and nonstationary, and gradients arise from credit assignment through rewards rather
than direct target labels. This mismatch shows up starkly in sequential prediction/imitation: naive behavior cloning trains
on expert state distributions but at test time visits states induced by its own errors, causing compounding error (a form of
distribution shift / “state drift”). Classical RL algorithms include temporal-difference learning (Sutton, 1988; Sutton et al.,
1998) and value-based control such as Q-learning (Watkins & Dayan, 1992), while policy-gradient methods (Williams,
1992; Sutton et al., 1999) directly optimize expected return via likelihood-ratio gradients (REINFORCE) and later stabilized
large-scale learning through variants like trust-region policy optimization (TRPO) (Schulman et al., 2015) and off-policy
actor–critic methods for continuous control (e.g., DDPG (Lillicrap et al., 2016)) and maximum-entropy actor–critic (e.g.,
SAC (Haarnoja et al., 2018)). Empirically, deep RL’s modern resurgence is often associated with representation learning +
RL on high-dimensional inputs (e.g., DQN (Mnih et al., 2013)).

26

### Page links

- [Link 1](https://github.com/tajwarfahim/maxrl)
- [Link 2](https://zanette-labs.github.io/MaxRL/)

## Page 27

Maximum Likelihood Reinforcement Learning

A large body of work blends supervised and RL to get the best of both: (i) Imitation + online correction methods like
DAgger (Ross et al., 2011) explicitly combine supervised learning with interactive data collection to mitigate distribution
shift ; (ii) Inverse RL / MaxEnt IRL reframes imitation as learning a reward/cost model that explains expert behavior, with
maximum-entropy formulations giving a principled probabilistic objective (Ziebart et al., 2008); (iii) Adversarial imitation
(GAIL) (Ho & Ermon, 2016) avoids explicit reward learning by matching occupancy measures via a GAN-like discriminator,
typically trained with policy optimization; (iv) Learning from demonstrations in deep RL injects supervised losses and/or
demonstration replay into RL to improve exploration and sample efficiency—e.g., DQfD (Hester et al., 2018) combines TD
learning with supervised large-margin imitation terms, and demonstration-augmented continuous-control methods address
sparse-reward exploration failures (Nair et al., 2018); and (v) Trajectory-optimization–guided policy learning (guided policy
search (Levine & Koltun, 2013)) explicitly produces supervised targets for a policy network from trajectory optimization /
local controllers, bridging optimal control, RL, and supervised regression. In modern LLM alignment, the same hybrid
template appears as “Supervised fine-tuning + preference-based RL”: InstructGPT (Ouyang et al., 2022) first performs
supervised fine-tuning on demonstrations and then applies RL from human feedback (RLHF), while more recent approaches
like Direct Preference Optimization (DPO) (Rafailov et al., 2023) recast parts of RLHF into a supervised-style classification
objective — illustrating an active trend of recovering supervised-like training signals even when the underlying goal is
preference/reward optimization. Concurrent work such as (Russo, 2026) has also studied policy improvement through
the lens of success conditioning. Another closely related view for comparing REINFORCE and Maximum Likelihood is
through the KL divergence: where REINFORCE can be seen as a reverse KL and Maximum Likelihood can be seen as
forward KL objective with different properties, as noted by Chan et al. (2022). Thus MAXRL is also conceptually related to
RWR (Peters & Schaal, 2007)/AWR (Peng et al., 2019), which are also forward KL objectives.

Control as inference is also a closely related topic (Millidge et al., 2020; O’Donoghue et al., 2020; Rawlik et al., 2012; Ito &
Kashima, 2024; Tarbouriech et al., 2023), and we point the reader to Levine (2018) for more details. Finally, our approach
is closely related to Monte Carlo Expectation Maximization (MCEM), which approximates intractable expectations in
maximum-likelihood estimation using samples (Dempster et al., 1977; Wei & Tanner, 1990; Levine & Casella, 2001; Ruth,
2024). In the infinite sample regime, MAXRL can be viewed through an EM lens: the observed event is that the answer is
correct, and the latent variable is the successful trajectory that produced it. A sample-until-success implementation of this
maximum-likelihood objective would therefore recover an MCEM-style procedure. The finite-compute version of MAXRL,
however, makes a different design choice: it fixes the number of rollouts and thereby defines a compute-indexed family of
sample-based objectives, interpolating between standard reward maximization and exact maximum likelihood. Thus, rather
than using Monte Carlo samples only to approximate a fixed EM objective, MAXRL uses the sampling budget itself to
define the learning objective optimized by policy-gradient methods.

Training LLMs for strong reasoning abilities.
A few different approaches for post-training have demonstrated success,
including supervised fine-tuning on human-crafted, high-quality demonstrations (Wang et al., 2023b), iterative supervised
training on self-generated, good-quality responses (Anthony et al., 2017; Zelikman et al., 2022; Gulcehre et al., 2023),
reinforcement learning from a learned reward model on human preferences (Ouyang et al., 2022), and more recently
preference-based contrastive learning (Rafailov et al., 2023; Pang et al., 2024). Reinforcement learning from verifiable
rewards (RLVR), where LLMs receive reward from a ground truth verifier instead of using a trained reward model, has
emerged as the dominant paradigm for instilling strong reasoning capabilities into LLMs (OpenAI et al., 2024; Guo et al.,
2025; Team et al., 2025; Lambert et al., 2025a; Yang et al., 2025). Whereas supervised training learns better behavior
from fixed static datasets, reinforcement learning uses policy gradient algorithms (e.g., PPO (Schulman et al., 2017),
GRPO (Shao et al., 2024), RLOO (Ahmadian et al., 2024)) to learn from self-generated responses and non-differentiable
rewards. However, these algorithms and their variants (Zheng et al., 2025; Liu et al., 2025b; MiniMax et al., 2025) optimize
expected reward or pass rate and only differ in how the advantage or off-policy updates are calculated. In contrast, in our
work we focus on recovering the cross-entropy-based classification objective in an RL training pipeline, fundamentally
differing from previous work.

Since the recent advent of RLVR, the RLVR pipeline has been studied extensively (Zeng et al., 2025b; Liu et al., 2025b;
Khatri et al., 2026) and alternative algorithms such as Dr.GRPO (Liu et al., 2025b), DAPO (Yu et al., 2025), GSPO (Zheng
et al., 2025), CISPO (MiniMax et al., 2025), and RAFT (Xiong et al., 2025a) have been proposed. The idea of normalizing
advantages by mean reward, similar to ours, has been explored in Huang et al. (2025), but whereas we normalize advantage
by group mean reward (mean reward over the rollouts associated with a particular prompt), Huang et al. (2025) normalizes
by the batch mean reward (mean reward over all prompts in a batch of policy gradient updates). A limitation of our work is
that we assign no gradient for tasks where the policy fails to generate even one correct rollout: recent work such as Feng

27

## Page 28

Maximum Likelihood Reinforcement Learning

et al. (2025) has studied this problem by employing a maximum-likelihood (MLE) objective in reward modeling to assign
non-zero, confidence-dependent rewards to incorrect generations. Similarly to us, earlier work has studied how to learn
effectively via RL from a collection of tasks as opposed to a single task, where each task may have different difficulties, and
thus reward distribution. PopArt (Hessel et al., 2019) is one such example, which uses a normalization by standard deviation
for the rewards of each task (as opposed to normalization by mean reward in MAXRL), and we consider this as an earlier
example of normalization by standard deviation before GRPO (Shao et al., 2024). Finally, recent work such as Zhang et al.
(2026) has also studied how RL training is influenced by pretraining and midtraining in toy didactic settings, establishing
the importance of good pretraining/midtraining for the success of RL, similar to Gandhi et al. (2025).

RL training causes distribution sharpening.
Despite its usefulness, questions remain on whether RLVR teaches LLMs
fundamentally new behavior/skills, or simply sharpens existing good behavior from the pretrained model. Previous
research (Liu et al., 2025b; Zhao et al., 2025; AI et al., 2025) demonstrated that certain reasoning skills like reflection
already exist in the pretrained model, and Gandhi et al. (2025) shows that good reasoning behaviors learned from pretraining
are crucial for the success of RLVR in the post-training phase. More recently, studies (Yue et al., 2025; Dang et al., 2025;
Wu et al., 2026) found that RLVR decreases the model’s diversity by reducing pass@k. In our paper, we confirm these
findings and attribute this to the RL objective itself as optimizing expected reward tends to marginalize learning signal from
harder prompts, which results in distribution sharpening.

On exploration for reinforcement learning for LLMs.
Exploration, or taking actions to discover new information, is a
widely studied topic in reinforcement learning. A closely related topic is curiosity, where an agent seeks new information
about its environment via interactions. Intrinsic motivation is a popular notion for curiosity, where the agent is driven
by an exploration bonus that is not necessarily related to the task to be achieved (Schmidhuber, 1991; 2007). Follow-up
research has built on this notion to mitigate problems of sparse reward (reward is observed at a very belated phase of
interactions) or no reward at all (Pathak et al., 2017; 2019; Eysenbach et al., 2018; Burda et al., 2018; Sharma et al., 2019;
Yang et al., 2024c; Houthooft et al., 2016). Count-based bonuses have also been introduced as a way of computing intrinsic
motivation (Bellemare et al., 2016). Prompt-level reweighting of gradients has also been studied (Yu et al., 2026), though
under a different context (self-training) and a different weighting mechanism. Finally, adding noise to network parameters
or optimization has been another line of work to improve exploration during RL training (Fortunato et al., 2018; Ishfaq et al.,
2024b;a; 2025). Maximum entropy RL, the principle where one attempts to recover an agent that achieves high reward but
is as stochastic as possible, can be seen as another attempt at solving exploration for classical RL (Haarnoja et al., 2018;
Boucher et al., 2025; Eysenbach & Levine, 2022; Dong et al., 2025). In summary, exploration-exploitation tradeoff (Sutton,
1988; Auer et al., 2002; Thompson, 1933) has been a crucial topic for ensuring RL agents’ success.

More recently, exploration has emerged as an important topic for building modern LLM-based systems. There are two types
of exploration to consider. The first is inference-time exploration, where an agent has to efficiently gather information during
deployment by strategically choosing its interactions with its environment, Tajwar et al. (2025) is an important work in this
line of research. More importantly, pass@k degradation (mode collapse) during RLVR (Yue et al., 2025; Wu et al., 2026;
GX-Chen et al., 2026) has prompted research into train-time exploration, where the challenge is to go beyond the pretrained
model’s capabilities (Ni et al., 2025) and discover new knowledge. Primary approaches include directly optimizing for
pass@k (Mahdavi et al., 2025; Walder & Karkhanis, 2025; Tang et al., 2025; Chen et al., 2025b), curriculum learning (Tajwar
et al., 2025; Chen et al., 2025a; Setlur et al., 2026; Motwani et al., 2026), learning from additional hints or abstractions (Qu
et al., 2026; Chen et al., 2026a; Liu et al., 2026), increasing number of rollouts to prevent RL gains from saturating (Hu
et al., 2026), employing data curation algorithm to redirect effort to problems with low success rate (Nguyen et al., 2025b),
leveraging expert guidance (Chang et al., 2024; Qu et al., 2025), or differential smoothing by penalizing entropy on low
reward trajectories and encouraging entropy on high reward trajectories. Entropy-based bonuses to encourage exploration
during RL training (Hao et al., 2025; Chen et al., 2026b; Cheng et al., 2026; Wang et al., 2025; Petrenko et al., 2026; Ged &
Veiga, 2024) is another popular line of work for improving exploration. A few modern approaches for exploration bonus
utilized for LLM training are proposed by Song et al. (2025); Tuyls et al. (2026). The idea of curiosity-driven exploration
from classical RL discussed above has also been adopted for LLMs (Dai et al., 2026). Although some literature has reported
pass@k degradation during RL training, others have found the opposite results. For example, ProRL (Liu et al., 2025a)
has shown that RL training on a mixture of reasoning puzzles (Stojanovski et al., 2025) can improve pass@k on a heldout
reasoning task. Similarly, Yuan et al. (2026) has shown that LLMs can learn new skills via RL by composing old ones,
showing the promise of going beyond pretraining knowledge, and Cheng et al. (2025) also found pass@k to improve,
particularly on tasks less likely to appear during the pretraining stage. Recent work also formalized Set-RL (Hamid et al.,

28

## Page 29

Maximum Likelihood Reinforcement Learning

2026; Orney et al., 2026) and Risk-Sensitive Reinforcement Learning (RS-GRPO) (Jiang et al., 2026) to improve diversity
during LLM reasoning training and better navigate the exploration-exploitation tradeoff in LLM RL training, with the latter
being a closely related prior work for our own work. A parallel effort has gone into difficulty-aware adaptive sampling,
with Xiong et al. (2025b); Nguyen et al. (2025b); Yang et al. (2026b) being notable examples. Ray interference (Schaul
et al., 2019) has been proposed as an explanation for the observed pass@k degradation. Overall, this line of research remains
important as focus moves to LLMs discovering new information during RL training and it is therefore an ongoing field of
research.

Generalization in reinforcement learning.
Research on generalization in reinforcement learning asks a core question:
does an agent learn principles that transfer beyond the exact environments it trained in, or does it just memorize experi-
ence (Zhang et al., 2018b;a; Schaul et al., 2019; Bengio et al., 2020)? Empirical work shows deep RL agents often overfit to
training seeds, visuals, or dynamics, performing poorly on new levels, layouts, or slightly shifted physics. To study this,
researchers built procedural benchmarks (like CoinRun/Procgen (Cobbe et al., 2020)) and multi-task suites (e.g., robotics
task collections (Yu et al., 2019; Atamuradov, 2025) or LLM sequential decision-making task suites (Tajwar et al., 2025))
that separate train and test environments. A major line of work improves generalization through regularization (Kostrikov
et al., 2021) and invariances (Zhang et al., 2021) — especially data augmentation (Laskin et al., 2020; Raileanu et al., 2021),
mixup-style methods (WANG et al., 2020), and representation learning tricks (Higgins et al., 2017; Srinivas et al., 2020;
Wang et al., 2021) that make policies rely less on superficial visual details. Another branch focuses on task and domain shift,
using meta-RL (Duan et al., 2016; Finn et al., 2017; Liang et al., 2024), multi-task learning (Brunskill & Li, 2013), domain
randomization, and distributionally robust RL (Clavier et al., 2022; Lu et al., 2024; Shi et al., 2023) to handle new tasks or
uncertain dynamics. Recent lines of work have also directly studied exploration as a means to achieve generalization in
RL (Jiang et al., 2023), and have shown that simple architectural changes and scale can often improve generalization in
the ProcGen benchmark (Jesson & Jiang, 2024). On the theory side, classical PAC-MDP (Strehl et al., 2009) and robust
MDP frameworks (Nilim & Ghaoui, 2004; Iyengar, 2005) formalize when policies learned from limited samples can be
expected to work in new situations. In the LLM settings, analogous questions appear in RLHF (Ouyang et al., 2022), where
reinforcement learning is used to align models with human preferences, and researchers now study how this training affects
generalization to unseen prompts, behaviors, and user distributions (Kirk et al., 2024; Lin et al., 2024; Lambert et al., 2025b;
Jia, 2024; Li et al., 2026). Overall, the field has moved from “can RL learn?” to “what exactly does it learn, and when does
that knowledge transfer?”

29

## Page 30

Maximum Likelihood Reinforcement Learning

C. Theoretical Results

Here we present the proofs of theorems mentioned in the main paper. First we restate and prove Theorem 4.1.

Theorem C.1 (Restatement of Theorem 4.1). The gradient of the maximum likelihood objective admits the following
conditional expectation representation:

∇θJML(x) = E\[∇θ log mθ(z | x) | f(z) = y∗(x)\] .

Proof. Recall the standard REINFORCE identity for the gradient of the pass rate:

∇θppass
θ
(x) = ∇θEz∼mθ(·|x)\[I{f(z) = y∗(x)}\] = Ez∼mθ(·|x)\[I{f(z) = y∗(x)}∇θ log mθ(z | x)\].

The gradient of the maximum likelihood objective is:

∇θJML(x) = ∇θ log ppass
θ
(x) = ∇θppass
θ
(x)
ppass
θ
(x)
= Ez∼mθ(·|x)\[I{f(z) = y∗(x)}∇θ log mθ(z | x)\]

Ez∼mθ(·|x)\[I{f(z) = y∗(x)}\]
.

By the definition of conditional expectation for an event A with P(A) > 0:

E\[X | A\] = E\[X · IA\]

P(A)
.

Letting X = ∇θ log mθ(z | x) and A = {z : f(z) = y∗(x)}, and noting that ppass
θ
(x) = P(A), we obtain:

∇θJML(x) = E\[∇θ log mθ(z | x) | f(z) = y∗(x)\] .

Next, we restate and prove Theorem 4.2.

Theorem C.2 (Restatement of Theorem 4.2). The estimator bgN(x) is an unbiased estimator for the MAXRL gradient of
order T = N, i.e.,
E\[bgN(x)\] = ∇θJ(N)
MAXRL(x).

Proof. Conditioned on K ≥1, the successful samples are i.i.d. draws from the success-conditioned distribution, so by
Theorem 4.1:

E\[bgN(x) | K ≥1\] = ∇θ log ppass
θ
(x).

Since bgN(x) = 0 when K = 0:

E\[bgN(x)\] = ∇θ log ppass
θ
(x) · P(K ≥1) = ∇θ log ppass
θ
(x) · pass@N(x).

Writing p = ppass
θ
(x) and using pass@k(x) = 1 −(1 −p)k:

∇θp

p
· (1 −(1 −p)N) = ∇θp

N
X

k=1
(1 −p)k−1 =

N
X

k=1

1
k ∇θpass@k(x) = ∇θJ(N)
MAXRL(x),

where the second equality uses ∇θpass@k(x) = k(1 −p)k−1∇θp.

30

## Page 31

Maximum Likelihood Reinforcement Learning

D. Analysis of the Practical Gradient Estimator from Algorithm 1

In this section, we will analyse the practical gradient estimator from Algorithm 1, which includes both an unconditional
average score baseline to reduce variance, and sets the gradient to be 0 in the case of all negative rollouts (no baseline is
used). We show that this changes the objective for which the gradient is unbiased for: while the gradient from Equation (9)
is unbiased for the MAXRL gradient of order T = N (Theorem 4.2), the practical gradient estimator is instead unbiased for
the MAXRL gradient of order T = N −1. We formally prove this result below.

Theorem D.1 (Effective truncation of the dropped-baseline estimator). Fix an input x and let z1, . . . , zN ∼mθ(· | x) be N
i.i.d. rollouts from the latent policy. Define

ri = I{f(zi) = y∗(x)},
K =

N
X

i=1
ri,
Si = ∇θ log mθ(zi | x).

Let
ppass
θ
(x) = Pz∼mθ(·|x)(f(z) = y∗(x)),

and assume the standard score-function identities

E\[Si\] = 0,
E\[riSi\] = ∇θppass
θ
(x).

Consider the practical gradient estimator from Algorithm 1

egN(x) = I{K > 0}

1
K

N
X

i=1
riSi −1

N

N
X

i=1
Si

!

.

Then

E\[egN(x)\] =

N−1
X

t=1
(1 −ppass
θ
(x))t−1∇θppass
θ
(x).

Equivalently, the practical dropped-baseline estimator is unbiased for the (N −1)-truncated MAXRL gradient.

Proof. For readability, write p = ppass
θ
(x) and ∇p = ∇θppass
θ
(x). Decompose the estimator as

egN(x) = I{K > 0} 1

K

N
X

i=1
riSi

|
{z
}
egsucc
N
(x)

−I{K > 0} 1

N

N
X

i=1
Si

|
{z
}
egbase
N
(x)

.

By the standard MAXRL estimator identity from Theorem 4.2, the successful-rollout term satisfies

E\[egsucc
N
(x)\] =

N
X

t=1
(1 −p)t−1∇p.

It remains to compute the expectation of the dropped baseline term. Since

E

"
1
N

N
X

i=1
Si

#

= 0,

we have

E

"

I{K > 0} 1

N

N
X

i=1
Si

#

= −E

"

I{K = 0} 1

N

N
X

i=1
Si

#

.

Now observe that

I{K = 0} =

N
Y

ℓ=1
(1 −rℓ).

31

## Page 32

Maximum Likelihood Reinforcement Learning

Using independence of the samples,

E

"

I{K = 0} 1

N

N
X

i=1
Si

#

= 1

N

N
X

i=1
E\[(1 −ri)Si\]
Y

ℓ̸=i
E\[1 −rℓ\]

= 1

N

N
X

i=1
(E\[Si\] −E\[riSi\]) (1 −p)N−1

= −(1 −p)N−1∇p.

Therefore,
E

egbase
N
(x)

= (1 −p)N−1∇p.

Combining the two terms gives

E\[egN(x)\] =

" N
X

t=1
(1 −p)t−1∇p

#

−(1 −p)N−1∇p

=

N−1
X

t=1
(1 −p)t−1∇p.

Substituting back p = ppass
θ
(x) yields

E\[egN(x)\] =

N−1
X

t=1
(1 −ppass
θ
(x))t−1∇θppass
θ
(x),

which is exactly the (N −1)-truncated MAXRL gradient, concluding our proof.

32

## Page 33

Maximum Likelihood Reinforcement Learning

E. More on Unifying Weight-Function View on RL Objectives

Here we provide full derivations following Section 5. Recall that we want to express population-level gradients of different
objectives in the following form:
∇θJ = Ex∼ρ \[w(pθ(x))∇θpθ(x)\]

where pθ(x) = ppass
θ
(x) and w(pθ(x)) is the weighting function. In this section, we show that all objectives of our
consideration can be written in this form. Furthermore, we will derive the weighting function w(pθ(x)) for each of them.

Classical RL (REINFORCE).
For classical reinforcement learning, i.e., the REINFORCE objective, we have:

JRL = Ex∼ρ\[Ez∼mθ(·|x)\[r(x, z)\]\]

= Ex∼ρ\[Ez∼mθ(·|x)\[I {f(z) = y∗(x)}\]\]

= Ex∼ρ\[ppass
θ
(x)\]

Therefore, its gradient is:

∇θJRL = Ex∼ρ\[∇θppass
θ
(x)\]

giving the corresponding wRL to be 1.

GRPO.
Our analysis is similar to that of Davis & Recht (2025). The gradient of the population level GRPO objective
gradient can be written as:

∇θJGRPO = Ex∼ρ

"

Ez∼mθ(·|x)

" 
r(x, z) −Ez∼mθ(·|x)\[r(x, z)\]
p

Varz∼mθ(·|x)\[r(x, z)\]

!

∇θ log mθ(z|x)

##

Since we consider a binary reward setting, we have Ez∼mθ(·|x)\[r(x, z)\] = ppass
θ
(x). Similarly, considering the variance of a
Bernoulli random variable, we get:

Varz∼mθ(·|x)\[r(x, z)\] = ppass
θ
(x) (1 −ppass
θ
(x))

Therefore, the objective becomes:

∇θJGRPO = Ex∼ρ

"
1
p

ppass
θ
(x) (1 −ppass
θ
(x))
∇θppass
θ
(x)

#

which thereby gives us the weighting function to be 1/
p

pθ(x)(1 −pθ(x)), as desired.

Maximum Likelihood (ML).
The maximum likelihood objective is given by

JML = Ex∼ρ\[log ppass
θ
(x)\].

Taking its gradient with respect to θ and applying the chain rule, we obtain

∇θJML = Ex∼ρ \[∇θ log ppass
θ
(x)\]

= Ex∼ρ


1
ppass
θ
(x)∇θppass
θ
(x)


This shows that the weighting function for the maximum likelihood objective is 1/ppass
θ
(x), as we claimed in Table 2.

MAXRL.
Finally, we consider the objective J(T )
MAXRL.
Proposition E.1. For MAXRL with order T, we can rewrite it as

∇θJ(T )
MAXRL = Ex∼ρ\[w(pθ(x)) ∇θpθ(x)\] ,

where

wT (p) =

T
X

k=1
(1 −p)k−1 = 1 −(1 −p)T

p
.

33

## Page 34

Maximum Likelihood Reinforcement Learning

Proof. From Equation (7), we have:

∇θJ(T )
MAXRL(x) =

T
X

k=1

1
k ∇θpass@k(x).

Using pass@k(x) = 1 −(1 −p)k where p = ppass
θ
(x):

∇θpass@k(x) = k(1 −p)k−1∇θp.

Substituting:

∇θJ(T )
MAXRL(x) =

T
X

k=1

1
k · k(1 −p)k−1∇θp =

T
X

k=1
(1 −p)k−1
!

∇θp = wT (p)∇θppass
θ
(x).

Taking the expectation over x ∼ρ completes the proof.

34

## Page 35

Maximum Likelihood Reinforcement Learning

F. RL Implementation Details for LLM Experiments

Our discussion here follows that of Shafayat et al. (2025). For continuity with existing literature, we use slightly different
notations from the rest of the paper for this section. Let x represent a prompt, and let y ∼π(·|x) represent sequence of
tokens autoregressively sampled from the language model π conditioned on the prompt x. Let πθ be the current policy,
and πθold be an older policy (from earlier iterations in training) used for data generation. In our implementation (based on
verl (Zhang et al., 2024; Sheng et al., 2024)), we use the following general RL objective:

J (θ) = Ex∼D, {yi}G
i=1∼πθold(·|x)

"
1
T

G
X

i=1

|yi|
X

t=1
min

wi,t(θ) ˆAi,t, clip(wi,t(θ), 1 −ε, 1 + ε) ˆAi,t
#

where T is the total number of tokens in the mini-batch (excluding tokens in the prompt etc., since we only compute loss
on the model generated tokens), πθ represents the current LLM’s autoregressive probability distribution, πθold denotes the
behavior policy/data generation policy’s probability distribution, wi,t(θ) is the importance ratio, defined as:

wi,t(θ) = πθ(yi,t | x, yi,<t)

πθold(yi,t | x, yi,<t)

Since we operate fully on-policy, i.e., one RL step per one batch of generated rollouts, this is always one in our experiments,
and the clipping parameter ϵ has no effect on our training. ˆAi,t represents the advantage for the t-th token in the sequence yi.
The same advantage defined at a sequence level is applied to each token in the sequence, so henceforth we will drop the t
from the notation as well.

The main difference between GRPO (Shao et al., 2024), RLOO (Ahmadian et al., 2024) and MAXRL comes from their use
of different advantage functions. RLOO objective uses the following advantage function:

1
G

G
X

i=1
\[R(y(i), x) −
1
G −1

X

j̸=i
R(y(j), x)\]

whereas GRPO uses the following advantage function:

ˆAi = r(x, yi) −mean
 
{r(x, yi)}G
i=1


std
 
{r(x, yi)}G
i=1

+ ϵ

where ϵ is a small number (1 × 10−6) added to avoid division by zero. Finally, the advantage for MAXRL is as follows:

ˆAi = r(x, yi) −mean
 
{r(x, yi)}G
i=1


mean
 
{r(x, yi)}G
i=1

+ ϵ

Here G is the number of online samples generated. RLOO, GRPO and MAXRL create a dynamic baseline for each sample
without needing a separate value function (unlike PPO (Schulman et al., 2017)), effectively estimating the expected return
on-the-fly during training. Not having a value network makes the training much simpler for all three algorithms.

35

## Page 36

Maximum Likelihood Reinforcement Learning

G. Pass@k Calculation

G.1. Closed-form Calculation for Differentiable Settings

To calculate pass@k from a generative model, one usually samples T ≥k rollouts from the model, calculate success or
failure from each of them, and then uses an appropriate statistical estimator for pass@k (Chen et al., 2021; Yue et al., 2025).
However, since there is no latent reasoning process involved in our didactic ImageNet experiments and since we can directly
calculate the model likelihood of label y ∈Y for an input image x ∈X, namely πθ(y|x), we can also analytically compute
pass@k without sampling as well. Formally, in all ImageNet experiments, we calculate pass@k for an example (image,
label) pair (x, y∗(x)) as follows:

Pass@k(x, y∗(x); πθ) = 1 −(1 −πθ(y∗(x)|x))k

The average pass@k is then obtained by averaging the above quantity over all example pairs in the validation dataset.

G.2. Sampling-based Estimator

Unlike the ImageNet setting, we can’t usually directly calculate pass@k via accessing the true probability of the correct
action. Therefore, we use the default pass@k calculation mechanism in verl (Sheng et al., 2024; Zhang et al., 2024),
using the bootstrapping low variance unbiased estimator introduced by Chen et al. (2021). This employs generating n ≥k
samples per task, counting the number of correct samples c(x) among the n samples, and estimate pass@k as:

Pass@k = Ex∼ρ

"

1 −

 n−c(x)
k

 n
k


#

36

## Page 37

Maximum Likelihood Reinforcement Learning

H. ImageNet Experiments

H.1. Training Procedure

Let X be the input space and Y be the label space. Let πθ denote our model: given an input image x ∈X, πθ(y|x) is
the model’s predicted probability of image x belonging to class y ∈Y. For an input image and label pair (x, y∗(x)), the
cross-entropy loss is:

LCE(x, y∗(x); πθ) = −log πθ(y∗(x)|x)

On the other hand, the corresponding RL objective for the same pair is:

LRL(x, y∗; πθ) = −Ey∼πθ(·|x)\[−log πθ(y|x) · ˆA(y|x)\]

where the expectation is computed using Monte-Carlo sampling with K rollouts of y from πθ(·|x). GRPO, REINFORCE
and MAXRL vary only in the calculation of the advantage A(y|x). Concretely, let y(1), . . . , y(K) be our K rollouts, sampled
from the conditional probability distribution πθ(·|x). We operate under a binary reward setting, meaning the reward function
r(x, y) is:

r(x, y) = I\[y = y∗(x)\] =

(
1,
if y = y∗(x)
0,
otherwise

Given this reward, we calculate advantage under GRPO, REINFORCE and MAXRL as follows:

ˆAGRPO(x, y) = r(x, y) −ˆµ

ˆσ

ˆAREINFORCE(x, y) = r(x, y) −ˆµ

ˆAMAXRL(x, y) = r(x, y) −ˆµ

ˆµ

where ˆµ =

PK
i=1 r(x,y(i))

K
, ˆσ =
q PK
i=1(r(x,y(i))−ˆµ)2

K
are the mean and standard deviation of rewards of the sampled rollouts.

Finally, at each training step, a batch of (input image, label) pairs is collected from the training dataset. The above
computation gives us per (input image, label) loss, we average them over all the pairs in a given batch to calculate the final
loss which is then used to update the model via gradient descent.

H.2. Training Hyperparameters

We train ResNet-50 (He et al., 2016) models on ImageNet (Deng et al., 2009) with a batch size of 256 for 20 epochs using
SGD with momentum 0.9 (no Nesterov momentum) and an initial learning rate of 0.1. We swept the learning rate over
{0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 0.7, 1.0} and found that the standard value of 0.1 generally works well for all objectives,
so we report results at this setting. The learning rate follows a cosine schedule (Loshchilov & Hutter, 2017) with linear
warmup for the first epoch. For evaluation, no augmentation is applied: each image is resized to 224 × 224 and normalized
by the channel-wise mean and standard deviation of pixel values. During training, in addition to the same resizing and
normalization, we apply a random horizontal flip (with probability 0.5) and a random resized crop to 224 × 224 (with scale
(0.08, 1.0)). The number of rollouts K is varied across experiments. All training runs are conducted on a single L40S GPU
for 15 hours.

37

## Page 38

Maximum Likelihood Reinforcement Learning

H.3. Equivalence of Validation Top-1 Accuracy and Majority Voting Accuracy

In this section, we discuss the validation top-1 accuracy metric, which is the traditional metric used in image classification.
Formally, validation accuracy for a single image and label pair (x, y∗(x)) is defined as:

Accuracy(x, y∗(x); πθ) = I

arg max
y∈Y πθ(y|x) = y∗(x)

=

(
1,
if arg maxy∈Y πθ(y|x) = y∗(x)
0,
otherwise

which is then averaged over all validation examples for the final metric. In other words, validation accuracy is the same as
majority voting accuracy (Wang et al., 2023a) in traditional LLM chain-of-thought reasoning tasks.

H.4. Gradient Norm Analysis

0.0
0.2
0.4
0.6
0.8
1.0
Pass Rate

0

100

200

300

Gradient L2 Norm

Cross Entropy

0.0
0.2
0.4
0.6
0.8
1.0
Pass Rate

0

100

200

300
MaxRL

0.0
0.2
0.4
0.6
0.8
1.0
Pass Rate

0

100

200

300
GRPO

0.000
0.001
0.002
0.003
Pass Rate

0.0

0.5

1.0

REINFORCE

Figure 8. (ImageNet gradient norm analysis) Scatter plot, where each point has the pass rate (model’s predicted probability of the
correct class) of a particular image in the x-axis, and gradient L2 norm for that image in the y-axis, for 1000 randomly selected images
from the ImageNet validation dataset after 1500 steps of training on a ResNet-50 model. Sampling-based algorithms’ (MAXRL, GRPO
and REINFORCE) gradients are calculated using 131,072 rollouts per example to reduce sampling error and estimate the population-level
gradient. Cross-entropy and MAXRL have similar scatter plot: with high gradient norm for hard inputs (pass rate close to 0) and lower
gradient norm for the easier ones (pass rate close to 1). In contrast, the highest gradient norm for GRPO is on medium-difficulty (pass rate
close to 0.5) inputs, with hard inputs having very low gradient norm. Finally, REINFORCE fails to produce any significant gradient norm
and its pass rate is confined below 0.003 after 1500 steps, demonstrating its difficulty to learn in this setting.

Figure 8 shows the correlation between gradient norm and pass rate (model’s predicted probability of the correct class)
for a particular image on different objectives. We see that cross-entropy and MAXRL have a similar scatter plot: with
high gradient norm for hard inputs (pass rate close to 0) and lower gradient norm for the easier ones (pass rate close to
1). In contrast, the highest gradient norm for GRPO is on medium-difficulty (pass rate close to 0.5) inputs, with hard
inputs having very low gradient norm. Finally, REINFORCE fails to produce any significant gradient norm compared to

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

20

40

60

Validation Pass@1 (
)

Pass@1 (
)

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

25

50

75

100

Validation Pass@128 (
)

Pass@128 (
)

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

25

50

75

Majority Voting (
)

Majority Voting (
)

1
4
16
64
256
k

0

20

40

60

80

100

Coverage (Pass@k) (
)

Pass@k vs k (
)

MaxRL (Rollout = 128)
GRPO (Rollout = 128)

MaxRL (Rollout = 1024)
GRPO (Rollout = 1024)

Cross Entropy
REINFORCE (Rollout = 1024)

Figure 9. (Additional ImageNet results) On the didactic image classification setting, MAXRL outperforms and scales better than GRPO
with additional compute, and approaches the same performance as maximum likelihood training via cross-entropy given sufficient number
of rollouts (≥1024). Note that REINFORCE remains flat, since the initial model’s pass rate is low (∼0.1%) and REINFORCE fails to
generate significant gradient signal (Figure 8). From left, the plots show pass@1, pass@128, Majority Voting Accuracy (equivalent to
traditional validation top-1 accuracy in image classification, see Appendix H.3), and coverage of the final checkpoint, respectively.

the other objectives and its pass rate is confined below 0.003 after 1500 steps, demonstrating its difficulty to learn in this
setting. This is also reflected in our other results, where REINFORCE does not show any signs of learning. We attribute
this to the very low gradient norm: since the randomly initialized model has pass rate 0.001 in expectation over all inputs,

38

## Page 39

Maximum Likelihood Reinforcement Learning

REINFORCE fails to produce sufficiently large gradients during training and therefore stalls in model improvement. One
caveat: REINFORCE’s failure may be due to us training the model from scratch — on a pretrained model, it indeed produces
gradients but still shows poor gradient norm on hard inputs (see Figure 6).

H.5. Comparison with GRPO and Additional Metrics

Here we present additional experimental results. In particular, (1) we compare against GRPO with varying number of
rollouts, (2) record additional metrics such as majority voting accuracy (i.e., validation top-1 accuracy), and (3) show
the resulting coverage (pass@k vs k) from different objectives. Figure 9 records our findings: MAXRL outperforms and
scales better than GRPO with additional compute. While GRPO improves performance if given more compute unlike
REINFORCE, it remains suboptimal compared to MAXRL and supervised cross-entropy training. Moreover, both GRPO
and REINFORCE exhibit worse coverage as their pass@k values are significantly lower compared to MAXRL, corroborating
our experiments from other sections.

39

## Page 40

Maximum Likelihood Reinforcement Learning

I. Maze Experiments

I.1. Model Architecture

We adopt a lightweight decoder-only Transformer model following the Qwen2 architecture (Yang et al., 2024a), with a
total of approximately 3M parameters. The model consists of 4 Transformer layers, each using full self-attention. The
hidden size is set to 256, with an intermediate (feed-forward) dimension of 1024, and 4 attention heads per layer. We use
grouped query attention with 2 key-value heads. The model employs RMSNorm with σ = 1 × 10−6 and uses the SiLU
activation function in the feed-forward networks. Rotary positional embeddings (RoPE) (Su et al., 2024) are applied with
θ = 1, 000, 000, and the maximum sequence length is 512 tokens. The vocabulary size is 32 tokens, and input and output
embeddings are tied. The model is trained and evaluated using bfloat16 precision, with attention dropout set to 0. The
architecture follows a standard causal language modeling setup with autoregressive decoding.

I.2. Task Description

Mazes are procedurally generated using Prim’s algorithm (Prim, 1957), and task difficulty is controlled by the grid size. We
use a symbolic tokenization to represent both the maze layout and the navigation policy, with tokens drawn from a small,
discrete vocabulary.

The input sequence describes a two-dimensional grid in row-major order. Each cell is represented by a single token indicating
its type (e.g., WALL, PATH, START, or GOAL). Rows are separated by a dedicated NEWLINE token, and the entire
grid is delimited by special boundary tokens marking the beginning (GRID_START) and end (GRID_END) of the grid
description. Following the maze specification, the model autoregressively generates a sequence of navigation actions drawn
from a fixed action vocabulary (e.g., directional moves) and terminates by a DONE token.

Below, we provide an example data instance following this format.

7*7 Maze Example Model Input and Output Format

Input:
<bos> GRID_START WALL WALL WALL WALL WALL WALL WALL NEWLINE WALL START WALL PATH PATH
PATH WALL NEWLINE WALL PATH WALL PATH WALL WALL WALL NEWLINE WALL PATH PATH PATH PATH
PATH WALL NEWLINE WALL PATH WALL WALL WALL PATH WALL NEWLINE WALL PATH WALL PATH PATH
GOAL WALL NEWLINE WALL WALL WALL WALL WALL WALL WALL NEWLINE GRID_END PATH_START
Output:
RIGHT RIGHT RIGHT RIGHT DOWN DOWN DOWN DOWN DONE <eos>

For reference, we also visualize one typical successful trajectory and one representative failed prediction in Figure 10.

Figure 10. (Maze data visualization) The left plot shows a successful navigation trajectory, while the right plot illustrates a failure case
produced by the trained model, where the generated action sequence deviates from the correct path before reaching the goal.

40

## Page 41

Maximum Likelihood Reinforcement Learning

I.3. Training Setups

To ensure sufficient task complexity and rigorous evaluation, we construct a training set of 1 million distinct 17 × 17
mazes and a test set of 256 non-overlapping samples. We first pretrain the model from scratch, where it is trained to
follow a provided ground-truth trajectory for each maze. During SFT, we use a learning rate of 5 × 10−4 with the AdamW
optimizer (Kingma & Ba, 2015; Loshchilov & Hutter, 2019) and train for 1,500 steps with a batch size of 32. This pretraining
stage3 initializes the model with the basic output format required for representing maze-solving trajectories.

Subsequently, we perform reinforcement learning (RL) training, where we use a learning rate of 1 × 10−4 in all our
experiments. We update the model parameters only once per RL step (i.e., the fully on-policy setting from Tajwar et al.
(2024)). We have two different training settings:

1. 256 Batch size, 9000 RL steps, varying number of training rollouts. This is used for Figures 3 and 11. Figure 3

compares performance across different number of training rollouts (from 4 to 128). We observed that when number of
training rollouts is sufficiently small (e.g., 4), lower batch size training runs can collapse, possibly due to noise/gradient
variance. Hence these runs use a larger batch size of 256. Since this setting is very expensive, we only train our models
for 9000 RL steps, and only train with MAXRL and our principal baselines, namely GRPO and RLOO. Figure 11
shows the evolution of various Pass@k metrics under these 3 objectives during training, and reports experiments
resulting from our highest compute setting, namely that with 128 training rollouts per prompt.

2. 32 Batch size, 20000 RL steps, 128 training rollouts per task. This setting is used for Figure 12, where we show
the training curves for different baselines on the maze setting, and Table 3, where we present summary Pass@k
performance of different baselines at the end of 20000 training steps. Our first setting of 256 batch size was beyond our
compute budget for being too expensive to train all the different baselines with, so we adopted this cheaper setting for
baseline comparison.

Each training run uses 4 RTX 4090 GPUs. Given the small number of model parameters, the model is no longer memory-
bound, so we modified the rollout engine (instead of using the default vLLM (Kwon et al., 2023) engine) in the verl (Zhang
et al., 2024; Sheng et al., 2024) codebase to increase sampling parallelism and speed up training.

I.4. Training Dynamics in Our Highest Compute Budget Setting

0
3000
6000
9000
Training Steps

0.0

0.2

0.4

0.6

0.8

Pass@1 (
)

Pass@1 (
)

0
3000
6000
9000
Training Steps

0.2

0.4

0.6

0.8

1.0

Pass@32 (
)

Pass@32 (
)

0
3000
6000
9000
Training Steps

0.2

0.4

0.6

0.8

1.0

Pass@128 (
)

Pass@128 (
)

0
3000
6000
9000
Training Steps

0.2

0.4

0.6

0.8

1.0

Pass@256 (
)

Pass@256 (
)

GRPO
RLOO
MaxRL
Base

Figure 11. (Training dynamics in the maze setting under our highest compute budget) We investigate how the Pass@k performance of
different objectives evolve when we train a 3M model to solve 17x17 maze puzzles on our highest compute budget, namely 256 batch size
and 128 training rollouts per task. MAXRL performs significantly better compared with GRPO and REINFORCE in pass@1, pass@32,
pass@128 and pass@256. These results signify MAXRL’s effectiveness in compute scaling during RL.

Here we provide additional results pertaining to the training dynamics of MAXRL in the infinite data maze setting. Figure 11
shows pass@1 through pass@256 over training steps for MAXRL, GRPO, and RLOO, trained for 9000 RL steps using 256
batch size and 128 training rollouts per task. MAXRL outperforms both GRPO and RLOO at all metrics.

3Our pretrained Maze transformer checkpoint, which is used as the starting model for RL fine-tuning, can be found here: https:
//github.com/tajwarfahim/maxrl/tree/main/maze/ckpt-1500.

41

### Page links

- [Link 1](https://github.com/tajwarfahim/maxrl/tree/main/maze/ckpt-1500)

## Page 42

Maximum Likelihood Reinforcement Learning

I.5. Comparison Table with Additional Baselines

0
4k
8k
12k
16k
20k
Steps

0.0

0.2

0.4

0.6

0.8

Pass@1 (
)

Pass@1 (
)

0
4k
8k
12k
16k
20k
Steps

0.2

0.4

0.6

0.8

Pass@16 (
)

Pass@16 (
)

0
4k
8k
12k
16k
20k
Steps

0.2

0.4

0.6

0.8

Pass@128 (
)

Pass@128 (
)

0
4k
8k
12k
16k
20k
Steps

0.2

0.4

0.6

0.8

Pass@256 (
)

Pass@256 (
)

GRPO
MaxRL
PKPO (K=16)
Differential Smoothing
GRPO (entropy)
SELF

Figure 12. (Training curves compared with other baselines.) We compare MAXRL with other RL algorithms, including entropy bonus,
PKPO (Walder & Karkhanis, 2025), Differential Smoothing (Gai et al., 2026) and SELF (Nguyen et al., 2025b), under batch size 32 and
number of training rollouts 128. MAXRL significantly outperforms other methods in all metrics, and is the only method to maintain both
good average performance (pass@1) and coverage (pass@k).

Table 3. Performance comparison across methods in maze (batch size 32, number of training rollouts per task 128).

Method
Pass@1
Pass@16
Pass@128
Pass@256

GRPO
39.6
41.3
42.4
43.0
GRPO (with entropy bonus)
47.2
51.7
53.4
54.0
PKPO (T = 16) (Walder & Karkhanis, 2025)
74.5
76.7
77.6
77.9
SELF (Nguyen et al., 2025b)
46.1
82.7
86.3
87.5
Differential Smoothing (Gai et al., 2026)
50.0
57.1
57.8
58.7

MAXRL
84.4
92.2
94.0
94.3

Table 3 compares MAXRL against a broader set of baselines in the Maze setting, where all models are trained for 20,000
steps with a batch size of 32 and 128 rollouts per prompt. MAXRL reaches 84.4 pass@1 and 94.3 pass@256, improving
over standard GRPO by more than 44 points on pass@1. PKPO attains a strong pass@1 of 74.5 but its pass@k curve is
nearly flat, indicating that it has largely collapsed onto a single mode and gains little from additional samples. SELF reaches
a high pass@256 of 87.5 yet a weak pass@1 of 46.1, trading away average accuracy for coverage. GRPO, with or without an
entropy bonus, and Differential Smoothing all remain well below 60 across the board; among these, Differential Smoothing
performs slightly better than GRPO with an entropy bonus, which in turn improves over vanilla GRPO. Figure 12 shows the
evolution of the Pass@k metrics for these baselines throughout during. Overall, MAXRL shows superior performance on
both average accuracy (pass@1) and coverage (pass@k).

42

## Page 43

Maximum Likelihood Reinforcement Learning

J. GSM8K Experiments

J.1. Prompt template

The goal of this experiment setting is to study how RL algorithms perform in data-scarce but compute rich settings. This is
similar in spirit to Kim et al. (2026), except that we study RL and not pre-training. Due to our compute limitations, we
choose a relatively small model (360M parameters) for our experiments. Specifically, we conduct reinforcement finetuning
on the SmolLM2-360M-Instruct model (Allal et al., 2025) using the GSM8K (Cobbe et al., 2021) training set for 1500
steps. We use GSM8K-Platinum (Vendrow et al., 2025), a revised version of the original GSM8K test that is non-overlapping
with the GSM8K train dataset, for evaluation. An example prompt and the model’s response are shown below. In particular,
we take each individual problem, append it with “ Let’s think step by step and output the final answer within \\boxed{}."
and process the string through the SmolLM2-360M-Instruct model’s tokenizer chat-template to obtain the final prompt for
the model.

SmolLM2-360M-Instruct

<|im_start|>system
You are a helpful AI assistant named SmolLM, trained by Hugging Face<|im_end|>
<|im_start|>user
Jeannie hikes the 12 miles to Mount Overlook at a pace of 4 miles per hour, and then
returns at a pace of 6 miles per hour.
How long did her hike take, in hours?
Let’s
think step by step and output the final answer within \\boxed{}.
<|im_end|>
<|im_start|>assistant
To find the time it takes for Jeannie to hike the entire trip, we need to calculate
her total travel time and then divide it by the rate at which she travels.
Jeannie hikes the 12 miles at a pace of 4 miles per hour.
So, the time taken is 12
miles / 4 miles per hour = 3 hours.
Next, she returns at a pace of 6 miles per hour.
So, the time taken to return is 12
miles / 6 miles per hour = 2 hours.
Therefore, the total time taken is 3 hours + 2 hours = 5 hours.
So, the final answer is 5 hours.
\\boxed{5} <|im_end|>

J.2. Hyperparameters

Detailed hyperparameter setup is provided in Table 4. For other baselines, we use T = 16 for PKPO, which means we
optimize pass@16 as the objective, and γ = 0.05 for differential smoothing.

Table 4. Training hyperparameters for SmolLM2-360M-Instruct on GSM8K.

Training hyperparameters for SmolLM2-360M-Instruct

Parameter
Value
Parameter
Value
Base model
SmolLM2-360M-Instruct
Training set
GSM8K
Test set
GSM8K
Prompts per batch
256
Generations per prompt
128
Grad update per RL step
1
Max prompt length
512
Max response len
2048
Learning rate
1 × 10−5
Training Steps
1500
KL coeff
0.0
Entropy coeff
0.0
Rollout temp
1.0
Validation top_p
0.95
Validation temp
0.6
Device
8 × Nvidia GH200

J.3. Effect of Additional Compute

In Figure 2, we demonstrated how MAXRL’s performance scales as additional compute is available in terms of rollout
budget, but in our supervised ImageNet classification setting. Here, we further experiment with the effect of additional

43

## Page 44

Maximum Likelihood Reinforcement Learning

compute on the finite data GSM8K training setting, which is a more realistic RL training since it involves autoregressive
generations from a 360M LLM on a real mathematical reasoning task.

1
4
16
64
256
1K
k

0.3

0.4

0.5

0.6

0.7

0.8

pass@k

SmolLM-360M-It (GSM8K)

T=1 (REINFORCE)
T=16
T=32
T=64
T=128

Figure 13. (Effect of number of training rollouts in the GSM8K setting) For MAXRL, increase in number of rollouts N directly leads
to an increase in the approximation order T of the maximum likelihood objective that the finite sample MAXRL optimizes. Here we
compare the final checkpoint resulting from training with different values of T(= Number of rollouts) but otherwise identical training
setup on the GSM8K setting. Increasing compute smoothly translates into performance gain, with the highest amount of gain for higher
pass@k.

Figure 13 shows our findings: as the number of training rollouts increases, it results in performance improvement in the final
checkpoint. Moreover, as expected, the biggest gains come at higher values of pass@k, with T = 128 outperforming T = 1
(REINFORCE) by almost 30% at pass@2048.

J.4. Comparison with Additional Baselines

Table 5. Performance comparison across methods on GSM8K.

Method
Pass@1
Pass@16
Pass@128
Pass@1024

GRPO (Shao et al., 2024)
29.3
40.1
45.8
48.8
RLOO (Ahmadian et al., 2024)
27.5
38.8
44.6
48.5
GRPO (with entropy bonus)
31.1
42.4
48.1
51.6
PKPO (T = 16) (Walder & Karkhanis, 2025)
30.7
53.6
67.2
75.9
Differential Smoothing (Gai et al., 2026)
31.4
42.7
48.5
52.3

MAXRL
33.2
60.3
75.0
83.4

Table 5 compares MAXRL against the same set of baselines in the data-scarce GSM8K training setting (Table 4). MAXRL
again achieves the best performance on every metric, reaching 33.2 pass@1 and 83.4 pass@1024. While all methods are
clustered within a few points at pass@1 (between 27.5 and 33.2), the differences widen dramatically as k grows: MAXRL
attains 83.4 pass@1024, 7.5 points above the strongest baseline (PKPO at 75.9) and more than 30 points above GRPO,
RLOO, GRPO with an entropy bonus, and Differential Smoothing, all of which saturate around 49–52. These results suggest
MAXRL extracts more learning signal from a fixed training dataset.

J.5. Per-Prompt Pass-Rate Distribution During Training

To visualize the sharpening dynamics of the three methods, Figure 14 tracks the empirical distribution of per-prompt pass
rates over the GSM8K training set throughout the SmolLM2-360M-Instruct run from Table 4. Each row corresponds to
a training epoch (0, 10, 20, 30, 40, 50), each column to a method, and each bar to the fraction of training prompts whose
pass-rate estimate falls into the corresponding log2-spaced bin (with the leftmost bin reserved for prompts with 0 correct
rollouts and the rightmost for prompts solved on every rollout). Validation pass@1 values of the corresponding checkpoints
over the entire evaluation dataset are reported on top of each panel.

Figure 14 suggests that GRPO and RLOO push the per-prompt pass-rate distribution towards either 0 or 1, supporting
the distribution sharpening narrative, whereas MAXRL retains a broad distribution of pass rates throughout training. This

44

## Page 45

Maximum Likelihood Reinforcement Learning

Epoch 0

Pass@1: 6.7%

MaxRL

Pass@1: 6.7%

GRPO

Pass@1: 6.7%

RLOO

Epoch 10

Pass@1: 21.3%
Pass@1: 29.1%
Pass@1: 27.5%

Epoch 20

Pass@1: 27.7%
Pass@1: 29.7%
Pass@1: 28.5%

Epoch 30

Pass@1: 31.5%
Pass@1: 29.4%
Pass@1: 28.0%

Epoch 40

Pass@1: 32.6%
Pass@1: 30.5%
Pass@1: 29.0%

-8 -7 -6 -5 -4 -3 -2 -1
0
Pass Rate (log2 )

Epoch 50

Pass@1: 33.1%

-8 -7 -6 -5 -4 -3 -2 -1
0
Pass Rate (log2 )

Pass@1: 29.4%

-8 -7 -6 -5 -4 -3 -2 -1
0
Pass Rate (log2 )

Pass@1: 27.6%

Figure 14. (Distribution sharpening over training on GSM8K) Evolution of the per-prompt pass-rate distribution on the SmolLM2-
360M-Instruct GSM8K training set across 50 training epochs for MAXRL, GRPO, and RLOO. All three methods start from the same
base-model distribution (epoch 0). As training progresses, GRPO and RLOO concentrate prompts into the two extreme bins (\[0, 0\] and
\[1, 1\]), so the model either trivially solves or trivially fails most prompts and the intermediate bins are emptied. In contrast, MAXRL keeps
probability mass spread across the entire pass-rate spectrum, gradually shifting weight from the failure end toward the higher pass-rate
bins while continuing to expose intermediate-difficulty prompts to non-zero learning signal.

contrast shows that MAXRL is more robust to the distribution sharpening commonly observed in LLM reinforcement
learning (Yue et al., 2025; Dang et al., 2025; Wu et al., 2026), allowing it to extract more learning signal from a fixed
training dataset.

45

## Page 46

Maximum Likelihood Reinforcement Learning

K. Qwen3 Experiments

K.1. Prompt template

We use the Qwen-math template (Yang et al., 2024a; Qwen et al., 2025; Yang et al., 2024b) for formatting our prompts. We
show an example prompt (Yu et al., 2025) after formatting through our template below. In particular, we take each individual
problem, append it with “\nPlease reason step by step, and put your final answer within \\boxed{{}}." and process the string
through the Qwen3 model’s tokenizer chat-template to obtain the final prompt for the model.

Qwen Math Prompt Template

<|im_start|>system
Please reason step by step and put the final answer in \\boxed{}.
<|im_end|>
<|im_start|>user
Denote by S(n) the sum of the digits of the positive integer n.
Find all the solutions
of the equation n(S(n) −1) = 2010.
Let’s think step by step and output the final answer
within \\boxed{}.
<|im_end|>
<|im_start|>assistant

K.2. Hyperparameters

Next, we describe the default hyperparameters for our training setup. Since there are many possible alternatives to handle
off-policy updates and corresponding importance ratio (Schulman et al., 2017; Shao et al., 2024; Zheng et al., 2025;
MiniMax et al., 2025; Yu et al., 2025), to keep things simple, we choose to train in the fully on-policy setup, meaning we
have no importance ratio or associated clipping. Similarly, to avoid tuning additional hyperparameters for each algorithm,
following Olmo et al. (2025), we remove KL penalty and also entropy bonus in our default training comparison. Note: we
train with GRPO and entropy bonus as a baseline in our SmolLM2-360M-Instruct training on GSM8K, results are recorded
in Table 5: MAXRL outperforms this variant, showing that entropy bonus does not fully mitigate issues resulting from
GRPO though it can slightly mitigate it, as also observed by Yue et al. (2025).

We generate all training rollouts using temperature 1.0, and do not use special sampling techniques. Similarly, we also do
not use any adaptive sampling (Yu et al., 2025) or fixes for inference-training logit mismatch (He, 2025; Khatri et al., 2026).
Finally, for evaluation, we follow the same protocol as Yue et al. (2025), and we run inference with temperature 0.6, top-p
sampling parameter 0.95, no top-k or min-p sampling (Nguyen et al., 2025a).

Table 6 shows our default hyperparameter setting.

Table 6. Training hyperparameters for Qwen3-1.7B-Base and Qwen3-4B-Base training.

Training hyperparameters for Qwen3-1.7B-Base and Qwen3-4B-Base

Parameter
Value
Parameter
Value
Base model
Qwen3-1.7B-Base, Qwen3-4B-Base
Prompts per batch
256
Generations per prompt
16
Grad update per RL step
1
Max prompt length
1024
Max response len
4096
Learning rate
1 × 10−6
Training Steps
1000
KL coeff
0.0
Entropy coeff
0.0
Rollout temp
1.0
Validation top-p
0.95
Validation temp
0.6
Device
32 × Nvidia H200

K.3. Additional Results

We report additional empirical results from our Qwen3-1.7B-Base and Qwen3-4B-Base training runs that complement the
main-paper evaluation. We expand the benchmark coverage with four further reasoning datasets, compare MAXRL against
the base model and GRPO under verifier-free majority voting, and report training-dynamics traces (response length, actor
entropy, gradient norm) as well as validation pass@1 curves throughout training.

46

## Page 47

Maximum Likelihood Reinforcement Learning

Extended Benchmarks.
Beyond the four primary benchmarks reported in the main paper, we further evaluate the
Qwen3-4B-Base trained model on four additional reasoning benchmarks: AIME 2024, HMMT Feb 2025 (MathArena,
2025a), HMMT Nov 2025 (MathArena, 2025b), and JEEBENCH (Arora et al., 2023). Figure 15 reports coverage on these
benchmarks; MAXRL matches or outperforms both the base model and GRPO, achieving up to 20.5× speedup over GRPO
when generating multiple samples under a perfect verifier while maintaining similar or better pass@1 performance.

1
16
256
4096

10

30

50

70

Qwen3-1.7B-Base

Coverage (Pass@k)

AIME 2024

7.3×

1
16
256
4096

10

30

50

HMMT Feb 2025

20.5×

1
16
256
4096

10

30

HMMT Nov 2025

3.4×

1
16
256
4096

10

30

50

70

90
JEEBENCH

1.6×

1
16
256
4096
k

10

30

50

70

Qwen3-4B-Base

Coverage (Pass@k)

1.7×

1
16
256
4096
k

10

30

50

17.0×

1
16
256
4096
k

10

30

50

3.3×

1
16
256
4096
k

10

30

50

70

90

4.6×

Base
GRPO
MaxRL

Figure 15. (Evaluation of Qwen3 model training on additional benchmarks) Coverage on AIME 2024, HMMT Feb 2025 (MathArena,

2025a), HMMT Nov 2025 (MathArena, 2025b), and JEEBENCH (Arora et al., 2023). MAXRL matches or outperforms both the base
model and GRPO, leading to up to 20.5× speedup compared to GRPO while generating multiple samples with a perfect verifier and
maintaining similar or better pass@1 performance.

Majority voting.
We compare MAXRL against the base model and GRPO under majority voting (Wang et al., 2023a),
a widely used verifier-free method for scaling test-time compute: we draw N i.i.d. rollouts for each prompt, group the
responses by their final answer, and take the most frequent answer as our prediction. Table 7 reports majority-voting
accuracy on five benchmarks; MAXRL outperforms both the pretrained base model and the GRPO-trained model on every
benchmark.

Table 7. (Majority voting performance comparison on Qwen3-4B-Base) We compare the performance of MAXRL in terms of majority
voting against the pretrained base model and GRPO.

AIME 2024
AIME 2025
BeyondAIME
MATH-500
Minerva
(majority@4096)
(majority@4096)
(majority@4096)
(majority@2048)
(majority@2048)
Base
23.3
23.3
7.0
69.8
18.8
GRPO
23.3
23.3
7.0
72.4
27.2
MAXRL
26.7
26.7
14.0
74.0
28.7

Training dynamics.
We record mean generated response length, actor entropy, and gradient norm throughout training
for both Qwen3-4B-Base (Figure 16) and Qwen3-1.7B-Base (Figure 17). The trends are consistent across model sizes:
MAXRL produces longer chains-of-thought, retains higher actor entropy, and exhibits larger gradient norms during training
compared with GRPO.

Validation accuracy during training.
In addition, we examine pass@1 (estimated using 32 samples) over the course of
training on intermediate evaluation datasets. For Qwen3-4B-Base, MAXRL consistently outperforms GRPO across the
three evaluation datasets (Figure 18). For the smaller Qwen3-1.7B-Base model (Figure 19), MAXRL initially trails GRPO

47

## Page 48

Maximum Likelihood Reinforcement Learning

0
250
500
750
1000
RL Step
800

1200

1600

2000

2400

Mean Response Length

Mean Response Length

0
250
500
750
1000
RL Step

0.04

0.08

0.12

0.16

0.20

Actor Entropy

Actor Entropy

0
250
500
750
1000
RL Step

0.05

0.10

0.15

0.20

0.25

Gradient Norm

Gradient Norm

GRPO
MaxRL

Figure 16. (Additional training dynamics metrics for Qwen3-4B-Base) We show comparison between GRPO and MAXRL in terms
of mean response length, entropy of the actor, and gradient norm during training for the Qwen3-4B-Base model. MAXRL generally
produces longer chains-of-thought, and also retains higher actor entropy during training. MAXRL also produces larger gradient norms
during training.

0
250
500
750
1000
RL Step
800

1200

1600

2000

Mean Response Length

Mean Response Length

0
250
500
750
1000
RL Step

0.12

0.16

0.20

Actor Entropy

Actor Entropy

0
250
500
750
1000
RL Step

0.05

0.10

0.15

0.20

0.25

Gradient Norm

Gradient Norm

GRPO
MaxRL

Figure 17. (Additional training dynamics metrics for Qwen3-1.7B-Base) We show comparison between GRPO and MAXRL in terms
of mean response length, entropy of the actor, and gradient norm during training for the Qwen3-1.7B-Base model. MAXRL generally
produces longer chains-of-thought, and also retains higher actor entropy during training. MAXRL also produces larger gradient norms
during training.

0
250
500
750
1000
RL Step

10

15

20

25

Validation pass@1 (%)

AIME 2024

0
250
500
750
1000
RL Step
5

10

15

20
AIME 2025

0
250
500
750
1000
RL Step
65

75

85
MATH-500

GRPO
MaxRL

Figure 18. (Qwen3-4B-Base validation pass@1 during training) Pass@1 (estimated using 32 samples) during training of Qwen3-4B-
Base, on 3 different evaluation datasets. MAXRL consistently outperforms GRPO during training.

0
250
500
750
1000
RL Step

4

8

12

Validation pass@1 (%)

AIME 2024

0
250
500
750
1000
RL Step
2

4

6

8
AIME 2025

0
250
500
750
1000
RL Step
55

60

65

70

75
MATH-500

GRPO
MaxRL

Figure 19. (Qwen3-1.7B-Base validation accuracy during intermediate training) We record validation pass@1 (using mean over 32
rollouts per prompt) over AIME 2024, AIME 2025 and MATH-500 during Qwen3-1.7B-Base model training.

at pass@1, similar to the SmolLM curve in Figure 4, but catches up with extended training and ultimately converges to a
higher value.

48

## Page 49

Maximum Likelihood Reinforcement Learning

L. Comparison with Additional Baselines

L.1. PKPO

Realizing the shortcomings of the expected reward (pass@1) optimization paradigm in reinforcement learning, recent
work (Walder & Karkhanis, 2025; Tang et al., 2025; Bagirov et al., 2025) has also proposed directly optimizing for pass@k
during RL training. The connection between maximum likelihood and harmonic mixture of pass@k optimization necessitates
a direct comparison between our work and these pass@k optimization procedures. Here we present comparisons with a
representative baseline, PKPO (Walder & Karkhanis, 2025). PKPO has a tunable hyperparameter T, which dictates the
order of optimization objective, namely PKPO with parameter T optimizes pass@T directly.

Table 8. Comparison between PKPO (T = 16) and MAXRL on the maze setting.

Method
Pass@1
Pass@16
Pass@128
Pass@256

PKPO (T = 16) (Walder & Karkhanis, 2025)
74.5
76.7
77.6
77.9
MAXRL
84.4
92.2
94.0
94.3

Table 9. Comparison between PKPO (T = 16) and MAXRL on the GSM8K setting.

Method
Pass@1
Pass@16
Pass@128
Pass@1024

PKPO (T = 16) (Walder & Karkhanis, 2025)
30.7
53.6
67.2
75.9
MAXRL
33.2
60.3
75.0
83.4

Tables 8 and 9 show comparison between PKPO and MAXRL on the maze and GSM8K settings, respectively. PKPO
experiments are run with T = 16, with all other hyperparameters kept the same as their default values for the respective
settings. We observe that MAXRL outperforms PKPO at all values of pass@k. More importantly, MAXRL outperforms
PKPO at pass@16, despite the latter explicitly optimizing for this metric. A similar phenomenon is observed with
REINFORCE, which directly optimizes pass@1 yet consistently underperforms MAXRL at pass@1. This suggests that
directly optimizing a specific pass@k objective does not necessarily yield the best performance at that pass@k. We
hypothesize that MAXRL’s aggregation of signals across pass@k events enables more effective use of the learning signal,
and leave a detailed investigation to future work.

1
16
256
4096
k

10

20

30

40

50

60

70

Qwen3-4B-Base

Coverage (Pass@k)

BeyondAIME

1
16
256
4096
k

20

30

40

50

60

70

80

AIME 2025

1
8
64
512
k

82.5

85.0

87.5

90.0

92.5

95.0

97.5

100.0
MATH-500

1
8
64
512
k

40

45

50

55

60

65

70
Minerva

PKPO (T = 4)
PKPO (T = 8)
PKPO (T = 16)
MaxRL

Figure 20. (Comparison with PKPO on Qwen3-4B-Base training) We compare MAXRL against PKPO for T ∈{4, 8, 16}. MAXRL
retains the same performance or outperforms PKPO with different values for T. On harder evaluation datasets like BeyondAIME and
AIME 2025, the gap is more pronounced, and MAXRL outperforms PKPO at pass@k for all values of k that we evaluated on.

Figure 20 shows further comparisons against PKPO on the large scale LLM training setting. Specifically, we train a
Qwen3-4B-Base model on the POLARIS-53K dataset, using the default hyperparameters for this setting. For PKPO, we
train with 3 different values of T, namely 4, 8, and 16. MAXRL retains similar performance or outperforms PKPO on all 4
evaluation datasets. On harder evaluation datasets like BeyondAIME and AIME 2025, the gap is more pronounced, and
MAXRL outperforms PKPO at pass@k for all values of k that we evaluated on. These large-scale training experiments
validate our results from the smaller maze and GSM8K settings.

49

## Page 50

Maximum Likelihood Reinforcement Learning

L.2. ZPD

One way of thinking about MAXRL is to focus on its upweighting of high-difficulty prompts. This raises the question: how
does MAXRL compare to methods that perform difficulty-aware sampling strategies? RLOO with a “not too easy, not too
hard" curriculum (ZPD (Bae et al., 2026)) can be interpreted as reweighting prompts with weight w(p) = p(1 −p), where
p = pθ(x) is the pass rate for prompt x, in Table 2. Since we do not use any additional curriculum learning or involved
sampling strategies in our setting for the sake of simplicity, we choose to compare against this variant of ZPD by employing
the advantage function ˆA(x, y) = ˆr(1 −ˆr)(r(x, y) −ˆr), where ˆr is the Monte-Carlo estimate of the pass rate for prompt x.

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

20

40

60

Validation Pass@1 (
)

Pass@1 (
)

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

25

50

75

100

Validation Pass@128 (
)

Pass@128 (
)

MaxRL (Rollout = 16)
ZPD (Rollout = 131072)

MaxRL (Rollout = 128)
Cross Entropy

MaxRL (Rollout = 1024)

Figure 21. (Comparison with ZPD on supervised ImageNet classification setting) We compare MAXRL against ZPD on the ImageNet
setting under identical training setup. Similar to REINFORCE, ZPD fails to improve significantly beyond the randomly initialized model.

First, we compare against ZPD on the ImageNet classification setting in Figure 21. ZPD performs similarly to REINFORCE
here, and fails to improve the model significantly beyond its random initialization at the beginning of training.

1
4
16
64
256
1K
k

0.2

0.4

0.6

0.8

1.0

pass@k

Qwen2-3M (Maze)

1
4
16
64
256
1K
k

0.3

0.4

0.5

0.6

0.7

0.8

SmolLM-360M-It (GSM8K)

MaxRL
ZPD

Figure 22. (Comparison with ZPD in the maze and GSM8K setting.) We compare MAXRL against ZPD on the infinite data maze
and finite data GSM8K training settings under identical training budget and hyperparameters. On both settings, MAXRL significantly
outperforms ZPD at pass@k, for all values of k that we evaluated on.

Next, we evaluate ZPD on the maze and GSM8K training settings. Figure 22 shows our main results: under identical training
settings and compute budget, MAXRL outperforms ZPD on both settings, achieving significantly higher pass@k for all
values of k that we evaluated on. On GSM8K, MAXRL achieves ∼30% improvement in pass@2048 over ZPD.

Finally, we also compared MAXRL with ZPD on our largest training setting: Qwen3-4B-Base trained on POLARIS-
53K. Figure 23 shows our main findings: under identical training setup and compute budget (1000 steps of RL training),
MAXRL outperforms ZPD on all evaluation datasets, achieving gains of 12.6× to 29.0× in test-time scaling efficiency
under a perfect verifier.

50

## Page 51

Maximum Likelihood Reinforcement Learning

1
16
256
4096
k

0

10

20

30

40

50

60

70

Qwen3-4B-Base

Coverage (Pass@k)

BeyondAIME

19.6×

1
16
256
4096
k

0

10

20

30

40

50

60

70

80

AIME 2025

15.0×

1
8
64
512
k

65

70

75

80

85

90

95

100
MATH-500

12.6×

1
8
64
512
k

30

40

50

60

70
Minerva

29.0×

Base
ZPD
MaxRL

Figure 23. (Comparison with ZPD on Qwen3-4B-Base training) We compare MAXRL against ZPD while training a Qwen3-4B-Base
model on the POLARIS-53K dataset under identical training setup and compute budget (1000 steps of RL training). MAXRL outperforms
ZPD on evaluation datasets, achieving 12.6× to 29.0× gains in test-time scaling efficiency under a perfect verifier.

L.3. Power Function

Finally, MAXRL can be seen as optimizing a particular non-linear function of the pass rate (log pθ(x)). This begs the
question of how other non-linear functions of the pass rate may perform. Here we compare with an example function
from Xiong et al. (2025b), namely, the Power Function weighting. The Power Function with parameter α > 0 is defined
as f(t) = tα, and correspondingly one can optimize Jα
power−function = Ex∼ρ\[pθ(x)\]α. The corresponding gradient of this
objective is:
∇θJα
power−function = Ex∼ρ

αpθ(x)α−1∇θpθ(x)


where ∇θpθ(x) is the standard REINFORCE gradient. Xiong et al. (2025b) particularly considers power functions with
α = 1

2, giving the following gradient:

∇θJpower−function = Ex∼ρ

"
1

2
p

pθ(x)
∇θpθ(x)

#

In practice, this objective can be optimized by setting the advantage to be ˆA(x, y) = r(x,y)−ˆr

2
√

ˆr
when ˆr > 0 and 0 otherwise,
with ˆr being the Monte-Carlo estimate of the pass rate for prompt x. This is the variant of the Power Function objective that
we will compare MAXRL against in this work.

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

20

40

60

Validation Pass@1 (
)

Pass@1 (
)

0.0
0.2
0.4
0.6
0.8
1.0
Gradient Steps
1e5

0

25

50

75

100

Validation Pass@128 (
)

Pass@128 (
)

MaxRL (Rollout = 16)
Power Function (Rollout = 131072)

MaxRL (Rollout = 128)
Cross Entropy

MaxRL (Rollout = 1024)

Figure 24. (Comparison with Power Function on supervised ImageNet classification setting) We compare MAXRL against the Power
Function on the ImageNet setting under identical training setup. Despite using significantly more compute, the Power Function remains
suboptimal at both pass@1 and pass@128, with the gap being larger at pass@128.

First, we compare against this version of the Power Function on our supervised ImageNet classification setting under an

51

## Page 52

Maximum Likelihood Reinforcement Learning

identical training recipe. Figure 24 shows our empirical findings: MAXRL outperforms Power Function at both pass@1
and pass@128 despite using 128x less rollout compute budget. Moreover, the gap is higher for pass@128, showing that
despite performing better than REINFORCE and GRPO in this setting, ultimately the Power Function is a suboptimal choice
compared to MAXRL here.

1
4
16
64
256
1K
k

0.85

0.9

0.95

pass@k

Qwen2-3M (Maze)

1
4
16
64
256
1K
k

0.3

0.4

0.5

0.6

0.7

0.8

SmolLM-360M-It (GSM8K)

MaxRL
Power Function

Figure 25. (Comparison with Power Function in the maze and GSM8K setting.) We compare MAXRL against the Power Function
variant mentioned in this section on the infinite data maze and finite data GSM8K training settings under identical training budget and
hyperparameters. On both settings, MAXRL significantly outperforms the Power Function at pass@k, for all values of k that we evaluated
on.

Next, we scale up our comparisons to the infinite training data maze and finite training data GSM8K settings using identical
training hyperparameters and compute budget. Figure 25 summarizes our main findings: MAXRL outperforms this variant
of the Power Function objective on both settings. MAXRL achieves significantly higher pass@k on both settings, and
outperforms Power Function by ∼20% at pass@2048 on GSM8K.

1
16
256
4096
k

0

10

20

30

40

50

60

70

Qwen3-4B-Base

Coverage (Pass@k)

BeyondAIME

4.1×

1
16
256
4096
k

0

10

20

30

40

50

60

70

80

AIME 2025

6.4×

1
8
64
512
k

65

70

75

80

85

90

95

100
MATH-500

1.4×

1
8
64
512
k

30

40

50

60

70
Minerva

12.4×

Base
Power Function
MaxRL

Figure 26. (Comparison with Power Function on Qwen3-4B-Base training) We compare MAXRL against the Power Function variant
mentioned in this section while training a Qwen3-4B-Base model on the POLARIS-53K dataset under identical training setup and
compute budget (1000 steps of RL training). MAXRL matches or outperforms the Power Function on evaluation datasets, achieving up to
12.4× gains in test-time scaling efficiency under a perfect verifier.

Finally, we also compared MAXRL against the Power Function on our largest training setting: Qwen3-4B-Base trained on
POLARIS-53K. Figure 26 shows our main findings: under identical training setup and compute budget (1000 steps of RL
training), MAXRL matches or outperforms Power Function on all 4 evaluation datasets, achieving up to 12.4× test-time
scaling efficiency gains under a perfect verifier.

52

## Page 53

Maximum Likelihood Reinforcement Learning

M. Additional Analyses

M.1. Non-Zero Gradient Signal Analysis

A prompt for which the model fails to generate any correct rollout contributes no gradient under REINFORCE, GRPO,
RLOO, or MAXRL, since the advantage vanishes when every sampled return equals the empirical baseline. The fraction of
training prompts with at least one correct rollout therefore serves as a direct measure of how much of the training batch
produces nonzero learning signal at each step. We extend the analysis in Figure 7 from the large-scale LLM settings to the
maze and SmolLM2-360M-Instruct on GSM8K training settings, and record this fraction throughout training in Figure 27.
MAXRL consistently produces at least one correct rollout for a larger fraction of prompts than GRPO and RLOO across
both settings, and the gap persists as training progresses. This matches the trends observed in the large-scale experiments
and offers a complementary view on why MAXRL continues to improve when REINFORCE-style baselines stall: by
upweighting harder prompts and producing larger gradient norms on them (Figure 6), MAXRL keeps a larger fraction of the
dataset contributing useful gradient signal even after the easier prompts have saturated.

0
300
600
900
1200
RL Step
40

50

60

70

80

90

Training prompts with

non-zero pass rate (%)

SmolLM-360M-Instruct

on GSM8K

0
3000
6000
9000
RL Step

20

40

60

80

17x17 Maze

MaxRL
GRPO
RLOO

Figure 27. (Fraction of training tasks with non-zero pass rate) Similar to Figure 6, we also record the fraction of training tasks where
the model generates at least one correct rollout on maze and SmolLM2-360M-Instruct training on GSM8K. We see the same trends
as Figure 7, and MAXRL consistently outperforms both GRPO and RLOO, demonstrating MAXRL’s ability to generate better learning
signal during training, as tasks with zero pass-rate contribute no gradients.

M.2. Policy Gradient Variance Analysis

In this section, we analyze the variance of policy-gradient estimates for MAXRL and other methods, focusing on two
questions: (1) does the baseline in our estimator (Equation (10)) actually reduce variance, and (2) how does estimator noise
scale with the number of rollouts for MAXRL?

We first study the effect of the control variate in MAXRL. Note that using the unconditional average score function as
the baseline is not guaranteed to reduce variance. Previous work such as Greensmith et al. (2004) has noted that this can
indeed be suboptimal even for the canonical REINFORCE objective, and provides the derivation of an optimal baseline.
However, computing the optimal baseline is complicated in practice, and the average score function as the standard choice
of baseline is empirically justified and widely used (Ahmadian et al., 2024; Zeng et al., 2025a). In this section, we follow
the same direction and provide empirical proof that the variance reduction technique used by us indeed reduces variance in
practical scenarios. Using the rollout pools from the previous experiments, we estimate the trace of the sample covariance
matrix across policy-gradient minibatches, following prior work (McCandlish et al., 2018; Zeng et al., 2025a). Given B
independently sampled minibatch gradient estimates {gb}B
b=1, we compute

bV(g) = tr

d
Cov(g)

=
1
B −1

B
X

b=1
∥gb −¯g∥2
2,
¯g = 1

B

B
X

b=1
gb,

where each gb is the flattened policy-gradient vector for one sampled minibatch. Specifically, for GSM8K and Polaris-53K,
we use 16 prompts with 512 pre-generated rollouts per prompt; for Maze, we use 256 prompts with 1024 rollouts per prompt.
For each N ∈{4, 8, 16, 32, 64, 128}, we randomly subsample B = 4 minibatches with N rollouts per prompt and report
bV(g). Figure 28 shows that the baseline consistently lowers the variance of the MAXRL gradient estimator across rollout

53

## Page 54

Maximum Likelihood Reinforcement Learning

counts and tasks. The baseline is most important when number of rollouts is low, and eventually for high enough rollout
count the gradient variance with and without baseline seems to converge, as expected.

4
8
16
32
64
128
Rollouts (N)

0.02

0.04

0.06

0.08

0.10

0.12

Gradient Variance

Qwen2-3M (Maze)

4
8
16
32
64
128
Rollouts (N)

0.2

0.3

0.4

0.5

SmolLM-360M (GSM8K)

4
8
16
32
64
128
Rollouts (N)

0.150

0.175

0.200

0.225

0.250
Qwen3-1.7B (Polaris-53K)

MaxRL
MaxRL (w/o baseline)

Figure 28. (Effect of the MAXRL baseline on gradient variance) We estimate the trace of the sample covariance matrix of gradient
estimates with and without the proposed baseline for experiments in Section 6. The baseline consistently lowers variance.

22
24
26
28
210
212
214
216
218
220
Rollouts (N)

10
6

10
5

10
4

10
3

10
2

10
1

1 / SNR

ResNet (ImageNet)

4
8
16
32
64
128
Rollouts (N)

0.02

0.05

0.1

0.2

0.5

1

Qwen2-3M (Maze)

4
8
16
32
64
128
Rollouts (N)

0.2

0.5

1

2

5

10

SmolLM-360M-It (GSM8K)

GRPO
RLOO
MaxRL

Figure 29. (Inverse gradient SNR across rollout counts) We compare normalized gradient variance for GRPO, RLOO, and MAXRL.
MAXRL becomes increasingly accurate as the number of rollouts grows.

We next study how the signal-to-noise ratio (SNR) of policy gradients scales with the number of rollouts for MAXRL,
GRPO, and RLOO. Since these methods optimize different objectives, raw variance is not directly comparable across
methods. We therefore normalize by the squared norm of the expected gradient and report inverse signal-to-noise ratio,
tr(Cov(g))

∥E\[g\]∥2
2 , where lower values indicate a more accurate gradient estimate relative to its signal. On ImageNet, we estimate
this quantity using ResNet-50 gradients over a fixed batch of 1024 images and 64 gradient samples per rollout count. For
Maze, we sample 8 prompt batches of 256 prompts from the pre-generated rollout table and estimate inverse SNR from 64
randomized rollout minibatches. For SmolLM on GSM8K, we fix one batch of 64 prompts and form 64 gradient samples
through repeated rollout subsampling. Figure 29 shows that the normalized variance of MAXRL decreases as N increases,
following the same qualitative trend as GRPO and RLOO.

Together, these results suggest that the proposed baseline reduces the raw variance of the MAXRL estimator. They
also show that the stability of MAXRL improves as the rollout budget increases, despite its stronger amplification of
very-low-success-rate problems.

M.3. On the Distribution Sharpening Narrative

Recent work (Yue et al., 2025; Wu et al., 2026) has shown that RL trained models can underperform base models at
pass@k, and thereby under a high sampling budget coupled with a perfect verifier, base models can solve a larger number
of problems than their RL-trained counterpart. We saw in our experiments that contrary to the standard REINFORCE
and GRPO objectives, MAXRL increases pass@k even for very large values of k beyond that of the base model in a
majority of scenarios and especially if we do not overtrain. The natural next question to ask is whether MAXRL can lead to
expansion of capability beyond the base model. Since any sequence of tokens that lead to the correct answer has a non-zero
probability under any language model, we instead ask this question from a finite compute perspective: if one has a large
but finite compute, what fraction of the problems can one solve with the base model, and its GRPO- and MAXRL-trained
counterparts?

54

## Page 55

Maximum Likelihood Reinforcement Learning

Table 10. Per-problem solvability on AIME 2025 with 4096 samples per question. We list the indices of problems solved by each model.
Compared to the base model and GRPO-trained model, MAXRL solves three additional problems (10, 24, and 27) exclusively.

Model
Solved Problem Indices (AIME 2025)
Solved

Qwen3-4B-Base
0, 1, 2, 3, 4, 5, 7, 8, 9, 12, 13, 14, 15, 16, 18,
19, 20, 21, 22, 23, 26, 28, 29
23/30

GRPO (1000 steps)
0, 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16,
18, 19, 20, 21, 22, 23, 26, 29
23/30

MAXRL (1000 steps)
0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29
27/30

Table 10 shows the results of empirical study. Specifically, we take the Qwen3-4B-Base model, and its final GRPO and
MAXRL trained checkpoints after 1000 steps of RL training. Next, we generate 4096 rollouts for each of the 30 questions
in the AIME 2025 dataset, from each of these 3 models. We list the indices of the problems where each model generates at
least 1 correct solution from its 4096 rollouts. We see that the problems solved by the base model and GRPO-trained model
are strict subsets of the problem set solved by MAXRL. Moreover, MAXRL solves 3 additional problems exclusively that
are not solved by either the base model or the GRPO-trained model.

PPLBase(YBase)
PPLBase(YMaxRL)
PPLGRPO(YMaxRL)
PPLMaxRL(YMaxRL)

1.0

1.1

1.2

1.3

1.4

Perplexity

Perplexity of MaxRL-solved trajectories

(AIME25 IDs 10, 24, 27)

Figure 30. (Perplexity analysis on math problems, using Qwen3-4B-Base and its fine-tuned variants) We collect YMaxRL, the 15
correct trajectories from 3 problems on AIME 2025 that only the MAXRL-trained model can solve, and compute the perplexity of each
trajectory under all three models. For comparison, we also compute the perplexity of YBase, an equal number of incorrect rollouts from
the base model. The results show that YMaxRL have high perplexity under both the base model and the GRPO-trained model, suggesting
that MAXRL develops capabilities beyond those present in the base model. Diamonds denote means and circles denote outliers.

Beyond Table 10, we also provide additional evidence in the form of perplexity analysis. Specifically, Figure 30 shows
that on the 3 problems from AIME 2025 that only our MAXRL-trained checkpoint could solve, the 15 correct rollouts
have very high perplexity under the base and GRPO trained checkpoint. As a control set, we also record perplexity of an
equal number of incorrect rollouts generated from the base model, and show that they have much lower perplexity than the
MAXRL-generated correct trajectories. Overall, we believe that MAXRL can induce capabilities beyond what is present in
the base model, and leave further studying this for future work.

M.4. Non-Binary Reward Settings

Our work focuses on binary correctness-based rewards, where the connection to maximum likelihood is most direct. While
the binary reward setting already captures a broad and practically important class of RL problems, including applications
such as improving complex reasoning in LLMs (e.g., math and code generation) (Zeng et al., 2025b; Mroueh, 2026; Luo
et al., 2025) and robotics (Liu et al., 2023; Herzog et al., 2023; Kalashnikov et al., 2018), here we study non-binary reward
settings for the sake of completeness.

Interestingly, MAXRL admits a natural extension to non-binary reward settings under mild assumptions. In particular,
for non-negative rewards with non-zero expectation under the policy (i.e., Ey∼πθ(·|x)\[r(x, y)\] > 0), we can generalize the

55

## Page 56

Maximum Likelihood Reinforcement Learning

0.0
0.2
0.4
0.6
0.8
1.0
1.2
Gradient Steps
1e4

10

30

50

70

Validation Mean@32 Reward

Mean Reward@32 (
)

0.0
0.2
0.4
0.6
0.8
1.0
1.2
Gradient Steps
1e4

20

40

60

80

Validation Best@32 Reward

Best Reward@32 (
)

GRPO
MaxRL

Figure 31. (MAXRL extended to non-binary reward maze setting) We experiment with our extension of MAXRL in the modified
maze setting with non-binary rewards. MAXRL outperforms GRPO in this setting: it achieves 38% higher Mean@32 and 51% higher
Best@32 validation reward compared to GRPO. On the other hand, the Best@32 reward for GRPO has collapsed, showing that training
for longer is unlikely to improve for GRPO, whereas both Mean and Best reward are still increasing at the end of training for MAXRL.

MAXRL objective from
log Ey∼πθ(·|x)\[I\[y = y∗\]\]

to
log Ey∼πθ(·|x)\[r(x, y)\]

This yields a gradient estimator analogous to MAXRL, with advantage:

A(x, yi) = r(x, yi) −ˆµ

ˆµ

where ˆµ is the Monte-Carlo estimate of Ey∼πθ(·|x)\[r(x, y)\].

We have evaluated this extension on a modified version of the Maze task with continuous rewards r ∈\[0, 1\], where shorter
trajectories receive higher rewards. Specifically, for maze x, let Li(x) denote the length of the i-th rollout, Lmin(x) denote
the shortest possible path length, and T denote the maximum trajectory length possible (usually equal to the token limit for
each generation). We define

ri =
T −Li(x)
T −Lmin(x)

In this setting, we train a 16M transformer with batch size 256 and 16 rollouts per task, with all other hyperparameters kept
the same as the default values for the maze setting. This extension of MAXRL outperforms GRPO by 38% in mean reward
and 51% in best@32 reward. Moreover, in this setting, the Best@32 reward for GRPO has collapsed, showing that training
for longer is unlikely to improve for GRPO, whereas both Mean and Best reward are still increasing at the end of training
for MAXRL.

While the initial results are encouraging, we leave the full theoretical treatment and broader empirical evaluation of
non-binary rewards to future work.

56
