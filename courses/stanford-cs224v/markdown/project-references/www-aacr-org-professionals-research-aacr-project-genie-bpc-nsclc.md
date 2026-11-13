# Project background: www.aacr.org/professionals/research/aacr-project-genie/bpc/nsclc/

[Course index](../../README.md) · [Original source](https://www.aacr.org/professionals/research/aacr-project-genie/bpc/nsclc/) · [Raw file](../../raw/project-references/www-aacr-org-professionals-research-aacr-project-genie-bpc-nsclc.html)

Retrieved: 2026-11-13T17:07:16.070900+00:00

# BPC NSCLC v2.0-public

The AACR Project GENIE® BPC NSCLC v2.0-public dataset contains 1,846 non-small cell lung cancer patients from four institutions: MSKCC, DFCI, VICC and UHN.

Read the BPC Core Team’s [publication introducing the GENIE® BPC NSCLC cohort](https://aacrjournals.org/clincancerres/article/29/17/3418/728542/The-GENIE-BPC-NSCLC-Cohort-A-Real-World-Repository), a real-world repository integrating standardized clinical and genomic data from 1,846 patients with non–small cell lung cancer.

### Data Access:

- A subset of the data is available through [cBioPortal](https://genie.cbioportal.org/study/summary?id=nsclc_public_genie_bpc). Both the genomic and clinical (phenomic) data can be evaluated in cBioPortal with opportunities for data exploration and visualization using a user-friendly interface.
- The complete, post-processed data are available on [Synapse.](https://www.synapse.org/Synapse:syn27056697)

See an [overview of the data set](https://www.aacr.org/wp-content/uploads/2023/01/2022_NSCLC-2.0-Public_graphics.pdf).

### What is included in Project GENIE BPC data?

- **Genomic Data:** Clinical-grade next-generation sequencing data for each patient from the AACR Project GENIE® registry. Genomic profiling was performed between 2014 and 2018.
- **Cancer Diagnosis:**NSCLC cancer diagnosis is considered the index tumor for this patient cohort. There are data about other cancer diagnoses antecedent to the NSCLC and subsequent to the NSCLC.
- **Pathologic Information:** Each pathology specimen from diagnosis through death or last follow-up is curated with specimen type, site, and histology.
- **Treatment Histories:** All anti-neoplastic systemic therapies–intravenous and oral chemotherapies–are included in the dataset. Dates are provided as intervals from diagnosis to start and stop of each drug. Investigational drugs are masked, no dosing information is included.
- **Imaging Information:** Each CT, MRI, PET-CT scan from diagnosis through death or last follow-up is curated for the presence or absence of cancer and an evaluation of whether the cancer was stable, responding, or progressing. These data are used to compute progression-free survival-imaging (PFS-I). Sites of tumor involvement are also recorded.
- **Medical Oncologist’s Evaluations:** Medical oncology notes (1/month) have been curated to ascertain the presence or absence of cancer and whether the cancer was stable, responding, or progressing. These data are used to compute progression-free survival-medonc (PFS-M) from diagnosis through death or date of last follow-up.
- **Overall Survival:** Overall survival is based on death with censoring at date of last contact known alive. Ascertainment of death varies by institution.
- **Additional Relevant Biomarkers:** Information about select biomarkers not included on the NGS panels, including PDL1, PD1 and MSI, are also curated. Note that MSI data is currently not exposed in the cBioPortal for this cohort, but can be accessed in raw data files found in [Synapse](https://www.synapse.org/Synapse:syn27056697).
- **Patient-Reported Outcomes:** There are no patient (self-) reported outcomes in the data.
- **Date Masking:** Exact date fields have been masked to preserve confidentiality. However, exact date intervals are available and allow for calculation of the time between events, e.g., diagnosis, treatment start, treatment end, PFS-I, PFS-M, OS, etc.
- **PRISSMM™:** the BPC NSCLC dataset uses the PRISSMM™ system licensed and enhanced by Memorial Sloan-Kettering Cancer Center, Memorial Hospital for Cancer and Allied Diseases, and Sloan-Kettering Institute for Cancer Research (collectively “MSK”) is for informational and research purposes only. The content is not intended as a substitute for professional medical advice, diagnosis, or treatment. Original system and improvements © 2019-2022 Dana-Farber Cancer Institute, Inc. Additional functionality and enhancements © 2023 MSK. All rights reserved. Additional information can be found in the analytic data guide and information about licensing PRISSMM™ can be obtained by emailing [PRISSMM@mskcc.org](mailto:PRISSMM@mskcc.org).
- **Resources:**
  - **Analytical Data Guide:** A more comprehensive overview of the data can be found in [the data guide](https://www.aacr.org/wp-content/uploads/2022/05/GENIE-BPC-NSCLC-v2.0-public-Analytic-Data-Guide-1.pdf), and a description and location of the variables collected can be found in [the variable synopsis spreadsheet](https://www.aacr.org/wp-content/uploads/2022/05/BPC_NSCLC_v2.0-public_variable_synopsis_posted.xlsx).
  - A dedicated [project wiki](https://www.synapse.org/Synapse:syn27056172/wiki/616601) describes each of the files and the data structure.
  - **Training Videos:**
    - BPC-specific cBioPortal video training [playlist](https://www.youtube.com/watch?v=leDlA48NKPA&list=PLE2tjlUyHL8Gn4ythnuvf2BxWJVpAxkMM).
    - Demo of Project GENIE® Data on the Synapse and cBioPortal Platforms:
