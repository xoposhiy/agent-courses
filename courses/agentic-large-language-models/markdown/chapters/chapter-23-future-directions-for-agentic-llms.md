# Chapter 23 Future Directions for Agentic LLMs

[Course index](../../README.md) · [Original source](https://arxiv.org/html/2610.13455v1#Ch23) · [Raw file](../../raw/originals/book.html)

Retrieved: 2026-11-13T16:41:17.579179+00:00

[Contents](../../CONTENTS.md) · [Full book](../book/full-book-html.md) · [Previous chapter](chapter-22-cognitive-perspectives-on-agentic-llms.md)

<a id="Ch23"></a>


### Chapter 23 Future Directions for Agentic LLMs

Having arrived at the end of this book, we provide a brief high-level summary of the material that we have discussed. First we look back at our chapters about how agentic LLMs are built. Then we summarize our discussion of different applications of agentic LLMs and their behavior in single and multi-agent settings. Finally, in Section [23.2](#Ch23.S2 "23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models") we look at the limitations of current approaches, and what the future may bring.

<a id="Ch23.S1"></a>


#### 23.1 The State of Agentic LLMs

As discussed in Parts I, II, and III, the foundations of agentic LLMs lie in language modeling, reasoning, tool use, and different degrees of autonomy.

<a id="Ch23.S1.SS1"></a>


##### 23.1.1 Technology

Agentic LLMs are reasoning models that act in the world and adapt their behavior from feedback. After having been pretrained and finetuned (Chapter [3](chapter-03-the-large-language-model-training-pipeline.md#Ch3 "Chapter 3 The Large Language Model Training Pipeline ‣ Part I Language Modeling ‣ Agentic Large Language Models")), at inference time they may access to external information (retrieval augmented generative AI, Chapter [12](chapter-12-search-and-retrieval-in-agentic-llms.md#Ch12 "Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")). They may also prompt themselves at inference time to verify results, leading to self-reflection and in-context reinforcement learning, Chapter [6](chapter-06-multi-step-reasoning-in-llms.md#Ch6 "Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models"). Agentic LLMs have become multi-modal, they operate in language, vision, and action domains (Chapter [7](chapter-07-vision-action-and-world-models.md#Ch7 "Chapter 7 Vision, Action and World Models ‣ Part II Reasoning ‣ Agentic Large Language Models")). To do so effectively, agentic LLMs can be provided with pretrained world models with a rudimentary understanding of the physical world. Through interacting with the environment, these world models may be improved at test time.

The main machine learning architecture used is the transformer architecture. Models are pretrained through self-supervision (next-token prediction) and finetuned on specific tasks through supervised and reinforcement learning.

In-context chain of thought prompting has improved reasoning abilities of models significantly. Inference-time methods have been developed for finetuning (such as RLVR and GRPO) and self-reflection (such as ReAct and reflexion, Chapter [6](chapter-06-multi-step-reasoning-in-llms.md#Ch6 "Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models")). A whole spectrum of agent-environment interaction prompting styles have been developed (Chapter [9](chapter-09-interaction-styles-for-agentic-llms.md#Ch9 "Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models")).

<a id="Ch23.S1.SS2"></a>


##### 23.1.2 Applications

In Part IV, various tools have been introduced to ease the construction of agentic LLMs (Chapter [11](chapter-11-how-agents-use-tools-to-act-in-the-world.md#Ch11 "Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")). Agentic LLMs have been designed for many different applications. In e-commerce, they can help understand the preferences of their users and act on recommendations. In medicine, they can read and summarize diagnostic texts. In finance, they can analyze financial reports and provide recommendations to traders. In science and education, they can help in literature research, they can generate scripts to run experiments, they can analyze results, they can help write papers, and they can help review them (Chapter [13](chapter-13-from-tools-to-assistants-real-world-applications.md#Ch13 "Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")).

<a id="Ch23.S1.SS3"></a>


##### 23.1.3 Behavior

In Part V we shifted gears from looking at agentic LLMs through a technical lens, to studying how they behave in single-agent and multi-agent settings. After discussing basic behavioral features of LLMs, in Chapter [15](chapter-15-studying-behavior-of-agentic-llms.md#Ch15 "Chapter 15 Studying Behavior of Agentic LLMs ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models") we discussed how LLM-driven agents perform on tasks adapted from human behavioral approaches and frameworks developed especially for AI benchmarking. Chapter [16](chapter-16-role-based-interaction-in-multi-llm-systems.md#Ch16 "Chapter 16 Role-Based Interaction in Multi-LLM Systems ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models") looked closely at multi-agent interactions that built on predefined roles and protocols. In Chapter [17](chapter-17-emergent-behavior-in-multi-llm-systems.md#Ch17 "Chapter 17 Emergent Behavior in Multi-LLM Systems ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models") focus shifted to open-ended settings in which the object of study were the behavioral structures, norms, and conventions that emerged at system level from small-scale interactions between agents.

Various recurring patterns were identified throughout the approaches and studies discussed in Part V. These include the discussions on construct validity (how do observations generalize to the human situation), prompt sensitivity and cascading effects (especially in multi-agent settings), the knowing-doing gap (models’ capabilities at verbal predicting often did not translate well into actions), positive effects of structured reasoning (increasing reasoning budgets was particularly useful when structured along lines inspired on human reasoning), and emergent properties in desired directions (performance above baseline matched for compute budget) and undesired directions (norm violations) were observed.

<a id="Ch23.S2"></a>


#### 23.2 Limitations and Future Work

Agentic LLMs build on the power of large language models, and have greatly expanded the capabilities and uses of LLMs. However, there are still many limitations, which we will discuss next.
We progress from memory, scale, explainability, and cognitive architectures, which are more technical, to topics with broad implications such as potential sentience or consciousness and ethical implications that follow from such properties. For some of these topics, solution directions have been discussed in the preceding chapters.

<a id="Ch23.S2.SS1"></a>


##### 23.2.1 Memory and Self-reflection

Language models are functions: the output that they compute is only based on their input—they are memory-less between calls. In order for agents to act naturally in the world, to hold a conversation, to be able to learn from their actions by self-reflection, agents must be able to remember. For us, our identity hinges on our ability to remember. Agents require a form of memory.

A simple way to achieve a rudimentary form of memory is to feed the past interaction history back into the prompt—and current chatbots use this method with success. However, context windows remain limited in size, despite some success with research into long-context models. Agentic memory methods are an active area of research. LLMs should learn how to best compact information and store it in long or short term memory.

Agents can access outside information through retrieval-augmented generative AI methods (RAG), for example from corporate databases.
Elaborate agentic memory architectures are being developed to provide agents with longer term memory, either textual, or token embeddings, in vector databases (Section [9.3](chapter-09-interaction-styles-for-agentic-llms.md#Ch9.S3 "9.3 Memory Architectures for Agentic LLMs ‣ Chapter 9 Interaction Styles for Agentic LLMs ‣ Part III Agents ‣ Agentic Large Language Models")).

<a id="Ch23.S2.SS2"></a>


##### 23.2.2 Scale

As agents become able to self-reflect and to learn from interactions with their environment, we should discuss the topic of scaling of the underlying language models.

<a id="Ch23.S2.SS2.p2.1"></a>


A major challenge in the development of large language models is how to further improve their performance. Originally, size was the major determinant—hence the name *large* language models—only models of sufficient size and trained on sufficiently large text corpuses achieved adequate benchmark performance, and only large models exhibited in-context learning. Scaling the size of the model and of the data thus appeared to be the way forward. However, scaling further is becoming more and more difficult, as most high-quality data that is available on the Internet has been now used to train current models. Also, training longer and larger models is expensive; time, money and power consumption are limiting this direction. Current methods are reaching a plateau [[Sutskever, 2024](#bibv.bib27)].

<a id="Ch23.S2.SS2.p3.1"></a>


To improve LLM performance further, it is important to continue to acquire training
data that is challenging (Chapter [19](chapter-19-synthetic-data-generation-for-training-agentic-llms.md#Ch19 "Chapter 19 *Synthetic Data Generation for Training Agentic LLMs ‣ Part VI Advanced Topics ‣ Agentic Large Language Models")). One approach is to use the interactions of agentic LLMs with their environment as training data. When this interaction data is new, diverse, and high quality, it can be used for pretraining (see also Figure [1.1](chapter-01-introduction.md#Ch1.F1 "Figure 1.1 ‣ 1.2.4 Training Data ‣ 1.2 Concepts and Definitions ‣ Chapter 1 Introduction ‣ Agentic Large Language Models")). Note that already inference-time methods such as GRPO and RLVR are using inference-time results for finetuning with good results [[Guo et al., 2025](#bibv.bib6)], and VLAs are trained on self-generated action data [[Black et al., 2024](#bibv.bib7), [Brohan et al., 2023](#bibv.bib26)], Chapter [7](chapter-07-vision-action-and-world-models.md#Ch7 "Chapter 7 Vision, Action and World Models ‣ Part II Reasoning ‣ Agentic Large Language Models").

<a id="Ch23.S2.SS2.SSS0.Px1"></a>


###### Overthinking

<a id="Ch23.S2.SS2.SSS0.Px1.p1.1"></a>


Scaling studies into chain of thought also reveal limitations of more thinking effort. Chain of thought works better for some domains than for others [[Sprague et al., 2024](#bibv.bib14)]. Furthermore, deeper reasoning may lead to *overthinking*, where the reasoning process becomes less effective as more effort is spent [[Liu et al., 2024](#bibv.bib16), [Wu et al., 2025](#bibv.bib13)]. Studies are ongoing and reveal more insight into how chain of thought works [[Chen et al., 2026b](#bibv.bib34)], and which mechanism are effective [[Chen et al., 2026a](#bibv.bib15)].

<a id="Ch23.S2.SS2.SSS0.Px2"></a>


###### Open World Models and Curriculum Learning

<a id="Ch23.S2.SS2.SSS0.Px2.p1.1"></a>


For the scaling approach to work it is important that synthetic training data is diverse, and different from the existing data. Open world models are studied to specifically generate diverse training environments. The idea of an open world-model is that it can create infinite datasets or environments, in which agents can continue to learn, to keep improving their intelligence [[Bruce et al., 2024](#bibv.bib5)]. Open world models are inspired by evolutionary algorithms, quality diversity, and computer games [[Vinyals et al., 2019](#bibv.bib31), [Mouret and Clune, 2015](#bibv.bib4), [Bakhtin et al., 2022](#bibv.bib32)].

<a id="Ch23.S2.SS2.SSS0.Px2.p2.1"></a>


Another approach to further scale model performance is to create better training methods. Curriculum learning is built on the observation that most learning works better if a system is first trained on easy tasks, before harder tasks are tried. (This holds both for human brains and for artificial neural networks.) In most domains a hierarchy of concepts exists that are related and build upon each other. (In school we learn addition before we learn long division, or even logarithms.) Curriculum methods are being tried for both pre- and posttraining [[Chen et al., 2025](#bibv.bib8), [Elgaar and Amiri, 2026](#bibv.bib9)].

<a id="Ch23.S2.SS3"></a>


##### 23.2.3 Hallucination and Explainability

Another limitation of current agentic LLMs is the problem of hallucination: models often provide answers that sound plausible but are factually incorrect, and their stated reasoning may not be causally responsible for the output they produce—a property known as *faithfulness*.

The field of explainable AI (XAI) provides a spectrum of techniques to address this, ranging from behavioral and attribution-based methods such as SHAP and LIME, which treat the model as a black box, to concept-based interpretability, which probes internal representations for human-understandable features. Going further, mechanistic interpretability (MI), as discussed in Chapter [21](chapter-21-mechanistic-interpretability-for-llm-agents.md#Ch21 "Chapter 21 *Mechanistic Interpretability for LLM Agents ‣ Part VI Advanced Topics ‣ Agentic Large Language Models"), aims to reverse-engineer the computational circuits inside transformer models.

Tools such as sparse autoencoders, neural lenses and activation patching have already been used to identify specific circuits responsible for hallucination and to provide empirical evidence that chain of thought reasoning can be a faithful, causally active component of model behavior in sufficiently large architectures. As agentic LLMs are increasingly deployed in high-stakes settings, MI offers a path toward hallucination detectors that trigger when a model’s internal confidence features diverge from its external output—a critical step toward accountable agentic systems.

A step further is the comparison of cognitive architectures between humans and transformers. Language models appear to produce natural language in a way that is similar to humans. Is that because the architectures that produce the utterances are similar, is it by coincidence, or is there another explanation? Chapter [22](chapter-22-cognitive-perspectives-on-agentic-llms.md#Ch22 "Chapter 22 *Cognitive Perspectives on Agentic LLMs ‣ Part VI Advanced Topics ‣ Agentic Large Language Models") explored this question.

<a id="Ch23.S2.SS4"></a>


##### 23.2.4 Emotional Behavior and Consciousness

Humans have a tendency to anthropomorphize: to attribute purposeful behavior to inanimate objects in their surroundings, when they behave in ways that are similar to our behavior, and sometimes even when they do not. Implicitly, we may attribute consciousness to such objects. This leads us to believe and say things such as *the computer is thinking*, *the computer wants*, and *the computer must not be feeling well* (or even *this book loves to be read*). LLMs suffer the same fate, and their utterances may from time to time persuade even the most rational philosophers to believe that they have a purpose (whereas they clearly cannot have a purpose, since they are merely algorithms that are being performed by a mechanical device---unlike humans, since we are organic).11
1
Note that the duck-typing point of view disagrees, this behaviorist view holds that if it walks like a duck and quacks like a duck, then we consider it a duck.

Reports have been published about emotional relations between chatbots and humans, sometimes leading to dangerous behavior, and worse.

<a id="Ch23.S2.SS4.p3.1"></a>


The topic of consciousness is actively debated by AI philosophers. Consciousness is generally assumed to mean being aware of oneself and the environment, and having subjective experiences, thoughts, and feelings [[Velmans, 2009](#bibv.bib10), [Butlin et al., 2023](#bibv.bib1)]. But how do we test for consciousness?
A pragmatic view is that for our society, behavior is what counts. If an entity acts, the consequences of its actions are what matters, and less so whether the entity was conscious or not. [Bengio and Elmoznino [2025]](#bibv.bib11) argue that the mere illusion of consciousness, through actions, has consequences, and that it will become increasingly difficult for us to discern conscious entities from non-conscious entities. They argue that society must find answers on how to deal with agents that act, whether in medicine, finance, or science. Both credit and liability must ultimately be attributed in a fair way, and answers must be found on how to handle self-preserving AI systems.

<a id="Ch23.S2.SS5"></a>


##### 23.2.5 Social Behavior

We have discussed examples of how LLMs can simulate reasoning by humans (Chapter [15](chapter-15-studying-behavior-of-agentic-llms.md#Ch15 "Chapter 15 Studying Behavior of Agentic LLMs ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models")), and how LLMs can improve simulations of social behavior in multi-agent systems. A limitation of current simulations of social behavior of agents is that the behavior is heavily influenced by the prompt script. Although some studies found realistic social behavior, many studies also found limits where the LLMs fail.

<a id="Ch23.S2.SS5.p2.1"></a>


Furthermore, the study of emergent behavior at scale poses challenges (Chapter [17](chapter-17-emergent-behavior-in-multi-llm-systems.md#Ch17 "Chapter 17 Emergent Behavior in Multi-LLM Systems ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models")).
As with all multi-agent simulations, validation of the emergent behavior, to see how realistic the simulated behavior is, is a challenge, although some studies report impressive results [[Park et al., 2024](#bibv.bib30)].

<a id="Ch23.S2.SS6"></a>


##### 23.2.6 Legal and Ethical Aspects

Actions by assistants in the real world have real world consequences. Many legal and ethical challenges exist for agentic LLMs that act, when the actions of imperfect models have real world consequences. When a financial trading assistant hallucinates, or when a self driving robot makes a wrong inference, questions of responsibility and liability should be addressed, before such systems are deployed in the real world.

<a id="Ch23.S2.SS6.p2.1"></a>


A major area of research is to improve the safety on the technical side.
Ensuring the safety of agentic LLMs requires moving beyond prompt-based defenses toward integrated, multi-layer safeguards. In the field of safe reinforcement learning, a key direction is to include explicit safety constraints on the agent’s actions and within the agent’s reasoning and planning pipeline [[Gu et al., 2024](#bibv.bib2)].

<a id="Ch23.S2.SS6.p3.1"></a>


Another approach to improve safety is to employ continual adversarial training and automated red-teaming to enhance robustness against manipulation. Further priorities are developing mechanisms for self-regulation and risk awareness, enabling agents to detect and avoid unsafe actions, and establishing rigorous, standardized safety benchmarks [[Andriushchenko et al., 2024](#bibv.bib28)]. Together, these measures outline a roadmap for accountable and trustworthy deployment of agentic LLMs in high-stakes domains.

<a id="Ch23.S2.SS6.p4.1"></a>


However, legal and ethical questions about who is responsible for the actions of an agent remain. Now that agents are starting to be employed in the real world, addressing these issues becomes of paramount importance.
Clearly, many safety, ethics and trust issues
will have to be addressed before the full breadth of the possibilities
of agentic LLMs can be enjoyed.
Safety and ethics will become important topics on the research agenda of agentic LLMs, deserving their own surveys and books [[Gan et al., 2024](#bibv.bib21), [Jiao et al., 2025](#bibv.bib22), [Raza et al., 2025](#bibv.bib23)].

<a id="Ch23.S2.SS7"></a>


##### 23.2.7 Crime

The discussion on ethics and consciousness becomes quite concrete when we consider criminal behavior. Technological developments can be used by people who act within the law, and those who act outside of the law. They can also be used for unethical behavior for which no effective laws yet exist.
As agentic LLMs are able to display more and more believable behavior, it will become difficult to distinguish real and artificial behavior. This may lead to dangerous ethical situations, for example when criminals use the technology to influence the behavior of unsuspecting victims.

<a id="Ch23.S2.SS7.p2.1"></a>


The line between lawful persuasion, misuse of confidence, and fraud, can be unclear.
Agentic LLMs will greatly increase the sophistication of social engineering using persuasive algorithms in social networks, marketing, espionage, and cybercrime [[Kshetri, 2025](#bibv.bib24), [Lupinacci et al., 2025](#bibv.bib12)]. Although agentic LLM can also be used to combat crime [[Challita and Parrend, 2025](#bibv.bib18), [Andriushchenko et al., 2024](#bibv.bib28)], it will be some time before societal awareness will have caught up with the risks. Especially people who are less familiar with social networks and LLMs may be susceptible to confidence tricks and agentic LLM cybercrime.

<a id="Ch23.S2.SS8"></a>


##### 23.2.8 Limitations of Applications

The list of applications of agentic LLMs is large. Proofs of concept have been created that impress us with their results, at first sight. When we look deeper at the results, limitations appear that may not be easy to fix and that may have serious consequences when the agents are used in the real world.

<a id="Ch23.S2.SS8.SSS1"></a>


###### 23.2.8.1 AI Science

Many agentic LLMs are developed to support scientific research. All phases of the research pipeline are being supported. Tools for summarizing literature helps the ideation phase, tools exist to generate scripts for running experiments in different fields, there is support for data interpretation and for creation of graphs, writing support exists, as well as tools to support the reviewing of scientific manuscripts. Indeed, it is becoming easier and easier to produce research papers that are well-written and that look good, on the surface.

<a id="Ch23.S2.SS8.SSS1.p2.1"></a>


In mathematics, impressive results are reported that LLM agents perform on the level of math olympiads, both in geometry [[Trinh et al., 2024](#bibv.bib20)] and in algebra [[Hubert et al., 2025](#bibv.bib19)]. These systems include transformer networks, but are otherwise designed as mathematics solvers, using specialized automated theorem proving technology such as Lean [[De Moura et al., 2015](#bibv.bib17)] and reinforcement learning [[Silver et al., 2017](#bibv.bib33), [Browne et al., 2012](#bibv.bib25)].

<a id="Ch23.S2.SS8.SSS1.p3.1"></a>


In 2025 a benchmark study was performed on AI science tools on a range of domains from machine learning [[Nathani et al., 2025](#bibv.bib29)]. Using then-current frontier models, the authors did not find that models could generate novel
hypotheses, algorithms, architectures, or make substantial scientific improvements. In particular, the authors note that *modern LLM agents can successfully tackle a diverse array of quantitative
experiments, reflecting advanced skills and domain adaptability* but also that *it is not yet clear if the notion of scientific novelty can
be successfully automated or even formally defined in a form suitable for agents*.

<a id="Ch23.S2.SS8.SSS2"></a>


###### 23.2.8.2 E-commerce

Liability for actions is a major problem for deploying agentic LLMs in e-commerce. Security and privacy concerns will inhibit users from providing personal details and preference to leaky computer systems. This leads to the catch-22 situation of recommender systems: when users are unwilling to provide elaborate information about their true preferences, the quality of suggestions will be low, users will have low trust in the system, and will be even less willing to provide information. Only when it is easy to collect high quality information about preferences, in a safe and secure way, and when the models are able to provide strong and useful suggestions, will agentic LLM for e-commerce be adopted by the public.

<a id="Ch23.S2.SS8.SSS3"></a>


###### 23.2.8.3 Trading

For financial trading liability is of paramount importance.
Studies report that LLMs can be better than human analysts in summarizing large volumes of financial reports. However, in financial trading the stakes are high. Wrong trading advice will directly lead to financial loss. Furthermore, given the unpredictable nature of financial markets, it may take some time to recognize an erroneous model, since it will not be clear when an individual loss is caused be an imperfection in the model or just by an unlucky trade. Models should be thoroughly tested before they will be trusted enough to be used. Unless bulletproof, automated trading systems will not go beyond support of human decision making.

<a id="Ch23.S2.SS8.SSS3.p2.1"></a>


LLMs in finance are mostly successful in analyzing textual reports. For time series analysis of financial data some results are published, but it is hard to achieve reliable and verifiable benchmark results.
Although some studies claim good results, others report that predictions by agentic LLM of financial market results remain in doubt [[Li et al., 2026](#bibv.bib3)].

<a id="Ch23.S2.SS8.SSS4"></a>


###### 23.2.8.4 Medicine

Accuracy and especially explainability of results are even more important for trustworthiness in medicine. In medicine, model predictions are directly related to liability and ethics of actions. For medical applications, explainability of results is essential, and agentic LLM systems will include a human in the decision making loop.

As in trading, the most promising results of agentic LLM in medicine are in the analysis and summarization of textual documents, such as meeting reports or literature surveys. Results in other applications, such as decisions on treatment plans, or performing operations, are limited.

Medicine might well be one of the most valuable and at the same time one of the most conservative fields of application for agentic LLM. In matters of life and death, we should be extra careful, and at the same time the potential gains are large.

<a id="Ch23.S3"></a>


#### 23.3 Concluding Remarks

Agentic LLM technology is developing at a rapid pace. This book has
traced that development across three interconnected pillars: *reasoning*,
*acting*, and *interacting*. Reasoning LLMs provide the cognitive
foundation, through chain of thought, self-reflection, and retrieval
augmentation: models have become capable of multi-step problem solving,
literature synthesis, and complex decision support. Acting agents extend this
foundation into the real world, using tools, APIs, and world models to assist
users in domains from robotics to finance to medicine. Interacting agents go
further still, engaging with one another in multi-agent simulations that
exhibit emergent social behaviors such as cooperation, trust, and norm formation, that
were not explicitly scripted in the prompts.

These three pillars are connected. As Figure [1.1](chapter-01-introduction.md#Ch1.F1 "Figure 1.1 ‣ 1.2.4 Training Data ‣ 1.2 Concepts and Definitions ‣ Chapter 1 Introduction ‣ Agentic Large Language Models")
illustrates, they form a cycle: reasoning enables better acting and
interacting, while the data generated by (inter)acting agents can be used to pretrain and finetune better reasoning models. This virtuous cycle
offers a promising path beyond plateaus in LLM scaling, as
inference-time interaction data from agentic assistants, robotic systems, and
multi-agent simulations, provides a continuously replenishing source of
high-quality, diverse training signals.

Yet, significant challenges remain across all three pillars. Hallucination
undermines trust in reasoning chains and threatens the stability of
self-improving systems. Safety, liability, and ethical accountability are
unresolved for acting agents in high-stakes domains. Emergent behavior in
large-scale multi-agent systems remains difficult to validate and control.
Further research in the fields of mechanistic interpretability, open world models, scalable simulation infrastructures, and robust safety
benchmarks is required to overcome these challenges.

We are at an early and consequential moment. Proofs of concept are
impressive; real-world deployments are beginning; and the theoretical
foundations—of memory, metacognition, consciousness, and collective
intelligence—remain open questions that connect artificial intelligence to
philosophy, cognitive science and law. This book has aimed to give you the
technical grounding and conceptual vocabulary to contribute to these
questions. The field needs researchers who understand both the power and the
limits of what agentic LLMs can do today, and who can help shape what they
will become tomorrow.

<a id="bibv"></a>


### References

<a id="bibv.bib28"></a>
- Andriushchenko et al. (2024)
  M. Andriushchenko, A. Souly, M. Dziemian, D. Duenas, M. Lin, J. Wang, D. Hendrycks, A. Zou, Z. Kolter, M. Fredrikson, et al.
  Agentharm: a benchmark for measuring harmfulness of llm agents.
  arXiv preprint arXiv:2410.09024.
  Cited by: [§23.2.6](#Ch23.S2.SS6.p3.1 "23.2.6 Legal and Ethical Aspects ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models"),
  [§23.2.7](#Ch23.S2.SS7.p2.1 "23.2.7 Crime ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib32"></a>
- Bakhtin et al. (2022)
  A. Bakhtin, N. Brown, E. Dinan, G. Farina, C. Flaherty, D. Fried, A. Goff, J. Gray, H. Hu, et al.
  Human-level play in the game of diplomacy by combining language models with strategic reasoning.
  Science 378 (6624), pp. 1067–1074.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px2.p1.1 "Open World Models and Curriculum Learning ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib11"></a>
- Bengio and Elmoznino (2025)
  Y. Bengio and E. Elmoznino
  Illusions of ai consciousness.
  Science 389 (6765), pp. 1090–1091.
  Cited by: [§23.2.4](#Ch23.S2.SS4.p3.1 "23.2.4 Emotional Behavior and Consciousness ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib7"></a>
- Black et al. (2024)
  K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, et al.
  $\pi_{0}$: A vision-language-action flow model for general robot control.
  arXiv preprint arXiv:2410.24164.
  Cited by: [§23.2.2](#Ch23.S2.SS2.p3.1 "23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib26"></a>
- Brohan et al. (2023)
  A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess, A. Dubey, C. Finn, et al.
  Rt-2: vision-language-action models transfer web knowledge to robotic control.
  arXiv preprint arXiv:2307.15818.
  Cited by: [§23.2.2](#Ch23.S2.SS2.p3.1 "23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib25"></a>
- Browne et al. (2012)
  C. B. Browne, E. Powley, D. Whitehouse, S. M. Lucas, P. I. Cowling, P. Rohlfshagen, S. Tavener, D. Perez, S. Samothrakis, and S. Colton
  A survey of monte carlo tree search methods.
  IEEE Transactions on Computational Intelligence and AI in games 4 (1), pp. 1–43.
  Cited by: [§23.2.8.1](#Ch23.S2.SS8.SSS1.p2.1 "23.2.8.1 AI Science ‣ 23.2.8 Limitations of Applications ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib5"></a>
- Bruce et al. (2024)
  J. Bruce, M. D. Dennis, A. Edwards, J. Parker-Holder, Y. Shi, E. Hughes, M. Lai, A. Mavalankar, R. Steigerwald, C. Apps, et al.
  Genie: generative interactive environments.
  In Forty-first International Conference on Machine Learning,
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px2.p1.1 "Open World Models and Curriculum Learning ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib1"></a>
- Butlin et al. (2023)
  P. Butlin, R. Long, E. Elmoznino, Y. Bengio, J. Birch, A. Constant, G. Deane, S. M. Fleming, C. Frith, X. Ji, R. Kanai, C. Klein, G. Lindsay, M. Michel, L. Mudrik, M. A. K. Peters, E. Schwitzgebel, J. Simon, and R. VanRullen
  Consciousness in artificial intelligence: insights from the science of consciousness.
  External Links: 2308.08708,
  [Document](https://dx.doi.org/10.48550/arXiv.2308.08708)
  Cited by: [§23.2.4](#Ch23.S2.SS4.p3.1 "23.2.4 Emotional Behavior and Consciousness ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib18"></a>
- Challita and Parrend (2025)
  B. Challita and P. Parrend
  RedTeamLLM: an agentic ai framework for offensive security.
  arXiv preprint arXiv:2505.06913.
  Cited by: [§23.2.7](#Ch23.S2.SS7.p2.1 "23.2.7 Crime ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib15"></a>
- Chen et al. (2026a)
  W. Chen, L. Peng, T. Tan, C. Zhao, B. J. Chen, Z. Lin, A. Go, and Y. Meng
  Think deep, not just long: measuring llm reasoning effort via deep-thinking tokens.
  arXiv preprint arXiv:2602.13517.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px1.p1.1 "Overthinking ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib34"></a>
- Chen et al. (2026b)
  X. Chen, A. Plaat, and N. van Stein
  How does chain of thought think? mechanistic interpretability of chain-of-thought reasoning with sparse autoencoding.
  In AAAI2026, arXiv preprint arXiv:2507.22928,
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px1.p1.1 "Overthinking ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib8"></a>
- Chen et al. (2025)
  X. Chen, J. Lu, M. Kim, D. Zhang, J. Tang, A. Piché, N. Gontier, Y. Bengio, and E. Kamalloo
  Self-evolving curriculum for llm reasoning.
  arXiv preprint arXiv:2505.14970.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px2.p2.1 "Open World Models and Curriculum Learning ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib17"></a>
- De Moura et al. (2015)
  L. De Moura, S. Kong, J. Avigad, F. Van Doorn, and J. von Raumer
  The lean theorem prover (system description).
  In International Conference on Automated Deduction,
  pp. 378–388.
  Cited by: [§23.2.8.1](#Ch23.S2.SS8.SSS1.p2.1 "23.2.8.1 AI Science ‣ 23.2.8 Limitations of Applications ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib9"></a>
- Elgaar and Amiri (2026)
  M. Elgaar and H. Amiri
  Curriculum learning for llm pretraining: an analysis of learning dynamics.
  arXiv preprint arXiv:2601.21698.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px2.p2.1 "Open World Models and Curriculum Learning ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib21"></a>
- Gan et al. (2024)
  Y. Gan, Y. Yang, Z. Ma, P. He, R. Zeng, Y. Wang, Q. Li, C. Zhou, S. Li, T. Wang, et al.
  Navigating the risks: a survey of security, privacy, and ethics threats in LLM-based agents.
  arXiv preprint arXiv:2411.09523.
  Cited by: [§23.2.6](#Ch23.S2.SS6.p4.1 "23.2.6 Legal and Ethical Aspects ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib2"></a>
- Gu et al. (2024)
  S. Gu, L. Yang, Y. Du, G. Chen, F. Walter, J. Wang, and A. Knoll
  A review of safe reinforcement learning: methods, theories, and applications.
  IEEE Transactions on Pattern Analysis and Machine Intelligence 46 (12), pp. 11216–11235.
  Cited by: [§23.2.6](#Ch23.S2.SS6.p2.1 "23.2.6 Legal and Ethical Aspects ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib6"></a>
- Guo et al. (2025)
  D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al.
  Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning.
  arXiv preprint arXiv:2501.12948.
  Cited by: [§23.2.2](#Ch23.S2.SS2.p3.1 "23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib19"></a>
- Hubert et al. (2025)
  T. Hubert, R. Mehta, L. Sartran, M. Z. Horváth, G. Žužić, E. Wieser, A. Huang, J. Schrittwieser, Y. Schroecker, H. Masoom, et al.
  Olympiad-level formal mathematical reasoning with reinforcement learning.
  Nature, pp. 1–3.
  Cited by: [§23.2.8.1](#Ch23.S2.SS8.SSS1.p2.1 "23.2.8.1 AI Science ‣ 23.2.8 Limitations of Applications ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib22"></a>
- Jiao et al. (2025)
  J. Jiao, S. Afroogh, Y. Xu, and C. Phillips
  Navigating LLM ethics: advancements, challenges, and future directions.
  AI and Ethics, pp. 1–25.
  Cited by: [§23.2.6](#Ch23.S2.SS6.p4.1 "23.2.6 Legal and Ethical Aspects ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib24"></a>
- Kshetri (2025)
  N. Kshetri
  Transforming cybersecurity with agentic ai to combat emerging cyber threats.
  Telecommunications Policy 49 (6), pp. 102976.
  Cited by: [§23.2.7](#Ch23.S2.SS7.p2.1 "23.2.7 Crime ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib3"></a>
- Li et al. (2026)
  W. W. Li, H. Kim, M. Cucuringu, and T. Ma
  Can llm-based financial investing strategies outperform the market in long run?.
  In Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 1,
  pp. 2711–2722.
  Cited by: [§23.2.8.3](#Ch23.S2.SS8.SSS3.p2.1 "23.2.8.3 Trading ‣ 23.2.8 Limitations of Applications ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib16"></a>
- Liu et al. (2024)
  R. Liu, J. Geng, A. J. Wu, I. Sucholutsky, T. Lombrozo, and T. L. Griffiths
  Mind your step (by step): chain-of-thought can reduce performance on tasks where thinking makes humans worse.
  arXiv preprint arXiv:2410.21333.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px1.p1.1 "Overthinking ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib12"></a>
- Lupinacci et al. (2025)
  M. Lupinacci, F. A. Pironti, F. Blefari, F. Romeo, L. Arena, and A. Furfaro
  The dark side of llms: agent-based attacks for complete computer takeover.
  arXiv preprint arXiv:2507.06850.
  Cited by: [§23.2.7](#Ch23.S2.SS7.p2.1 "23.2.7 Crime ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib4"></a>
- Mouret and Clune (2015)
  J. Mouret and J. Clune
  Illuminating search spaces by mapping elites.
  arXiv preprint arXiv:1504.04909.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px2.p1.1 "Open World Models and Curriculum Learning ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib29"></a>
- Nathani et al. (2025)
  D. Nathani, L. Madaan, N. Roberts, N. Bashlykov, A. Menon, V. Moens, A. Budhiraja, D. Magka, V. Vorotilov, G. Chaurasia, et al.
  MLGym: a new framework and benchmark for advancing ai research agents.
  arXiv preprint arXiv:2502.14499.
  Cited by: [§23.2.8.1](#Ch23.S2.SS8.SSS1.p3.1 "23.2.8.1 AI Science ‣ 23.2.8 Limitations of Applications ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib30"></a>
- Park et al. (2024)
  J. S. Park, C. Q. Zou, A. Shaw, B. M. Hill, C. Cai, M. R. Morris, R. Willer, P. Liang, and M. S. Bernstein
  Generative agent simulations of 1,000 people.
  arXiv preprint arXiv:2411.10109.
  Cited by: [§23.2.5](#Ch23.S2.SS5.p2.1 "23.2.5 Social Behavior ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib23"></a>
- Raza et al. (2025)
  S. Raza, R. Sapkota, M. Karkee, and C. Emmanouilidis
  Responsible agentic reasoning and ai agents: a critical survey: proposal for safe agentic AI via responsible reasoning ai agents (r2a2).
  SuperIntelligence-Robotics-Safety & Alignment 2 (6).
  Cited by: [§23.2.6](#Ch23.S2.SS6.p4.1 "23.2.6 Legal and Ethical Aspects ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib33"></a>
- Silver et al. (2017)
  D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou, A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai, A. Bolton, et al.
  Mastering the game of go without human knowledge.
  nature 550 (7676), pp. 354–359.
  Cited by: [§23.2.8.1](#Ch23.S2.SS8.SSS1.p2.1 "23.2.8.1 AI Science ‣ 23.2.8 Limitations of Applications ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib14"></a>
- Sprague et al. (2024)
  Z. Sprague, F. Yin, J. D. Rodriguez, D. Jiang, M. Wadhwa, P. Singhal, X. Zhao, X. Ye, K. Mahowald, and G. Durrett
  To cot or not to cot? chain-of-thought helps mainly on math and symbolic reasoning.
  arXiv preprint arXiv:2409.12183.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px1.p1.1 "Overthinking ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib27"></a>
- Sutskever (2024)
  I. Sutskever
  Acceptance speech for test of time award.
  In Advances in Neural Information Processing Systems,
  Vancouver, British Columbia, Canada.
  Cited by: [§23.2.2](#Ch23.S2.SS2.p2.1 "23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib20"></a>
- Trinh et al. (2024)
  T. H. Trinh, Y. Wu, Q. V. Le, H. He, and T. Luong
  Solving olympiad geometry without human demonstrations.
  Nature 625 (7995), pp. 476–482.
  Cited by: [§23.2.8.1](#Ch23.S2.SS8.SSS1.p2.1 "23.2.8.1 AI Science ‣ 23.2.8 Limitations of Applications ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib10"></a>
- Velmans (2009)
  M. Velmans
  Understanding consciousness.
   Routledge.
  Cited by: [§23.2.4](#Ch23.S2.SS4.p3.1 "23.2.4 Emotional Behavior and Consciousness ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib31"></a>
- Vinyals et al. (2019)
  O. Vinyals, I. Babuschkin, W. M. Czarnecki, M. Mathieu, A. Dudzik, J. Chung, D. H. Choi, R. Powell, T. Ewalds, P. Georgiev, et al.
  Grandmaster level in starcraft ii using multi-agent reinforcement learning.
  Nature 575 (7782), pp. 350–354.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px2.p1.1 "Open World Models and Curriculum Learning ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
<a id="bibv.bib13"></a>
- Wu et al. (2025)
  Y. Wu, Y. Wang, Z. Ye, T. Du, S. Jegelka, and Y. Wang
  When more is less: understanding chain-of-thought length in llms.
  arXiv preprint arXiv:2502.07266.
  Cited by: [§23.2.2](#Ch23.S2.SS2.SSS0.Px1.p1.1 "Overthinking ‣ 23.2.2 Scale ‣ 23.2 Limitations and Future Work ‣ Chapter 23 Future Directions for Agentic LLMs ‣ Part VII Conclusion ‣ Agentic Large Language Models").
