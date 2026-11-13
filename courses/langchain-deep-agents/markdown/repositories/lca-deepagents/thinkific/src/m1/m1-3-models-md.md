# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m1/m1.3-models.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m1/m1.3-models.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m1/m1.3-models.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m1.3-models.md)

Python TypeScript

<a id="models"></a>


# Models

```text
<button class="lt-tab active" data-p="models" role="tab" aria-selected="true">Models</button>
```

```text
<button class="lt-tab" data-p="lab1" role="tab" aria-selected="false">Lab</button>
```

<a id="p-models"></a>


<a id="models-use-any-model-provider"></a>


## Models: Use Any Model Provider

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/jpAgDzQoj7Z.md)

**What is a model provider?**

A model provider is a company or platform that hosts AI models and lets you call them through an API (e.g., OpenAI, Anthropic, Google). `langchain` gives you one consistent way to call those models: install the provider package, pick a model name, and swap models without rewriting your agent code.

`langchain` supports 50+ chat model providers. See the full [chat model integrations](../../../../../readings/docs-langchain-com-oss-python-integrations-chat-03aad07c.md) list for what’s available.

![LangChain](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m1/images/langchain-symbol.png)

`langchain`’s model-agnostic design means you can swap in whatever fits your needs:

- a cheaper model to cut costs
- an open-source model for privacy
- a more capable one for complex reasoning

<a id="model-categories"></a>


### Model Categories

| Category | Best for | Examples |
| --- | --- | --- |
| Proprietary & Conversational | Fluid conversation, instruction-following, and general-purpose tasks | Claude Haiku/Sonnet, GPT-4.1, Gemini 3.6 Flash |
| Advanced Reasoning | Multi-step problem-solving, math, code, and logic-heavy tasks | Claude Opus 4, o3, Gemini 2.5 Pro |
| Open-Source & Open-Weight | Local or private deployment; lower cost and full control over the model | Llama 3.3, Mistral, Qwen |

Most models in all three categories also accept image inputs (and some accept audio). Multimodal support works through the same `init_chat_model` interface.

The table above covers the main categories used in this course. For the full directory of 50+ supported chat model providers (OpenAI, Anthropic, Google, Groq, Ollama, Mistral, and many more), see the [LangChain chat model integrations](../../../../../readings/docs-langchain-com-oss-python-integrations-chat-03aad07c.md).

Every lab gets its model from a single shared file, **`python/models.py`**. It exports a `model` object built with `init_chat_model(...)`, and the lab scripts simply do `from models import model`.

To use a different model or model provider, edit `models.py` (comment out the active line and uncomment the desired model):

```text
# python/models.py
model = init_chat_model("anthropic:claude-haiku-4-5")   # workshop default, fast & cheap
# model = init_chat_model("ollama:qwen2.5:7b")
# model = init_chat_model("openai:gpt-6-luna", use_responses_api=True)
# strong_model = init_chat_model("openai:gpt-6.1-sol", use_responses_api=True)
```

For official OpenAI models, keep `use_responses_api=True` when changing the model name (including `gpt-5.6-luna`). This explicitly selects the Responses API instead of relying on model-name detection. Do not copy this setting to third-party OpenAI-compatible providers unless they support that API.

If you set up Anthropic or OpenAI in the setup lesson, those work out of the box. If you want to use Azure, Bedrock, or Google, those require an extra install (`uv sync --extra azure|bedrock|google`) and additional env vars; see the notes at the top of `models.py`.

Head to **Lab 1** to run this yourself and see how the output changes across models. Scroll back to the top of this lesson and choose the **Lab** tab.

**Optional: feeling lost?** If agents and harnesses are new to you, watch the [Agent Harnesses and Deep Agents 101](https://events.langchain.com/on-demand/bac35c58-985f-449c-826d-d5a8474ce2fe) talk for a big-picture overview before continuing.

---

<a id="recap"></a>


## Recap

- `init_chat_model("provider:model")` targets any `langchain`-supported chat model with a single string; swap the prefix to switch model providers, swap the suffix to switch models
- All labs share one model object from `python/models.py`; changing that one line is the only code change needed to run a different model
- Three categories in this course: Proprietary & Conversational, Advanced Reasoning, and Open-Source/Open-Weight; 50+ chat model providers are supported in total
- Swapping the model changes nothing else in the agent; the system prompt, tools, and behavior instructions stay identical

---

<a id="next"></a>


## Next

Complete the **Lab** above, then continue to the next lesson on the **system prompt**: how a single instruction string steers the agent’s persona and domain without touching anything else.

---

<a id="references"></a>


## References

**Documentation:**

- [Deep Agents overview](../../../../../readings/docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md)
- [Models (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-models-d81a8a13.md)
- [Customization & prompt assembly (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-customization-86c6cc54.md)
- [Context engineering (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-context-engineering-e0a127e9.md)
- [deepagents README (GitHub)](../../../../../readings/github-191947403d65.md)
- [Built-in harness profiles (GitHub)](../../../../../readings/github-04b9208101d4.md)
- [Chat model integrations (LangChain)](../../../../../readings/docs-langchain-com-oss-python-integrations-chat-03aad07c.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`_models.py`](../../../../../readings/github-0e291805e105.md): helpers that resolve model strings into chat models

<a id="models-use-any-model-provider-1"></a>


## Models: Use Any Model Provider

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/jpAgDzQoj7Z.md)

**What is a model provider?**

A model provider is a company or platform that hosts AI models and lets you call them through an API (e.g., OpenAI, Anthropic, Google). `langchain` gives you one consistent way to call those models: install the provider package, pick a model name, and swap models without rewriting your agent code.

`langchain` supports 50+ chat model providers. See the full [chat model integrations](../../../../../readings/docs-langchain-com-oss-javascript-integrations-chat-c2ad5190.md) list for what’s available.

![LangChain](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m1/images/langchain-symbol.png)

`langchain`’s model-agnostic design means you can swap in whatever fits your needs:

- a cheaper model to cut costs
- an open-source model for privacy
- a more capable one for complex reasoning

<a id="model-categories-1"></a>


### Model Categories

| Category | Best for | Examples |
| --- | --- | --- |
| Proprietary & Conversational | Fluid conversation, instruction-following, and general-purpose tasks | Claude Haiku/Sonnet, GPT-4.1, Gemini 3.6 Flash |
| Advanced Reasoning | Multi-step problem-solving, math, code, and logic-heavy tasks | Claude Opus 4, o3, Gemini 2.5 Pro |
| Open-Source & Open-Weight | Local or private deployment; lower cost and full control over the model | Llama 3.3, Mistral, Qwen |

Most models in all three categories also accept image inputs (and some accept audio). Multimodal support works through the same `initChatModel` interface.

The table above covers the main categories used in this course. For the full directory of 50+ supported chat model providers (OpenAI, Anthropic, Google, Groq, Ollama, Mistral, and many more), see the [LangChain chat model integrations](../../../../../readings/docs-langchain-com-oss-javascript-integrations-chat-c2ad5190.md).

Every lab gets its model from a single shared file, **`typescript/models.ts`**. It exports a `model` object built with `initChatModel(...)`, and the lab scripts simply do `import { model } from "../models.js"`.

To use a different model or model provider, edit `models.ts` (comment out the active line and uncomment the desired model):

```text
// typescript/models.ts
export const model = await initChatModel("anthropic:claude-haiku-4-5");   // workshop default, fast & cheap
// export const model = await initChatModel("ollama:qwen2.5:7b");
// export const model = await initChatModel("openai:gpt-6-luna", { useResponsesApi: true });
// export const strongModel = await initChatModel("openai:gpt-6.1-sol", { useResponsesApi: true });
```

For official OpenAI models, keep `useResponsesApi: true` when changing the model name (including `gpt-5.6-luna`). This explicitly selects the Responses API instead of relying on model-name detection. Do not copy this setting to third-party OpenAI-compatible providers unless they support that API.

If you set up Anthropic or OpenAI in the setup lesson, those work out of the box. If you want to use Bedrock or Google, those require an extra install (`@langchain/aws` and `@langchain/google-genai`) and additional env vars; see the notes at the top of `models.ts`.

Head to **Lab 1** to run this yourself and see how the output changes across models. Scroll back to the top of this lesson and choose the **Lab** tab.

**Optional: feeling lost?** If agents and harnesses are new to you, watch the [Agent Harnesses and Deep Agents 101](https://events.langchain.com/on-demand/bac35c58-985f-449c-826d-d5a8474ce2fe) talk for a big-picture overview before continuing.

---

<a id="recap-1"></a>


## Recap

- `initChatModel("provider:model")` targets any `langchain`-supported chat model with a single string; swap the prefix to switch model providers, swap the suffix to switch models
- All labs share one model object from `typescript/models.ts`; changing that one line is the only code change needed to run a different model
- Three categories in this course: Proprietary & Conversational, Advanced Reasoning, and Open-Source/Open-Weight; 50+ chat model providers are supported in total
- Swapping the model changes nothing else in the agent; the system prompt, tools, and behavior instructions stay identical

---

<a id="next-1"></a>


## Next

Complete the **Lab** above, then continue to the next lesson on the **system prompt**: how a single instruction string steers the agent’s persona and domain without touching anything else.

---

<a id="references-1"></a>


## References

**Documentation:**

- [Deep Agents overview](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-overview-9687b9be.md)
- [Models (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-models-4dcacd72.md)
- [Customization & prompt assembly (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-customization-6f109080.md)
- [Context engineering (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-context-engineering-de9e92ff.md)
- [deepagents README (GitHub)](../../../../../readings/github-191947403d65.md)
- [Built-in harness profiles (GitHub)](../../../../../readings/github-04b9208101d4.md)
- [Chat model integrations (LangChain)](../../../../../readings/docs-langchain-com-oss-javascript-integrations-chat-c2ad5190.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`agent.ts`](../../../../../readings/github-8221cd675654.md): where `createDeepAgent` resolves your model string into a harness profile

<a id="p-lab1"></a>


<a id="models-1"></a>


## Models

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/MKueYS2eqAV.md)

First, run your scratch agent from the previous lesson with the default model:

```text
cd python
uv run ./m1/m1.2_scratch_agent.py
```

Next, open `python/models.py` and switch the model: comment out the active Haiku line and uncomment another model line you want to try.

After you change `models.py`, run the same script again and compare the output:

```text
cd python
uv run ./m1/m1.2_scratch_agent.py
```

This also works with open-source models; no code changes required, just a different model line in `models.py`.

**Why use an open-source model?**

- **Privacy:** data never leaves your machine when running locally (using a local runtime such as Ollama); useful for sensitive or proprietary content
- **Cost:** no per-token charges when self-hosted; many hosted options are free or significantly cheaper than proprietary APIs
- **No vendor lock-in:** swap between different providers and models (e.g. Llama, Mistral, Qwen) with a single line change
- **Customization:** open weights mean you can fine-tune the model on your own data

**Try an open-source model via OpenRouter**

OpenRouter gives you access to free hosted open-source models with no extra install. If you added your `OPENROUTER_API_KEY` to `.env` during setup, just uncomment the OpenRouter lines in `models.py` and run the lab again. If you haven’t added it yet, head back to the [setup lesson](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m0/m0.1-setup-python.html) to add it to your `.env` file.

Model used in this course: [nvidia/nemotron-3-ultra-550b-a55b:free on OpenRouter](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free)

**Note:** Free models on hosted platforms typically mean you are consenting to the provider using your prompts and completions as training data. Avoid sending sensitive or proprietary information through free-tier endpoints.

Open-Source (Nvidia) Setup

[Public video walkthrough](../../../../../videos/O1Vjox9ay96.md)

Here are two real responses to “What is an LLM?”, one from each model:

claude-haiku-4-5

An LLM (Large Language Model) is a type of artificial intelligence system trained on vast amounts of text data to predict and generate human language.

**Key characteristics:**

- **Scale**: Contains billions to hundreds of billions of parameters (learnable weights), which is why they’re “large”
- **Training**: Learns patterns from massive text datasets using transformer-based neural networks
- **Capability**: Can perform tasks like answering questions, writing, summarizing, translating, coding, and reasoning
- **Generative**: Produces text one word (or “token”) at a time, based on patterns learned during training
- **Context-aware**: Maintains understanding of conversation history and context within a session

**Common examples**: ChatGPT, Claude, Gemini, Llama, and Mistral are all LLMs.

LLMs don’t truly “understand” in the human sense; they’re sophisticated pattern-matching systems that are remarkably effective at tasks requiring language comprehension and generation.


nvidia/nemotron-3-ultra-550b-a55b

An **LLM (Large Language Model)** is a type of artificial intelligence model trained on vast amounts of text data to understand and generate human-like language.

**Key characteristics:**

- **Scale**: Billions to trillions of parameters (e.g., GPT-4, Claude, Llama)
- **Training**: Self-supervised learning on diverse text corpora (books, websites, code, etc.)
- **Architecture**: Typically based on the Transformer architecture with attention mechanisms
- **Capabilities**: Text generation, summarization, translation, coding, reasoning, question answering

**How it works:** LLMs predict the next token (word/character) in a sequence based on context. Through massive training, they learn patterns, facts, reasoning, and linguistic structures.

**Limitations:** They can hallucinate (generate false information), lack true understanding, have knowledge cutoffs, and can be biased by training data.

---

<a id="ollama-run-a-model-locally"></a>


### Ollama: run a model locally

**[NO API KEY NEEDED]**

Ollama is a tool for downloading and running open-source models directly on your machine. No API key, no data sent to a third party: the model runs entirely on your hardware.

Open-Source (Ollama) Setup

[Public video walkthrough](../../../../../videos/5t0FLKmmD7h.md)

**Step 1: Install Ollama** from [ollama.com](https://ollama.com)

**Step 2: Pull a model:**

```text
ollama pull qwen2.5:7b
```

**Step 3: Update `python/models.py`.** Comment out the active line and uncomment the Ollama line:

```text
# model = init_chat_model("anthropic:claude-haiku-4-5")
model = init_chat_model("ollama:qwen2.5:7b")
```

**Step 4: Run the lab as normal.** No other code changes needed.

The agent code and system prompt are identical. Only the model line in `models.py` is different.

> **Local only.** Ollama also offers hosted cloud models at ollama.com, which do require an API key. These steps are for running a model locally on your own machine.

**Heads up: small or older local models can struggle with deep agents**

Deep agent workflows lean hard on reliable tool calling and system-prompt adherence. Tiny local models are best suited to lightweight tasks like summarization, and tend to struggle with agentic work like this.

- Consumer hardware generally can’t run frontier-capable open models locally, which is part of why Ollama itself sells [hosted cloud models](https://ollama.com/cloud) for the larger ones.
- Open-weight models have improved dramatically in recent releases, so if yours ignores your system prompt, skips tool calls, or loops, that’s likely a model-capability limit (not a bug in your setup).
- Hardware permitting, pull a newer, larger model instead (check what your machine can handle before pulling one):
  - 7B models: ~8GB RAM
  - 14B models: ~16GB RAM
  - 32B models: ~24GB+ RAM
  - 70B-class models (e.g. Llama 3.3 70B): ~64GB RAM
- Otherwise, use the **OpenRouter** option above for a larger open-weight model without the local hardware requirement.

<a id="models-2"></a>


## Models

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/MKueYS2eqAV.md)

First, run your scratch agent from the previous lesson with the default model:

```text
cd typescript
pnpm tsx ./m1/m1.2_scratch_agent.ts
```

Next, open `typescript/models.ts` and switch the model: comment out the active Haiku line and uncomment another model line you want to try.

After you change `models.ts`, run the same script again and compare the output:

```text
cd typescript
pnpm tsx ./m1/m1.2_scratch_agent.ts
```

This also works with open-source models; no code changes required, just a different model line in `models.ts`.

**Why use an open-source model?**

- **Privacy:** data never leaves your machine when running locally (using a local runtime such as Ollama); useful for sensitive or proprietary content
- **Cost:** no per-token charges when self-hosted; many hosted options are free or significantly cheaper than proprietary APIs
- **No vendor lock-in:** swap between different providers and models (e.g. Llama, Mistral, Qwen) with a single line change
- **Customization:** open weights mean you can fine-tune the model on your own data

**Try an open-source model via OpenRouter**

OpenRouter gives you access to free hosted open-source models with no extra install. If you added your `OPENROUTER_API_KEY` to `.env` during setup, just uncomment the OpenRouter lines in `models.ts` and run the lab again. If you haven’t added it yet, head back to the [setup lesson](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m0/m0.1-setup-typescript.html) to add it to your `.env` file.

Model used in this course: [nvidia/nemotron-3-ultra-550b-a55b:free on OpenRouter](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free)

**Note:** Free models on hosted platforms typically mean you are consenting to the provider using your prompts and completions as training data. Avoid sending sensitive or proprietary information through free-tier endpoints.

Open-Source (Nvidia) Setup

[Public video walkthrough](../../../../../videos/O1Vjox9ay96.md)

Here are two real responses to “What is an LLM?”, one from each model:

claude-haiku-4-5

An LLM (Large Language Model) is a type of artificial intelligence system trained on vast amounts of text data to predict and generate human language.

**Key characteristics:**

- **Scale**: Contains billions to hundreds of billions of parameters (learnable weights), which is why they’re “large”
- **Training**: Learns patterns from massive text datasets using transformer-based neural networks
- **Capability**: Can perform tasks like answering questions, writing, summarizing, translating, coding, and reasoning
- **Generative**: Produces text one word (or “token”) at a time, based on patterns learned during training
- **Context-aware**: Maintains understanding of conversation history and context within a session

**Common examples**: ChatGPT, Claude, Gemini, Llama, and Mistral are all LLMs.

LLMs don’t truly “understand” in the human sense; they’re sophisticated pattern-matching systems that are remarkably effective at tasks requiring language comprehension and generation.


nvidia/nemotron-3-ultra-550b-a55b

An **LLM (Large Language Model)** is a type of artificial intelligence model trained on vast amounts of text data to understand and generate human-like language.

**Key characteristics:**

- **Scale**: Billions to trillions of parameters (e.g., GPT-4, Claude, Llama)
- **Training**: Self-supervised learning on diverse text corpora (books, websites, code, etc.)
- **Architecture**: Typically based on the Transformer architecture with attention mechanisms
- **Capabilities**: Text generation, summarization, translation, coding, reasoning, question answering

**How it works:** LLMs predict the next token (word/character) in a sequence based on context. Through massive training, they learn patterns, facts, reasoning, and linguistic structures.

**Limitations:** They can hallucinate (generate false information), lack true understanding, have knowledge cutoffs, and can be biased by training data.

---

<a id="ollama-run-a-model-locally-1"></a>


### Ollama: run a model locally

**[NO API KEY NEEDED]**

Ollama is a tool for downloading and running open-source models directly on your machine. No API key, no data sent to a third party: the model runs entirely on your hardware.

Open-Source (Ollama) Setup

[Public video walkthrough](../../../../../videos/5t0FLKmmD7h.md)

**Step 1: Install Ollama** from [ollama.com](https://ollama.com)

**Step 2: Pull a model:**

```text
ollama pull qwen2.5:7b
```

**Step 3: Update `typescript/models.ts`.** Comment out the active line and uncomment the Ollama line:

```text
// export const model = await initChatModel("anthropic:claude-haiku-4-5");
export const model = await initChatModel("ollama:qwen2.5:7b");
```

**Step 4: Run the lab as normal.** No other code changes needed.

The agent code and system prompt are identical. Only the model line in `models.ts` is different.

> **Local only.** Ollama also offers hosted cloud models at ollama.com, which do require an API key. These steps are for running a model locally on your own machine.

**Heads up: small or older local models can struggle with deep agents**

Deep agent workflows lean hard on reliable tool calling and system-prompt adherence. Tiny local models are best suited to lightweight tasks like summarization, and tend to struggle with agentic work like this.

- Consumer hardware generally can’t run frontier-capable open models locally, which is part of why Ollama itself sells [hosted cloud models](https://ollama.com/cloud) for the larger ones.
- Open-weight models have improved dramatically in recent releases, so if yours ignores your system prompt, skips tool calls, or loops, that’s likely a model-capability limit (not a bug in your setup).
- Hardware permitting, pull a newer, larger model instead (check what your machine can handle before pulling one):
  - 7B models: ~8GB RAM
  - 14B models: ~16GB RAM
  - 32B models: ~24GB+ RAM
  - 70B-class models (e.g. Llama 3.3 70B): ~64GB RAM
- Otherwise, use the **OpenRouter** option above for a larger open-weight model without the local hardware requirement.

```javascript

(function () {
  var tabs = document.querySelectorAll('.lt-tab');
  function show(p) {
    tabs.forEach(function (t) {
      var on = t.getAttribute('data-p') === p;
      t.classList.toggle('active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    document.querySelectorAll('.lt-panel').forEach(function (panel) {
      panel.classList.toggle('active', panel.id === 'p-' + p);
    });
  }
  tabs.forEach(function (t) {
    t.addEventListener('click', function () { show(t.getAttribute('data-p')); });
  });
})();

```
