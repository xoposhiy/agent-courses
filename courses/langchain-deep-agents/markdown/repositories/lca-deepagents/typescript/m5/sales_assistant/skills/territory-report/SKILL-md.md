# Official course repository: Python, TypeScript, lesson sources, and agent UI: typescript/m5/sales_assistant/skills/territory-report/SKILL.md

[Course index](../../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/typescript/m5/sales_assistant/skills/territory-report/SKILL.md) · [Raw file](../../../../../../../../raw/repositories/lca-deepagents/typescript/m5/sales_assistant/skills/territory-report/SKILL.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

---
name: territory-report
description: "Build a report on the rep's sales territory — revenue, top customers, top genres, and trends for Jane's book of business — with a chart. Use when asked for a territory report, sales summary, performance numbers, or 'how is my book doing'."
---

# Territory Report

A metrics task. The numbers come from the database; the chart is rendered
from them.

## 1. Gather the metrics

Ask **chinook-analyst** for Jane's book of business (`SupportRepId = 3`):

- Total revenue and number of invoices.
- Top customers by revenue (with amounts).
- Revenue by genre (for Jane's customers).
- Any obvious trend (e.g. revenue by year, if useful).

Get exact figures; do the arithmetic with the **code interpreter** if you need
to combine results.

## 2. Write the report

- Use the code interpreter to get today's date: `new Date().toISOString().slice(0, 10)`.
- `write_file` a clear Markdown report to `/outputs/territory_report-<date>.md`:
  headline totals, a top-customers list, and a revenue-by-genre table.

## 3. Chart

Call `render_pie_chart` with the revenue-by-genre labels and values, saved as
`territory_chart.png`. Reference the image in the report.

## Done

Tell Jane where the report and chart were saved, with the headline revenue
number.
