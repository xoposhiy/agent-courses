# Docent

[Course index](../../README.md) · [Original source](https://transluce.org/docent) · [Raw file](../../raw/optional-readings/ref-5f2e04db952a.html)

Retrieved: 2026-11-13T16:57:30.712276+00:00

[TransluceTransluceTransluceTransluceTransluceTransluceTransluce](https://transluce.org/)

Search posts`⌘K`[Careers](https://jobs.gem.com/transluce)Menu

# Precisely understand complex AI behaviors

Docent helps analyze AI agent transcripts by turning **anecdotes and intuitions** into reliable, traceable **measurements**.

Use Docent to perform safety evaluations, monitor RL jobs, or iterate on production agents.

Try DocentDocs

![The Docent homepage](../../raw/assets/7d2444a5eac15f7d.png)

## How Docent works

### 1. Ingest your data

To ingest your data, use our Python **tracing library** which hooks your LLM API calls directly, upload files directly with our native **[Inspect](https://github.com/UKGovernmentBEIS/inspect_ai)** integration, or write a **custom ingestion** script with our SDK.

Docent supports any text-only, single or multi-agent transcript.

```
from docent.trace import agent_run, initialize_tracing

initialize_tracing("my-collection")

@agent_run
def analyze_document(document_text: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{
            "role": "user",
            "content": f"Analyze this document: {document_text}"
        }]
    )
    return response.choices[0].message.content
```

### 2. Create a rubric

Ask any question about your agent, such as "where is it reward hacking?" or "why did it fail?"

Docent first converts it into a precise **behavior rubric** by reading through your data, asking questions about ambiguities, and suggesting concrete re-writes based on your feedback.

### 3. Spot-check qualitative results

Docent then searches for agent behaviors that match your rubric. You can click on each result to see **where** it was found in each transcript, as well as an explanation of **why** it matched.

### 4. Quantify and visualize

Finally, visualize quantitative patterns by **aggregating, slicing, and filtering** using Docent's charts. For example, you can plot the number of reward hacks across training steps, or compare the prevalence of reward hacking between different models.

## Use cases

Select an example use case to understand how Docent helps.

Detect eval awarenessFind environment issuesFind surprising behaviors

AgentHarm is a benchmark that evaluates whether agents comply with harmful instructions.

1

### Search for eval awareness

Using Docent, we find that the agent frequently suggests that it is in an evaluation environment, which may affect behavior.

2

### Compare across models

## Get started in minutes

Choose a path that fits your workflow—no heavy setup required.

[Read the full setup guide in our docs](https://docs.transluce.org/introduction)

1

### Python tracing library

Instrument any Python project with a tiny tracing helper and stream rich events into Docent.

2

### Inspect auto-ingestion

3

### Custom transcript converter

Python tracing library

Instrument any Python project with a tiny tracing helper and stream rich events into Docent.

```
from docent.trace import agent_run, initialize_tracing

initialize_tracing("my-collection")

@agent_run
def analyze_document(document_text: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"Analyze this document: {document_text}"
            }
        ]
    )
    return response.choices[0].message.content
```

Works alongside your existing stack (OpenAI, Anthropic, vLLM, LangChain, custom scaffolds, etc.).

![AI Technology Illustration](../../raw/assets/95dbc148aef8b6eb.png)![Overlay](../../raw/assets/363c5a60b8286083.png)

## What you can understand, you can improve

[Try Docent](https://docent.transluce.org)[Book a call](https://calendly.com/kevin-transluce/30min)
