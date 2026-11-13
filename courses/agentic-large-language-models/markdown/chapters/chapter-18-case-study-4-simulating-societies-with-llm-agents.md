# Chapter 18 Case Study 4: Simulating Societies with LLM Agents

[Course index](../../README.md) · [Original source](https://arxiv.org/html/2610.13455v1#Ch18) · [Raw file](../../raw/originals/book.html)

Retrieved: 2026-11-13T16:41:17.579179+00:00

[Contents](../../CONTENTS.md) · [Full book](../book/full-book-html.md) · [Previous chapter](chapter-17-emergent-behavior-in-multi-llm-systems.md) · [Next chapter](chapter-19-synthetic-data-generation-for-training-agentic-llms.md)

<a id="Ch18"></a>


### Chapter 18 Case Study 4: Simulating Societies with LLM Agents

**What You Will Learn**

<a id="Ch18.p1.pic1.2.1.1"></a>
In this case study you will familiarize yourselves with agent-based social simulations through the lens of the widely adopted Generative Agents framework [[Park et al., 2023](#bibq.bib2)].
Specifically, you will be able to:

- Run and configure a *multi-agent social simulation* powered by LLMs.
- Work with a structured *machine-psychological* experiment.
- Compare two *cognitive architectures*: a standard memory system and one with a negativity bias.
- Investigate how *personality descriptions* and architectural choices shape emergent agent behavior.
- Critically reflect on *prompt fragility*, model dependence, and the limits of LLM-driven simulations.

<a id="Ch18.S1"></a>


#### 18.1 Social Simulation

<a id="Ch18.S1.p1.1"></a>


In social simulations, generative agents are LLM-driven characters that interact with an environment and with one another. The agents may plan activities, maintain memories, or reflect on their experiences. The Generative Agents Framework, introduced by [Park et al. [2023]](#bibq.bib2), showed that LLM-powered characters together can produce believable daily routines, social interactions, and even coordinated group activities—all emerging from a relatively simple and elegant cognitive architecture.

<a id="Ch18.S1.p2.1"></a>


The twist in this case study is that you will work with *two* cognitive architectures for your agents, run the same scenario with both, and compare the emergent behavior. One architecture treats all memories equally. The other introduces a *negativity bias*: negative experiences are encoded more strongly and are more likely to be retrieved and reflected upon. We will observe that this asymmetry, inspired by findings from cognitive psychology [[Baumeister et al., 2001](#bibq.bib3)], has measurable effects on our experimental agents.

The goal of this chapter is to understand how architectural choices—in our case, small changes in the internal processing of an agent—lead to emergent consequences. You will also see how fragile agent personas can be: a single word in a personality description, or a subtle change in memory weighting, can fundamentally alter how an agent acts, plans, and reflects.

<a id="Ch18.S1.SSx1"></a>


##### Course Materials

You can find the course exercise materials here:
  
<https://github.com/DorotaMoravcikova/agentic-llm-course-excercises>

<a id="Ch18.S2"></a>


#### 18.2 Background

<a id="Ch18.S2.SS1"></a>


##### 18.2.1 Generative Agents

<a id="Ch18.S2.SS1.p1.1"></a>


The generative agents framework, introduced by [Park et al. [2023]](#bibq.bib2), showed that LLM-powered characters can produce believable daily routines, social interactions, and even coordinate group activities.

Each agent has three core components:

1. Memory stream: a timestamped log of everything the agent has perceived, done, and thought.
2. Retrieval function: when the agent needs to act, it retrieves relevant memories based on recency, importance, and relevance to the current situation.
3. Reflection mechanism: periodically, the agent synthesizes higher-level insights from its raw memories.

The agent’s *personality* is defined by a short natural-language description—a *scratch* file that specifies the character’s name, age, learned and innate traits, and their lifestyle. This description is included in every LLM prompt, anchoring the agent’s behavior.

<a id="Ch18.S2.SS2"></a>


##### 18.2.2 Bad is Stronger Than Good

When an LLM-powered agent embedded in the original Generative Agents simulation receives criticism, it forms a memory. When praised an hour later, it forms another memory. Generative agents retrieve the two memories—one negative and one positive—with identical priority, as long as they are equally recent, equally relevant, and equally important.

<a id="Ch18.S2.SS2.p2.1"></a>


In general, cognitive architectures for agent-based social simulations draw on cognitive science to produce believable behavior. The recency, relevance, and importance variables are loosely inspired by insights about memory retrieval in humans. The importance variable captures something akin to the arousal or salience of an event. However, in the original simulation [[Park et al., 2022](#bibq.bib1)] the memory system is effectively valence-blind: all memories—positive, negative, neutral—are encoded and retrieved with equal weight. If the agent were human, it would treat the negatively valenced event differently: encoding it with sharper sensory detail, retrieving it with greater vividness, and rendering it more likely to resurface in subsequent thoughts. Psychological studies find that people remember insults longer than compliments. A single bad interaction with a colleague can outweigh weeks of pleasant ones. In other words, in our psychology *bad is stronger than good* [[Baumeister et al., 2001](#bibq.bib3)], and this asymmetry is nowhere more consequential than in memory.

In this case study, we test the effect of implementing the NEVER (Negative Emotional Valence Enhances Recapitulation) model, a more human-like mechanism for memory retrieval. In the NEVER-augmented agent, negative memories receive higher importance scores at encoding time. As a consequence, they are more likely to be retrieved and more likely to trigger reflections.

The architecture remains identical in every other respect. This allows for a controlled *machine-psychological* experiment in which the effects can be compared of an architectural choice: valence-blind versus valence-sensitive memory. In addition, you will use the structured setup to test the effects of adapting the agent initialisations in terms of their personality descriptions and system prompts.

<a id="Ch18.S2.SS3"></a>


##### 18.2.3 Why This Matters for Agent Design

This case study illustrates two important lessons:

1. Architectural choices have emergent consequences: A memory weighting parameter that seems innocuous at the component level can produce dramatic changes in the agent’s social behavior, emotional tone, and decision-making over time. These emergent effects are difficult to predict from the architecture alone.
2. Prompt fragility: Agent behavior is highly sensitive to the contents of personality descriptions and system prompts. Small perturbations can produce large behavioral shifts—a phenomenon sometimes called *prompt sensitivity* in the LLM literature.

<a id="Ch18.S3"></a>


#### 18.3 Implementation

<a id="Ch18.S3.SS1"></a>


##### 18.3.1 The Simulation Environment

<a id="Ch18.S3.SS1.p1.1"></a>


The simulation uses the Smallville environment from [Park et al. [2023]](#bibq.bib2): a small town rendered as a 2D tile map, where agents move between locations, interact with objects, and have conversations.

Our simulation features a simplified scenario: a cafe with three agents. Please meet:

- Dolores: A barista. Warm, empathetic, detail-oriented. The *experimental* agent—the one who will receive the negativity bias.
- Maeve: A barista with a matched personality profile. The *control* agent—standard architecture, no negativity bias.
- Bernard: The cafe manager. Unpredictable, moody, occasionally confrontational. Bernard serves as a naturalistic *stressor*: a source of social friction that both baristas are exposed to.

This setup with three agents of which two have a similar role and position (barista working under supervision of Bernard), allows for a controlled experiment with agent architectures and initializations. In our first step, Dolores and Maeve are given the same personality traits and are exposed to the same environment. The only difference is in how Dolores processes her memories: using the NEVER implementation that encodes negative memories with higher importance.

<a id="Ch18.S3.SS2"></a>


##### 18.3.2 Agent Architecture

Each agent maintains:

- A *personality description* (the scratch file): a short text describing the agent’s name, traits, occupation, relationships, and goals.
- A *memory stream*: a list of timestamped observations, actions, and reflections.
- A *current plan*: a short description of what the agent intends to do.

<a id="Ch18.S3.SS3"></a>


##### 18.3.3 The Cognitive Loop

At each simulation step (representing 10 seconds of in-game time), each agent executes the following cycle:

1. Perceive: Observe the current state of the environment—what other agents are doing, any ongoing conversations, changes in the surroundings.
2. Retrieve: Query the memory stream for relevant past experiences.
3. Plan: Given the personality description, retrieved memories, and current observations, use the LLM to decide what to do next.
4. Act: Execute the planned action in the environment.
5. Reflect (periodic): Every few hours of in-game time, synthesize higher-level reflections from recent memories.

Each of these steps involves an LLM call. The prompt is constructed from the agent’s personality description (which remains constant) and the relevant retrieved memories and current observations (which are dynamic).

<a id="Ch18.S3.SS4"></a>


##### 18.3.4 Two Architecture Variants

You will work with two variants of the retrieval function:

<a id="Ch18.S3.SS4.SSS0.Px1"></a>


###### Variant A: Baseline memory retrieval

<a id="Ch18.S3.SS4.SSS0.Px1.p1.1"></a>


Retrieval is based on a weighted combination of recency, relevance, and importance. This is the standard generative agent architecture as described by [Park et al. [2023]](#bibq.bib2).

<a id="Ch18.S3.SS4.SSS0.Px2"></a>


###### Variant B: Negativity-biased memory retrieval

When a new memory is created, its emotional valence is assessed. The retrieval function is extended with a valence term. Absolute valence is normalized to $[0,1]$ and multiplied by 1.5 for negative memories, producing a retrieval hierarchy (negative $>$ positive $>$ neutral). The retrieval score becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \textit{score}=\alpha_{\text{rec}}\cdot R+\alpha_{\text{rel}}\cdot L+\alpha_{\text{imp}}\cdot I+\alpha_{\text{val}}\cdot V $$ |  | (18.1) |

with all $\alpha=1$. Thus: the only difference between the two variants is the addition of the valence term; everything else is identical.

<a id="Ch18.S3.SS5"></a>


##### 18.3.5 Setup and Installation

Clone the repository and follow the instructions in the README:
  
<https://github.com/DorotaMoravcikova/generative_agents/tree/course-exercises>

<a id="Ch18.S4"></a>


#### 18.4 Discussion

Having run your experiments, reflect on the following questions:

1. Prompt versus Architecture: You have seen that both the personality prompt and the memory architecture influence agent behavior. Which lever is more powerful? Which is more predictable? If a simulation were to be used for consequential applications such as modeling policy adoption, which would you prefer to use to shape agent behavior, and why?
2. Emergent Behavior: Did you observe any agent behaviors that surprised you—things that were not explicitly specified in the personality or architecture? What mechanisms produced these emergent behaviors in your view?
3. Evaluation Challenges: How do you evaluate whether a generative agent is behaving well? The valence score is one metric, but it is itself an LLM judgment. What are the limitations of using an LLM to evaluate the output of another LLM (or the same LLM)? Can you think of alternative evaluation approaches?
4. Cognitive Realism: The negativity bias is one example of a finding from cognitive psychology. Can you think of other cognitive biases or memory effects that could be implemented architecturally? What would you expect their emergent effects to be? (Consider, for example: confirmation bias, the availability heuristic, recency bias.)

<a id="Ch18.S5"></a>


#### 18.5 Concluding Remarks

In this chapter we have familiarized ourselves with a generative agent simulation and used it to explore two important phenomena in agentic AI: the emergent effects of cognitive architecture choices (the negativity bias) and the sensitivity of agent behavior to prompt content (prompt fragility).

We have seen that a small change in how memories are weighted—negative memories receiving higher importance scores—can produce measurable shifts in agent behavior over time. We have also seen that agent personas are fragile: small changes to personality descriptions can produce large and sometimes unpredictable behavioral effects.

These findings have practical implications for anyone building LLM-driven agent systems. The persona is not a reliable anchor for behavior. The architecture—how memories are stored, retrieved, and reflected upon—shapes behavior in ways that may not be apparent from reading the code.

The field of generative agent simulation is young and evolving. The exercises in this chapter have given you hands-on experience with the core mechanisms and the core challenges. As the field matures, the problems of prompt robustness, cognitive architecture design, and emergent behavior evaluation will remain central.

<a id="bibq"></a>


### References

<a id="bibq.bib3"></a>
- Baumeister et al. (2001)
  R. F. Baumeister, E. Bratslavsky, C. Finkenauer, and K. D. Vohs
  Bad is stronger than good.
  Review of General Psychology 5 (4), pp. 323–370.
  Cited by: [§18.1](#Ch18.S1.p2.1 "18.1 Social Simulation ‣ Chapter 18 Case Study 4: Simulating Societies with LLM Agents ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models"),
  [§18.2.2](#Ch18.S2.SS2.p2.1 "18.2.2 Bad is Stronger Than Good ‣ 18.2 Background ‣ Chapter 18 Case Study 4: Simulating Societies with LLM Agents ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models").
<a id="bibq.bib2"></a>
- Park et al. (2023)
  J. S. Park, J. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein
  Generative agents: interactive simulacra of human behavior.
  In Proceedings of the 36th annual acm symposium on user interface software and technology,
  pp. 1–22.
  Cited by: [§18.1](#Ch18.S1.p1.1 "18.1 Social Simulation ‣ Chapter 18 Case Study 4: Simulating Societies with LLM Agents ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models"),
  [§18.2.1](#Ch18.S2.SS1.p1.1 "18.2.1 Generative Agents ‣ 18.2 Background ‣ Chapter 18 Case Study 4: Simulating Societies with LLM Agents ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models"),
  [§18.3.1](#Ch18.S3.SS1.p1.1 "18.3.1 The Simulation Environment ‣ 18.3 Implementation ‣ Chapter 18 Case Study 4: Simulating Societies with LLM Agents ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models"),
  [§18.3.4](#Ch18.S3.SS4.SSS0.Px1.p1.1 "Variant A: Baseline memory retrieval ‣ 18.3.4 Two Architecture Variants ‣ 18.3 Implementation ‣ Chapter 18 Case Study 4: Simulating Societies with LLM Agents ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models"),
  [Chapter 18](#Ch18.p1.pic1.2.1.1 "Chapter 18 Case Study 4: Simulating Societies with LLM Agents ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models").
<a id="bibq.bib1"></a>
- Park et al. (2022)
  J. S. Park, L. Popowski, C. Cai, M. R. Morris, P. Liang, and M. S. Bernstein
  Social simulacra: creating populated prototypes for social computing systems.
  In Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology,
  pp. 1–18.
  Cited by: [§18.2.2](#Ch18.S2.SS2.p2.1 "18.2.2 Bad is Stronger Than Good ‣ 18.2 Background ‣ Chapter 18 Case Study 4: Simulating Societies with LLM Agents ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models").
