# Lecture 9: Optimization

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture09.pdf) · [Raw file](../../raw/slides/lecture09.pdf)

Retrieved: 2026-11-13T16:29:33.410733+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Optimization

Diyi Yang, Michael Ryan, John Yang

CS329Z: Engineering AI Agents

## Page 2

CS329Z: Engineering AI Agents

• Guest Lecture next Monday!

• Homework 2 releases next Monday.

• Homework 1 due next Friday, Midway report is the following week.

Announcements

## Page 3

CS329Z: Engineering AI Agents

Quick Poll: Which Prompt is best for PaLM 2-L-IT

A

B

C

\[Math Problem\]  Let’s think step by step.

\[Math Problem\]  Take a deep breath and work on 
this problem step-by-step.

\[Math Problem\]  Let’s combine our numerical 
command and clear thinking to quickly and 
accurately decipher the answer.

71.8%

74.5%

80.2%

## Page 4

CS329Z: Engineering AI Agents

Optimization enables us to specify

intent through data and evals and

improve our system.

Today we will break down 
common optimization algorithms

and when to use them.

## Page 5

CS329Z: Engineering AI Agents

Learning Objectives

• Identify when to use optimization for AI systems.

• Describe various common context/weight optimization algorithms.

• Differentiate times to use each optimization strategy.

## Page 6

CS329Z: Engineering AI Agents

Lecture Overview

• Conditions for Optimization (5 minutes)

• Context Optimization (25 minutes)

• Weight Optimization (25 minutes)

• Optimization with Agents (10 minutes)

• Which Strategy to Use (10 minutes)

## Page 7

CS329Z: Engineering AI Agents

Conditions for Optimization

Conditions
Context/Prompt
Weights
Which to Use?
Agents

## Page 8

CS329Z: Engineering AI Agents

Three Pillars of AI Systems

Data

• Training Data

• Rollouts

• Demonstrations

• Human Feedback

• …

System or

Model

• Language Model

• Compound AI 
System / 
Workflow

• Agentic System

• …

Evaluation +

Metric

• Pass Rate

• Exact Match

• LLM Judge

• Cost/Latency

• …

To optimize an AI System you need all three!

## Page 9

CS329Z: Engineering AI Agents

Is (Context) Optimization Necessary?

• Do we really need to fiddle with prompts anymore?

• Aren’t models going to just get better with scale?

• Optimization is useful for LAST MILE adaptation.

• Once we know your exact setting we can adapt to it.

• Models offer a great general solution, we can optimize for the specifics.

Image Credit: https://msukhareva.substack.com/p/the-last-mile-problem

## Page 10

CS329Z: Engineering AI Agents

When to Optimize

• You have data and evals that suit your 
particular domain.

• Examples and feedback can communicate 
requirements that are difficult to express 
completely in a prompt/system

• Sometimes proper evals convey intent better 
and you can tune the system to your evals.

• The system has many complex components 
that are difficult to tune manually.

## Page 11

CS329Z: Engineering AI Agents

Benefits of Optimization

• Greater reliability: Reduce recurring errors and 
improve consistency across tasks.

• Domain adaptation: Improve performance on 
specialized tasks, workflows, and requirements.

• Lower cost and latency: Maintain quality with smaller 
models, shorter prompts, or fewer tool calls.

• Learning from experience: Turn successful trajectories 
and failure feedback into lasting improvements.

• Adaptability: Adjust behavior as models, tools, and 
task requirements change.

## Page 12

CS329Z: Engineering AI Agents

Context Optimization

Conditions
Context/Prompt
Weights
Which to Use?
Agents

## Page 13

CS329Z: Engineering AI Agents

Fewshot Optimization

## Page 14

CS329Z: Engineering AI Agents

Fewshot Prompting

Image Credit: https://arxiv.org/pdf/2005.14165

## Page 15

CS329Z: Engineering AI Agents

Fantastically Ordered Prompts and Where to Find Them \[Lu et al., 2022\]

Image Credit: https://arxiv.org/pdf/2005.14165

Try a bunch of prompt orderings on the trainset and measure how this changes labels on 
the probing set.  Interestingly we throw ignore the ground truth labels on the probing set.

## Page 16

CS329Z: Engineering AI Agents

Fantastically Ordered Prompts and Where to Find Them \[Lu et al., 2022\]

the ending is universally panned

features multiple endings

nice movie

quite hard to sit through

0

0

1

1

High Global Entropy

the ending is universally panned

features multiple endings

nice movie

quite hard to sit through

0

0

0

0

Low Global Entropy

## Page 17

CS329Z: Engineering AI Agents

Fantastically Ordered Prompts and Where to Find Them \[Lu et al., 2022\]

High Local Entropy
Low Local Entropy

0
1

the ending is universally panned
the ending is universally panned

0
1

Average over probe set
logprobs
logprobs

## Page 18

CS329Z: Engineering AI Agents

Fantastically Ordered Prompts and Where to Find Them \[Lu et al., 2022\]

Image Credit: https://arxiv.org/pdf/2005.14165

Using the probing set and measuring entropy approaches the oracle ordering accuracy 
(trying every ordering to find the best on the devset)

## Page 19

CS329Z: Engineering AI Agents

Bootstrap Reasoning

Image Credit: https://arxiv.org/pdf/2201.11903

We know Chain of Thought Reasoning is important… but labeled examples 
for few shot often do not come with reasoning.

## Page 20

CS329Z: Engineering AI Agents

Bootstrap Reasoning: STaR \[Zelikman et al., 2022\]

Image Credit: https://arxiv.org/pdf/2203.14465

We can rejection sample our way to mining reasoning traces

## Page 21

CS329Z: Engineering AI Agents

Bootstrap Reasoning: DSPy \[Khattab et al., 2023\]

We don’t even need to fine-tune; just rejection sample successful reasoning.

Input
Model
Reasoning

Output

Metric

Input
Model
Reasoning

Output

Metric

Keep

Discard

Then try out 
combinations on

the devset to

find best 
performing

fewshot 
examples.

## Page 22

CS329Z: Engineering AI Agents

Bootstrap Reasoning: DSPy \[Khattab et al., 2023\]

Image Credit: https://aclanthology.org/2024.emnlp-main.525.pdf

Table Credit: https://arxiv.org/pdf/2310.03714

Bootstrapping Reasoning/Outputs and then 
randomly searching on the trainset can be better 
than providing human reasoning or gold labels.

## Page 23

CS329Z: Engineering AI Agents

Reflective Optimization

## Page 24

CS329Z: Engineering AI Agents

Large Language Models as Optimizers \[Yang et al., 2024\]

Image Credit: https://arxiv.org/pdf/2309.03409

Allow the LLM to see past 
instructions and how performant 
they were, then ask the LLM to 
write a new instruction.

## Page 25

CS329Z: Engineering AI Agents

Large Language Models as Optimizers \[Yang et al., 2024\]

Image Credit: https://arxiv.org/pdf/2309.03409

Identifies interesting strategies like “Take a deep breath…”

## Page 26

CS329Z: Engineering AI Agents

MIPROv2 \[Opsahl-Ong et al., 2024\]

Image Credit: https://aclanthology.org/2024.emnlp-main.525.pdf

1. Bootstrap Demonstrations (Reasoning/Output if the program is CoT)

2. Propose Instructions based on Reflection

3. Search the Combinations of Instructions and Demonstrations

Let’s walk through an example!

## Page 27

> Bootstrap Fewshot Generation

We run training examples several times to collect successful 
traces of your program to use as few shot demonstrations.

## Page 28

> Bootstrap Fewshot Generation

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

LM Program

## Page 29

> Bootstrap Fewshot Generation

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

LM Program
Training

Input

## Page 30

> Bootstrap Fewshot Generation

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

LM Program
Training

Input
Metric

## Page 31

> Bootstrap Fewshot Generation

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

LM Program
Training

Input
Metric

## Page 32

> Bootstrap Fewshot Generation

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

LM Program
Training

Input

Species Prediction Rationale and Output

If the output scores poorly on the metric we discard the trace

Metric

## Page 33

> Bootstrap Fewshot Generation

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

LM Program
Training

Input

Species Prediction Rationale and Output

If the output scores highly on the metric we keep the trace

Metric

## Page 34

> Bootstrap Fewshot Generation

petal_length: "1.4", 
petal_width: "0.2", 
sepal_length: "4.6", 
sepal_width: "3.2", 
rationale: “Let’s think step by step in order to predict 
the iris species. We know that the petal length is 1.4 cm, 
which is relatively short compared to the other species. 
The petal width is 0.2 cm, which is also relatively narrow. 
The sepal length is 4.6 cm, which is relatively long, and 
the sepal width is 3.2 cm, which is relatively wide. Based 
on these characteristics, we can conclude that the iris 
species is likely to be setosa.", 
answer: "setosa"

. . .

## Page 35

> Grounded Instruction Proposal with MIPROv2

We collect several details about your task to inform the 
prompt proposal LM.

## Page 36

> Grounded Instruction Proposal with MIPROv2

1. Program-Aware Grounding

## Page 37

> Grounded Instruction Proposal with MIPROv2

1. Program-Aware Grounding

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

## Page 38

> Grounded Instruction Proposal with MIPROv2

1. Program-Aware Grounding

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

The task the program is designed to solve is classifying iris flowers into 
one of three species (setosa, versicolour, or virginica) based on the given 
dimensions of their petals and sepals. The program uses a language model to 
predict the species by reasoning through the provided dimensions.

## Page 39

> Grounded Instruction Proposal with MIPROv2

2. Data-Aware Grounding

Sepal Length
Sepal Width (cm)
Pedal Length (cm)
Pedal Width (cm)
Species

5.1
3.5
1.4
0.2
Iris-setosa

6.3
2.3
4.4
1.3
Iris-versicolor

5.4
3.7
1.5
0.2
Iris-setosa

6.9
3.1
5.1
2.3
Iris-virginica

...

## Page 40

> Grounded Instruction Proposal with MIPROv2

2. Data-Aware Grounding

Sepal Length
Sepal Width (cm)
Pedal Length (cm)
Pedal Width (cm)
Species

5.1
3.5
1.4
0.2
Iris-setosa

6.3
2.3
4.4
1.3
Iris-versicolor
...
The dataset appears to have three classes: setosa, versicolor, and 
virginica. Each of the classes has a distinct distribution on the 
petal_length and petal_width variables. However, the sepal_length and 
sepal_width variables appear to have less clear cut trends. Additionally, 
the species variable does not provide much additional information since it 
is a duplicate of the answer variable. ---

Is this correct? Can I improve this? Please let me know if so.

## Page 41

> Grounded Instruction Proposal with MIPROv2

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

classify_iris(5.1, 3.5, 1.4, 0.2)

3. Successful Bootstrapped Program Traces

“versicolor”

classify_iris(5.1, 1.8, 5.9, 3.0) 
“verginica”

## Page 42

> Grounded Instruction Proposal with MIPROv2

3. Successful Bootstrapped Program Traces

classify_iris(5.1, 1.8, 5.9, 3.0) 
“verginica”

## Page 43

> Grounded Instruction Proposal with MIPROv2

3. Successful Bootstrapped Program Traces

classify_iris(5.1, 1.8, 5.9, 3.0) 
“verginica”

petal_length: 5.1  
petal_width: 1.8 
sepal_length: 5.9 
sepal_width: 3.0 
rationale: Let’s think step by step to produce the answer. We know that the 
petal length of 5.1 is relatively long compared to the setosa species, 
which typically has a petal length of around 4.8. The petal width of 1.8 is 
also slightly wider than the setosa species, which typically has a petal 
width of around 1.5. The sepal length and width are both relatively long 
compared to the setosa species. Therefore, based on these characteristics, 
we can conclude that the iris is likely to be either a versicolor or 
virginica. However, the sepal length of 5.9 and the sepal width of 3.0 are 
slightly more characteristic of the virginica species. Therefore, we can 
answer: virginia

## Page 44

> Grounded Instruction Proposal with MIPROv2

4. Prompting Tips

“Don’t be afraid to be creative”

“The instruction should include a high stakes 
scenario in which the LM must solve the task!”

“Provide the LM with a persona that is relevant to 
the task (ie. \"You are a …\")”

“Keep the instruction clear and concise.”

We only show one of these at a time.

## Page 45

> Grounded Instruction Proposal with MIPROv2

</> Program Summary

Tips

Successful Traces

Data Summary

Instructions

## Page 46

> Grounded Instruction Proposal with MIPROv2

Instructions

## Page 47

> Grounded Instruction Proposal with MIPROv2

Instructions

Using the provided petal length, petal width, sepal length, and sepal 
width measurements in cm, predict the iris species accurately to save a 
critically endangered species from extinction.

Given the petal length, petal width, sepal length, and sepal width in 
centimeters, predict the species of the iris flower (setosa, versicolour, 
or virginica). Provide a step-by-step reasoning for your prediction based 
on the given measurements.

Given the critical situation in which a rare species of iris is on the 
brink of extinction, predict the iris species based on the dimensions of 
the petals and sepals in order to save it from extinction.

...

## Page 48

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

Given our set of instructions and demonstrations from the first two 
steps we iteratively sample combinations to update our belief that a 
given instruction or demonstration is good using a bayesian surrogate 
model.

## Page 49

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

Instruction 1
Demo Set 1

Instruction 2
Demo Set 2

Instruction 3
Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

Sample parameters for our program based on beliefs

## Page 50

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

Instruction 1
Demo Set 1

Instruction 2
Demo Set 2

Instruction 3
Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

Sample parameters for our program based on beliefs

## Page 51

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

Instruction 1

Demo Set 2

## Page 52

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

Instruction 1
Demo Set 2

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

Slot parameters into the program

## Page 53

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

Instruction 1
Demo Set 2

)

Slot parameters into the program

## Page 54

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

Sample minibatch from training data
*Every few iterations we also do a full evaluation

## Page 55

def classify_iris(ptl_len, ptl_wid, sep_len, sep_wid):

return (               
)

LM Program
Training

Input
Metric

Run the minibatch on the updated program

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 56

Update beliefs based on mini batch results

Instruction 1
Demo Set 1

Instruction 2
Demo Set 2

Instruction 3
Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 57

Update beliefs based on mini batch results

Instruction 1
Demo Set 1

Instruction 2
Demo Set 2

Instruction 3
Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 58

Repeat num_batches times, doing a full evaluation every

few iterations

Instruction 1
Demo Set 1

Instruction 2
Demo Set 2

Instruction 3
Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 59

Repeat num_batches times, doing a full evaluation every

few iterations

Instruction 1
Demo Set 1

Instruction 2
Demo Set 2

Instruction 3
Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 60

Repeat num_batches times, doing a full evaluation every

few iterations

Instruction 1
Demo Set 1

Instruction 2
Demo Set 2

Instruction 3
Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 61

Repeat num_batches times, doing a full evaluation every

few iterations

Instruction 1
Demo Set 1

Instruction 2
Demo Set 2

Instruction 3
Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 62

Repeat num_batches times, doing a full evaluation every

few iterations

Instruction 1
Demo Set 1

Instruction 2

Demo Set 3

... 
...

Instruction N
Demo Set N

Beliefs

Instruction 3

Demo Set 2

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 63

Example Optimized Module

“Given the petal and sepal dimensions in cm, predict the iris species.”

Given the critical situation in which a rare species of iris is on the brink 
of extinction, predict the iris species based on the dimensions of the 
petals and sepals in order to save it from extinction. 
— 
petal_length: "1.5",petal_width: "0.1",sepal_length: "5.2",sepal_width: 
"4.1", 
rationale: "predict the iris species. We know that the petal length is 1.5 
cm, which is relatively short compared to the other species. The petal width 
is 0.1 cm, which is also relatively narrow. The sepal length is 5.2 cm, 
which is relatively long, and the sepal width is 4.1 cm, which is also 
relatively wide. Based on these characteristics, we can conclude that the 
iris species is likely to be setosa.", 
answer: “setosa" 
—

> Optimizing the Combination of Instructions and Demonstrations in 
MIPROv2

## Page 64

CS329Z: Engineering AI Agents

Feedback Gradients (TextGrad) \[Yuksekgonul et al., 2024\]

Have an LLM reflect on what can be improved about an output and propagate that 
feedback back through the prompts in the system.

Image Credit: https://arxiv.org/pdf/2406.07496

## Page 65

CS329Z: Engineering AI Agents

Genetic Pareto Prompt Evolution (GEPA) \[Agrawal et al., 2026\]

Image Credit: https://arxiv.org/pdf/2507.19457

## Page 66

CS329Z: Engineering AI Agents

GEPA Example: PAPILLON \[Siyan et al., 2025\]

Image Credit: https://arxiv.org/pdf/2410.17127

Baseline Prompts from GEPA Paper (not the 
baseline prompts from the PAPILLON paper)

Given a private user query, create a privacy-preserving request for 
a powerful external LLM.

The LLM may assist without learning private information about the 
user.

1

Respond to a user query.

For inspiration, we found a potentially related request to a powerful 
external LLM and its response.

3

## Page 67

CS329Z: Engineering AI Agents

GEPA Example

Image Credit: https://arxiv.org/pdf/2507.19457

## Page 68

CS329Z: Engineering AI Agents

GEPA Results

Image Credit: https://arxiv.org/pdf/2507.19457

Reflective prompt evolution with GEPA outperforms baselines across tasks.

## Page 69

CS329Z: Engineering AI Agents

Context Optimization Summary

• Fewshot Optimization:

• Takeaway: Bootstrapping reasoning/output 
and searching for useful few shot examples 
is a strong pattern for prompt optimization.

• Reflective Optimization:

• Takeaway: Running the task and reflecting on what to change, then 
including that into the prompt is a strong pattern.  Evolving the prompt 
based on improvements to the Pareto frontier also helps.

## Page 70

CS329Z: Engineering AI Agents

Weight Optimization

Conditions
Context/Prompt
Weights
Which to Use?
Agents

## Page 71

CS329Z: Engineering AI Agents

Supervised Finetuning

## Page 72

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

Recall:

## Page 73

CS329Z: Engineering AI Agents

Recall:
Instruction Finetuning

Image Credit: https://arxiv.org/pdf/2210.11416

## Page 74

CS329Z: Engineering AI Agents

SFT For Agents

• Rollout teacher on agentic tasks.

• Post-train student models on teacher 
completed tasks.

• Focus on diversity of tasks and environments.

• Student learns task execution.

## Page 75

CS329Z: Engineering AI Agents

Have a teacher 
model perform the 
task and then train 
on the outputs.

Also possible to 
verify the output of 
the model 
somehow and train 
using rejection 
sampling.

## Page 76

CS329Z: Engineering AI Agents

OpenThoughts-Agent \[Raoof et al., 2026\]

Image Credit: https://arxiv.org/pdf/2606.24855
Stay tuned for the Agent Data lectures!

## Page 77

CS329Z: Engineering AI Agents

OpenThoughts-Agent \[Raoof et al., 2026\]

Image Credit: https://arxiv.org/pdf/2606.24855
Finetuning on rollouts from a strong teacher helps!

## Page 78

CS329Z: Engineering AI Agents

FireAct \[Chen et al., 2023\]

Image Credit: https://arxiv.org/pdf/2310.05915

Finetune LLama2 on GPT-4 rollouts with various agent reasoning design patterns

At inference time allow the model to select how to reason.

## Page 79

CS329Z: Engineering AI Agents

FireAct \[Chen et al., 2023\]

Image Credit: https://arxiv.org/pdf/2310.05915

Finetuning LLama2-13B on GPT-4 rollouts makes it

a better agent than prompted GPT-3.5

## Page 80

CS329Z: Engineering AI Agents

Reinforcement Learning

## Page 81

CS329Z: Engineering AI Agents

RL For Agents

• Rollout student on agentic tasks.

• Reward the student for successfully 
completing the task.

• Focus on varying environments and task 
complexity.

• Verifiability is key.

## Page 82

CS329Z: Engineering AI Agents

External reward 
verifies if the task 
was completed 
successfully.

Run several times 
within a group and 
several groups to a 
batch.

## Page 83

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

## Page 84

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

Generate an Output

KL per Token
One reward for

entire output

Value per Token

Per token reward

Per token value

Generalized 
Advantage Estimate:

How useful is this 
token compared to

other possible

tokens?

## Page 85

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

1. Four Models to keep in memory!

## Page 86

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

1. Four Models to keep in memory!
1. Four Models to keep in memory!

2. Two Models to train every step!

## Page 87

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

1. Four Models to keep in memory!
1. Four Models to keep in memory!

2. Two Models to train every step!
2. Two Models to train every step!

3. Several (expensive) per token steps!

## Page 88

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

Generate a Group of

Outputs

Per Output Rewards

Token Level KL

Group 
Advantage

## Page 89

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

1. Three Models to keep in memory!  Also “Reward Model” 
doesn’t have to be a model.

## Page 90

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

1. Three Models to keep in memory!  Also “Reward Model” 
doesn’t have to be a model.

2. One Model to train every step!

## Page 91

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

1. Three Models to keep in memory!  Also “Reward Model” 
doesn’t have to be a model.

2. One Model to train every step!

3. Only KL is per token, everything else is sequence level!

Token Level KL

## Page 92

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

Advantage Calculation

Compute the z-score for each output reward!

## Page 93

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.03300

Expectation over a prompt pulled from our dataset, and a 
group of sampled outputs for that prompt.

Avg over

group
Avg over 
tokens in

response

How important is this

token based on our 
new policy compared

to our old

Advantage

Don’t deviate too far

from reference

Don’t over update on

any one token.

## Page 94

CS329Z: Engineering AI Agents

Real World Example

Image Credit: https://arxiv.org/pdf/2501.12948

## Page 95

CS329Z: Engineering AI Agents

GRPO vs PPO for DeepSeekR1

Image Credit: https://arxiv.org/pdf/2501.12948

## Page 96

CS329Z: Engineering AI Agents

On-Policy Distillation

## Page 97

CS329Z: Engineering AI Agents
Image Credit: https://thinkingmachines.ai/blog/on-policy-distillation/

It’s handy to get chess coaching on a game you actually 
played rather than a game you just observed.

## Page 98

CS329Z: Engineering AI Agents
Image Credit: https://thinkingmachines.ai/blog/on-policy-distillation/

SFT vs RL vs On Policy Distillation

RL

SFT

On Policy 
Distillation

## Page 99

CS329Z: Engineering AI Agents
Image Credit: https://thinkingmachines.ai/blog/on-policy-distillation/

SFT vs RL vs On Policy Distillation

## Page 100

CS329Z: Engineering AI Agents
Image Credit: https://thinkingmachines.ai/blog/on-policy-distillation/

On Policy Distillation Loss

Student logprobs

minus teacher 
logprobs for each

token

Expectation over 
response sampled

from policy

## Page 101

CS329Z: Engineering AI Agents
Image Credit: https://thinkingmachines.ai/blog/on-policy-distillation/

On Policy Distillation Example

## Page 102

CS329Z: Engineering AI Agents
Image Credit: https://thinkingmachines.ai/blog/on-policy-distillation/

Real Model Example

## Page 103

CS329Z: Engineering AI Agents
Image Credit: https://thinkingmachines.ai/blog/on-policy-distillation/

On Policy Distillation Results

On-policy distillation was more efficient and produced better models than RL.

## Page 104

CS329Z: Engineering AI Agents

Weight Optimization Summary

## Page 105

CS329Z: Engineering AI Agents

Optimization with Agents

Conditions
Context/Prompt
Weights
Which to Use?
Agents

## Page 106

CS329Z: Engineering AI Agents

Self Improvement

## Page 107

CS329Z: Engineering AI Agents

Darwin Gödel Machine \[Zhang et al., 2026\]

Image Credit: https://arxiv.org/pdf/2505.22954

Select parents to self-modify proportionally to performance and 
inversely proportional  to the number of children.

## Page 108

CS329Z: Engineering AI Agents

Darwin Gödel Machine \[Zhang et al., 2026\]

Image Credit: https://arxiv.org/pdf/2505.22954

## Page 109

CS329Z: Engineering AI Agents

Darwin Gödel Machine \[Zhang et al., 2026\]

Image Credit: https://arxiv.org/pdf/2505.22954

Both the self-improvement (parent modifies itself rather than meta-agent) AND the 
exploration (returning to prior parents instead of always building on latest) were critical.

## Page 110

CS329Z: Engineering AI Agents

Meta-Harness

Image Credit: https://arxiv.org/pdf/2603.28052

Allow a meta agent to see ALL prior experience and decide what to edit next.

## Page 111

CS329Z: Engineering AI Agents

Meta-Harness

Image Credit: https://arxiv.org/pdf/2603.28052

Over time the meta-agent can use the context to build better and better harnesses

for agents to solve domain-targeted problems.

## Page 112

CS329Z: Engineering AI Agents

Auto Research (Optimize Anything)

## Page 113

CS329Z: Engineering AI Agents

Auto-Research

Image Credit: https://www.cerebras.ai/blog/how-to-stop-
your-autoresearch-loop-from-cheating

Give agent access to repository.  Let it brainstorm, write a change.  Run 
experiments to see if the change was positive.  If metrics improve, build upon

it, otherwise reset.  Log the findings.

## Page 114

CS329Z: Engineering AI Agents

Auto-Research Prompt

Image Credit: https://github.com/karpathy/autoresearch

…

## Page 115

CS329Z: Engineering AI Agents

Auto-Research

Image Credit: https://github.com/karpathy/autoresearch

## Page 116

CS329Z: Engineering AI Agents

Optimization with Agents Summary

• Agents are relatively capable optimizers.

• Set them up in an environment where they 
can log results, ideate, and execute, and 
they are pretty good at optimizing anything 
that runs on software.

• The metric/evals becomes the most critical 
part to control.

## Page 117

CS329Z: Engineering AI Agents

Which Strategy to Use

Conditions
Context/Prompt
Weights
Which to Use?
Agents

## Page 118

CS329Z: Engineering AI Agents

BetterTogether \[Soylu et al., 2024\]

Image Credit: https://aclanthology.org/2024.emnlp-main.597.pdf

Sometimes it is best to optimize the prompts, then the weights, then the prompts again.

## Page 119

CS329Z: Engineering AI Agents

GEPA \[Agrawal et al., 2026\]

Image Credit: https://arxiv.org/pdf/2507.19457

Prompt optimization is much more sample-efficient than RL.

## Page 120

CS329Z: Engineering AI Agents

OpenThoughts-Agent \[Raoof et al., 2026\]

Image Credit: https://arxiv.org/pdf/2606.24855

Weight optimization is more data hungry, but can effectively grow with thousands and

thousands of examples.

## Page 121

CS329Z: Engineering AI Agents

Reasons to use context optimization

• Optimization for API Access models.  Some 
strong models do not provide fine-tuning 
access.

• Need to rerun optimization frequently and 
quickly. Context optimization runs faster 
and on simpler infrastructure than weight.

• Environment interactions are expensive. 
Context optimization is more sample 
efficient.

## Page 122

CS329Z: Engineering AI Agents

Reasons to use weight optimization

• Context Optimization fails. Especially for small 
models sometimes instruction following skills are 
minimal.

• You have a capable teacher and want a cheaper 
model.  Distilling directly into a student model is 
often effective.

• The context is getting too long.  Context 
optimization adds more complexity to the prompt.  
Sometimes it is useful to use weight optimization 
to avoid context-bloat from prompt optimization.

## Page 123

CS329Z: Engineering AI Agents

Summary

SAS vs MAS
Orchestration
Communication
Failure Modes
Coordination

## Page 124

CS329Z: Engineering AI Agents

Summary

• Conditions for Optimization

• Context Optimization

• Weight Optimization

• Optimization with Agents

• Which Strategy to Use

## Page 125

CS329Z: Engineering AI Agents

Guest Lecture next Monday!
