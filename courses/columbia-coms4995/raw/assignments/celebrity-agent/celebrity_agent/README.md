# HW3 Agent Skeleton

In this homework, you will build a conversational agent with:

- a memory store (ingest, index, retrieve)
- a content module (grounded content planning)
- a style module (voice transformation)
- guardrails (decline questions the celebrity would not know about)
- a conversation store (start, list, and continue conversations)
- a web app (backend server and frontend) for user interaction

## Project layout

```text
celebrity_agent/
  README.md
  requirements.txt
  data/
    sample_sources.json
    sample_index.json
  src/
    llm.py
    memory_store.py
    content_module.py
    style_module.py
    guardrails.py
    conversations.py
    agent.py
  frontend/        <- you add this
```

## Getting started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your Gemini API key as an environment variable. Get a key at
https://ai.google.dev/gemini-api/docs/api-key.

```bash
export GEMINI_API_KEY="your_api_key_here"
```

3. Implement `build_memory_store()` in `src/memory_store.py`, then run:

```bash
python -m src.memory_store
```

4. Implement the remaining modules, then build your backend and frontend.

## Launching your celebrity agent

Replace this section with the commands to install and launch your app.

## Notes

- `sample_sources.json` contains example source objects.
- `sample_index.json` contains an example memory index format.
- This starter code is intentionally simple. Feel free to add any needed files or functions (e.g., embeddings, prompting files, databases).
