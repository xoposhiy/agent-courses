# Homework 2 bundle: vendor/aos/aos/capabilities/runners/run_grill.py

[Course index](../../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/capabilities/runners/run_grill.py) · [Raw file](../../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/capabilities/runners/run_grill.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""Run GRILL (graph-search-sliders, the belief-ledger research agent) on one question.

Executed with external/graph-search-sliders/.venv/bin/python, cwd = the repo root.
Needs the `codex` CLI on PATH. Reads API_KEY, BASE_URL and AOS_MODEL from the environment.

Local adaptations are applied in-process, without touching the repo:
- embeddings: the proxy key has no embeddings model, so the Embedder is replaced by a
  hashed character-trigram embedder (similarity is only used to rank the frontier);
- pricing: the Gemini model is added to the USD rate table so the budget is meaningful;
- provider: codex is pointed at BASE_URL from .env instead of the repo's hard-coded endpoint;
- web search: codex's built-in web_search tool does nothing through the Gemini proxy, so every
  research task is told to run web_search.py (Serper web + Google Scholar search, page fetching)
  from its sandbox shell; the run directory is made writable so the searches are kept there;
- verification: GRILL's stage-2 deep test (an adversarial, extensive hunt for counter-evidence)
  dominates run time. --verify light (the default) keeps stage 2 but as a focused source check
  plus one deliberate search for contradicting evidence, with a smaller per-task cap; --verify deep is GRILL's own; --verify off skips stage 2
  (GRILL's no-verifier ablation, which leaves every pooled claim marked untested). --no-screen
  drops stage 1 (the quick plausibility search) so every hypothesis goes straight to stage 2.
"""

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import sys
from pathlib import Path

DIM = 512
GEMINI_RATES_PER_M = (0.30, 2.50)

TOOLS_NOTE = """TOOLS: this environment has NO built-in web search. Search and read sources from the shell:
  python3 {tools} search "<query>" --scholar        # Google Scholar: papers with title, link, publication, year, cited_by, pdf
  python3 {tools} search "<query>" [--num 10]       # Google web results: title, link, snippet, date
  python3 {tools} fetch <url> [--max-chars 30000]  # readable text of a page or PDF, to verify quotes before citing
Prefer --scholar for the literature; run several focused queries rather than one broad one. Results and fetched
pages are saved under {searches} and repeated calls are answered from there. Cite only what you have read.

"""


LIGHT_TASK_USD = 0.80  # per light verification task (GRILL's deep test defaults to $2.00)


def light_deep_test(executors):
    """A replacement for executors.deep_test: verify against the sources actually read, without the
    extensive counter-example hunt. Same schema and verdicts, so the ledger treats it as stage 2."""

    def deep_test(h, question, prior_evidence, task_dir, budget_hint=None, guardrails="", **kw):
        prompt = (
            "You are verifying a research hypothesis against the literature with a FOCUSED check, not an "
            "exhaustive one.\n\n"
            "OVERALL QUESTION:\n{q}\n\nHYPOTHESIS UNDER TEST:\n{h}\n(why it was proposed: {why})\n\n"
            "EVIDENCE ALREADY ATTACHED (verify it; do not just trust it):\n{prior}\n\n"
            "Steps:\n"
            "1. Run two or three targeted searches (prefer Google Scholar) and READ the one to three most "
            "relevant sources. Check that each is real and resolvable and that its authors, venue and numbers "
            "are as cited.\n"
            "2. Then run ONE search deliberately aimed at contradiction (negative results, failed replications, "
            "populations or settings where it does not hold, stated limitations) and read the most relevant hit "
            "if there is one. Stop there: a single targeted look, not the open-ended adversarial hunt.\n"
            "3. Report EVERY source you used as an `evidence` item with its stance. {rules}\n"
            "4. Decide the `verdict`:\n"
            "   \u2022 \"supported\" \u2014 the sources you read support it and your deliberate look for contradiction found none that stands.\n"
            "   \u2022 \"conflicted\" \u2014 there is real support AND a real contradiction; list each in `conflicts`.\n"
            "   \u2022 \"refuted\" \u2014 the sources give no support, or contradict it outright.\n"
            "Give your `rationale`, your posterior `confidence` P(true) in [0,1], and any `new_directions` "
            "this check opened up."
        ).format(q=question, h=h.text, why=h.rationale, prior=prior_evidence, rules=executors._evidence_rules())
        prompt += executors._guard(guardrails)
        if budget_hint:
            prompt += "\n\nBUDGET: ~${:.2f} for this check; it is a light pass, so emit the JSON well before you run out.".format(budget_hint)
        return executors.run_task(task_dir, prompt, executors.schemas.DEEP_TEST, mode="research", **kw)

    return deep_test


def skip_screen(orchestrator_module):
    """Replace stage 1: every proposed hypothesis is queued for stage 2 without the screening search."""
    proposed, screened = orchestrator_module.PROPOSED, orchestrator_module.SCREENED

    def _screen(self, hyps):
        n = 0
        for h in hyps:
            if h.status == proposed:
                h.status = screened
                n += 1
        self.log("  SCREEN: skipped (AOS --no-screen); {} hypotheses go straight to the verification stage".format(n))

    orchestrator_module.Orchestrator._screen = _screen


def configure_verification(executors, argv, mode):
    """Apply the --verify mode: extra GRILL CLI arguments and, for light, the replacement stage 2."""
    if mode == "off":
        argv += ["--ablate", "no-verifier"]
    elif mode == "light":
        executors.deep_test = light_deep_test(executors)
        argv += ["--deep-task-usd", str(LIGHT_TASK_USD)]
    elif mode != "deep":
        raise SystemExit("--verify must be light, deep or off")
    return argv


def provider_overrides(base_url):
    """codex -c overrides that point it at the AOS proxy (the repo hard-codes another endpoint)."""
    return [
        "model_provider=aos",
        'model_providers.aos.name="AOS proxy"',
        'model_providers.aos.base_url="{}"'.format(base_url),
        'model_providers.aos.env_key="OPENAI_API_KEY"',
        'model_providers.aos.wire_api="responses"',
    ]


def tools_note(tools, searches):
    return TOOLS_NOTE.format(tools=tools, searches=searches)


def install_tools(codex_exec, tools, run_dir):
    """Give every research task the search tool: prepend the usage note to its prompt, point the
    searches folder into the run directory and let the sandbox write there."""
    searches = Path(run_dir) / "searches"
    os.environ["AOS_SEARCH_LOG_DIR"] = str(searches)
    codex_exec.PROVIDER = provider_overrides(os.environ["BASE_URL"]) + [
        'sandbox_workspace_write.writable_roots=["{}"]'.format(run_dir)]
    note = tools_note(tools, searches)
    original = codex_exec._run_task_once

    def with_tools(task_dir, prompt, schema, **kw):
        if kw.get("mode", "research") == "research":
            prompt = note + prompt
        return original(task_dir, prompt, schema, **kw)

    codex_exec._run_task_once = with_tools
    return note


def local_embedding(text: str) -> list[float]:
    vec = [0.0] * DIM
    t = re.sub(r"\s+", " ", text.lower())
    for i in range(max(len(t) - 2, 0)):
        h = int(hashlib.md5(t[i:i + 3].encode()).hexdigest()[:8], 16)
        vec[h % DIM] += 1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--question", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--budget", type=float, default=12.0)
    ap.add_argument("--max-rounds", type=int, default=6)
    ap.add_argument("--batch", type=int, default=3)
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--reasoning", default="low")
    ap.add_argument("--task-timeout", type=int, default=1200)
    ap.add_argument("--tools", default=None, help="path of web_search.py to advertise to the agents")
    ap.add_argument("--verify", default="light", choices=["light", "deep", "off"],
                    help="stage-2 verification: light = focused source check (default), deep = GRILL's "
                         "adversarial deep test (slow), off = skip stage 2 (claims stay marked untested)")
    ap.add_argument("--no-screen", action="store_true",
                    help="skip stage 1 (the quick plausibility search per hypothesis): everything goes straight to stage 2")
    args = ap.parse_args()

    model = os.environ.get("AOS_MODEL", "gemini-3.6-flash")
    os.environ["OPENAI_API_KEY"] = os.environ["API_KEY"]
    os.environ["OPENAI_BASE_URL"] = os.environ["BASE_URL"]
    os.environ["RUN_MODEL"] = model
    os.environ["CLASSIFY_MODEL"] = model
    os.environ["GSS_ENV_FILE"] = "/nonexistent/.env"  # our environment is authoritative
    sys.path.insert(0, str(Path.cwd()))

    from src import config, embed

    prices = json.loads(os.environ.get("AOS_PRICES", "{}"))
    config.MODEL_RATES_M[model] = tuple(prices.get(model, GEMINI_RATES_PER_M))
    embed.Embedder.embed = lambda self, texts: [local_embedding(x.strip()) if x.strip() else None for x in texts]

    from src import cli, codex_exec, executors
    from src import orchestrator as grill_orchestrator

    out = Path(args.output_dir).resolve()
    run_dir = out / "grill_run"
    run_dir.mkdir(parents=True, exist_ok=True)
    tools = Path(args.tools or Path(__file__).with_name("web_search.py")).resolve()
    install_tools(codex_exec, tools, run_dir)
    sys.argv = [
        "grill", "--question", args.question, "--run-dir", str(run_dir),
        "--budget", str(args.budget), "-K", str(args.batch), "--max-rounds", str(args.max_rounds),
        "--concurrency", str(args.concurrency), "--reasoning", args.reasoning, "--model", model,
        "--sources", "", "--task-timeout", str(args.task_timeout), "--no-auto-artifacts",
    ]
    configure_verification(executors, sys.argv, args.verify)
    if args.no_screen:
        skip_screen(grill_orchestrator)
    rc = cli.main()
    if rc:
        raise SystemExit(f"GRILL exited with {rc}")

    nested_git = run_dir / "workspace" / ".git"
    if nested_git.is_dir():  # keep the files, not a repo inside the AOS workspace repo
        shutil.rmtree(nested_git)
    answer = run_dir / "answer.md"
    if not answer.is_file():
        raise SystemExit("GRILL produced no answer.md")
    shutil.copyfile(answer, out / "report.md")
    data = run_dir / "workspace" / "data"
    for src_name, dst_name in (("evidence.csv", "sources.csv"), ("findings.csv", "findings.csv"),
                               ("metrics.csv", "metrics.csv")):
        if (data / src_name).is_file():
            shutil.copyfile(data / src_name, out / dst_name)
    spent = None
    try:
        spent = json.loads((run_dir / "run.json").read_text()).get("budget", {}).get("spent")
    except (OSError, ValueError, AttributeError):
        pass
    (out / "usage.json").write_text(json.dumps({"model": model, "calls": None, "input_tokens": None,
                                                "output_tokens": None, "cost_usd": spent}, indent=2))
    print(f"GRILL finished; report at {out / 'report.md'}; spent ${spent}")


if __name__ == "__main__":
    main()

```
