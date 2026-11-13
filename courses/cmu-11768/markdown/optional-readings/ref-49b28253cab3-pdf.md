# Differential Smoothing (PDF)

[Course index](../../README.md) · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/gai26a/gai26a.pdf) · [Raw file](../../raw/optional-readings/ref-49b28253cab3-pdf.pdf)

Retrieved: 2026-11-13T16:59:52.643294+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Jingchu Gai * 1 Guanning Zeng * 2 Huaqing Zhang * 2 Aditi Raghunathan 1

Abstract

It is widely recognized that reinforcement learn-
ing (RL) fine-tuning of large language models
often leads to diversity collapse, where outputs
lack variety. Prior work has proposed a range of
heuristics to counteract this effect, but these meth-
ods are ad hoc: they frequently trade off correct-
ness for diversity, their effectiveness varies across
tasks, and in some cases they even contradict one
another. In this work, we place these observa-
tions on a rigorous foundation. We first provide
a formal proof of why RL fine-tuning exhibits di-
versity collapse via a selection and reinforcement
bias. Next, we make a key observation that any
reward modification to address diversity collapse
only needs to be applied on the correct trajecto-
ries. Building directly on this analysis, we intro-
duce a principled method—differential smooth-
ing—that provably improves both correctness and
diversity, outperforming vanilla RL as well as
widely used entropy-based heuristics. Our theory
precisely characterizes when existing heuristics
help and why they fail, while showing that differ-
ential smoothing is universally superior. Exten-
sive experiments with models from 1B to 7B pa-
rameters, across domains including CountDown
and real-world mathematical reasoning, demon-
strate consistent gains. Differential smoothing
improves both Pass@1 and Pass@k in most eval-
uated settings, with up to 11.4% improvements
on AIME25 dataset.

1. Introduction

Reinforcement learning (RL) has become a powerful tech-
nique for fine-tuning Large Language Models (LLMs), en-
hancing capabilities ranging from complex reasoning (Guo

1Carnegie
Mellon
University,
Pittsburgh,
PA,
USA.
jgai@andrew.cmu.edu, raditi@cmu.edu 2Tsinghua University, Bei-
jing, China. {zgn21,zhanghq22}@mails.tsinghua.edu.cn. Corre-
spondence to: Jingchu Gai <jgai@andrew.cmu.edu>.

Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).

et al., 2025; Yu et al., 2026; Shao et al., 2024) to human
preference alignment (Ouyang et al., 2022; Bai et al., 2022).
However, this process is often plagued by a significant side
effect: a collapse in generation diversity (Song et al., 2025b;
Dang et al., 2025; Chen et al., 2026b; Zhao et al., 2025; He
et al., 2025a). This degradation is empirically observed in
metrics like Pass@K; RL-tuned models often show dimin-
ishing improvements for larger values of K and can even
underperform the original base model (He et al., 2025a;
Cobbe et al., 2021; Chow et al., 2025; Chen et al., 2026a).

However, mitigating this diversity collapse is non-trivial
and presents several challenges. Simple heuristics such as
early stopping or high-temperature decoding may boost di-
versity and achieve higher Pass@K, but they frequently hurt
Pass@1 performance. This points to an inherent tension
between increasing diversity and preserving accuracy. Sec-
ond, most existing methods lack robustness across settings.
A striking example is entropy control, where some works
recommend maximizing entropy to improve both Pass@1
and Pass@K, while others report that minimizing entropy
can yield the same outcome. Our experiments confirm that
prior techniques designed to enhance diversity fail to suc-
ceed broadly and often succeed only on the tasks for which
they were originally developed.

Motivated by these limitations, our work has two primary
goals: (1) to provide clarity on the seemingly contradictory
effects of previous methods, and (2) to develop a principled
method that robustly improves both correctness (Pass@1)
and diversity (Pass@K) across a range of benchmarks.

Our analysis from first principles shows that RL fine-tuning
introduces two biases, selection bias and reinforcement
bias, which jointly cause diversity collapse within the cor-
rect trajectories. Selection bias arises because correct tra-
jectories with high probability under the pre-trained model
are more likely to be reinforced (Theorem 6). Reinforce-
ment bias then arises because these same trajectories receive
disproportionately larger updates (Theorem 7).

Leveraging the insights from our theoretical analysis, we
propose a simple but novel twist to vanilla RL. The core of
our method is that while we need to change the reward func-
tion on correct trajectories to prevent the diversity collapse,
the incorrect trajectories can continue to use the original
reward or even a modification that encourages “sharpening”.

1

## Page 2

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Figure 1. Illustration on the effect of entropy

This differentiated reward mechanism that applies distinct
pressures to correct and incorrect trajectories can provably
mitigate the tradeoff between correctness and diversity that
plagues other heuristics.

We propose the differential smoothing approach. For cor-
rect trajectories, our reward mitigates the diversity collapse
by subtracting a term proportional to their log-probability.
On incorrect trajectories, our reward modification focuses
on correctness, by adding the log-probability of the incor-
rect trace. We present our proposed DS-GRPO algorithm in
Section 3.2.

We validate our differential smoothing approach both the-
oretically and empirically. Our theoretical analysis (Sec-
tion 2) formally proves that the reward modification for
correct trajectories directly optimizes for diversity, while
the adjustment for incorrect ones enhances correctness with-
out compromising diversity.

We evaluate DS-GRPO on five different models ranging
from 1.5B-8B, and across a range of real-world settings,
from simpler tasks such as Countdown to more challenging
benchmarks in mathematical reasoning tasks. We consis-
tently observe that DS-GRPO improves both Pass@1 and
Pass@K relative to the vanilla baseline; on the Mistral-
8B model, DS-GRPO outperforms the baseline by up to
11.4% (Pass@64 on AIME25). We further compare against
prior heuristics, including entropy regularization and recent
diversity-prompting techniques (He et al., 2025a; Chen et al.,
2025b; Walder & Karkhanis, 2026). While these baselines
yield improvements only in certain settings, DS-GRPO de-
livers robust gains across most datasets and models tested.
Thus, DS-GRPO represents a principled approach that not
only improves upon vanilla RL but also provides consis-
tently stronger results than existing heuristics.

Finally, our analysis clarifies the contradictory effects of
global entropy regularization in prior work. Increasing en-
tropy across all trajectories improves diversity but reduces
correctness, which can help on tasks with many valid solu-
tions. Conversely, decreasing entropy improves correctness
at the cost of diversity, which suits tasks with few valid

solutions. Our experiments confirm this principle, and we
further show that differential entropy control, increasing en-
tropy on correct trajectories while decreasing it on incorrect
ones—achieves the best of both, paralleling the effect of
differential smoothing.

Summary of Our Main Contribution

1. We analyze diversity collapse from first principles in
a formal setting.

2. Based on our diagnosis, we propose a novel differen-
tial smoothing algorithm that empirically improves
both Pass@1 and Pass@K and outperforms previous
methods in most of the real-world settings we tested.

3. We formally prove that our proposed differential
smoothing approach improves diversity and correct-
ness over the vanilla approach and the popular en-
tropy maximization heuristic.

4. The analysis in this work also has broader implica-
tions of clarifying when and why existing heuristics
work and guide the principled modifications of such
heuristics.

2. A theoretical perspective on the diversity
collapse in RL

In this section, we theoretically analyze the diversity col-
lapse phenomenon that arises during the RL fine-tuning of
LLMs where the fine-tuned model converges to a limited
set of solutions for a given problem, neglecting other valid
alternatives. (He et al., 2025a; Song et al., 2025a). This di-
versity collapse leads to a measurable degradation in metrics
such as Pass@K as RL progresses, and potentially stifles
the model’s creative problem-solving capabilities.

Our analysis proceeds as follows: We first introduce our the-
oretical abstraction of the RL fine-tuning process (Sec 2.1).
We then identify and analyze two primary factors that drive
diversity collapse (Sec 2.2). Finally, based on these insights,
we derive a principled reward function designed to miti-

2

## Page 3

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

gate this collapse and actively promote solution diversity
(Sec 2.2 and Sec 2.4).

2.1. Setup

Preliminaries. We model language generation as a token-
level Markov Decision Process (MDP). The environment is
defined by a state space S, a token vocabulary (action space)
A, and a maximum length H. An episode begins with an in-
put prompt x ∈X, which defines the initial state s1 = (x).
At each step h, the state sh = (x, a1, . . . , ah−1) ∈Sh cap-
tures the prompt and previously generated tokens. The
agent’s policy πh(·|sh) : Sh →∆(A) provides a dis-
tribution over the next token. State transitions are deter-
ministic: selecting action ah ∈A in state sh leads to
sh+1 = (x, a1, . . . , ah). A complete trajectory is τ =
(x, a1, . . . , aH), which receives a terminal reward r(τ). Let
C denote the set of all correct (successful) trajectories. We
assume a binary reward function r(τ) = 1\[τ ∈C\]. We use
an estimated reward function br, which is constructed as fol-
lows: Initially, br(τ) = 0 for all τ. A dataset of trajectories
is sampled from base policy πbase. A verifier then identifies
the subset of successful trajectories . The estimated rewards
for these trajectories are subsequently set to 1.

RL fine-tuning over a base policy. A base model (or a pre-
trained model) with corresponding policy πbase is fine-tuned
to optimize the following objective:

πvan(τ) = arg max
π
Eτ∼πbr(τ) −β · DKL(π||πbase),
(1)

where the KL-divergence term serves as a regularizer that
prevents the updated policy from deviating too much from
the base policy πbase and β is a hyperparameter that balances
the trade-off between maximizing reward and preserving
the knowledge of the base model. We denote this by πvan to
distinguish from proposed improvements in later sections.

2.2. Why does RL collapse diversity?

Ideally, RL fine-tuning should increase the likelihood of
all correct trajectories. In practice, however, the process
disproportionately reinforces correct trajectories that are al-
ready high-probability under the base LLM, a phenomenon
we refer to as diversity collapse. As a starting point for
mitigation, we first formally analyze why there is a diversity
collapse in the theoretical setup discussed above.

Analysis of Diversity Collapse

Proposition 1 (Selection bias). The probability that
a correct trajectory’s likelihood increases is monoton-
ically related to its initial probability under the base
model. Formally, for any two correct trajectories τ1, τ2

and β > 0, we have

πbase(τ1) ≥πbase(τ2)
=⇒

P(πvan(τ1) > πbase(τ1))
≥
P(πvan(τ2) > πbase(τ2)) .

Proposition 2 (Reinforcement bias). The magnitude of
probability gain for a given corect trajectory is directly
proportional to its probability under the base policy.
Formally, if the reward update mechanism has access to
the complete set of correct trajectories (br(τ) = 1 for all
correct trajectories), then for any correct trajectory τ
and β > 0, we have

πvan(τ) −πbase(τ) ∝πbase(τ).

Proposition 1 reveals a selection bias: among correct trajec-
tories, those with higher base probabilities are more likely
to be reinforced. In addition, Proposition 2 shows that there
is a reinforcement bias: these same high-probability correct
trajectories further receive disproportionately larger boosts,
further amplifying the model’s existing preferences and
sharpening the distribution. The proofs for Proposition 2
and Proposition 1 are provided in Appendix B.1. These
results are derived by directly calculating the expression for
the fine-tuned policy and analyzing its resulting probability
distribution across trajectories. Crucially, the analysis of
reinforcement and selection biases pertains specifically to
correct trajectories. Conversely, incorrect trajectories ex-
hibit an inverse dynamic: high-probability errors are subject
to stronger penalization. Consequently, the probability dis-
tribution over incorrect trajectories is flattened rather than
sharpened.

2.3. The correctness-diversity tradeoff

A reward function to mitigate diversity collapse.
To
counter diversity collapse, we modify the reward to discour-
age the reinforcement of high-probability trajectories. Since
Lemma 5 implies that π⋆(τ) ∝exp(br(τ)/β), we define the
modified reward ˜r(τ) = br(τ) −γent log πbase(τ), where
γent > 0 controls the strength of regularization. The addi-
tional entropy bonus encourages the policy to assign more
weight to trajectories that were less likely under the base
policy countering the selection and reinforcement biases.

While such a change is natural, and has been previously
proposed, we see that the gains of an entropy bonus are
not universal. In Section 3.7 (Fig 5), we test out the en-
tropy bonus objective and find that entropy bonus improves
performance on Countdown but hurts performance (and
underperforms standard GRPO) on MATH500.

Conversely, other works advocate for an entropy penalty i.e.
adding rather than subtracting γent log πbase(τ) rather than

3

## Page 4

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

an entropy bonus to improve performance (Gao et al., 2025;
Agarwal et al., 2026). We see that entropy penalty in fact im-
proves performance on MATH500, while underperforming
on Countdown.

This apparent contradictory benefits of both entropy
bonus and entropy penalty suggests the optimal strategy
is task-dependent. Intuitively, entropy bonus improves di-
versity but at the cost of correctness. Such a tradeoff has
also been reported with other methods such as increasing
temperature (Dang et al., 2025). On the other hand, entropy
penalty does the reverse and improves correctness but at the
cost of diversity. For tasks with high inherent diversity in
correct solutions, the gain in diversity offers a significant
benefit and an entropy bonus overall works out to be bene-
ficial; for tasks with low solution diversity, the increase in
diversity does not offer a benefit that outweighs a potential
decrease in correctness, and an entropy penalty ends up
being beneficial.

We can observe this more precisely by defining a Solution
Multiplicity metric, defined as the average number of unique
correct solutions per problem:

Solution Multiplicity(X) =
1
|X|
P
x∈X A(x),
(2)

where A(x) is the number of correct solutions for problem
x.

We experimentally test the performance of entropy
bonus/penalty on a few other datasets and find that entropy
bonus is more effective when Solution Multiplicity is high,
whereas an entropy penalty performs better when it is low
(Section 3.7).

Overall, entropy bonus addresses diversity collapse but at
the cost of correctness. Furthermore, both entropy max-
imization and minimization have been proposed as valid
modifications, but neither is universally optimal across all
tasks.

2.4. A differential approach to mitigating the tradeoff

The natural mitigation of diversity collapse—entropy
bonus—is not the perfect solution because it decreases cor-
rectness.

Is this tradeoff inherent, or is there a way to simultaneously
improve both the correctness and diversity?

We make a key observation: we only care about diversity
over correct (high reward) trajectories. Also, reinforce-
ment and selection biases pertains specifically to correct
trajectories. Hence, one must redefine the desired diversity
metric to focus exclusively on correct trajectories.

We formalize our definition in the simple theoretical frame-
work described previously in Section 2.1. We then describe

a new differential reward modification that assigns different
entropy terms to the positive and negative trajectories. Fi-
nally, we theoretically show that our proposed differential
loss mitigates the tradeoff between diversity (over high-
reward trajectories) and correctness.

Definition 3 (Correctness and Correct-Solution Diversity).
For any policy π, we define its correctness as C(π) =
P
τ∈C π(τ).
We use the normalized variance on cor-
rect trajectories to measure diversity over correct solu-
tions.
Namely, we define σ(π) = \[P

τ∈C π(τ)2|C| −
C(π)2/C(π)2.

A small normalized variance indicates that the probability
distribution is more uniform (i.e., less ”sharp”). In such a
distribution, the probability mass is not concentrated on a
few high-probability trajectories but is spread more evenly
across a wider set of solutions. This directly translates to
higher diversity, as a greater variety of trajectories are likely
to be sampled. Therefore, a policy with lower normalized
variance exhibits higher diversity. Based on this insight, we
consider the following differential reward modification:

rDS(τ) =

(
br(τ) −γDS · log(πbase(τ))
if br(τ) > 0
br(τ)
if br(τ) ≤0.
(3)
We then proceed to compare πDS that maximizes the reward
above, and πent that maximizes the standard entropy bonus
modification to improve diversity.

πent = arg maxπ Eτ∼π\[˜r(τ)\] −βent · DKL(π||πbase),

πDS = arg maxπ Eτ∼π \[rDS(τ)\] −βDS · DKL(π||πbase).

Here, βent and βDS denote the KL coefficients for the two RL
algorithms we are comparing, which use different reward
modifications. With the definitions above, we aim to show
that our differential reward modification performs better in
both correctness and diversity. To this end, we present the
following theoretical result:

Theoretical Benefit of Differential Reward

Theorem 4. Assume the model have correct estimation
for the reward of all trajectories. For any parameters
γent ≥0 and βent > 0 used in Eq. 1 (for πent) that satisfy
a proximity constraint Kρ(πent, πbase) ≤κ, there exist
parameters γDS ≥0 and βDS > 0 for πDS such that
it also satisfies Kρ(πDS, πbase) ≤κ, and the following
inequalities hold:

C(πDS) ≥C(πent)
and
σ(πDS) ≤σ(πent).

This result holds for Kρ(π, πbase) ∈{DKL(π∥πbase),
DKL(πbase∥π), Dχ2(π∥πbase), Dχ2(πbase∥π)}.

4

## Page 5

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

The KL-divergence constraint (Kρ(·, πbase) ≤κ) is a practi-
cal necessity and a standard assumption in prior work (Setlur
et al., 2025). It prevents the fine-tuned policy from devi-
ating excessively from the base model, thereby retaining
pre-trained knowledge and avoiding catastrophic forgetting.
Thus, Theorem 4 demonstrates that differential reward mod-
ification (for πDS) achieves superior correctness (C) and di-
versity (σ) while adhering to the same proximity constraints
as the global penalty method (for πent).

2.5. Differential Smoothing with Entropy Bonus and
Entropy Penalty

We proved that increasing entropy on correct trajectories
alone can mitigate the tradeoff with correctness. Addition-
ally, our analysis indicates that reducing the entropy (diver-
sity) of incorrect trajectories enhances model correctness
without detriment to the diversity of correct generations.
With this perspective, let’s revisit entropy penalty which we
saw improves performance on some tasks with low solution
diversity such as MATH500 but underperformed on tasks
with high solution diversity such Countdown. Interestingly,
theorem 4 interestingly holds even if we apply an entropy
penalty exclusively on negative trajectories. In other words,
an entropy penalty on negative trajectories does not impact
the policy’s diversity over correct responses and hence such
a modification could prevent

Motivated by this finding, as well as the empirical obser-
vation that entropy penalties can improve correctness (Gao
et al., 2025; Agarwal et al., 2026), we propose our final
method. We term this approach Differential Smoothing
(DS), which applies an entropy bonus exclusively to posi-
tive samples and an entropy penalty exclusively to negative
samples:

rDS(τ) =

(
br(τ) −γp · log(πbase(τ))
if br(τ) > 0
br(τ) + γn · log(πbase(τ))
if br(τ) ≤0,
(4)

where γp, γn ≥0 are hyperparameters. This formulation
generalizes the reward modification strategy in Equation (3).
In the following sections, we first detail the implementation
of differential smoothing in GRPO. We will then demon-
strate empirically that differential smoothing achieves a
significant advantage: it simultaneously increases both cor-
rectness (Pass@1) and diversity (Pass@K) across different
tasks, outperforming other methods that aim to improve
diversity.

3. Empirical evaluation of differential
smoothing GRPO

In this section, we empirically evaluate the effectiveness of
our proposed reward modification (Eq.4) in LLM reinforce-
ment finetuning.

We first recap the popular GRPO algorithm for LLM fine-

tuning with RL and present our adaptation, DS-GRPO that
incorporates the differential reward described in Section 2.5.
We then compare DS-GRPO with GRPO on Countdown
and mathematical reasoning. We further compare our pro-
posed method with other methods aimed at improving diver-
sity, including entropy-based approaches and other recently
proposed techniques. Our key finding is that DS-GRPO
consistently outperforms both GRPO and prior approaches
on most tasks. In contrast, previous methods only outper-
form baselines on a subset of tasks because they fail to
resolve the inherent tradeoff between correctness and diver-
sity. We further analyze entropy-based approaches (both
entropy bonus and entropy penalty) and show why their
gains are uneven and fundamentally limited. In contrast,
our differential reward formulation offers a principled way
to enhance diversity over correct trajectories, leading to
consistent improvements across the board.

3.1. Preliminaries: Group Relative Policy Optimization

We
adopt
Group
Relative
Policy
Optimization
(GRPO) (Shao et al., 2024) as our training backbone. For
each input x sampled from the training set, the policy
decodes a group of G completions {yi}G
i=1 ∼πθold(· | x),
where πθold denotes the behavior policy used to collect the
batch (the policy parameters at the previous update). Let
ri = r(yi) be the scalar reward of completion yi, and denote
by µ({rj}G
j=1) and σ({rj}G
j=1) the mean and standard devi-
ation of {rj}G
j=1, respectively. GRPO replaces the learned
critic with a group baseline and uses the group-standardized
advantage Ai = \[ri −µ({rj}G
j=1)\]/σ({rj}G
j=1). GRPO
adopts a clipped objective with a forward KL reg-
ularizer to the fixed base policy πb:
JGRPO(θ)
=
ExE{yi}G
i=1∼πθold(·|q)
 1

G
PG
i=1
1
|yi|
P|yi|
t=1 min

ρi,t(θ) Ai,
clip
 
ρi,t(θ), 1 −ϵ, 1 + ϵ

Ai
	
−
βKLDKL
 
πθ


 πb

where ρi,t(θ) =
πθ(yi,t|x,yi,<t)
πθold(yi,t|x,yi,<t) is the importance ratio.

3.2. Reward Modification for Mitigating Diversity
Collapse

To operationalize the theoretical principles from Section 2.4
within the GRPO framework, we propose Differential
Smoothing GRPO (DS-GRPO), a novel algorithm that re-
shapes the advantage function Ai (Eq. 3.2). This reshaping
directly implements our theoretical reward modification for
a detailed discussion). Specifically, for successful comple-
tions (where ri = 1), we subtract the term γp log πθold(yi |
x) from the advantage; conversely, for unsuccessful com-
pletions, we add the term γn log πθold(yi | x).

5

## Page 6

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Figure 2. Performance of DS-GRPO on the Countdown task, compared with GRPO under varying temperatures and KL coefficients.

Estimation of Entropy Discrepancy

ADS
i
= Ai +

(
−γp log πθold(yi | x),
if ri = 1,

+ γn log πθold(yi | x),
otherwise,

We plug the modified advantages ADS
i
into the GRPO
objective:

JGRPO(θ) = ExE{yi}G
i=1∼πθold(·|q)
 1

G
PG
i=1
1
|yi|
P|yi|
t=1
min

ρi,t(θ) ADS
i , clip
 
ρi,t(θ), 1 −ϵ, 1 + ϵ

ADS
i

−βKLDKL
 
πθ


 πb
.

In our theoretical framework, we employ πbase as the bonus
and penalty terms within the modified reward function. No-
tably, our analysis remains valid even if πbase is substituted
with π. However, for practical implementation, we empiri-
cally select πθold due to its superior stability. A detailed justi-
fication linking the theory to this practical choice is provided
in Appendix B.3. We evaluate DS-GRPO on the Countdown
and MATH reasoning benchmarks across a range of models.
As demonstrated in the subsequent sections, our method
consistently improves both correctness (Pass@1) and diver-
sity (Pass@K), outperforming existing diversity-promoting
approaches on most evaluation metrics.

3.3. Experimental Setup

We detail our experimental setup below, covering task spec-
ifications, model architectures, and hyperparameter configu-
rations.

Countdown. We evaluate the performance of DS-GRPO
on the arithmetic reasoning task Countdown, where 3 to 4
integers in \[1, 99\] are provided and the goal is to produce
an equation that equals a target number using all given
integers exactly once. Following Pan et al. (2025), we use
the Qwen2.5-3B-Instruct(Hui et al., 2024) as the backbone
model. For DS-GRPO, we set γp = 0.03, γn = 0.01. More
experiment details are given in Appendix C.1.

Math Reasoning. We further explore DS-GRPO on the
task of math reasoning. We choose four models with varied

sizes and response lengths, Qwen2.5-Math-1.5B (Hui et al.,
2024), Qwen3-1.7B (Yang et al., 2025), Qwen2.5-Math-7B
(Hui et al., 2024) and Ministral-8B-Instruct (Jiang et al.,
2023). The three Qwen models are fine-tuned on 14,053
English questions filtered from the DAPO17k (Yu et al.,
2026) dataset (DAPO14k); Ministral-8B-Instruct is addition-
ally augmented with 12,000 questions from the MATH12k
dataset (Hendrycks et al., 2021). We train the Qwen mod-
els with batch size 32 and Ministral with batch size 128
until the training reward saturates, then evaluate on five
commonly used benchmarks of math reasoning: MATH500
(Hendrycks et al., 2021), OlympiadBench (He et al., 2024),
AMC23 (math ai, 2025), AIME24 (H4, 2025) and AIME25
(OpenCompass, 2025), using a rollout temperature of 1.0
during training and a validation temperature of 0.7. Follow-
ing DAPO (Yu et al., 2026), we adopt asymmetric clipping
for Qwen3-1.7B (high 0.25, low 0.20) and Ministral-8B
(high 0.22, low 0.20); Qwen2.5-Math models keep symmet-
ric clipping (0.20/0.20). We use DAPO’s length-dependent
loss aggregation across all models. Experimental details are
in App.C.3.

3.4. Comparison of DS-GRPO with Vanilla GRPO

As shown in Figure 2, DS-GRPO demonstrates remarkable
robustness. It consistently enhances Pass@K (for most K)
by ≈4% compared to vanilla GRPO. Crucially, these per-
formance gains are accompanied by a 4× inference speedup.
(See Appendix D for additional results).

Figure 3 extends our evaluation to three base models and five
mathematical reasoning benchmarks. Our strategy yields
substantial improvements, with Pass@1 gains of up to 1.1%
and Pass@64 gains of up to 11.4% (on AIME25); the largest
gains concentrate on the harder AIME 2024/2025 bench-
marks, while easier benchmarks (MATH500, Olympiad-
Bench) see smaller but mostly positive improvements (de-
tailed in Appendix E.1). This demonstrates our method’s
ability to improve RL reasoning while mitigating diver-
sity collapse. Furthermore, it delivers significant efficiency
gains: DS-GRPO matches the Pass@64 of vanilla GRPO
using only k = 16 samples—yielding a nearly 4× infer-
ence speedup—while simultaneously pushing the maximum

6

## Page 7

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Figure 3. Pass@K performance after reward modification, compared with vanilla GRPO. X-axis denotes K and y-axis denotes pass rates.

achievable Pass@K. This uniform uplift underscores our
approach’s efficacy in enhancing both exploration and diver-
sity.

3.5. Ablation Experiments on Hyperparameters

To demonstrate the robustness of our method, we further
evaluate performance across different hyperparameters, in-
cluding sampling temperature, the KL coefficient βKL, and
the reward modification coefficients γp and γn.

Temperature and KL Coefficient. We evaluate the sta-
bility of DS-GRPO across varying sampling temperatures
and KL coefficients (βKL). Our results demonstrate consis-
tent improvements over vanilla GRPO: DS-GRPO enhances
Pass@K (for all K) by ≈4% across the temperature range
and by ≈3.2% across different KL coefficients.

Reward Modification Coefficient To isolate the contribu-
tion of each component in our reward modification strat-
egy, we conduct an ablation study. We compare the full
DS-GRPO algorithm against two specialized variants: DS-
GRPO-Positive, which only modifies the advantage for cor-
rect trajectories, and DS-GRPO-Negative, which only modi-
fies the advantage for incorrect trajectories. Their respective
advantage modifications are defined as follows:

ADS+
i
= Ai −γp log πθold(yi | x),
if ri = 1,

ADS-
i
= Ai + γn log πθold(yi | x),
if ri ̸= 1.

The full DS-GRPO algorithm demonstrates superior perfor-
mance over both of its individual components (DS-GRPO-
Positive and DS-GRPO-Negative) for all K. Detailed results
and discussion are available in Section E.2. sharpening.

3.6. Comparison with Other Methods for Increasing
Diversity

We compare DS-GRPO with prior approaches that encour-
age diversity in reasoning through reward or advantage shap-
ing, either by optimizing Pass@K rate directly(Tang et al.,
2025; Walder & Karkhanis, 2026; Chen et al., 2025b) or
by applying rank-based penalties (He et al., 2025a). For
mathematical reasoning experiments, we use the Qwen2.5-
Math-7B(Hui et al., 2024) as the base model. For PKPO and
GR-PKPO, we use K = 4 which performs best in previous
work (Chen et al., 2025b); for rank-based panelty, we sweep

across various configurations. See more result details in
Appendix D.

Pass@K Optimization Methods. Methods that directly
optimize the Pass@K metric use it as a reward signal (Tang
et al., 2025; Walder & Karkhanis, 2026; Chen et al., 2025b).
However, this approach can assign zero reward to correct
solutions, which increases gradient variance and harms train-
ing stability. Experimentally, these methods often trade
correctness for diversity; for instance, GR-PKPO slightly
improves Pass@64 at the cost of Pass@1 and is unstable
on the Countdown task (Figure 4). In contrast, DS-GRPO
consistently improves Pass@K across all values of K.

Figure 4. Comparison with Other Methods

Comparison with Unlikeliness Reward Method. Our
work is conceptually similar to methods that reward unlikely
solutions, such as the one proposed by He et al. (2025a).
However, our approach has key advantages. DS-GRPO is
derived from a theoretical framework that guarantees its op-
timality. More critically, it employs a differentiated reward
strategy: it modifies rewards for correct trajectories to boost
diversity, while a complementary modification for incorrect
trajectories improves correctness. In contrast, methods like
that of He et al. (2025a) focus solely on diversity, which
can harm correctness. Our experimental results (Figure 4)
validate this, showing DS-GRPO’s superior performance
across all values of K.

Comparison with Other RL Reasoning Methods. We fur-
ther compare our approach with a recently proposed method
that focuses on improving RL reasoning: CISPO (Chen
et al., 2025a). However, in our setup, empirical results
demonstrate that our method outperforms CISPO at most
K across all four mathematical reasoning datasets, with the
largest gains at large K. Detailed results are provided in
Appendix E.3.

7

## Page 8

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

3.7. Comparing Differential Approach to Entropy
Control Method

Entropy control is a widely adopted strategy for enhancing
the diversity and reasoning capabilities of large language
models. In Section 2.4, we have theoretically shown that
our differential control approach outperforms both base-
line methods and those based on direct entropy maximiza-
tion. This section presents an empirical comparison of our
method against these prior entropy control strategies. We
demonstrate that our method achieves superior performance
compared to both the vanilla GRPO baseline and GRPO
augmented with direct entropy maximization.

3.7.1. DS-GRPO OUTPERFORM ENTROPY BASED
METHOD

The role of entropy in RL fine-tuning is complex and sub-
ject to ongoing debate. While conventional methods employ
entropy regularization to prevent policy collapse (Schulman
et al., 2017), recent studies suggest that explicitly minimiz-
ing entropy can, counter-intuitively, boost performance in
certain scenarios (Agarwal et al., 2026; Wang et al.). To
position our method within this context, we compare it
against two direct entropy control baselines: one that adds
an entropy bonus to encourage exploration, and one that
applies an entropy penalty to encourage exploitation. The
respective optimization objectives are:

Entropy Based Method

Jent+ = JGRPO(θ) −η+
P

y πθ(y|x) log(πθ(y|x)),

Jent−= JGRPO(θ) + η−
P

y πθ(y|x) log(πθ(y|x)),

As illustrated in Fig. 5, our method consistently outperforms
both the entropy bonus and penalty approaches, regardless
of the direction of the regularization. This suggests that a
simple, global adjustment to entropy is less effective than
our differentiated reward strategy.

Figure 5. Comparison with Entropy Control Method

3.7.2. DEEPER DISCUSSION ON ENTROPY CONTROL

Our experiments (Fig. 5) reveal a critical insight: the effec-
tiveness of global entropy control is highly task-dependent.
Specifically, an entropy bonus improves performance over

vanilla GRPO on the Countdown task (at large K) but hin-
ders it on math reasoning benchmarks. Conversely, an en-
tropy penalty benefits math reasoning while degrading per-
formance on Countdown. Can we explain these differing
trends?

A Principle for Task-Aware Entropy Control. Our theo-
retical analysis in Section 2.4 reveals a fundamental conflict:
global entropy bonuses improve diversity but degrade cor-
rectness, while penalties enhance precision but reduce vari-
ety. Therefore, effective entropy control must be task-aware:
aligning the regularization direction (bonus vs. penalty)
with the specific diversity-accuracy demands of the down-
stream application.

To quantify task-specific diversity requirements, we define
Solution Multiplicity (Eq. 2). We assess this metric across
four tasks and correlate it with Pass@8 variations induced
by entropy bonuses (Table 1; see Appendix C.4). We find
that for tasks with abundant unique solutions, the gains from
diversity outweigh the trade-off in individual correctness.
This motivates our task-aware control principle: employ an
entropy bonus for tasks with high Solution Multiplicity, and
an entropy penalty for those with low Solution Multiplicity.

Differential Control for Correct and Incorrect Trajecto-
ries. The underlying mechanism of DS-GRPO is similar to
a form of differentiated entropy control.

Differential Entropy Control

An objective function representing this principle can be
formulated as:
JDS−En =JGRPO −ηp
P

y:r(y)>0 πθ(y|x) log πθ(τ|x)

+ ηn
P

y:r(y)≤0 πθ(y|x) log πθ(y|x).

By selectively increasing entropy only for positive samples,
we attain the full diversity benefits of traditional entropy reg-
ularization, as we are only concerned with diversity among
correct solutions. Concurrently, decreasing entropy for neg-
ative samples reinforces correctness. This targeted approach
enables simultaneous gains in both correctness (Pass@1)
and diversity (Pass@K), offering a more robust and prin-
cipled method for model fine-tuning across different tasks.
The experimental results for differential entropy control is
presented in Appendix F.2

4. Related Work

Reinforcement fine-tuning for LLMs is a nuanced process
that involves several widely studied ingredients, including
surrogate objectives (Tang et al., 2025; Tajwar et al., 2026),
policy-gradient baselines (Ahmadian et al., 2024; Li et al.,
2023; Zeng et al., 2025), entropy mechanisms (Agarwal
et al., 2026; Gao et al., 2025) and so on. While RLVR

8

## Page 9

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

effectively enhances reasoning, it frequently induces diver-
sity collapse, degrading generation quality at large sam-
ple sizes (Dang et al., 2025; Chen et al., 2026b). Existing
countermeasures, ranging from algorithmic adjustments to
diversity-aware reward designs (Yu et al., 2026; Walder &
Karkhanis, 2026; He et al., 2025a), often force a trade-off
between diversity and correctness. Furthermore, the optimal
strategy for entropy regulation remains debated: some advo-
cate for maximization to aid exploration (He et al., 2025b),
while others observe benefits from minimization (Agarwal
et al., 2026). Unlike these uniform strategies, we propose a
conditional approach—incentivizing entropy for correct tra-
jectories while suppressing it for incorrect ones. We provide
a detailed discussion of these related works in Appendix B.

5. Conclusion

In this work, we conduct a formal, first-principles analysis
of diversity collapse, from which we derive a novel method
to enhance policy diversity. We empirically demonstrate
that our method outperforms existing approaches and theo-
retically prove its optimality. Our analysis also clarifies the
nuanced, task-dependent role of entropy in fine-tuning, lead-
ing to a principled control strategy that simultaneously im-
proves both correctness (Pass@1) and diversity (Pass@K).
A formal theoretical analysis of our entropy principle and
the nuanced effects of entropy it reveals is left as a promising
direction for future research.

Impact Statement

This paper presents work whose goal is to advance the field
of machine learning. There are many potential societal
consequences of our work, none of which we feel must be
specifically highlighted here.

References

Agarwal, S., Zhang, Z., Yuan, L., Han, J., and Peng, H. The
unreasonable effectiveness of entropy minimization in llm
reasoning. Advances in Neural Information Processing
Systems, 38:107150–107180, 2026.

Ahmadian, A., Cremer, C., Gall´e, M., Fadaee, M., Kreutzer,
J., Pietquin, O., ¨Ust¨un, A., and Hooker, S. Back to basics:
Revisiting reinforce-style optimization for learning from
human feedback in llms. In Proceedings of the 62nd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pp. 12248–12267,
2024.

Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., Das-
Sarma, N., Drain, D., Fort, S., Ganguli, D., Henighan, T.,
et al. Training a helpful and harmless assistant with rein-

forcement learning from human feedback. arXiv preprint
arXiv:2204.05862, 2022.

Chen, A., Li, A., Gong, B., Jiang, B., Fei, B., Yang, B.,
Shan, B., Yu, C., Wang, C., Zhu, C., et al. Minimax-
m1: Scaling test-time compute efficiently with lightning
attention. arXiv preprint arXiv:2506.13585, 2025a.

Chen, F., Raventos, A., Cheng, N., Ganguli, S., and Druck-
mann, S. Rethinking fine-tuning when scaling test-time
compute: Limiting confidence improves mathematical
reasoning. Advances in Neural Information Processing
Systems, 38:158785–158818, 2026a.

Chen, Z., Qin, X., Wu, Y., Ling, Y., Ye, Q., Zhao, W. X.,
and Shi, G. Pass@ k training for adaptively balancing
exploration and exploitation of large reasoning models.
arXiv preprint arXiv:2508.10751, 2025b.

Chen, Z., Lu, R., Zhao, A., Wang, Z., Yue, Y., Song, S.,
and Huang, G. Does reinforcement learning really incen-
tivize reasoning capacity in llms beyond the base model?
Advances in Neural Information Processing Systems, 38:
57654–57689, 2026b.

Cheng, D., Huang, S., Zhu, X., Dai, B., Zhao, X., Zhang,
Z., and Wei, F. Reasoning with exploration: An entropy
perspective.
In Proceedings of the AAAI Conference
on Artificial Intelligence, volume 40, pp. 30377–30385,
2026.

Chow, Y., Tennenholtz, G., Gur, I., Zhuang, V., Dai, B.,
Kumar, A., Agarwal, R., Thiagarajan, S., Boutilier, C.,
and Faust, A. Inference-aware fine-tuning for best-of-
n sampling in large language models. In International
Conference on Learning Representations, volume 2025,
pp. 78936–78959, 2025.

Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H.,
Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano,
R., et al. Training verifiers to solve math word problems.
arXiv preprint arXiv:2110.14168, 2021.

Cui, G., Zhang, Y., Chen, J., Yuan, L., Wang, Z., Zuo, Y., Li,
H., Fan, Y., Chen, H., Chen, W., et al. The entropy mech-
anism of reinforcement learning for reasoning language
models. arXiv preprint arXiv:2505.22617, 2025.

Dang, X., Baek, C., Wen, K., Kolter, Z., and Raghunathan,
A. Weight ensembling improves reasoning in language
models. arXiv preprint arXiv:2504.10478, 2025.

Gao, Z., Chen, L., Luo, H., Zhou, J., and Dai, B. One-shot
entropy minimization. arXiv preprint arXiv:2505.20282,
2025.

9

## Page 10

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., Zhu,
Q., Xu, R., Zhang, R., Ma, S., Bi, X., et al. Deepseek-
r1 incentivizes reasoning in llms through reinforcement
learning. Nature, 645(8081):633–638, 2025.

H4,
H. F.
AIME 2024 Dataset (Hugging Face).
https://huggingface.co/datasets/
HuggingFaceH4/aime_2024, 2025.
Accessed:
2025-09-18.

He, A. W., Fried, D., and Welleck, S. Rewarding the un-
likely: Lifting grpo beyond distribution sharpening. In
Proceedings of the 2025 Conference on Empirical Meth-
ods in Natural Language Processing, pp. 25559–25571,
2025a.

He, C., Luo, R., Bai, Y., Hu, S., Thai, Z., Shen, J., Hu, J.,
Han, X., Huang, Y., Zhang, Y., et al. Olympiadbench: A
challenging benchmark for promoting agi with olympiad-
level bilingual multimodal scientific problems. In Pro-
ceedings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers),
pp. 3828–3850, 2024.

He, J., Liu, J., Liu, C. Y., Yan, R., Wang, C., Cheng, P.,
Zhang, X., Zhang, F., Xu, J., Shen, W., et al.
Sky-
work open reasoner 1 technical report. arXiv preprint
arXiv:2505.22312, 2025b.

Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart,
S., Tang, E., Song, D., and Steinhardt, J. Measuring math-
ematical problem solving with the math dataset. arXiv
preprint arXiv:2103.03874, 2021.

Hochlehnert, A., Bhatnagar, H., Udandarao, V., Albanie, S.,
Prabhu, A., and Bethge, M. A sober look at progress in
language model reasoning: Pitfalls and paths to repro-
ducibility. arXiv preprint arXiv:2504.07086, 2025.

Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang,
S., Wang, L., Chen, W., et al. Lora: Low-rank adaptation
of large language models. Iclr, 1(2):3, 2022.

Huang, A., Block, A., Foster, D., Rohatgi, D., Zhang, C.,
Simchowitz, M., Ash, J., and Krishnamurthy, A. Self-
improvement in language models: The sharpening mech-
anism. In International Conference on Learning Repre-
sentations, volume 2025, pp. 76687–76739, 2025.

Hui, B., Yang, J., Cui, Z., Yang, J., Liu, D., Zhang, L.,
Liu, T., Zhang, J., Yu, B., Lu, K., et al. Qwen2. 5-coder
technical report. arXiv preprint arXiv:2409.12186, 2024.

Jaech, A., Kalai, A., Lerer, A., Richardson, A., El-Kishky,
A., Low, A., Helyar, A., Madry, A., Beutel, A., Car-
ney, A., et al. Openai o1 system card. arXiv preprint
arXiv:2412.16720, 2024.

Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C.,
Chaplot, D. S., de Las Casas, D., Bressand, F., Lengyel,
G., Lample, G., Saulnier, L., Lavaud, L. R., Lachaux, M.-
A., Stock, P., Scao, T. L., Lavril, T., Wang, T., Lacroix,
T., and Sayed, W. E. Mistral 7b. ArXiv, abs/2310.06825,
2023.
URL https://api.semanticscholar.
org/CorpusID:263830494.

Li, Z., Xu, T., Zhang, Y., Lin, Z., Yu, Y., Sun, R., and Luo,
Z.-Q. Remax: A simple, effective, and efficient reinforce-
ment learning method for aligning large language models.
arXiv preprint arXiv:2310.10505, 2023.

math ai. AMC23 Dataset (Hugging Face). https://
huggingface.co/datasets/math-ai/amc23,
2025. Accessed: 2025-09-18.

OpenCompass.
AIME 2025 Dataset (Hugging Face).
https://huggingface.co/datasets/
opencompass/AIME2025,
2025.
Accessed:
2025-09-18.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C.,
Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A.,
et al. Training language models to follow instructions
with human feedback. Advances in neural information
processing systems, 35:27730–27744, 2022.

Pan, J., Zhang, J., Wang, X., Yuan, L., Peng, H., and Suhr, A.
Tinyzero. https://github.com/Jiayi-Pan/TinyZero, 2025.
Accessed: 2025-01-24.

Pang, J.-C., Wang, P., Li, K., Chen, X.-H., Xu, J., Zhang,
Z., and Yu, Y. Language model self-improvement by
reinforcement learning contemplation. arXiv preprint
arXiv:2305.14483, 2023.

Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and
Klimov, O. Proximal policy optimization algorithms.
arXiv preprint arXiv:1707.06347, 2017.

Setlur, A., Rajaraman, N., Levine, S., and Kumar, A. Scaling
test-time compute without verification or rl is suboptimal.
arXiv preprint arXiv:2502.12118, 2025.

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang,
H., Zhang, M., Li, Y., Wu, Y., et al. Deepseekmath: Push-
ing the limits of mathematical reasoning in open language
models. arXiv preprint arXiv:2402.03300, 2024.

Song, Y., Kempe, J., and Munos, R.
Outcome-
based exploration for llm reasoning.
arXiv preprint
arXiv:2509.06941, 2025a.

Song, Y., Zhang, H., Eisenach, C., Kakade, S., Foster,
D., and Ghai, U. Mind the gap: Examining the self-
improvement capabilities of large language models. In
International Conference on Learning Representations,
volume 2025, pp. 39894–39931, 2025b.

10

### Page links

- [Link 1](https://api.semanticscholar.org/CorpusID:263830494)
- [Link 2](https://huggingface.co/datasets/HuggingFaceH4/aime_2024)
- [Link 3](https://huggingface.co/datasets/math-ai/amc23)
- [Link 4](https://huggingface.co/datasets/opencompass/AIME2025)

## Page 11

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Stojanovski, Z., Stanley, O., Sharratt, J., Jones, R., Adefioye,
A., Kaddour, J., and K¨opf, A. Reasoning gym: Reasoning
environments for reinforcement learning with verifiable
rewards. Advances in Neural Information Processing
Systems, 38, 2026.

Tajwar, F., Zeng, G., Zhou, Y., Song, Y., Arora, D., Jiang, Y.,
Schneider, J., Salakhutdinov, R., Feng, H., and Zanette,
A. Maximum likelihood reinforcement learning. arXiv
preprint arXiv:2602.02710, 2026.

Tang, Y., Zheng, K., Synnaeve, G., and Munos, R. Optimiz-
ing language models for inference time objectives using
reinforcement learning. arXiv preprint arXiv:2503.19595,
2025.

Walder, C. and Karkhanis, D. T. Pass@ k policy optimiza-
tion: Solving harder reinforcement learning problems.
Advances in Neural Information Processing Systems, 38:
152416–152445, 2026.

Wang, S., Yu, L., Gao, C., Zheng, C., Liu, S., Lu, R., Dang,
K., Chen, X.-H., Yang, J., Zhang, Z., et al. Beyond the
80/20 rule: High-entropy minority tokens drive effec-
tive reinforcement learning for llm reasoning. Advances
in Neural Information Processing Systems, 38:115452–
115486, 2026.

Wang, X., Tissue, H., Wang, L., Li, L., and Zeng, D. D.
Entropy scheduling in reinforcement learning for large
language models.

Wu, F., Xuan, W., Lu, X., Harchaoui, Z., and Choi, Y. The
invisible leash: Why rlvr may not escape its origin, 2025.
URL https://arxiv. org/abs/2507.14843.

Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B.,
Yu, B., Gao, C., Huang, C., Lv, C., et al. Qwen3 technical
report. arXiv preprint arXiv:2505.09388, 2025.

Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai,
W., Fan, T., Liu, G., Liu, L., et al. Dapo: An open-source
llm reinforcement learning system at scale. Advances
in Neural Information Processing Systems, 38:113222–
113244, 2026.

Zeng, G., Zhou, Z., Arora, D., and Zanette, A. Shrinking the
variance: Shrinkage baselines for reinforcement learning
with verifiable rewards. arXiv preprint arXiv:2511.03710,
2025.

Zhao, R., Meterez, A., Kakade, S., Pehlevan, C., Jelassi,
S., and Malach, E. Echo chamber: Rl post-training am-
plifies behaviors learned in pretraining. arXiv preprint
arXiv:2504.07912, 2025.

Zhu, X., Xia, M., Wei, Z., Chen, W.-L., Chen, D., and Meng,
Y. The surprising effectiveness of negative reinforcement

in llm reasoning. Advances in Neural Information Pro-
cessing Systems, 38:126546–126573, 2026.

11

## Page 12

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

A. Additional Related Work

Mitigating Diversity Collapse in RL for Reasoning. Reinforcement Learning with Verifiable Rewards (RLVR) has
become a dominant paradigm for enhancing reasoning capabilities in LLMs (Guo et al., 2025; Jaech et al., 2024). While
RLVR effectively “sharpens” the policy toward high-quality sequences (Huang et al., 2025; Pang et al., 2023), recent studies
indicate that it often induces diversity collapse (Dang et al., 2025; Chen et al., 2026b). This phenomenon manifests as
a degradation in Pass@k performance for large k, suggesting that the model’s generation distribution becomes overly
concentrated around a few solutions (Wu et al.).

Various strategies have been proposed to mitigate this issue. From an algorithmic perspective, Yu et al. (2026) introduce
a clip-higher strategy and remove KL divergence penalties in GRPO, while He et al. (2025b) utilize adaptive entropy
regularization. Zhu et al. (2026) observe that while positive samples sharpen the distribution, penalizing negative samples
helps preserve diversity. In terms of reward design, explicitly diversity-aware objectives have been explored, such as
optimizing directly for Pass@k (Walder & Karkhanis, 2026; Chen et al., 2025b), incorporating rank-based penalties (He
et al., 2025a), or adding entropy terms to advantage estimation (Cui et al., 2025). However, these methods often force a
trade-off: enhancing diversity (Pass@k) frequently comes at the expense of correctness (Pass@1) or stability. Unlike prior
works that apply global constraints, we propose a differential reward structure that fundamentally reconciles this trade-off.
While He et al. (2025a) also employ differential rewards, our approach demonstrates greater robustness across diverse tasks,
particularly in mathematical reasoning, by rigorously distinguishing between the entropy dynamics of correct and incorrect
trajectories.

Controlling Distribution Entropy in RLVR. Policy entropy serves as a key indicator of exploration capability (Cheng
et al., 2026). However, the optimal strategy for entropy regulation remains a subject of debate. One line of work advocates
for entropy maximization to encourage exploration, employing techniques such as entropy bonuses (Yu et al., 2026; He
et al., 2025b) or selective training on high-entropy tokens (Wang et al., 2026). Conversely, other studies report that entropy
minimization is essential for improving Pass@1 accuracy (Agarwal et al., 2026; Gao et al., 2025), or suggest scheduling
entropy reduction over the course of training (Wang et al.). These contradictory findings highlight the limitations of uniform
entropy control. Our work addresses this ambiguity by interpreting our method as a form of conditional entropy control. In
contrast to global maximization or minimization, we incentivize entropy for correct trajectories (to maintain diversity) while
penalizing it for incorrect ones (to eliminate errors). We provide both theoretical and empirical evidence that this targeted
approach outperforms uniform strategies.

12

## Page 13

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

B. Proof of Theorems

B.1. Proof of Proposition 6 and Proposition 7

Lemma 5. The solution to the KL-regularized optimization problem:

π∗
βent = arg max
π
{Eτ∼πr(τ) −βent · DKL(π||πbase)}

has the following closed-form expression for a trajectory τ:

π∗
βent(τ) =

hQH
h=1 πbase,h(ah | sh)
i
exp

1
βent r(τ)


P

τ ′:s′
1=s
hQH
h=1 πbase,h(a′
h | s′
h)
i
exp

1
βent r(τ ′)
,

where the summation in the denominator is over all valid trajectories τ ′ starting from the initial state s.

Proof. The optimization problem can be written as finding a probability distribution π(τ) over trajectories that solves:

max
π

X

τ
π(τ)r(τ) −βent
X

τ
π(τ) ln
 π(τ)

πbase(τ)


,
subject to
X

τ
π(τ) = 1.

We introduce a Lagrange multiplier µ for the probability constraint and form the Lagrangian L(π, µ):

L(π, µ) =
X

τ
π(τ)r(τ) −βent
X

τ
π(τ) \[ln(π(τ)) −ln(πbase(τ))\] −µ

X

τ
π(τ) −1

!

.

To find the optimal policy, we take the partial derivative of L with respect to π(τ) and set it to zero:

∂L
∂π(τ) = r(τ) −βent


ln
 π(τ)

πbase(τ)


+ 1

−µ = 0.

Solving for π(τ), we obtain:

ln
 π(τ)

πbase(τ)


= r(τ)

βent
−1 −µ

βent

=⇒π(τ) = πbase(τ) exp
r(τ)

βent
−1 −µ

βent


= πbase(τ) exp
r(τ)

βent


exp

−1 −µ

βent


.

The term exp(−1 −µ/βent) is a constant determined by the normalization constraint P

τ ′ π(τ ′) = 1. Let the partition

function be Z = P

τ ′ πbase(τ ′) exp

r(τ ′)

βent


. The normalization constant must be 1/Z, which gives the solution:

π∗
βent(τ) =
πbase(τ) exp

1
βent r(τ)


Z
=
πbase(τ) exp

1
βent r(τ)


P

τ ′ πbase(τ ′) exp

1
βent r(τ ′)
.

By substituting the definitions πbase(τ) = QH
h=1 πbase,h(ah | sh), we arrive at the expression stated in the lemma. This
completes the proof.

Proposition 6 (Selection Bias). The probability that a correct trajectory’s likelihood increases is monotonically
related to its initial probability under the base model. Formally, for any two correct trajectories τ1, τ2 and βent > 0,
we have

πbase(τ1) ≥πbase(τ2)
=⇒
P(πvan(τ1) > πbase(τ1))
≥
P(πvan(τ2) > πbase(τ2)) .

13

## Page 14

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Proposition 7 (Reinforcement bias). The magnitude of probability gain for a given trajectory is directly proportional
to its probability under the base policy. Formally, if the reward update mechanism has access to the complete set of
correct trajectories (r(τ) = 1 for all correct trajectories), then for any trajectory τ and βent > 0, we have

πvan(τ) −πbase(τ) ∝πbase(τ).

Proof. Part 1: Monotonicity of Likelihood Improvement. Under the specified reward mechanism, a correct trajectory τ
receives a positive reward if it is not missed in all N independent samples. This occurs with probability 1−(1−πbase(τ))N. A
positive reward ensures that the likelihood of the trajectory increases after fine-tuning. Thus, the probability of improvement
is:

P(πvan(τ) > πbase(τ)) = 1 −(1 −πbase(τ))N.

This function is monotonically increasing with respect to πbase(τ) for πbase(τ) ∈\[0, 1\]. Therefore, if πbase(τ1) ≥πbase(τ2),
the first claim holds.

Part 2: Proportionality of Probability Gain. From the closed-form solution for the optimal policy (as derived in Lemma 5),
we have π∗
βent(τ) = πbase(τ) exp(r(τ)/βent)/Z, where Z is the partition function. The change in probability is:

π∗
βent(τ) −πbase(τ) = πbase(τ) exp(r(τ)/βent)

Z
−πbase(τ) = πbase(τ)
exp(r(τ)/βent) −Z

Z


.

The partition function Z = P

τ ′ πbase(τ ′) exp(r(τ ′)/βent) is a constant for a given policy πbase and reward function r. The
term in the brackets is therefore constant for all trajectories τ that share the same reward value (e.g., all correct trajectories).
Consequently, the probability gain is directly proportional to the initial probability πbase(τ).

B.2. Proof of Theorem 4

Lemma 8. The solution to the KL-regularized optimization problem with an entropy-based reward modification:

π∗
βent,γent = arg max
π
{Eτ∼π \[r(τ) −γent log(πbase(τ))\] −βent · DKL(π||πbase)}

is given by:

π∗
βent,γent(τ) =
\[πbase(τ)\]1−γent

βent exp

1
βent r(τ)


P

τ ′ \[πbase(τ ′)\]1−γent

βent exp

1
βent r(τ ′)
,

where the summation in the denominator is over all valid trajectories τ ′.

Proof. The objective function can be expanded as:

max
π

X

τ
π(τ) (r(τ) −γent log(πbase(τ))) −βent
X

τ
π(τ) ln
 π(τ)

πbase(τ)


,

subject to the constraint P
τ π(τ) = 1. We form the Lagrangian L(π, µ):

L(π, µ)

=
X

τ
π(τ) (r(τ) −γent log(πbase(τ))) −βent
X

τ
π(τ) (ln(π(τ)) −ln(πbase(τ))) −µ

X

τ
π(τ) −1

!

.

Setting the partial derivative with respect to π(τ) to zero yields:

∂L
∂π(τ) = r(τ) −γent log(πbase(τ)) −βent


ln
 π(τ)

πbase(τ)


+ 1

−µ = 0.

14

## Page 15

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Solving for π(τ):

ln
 π(τ)

πbase(τ)


= r(τ)

βent
−γent

βent
log(πbase(τ)) −1 −µ

βent

=⇒π(τ) = πbase(τ) exp
r(τ)

βent
−γent

βent
log(πbase(τ)) −1 −µ

βent



= πbase(τ) · (exp(log(πbase(τ))))−γent

βent · exp
r(τ)

βent


· exp

−1 −µ

βent



= \[πbase(τ)\]1−γent

βent exp
r(τ)

βent


exp

−1 −µ

βent


.

The term exp(−1 −µ/βent) is a normalization constant. By enforcing the constraint P

τ ′ π(τ ′) = 1, we find that this
constant is the reciprocal of the partition function Z = P

τ ′\[πbase(τ ′)\]1−γent

βent exp(r(τ ′)/βent). This gives the final solution
stated in the lemma.

Lemma 9. Consider the reward function rDS(τ) which modifies the reward based on trajectory correctness, defined by a set
of correct trajectories C:

rDS(τ) =

(
r(τ) −γDS log(πbase(τ))
if τ ∈C
r(τ)
if τ /∈C

The solution to the KL-regularized optimization problem πDS = arg maxπ{Eτ∼π\[rDS(τ)\] −βDS · DKL(π||πbase)} is given
by:

πDS(τ) = 1

Z ×






\[πbase(τ)\]1−γDS

βDS exp

1
βDS r(τ)

if τ ∈C

\[πbase(τ)\] · exp

1
βDS r(τ)

if τ /∈C

where Z is the partition function ensuring normalization.

Proof. The objective function is maximized subject to P

τ π(τ) = 1. The Lagrangian is:

L(π, µ) =
X

τ∈C
π(τ) (r(τ) −γDS log(πbase(τ))) +
X

τ /∈C
π(τ)r(τ)

−βDS
X

τ
π(τ) (ln(π(τ)) −ln(πbase(τ))) −µ

X

τ
π(τ) −1

!

.

We take the partial derivative with respect to π(τ) for each case and set it to zero.

For a correct trajectory, τ ∈C:

∂L
∂π(τ) = r(τ) −γDS log(πbase(τ)) −βDS


ln
 π(τ)

πbase(τ)


+ 1

−µ = 0.

Solving for π(τ) yields: π(τ) ∝\[πbase(τ)\]1−
γDS
βDS exp

r(τ)

βDS


.

For an incorrect trajectory, τ /∈C:

∂L
∂π(τ) = r(τ) −βDS ·

ln
 π(τ)

πbase(τ)


+ 1

−µ = 0.

Solving for π(τ) yields: π(τ) ∝\[πbase(τ)\] · exp

r(τ)

βent


.

Combining these results, the unnormalized solution ˜π(τ) is:

˜π(τ) =






\[πbase(τ)\]1−
γDS
βent exp

1
βent r(τ)

if τ ∈C

\[πbase(τ)\] · exp

1
βent r(τ)

if τ /∈C

15

## Page 16

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

The final solution πDS is obtained by normalizing ˜π(τ) with the partition function Z = P

τ ′ ˜π(τ ′), which gives the
expression stated in the lemma.

Lemma 10 (Correctness under Reverse KL Constraint). When Kρ(π, πbase) = DKL(πbase∥π), for any γent ≥
0, βent > 0 such that DKL(πbase∥πent) ≤κ, there exist γDS ≥0 and βDS > 0 such that DKL(πbase∥πDS) ≤κ and
C(πDS) ≥C(πent), and σ(πDS) ≥σ(πent).

Proof. To simplify the notation, we define the following sums over trajectory probabilities, where C is the set of correct
trajectories:

bx =
X

τ∈C
\[πbase(τ)\]1−x ,
Bx =
X

τ
\[πbase(τ)\]1−x ,
pc =
X

τ∈C
πbase(τ).

The proof proceeds in three steps: we first find a functional relationship between correctness C and the KL divergence for
each policy, and then compare them.

Step 1: Analyze the Entropy-Maximization Policy (πent). The correctness is the total probability mass on correct
trajectories:

C(πent) =
P

τ∈C \[πbase(τ)\]1−γent

βent exp(1/βent)
P

τ∈C \[πbase(τ)\]1−γent

βent exp(1/βent) + P

τ /∈C \[πbase(τ)\]1−γent

βent
=
b γent

βent e1/βent

b γent

βent e1/βent + (B γent

βent −b γent

βent ).

Solving for e1/βent gives:
e1/βent
=
B γent

βent
−b γent

βent
b γent

βent


C(πent)
1−C(πent)

.
The reverse KL divergence is DKL(πbase∥πent) =
P

τ πbase(τ) ln(πbase(τ)/πent(τ)). Substituting the policy definition:

DKL(πbase∥πent) = γent

βent

X

τ
πbase ln πbase −
1
βent

X

τ
πbase · r(τ) + ln

b γent

βent e1/βent + B γent

βent −b γent

βent



= γent

βent

X

τ
πbase ln πbase −pc

βent
+ ln

b γent

βent e1/βent

C(πent)

!

.

Substituting the expression for 1/βent leads to a relationship between divergence and correctness:

DKL(πbase∥πent) =γent

βent

X

τ
πbase ln πbase + pc ln b γent

βent + (1 −pc) ln(B γent

βent −b γent

βent )

−\[pc ln C(πent) + (1 −pc) ln(1 −C(πent))\] .

Step 2: Analyze Differential Policy (πDS). Similarly, the correctness is:

C(πDS) =
b γDS

βDS e1/βDS

b γDS

βDS e1/βDS + (1 −pc).

The reverse KL divergence, after a similar derivation, is:

DKL(πbase∥πDS) =γDS

βDS

X

τ∈C
πbase ln πbase + pc ln b γDS

βDS + (1 −pc) ln(1 −pc)

−\[pc ln C(πDS) + (1 −pc) ln(1 −C(πDS))\] .
(5)

Step 3: Compare the Policies. Our goal is to show that for any C(πent), we can choose parameters for our method to achieve
C(πDS) = C(πent) with a smaller or equal KL divergence. Let’s choose γDS = βDS

βent γent, and set C(πDS) = C(πent) = C.
Equivalently, we assume that
γDS
βDS
= γent

βent
= eγ.

16

## Page 17

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Then the KL divergence for our method becomes:

DKL(πbase∥πDS) = eγ
X

τ∈C
πbase ln πbase + pc ln bγent + (1 −pc) ln(1 −pc) −H(Cent),

where H(C) = −\[pc ln C + (1 −pc) ln(1 −C)\]. For the entropy method, the KL is:

DKL(πbase∥πent) = eγ
X

τ∈C
πbase ln πbase + eγ
X

τ /∈C
πbase ln πbase + pc ln beγ + (1 −pc) ln(Beγ −beγ) −H(Cent).

The difference is DKL(πbase∥πent) −DKL(ours) = eγ P

τ /∈C πbase ln πbase + (1 −pc) ln(Beγ −beγ) −(1 −pc) ln(1 −pc). By
Jensen’s inequality on the concave function ln(·):

X

τ /∈C

πbase(τ)

1 −pc
ln

\[πbase(τ)\]−eγ
≤ln

X

τ /∈C

πbase(τ)

1 −pc
\[πbase(τ)\]−eγ
!

= ln
Beγ −beγ

1 −pc



Multiplying by −(1 −pc) gives:

eγ
X

τ /∈C
πbase(τ) ln(πbase(τ)) ≥−(1 −pc) ln
Beγ −beγ

1 −pc


= −(1 −pc) \[ln(Beγ −beγ) −ln(1 −pc)\] .

Furthermore, assuming the ratio equality γDS

βDS = γent

βent = eγ, the policy πDS takes the form:

πDS(τ) = 1

Z






\[πbase(τ)\]1−eγ exp

1
βDS r(τ)

if τ ∈C,

\[πbase(τ)\] · exp

1
βDS r(τ)

if τ /∈C,

where Z is the partition function. Similarly, the entropy-regularized policy is given by:

π∗
ent(τ) =
\[πbase(τ)\]1−eγ exp

1
βent r(τ)


P

τ ′ \[πbase(τ ′)\]1−eγ exp

1
βent r(τ ′)
.

This yields the equivalence σ(πDS) = σ(πent), which concludes the proof.

Lemma 11 (Correctness under Forward KL Constraint). When Kρ(π, πbase) = DKL(π∥πbase), for any γent ≥
0, βent > 0 such that DKL(πent∥πbase) ≤κ, there exist γDS ≥0 and βDS > 0 such that DKL(πDS∥πbase) ≤κ and
C(πDS) ≥C(πent), and σ(πDS) ≥σ(πent).

Proof. The proof proceeds in three steps: we first find a functional relationship between correctness C and the KL divergence
for each policy, and then compare them.

Step 1: Analyze the Entropy-Maximization Policy (πent). The correctness of πent is the total probability mass on correct
trajectories:

C(πent) =
P

τ∈C \[πbase(τ)\]1−γent

βent exp(1/βent)
P

τ∈T \[πbase(τ)\]1−γent

βent exp(r(τ)/βent)
=
b γent

βent e1/βent

b γent

βent e1/βent + (B γent

βent −b γent

βent ).
(6)

Solving for e1/βent yields: e1/βent =
B γent

βent
−b γent

βent
b γent

βent


C(πent)
1−C(πent)

.

17

## Page 18

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

The reverse KL divergence DKL(πent∥πbase) can be expressed as a function of C(πent). Following the derivation previously,
we arrive at:

DKL(πent∥πbase) = −

γent
βent
b γent

βent

X

τ∈C
πbase(τ)1−γent

βent ln(πbase(τ)) · C(πent)

−

γent
βent
B γent

βent −b γent

βent

X

τ /∈C
πbase(τ)1−γent

βent ln(πbase(τ)) · (1 −C(πent))

+ (1 −C(πent)) ln

b γent

βent
B γent

βent −b γent

βent

!

−ln b γent

βent + H(C(πent)),

(7)

where H(C) = C ln C + (1 −C) ln(1 −C) is the binary entropy function.

Step 2: Analyze Differential Policy (πDS). Similarly, the correctness for our policy is given by:

C(πDS) =
b γDS

βDS e1/βDS

b γDS

βDS e1/βDS + (1 −pc).
(8)

The corresponding reverse KL divergence as a function of C(πDS) is:

DKL(πDS∥πbase) = −

γDS
βDS
b γDS

βDS

X

τ∈C
πbase(τ)1−
γDS
βDS ln(πbase(τ)) · C(πDS)

+ (1 −C(πDS)) ln

b γDS

βDS
1 −pc

!

−ln b γDS

βDS + H(C(πDS)).

(9)

Step 3: Compare the Policies. Our goal is to show that for any C(πent), we can choose parameters for our method to achieve
C(πDS) = C(πent) with a smaller or equal KL divergence. Let’s choose γDS = βDS

βent γent, and set C(πDS) = C(πent) = C.
Equivalently, we assume that
γDS
βDS
= γent

βent
= eγ.

Then the KL divergence for our method becomes: According to Jensen’s inequality, we have

eγ P

τ /∈C πbase(τ)1−eγ ln(πbase(τ))

Beγ −beγ
· (1 −C) ≤(1 −C) · ln
P

τ /∈C πbase(τ)

Beγ −beγ


= (1 −C) · ln
 1 −pC

Beγ −beγ



Then in this case we have

DKL(πent∥πbase) = −eγ · P

τ∈C πbase(τ)1−eγ ln(πbase(τ))

beγ
· C + (1 −C)

ln

beγ
Beγ −beγ


−ln beγ

+ C ln C + (1 −C) ln(1 −C) −eγ P

τ /∈C πbase(τ)1−eγ ln(πbase(τ))

1 −pC
· (1 −C)

≥−eγ P

τ∈C πbase(τ)1−eγ ln(πbase(τ))

beγ
· C + (1 −C)

ln

beγ
Beγ −beγ


−ln beγ

+ C ln C + (1 −C) ln(1 −C)

=DKL(πDS∥πbase)

Therefore, the difference is non-negative: DKL(πent∥πbase) −DKL(πDS∥πbase) ≥0. This means that for any given correctness
level C, our method (with γDS = γent · βDS

βent ) can achieve it with a lower or equal KL-divergence cost. Thus, if the entropy
method is constrained by DKL ≤κ, our method can achieve a correctness C(πDS) ≥C(πent) while also satisfying the
constraint.

Furthermore, assuming the ratio equality γDS

βDS = γent

βent = eγ, the policy πDS takes the form:

πDS(τ) = 1

Z






\[πbase(τ)\]1−eγ exp

1
βDS r(τ)

if τ ∈C,

\[πbase(τ)\] · exp

1
βDS r(τ)

if τ /∈C,

18

## Page 19

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

where Z is the partition function. Similarly, the entropy-regularized policy is given by:

π∗
ent(τ) =
\[πbase(τ)\]1−eγ exp

1
βent r(τ)


P

τ ′ \[πbase(τ ′)\]1−eγ exp

1
βent r(τ ′)
.

This yields the equivalence σ(πDS) = σ(πent), which concludes the proof.

Lemma 12 (Correctness under Reverse χ2 Constraint). When Kρ(π, πbase) = Dχ2(πbase∥π), for any γent ≥
0, βent > 0 such that DKL(πbase∥πent) ≤κ, there exist γDS ≥0 and βDS > 0 such that Dχ2(πbase∥πDS) ≤κ and
C(πDS) ≥C(πent), and σ(πDS) ≥σ(πent).

Step 1: Analyze the Entropy-Maximization Policy (πent). The correctness of πent is the total probability mass on correct
trajectories:

C(πent) =
P

τ∈C \[πbase(τ)\]1−γent

βent exp(1/βent)
P

τ∈T \[πbase(τ)\]1−γent

βent exp(r(τ)/βent)
=
b γent

βent e1/βent

b γent

βent e1/βent + (B γent

βent −b γent

βent ).
(10)

Solving for e1/βent yields: e1/βent =
B γent

βent
−b γent

βent
b γent

βent


C(πent)
1−C(πent)

.

The reverse χ2 divergence Dχ2(πbase∥πent) can be expressed as a function of C(πent). Following the derivation previously,
we arrive at:

Dχ2(πbase∥πent) =
X

τ
πbase(τ)
 πent(τ)

πbase(τ) −1
2
=
X

τ

(πent(τ))2

πbase(τ) −1

We insert the expression of πent into the divergence constraints and we can obtain that

Dχ2(πbase∥πent) = −1 + e
2
βent P

τ∈C πbase(τ)1−2 γent

βent + P

τ /∈C πbase(τ)1−2 γent

βent
h
B γent

βent −b γent

βent + b γent

βent e
1
βent
i2

We then insert Eq. 10 into the expression of divergence and we can obtain that

Dχ2(πbase∥πent) = −1 +
P

τ∈C πbase(τ)1−2 γent

βent

b2γent

βent
· C(πent)2 + (1 −C(πent))2
P

τ /∈C πbase(τ)1−2 γent

βent

B γent

βent −b γent

βent

2

Step 2: Analyze Differential Policy (πDS). Similarly, the correctness is:

C(πDS) =
b γDS

βDS e1/βDS

b γDS

βDS e1/βDS + (1 −pc).

The reverse χ2 divergence, after a similar derivation, is:

Dχ2(πbase∥πDS) = −1 +
P

τ∈C πbase(τ)1−2
γDS
βDS

b2γDS

βDS

· C(πDS)2 + (1 −C(πDS))2
P

τ /∈C πbase(τ)

(1 −pc)2

Step 3: Compare the Policies. Our goal is to show that for any C(πent), we can choose parameters for our method to achieve
C(πDS) ≥C(πent) with a smaller or equal χ2 divergence. Let’s choose γDS = βDS

βent γent, and set C(πDS) = C(πent) = C.
Equivalently, we assume that
γDS
βDS
= γent

βent
= eγ.

19

## Page 20

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

According to Cauchy Inequality:

"X

τ /∈C
πbase(τ)1−2eγ
#

·

"X

τ /∈C
πbase(τ)

#

≥

"X

τ /∈C
πbase(τ)1−eγ
#2

.

Thus, we have

Dχ2(πbase∥πent) = −1 +
P

τ∈C πbase(τ)1−2eγ

b2
eγ
· C(πent)2 + (1 −C(πent))2
P

τ /∈C πbase(τ)1−2eγ

(Beγ −beγ)2

≥−1 +
P

τ∈C πbase(τ)1−2eγ

b2
eγ
· C(πent)2 + (1 −C(πent))2
1
P
τ /∈C πbase(τ) = Dχ2(πbase∥πDS).

Therefore, the difference is non-negative: Dχ2(πbase∥πent) −Dχ2(πbase∥πDS) ≥0. This means that for any given correctness
level C, our method (with γDS = γent · βDS

βent ) can achieve it with a lower or equal KL-divergence cost. Thus, if both methods
is constrained by DKL(πbase∥πent) ≤κ and DKL(πbase∥πDS) ≤κ, our method can achieve a correctness C(πDS) ≥C(πent).
Furthermore, assuming the ratio equality γDS

βDS = γent

βent = eγ, the policy πDS takes the form:

πDS(τ) = 1

Z






\[πbase(τ)\]1−eγ exp

1
βDS r(τ)

if τ ∈C,

\[πbase(τ)\] · exp

1
βDS r(τ)

if τ /∈C,

where Z is the partition function. Similarly, the entropy-regularized policy is given by:

π∗
ent(τ) =
\[πbase(τ)\]1−eγ exp

1
βent r(τ)


P

τ ′ \[πbase(τ ′)\]1−eγ exp

1
βent r(τ ′)
.

This yields the equivalence σ(πDS) = σ(πent), which concludes the proof.

Lemma 13 (Correctness under Forward χ2 Constraint). When Kρ(π, πbase) = Dχ2(π∥πbase), for any γent ≥
0, βent > 0 such that Dχ2(πent∥πbase) ≤κ, there exist γDS ≥0 and βDS > 0 such that Dχ2(πDS∥πbase) ≤κ and
C(πDS) ≥C(πent), and σ(πDS) ≥σ(πent).

Proof. The proof proceeds in three steps: we first find a functional relationship between correctness C and the KL divergence
for each policy, and then compare them.

Step 1: Analyze the Entropy-Maximization Policy (πent). The correctness of πent is the total probability mass on correct
trajectories:

C(πent) =
P

τ∈C \[πbase(τ)\]1−γent

βent exp(1/βent)
P

τ∈T \[πbase(τ)\]1−γent

βent exp(r(τ)/βent)
=
b γent

βent e1/βent

b γent

βent e1/βent + (B γent

βent −b γent

βent ).
(11)

Solving for e1/βent yields: e1/βent =
B γent

βent
−b γent

βent
b γent

βent


C(πent)
1−C(πent)

.

The reverse χ2 divergence Dχ2(πent∥πbase) can be expressed as a function of C(πent). Following the derivation previously,
we arrive at:

Dχ2(πent∥πbase) = −1 +

"X

τ
πbase(τ)1−γent

βent exp
r(τ)

βent

#

·

"X

τ
πbase(τ)1+ γent

βent exp

−r(τ)

βent

#

=
1
C(πent)b γent

βent

X

τ∈C
πbase(τ)1+ γent

βent +
1
1 −C(πent)(B γent

βent −b γent

βent )
X

τ /∈C
πbase(τ)1−γent

βent

20

## Page 21

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Step 2: Analyze Differential Policy (πDS). Similarly, the correctness for our policy is given by:

C(πDS) =
b γDS

βDS e1/βDS

b γDS

βDS e1/βDS + (1 −pc).
(12)

The corresponding reverse χ2 divergence as a function of C(πDS) is:

Dχ2(πent∥πbase) =
1
C(πent)b γDS

βDS

X

τ∈C
πbase(τ)1+
γDS
βDS +
1
(1 −C(πent)) ((1 −pc))
X

τ /∈C
πbase(τ)1+ γn

βDS

Step 3: Compare the Policies. Our goal is to show that for any C(πent), we can choose parameters for our method to achieve
C(πDS) ≥C(πent) with a smaller or equal χ2 divergence. Let’s choose γDS = βDS

βent γent, and set C(πDS) = C(πent) = C.
Equivalently, we assume that
γDS
βDS
= γent

βent
= eγ.

. According to Cauchy Inequality:
"X

τ /∈C
πbase(τ)1+eγ
#

·

"X

τ /∈C
πbase(τ)1−eγ
#

≥

"X

τ /∈C
πbase(τ)

#2

.

Thus, we have

Dχ2(πent∥πbase) =
1
C(πent)beγ
X

τ∈C
πbase(τ)1+eγ +
1
1 −C(πent)(Beγ −beγ)
X

τ /∈C
πbase(τ)1−eγ

≥
1
C(πent)beγ
X

τ∈C
πbase(τ)1+eγ +
1
1 −C(πent)

X

τ /∈C
πbase(τ)

!2

= Dχ2(πent∥πbase)

Therefore, the difference is non-negative: Dχ2(πent∥πbase) −Dχ2(πDS∥πbase) ≥0. This means that for any given correctness
level C, our method (with γDS = γent · βDS

βent ) can achieve it with a lower or equal KL-divergence cost. Thus, if the entropy
method is constrained by Dχ2 ≤κ, our method can achieve a correctness C(πDS) ≥C(πent) while also satisfying the
constraint. Furthermore, assuming the ratio equality γDS

βDS = γent

βent = eγ, the policy πDS takes the form:

πDS(τ) = 1

Z






\[πbase(τ)\]1−eγ exp

1
βDS r(τ)

if τ ∈C,

\[πbase(τ)\] · exp

1
βDS r(τ)

if τ /∈C,

where Z is the partition function. Similarly, the entropy-regularized policy is given by:

π∗
ent(τ) =
\[πbase(τ)\]1−eγ exp

1
βent r(τ)


P

τ ′ \[πbase(τ ′)\]1−eγ exp

1
βent r(τ ′)
.

This yields the equivalence σ(πDS) = σ(πent), which concludes the proof.

Theorem 14. Assume the reward mechanism has access to all correct trajectories. For any parameters γent ≥0 and
βent > 0 used in the entropy-regularized policy πent that satisfy a proximity constraint Kρ(πent, πbase) ≤κ, there exist
parameters γDS ≥0 and βn,p > 0 for our proposed policy πDS such that it also satisfies Kρ(πDS, πbase) ≤κ, and the
following inequalities hold:

C(πDS) ≥C(πent)
and
σ(πDS) ≤σ(πent).

This result holds for divergence measures Kρ(π, πbase) including DKL(π∥πbase), DKL(πbase∥π), Dχ2(π∥πbase), and
Dχ2(πbase∥π).

Proof. According to Lemma 10, Lemma 11, Lemma 12, and Lemma 13, we obtain that Theorem 14 holds for Kρ(π, πbase) =
DKL(π∥πbase), DKL(πbase∥π), Dχ2(π∥πbase), Dχ2(πbase∥π). Thus, we finish the proof of the theorem.

21

## Page 22

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

B.3. Equivalence of Theoretical and Practical Reward Modifications

In this section, we clarify the relationship between our theoretical reward modification and its practical implementation.
Specifically, we demonstrate that subtracting a log π term from the reward is equivalent to subtracting a log πbase term, under
a re-parameterization of the optimization objective.

Consider the following theoretical reward modification, which uses the policy’s own probability π:

rπ
DS(τ) =

(
r(τ) −γp · log(π(τ))
if r(τ) > 0
(correct trajectories)
r(τ) + γn · log(π(τ))
if r(τ) ≤0
(incorrect trajectories).
(13)

We first define the theoretical optimization problem for parameters β, γn, γp:

πDS = arg max
π
Eτ∼π \[rπ
DS(τ)\] −β · DKL(π||πbase).
(14)

Now, consider an alternative formulation where the reward is modified using the base policy πbase:

rπbase
DS (τ) =

(
r(τ) −eγp · log(πbase(τ))
if r(τ) > 0
(correct trajectories)
r(τ) + eγn · log(πbase(τ))
if r(τ) ≤0
(incorrect trajectories).
(15)

We show that the solution πDS to the original problem Equation (14) is also the solution to the following practical objective,
which uses rπbase
DS :

πDS = arg max
π
Eτ∼π \[rπbase
DS (τ)\] −eβ · DKL(π||πbase).
(16)

This equivalence holds when the new parameters eβ, eγp, and eγn are set as follows:

eβ = β + γp,
eγp = γp,
eγn = γn(β + γp)

β + γn
.
(17)

Therefore, the theoretical analysis from Theorem 4 still holds when log π is substituted for log πbase. Furthermore, the policy
selection mechanism in Eq. 4 is equivalent to directly maximizing entropy via an added regularization term. In practice, we
find that using log πθold (i.e., the log-probability of a previous policy iteration) in the advantage function modification yields
empirically better performance than using log πbase (the log-probability of the base policy).

C. Experimental Details

In this section, we provide additional details for the experiments in Section 3.

C.1. Countdown Experiment

C.1.1. DATA

We use the dataset released by Pan et al. (2025), which contains 327,680 training samples and 1,024 test samples.1 An
example training prompt is shown below.

Countdown Task Example

A conversation between User and Assistant. The user asks a question, and the Assistant solves it.
The assistant first thinks about the reasoning process in the mind and then provides the user with
the answer.
User: Using the numbers \[5, 94, 9, 44\], create an equation that equals 93. You can use basic
arithmetic operations (+, -, *, /) and each number can only be used once. Show your work in
<think> </think> tags. And return the final answer in <answer> </answer> tags, for example

1https://huggingface.co/datasets/Jiayi-Pan/Countdown-Tasks-3to4

22

### Page links

- [Link 1](https://huggingface.co/datasets/Jiayi-Pan/Countdown-Tasks-3to4)

## Page 23

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

<answer> (1 + 2) / 3 </answer>.
Assistant: Let me solve this step by step.
<think>

Our implementation builds on the official repository of Pan et al. (2025)2 and a fork adapted for A100 training.3

C.1.2. TRAINING

We train with a global batch size of 128, with 5 rollouts per prompt, and use a mini-batch size of 64. The learning rate is
1 × 10−6, and the KL penalty coefficient is set to βKL = 1 × 10−3. The reward is 1 for correct responses, 0.1 for incorrect
yet properly formatted responses, and 0 for all others. The maximum response length is 8,192 tokens. We perform RL
fine-tuning of the Qwen2.5-3B-Instruct model (Hui et al., 2024) for 320 steps on 2 A100 GPUs.

Configuration for Qwen3-1.7B

Parameter
Value
Parameter
Value
Pretrained model
Qwen3-1.7B
Training set
DAPO14k
Prompts per batch
32
Generations/prompt
8
Gradient update/step
1
Max prompt length
1024
Max response length
4096
Learning rate
5 × 10−7

Clip ratio low
0.2
Clip ratio high
0.25
Training Steps
300
β
0.0
Entropy coefficient
0.0
γp
0.02
γn
0.02
Remove padding
Enabled
Rollout engine
vllm
Rollout temperature
1.0
Validation temperature
0.7
Device
4 x Nvidia-H100

Configuration for Qwen2.5-Math-1.5B

Parameter
Value
Parameter
Value
Pretrained Model
Qwen2.5-Math-1.5B
Training Set
DAPO14k
Prompts per batch
32
Generations/prompt
8
Gradient update/step
1
Max prompt length
1024
Max response length
2048
Learning rate
1 × 10−6

Clip ratio low
0.2
Clip ratio high
0.2
Training Steps
1000
β
0.0
Entropy coefficient
0.0
γp
0.05
γn
0.05
Remove padding
Enabled
Rollout engine
vllm
Rollout temperature
1.0
Validation temperature
0.7
Device
4 x Nvidia-L6000

For Qwen2.5-Math-7B model, we trained for three random seeds. During evaluation, we first generated 128 rollouts for each
question, then estimated Pass@1 to Pass@64 using the unbiased estimator of each metric respectively, following Walder &
Karkhanis (2026).

2https://github.com/Jiayi-Pan/TinyZero
3https://github.com/JerryWu-code/TinyZero

23

### Page links

- [Link 1](https://github.com/JerryWu-code/TinyZero)
- [Link 2](https://github.com/Jiayi-Pan/TinyZero)

## Page 24

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Configuration for Qwen2.5-Math-7B

Parameter
Value
Parameter
Value
Pretrained Model
Qwen2.5-Math-7B
Training Set
DAPO14k
Prompts per batch
32
Generations/prompt
8
Gradient update/step
1
Max prompt length
1024
Max response length
2048
Learning rate
1 × 10−6

Clip ratio low
0.2
Clip ratio high
0.2
Training Steps
500
β
0.0
Entropy coefficient
0.0
γp
0.05
γn
0.05
Remove padding
Enabled
Rollout engine
vllm
Rollout temperature
1.0
Validation temperature
0.7
Device
4 x Nvidia-A100

Configuration for Ministral-8B-Instruct

Parameter
Value
Parameter
Value
Pretrained model
Ministral-8B-Instruct
Training set
DAPO14k + MATH12k
Prompts per batch
128
Generations/prompt
8
Gradient update/step
4
Max prompt length
1024
Max response length
2048
Learning rate
3 × 10−7

Clip ratio low
0.2
Clip ratio high
0.22
Training steps
300
β
0.0
Entropy coefficient
0.0
γp
0.02
γn
0.02
Remove padding
Enabled
Rollout engine
vllm
Rollout temperature
1.0
Validation temperature
0.7
Device
4 x Nvidia-A100

C.2. Baseline Implementation

GR-PKPO. We attempted to train the model using the Pass@k metric directly as the reward signal for k ∈{2, 3, 4}.
However, this approach proved unstable across all configurations. The training process quickly collapsed, causing the model
to generate degenerate outputs and yielding performance substantially worse than the baseline. Consequently, these results
are omitted from our main comparisons. We hypothesize this instability may be attributed to the limited number of rollouts
(5) used during training.

Unlikeliness Reward Method. We compare against the rank-based penalty proposed by He et al. (2025a), which down-
weights the reward for high-probability solutions to encourage diversity. For a set of rollouts {yi}G
i=1, the modified reward
is:

runlikely(yi) = r(yi)

1 −βrank
G −rank(yi)

G


,

where rank(yi) is the rank of the solution yi based on its probability under the policy πold(· | x). We performed a
hyperparameter sweep for βrank ∈{0.05, 0.1, 0.15, 0.2, 0.25, 0.3} and found that βrank = 0.05 yielded the best Pass@64
performance. For values of βrank ≥0.15, the training became unstable and collapsed.

Entropy-Based Methods. For the entropy-based baselines, we augment GRPO with either an entropy bonus or penalty.
We swept the coefficients η+ and η−over the set {0.005, 0.01, 0.03, 0.05}. In Figure 5, we report the results for the
hyperparameter value that achieved the highest Pass@64 score. A comprehensive summary of all experimental runs is
available in Appendix D.

24

## Page 25

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

C.3. Math Reasoning Experiment

We first filter out 14,042 questions written in English from the DAPO dataset (Yu et al., 2026) (which we refer to
as DAPO14k).
We then conduct reinforcement fine-tuning on four models: Qwen2.5-Math-1.5B (Hui et al.,
2024), Qwen2.5-Math-7B (Hui et al., 2024), and Qwen3-1.7B (Yang et al., 2025) are trained on DAPO14k;
Ministral-8B-Instruct (Jiang et al., 2023) is trained on DAPO14k augmented with 11,998 questions from the
MATH12k dataset (Hendrycks et al., 2021). The detailed per-model training setups are shown in the tables above and below;
response examples are shown in the boxes below.

Mistral Instruction Response Example

\[INST\] Convert the point (0, 3) in rectangular coordinates to polar coordinates. Enter your answer
in the form (r, θ), where r > 0 and 0 ≤θ < 2π. Let’s think step by step and output the final answer
within \boxed{}. \[/INST\]
1. **Calculate the radius r:**

r =
p

02 + 32 =
√

0 + 9 =
√

9 = 3.

2. **Determine the angle θ:**

• The point (0, 3) is on the positive y-axis.

• The angle θ with the positive x-axis is given by:

θ = tan−1
3

0


.

• Since the point is on the positive y-axis, the angle is π
2 .

3. **Combine the results to get the polar coordinates:**

(3, π

2 )

Qwen2.5-Math-1.5B

<|im start|>system
Please reason step by step, and put your final answer within \boxed{}. <|im end|>
<|im start|>user
Cities A and B are 45 miles apart. Alicia lives in A and Beth lives in B. Alicia bikes towards B at
18 miles per hour. Leaving at the same time, Beth bikes toward A at 12 miles per hour. How many
miles from City A will they be when they meet? Let’s think step by step and output the final answer
within \boxed{}. <|im end|>
<|im start|>assistant
To determine where Alicia and Beth will meet, we need to find out how long it will take for them to
meet and then use that time to calculate the distance Alicia has traveled.

1. First, let’s calculate their combined speed. Since Alicia bikes at 18 miles per hour and Beth
bikes at 12 miles per hour, their combined speed is 18 + 12 = 30 miles per hour.

2. Since the distance between the two cities is 45 miles, the time it takes for them to meet is the
total distance divided by their combined speed. So, the time t it takes for them to meet is

t = 45

30 = 1.5 hours.

3. Now, we need to find out how far Alicia has traveled in 1.5 hours. Since Alicia bikes at 18 miles

25

## Page 26

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

per hour, the distance she travels in 1.5 hours is

18 × 1.5 = 27 miles.

So, Alicia and Beth will meet 27 miles from City A. The final answer is

27

<|im end|>

Configuration for Countdown Task

Parameter
Value
Parameter
Value
Pretrained model
Qwen2.5-3B-Instruct
Batch size
128
Generations/prompt
5
Mini-batch size
64
Max prompt length
2,048
Max response length
8,192
Learning rate
1 × 10−6
Training steps
320
Entropy coefficient
0.001
Clip ratio
0.2
γp
0.03
γn
0.01
Rollout engine
vllm
Rollout temperature
1
Validation temperature
1
Validation top-k
50
Validation top-p
0.7
Device
2 x A100

C.4. Experimental Details for Section 3.7

In this section, we present experimental details to substantiate the claim made in Section 3.7: namely, that the Solution Mul-
tiplicity Solution Multiplicity(X), the average number of unique solutions per problem instance, serves as an appropriate
metric for evaluating the benefits of encouraging policy entropy in a task. The tasks we consider are as follows:

• Math Reasoning: As described in Appendix C.3.

• Countdown: As described in Appendix C.1.

• Countdown-3: A variant of Countdown where we filter the dataset to retain only samples with three given numbers.

• Knights and Knaves: A classic logic puzzle in which the objective is to identify truth-tellers (knights) and liars
(knaves) from their statements. (Stojanovski et al., 2026). Below is an example question and correct response.

Knights-and-Knaves

Question:
A very special island is inhabited only by sages and fools. Sages always tell the truth, and fools always lie. You meet 6 inhabitants: Owen,
Liam, Evelyn, William, Sofia, and Emily. As Owen put it, ”William is a sage”. Liam was heard saying, ”William is a fool”. Evelyn noted, ”Sofia
is a fool and Evelyn is a sage”. ”if Owen is a sage then Sofia is a sage,” William mentioned. ”if Liam is a sage then Evelyn is a sage,” Sofia
claimed. Emily told you that if Emily is a sage then Liam is a fool. So who is a sage and who is a fool? (Format your answer like: ”Owen is a
sage/fool, Liam is a sage/fool, Evelyn is a sage/fool, William is a sage/fool, Sofia is a sage/fool, and Emily is a sage/fool”) Let’s think step by
step and output the final answer (should be a sentence) within \boxed{}.
Response:

• We need to consider two cases for Owen:

– Case 1: Owen is a sage. If Owen is a sage, then his statement is true. Therefore, William must be a sage.
– Case 2: Owen is a fool. If Owen is a fool, then his statement is false. Therefore, William must be a fool.

• Liam’s statement: “William is a fool.”

– Case 1: Liam is a sage. If Liam is a sage, then his statement is true. Therefore, William must be a fool.

26

## Page 27

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

– Case 2: Liam is a fool. If Liam is a fool, then his statement is false. Therefore, William must be a sage.

• William’s statement: “If Owen is a sage then Sofia is a sage.”
Since Sofia is a sage, William’s statement is true. Therefore, William must be a sage.

• Owen’s statement revisited: “William is a sage.”
Since William is a sage, Owen’s statement is true. Therefore, Owen must be a sage.

• Liam’s statement revisited: “William is a fool.”
Since William is a sage, Liam’s statement is false. Therefore, Liam must be a fool.

• Emily’s statement revisited: “If Emily is a sage then Liam is a fool.”
Since Emily is a sage (from earlier), according to her statement, Liam must be a fool. This confirms our previous determination.

• Owen’s initial statement: “William is a sage.”
Since Owen is a sage and William is a sage, Owen’s statement is true. This is consistent.

Therefore, summarizing:

• Owen is a sage.

• Liam is a fool.

• Evelyn’s statement was a contradiction, so Evelyn must be a fool.

• William is a sage.

• Sofia is a sage.

• Emily’s statement was consistent, so Emily must be a sage.

Owen is a sage, Liam is a fool, Evelyn is a fool, W illiam is a sage, Sofia is a sage, and Emily is a sage

To estimate Solution Multiplicity, we query the GPT-5-Think model on 200 randomly selected samples with the following
prompt:

Prompt for Querying Solution Multiplicity

User: You are an expert mathematics educator and problem solver. Analyze the given mathematical
problem and determine how many different solution approaches exist for it.
Please provide a comprehensive analysis that: 1. Identifies all distinct solution methods/approaches
2. Briefly explains what each approach involves 3. Counts the total number of different approaches
Mathematical Problem: problem
Please first explain what different solution approaches exist for this problem, then provide your final
answer in the format: ¡ways¿ \[number\] ¡/ways¿
For example, if a problem has exactly 2 different solution methods, your response should end with:
¡ways¿ 2 ¡/ways¿

Table 1. Illustration of Experimental Result

Task
Knights
Math
Count-3
Count
Solution Multiplicity
1.5
3.7
6.5
15.7
Pass@8 of GRPO
47.1
78.6
97.7
73.4
Pass@8 (GRPO + Ent)
38.1
72.6
98.7
76.8
Entropy Effect
-9.0%
-6.0%
+1.0%
+3.4%

Training details.
The training setups of Math reasoning and Countdown task are identical to the main experiments
as described in Appendix C.1 and C.3. For Countdown-3, we train the model for 160 steps. For GRPO with entropy
bonus, we use a bonus coefficient of η+ = 0.05. Other configurations are identical to those of the main experiment. For
Knights-and-Knaves, we RL fine-tune the Qwen2.5-7B-Instruct (Hui et al., 2024) model with LoRA adaptation (rank 256)
(Hu et al., 2022) for 100 steps. We use a learning rate of 4 × 10−5 and a batch size of 32, with 8 rollouts per sample.

27

## Page 28

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Result Analysis.
The experimental results, presented in Table 1, reveal a direct correlation between Solution Multiplicity
and the efficacy of entropy regularization. Specifically, as a task’s Solution Multiplicity increases, so does the performance
gain (Pass@8) of an entropy bonus over vanilla GRPO. This provides strong empirical support for our hypothesis: for
tasks with a larger solution space, the benefits of enhanced diversity outweigh the potential trade-offs in single-solution
correctness. These findings thus validate Solution Multiplicity as a practical metric for guiding the decision of whether to
increase or decrease entropy for a given task.

D. Additional Experimental Results for Countdown

In this section, we provide additional results for the Countdown task.

D.1. Additional Experiments for Entropy coefficient
To provide a more comprehensive comparison, we analyze the performance of the entropy-based baselines across their
full hyperparameter sweep. We compare DS-GRPO against GRPO with varying entropy bonus (η+) and penalty (η−)
coefficients, with the results illustrated in Figure 6 (Top). The figure clearly demonstrates that DS-GRPO consistently
outperforms the global entropy control methods across their entire range of tested hyperparameters for all values of K.

D.2. Effects of KL Coefficient and Other Factors

Figure 6 (Bottom Left) reports results with varying sampling temperatures for both DS-GRPO and GRPO. Under the same
temperature, DS-GRPO achieves consistently higher Pass@K.

Figure
6
(Bottom
Right)
presents
results
from
varying
the
unlikeliness
reward
coefficient
βrank
∈
{0.05, 0.1, 0.15, 0.2, 0.25, 0.3} (He et al., 2025a).
For βrank ≥0.15, training collapses and accuracy drops to 0,
so we omit those results.

28

## Page 29

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

1
2
4
8
16
32
64
Pass@K

45

50

55

60

65

70

75

80

Pass Rate (%)

Countdown: Entropy Bonus

DS-GRPO
Vanilla GRPO
GRPO with entropy bonus 
+ = 0.005

GRPO with entropy bonus 
+ = 0.01

GRPO with entropy bonus 
+ = 0.03

GRPO with entropy bonus 
+ = 0.05

1
2
4
8
16
32
64
Pass@K

45

50

55

60

65

70

75

80

Pass Rate (%)

Countdown: Entropy Penalty

DS-GRPO
Vanilla GRPO
GRPO with entropy penalty 
= 0.005

GRPO with entropy penalty 
= 0.01

GRPO with entropy penalty 
= 0.03

GRPO with entropy penalty 
= 0.05

1
2
4
8
16
32
64
Pass@K

60

65

70

75

80

85

Pass Rate (%)

Countdown: Temperature Sweep

T=0.5
T=0.75
T=1.0

T=1.25
T=1.5

DS-GRPO
GRPO

1
2
4
8
16
32
64
Pass@K

40

50

60

70

80

Pass Rate (%)

Countdown: DS-GRPO vs. Unlikeliness Reward

DS-GRPO
Vanilla GRPO
Unlikeliness Reward 
rank = 0.05
Unlikeliness Reward 
rank = 0.1

Figure 6. Additional results on the Countdown task comparing DS-GRPO with various baselines. Top: Pass@K performance of
DS-GRPO and GRPO under entropy bonus and entropy penalty. Bottom Left: Pass@K performance of DS-GRPO and GRPO across
different sampling temperatures. Bottom Right: Pass@K performance of DS-GRPO and the Unlikeliness Reward method with varying
coefficients.

E. Additional Experimental Results for Math Reasoning Experiment

E.1. Additional Experimental Results on DS-GRPO vs GRPO

Experimental Results. Figure 7, which contains the full results for Section 3.4, compares our proposed DS-GRPO against
the vanilla GRPO baseline across four different base models and five mathematical reasoning benchmarks. The results
demonstrate that DS-GRPO outperforms vanilla GRPO across most tested (model, dataset) pairs.

E.2. Additional Ablation Study for DS-GRPO

Ablation Study Implementation. To isolate the contribution of each component in our reward modification strategy, we
conduct an ablation study. We compare the full DS-GRPO algorithm against two specialized variants: DS-GRPO-Positive,

29

## Page 30

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Figure 7. Pass@K performance after reward modification, compared with vanilla GRPO. X-axis denotes K and y-axis denotes pass rates.
Trained on the DAPO(Yu et al., 2026) and the MATH(Hendrycks et al., 2021) Dataset.

which only modifies the advantage for correct trajectories, and DS-GRPO-Negative, which only modifies the advantage for
incorrect trajectories.

Their respective advantage modifications are defined as follows:

ADS+
i
= Ai −γp log πθold(yi | x),
if ri = 1,

ADS-
i
= Ai + γn log πθold(yi | x),
if ri ̸= 1.

The DS-GRPO-Positive variant applies only the modification to correct trajectories (ADS+
i
), leaving the advantage for
incorrect trajectories as the standard Ai. Conversely, the DS-GRPO-Negative variant applies only the modification to
incorrect trajectories (ADS-
i
), leaving the advantage for correct trajectories unchanged. Result Analysis. We present the
results of our ablation study in Figure 8. The key findings are as follows:

• DS-GRPO-Positive vs. Vanilla GRPO. As shown in Figure 8, DS-GRPO-Positive outperforms vanilla GRPO, particularly
for larger values of K. This demonstrates that modifying the reward for correct trajectories successfully mitigates the
sharpening effect, providing empirical support for our intuition in Section 2.4 that penalizing high-probability correct
solutions enhances diversity.

• DS-GRPO-Negative vs. Vanilla GRPO. The figure also shows that DS-GRPO-Negative consistently outperforms vanilla
GRPO across all values of K. This indicates that modifying the reward for incorrect trajectories is effective at improving

30

## Page 31

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Figure 8. Comparison of DS-GRPO with single-side ablations on AIME24 (Qwen2.5-Math-1.5B). Left: DS-GRPO-Negative only
(γp = 0, vary γn). Right: DS-GRPO-Positive only (γn = 0, vary γp). The combined DS-GRPO (blue/purple solid) dominates each
single-side variant at large K.

the model’s overall correctness.

• DS-GRPO vs. Its Components. The full DS-GRPO algorithm demonstrates superior performance over both of its
individual components (DS-GRPO-Positive and DS-GRPO-Negative) for all K. This highlights a clear synergy: the
”Positive” component drives diversity, while the ”Negative” component enhances correctness. Their combination in
DS-GRPO achieves the best balance, validating our complete reward modification strategy as outlined in Section 2.4.

31

## Page 32

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

E.3. Additional Experiment on Comparing DS-GRPO with CISPO

We compare DS-GRPO with CISPO (Chen et al., 2025a), as illustrated in Figure 9. The results demonstrate that DS-GRPO
achieves a higher Pass@K than CISPO at most K across all datasets, with the largest gains at large K. All experiments
were conducted using the Qwen2.5-Math-1.5B model.

Figure 9. Comparison on CISPO with DS-GRPO.

F. Supplementary Experiments and Analysis

F.1. Diversity Changes of DS-GRPO Comparing to Baseline Model

To provide stronger evidence that DS-GRPO truly mitigates entropy collapse, follow the convention of (Hochlehnert et al.,
2025). We plot the Pass@K difference between DS-GRPO with base model over K in the following figure. We can see that
the Pass@K difference between DS-GRPO with base model does not go down as K increases. This shows that DS-GRPO
truly mitigates diversity collapse. The figure is shown in Fig 10.

Figure 10. Pass@K change of GRPO and DS-GRPO.

F.2. Comparison of Differential Entropy Control with Other Entropy Based Methods

We extended our experiments to four mathematical reasoning datasets, comparing our method against Entropy Bonus,
Entropy Penalty, and vanilla GRPO. The results are shown in Figure 11, our proposed method outperforms competing
baselines in the vast majority of settings. The results highlight the performance gain of our Differential Entropy method over
vanilla GRPO and other entropy-based variants. Notably, our method exhibits consistent performance gains across varying
K, particularly demonstrating superior scaling capability at higher K values (e.g., K ≥4).

32

## Page 33

Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning

Figure 11. Differential entropy control vs entropy bonus, entropy penalty, and vanilla GRPO on four math benchmarks (OlympiadBench,
MATH500, AIME25, AIME24; Qwen2.5-Math-1.5B).

F.3. Statistical Analysis of DS-GRPO Improvements

We further quantify the performance gains of DS-GRPO compared to the GRPO baseline. The improvements, averaged
across the four base models, are detailed in Table 2. The largest gains concentrate on the more challenging AIME
benchmarks—particularly AIME 2025, where DS-GRPO improves Pass@64 by 9.4% on average. On the easier benchmarks
(MATH500, OlympiadBench) the gains are smaller but consistently positive across all K. On AMC 2023, the gain vanishes
at large K as both methods saturate near 100%.

Table 2. Average performance improvement of DS-GRPO over GRPO across different datasets. The values represent the percentage point
increase in Pass@K.

Dataset
P@1
P@2
P@4
P@8
P@16
P@32
P@64
MATH500
+0.9%
+0.9%
+0.8%
+0.7%
+0.7%
+0.8%
+0.9%
AIME 2024
-0.4%
-0.4%
+0.1%
+0.9%
+1.8%
+2.9%
+3.9%
AIME 2025
+0.3%
+0.6%
+1.2%
+2.2%
+4.0%
+6.4%
+9.4%
OlympiadBench
+0.5%
+0.4%
+0.4%
+0.5%
+0.6%
+0.8%
+1.0%
AMC 2023
+0.6%
+0.6%
+0.5%
+0.2%
-0.1%
-0.3%
-0.5%

33
