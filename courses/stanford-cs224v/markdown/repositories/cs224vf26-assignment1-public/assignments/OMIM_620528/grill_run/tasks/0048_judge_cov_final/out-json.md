# Homework 1 public teaching repository: assignments/OMIM_620528/grill_run/tasks/0048_judge_cov_final/out.json

[Course index](../../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/cs224vf26-assignment1-public/blob/HEAD/assignments/OMIM_620528/grill_run/tasks/0048_judge_cov_final/out.json) · [Raw file](../../../../../../../../raw/repositories/cs224vf26-assignment1-public/assignments/OMIM_620528/grill_run/tasks/0048_judge_cov_final/out.json)

Retrieved: 2026-11-13T16:58:36.902200+00:00

```json
{
  "fields": [
    {
      "field": "Clinical phenotypes reported in affected individuals with exact frequency numerators and denominators per cohort (not percentage alone), using the paper's original wording plus standard HPO term where identifiable",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Resolvable source citation (PMID or DOI) and cohort identifier attached to every reported phenotype frequency",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Most discriminating clinical findings (common in affected individuals but uncommon in overlapping/confusing disorders), naming the specific confusing disorders and assessing confidence in the distinction",
      "covered": true,
      "contributing_aspects": [
        "Discriminating features vs mimics",
        "dHMN11",
        "deep tendon reflexes",
        "differential diagnosis"
      ]
    },
    {
      "field": "Findings looked for and found absent in affected individuals (pertinent negatives whose presence argues against the diagnosis)",
      "covered": true,
      "contributing_aspects": [
        "Pertinent negatives and exclusionary findings",
        "Pertinent negatives"
      ]
    },
    {
      "field": "Phenotype differences/correlations by variant type, variant position, age, or sex",
      "covered": true,
      "contributing_aspects": [
        "Genotype-phenotype correlation",
        "Loss-of-function mechanism",
        "dHMN11 etiology",
        "Phenotypic spectrum",
        "Distal myopathy overlap",
        "Incomplete penetrance",
        "penetrance",
        "clinical-genetics"
      ]
    },
    {
      "field": "Contradictory findings reported by one paper and explicitly contradicted by another",
      "covered": false,
      "contributing_aspects": []
    }
  ]
}
```
