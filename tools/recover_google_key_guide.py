"""Archive the public Markdown representation of a course-linked Google guide."""

from datetime import datetime, timezone
import hashlib
from pathlib import Path

from corpus import Corpus, resolve_markdown_urls


def main():
    corpus = Corpus(
        "courses/columbia-coms4995", "columbia-coms4995",
        "Columbia COMS 4995: Designing LLM Agents",
        "https://designing-agents.github.io/",
    )
    original_url = "https://ai.google.dev/gemini-api/docs/api-key"
    url = "https://aistudio.google.com/docs/api-key"
    record_id = "references/google-ai-studio-api-key-markdown"
    existing = next((item for item in corpus.data["materials"] if item["id"] == record_id), None)
    if existing:
        for prior in corpus.data["materials"]:
            if prior["url"] == original_url:
                prior["recovered_by"] = existing["markdown_path"]
        corpus.finalize()
        print("The public Markdown guide is already archived.")
        return
    response = corpus.session.get(url, headers={"Accept": "text/markdown"}, timeout=(15, 35))
    response.raise_for_status()
    if "text/markdown" not in response.headers.get("Content-Type", ""):
        raise ValueError("The server did not return the public Markdown representation")
    if "# Using Gemini API keys" not in response.text:
        raise ValueError("The response does not contain the expected guide title")
    relative = Path("raw/references/google-ai-studio-api-key.md")
    (corpus.root / relative).write_bytes(response.content)
    item = {
        "id": "google-ai-studio-api-key-markdown",
        "title": "Google AI Studio: Using Gemini API keys",
        "url": url,
        "aliases": [original_url],
        "category": "references",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "http_status": response.status_code,
        "final_url": response.url,
        "content_type": response.headers.get("Content-Type"),
        "raw_path": relative.as_posix(),
        "bytes": len(response.content),
        "sha256": hashlib.sha256(response.content).hexdigest(),
        "download_status": "downloaded",
        "conversion_status": "converted",
        "conversion_method": "source-markdown",
        "notes": ["The server provides a public Markdown representation when Accept: text/markdown is requested. The default HTML response is an app shell."],
        "request_headers": {"Accept": "text/markdown"},
    }
    corpus.write_markdown(item, resolve_markdown_urls(response.text, response.url))
    item["id"] = record_id
    corpus.data["materials"].append(item)
    for prior in corpus.data["materials"]:
        if prior["url"] == original_url:
            prior["recovered_by"] = item["markdown_path"]
            prior["notes"].append("Full guide recovered from the server's public Markdown representation: " + item["markdown_path"])
    corpus.finalize()
    print("Archived the full public Markdown guide.")


if __name__ == "__main__":
    main()
