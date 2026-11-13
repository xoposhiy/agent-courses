# Development

## Setup

```bash
uv sync --group dev                 # Python 3.12 virtualenv in .venv with aos, openai, pandas, python-dotenv, pytest
uv sync --group dev --group notebook  # plus Jupyter, for examples/cs224v/
cp -n .env.example .env             # then put the real API_KEY, BASE_URL and SERPER_API_KEY in it
scripts/setup_external.sh all       # clone the external systems into external/ and build their virtualenvs
.venv/bin/aos workers               # confirm which workers can run here
```

Requirements on the machine: `uv`, `git`, SSH access to the `stanford-oval` GitHub organisation
(the setup script clones with `git@github.com:stanford-oval/...`), and for GRILL the `codex` CLI
(`npm i -g @openai/codex`). The Python interpreters the external systems need (3.11 and 3.12) are
fetched by `uv` on demand.

`scripts/setup_external.sh` takes one system name or `all`. Per system it clones (if absent), applies
AOS's patch when there is one, creates `external/<repo>/.venv` with the right Python version and
installs the system:

| repo | python | notes |
|---|---|---|
| `storm` | 3.11 | CPU torch; the unpinned requirements resolve to an incompatible transformers stack, so `transformers==4.47.1`, `sentence-transformers==3.3.1` and `huggingface_hub<1.0` are pinned; `torchvision` removed; patched with `patches/storm-fetch-archive.patch` |
| `sliders-new` | 3.11 | installed as `-e .[canon]` |
| `datastorm` | 3.11 | CPU torch, `tabulate`; patched with `patches/datastorm-fetch-archive.patch` |
| `historygenie` | 3.12 | only `common/core` plus `pymupdf` and `pillow` |
| `graph-search-sliders` (GRILL) | 3.12 | `openai`; runs the repo's `src.selftest`; warns if `codex` is missing |
| `trial-forma` (SatIR, VERDICT) | – | cloned only; needs SNOMED CT and UMLS licenses, Elasticsearch 7.17 and Snowstorm (see the repo's `snowstrom_setup.md`) |

The script is idempotent: an existing clone or virtualenv is reused and an already applied patch is
detected. `AOS_EXTERNAL_DIR` relocates `external/`.

## Tests

```bash
.venv/bin/python -m pytest -q                      # unit tests: fast, no network (127 tests)
AOS_LIVE=1 .venv/bin/python -m pytest -q -m live   # 4 live tests against the proxy (a few minutes)
```

Unit tests use `FakeLLM` from [tests/conftest.py](../tests/conftest.py): a scripted stand-in whose
replies are strings (text), dicts (JSON) or lists of `(tool_name, arguments)` pairs (tool calls), and
which counts tokens so cost accounting can be asserted. The `ws` fixture creates a fresh workspace in
a temp directory. Wrapper tests replace the runner with a fake script, so no external system is
needed. Tests marked `live` are skipped unless `AOS_LIVE=1`.

| file | covers |
|---|---|
| `test_workspace.py` | folders, path confinement, catalog register/describe/query, snapshots, pruning, checkpoint, rollback, edited-file detection, settings, legacy migration |
| `test_tasks.py` | task ids, step records, summary text |
| `test_orchestrator.py` | the full loop with a scripted planner, failures and retries, invalid decisions, step limit, rollback action, workflow replay, user files mid-step and between decisions, usage and budget, adapter refresh, mixed files |
| `test_coding_agent.py` | the tool loop, escape and protected-file refusals, unique-match replace, error returns, turn limit, catalog queries |
| `test_assistant.py` | read-only tools, conversation memory, turn limit |
| `test_capabilities.py` | availability reasons, registry, `AOS_WORKERS` loading, the example glossary worker, adapter installation and refresh, each wrapper's command line and output checks, environment cleanup, workspace adapter precedence |
| `test_trace.py` | the LLM call trace: per-thread contexts, one record per call with delta messages, tokens, cost and errors, tagging by the orchestrator, `aos trace` |
| `test_runners.py` | runner helpers: DataSTORM domain folder, input collection, GRILL tool injection, verification modes, screen skipping, local embedding |
| `test_web_search_tool.py` | the search tool: normalization, caching, fetching, error messages, running on the system python |
| `test_worker.py` | `run_command`: live log streaming, failure tail, timeout kill, stdin |
| `test_llm.py` | JSON parsing, prices, usage recording, placeholder rejection; live completion and tool call |
| `test_api.py` | the Python interface: create/open, add (files and folders), step, run, ask, query, trace, budget, workflows, rollback, lazy credentials |
| `test_cli.py` | init, status, describe, log, rollback, workflow-save, workers, query, add, step |
| `test_ui.py` | every endpoint through `App`/`Hub` and the HTTP server, background runs, interrupted tasks, database tab, budget, models |
| `test_prompts.py` | the prompt files under `aos/prompts/`: each is loaded by a module and formats with its placeholders |
| `test_plan_coverage.py` | keeps [PLAN_COVERAGE.md](PLAN_COVERAGE.md) honest: every PLAN.md section has an entry, every referenced file and test function exists |

## Adding a worker

[CUSTOM_WORKERS.md](CUSTOM_WORKERS.md) is the user-facing guide, with a complete in-process example
([examples/workers/glossary.py](../examples/workers/glossary.py)) and the `AOS_WORKERS` variable that
loads a worker without editing AOS. The steps below make a subprocess worker part of AOS itself:

1. **Write a runner** in `aos/capabilities/runners/run_<system>.py`. It runs with the system's own
   Python, takes instructions and paths as arguments (`--output-dir` at least), reads `API_KEY`,
   `BASE_URL` and `AOS_MODEL` from the environment, writes its files under the output directory, and
   leaves a `usage.json` there (`model`, `calls`, `input_tokens`, `output_tokens`, `cost_usd`; any
   may be null). Print progress to stdout: it streams into the step log.
2. **Write a wrapper** in `aos/capabilities/<system>.py` subclassing `ExternalCapability`: set
   `name`, `repo` (folder under `external/`), `required_env`, and a `description` that tells the
   planner precisely what `instructions` and `inputs` mean and which files come out. In `run`, build
   the command with `self.python` and `self.runner(ws, "run_<system>.py")`, call `run_command`
   with a timeout, call `self.report_usage(out)`, check the expected artifact exists and raise
   `StepFailed` otherwise, and return a one-line summary.
3. **Register it** in `aos/capabilities/__init__.py` (`all_workers`), or leave it out of AOS and
   load it with `AOS_WORKERS=path/to/wrapper.py:Class`.
4. **Add setup** to `scripts/setup_external.sh` (clone, venv, install), and a patch under `patches/`
   if the system needs source changes to keep fetched material inside the workspace.
5. **Test** the wrapper with a fake runner script (see `test_capabilities.py`) and the runner's pure
   helpers directly (see `test_runners.py`).

A worker that runs in-process (like the coding agent) only needs steps 2 and 3, subclassing `Worker`
instead. Workers must not register files or commit; the orchestrator does both.

Because `aos init` copies every `run_*.py` and `web_search.py` into the workspace's
`code/adapters/`, a new runner is picked up by existing workspaces at their next external step (the
pristine copy is refreshed automatically; an edited copy is left alone).

## Patches to external systems

`patches/storm-fetch-archive.patch` and `patches/datastorm-fetch-archive.patch` add a `FetchArchive`
class to the systems' `knowledge_storm/utils.py` and call it from the retriever and the page fetcher,
so every search hit and downloaded page is saved under `STORM_FETCH_DIR` when that variable is set.
Without the variable the hook is inert. The setup script applies them with `git apply` and detects an
already applied patch. Regenerate a patch after changing it with
`git -C external/storm diff > patches/storm-fetch-archive.patch`.

## Documentation conventions

- [PLAN.md](../PLAN.md) is the design; it is not edited to match the code.
- [PLAN_COVERAGE.md](PLAN_COVERAGE.md) maps every `##` section of PLAN.md to code and tests.
  `test_plan_coverage.py` fails when a section lacks an entry, a backticked path in it does not
  exist, or a `test_...` name it mentions is not defined. Keep paths in backticks and accurate.
- Prompts are text files under [aos/prompts/](../aos/prompts/), one per use, loaded with
  `prompts.load(name)`; `test_prompts.py` checks each file is used and formats with its placeholders.
  Runner scripts keep their prompts inline: they run in other virtualenvs and are copied into workspaces.
- Worker `description` strings are documentation the planner reads. When a runner's outputs change,
  update the description, [WORKERS.md](WORKERS.md) and the wrapper's test together.
- `API_VERSION` in `aos/ui.py` is bumped whenever the page needs a route the server did not have,
  so a stale server shows a restart banner instead of a bare "not found".

## Repository layout

```
aos/                    the package (see ARCHITECTURE.md)
aos/capabilities/       wrappers, registry, runners/
aos/static/index.html   the web page
docs/                   this documentation
examples/fabry/         the first use case: synthetic patients.csv and its README
patches/                source patches applied to external systems
scripts/setup_external.sh
tests/
external/               cloned systems and their virtualenvs (git-ignored)
workspaces/             default root for `aos ui` (git-ignored)
.env                    credentials (git-ignored); .env.example is the template
pyproject.toml, uv.lock
```
