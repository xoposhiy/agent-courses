# Chapter 5 Case Study 1: Building LLMs from Scratch

[Course index](../../README.md) · [Original source](https://arxiv.org/html/2610.13455v1#Ch5) · [Raw file](../../raw/originals/book.html)

Retrieved: 2026-11-13T16:41:17.579179+00:00

[Contents](../../CONTENTS.md) · [Full book](../book/full-book-html.md) · [Previous chapter](chapter-04-scaling-laws-and-efficient-large-language-models.md) · [Next chapter](chapter-06-multi-step-reasoning-in-llms.md)

<a id="Ch5"></a>


### Chapter 5 Case Study 1: Building LLMs from Scratch

**What You Will Learn**

In this case study you will learn how to train your own model.
Specifically, you will be able to:

- Explain the end-to-end *training pipeline* of a ChatGPT-style LLM, distinguishing the purpose and mechanics of each stage: tokenization, pre-training, mid-training, and supervised fine-tuning.
- Configure and train a Byte Pair Encoding (BPE) *tokenizer* and articulate the trade-offs involved in choosing a vocabulary size.
- Describe the transformer *architecture* at a mechanistic level: attention heads, layer depth, embedding dimensions. You will investigate how these hyperparameters interact with model capacity and compute budget.
- Evaluate a trained language model on standard *benchmarks* (ARC-Easy, ARC-Challenge, GSM-8K) and interpret results critically, including failure modes.
- Critically reflect on the *ethical*, environmental, and access dimensions of LLM training, including cost as a barrier to entry and data curation as a values-laden choice.
- Access and navigate the information related to open-access LLM models. This includes reading model cards, training reports, reading code related to training LLMs, and other types of *hub entries*.

<a id="Ch5.S1"></a>


#### 5.1 Building a Chatbot

We will work through a practical case that covers the full lifecycle of a modern ChatGPT-style language model. We use *nanochat*,11
1
<https://github.com/karpathy/nanochat> a minimal, single-codebase, full-stack implementation of an instruction-following LLM, released by Andrej Karpathy in April 2025. Unlike his earlier *nanoGPT*, which covered pre-training only, nanochat implements the complete training pipeline: a Byte Pair Encoding tokenizer, pre-training on web text followed by supervised fine-tuning (SFT) on benchmark datasets, an inference server, and a chat web UI.

The code uses mostly pure Python with minimal dependencies, and therefore is easy to use and extend. The codebase comprises roughly 8,000 lines of Python and a small amount of Rust.22
2
If that number sounds large, it is worth noting that the corresponding proprietary systems run to millions of lines. Nanochat is aimed to be a small self-contained version.

<a id="Ch5.S1.p3.1"></a>


The performance of nanochat is striking: a GPT-2-capable LLM (which cost $\sim$$43,000 to train in 2019 [[Radford et al., 2019](#bibd.bib2)]) for only $48 ($\sim$2 hours of 8xH100 GPU node). While this compute is not exactly commonplace for standard student projects at a university, we can scale down the experiment to make it suited to a hands-on course assignment. It is important to realize that every gradient update and every design decision is visible, from raw bytes to a working chat assistant.
We will take you trough the nanochat pipeline across four tasks that you should all perform.

Because GPU budgets on a course are limited, you will train a *small* model (depth 4, depending on availability, see Section [5.3](#Ch5.S3 "5.3 Experiment Preparation ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models")); you will then reflect on what may happen at larger scale using some theory and the published (nanochat) benchmarks.

<a id="Ch5.S2"></a>


#### 5.2 Background: Karpathy’s nanochat

The case study will give you direct, hands-on experience with every stage of the modern LLM training pipeline, from input text to a deployed chat assistant. This experience will ground the theoretical concepts from Chapters 2–4 in concrete, debuggable code.

nanochat is configured out of the box to train a compute-optimal model by setting a single complexity dial: --depth, which specifies the number of transformer layers. All other hyperparameters—embedding width, number of attention heads, learning rate schedule, training horizon, weight decay—are derived automatically in a near-optimal way. This keeps the configuration space manageable while preserving the full educational value of understanding what each parameter does.

The training pipeline proceeds with the by now hopefully familiar stages, which are briefly described next.

<a id="Ch5.S2.SS0.SSS0.Px1"></a>


###### Pretraining

<a id="Ch5.S2.SS0.SSS0.Px1.p1.1"></a>


The model is trained on approximately 6 billion tokens drawn from CLIMBMix [[Diao et al., 2026](#bibd.bib6)], a clustering-based iteratively bootstrapped data mixture corpus. A depth-24 ($\sim$1.4B-parameter) model trains to a validation loss of 2.41 (0.717 bits-per-byte) in roughly 4 hours on a 4$\times$H100 node compute cluster.

<a id="Ch5.S2.SS0.SSS0.Px2"></a>


###### Supervised finetuning (SFT)

<a id="Ch5.S2.SS0.SSS0.Px2.p1.1"></a>


Starting from the pretrained checkpoint, the model is finetuned on a mixture of instruction-following and reasoning data: SmolTalk [[Ben Allal and others, 2024](#bibd.bib7)] (460K general-purpose conversations), MMLU (multiple-choice knowledge questions, 3 epochs), GSM-8K (grade-school mathematics, 4 epochs), identity conversations, and synthetic spelling tasks—approximately 1.1 million training examples in total. Note that the cross-entropy loss is computed *only on assistant tokens*, not on user prompts, mirroring the InstructGPT training procedure [[Ouyang et al., 2022](#bibd.bib1)].

Before each training stage, a BPE tokenizer is trained on 2 billion characters using a Rust implementation, producing a vocabulary of 32,768 tokens in under one minute.

A web inference server and a lightweight JavaScript chat UI are included out of the box, allowing immediate interaction with your trained model.

<a id="Ch5.S2.SS0.SSS0.Px3"></a>


###### Supplementary resources

<a id="Ch5.S2.SS0.SSS0.Px3.p1.1"></a>


Two freely available courses provide complementary perspectives on the material in this case study. The *Hugging Face LLM Course* [[Hugging Face, 2022](#bibd.bib8)] introduces the transformers, datasets, tokenizers, and accelerate libraries, and the Hugging Face Hub through which most open-weight models are distributed and evaluated today. Mathieu Labonne’s *LLM Course* [[Labonne, 2023](#bibd.bib9)] provides a practitioner roadmap covering pre-training data curation, parameter-efficient fine-tuning (LoRA, QLoRA), preference alignment (DPO, PPO, GRPO), quantization (GGUF, GPTQ), and production inference serving (vLLM, TGI). Together these resources situate nanochat within the broader open-source LLM ecosystem and are referenced explicitly in Tasks 3 and 4. You are also free to browse around for additional resources. It is strongly recommended to link and reference sources in your report where needed.

<a id="Ch5.S3"></a>


#### 5.3 Experiment Preparation

<a id="Ch5.S3.SS0.SSS0.Px1"></a>


###### Repository

Clone the course repository and read the README carefully before writing any code.

Listing 1: Cloning the nanochat repository

[⬇](data:text/plain;base64,Z2l0IGNsb25lIGdpdEBnaXRodWIuY29tOmthcnBhdGh5L25hbm9jaGF0LmdpdA==)

1
git clone git@github.com:karpathy/nanochat.git

<a id="Ch5.S3.SS0.SSS0.Px2"></a>


###### Compute

No dedicated compute is necessary. You may use your own laptop (with a GPU), or a larger computer. The experiments are planned so that each run completes a maximum of approximately 8 hours. For pretraining, use a --depth 4 configuration; --depth 2 is acceptable only if your hardware does not permit the larger model. Do *not* attempt depth $\geq$12 unless you have some serious hardware.

<a id="Ch5.S3.SS0.SSS0.Px3"></a>


###### Logging

nanochat logs training loss, validation loss, and bits-per-byte at configurable intervals to your terminal, and additional functionality for reporting and saving information during the run is available. It is therefore wise to enable structured logging to a .jsonl file from the start. Retrofitting logging after a run is painful. You may want to experiment with the logging file formats. We recommend using a service such as wandb.ai before training full models.

<a id="Ch5.S4"></a>


#### 5.4 Task 0: Model Hub warm-up.

<a id="Ch5.S4.SS0.SSS0.Px1"></a>


###### Description

Before starting the tasks, it is a good idea to get a feel for common parameter settings and common training settings for different models. For this purpose, practice navigating the Hugging Face Hub.33
3
<https://huggingface.co/models> For each of the three model IDs in Table [5.1](#Ch5.T1 "Table 5.1 ‣ Description ‣ 5.4 Task 0: Model Hub warm-up. ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models"), locate and record:

1. the number of training tokens or steps,
2. the model architecture (number of layers, hidden dimension, attention heads, number of trainable parameters), and
3. the training data sources, if possible.

<a id="Ch5.T1"></a>


| **Model ID** | **Organization** |
| --- | --- |
| allenai/OLMo-1B | Allen Institute for AI |
| HuggingFaceTB/SmolLM2-360M | Hugging Face |
| Qwen/Qwen2.5-0.5B | Alibaba Cloud |

Table 5.1: Model IDs for the Hub warm-up exercise

Pay attention to *where* you look for each piece of information: some fields appear directly on the model card, others require inspecting config.json under the Files tab, and some are only available in the accompanying paper. Include a short table with your findings in your report, noting the source for each field.

<a id="Ch5.S5"></a>


#### 5.5 Task 1: Tokenization

<a id="Ch5.S5.SS1"></a>


##### 5.5.1 What to Do

Train a BPE tokenizer using nanochat’s Rust tokenizer trainer on a 500 million character sample of the CLIMBMix dataset. Run two experiments: one with a vocabulary size of *8,192* tokens and one with *32,768* tokens.

<a id="Ch5.S5.SS2"></a>


##### 5.5.2 Deliverables

- A short script that reproduces your tokenizer training run.
- A report section (at most 1 page) answering the following questions with evidence from your own tokenizer outputs:

  1. What is BPE, and how does it differ from word-level and character-level tokenization? Draw a merge tree for a concrete example (you can look for one in the data, or make your own. Do not reuse an existing example!). Make sure to also include the counts for your merges.
  2. How does vocabulary size affect *compression ratio* (tokens per character) and *sequence length* for a fixed text sample? Show measurements from both of your tokenizers on English text.
  3. Why does vocabulary size matter for the downstream language model? In your answer, consider the embedding matrix size, the softmax denominator, and the challenge of learning reliable representations for rare tokens.
  4. What artifacts or failure cases do you observe? How does your tokenizer handle numbers, source code, or non-English text?

Pay attention to: correctness of the BPE explanation; quality of empirical evidence; depth of analysis on vocabulary trade-offs; perceptiveness of failure-case discussion.

<a id="Ch5.S6"></a>


#### 5.6 Task 2: Pretraining

<a id="Ch5.S6.SS1"></a>


##### 5.6.1 What to Do

Pretrain a transformer using nanochat with --depth 4 (or, in case your computer is not fast enough, --depth 2) on the CLIMBMix dataset. Log training loss, validation loss, and bits-per-byte at regular checkpoints.

<a id="Ch5.S6.SS2"></a>


##### 5.6.2 Deliverables

- Bits-per-byte curves for training and validation set (plots, to be included in the report). Use bpb instead of the raw loss.
- A saved model checkpoint.
- A report section (approximately 2 pages) covering:

  1. The Depth Parameter: Explain what the --depth argument controls in nanochat and how the codebase derives all other hyperparameters automatically from it: embedding width, number of attention heads, learning rate schedule, training horizon. For the chosen depth, state the number of layers, attention heads, embedding dimension, the total trainable parameter count, and the number of total tokens the model will be trained on. Why is a single-dial design useful for such a codebase? What are its limitations compared to tuning each hyperparameter independently?
  2. <a id="Ch5.S6.I1.i3.I0.i2.p1.1"></a>


     Scaling Laws: Using the Chinchilla framework [[Hoffmann et al., 2022](#bibd.bib4)], compute the compute-optimal number of training tokens for your model’s parameter count. How does nanochat’s default training horizon compare? What does it mean to be *under-trained* or *over-trained*?
  3. Loss Analysis: Plot the progress of bits-per-byte (bpb) during training as your training curve and explain its shape. At what point does the curve flatten? What does the gap between training and validation tell you?
  4. Qualitative Inspection: Sample five completions from your pretrained model with no system prompt (raw next-token prediction). What is the model able to do at this stage, and why do you think that is the case?

Pay attention to: correctness of the depth-parameter explanation and auto-configuration description; accuracy of architecture description; correct application of scaling law calculations; quality of loss analysis; insightfulness of qualitative assessment.

<a id="Ch5.S7"></a>


#### 5.7 Task 3: Mid-Training and Supervised Finetuning

<a id="Ch5.S7.SS1"></a>


##### 5.7.1 What to Do

Recall that nanochat only performs two training stages: pretraining and SFT. However, in the book, we discussed that additional stages in the form of mid-training can help the model perform better. In this task, you will implement a new mid-training stage by modifying scripts/chat_sft.py. The goal is to separate *reasoning adaptation* (mid-training) from *instruction following* (SFT) and measure the effect empirically.

<a id="Ch5.S7.SS1.SSS0.Px1"></a>


###### Stage 1 — Mid-training

Modify the train_tasks list in chat_sft.py so that it contains only reasoning and knowledge tasks: MMLU and GSM-8K. Remove all other conversational and spelling data. Run chat_sft.py from your pre-trained base checkpoint and save the resulting checkpoint.

<a id="Ch5.S7.SS1.SSS0.Px2"></a>


###### Stage 2 — SFT

Modify chat_sft.py again so that train_tasks contains only SmolTalk. You will also need to make a small change so the script loads your Stage 1 checkpoint rather than the base pre-trained model. Inspect the load_model call in chat_sft.py as a starting point.44
4
Hint: read nanochat/checkpoint_manager.py to understand how checkpoints are located. Run chat_sft.py from your Stage 1 checkpoint to proceed with SFT after mid-training.

After each stage, evaluate with scripts/chat_eval.py on ARC-Easy, ARC-Challenge, and GSM-8K.

**Sanity check:** Before running Stage 1, inspect the data: print the first few rows of the MMLU and SmolTalk datasets to understand their format and content. Make sure you are able to answer: how many training examples does each dataset contribute, and what does a single training example look like?

<a id="Ch5.S7.SS2"></a>


##### 5.7.2 Deliverables

- Two checkpoints, one for each stage (mid-training and SFT).
- Evaluation scores on ARC-Easy, ARC-Challenge, and GSM-8K after each stage, reported as a table. This should be part of the report (see below).
- A report section (approximately 3 pages) covering:

  1. Implementation: Describe the changes you made to the codebase such that you can do training in stages. List the hyperparameters that you are using for the training experiments. You are free to experiment with them!
  2. Loss Masking: Why is the SFT loss computed only on assistant tokens? Construct a concrete token-level example illustrating what the loss would look like with and without masking.
  3. Dataset Analysis: For each stage, describe the dataset used, its approximate size, and why it was chosen for that stage specifically. What values or potential biases might be embedded in dataset training splits? How might these shape model behavior?
  4. Benchmark Scores: Report your evaluation scores after each stage in a table. What changed between Stage 1 and Stage 2, and why? Also compare to the pretrained results such that your analysis covers all three stages. Note any results that surprised you.
  5. Parameter-efficient Finetuning: nanochat performs full fine-tuning: every parameter is updated during SFT. Describe how LoRA (Low-Rank Adaptation) and its quantized variant QLoRA differ from full fine-tuning. What are the trade-offs in compute, memory, and final model quality? Would you recommend using PEFT techniques for the depths we have used in training so far?

Pay attention to: correctness and clarity of the implementation description; correctness of the loss-masking explanation; critical quality of dataset analysis; accuracy and completeness of reported benchmark scores and their interpretation; conceptual accuracy of the LoRA/QLoRA comparison.

<a id="Ch5.S8"></a>


#### 5.8 Task 4: Inference, Deployment, and Critical Reflection

<a id="Ch5.S8.SS1"></a>


##### 5.8.1 Part A: Inference and Deployment

Launch nanochat’s inference server and web UI. Interact with your trained model. Then address the following in your report (approximately 1 page):

1. The Inference Loop: Describe how autoregressive sampling works, including the role of the key–value (KV) cache in avoiding redundant computation across decoding steps. Play around with decoding with different parameters: What is temperature, and what effect does varying it (try 0.1, 0.7, and 1.5) have on output quality and diversity? Show and discuss five representative examples from your own model.
2. Production Hardening: Identify three concrete engineering changes that the nanochat inference server would need before deployment at production scale.
3. Capability Comparison and Scaling: Look up published benchmark scores on ARC-Easy, ARC-Challenge, and GSM-8K for at least two publicly available models: one in a comparable size range to your nanochat model, and one substantially larger. Feel free to find scores for any type of inference design (e.g., zero-shot, few-shot, others) but report the specific conditions. Model cards and leaderboard entries on the Hugging Face Hub are a good starting point; cite every source you use. Build a table placing your own results alongside the published figures. Then address the following two questions. Where does your model fall relative to models of similar parameter count? What does the gap between your model and a well-trained model of the same size reveal about the role of data quality, training duration, and alignment?

<a id="Ch5.S8.SS2"></a>


##### 5.8.2 Part B: Critical Reflection

Write a short discussion (approximately 0.5-1 page) responding to *one* of the following three prompts.

> *Prompt 1 — Access and Democratization*
> nanochat’s headline claim is that “the best ChatGPT that $100 can buy” brings LLM training within reach of individuals. Critically evaluate this claim. Who still cannot access this pipeline, and why?

> *Prompt 2 — Data and Values*
> nanochat pretrains on CLIMBMix, a clustering-based iteratively bootstrapped data mixture corpus. What decisions were made in constructing this dataset, and whose values do they embed? How might a different pre-training corpus lead to a qualitatively different model?

> *Prompt 3 — Environmental Cost*
> nanochat’s “affordable” training run consumes approximately four hours of 8$\times$H100 GPUs. Estimate the carbon cost of your own training run using an established methodology (e.g. the ML CO2 Impact calculator).55
> 5
> <https://mlco2.impact.compute.org> Situate this in the broader context of LLM environmental impact. Is *cheap* the same as *low-impact*?

Part A: pay attention to: correctness of inference loop description; practicality of production hardening proposals; completeness of the benchmark description and relevance of discussion to state-of-the-art;

Part B: pay attention to: analytical depth; use of evidence; willingness to challenge assumptions.

<a id="Ch5.S9"></a>


#### 5.9 Recommended Reading

- <a id="Ch5.S9.I1.i1.p1.1"></a>


  [Vaswani et al. [2017]](#bibd.bib3) — The original transformer paper; essential reading before Task 2.
- <a id="Ch5.S9.I1.i2.p1.1"></a>


  [Hoffmann et al. [2022]](#bibd.bib4) — Chinchilla scaling laws; required for the scaling-law question in Task 2.
- <a id="Ch5.S9.I1.i3.p1.1"></a>


  [Ouyang et al. [2022]](#bibd.bib1) — InstructGPT; the basis for SFT and RLHF in Task 3.
- <a id="Ch5.S9.I1.i4.p1.1"></a>


  [Diao et al. [2026]](#bibd.bib6) — CLIMBMix / Nemotron-CLIMB; read the data curation methodology before Task 2’s dataset analysis question.
- <a id="Ch5.S9.I1.i5.p1.1"></a>


  [Bender et al. [2021]](#bibd.bib5) — Critical perspective on large language models; relevant to the Task 4 reflection prompts.
- <a id="Ch5.S9.I1.i6.p1.1"></a>


  [Hugging Face [2022]](#bibd.bib8) — The Hugging Face LLM Course; covers the transformers, tokenizers, and datasets libraries and the Hugging Face Hub; useful context for Tasks 1, 3, and 4.
- <a id="Ch5.S9.I1.i7.p1.1"></a>


  [Labonne [2023]](#bibd.bib9) — Labonne’s *LLM Course*; practitioner roadmap covering LoRA/QLoRA, DPO, GGUF/GPTQ quantization, and vLLM/TGI serving; recommended before Tasks 3 and 4.

<a id="Ch5.S10"></a>


#### 5.10 Concluding Remarks

In this chapter we have used nanochat as a window into the complete LLM training pipeline. You have trained a BPE tokenizer, observed a transformer learn from web text, adapted that model to follow instructions, evaluated it on standard benchmarks, and deployed it as a chat assistant.

The gap between your depth-4 model and the frontier will be obvious, because we don’t expect you to have access to datacenter-grade compute capabilities. However, the experiments are, in theory, scalable: rerunning at higher depths and with additional data resources should lead to more capable models, as predicted by the scaling laws. After completion of Assignment 1, you have essentially trained a full LLM by yourself, and you will be better equipped for future experiments where an increased scale is necessary.

<a id="bibd"></a>


### References

<a id="bibd.bib7"></a>
- Ben Allal et al. (2024)
  L. Ben Allal et al.
  SmolTalk.
   Hugging Face.
  External Links: [Link](https://huggingface.co/datasets/HuggingFaceTB/smoltalk)
  Cited by: [§5.2](#Ch5.S2.SS0.SSS0.Px2.p1.1 "Supervised finetuning (SFT) ‣ 5.2 Background: Karpathy’s nanochat ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
<a id="bibd.bib5"></a>
- Bender et al. (2021)
  E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell
  On the dangers of stochastic parrots: can language models be too big?.
  In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency,
  FAccT ’21, New York, NY, USA, pp. 610–623.
  External Links: ISBN 9781450383097,
  [Link](https://doi.org/10.1145/3442188.3445922),
  [Document](https://dx.doi.org/10.1145/3442188.3445922)
  Cited by: [5th item](#Ch5.S9.I1.i5.p1.1 "In 5.9 Recommended Reading ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
<a id="bibd.bib6"></a>
- Diao et al. (2026)
  S. Diao, Y. Yang, Y. Fu, X. Dong, D. Su, M. Kliegl, Z. Chen, P. Belcak, Y. Suhara, H. Yin, et al.
  Nemotron-climb: clustering-based iterative data mixture bootstrapping for language model pre-training.
  Advances in Neural Information Processing Systems 38.
  Cited by: [§5.2](#Ch5.S2.SS0.SSS0.Px1.p1.1 "Pretraining ‣ 5.2 Background: Karpathy’s nanochat ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models"),
  [4th item](#Ch5.S9.I1.i4.p1.1 "In 5.9 Recommended Reading ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
<a id="bibd.bib4"></a>
- Hoffmann et al. (2022)
  J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. de Las Casas, L. A. Hendricks, J. Welbl, A. Clark, T. Hennigan, E. Noland, K. Millican, G. van den Driessche, B. Damoc, A. Guy, S. Osindero, K. Simonyan, E. Elsen, O. Vinyals, J. W. Rae, and L. Sifre
  Training compute-optimal large language models.
  In Proceedings of the 36th International Conference on Neural Information Processing Systems,
  NIPS ’22, Red Hook, NY, USA.
  External Links: ISBN 9781713871088
  Cited by: [item 2](#Ch5.S6.I1.i3.I0.i2.p1.1 "In 3rd item ‣ 5.6.2 Deliverables ‣ 5.6 Task 2: Pretraining ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models"),
  [2nd item](#Ch5.S9.I1.i2.p1.1 "In 5.9 Recommended Reading ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
<a id="bibd.bib8"></a>
- Hugging Face (2022)
  Hugging Face
  The hugging face LLM course.
  External Links: [Link](https://huggingface.co/learn/llm-course)
  Cited by: [§5.2](#Ch5.S2.SS0.SSS0.Px3.p1.1 "Supplementary resources ‣ 5.2 Background: Karpathy’s nanochat ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models"),
  [6th item](#Ch5.S9.I1.i6.p1.1 "In 5.9 Recommended Reading ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
<a id="bibd.bib9"></a>
- Labonne (2023)
  M. Labonne
  LLM course.
  External Links: [Link](https://github.com/mlabonne/llm-course)
  Cited by: [§5.2](#Ch5.S2.SS0.SSS0.Px3.p1.1 "Supplementary resources ‣ 5.2 Background: Karpathy’s nanochat ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models"),
  [7th item](#Ch5.S9.I1.i7.p1.1 "In 5.9 Recommended Reading ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
<a id="bibd.bib1"></a>
- Ouyang et al. (2022)
  L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al.
  Training language models to follow instructions with human feedback.
  Advances in Neural Information Processing Systems 35, pp. 27730–27744.
  Cited by: [§5.2](#Ch5.S2.SS0.SSS0.Px2.p1.1 "Supervised finetuning (SFT) ‣ 5.2 Background: Karpathy’s nanochat ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models"),
  [3rd item](#Ch5.S9.I1.i3.p1.1 "In 5.9 Recommended Reading ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
<a id="bibd.bib2"></a>
- Radford et al. (2019)
  A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever, et al.
  Language models are unsupervised multitask learners.
  OpenAI blog 1 (8), pp. 9.
  Cited by: [§5.1](#Ch5.S1.p3.1 "5.1 Building a Chatbot ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
<a id="bibd.bib3"></a>
- Vaswani et al. (2017)
  A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin
  Attention is all you need.
  Advances in neural information processing systems 30.
  Cited by: [1st item](#Ch5.S9.I1.i1.p1.1 "In 5.9 Recommended Reading ‣ Chapter 5 Case Study 1: Building LLMs from Scratch ‣ Part I Language Modeling ‣ Agentic Large Language Models").
