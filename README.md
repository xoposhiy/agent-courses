# AI Agent Course Corpus

This corpus contains the seven selected courses and one book from the source list. Start with a course index, follow the local Markdown links, and consult the raw source when a conversion has limits.

[Topic analysis](analysis/README.md) · [Category dictionaries](analysis/categories/README.md) · [Collection rules](COLLECTION.md) · [Machine-readable catalog](catalog.json) · [Shared readings](SHARED-READINGS.md) · [Validation results](validation-report.json) · [Original source list](resources.md)

## Sources

| Source | Markdown files | Downloaded records | Recorded gaps |
| --- | ---: | ---: | ---: |
| [1. Stanford: Engineering AI Agents](courses/stanford-cs329z/README.md) | 278 | 278 | [5](courses/stanford-cs329z/GAPS.md) |
| [2. Columbia: Designing LLM Agents](courses/columbia-coms4995/README.md) | 65 | 66 | [2](courses/columbia-coms4995/GAPS.md) |
| [4. Carnegie Mellon: AI Agents](courses/cmu-11768/README.md) | 721 | 731 | [17](courses/cmu-11768/GAPS.md) |
| [10. LangChain Academy: Introduction to Deep Agents](courses/langchain-deep-agents/README.md) | 606 | 610 | [6](courses/langchain-deep-agents/GAPS.md) |
| [12. Stanford: Agentic AI](courses/stanford-cs224v/README.md) | 6747 | 6754 | [25](courses/stanford-cs224v/GAPS.md) |
| [15. DeepLearning.AI / Arize: Evaluating and Improving Agentic Applications](courses/dlai-agentic-evals/README.md) | 38 | 40 | [29](courses/dlai-agentic-evals/GAPS.md) |
| [17. CU Boulder: Building AI Agents](courses/colorado-csci7000/README.md) | 39 | 39 | [12](courses/colorado-csci7000/GAPS.md) |
| [Book: Agentic Large Language Models](courses/agentic-large-language-models/README.md) | 26 | 27 | [0](courses/agentic-large-language-models/GAPS.md) |

## Read the corpus

Counts refer to files and manifest records. Repository files and saved experiment traces count separately; these are not lesson counts.

Gap counts include failed original URLs with recovered copies. Read the source's gap report to distinguish unavailable content from a failed request that has an alternative.

- Each source has `README.md`, `manifest.json`, `GAPS.md`, `raw/`, and `markdown/`.
- Markdown files contain the full converted source content. Generated indexes and gap reports are labeled separately.
- Each converted file links to its source, raw file, and course index. Links to other archived materials point to local files when a matching source was found.
- PDF extraction keeps page numbers. Diagrams, complex tables, and equations can require the original PDF. Check conversion notes in the manifest.
- Repository archives preserve source files. Notebook Markdown contains cells and available saved text outputs. Downloaded code was not executed.
- Gaps include access restrictions, failed requests, missing transcripts, and unpublished materials. A saved error response is evidence of a failed request, not course content.
- Large video files, model weights, installed dependencies, private course systems, and recursive copies of external sites are outside this archive. Video links and retrieval gaps remain documented.

## Search and verify

Search the clean text with `rg -n -i 'search term' courses -g '*.md'`. Use `catalog.json` to filter by `source_id`, `category`, `download_status`, or `conversion_status`.

Run `python tools/validate_corpus.py --output validation-report.json` to check local links, recorded files, hashes, and PDF page coverage. Run `python tools/build_catalog.py` after a source manifest changes.

The collection reflects the dates recorded in each manifest. Fall 2026 courses were still in progress during collection. Preserve the authors' attribution and source license notices when reusing materials.
