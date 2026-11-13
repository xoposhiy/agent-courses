# Homework 2 bundle: vendor/aos/docs/CONFIGURATION.md

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/docs/CONFIGURATION.md) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/docs/CONFIGURATION.md)

Retrieved: 2026-11-13T17:00:50.402745+00:00

# Configuration

All configuration is environment variables. `aos` loads `AOS/.env` (the file next to
`pyproject.toml`) and then a `.env` in the current directory, never overriding variables already set
in the shell. Start from [.env.example](../-env-example.md):

```bash
cp -n .env.example .env     # -n: never overwrite an existing .env
```

AOS refuses to run with the placeholder values (`your-key`, `your-...`) and the setup script warns
when it finds them.

## Variables

| variable | required | default | used by |
|---|---|---|---|
| `API_KEY` | yes | – | every LLM call; passed to the external systems as `API_KEY` and `OPENAI_API_KEY` |
| `BASE_URL` | yes | – | the OpenAI-compatible endpoint (the lab proxy serving Gemini); passed on as `BASE_URL` and `OPENAI_BASE_URL` |
| `AOS_MODEL` | no | `gemini-3.6-flash` | the planner, file summaries, coding agent, assistant, natural-language SQL, and the model every external runner uses |
| `SERPER_API_KEY` | for storm, datastorm, grill | – | web search (Serper). Workers that need it report themselves unavailable without it |
| `AOS_PRICES` | no | table in [aos/llm.py](../aos/llm-py.md) | cost estimates: JSON `{"model": [input_usd_per_1M, output_usd_per_1M]}`, merged over the defaults |
| `AOS_WORKERS` | no | – | your own workers, comma-separated `path/to/file.py:Class` or `module:Class` entries, added to (or, by name, replacing) the built-in ones; see [CUSTOM_WORKERS.md](CUSTOM_WORKERS-md.md) |
| `AOS_GRILL_VERIFY` | no | `light` | GRILL stage-2 verification: `light`, `deep` or `off` (see [WORKERS.md](WORKERS-md.md)) |
| `AOS_GRILL_SCREEN` | no | `1` | `0`/`false`/`no`/`off` skips GRILL's stage-1 screen |
| `AOS_EXTERNAL_DIR` | no | `AOS/external` | where the external repositories and their virtualenvs live (also read by `scripts/setup_external.sh`) |
| `AOS_MAX_FILE_CHARS` | no | `2000000` | how many characters of a text file the web UI sends at once |
| `AOS_LIVE` | no | unset | `1` runs the live tests that call the real endpoint |

Variables the runners and tools read inside their own processes (set by AOS, listed for debugging):

| variable | set by | meaning |
|---|---|---|
| `OPENAI_API_KEY`, `OPENAI_BASE_URL` | the wrapper's `env()` | what the OpenAI SDK and the systems' own clients read |
| `PYTHONUNBUFFERED=1` | wrapper | so runner output streams into the step log line by line |
| `LD_LIBRARY_PATH` | wrapper | the caller's value with NVIDIA HPC SDK directories removed (their `libgomp` shadows the one bundled with torch) |
| `AOS_PRICES` | wrapper | the merged price table, so GRILL's budget uses the same rates |
| `STORM_FETCH_DIR` | run_storm.py, run_datastorm.py | where the patched STORM/DataSTORM archive every search hit and fetched page |
| `AOS_SEARCH_LOG_DIR` | run_grill.py | where `web_search.py` saves queries and fetched pages (default `./searches`) |
| `SERPER_ENDPOINT` | you, optionally | alternative Serper endpoint for `web_search.py` (default `https://google.serper.dev`) |

## Models and the proxy

The proxy serves Gemini models under the OpenAI chat, responses, tool-calling and JSON-mode APIs.
Facts that shape how AOS calls it:

- **No embeddings model.** GRILL's embedder is replaced in-process by a hashed character-trigram
  embedder (only used to rank its frontier); SLIDERS falls back to its offline embedder.
- **Reasoning tokens count against `max_tokens`.** AOS never sets `max_tokens`; a low cap returns
  an empty reply. The STORM runner sends `reasoning_effort=none` with generous caps for its short
  calls.
- **Thinking tokens are billed as output.** The proxy reports them inside `completion_tokens`;
  AOS records their share separately (`reasoning_tokens`) and prices all output at the output rate.
- **No published prices.** Costs are estimates. Defaults (USD per million tokens, input/output):
  `gemini-3.6-flash` 0.30/2.50, `gemini-3.5-flash` 0.30/2.50, `gemini-3.5-flash-lite` 0.10/0.40,
  `gemini-3.1-pro-preview` 1.25/10.00. Override or extend with `AOS_PRICES`; calls to a model
  without a price are counted as `unpriced_calls`.

`aos ... --model NAME` overrides `AOS_MODEL` for one invocation. In the web UI the status bar lists
the models the key can use (`GET /api/models`); switching applies to every later call in that server
process, including the external systems, because the server sets `AOS_MODEL` in its own environment.

## Budget cap

Each workspace can carry a cap in estimated USD, stored as `setting.budget_usd` in the catalog's
`workspace` table and set from the UI's settings (gear) or through `POST /api/settings`. The CLI and
the server both enforce it: once tasks' recorded usage (plus, in the UI, the session's assistant and
summary calls) reaches the cap, new runs are refused and a running task stops before its next step
with status `stopped`. A single long step can overshoot, because the check runs between steps.
Questions to the assistant are never blocked. Clear the cap by saving an empty value.

## Timeouts and limits

| what | value | where |
|---|---|---|
| steps per run | 12 | `--max-steps` on `aos run`/`aos ui` |
| planner retries on an invalid decision | 3 | `Orchestrator.decide` |
| coding agent turns per step | 40 | `CodingAgent(max_turns=...)` |
| coding agent shell command | 600 s | `CodingAgent(shell_timeout=...)`, also the per-call cap |
| assistant turns per question | 12 | `Assistant(max_turns=...)` |
| GRILL runner | 4 h | `aos/capabilities/grill.py` |
| STORM, SLIDERS, DataSTORM runners | 3 h | their wrappers |
| HistoryGenie runner | 2 h | its wrapper |
| LLM request | 600 s, 3 retries | `LLM.__init__` |
| files summarized per step | 25 | `MAX_SUMMARIZED_FILES` |
| characters of a file shown to the summarizer | 1,500 | `HEAD_CHARS` |
| tool output returned to the coding agent | 12,000 chars | `MAX_TOOL_OUTPUT` |
| catalog rows returned by the UI's SQL box | 500 | `MAX_SQL_ROWS` |

These are constants in the code rather than settings; change them there if a deployment needs to.
