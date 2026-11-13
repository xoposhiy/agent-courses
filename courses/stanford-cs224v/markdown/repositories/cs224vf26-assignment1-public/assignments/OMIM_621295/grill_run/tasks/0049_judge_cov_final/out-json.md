# Homework 1 public teaching repository: assignments/OMIM_621295/grill_run/tasks/0049_judge_cov_final/out.json

[Course index](../../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/cs224vf26-assignment1-public/blob/HEAD/assignments/OMIM_621295/grill_run/tasks/0049_judge_cov_final/out.json) · [Raw file](../../../../../../../../raw/repositories/cs224vf26-assignment1-public/assignments/OMIM_621295/grill_run/tasks/0049_judge_cov_final/out.json)

Retrieved: 2026-11-13T16:58:36.902200+00:00

```json
{
  "fields": [
    {
      "field": "Clinical phenotypes reported in affected individuals with exact numerator and denominator per cohort (not percentage alone)",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Phenotype wording as stated in the source paper plus standard HPO term if identifiable",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "PMID or DOI and cohort attribution for every reported phenotype frequency",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Most discriminating clinical findings present in most affected individuals but uncommon in overlapping disorders",
      "covered": true,
      "contributing_aspects": [
        "neuroimaging",
        "periatrial volume loss",
        "periventricular leukomalacia phenocopy",
        "microcalcifications",
        "anterior temporal pole sparing",
        "differential diagnosis"
      ]
    },
    {
      "field": "Specific disorders usually confused with this disease and the confidence level of the phenotypic distinction",
      "covered": true,
      "contributing_aspects": [
        "Differential discrimination against CARASIL",
        "neuroimaging",
        "periventricular leukomalacia phenocopy",
        "anterior temporal pole sparing",
        "differential diagnosis"
      ]
    },
    {
      "field": "Findings specifically evaluated and confirmed ABSENT in affected individuals that argue against the diagnosis",
      "covered": true,
      "contributing_aspects": [
        "Differential discrimination against CARASIL",
        "anterior temporal pole sparing",
        "differential diagnosis"
      ]
    },
    {
      "field": "Phenotypic differences or correlations by variant type, variant position, age, or sex",
      "covered": true,
      "contributing_aspects": [
        "genotype-phenotype correlation",
        "age of onset",
        "variant mechanism",
        "genotype_phenotype",
        "genotype-phenotype divergence",
        "variant_stratification"
      ]
    },
    {
      "field": "Findings reported by one paper and explicitly contradicted by another",
      "covered": false,
      "contributing_aspects": []
    }
  ]
}
```
