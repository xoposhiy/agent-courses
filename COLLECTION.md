# Course Collection Rules

Use [Stanford CS329Z](courses/stanford-cs329z/README.md) as the reference structure. Use `tools/corpus.py` when useful. Choose the collection method that fits the source.

1. Work only in the assigned source folder from `collection-plan.json`. Keep original downloads in `raw/` and full-content conversions in `markdown/`. Add `README.md`, `manifest.json`, and `GAPS.md`.
2. Follow the official course pages to published lectures, slides, assignments, project rules, teaching repositories, notebooks, and course-curated readings, including optional readings. Check secondary course pages. Keep required and optional readings distinct. Do not recursively copy external sites or a book's bibliography.
3. Convert the full available content, not a summary. Keep useful headings, code, notebook cells and saved outputs, page numbers, and attribution. Prefer source HTML, Markdown, or TeX when these give better results. Keep PDF originals and state conversion limits.
4. Link the index to the materials. Link each conversion to the course index, original URL, and raw file. Use relative links between archived materials. Repair links from repository documents to local files. Keep unavailable targets as external references.
5. Use the pilot manifest schema: `source_id`, `title`, `source_url`, `retrieved_at`, and `materials`. Each material needs a unique `id`, title, URL, category, retrieval time, download status, conversion status, notes, and local paths when available. Record raw file size and SHA-256. Separate download failures from conversion failures.
6. Verify responses before treating them as content. Check for login and verification pages even after HTTP 200. Record unpublished, restricted, failed, or partly converted materials in `GAPS.md`. Try public video captions where practical; record missing captions. Exclude large video files, model weights, installed dependencies, and private services. Preserve source code without running it.
7. Check completeness against the course schedule and repository contents. Check local links, file paths, hashes, and conversion coverage. Report actual results and remaining gaps. Artifacts must be in English; preserve quoted source content.

Keep source-specific collector scripts in `tools/` with distinct names. Coordinate changes to shared helpers with the parent agent. Shared arXiv request pacing is provided by `tools/network_pacing.py`.
