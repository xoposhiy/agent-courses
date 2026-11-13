# Shared Concept Dictionary

Canonical names, scope, aliases, and parent concepts. Parent and child concepts remain separate. A child does not automatically add coverage to its parent.

Aliases name the same concept. Related terms are examples or associated systems, not synonyms.

| ID | Canonical name | Type | Definition | Aliases | Related terms | Parent |
| --- | --- | --- | --- | --- | --- | --- |
| abstention | Abstention and uncertainty handling | pattern | Decline to answer or ask for help when evidence or confidence is insufficient. | I don't know; selective answering |  | grounding |
| activation-patching | Activation patching and causal intervention | method | Change internal activations to test their causal effect on model output. | activation patching; causal tracing |  | interpretability |
| agent-architecture | Agent architecture | topic | Combine a model, tools, memory, control flow, and an environment into an agent. | agent anatomy; agent components |  |  |
| agent-as-tool | Agent as a tool | pattern | Call a specialist agent as a tool while the caller keeps control. | subagent as tool |  | multi-agent |
| deployment | Agent deployment and service APIs | topic | Run an agent as a persistent service with APIs and supporting infrastructure. | agent deployment; agent server |  | frameworks |
| evaluation | Agent evaluation and benchmarks | topic | Measure agent behavior and outcomes with defined tasks and scores. | agent evals; agent benchmarking |  |  |
| filesystem | Agent filesystem and storage backends | topic | Expose file tools while controlling where files are stored and how they persist. | filesystem backends; agent filesystem |  | harness |
| frameworks | Agent frameworks and orchestration | topic | Use reusable components and control flow to build agent systems. | agent orchestration; agent frameworks |  | agent-architecture |
| agent-handoff | Agent handoffs | pattern | Transfer control and relevant information from one agent to another. | handoff |  | multi-agent |
| harness | Agent harness design | topic | Design the runtime around a model, including tools, state, limits, and execution. | agent scaffolds; agent scaffolding |  | agent-architecture |
| memory | Agent memory | topic | Store and reuse information across steps or interactions. | agent memory architectures |  |  |
| middleware | Agent middleware | concept | Add reusable behavior around model calls, tool calls, and agent execution. | middleware hooks |  | harness |
| safety | Agent safety and guardrails | topic | Limit harmful agent actions and enforce task or use constraints. | agent guardrails; safety guardrails |  |  |
| a2a | Agent2Agent protocol | protocol | Describe and exchange tasks between agents through a shared protocol. | A2A |  | multi-agent |
| refactoring | Agentic debugging and refactoring | application | Use agents to locate bugs or change code structure while preserving required behavior. | autonomous program improvement; refactoring agents |  | coding-agents |
| agentic-rag | Agentic retrieval | pattern | Let an agent decide when and how to retrieve and revise a search. | agentic RAG | corrective RAG | rag |
| game-agents | Agents for games and puzzles | application | Use agents to act in game environments or solve interactive puzzles. | game-playing agents | BALROG |  |
| verification | Answer verification | pattern | Check claims or candidate answers before accepting a result. | self-verification | chain of verification | reasoning |
| async-agents | Asynchronous agent coordination | pattern | Run agents concurrently and coordinate completion, progress, and results. | async subagents; asynchronous subagents |  | multi-agent |
| harness-optimization | Automatic harness improvement | method | Search or revise agent runtime instructions and structure using measured feedback. | harness search | recursive agent harnessing | harness |
| prompt-optimization | Automatic prompt optimization | method | Use measured feedback to search for better instructions or examples. | context optimization; instruction optimization |  | prompting |
| beam-search | Beam search | method | Keep several high-scoring partial outputs during decoding. |  |  | decoding |
| behavioral-experiments | Behavioral experiments on agents | method | Use controlled tasks to measure observable agent behavior. | experimental agent behavior analysis |  | evaluation |
| bdi | Belief-desire-intention agents | concept | Represent agent behavior through beliefs, goals, and intentions. |  | BDI agents | agent-architecture |
| benchmark-design | Benchmark and test-set design | topic | Define tasks, environments, stopping rules, and scoring for evaluation. | benchmark design; test set design |  | evaluation |
| best-of-n | Best-of-N selection | pattern | Generate several candidates and select one with a verifier or reward score. | best of n; candidate selection |  | inference-scaling |
| cot | Chain of thought | pattern | Generate intermediate reasoning steps before a final answer. | CoT; chain-of-thought |  | reasoning |
| checkpointing | Checkpointing and resuming | pattern | Save agent state so a thread or task can resume after interruption. | checkpointers; execution checkpoints |  | durable-execution |
| citation-eval | Citation and evidence evaluation | topic | Check that references exist, support claims, and cover the answer. | citation accuracy; citation support |  | evaluation |
| clinical-agents | Clinical decision and literature agents | application | Use agents to analyze clinical evidence, compare patient findings, or match trial criteria. | clinical trial matching; rare-disease diagnosis |  |  |
| code-grader | Code-based evaluators | method | Use deterministic code or tests to score agent behavior or outputs. | code based graders; programmatic evaluators |  | evaluation |
| codeact | CodeAct | pattern | Use executable code as the agent action interface. | code actions |  | tool-use |
| coding-agents | Coding and terminal agents | application | Use agents to write, edit, test, or run code and command-line tasks. | software engineering agents; terminal agents |  |  |
| cognitive-perspectives | Cognitive analysis of agents | topic | Compare behavioral, representational, and mechanistic evidence about agent capabilities. |  | cognitive perspectives |  |
| computer-use | Computer-use and web agents | application | Observe and operate browser or desktop interfaces to complete tasks. | GUI agents; computer use agents; browser agents |  |  |
| canonicalization | Concept canonicalization and ontologies | method | Map varied terms to shared concepts and logical relations. | terminology normalization; canonical concepts |  |  |
| consciousness | Consciousness and agency theories | topic | Discuss theories and evidence about consciousness in model-based agents. | machine consciousness |  | cognitive-perspectives |
| constraint-retrieval | Constraint-satisfaction retrieval | method | Retrieve records whose formal constraints are satisfied instead of relying only on similarity. | satisfiability-based retrieval | SatIR | rag |
| context-engineering | Context engineering | topic | Select and organize the information supplied to a model for each step. | context management |  |  |
| context-isolation | Context isolation | pattern | Give a task or subagent a separate context to limit interference. |  |  | context-engineering |
| context-offload | Context offloading | pattern | Store information outside the active prompt and load it when needed. | memory offloading; context offloading to files | memory offloading | context-engineering |
| compaction | Context summarization and compaction | pattern | Replace long interaction history with a shorter useful representation. | context summarization; compaction |  | context-engineering |
| controlled-eval | Controlled improvement experiments | method | Change a defined part of an agent and compare versions under the same test conditions. | improvement tests; controlled version comparison |  | evaluation |
| state | Conversation and execution state | concept | Track messages, task progress, and runtime data across agent steps. | agent state; conversation state |  | agent-architecture |
| cost-quality | Cost, latency, and quality tradeoffs | topic | Compare performance gains with runtime cost, time, and failure consequences. | cost-quality tradeoffs; latency tradeoffs |  |  |
| rl-credit | Credit assignment and advantage estimation | method | Estimate which actions contribute to reward and use baselines or value estimates. | advantage estimation | GAE | rl |
| structured-research | Data-driven research and analysis | application | Use queries and analysis to form, test, and explain findings from structured data. | data-driven deep research | DataSTORM | deep-research |
| data-reconciliation | Database reconciliation and deduplication | method | Resolve duplicate, conflicting, or partial extracted records while keeping provenance. | chunk and reconcile; data reconciliation |  | knowledge-curation |
| provenance | Decision rationale and data provenance | concept | Record where facts came from and how evidence and assumptions support a decision. | data provenance; decision rationale | accountability; faithful rationale | grounding |
| declarative-agents | Declarative task-oriented agent specifications | pattern | Define task fields, constraints, and policies and let a runtime manage the dialogue. | task-oriented dialogue | Genie Worksheets | harness |
| decoding | Decoding and sampling | topic | Choose output tokens from model probabilities. | token sampling; generation strategies |  | llm-foundations |
| deep-research | Deep research agents | application | Run repeated searches, inspect evidence, and synthesize a research answer. | deep research; research agents |  |  |
| developer-alignment | Developer-agent alignment | topic | Analyze whether an agent follows developer intent, constraints, and expected workflows. | developer-agent misalignment |  | human-collaboration |
| dialogue-state | Dialogue state tracking and management | topic | Represent conversation facts, task state, and valid next actions. | dialog state tracking; conversational management |  | state |
| dpo | Direct preference optimization | method | Train directly on preferred and rejected response pairs. | DPO |  | model-training |
| rl-systems | Distributed and asynchronous RL systems | topic | Coordinate rollout generation, training engines, and policy synchronization. | async RL; agentic RL systems |  | rl |
| chunking | Document chunking and indexing | method | Split source documents and build an index for retrieval. | chunking; document indexing |  | rag |
| dspy | DSPy | tool | Build and optimize language model programs with signatures, modules, and optimizers. |  |  | frameworks |
| durable-execution | Durable execution and recovery | pattern | Persist execution state and recover work after failures or pauses. | durable workflows; retries and recovery |  | frameworks |
| dynamic-delegation | Dynamic subagent creation and batch delegation | pattern | Create or schedule subagents for a changing list of work items. | dynamic subagents; batch subagents |  | multi-agent |
| code-interpreter | Embedded code interpreter | method | Run generated code in an interpreter within the agent loop. | code interpreter; interpreter middleware |  | tool-use |
| embeddings | Embedding-based retrieval | method | Encode queries and documents as vectors and retrieve similar documents. | dense retrieval; vector search | DPR | rag |
| emergent-norms | Emergent communication and social norms | concept | Study conventions and norms that arise from repeated agent interaction. | emergent conventions; emergent communication |  | social-behavior |
| episodic-memory | Episodic memory | concept | Store events or past experiences that an agent can recall. |  |  | memory |
| error-analysis | Error analysis and failure taxonomy | method | Inspect failed cases, label failure types, and prioritize fixes by frequency and impact. | failure analysis; failure categories |  | evaluation |
| error-recovery | Error handling and retries | pattern | Detect model or tool errors and retry, recover, or stop safely. | exception handling; exponential backoff |  | frameworks |
| rubrics | Evaluation rubrics | method | Define explicit criteria and rating rules for judgments. | custom rubrics; grading rubrics |  | evaluation |
| critic-loop | Evaluator and optimizer loop | pattern | Use a separate evaluator to guide repeated improvement of an output. | evaluator-optimizer; generator-critic |  | reflection |
| evaluator-metrics | Evaluator precision, recall, and agreement | method | Measure evaluator errors and agreement against trusted labels. | judge precision and recall | Cohen kappa | judge-validation |
| grounding | Evidence grounding and hallucination control | topic | Tie claims to trusted evidence and reduce unsupported statements. | grounded generation; hallucination mitigation |  |  |
| rl-exploration | Exploration and curriculum design | topic | Maintain useful policy exploration and select training tasks by difficulty. |  | exploration collapse; curriculum learning | rl |
| few-shot | Few-shot prompting | method | Include examples in a prompt to guide the response. | fewshot prompting; in-context examples |  | prompting |
| smt | Formal reasoning with SMT | method | Translate constraints to logic and use a satisfiability-modulo-theories solver. | satisfiability modulo theories | MaxSMT | verification |
| gradient-training | Gradient descent and backpropagation | method | Compute loss gradients and update neural-network weights. | backpropagation; gradient descent |  | model-training |
| graph-rag | Graph-based retrieval | method | Use graph relations or graph summaries to support retrieval. | GraphRAG; graph RAG |  | rag |
| grpo | Group relative policy optimization | method | Compare rewards within groups of sampled outputs to update a policy. | GRPO |  | rl |
| document-transcription | Historical document transcription | application | Extract structured text and layout from scans of printed or handwritten documents. | document transcription | OCR; CHURRO | vlm |
| human-demos | Human demonstrations and feedback | method | Collect human actions or feedback to train or improve an agent. | human demonstrations; human feedback |  | data-curation |
| human-eval | Human evaluation | method | Use human judgments or labels to assess agent behavior or outputs. | human graders |  | evaluation |
| hitl | Human oversight and approval | pattern | Pause or route an agent decision to a person for review or approval. | human-in-the-loop; HITL; human oversight |  | safety |
| human-collaboration | Human-agent collaboration | topic | Design how people and agents share tasks, control, and interaction. | human agent interaction; human-agent interaction |  |  |
| hybrid-search | Hybrid retrieval | method | Combine lexical and embedding-based retrieval results. | hybrid search | reciprocal rank fusion | rag |
| hypothesis-ledger | Hypothesis and evidence ledger | pattern | Track competing hypotheses, supporting evidence, refutations, and open questions. | belief ledger; hypothesis tracking |  | deep-research |
| serving | Inference serving and performance | topic | Manage inference engines, batching, latency, throughput, and memory use. | model serving; inference optimization |  | llm-foundations |
| inference-scaling | Inference-time scaling | method | Spend more inference compute on reasoning, search, or repeated attempts. | test-time scaling; test time compute |  | reasoning |
| judge-validation | Judge validation and bias | topic | Check evaluator agreement, accuracy, and bias against trusted labels. | validating LLM judges; evaluator calibration |  | llm-judge |
| knowledge-curation | Knowledge curation and synthesis | topic | Search, organize, compare, and combine information into an evidence-based account. | knowledge synthesis; evidence synthesis |  | deep-research |
| distillation | Knowledge distillation | method | Train a model to follow the outputs or behavior of a teacher model. | on-policy distillation |  | model-training |
| langgraph | LangGraph | tool | Build stateful model workflows with nodes, edges, and graph state. |  |  | frameworks |
| llm-foundations | Language model foundations | topic | Explain next-token modeling and the main parts of a language model. | LLM foundations; language modeling |  |  |
| scaling-laws | Language model scaling laws | concept | Relate model performance to data size, parameter count, and compute budget. | compute-optimal scaling | Chinchilla scaling | llm-foundations |
| llm-judge | LLM as a judge | method | Use a language model to score another system with stated criteria. | LLM-as-judge; LM-as-a-judge; LLM judge |  | evaluation |
| long-context | Long-context modeling | topic | Extend or manage model behavior on long input sequences. | long context; context length extension |  | llm-foundations |
| long-horizon | Long-horizon agent tasks | topic | Maintain progress over long sequences of dependent actions. | long horizon tasks |  | planning |
| lora | Low-rank adaptation | method | Adapt a model by training small low-rank weight updates. | LoRA | parameter-efficient fine-tuning (PEFT) | model-training |
| managed-agents | Managed agent hosting | tool | Use a hosted service to run agents and provide storage, tools, and interfaces. |  | Managed Deep Agents; MDA | deployment |
| interpretability | Mechanistic interpretability | topic | Study internal model features and computations that cause behavior. | mechanistic analysis |  |  |
| memory-eval | Memory evaluation | topic | Measure recall, updating, temporal reasoning, and useful memory use. | memory benchmarks |  | evaluation |
| memory-maintenance | Memory maintenance and consolidation | pattern | Update, combine, remove, or reorganize stored memories. | memory consolidation; forgetting |  | memory |
| memory-poisoning | Memory poisoning | concept | An attacker changes stored memory to affect later agent behavior. |  |  | safety |
| memory-scoping | Memory scoping and user isolation | pattern | Keep persistent memories separate by user, thread, or workspace. | memory isolation; memory namespaces |  | memory |
| meta-learning | Meta-learning | topic | Learn how to adapt to new tasks through shared learning structure. | metalearning; learning to learn |  | model-training |
| metacognition | Metacognition and self-knowledge | topic | Study how agents estimate, monitor, or describe their own knowledge and limits. | introspection; self-knowledge |  |  |
| imputation | Missing-data imputation and assumptions | method | Fill missing facts using stated policies and expose the resulting assumptions. | data imputation | salience-based imputation | provenance |
| circuits | Model circuit analysis | method | Identify groups of model components that implement specific computations. | circuit discovery | induction heads | interpretability |
| model-collapse | Model collapse and synthetic-data risks | concept | Study how repeated training on generated data can reduce quality or diversity. | synthetic data collapse |  | synthetic-data |
| compression | Model compression and quantization | method | Reduce model size or arithmetic precision to lower execution costs. | model quantization; compression |  | llm-foundations |
| mcp | Model Context Protocol | protocol | Connect agent hosts and tool servers through a shared tool interface. | MCP |  | tool-use |
| model-selection | Model selection and provider integration | topic | Choose a model for capability, cost, privacy, and tool support and connect its API. | model selection | model providers | frameworks |
| model-training | Model training and post-training | topic | Train model weights before or after initial pretraining. | LLM training; posttraining |  | llm-foundations |
| model-based-rl | Model-based reinforcement learning | method | Use a learned or given environment model to plan or improve a policy. | model based RL |  | rl |
| moral-behavior | Moral judgment and ethical behavior | topic | Study moral choices, value alignment, and differences between stated judgments and actions. | moral judgment; ethical behavior |  | social-behavior |
| multi-agent-debate | Multi-agent debate | pattern | Let several agents exchange arguments or critique candidate answers. | agent debate |  | multi-agent |
| multi-agent-failures | Multi-agent failure analysis | topic | Analyze coordination failures, conflicting goals, and harmful group behavior. | coordination failures |  | multi-agent |
| multi-agent | Multi-agent systems | topic | Use several agents that interact to solve tasks. | MAS; multiagent systems |  |  |
| reasoning | Multi-step reasoning | topic | Use intermediate reasoning steps to solve a task. | LLM reasoning |  | agent-architecture |
| session-eval | Multi-turn and session evaluation | topic | Evaluate behavior across conversation turns and preserve relevant earlier constraints. | session evaluation; multi-turn evaluation |  | evaluation |
| db-query | Natural-language database and graph queries | application | Use language models to query structured databases and knowledge graphs. | knowledge graph querying; database agents |  |  |
| observation-masking | Observation masking | pattern | Remove or hide older tool outputs while keeping useful interaction structure. |  |  | context-engineering |
| orchestrator-workers | Orchestrator and workers | pattern | Let a coordinator split work and assign subtasks to worker agents. | orchestrator-workers; supervisor-worker |  | multi-agent |
| parallelization | Parallel execution | pattern | Run independent tasks at the same time and combine results. | parallelization; parallelisation |  | workflow-agent |
| persona | Persona and response style control | application | Make an agent follow a defined identity and style while preserving factual constraints. | persona agents; style control |  |  |
| personalization | Personalization and user modeling | topic | Adapt agent behavior to a user's preferences, history, or needs. | user modeling; personal agents |  |  |
| perspective-search | Perspective-guided research | pattern | Use several viewpoints to generate questions and broaden evidence collection. | multi-perspective research; perspective-guided question asking |  | deep-research |
| plan-execute | Plan then execute | pattern | Separate a planning stage from the execution of the planned steps. | plan-and-execute; plan then execution |  | planning |
| planning | Planning and task decomposition | topic | Choose and organize steps or subtasks before or during action. | task planning; task decomposition |  | agent-architecture |
| rl-policy-gradient | Policy gradient methods | method | Update a policy using gradients of expected reward. | policy gradients | REINFORCE | rl |
| privacy | Privacy and user data protection | topic | Control disclosure and use of private user information. | privacy risks |  | safety |
| proactive | Proactive and mixed-initiative agents | pattern | Let an agent decide when to initiate useful actions or interaction. | mixed initiative; proactive agents |  | personalization |
| procedural-memory | Procedural memory and skills | concept | Store reusable procedures or skills that guide actions. | skill libraries; agent skills |  | memory |
| production-eval | Production monitoring and evaluation feedback | pattern | Inspect real runs and feedback and turn production failures into test cases. | production evals | data flywheel | evaluation |
| programmatic-tools | Programmatic tool composition | pattern | Write code that calls and combines several tools in one execution. | programmatic tool calling; PTC |  | tool-use |
| progressive-disclosure | Progressive disclosure | pattern | Load instructions or tool details only when the current task needs them. |  |  | context-engineering |
| prompt-chain | Prompt chaining | pattern | Pass the output of one model step into the next step. | prompt chain |  | workflow-agent |
| prompting | Prompt design | topic | Design instructions, examples, and role messages to guide a model. | prompt engineering; prompting |  |  |
| prompt-injection | Prompt injection | concept | Untrusted content attempts to redirect an agent or override instructions. | indirect prompt injection |  | safety |
| kv-cache | Prompt prefix and KV caching | method | Reuse attention keys and values or shared prompt prefixes to reduce inference work. | KV caching; prefix caching |  | llm-foundations |
| ppo | Proximal policy optimization | method | Update a policy with a clipped objective to limit policy changes. | PPO |  | rl |
| hybrid-data | Queries over structured and unstructured data | method | Compose database operations with free-text retrieval and language processing. | hybrid data queries | SUQL | db-query |
| query-rewriting | Query rewriting and expansion | method | Change or extend a search query to retrieve more useful evidence. | query expansion; search query reformulation |  | rag |
| react | ReAct | pattern | Alternate reasoning, tool actions, and observations. | reasoning and acting |  | agent-architecture |
| recursive-agents | Recursive and self-modifying agents | pattern | Use recursive agent calls or agent-directed changes to system behavior. | recursive agents | hyperagents | agent-architecture |
| red-teaming | Red teaming and adversarial evaluation | method | Test an agent with attacks and difficult misuse cases. | red teaming; adversarial testing |  | safety |
| reflection | Reflection and self-correction | pattern | Use feedback about an attempt to revise reasoning or future actions. | self-reflection; self correction |  | reasoning |
| reflexion | Reflexion | method | Store verbal feedback from earlier attempts to improve later attempts. |  |  | reflection |
| regression-eval | Regression and version comparison | method | Compare agent versions on shared cases and detect behavior that became worse. | regression testing; version comparison |  | evaluation |
| rl | Reinforcement learning | topic | Learn a policy by using rewards from interaction. | RL |  | model-training |
| rlhf | Reinforcement learning from human feedback | method | Train a reward model from human preferences and use it to guide policy updates. | RLHF |  | rl |
| reliability | Reliability and repeated-run evaluation | topic | Measure variation and success across repeated agent runs. | nondeterminism | pass@k; pass^k | evaluation |
| requirements | Requirements and expected behavior | method | Define observable agent behavior and expected outcomes before evaluating a system. | application requirements; behavior requirements |  | benchmark-design |
| reranking | Reranking and late interaction | method | Rescore retrieved candidates with richer query-document comparisons. | cross-encoder reranking | ColBERT | rag |
| research-methods | Research design and paper critique | topic | Form research questions, assess prior work, design experiments, and report evidence. | paper critique; research project design |  |  |
| research-reproduction | Research result reproduction | method | Reproduce published claims using source data and executable analysis. | scientific reproducibility | SEER-Repro | structured-research |
| caching | Response caching | method | Reuse stored results for repeated model or tool requests. | API caching; disk cache |  | frameworks |
| retrieval-eval | Retrieval evaluation | topic | Measure whether retrieval returns relevant evidence. | retrieval metrics; recall at k; MRR; nDCG |  | evaluation |
| rag | Retrieval-augmented generation | topic | Retrieve external information and use it to generate an answer. | RAG; retrieval augmented generation |  |  |
| reward-hacking | Reward hacking and evaluation gaming | concept | Exploit a reward or scoring rule without meeting the intended task. | reward hacking; benchmark gaming |  | evaluation |
| reward-model | Reward modeling | method | Learn or define a score that guides policy training. | reward models; reward functions |  | rl |
| routing | Routing | pattern | Choose a specialized path or component for an input. | router pattern |  | workflow-agent |
| sales-agents | Sales and business assistants | application | Use an agent to manage customer requests, business data, reports, or messages. | sales assistants; business assistants |  |  |
| sandboxing | Sandboxed execution | method | Run code or tools inside a restricted environment. | sandboxing; execution sandbox |  | safety |
| schema-induction | Schema induction and information extraction | method | Define or infer a structured schema and extract source evidence into it. | automatic schematization; schema induction |  | knowledge-curation |
| scientific-workflows | Scientific workflow automation | application | Use agents to configure and run scientific tools or experiments. |  | MDCrow; molecular dynamics agents |  |
| self-consistency | Self-consistency | pattern | Sample several reasoning paths and combine their answers. | self consistency |  | reasoning |
| self-play | Self-play training | method | Generate training challenges through interaction between agents or roles and learn from the resulting tasks. | self play | self-play SWE-RL | rl |
| semantic-memory | Semantic memory | concept | Store facts and general knowledge for later use. |  |  | memory |
| semantic-parsing | Semantic parsing to formal queries | method | Translate natural language to a formal query or logical representation. |  | text-to-SQL; text-to-SPARQL; NL-to-SMT |  |
| shared-memory | Shared memory and task coordination | pattern | Coordinate agents through shared state, task records, or message stores. |  | task ledger; message board | multi-agent |
| skill-induction | Skill induction from experience | method | Extract reusable procedures or code from prior task trajectories. | skill learning; skill induction |  | procedural-memory |
| sliding-memory | Sliding-window conversation memory | pattern | Keep only a recent window of interaction history in the prompt. | sliding window memory |  | working-memory |
| social-simulation | Social simulation with agents | application | Use interacting agents to model communities, groups, or societies. | generative agent societies; agent-based social simulation |  | multi-agent |
| soft-prompts | Soft prompt tuning | method | Learn prompt embeddings while keeping the main model weights fixed. | soft prompting; prompt tuning |  | prompting |
| sparse-autoencoders | Sparse autoencoders for feature discovery | method | Learn sparse features from model activations to inspect internal representations. | SAEs; sparse autoencoders |  | interpretability |
| sparse-retrieval | Sparse retrieval | method | Rank documents with token-based relevance scores. | lexical retrieval | BM25 | rag |
| speculative-decoding | Speculative decoding | method | Use a draft model and verification to generate tokens with less inference time. |  |  | serving |
| state-replay | State replay and branching | pattern | Inspect earlier checkpoints and resume or fork from a previous state. | time travel; state branching |  | checkpointing |
| social-behavior | Strategic and social agent behavior | topic | Study cooperation, coordination, persuasion, and social interaction among agents. | strategic interaction | social dilemmas | multi-agent |
| structured-output | Structured output and constrained decoding | method | Constrain model output to a schema or a set of valid tokens. | structured I/O; constrained generation |  | llm-foundations |
| sft | Supervised fine-tuning | method | Train a model on examples of desired responses or action trajectories. | SFT; instruction fine-tuning |  | model-training |
| synthetic-data | Synthetic data and trajectory generation | method | Generate tasks, examples, or agent rollouts for training or testing. | synthetic data generation; synthesized trajectories |  | data-curation |
| outcome-eval | Task outcome and state-change verification | topic | Check the actual system state and side effects after an agent acts. | outcome verification; end-state verification |  | evaluation |
| theory-of-mind | Theory of mind | concept | Represent or infer another actor's beliefs, goals, or knowledge. | ToM; social cognition |  | social-behavior |
| threat-modeling | Threat modeling and least privilege | method | Identify threats and limit access to the permissions a task requires. |  | threat modeling; least privilege | safety |
| tiered-memory | Tiered memory | pattern | Move information between memory levels with different capacity and access costs. | memory hierarchy | MemGPT | memory |
| tokenization | Tokenization | method | Convert text to token IDs and back using a defined vocabulary and algorithm. |  | BPE; byte pair encoding | llm-foundations |
| auth | Tool authentication and credential handling | topic | Authenticate tool connections and control how credentials reach tools. |  | OAuth; credential brokering | safety |
| tool-discovery | Tool discovery and selection | method | Find and select relevant tools from available tool descriptions. | tool retrieval; API selection |  | tool-use |
| tool-use | Tool use and function calling | topic | Let a model choose and call external functions and consume their results. | tool calling; function calling; tool invocation |  |  |
| tool-eval | Tool-call evaluation | topic | Check selected tools, arguments, execution, and tool-use outcomes. | function-call evaluation; tool use evaluation |  | evaluation |
| observability | Tracing and observability | topic | Record agent steps and inspect behavior, failures, and runtime measurements. | agent traces; telemetry; tracing |  |  |
| trading-agents | Trading and financial assistants | application | Use agents to analyze financial information or support trading decisions. | financial agents |  |  |
| data-curation | Training data selection and quality | topic | Select and check useful tasks, demonstrations, and trajectories. |  | data selection; data quality | model-training |
| trajectory-eval | Trajectory and process evaluation | topic | Evaluate the sequence of agent decisions and actions rather than only the final output. | process evaluation; trajectory evaluation |  | evaluation |
| transformer | Transformer and attention | concept | Use attention-based neural networks to model token sequences. | transformers; self-attention |  | llm-foundations |
| travel-agents | Travel and flight assistants | application | Use agents to plan trips, book travel, or support flight operations. | travel planning agents |  |  |
| tree-thoughts | Tree of thoughts | pattern | Search a branching set of intermediate reasoning states. | ToT; tree-of-thoughts |  | reasoning |
| user-simulation | User and environment simulation | method | Simulate interaction partners or environments for training and testing. | user simulators; simulated users |  | evaluation |
| vlm | Vision-language models | topic | Use models that combine visual inputs and language outputs. | VLMs; multimodal language models |  | llm-foundations |
| vla | Vision-language-action models | topic | Map visual and language inputs to actions, often for embodied tasks. | VLA models; vision language action models |  | vlm |
| visual-grounding | Visual interface grounding | method | Map a visual instruction or screen element to an actionable UI target. | UI grounding; screen grounding |  | computer-use |
| work-impact | Work automation and social impact | topic | Analyze how agent automation affects tasks, workers, and the design of work. | future of work; labor impact |  | human-collaboration |
| workflow-agent | Workflows versus agents | concept | Distinguish fixed program control flow from model-directed control flow. | workflows vs agents; workflow versus agent |  | agent-architecture |
| working-memory | Working memory | concept | Keep information needed for the current task in active context. | short-term memory |  | memory |
| worktree-isolation | Workspace isolation | pattern | Give agents separate working directories to prevent conflicting file changes. | worktree isolation |  | multi-agent |
| world-models | World models | concept | Predict environment states or outcomes to support reasoning and action. | agentic world models |  |  |
