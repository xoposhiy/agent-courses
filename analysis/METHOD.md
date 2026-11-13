# Method and Limits

## Scope

This analysis uses the downloaded corpus in `courses/`, as recorded in the source manifests. It covers seven courses and the book *Agentic Large Language Models*. It does not add current web content or reconstruct restricted lessons. Source content can change after the archived version.

The main frequency counts **distinct courses**. A concept counts at most once in each of the seven courses. The book has a separate presence column and never increases course frequency.

## Sequential extraction

The first pass processed the sources in catalog order:

1. Stanford CS329Z
2. Columbia COMS4995
3. CMU 11-768
4. LangChain Introduction to Deep Agents
5. Stanford CS224V
6. DeepLearning.AI / Arize Evaluating and Improving Agentic Applications
7. CU Boulder CSCI7000
8. Agentic Large Language Models, as a separate comparison

Each step added new definitions to the shared dictionary and reused existing concept IDs. The `checkpoints/` folder preserves the dictionary after each first-pass source. The `curation/` folder preserves the reviewed input. A final cross-course review checks earlier courses for concepts introduced later and corrects weak evidence. Those changes are explicit in `reconciliation.json` and `reconciliation-audit.json`.

The analyst screened schedules and available lecture or lesson structure, then selected passages from teaching materials and assigned readings. This is a reviewed curriculum inventory. It is not an exhaustive semantic annotation of every sentence in every repository, paper, trace, or example.

## Evidence levels

| Value | Meaning | In course frequency? |
| --- | --- | --- |
| `taught` | Available slides, lesson text, assignment instructions, or teaching code explain or implement the concept. | Yes |
| `assigned` | A course-assigned reading contains the concept. This does not establish how much class time it received. | Yes |
| `planned` | The schedule or outline announces the concept, but confirmed teaching or assigned-reading evidence is not recorded. This includes future sessions and unavailable materials. | No |
| `not evidenced` | No coverage record was selected for this concept and source. | No |

An assignment instruction is teaching evidence. Test data, experiment logs, output records, dependency declarations, and access errors are not teaching evidence. A named paper in a bibliography does not establish coverage by itself. A prerequisite, a student wish, or an incidental example is not enough.

For the seminar at CU Boulder, assigned papers are the main teaching material. The tables separate this evidence from lectures and exercises so the seminar can be compared without implying that it has the same format as a hands-on course.

## Naming and scope

Every concept has a stable ID, one English name, a type, a definition, and optional aliases and a parent. Types distinguish topics, concepts, patterns, methods, tools, protocols, and applications. The dictionary preserves differences such as prompt chaining versus chain of thought, generic reflection versus Reflexion, tool use versus MCP, and prompt optimization versus harness improvement.

Aliases are equivalent names within the defined scope. Named systems and narrower examples belong under related terms when they are not synonyms. Parent and child topics remain distinct. Counts are never added across the hierarchy, and a child does not automatically establish coverage of a parent.

Some related details share a stated curriculum topic, such as decoding and sampling or model compression and quantization. The inventory does not create a separate row for every paper, product, parameter, or benchmark. Different grouping choices can change the ranking.

## Counts and reproducibility

- `course_count`: courses with `taught` or `assigned` evidence, from 0 to 7.
- `taught_course_count` and `assigned_course_count`: separate parts of that total. A source uses one coverage level for each concept.
- `planned_course_count`: schedule-only courses, outside the main total.
- `book_present`: confirmed evidence in the book, outside the main total.
- `evidence_file_count`: distinct course files selected as confirmed evidence. This is a lower bound on supporting files, not a count of all lectures or all occurrences.

The reports do not count raw word mentions. Mention counts depend on file size, repeated slides, PDF and HTML copies, language versions, shared readings, vendored repositories, and saved traces. Those differences do not measure how widely a topic is taught.

Each evidence record contains a local path, a line number, a page number when available, the matching source line, a material ID, an original URL, and a hash of the converted file. Markdown reports link to the file and show the relevant page or line.

Rebuild the first pass, then apply the reviewed corrections and regenerate the reports:

```powershell
$sources = 'stanford-cs329z', 'columbia-coms4995', 'cmu-11768', 'langchain-deep-agents', 'stanford-cs224v', 'dlai-agentic-evals', 'colorado-csci7000', 'agentic-large-language-models'
foreach ($source in $sources) {
    python tools/topic_analysis.py apply --course $source
    if ($LASTEXITCODE -ne 0) { throw "Topic extraction failed: $source" }
}
python tools/topic_analysis.py reconcile
python tools/topic_analysis.py build
python tools/topic_analysis.py validate
```

The script validates structure, aliases, evidence, hashes, links, and counts. It does not prove semantic completeness. Concept selection and evidence classification remain analyst judgments.

## Category dictionaries

[Separate category dictionaries](categories/README.md) classify the same concepts by their role in agent development. [Category rules](categories/METHOD.md) explain the boundaries between architecture, local techniques, technologies, and applications. Each concept has one primary category; cross-references do not create duplicate membership. The category reports preserve the original course frequencies.

After rebuilding the source analysis, refresh the category exports:

```powershell
python tools/categorize_topics.py build
python tools/categorize_topics.py validate
```

## Interpretation

Course frequency measures breadth across this collection. It does not measure teaching time, depth, quality, prerequisites, or importance. Available content is incomplete for several courses, and some courses were still running when collected. Read each archive's `GAPS.md` before interpreting missing evidence as a missing curriculum topic.
