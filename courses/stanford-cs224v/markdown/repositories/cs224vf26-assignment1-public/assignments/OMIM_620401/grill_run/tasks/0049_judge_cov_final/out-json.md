# Homework 1 public teaching repository: assignments/OMIM_620401/grill_run/tasks/0049_judge_cov_final/out.json

[Course index](../../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/cs224vf26-assignment1-public/blob/HEAD/assignments/OMIM_620401/grill_run/tasks/0049_judge_cov_final/out.json) · [Raw file](../../../../../../../../raw/repositories/cs224vf26-assignment1-public/assignments/OMIM_620401/grill_run/tasks/0049_judge_cov_final/out.json)

Retrieved: 2026-11-13T16:58:36.902200+00:00

```json
{
  "fields": [
    {
      "field": "Clinical phenotypes reported in affected individuals with exact counts (numerator and denominator per cohort, not just percentage), original paper wording, and standard HPO terms where identifiable",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Source attribution for every phenotype frequency linking it to a specific cohort and a paper with a PMID or DOI",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Most discriminating findings present in most affected individuals but uncommon in overlapping disorders, along with the names of those disorders and the confidence level of the distinction",
      "covered": true,
      "contributing_aspects": [
        "Differential diagnosis and discriminating features"
      ]
    },
    {
      "field": "Findings explicitly evaluated and found absent in affected individuals whose presence argues against the diagnosis",
      "covered": true,
      "contributing_aspects": [
        "Pertinent negative findings",
        "Differential diagnosis and discriminating features"
      ]
    },
    {
      "field": "Analysis of whether the phenotype varies by variant type, variant position, age, or sex",
      "covered": true,
      "contributing_aspects": [
        "longitudinal trajectory",
        "speech phenotype",
        "short stature",
        "phenotypic spectrum",
        "syndromic vs nonsyndromic"
      ]
    },
    {
      "field": "Discrepant or contradictory findings reported between different papers",
      "covered": false,
      "contributing_aspects": []
    }
  ]
}
```
