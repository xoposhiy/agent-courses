# Homework 2 bundle: vendor/aos/docs/WORKERS.md

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/docs/WORKERS.md) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/docs/WORKERS.md)

Retrieved: 2026-11-13T17:00:50.402745+00:00

# Workers

A worker is what AOS hands a step to. Each reads its instructions and its input files and writes
files; the orchestrator discovers the outputs by diffing the workspace, catalogs them and commits.
Workers never call each other. `aos workers` lists them with their availability on this machine.

| worker | kind | repo under `external/` | needs beyond `API_KEY`/`BASE_URL` | typical duration |
|---|---|---|---|---|
| `coding_agent` | built in | – | – | seconds to minutes |
| `storm` | subprocess | `storm` | `SERPER_API_KEY` | 5–15 min |
| `grill` | subprocess | `graph-search-sliders` | `SERPER_API_KEY`, `codex` on PATH | tens of minutes |
| `sliders` | subprocess | `sliders-new` | – | minutes |
| `datastorm` | subprocess | `datastorm` | `SERPER_API_KEY` | 10–30 min |
| `historygenie` | subprocess | `historygenie` | – | minutes |
| `satir`, `verdict` | subprocess | `trial-forma` | SNOMED CT/UMLS licenses, Elasticsearch + Snowstorm, compiled `build/` | not runnable here |

The planner only sees available workers. Each worker's `description` string in its wrapper is what
the planner reads to choose it and to phrase `instructions`, `inputs` and `output_dir`, so those
strings are the authoritative contract; this page restates them with the operational detail.

## How external systems are run

Each system is a repository cloned under `external/<repo>` with its own virtualenv, built by
scripts/setup_external.sh (source archive omits `../scripts/setup_external.sh`). AOS never imports its code. A wrapper in
[aos/capabilities/](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/capabilities) builds one command line:

```
external/<repo>/.venv/bin/python  <workspace>/code/adapters/run_<system>.py  --<args> ...
```

executed with the repo as working directory, a 2 to 4 hour timeout, and an environment carrying
`API_KEY`, `BASE_URL`, `AOS_MODEL`, their OpenAI-style aliases, `AOS_PRICES`, `PYTHONUNBUFFERED=1`
and a cleaned `LD_LIBRARY_PATH` (see [CONFIGURATION.md](CONFIGURATION-md.md)). Output streams into the
step log as it is written. On a non-zero exit the step fails with the last 3,000 characters of
output; on timeout the whole process group is killed.

Every runner leaves a `usage.json` (`model`, `calls`, `input_tokens`, `output_tokens`, `cost_usd`)
in its output directory, which the wrapper attaches to the step for cost accounting.

### Adapters in the workspace

`aos init` copies every runner (`run_*.py`) and `web_search.py` into the workspace as
`code/adapters/…`, cataloged with source `aos` and a tag `adapter-sha:<hash>`. The wrappers run the
workspace's copy when it exists. This is deliberate: when an integration breaks mid-task, the planner
can send the coding agent to read the step log, fix the adapter in the workspace, test it, and the
fix is committed like any other change and undone by a rollback. Before each external step AOS
refreshes copies that nobody edited when its own version has moved on, and leaves edited copies
alone (the catalog knows: source no longer `aos`, or the on-disk hash differs from the installed
one).

## coding_agent

[aos/coding_agent.py](../aos/coding_agent-py.md). A tool-calling loop on the configured model, up to 40
turns, running inside the AOS process.

- **instructions**: what to do and what to produce. **inputs**: files it must read. **output_dir**:
  where new files go (it is also told to put reusable scripts under `code/scripts/`).
- **Tools**: `query_metadata` (read-only SQL over the catalog), `list_files`, `read_file`
  (paged, 300 lines by default), `write_file`, `replace_in_file` (one exact, unique match),
  `run_shell` (bash with the workspace root as working directory, 600 s cap; `python` is the AOS
  virtualenv with `openai` and `pandas`, and `API_KEY`/`BASE_URL`/`AOS_MODEL` are in its
  environment).
- **Confinement**: every path resolves inside the workspace; writes to `workspace.db`, `tasks/` and
  `.git/` are refused; it is told not to run git (AOS commits) and to verify its outputs before
  finishing.
- **Context**: the overall goal, the step's instructions, inputs and output directory, and the
  workspace listing with provenance. Its system prompt tells it to start with `query_metadata`.
- **Output**: its final message is the step summary; the step log holds every tool call and result.
  If it exhausts its turns it is asked for a summary and the step is marked with "turn limit".

Use it for inspection, transformations, format conversion, joining outputs of other workers,
writing decisions or notes from workspace files, debugging failed steps and fixing adapters. In the
first use case it also covered the criteria-based decision step that VERDICT could not.

## storm

[aos/capabilities/storm.py](../aos/capabilities/storm-py.md), runner `run_storm.py`. Broad research for
a general audience: STORM (`knowledge-storm`) runs perspective-guided conversations against web
search, writes an outline and a Wikipedia-style article with numbered citations.

- **instructions**: the topic or question, with the aspects to cover. **inputs**: ignored. Use a
  fresh `output_dir` per topic.
- **Outputs** in `output_dir`: `report.md` (the polished article), `url_to_info.json` (cited sources
  with snippets), `raw_search_results.json`, `storm_gen_outline.txt`, `direct_gen_outline.txt`,
  `conversation_log.json`, `storm_gen_article.txt`, `storm_gen_article_polished.txt`,
  `llm_call_history.jsonl`, `run_config.json`, `usage.json`. Every search hit and fetched page is
  archived under `sources/webpages/<output_dir name>/` as `results/<key>.json`, `pages/<key>.html`
  and `pages/<key>.txt` by the `FetchArchive` hook that `patches/storm-fetch-archive.patch` adds.
- **Runner arguments**: `--topic`, `--output-dir`, `--sources-dir`, `--max-conv-turn 3`,
  `--max-perspective 3`, `--search-top-k 3`, `--max-thread-num 3`.
- **Model setup**: the model is used through LiteLLM as `openai/<AOS_MODEL>` with
  `reasoning_effort=none` and caps of 4,000 to 16,000 tokens, because reasoning tokens count
  against `max_tokens` on this endpoint. Retrieval is Serper with full-page fetching.
- **Fails** when no `report.md` is produced.

## grill

[aos/capabilities/grill.py](../aos/capabilities/grill-py.md), runner `run_grill.py`. Academic deep
research with source-verified claims: GRILL (`graph-search-sliders`, the belief-ledger research
agent) explores research directions, proposes hypotheses and tests each against sources it retrieves,
then writes a ranked, cited report. Its research tasks run as Codex sessions, so the `codex` CLI must
be on PATH.

- **instructions**: one well-posed research question, saying which aspects matter. **inputs**:
  ignored.
- **Outputs** in `output_dir`: `report.md` (findings with a Sources section), `sources.csv` (every
  evidence item with DOI/PMID/URL and quote), `findings.csv`, `metrics.csv` (every number reported
  by a source), `usage.json` (with the spend GRILL tracked), and `grill_run/`: `ledger.json`,
  `run.json`, `artifacts.json`, `orchestrator.log`, `steer.log`, `tasks/` (per-task prompts,
  transcripts and answers), `workspace/` (GRILL's own data, with its nested `.git` removed) and
  `searches/` (every `search-*.json` and `scholar-*.json` query, and `pages/` with fetched pages).
- **Runner arguments**: `--question`, `--output-dir`, `--tools` (path of `web_search.py`),
  `--budget 12.0` (USD), `--max-rounds 6`, `--batch 3`, `--concurrency 3`, `--reasoning low`,
  `--task-timeout 1200`, `--verify light|deep|off`, `--no-screen`.
- **Adaptations applied in-process** (the repo itself is untouched): the embedder is replaced by a
  hashed character-trigram embedder because the proxy has no embeddings model; the configured model
  is added to GRILL's USD rate table from `AOS_PRICES`; Codex is pointed at `BASE_URL`; and since
  Codex's built-in web search is inert through the proxy, every research prompt is prefixed with
  instructions to run `web_search.py` from the sandbox shell, whose run directory is made writable.
- **Verification modes** (`AOS_GRILL_VERIFY`, default `light`): GRILL screens each hypothesis
  cheaply (stage 1), then verifies it (stage 2). GRILL's own stage 2 is an adversarial hunt for
  counter-evidence that dominates run time. `light` keeps stage 2 with the same verdicts but as a
  focused check of the one to three sources the agent reads plus one deliberate search for
  contradicting evidence (a single targeted look, not the open-ended hunt), with a smaller per-task cap
  ($0.80 instead of $2.00). `deep` restores GRILL's test. `off` skips stage 2 (GRILL's no-verifier
  ablation, leaving pooled claims marked untested). `AOS_GRILL_SCREEN=0` drops stage 1 so every
  hypothesis goes straight to verification: fewer Codex tasks, but verification rates paid for
  hypotheses the screen would have binned.
- **Fails** when no `report.md` is produced.

Routing rule the planner is given: academic, scientific, medical or technical questions where
evidence quality matters go to `grill`; broad general-audience overviews go to `storm`.

### web_search.py

[aos/capabilities/runners/web_search.py](../aos/capabilities/runners/web_search-py.md) is the search
tool the GRILL agents run inside their sandbox. Standard library only and Python 3.8 compatible so it
works with whatever `python3` the sandbox has:

```
python3 web_search.py search "query" [--num 10]     # Google web results via Serper
python3 web_search.py search "query" --scholar      # Google Scholar results
python3 web_search.py fetch URL [--max-chars 30000] # readable text of a page or PDF
```

It reads `SERPER_API_KEY`, saves every query and fetched page under `AOS_SEARCH_LOG_DIR` (the run's
`searches/` folder), and answers repeated queries and fetches from that folder. It is the reason
GRILL needs `SERPER_API_KEY`. Agent tools like this one live in the sandbox as scripts, not as tool
servers.

## sliders

[aos/capabilities/sliders.py](../aos/capabilities/sliders-py.md), runner `run_sliders.py`. SLIDERS
(`sliders-new`) turns text documents into a structured table whose schema is chosen for the
question, with every cell backed by a quote and a `file:line` locator, then answers the question over
that table.

- **instructions**: the question, or what to extract ("List the clinical features, symptoms, genetic
  cause, diagnostic tests and treatments of X as a table"). **inputs** (required): `.md`, `.txt`,
  `.markdown`, `.rst` or `.text` files, or directories of them. PDFs and images are not accepted;
  transcribe them with `historygenie` first.
- **Outputs** in `output_dir`: `tables/<Table>.csv` per extracted table, `evidence.csv` (table,
  row, field, value, quote, document, path, start and end line, quote_verified), `table.json`,
  `answer.md` and `answer.json` (grounded answer with citations; `answer.md` notes when the table did
  not support the answer), `trace.json`, `usage.json`, and the hidden `.sliders/` table store.
- **Runner arguments**: `--docs`, `--question`, `--output-dir`.
- **Model setup**: every model role in SLIDERS' config is set to `AOS_MODEL` through the proxy;
  SLIDERS silently falls back to its offline embedder.
- **Fails** when no input is given or no table is produced.

## datastorm

[aos/capabilities/datastorm.py](../aos/capabilities/datastorm-py.md), runner `run_datastorm.py`.
DataSTORM explores a database by an LLM-driven tree search of questions answered with SQL and writes
an analyst-style report whose claims cite the queries behind them.

- **instructions**: the research question or topic to investigate in the data. **inputs**
  (required): one SQLite database (`.db`, `.sqlite`, `.sqlite3`) or one or more CSV files (each
  becomes a table in a new `data.sqlite`).
- **Outputs** in `output_dir`: `report.md`, `staged_report_*.json`, `tree.json` (the explored
  question tree with answers), `sql_results/*.csv`, the SQLite database used, `usage.json`, and the
  hidden `.domains/` (the generated DataTalk domain description) and `.debug_rm.log`. Web pages it
  fetches are archived under `sources/webpages/<output_dir name>/` like STORM's.
- **Runner arguments**: `--topic`, `--output-dir`, `--inputs`, `--sources-dir`,
  `--db-description`, `--first-level-questions 3`, `--max-tree-depth 3`, `--population 2`,
  `--max-global-insights 10`, `--expansion-max-questions 2`. A tree shallower than depth 3 skips
  the thesis stage.
- **Model setup**: the repo hard-codes `gpt-5` in several places; the runner routes every LangChain
  client to `AOS_MODEL` and counts tokens with a callback.
- **Fails** when no `report.md` is produced.

## historygenie

[aos/capabilities/historygenie.py](../aos/capabilities/historygenie-py.md), runner
`run_historygenie.py`. Transcribes image-based documents into markdown with HistoryGenie's
vision-LLM OCR, preserving headings and tables.

- **instructions**: ignored (fixed transcription prompt). **inputs** (required): PDFs or images
  (`.png`, `.jpg`, `.jpeg`, `.webp`, `.tif`, `.tiff`, `.bmp`), or directories of them.
- **Outputs** in `output_dir`: one `<document name>.md` per input with one section per page, and
  `usage.json`.
- **Runner arguments**: `--inputs`, `--output-dir`, `--dpi 200`.
- **Model setup**: only `engine/ocr/llm_ocr.py` is imported from the repo (the full engine pulls in
  cloud dependencies); pages are rendered with PyMuPDF and sent to `AOS_MODEL` through LiteLLM.
- **Fails** when no markdown is produced. Use it first when documents are scans, then hand the
  markdown to `sliders` or `coding_agent`.

## satir and verdict

[aos/capabilities/forma.py](../aos/capabilities/forma-py.md). Both belong to FORMA (`trial-forma`), a
clinical-trial formal-reasoning pipeline:

- **SatIR**: high-recall retrieval of clinical trials for a patient from FORMA's relational
  projection of compiled criteria (SQL over ontology-closed concept sets). instructions = the patient
  id; inputs = the compiled trial database (`build/trial.db`).
- **VERDICT**: eligibility decisions of a patient against trial criteria compiled to SMT (z3), with
  unsat-core rationales. instructions = trial id and patient id; inputs = the patient note JSON and
  the compiled programs (`build/noslice_ir_linked`).

Running them needs licensed ontologies (SNOMED CT, UMLS), Elasticsearch 7.17 with Snowstorm, and
FORMA's offline compile steps. None of that is in the checkout, so both report themselves
unavailable with that reason, `aos workers` says so, and the planner never sees them. Retrieval and
criteria-based decisions are routed to `coding_agent` instead.

## Writing instructions that work

- Instructions are the only thing a worker knows besides its inputs and the workspace listing. Make
  them self-contained: name the entity, the aspects wanted, and the output format or path.
- Inputs must exist; the planner's decision is rejected otherwise. For `sliders`, `datastorm` and
  `historygenie` they are required; `storm` and `grill` ignore them.
- Put each research run in its own `output_dir` (`generated/research/<topic>`); STORM and DataSTORM
  key their source archives by that directory name.
- After a failed external step, read `tasks/task-NNN/step-NN.log`: it holds the runner's command
  line and full output.
