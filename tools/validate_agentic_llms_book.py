"""Check book paths, hashes, chapter anchors, and asset coverage."""

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from validate_corpus import audit


def main():
    root = Path(__file__).resolve().parents[1]
    folder = root / "courses/agentic-large-language-models"
    report = audit(root)
    course = next(item for item in report["courses"] if item["id"] == "agentic-large-language-models")
    errors = [error for error in report["errors"] if "courses/agentic-large-language-models" in error]
    documents = list((folder / "markdown").rglob("*.md")) + [folder / "CONTENTS.md"]
    anchors = {path.resolve(): set(re.findall(r'<a id="([^"]+)"', path.read_text(encoding="utf-8"))) for path in documents}
    checked = 0
    for path in documents:
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"(?<!\\)\[[^\]\n]*\]\(([^\s)]+)\)", text):
            parsed = urlsplit(match.group(1))
            if parsed.scheme or not parsed.fragment:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            if dest not in anchors:
                continue
            checked += 1
            if unquote(parsed.fragment) not in anchors[dest]:
                errors.append(f"Missing chapter anchor: {path.relative_to(folder)} -> {match.group(1)}")
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    assets = next(item["assets"] for item in manifest["materials"] if item.get("conversion_method") == "arxiv-html-with-latex-and-local-figures")
    for asset in assets:
        path = folder / asset["raw_path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != asset["sha256"]:
            errors.append("Figure checksum mismatch: " + asset["raw_path"])
    result = {"course": course, "chapter_anchor_links_checked": checked, "figure_checksums_checked": len(assets), "errors": errors}
    (folder / "validation.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
