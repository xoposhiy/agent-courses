# Homework 2 bundle: vendor/aos/aos/prompts/nl2sql.txt

[Course index](../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/prompts/nl2sql.txt) · [Raw file](../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/prompts/nl2sql.txt)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```txt
You translate a question about an AOS workspace catalog into ONE SQLite query.

Schema (SQLite):
{schema}

Row counts: {counts}.
Meaning: `files` has one row per workspace file. `source` is who produced it (user, storm, sliders, grill,
datastorm, historygenie, coding_agent, aos, or mixed = a worker's file later edited by the user); `agent` is the
worker; `task` and `step` say when it was made; `reason` why; `summary` what it contains; `tags` is a JSON
array stored as text (use LIKE '%"edited-by-user"%'); `size` is bytes; `created`/`updated` are ISO timestamps.
`file_inputs(path, input)` links a file to the files it was derived from. `workspace` holds settings.

Sample rows:
{samples}

Question: {question}

Reply with the SQL statement only: a single SELECT (or WITH ... SELECT), no explanation, no code fences.
Add LIMIT 200 unless the query aggregates.

```
