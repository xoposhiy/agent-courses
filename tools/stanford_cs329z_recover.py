"""Recover an author-linked reading and annotate assignment output placeholders."""

import json
from pathlib import Path

from corpus import Corpus


def main():
    root = Path("courses/stanford-cs329z")
    data = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    corpus = Corpus(root, data["source_id"], data["title"], data["source_url"])
    corpus.data = data
    corpus.add("https://autolibra.org/", "AutoLibra author page and full-text provenance", "metadata", "autolibra-author-page")
    corpus.add("https://arxiv.org/abs/2505.02820", "AutoLibra arXiv record (metadata)", "metadata", "arxiv-2505-02820")
    fallback = corpus.add("https://arxiv.org/pdf/2505.02820", "AutoLibra: Agent Metric Induction from Open-Ended Human Feedback", "readings", "arxiv-2505-02820", expected="pdf")
    if fallback.get("markdown_path"):
        fallback["aliases"] = ["https://openreview.net/forum?id=4BjGVZ7Bxn", "https://openreview.net/pdf?id=4BjGVZ7Bxn"]
        fallback["discovered_from"] = "https://autolibra.org/"
        for item in data["materials"]:
            if item["url"] == "https://openreview.net/pdf?id=4BjGVZ7Bxn":
                item["recovered_by"] = fallback["markdown_path"]
                item["notes"].append("Full text recovered from the author-linked arXiv PDF: " + fallback["markdown_path"])
                item["notes"].append("The static published OpenReview URL also returned HTTP 403: https://openreview.net/pdf/14b3218a8e2b6f4becdebebdbfe120159f322a60.pdf")
    figures = ("effort-distribution", "bash-command-usage", "exploration-to-implementation", "repeated-effort", "context-consulted", "failure-recovery", "custom-analysis")
    for item in data["materials"]:
        if item.get("raw_path", "").endswith("writeup/3_run_example_tasks/responses.md") and item.get("markdown_path"):
            target = root / item["markdown_path"]
            content = target.read_text(encoding="utf-8")
            for figure in figures:
                content = content.replace(f"![]({figure}.png)", f"> Student output placeholder: `{figure}.png`. The assignment asks the student to create this figure; the source repository does not provide the image.")
            target.write_text(content, encoding="utf-8")
            item["notes"].append("Seven image references are student output placeholders, not missing teaching assets. The raw response template preserves the original image markup.")
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
    data["notes"].append("The assignment2-harness and assignment2-evals GitHub URLs resolve to identical repository archives with the same SHA-256. Both URL snapshots are retained for provenance; they represent one assignment.")
    data["notes"].append("The Homework 2 response templates contain seven image placeholders for plots that students must generate. Markdown marks these as student output placeholders; the raw templates are unchanged.")
    corpus.finalize()
    print(json.dumps(data["counts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
