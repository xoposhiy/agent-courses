# Lecture slides: week4

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/assets/lecture_slides/week4.pdf) · [Raw file](../../raw/slides/week4.pdf)

Retrieved: 2026-11-13T16:40:57.198773+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Shreya Havaldar

Week 4

Prompting, Reasoning, & 
Memory

COMS 4995-15

## Page 2

-
HW 1 due today at 11:59 pm EST

-
Reminder: 3 late days per semester
-
HW 2 will be released tomorrow

Announcements

2

## Page 3

1.
Prompting
2.
Reasoning techniques 
3.
Memory management

Today’s Lecture

3

## Page 4

Key framing:

Prompts are not questions; they are specifications

Prompts!

4

## Page 5

Main components:

1.
Goal (what success means)

2.
Inputs (what is provided; what is missing)

3.
Constraints (must/never; policy; style; length)

4.
Output format (schema; sections; deterministic formatting)

5.
Acceptance tests (2–5 examples of correct/incorrect outputs)

Prompts as specifications

5

## Page 6

Prompts always involve instructions and context passed to an LLM to 
achieve a desired task.

Prompt engineering is the practice of developing and optimizing these 
prompts.

Prompt Engineering

6

## Page 7

Use consistent blocks to reduce ambiguity and improve debugging:

Role/Task: “You are … your task is …”

Rules: bullet list, straightforward information

Context: any needed facts or data

Output format: exact schema + “no extra text”

Examples: correct and incorrect (if needed)

Typical prompt layout

7

## Page 8

1.
Start simple

a.
Prompting is an iterative process!
b.
Experiment, tweak the prompt, repeat

Three main things to remember: 
specificity, simplicity, and conciseness

Design Tips

8

## Page 9

2. Break things down into subtasks

a.
LLMs are (usually) bad at doing many complex things at once
b.
Helps you keep your prompts simple and specific.
c.
Iteratively break down components your LLM struggles with

Design Tips

9

## Page 10

3. Be clear about the task and expected output

a.
The more descriptive the prompt is, the better the results
b.
But… too many (unnecessary) details may degrade results
c.
Examples are almost always beneficial

Design Tips

10

## Page 11

“Explain the concept prompt engineering. Keep the 
explanation short, only a few sentences, and don't 
be too descriptive”

-
Length of explanation ❌
-
Style of explanation ❌

A bad prompt

11

## Page 12

“Use 2-3 sentences to explain the concept of prompt 
engineering to a high school student.”

-
Length of explanation ✅
-
Style of explanation ✅

A better prompt

12

## Page 13

“You are an agent that recommends movies to a 
customer. DO NOT ASK FOR INTERESTS. DO NOT ASK FOR 
PERSONAL INFORMATION.”

-
Output constraints ❌
-
Edge cases ❌

A bad prompt

13

## Page 14

“You are an agent that recommends movies to a 
customer. The agent should recommend a movie from 
the top global trending movies. It should not ask 
users for their preferences or personal information. 
If the agent doesn't have a movie to recommend, it 
should respond “Sorry, no movie available””

-
Output constraints ✅
-
Edge cases ✅

A better prompt

14

## Page 15

Soft Prompting

15

Soft prompting is a parameter-efficient technique that uses learned 
embeddings instead of human-readable text to guide LLMs

1.
Appends trainable vectors (also called “virtual tokens”) directly to the input 
embedding sequence.

2.
Keeps the core LLM weights completely frozen during the learning process.

3.
Gradient Optimization: Updates only the small set of prompt parameters via 
backpropagation using a task-specific training dataset.

## Page 16

Soft Prompting

16

## Page 17

Soft Prompting

17

Opaque and completely 
unreadable to humans. 
Works well for a highly 
specialized task, but not 
popular nowadays.

Fully transparent and easy 
for humans to read + debug

## Page 18

Templates exist for most basic LLM tasks (like those here!)

-
Text Summarization
-
Information Extraction
-
Question Answering
-
Text Classification
-
Code Generation

Also useful: https://chatgpt.com/use-cases/students

Prompting templates

18

### Page links

- [Link 1](https://chatgpt.com/use-cases/students)
- [Link 2](https://www.promptingguide.ai/introduction/examples)

## Page 19

Good practice: exponential backoff

19

## Page 20

Good practice: caching

20

Prompt caching 
improves efficiency 
and reduces costs for 
repeat queries

## Page 21

21

def ask(prompt: str, temperature: float = 0.0) -> str:

"""

Written for you. Sends one prompt to MODEL and returns the reply text.

Every reply is saved to .autoprompting_cache.json, and an identical request

returns the saved reply, even at a temperature above 0. Delete the file to

draw fresh replies. Waits and retries when the free tier's rate limit is

hit.

"""

global _client

request = {"model": MODEL, "prompt": prompt, "temperature": temperature}

key = hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()

cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}

if key in cache:

return cache\[key\]

if _client is None:

... < NORMAL API CALL CODE >

hashlib.sha256() 
Converts any text or 
file into a unique, 
fixed 64-character 
hexadecimal string

## Page 22

Good practice: API key safety

22

In terminal:

export GEMINI_API_KEY=<your_api_key>

In your code:

api_key=os.environ\["GEMINI_API_KEY" \]

-
Storing API keys as environment 
variables is the industry 
standard for preventing 
accidental credential leaks

-
Allows you to safely share or 
commit your codebase without 
exposing secret keys

## Page 23

1.
Prompting
2.
Reasoning techniques 
3.
Memory management

Today’s Lecture

23

## Page 24

Reasoning in LLMs refers to the capability of models to solve complex, 
multi-step problems by breaking them down into intermediate, logical, and 
sequential steps

What is reasoning?

24

## Page 25

Reasoning in LLMs refers to the capability of models to solve complex, 
multi-step problems by breaking them down into intermediate, logical, and 
sequential steps

Reasoning in prompts: Taking any LLM and prompting it in a way that 
elicits reasoning capabilities

Reasoning models: LLMs that have been fine-tuned to internally reason 
before generating an output

What is reasoning?

25

## Page 26

Reasoning techniques typically help for:

-
Multi-step arithmetic
-
Multi-constraint decisions
-
Compositional tasks
-
Multi-hop QA.

They often don’t help for:

-
Missing knowledge
-
Ambiguous tasks
-
Tasks better solved by tools

When reasoning prompts help

26

## Page 27

CoT improves multi-step reasoning by eliciting intermediate steps
→ “let’s think step-by-step”

Chain-of-Thought (CoT)

27

## Page 28

Types of CoT prompting:

Zero-shot: task description only, with no examples given

Few-shot: task description with some amount of examples

8-shot: task description with exactly 8 examples

When to use CoT: multi-step math, symbolic manipulation, compositional 
reasoning, planning subproblems.

Chain-of-Thought (CoT)

28

## Page 29

Generic scaffold:

List the constraints
Break into 3–6 substeps
Solve each substep
Assemble final answer in the required format

“Least-to-most” style decomposition: Start with easy subquestions; use 
them as givens for the harder step.

Decomposition

29

## Page 30

Uses sampling to choose the highest likelihood answer

1.
Set the temperature to a higher value

a.
→ increases diversity in generations

2.
Have the LLM produce N independent solutions

3.
Choose the majority, or “most consistent” generation

Self-consistency

30

## Page 31

Generic scaffold:

Define “thought” unit (partial solution / subplan)
Generate k candidates
Score candidates (model-based evaluation, verifier)
Expand best nodes until depth/timeout
Return best leaf + justification

Generalizes CoT into a search over “thoughts” (branches), enabling 
exploration and lookahead, improving problems requiring search.

Tree of Thoughts (ToT)

31

## Page 32

-
Offloads execution 
correctness to a runtime 
(e.g., Python)

-
Reduces arithmetic or 
logical slip-ups in final 
computation.

-
Good for problems 
needing mathematical 
reasoning

Program-Aided Language (PAL)

32

## Page 33

Reflexion converts feedback into self-reflections stored in memory.

These reflections are re-used in subsequent trials.

→ Improving performance without fine-tuning.

Generic scaffold:

Attempt → Evaluate → Write reflection → Next attempt 
conditioned on reflection

Reflexion

33

## Page 34

The LLM has to “verify” it’s answer before continuing

-
Self-consistency: Majority vote for single-answer tasks.

-
Checker model: critique + conditioned regeneration.

-
Tool-based verification: compute with interpreter; retrieve citations; 
cross-check constraints.

-
Invariant checks: schema validity (e.g. correct json), policy 
constraints, numeric sanity checks

Self-verification

34

## Page 35

-
Constraint drop: the LLM ignores a must/never rule

-
Premature closure: answers before considering all constraints

-
Spurious precision: invents missing values

-
Non-robust in long context: fails when the relevant fact is not near 
the beginning/end

* Research shows that LLM performance can degrade when relevant information is positioned 
in the middle of a long input prompt, even for long-context models.

Reasoning failure modes

35

## Page 36

Prompt engineering for complex reasoning problems is a challenging task. 
This motivated reasoning models!

Reasoning models generate internal chains of intermediate steps, 
then select and refine a final answer.

Reasoning Models

36

## Page 37

During generation, an LLM:

1.
Tokenizes the input

2.
Runs a forward pass

3.
Gets a set of logits for every token in its vocabulary

4.
Converts these logits to a probability distribution over tokens

5.
Selects the output token using this distribution

6.
Appends the output token to the generation; repeats

Recap: standard LLM inference

37

## Page 38

Same as standard inference, but…

-
The LLM first generates “thinking tokens”

-
Structured intermediate reasoning traces

-
Thinking step-by-step, decomposition, verification, etc.

-
These “thinking tokens” are not part of the final answer

Reasoning LLM inference

38

## Page 39

[No extractable text on this page. See the original PDF.]

## Page 40

https://aistudio.google.com/ (use your PERSONAL email)

1.
Make an API key
2.
Run pip install -U google-genai
3.
Download gemini.py from the class website and make sure you can 
run it

* You will need your API key for future activities and HW 2!

Gemini: Getting an API key

40

### Page links

- [Link 1](http://gemini.py)
- [Link 2](https://aistudio.google.com/)

## Page 41

Google AI Studio https://aistudio.google.com/

41

### Page links

- [Link 1](https://aistudio.google.com/)

## Page 42

Google AI Studio https://aistudio.google.com/

42

### Page links

- [Link 1](https://aistudio.google.com/)

## Page 43

Google AI Studio https://aistudio.google.com/

43

### Page links

- [Link 1](https://aistudio.google.com/)

## Page 44

Google AI Studio https://aistudio.google.com/

44

Please start the HWs early!!
You get 500 free queries per day 
with gemini-3.5-flash-lite

### Page links

- [Link 1](https://aistudio.google.com/)

## Page 45

1.
Prompting
2.
Reasoning techniques 
3.
Memory management

Today’s Lecture

45

## Page 46

“Memory” for an LLM means context selection and presentation.

-
Your LLM should “remember” pieces of information from prior queries

-
You must strategically manage relevant information from prior 
exchanges to maintain coherence.

Memory

46

## Page 47

[No extractable text on this page. See the original PDF.]

## Page 48

Example: a travel agent

Short: current conversation with user

Facts: USD exchange rates, weather 
information, flight prices/times, etc.

Long: user’s dietary restrictions, likes + 
dislikes, preferred generation style, etc.

## Page 49

In sequential memory chaining, you append everything.

Pros: Easy to implement, you append each new turn and include the 
entire conversation chain as the input

Cons: Quickly runs into context limits. Only useful for very short 
sessions

Sequential chain

49

## Page 50

In sliding window memory, you append only the N last turns.

Pros: Also easy to implement, you keep a fixed-size recent window and 
drop older turns.

Cons: Does not run into context limits, but can drop important 
information from earlier turns

Sliding window

50

## Page 51

In summary-based memory, you periodically summarize the 
conversation

Pros: You can maintain longer-term context under token limits

Cons: Requires iteration to determine how to best summarize 
information for your specific application

Summary-based memory

51

## Page 52

Summary-based compaction 
replaces older conversation turns 
with an LLM-generated summary 
to stay within context window 
limits + shrink input length for a 
conversation

What is kept during compaction 
(files, tool outputs, user inputs, etc.) 
varies depending on task.

## Page 53

Agentic memory in practice

Ways to store information an agent must remember

1.
Context window
2.
In-Memory Cache
3.
Relational Database
4.
NoSQL Database
5.
Vector Database + Embeddings

## Page 54

Agentic memory in practice

Ways to store information an agent must remember

1.
Context window: LLM must process immediate, active conversation history
2.
In-Memory Cache: Sub-millisecond retrieval of active session states
3.
Relational Database: Store structured data (e.g. chat logs, user accounts, billing 
records)
4.
NoSQL Database: Store highly dynamic or unstructured data (e.g. agent trace logs)
5.
Vector Database + Embeddings: Perform semantic searches to pull contextually 
relevant facts based on meaning, not exact keywords (RAG)

## Page 55

Example: a travel agent

Short: current conversation with user 
(context window)

Facts: USD exchange rates, weather 
information, flight prices/times, etc. 
(relational database)

Long: user’s dietary restrictions, likes + 
dislikes, preferred generation style, etc. 
(NoSQL database)

## Page 56

Step 1: Think of an LLM task that requires multiple turns, has evolving 
constraints, depends on remembering prior decisions, and fails if earlier 
information is forgotten

Step 2: Design a memory store that includes (1) a method to extract 
relevant information from a conversation, and (2) a storage schema for 
this information under 500 total tokens

Discussion (10 min)

56
