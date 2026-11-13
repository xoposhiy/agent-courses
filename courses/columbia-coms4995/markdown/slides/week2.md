# Lecture slides: week2

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/assets/lecture_slides/week2.pdf) · [Raw file](../../raw/slides/week2.pdf)

Retrieved: 2026-11-13T16:40:56.350142+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Shreya Havaldar

Week 2

LLM Architectures & 
Training

COMS 4995-15

## Page 2

-
HW 1 is on the website and it is due in 2 weeks!
-
Late days are rounded up

-
1 hr late or 23 hrs late = 1 late day

Auditing

-
This class will likely be offered again!
-
You can come to class + participate in discussions and activities
-
You can attend OH with questions
-
If you do the HWs/project, they will not be graded

Announcements

2

## Page 3

1.
Neural Networks

2.
Training

3.
The Transformer

Today’s Lecture

3

## Page 4

4

-
A neural network is a high-dimensional function f(Θ, x) → y

-
Goal: Map inputs to outputs.
-
LLM-specific output: A probability distribution over a vocabulary.

-
Consist of:

-
Parameters (learned weights + biases) 
-
Input, hidden, output layers
-
Activation functions

Neural networks are 
high-dimensional functions

## Page 5

5

Parameters store the knowledge acquired during training and do not 
change while the model is being used.

Weights: Numerical values representing the strength of 
connections between neurons, adjusted during learning

Biases: Additional parameters that help shift the activation 
function, giving the network more flexibility.

Parameters

## Page 6

6

Example: Perceptron

Input: < 3, 5, 4 >
Weights: <2, 1, 2>

## Page 7

7

Example: Perceptron

Input: < 3, 5, 4 >
Weights: <2, 1, 2>

Weighted sum:
3*2 + 5*1 + 4*2

= 19

## Page 8

8

Example: Perceptron

Input: < 3, 5, 4 >
Weights: <2, 1, 2>
Bias: 1.5

## Page 9

9

Example: Perceptron

Input: < 3, 5, 4 >
Weights: <2, 1, 2>
Bias: 1.5

Weighted sum:
3*2 + 5*1 + 4*2 + 
1.5

= 20.5

## Page 10

10

## Page 11

11

Discuss how many input and output nodes each 
example network would have

Example 3:

Predicting the next 
word in a sentence

Example 1:

Predict if a student will 
pass or fail an exam 
given hours studied, 
attendance %, and GPA

Example 2:

Given an 28x28 image 
of a handwritten digit, 
classify what number it 
is

## Page 12

12

A mathematical function that 
decides whether a neuron should 
"fire" (activate) and pass 
information to the next layer

-
Introduces non-linearity
-
Changes with every 
different input

Activation Functions

## Page 13

13

Example: Perceptron

Input: <3, 5, 4>
Weights: <2, 1, 2>
Bias: -22
Activation: Tanh

## Page 14

14

Example: Perceptron

Input: <3, 5, 4>
Weights: <2, 1, 2>
Bias: -22
Activation: Tanh

Weighted sum: -3
tanh(-3) = -0.995

## Page 15

15

Example: Perceptron

Input: <3, 5, 4>
Weights: <2, 1, 2>
Bias: -22
Activation: ReLU

## Page 16

16

Example: Perceptron

Input: <3, 5, 4>
Weights: <2, 1, 2>
Bias: -22
Activation: ReLU

Weighted sum: -3
relu(-3) = 0

## Page 17

17

Example: Perceptron

Input: <3, 5, 4>
Weights: <2, 1, 2>
Bias: -22
Activation: Sigmoid

## Page 18

18

Example: Perceptron

Input: <3, 5, 4>
Weights: <2, 1, 2>
Bias: -22
Activation: Sigmoid

Weighted sum: -3
sigmoid(-3) = 0.0474

## Page 19

[No extractable text on this page. See the original PDF.]

## Page 20

[No extractable text on this page. See the original PDF.]

## Page 21

1.
Neural Networks

2.
Training

3.
The Transformer

Today’s Lecture

21

## Page 22

Train, Val, Test

22

## Page 23

23

A scalar value 
measuring the 
discrepancy 
between prediction 
and ground truth.

Cost function: 
average loss over 
entire training set

The Loss Function

## Page 24

-
An iterative optimization algorithm used in machine learning to find 
the minimum of a cost or loss function

-
Optimization problem in a high-dimensional landscape

-
All training pipelines use gradient descent/ascent

-
Supervised fine-tuning 
-
Instruction tuning
-
Preference optimization

Gradient Descent

24

## Page 25

1.
The algorithm begins with initial values for the model's parameters.
Gradient Descent

25

## Page 26

2. It computes the gradient (slope) of the cost function, which indicates 
the direction of the steepest increase.

Gradient Descent

26

## Page 27

3. It then updates the parameters by taking a small step in the opposite 
direction of the gradient (the negative gradient), which is the direction of 
steepest decrease.

Gradient Descent

27

## Page 28

4. This process repeats, with each step getting smaller as it approaches 
the minimum, until the model converges (the loss stops changing 
significantly).

Gradient Descent

28

## Page 29

A parameter that controls how much the weights are adjusted with 
respect to the gradient of the loss function during training. It determines 
the step size taken towards the minimum of a loss function

Learning Rate

29

## Page 30

Go to playground.tensorflow.org 
Activity (10 min)

30

Adjust features, layers, 
neurons, activations, and 
learning rate.

### Page links

- [Link 1](http://playground.tensorflow.org)

## Page 31

How are you supposed to determine how much each weight contributes 
to the final error?

Backpropagation is the method for computing those gradients 
efficiently.

Backpropagation

31

## Page 32

A neural network is a chain of functions:

input → layer 1 → layer 2 → ... → output → loss.

Forward pass: feed input through the network, layer by layer, 
computing activations, until you get an output and a loss value.

Backward pass: differentiates the loss function to compute how each 
individual parameter of the network contributes to the overall error for a 
single input.

Backpropagation

32

## Page 33

Compute how much the loss changes with respect to the output

(∂L / ∂output)

Use the chain rule to iteratively calculate the gradient of the loss through 
each layer:

∂L / ∂(Layeri input) 
= ∂L / ∂(Layeri output) · ∂(Layeri output) / ∂(Layeri input)

Layer i’s input = Layer i-1’s output
→can iterate backwards through L-1, L-2, L-3, … Layer 1

Backpropagation

33

## Page 34

[No extractable text on this page. See the original PDF.]

## Page 35

1.
A forward pass, making predictions on training data.

2.
A loss function measures the error of the model’s predictions during 
that forward pass.

3.
Backpropagation of error, or a backward pass, to calculate the partial 
derivatives of the loss function.

4.
Gradient descent, to update model weights.

The training loop

## Page 36

36

Activity (45 min)

Watch the following videos:

●
https://www.3blue1brown.com/lessons/gradient-descent/

●
https://www.3blue1brown.com/lessons/backpropagation/

Complete gradient_descent.py (on the class website)

Quiz Code: W34JK9

### Page links

- [Link 1](https://www.3blue1brown.com/lessons/backpropagation/)
- [Link 2](https://www.3blue1brown.com/lessons/gradient-descent/)

## Page 37

1.
Look up what “local minima” are. How can you modify training to 
escape a local minimum?

2.
If training loss goes down but test loss rises, what is happening? 
What are 2–3 actions you could take, and what outcome would you 
expect from each?

3.
If both training and test loss don’t go down, what is happening? 
What are 2–3 actions you could take, and what outcome would you 
expect from each?

Discussion

37

## Page 38

1.
Neural Networks

2.
Training

3.
The Transformer

Today’s Lecture

38

## Page 39

A specific kind of network architecture. It is still a feedforward neural 
network, but based on attention.

The transformer

39

## Page 40

1.
Token embedding converts text 
into continuous vectors

2.
Positional encoding introduces 
sequence order

3.
Self-attention layers compute 
token-to-token relationships

4.
Feed-forward layers transform 
representations

5.
Stacked blocks enable deep 
hierarchical features

Components of the Transformer

40

## Page 41

Raw Text to Tokens

41

## Page 42

How is text split into tokens? Via a tokenization algorithm

●
“unbelievable” → “un | believ | able”
●
“GPT-5?” → “GPT”, “-”, “5”, “?”
●
Emojis → each emoji is usually a token
●
URLs → often split into many tokens

Why a good tokenization algorithm matters for efficiency.

-
Tokens too short: text is broken up into too many pieces
-
Tokens too long: the model can’t generalize to unseen words

Raw Text to Tokens

42

## Page 43

Exercise: How does each tokenization scheme handle the following words
Training words: “burning”, “satisfactory”, “information”
Text to Tokens: Exercise

43

Word-Level
Subword
Character-level

burning
satisfactory
information

burn
#ing
satis
#fac#
#tory
inform
#a#
#tion

b
u 
r
n
i
g
s
… etc.

1.
Which vocabulary produces 
the fewest tokens overall for 
the training words?

2.
Which vocabulary is the 
most flexible for unseen 
words?

## Page 44

Exercise: How does each tokenization scheme handle the following words
Unseen words: “satisfaction”, “informing”
Text to Tokens: Exercise

44

Word-Level
Subword
Character-level

burning
satisfactory
information

burn
#ing
satis
#fac#
#tory
inform
#a#
#tion

b
u 
r
n
i
g
s
… etc.

1.
Which vocabulary produces 
the fewest tokens overall for 
the unseen words?

2.
Which vocabulary is the 
least efficient for unseen 
words?

## Page 45

Embeddings

45

## Page 46

What do embeddings capture?

●
Semantic similarity
●
Syntactic roles
●
Frequency-based structure

Why are embeddings useful?

●
Numerical representation of language
●
Words used similarly are close in vector space

Embeddings are learned from next-token prediction during LLM training

Embeddings

46

## Page 47

Embeddings: Exercise

47

## Page 48

Embeddings: Exercise

48

## Page 49

Embeddings: Exercise

49

## Page 50

We can’t simply use “femininity”, “youth”, or “royalty” to describe all words in the 
English language

More on embeddings:

●
Each dimension doesn’t measure a clear construct; it’s quite complex
●
Common dimensionality is 300-700
●
But, research shows that enough is captured to do “word math” with 
embeddings

○
“king – man + woman ≈ queen”
○
“doctor – hospital + school ≈ teacher”

Step 2: Embeddings

50

## Page 51

Components of the Transformer

51

1.
Token embedding converts text into 
continuous vectors

2.
Positional encoding introduces 
sequence order

3.
Self-attention layers compute 
token-to-token relationships

4.
Feed-forward layers transform 
representations

5.
Stacked blocks enable deep 
hierarchical features

## Page 52

Transformers 
process tokens in 
parallel

Positional encodings 
allow transformers 
to know the order of 
tokens

Positional Encodings

52

## Page 53

Components of the Transformer

53

1.
Token embedding converts text into 
continuous vectors

2.
Positional encoding introduces 
sequence order

3.
Self-attention layers compute 
token-to-token relationships

4.
Feed-forward layers transform 
representations

5.
Stacked blocks enable deep 
hierarchical features

## Page 54

They are static! The embedding for a word doesn't reflect how its meaning 
changes in context.

The chicken didn't cross the road because it was 
too tired

What is the meaning represented in the static embedding for "it"?

Problem with static word 
embeddings

54

## Page 55

●
Intuition: a representation of meaning of a word should be different in 
different contexts!

●
Contextual Embedding: each word has a different vector that expresses 
different meanings depending on the surrounding words

●
How to compute contextual embeddings?

○
Attention!!

Contextual Embeddings

55

## Page 56

The chicken didn't cross the road because it

What should be the properties of "it"?

The chicken didn't cross the road because it was too tired 
The chicken didn't cross the road because it was too wide

At this point in the sentence, it's probably referring to either the chicken or 
the street

Contextual Embeddings

56

## Page 57

Build up the contextual embedding from a word by selectively integrating 
information from all the neighboring words

We say that a word "attends to" some neighboring words more than others

Intuition of attention

57

## Page 58

Intuition of attention

58

## Page 59

A mechanism for helping compute the contextual embedding for a token 
by selectively attending to and integrating information from surrounding 
tokens (at the previous layer).

In practice: computed using a weighted sum of vectors.

So, what is attention?

59

## Page 60

Vectors learned during training

Attention score 
A(i,j)

= dot(v_i,  v_j)

= how much 
token i attends 
to token j

Contextualized 
vector for “station” 
= weighted sum of 
all token vectors by 
attention to 
“station”

## Page 61

61

## Page 62

Components of the Transformer

62

1.
Token embedding converts text into 
continuous vectors

2.
Positional encoding introduces 
sequence order

3.
Self-attention layers compute 
token-to-token relationships

4.
Feed-forward layers transform 
representations

5.
Stacked blocks enable deep 
hierarchical features

## Page 63

Components of the Transformer

63

1.
Token embedding converts text into 
continuous vectors

2.
Positional encoding introduces 
sequence order

3.
Self-attention layers compute 
token-to-token relationships

4.
Feed-forward layers transform 
representations

5.
Stacked blocks enable deep 
hierarchical features

## Page 64

1.
Explain the architecture of a transformer. What makes it different from 
RNNs and LSTMs?

2.
A transformer’s context window is the number of tokens it can take as 
input. What happens to the number of attention scores as the context 
window increases?

Discussion

64
