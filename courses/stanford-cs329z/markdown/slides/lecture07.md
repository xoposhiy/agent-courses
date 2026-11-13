# Lecture 7: Agent Memory Architectures

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture07.pdf) · [Raw file](../../raw/slides/lecture07.pdf)

Retrieved: 2026-11-13T16:22:31.099004+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Agent Memory Architectures

Diyi Yang, Michael Ryan, John Yang

CS329Z: Engineering AI Agents

## Page 2

CS329Z: Engineering AI Agents

Announcements

• Laude Institute provided everyone with $200 more Amazon credits 
through partnership with AWS!

• Details on obtaining this will be sent out soon.

• HW1 due on October 30th (2 weeks and 2 days!)

## Page 3

CS329Z: Engineering AI Agents

…

Image Credit: https://andonlabs.com/blog/ai-bosses-2

## Page 4

CS329Z: Engineering AI Agents
Image Credit: https://x.com/summeryue0/status/2025774069124399363

“Check this inbox too and suggest what you would 
archive or delete, don’t action until I tell you to.”

## Page 5

CS329Z: Engineering AI Agents

Memory is essential for long-
running, multi-session agents.

Today we will introduce types of 
agent memory and a few concrete

agent memory architectures.

## Page 6

CS329Z: Engineering AI Agents

Learning Objectives

• Recognize the importance of memory in multi-session/user-facing 
agent systems.

• Differentiate architectures for agent memory based on their design 
patterns.

• Identify ongoing challenges with agent memory.

## Page 7

CS329Z: Engineering AI Agents

Lecture Overview

• Motivating Agent Memory (5 minutes)

• Review: Types of Agent Memory (10 minutes)

• Agent Memory Architectures (35 minutes)

• Evaluating Agent Memory (15 minutes)

• Challenges and Open Problems (10 minutes)

## Page 8

CS329Z: Engineering AI Agents

Motivating Agent Memory

Motivation
Memory Types
Architectures
Evaluation
Challenges

## Page 9

CS329Z: Engineering AI Agents

Problems without memory

• Loss of procedure: Every time you 
need to teach the agent the task again.

• Loss of knowledge: Important facts, 
rules, and preferences can be lost 
between sessions.

• Loss of progress: As sessions grow 
longer the agent can forget what it did, 
earlier goals, earlier instructions, etc.

## Page 10

CS329Z: Engineering AI Agents

Benefits of Agent Memory

• Personalization: Agents can learn your 
personal preferences.

• Learning from Experience: Agents can 
learn skills in one session and apply 
them later.

• Statefulness: You can continue where 
you left off in new conversations (e.g. 
“Open up the proposal we were 
working on again”)

## Page 11

CS329Z: Engineering AI Agents

Personalization: Example \[Jiang et al., 2025\]

Image Credit: https://arxiv.org/pdf/2504.14225v2#page=2

## Page 12

CS329Z: Engineering AI Agents

Learning from experience: Example \[Wang et al., 2024\]

Image Credit: https://arxiv.org/pdf/2409.07429

## Page 13

CS329Z: Engineering AI Agents

Statefulness: Example \[Du et al., 2025\]

Image Credit: https://arxiv.org/pdf/2505.20231v2#page=1

## Page 14

CS329Z: Engineering AI Agents

Types of Agent Memory

Motivation
Memory Types
Architectures
Evaluation
Challenges

## Page 15

CS329Z: Engineering AI Agents

Cognitive Architectures for 
Language Agents (CoALA)  
\[Sumers et al., 2024\]

### Page links

- [Link 1](../readings/arxiv-2309-02427.md)

## Page 16

CS329Z: Engineering AI Agents

CoALA \[Sumers et al., 2024\]

Image Credit: https://arxiv.org/pdf/2309.02427

## Page 17

CS329Z: Engineering AI Agents

Working Memory

Image Credit: https://www.anthropic.com/engineering/building-effective-agents

• Typically the Context Window.

• What the agent currently sees 
and is reasoning over

• Includes observations, goals, user 
input, and internal reasoning.

## Page 18

CS329Z: Engineering AI Agents

Episodic Memory

Image Credit: https://arxiv.org/pdf/2304.03442

• Sequences of the agents past 
behaviors (trajectories)

• In chatbots this is a store of all the 
prior conversations.

• Typically the raw logs of what 
occurred.

## Page 19

CS329Z: Engineering AI Agents

Semantic Memory

Image Credit: https://openai.com/index/memory-and-
new-controls-for-chatgpt/

• Stores facts about the world.

• Details about the user, 
preferences, general knowledge, 
etc. all fall under semantic 
memory.

• This is what people typically think 
of for chatbot memory.

## Page 20

CS329Z: Engineering AI Agents
Image Credit: https://platform.claude.com/cookbook/skills-
notebooks-01-skills-introduction

Procedural Memory

• The set of rules that can be 
applied to the working memory to 
determine the agents behavior.

• Essentially the skills of the agent.

• The knowledge of HOW to 
complete tasks.

## Page 21

CS329Z: Engineering AI Agents

Parametric vs Context Memory

Parametric
Context

• Built into the model weights

• Semantic: Pre-trained knowledge

• Procedural: Instruction following

• Episodic: Not Applicable

• Can be fine-tuned to add more 
knowledge or skills.

• Added to the model context

• Semantic: Retrieved Facts

• Procedural: Retrieved Skills

• Episodic: Retrieved conversations

• Managed by the context manager 
to pull the appropriate memories.

## Page 22

CS329Z: Engineering AI Agents

Recap

Table Credit: CS329Z Lecture 1

### Page links

- [Link 1](lecture01.md)

## Page 23

CS329Z: Engineering AI Agents

Agent Memory Architectures

Motivation
Memory Types
Architectures
Evaluation
Challenges

## Page 24

CS329Z: Engineering AI Agents

Key Questions: What, When, and How?

• What will get stored to/retrieved from memory?

• When will we trigger the memory storage/retrieval?

• How will we store memories/retrieve from memory?

• Facts (specific and general), Procedures, Conversation Progression, …

• Agent tools (on-demand), background workers, event-driven, …

• Filesystem, databases (retrieval), knowledge graphs, …

## Page 25

CS329Z: Engineering AI Agents

How: Three Systems for Memory

• Underlying memory we need some way to get/store information to 
your disk.

• Three most common approaches are: Filesystem, Database, and 
Knowledge Graphs.

## Page 26

CS329Z: Engineering AI Agents

Memory Systems: Filesystem

Image Credit: https://www.langchain.com/blog/
how-we-built-agent-builders-memory-system

• Every memory is a file.

• Can let the agent 
manage it’s memories.

• Adds hierarchy by 
default.

• Grep, ls, and other 
bash commands are 
the memory tools.

## Page 27

CS329Z: Engineering AI Agents

Memory System: Database

• Can build a vector database and 
retrieve memories from it.

• Also common to use an SQLite 
database if you want to search over 
metadata.

• For exact term lookup you can use 
BM25.

• Recall our RAG lecture!

## Page 28

CS329Z: Engineering AI Agents

Memory System: Knowledge Graph \[Rasmussen et al.,  2025\]

Image Credit: https://blog.dailydoseofds.com/p/
hands-on-build-an-ai-agent-with-human

Image Credit: https://www.getzep.com/

Zep

### Page links

- [Link 1](https://arxiv.org/pdf/2501.13956)

## Page 29

CS329Z: Engineering AI Agents

Pattern Overview

• Learning Procedures from Experience: Recall past successful 
trajectories.

• Tiered Memory Hierarchy: Organize long-term and short-term 
memory.

• Reflective Memory Consolidation: Reflect on the memories before 
storing them.

• Memory Maintenance: Clean up and remove/update old memories.

## Page 30

CS329Z: Engineering AI Agents

Pattern 1: Learning Procedures 
from Experience

## Page 31

CS329Z: Engineering AI Agents

Voyager \[Wang et al., 2023\]

Image Credit: https://arxiv.org/pdf/2305.16291

## Page 32

CS329Z: Engineering AI Agents

Voyager Skill Library

Image Credit: https://arxiv.org/pdf/2305.16291

## Page 33

CS329Z: Engineering AI Agents

Voyager Skill Library

Image Credit: https://arxiv.org/pdf/2305.16291

The Skill Library enables Voyager to craft diamond tools in 102 prompt iterations

Without the skill library this was never achieved.

## Page 34

CS329Z: Engineering AI Agents

Voyager Skill Library

Image Credit: https://arxiv.org/pdf/2305.16291

## Page 35

CS329Z: Engineering AI Agents

Agent Workflow Memory (AWM) \[Wang et al., 2024\]

Image Credit: https://arxiv.org/pdf/2409.07429

## Page 36

CS329Z: Engineering AI Agents

AWM Inducing the “Workflows”

Image Credit: https://arxiv.org/pdf/2409.07429

## Page 37

CS329Z: Engineering AI Agents

AWM “Workflows”

Image Credit: https://arxiv.org/pdf/2409.07429

These are included in the system prompt as context when solving the task.

## Page 38

CS329Z: Engineering AI Agents

AWM Results

Image Credit: https://arxiv.org/pdf/2409.07429

## Page 39

CS329Z: Engineering AI Agents

Skill Files

Image Credit: https://platform.claude.com/cookbook/skills-
notebooks-01-skills-introduction

## Page 40

CS329Z: Engineering AI Agents

Skill Files

Image Credit: https://platform.claude.com/docs/en/agents-
and-tools/agent-skills/overview

## Page 41

CS329Z: Engineering AI Agents

Limitation

• These procedural memory stores are 
not robust to dynamic environments. 
\[Cao et al., 2026\]

• Skill files are the common solution for 
generalist user-facing agents (can 
also be updated).

???

### Page links

- [Link 1](https://arxiv.org/pdf/2512.10696)

## Page 42

CS329Z: Engineering AI Agents

Pattern 2: Tiered Memory 
Hierarchy

## Page 43

CS329Z: Engineering AI Agents

MemGPT \[Packer et al., 2024\]

Image Credit: https://arxiv.org/pdf/2310.08560

Key Insight: Give the LLM tools to manage its own memory

## Page 44

CS329Z: Engineering AI Agents

MemGPT \[Packer et al., 2024\]

Image Credit: https://arxiv.org/pdf/2310.08560

Key Insight: Give the LLM tools to manage its own memory

Vector Database
String/Date Lookup

Messages are FIFO

## Page 45

CS329Z: Engineering AI Agents

Memory Functions: Write/Replace

Image Credit: https://arxiv.org/pdf/2310.08560

Working Context Write
Working Context Replace

Similar tools for archival memory, but not for recall memory.

## Page 46

CS329Z: Engineering AI Agents

Memory Functions: Search

Image Credit: https://arxiv.org/pdf/2310.08560

Recall Storage
Archival Storage

No need to search working memory since it is in context.

## Page 47

CS329Z: Engineering AI Agents

MemGPT Results

Slide Credit: CS224N

### Page links

- [Link 1](https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture10-rag-agents.pdf)

## Page 48

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2506.06326

MemoryOS \[Kang et al., 2025\]

## Page 49

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2506.06326

MemoryOS \[Kang et al., 2025\]

Short Term 
Memory

Medium Term 
Memory

Long Term 
Persona Memory

## Page 50

CS329Z: Engineering AI Agents

Pattern 3: Reflective Memory 
Consolidation

## Page 51

CS329Z: Engineering AI Agents

Refresher: Reflexion \[Shinn et al., 2023\]

Image Credit: https://arxiv.org/pdf/2303.11366

## Page 52

CS329Z: Engineering AI Agents

Refresher: Importance of Reflecting

Image Credit: https://arxiv.org/pdf/2303.11366

## Page 53

CS329Z: Engineering AI Agents

Generative Agents \[Park et al., 2023\]

Image Credit: https://arxiv.org/pdf/2304.03442

## Page 54

CS329Z: Engineering AI Agents

Generative Agents \[Park et al., 2023\]

Image Credit: https://arxiv.org/pdf/2304.03442

## Page 55

CS329Z: Engineering AI Agents

Generative Agents \[Park et al., 2023\]

Image Credit: https://arxiv.org/pdf/2304.03442

## Page 56

CS329Z: Engineering AI Agents

Generative Agents \[Park et al., 2023\]

Image Credit: https://arxiv.org/pdf/2304.03442

## Page 57

CS329Z: Engineering AI Agents

Pattern 4: Memory Maintenance

## Page 58

CS329Z: Engineering AI Agents

Sleep Time Compute \[Lin et al., 2025\]

Image Credit: https://arxiv.org/pdf/2504.13171

## Page 59

CS329Z: Engineering AI Agents

Sleep Time Compute \[Lin et al., 2025\]

Image Credit: https://www.letta.com/blog/sleep-time-compute/

## Page 60

CS329Z: Engineering AI Agents

Sleep Time Compute \[Lin et al., 2025\]

Image Credit: https://arxiv.org/pdf/2504.13171

## Page 61

CS329Z: Engineering AI Agents

A-Mem: Agentic Memory for LLM Agents \[Xu et al., 2025\]

Image Credit: https://arxiv.org/pdf/2502.12110

Key Idea: Build an Agent just for Memory Management

## Page 62

CS329Z: Engineering AI Agents

A-Mem: Agentic Memory for LLM Agents \[Xu et al., 2025\]

Image Credit: https://arxiv.org/pdf/2502.12110

## Page 63

CS329Z: Engineering AI Agents

Mem0 \[Chhikara et al., 2025\]

Image Credit: https://arxiv.org/pdf/2504.19413

## Page 64

CS329Z: Engineering AI Agents

Mem0 \[Chhikara et al., 2025\]

Image Credit: https://arxiv.org/pdf/2504.19413

A background memory workflow detects conflicts and automatically updates memories.

Four memory actions to resolve: ADD, UPDATE, DELETE, and NOOP

## Page 65

CS329Z: Engineering AI Agents

Recap

## Page 66

CS329Z: Engineering AI Agents

Recap

## Page 67

CS329Z: Engineering AI Agents

Evaluating Agent Memory

Motivation
Memory Types
Architectures
Evaluation
Challenges

## Page 68

CS329Z: Engineering AI Agents

Desiderata

• Realistic: Both the memory source (haystack) and the 
queries should reflect real scenarios.

• Long-Context: No need to benchmark memory on 
short conversations.

• Challenging: If the benchmark is too easy it won’t 
distinguish failures of systems.

• Verifiable: We should know when the system 
succeeds or fails at the task.

## Page 69

CS329Z: Engineering AI Agents

Overview

• LoCoMo: Multi-task benchmark over many long simulated 
conversations with agents role-playing as users.

• PersonaMem: Personal preference based multiple choice over many 
simulated user conversations with evolving preferences.

• LongMemEval-v2: Web agent trajectory detail recall with diverse 
human-written queries.

• MemoryArena: Multi-task verifiable completion benchmark with 
progressively building subtasks.

## Page 70

CS329Z: Engineering AI Agents

LoCoMo \[Maharana et al., 2024\]

Evaluating Very Long-Term Conversational Memory of LLM Agents

### Page links

- [Link 1](https://aclanthology.org/2024.acl-long.747.pdf)

## Page 71

CS329Z: Engineering AI Agents

LoCoMo \[Maharana et al., 2024\]

Image Credit: https://aclanthology.org/2024.acl-long.747.pdf

## Page 72

CS329Z: Engineering AI Agents

Constructing LoCoMo

Image Credit: https://aclanthology.org/2024.acl-long.747.pdf

Uses the “Generative 
Agents” Architecture.

## Page 73

CS329Z: Engineering AI Agents

LoCoMo RAG Results

Image Credit: https://aclanthology.org/2024.acl-long.747.pdf

Even when models get the right memories they can’t always use them.

## Page 74

CS329Z: Engineering AI Agents

LoCoMo Properties

• Realistic: Simulated Conversations between users is not exactly what 
we care about agents retrieving from.

• Long-Context: 16.6k tokens per conversation

• Challenging: Multi-task, adversarial

• Verifiable: Question Answering has ground truth

🟨

🟨

✅

✅

People have multiple conversations and their preferences change over time

We can simulate conversations with assistant agent instead of between users ➡

## Page 75

CS329Z: Engineering AI Agents

PersonaMem \[Jiang et al., 2025\]

### Page links

- [Link 1](https://arxiv.org/pdf/2504.14225)

## Page 76

CS329Z: Engineering AI Agents

PersonaMem \[Jiang et al., 2025\]

Image Credit: https://arxiv.org/pdf/2504.14225

## Page 77

CS329Z: Engineering AI Agents

PersonaMem \[Jiang et al., 2025\]

Image Credit: https://arxiv.org/pdf/2504.14225

## Page 78

CS329Z: Engineering AI Agents

PersonaMem \[Jiang et al., 2025\]

## Page 79

CS329Z: Engineering AI Agents

PersonaMem \[Jiang et al., 2025\]

Image Credit: https://arxiv.org/pdf/2504.14225
Memory/RAG are essential, and Mem0 helps with preference evolution/recent preferences

## Page 80

CS329Z: Engineering AI Agents

PersonaMem Properties

• Realistic: Simulated Conversations between user and agents is better 
but multiple choice questions are not a realistic representation of 
how agents will need to use the information.

• Long-Context: Up to almost 1M tokens in a conversation

• Challenging: Multiple choice with distractors

• Verifiable: Multiple choice has ground truth

🟨

🟨

✅

✅

What if we could have memory over agent trajectories 
rather than just conversations?
➡

## Page 81

CS329Z: Engineering AI Agents

LongMemEval-v2 \[Wu et al., 2026\]

### Page links

- [Link 1](https://arxiv.org/abs/2605.12493)

## Page 82

CS329Z: Engineering AI Agents

LongMemEval-v2 \[Wu et al., 2026\]

Image Credit: https://arxiv.org/pdf/2605.12493

## Page 83

CS329Z: Engineering AI Agents

LongMemEval-v2 \[Wu et al., 2026\]

Image Credit: https://arxiv.org/pdf/2605.12493

## Page 84

CS329Z: Engineering AI Agents

LongMemEval-v2 Construction

Image Credit: https://arxiv.org/pdf/2605.12493

• Obtain rollouts on four WebArena 
environments with Codex (GPT-5.2 and 
GPT-5-mini).

• Manually curate questions spanning 5 
categories.

• Ensure only a few trajectories could 
answer the question.

• Generate a haystack (100-500 trajectories 
that don’t answer the question)

## Page 85

CS329Z: Engineering AI Agents

LongMemEval-v2 Results

Image Credit: https://arxiv.org/pdf/2605.12493
Filesystem based memory with GPT-5.4-mini
Retrieval based memory with Qwen3.5 9B

Filesystem memory outperforms retrieval here, although better model advantage

## Page 86

CS329Z: Engineering AI Agents

LongMemEval-v2 Properties

• Realistic: Agent trajectories is even more realistic for agents, but still 
asking multiple choice questions about old observations

• Long-Context: Hundreds of millions of tokens in trajectories

• Challenging: Only few trajectories in a huge haystack has the answer

• Verifiable: Multiple choice has ground truth

🟨

✅

✅

Can we test agents on solving realistic/diverse problems 
rather than multiple choice?
➡

✅

## Page 87

CS329Z: Engineering AI Agents

MemoryArena \[He et al., 2026\]

### Page links

- [Link 1](https://arxiv.org/pdf/2602.16313)

## Page 88

CS329Z: Engineering AI Agents

MemoryArena \[He et al., 2026\]

Image Credit: https://arxiv.org/pdf/2602.16313

## Page 89

CS329Z: Engineering AI Agents

MemoryArena \[He et al., 2026\]

Image Credit: https://arxiv.org/pdf/2602.16313

## Page 90

CS329Z: Engineering AI Agents

MemoryArena \[He et al., 2026\]

Image Credit: https://arxiv.org/pdf/2602.16313

## Page 91

CS329Z: Engineering AI Agents

MemoryArena \[He et al., 2026\]

Image Credit: https://arxiv.org/pdf/2602.16313

Memory controllers 
were *weakest* 
method here.

Lots of headroom!

Since this is a real and 
complex task, failure 
cannot entirely be 
attributed to memory.

## Page 92

CS329Z: Engineering AI Agents

MemoryArena Properties

• Realistic: Four distinct, realistic evaluation environments.

• Long-Context: Hundreds of thousands of tokens in trajectories.

• Challenging: Solving real tasks with many building constraints.

• Verifiable: The constraints on the solutions are verifiable.

✅

✅

✅

✅

## Page 93

CS329Z: Engineering AI Agents

Recap

## Page 94

CS329Z: Engineering AI Agents

Recap
Good agent memory evals should be realistic, long-context, challenging and verifiable.

Image Credit: https://arxiv.org/pdf/2605.12493

These are all popular and pretty good examples!

## Page 95

CS329Z: Engineering AI Agents

Challenges and Open Problems

Motivation
Memory Types
Architectures
Evaluation
Challenges

## Page 96

CS329Z: Engineering AI Agents

Challenges and Open Problems

• Choosing what to remember and to forget: Future relevance is 
unknown when the memory is created.

• Trust, Privacy, and User Control: Memory is an attack vector for 
agents.  Also user memories have important privacy implications.

• Using Memory Correctly: Many instances of over-personalization due 
to misused memories.

## Page 97

CS329Z: Engineering AI Agents

Choosing what to remember and what to forget

• Future relevance is unknown 
when a memory is created.

• Keeping everything increases 
retrieval, context, and 
maintenance costs.

• Forgetting can remove useful 
evidence or unresolved 
commitments.

\[Ma et al., 2026\]

Memory or joke???  Which aspect to remember?

## Page 98

CS329Z: Engineering AI Agents

Trust, Privacy, and User Control \[Chen et al., 2024\]

Possible to trigger 
model to act on 
poisoned procedural 
memories to take 
dangerous behaviors.

Image Credit: https://arxiv.org/pdf/2407.12784

## Page 99

CS329Z: Engineering AI Agents

Trust, Privacy, and User Control \[Shao et al., 2025\]

Agents interact with the 
world without fully 
understanding what you 
wish to keep private.

Doing so with memory 
can expose personal 
details.

Image Credit: https://arxiv.org/pdf/2409.00138

## Page 100

CS329Z: Engineering AI Agents

Using Memory Correctly \[Hu et al., 2026\]

• LLMs are sometimes over-eager 
to use what is in their context.

• This can be resolved with either 
better retrieval or better 
training LLMs to ignore 
unimportant context, but 
neither is fully solved.

• Some users like personalization 
more than others.

Image Credit: https://arxiv.org/pdf/2601.13722v2#page=33

## Page 101

CS329Z: Engineering AI Agents

Summary

Motivation
Memory Types
Architectures
Evaluation
Challenges

## Page 102

CS329Z: Engineering AI Agents

Summary

• Motivating Agent Memory

• Types of Agent Memory

• Agent Memory Architectures

• Evaluating Agent Memory

• Challenges and Open Problems

## Page 103

CS329Z: Engineering AI Agents

See you Monday for Multi-Agent

Systems!
