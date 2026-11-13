"""Keep an OpenReview access response separate from the recovered paper text."""

import os
from pathlib import Path
import re

from corpus import Corpus, map_prose


def main():
    corpus = Corpus("courses/stanford-cs329z", "stanford-cs329z", "Stanford CS329Z: Engineering AI Agents", "https://cs329z.stanford.edu/")
    blocked = next(item for item in corpus.data["materials"] if item["url"] == "https://openreview.net/forum?id=4BjGVZ7Bxn")
    recovered = "markdown/readings/arxiv-2505-02820.md"
    old_relative = blocked.pop("markdown_path", None)
    if old_relative:
        old_path = (corpus.root / old_relative).resolve()
        destination = Path("tmp/rejected-conversions/stanford-autolibra-access-page.md").resolve()
        workspace = Path.cwd().resolve()
        if not old_path.is_relative_to(workspace) or not destination.is_relative_to(workspace):
            raise ValueError("The rejected conversion must remain within the workspace")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if old_path.exists():
            old_path.replace(destination)
        for path in (corpus.root / "markdown").rglob("*.md"):
            content = path.read_text(encoding="utf-8")
            def rewrite(match):
                label, target = match.groups()
                if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    return match.group(0)
                if (path.parent / target.split("#", 1)[0]).resolve() != old_path:
                    return match.group(0)
                local = os.path.relpath(corpus.root / recovered, path.parent).replace("\\", "/")
                return f"[{label}]({local})"
            updated = map_prose(content, lambda line: re.sub(r"(?<!\\)\[([^\]]+)\]\(([^\s)]+)\)", rewrite, line))
            if updated != content:
                path.write_text(updated, encoding="utf-8")
    blocked.update(
        download_status="access_blocked", conversion_status="failed",
        conversion_method="access-response-only", recovered_by=recovered,
        notes=["OpenReview returned a browser-verification challenge instead of the paper page. The saved HTML is an access response, not course content."],
    )
    corpus.finalize()
    print("Rejected the access-page conversion and linked the recovered full text.")


if __name__ == "__main__":
    main()
