# How to RAG without hallucination

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-freetext.pdf) · [Raw file](../../raw/slides/l-freetext.pdf)

Retrieved: 2026-11-13T16:49:47.008157+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Stanford CS224v Course
Conversational Virtual Assistants with Deep Learning

Lecture 5

Minimizing Hallucination in 
Retrieval-Augmented Generation

(A lesson in Agent Engineering)

1

Monica Lam & Sina Semnani

WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia 
Sina J. Semnani, Violet Z. Yao*, Heidi C. Zhang*, Monica S. Lam
In Proceedings of Association for Computational Linguistics: EMNLP 2023, Singapore, December 6-10, 2023.
Winner of the Wikimedia’s Research of the Year Award, 2024.

### Page links

- [Link 1](../readings/arxiv-2305-14292.md)

## Page 2

H ALLUCINATION IS S TILL R AMPANT WITH RAG T ODAY

M A S S C O N S UM E R A I  S UM M A RI E S ,  N Y T

J O UR N A LI S M ,  B BC

L A W,  S T A N F O RD

S C I E N CE ,  N A T UR E

M E D I C I N E,  O P E NE VI D E N CE

## Page 3

STANFORD
LAM

• Conversational Q&A in open domain with 97% accuracy

• In Proceedings of Association for Computational Linguistics: 
EMNLP, Singapore, December 2023.

• Winner of the Wikimedia’s Research of the Year Award, 2024

## Page 4

STANFORD
LAM

Lecture Outline

• Design and engineering of Wikichat

• Evaluation

## Page 5

W IKIC HAT P ROJECT
T OOK 3 S TUDENTS X 4 M ONTHS!

( S T A R TE D A S A CS 2 2 4 V  P R OJ E C T)

E VALUATION T OOK A NOTHER 2-3 MONTHS!

W HY? LLM S K EEP H ALLUCINATING!

## Page 6

STANFORD
LAM

NLP Research in 2022

• The classic NLP development methodology:

• Create a dataset (train, eval, test)
“Annotations in existing NLP datasets are full of mistakes!

LLM-generated results are better!”
“There is no single golden answer. How do we compare?”

• Train
“Fine-tuning on a problem-specific dataset

can make LLMs worse (and it is very expensive)”.

We need to invent the engineering and evaluation methodology

for LLM-based agents

## Page 7

STANFORD
LAM

Agent Engineering Methodology

1. Design the metrics

2. Start with the most general instruction

3. Debug until you can’t break it

•
Test with “critical” examples

•
Root-cause analysis of LLM errors

•
Add/refine the steps

•
Add rationale to the prompt; 
add critical examples as an aid

4. Evaluate

•
Tests must cover the hardest cases

•
Test with LLM-simulated chats 
with hard, varied personalities

•
Evaluate with an LLM

•
If LLM disagrees with human

•
Use human evaluation

•
Test with real users

Systematically create well-tested step-by-step algorithms

Good news: Debugging with critical examples achieves high Wikichat quality.

The key: Look at the errors!

## Page 8

STANFORD
LAM

Metrics for Conversational Agents

• Relevant

• Informational

• Saying “I don’t know” is penalized under this metric.

• Natural

• Non-Repetitive

• Temporally Correct

• Chatbots should provide up-to-date information 
and use the appropriate tense

## Page 9

STANFORD
LAM

Grounding LLMs with Wikipedia

• We assume access to a knowledge source, 
in the form of a collection of text documents

• We choose the English Wikipedia

• Large scale (4.3B words in 6.7M articles)

• Open-domain: talk about “everything”

• A ton of prior work to compare to

• Publicly available for reproducibility

If we can handle Wikipedia, we can handle other large corpora

## Page 10

WikiChat

## Page 11

STANFORD
LAM

WikiChat Demo

https://wikichat.genie.stanford.edu/

35K+ questions so far, in 10+ languages

Words from conversations

translated into English

### Page links

- [Link 1](https://wikichat.genie.stanford.edu/)

## Page 12

STANFORD
LAM

Basic RAG (Retrieval Augmented Generation)

Question

Retrieved

Data

LLM
question
answering
Answer
Information

Retrieval

Quiz: is this hallucination-free?

## Page 13

STANFORD
LAM

General Approach: 
Formalize our Human Cognitive Process

Combine

Information Retrieval

(factuality)

LLM Generation

(factuality
conversationality)

Question

Answer

## Page 14

STANFORD
LAM

What do you think about the 
casting of Oppenheimer?

LLM (Conversationality + Factuality)

Traditional (Factuality)

1 & 2. Search, summarize, filter:
• Much of the Oppenheimer 
(2023) movie’s cast signed on 
between September 2021 and 
April 2022.
• Cilian Murphy is to play as 
Robert Oppenheimer in the 
Oppenheimer (2023) movie.

4. Extract claims:
• Christopher Nolan is known for his meticulous casting choices.
• Christopher Nolan often casts well-known actors in his films.
• Tom Hanks stars in the Oppenheimer (2023) movie.
• Michael Caine stars in the Oppenheimer (2023) movie.

5. Filter incorrect claims:
• Christopher Nolan is known for his meticulous casting choices.
• Christopher Nolan often casts well-known actors in his films.

7. Refine: Christopher Nolan has cast Cillian Murphy as the titular role of Oppenheimer, keeping with his 
tradition of meticulous casting choices. I’m sure it will be an excellent film!

3. GPT: Christopher Nolan is known for his meticulous casting 
choices. He often casts well-known actors in his films, and this 
time he has selected Tom Hanks and … Michael Caine.

6. Draft: Cillian Murphy has been cast to play Robert Oppenheimer in Christopher Nolan's 
"Oppenheimer" movie. Christopher Nolan is known for his meticulous casting choices and often casts 
well-known actors in his films. The movie's cast was signed on between September 2021 and April 2022.

## Page 15

The 7-Stage WikiChat Pipeline

1. Query

Retrieve

Retrieve

## Page 16

STANFORD
LAM

Basic RAG Pipeline

Question

Retrieved

Data

LLM
question
answering
Answer
Information

Retrieval

Retrieval must return the right document for accuracy

S T A G E 1 :  R E T RI E V A L

## Page 17

STANFORD
LAM

Retrieving from a Large Corpus

ColBERT Information Retrieval (IR)
•
Find the document that best 
matches a question
•
Highest similarity score between 
query and chunk of document
•
Fine-tune BERT on MS MARCO (2016)
•
Passage ranking for questions

Retrieving the right article is critical to the 
success of retrieval-based methods

https://microsoft.github.io/msmarco/

Similarity score between

Query and Document

S T A G E 1 :  R E T RI E V A L

## Page 18

STANFORD
LAM

M3 Embedding
(Multi-lingual Documents)

Find the document that best matches a question

•
Fine-tune XLM-R on 17 multilingual passage ranking datasets

•
And some synthetic data too

•
Multilingual: > 100 languages

•
Multifunctional: dense, multi-vector and sparse retrieval

•
Multigranularity: short sentences to long documents

•
Wikichat updated to use M3: multi-lingual.

Similarity score between

Query and Document

M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation, Chen et al, Findings of ACL August 
2024

S T A G E 1 :  R E T RI E V A L

## Page 19

STANFORD
LAM

Quiz: What’s Wrong with this Conversation?

Time of the conversation: March 2023; 
Retrieved data1:

‘House of the Dragon’ won the Golden Globe Best Television Series in January 2023.

Retrieved data2:

‘House of the Dragon’ Earns Two Golden Global Nominations,  Dec. 2022

…
User: Why else do you think it is a good drama?
Chatbot: The first season received highly positive reviews, … 
In January 2023, the series is expected to win the Golden Globe Award 
for Best Television Series - Drama.

S T A G E 1 :  R E T RI E V A L

## Page 20

STANFORD
LAM

Problem: Context of Retrieved Information vs. Now

• LLMs are trained with all past knowledge all at once

• Does not have a good model of the passage of time

• We need to tell it “the current time”

S T A G E 1 :  R E T RI E V A L

## Page 21

STANFORD
LAM

Solution: Provide the Time/place Context

1. Query Prompt

Time context is included in every prompt!

S T A G E 1 :  R E T RI E V A L

## Page 22

The 7-Stage WikiChat Pipeline

1. Query

Retrieve

Retrieve

## Page 23

Retrieved result
+ Filter each paragraph separately

24

x
1. Query

2. Summarize & Filter

Retrieve

Output

S T A G E 2 :  A N SW E R IN G W IT H R E T RI E V E D I N F O

## Page 24

STANFORD
LAM

Prompt 2: Summarize & Filter

S T A G E 2 :  A N SW E R IN G W IT H R E T RI E V E D I N F O

## Page 25

Problem 3: LLM’s Generation May Not be Factual

LLM may hallucinate.
How to fact-check generation?

1. Query

Retrieve

3. Generate

S T A G E 3 :  L L M  G E N E R A T I ON

## Page 26

+ Extract Claims + Fact-check

1. Query

2. Summarize & Filter

Retrieve

3. Generate 
4. Extract Claims

5. Fact-

check

S T A G E 4 - 5 :  F A C T- C H E C K I N G L L M  G E N E R A T I ON

-5

Output

## Page 27

STANFORD
LAM

Why is Fact-Checking Hard? Example

S T A G E 4 - 5 :  F A C T- C H E C K I N G L L M  G E N E R A T I ON

## Page 28

STANFORD
LAM

Why is Fact-Checking Hard? Example

Just a part of the response is false!

Correct: only top 2 teams qualified
But there was indeed a third place match!

S T A G E 4 - 5 :  F A C T- C H E C K I N G L L M  G E N E R A T I ON

## Page 29

People Fact-Checking People for People

•
Journalists fact-check politicians all the time:

•
Identify the claims

https://www.nytimes.com/2023/08/03/us/politics/trump-indictment-fact-check.html

S T A G E 4 - 5 :  F A C T- C H E C K I N G L L M  G E N E R A T I ON

## Page 30

People Fact-Checking People for People

•
Journalists fact-check politicians all the time:

•
Identify the claims

•
Score them

S T A G E 4 - 5 :  F A C T- C H E C K I N G L L M  G E N E R A T I ON

## Page 31

People Fact-Checking Bots

•
Reduce the complexity of fact-checking with two assumptions:

•
Factuality is only meaningful 
when measured against a source of ground truth

•
Wikipedia

•
Newspapers trust their own prior publications

•
If claims are atomic, each claim is either true or false

•
Factuality: #(fact-checked claims)

#claims

S T A G E 4 - 5 :  F A C T- C H E C K I N G L L M  G E N E R A T I ON

## Page 32

Fact-Checking an LLM Response

Identify the claims made
For each claim:

1. Search the ground truth to find relevant docs

2. Verify if the claim is supported

User: I would like to talk about the 
2023 Australian Open Men’s singles 
tennis championship. Did you hear 
about it?
Chatbot: Yes, I did hear about it! Novak 
Djokovic won the 2023 Australian Open 
Men’s singles tennis championship, 
claiming his tenth Australian Open title 
and 22nd major title overall. It was an 
impressive victory!

…

Many claims in a sentence: 
For each claim

Claim is supported

or not?

Retrieve

S T A G E 4 - 5 :  F A C T- C H E C K I N G L L M  G E N E R A T I ON

Output

## Page 33

STANFORD
LAM

Performance on Fact-Checking

• Claim Identification

• Can be done well using GPT-4

• Need to ensure that the claims are self-contained

• Search

• Can be done well using state-of-the-art IR

• Fact check a statement against a given paragraph

• Automatic SOTA has ~67% F1 with fine-tuned LLaMA
or 83.2% F1 with few-shot ChatGPT

Automatic Evaluation of Attribution by Large Language Models, Yue  et al, arXiv 2023
FactScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation, Min et al, arXiv 2023

Not so good!

S T A G E 4 - 5 :  F A C T- C H E C K I N G L L M  G E N E R A T I ON

Must evaluate by hand

## Page 34

+ Draft + Refine

1. Query

Retrieve

Retrieve

S T A G E 6 - 7 :  C O MB I N I N G R E T RI E V A L W IT H G E N E R A T I ON

## Page 35

STANFORD
LAM

Problem: LLMs Still May Hallucinate

• If we simply ask LLMs to answer based on the combination

• May still hallucinate!

• Hardest thing for LLMs to say: “I don’t know”

• It likes to hallucinate

• When no information remains in a topic

• Draft is prompted to say: ”Sorry, I don’t know”

S T A G E 6 - 7 :  C O MB I N I N G R E T RI E V A L W IT H G E N E R A T I ON

## Page 36

STANFORD
LAM

Summary of WikiChat (7 Prompts)

1.
Formulate query from input
•
Retrieve documents (M3)
2.
Filter each retrieved doc

3.
Ask GPT to generate answer

4.
Extract claims

5.
Fact-check/remove each claim

•
Retrieve documents (M3)

6.
Draft
7.
Refine

Retrieval (Factuality)

LLM (Conversationality + Factuality)

# LLM calls: 5 + n + c
n: # documents retrieved based on user queries

c: # claims generated

## Page 37

STANFORD
LAM

LLM Engineering

1. Design the metrics

2. Start with the most general instruction

3. Debug until you can’t break it

•
Test with “critical” examples

•
Root-cause analysis of LLM errors

•
Add/refine the steps

•
Add rationale to the prompt; 
add critical examples as an aid

4. Evaluate

•
Tests must cover the hardest cases

•
Test with LLM-simulated chats 
with hard, varied personalities

•
Evaluate with an LLM

•
If LLM disagrees with human

•
Use human evaluation

•
Test with real users

Systematically create well-tested step-by-step algorithms  (computational thinking)

Good news: Debugging with critical examples achieves high Wikichat quality.

The key: Look at the errors!

RECAP

## Page 38

STANFORD
LAM

Lecture Outline

• Design and engineering of Wikichat

• Evaluation

## Page 39

STANFORD
LAM

Old Data Sets Do Not Work

No simple numeric benchmark to iterate on

•
Evaluation conversations in the past were crowdsourced

•
Ask crowdworkers to talk to each other about a familiar topic

•
Have blind spots like tail or expert topics

•
Evaluation conversations were static

•
Get outdated quickly

•
Wizard of Wikipedia dataset topics in GPT-3’s pre-training data

•
New benchmarks used for pre-training in the future

## Page 40

STANFORD
LAM

How to Eval WikiChat?

• How to evaluate tail questions?

• Humans do not know tail topics!

• How to evaluate LLM conversations?

• How to compare the results between systems
since their dialogue diverges after the first turn!

• Cannot get a numeric result to measure success

• How to minimize human effort, cost, and potential errors?

Solution: LLMs come to the rescue!

## Page 41

STANFORD
LAM

How to Evaluate WikiChat

1.
Generate simulated conversations
•
The user is GPT-4; the agent is the Chat pipeline
•
Different conversations: 
•
Head (most viewed pages);  
•
Tail (least viewed pages); 
•
Recent (most edited in 2023)
2.
Are LLM conversations similar to human conversations?

•
Improve and Assess
•
Prompt with different user profiles 
to generate diverse user input; eyeball result 
•
Prove with Evaluation
•
Conduct user study on a subset, show the results match

## Page 42

Simulation Prompt

## Page 43

STANFORD
LAM

Evaluation

Simulated

User

Head/Tail/Recent

LLM chatbot

Conversation Generation

User: I would like to talk about the 2023 
Australian Open Men’s singles tennis 
championship. Did you hear about it?
Chatbot: Yes, I did hear about it! Novak 
Djokovic won the 2023 Australian Open 
Men’s singles tennis championship, 
claiming his tenth Australian Open title and 
22nd major title overall. It was an 
impressive victory!

Claim 
Identifier

Evidence

Retriever
Crowdworker

Factual Accuracy

Conversationality

Rater

Evaluation

When claim checking fails 
•
IR may not have retrieved 
relevant articles 
•
Retrieve/check manually
Expensive, but rare

## Page 44

STANFORD
LAM

Experiment

•
Baselines

•
Fine-tuned models

•
Atlas: state-of-the-art on many knowledge-grounded tasks

•
3B parameters

•
LLMs

•
Text-davinci-003 or GPT-4, prompted to be a chatbot

•
Each evaluated for 600 dialog turns

## Page 45

STANFORD
LAM

Distillation to Llama

•
WikiChat pipeline takes 40 seconds per response

•
Fine-tuned LLaMA takes about 4 seconds!
•
Faster, cheaper, more private

•
Not necessary when GPT-4 mini was released (similar speed as LLaMa)

Teacher Model

(multi-step)

e.g. GPT-4

GPT-
generated

Inputs

Instruction

+ a few 
examples

Final 
answer

Student Model

Fine-tune

+

Takeaway: Speed can be optimized later

## Page 46

STANFORD
LAM

Simulated Dialogues: WikiChat-GPT4

94.9

56

47.5

66.1

98.8
94.6
98.5
97.3

0

20

40

60

80

100

Head
Tail
Recent
All

Factuality

GPT-4
WikiChat-GPT4
WikiChat-GPT3.5
WikiChat-LLaMA

Semnani, Sina et al. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia, EMNLP Findings 2023

## Page 47

STANFORD
LAM

Simulated Dialogues: WikiChat-GPT3.5

94.9

56

47.5

66.1

98.8
94.6
98.5
97.3
97.1

82.2

88.2
89.2

0

20

40

60

80

100

Head
Tail
Recent
All

Factuality

GPT-4
WikiChat-GPT4
WikiChat-GPT3.5
WikiChat-LLaMA

Semnani, Sina et al. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia, EMNLP Findings 2023

## Page 48

STANFORD
LAM

94.9

56

47.5

66.1

98.8
94.6
98.5
97.3
97.1

82.2

88.2
89.2
95.2

87.1
90.9
91.1

0

20

40

60

80

100

Head
Tail
Recent
All

Factuality

GPT-4
WikiChat-GPT4
WikiChat-GPT3.5
WikiChat-LLaMA

Simulated Dialogues: WikiChat-LLaMA

Semnani, Sina et al. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia, EMNLP Findings 2023

(Distilled)

## Page 49

94.9

56

47.5

66.1

98.8
94.6
98.5
97.3
97.1

82.2

88.2
89.2
95.2

87.1
90.9
91.1
90.6
86.5
89.4
88.8

0

20

40

60

80

100

Head
Tail
Recent
All

Factuality

GPT-4
WikiChat-GPT4
WikiChat-GPT3.5
WikiChat-LLaMA
Atlas

Simulated Dialogues: Atlas (Contemporary chatbot)

## Page 50

Conversationality

5
4.8
5
5
4.9
4.9

4.6

4.9
5
5
4.8
4.6

4.9
4.8
4.8
4.7

4.3

4.8
4.9
4.7

3.6

2.8

3.8

4.5
4.6

0

1

2

3

4

5

Relevant
Informational
Natural
Non-Repetitive
Temporal

GPT-4
WikiChat-GPT4
WikiChat-GPT3.5
WikiChat-LLaMA
Atlas

Atlas: Sacrifices conversationality for factuality
WikiChat: maintains conversational with factuality

## Page 51

Design Analysis: Do we need both IR and LLM?

Information Retrieval and LLM are color-coded

User: Can we talk about Sting, the musician?
WikiChat: Sure! Sting is an English musician and actor, best known as the frontman, 
songwriter and bassist for the new wave rock band the Police. He has released several solo 
albums and has won numerous awards, including 17 Grammy Awards and a Golden Globe.

User: \[…\] What do you think makes Sting’s music so unique?
WikiChat: Sting’s music is often very personal and introspective, and he often uses his music 
to express his own thoughts and feelings. He also has a great ability to blend different genres 
and create unique sounds.

User: Do you think his birthplace has influenced his music?

WikiChat: Yes, Sting has been heavily influenced by his birthplace of Newcastle upon Tyne, 
England. As a child, he was inspired by the Queen waving at him from a Rolls-Royce, which 
diverted him from the shipyard prospect towards a more glamorous life. He was also 
influenced by the music he heard in local nightclubs he visited such as Club A'Gogo.

## Page 52

STANFORD
LAM

Analyzing the Design

• Analysis of each component

• Do we need 2 pipelines? YES

• 27% of facts come from LLM generation

• Do we need to fact-check LLM output: YES

• Failed: 20% (head); 45% (tail); 56% (recent)

## Page 53

Q UIZ:

A RE W E D ONE A NALYZING W IKIC HAT?

## Page 54

STANFORD
LAM

Real User Evaluation

• Real user evaluation was seldom performed before LLM
because of poor accuracy

• Most important metric!

User study: User reads the first sentence of a new Wikipedia page

Model
User Rating (out of 5)
Factuality

GPT-4
3.4
42.9%

WikiChat using GPT-4
3.8
97.9%

GPT-4: Users are not even aware that over half of the statements are false

## Page 55

STANFORD
LAM

Extra Notes

• Speed

• We showed distilling to Llama could speed up the process

• OpenAI O1-mini is fast enough without fine-tuning

• Multi-lingual Knowledge

• Requires multi-lingual entity resolution
e.g. Hsiang-Tsung Kung and 孔祥重is the same person 
(Wikidata)

## Page 56

H OW TO B UILD A P ERSUASION B OT?

D O N A T I O N SO LI C I T A T IO N

R E C OM M E N D A T I O N S

H E A L T H I N T E RV E N T I ON

## Page 57

STANFORD
LAM

Are LLMs Good at Persuasion?

Very persuasive, much better than previous SOTA bots with “persuasion acts”

BUT it hallucinates success stories!  “There is a girl called Maria ….”

Is that acceptable?
•
Is Wikichat pipeline sufficient? 
•
No! all the success stories are removed!  Not very persuasive!
•
Solution: Search with the intent of the fake story:
•
”Tell an impact story about an individual”
•
Is the evaluation method for conversationality applicable? 
•
No! LLM evaluation on persuasiveness is not correlated with human 
evaluation
•
Solution: Manual evaluation

Zero-shot Persuasive Chatbots with LLM-Generated Strategies and Information Retrieval 
Kazuaki Furumai, Roberto Legaspi, Julio Vizcarra, Yudai Yamazaki, Yasutaka Nishimura, Sina J. Semnani, Kazushi Ikeda, Weiyan Shi, Monica S. Lam
In Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP) , Miami, Florida, November 12 –16, 2024.

### Page links

- [Link 1](../readings/arxiv-2407-03585.md)

## Page 58

STANFORD
LAM

Conclusion

Stopping hallucination is difficult!
•
But it can be done 
•
Formalize the human cognitive process step-by-step
•
Systematically create well-tested step-by-step algorithms
•
Optimize for speed later
•
Detailed LLM engineering
•
Development + evaluation (LLM + Real users)
•
Error analysis
•
Is it worth it?
•
A critical building block of trustworthy agents!

## Page 59

STANFORD
LAM

Agent Engineering Methodology

1. Design the metrics

2. Start with the most general instruction

3. Debug until you can’t break it

•
Test with “critical” examples

•
Root-cause analysis of LLM errors

•
Add/refine the steps

•
Add rationale to the prompt; 
add critical examples as an aid

4. Evaluate

•
Tests must cover the hardest cases

•
Test with LLM-simulated chats 
with hard, varied personalities

•
Evaluate with an LLM

•
If LLM disagrees with human

•
Use human evaluation

•
Test with real users

Systematically create well-tested step-by-step algorithms

Good news: Debugging with critical examples achieves high Wikichat quality.

The key: Look at the errors!
