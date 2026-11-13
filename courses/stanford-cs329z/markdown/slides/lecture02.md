# Lecture 2: LLMs for Builders

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf) · [Raw file](../../raw/slides/lecture02.pdf)

Retrieved: 2026-11-13T16:17:57.138142+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Diyi Yang, Michael Ryan, John Yang

LLMs for Builders

CS 329Z: Engineering AI Agents

## Page 2

CS329Z: Engineering AI Agents
CS329Z: Engineering AI Agents

LLM 
Applications

LLM 
Adaptation

LLM 
Engineering

GPU Kernels

Pretraining

Architectures

Post-training

Distributed Compute

Scaling Laws

Finetuning

Chatbots

In-Context Learning

Agents

RAG

Learning from Feedback (RLHF/DPO)

LoRA

Distillation

The LLM Stack

CS336

CS224N

CS329Z

RL
Tokenizer

Agent Frameworks

Multi Agent
Agent Memory

Proactive Agents
Agent Evals

…
Agent Design

## Page 3

CS329Z: Engineering AI Agents

We are going to operate at the 
highest level of the LLM stack, but

it is still important to understand a

bit about how they work…

CS329Z: Engineering AI Agents

## Page 4

CS329Z: Engineering AI Agents

Learning Objectives

• Understand and explain the core design decisions that go into training and 
inferencing modern Large Language Models (LLMs).

• Synthesize how these design decisions lead to limitations that impact the 
way in which applications leverage LLMs.

## Page 5

CS329Z: Engineering AI Agents

Lecture Overview

• What is a Language Model?

• Language Model Architecture

• Training

• Inference

• LLMs for Agents

## Page 6

CS329Z: Engineering AI Agents

What is a Language Model?

Language Models?
Architecture
Training
Inference
LLMs for Agents

## Page 7

CS329Z: Engineering AI Agents

Probability of a 
sequence of tokens Equals Product from the

first to last token

of the probability of the current 
token given the previous tokens

## Page 8

CS329Z: Engineering AI Agents

class
was
about
agents
.

The
P(                     ) = 0.0377

The

The
P(                     |                  ) = 0.0001
class

The
P(                     |                  ,                 ) = 0.0344
class
was

…

The
P(                     |                  ,                 ,                ,                ,                )    0.0252
class
.
was
about
agents

0.0377

0.0001

0.0344

…

x=

1.2e-17
*in practice we typically take the sum of the log of the probabilities instead for numerical stability.

## Page 9

CS329Z: Engineering AI Agents

This is a Language

Model

## Page 10

CS329Z: Engineering AI Agents

Generative vs. Discriminative

Models

## Page 11

CS329Z: Engineering AI Agents

Learn to Distinguish Classes
Learn Distribution of Data

- Naive Bayes 
- Diffusion models
- Logistic Regression 
- SVM

E.g.
E.g.

Image Credit: Akanksha Malhotra | medium.com

## Page 12

CS329Z: Engineering AI Agents

Knowledge Check
Are Language Models that model the probability of a token sequence as shown below 
generative or discriminative?

This isn’t meant to be a trick question, but the notation here can make it tricky.

## Page 13

CS329Z: Engineering AI Agents

LMs are generative, which means

we can sample from them.

## Page 14

CS329Z: Engineering AI Agents

Language Model Sampling

## Page 15

CS329Z: Engineering AI Agents

class
was
about
The

to

as

the

a

two

“

time

three

getting

how

## Page 16

CS329Z: Engineering AI Agents

about

to

as

the

a

two

“

time

three

getting

how

P(               |               ,               ,               ,               ) = 0.3171 
The
class
to
was
about

P(               |               ,               ,               ,               ) = 0.0491 
The
class
as
was
about

P(               |               ,               ,               ,               ) = 0.036 
The
class
the
was
about

P(               |               ,               ,               ,               ) = 0.033 
The
class
a
was
about

P(               |               ,               ,               ,               ) = 0.0147 
The
class
two
was
about

P(               |               ,               ,               ,               ) = 0.0124
The
class
how
was
about

P(               |               ,               ,               ,               ) = 0.0101
The
class
getting
was
about

P(               |               ,               ,               ,               ) = 0.01 
The
class
three
was
about

P(               |               ,               ,               ,               ) = 0.0091 
The
class
time
was
about

P(               |               ,               ,               ,               ) = 0.0081 
The
class
“
was
about

## Page 17

CS329Z: Engineering AI Agents

about

to
0.3171

as
0.0491

the
0.036

a
0.033

two
0.0147

how
0.0124

getting
0.0101

three
0.01

time
0.0091

“
0.0081

## Page 18

CS329Z: Engineering AI Agents

about
to

be

begin

go

start

get

graduate

end

take

enter

become

0.1501

0.0855

0.0627

0.0496

0.0390

0.0342

0.0313

0.0220

0.0192

0.0180

We don’t always have to pick the most 
likely next token.  There are different 
sampling (decoding) strategies.

• Greedy 
• Nucleus (top p) 
• Top k 
• …

## Page 19

CS329Z: Engineering AI Agents

class
was
about
The
to
begin
.

## Page 20

CS329Z: Engineering AI Agents

Temperature

Image Credit: https://towardsdatascience.com/
decoding-the-temperature-parameter-in-llms/

Divide all the 
probabilities by 
some temperature T 
and then renormalize 
to sum to 1.

### Page links

- [Link 1](https://towardsdatascience.com/decoding-the-temperature-parameter-in-llms/)

## Page 21

CS329Z: Engineering AI Agents

Beam Search

Image Credit: https://medium.com/@chawthirisan/
beam-search-navigating-possibilities-with-controlled-
exploration-dde901e9baa7

### Page links

- [Link 1](https://medium.com/@chawthirisan/beam-search-navigating-possibilities-with-controlled-exploration-dde901e9baa7)

## Page 22

CS329Z: Engineering AI Agents

Considerations for Sampling

• Each Sampling Strategy has different tradeoffs

• Temperature and Top-p/Top-k help with diversity

• The strategy you use may depend on your task

• Math/Code are more predictable (lower temperature)

• Creative Writing may benefit from higher diversity

• Your strategy also depends on your budget (beam search has higher time and 
memory complexity)

## Page 23

CS329Z: Engineering AI Agents

Further Reading

• Decoding Strategies in Large Language Models: https://huggingface.co/
blog/mlabonne/decoding-strategies

• Tokenizers: https://huggingface.co/learn/llm-course/en/chapter2/4

• Generative Models: https://deepgenerativemodels.github.io/notes/
introduction/

### Page links

- [Link 1](https://deepgenerativemodels.github.io/notes/introduction/)
- [Link 2](https://huggingface.co/blog/mlabonne/decoding-strategies)
- [Link 3](https://huggingface.co/learn/llm-course/en/chapter2/4)

## Page 24

CS329Z: Engineering AI Agents

Language Model Architecture

Language Models?
Architecture
Training
Inference
LLMs for Agents

## Page 25

CS329Z: Engineering AI Agents

A brief history of Language Model Architectures

• N-gram Models (Pre 2010s)

• First Neural Language Model (2003)

• Recurrent Neural Network Language Models (2010)

• Long Short Term Memory (Invented 1997 & popularized for LMs 2014)

## Page 26

CS329Z: Engineering AI Agents

Transformers

Figure Credit: DeltaNet Explained (Part III) |

Songlin Yang

### Page links

- [Link 1](https://sustcsonglin.github.io/blog/2024/deltanet-3/)

## Page 27

CS329Z: Engineering AI Agents

Transformers: Attention Is All You Need (2017)

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin

Image Credit: Attention Is All You Need

Decoder

Encoder

## Page 28

CS329Z: Engineering AI Agents

Decoder-only Transformer

was
class
about
The

## Page 29

CS329Z: Engineering AI Agents

Decoder-only Transformer

was
class
about
The

…
…
…
…
Embedding

## Page 30

CS329Z: Engineering AI Agents

Decoder-only Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

…
+

Positional 
Embedding

## Page 31

CS329Z: Engineering AI Agents

Decoder-only Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

…
+

…
…
…

…

## Page 32

CS329Z: Engineering AI Agents

If you get lost here much of the rest of the lecture will be

very confusing!

Important!  Pay Close Attention Here!

## Page 33

CS329Z: Engineering AI Agents

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

…
+

…
…
…

…

Attention 
Layer

## Page 34

CS329Z: Engineering AI Agents

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

…
+

…
…
…

…
Layer Norm(
)

Attention 
Layer

## Page 35

CS329Z: Engineering AI Agents

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Matrix 
Multiply to 
obtain Q, K, V

activations

…
…
…

…

## Page 36

CS329Z: Engineering AI Agents

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

X

…
+

…
…
…

…

## Page 37

CS329Z: Engineering AI Agents

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

X

…
+

Causal 
Attention

Mask

…
…
…

…

## Page 38

CS329Z: Engineering AI Agents

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

X

…
+

)
÷
(

…
…
…

…

## Page 39

CS329Z: Engineering AI Agents

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

X

…
+

)
÷
(
Softmax(
)=

…
…
…

…

## Page 40

CS329Z: Engineering AI Agents

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

X

…
+

)
÷
(
Softmax(
)=
X

…
…
…

…

## Page 41

CS329Z: Engineering AI Agents

)=

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO
…
…
…

…

X

X
÷

…
+

Softmax(

Matrix 
Multiply to 
project back

to model 
dimensions

…
…
…

…

## Page 42

CS329Z: Engineering AI Agents

)=

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO
…
…
…

…

X

X
÷

…
+

Softmax(

+
Residual 
Connection

…
…
…

…

## Page 43

CS329Z: Engineering AI Agents

)=

Attention 
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO
…
…
…

…

X

X
÷

…
+

Softmax(

+
Multi-Head  
Attention  
Layer

…
…
…

…

## Page 44

CS329Z: Engineering AI Agents

)=

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

X

X
÷

…
+

Softmax(

Multi-Head  
Attention  
Layer

1. Multiple

Weight 
Matrices

…
…
…

…

## Page 45

CS329Z: Engineering AI Agents

Multi-Head  
Attention  
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

X

X
÷dk)=

…
+

WQ
WQ
WK
WK
WV
WV

++
++

+
+

÷dk)=
Softmax(
÷.   )=

1. Multiple

Weight 
Matrices

…
…
…

…

## Page 46

CS329Z: Engineering AI Agents

Multi-Head  
Attention  
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

X

X
÷dk)=

…
+

WQ
WQ
WK
WK
WV
WV

++
++

+
+

÷dk)=
Softmax(
÷.   )=

1. Multiple

Weight 
Matrices

2. Concatenate

Attention

Outputs

…
…
…

…

## Page 47

CS329Z: Engineering AI Agents

Multi-Head  
Attention  
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO
…
…
…

…

X

X
÷dk)=

…
+

WQ
WQ
WK
WK
WV
WV

++
++

+
+

÷dk)=
Softmax(
÷.

+

)=

1. Multiple

Weight 
Matrices

2. Concatenate

Attention

Outputs

3. Bigger 
Projection Matrix

…
…
…

…

## Page 48

CS329Z: Engineering AI Agents

Multi-Head  
Attention  
Layer

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO
…
…
…

…

X

X
÷dk)=

…
+

WQ
WQ
WK
WK
WV
WV

++
++

+
+

÷dk)=
Softmax(
÷.

+

)=

…
…
…

…

## Page 49

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

…
…
…

…

…
…
…

…

## Page 50

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Multi-head, Causal 
Self-Attention Layer

…
…
…

…

…
…
…

…

## Page 51

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Multi-head, Causal 
Self-Attention Layer

…
…
…

…
Layer Norm(
)

…
…
…

…

## Page 52

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Multi-head, Causal 
Self-Attention Layer

…
…
…

…
Layer Norm(
)

+

…
…
…

…

## Page 53

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Multi-head, Causal 
Self-Attention Layer

…
…
…

…
Layer Norm(
)

+

Feed Forward

…
…
…

…

…
…
…

…

## Page 54

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Multi-head, Causal 
Self-Attention Layer

…
…
…

…
Layer Norm(
)

+

Feed Forward

…
…
…

…

+

…
…
…

…

## Page 55

CS329Z: Engineering AI Agents

…
…
…

…
Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

…
…
…

…

## Page 56

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Transformer

Block

x N

…
…
…

…

…
…
…

…

## Page 57

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Transformer

Block

x N

…
…
…

…
Layer Norm(
)

LM Head

…
…
…

…

## Page 58

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Transformer

Block

x N

…
…
…

…
Layer Norm(
)

LM Head

…
…
…

…

…
…
…

…

## Page 59

CS329Z: Engineering AI Agents

Decoder-only 
Transformer

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Transformer

Block

x N

…
…
…

…
Layer Norm(
)

LM Head

…
…
…

…
Softmax(
)

…
…
…

…

## Page 60

CS329Z: Engineering AI Agents

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

…
+

Transformer

Block

x N

…
…
…

…
Layer Norm(
)

LM Head

…
…
…

…
Softmax(
)

…
Softmax(
)
…
Softmax(
)
…
Softmax(
)
…
Softmax(
)

…
…
…

…

## Page 61

CS329Z: Engineering AI Agents

Attention vs Recurrence

Table Credit: Attention Is All You Need

O(1) Sequential Operations is a huge deal for parallel training on GPUs!

O(n²) Sequence length means long context becomes expensive.

## Page 62

CS329Z: Engineering AI Agents

Transformers were better and cheaper

Table Credit: Attention Is All You Need

## Page 63

CS329Z: Engineering AI Agents

Linear Attention

Figure Credit: DeltaNet Explained (Part III) |

Songlin Yang

### Page links

- [Link 1](https://sustcsonglin.github.io/blog/2024/deltanet-3/)

## Page 64

CS329Z: Engineering AI Agents

)=

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

…

X

X
÷

…
+

Softmax(

+

…

Attention 
Layer

Linear 
Attention

## Page 65

CS329Z: Engineering AI Agents

)=

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

…

X

X
÷

…
+

Softmax(

+

…

Linear 
Attention

## Page 66

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

…

X

X

…
+

+

…

Linear 
Attention

“Drop Softmax”

## Page 67

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

…

X

X

…
+

+

…

Linear 
Attention

“Drop Softmax”

Everything here is

now linear!
We can change the

associativity.

Let’s Multiply K and

V instead.

## Page 68

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

…

Linear 
Attention

## Page 69

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

…

Linear 
Attention

X

S1

## Page 70

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

…

Linear 
Attention

X

S1
X

## Page 71

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

…

Linear 
Attention

X

S1
X

…

+

WO

…

+

## Page 72

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

…

Linear 
Attention

Update

Rule

X

S1
X

…

+

WO

…

+

## Page 73

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

S1
X

…

+

WO

+

Clear 
Unimportant

Memory

## Page 74

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

S1
X

…

+

WO

+

Save the state

## Page 75

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

X

…

+

WO

+

S1

class
The

…
…
+

…

…

## Page 76

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

X

…

+

WO

+

S1

class
The

…
…
+

…

…

## Page 77

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

X

…

+

WO

+

S1

class
The

…
…
+

…

…

## Page 78

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

X

…

+

WO

+

S1

class
The

…
…
+

…

…

S2

+

## Page 79

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

X

…

+

WO

+

S1

class
The

…
…
+

…

…

S2

+

…

## Page 80

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

X

…

+

WO

+

Clear 
Unimportant

Memory

S2

class

…
…
+

…

## Page 81

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

X

…

+

WO

+

S2

class
The

…
…
+

…

S3

+

…

was

…
…
+

…

…

## Page 82

CS329Z: Engineering AI Agents

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

+

+

…
+

Linear 
Attention

Update

Rule

X

X

…

+

WO

+

S3

class
The

…
…
+

…

S4

+

…

was

…
…
+

…

…

about

…
…
+

…

## Page 83

CS329Z: Engineering AI Agents

Linear Attention is way faster and has a better memory footprint

Figure Credit: Transformers are RNNs Fast 
Autoregressive Transformers with Linear Attention

## Page 84

CS329Z: Engineering AI Agents

However… it struggles more with longer context

Figure Credit: RULER: What’s the Real Context

Size of Your Long-Context Language Models?

## Page 85

CS329Z: Engineering AI Agents

A Note about Context Length

Nothing the Transformer or Linear Attention enforced a strict context length…
except the way the model processes positional embeddings.

In practice we need the model to learn to use the positional embeddings so we are 
limited to the context length that we trained the model with.

## Page 86

CS329Z: Engineering AI Agents

Bringing it together

Figure Credit: DeltaNet Explained (Part III) |

Songlin Yang

### Page links

- [Link 1](https://sustcsonglin.github.io/blog/2024/deltanet-3/)

## Page 87

CS329Z: Engineering AI Agents

Full Softmax Attention vs Linear Attention

Full Softmax Attention
Linear Attention

- O(n²) in context length
- O(n) in context length

-
All tokens can refer back to all 
prior tokens

-
Helps long context

-
New tokens interact with a 
compressed state representation

-
Harder for long context

- KV Cache (memory) grows O(n)
- State representation uses 
constant memory

## Page 88

CS329Z: Engineering AI Agents

In practice people mix global and linear attention

Figure Credit: DeltaNet Explained (Part III) |

Songlin Yang

### Page links

- [Link 1](https://sustcsonglin.github.io/blog/2024/deltanet-3/)

## Page 89

CS329Z: Engineering AI Agents

In practice people mix global and linear attention

Figure Credit: DeltaNet Explained (Part III) |

Songlin Yang

### Page links

- [Link 1](https://sustcsonglin.github.io/blog/2024/deltanet-3/)

## Page 90

CS329Z: Engineering AI Agents

Kimi K3

Figure Credit:  Kimi K3: Open Frontier

Intelligence | arxiv 2607.24653

Feed Forward

Feed Forward

Multi-Head 
(Latent) Attention

Linear Attention

## Page 91

CS329Z: Engineering AI Agents

Why does all of this matter for agents?

• Agents can deal with extremely long contexts

• Inference efficiency is a design consideration in building agentic systems

• Knowing the underlying model architectures can help you select the right 
model for your agentic application

• Developing the harness and scaffolding around your particular model’s 
strengths and weaknesses will make you a better agent engineer!

## Page 92

CS329Z: Engineering AI Agents

LLM Training

Language Models?
Architecture
Training
Inference
LLMs for Agents

## Page 93

CS329Z: Engineering AI Agents

Defining the Loss

## Page 94

CS329Z: Engineering AI Agents

The class was about how 
agents work, and how to 
build AI systems that use 
tools, retrieve information, 
and carry out tasks across 
multiple steps…

Training Data (Example)

Engineering

## Page 95

CS329Z: Engineering AI Agents

class
was
about
The

to

as

the

a

two

“

time

three

getting

how

## Page 96

CS329Z: Engineering AI Agents

about

to

as

the

a

two

“

time

three

getting

how

0.3171

0.0491

0.036

0.033

0.0147

0.0124

0.0101

0.01

0.0091

0.0081

The class was about 
how agents work…

## Page 97

CS329Z: Engineering AI Agents

about

to

as

the

a

two

“

time

three

getting

how

0.3171

0.0491

0.036

0.033

0.0147

0.0124

0.0101

0.01

0.0091

0.0081

The class was about 
how agents work…

## Page 98

CS329Z: Engineering AI Agents

about

how
0.0124

The class was about 
how agents work…

## Page 99

CS329Z: Engineering AI Agents

about

how
0.0124

The class was about 
how agents work…

Loss = - log(0.0124) =1.907

## Page 100

CS329Z: Engineering AI Agents

Cross Entropy Loss

For every token in

the vocabulary

1 when this is the

token in the data

0 when this is not the

token in the data

log probability of that

token

## Page 101

CS329Z: Engineering AI Agents

Pretraining

## Page 102

CS329Z: Engineering AI Agents

Data

HTML

Text 
Extraction
Deduplication

Lang ID

Final Training

Data

Rule-Based

Filters

Quality

Filters

## Page 103

CS329Z: Engineering AI Agents

Data

Image Credit: DataComp-LM: In Search of the 
Next Generation of Training Sets for Language 
Models. arXiv:2406.11794.

## Page 104

CS329Z: Engineering AI Agents

Data

Image Credit: Nemotron-CC-Math: A 133 Billion-
Token-Scale High Quality Math Pretraining 
Dataset. arXiv:2508.15096

## Page 105

CS329Z: Engineering AI Agents

AnimeSuki Forum (

-   Suggestions (

-   -   trying something new (

tedybearsoka 2013-06-27 00:21

trying something new

anybody know of a hacking anime. ide like it to involve a person who is a legendary hacker or 
something like that.the only other thing is can the anime be dubbed (well actually ide prefer it to be 
dubbed) :)

SeijiSensei 2013-06-27 08:07

Watch the movie Summer Wars. It's been dubbed by Funimation.

All the kids in the extraordinary Dennou Coil are hackers of varying skills. It's only subtitled, though.

Shirow Masamune's Real Drive also has hacking, but it's presented in an very unconventional way. 
Also subtitled.

It's 7 a.m. at the Culinary Institute of America at Greystone. Chef John Difilippo is in front of his 
baking and pastry class, explaining the difference between a pie and a tart. “This is not a pie, it’s a 
tart,” he tells the students, who are surprisingly alert and maybe even a little hyper for so early in the 
morning. They lean forward in their seats. “A tart is more refined than a pie, while a pie is more rustic,” 
he tells them. RECIPE: Pear ...

Register to view this Article

Why Register for FREE?

Already registered? here.

Next: , Previous: DTIME, Up: Intrinsic Procedures

8.48 EOSHIFT — End-off shift function

EOSHIFT(ARRAY, SHIFT\[,BOUNDARY, DIM\]) performs an end-off shift on elements of ARRAY along 
the dimension of DIM. If DIM is omitted it is taken to be 1. DIM is a scaler of type INTEGER in the 
range of 1 /leq DIM /leq n) where n is the rank of ARRAY. If the rank of ARRAY is one, then all 
elements of ARRAY are shifted by SHIFT places. If rank is greater than one, then all complete rank 
one sections of ARRAY along the given dimension are shifted. Elements shifted out one end of each 
rank one section are dropped. If BOUNDARY is present then the corresponding value of from 
BOUNDARY is copied back in the other end. If BOUNDARY is not present then the following are 
copied in depending on the type of ARRAY.

Array Type Boundary Value

Numeric 0 of the type and kind of ARRAY.

Logical .FALSE..

Character(len) len blanks

Data

Engineering

Examples of Data from DCLM

## Page 106

CS329Z: Engineering AI Agents

Data

Image Credit: The Pile: An 800GB Dataset of Diverse 
Text for Language Modeling. arXiv: 2101.00027

## Page 107

CS329Z: Engineering AI Agents

Data Mixing

Image Credit: Olmix: A Framework for Data 
MixingThroughout LM Development | arxiv 2602.12237

## Page 108

CS329Z: Engineering AI Agents

Midtraining

Engineering

## Page 109

CS329Z: Engineering AI Agents
Engineering

Change your data mix to be focused more 
on your target domains (math, code, etc)

Image Credit: Curating 25 Trillion Tokens for LLM 
Pretraining | https://openathena.ai

### Page links

- [Link 1](https://openathena.ai/blog/marin-data-pipeline-overview/#3-learn-the-data-mixture)

## Page 110

CS329Z: Engineering AI Agents
Engineering
Image Credit: The Finetuner's Fallacy: When to 
Pretrain with Your Finetuning Data.  arxiv 2603.16177

Mixing in more of your target domain data 
into “pretraining” tends to help

## Page 111

CS329Z: Engineering AI Agents
Engineering
Image Credit: Midtraining Bridges Pretraining and 
Posttraining Distributions.  arxiv 2510.14865

## Page 112

CS329Z: Engineering AI Agents

Posttraining

## Page 113

CS329Z: Engineering AI Agents

Instruction Finetuning

Image Credit: Scaling Instruction-Finetuned 
Language Models.  arxiv 2210.11416

## Page 114

CS329Z: Engineering AI Agents

Learning from Human Preferences

Image Credit: Training language models to follow 
instructions with human feedback.  arxiv 2203.02155

## Page 115

CS329Z: Engineering AI Agents

Problems with Human Feedback

Slide inspiration: CS329X

• Human annotators can be unreliable

• Everyone has different preferences

• Leads to bad incentives for model optimization (sycophancy, 
authoritativeness)

• The data itself can be sourced unethically

## Page 116

CS329Z: Engineering AI Agents

Reinforcement Learning with Verifiable 
Rewards (RLVR)

• Make the reward verifiable

• Great for math and code!

• Need to be careful about the verifier 
design

Verifiable Rewards

-
Unit Tests 
-
Lean Proof 
-
Exact Match 
-
System state 
-
…

Image Credit: DeepSeekMath: Pushing the Limits of Mathematical 
Reasoning in Open Language Models | arxiv 2402.03300

## Page 117

CS329Z: Engineering AI Agents

Agent-Specific Training (E.g. SWE-Smith)

Image Credit: SWE-smith: Scaling Data for Software 
Engineering Agents | arxiv 2504.21798

## Page 118

CS329Z: Engineering AI Agents

SWE-Smith

Image Credit: SWE-smith: Scaling Data for Software 
Engineering Agents | arxiv 2504.21798

## Page 119

CS329Z: Engineering AI Agents

LLM Inference

Language Models?
Architecture
Training
Inference
LLMs for Agents

## Page 120

CS329Z: Engineering AI Agents

Prefill and Decode

## Page 121

CS329Z: Engineering AI Agents

GPUs

Image Credit: https://developer.nvidia.com/blog/cuda-
refresher-reviewing-the-origins-of-gpu-computing/

### Page links

- [Link 1](https://developer.nvidia.com/blog/cuda-refresher-reviewing-the-origins-of-gpu-computing/)

## Page 122

CS329Z: Engineering AI Agents

Roofline Performance Model

Image Credit: https://docs.nersc.gov/tools/
performance/roofline/

### Page links

- [Link 1](https://docs.nersc.gov/tools/performance/roofline/)

## Page 123

CS329Z: Engineering AI Agents

Prefill and Decode

Image Credit: https://huggingface.co/blog/tngtech/llm-
performance-prefill-decode-concurrent-requests

### Page links

- [Link 1](https://huggingface.co/blog/tngtech/llm-performance-prefill-decode-concurrent-requests)

## Page 124

CS329Z: Engineering AI Agents

)=

Prefill

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO
…
…
…

…

X

X
÷

…
+

Softmax(

+

…
…
…

…

## Page 125

CS329Z: Engineering AI Agents

)=

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

…

X

X
÷

…
+

Softmax(

+

…

Decode

## Page 126

CS329Z: Engineering AI Agents

)=

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

X

X
÷

…
+

Softmax(

+

Clear 
Unimportant

Memory

Decode

## Page 127

CS329Z: Engineering AI Agents

)=

class
The

…
…

+

…
+

…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

…

X

X
÷

…
+

Softmax(

+

…

Decode

## Page 128

CS329Z: Engineering AI Agents

)=

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

X

X
÷

…
+

Softmax(

+

Clear 
Unimportant

Memory

class

…
…
+

…

Decode

## Page 129

CS329Z: Engineering AI Agents

)=

was
class
The

…
…
…

+

…
+
…
+

…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO
…

X

X
÷

…
+

Softmax(

+

…

Decode

## Page 130

CS329Z: Engineering AI Agents

)=

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

X

X
÷

…
+

Softmax(

+

Clear 
Unimportant

Memory

class

…
…
+

…

was

…
…
+

…

Decode

## Page 131

CS329Z: Engineering AI Agents

)=

was
class
about
The

…
…
…
…

+

…
+
…
+
…
+

…
…
…
…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO
…

X

X
÷

…
+

Softmax(

+

…

Decode

## Page 132

CS329Z: Engineering AI Agents

)=

The

…

+

…

Layer Norm(
)

WQ
WK
WV

Q
V
K

T

…
+

+

+

WO

X

X
÷

…
+

Softmax(

+

Clear 
Unimportant

Memory

was
class
about
The

…
…
…
…
+
…
+
…
+

…
…
…

Decode

## Page 133

CS329Z: Engineering AI Agents

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

…
+

K

T
V
KV Cache

## Page 134

CS329Z: Engineering AI Agents

Roofline Performance Model

Image Credit: https://docs.nersc.gov/tools/
performance/roofline/

Prefill
Decode

### Page links

- [Link 1](https://docs.nersc.gov/tools/performance/roofline/)

## Page 135

CS329Z: Engineering AI Agents

Metrics

Image Credit: https://docs.nersc.gov/tools/
performance/roofline/

### Page links

- [Link 1](https://docs.nersc.gov/tools/performance/roofline/)

## Page 136

CS329Z: Engineering AI Agents

Speculative Decoding

Image Inspiration: Speed Up LLM Inference with 
Speculative Decoding | medium.com

a
upon
time
Once

Draft 
Model

Draft 
Model

Draft 
Model

Draft 
Model

time
a
there
upon

a
upon
time
Once

time
a
there
upon

Target Model

### Page links

- [Link 1](https://medium.com/@genai.works/speed-up-llm-inference-with-speculative-decoding-1fc79701e9d6)

## Page 137

CS329Z: Engineering AI Agents

Speculative Decoding

Image Credit: Accelerating Large Language Model 
Decoding with Speculative Sampling | arxiv 2302.01318

Some domains are more

predictable than others

## Page 138

CS329Z: Engineering AI Agents

Inference Time Scaling (Test Time Scaling)

## Page 139

CS329Z: Engineering AI Agents

Chain of Thought

Image Credit: Chain-of-Thought Prompting Elicits 
Reasoning in Large Language Models | arxiv 2201.11903

## Page 140

CS329Z: Engineering AI Agents

Reasoning LLM

A jacket costs $80. The store raises 
its price by 25%, then offers a 25% 
discount on the new price. 
What is the final price?

After the 25% increase, the jacket 
costs: 
$80 × 1.25 = $100. 
The 25% discount applies to that 
new price: 
$100 × 0.75 = $75.

Traditional LLM

Image Inspiration: https://magazine.sebastianraschka.com/p/
controlling-reasoning-effort-in-llms

Query

Adding 25% and subtracting 25% appears to 
produce no change, suggesting a final price of 
$80. 
 
Wait… That cancellation would require both 
percentages to use the same base amount. Here, 
the discount applies to the increased price. 
 
So the increase is 25% of $80, or $20, bringing 
the price to $100.  Then the discount is 25% of 
$100, or $25, bringing the price to $75. 
 
Let me check that.  $80 + $20 − $25 = $75. Okay. 
 
The jacket’s final price is $75, which is $5 less 
than its original price.

Reasoning LLM

### Page links

- [Link 1](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms)

## Page 141

CS329Z: Engineering AI Agents

Reasoning LLM

Image Credit: https://magazine.sebastianraschka.com/p/
controlling-reasoning-effort-in-llms

### Page links

- [Link 1](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms)

## Page 142

CS329Z: Engineering AI Agents
Image Credit: https://openai.com/index/introducing-
gpt-6-sol-and-luna/

Medium

Max

Low

### Page links

- [Link 1](https://openai.com/index/introducing-gpt-6-sol-and-luna/)

## Page 143

CS329Z: Engineering AI Agents

Setting the Reasoning Level (GPT-OSS)

System Prompt

Reasoning: low

System Prompt

Reasoning: medium

System Prompt

Reasoning: high

User Prompt

Solve this math problem...

## Page 144

CS329Z: Engineering AI Agents

Some ways it is done:

Inkling (Thinking Machines)

Set Lambda higher for low effort

Set Lambda lower for high effort

Kimi K3 (Moonshot)

Reward = 1 for correct, 0 for wrong, 
-1 for wrong and exceeds budget

Student

General Task 
Teacher (High)

General Task 
Teacher (Med)

General Task 
Teacher (Low)

General Agent 
Teacher (High)

General Agent

Teacher (Med)

General Agent

Teacher (Low)

Coding Agent 
Teacher (High)

Coding Agent 
Teacher (Med)

Coding Agent 
Teacher (Low)

Multi Teacher Distillation

## Page 145

CS329Z: Engineering AI Agents

Scaling with Repeated Sampling

Image Credit: Large Language Monkeys: Scaling Inference 
Compute with Repeated Sampling | arxiv 2407.21787

## Page 146

CS329Z: Engineering AI Agents

Scaling with Repeated Sampling

Image Credit: Large Language Monkeys: Scaling Inference 
Compute with Repeated Sampling | arxiv 2407.21787

## Page 147

CS329Z: Engineering AI Agents

What if you don’t have a verifier?  Self-Consistency

Image Credit: Self-Consistency Improves Chain of Thought 
Reasoning in Language Models | arxiv 2203.11171

## Page 148

CS329Z: Engineering AI Agents

What if you don’t have a verifier?  Self-Consistency

Image Credit: Self-Consistency Improves Chain of Thought 
Reasoning in Language Models | arxiv 2203.11171

## Page 149

CS329Z: Engineering AI Agents

LLMs for Agents

Language Models?
Architecture
Training
Inference
LLMs for Agents

## Page 150

CS329Z: Engineering AI Agents

## Page 151

CS329Z: Engineering AI Agents

Structured I/O

## Page 152

CS329Z: Engineering AI Agents

Motivating Structured I/O

Image Credit: https://bair.berkeley.edu/blog/2024/02/18/
compound-ai-systems/

Require a shared contract of how these system components will communicate.

### Page links

- [Link 1](../readings/zaharia-et-al-the-shift-from-models-to-compound-ai-systems-bair-blog-2024.md)

## Page 153

CS329Z: Engineering AI Agents

Constrained Decoding

Force the language model to output to a particular structure

Image Credit: SGLang: Efficient Execution of Structured 
Language Model Programs | arxiv 2312.07104

## Page 154

CS329Z: Engineering AI Agents

Constrained Decoding

Force the language model to output to a particular structure

Image Credit: SGLang: Efficient Execution of Structured 
Language Model Programs | arxiv 2312.07104

SGLang has Finite State Machines for decoding (among other optimizations)

## Page 155

CS329Z: Engineering AI Agents

DSPy Signatures

Image Credit: https://dspy.ai/current/

### Page links

- [Link 1](https://dspy.ai/current/)

## Page 156

CS329Z: Engineering AI Agents

DSPy Signatures: Peek inside

System Prompt

User Prompt

\[\[ ## message ## \]\] 
I'm Sarah(sarah@acme.co). Meet Thursday?

Respond with the corresponding output fields, starting with the field \`\[\[ ## name ## \]\]\`, then \`\[\[ ## email ## \]\]\` (must be formatted as a valid Python Union\[str, 
NoneType\]), then \`\[\[ ## intent ## \]\]\` (must be formatted as a valid Python Literal\['meeting', 'intro', 'follow-up'\]), and then ending with the marker for \`\[\[ ## 
completed ## \]\]\`.

Your input fields are: 
1. \`message\` (str): 
Your output fields are: 
1. \`name\` (str): 
2. \`email\` (Union\[str, NoneType\]): 
3. \`intent\` (Literal\['meeting', 'intro', 'follow-up'\]): 
All interactions will be structured in the following way, with the appropriate values filled in.

\[\[ ## message ## \]\] 
{message}

\[\[ ## name ## \]\] 
{name}

\[\[ ## email ## \]\] 
{email}        # note: the value you produce must adhere to the JSON schema: {"anyOf": \[{"type": "string"}, {"type": "null"}\]}

\[\[ ## intent ## \]\] 
{intent}        # note: the value you produce must exactly match (no extra characters) one of: meeting; intro; follow-up

\[\[ ## completed ## \]\] 
In adhering to this structure, your objective is: 
        Extract contact info.

## Page 157

CS329Z: Engineering AI Agents

Constrain the Model: Classifiers

Train a small head on top of embeddings to map to class labels

Image Credit: https://jalammar.github.io/a-visual-guide-to-
using-bert-for-the-first-time/

### Page links

- [Link 1](https://jalammar.github.io/a-visual-guide-to-using-bert-for-the-first-time/)

## Page 158

CS329Z: Engineering AI Agents

Constrain the Model: System One Models

Popular term right now, but roughly classifiers with adaptable options (for “decisions”)

Image Credit: https://contrastive-lm.notion.site/

### Page links

- [Link 1](https://contrastive-lm.notion.site/)

## Page 159

CS329Z: Engineering AI Agents

Example: Tool Calling

Image Credit: Toolformer: Language Models Can 
Teach Themselves to Use Tools | arxiv 2302.04761

## Page 160

CS329Z: Engineering AI Agents

Context Engineering

## Page 161

CS329Z: Engineering AI Agents
Image Credit: https://www.anthropic.com/engineering/
effective-context-engineering-for-ai-agents

### Page links

- [Link 1](../readings/rajasekaran-et-al-effective-context-engineering-for-ai-agents-anthropic-2025.md)

## Page 162

CS329Z: Engineering AI Agents

What goes in the context of an agent?

• System Prompt

• Message History

• Memories

• Tool Call Results

• Attached Files

## Page 163

CS329Z: Engineering AI Agents

Why not just put everything?  Context Rot

Image Credit: OOLONG: Evaluating Long Context 
Reasoning and Aggregation Capabilities | arxiv 2511.02817

## Page 164

CS329Z: Engineering AI Agents

Why not just put everything?  Context Rot

Image Credit: OOLONG: Evaluating Long Context 
Reasoning and Aggregation Capabilities | arxiv 2511.02817

## Page 165

CS329Z: Engineering AI Agents

There is no one way to build the context, 
this will be something you experiment with 
in HW1.

Instead we will provide some practical tips 
and considerations.

Image Credit: OOLONG: Evaluating Long Context 
Reasoning and Aggregation Capabilities | arxiv 2511.02817

## Page 166

CS329Z: Engineering AI Agents

Avoid bloat

Image Credit: https://arena.ai/blog/coding-agents-harness-tax

Sometimes a few tools are all you need.  Pi has just read, write, edit, and bash.

### Page links

- [Link 1](../readings/arena-ai-harnesstax-how-much-does-the-harness-matter-for-coding-agents-arena-blog-2026.md)

## Page 167

CS329Z: Engineering AI Agents

Avoid bloat

Image Credit: https://developer.nvidia.com/blog/build-a-rag-
agent-with-nvidia-nemotron/

Use retrieval to recover the most relevant memories or files

More on this in the next lecture!

### Page links

- [Link 1](https://developer.nvidia.com/blog/build-a-rag-agent-with-nvidia-nemotron/)

## Page 168

CS329Z: Engineering AI Agents

was
class
about
The

…
…
…
…
…
+
…
+
…
+

…
…
…
…

…
+

K

T
V

Add sequentially
Avoid invalidating the KV Cache

## Page 169

CS329Z: Engineering AI Agents

was
class
The

…
…
…
…
+
…
+

…
…
…

…
+

K

T
V
KV Cache

Add sequentially
Avoid invalidating the KV Cache

Actually

…

…

…
+

All of these position embeddings just changed.

Invalidated

## Page 170

CS329Z: Engineering AI Agents

Evaluate context choices empirically
You can setup benchmarks/evals and test your changes

Image Credit: Toolformer: Language Models Can Teach 
Themselves to Use Tools | arxiv 2302.04761

## Page 171

CS329Z: Engineering AI Agents

Compaction

• By the time you reach compaction the context has grown extremely long.

• The new decision is what to keep in the new context.

• Keep too much and you will have to compact again soon.

• Drop too much and you can lose critical context needed to complete the task.

Image Credit: https://www.threads.com/@therundownai

### Page links

- [Link 1](https://www.threads.com/@therundownai)

## Page 172

CS329Z: Engineering AI Agents
Image Credit: Recursive Language Models | arxiv 2512.24601

Different Philosophy:  
Recursive LMs  
(RLMs)

## Page 173

CS329Z: Engineering AI Agents
Image Credit: https://alexzhang13.github.io/blog/2025/rlm/

Recursive LMs (RLMs)

### Page links

- [Link 1](https://alexzhang13.github.io/blog/2025/rlm/)

## Page 174

CS329Z: Engineering AI Agents

Summary

Language Models?
Architecture
Training
Inference
LLMs for Agents

## Page 175

CS329Z: Engineering AI Agents

• What are Language Models?

• Language Model Architecture (Transformers, Linear Attention)

• Language Model Training (Pretraining, Midtraining, Posttraining, Agent 
Training)

• Language Model Inference (Prefill/Decode, Inference Time Scaling)

• LLMs for Agents (Structured I/O, Context Engineering)

Summary

## Page 176

CS329Z: Engineering AI Agents

See you on Wednesday for RAG!
