"""Keep teaching placeholders readable without presenting them as archive links."""

from pathlib import Path

from corpus import Corpus


def main():
    root = Path("courses/langchain-deep-agents")
    corpus = Corpus(root, "langchain-deep-agents", "LangChain Academy: Introduction to Deep Agents", "https://academy.langchain.com/courses/foundation-introduction-to-deepagents")
    for item in corpus.data["materials"]:
        if item["category"] == "lessons":
            aliases = item.get("aliases", [])
            item["aliases"] = sorted(set(aliases + [url.replace("/lca-lessons/deepagents/", "/lca-deepagents/") for url in aliases]))
        if not item.get("markdown_path"):
            continue
        path = root / item["markdown_path"]
        text = path.read_text(encoding="utf-8")
        if "[Configure TTL](Configure TTL)" in text:
            text = text.replace("[Configure TTL](Configure TTL)", "\\[Configure TTL](Configure TTL)")
            item["notes"].append("The source contains an intentional invalid-link example, which is shown as literal markup.")
        if "[](TODO)" in text:
            text = text.replace("[](TODO)", "> Source video placeholder: `TODO`. The tutor snapshot provides no video URL here. Use the current lesson and its archived public walkthroughs.")
            item["notes"].append("The tutor source contains a TODO video placeholder rather than a public video URL.")
        path.write_text(text, encoding="utf-8")
    note = "The tutor overview contains a TODO video placeholder. The source placeholder is labelled explicitly; current primary lesson text and all 78 linked public walkthrough transcripts are archived. Literal chart paths in sandbox skills are runtime output examples, not missing course assets."
    if note not in corpus.data["notes"]:
        corpus.data["notes"].append(note)
    corpus.finalize()
    readme = root / "README.md"
    readme.write_text(readme.read_text(encoding="utf-8").replace("[Manifest](manifest.json)", "[Lesson contents](CONTENTS.md) · [Manifest](manifest.json)", 1), encoding="utf-8")


if __name__ == "__main__":
    main()
