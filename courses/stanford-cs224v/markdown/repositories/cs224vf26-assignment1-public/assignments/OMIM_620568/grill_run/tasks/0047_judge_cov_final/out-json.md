# Homework 1 public teaching repository: assignments/OMIM_620568/grill_run/tasks/0047_judge_cov_final/out.json

[Course index](../../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/cs224vf26-assignment1-public/blob/HEAD/assignments/OMIM_620568/grill_run/tasks/0047_judge_cov_final/out.json) · [Raw file](../../../../../../../../raw/repositories/cs224vf26-assignment1-public/assignments/OMIM_620568/grill_run/tasks/0047_judge_cov_final/out.json)

Retrieved: 2026-11-13T16:58:36.902200+00:00

```json
{
  "fields": [
    {
      "field": "Reported clinical phenotypes in affected individuals, including verbatim wording from the paper and standard HPO term if identifiable",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Phenotype frequencies with exact numerator and denominator per cohort (not percentage alone)",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Resolvable source citation (PMID or DOI) and cohort identification for every reported frequency",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Most discriminating findings present in most affected individuals but uncommon in usually confused disorders",
      "covered": true,
      "contributing_aspects": [
        "discriminating_features",
        "limb defects",
        "genotype-phenotype"
      ]
    },
    {
      "field": "Names of overlapping disorders usually confused with Cornelia de Lange syndrome 6 and confidence level of the distinction",
      "covered": true,
      "contributing_aspects": [
        "discriminating_features"
      ]
    },
    {
      "field": "Findings looked for and found absent in affected individuals (findings that argue against the diagnosis)",
      "covered": true,
      "contributing_aspects": [
        "exclusionary_findings",
        "limb defects",
        "discriminating features",
        "genotype-phenotype"
      ]
    },
    {
      "field": "Differences in phenotype by variant type, variant position, age, or sex",
      "covered": true,
      "contributing_aspects": [
        "craniofacial dysmorphism",
        "phenotype by age",
        "differential diagnosis"
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
