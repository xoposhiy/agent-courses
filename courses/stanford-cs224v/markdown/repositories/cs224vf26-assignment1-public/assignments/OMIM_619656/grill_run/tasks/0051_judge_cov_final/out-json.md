# Homework 1 public teaching repository: assignments/OMIM_619656/grill_run/tasks/0051_judge_cov_final/out.json

[Course index](../../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/cs224vf26-assignment1-public/blob/HEAD/assignments/OMIM_619656/grill_run/tasks/0051_judge_cov_final/out.json) · [Raw file](../../../../../../../../raw/repositories/cs224vf26-assignment1-public/assignments/OMIM_619656/grill_run/tasks/0051_judge_cov_final/out.json)

Retrieved: 2026-11-13T16:58:36.902200+00:00

```json
{
  "fields": [
    {
      "field": "Clinical phenotypes reported in affected individuals with SMAD2-related Loeys-Dietz syndrome 6, including exact numerator and denominator per cohort (not percentage alone), the finding as worded in the paper, and the standard HPO term if identifiable",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Most discriminating findings that are present in most affected individuals but uncommon in overlapping disorders, including naming the confused disorders and stating the confidence of the distinction",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Findings looked for and found absent in affected individuals, whose presence would argue against the diagnosis",
      "covered": true,
      "contributing_aspects": [
        "negative_findings_exclusionary"
      ]
    },
    {
      "field": "Analysis of whether the phenotype differs by variant type, variant position, age, or sex",
      "covered": true,
      "contributing_aspects": [
        "genotype-phenotype",
        "variant-type",
        "phenotype_frequencies_vascular"
      ]
    },
    {
      "field": "Any finding that one paper reports and another explicitly contradicts",
      "covered": false,
      "contributing_aspects": []
    },
    {
      "field": "Attachment of every reported phenotype frequency to its specific cohort and resolvable source citation (PMID or DOI)",
      "covered": false,
      "contributing_aspects": []
    }
  ]
}
```
