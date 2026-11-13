# Chapter 9 Interaction Styles for Agentic LLMs

[Course index](../../README.md) · [Original source](https://arxiv.org/html/2610.13455v1#Ch9) · [Raw file](../../raw/originals/book.html)

Retrieved: 2026-11-13T16:41:17.579179+00:00

[Contents](../../CONTENTS.md) · [Full book](../book/full-book-html.md) · [Previous chapter](chapter-08-metalearning.md) · [Next chapter](chapter-10-case-study-2-balrog-for-llm-reasoning-and-reflection.md)

<a id="Ch9"></a>


### Chapter 9 Interaction Styles for Agentic LLMs

**What You Will Learn**

In this chapter you will learn about different agentic interaction styles and agentic memory.
Specifically, you will be able to:

- Recognize three different historic types of *agents in AI*, and how they connect to current agentic LLMs.
- Recognize five different agentic LLM *interaction* styles.
- Understand the importance of *memory* in agentic LLMs, and recognize different agentic memory architectures.

<a id="Ch9.S1"></a>


#### 9.1 Agents in AI

Agents play a central role in artificial intelligence, and we will first discuss some of the background of agents in AI.

<a id="Ch9.S1.SS1"></a>


##### 9.1.1 Agents Act and Adapt in their Environment

In artificial intelligence, entities that act in the world are called *agents*. They are the AI equivalent of humans acting in the world. In the agent concept, AI researchers try to capture what they perceive to be the essence of what humans do—understanding intelligence by building it.

Agents are autonomous software systems that act in an environment. They (1) have goals, they (2) perceive their environment, they (3) make decisions, they (4) take actions to achieve their goals, and, most importantly, they (5) learn from experience.
Agents should adapt to new information in order to achieve their goals better, or, in reinforcement learning terms, agents improve their action policy.

Traditional computer programs are deterministic, they predictably follow pre-set instructions (this makes computers so useful to do things from accounting to control, in which predictability is paramount). LLM agents, in contrast, are less deterministic, and less predictable. They learn, and change their behavior from time to time. They can autonomously reason, plan, and perform tasks using tools to perform simple workflows for users in areas such as coding, customer service, and data analysis. (They also hallucinate, make mistakes, and generally are unpredictable and undependable. In that respect, LLM agents are more like humans than computers.)

Agents have been studied for quite some time in artificial intelligence.
It is useful to distinguish three types of agents: (1) robotic assistant agents, (2) belief-desire-intention agents, and (3) swarm agents.

<a id="Ch9.S1.SS1.SSS1"></a>


###### 9.1.1.1 Robotic Assistants

First we discuss agents that are robotic assistants.
This view on AI agents is from the field of engineering: agents perform human-like tasks for humans. An agent is a tool to more easily achieve routine tasks. An example is a welding robot in a factory, an auto-pilot in an airplane, or a self-driving car that has to find a safe route in an unpredictable environment.

<a id="Ch9.S1.SS1.SSS1.p2.1"></a>


Further examples of such agents are virtual assistants, such as Alexa and Siri, or coding assistants such as CoPilot that help software developers become more productive, or customer service bots that help customers navigate the maze of rules of a company to achieve goals such as filing a complaint or getting a refund. Robotic assistant agents can have significant reasoning abilities [[Dorri et al., 2018](#bibh.bib6)], and LLMs are increasingly used for such assistants [[Plaat et al., 2025](#bibh.bib11)].

<a id="Ch9.S1.SS1.SSS2"></a>


###### 9.1.1.2 Agents with Beliefs, Desires, and Intentions

Another view on AI agents is rooted in the field of cognitive science. Here the goal is for agents to model human cognitive processes, and agents have beliefs, desires and intentions (BDI). Cognitive science studies human thinking processes. AI agents can be used to implement cognitive models, and experiment with models of thinking: is the model able to reason logically, to cooperate with human players in a game of Bridge, to deconstruct a theater play by Shakespeare, to compose music, or to have self-awareness? Cognition may take many subtle forms, such as interpreting sensory input, guiding physical actions, and empathizing with others.

<a id="Ch9.S1.SS1.SSS2.p2.1"></a>


Originally, BDI agents come from the tradition of logic reasoning. They are imbued with goals, which they pursue through actions. The literature in this field sees actions as a way to achieve the goals of an agent [[Rao et al., 1995](#bibh.bib8), [Georgeff et al., 1998](#bibh.bib5)].

<a id="Ch9.S1.SS1.SSS3"></a>


###### 9.1.1.3 Swarm Agents

<a id="Ch9.S1.SS1.SSS3.p1.1"></a>


A third view on AI agents stresses interaction patterns between large numbers of small agents. Where the previous multi-agent systems consisted of few, complex, agents that act and think—agents that could assist, or agents with beliefs, desires and intentions (BDI)—this approach studies flocks and swarms of many, simple, agents. Now the emphasis is on emergent collaborative behavior, behavior that emerges at a scale beyond the reasoning of the agents themselves. Can a swarm offer protection against a predator? What are the prerequisites for collaboration to occur? When is a society peaceful, when is it at war? What is a super-organism [[Johnson and Linksvayer, 2010](#bibh.bib16), [Wilson and Sober, 1989](#bibh.bib17)]?

<a id="Ch9.S1.SS1.SSS3.p2.1"></a>


Swarm agents come from the connectionist tradition of embodied AI [[Brooks, 1990](#bibh.bib14)]. The agents communicate, and researchers are often interested in the emergence of large scale behavioral patterns such as cooperation and communication. A well-known swarm algorithm is ant colony optimization [[Dorigo et al., 2007](#bibh.bib13)], and a well-known software environment to study such patterns is Netlogo [[Wilensky and Rand, 2015](#bibh.bib9)].11
1
<https://www.netlogo.org>

Multi-agent systems and agentic LLMs are suitable for the study of all three types of approaches: agents as tools, agents as cognitive entities, and agents that help us study how to achieve peaceful societies (or how to conquer another). Part IV of this book is dedicated to agents as tools, and Part V is dedicated to cognition and agent societies.

<a id="Ch9.S1.SS2"></a>


##### 9.1.2 Agentic LLMs as Reinforcement Learning Agents

<a id="Ch9.S1.SS2.p1.1"></a>


The study of the behavior of intelligent agents has a long
tradition in AI. A central aspect of agent behavior is how agents learn in their environment. Mechanisms by which agents learn from feedback are studied in reinforcement learning [[Sutton and Barto, 2018](#bibh.bib34)] and multi-agent reinforcement learning [[Wong et al., 2021](#bibh.bib15)].

In the next section we will discuss five interaction styles that we see in agentic LLM. As preparation for this overview, we will provide a formal basis for agents that interact in the world using the language of reinforcement learning.

Figure [9.1](#Ch9.F1 "Figure 9.1 ‣ 9.1.2 Agentic LLMs as Reinforcement Learning Agents ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models") shows a reinforcement learning system that consists of an agent and an environment. In this system, the agent interacts with the
environment through actions, and the environment responds with the new
state of the system and a reward value, indicating how good the new
state is.

The agent can learn from these reward values, and note which actions
are favorable and which are unfavorable in each state. The goal of the agent is to find the optimal behavior for the environment, and thus, the best actions in each state. The agent uses the rewards to reinforce its notion of the best actions in each state, and thus learn a function of optimal behavior. This function, mapping each state to an action, is called the
behavior policy, denoted as $\pi$. The optimal policy is denoted as
$\pi^{*}$.
If the agent learns
through deep learning, then the policy is parameterized by the weights $\theta$
of a neural network.

<a id="Ch9.F1"></a>


![Original vector figure](../../raw/assets/Ch9.F1.pic1.svg)

Environment: $T(s,a)\rightarrow s^{\prime},R(s^{\prime})\rightarrow r$Agent: $r$ improves $\pi_{\theta}(s)\rightarrow a$$(s^{\prime},r)$$a$


Figure 9.1: <a id="Ch9.F1.4"></a>
The reinforcement learning loop where the agent learns a parameterized policy $\pi_{\theta}$ from feedback rewards $r$ from the environment’s transition $T$ and reward function $R$, upon the agent’s actions $a$ [[Sutton and Barto, 2018](#bibh.bib34)]

The world in which the agent operates is represented by the environment. The agent takes actions and changes the state of the environment. The environment has a probabilistic transition function that computes the new
state whenever an action has been performed by the agent. The environment also computes a corresponding reward for the new
state. Thus, the environment is modeled with two functions: a
transition function $T$ and a reward function $R$.

This model, of an agent acting in an environment, receiving feedback
to learn which actions caused good state transitions, and which did
not, suits the concept of agentic LLMs quite well, as we will see in the next section.

<a id="Ch9.F2"></a>


![Original vector figure](../../raw/assets/Ch9.F2.pic1.svg)

Environment: $T(s,a)\rightarrow s^{\prime},R(s^{\prime})\rightarrow r$Agent: $\pi_{LLM_{P\pi}}(s,r)\rightarrow a$$(s^{\prime},r)$$a$


Figure 9.2: Reinforcement learning where the agent uses an LLM to parameterize policy $\pi_{LLM_{P\pi}}$ to use feedback $r$ from the environment to choose its actions $a$

From the reinforcement learning point of view, we can use the LLM as a function in the agent: $LLM(prompt)\rightarrow answer$. The LLM can be used in different places in reinforcement learning: in the agent, or in the environment. For example, the agent can use the LLM as policy-improver. It can call an LLM with a certain prompt for the policy function $\pi_{LLM_{P\pi}}(s,r)$ that learns from environment feedback which actions to take in the different states that the environment can be in (see Figure [9.2](#Ch9.F2 "Figure 9.2 ‣ 9.1.2 Agentic LLMs as Reinforcement Learning Agents ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models")). The LLM is given a prompt $P\pi$ that tells it to act as a policy improver using reward $r$, and returns an action $a$ for state $s$. As we will see in Section [20.2.1](chapter-20-advanced-transformer-and-agentic-architectures.md#Ch20.S2.SS1 "20.2.1 In-Context Reinforcement Learning ‣ 20.2 Agentic Architectures ‣ Chapter 20 *Advanced Transformer and Agentic Architectures ‣ Part VI Advanced Topics ‣ Agentic Large Language Models"), in-context reinforcement learning (ICRL) uses the LLM as a policy improver, and tree of thoughts can use an LLM to generate the successor actions.

<a id="Ch9.F3"></a>


![Original vector figure](../../raw/assets/Ch9.F3.pic1.svg)

Environment: $T_{LLM_{PT}}(s,a)\rightarrow s^{\prime},R_{LLM_{PR}}(s^{\prime})\rightarrow r$Agent: $\pi_{LLM_{P\pi}}(s,r)\rightarrow a$$(s^{\prime},r)$$a$


Figure 9.3: Reinforcement learning where both the agent and the environment use LLMs for $\pi$, $T$, and $R$. The LLMs are each given a prompt $Px$ to return an action, state, or reward value

The LLM can also be used in the environment, to compute the reward of the state $LLM_{R(s)}$, or to compute the next state $LLM_{T(s,a)}$, see Figure [9.3](#Ch9.F3 "Figure 9.3 ‣ 9.1.2 Agentic LLMs as Reinforcement Learning Agents ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"). In the figure, the same LLM is now used for three different roles, with three different prompts: to perform the policy, the transition, and the reward function. For example, tree of thoughts can use an LLM to evaluate the reward of a state. There are many options in designing our agentic LLMs,
as we will see next. We use the reinforcement learning paradigm to discuss and illustrate the different agentic styles.

<a id="Ch9.S2"></a>


#### 9.2 Learning Mechanisms in Agentic LLMs

The field of agentic LLM is new, and the previous chapters have shown many different approaches in which LLMs have been used in an agentic setting. In this section we will review the approaches that we have seen so far in this book. We distinguish the approaches based on their prompting method and their training method.

We will describe five styles of interaction that fit agentic LLMs.
Table [9.1](#Ch9.T1 "Table 9.1 ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models") summarizes the five agent styles. We focus on the way
that the LLM is prompted by the harness at inference time, and how it is trained. All prompting styles can yield useful agentic assistants and interaction partners, that act in realistic ways, for certain domains. The more elaborate prompting styles have been developed in the pursuit for better performance in more challenging domains.

The first column of the table gives the name of the agentic
interaction style, from query to reinforcement finetuning. The second
column lists the type of prompting of the styles, from a simple static
instruction prompt without any examples, to a dynamic reinforcement
learning prompt. The third column shows the training method of the
LLM, whether it is pretrained or finetuned or both. The fourth column
gives a concrete example of the interaction style (with references to the
literature).

<a id="Ch9.T1"></a>


|  |  |  |  |
| --- | --- | --- | --- |
| *Agent type* | *Prompt* | *LLM* | *Example* |
| **A: Query** | zero-shot user-written | pretrained | <a id="Ch9.T1.3.2.4.1"></a> GPT-2 [[Vaswani et al., 2017](#bibh.bib39)] |
|  | query or instruction |  |  |
| **B: In-Context Learning** | few-shot | pretrained | <a id="Ch9.T1.3.4.4.1"></a> GPT-3 [[Brown et al., 2020](#bibh.bib38)] |
| (supervised example) | examples |  |  |
| **C: In-Context Learning** | chain-of-thought-steps | pretrained | <a id="Ch9.T1.3.6.4.1"></a> Chain of Thought [[Wei et al., 2022](#bibh.bib42)] |
| (reasoning-steps) | example |  | <a id="Ch9.T1.3.7.4.1"></a> Zero-shot CoT [[Kojima et al., 2022](#bibh.bib37)] |
|  | feedback harness |  | <a id="Ch9.T1.3.8.4.1"></a> Tree of Thoughts [[Yao et al., 2024](#bibh.bib36)] |
| **D: Self-Reflection** | prompt optimization | pretrained | <a id="Ch9.T1.3.9.4.1"></a> LLaMea [[van Stein and Bäck, 2024](#bibh.bib33)] |
|  | search or RL |  | <a id="Ch9.T1.3.10.4.1"></a> ReAct [[Yao et al., 2022](#bibh.bib43)] |
| **E: Reinforcement Finetuning** | RL prompt | pretraining/ | <a id="Ch9.T1.3.11.4.1"></a> RLVR [[Lambert et al., 2024](#bibh.bib10)] |
|  | optimization harness | finetuning |  |

Table 9.1: Five Agent Styles

<a id="Ch9.S2.SS1"></a>


##### 9.2.1 Agentic Interaction Styles

We will now discuss the interaction styles. In the first three agent styles the prompt of the LLM is static. The prompt is
written by the user and does not change.

<a id="Ch9.S2.SS1.SSS1"></a>


###### 9.2.1.1 A. Query Prompt

The first interaction style is interacting with the LLM by giving it a simple instruction. Figure [9.4](#Ch9.F4 "Figure 9.4 ‣ 9.2.1.1 A. Query Prompt ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models") shows this interaction style. It simply
consists of an instruction written by the user. For example, *Lily
missed the train. She felt very …* to which the model hopefully
responds with something like *angry*, or *sad*. The prompt is purely a query, without
any training examples. The learning style is zero-shot learning,
instruction only.

<a id="Ch9.F4"></a>


![Original vector figure](../../raw/assets/Ch9.F4.pic1.svg)

QueryLLMAnswer


Figure 9.4: Style A: Static Query

<a id="Ch9.S2.SS1.SSS1.p2.1"></a>


The LLM is able to correctly answer many such queries because it has
been pretrained on a large corpus of text, which may provide an answer
to many of the queries that users may ask. The model has also been finetuned for instruction answering. Examples of this
interaction style are the early LLMs, such as GPT-2 [[Vaswani et al., 2017](#bibh.bib39)].

<a id="Ch9.S2.SS1.SSS2"></a>


###### 9.2.1.2 B. In-Context Learning

Next, we turn to in-context learning. For machine learning,
in-context learning is an exciting new type of learning, in addition
to supervised and reinforcement learning. In a large language
model in-context learning often achieves good results with just a few examples,
achieving one of the main challenges of the field of machine learning.

Compared to interaction style A, in-context few-shot learning is a more involved interaction style.

<a id="Ch9.F5"></a>


![Original vector figure](../../raw/assets/Ch9.F5.pic1.svg)

Query + ex1, ex2, ex3LLMAnswer


Figure 9.5: Style B: In Context Supervised Learning with a prompt based on few examples

In-context learning occurs when the user provides a few examples
along with the query. In doing so, the user conditions the decoder model to activate the correct
part of the large amount of knowledge that is represented in its parameters.

<a id="Ch9.S2.SS1.SSS2.p4.1"></a>


Figure [9.5](#Ch9.F5 "Figure 9.5 ‣ 9.2.1.2 B. In-Context Learning ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models") shows an illustration of a prompt that fits this
interaction style. An example from the literature of this interaction style is GPT-3. The
paper that introduced in-context learning is
[Brown et al. [2020]](#bibh.bib38). An example of a few-shot prompt is: *Fill
in the dots: the
sea-la mer, oysters-huitre, the window-la fenetre, cheese-…* to
which the model hopefully responds with *fromage*.

Note that in-context learning only emerges when the model is large
enough. Originally, in-context learning emerged in
models with around 100 billion parameters. At that size, the model
was rich enough for the few prompt examples to activate the right
parts of the model. As our LLM methods improve, this boundary keeps shrinking.

<a id="Ch9.S2.SS1.SSS3"></a>


###### 9.2.1.3 C. Chain of Thought

<a id="Ch9.S2.SS1.SSS3.p1.1"></a>


Next, we turn to another famous method, chain of thought learning [[Wei et al., 2022](#bibh.bib42)], Figure [9.6](#Ch9.F6 "Figure 9.6 ‣ 9.2.1.3 C. Chain of Thought ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"), top. This method
was developed, as we saw in Chapter [6](chapter-06-multi-step-reasoning-in-llms.md#Ch6 "Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models"), to address
the weakness of LLMs in solving simple math word reasoning problems. A disadvantage of the original chain of thought approach is that
a new prompt has to be written by the user for each new reasoning task at
hand. A subsequent development was the zero-shot chain of thought prompt, Figure [9.6](#Ch9.F6 "Figure 9.6 ‣ 9.2.1.3 C. Chain of Thought ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"), bottom. [Kojima et al. [2022]](#bibh.bib37) found that adding the generic sentence: *Let’s
think step by step* to prompts already improves performance on many benchmarks,
although often not by as much as a hand-written task-specific prompt.

<a id="Ch9.F6"></a>


![Original vector figure](../../raw/assets/Ch9.F6.pic1.svg)

Query + step1, step2, step3 = ex1LLMAnswerQuery + ”Let’s think step by step” = ex1LLMAnswer


Figure 9.6: Style C: Top: Chain of Thought: In-Context Learning with an LLM based on examples of the reasoning steps; Bottom: Zero-shot Chain of Thought with an instruction that often works

As in the previous interaction style, chain of thought is an in-context few-shot learning method, although now
the examples in the prompt are a few examples of the *steps* that the model
should take before it provides its answer—whereas previously they were examples of facts. These steps help the model
arrive at the right answer, following a multi-step reasoning
chain. The examples are not examples of answers to activate parts of the model, but of steps on
how to arrive at the answer. Example prompts for few-shot and zero-shot chain of thought
have been shown in Figure [6.1](chapter-06-multi-step-reasoning-in-llms.md#Ch6.F1 "Figure 6.1 ‣ 6.1.3 Chain of Thought Prompting ‣ 6.1 In-Context Reasoning ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models") on page [6.1](chapter-06-multi-step-reasoning-in-llms.md#Ch6.F1 "Figure 6.1 ‣ 6.1.3 Chain of Thought Prompting ‣ 6.1 In-Context Reasoning ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models").

<a id="Ch9.S2.SS1.SSS3.p3.1"></a>


Again, as with in-context learning, chain of thought only works in models of sufficient size, and
again, this size is getting smaller as our understanding of LLM methods
increases and models are being finetuned for chain of thought. Furthermore, it is possible to transfer
the learned reasoning methods from a large model to a model with
orders of magnitude fewer parameters, by distillation [[Li et al., 2023](#bibh.bib4)].

<a id="Ch9.S2.SS1.SSS4"></a>


###### 9.2.1.4 D. Self-Reflection Harness

The preceding agentic interaction styles all used a single static
prompt, achieving encouraging performance on many
benchmarks. To perform well on planning problems, or other problems where state must be tracked, a reasoning
style is needed where prompts are optimized, searching through options in a tree
of possibilities.

We will now discuss two interaction styles where the LLM prompt is
dynamically manipulated by a small algorithm that is external to the LLM. This algorithm is called a *harness*. The first style is in-context (LLM parameters are not changed), while the second style (in the next subsection) also uses
finetuning of the model.

These interaction styles are dynamic.
As we saw in the previous chapter on metalearning, a challenge of dynamic methods is to achieve a stable learning process.
When training targets are changing, learning algorithms may diverge, and extra care is needed to achieve convergence.
Achieving predictable high performance with self-reflection is still an area of active research.

The first dynamic prompting methods that we discuss
emerged out of
the need to model more complex reasoning structures, that go beyond
the straight line sequence of steps of chain of thought. First, simple search algorithms were introduced (tree of thoughts). Next, full fledged dynamic prompting methods were introduced to manage prompt development (ReAct, reflexion, self refine). Often, the harness of these methods introduced short-term and long-term memories to remember state between LLM invocations.

An interesting aspect of these methods is that the LLM is
used in different roles, for which it is called with different types of prompts. The original role of the LLM in chain of thought
tasks is to *evaluate* the answer in each reasoning step. This evaluation prompt is now augmented with
a different type of prompt, to *generate* a new reasoning step. Sometimes a third type of prompt is added, whose task is to *improve* the prompt
itself. Thus, a single model is used to self-reflect on itself through different prompts, managed by an external harness.

<a id="Ch9.F7"></a>


![Original vector figure](../../raw/assets/Ch9.F7.pic1.svg)

Initial Problem $s$$LLM_{Pgenerate}(s)$$LLM_{Peval}(s_{1})$$LLM_{Peval}(s_{2})$$LLM_{Peval}(s_{3})$$LLM_{P\pi}(s,\mbox{history})\rightarrow a$$LLM_{Peval}(s,a)\rightarrow(s^{\prime},a,r)$history $\cup(s^{\prime},a,r)$$(s,a)$


Figure 9.7: Style D: Self-reflection with an LLM;
the prompt is being optimized in context with answers from an
LLM, first to generate subproblems, then to evaluate them; controlled by search (top), or reinforcement learning
(bottom)

<a id="Ch9.S2.SS1.SSS4.p6.1"></a>


Figure [9.7](#Ch9.F7 "Figure 9.7 ‣ 9.2.1.4 D. Self-Reflection Harness ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models") shows these ideas. At the top, the self-reflection is controlled by a standard tree search algorithm, as in tree of thoughts [[Yao et al., 2024](#bibh.bib36)]. At the bottom, a reinforcement learning loop controls self-reflection, where the prompt for policy $\pi$ is updated with the history of (state, action, reward) triples (see also Section [20.2.1](chapter-20-advanced-transformer-and-agentic-architectures.md#Ch20.S2.SS1 "20.2.1 In-Context Reinforcement Learning ‣ 20.2 Agentic Architectures ‣ Chapter 20 *Advanced Transformer and Agentic Architectures ‣ Part VI Advanced Topics ‣ Agentic Large Language Models")).

<a id="Ch9.S2.SS1.SSS5"></a>


###### 9.2.1.5 E. Reinforcement Finetuning Harness

Up to now, all learning was in-context, the model provided answers based on examples provided in the context. The parameters of the LLM were not
changed. Although ICL is easy to use, it limits learning. If we wish the model to adapt more profoundly to a certain environment, if we wish the model to remember what it learned at inference time, then it helps if the parameters can change. We call approaches that use this method *reinforcement finetuning*. RLVR is a well-known example.

Figure [9.8](#Ch9.F8 "Figure 9.8 ‣ 9.2.1.5 E. Reinforcement Finetuning Harness ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models") provides an illustration, where the trainable model parameters are indicated as $\psi$. Note that the only difference with Figure [9.7](#Ch9.F7 "Figure 9.7 ‣ 9.2.1.4 D. Self-Reflection Harness ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models") (bottom) is the introduction of the $\psi$ parameters. In ReFT the LLM parameters $\psi$ change, they are finetuned based on the rewards from the dataset. We should interpret the figures such that where learning at inference time was in-context, this has now changed, since we allow finetuning of the parameters $\psi$.
In the traditional LLM training pipeline, finetuning is a stage that comes before inference. However, for many important applications, such as math reasoning or coding, chain of thought multi-step inference-time roll-outs produce accurate rewards that can be used for finetuning. Therefore, in reinforcement finetuning, the model is used to produce training targets at inference-time, that are then used to finetune the parameters of the same model—finetuning at inference-time. Reinforcement finetuning blurs the line between inference and finetuning, where supervised finetuning has a clear separation between training and inference.

<a id="Ch9.F8"></a>


![Original vector figure](../../raw/assets/Ch9.F8.pic1.svg)

$LLM_{\pi/CoT}^{\psi}(s)\rightarrow a$$LLM_{eval}^{\psi}(s,a)\rightarrow(s^{\prime},a,r)$$(s^{\prime},a,r)$$(s,a)$


Figure 9.8: <a id="Ch9.F8.4"></a>
Style E: Reinforcement Finetuning of the LLM parameters
$LLM^{\psi}$ in addition to reinforcement learning of the
policy $\pi$ parameters $\pi_{\theta}$
[[Luong et al., 2024](#bibh.bib12)].

In LLM training there are three main training/inference moments: (1) pretraining, (2) finetuning, (3) testing (inference). Self-reflection (Style D) does reinforcement learning at inference time.
In style E, reinforcement finetuning, we do not do reinforcement learning at test time (3), but at finetune time (2). In agentic LLM, this interaction style allows the LLM to learn from agent interaction with the world.

For the dynamic agentic styles D and E, care must be taken to achieve stable convergence. As of this writing, few works have been published that report on such results.

<a id="Ch9.S3"></a>


#### 9.3 Memory Architectures for Agentic LLMs

Humans (and other forms of life) remember. Our memory enables us to have an identity. We can remember our name, our friends, and our family members. Memory allows us to learn what is good an what is bad for us, and it allows us to adapt our behavior.
When we suffer memory-loss, either through injury, illness, or old age, our personality changes. Severe memory-loss leads to loss of identity, we wander aimlessly through the world.

Agents also need memory. In this section we will discuss why agentic LLM needs memory, and we provide a brief overview of the different types of memory that have been developed for agentic LLM.

<a id="Ch9.S3.SS1"></a>


##### 9.3.1 The Need for Memory

A statistical model $f(x)\rightarrow\hat{y}$ estimates an output $\hat{y}$ based on the relation $f$ that it has learned for its input $x$ at training time. Such functional behavior is memory-free. Any new information (post-training) must be provided to the model through the input parameters $x$. LLMs are no different, and even the earliest chatbots were provided with special hidden *system prompts* that fed the model a history of the conversation, so that it is able to hold a coherent conversation.

As the use cases for agentic LLM increase, more advanced techniques are needed, beyond the system-prompt method.
To better understand what memory is used for in agentic LLMs, we will now discuss different use cases for memory.

<a id="Ch9.S3.SS1.SSS1"></a>


###### 9.3.1.1 Coherent Conversation

Many machine learning benchmarks for LLMs are of the challenge/response type, and they are well suited for the functional input/output behavior of statistical models. The main real world use case for LLMs, however, is as a chat-bot, where the LLM is expected to engage in a meaningful conversation with the user. In order to maintain a coherent conversation, in which conversational partners react and respond to each other, chat-bots must be able to know what has been said before.

Thus, a first requirement for agentic LLMs is to be able know what has been said before in a conversation.

<a id="Ch9.S3.SS1.SSS2"></a>


###### 9.3.1.2 Adaptation

According to our definition in Chapter [1](chapter-01-introduction.md#Ch1 "Chapter 1 Introduction ‣ Agentic Large Language Models"), agentic LLMs are expected to learn. When a robot performs a task in a kitchen, such as chopping an onion, and the location of the knife has moved, then it should adapt its actions: it should now first pick up the knife from its new location before starting to chop. Agents interact with the environment, and if the environment changes, then agents should adapt.

Either our agent’s pretrained policies must be highly general, and able to adapt to all new situations in a certain domain, or our agents architecture must flexible, and recognize when a pretrained policy requires adaptation, finetuning or even re-training. For this, they need memory.

As we have seen in Section [6.2.4](chapter-06-multi-step-reasoning-in-llms.md#Ch6.S2.SS4 "6.2.4 Agentic Harness for Prompt Improvement ‣ 6.2 Self-Reflection and State ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models"), the external prompt improvement harnesses that are used in self-reflective agent architectures require buffers and other memory types for explicit prompt improvement.

<a id="Ch9.S3.SS1.SSS3"></a>


###### 9.3.1.3 Identity

Our experiences shape our personality and our identity. When LLM agents are to build up their own identity, the experiences must either be collected and held in a memory, to be used for self-reflection, or they must be processed and used in other ways to adapt their behavior policy.

As the memory architectures of agentic harnesses improve, agents will be able to better remember their experiences. When that happens, we may find that our agents can acquire, through their agentic experiences, a unique personality.

<a id="Ch9.S3.SS1.SSS4"></a>


###### 9.3.1.4 Continual Learning

<a id="Ch9.S3.SS1.SSS4.p1.1"></a>


Traditional machine learning trains a model on a particular dataset for a particular task. Human learning is different, our learning evolves continuously throughout our lives.
In machine learning, continual learning studies how models can be trained for a sequence of new tasks while preserving previously learned tasks [[Wang et al., 2024](#bibh.bib32), [Li et al., 2025a](#bibh.bib3)]. Like metalearning, it studies generalization across related tasks. Major challenges in continual learning are to overcome
catastrophic forgetting, and how to cope with changing data distributions.

The field of continual learning provides a variety of architectures that support this type of training.

<a id="Ch9.S3.SS2"></a>


##### 9.3.2 Memory Architectures

The field of agentic LLM is young. Only recently are memory architectures for LLM agents starting to receive attention. We will discuss the different approaches that have so far appeared.

<a id="Ch9.S3.SS2.SSS1"></a>


###### 9.3.2.1 Finetuning

A pragmatic way to deal with the need for memory is to incorporate new information into the model as it arrives. Instead of developing external memory management algorithms, we could take advantage of the fact that model parameters are a form of memory, and finetune the model as the new examples arrive.

<a id="Ch9.S3.SS2.SSS1.p2.1"></a>


To achieve this approach in an agentic setting, the finetuning must happen quickly, before the user can perceive a lag. Parameter efficient finetuning methods such as LoRA are an option [[Yang et al., 2024](#bibh.bib18)]. Although this is an elegant approach that does not require external algorithms or memory structures, for most applications the finetuning will not happen quickly enough, and an in-context or harness solution should be developed.

<a id="Ch9.S3.SS2.SSS2"></a>


###### 9.3.2.2 Long Context Windows and Compression

A second approach is to perform prompt management. The standard approach of chat-bots is to provide a truncated form of the chat-history to the LLM by injecting it into the prompt in addition to the user’s text. This is an approach that works quite well in practice. A limitation is that context windows are limited in size, and processing large contexts is expensive because of the squared time complexity of the attention mechanism.

<a id="Ch9.S3.SS2.SSS2.p2.1"></a>


Two types of solutions have been pursued. First, specific long-context architectures have been developed, that keep track of attention in different ways [[Smith et al., 2022](#bibh.bib2)]. This is an active field of research, a survey of recent approaches is [Liu et al. [2025]](#bibh.bib40).
Second, compression schemes have been developed, to semantically compress the prompt into a smaller stream. A survey is [Li et al. [2025b]](#bibh.bib31).
Prompts can be divided into chunks [[Sheng et al., 2025](#bibh.bib41)], to allow processing of large prompts. A related approach uses the LLM to generate code for processing long prompts recursively [[Zhang et al., 2025a](#bibh.bib35)].

<a id="Ch9.S3.SS2.SSS2.p3.1"></a>


Prompts can also be compressed through filtering of unnecessary tokens (this sentence could become *Prompts compressed filtering unnecessary tokens*).
Another approach is soft prompts [[Lester et al., 2021](#bibh.bib25)].
Soft prompts eliminate discrete tokens, but learn embeddings (via backpropagation) that can be fed directly into the transformer, without mapping them to actual language tokens. This context can serve as an alternative to a plain-text context. Impressive compression rates have been reported, from ten-fold [[Mu et al., 2023](#bibh.bib27)] to hundred-fold [[Li et al., 2025c](#bibh.bib26)].

<a id="Ch9.S3.SS2.SSS3"></a>


###### 9.3.2.3 Explicit Memory Management

If we need to store state between LLM calls, then a straightforward solution is for the agent harness to provide this storage, as part of its prompt management. In Section [6.2.4](chapter-06-multi-step-reasoning-in-llms.md#Ch6.S2.SS4 "6.2.4 Agentic Harness for Prompt Improvement ‣ 6.2 Self-Reflection and State ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models") we saw how the external prompt-improvement algorithms for self-reflection add different types of storage, such as in the reflexion approach and the buffer of thoughts approach (Figures [6.8](chapter-06-multi-step-reasoning-in-llms.md#Ch6.F8 "Figure 6.8 ‣ Reflexion ‣ 6.2.4.2 Self-Reflection ‣ 6.2.4 Agentic Harness for Prompt Improvement ‣ 6.2 Self-Reflection and State ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models") and [6.6](chapter-06-multi-step-reasoning-in-llms.md#Ch6.F6 "Figure 6.6 ‣ 6.2.4.1 Search-based Prompt Optimization ‣ 6.2.4 Agentic Harness for Prompt Improvement ‣ 6.2 Self-Reflection and State ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models")).

<a id="Ch9.S3.SS2.SSS3.p2.1"></a>


Agents can have different requirements for their storage (see [Zhang et al. [2025b]](#bibh.bib29), [Chhikara et al. [2025]](#bibh.bib24) for a survey). We will discuss some of the recent studies of this active field of research. Prompts can be stored in textual or parametric form, and relevant operations are the reading and writing to memory. Furthermore, memory management operations are important, such as for compacting and forgetting information. Also, additional services can be provided by the memory systems. For example, MemoryBank [[Zhong et al., 2024](#bibh.bib28)] adds hierarchical summaries and uses LLM prompts to provide a running personality of the interaction events of a user.

<a id="Ch9.S3.SS2.SSS3.p3.1"></a>


Operations to store and retrieve items can be added to an agent. MemGPT [[Packer et al., 2023](#bibh.bib21)] studies how LLMs can read and write to external memory using function calls (memory as a tool). A-mem [[Xu et al., 2025](#bibh.bib19)] introduces contextual descriptions of memory, based on a mailbox principle.

A disadvantage of the explicit memory management approach is that the LLM has to perform memory management explicitly, without having been trained how to do this effectively. An alternative solution is to manually write memory management code, when it is possible to foresee all possible requirements.
The Model Context Protocol (MCP) is a set of strategies designed for context management. Section [11.4](chapter-11-how-agents-use-tools-to-act-in-the-world.md#Ch11.S4 "11.4 Model Context Protocol and Context Management ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") describes the protocol in more depth.

<a id="Ch9.S3.SS2.SSS3.Px1"></a>


###### Learning to use memory

<a id="Ch9.S3.SS2.SSS3.Px1.p1.1"></a>


Mem1 [[Zhou et al., 2025](#bibh.bib7)] uses a different approach: after each LLM interaction the agent updates a compact state to be shared with future LLM calls. The memory size required is constant, so that the state does not run out of the context window. The shared state is created by inserting reasoning-style tags into the prompt, and is trained using reinforcement learning to incentivize state consolidation. Mem-$\alpha$ is another approach that uses reinforcement learning to train agents to effectively use memory [[Wang et al., 2025](#bibh.bib20)].

<a id="Ch9.S3.SS2.SSS3.Px1.p2.1"></a>


AgeMem [[Yu et al., 2026](#bibh.bib30)] integrates memory management operations into agent’s policy for end-to-end optimization. It distinguishes long term and short term memory, and uses a three-stage reinforcement learning scheme to train the agent in the use of the two types of memory.

<a id="Ch9.S3.SS2.SSS3.Px1.p3.1"></a>


This, too, is an active field of research, new studies and frameworks can be expected. See, for an overview, [Zhou et al. [2026]](#bibh.bib1).

<a id="Ch9.S3.SS2.SSS3.Px2"></a>


###### Vector Databases

In addition to the storage of prompts as human-readable text, we can also store their tokenized embeddings directly.
Storing prompts as text is useful for retrieving data when an exact textual match is needed. Embeddings encode semantic information—which tokens are close to each other in meaning. Storing embeddings is therefore useful when we would like to retrieve items that are semantically close.

<a id="Ch9.S3.SS2.SSS3.Px2.p2.1"></a>


Embeddings can be stored in vector databases. Traditional relational databases store data in rows and columns. Vector databases store high-dimensional lists of numbers, and provide low-latency access to them, making them well-suited for LLMs [[Xie et al., 2023](#bibh.bib23), [Ma et al., 2023](#bibh.bib22)].

<a id="Ch9.S4"></a>


#### 9.4 Concluding Remarks

The concept of an intelligent agent is a central concept in artificial intelligence. LLMs have increased the communication and reasoning capabilities of agents significantly. In this chapter, we have discussed different agent types, and have connected them to different traditions in AI.

Agents act. We have discussed 5 main interaction styles based on the preceding chapters. Agents need memory to interact meaningfully with their environments, and we have discussed this new field of research.

After covering so much theory, it is high time to get our hands dirty. In the next chapter we will look at a practical case study, to get more experience with using some of the theoretical concepts that we have seen.

<a id="bibh"></a>


### References

<a id="bibh.bib14"></a>
- Brooks (1990)
  R. A. Brooks
  Elephants don’t play chess.
  Robotics and autonomous systems 6 (1-2), pp. 3–15.
  Cited by: [§9.1.1.3](#Ch9.S1.SS1.SSS3.p2.1 "9.1.1.3 Swarm Agents ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib38"></a>
- Brown et al. (2020)
  T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al.
  Language models are few-shot learners.
  Advances in neural information processing systems 33, pp. 1877–1901.
  Cited by: [§9.2.1.2](#Ch9.S2.SS1.SSS2.p4.1 "9.2.1.2 B. In-Context Learning ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"),
  [Table 9.1](#Ch9.T1.3.4.4.1 "In 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib24"></a>
- Chhikara et al. (2025)
  P. Chhikara, D. Khant, S. Aryan, T. Singh, and D. Yadav
  Mem0: building production-ready ai agents with scalable long-term memory.
  arXiv preprint arXiv:2504.19413.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.p2.1 "9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib13"></a>
- Dorigo et al. (2007)
  M. Dorigo, M. Birattari, and T. Stutzle
  Ant colony optimization.
  IEEE computational intelligence magazine 1 (4), pp. 28–39.
  Cited by: [§9.1.1.3](#Ch9.S1.SS1.SSS3.p2.1 "9.1.1.3 Swarm Agents ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib6"></a>
- Dorri et al. (2018)
  A. Dorri, S. S. Kanhere, and R. Jurdak
  Multi-agent systems: a survey.
  Ieee Access 6, pp. 28573–28593.
  Cited by: [§9.1.1.1](#Ch9.S1.SS1.SSS1.p2.1 "9.1.1.1 Robotic Assistants ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib5"></a>
- Georgeff et al. (1998)
  M. Georgeff, B. Pell, M. Pollack, M. Tambe, and M. Wooldridge
  The belief-desire-intention model of agency.
  In International workshop on agent theories, architectures, and languages,
  pp. 1–10.
  Cited by: [§9.1.1.2](#Ch9.S1.SS1.SSS2.p2.1 "9.1.1.2 Agents with Beliefs, Desires, and Intentions ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib16"></a>
- Johnson and Linksvayer (2010)
  B. R. Johnson and T. A. Linksvayer
  Deconstructing the superorganism: social physiology, groundplans, and sociogenomics.
  The Quarterly Review of Biology 85 (1), pp. 57–79.
  Cited by: [§9.1.1.3](#Ch9.S1.SS1.SSS3.p1.1 "9.1.1.3 Swarm Agents ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib37"></a>
- Kojima et al. (2022)
  T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa
  Large language models are zero-shot reasoners.
  Advances in neural information processing systems 35, pp. 22199–22213.
  Cited by: [§9.2.1.3](#Ch9.S2.SS1.SSS3.p1.1 "9.2.1.3 C. Chain of Thought ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"),
  [Table 9.1](#Ch9.T1.3.7.4.1 "In 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib10"></a>
- Lambert et al. (2024)
  N. Lambert, J. Morrison, V. Pyatkin, S. Huang, H. Ivison, F. Brahman, L. J. V. Miranda, A. Liu, N. Dziri, S. Lyu, et al.
  Tulu 3: pushing frontiers in open language model post-training.
  arXiv preprint arXiv:2411.15124.
  Cited by: [Table 9.1](#Ch9.T1.3.11.4.1 "In 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib25"></a>
- Lester et al. (2021)
  B. Lester, R. Al-Rfou, and N. Constant
  The power of scale for parameter-efficient prompt tuning.
  In Proceedings of the 2021 conference on empirical methods in natural language processing,
  pp. 3045–3059.
  Cited by: [§9.3.2.2](#Ch9.S3.SS2.SSS2.p3.1 "9.3.2.2 Long Context Windows and Compression ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib4"></a>
- Li et al. (2023)
  L. H. Li, J. Hessel, Y. Yu, X. Ren, K. Chang, and Y. Choi
  Symbolic chain-of-thought distillation: small models can also “think” step-by-step.
  In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), A. Rogers, J. Boyd-Graber, and N. Okazaki (Eds.),
  Toronto, Canada, pp. 2665–2679.
  External Links: [Link](https://aclanthology.org/2023.acl-long.150/),
  [Document](https://dx.doi.org/10.18653/v1/2023.acl-long.150)
  Cited by: [§9.2.1.3](#Ch9.S2.SS1.SSS3.p3.1 "9.2.1.3 C. Chain of Thought ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib3"></a>
- Li et al. (2025a)
  Y. Li, X. Wang, X. Yang, M. Bonsangue, J. Zhang, and T. Li
  Improving open-world continual learning under the constraints of scarce labeled data.
  In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2,
  pp. 1647–1658.
  Cited by: [§9.3.1.4](#Ch9.S3.SS1.SSS4.p1.1 "9.3.1.4 Continual Learning ‣ 9.3.1 The Need for Memory ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib31"></a>
- Li et al. (2025b)
  Z. Li, Y. Liu, Y. Su, and N. Collier
  Prompt compression for large language models: a survey.
  In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
  pp. 7182–7195.
  Cited by: [§9.3.2.2](#Ch9.S3.SS2.SSS2.p2.1 "9.3.2.2 Long Context Windows and Compression ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib26"></a>
- Li et al. (2025c)
  Z. Li, Y. Su, and N. Collier
  500xcompressor: generalized prompt compression for large language models.
  In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
  pp. 25081–25091.
  Cited by: [§9.3.2.2](#Ch9.S3.SS2.SSS2.p3.1 "9.3.2.2 Long Context Windows and Compression ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib40"></a>
- Liu et al. (2025)
  J. Liu, D. Zhu, Z. Bai, Y. He, H. Liao, H. Que, Z. Wang, C. Zhang, G. Zhang, J. Zhang, et al.
  A comprehensive survey on long context language modeling.
  arXiv preprint arXiv:2503.17407.
  Cited by: [§9.3.2.2](#Ch9.S3.SS2.SSS2.p2.1 "9.3.2.2 Long Context Windows and Compression ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib12"></a>
- Luong et al. (2024)
  T. Q. Luong, X. Zhang, Z. Jie, P. Sun, X. Jin, and H. Li
  Reft: reasoning with reinforced fine-tuning.
  arXiv preprint arXiv:2401.08967.
  Cited by: [Figure 9.8](#Ch9.F8 "In 9.2.1.5 E. Reinforcement Finetuning Harness ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"),
  [Figure 9.8](#Ch9.F8.4 "In 9.2.1.5 E. Reinforcement Finetuning Harness ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib22"></a>
- Ma et al. (2023)
  L. Ma, R. Zhang, Y. Han, S. Yu, Z. Wang, Z. Ning, J. Zhang, P. Xu, P. Li, W. Ju, et al.
  A comprehensive survey on vector database: storage and retrieval technique, challenge.
  arXiv preprint arXiv:2310.11703.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.Px2.p2.1 "Vector Databases ‣ 9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib27"></a>
- Mu et al. (2023)
  J. Mu, X. Li, and N. Goodman
  Learning to compress prompts with gist tokens.
  Advances in Neural Information Processing Systems 36, pp. 19327–19352.
  Cited by: [§9.3.2.2](#Ch9.S3.SS2.SSS2.p3.1 "9.3.2.2 Long Context Windows and Compression ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib21"></a>
- Packer et al. (2023)
  C. Packer, V. Fang, S. Patil, K. Lin, S. Wooders, and J. Gonzalez
  MemGPT: towards llms as operating systems..
   ArXiv.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.p3.1 "9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib11"></a>
- Plaat et al. (2025)
  A. Plaat, M. van Duijn, N. van Stein, M. Preuss, P. van der Putten, and K. J. Batenburg
  Agentic large language models, a survey.
  Journal of Artificial Intelligence Research, arXiv preprint arXiv:2503.23037 84, pp. 29:1–29:74.
  Cited by: [§9.1.1.1](#Ch9.S1.SS1.SSS1.p2.1 "9.1.1.1 Robotic Assistants ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib8"></a>
- Rao et al. (1995)
  A. S. Rao M. P. Georgeff et al.
  BDI agents: from theory to practice..
  In Icmas,
  Vol. 95, pp. 312–319.
  Cited by: [§9.1.1.2](#Ch9.S1.SS1.SSS2.p2.1 "9.1.1.2 Agents with Beliefs, Desires, and Intentions ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib41"></a>
- Sheng et al. (2025)
  B. Sheng, J. Yao, M. Zhang, and G. He
  Dynamic chunking and selection for reading comprehension of ultra-long context in large language models.
  arXiv preprint arXiv:2506.00773.
  Cited by: [§9.3.2.2](#Ch9.S3.SS2.SSS2.p2.1 "9.3.2.2 Long Context Windows and Compression ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib2"></a>
- Smith et al. (2022)
  J. T. Smith, A. Warrington, and S. W. Linderman
  Simplified state space layers for sequence modeling.
  arXiv preprint arXiv:2208.04933.
  Cited by: [§9.3.2.2](#Ch9.S3.SS2.SSS2.p2.1 "9.3.2.2 Long Context Windows and Compression ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib34"></a>
- Sutton and Barto (2018)
  R. S. Sutton and A. G. Barto
  Reinforcement learning.
  2 edition, Adaptive Computation and Machine Learning series, Bradford Books, Cambridge, MA.
  Cited by: [Figure 9.1](#Ch9.F1 "In 9.1.2 Agentic LLMs as Reinforcement Learning Agents ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"),
  [Figure 9.1](#Ch9.F1.4 "In 9.1.2 Agentic LLMs as Reinforcement Learning Agents ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"),
  [§9.1.2](#Ch9.S1.SS2.p1.1 "9.1.2 Agentic LLMs as Reinforcement Learning Agents ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib33"></a>
- van Stein and Bäck (2024)
  N. van Stein and T. Bäck
  LLaMEA: a large language model evolutionary algorithm for automatically generating metaheuristics.
  arXiv preprint arXiv:2405.20132.
  Cited by: [Table 9.1](#Ch9.T1.3.9.4.1 "In 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib39"></a>
- Vaswani et al. (2017)
  A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin
  Attention is all you need.
  Advances in neural information processing systems 30.
  Cited by: [§9.2.1.1](#Ch9.S2.SS1.SSS1.p2.1 "9.2.1.1 A. Query Prompt ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"),
  [Table 9.1](#Ch9.T1.3.2.4.1 "In 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib32"></a>
- Wang et al. (2024)
  L. Wang, X. Zhang, H. Su, and J. Zhu
  A comprehensive survey of continual learning: theory, method and application.
  IEEE transactions on pattern analysis and machine intelligence 46 (8), pp. 5362–5383.
  Cited by: [§9.3.1.4](#Ch9.S3.SS1.SSS4.p1.1 "9.3.1.4 Continual Learning ‣ 9.3.1 The Need for Memory ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib20"></a>
- Wang et al. (2025)
  Y. Wang, R. Takanobu, Z. Liang, Y. Mao, Y. Hu, J. McAuley, and X. Wu
  Mem-$\{$$\backslash$alpha$\}$: learning memory construction via reinforcement learning.
  arXiv preprint arXiv:2509.25911.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.Px1.p1.1 "Learning to use memory ‣ 9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib42"></a>
- Wei et al. (2022)
  J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al.
  Chain-of-thought prompting elicits reasoning in large language models.
  Advances in neural information processing systems 35, pp. 24824–24837.
  Cited by: [§9.2.1.3](#Ch9.S2.SS1.SSS3.p1.1 "9.2.1.3 C. Chain of Thought ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"),
  [Table 9.1](#Ch9.T1.3.6.4.1 "In 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib9"></a>
- Wilensky and Rand (2015)
  U. Wilensky and W. Rand
  An introduction to agent-based modeling: modeling natural, social, and engineered complex systems with netlogo.
  The MIT Press, MIT Press.
  External Links: ISBN 9780262731898,
  LCCN 2014023747,
  [Link](https://books.google.nl/books?id=LQrhBwAAQBAJ)
  Cited by: [§9.1.1.3](#Ch9.S1.SS1.SSS3.p2.1 "9.1.1.3 Swarm Agents ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib17"></a>
- Wilson and Sober (1989)
  D. S. Wilson and E. Sober
  Reviving the superorganism.
  Journal of theoretical Biology 136 (3), pp. 337–356.
  Cited by: [§9.1.1.3](#Ch9.S1.SS1.SSS3.p1.1 "9.1.1.3 Swarm Agents ‣ 9.1.1 Agents Act and Adapt in their Environment ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib15"></a>
- Wong et al. (2021)
  A. Wong, T. Bäck, A. V. Kononova, and A. Plaat
  Multiagent deep reinforcement learning: challenges and directions towards human-like approaches.
  arXiv preprint arXiv:2106.15691.
  Cited by: [§9.1.2](#Ch9.S1.SS2.p1.1 "9.1.2 Agentic LLMs as Reinforcement Learning Agents ‣ 9.1 Agents in AI ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib23"></a>
- Xie et al. (2023)
  X. Xie, H. Liu, W. Hou, and H. Huang
  A brief survey of vector databases.
  In 2023 9th international conference on big data and information analytics (BigDIA),
  pp. 364–371.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.Px2.p2.1 "Vector Databases ‣ 9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib19"></a>
- Xu et al. (2025)
  W. Xu, Z. Liang, K. Mei, H. Gao, J. Tan, and Y. Zhang
  A-mem: agentic memory for llm agents.
  arXiv preprint arXiv:2502.12110.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.p3.1 "9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib18"></a>
- Yang et al. (2024)
  M. Yang, J. Chen, J. Tao, Y. Zhang, J. Liu, J. Zhang, Q. Ma, H. Verma, R. Zhang, M. Zhou, et al.
  Low-rank adaptation for foundation models: a comprehensive review.
  arXiv preprint arXiv:2501.00365.
  Cited by: [§9.3.2.1](#Ch9.S3.SS2.SSS1.p2.1 "9.3.2.1 Finetuning ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib36"></a>
- Yao et al. (2024)
  S. Yao, D. Yu, J. Zhao, I. Shafran, T. Griffiths, Y. Cao, and K. Narasimhan
  Tree of thoughts: deliberate problem solving with large language models.
  Advances in Neural Information Processing Systems 36.
  Cited by: [§9.2.1.4](#Ch9.S2.SS1.SSS4.p6.1 "9.2.1.4 D. Self-Reflection Harness ‣ 9.2.1 Agentic Interaction Styles ‣ 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models"),
  [Table 9.1](#Ch9.T1.3.8.4.1 "In 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib43"></a>
- Yao et al. (2022)
  S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao
  React: synergizing reasoning and acting in language models.
  arXiv preprint arXiv:2210.03629.
  Cited by: [Table 9.1](#Ch9.T1.3.10.4.1 "In 9.2 Learning Mechanisms in Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib30"></a>
- Yu et al. (2026)
  Y. Yu, L. Yao, Y. Xie, Q. Tan, J. Feng, Y. Li, and L. Wu
  Agentic memory: learning unified long-term and short-term memory management for large language model agents.
  arXiv preprint arXiv:2601.01885.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.Px1.p2.1 "Learning to use memory ‣ 9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib35"></a>
- Zhang et al. (2025a)
  A. L. Zhang, T. Kraska, and O. Khattab
  Recursive language models.
  arXiv preprint arXiv:2512.24601.
  Cited by: [§9.3.2.2](#Ch9.S3.SS2.SSS2.p2.1 "9.3.2.2 Long Context Windows and Compression ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib29"></a>
- Zhang et al. (2025b)
  Z. Zhang, Q. Dai, X. Bo, C. Ma, R. Li, X. Chen, J. Zhu, Z. Dong, and J. Wen
  A survey on the memory mechanism of large language model-based agents.
  ACM Transactions on Information Systems 43 (6), pp. 1–47.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.p2.1 "9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib28"></a>
- Zhong et al. (2024)
  W. Zhong, L. Guo, Q. Gao, H. Ye, and Y. Wang
  Memorybank: enhancing large language models with long-term memory.
  In Proceedings of the AAAI conference on artificial intelligence,
  Vol. 38, pp. 19724–19731.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.p2.1 "9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib1"></a>
- Zhou et al. (2026)
  W. Zhou, X. Zhou, S. Han, H. Xu, G. Li, Z. Li, F. Xiong, and F. Wu
  Are we ready for an agent-native memory system?.
  arXiv preprint arXiv:2606.24775.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.Px1.p3.1 "Learning to use memory ‣ 9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
<a id="bibh.bib7"></a>
- Zhou et al. (2025)
  Z. Zhou, A. Qu, Z. Wu, S. Kim, A. Prakash, D. Rus, J. Zhao, B. K. H. Low, and P. P. Liang
  MEM1: learning to synergize memory and reasoning for efficient long-horizon agents.
  arXiv preprint arXiv:2506.15841.
  Cited by: [§9.3.2.3](#Ch9.S3.SS2.SSS3.Px1.p1.1 "Learning to use memory ‣ 9.3.2.3 Explicit Memory Management ‣ 9.3.2 Memory Architectures ‣ 9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models").
