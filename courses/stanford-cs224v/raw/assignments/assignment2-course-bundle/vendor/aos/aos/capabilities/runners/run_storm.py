"""Run STORM (knowledge-storm) on one topic and leave its artifacts in --output-dir.

Executed with external/storm/.venv/bin/python. Reads API_KEY, BASE_URL, AOS_MODEL
and SERPER_API_KEY from the environment.
"""

import argparse
import json
import logging
import os
import sys
import shutil
from pathlib import Path


def main() -> None:
    logging.basicConfig(level=logging.WARNING, stream=sys.stdout, format="%(name)s: %(message)s")
    logging.getLogger("knowledge_storm").setLevel(logging.INFO)  # stage progress, streamed into the step log
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--sources-dir", default=None,
                    help="where every search hit and fetched page is archived (STORM_FETCH_DIR)")
    ap.add_argument("--max-conv-turn", type=int, default=3)
    ap.add_argument("--max-perspective", type=int, default=3)
    ap.add_argument("--search-top-k", type=int, default=3)
    ap.add_argument("--max-thread-num", type=int, default=3)
    args = ap.parse_args()
    if args.sources_dir:
        os.environ["STORM_FETCH_DIR"] = str(Path(args.sources_dir).resolve())

    from knowledge_storm import STORMWikiLMConfigs, STORMWikiRunner, STORMWikiRunnerArguments
    from knowledge_storm.lm import LitellmModel
    from knowledge_storm.rm import SerperRM

    model = "openai/" + os.environ.get("AOS_MODEL", "gemini-3.6-flash")
    # Generous caps: reasoning tokens count against max_tokens on this endpoint, so
    # thinking is switched off and the caps are kept far above STORM's defaults.
    kw = dict(api_key=os.environ["API_KEY"], api_base=os.environ["BASE_URL"],
              temperature=1.0, top_p=0.9, reasoning_effort="none")
    lms = STORMWikiLMConfigs()
    lms.set_conv_simulator_lm(LitellmModel(model=model, max_tokens=4000, **kw))
    lms.set_question_asker_lm(LitellmModel(model=model, max_tokens=4000, **kw))
    lms.set_outline_gen_lm(LitellmModel(model=model, max_tokens=4000, **kw))
    lms.set_article_gen_lm(LitellmModel(model=model, max_tokens=8000, **kw))
    lms.set_article_polish_lm(LitellmModel(model=model, max_tokens=16000, **kw))

    out = Path(args.output_dir)
    scratch = out / ".storm_run"
    shutil.rmtree(scratch, ignore_errors=True)  # leftovers of an earlier run that crashed
    scratch.mkdir(parents=True, exist_ok=True)
    engine_args = STORMWikiRunnerArguments(
        output_dir=str(scratch), max_conv_turn=args.max_conv_turn,
        max_perspective=args.max_perspective, search_top_k=args.search_top_k,
        max_thread_num=args.max_thread_num,
    )
    # full pages are fetched (and archived under --sources-dir), not only the search snippets
    rm = SerperRM(serper_search_api_key=os.environ["SERPER_API_KEY"], k=args.search_top_k,
                  query_params={"autocorrect": True, "num": 10, "page": 1},
                  ENABLE_EXTRA_SNIPPET_EXTRACTION=True)
    runner = STORMWikiRunner(engine_args, lms, rm)
    runner.run(topic=args.topic, do_research=True, do_generate_outline=True,
               do_generate_article=True, do_polish_article=True)
    usage = {"model": os.environ.get("AOS_MODEL", "gemini-3.6-flash"), "calls": None,
             "input_tokens": 0, "output_tokens": 0, "cost_usd": None}
    # STORM resets each LM's counter after every stage and keeps the totals per stage in runner.lm_cost
    for stage in runner.lm_cost.values():
        for counts in stage.values():
            usage["input_tokens"] += int(counts.get("prompt_tokens", 0))
            usage["output_tokens"] += int(counts.get("completion_tokens", 0))
    runner.post_run()
    runner.summary()

    # STORM writes into <output_dir>/<topic slug>/; flatten that into output_dir.
    topic_dirs = [p for p in scratch.iterdir() if p.is_dir()]
    if not topic_dirs:
        raise SystemExit("STORM produced no output directory")
    for item in topic_dirs[0].iterdir():
        shutil.move(str(item), str(out / item.name))
    shutil.rmtree(scratch)
    for name in ("storm_gen_article_polished.txt", "storm_gen_article.txt"):
        article = out / name
        if article.is_file():
            shutil.copyfile(article, out / "report.md")
            break
    (out / "usage.json").write_text(json.dumps(usage, indent=2))
    print(f"STORM finished; artifacts in {out}; tokens in/out {usage['input_tokens']}/{usage['output_tokens']}")


if __name__ == "__main__":
    main()
