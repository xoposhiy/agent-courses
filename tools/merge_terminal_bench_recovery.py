"""Merge the verified public Terminal-Bench page capture into the pilot course."""

import json
from pathlib import Path
import shutil

from corpus import Corpus


def main():
    root = Path(__file__).resolve().parents[1]
    package = root / "tmp/recoveries/terminal-bench"
    corpus = Corpus(root / "courses/stanford-cs329z", "stanford-cs329z", "Stanford CS329Z: Engineering AI Agents", "https://cs329z.stanford.edu/")
    patch = json.loads((package / "manifest-patch.json").read_text(encoding="utf-8"))
    item = next(record for record in corpus.data["materials"] if record["id"] == patch["target_resource_id"])
    original = {key: item[key] for key in ("url", "raw_path", "bytes", "sha256", "retrieved_at")}
    for directory in ("raw", "markdown"):
        for source in (package / directory).rglob("*"):
            if not source.is_file():
                continue
            target = corpus.root / source.relative_to(package)
            if not target.resolve().is_relative_to(corpus.root.resolve()):
                raise ValueError("A recovery file must stay inside its source folder")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    item.update(patch["replace_fields"])
    if original["raw_path"] != item["raw_path"]:
        original["capture_method"] = "HTTP-only snapshot from the initial course collection"
        item["assets"].append(original)
    corpus.finalize()
    print("Merged the complete default leaderboard table and its capture limits.")


if __name__ == "__main__":
    main()
