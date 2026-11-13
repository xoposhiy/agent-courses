"""Archive public LangChain Deep Agents teaching pages and repository."""

import json
from pathlib import Path

from corpus import Corpus


def main():
    corpus = Corpus("courses/langchain-deep-agents", "langchain-deep-agents", "LangChain Academy: Introduction to Deep Agents", "https://academy.langchain.com/courses/foundation-introduction-to-deepagents")
    corpus.add(corpus.data["source_url"], "Public course curriculum and access information", "pages", "curriculum")
    corpus.add_repo("https://github.com/langchain-ai/lca-deepagents", "Official course repository: Python, TypeScript, lesson sources, and agent UI", "lca-deepagents")
    corpus.finalize()
    root = corpus.root / "raw/repositories/lca-deepagents"
    print("Lesson sources:", [str(path.relative_to(root)) for path in (root / "thinkific/src").rglob("*") if path.is_file()], flush=True)
    print(json.dumps(corpus.data["counts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
