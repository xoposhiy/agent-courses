# Homework 2 bundle: vendor/aos/.env.example

[Course index](../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/.env.example) · [Raw file](../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/.env.example)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```example
# Gemini through the lab's OpenAI-compatible proxy
API_KEY=your-key
BASE_URL=https://azureopenai.genie.stanford.edu/v1/
# default model for the planner, the coding agent and every wrapped system
AOS_MODEL=gemini-3.6-flash
# web search for STORM and DataSTORM
SERPER_API_KEY=your-serper-key
# optional: USD per 1M tokens as [input, output]; unlisted models use the defaults in aos/llm.py
# AOS_PRICES={"gemini-3.6-flash": [0.30, 2.50], "gemini-3.1-pro-preview": [1.25, 10.00]}
# optional: your own workers, comma-separated path/to/file.py:Class or module:Class (docs/CUSTOM_WORKERS.md)
# AOS_WORKERS=examples/workers/glossary.py:Glossary

```
