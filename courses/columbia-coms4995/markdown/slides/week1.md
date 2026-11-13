# Lecture slides: week1

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/assets/lecture_slides/week1.pdf) · [Raw file](../../raw/slides/week1.pdf)

Retrieved: 2026-11-13T16:40:56.295132+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Shreya Havaldar

Week 1

What is an Agent? 
A brief history of 
language modeling

COMS 4995-15

## Page 2

Introductions

Aaditya (TA)
Shreya

## Page 3

A little about me!

-
From LA + Orange County

-
Graduated from USC in 2021!

-
Got my PhD at Penn in May 2026

Researched sociotechnical alignment 
of LLMs (how personal + cultural 
context influence what a “correct 
generation” should be)

My mom + my dog!

## Page 4

A few things to note

1.
This is the first time this class is being offered at Columbia
2.
There will (inevitably) be some bumps in the road! We will work 
them out!!
3.
This course will be equal parts computer science and design.

Welcome!

4

## Page 5

What you’ll get from this course

1.
A basic understanding of how LLMs work
2.
Overview of agentic design principles
3.
Insights into how agents are being used in academia + industry
4.
Hands-on project where you build an agent!

5

Welcome!

Course website: https://designing-agents.github.io/

### Page links

- [Link 1](../pages/index.md)

## Page 6

Full use of AI agents is allowed for coding components of HWs and the final 
project

-
Main goal: learn how agents fit into your workflow, and practice 
orchestration and delegation

Because of this, what you put in is what you get out

-
This course (likely) won't be stressful
-
It's on to take charge of your own learning

6

Expected difficulty

## Page 7

Grades will be 45% homeworks, 35% final project, and 20% participation.

-
HWs are individual
-
Final project is in groups of 3
-
Participation is based on attendance + contribution during class labs

-
You are allowed to miss class 2 times without penalty
-
No exams!!

7

Grading

## Page 8

-
Yes! if you have…

-
No ML experience
-
Some ML experience

-
Taken 1-2 ML courses, but feel you would benefit from a 
refresher 
-
Not done too many applied AI projects
-
Curiosity about how agents work and are built!
-
Willingness to engage with and talk to your peers

8

Is this course for me?

## Page 9

-
Probably not, if you have…

-
Extensive ML experience

-
Taken multiple ML courses
-
Fully understand how LLMs are trained, improved, and 
deployed
-
Completed many applied AI projects
-
Built any type of agent yourself already
-
Prefer classes where attendance/participation is optional

* Come talk to me after class if you’re not sure

9

Is this course for me?

## Page 10

-
AI tools are allowed for coding tasks, provided you fully understand 
and can explain any code you submit.

-
AI delegation is NOT allowed for writing components of assignments.

-
Short-answer questions in the HWs
-
Design document for final project
-
Note: collaboration != delegation

-
You have 3 late days you can use as needed

10

Policies

## Page 11

Class will (typically) consist of:

-
Around 75 min of lecture
-
Around 45 min of in-class labs / activities

-
Proof of completion will serve as attendance

I will do my best to get you out of here by 9pm!!

It is okay to eat dinner in class (as long as it’s not disruptive)


11

Lecture Format

## Page 12

1.
History of language modeling

2.
Defining the AI Agent

Today’s Lecture

12

## Page 13

The Evolution of language models

## Page 14

The Rule-Based Era (1950s – 1990s)

Early researchers viewed 
language as a set of 
logical puzzles. If you 
could map every 
grammatical rule, you 
could "solve" language.

## Page 15

The Turing Test (1950)

Alan Turing proposed 
that if a machine 
could mimic human 
conversation 
perfectly, it could be 
considered "thinking."

## Page 16

The Turing Test (1950)

CAPTCHA (Completely 
Automated Public Turing 
test to tell Computers and 
Humans Apart)

## Page 17

Chomskyan Linguistics

Noam Chomsky argued for "Universal 
Grammar" — the idea that humans have an 
innate, rule-based biological structure for 
language.

Computers tried to mimic this with 
Context-Free Grammars (CFGs).

## Page 18

Chomskyan Linguistics

Controversial viewpoint — other

linguists believed there was no

set of grammatical rules that

1.
spanned all languages
2.
humans inherently knew

## Page 19

CFGs

A formal system in computer science that uses recursive rules 
to describe the structure of languages.

## Page 20

Activity: Rules for WSD

WSD = Word Sense Disambiguation

For example, does “date” mean

(1) a dried fruit 
(2) a romantic meeting
(3) a calendar day

Get into groups of 2!

## Page 21

Activity: Rules for WSD

Phase 1: Build Your “Date” Rules (20 Minutes)

Write strict rules that ONLY using logic. Examples:

IF "love" is in the sentence, THEN it is a romantic meeting.
IF "january" is in the sentence, THEN it is a calendar day.

def disambiguate_date(input_sentence):

…
return {“dried_fruit”, “romantic date”, “calendar_day”}

## Page 22

Activity: Rules for WSD

Phase 2: Break someone else’s “Date” Rules (10 Minutes)

IF "love" is in the sentence, THEN it is a romantic meeting.
IF "january" is in the sentence, THEN it is a calendar day.

→ I have a Hinge date planned in January
→I love to put dates in my smoothie

Feel free to use AI tools!

## Page 23

Activity: Rules for WSD

Submit the sentence you used to break your opponent’s system on 
courseworks for attendance credit

Code: 6G4YC

## Page 24

The Statistical Shift (1990s – 2010s)

Key Question:

How do you model data where context 
matters over time?

## Page 25

The Statistical Shift (1990s – 2010s)

The world is too messy for rules!

Instead of rules, researchers began 
using large corpora (like the Wall Street 
Journal, Wikipedia, etc.) to calculate 
the probability of word sequences.

## Page 26

N-Grams

Predicting the nth word based on 
the previous n-1 words.

This is fundamentally a Markov 
Chain — the future state depends 
only on the current state, not the 
entire past history

## Page 27

N-Grams: an example

Corpus:

I like cats
I like dogs
I love cats
You like dogs

## Page 28

N-Grams: an example

Corpus:

I like cats
I like dogs
I love cats
You like dogs

Vocabulary: 
{I, You, like, love, cats, dogs}

## Page 29

N-Grams: an example

Corpus:

I like cats
I like dogs
I love cats
You like dogs

Vocabulary: 
{I, You, like, love, cats, dogs}

Create a bigram model

for this corpus:

P(wt | wt-1)

## Page 30

N-Grams: an example

Current word
Next word
Count

I
like
2

I 
love

You
like

like
cats

like
dogs

love
cats

Corpus:

I like cats
I like dogs
I love cats
You like dogs

## Page 31

N-Grams: an example

Current word
Next word
Count

I
like
2

I 
love
1

You
like
1

like
cats
1

like
dogs
2

love
cats
1

Corpus:

I like cats
I like dogs
I love cats
You like dogs

## Page 32

N-Grams: an example

Current word
Next word
Count

I
like
2

I 
love
1

You
like
1

like
cats
1

like
dogs
2

love
cats
1

P(like | I) = ⅔

P(love | I) = ?

P(dogs | like) = ?

P(cats | like) = ?

## Page 33

N-Grams: an example

Current word
Next word
Count

I
like
2

I 
love
1

You
like
1

like
cats
1

like
dogs
2

love
cats
1

P(like | I) = ⅔

P(love | I) = ⅓

P(dogs | like) = ⅔

P(cats | like) = ⅓

## Page 34

N-Grams: an example

P(like | I) = ⅔

P(love | I) = ⅓

P(dogs | like) = ⅔

P(cats | like) = ⅓

What would this model generate with the 
Prompt:

“I …”

## Page 35

N-Grams: an example

P(like | I) = ⅔

P(love | I) = ⅓

P(dogs | like) = ⅔

P(cats | like) = ⅓

Would this model ever generate:

1.
“I love dogs”?

2.
“I hate cats”?

## Page 36

Deep Learning (2010s)

-
Motivation: learn representations so similar words and contexts can 
share information

-
Not possible with purely statistical methods like n-gram modeling

-
Increased availability of GPUs → deeper, multi-layer architectures

## Page 37

Deep Learning (2010s)

-
2012 AlexNet breakthrough on ImageNet proved the power of deep 
convolutional neural networks: cut previous error rate in ~ half

-
Designed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton

## Page 38

The Vector Revolution (2013)

The introduction of Word2Vec and GloVe. Instead of representing the 
word "Apple" as a unique ID, we represented it as a point in a 
300-dimensional space.

Key Insight: "You shall know a word by the company it keeps." 
→ Words with similar meanings (e.g., "King" and "Queen") were 
mathematically closer together.

## Page 39

[No extractable text on this page. See the original PDF.]

## Page 40

Recurrent Neural Networks (RNNs)

RNNs process tokens one by one, maintaining a "hidden state."

## Page 41

Recurrent Neural Networks (RNNs)

The Problem: The "Vanishing Gradient." As the input sentence grows, the 
influence of the first word on the last word decays to zero.

## Page 42

LSTMs (Long Short-Term Memory)

Introduced gates and and a cell state

-
Gates control the flow of information into and out of the cell state
-
Input, Forget, and Output gates
-
Cell state acts as a persistent memory conveyor belt.

Solved the vanishing gradient problem!

## Page 43

[No extractable text on this page. See the original PDF.]

## Page 44

LSTMs (Long Short-Term Memory)

New problem: Still sequential.

-
You cannot parallelize the training. 
-
You must wait for word #1 to finish before starting word #2.

## Page 45

The Transformer & Scaling Laws (2017 – 
Present)

The paper "Attention is 
All You Need" removed 
the sequence requirement 
entirely.

## Page 46

The Transformer

Self-Attention: Every 
word in a sentence 
looks at every other 
word at the same 
time. This allows the 
model to understand 
global context 
instantly.

## Page 47

Scaling Laws

Researchers discovered that as you increase the number of parameters 
and the amount of data, the "Loss" (error) decreases in a predictable power 
law. This led to the race for trillion-parameter models.

## Page 48

LLMs 
today

## Page 49

1.
History of language modeling

2.
Defining the AI Agent

Today’s Lecture

49

## Page 50

From Completion to Agency

Passive LLM: You give it a prompt, and it gives you a completion. It has no 
memory of the world and no way to change it.

Active Agent: An agent is Autonomous, Reactive, and Proactive. It can 
observe a result, realize it made a mistake, and try a different approach.

## Page 51

Definition

An agent is a system that chooses and executes actions based on

intermediate results.

## Page 52

[No extractable text on this page. See the original PDF.]

## Page 53

The Cognitive Architecture of an Agent

1.
Planning
2.
Memory
3.
Tool Use / Action
4.
Perception

## Page 54

The Cognitive Architecture of an Agent

1.
Planning

a.
Task Decomposition: The agent breaks a "Goal" into "Steps."
b.
Self-Reflection: The agent looks at its own output and asks, "Does 
this make sense?" (e.g., the Self-Refine or Reflexion frameworks).
c.
Chain of Thought (CoT): Forcing the model to "show its work" 
step-by-step, which significantly reduces logic errors.

## Page 55

The Cognitive Architecture of an Agent

1.
Planning

1.
Memory

a.
Short-term: The conversation history stored in the context window.
b.
Long-term: Vector Databases (using RAG or other retrieval 
mechanisms). The agent can "search" its past experiences or 
external documents to inform its current action.

## Page 56

The Cognitive Architecture of an Agent

1.
Planning 
2.
Memory

1.
Tool Use / Action

a.
Function Calling: The model doesn't just write text; it outputs a 
specific piece of code that a computer can execute.
b.
The MRKL (Miracle) Architecture: Modular reasoning, knowledge, 
and language.

i.
A system that combines an LLM with "expert" tools (like a 
calculator or a weather API).

## Page 57

The Cognitive Architecture of an Agent

1.
Planning
2.
Memory 
3.
Tool Use / Action

1.
Perception

a.
Modern agents are often Multimodal. They don't just "read" the 
internet; they can "see" a screenshot of a website or "hear" a user's 
voice command.
b.
Inputs from different modalities can be processed together to give 
the agent a better understanding of its task

## Page 58

The ReAct Pattern (Reasoning + Acting)

The most common agentic loop is ReAct:

Example: “How many women are there in Paris?”

Step 1 (Thought): "I need to find the population of Paris and divide it by 2."
Step 2 (Action): Search("Population of Paris")
Step 3 (Observation): "The search result says 2.1 million."
Step 4 (Thought): "Now I need to use the calculator tool."
Step 5 (Action): Calculate(2100000 / 2)

## Page 59

Activity: Applying ReAct (15 min)

Get into groups of 3-4. Pick an open-ended problem 
(e.g. plan a 1-week trip to Paris on a 500 euro budget)

Sketch out how an agent would approach this problem

1.
Planning: How does the agent break this down? 
2.
Tool Use: Which APIs/external tools are needed?
3.
Memory: What does it need to "retrieve" from the user’s 
past data to succeed? 
4.
Perception: What real-time data must it "observe" to 
make a decision?

## Page 60

Announcements

-
There are many people on the waitlist! If you plan to drop, please lmk 
sooner rather than later

-
Come talk to me right now if you’re unsure whether this class is a good 
fit for you

-
Reminder to sign up for EdStem + Gradescope
