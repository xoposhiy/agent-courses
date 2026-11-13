# Lecture 3 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-03-long-context.pdf) · [Raw file](../../raw/slides/lecture-03-long-context.pdf)

Retrieved: 2026-11-13T16:45:21.175271+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Context Management for
Long-Context Agents

Graham Neubig

Language Technologies Institute

How agents keep working as their history grows

1

## Page 2

Agent context growth

2

## Page 3

Quadratic input from linear history growth

input  = fixed prefix + history before call t

Call 1
6K
6K cumulative

Call 2
11K
17K cumulative

Call 3
16K
33K cumulative

Call 4
21K
54K cumulative

Call 5
26K
80K cumulative

t

3

## Page 4

Agent prompt composition example

23%

System + tools

9%

User

9%

Reasoning
2%
20%

Tool calls

37%

Tool results

77,922 mean tokens per session across 1,500 OpenHands sessions

4

## Page 5

Two long-context challenges

Capacity

Can the model use the needed evidence?

Architecture, position encoding, and training shape
usable context; evaluation measures it.

Efficiency

Can the system afford to serve it?

Attention, KV memory, caching, and compaction
shape cost and latency.

5

## Page 6

LLM inference

6

## Page 7

Elements of the serving stack

Request

prompt +

controls
→

Scheduler

queue · batch ·

route
→

↓write
KV
cache

persistent per-request state ↕read + append

→

Response

streamed

tokens

Prefill

all prompt positions

Decode

one new position per step

↺

DistServe · Zhong et al., OSDI 2024 ↗
7

### Page links

- [Link 1](../optional-readings/arxiv-2401-09670.md)

## Page 8

Inference phases

model pass

tokens processed

KV state after pass

1 · Prefill

x₁
x₂
x₃
…
xₙ

K,V
K,V
K,V
…
K,V

→

2 · Decode

y₁

prompt KV
K,V

→

3 · Decode

y₂

prompt + y₁ KV
K,V

Prefill: compute-intensive; latency grows with prompt length
Decode: sequential and memory-bandwidth-intensive; one step per
output token

Prefill/decode execution model · DistServe, OSDI 2024 ↗
8

### Page links

- [Link 1](../optional-readings/arxiv-2401-09670.md)

## Page 9

Serving metrics

request arrives
first token
token 2
token 3
token 4

Throughput
completed tokens or requests ÷ wall-clock time
Cost
input + cached input + output token charges

prefill

TTFT
arrival → first token

TPOT
gap between output

tokens

TTFT and TPOT phase decomposition · DistServe, OSDI 2024 ↗
9

### Page links

- [Link 1](../optional-readings/arxiv-2401-09670.md)

## Page 10

Refresher: attention

Linear projections

Causal self-attention

Notation: X ∈ ℝⁿˣᵈ has token-state row zₜ; lowercase qᵢ, kⱼ, vⱼ denote rows of Q, K, V; dₖ is key width; Mᵢⱼ = 0 for j ≤ i and −∞ otherwise.

Q = XW
​,
K =
Q
XW
​,
V =
K
XW
​
V

A = softmax
​
,
O =
(

​
d

​k

QK
+ M
⊤

)
AV

Visible history
Future masked

Keys

Queries

10

## Page 11

Advertised vs. effective context

GPT-4 needle-in-a-haystack evaluation · Kamradt, 2023 ↗
11

### Page links

- [Link 1](../optional-readings/ref-17f8e83fab7b.md)

## Page 12

Architectures for long context

12

## Page 13

Standard attention is global

Typically, attention makes pairwise comparisons across the entire sequence.

Visible history
Future masked

Keys

Queries

13

## Page 14

Local modeling

Local computation only considers a constant subset of the other data.

Pairwise-comparison cost

w is the local window size; for constant w, work is linear in n.

O(n )  ⟶ 
2
O(wn)

14

## Page 15

Periodic global access in hybrid models

Local 1

cheap state update

Local 2

cheap state update

Local N

cheap state update

N × local computation → 1 × global computation → repeat

Global

retrieve from full history

15

## Page 16

Long-context hybrid architectures

Model
Local / stateful calculation
Global calculation
Local : global

Qwen3.8-Flash-Next
Gated DeltaNet
QSA sparse retrieval
36 : 12 ≈ 3:1

GLM-5.3-Flash
Kimi Delta Attention
DSA + IndexPool
34 : 11 ≈ 3:1

Kimi K3
Kimi Delta Attention
dense Gated MLA
69 : 24 ≈ 3:1

Nemotron 3 Ultra
Mamba-2
dense GQA
48 : 12 = 4:1

Inkling-Small
512-token window
dense GQA
35 : 7 = 5:1

DeepSeek-V4-Pro-0813
128-token window branch
compressed sparse / dense
interleaved branches

Qwen ↗
GLM ↗
Kimi ↗
Nemotron ↗
Inkling ↗
DeepSeek ↗
16

### Page links

- [Link 1](../optional-readings/arxiv-2607-24653.md)
- [Link 2](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)
- [Link 3](../optional-readings/ref-5302786105ea.md)
- [Link 4](../optional-readings/qwen3-8-flash-next-rendered.md)
- [Link 5](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-White-Paper.pdf)
- [Link 6](../optional-readings/ref-8c3acf43834d.md)

## Page 17

Four recurring mechanisms

Sliding-window attention

Linear attention or recurrent models

Sparse attention

KV compression

17

## Page 18

Sliding-window attention

Causal window mask

Using the same attention equation, work falls from O(n²) to O(nw).

A local layer cannot directly retrieve distant tokens.

New variable: w is the number of causal positions retained by each query.

Visible local
history

Outside window /
future

Keys

Queries

M
​ =
ij

(w)

​
​
{0,

−∞,

0 ≤i −j < w
otherwise

Longformer · Beltagy et al., 2020 ↗
18

### Page links

- [Link 1](../optional-readings/arxiv-2004-05150.md)

## Page 19

Softmax attention

1

Softmax

2

Linear

3

DeltaNet

4

Gated DeltaNet

5

KDA

Past representation

Growing KV cache

Retain every prior kᵢ, vᵢ; compare qₜ with
every kᵢ.

explicit token-level access · O(t) decode
comparisons

Normalized causal score

Read from explicit values

New variable: aₜᵢ is the normalized causal attention weight from query t to key i.

a
​ =
ti

​

​ exp(q
​k
​/
​)
∑j=1

t

t

⊤
j
d
​k

exp(q
​k
​/
​)
t

⊤
i
d
​k

o
​ =
t

​a
​v
​

i=1
∑

t

ti i

Attention Is All You Need · Vaswani et al., NeurIPS 2017 ↗
19

### Page links

- [Link 1](../optional-readings/arxiv-1706-03762.md)

## Page 20

Linear attention

1

Softmax

2

Linear

3

DeltaNet

4

Gated DeltaNet

5

KDA

Past representation

Fixed matrix state

Sₜᵀ stores an online mapping from keys
to values.

additive writes · interference is not
explicitly erased

1 · Start from standard attention

2 · Replace normalization with a bilinear score

3 · Reassociate, then update recurrently

Key step: replacing query-normalized softmax weights with bilinear scores lets us reorder the sum. Sₜ ∈ ℝᵈᵏˣᵈᵛ stores that fixed-size recurrent memory.

o

​ =
t

​softmax
​ q

​k

​/
​ v

​

i=1
∑

t

i( t

⊤

i
d

​k)
i

softmax
​ q
​k
​/
​
⟶
i( t

⊤

i
d
​k)
q
​k
​
t

⊤

i

​
​
o

​t

S
​t

=
​(q

​k

​)v

​ =
​k

​v

​
q

​ = S

​q

​,

i=1
∑

t

t

⊤

i
i
(

i=1
∑

t

i i

⊤)

⊤

t
t

⊤

t

= S
​ + k
​v
​.
t−1
t t

⊤

Transformers are RNNs · Katharopoulos et al., ICML 2020 ↗
20

### Page links

- [Link 1](../optional-readings/arxiv-2006-16236.md)

## Page 21

DeltaNet

1

Softmax

2

Linear

3

DeltaNet

4

Gated DeltaNet

5

KDA

Memory operation

Targeted correction

Read the current association, then write
only its prediction error.

correct along kₜ · unrelated memory
persists

Prediction and error

Delta-rule write

New variables: v̂ₜ is the current memory prediction; eₜ is its error; βₜ ∈ \[0,1\] is the correction strength.

​ =
v^t
S
​k
​,
e
​ =
t−1

⊤
t
t
v
​ −
t

​v^t

S
​ =
t
S
​ +
t−1
β
​k
​e
​,
o
​ =
t
t t

⊤

t
S
​q
​
t

⊤

t

Linear Transformers Are Secretly Fast Weight Programmers · Schlag et al., ICML 2021 ↗
21

### Page links

- [Link 1](../optional-readings/arxiv-2102-11174.md)

## Page 22

Gated DeltaNet

1

Softmax

2

Linear

3

DeltaNet

4

Gated DeltaNet

5

KDA

New operation

Scalar forgetting

Decay the entire memory before
applying the same targeted correction.

αₜ: global retention · βₜ: targeted edit

Whole-state decay

Correction after decay

New variables: αₜ ∈ \[0,1\] is a scalar retention gate; S̃ₜ₋₁ is the decayed memory. Setting αₜ = 1 recovers DeltaNet.

​ =
St−1
α

​S

​
t
t−1

S
​ =
t

​ +
St−1
β
​k
​ v
​ −
​k
​
t
t( t
St−1

⊤
t)

⊤

Gated Delta Networks · Yang et al., 2024 ↗
22

### Page links

- [Link 1](../optional-readings/arxiv-2412-06464.md)

## Page 23

Kimi Delta Attention

1

Softmax

2

Linear

3

DeltaNet

4

Gated DeltaNet

5

KDA

New operation

Channelwise forgetting

Give each key-space feature its own
memory lifetime.

fine-grained retention · same targeted
correction

Per-channel decay

KDA recurrence

New variables: αₜ ∈ \[0,1\]ᵈᵏ is the vector retention gate; Dₜ is its diagonal matrix; I is the dₖ × dₖ identity. Equal retention in every channel recovers Gated DeltaNet.

D
​ =
t
Diag(α
​),
​ =
t
St−1
D
​S
​
t
t−1

S
​ =
t
(I −β
​k
​k
​)D
​S
​ +
t
t
t

⊤
t
t−1
β
​k
​v
​
t
t t

⊤

Kimi Linear / KDA · Kimi Team, 2025 ↗
23

### Page links

- [Link 1](../optional-readings/arxiv-2510-26692.md)

## Page 24

Sparse attention

Fixed pattern

Input-independent

Visible keys

Predictable cost; the pattern cannot adapt to
the query.

Content-dependent

Query-specific

Visible keys

Adaptive retrieval; selector errors exclude
relevant keys.

Both renormalize over the retained set

New variables: G is a fixed set of global positions; g is a learned selector; |𝒮ᵢᵈʸⁿ| = K.

Fixed
pattern

Outside pattern /
future

Keys

Queries

S

​ =
i

fixed
{j ≤i : i −j < w} ∪(G ∩\[1, i\])

Selected
history

Not selected /
future

Keys

Queries

S

​ =
i

dyn
TopK

​ g(q

​, k

​)
j≤i
i
j

A
=
ij
softmax
​
​
,
o
​ =
j∈S
​i(

​
d
​k

q
​k
​
i

⊤
j )
i

​A
​v
​

j∈S
​i
∑
ij
j

Fixed local + global pattern · Longformer, 2020 ↗
Content-dependent top-K · DeepSeek Sparse Attention, 2025 ↗
24

### Page links

- [Link 1](../optional-readings/arxiv-2004-05150.md)
- [Link 2](../optional-readings/arxiv-2512-02556.md)

## Page 25

KV compression

MLA caches the latent and reconstructs head-specific keys and values

New variables: cₜᴷⱽ is the cached latent; h indexes heads; Wᴰ compresses and Wᵁᴷ, Wᵁⱽ recover per-head K,V.

c

​ =
t
KV
W

​z

​,
k

​ =
D

KV

t
t
(h)
W

​c

​,
v

​ =
UK

(h)

t
KV

t

(h)
W

​c

​
UV

(h)

t
KV

GQA · Ainslie et al., 2023 ↗
Attention comparison and MLA · DeepSeek-V2, 2024 ↗
25

### Page links

- [Link 1](../optional-readings/arxiv-2305-13245.md)
- [Link 2](../optional-readings/arxiv-2405-04434.md)

## Page 26

Training long-context models

26

## Page 27

Short-to-long training

Short pretraining

abundant data · lower cost

4K–8K

→

Continued training

long documents · packed
sequences

32K–128K

→

Long adaptation

task traces · synthetic curricula

128K+

27

## Page 28

Absolute positional encodings

token state

E\[xₜ\]
+

position vector

pₜ

Input to the first layer

Fixed sinusoidal encoding

New variables: xₜ is a token ID; E is the embedding table; pₜ is the positional vector; ℓ indexes sinusoid pairs.

Position enters before the projections that produce Q, K, and V.

Learned absolute embeddings have a fixed table; sinusoids define positions analytically.

z

​ =
t
E\[x

​\] +
t
p

​t

p
​ =
t,2ℓ
sin(t/ω
​),
p
​ =
ℓ
t,2ℓ+1
cos(t/ω
​),
ω
​ =
ℓ
ℓ
100002ℓ/d

Transformer positional encoding · Vaswani et al., 2017 ↗
28

### Page links

- [Link 1](../optional-readings/arxiv-1706-03762.md)

## Page 29

Rotary position embeddings (RoPE)

qᵢ
↗

kⱼ
↘

Relative angle

j − i

Rotate rows of Q and K

The score depends on relative displacement

New variable: R(t) is block-diagonal in 2D rotations with angles tθₗ.

V is unchanged; attention uses the same equation with rotated Q and K.

​
​ =
q~i
R(i)q
​,
​ =
i
k~

j
R(j)k
​j

​
​
​ =
q~

i

⊤k~

j
q
​R(j −
i

⊤
i)k
​j

RoFormer · Su et al., Neurocomputing 2024 ↗
29

### Page links

- [Link 1](../optional-readings/arxiv-2104-09864.md)

## Page 30

No positional encoding (NoPE)

token state only

E\[xₜ\]
→

model layers

causal

order

Input to the first layer

Attention equation is unchanged

Order is inferred from causal computation or recurrent dynamics—not from pₜ or R(t).

This removes position extrapolation, but not the need to train long-range behavior.

z

​ =
t
E\[x

​\]
t

A = softmax
​
,
O =
(

​
d
​k

QK
+ M
⊤

)
AV

NoPE length generalization · Kazemnejad et al., NeurIPS 2023 ↗
Kimi K3 · NoPE with recurrent KDA ↗
30

### Page links

- [Link 1](../optional-readings/arxiv-2305-19466.md)
- [Link 2](../optional-readings/arxiv-2607-24653.md)

## Page 31

Position interpolation

evaluate target position t using the familiar phase t / s

Uniform position interpolation

New variables: L and L′ are original and target limits; s = L′/L.

Every RoPE dimension is stretched by the same scale s.

Long positions stay inside the phase range observed during pretraining.

Pretraining range

0
L

Target range

0
L′ = sL

R(t)  ⟶  R(t/s)
equivalently
θ
​  ⟶ 
ℓ
θ
​/s
ℓ

Position Interpolation · Chen et al., 2023 ↗
31

### Page links

- [Link 1](../optional-readings/arxiv-2306-15595.md)

## Page 32

YaRN

Long wavelength
interpolate fully

Middle
blend

Short wavelength
keep local phase

Frequency-selective interpolation

Attention-temperature adjustment

New variables: γₗ ramps from 0 for long wavelengths to 1 for short wavelengths; τ is attention temperature.

Long-wavelength dimensions are interpolated; short-wavelength dimensions preserve local

distinctions.

The temperature correction counteracts attention-entropy drift at larger extension scales.

The published formula for τ was fit on LLaMA models; it is a recipe, not a universal constant.

θ
​ =
ℓ
′
(1 −γ
​)
​ +
ℓs

θ
​ℓ
γ
​θ
​,
0 ≤
ℓℓ
γ
​ ≤
ℓ
1

A = softmax
​
,
​ =
(
τ
​
d
​k

​
+ M
Q~K~ ⊤

)
1/τ
0.1 ln s + 1

YaRN · Peng et al., ICLR 2024 ↗
32

### Page links

- [Link 1](../optional-readings/arxiv-2309-00071.md)

## Page 33

Model-specific extension paths

Model
Context-length training
Position method
How it reaches maximum context

Qwen3.8-Flash-Next
262K native; full curriculum undisclosed
partial RoPE
YaRN extension to 1M

DeepSeek V4
4K → 16K → 64K → 1M
partial RoPE
progressive training + YaRN

GLM-5.3-Flash
1M native; exact curriculum undisclosed
NoPE in main attention
no RoPE rescaling

Kimi K3
8K → 64K → 256K → 1M
NoPE
progressive training to 1M

Nemotron 3 Ultra
1M long-context CPT; SFT to 512K
implicit order in Mamba; no RoPE
trained/evaluated at long lengths

Inkling
1M context; curriculum undisclosed
relative position embedding
learned relative representation

Qwen ↗
DeepSeek ↗
GLM ↗
Kimi ↗
Nemotron ↗
Inkling ↗
33

### Page links

- [Link 1](../optional-readings/arxiv-2606-19348.md)
- [Link 2](../optional-readings/arxiv-2607-24653.md)
- [Link 3](https://huggingface.co/zai-org/GLM-5.3-Flash/blob/main/config.json)
- [Link 4](../optional-readings/qwen3-8-flash-next-rendered.md)
- [Link 5](../optional-readings/ref-1e31be6807c5.md)
- [Link 6](../optional-readings/ref-8c3acf43834d.md)

## Page 34

Long-context data examples

Long documents

coherent natural structure

Books, codebases, repositories, and multi-document corpora.

Packed examples

high token utilization

Efficient, but boundaries and cross-example leakage matter.

Agent trajectories

actions + observations

Teach long-horizon recovery, state tracking, and tool use.

Synthetic tasks

controlled dependencies

Place evidence and distractors at designed positions.

34

## Page 35

Long-context data mixtures

Model
Natural long data
Constructed supervision
Length curriculum

Kimi K3
cleaned, upsampled documents + video
permuted multimodal subtasks with evidence across the full
context

8K → 64K → 256K → 1M

GLM-5
documents; repository files, issues, PRs, and
diffs

synthetic dependencies + agent trajectories
32K → 128K → 200K

Nemotron 3 Ultra
long-document QA
multi-document reasoning, sequential scans, synthetic tables
33B-token 1M CPT; SFT to 512K

DeepSeek V4
scientific papers + technical reports
agentic post-training after long-context pretraining
4K → 16K → 64K → 1M

The shared recipe is coherent long sources + tasks whose answer depends on distant evidence + progressive length growth.

Kimi K3 ↗
GLM-5 ↗
Nemotron 3 Ultra ↗
DeepSeek V4 ↗
35

### Page links

- [Link 1](../optional-readings/arxiv-2602-15763.md)
- [Link 2](../optional-readings/arxiv-2606-19348.md)
- [Link 3](../optional-readings/arxiv-2607-24653.md)
- [Link 4](../optional-readings/ref-1e31be6807c5.md)

## Page 36

Context parallelism

Memory / device O(ndₖ/P)
Communication overlapped with block attention
Total work O(n²dₖ) · exact, not sparse

Ring Attention · Liu et al., 2023 ↗
Megatron context parallelism ↗
36

### Page links

- [Link 1](../optional-readings/arxiv-2310-01889.md)
- [Link 2](../optional-readings/ref-5a91a973dc05.md)

## Page 37

Prompt and KV caching

37

## Page 38

KV caching during decoding

cached input
regular input
model output
tool result

Call 1
new input
output
tool result
create prompt KV;
decode output

Call 2
cached
new input
output
tool result
tool result returns as
new input

Call 3
cached
new input
output
tool result
the reusable prefix
keeps growing

Within a call: output tokens extend the KV cache during decode. Between calls: the tool result returns as new input; after prefill, it joins the

reusable prefix.

KV and prompt-state reuse · Prompt Cache, MLSys 2024 ↗
38

### Page links

- [Link 1](../optional-readings/arxiv-2311-04934.md)

## Page 39

Empirical benefits of cache reuse

Prompt Cache

Compute grows faster than loading cached attention state; the crossover depends
on hardware.

Can I Buy Your KV Cache?

One-time prefill is amortized across readers; per-call cost approaches the reuse-step
floor.

Measured physical cost and provider API price are different quantities.

Prompt Cache · Gim et al., 2024 ↗
Can I Buy Your KV Cache? · 2026 ↗
39

### Page links

- [Link 1](../optional-readings/arxiv-2311-04934.md)
- [Link 2](../optional-readings/arxiv-2606-13361.md)

## Page 40

Cached-token API pricing

Model
Cached input
Regular input
Output

DeepSeek V4 Flash
$0.007–0.014
$0.22–0.44
$0.66–1.32

GLM-5.2
$0.26
$1.40
$4.40

Kimi K3
$0.30
$3.00
$15.00

GPT-5.6 Luna
$0.02
$0.20
$1.20

GPT-5.6 Sol
$0.40
$4.00
$20.00

Claude Opus 5
$0.50
$5.00
$25.00

USD per 1M tokens · prices checked Aug. 30, 2026
“Cached” means a cache read/hit; cache creation may be billed separately.
DeepSeek range: off-peak–peak.

DeepSeek ↗
Z.AI ↗
Kimi ↗
OpenAI ↗
Anthropic ↗
40

### Page links

- [Link 1](../optional-readings/ref-280758cc57a6.md)
- [Link 2](../optional-readings/ref-788ec084b414.md)
- [Link 3](../optional-readings/ref-667e800254a1.md)
- [Link 4](../optional-readings/ref-9a3bbc4f637b.md)
- [Link 5](../optional-readings/ref-d5ad370f5e10.md)

## Page 41

Paged KV-cache allocation

Block-table translation · vLLM / PagedAttention · Kwon et al., SOSP 2023 ↗
41

### Page links

- [Link 1](../optional-readings/arxiv-2309-06180.md)

## Page 42

RadixAttention prefix sharing

3 · Match

reuse prefix, append suffix

4 · Split

share the common prefix

5 · Evict

remove an LRU leaf

RadixAttention operations (steps 3–5) · SGLang · Zheng et al., 2023 ↗
42

### Page links

- [Link 1](../optional-readings/arxiv-2312-07104.md)

## Page 43

Cache-aware request routing

Incoming request

A
prefix hash A

Cache-aware router

score = reusable prefix − queue penalty

Worker 1
18K match · queue 2

Worker 2
2K match · queue 0
→
→

SGLang v0.4 · cache-aware load balancing ↗
43

### Page links

- [Link 1](../optional-readings/ref-2343cb57205a.md)

## Page 44

Prompt design for cache reuse

Stabilize the prefix

instructions · tools · examples

Append changing state

new user turn · observations

Avoid needless churn

timestamps · reordered schemas

Measure reuse

cached tokens · TTFT · eviction

44

## Page 45

Context compaction

45

## Page 46

Compaction example

Before

OBSERVATION
CI job times out after 30 minutes.

ACTION
Inspect the job log.

OBSERVATION
24K-line log; repeated “address already in use.”

ACTION
Set --workers=1  and rerun.

OBSERVATION
Suite passes; log saved at /tmp/ci.log .

→

compact

After

OBSERVATION

Goal: fix CI timeout.
Cause: port collision.
Verified: --workers=1  passes.
Evidence: /tmp/ci.log .

NEXT ACTION
Open the PR with the tested worker setting.

46

## Page 47

Compaction as state estimation

History
H
→
Compactor
𝒞
→
Working state
ŝ

Behavioral fidelity
Bounded representation
Recoverability

Copy exact anchors; retain pointers to
source evidence.

Notation: Hₜ is the full history; ŝₜ is compacted working state; B is its token budget; A
 denotes future actions.

t
B
t

p(A

​ ∣
future
H

​)  ≈ 
t
p(A

​ ∣
future

​)
s^t

​ =
s^t
C(H

​; B),
∣

​∣≤
t
s^t
B

future

47

## Page 48

What survives compaction

MODEL-VISIBLE CONTEXT

KEEP EXACT
Anchors

goal · constraints

ENCODE
Checkpoint

decisions · progress · IDs

KEEP EXACT
Recent tail

active attempt · fresh result

↘

EXTERNALIZE
Evidence store

24K-line log → 3 failures + command + artifact path

DISCARD
duplicates · superseded
attempts

MemGPT · externalize and retrieve ↗
LongLLMLingua · selective compression ↗
48

### Page links

- [Link 1](../optional-readings/ref-21b9648ed469.md)
- [Link 2](../readings/arxiv-2310-08560.md)

## Page 49

Compaction policy decisions

1 · Trigger

token threshold

provider overflow

manual request

reserve room for the next
output

→

2 · Select

protect beginning

compact older region

keep recent tail

cut at a valid turn / tool
boundary

→

3 · Replace

readable summary

structured checkpoint

opaque provider item

fresh context

→

4 · Recover

leave history unchanged

retry or reset

retain searchable history

define behavior when
compaction fails

Codex ↗
OpenCode ↗
Pi ↗
Hermes ↗
OpenHands ↗
49

### Page links

- [Link 1](../optional-readings/ref-a04396a09788.md)
- [Link 2](../optional-readings/ref-ec2b8bd43eef.md)
- [Link 3](../optional-readings/ref-ffccace0ba14.md)
- [Link 4](../optional-readings/ref-97416d4ba885.md)
- [Link 5](../optional-readings/ref-8c3dc2a0187c.md)

## Page 50

Repeated compaction drift

History

Use CUDA 12.4
→

Summary 1

Use CUDA 12.x
→

Summary 2

Use recent CUDA
→

Summary 3

Constraint missing

Each update inherits the previous checkpoint

copy anchors exactly
·
keep the recent tail
·
retrieve source evidence

​ =
s^k+1
C(
​ ⊕
s^k
R
​)
k

ReSum · summary-conditioned agent continuation ↗
50

### Page links

- [Link 1](../optional-readings/arxiv-2509-13313.md)

## Page 51

Continuation-based evaluation

Plant state

constraints · decisions · artifacts
→

Compact

apply the production policy
→

Continue

measure later decisions

State recall  constraints + identifiers
Task success  correct continuation

Efficiency  tokens + latency + cost
Stability  repeated compactions

51

## Page 52

Takeaways

52

## Page 53

The long-context system stack

1
Growth: agent loops repeatedly ingest instructions, actions, and environment observations.

2
Inference: prefill, decode, dense attention, and KV memory create different bottlenecks.

3
Architecture: local, recurrent, sparse, and compressed mechanisms choose what history remains accessible.

4
Caching: stable prefixes avoid repeated prefill but do not reduce visible history.

5
Compaction: preserve intent, exact task state, recent work, and recovery paths—then evaluate continuation.

53

## Page 54

Questions

Next Class: Agent Capabilities 3 — Skills and Memory

54
