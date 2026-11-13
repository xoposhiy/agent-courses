# Tutorial: building an agent for your own task

This walkthrough takes a task of your own from an empty folder to a finished, auditable result:
bring your documents in, add a database, pull in outside sources, run the agents, inspect what they
did, and turn the result into a repeatable workflow. Every command here works the same from the web
interface; the UI equivalents are noted along the way.

The running example is a records-review task: you have a folder of patient notes (PDF scans and
text), a spreadsheet of lab results, and you want to know which patients match a disease profile
that has to be researched first. Substitute your own documents and question; the mechanics do not
change.

Prerequisites: AOS set up as in the [README](../README.md#setup) (`uv sync`, a filled-in `.env`,
`scripts/setup_external.sh` for the systems you want) and `aos workers` showing at least
`coding_agent`, `storm`, `sliders` and `historygenie` as available.

Everything below is also available from Python through one object, `aos.api.AOS`; section 10 shows
the whole walkthrough as a script.

## 1. The mental model

AOS does not have "an agent" you configure. It has a **workspace folder** and **workers**:

- The workspace is the whole state of the task: your inputs, everything fetched, everything
  produced, the task records and a git history. Nothing lives outside it.
- A worker reads files and instructions and writes files. The built-in `coding_agent` is a
  general tool-using agent; `storm`, `grill`, `sliders`, `datastorm` and `historygenie` wrap
  specialised research systems ([WORKERS.md](WORKERS.md)); you can add your own
  ([CUSTOM_WORKERS.md](CUSTOM_WORKERS.md)).
- The **planner** (the model) looks at the goal, the workers, the files and the steps so far, and
  picks the next step. You can let it drive (`aos run`), drive yourself (`aos step`), or replay a
  recorded sequence (`aos workflow-run`).

So "building an agent to perform a task" means: give a workspace the right inputs, phrase the goal
well, and let the planner sequence the workers. When the built-in workers are not enough, you add
one.

## 2. Create the workspace

```bash
aos init workspaces/review
```

A workspace is identified by its folder name; that is all it needs. This creates the standard
folders, the `workspace.db` catalog, a git repository and copies of the runner scripts under
`code/adapters/` (so an agent can fix an integration without touching AOS). In the UI: `aos ui`,
then "New workspace".

Goals belong to runs, not to the workspace: every `aos run` carries its own, and a workspace
accumulates many over time as the questions change. The optional `--goal` on `aos init` only stores
a one-line description shown in `aos status` and the page title and mentioned to the assistant; the
planner never reads it. Leave it out, or use it as a project description.

```
workspaces/review/
  inputs/       your files
  sources/      material the workers fetch (web pages, search results)
  generated/    what the workers produce
  code/         adapter copies and any scripts an agent writes
  workflows/    saved step sequences
  tasks/        task records, step logs and the LLM call trace
  workspace.db  the catalog: one row per file with its provenance
```

## 3. Bring your documents in

Anything under `inputs/` belongs to you. There are four ways to put files there, and they all end
the same way: the file is cataloged with source `user`, gets a one-sentence model-written summary,
and is committed.

```bash
aos add workspaces/review ~/cases/notes/*.pdf --reason "scanned clinical notes, one per patient"
aos add workspaces/review ~/cases/labs.csv --reason "lab results, one row per patient and test"
cp ~/cases/discharge_summaries/*.txt workspaces/review/inputs/      # plain copy works too
```

A plain copy is cataloged at the next planning decision, so files can arrive while a run is in
progress; the planner is told about them. In the UI: the upload button, drag and drop onto the
explorer, or the folder button to copy a path from the server's machine (whole folders included).

Check what AOS understood:

```bash
aos status workspaces/review          # every file with source and summary
aos describe workspaces/review inputs/labs.csv
```

**Scans and PDFs.** `sliders` (table extraction) and the glossary-style workers read text only.
Transcribe image-based documents first with `historygenie`, which writes one markdown file per
document with a section per page:

```bash
aos step workspaces/review historygenie "" --inputs inputs/notes --output-dir generated/transcripts
```

The planner knows this rule too (it is in `historygenie`'s description), so in an `aos run` it
inserts the transcription step itself when it sees PDFs.

## 4. Add a database

There are two kinds of database in a workspace.

**Your data.** A SQLite file or CSVs in `inputs/` are data the workers can analyse:

- `datastorm` explores a database with LLM-driven question trees and writes an analyst-style
  report. It takes one `.db`/`.sqlite` file or several CSVs (each becomes a table).
- `coding_agent` can run SQL and pandas over anything: convert CSVs to SQLite, join the lab results
  with the transcripts, compute per-patient features.

```bash
aos step workspaces/review coding_agent \
  "Load inputs/labs.csv into generated/data/labs.sqlite (table labs) and write a per-patient \
   summary table generated/data/patient_labs.csv with the latest value of each test." \
  --inputs inputs/labs.csv --output-dir generated/data
aos step workspaces/review datastorm "Which lab patterns distinguish patient groups?" \
  --inputs generated/data/labs.sqlite --output-dir generated/analysis/labs
```

**The catalog.** `workspace.db` is AOS's own database: table `files` (what each file is, who made
it, in which task and step, why, a summary) and `file_inputs` (what each file was derived from).
Query it from the shell, the UI's database tab (SQL box or a plain-English question) or inside the
coding agent (`query_metadata`), see [WORKSPACE.md](WORKSPACE.md#the-catalog-workspacedb):

```bash
aos query workspaces/review "SELECT path, summary FROM files WHERE source='user'"
aos query workspaces/review "SELECT f.path FROM files f JOIN file_inputs i ON i.path=f.path WHERE i.input='inputs/labs.csv'"
```

## 5. Add outside sources

**Web and literature research** is a worker step. `storm` writes a broad, cited overview;
`grill` answers one well-posed academic question with source-verified claims. Both archive every
search hit and fetched page under `sources/webpages/<output dir name>/`, so the evidence stays in
the workspace and can be cited, re-read or audited later.

```bash
aos step workspaces/review storm \
  "Fabry disease: genetics, clinical features by organ system, diagnostic criteria and lab findings" \
  --output-dir generated/research/fabry
aos step workspaces/review grill \
  "Which laboratory findings best discriminate Fabry disease from other causes of left ventricular hypertrophy?" \
  --output-dir generated/research/fabry_labs
```

**Your own references** (guidelines, papers you already have) go in through `aos add` like any
other input; the planner sees them in the listing with your reason and summary and the workers get
them as `inputs`. Use a subfolder (`inputs/references/`) to keep them apart from the case files.

**Turning prose into structured data.** `sliders` reads text documents and builds a table whose
schema fits the question, every cell backed by a quote and a `file:line` locator:

```bash
aos step workspaces/review sliders \
  "List the clinical features, diagnostic criteria and characteristic lab findings of Fabry disease as tables" \
  --inputs generated/research/fabry/report.md --output-dir generated/tables/fabry
```

## 6. Run the agents

### Let the planner drive

Now the workspace holds inputs, transcripts, a database and research. Give the whole goal to
`aos run` and the planner sequences the steps, including any you did not do by hand:

```bash
aos run workspaces/review "Determine which patients in inputs/notes (transcribed under \
  generated/transcripts) and inputs/labs.csv match Fabry disease. Use the research under \
  generated/research and the feature tables under generated/tables; decide patient by patient \
  with a rationale citing the evidence, into generated/decisions/results.json and rationale.md."
```

What happens, step by step, is in [ARCHITECTURE.md](ARCHITECTURE.md#the-orchestration-loop): the
planner gets one JSON decision per step, the worker runs, AOS diffs the workspace to find the new
files, summarises and catalogs them, commits, and asks the planner again until it says `done`.
Progress prints to the terminal; in the UI the run appears as a card with each step's worker,
duration, files, cost and the live tail of its log.

Writing goals that work:

- Name the paths. "the patient notes" is ambiguous; `inputs/notes` is not.
- Name the deliverables and where they go. The planner stops when they exist.
- Name a worker when you have a preference ("use grill for the research").
- Say what good looks like ("a rationale citing the transcript line for each decision").

### How the planner chooses a worker

There is no routing table. Before every step the planner, the configured model in JSON mode, is
shown four things ([aos/prompts/planner.txt](../aos/prompts/planner.txt)): the goal; the
list of **available** workers, each with its `description` string; the workspace listing with every
file's source and summary; and the steps so far with their outputs, summaries and errors. It replies
with one decision: `run` a named worker with instructions, inputs and an output directory, `done`
with a summary, or `rollback` to an earlier step. AOS validates the decision (known worker,
non-empty instructions, inputs that exist, output directory inside the workspace) and sends an
invalid one back with the error, up to three times.

So the choice is driven by the descriptions. Each worker's description says what it does, when to
prefer it, what its instructions and inputs mean and what it produces; `sliders` says it needs text
files, `historygenie` says to use it first for scans, `storm` and `grill` say which kind of
research each is for. A few routing hints are in the prompt itself: specialised workers for what
they do best and `coding_agent` for everything else; `grill` for evidence-grade academic questions
and `storm` for general overviews; retry or investigate after a failure; never repeat a step that
succeeded. Workers whose system is not installed are not offered at all.

You influence the choice in three ways: phrase the goal (naming a worker or a path is usually
decisive); change the menu, by adding a worker or replacing a built-in one with your own under the
same name ([CUSTOM_WORKERS.md](CUSTOM_WORKERS.md)); or bypass the planner with `aos step` and
workflows. `aos trace TASK --full` shows every decision prompt and reply, which is the way to see
why the planner picked what it picked.

Steps that fail stay in the record with their error and the planner retries with corrected
instructions, sends the coding agent to investigate, or rolls back. Twelve steps is the default
cap (`--max-steps`); a budget cap in USD can be set per workspace
([CONFIGURATION.md](CONFIGURATION.md#budget-cap)).

### Drive it yourself

`aos step` runs exactly one worker with your instructions, with the same bookkeeping (a task record,
catalog rows, a commit, cost). It is the right tool while you are working out what the pipeline for
your documents should be. The examples above are all `aos step`.

### Talk to the workspace

The assistant answers questions about the workspace without changing it: what exists, why, what
each task did, what to run next.

```bash
aos ask workspaces/review "Which patients were flagged, and which transcript lines support each decision?"
aos ask workspaces/review "What would you run next to double-check the negatives?"
```

In the UI the chat box takes both: a question goes to the assistant, anything else starts a run.

## 7. Inspect, audit, undo

```bash
aos status workspaces/review                  # tasks, steps, every file with provenance
aos log workspaces/review                     # one commit per step
aos describe workspaces/review generated/decisions/results.json   # who made it, from which inputs
aos trace workspaces/review task-003          # every LLM call of the task: tokens, cost, latency, reply
aos trace workspaces/review task-003 --step 2 --full   # the prompts and replies of one step
```

Each step's log (`tasks/task-NNN/step-NN.log`) holds the runner's full output or the coding agent's
tool calls; the trace (`tasks/task-NNN/llm-calls.jsonl`) holds every model request and reply. See
[OBSERVABILITY.md](OBSERVABILITY.md).

If a step damaged something, roll back to the commit after the last good step; the task records
survive:

```bash
aos rollback workspaces/review <commit from aos log>
```

Edit any produced file by hand when you know better: the catalog marks it `mixed` and the planner
is told your version is authoritative.

## 8. Make it repeatable

When a task has done what you want, save its successful steps and replay them on the next batch of
documents, in a new workspace, without the planner:

```bash
aos workflow-save workspaces/review task-003 fabry-review
aos init workspaces/review-batch2
aos add workspaces/review-batch2 ~/cases2/notes/*.pdf ~/cases2/labs.csv
aos workflow-run workspaces/review-batch2 workspaces/review/workflows/fabry-review.json
```

The workflow is a JSON list of steps ([WORKSPACE.md](WORKSPACE.md#workflows)); edit instructions or
paths by hand between runs.

## 9. When the built-in workers are not enough

If your task needs a capability no worker offers (a proprietary extractor, a domain model, a tool
behind an API), write a worker: a small Python class with a `name`, a `description` the planner
reads, and a `run(ws, step, log)` method that reads inputs and writes files. Point `AOS_WORKERS` at
it, or assign it to `aos.workers` from Python, and it appears in the planner's menu without editing
AOS. The full guide, with a complete example, is [CUSTOM_WORKERS.md](CUSTOM_WORKERS.md).

## 10. The same thing from Python

[aos/api.py](../aos/api.py) exposes the whole flow as one object. The `aos` command is a thin layer
over it, so the two never diverge. The walkthrough above, as a script:

```python
from aos.api import AOS

aos = AOS.create("workspaces/review")          # goal="..." adds the optional one-line description
# AOS.open("workspaces/review") reopens it later; both accept llm=, workers= and log= (default: print)

# 3. documents: outside paths are copied into inputs/ (folders too), summarised, cataloged, committed
aos.add("~/cases/notes", "~/cases/labs.csv", reason="scanned notes and lab results")
aos.step("historygenie", "", inputs=["inputs/notes"], output_dir="generated/transcripts")

# 4./5. a database and sources, one worker at a time
aos.step("coding_agent", "Load inputs/labs.csv into generated/data/labs.sqlite (table labs) ...",
         inputs=["inputs/labs.csv"], output_dir="generated/data")
aos.step("storm", "Fabry disease: genetics, clinical features, diagnostic criteria and lab findings",
         output_dir="generated/research/fabry")
aos.step("sliders", "List the clinical features, diagnostic criteria and lab findings as tables",
         inputs=["generated/research/fabry/report.md"], output_dir="generated/tables/fabry")

# 6. let the planner drive the rest
task = aos.run("Determine which patients in generated/transcripts and inputs/labs.csv match Fabry disease ...",
               max_steps=12)
print(task.data["status"], task.data["result"])
for step in task.steps:
    print(step["n"], step["worker"], step["status"], step["outputs"][:3])

# 7. inspect
print(aos.ask("Which patients were flagged, and which transcript lines support each decision?"))
rows = aos.query("SELECT path, summary FROM files WHERE source='coding_agent'")
entry = aos.describe("generated/decisions/results.json")        # source, task, step, inputs
calls = aos.trace(task.id, step=2)                              # the LLM calls of one step, as dicts
aos.rollback(task.steps[0]["commit"])                           # if needed

# 8. repeat
aos.save_workflow(task.id, "fabry-review")
batch2 = AOS.create("workspaces/review-batch2")
batch2.add("~/cases2/notes", "~/cases2/labs.csv")
batch2.workflow("workspaces/review/workflows/fabry-review.json")

# 9. your own worker, for this session only
from glossary import Glossary
aos.workers["glossary"] = Glossary(aos.llm)
```

`step` returns the step record (`status`, `outputs`, `summary`, `error`, `commit`, `usage`) and
`run` and `workflow` return a `Task` (`id`, `data["status"]`, `data["result"]`, `steps`, `data["usage"]`).
`aos.workers` is the dict the planner chooses from; `aos.llm` is the model client workers can share
so their calls are costed and traced; `aos.budget_usd` and `aos.spent_usd` are the cap and the
running estimate; `aos.ws` is the underlying `Workspace` when you need the lower level
(`abspath`, `register`, `checkpoint`, `git`). Progress lines go to `log` (pass `lambda _: None` to
silence them). Opening a workspace needs no credentials; the model client is created on first use.

## Where to go next

- [CLI.md](CLI.md): every command and flag.
- [WEB_UI.md](WEB_UI.md): the same operations from the browser, and the HTTP API.
- [WORKERS.md](WORKERS.md): what each worker expects and produces, and how to phrase instructions.
- [examples/fabry/README.md](../examples/fabry/README.md): the shortest end-to-end run.
- The CS224V assignment 2 repository (`cs224vf26-assignment2`, a sibling of this one, with AOS vendored under
  `vendor/aos/`): students build a ReAct agent, then put it in a workspace for one disease's documents, run
  SLIDERS on the report, wrap the agent as a worker, and compare the two readings.
