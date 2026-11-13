# Chapter 13 From Tools to Assistants: Real-World Applications

[Course index](../../README.md) · [Original source](https://arxiv.org/html/2610.13455v1#Ch13) · [Raw file](../../raw/originals/book.html)

Retrieved: 2026-11-13T16:41:17.579179+00:00

[Contents](../../CONTENTS.md) · [Full book](../book/full-book-html.md) · [Previous chapter](chapter-12-search-and-retrieval-in-agentic-llms.md) · [Next chapter](chapter-14-case-study-3-building-a-multi-agent-diagnosis-framework.md)

<a id="Ch13"></a>


### Chapter 13 From Tools to Assistants: Real-World Applications

**What You Will Learn**

In this chapter you will learn how agentic language models are
deployed as practical assistants across real-world domains.
Specifically, you will be able to:

- Describe how assistants go beyond question answering to plan, retrieve information, invoke tools, and *adapt their behavior* over time.
- Compare assistant architectures across domains including *shopping, medicine, aviation, scientific research and coding*
  .
- Explain why high-risk domains impose stricter requirements around *safety, transparency, and regulatory compliance* and how agentic designs respond to these demands.
- Critically evaluate assistant behavior and reflect on the *ethical* implications of deploying agentic systems in socially consequential settings.

<a id="Ch13.S1"></a>


#### 13.1 Agentic LLMs as Assistants

LLMs have moved from text generators to active assistants.
They combine reasoning, retrieval, and tool use to perform actions in the real world.
Assistants are the practical (software) form of agentic LLMs: systems that interact, plan, and learn from feedback.
Assistants are where reasoning meets reality:
they turn language models into collaborative actors in the world.

An assistant links perception, reasoning, and action.
Through APIs and external tools, it can converse, execute tasks, and adapt to a specific context. These systems not only support users but also create valuable human-AI interaction data that we can then use for further developments and training the next generation of models.

This chapter reviews the main types of assistants.
We start with conversational systems and their evolution toward multi-modal, tool-aware interfaces.
Next, we discuss domain-specific assistants in medicine, finance, and trading.
Finally, we look at scientific assistants for reasoning and discovery.

<a id="Ch13.S2"></a>


#### 13.2 Conversational Assistants

The first application domain is in general conversational situations, such as helping with meetings by taking meeting minutes, acting as meeting chair or general administrative assistant.

<a id="Ch13.S2.p2.1"></a>


In this type of application, the LLM basically serves to make the interaction between human and computer more natural and streamlined [[Neszlényi et al., 2024](#bibl.bib25), [Oluwagbade, 2024](#bibl.bib21)]. For example, the AssistantGPT system [[Neszlényi et al., 2024](#bibl.bib25)] is a general purpose administrative assistant, designed for deployment in an educational or corporate
setting. Furthermore, it supports remote work environments such as Teams and Slack. AssistantGPT supports a diverse range of operations, including web searches, API interactions via OpenAPI, voice conversations, and command execution through the shell. The system consists of an LLM with access to various tools such as a planner, and memory (see Figure [13.1](#Ch13.F1 "Figure 13.1 ‣ 13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")).

<a id="Ch13.F1"></a>
![Refer to caption](../../raw/source/figures/assist.png)


Figure 13.1: <a id="Ch13.F1.4"></a>
AssistGPT system architecture [[Neszlényi et al., 2024](#bibl.bib25)]

<a id="Ch13.S2.p3.1"></a>


These conversation and meeting assistants have been shown to
improve agile software development team meetings [[Cabrero-Daniel et al., 2024](#bibl.bib29)]. They created favorable results for preparation and live assistance during Scrum meetings, although some testers remarked that LLM interventions felt
unnatural and inflexible.

<a id="Ch13.S2.p4.1"></a>


Other examples include LLM agents in a collaborative learning classroom setting where the LLM agents improved overall collaboration between participants [[Wei et al., 2024b](#bibl.bib28)]. Another study [[Bastola et al., 2023](#bibl.bib27)] reports improved work efficiency in a collaborative task scheduling experiment including conversational assistants.

<a id="Ch13.S2.p5.1"></a>


A slightly different type of assistant is the thinking assistant. This assistant tries to improve human reflective thinking for difficult decisions, by asking instead of
answering [[Park and Kulkarni, 2023](#bibl.bib26)]. Similar initiatives have recently appeared from the large LLM vendors, such as *Study mode* in OpenAI’s ChatGPT and Google’s Gemini applications.

Conversational assistants have mostly evolved from regular pretrained LLMs, sometimes finetuned for a particular domain. Some approaches use a specialized multi-LLMs approach,
specializing LLMs for different sub-tasks, or orchestrating a single LLM with different prompt sequences focusing on different sub-tasks.

<a id="Ch13.S3"></a>


#### 13.3 Shopping Assistant

In this section we examine how language-based assistants can be applied in the e-commerce domain. Our goal is to highlight the principal components, architectural choices and domain-specific challenges in this domain.

<a id="Ch13.S3.SS0.SSS0.Px1"></a>


###### What does a shopping assistant do?

A shopping assistant is a conversational system built on an LLM that helps users navigate online shopping tasks. It can help in understanding product needs, comparing alternatives, recommending items and completing purchases. Such a system typically complements the underlying LLM with domain-specific modules, including retrieval of up-to-date product information, API access to product-catalogs, integration with recommender engines and reasoning (e.g., via chain of thought) over user requirements, attributes and constraints.

<a id="Ch13.S3.SS0.SSS0.Px2"></a>


###### Key ingredients

Because general-purpose LLMs lack built-in awareness of e-commerce concepts (brands, categories, product hierarchies, user purchase behavior), building a capable assistant requires several augmentations:

- Retrieval Augmentation: dynamically fetch product metadata, pricing, availability from external sources.
- Tool / API Invocation: the assistant may call search, filter, ranking tools to interact with product databases.
- Domain Finetuning or Instruction Tuning: adapt the LLM to the shopping context (branded language, attribute reasoning, user intents).
- Structured Reasoning: add chain of thought prompting or explicit reasoning steps. This helps the model compare products, evaluate trade-offs (e.g., price vs features) and align with user preferences.

<a id="Ch13.S3.SS0.SSS0.Px3"></a>


###### Benchmarking shopping-assistants

<a id="Ch13.S3.SS0.SSS0.Px3.p1.1"></a>


To study how well models cope with shopping-specific tasks, researchers have developed benchmarks. For example, the *Multi-task Online Shopping Benchmark dataset (ShopMMLU)* [[Jin et al., 2024](#bibl.bib30)] defines 57 tasks grouped into four skills: concept understanding, knowledge reasoning, user-behavior alignment and multi-linguality. It draws on real-world e-commerce data (Amazon product catalogs, sessions and reviews) and evaluates how well an LLM can handle aspects like brand-model recognition, reasoning about product compatibility, session-based recommendation tasks, and multilingual queries.
Another example is the LLaSA system (large language and E-commerce shopping assistant) [[Zhang et al., 2024a](#bibl.bib31)] which is trained via an instruction dataset (65,000 samples) dubbed *EshopInstruct*. After instruction-tuning on shopping tasks, LLaSA competes on the ShopBench benchmark and achieves strong results, showing that adaptation significantly improves performance in this domain.

<a id="Ch13.S3.SS0.SSS0.Px4"></a>


###### Practical Recommendations

The following principles are important for building shopping assistants:

- A capable assistant merges natural-language understanding and domain reasoning. It should know what *noise-canceling headphones under 200 euro with ¿ 20 h battery* means, and be able to translate this into product attributes and user constraints.
- <a id="Ch13.S3.I2.i2.p1.1"></a>


  Domain-specific data matters: off-the-shelf LLMs work to some degree, but fine-tuning or instruction-tuning on shopping tasks significantly lifts performance. LLaSA [[Zhang et al., 2024a](#bibl.bib31)] shows this in practice.
- Evaluation must reflect the domain. Accuracy in understanding product attributes or generating queries is less relevant than whether the assistant can align with user behavior, handle multi-step sessions and support multilingual users.
- Tool and retrieval integration is important. The assistant must act as an interface to product systems, not just as a pure language model. This introduces additional complexity (API design, latency, freshness of data and handling integration errors).
- Consider ethics and trust. In shopping, recommendations carry commercial, privacy and bias implications. These issues should be assessed before deploying such a system in production, through questions such as: *which brands are shown*, *is user history handled correctly*, and *how transparent is the reasoning*.

<a id="Ch13.S3.SS0.SSS0.Px5"></a>


###### Challenges and open questions

Even with recent progress, shopping assistants face several non-trivial challenges. First, handling long interaction trajectories (browsing, refining queries, switching intents) is still difficult for LLM agents. Second, updating product knowledge in real-time (new models, price changes, availability) remains a major engineering pain-point. Third, explaining and justifying recommendations to users (why this product vs another) is under-explored in LLM-based assistants. Finally, cross-lingual behavior and multilingual product queries increase complexity (shopping contexts span languages and regions).

<a id="Ch13.S4"></a>


#### 13.4 Flight Operations Assistant

Language-based assistants are also applied in aviation operations, a domain that extends beyond consumer booking and moves into planning and decision support.

<a id="Ch13.S4.SS0.SSS0.Px1"></a>


###### Booking and travel-planning

<a id="Ch13.S4.SS0.SSS0.Px1.p1.1"></a>


One of the simpler applications is a conversational booking assistant, similar to the shopping assistants in the previous section. For example, [Manasa et al. [2024]](#bibl.bib24) present a system built on LLaMa 2 with RAG to interactively help users book flights. The assistant is fine-tuned on flight-booking data, and connects to current flight information via retrieval. User testing achieved strong marks for capturing user preferences and guiding the booking process efficiently.

Notice how this use-case remains relatively shallow in operational complexity. The assistant deals with structured user intents (*I want to fly from A to B on date D*), retrieval of up-to-date product data, preference elicitation and generation of responses. It does not (yet) deeply engage with, say, dynamic air-traffic constraints or safety margins.

<a id="Ch13.S4.SS0.SSS0.Px2"></a>


###### Operational decision support

Moving to more demanding settings, LLM-based assistants are being proposed for actual flight operations. We discuss two examples.

<a id="Ch13.S4.SS0.SSS0.Px2.p2.1"></a>


In a study by [Zhou et al. [2024]](#bibl.bib22), the arrival-slot-allocation problem (i.e., determining in which sequence arriving aircraft should land) is formulated as a language modeling task. The authors encode the scheduling inputs and outputs as tokens and fine-tune an LLM to generate conflict-free landing sequences. Their experiments show that the model can reduce conflict rate and total delay time even for airports where traditional methods struggle.

<a id="Ch13.S4.SS0.SSS0.Px2.p3.1"></a>


Another operational problem is planning under environmental hazards. [Tabrizian et al. [2024]](#bibl.bib23) use chain of thought to support routing or flight plan generation under wind-hazard constraints. Here, the assistant’s task is no longer simply *book a flight* but it has to reason about constraints (wind, routing, aircraft performance) and propose operationally feasible plans.

<a id="Ch13.S4.SS0.SSS0.Px3"></a>


###### Key recommendations

These studies illustrate several important aspects of agentic systems with LLMs:

- Tool/Backend Integration: in operational assistants, the LLM must not only converse but also interface with flight-databases, weather feeds, routing engines and slot‐allocation systems. This means implementing tool invocation, retrieval pipelines and decision logic.
- Reasoning under Constraints: these assistants must handle combinatorial or scheduling constraints, generate plans, and deal with real‐time uncertainties (such as weather, runway availability). The arrival-slot example is a good example, where the LLM must reason about dynamic sequencing.
- Domain-specific Data and Finetuning: the standard pretrained LLM lacks priors about aviation operations. The systems above are finetuned or prompted specifically for the domain. A dataset of domain-tasks, prompts, expected outputs are evaluation metrics tailored to the domain are necessary.
- From Conversational Agent to Autonomous Planner: while booking assistants remain user-driven (the user asks, the assistant helps), operational assistants increasingly take on planning roles. The assistant should handle requests such as *here are constraints, propose a schedule or route*. This change raises issues of trust, verification and explainability.
- Evaluation in Real Contexts: the evaluation of operational systems often involves more than *does the assistant answer the user?*, but also measure aspects such as conflict rate, delay time, and sequence efficiency. For example, the arrival-slot LLM study measured total delay and conflict rate.

<a id="Ch13.S5"></a>


#### 13.5 Medical Assistant

<a id="Ch13.S5.p1.1"></a>


Medicine is one of the most active application domains for LLM-based assistants [[Thirunavukarasu et al., 2023](#bibl.bib11), [Clusmann et al., 2023](#bibl.bib6), [Mehandru et al., 2024](#bibl.bib5)].
Recent studies report that LLMs can outperform trained physicians on diagnostic tasks
[[Goh et al., 2024](#bibl.bib7)] and exceed human medical scribes in clinical note generation
[[Yuan et al., 2024](#bibl.bib10)]. Other evaluations confirm these strengths, while also identifying
systematic weaknesses in specific clinical scenarios [[Panagoulias et al., 2024](#bibl.bib8)].

<a id="Ch13.S5.p2.1"></a>


Agentic architectures are increasingly used to address regulatory, ethical, and usability
requirements. [Sudarshan et al. [2024]](#bibl.bib14) present an agentic workflow for generating
patient-friendly medical reports that comply with the 21st Century Cures Act. Their system
uses reflexion (Section [6.2.4](chapter-06-multi-step-reasoning-in-llms.md#Ch6.S2.SS4 "6.2.4 Agentic Harness for Prompt Improvement ‣ 6.2 Self-Reflection and State ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models"), [[Shinn et al., 2024](#bibl.bib38)]) to iteratively improve clarity and correctness before information is released to patients.

<a id="Ch13.S5.p3.1"></a>


Other studies explore the use of LLM agents for broader clinical support. [Qiu et al. [2024]](#bibl.bib15) identify
applications ranging from clinical workflow automation to multi-agent diagnostic support, although concerns remain regarding accuracy, completeness, and hallucinations.
A scoping review by [Ullah et al. [2024]](#bibl.bib9) emphasizes that medical domain knowledge and ethical constraints are essential when training and fine-tuning such systems.

<a id="Ch13.S5.p4.1"></a>


To mitigate common failure modes, [Das et al. [2024]](#bibl.bib13) propose an agentic retrieval-based architecture in which the LLM acts as a planner rather than a direct answer generator. The agent coordinates specialized tools to retrieve and synthesize evidence from trusted medical
sources, reducing hallucinations and *lost-in-the-middle* errors.

<a id="Ch13.S5.SS0.SSS0.Px1"></a>


###### High-risk application domain

Medicine is a high-risk application domain, where incorrect or biased outputs can have direct consequences for patient safety. As a result, medical AI systems are subject to strict regulatory frameworks, including the EU AI Act, which classifies many medical uses of AI as high-risk. Transparency, fairness, and accountability therefore play a central role, both in clinical practice and in academic research on medical LLMs.
These concerns motivate increased interest in methods that go beyond post-hoc explanations and aim to understand model behavior at a deeper level. We return to this topic in the chapter on *mechanistic interpretability* (Chapter [21](chapter-21-mechanistic-interpretability-for-llm-agents.md#Ch21 "Chapter 21 *Mechanistic Interpretability for LLM Agents ‣ Part VI Advanced Topics ‣ Agentic Large Language Models")), where techniques for analyzing and controlling internal model representations are discussed.

<a id="Ch13.S5.SS0.SSS0.Px2"></a>


###### Medical education

<a id="Ch13.S5.SS0.SSS0.Px2.p1.1"></a>


In medical education, agentic systems are used to simulate realistic training environments.
[Wei et al. [2024a]](#bibl.bib12) introduce a multi-agent copilot that supports case-based learning and clinical reasoning practice (Figure [13.2](#Ch13.F2 "Figure 13.2 ‣ Medical education ‣ 13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")). For systematic evaluation of medical retrieval-augmented generation, a dedicated benchmark is provided by
[Qiao et al. [2024]](#bibl.bib20).

<a id="Ch13.F2"></a>
![Refer to caption](../../raw/source/figures/medco.png)


Figure 13.2: <a id="Ch13.F2.4"></a>
Medical Education Copilot [[Wei et al., 2024a](#bibl.bib12)]

<a id="Ch13.S6"></a>


#### 13.6 Trading Assistant

<a id="Ch13.S6.p1.1"></a>


A further specialized domain is financial trading.
Already many (non-LLM) algorithms are used
in financial organizations for trading decisions. The interest in
agentic LLMs in the financial world is large [[Ding et al., 2024](#bibl.bib2)].

<a id="Ch13.S6.p2.1"></a>


InvestorBench is a benchmark for financial trading systems [[Li et al., 2024](#bibl.bib16)].
FinAgent is a tool-augmented multimodal agent for financial trading
[[Zhang et al., 2024b](#bibl.bib19)].
It contains a market intelligence module, which is able to
extract insights from multi-modal datasets of
asset prices, visual representations, news and expert
analyses. The system can also perform query retrieval and performs
reflection in a low-level module for technical analysis
and in a high-level module to analyze past trading decisions.

<a id="Ch13.S6.p3.1"></a>


FinRobot is an agentic LLM for financial analysis, to assist human traders.
[[Yang et al., 2024a](#bibl.bib18)]. FinRobot can provide document analysis and
generation and market forecasts for
individual stocks.
FinMem is an agentic LLM framework devised for financial decision-making
[[Yu et al., 2024](#bibl.bib4)]. It features a layered memory system and
adjustable character design for the trading agent. FinMem is inspired
by the generative agents framework by [Park et al. [2023]](#bibl.bib3) (see Section [17.2.1](chapter-17-emergent-behavior-in-multi-llm-systems.md#Ch17.S2.SS1 "17.2.1 Small Worlds ‣ 17.2 Simulation Infrastructure ‣ Chapter 17 Emergent Behavior in Multi-LLM Systems ‣ Part V Behavior and Cognition ‣ Agentic Large Language Models") and Case Study 4).

<a id="Ch13.S6.p4.1"></a>


So far, most financial market machine learning has focused on single agent
systems. An approach called *TradingAgents* uses a multi agent
system to replicate real-world trading firms’ collaborative dynamics
[[Xiao et al., 2024](#bibl.bib17)]. TradingAgents simulates LLM-powered
agents in specialized roles such as fundamental analysts,
sentiment analysts, technical analysts and traders with varied risk
profiles. The outcome of the system is a buy or sell
advice to a human manager. A simulation showed that it outperformed baseline models.

<a id="Ch13.S6.SS0.SSS0.Px1"></a>


###### Evaluation

Financial trading is a challenging field of research. The competitive interests in financial trading are high, and there is a natural tendency to keep strong research findings private, which creates a tension with the principles of openness and transparency of scientific research.

<a id="Ch13.S6.SS0.SSS0.Px1.p2.1"></a>


Furthermore, despite the abundance of available numerical data in the field, there are relatively few benchmarking studies that compare different agentic LLM approaches on the same data. A recent benchmarking study found methodological flaws in some financial LLM studies, such as selecting short evaluation periods with positive market trends or leakage of test in training data [[Li et al., 2026](#bibl.bib1)].

<a id="Ch13.S7"></a>


#### 13.7 Automated Scientific Discovery

<a id="Ch13.S7.p1.1"></a>


The workflow of scientific experimentation is relatively standardized in certain fields of science. For example, in machine learning, (1) ideas are generated, (2) a hypothesis is formulated, (3) an experiment is designed, (4) datasets are acquired, (5) experiments are performed, (6) results are interpreted and (7) a report is produced. This standard workflow has attracted researchers to experiment with agentic LLMs for performing scientific research, see [Eger et al. [2025]](#bibl.bib37) for a survey.

Google and OpenAI have both released Deep Research agents. These agents can perform multi-step research tasks, such as synthesizing online information. They are built with a reasoning LLM and use retrieval augmentation for finding information sources. The systems are able to create scientific research papers that look impressive, but are often not error-free.

<a id="Ch13.S7.p3.1"></a>


AI Scientist [[Lu et al., 2024](#bibl.bib35)] is a framework to automate the process of scientific discovery, from idea generation to paper writing, including a review process. Users must specify a topic and provide an experimentation template and indicate datasets. The authors report experiments in three areas of machine learning: diffusion
modeling, transformer-based language modeling, and learning dynamics, with promising results. To improve idea generation and reviewing, the agent accesses open sources. Current limitations include limited experiments, incorrect implementation if ideas, and visual errors when the paper is produced. On the other hand, rarely are entire results hallucinated. Nevertheless, results of the AI scientist are recommended to be taken as hints of promising ideas, worthy of a follow up study [[Lu et al., 2024](#bibl.bib35)].

<a id="Ch13.S7.p4.1"></a>


Building on top of the AI scientist idea, the Agent Laboratory was proposed [[Schmidgall et al., 2025](#bibl.bib39)], an open-source framework that employs specialized LLM-based agents to accelerate the full research cycle. Unlike the AI Scientist, Agent Laboratory is explicitly designed as a co-pilot for human researchers, complementing rather than replacing human ideation.
The framework consists of three main phases: *literature review*, *experimentation*, and *report writing*. Each phase is executed by dedicated agents, such as the PhD, Postdoc, and Professor agents, coordinated through a structured pipeline. The system integrates two specialized components: *mle-solver*, responsible for autonomously generating, testing, and refining machine learning code, and *paper-solver*, which produces a complete research report in LaTeX format based on the experimental results. Both solvers employ iterative refinement, self-evaluation, and reward-based scoring to improve code and report quality across cycles.

Evaluation results demonstrate that Agent Laboratory can autonomously generate complete research projects, including executable code and publication-ready reports, at a fraction of the computational cost of comparable systems (approximately $2.33 per paper using the gpt-4o backend). Human-in-the-loop or co-pilot mode further improves research quality and usability, with participants reporting high satisfaction and continued use intentions. Nonetheless, human oversight remains essential, as automated self-evaluations tend to overestimate research quality compared to human reviewers.

<a id="Ch13.S8"></a>


#### 13.8 Coding Assistants and General Advances

<a id="Ch13.S8.p1.1"></a>


SWE-Agent (short for *software engineering agent*) [[Yang et al., 2024b](#bibl.bib33)] aims to automate the process of software discovery, to help agents to autonomously use computers to solve software engineering tasks. SWE-agent introduces tools to create and edit code files, navigate through software repositories, and execute computer programs. Experiments on coding benchmarks such as HumanEvalFix achieve high success rates of over 80%. This success is attributed to the interactive design of the agent (see Figure [13.3](#Ch13.F3 "Figure 13.3 ‣ 13.8 Coding Assistants and General Advances ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")).

<a id="Ch13.F3"></a>
![Refer to caption](../../raw/source/figures/swe.png)


Figure 13.3: <a id="Ch13.F3.4"></a>
SWE-Agent for Software Engineering [[Yang et al., 2024b](#bibl.bib33)]

<a id="Ch13.S8.p2.1"></a>


MLGym [[Nathani et al., 2025](#bibl.bib34)] follows the popular Gym reinforcement learning framework [[Brockman et al., 2016](#bibl.bib32)]. Gym provides a standardized interface between environment and agent. Introduced in 2016, it accelerated the development of reinforcement learning algorithms, facilitating progress in the field. Taking further inspiration from SWE-agent (such as file editing capabilities) the MLGym work shows how the process of scientific discovery can be modeled as an interactive process. Applications are discussed in fields ranging from data science, game theory, computer vision, reinforcement learning, to natural language processing. Experiments are reported with commercial LLMs
(OpenAI, Meta, Google, and Anthropic).

<a id="Ch13.S8.p3.1"></a>


Most LLM-based assistants, including research and coding assistants, depend on pre-defined tools, limiting their autonomy and scalability.
Toolmaker [[Wölflein et al., 2025](#bibl.bib40)] addresses this limitation by enabling agents to create new tools directly from scientific papers and their code repositories. Given a task description and GitHub URL, it installs dependencies, configures a reproducible Docker environment, and implements a working Python tool through iterative self-correction and error diagnosis.
The system was evaluated on TM-Bench (also introduced in [Wölflein et al. [2025]](#bibl.bib40)), a benchmark of 15 real-world scientific tasks across medicine, biology, and AI. Toolmaker achieved 80% task success. Its closed-loop design allows agents not only to use but also to autonomously build new tools, marking a step toward self-extending research assistants and adaptive scientific workflows.

<a id="Ch13.S8.p4.1"></a>


While systems such as Agent Laboratory and Toolmaker focus on the capabilities of individual agents, The Agent Company [[Xu et al., 2024](#bibl.bib36)] provides a comprehensive benchmark to evaluate how LLM agents perform in realistic, work-like environments. It simulates a small software company where agents must complete professional tasks, ranging from software development and project management to finance and human resources, using standard digital tools like browsers, terminals, and communication platforms.

The benchmark includes 175 tasks designed to test multi-step reasoning, tool use, and collaboration with simulated colleagues powered by LLMs. Each task is divided into checkpoints that measure both full and partial completion. Experiments with twelve foundation models, including GPT-4o, Claude, Gemini, and Llama, reveal that even the strongest current systems can autonomously complete only about 30% of tasks. Failures often come from weaknesses in communication, long-horizon planning, and navigation of complex user interfaces.

By introducing a reproducible, self-hosted environment that mirrors a modern workplace, The Agent Company offers a critical stress test for evaluating the maturity of agentic LLMs. It highlights both the rapid progress and the persistent limitations of current systems, underscoring that while digital work automation is within reach, truly autonomous collaboration remains a major research frontier.

<a id="Ch13.S9"></a>


#### 13.9 Concluding Remarks

This chapter has shown how agentic LLMs have been used as assistants, interacting with the real world. Assistants move beyond passive question answering toward active collaboration in domains such as dialogue, flight operations, medicine, education and scientific research. They plan, retrieve information, invoke tools, reflect on outcomes and adapt their behavior over time. Agentic LLMs therefore shift the role of language models from isolated reasoning engines to participants in broader socio-technical systems.

<a id="Ch13.S9.SS0.SSS0.Px1"></a>


###### Domain sensitivity and risk

Not all assistants operate under the same constraints. High-risk domains such as medicine and aviation demand strong guarantees on safety, robustness, transparency and fairness, and are shaped by regulatory frameworks such as the EU AI Act. In these settings, agentic designs increasingly rely on retrieval, planning, verification and human oversight rather than on end-to-end generation. Academic research mirrors these concerns, with growing emphasis on evaluation, bias analysis and interpretability as first-class design objectives rather than afterthoughts.

<a id="Ch13.S9.SS0.SSS0.Px2"></a>


###### Practical advice

When building assistants, grounding (real-world evaluation) is important. Use architectures where agents retrieve evidence, justify actions and defer to humans under uncertainty (human in the loop). Treat tools as modular components with explicit contracts and failure modes. Log decisions, plans and intermediate states to enable debugging and auditing. In high-stakes domains, we suggest to design for graceful degradation; an agent asking for clarification or abstaining is preferable to confident error.

<a id="Ch13.S9.SS0.SSS0.Px3"></a>


###### Outlook

The future of agentic assistants lies in tighter integration between reasoning, learning and control. Progress will require richer cognitive structure, continual adaptation from interaction and stronger guarantees around safety and ethics. These goals connect directly to advances in interpretability and transparency. In later chapters, particularly in mechanistic interpretability (Chapter [21](chapter-21-mechanistic-interpretability-for-llm-agents.md#Ch21 "Chapter 21 *Mechanistic Interpretability for LLM Agents ‣ Part VI Advanced Topics ‣ Agentic Large Language Models")), we return to techniques that aim to open the black box and better understand how agentic LLMs represent goals, plans and decisions internally.

<a id="bibl"></a>


### References

<a id="bibl.bib27"></a>
- Bastola et al. (2023)
  A. Bastola, H. Wang, J. Hembree, P. Yadav, N. McNeese, and A. Razi
  Llm-based smart reply (lsr): enhancing collaborative performance with chatgpt-mediated smart reply system (acm)(draft) llm-based smart reply (lsr): enhancing collaborative performance with chatgpt-mediated smart reply system.
  arXiv preprint arXiv:2306.11980.
  Cited by: [§13.2](#Ch13.S2.p4.1 "13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib32"></a>
- Brockman et al. (2016)
  G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman, J. Tang, and W. Zaremba
  Openai gym.
  arXiv preprint arXiv:1606.01540.
  Cited by: [§13.8](#Ch13.S8.p2.1 "13.8 Coding Assistants and General Advances ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib29"></a>
- Cabrero-Daniel et al. (2024)
  B. Cabrero-Daniel, T. Herda, V. Pichler, and M. Eder
  Exploring human-ai collaboration in agile: customised llm meeting assistants.
  In International Conference on Agile Software Development,
  pp. 163–178.
  Cited by: [§13.2](#Ch13.S2.p3.1 "13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib6"></a>
- Clusmann et al. (2023)
  J. Clusmann, F. R. Kolbinger, H. S. Muti, Z. I. Carrero, J. Eckardt, N. G. Laleh, C. M. L. Löffler, S. Schwarzkopf, M. Unger, G. P. Veldhuizen, et al.
  The future landscape of large language models in medicine.
  Communications medicine 3 (1), pp. 141.
  Cited by: [§13.5](#Ch13.S5.p1.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib13"></a>
- Das et al. (2024)
  R. Das, K. Maheswari, S. Siddiqui, N. Arora, A. Paul, J. Nanshi, V. Udbalkar, A. Sarvade, H. Chaturvedi, T. Shvartsman, et al.
  Improved precision oncology question-answering using agentic llm.
  medRxiv, pp. 2024–09.
  Cited by: [§13.5](#Ch13.S5.p4.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib2"></a>
- Ding et al. (2024)
  H. Ding, Y. Li, J. Wang, and H. Chen
  Large language model agent in financial trading: a survey.
  arXiv preprint arXiv:2408.06361.
  Cited by: [§13.6](#Ch13.S6.p1.1 "13.6 Trading Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib37"></a>
- Eger et al. (2025)
  S. Eger, Y. Cao, J. D’Souza, A. Geiger, C. Greisinger, S. Gross, Y. Hou, B. Krenn, A. Lauscher, Y. Li, et al.
  Transforming science with large language models: a survey on ai-assisted scientific discovery, experimentation, content generation, and evaluation.
  arXiv preprint arXiv:2502.05151.
  Cited by: [§13.7](#Ch13.S7.p1.1 "13.7 Automated Scientific Discovery ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib7"></a>
- Goh et al. (2024)
  E. Goh, R. Gallo, J. Hom, E. Strong, Y. Weng, H. Kerman, J. A. Cool, Z. Kanjee, A. S. Parsons, N. Ahuja, et al.
  Large language model influence on diagnostic reasoning: a randomized clinical trial.
  JAMA Network Open 7 (10), pp. e2440969–e2440969.
  Cited by: [§13.5](#Ch13.S5.p1.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib30"></a>
- Jin et al. (2024)
  Y. Jin, Z. Li, C. Zhang, T. Cao, Y. Gao, P. Jayarao, M. Li, X. Liu, R. Sarkhel, X. Tang, et al.
  Shopping mmlu: a massive multi-task online shopping benchmark for large language models.
  arXiv preprint arXiv:2410.20745.
  Cited by: [§13.3](#Ch13.S3.SS0.SSS0.Px3.p1.1 "Benchmarking shopping-assistants ‣ 13.3 Shopping Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib16"></a>
- Li et al. (2024)
  H. Li, Y. Cao, Y. Yu, S. R. Javaji, Z. Deng, Y. He, Y. Jiang, Z. Zhu, K. Subbalakshmi, G. Xiong, et al.
  INVESTORBENCH: a benchmark for financial decision-making tasks with llm-based agent.
  arXiv preprint arXiv:2412.18174.
  Cited by: [§13.6](#Ch13.S6.p2.1 "13.6 Trading Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib1"></a>
- Li et al. (2026)
  W. W. Li, H. Kim, M. Cucuringu, and T. Ma
  Can llm-based financial investing strategies outperform the market in long run?.
  In Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 1,
  pp. 2711–2722.
  Cited by: [§13.6](#Ch13.S6.SS0.SSS0.Px1.p2.1 "Evaluation ‣ 13.6 Trading Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib35"></a>
- Lu et al. (2024)
  C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha
  The ai scientist: towards fully automated open-ended scientific discovery.
  arXiv preprint arXiv:2408.06292.
  Cited by: [§13.7](#Ch13.S7.p3.1 "13.7 Automated Scientific Discovery ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib24"></a>
- Manasa et al. (2024)
  S. Manasa, P. Agarwal, G. Pal, P. Mahendra, S. R. Pendyala, and S. Marge
  Towards seamless air travel: developing a next-generation flight booking assistant.
  Journal of Electrical Systems 20 (2), pp. 2558–2567.
  Cited by: [§13.4](#Ch13.S4.SS0.SSS0.Px1.p1.1 "Booking and travel-planning ‣ 13.4 Flight Operations Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib5"></a>
- Mehandru et al. (2024)
  N. Mehandru, B. Y. Miao, E. R. Almaraz, M. Sushil, A. J. Butte, and A. Alaa
  Evaluating large language models as agents in the clinic.
  NPJ digital medicine 7 (1), pp. 84.
  Cited by: [§13.5](#Ch13.S5.p1.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib34"></a>
- Nathani et al. (2025)
  D. Nathani, L. Madaan, N. Roberts, N. Bashlykov, A. Menon, V. Moens, A. Budhiraja, D. Magka, V. Vorotilov, G. Chaurasia, et al.
  MLGym: a new framework and benchmark for advancing ai research agents.
  arXiv preprint arXiv:2502.14499.
  Cited by: [§13.8](#Ch13.S8.p2.1 "13.8 Coding Assistants and General Advances ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib25"></a>
- Neszlényi et al. (2024)
  K. B. Neszlényi, A. Milos, and A. Kiss
  AssistantGPT: enhancing user interaction with llm integration.
  In 2024 IEEE 22nd Jubilee International Symposium on Intelligent Systems and Informatics (SISY),
  pp. 000619–000624.
  Cited by: [Figure 13.1](#Ch13.F1 "In 13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [Figure 13.1](#Ch13.F1.4 "In 13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§13.2](#Ch13.S2.p2.1 "13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib21"></a>
- Oluwagbade (2024)
  E. Oluwagbade
  Conversational ai as the new employee liaison: llm-powered chatbots in enhancing workplace collaboration and inclusion.
  Cited by: [§13.2](#Ch13.S2.p2.1 "13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib8"></a>
- Panagoulias et al. (2024)
  D. P. Panagoulias, M. Virvou, and G. A. Tsihrintzis
  Evaluating llm–generated multimodal diagnosis from medical images and symptom analysis.
  arXiv preprint arXiv:2402.01730.
  Cited by: [§13.5](#Ch13.S5.p1.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib3"></a>
- Park et al. (2023)
  J. S. Park, J. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein
  Generative agents: interactive simulacra of human behavior.
  In Proceedings of the 36th annual acm symposium on user interface software and technology,
  pp. 1–22.
  Cited by: [§13.6](#Ch13.S6.p3.1 "13.6 Trading Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib26"></a>
- Park and Kulkarni (2023)
  S. Park and C. Kulkarni
  Thinking assistants: llm-based conversational assistants that help users think by asking rather than answering.
  arXiv preprint arXiv:2312.06024.
  Cited by: [§13.2](#Ch13.S2.p5.1 "13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib20"></a>
- Qiao et al. (2024)
  S. Qiao, R. Fang, Z. Qiu, X. Wang, N. Zhang, Y. Jiang, P. Xie, F. Huang, and H. Chen
  Benchmarking agentic workflow generation.
  arXiv preprint arXiv:2410.07869.
  Cited by: [§13.5](#Ch13.S5.SS0.SSS0.Px2.p1.1 "Medical education ‣ 13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib15"></a>
- Qiu et al. (2024)
  J. Qiu, K. Lam, G. Li, A. Acharya, T. Y. Wong, A. Darzi, W. Yuan, and E. J. Topol
  LLM-based agentic systems in medicine and healthcare.
  Nature Machine Intelligence, pp. 1–3.
  Cited by: [§13.5](#Ch13.S5.p3.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib39"></a>
- Schmidgall et al. (2025)
  S. Schmidgall, Y. Su, Z. Wang, X. Sun, J. Wu, X. Yu, J. Liu, M. Moor, Z. Liu, and E. Barsoum
  Agent laboratory: using llm agents as research assistants.
  arXiv preprint arXiv:2501.04227.
  Cited by: [§13.7](#Ch13.S7.p4.1 "13.7 Automated Scientific Discovery ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib38"></a>
- Shinn et al. (2024)
  N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao
  Reflexion: language agents with verbal reinforcement learning.
  Advances in Neural Information Processing Systems 36.
  Cited by: [§13.5](#Ch13.S5.p2.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib14"></a>
- Sudarshan et al. (2024)
  M. Sudarshan, S. Shih, E. Yee, A. Yang, J. Zou, C. Chen, Q. Zhou, L. Chen, C. Singhal, and G. Shih
  Agentic llm workflows for generating patient-friendly medical reports.
  arXiv preprint arXiv:2408.01112.
  Cited by: [§13.5](#Ch13.S5.p2.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib23"></a>
- Tabrizian et al. (2024)
  A. Tabrizian, P. Gupta, A. Taye, J. Jones, E. Thompson, S. Chen, T. Bonin, D. Eberle, and P. Wei
  Using large language models to automate flight planning under wind hazards.
  In 2024 AIAA DATC/IEEE 43rd Digital Avionics Systems Conference (DASC),
  pp. 1–8.
  Cited by: [§13.4](#Ch13.S4.SS0.SSS0.Px2.p3.1 "Operational decision support ‣ 13.4 Flight Operations Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib11"></a>
- Thirunavukarasu et al. (2023)
  A. J. Thirunavukarasu, D. S. J. Ting, K. Elangovan, L. Gutierrez, T. F. Tan, and D. S. W. Ting
  Large language models in medicine.
  Nature medicine 29 (8), pp. 1930–1940.
  Cited by: [§13.5](#Ch13.S5.p1.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib9"></a>
- Ullah et al. (2024)
  E. Ullah, A. Parwani, M. M. Baig, and R. Singh
  Challenges and barriers of using large language models (llm) such as chatgpt for diagnostic medicine with a focus on digital pathology–a recent scoping review.
  Diagnostic pathology 19 (1), pp. 43.
  Cited by: [§13.5](#Ch13.S5.p3.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib12"></a>
- Wei et al. (2024a)
  H. Wei, J. Qiu, H. Yu, and W. Yuan
  Medco: medical education copilots based on a multi-agent framework.
  arXiv preprint arXiv:2408.12496.
  Cited by: [Figure 13.2](#Ch13.F2 "In Medical education ‣ 13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [Figure 13.2](#Ch13.F2.4 "In Medical education ‣ 13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§13.5](#Ch13.S5.SS0.SSS0.Px2.p1.1 "Medical education ‣ 13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib28"></a>
- Wei et al. (2024b)
  R. Wei, K. Li, and J. Lan
  Improving collaborative learning performance based on llm virtual assistant.
  In 2024 13th International Conference on Educational and Information Technology (ICEIT),
  pp. 1–6.
  Cited by: [§13.2](#Ch13.S2.p4.1 "13.2 Conversational Assistants ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib40"></a>
- Wölflein et al. (2025)
  G. Wölflein, D. Ferber, D. Truhn, O. Arandjelović, and J. N. Kather
  Llm agents making agent tools.
  arXiv preprint arXiv:2502.11705.
  Cited by: [§13.8](#Ch13.S8.p3.1 "13.8 Coding Assistants and General Advances ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib17"></a>
- Xiao et al. (2024)
  Y. Xiao, E. Sun, D. Luo, and W. Wang
  TradingAgents: multi-agents llm financial trading framework.
  arXiv preprint arXiv:2412.20138.
  Cited by: [§13.6](#Ch13.S6.p4.1 "13.6 Trading Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib36"></a>
- Xu et al. (2024)
  F. F. Xu, Y. Song, B. Li, Y. Tang, K. Jain, M. Bao, Z. Z. Wang, X. Zhou, Z. Guo, M. Cao, et al.
  Theagentcompany: benchmarking llm agents on consequential real world tasks.
  arXiv preprint arXiv:2412.14161.
  Cited by: [§13.8](#Ch13.S8.p4.1 "13.8 Coding Assistants and General Advances ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib18"></a>
- Yang et al. (2024a)
  H. Yang, B. Zhang, N. Wang, C. Guo, X. Zhang, L. Lin, J. Wang, T. Zhou, M. Guan, R. Zhang, et al.
  FinRobot: an open-source ai agent platform for financial applications using large language models.
  arXiv preprint arXiv:2405.14767.
  Cited by: [§13.6](#Ch13.S6.p3.1 "13.6 Trading Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib33"></a>
- Yang et al. (2024b)
  J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. R. Narasimhan, and O. Press
  Swe-agent: agent-computer interfaces enable automated software engineering.
  In The Thirty-eighth Annual Conference on Neural Information Processing Systems,
  Cited by: [Figure 13.3](#Ch13.F3 "In 13.8 Coding Assistants and General Advances ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [Figure 13.3](#Ch13.F3.4 "In 13.8 Coding Assistants and General Advances ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§13.8](#Ch13.S8.p1.1 "13.8 Coding Assistants and General Advances ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib4"></a>
- Yu et al. (2024)
  Y. Yu, H. Li, Z. Chen, Y. Jiang, Y. Li, D. Zhang, R. Liu, J. W. Suchow, and K. Khashanah
  FinMem: a performance-enhanced llm trading agent with layered memory and character design.
  In Proceedings of the AAAI Symposium Series,
  Vol. 3, pp. 595–597.
  Cited by: [§13.6](#Ch13.S6.p3.1 "13.6 Trading Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib10"></a>
- Yuan et al. (2024)
  D. Yuan, E. Rastogi, G. Naik, S. P. Rajagopal, S. Goyal, F. Zhao, B. Chintagunta, and J. Ward
  A continued pretrained llm approach for automatic medical note generation.
  arXiv preprint arXiv:2403.09057.
  Cited by: [§13.5](#Ch13.S5.p1.1 "13.5 Medical Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib31"></a>
- Zhang et al. (2024a)
  S. Zhang, B. Peng, X. Zhao, B. Hu, Y. Zhu, Y. Zeng, and X. Hu
  Llasa: large language and e-commerce shopping assistant.
  arXiv preprint arXiv:2408.02006.
  Cited by: [2nd item](#Ch13.S3.I2.i2.p1.1 "In Practical Recommendations ‣ 13.3 Shopping Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§13.3](#Ch13.S3.SS0.SSS0.Px3.p1.1 "Benchmarking shopping-assistants ‣ 13.3 Shopping Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib19"></a>
- Zhang et al. (2024b)
  W. Zhang, L. Zhao, H. Xia, S. Sun, J. Sun, M. Qin, X. Li, Y. Zhao, Y. Zhao, X. Cai, et al.
  FinAgent: a multimodal foundation agent for financial trading: tool-augmented, diversified, and generalist.
  arXiv preprint arXiv:2402.18485.
  Cited by: [§13.6](#Ch13.S6.p2.1 "13.6 Trading Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibl.bib22"></a>
- Zhou et al. (2024)
  W. Zhou, J. Wang, L. Zhu, Y. Wang, and Y. Ji
  Flight arrival scheduling via large language model.
  Aerospace 11 (10), pp. 813.
  Cited by: [§13.4](#Ch13.S4.SS0.SSS0.Px2.p2.1 "Operational decision support ‣ 13.4 Flight Operations Assistant ‣ Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
