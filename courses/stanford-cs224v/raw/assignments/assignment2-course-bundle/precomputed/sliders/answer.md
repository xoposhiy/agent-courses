# For this disease report, we want to understand how to use disease profile for matching to patient phenotypes data to identify the disease.

To match a patient's phenotypes against disease profiles to identify a disease, clinical phenotype data is evaluated using the following framework of rules and criteria:

1. **Inclusion Criteria (`inclusion_criterion`)**:
   - **`must_be_present`**: Mandatory core features required to establish baseline suspicion for the disease (e.g., Intellectual Disability in LRRC7-Related Intellectual Developmental Disorder).
   - **`supportive_if_present`**: Non-mandatory features that bolster diagnostic likelihood if detected.
   - **`variable`**: Features that vary across patient subgroups or disease severity levels.

2. **Exclusion Criteria (`exclusion_criterion`)**:
   - **`must_be_absent`**: 'Red flag' features or pertinent negatives. The presence of any such phenotype strongly rules out or argues against the diagnosis (e.g., Severe Congenital Heart Defects in Fliedner-Zweier syndrome).

3. **Discriminating Features (`discriminating_feature`)**:
   - Specific phenotypic triads, neuroimaging biomarkers, or cardinal signs that differentiate the disease from clinical mimics (e.g., severe intellectual disability, hyperkinetic movement disorders, and episodic respiratory dysrhythmia in DEE119).

4. **Algorithm Steps & Diagnostic Scoring Rules (`algorithm_step`, `diagnostic_scoring_rule`)**:
   - Decision steps in diagnostic workflows that require specific findings to be present (`must_be_present`) or absent (`must_be_absent`) to filter down candidate conditions.

5. **Differential Matching (`phenotypic_differential_matching`)**:
   - Evaluates overlapping features shared with mimic diseases and applies specific discriminating logic to rule out mimics and confirm the target diagnosis.

## Citations
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_620511/report.md:1-55 (phenotypic_matching_rules.disease_name): # Clinical Identification and Phenotypic Delineation of Fliedner-Zweier Syndrome (SCAF4-Related Neurodevelopmental Disorder)

Fliedner-Zweier syndrome (FZS; OMIM #620511) is an autosomal dominant neurodevelopmental condition caused by heterozygous loss-of-function variants in *SCAF4* (SR-related CTD-associated factor 4), which encodes an RNA polymerase II CTD-binding factor critical for mRNA transcription termination and suppression of premature cleavage and polyadenylation [F1, F2]. While early ascertainment suggested a uniform, recognizable presentation, recent cohort expansions encompassing at least 68 to 69 cumulative individuals across international series have revealed significant variable expressivity and incomplete penetrance [F1, F2, F18].

---

## 1. Phenotypic Spectrum and Documented Clinical Frequencies

Identifying an individual with Fliedner-Zweier syndrome from clinical phenotype alone is exceptionally difficult because its core features overlap broadly with common neurodevelopmental presentations [F2, F5]. Across documented cohorts, prominent developmental delay and expressive speech impairment represent the most consistently penetrant features, even in individuals with preserved or borderline general intellectual abilities [F4, F5, F7].

### Cohort-Level Frequencies and Verbatim Phenotypes

| Cohort / Source | Verbatim Clinical Finding | Human Phenotype Ontology (HPO) Term | Count / Assessed Individuals (Fraction, %) | Finding Attribution |
| :--- | :--- | :--- | :--- | :--- |
| **Schmid et al. (2025)**<br>(DOI: [10.1038/s41431-024-01760-2](https://doi.org/10.1038/s41431-024-01760-2)) | Developmental delay / intellectual disability spectrum (ranging from normal IQ to severe ID) | Intellectual disability (HP:0001249) / Global developmental delay (HP:0001263) | Evaluated across an expanded multicenter cohort of 50 novel individuals (incomplete penetrance demonstrated; normal IQ observed in transmitting carriers and select probands) | [F1, F4, F7] |
| **Schmid et al. (2025)**<br>(DOI: [10.1038/s41431-024-01760-2](https://doi.org/10.1038/s41431-024-01760-2)) | Inherited loss-of-function transmission | Autosomal dominant inheritance (HP:0000006) | 13/50 inherited cases (with 23/50 de novo cases established in cohort) | [F1, F11, F15] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Developmental delay and/or intellectual disability | Intellectual disability (HP:0001249) | 13/13 (100%) in initial discovery series (9 distinct pathogenic germline variants identified) | [F4, F10] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Speech and language impairment | Speech delay (HP:0000750) | 13/13 (100%) in initial discovery series | [F7, F10] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Muscular hypotonia | Muscular hypotonia (HP:0001252) | 9/12 (75%) | [F10] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Behavioral abnormalities (e.g., ADHD, autistic features) | Abnormal repetitive mannerism / Behavioral abnormality (HP:0000708) | 8/11 (73%) | [F10] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Facial dysmorphic features | Facial dysmorphism (HP:0001999) | 11/13 (85%) | [F10] |
| **Fliedner et al. (2020)**<br>(DOI: [10.1016/j.ajhg.2020.06.019](https://doi.org/10.1016/j.ajhg.2020.06.019)) | Inherited transmission in discovery series | Autosomal dominant inheritance (HP:0000006) | 1/9 (11%) families (8/9 de novo) | [F1, F11] |
| **Hu et al. (2024)**<br>(DOI: [10.1016/j.seizure.2023.09.006](https://doi.org/10.1016/j.seizure.2023.09.006)) | Seizures / focal epilepsy | Focal-onset seizure (HP:0007359) / Seizure (HP:0001250) | 3/3 (100%) in epilepsy-ascertained series (median onset age: 4 years) | [F9, F13] |
| **Hu et al. (2024)**<br>(DOI: [10.1016/j.seizure.2023.09.006](https://doi.org/10.1016/j.seizure.2023.09.006)) | Normal brain MRI | Normal brain morphology (HP:0002534) | 2/3 (66.7%) structurally normal on neuroimaging | [F9] |
| **Schmid et al. (2025)**; **Chen et al. (2025)**<br>(DOI: [10.1038/s41431-024-01760-2](https://doi.org/10.1038/s41431-024-01760-2); [10.3389/fgene.2025.1487352](https://doi.org/10.3389/fgene.2025.1487352)) | Skeletal abnormalities (clubfoot, scoliosis, hip dysplasia) | Talipes equinovarus (HP:0001762), Scoliosis (HP:0002650), Hip dysplasia (HP:0001385) | Recurrent core syndromic finding noted across 50 novel cases and cumulative 69 reviewed patients | [F2, F5, F12] |
| **Yan et al. (2025)**<br>(PMID: [41811042](https://pubmed.ncbi.nlm.nih.gov/41811042/)) | Isolated de novo Chinese case evaluation | Global developmental delay (HP:0001263) | 1/1 evaluated proband (age 4.58 years) | [F1, F2, F10] |

---

## 2. Discriminative Features and Clinical Differential Diagnosis

Bedside differentiation of Fliedner-Zweier syndrome solely on clinical criteria is **not achievable with moderate or high clinical confidence**, and the confidence of bedside distinction without sequencing is very low [F2, F15]. Fliedner-Zweier syndrome exhibits extensive phenotypic pleiotropy: affected individuals present with non-specific developmental delay, a wide cognitive spectrum (from completely normal IQ or borderline intellectual disability to severe ID), variable speech delay, behavioral abnormalities (ADHD, autism spectrum traits), skeletal anomalies, and seizures [F1, F2, F4, F5].

### Confused Overlapping Disorders and Confidence of Distinction

1. **Spliceosomal and Transcription-Elongation Machinery Syndromes**:
   - *Overlapping entities*: *SRRM1*-related neurodevelopmental disorder (Altay et al., 2026, [10.1038/s41431-025-01966-y](https://doi.org/10.1038/s41431-025-01966-y)), *THOC6*-related neurodevelopmental disorder, *RNU4ATAC*-related microcephalic dwarfism/syndromes, and *SCAF8*-associated conditions [F2, F15].
   - *Overlapping findings*: Shared disruption of general mRNA transcription elongation and splicing creates converging clinical phenotypes involving developmental delay, speech limitations, muscular hypotonia, and non-specific skeletal anomalies [F2, F15].
   - *Confidence of bedside distinction*: **Very Low (<0.30)**. Transcriptome deregulations affect thousands of downstream targets (e.g., >9,000 deregulated genes and ~2,900 differentially spliced transcripts [F2]), producing convergent neurodevelopmental disruptions that cannot be separated clinically without exome or genome sequencing [F2, F15].
2. **Chromatin Remodeling Syndromes (e.g., Coffin-Siris Syndrome, *ARID1B* / *SMARCA4*)**:
   - *Overlapping findings*: Muscular hypotonia, intellectual impairment, expressive language delay, and subtle craniofacial dysmorphisms [F15].
   - *Discriminating clues*: Coffin-Siris and related SWI/SNFopathies frequently show fifth-digit nail/distal phalanx hypoplasia, pronounced coarse facial coarsening, and structural internal organ malformations, whereas FZS dysmorphism remains subtle and unclassifiable [F10, F15].
   - *Confidence of bedside distinction*: **Low to Moderate**. While digit hypoplasia points toward Coffin-Siris, genomic sequencing remains mandatory [F2, F15].

### Most Discriminating Features of Fliedner-Zweier Syndrome
When comparing an affected individual to patients with generic neurodevelopmental delay, the combination of features that raises suspicion includes:
- **Severe expressive language delay relative to general cognitive performance**: Speech deficits are consistently penetrant even in patients who preserve mild or near-normal non-verbal cognitive capacities [F4, F7].
- **Co-occurrence of axial and lower-extremity joint positional anomalies**: Recurrent skeletal signs specifically encompass scoliosis, developmental dysplasia of the hip, and clubfoot (talipes equinovarus) [F5, F12].
- **Pharmacoresponsive focal epilepsy**: When seizures occur (median onset around 4 years of age), they often present as focal seizures responsive to standard anti-seizure medications [F9, F13].

---

## 3. Exclusionary Criteria: Absent Features that Argue Against Diagnosis

Because positive findings are heterogeneous, negative criteria provide critical exclusionary value. Systematic evaluation of large cohorts (Schmid et al., 2025; Yan et al., 2025; n = 50 novel cases, 69 total reviewed) establishes that the following findings are **consistently absent** in Fliedner-Zweier syndrome; their presence argues strongly against the diagnosis [F6]:
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_620511/report.md:57 (phenotypic_matching_rules.phenotype_name): 1. **Severe Congenital Heart Defects**: Complex cardiac malformations requiring early surgical intervention (such as transposition of the great arteries, hypoplastic left heart syndrome, or tetralogy of Fallot) have not been observed as core features of *SCAF4* haploinsufficiency [F6].
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_620511/report.md:55-57 (phenotypic_matching_rules.rule_category): Because positive findings are heterogeneous, negative criteria provide critical exclusionary value. Systematic evaluation of large cohorts (Schmid et al., 2025; Yan et al., 2025; n = 50 novel cases, 69 total reviewed) establishes that the following findings are **consistently absent** in Fliedner-Zweier syndrome; their presence argues strongly against the diagnosis [F6]:

1. **Severe Congenital Heart Defects**: Complex cardiac malformations requiring early surgical intervention (such as transposition of the great arteries, hypoplastic left heart syndrome, or tetralogy of Fallot) have not been observed as core features of *SCAF4* haploinsufficiency [F6].
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_620511/report.md:55-57 (phenotypic_matching_rules.phenotype_status_required): Because positive findings are heterogeneous, negative criteria provide critical exclusionary value. Systematic evaluation of large cohorts (Schmid et al., 2025; Yan et al., 2025; n = 50 novel cases, 69 total reviewed) establishes that the following findings are **consistently absent** in Fliedner-Zweier syndrome; their presence argues strongly against the diagnosis [F6]:

1. **Severe Congenital Heart Defects**: Complex cardiac malformations requiring early surgical intervention (such as transposition of the great arteries, hypoplastic left heart syndrome, or tetralogy of Fallot) have not been observed as core features of *SCAF4* haploinsufficiency [F6].
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_620511/report.md:1-47 (phenotypic_matching_rules.disease_name): # Clinical Identification and Phenotypic Delineation of Fliedner-Zweier Syndrome (SCAF4-Related Neurodevelopmental Disorder)

Fliedner-Zweier syndrome (FZS; OMIM #620511) is an autosomal dominant neurodevelopmental condition caused by heterozygous loss-of-function variants in *SCAF4* (SR-related CTD-associated factor 4), which encodes an RNA polymerase II CTD-binding factor critical for mRNA transcription termination and suppression of premature cleavage and polyadenylation [F1, F2]. While early ascertainment suggested a uniform, recognizable presentation, recent cohort expansions encompassing at least 68 to 69 cumulative individuals across international series have revealed significant variable expressivity and incomplete penetrance [F1, F2, F18].

---

## 1. Phenotypic Spectrum and Documented Clinical Frequencies

Identifying an individual with Fliedner-Zweier syndrome from clinical phenotype alone is exceptionally difficult because its core features overlap broadly with common neurodevelopmental presentations [F2, F5]. Across documented cohorts, prominent developmental delay and expressive speech impairment represent the most consistently penetrant features, even in individuals with preserved or borderline general intellectual abilities [F4, F5, F7].

### Cohort-Level Frequencies and Verbatim Phenotypes

| Cohort / Source | Verbatim Clinical Finding | Human Phenotype Ontology (HPO) Term | Count / Assessed Individuals (Fraction, %) | Finding Attribution |
| :--- | :--- | :--- | :--- | :--- |
| **Schmid et al. (2025)**<br>(DOI: [10.1038/s41431-024-01760-2](https://doi.org/10.1038/s41431-024-01760-2)) | Developmental delay / intellectual disability spectrum (ranging from normal IQ to severe ID) | Intellectual disability (HP:0001249) / Global developmental delay (HP:0001263) | Evaluated across an expanded multicenter cohort of 50 novel individuals (incomplete penetrance demonstrated; normal IQ observed in transmitting carriers and select probands) | [F1, F4, F7] |
| **Schmid et al. (2025)**<br>(DOI: [10.1038/s41431-024-01760-2](https://doi.org/10.1038/s41431-024-01760-2)) | Inherited loss-of-function transmission | Autosomal dominant inheritance (HP:0000006) | 13/50 inherited cases (with 23/50 de novo cases established in cohort) | [F1, F11, F15] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Developmental delay and/or intellectual disability | Intellectual disability (HP:0001249) | 13/13 (100%) in initial discovery series (9 distinct pathogenic germline variants identified) | [F4, F10] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Speech and language impairment | Speech delay (HP:0000750) | 13/13 (100%) in initial discovery series | [F7, F10] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Muscular hypotonia | Muscular hypotonia (HP:0001252) | 9/12 (75%) | [F10] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Behavioral abnormalities (e.g., ADHD, autistic features) | Abnormal repetitive mannerism / Behavioral abnormality (HP:0000708) | 8/11 (73%) | [F10] |
| **Fliedner et al. (2020)**<br>(PMID: [33232675](https://pubmed.ncbi.nlm.nih.gov/33232675/); DOI: [10.1016/j.ajhg.2020.07.003](https://doi.org/10.1016/j.ajhg.2020.07.003)) | Facial dysmorphic features | Facial dysmorphism (HP:0001999) | 11/13 (85%) | [F10] |
| **Fliedner et al. (2020)**<br>(DOI: [10.1016/j.ajhg.2020.06.019](https://doi.org/10.1016/j.ajhg.2020.06.019)) | Inherited transmission in discovery series | Autosomal dominant inheritance (HP:0000006) | 1/9 (11%) families (8/9 de novo) | [F1, F11] |
| **Hu et al. (2024)**<br>(DOI: [10.1016/j.seizure.2023.09.006](https://doi.org/10.1016/j.seizure.2023.09.006)) | Seizures / focal epilepsy | Focal-onset seizure (HP:0007359) / Seizure (HP:0001250) | 3/3 (100%) in epilepsy-ascertained series (median onset age: 4 years) | [F9, F13] |
| **Hu et al. (2024)**<br>(DOI: [10.1016/j.seizure.2023.09.006](https://doi.org/10.1016/j.seizure.2023.09.006)) | Normal brain MRI | Normal brain morphology (HP:0002534) | 2/3 (66.7%) structurally normal on neuroimaging | [F9] |
| **Schmid et al. (2025)**; **Chen et al. (2025)**<br>(DOI: [10.1038/s41431-024-01760-2](https://doi.org/10.1038/s41431-024-01760-2); [10.3389/fgene.2025.1487352](https://doi.org/10.3389/fgene.2025.1487352)) | Skeletal abnormalities (clubfoot, scoliosis, hip dysplasia) | Talipes equinovarus (HP:0001762), Scoliosis (HP:0002650), Hip dysplasia (HP:0001385) | Recurrent core syndromic finding noted across 50 novel cases and cumulative 69 reviewed patients | [F2, F5, F12] |
| **Yan et al. (2025)**<br>(PMID: [41811042](https://pubmed.ncbi.nlm.nih.gov/41811042/)) | Isolated de novo Chinese case evaluation | Global developmental delay (HP:0001263) | 1/1 evaluated proband (age 4.58 years) | [F1, F2, F10] |

---

## 2. Discriminative Features and Clinical Differential Diagnosis

Bedside differentiation of Fliedner-Zweier syndrome solely on clinical criteria is **not achievable with moderate or high clinical confidence**, and the confidence of bedside distinction without sequencing is very low [F2, F15]. Fliedner-Zweier syndrome exhibits extensive phenotypic pleiotropy: affected individuals present with non-specific developmental delay, a wide cognitive spectrum (from completely normal IQ or borderline intellectual disability to severe ID), variable speech delay, behavioral abnormalities (ADHD, autism spectrum traits), skeletal anomalies, and seizures [F1, F2, F4, F5].

### Confused Overlapping Disorders and Confidence of Distinction

1. **Spliceosomal and Transcription-Elongation Machinery Syndromes**:
   - *Overlapping entities*: *SRRM1*-related neurodevelopmental disorder (Altay et al., 2026, [10.1038/s41431-025-01966-y](https://doi.org/10.1038/s41431-025-01966-y)), *THOC6*-related neurodevelopmental disorder, *RNU4ATAC*-related microcephalic dwarfism/syndromes, and *SCAF8*-associated conditions [F2, F15].
   - *Overlapping findings*: Shared disruption of general mRNA transcription elongation and splicing creates converging clinical phenotypes involving developmental delay, speech limitations, muscular hypotonia, and non-specific skeletal anomalies [F2, F15].
   - *Confidence of bedside distinction*: **Very Low (<0.30)**. Transcriptome deregulations affect thousands of downstream targets (e.g., >9,000 deregulated genes and ~2,900 differentially spliced transcripts [F2]), producing convergent neurodevelopmental disruptions that cannot be separated clinically without exome or genome sequencing [F2, F15].
2. **Chromatin Remodeling Syndromes (e.g., Coffin-Siris Syndrome, *ARID1B* / *SMARCA4*)**:
   - *Overlapping findings*: Muscular hypotonia, intellectual impairment, expressive language delay, and subtle craniofacial dysmorphisms [F15].
   - *Discriminating clues*: Coffin-Siris and related SWI/SNFopathies frequently show fifth-digit nail/distal phalanx hypoplasia, pronounced coarse facial coarsening, and structural internal organ malformations, whereas FZS dysmorphism remains subtle and unclassifiable [F10, F15].
   - *Confidence of bedside distinction*: **Low to Moderate**. While digit hypoplasia points toward Coffin-Siris, genomic sequencing remains mandatory [F2, F15].

### Most Discriminating Features of Fliedner-Zweier Syndrome
When comparing an affected individual to patients with generic neurodevelopmental delay, the combination of features that raises suspicion includes:
- **Severe expressive language delay relative to general cognitive performance**: Speech deficits are consistently penetrant even in patients who preserve mild or near-normal non-verbal cognitive capacities [F4, F7].
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_620511/report.md:45-47 (phenotypic_matching_rules.rule_category): ### Most Discriminating Features of Fliedner-Zweier Syndrome
When comparing an affected individual to patients with generic neurodevelopmental delay, the combination of features that raises suspicion includes:
- **Severe expressive language delay relative to general cognitive performance**: Speech deficits are consistently penetrant even in patients who preserve mild or near-normal non-verbal cognitive capacities [F4, F7].
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_620511/report.md:46-47 (phenotypic_matching_rules.phenotype_status_required): When comparing an affected individual to patients with generic neurodevelopmental delay, the combination of features that raises suspicion includes:
- **Severe expressive language delay relative to general cognitive performance**: Speech deficits are consistently penetrant even in patients who preserve mild or near-normal non-verbal cognitive capacities [F4, F7].
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621304/report.md:1 (phenotypic_matching_rules.disease_name): # Clinical Phenotypic Characterization and Diagnostic Discrimination of Developmental and Epileptic Encephalopathy 119 (DEE119; OMIM #621304)
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621304/report.md:51 (phenotypic_matching_rules.phenotype_name): ### The Discriminatory Triad
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621304/report.md:51-52 (phenotypic_matching_rules.rule_category): ### The Discriminatory Triad
A syndromic triad consisting of **severe intellectual disability**, **hyperkinetic movement disorders** (chorea, dystonia, complex hyperkinesia), and **episodic respiratory dysrhythmia** (episodic central hyperventilation and/or obstructive sleep apnea) provides greater than 80% diagnostic specificity in differentiating *RNU2-2*-associated encephalopathy from *RNU4-2*-related disorder (F4). While *RNU4-2* mutations represent one of the most frequent monogenic causes of neurodevelopmental delay, hyperventilation episodes are documented in 60% (3/5) of dominant *RNU2-2* cases (Chiu et al., 2026) and 2/14 undiagnosed movement disorder cases (Krygier et al., 2026), but are distinctly uncommon in *RNU4-2* patients (F3; F4; F10).
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621304/report.md:51-52 (phenotypic_matching_rules.phenotype_status_required): ### The Discriminatory Triad
A syndromic triad consisting of **severe intellectual disability**, **hyperkinetic movement disorders** (chorea, dystonia, complex hyperkinesia), and **episodic respiratory dysrhythmia** (episodic central hyperventilation and/or obstructive sleep apnea) provides greater than 80% diagnostic specificity in differentiating *RNU2-2*-associated encephalopathy from *RNU4-2*-related disorder (F4). While *RNU4-2* mutations represent one of the most frequent monogenic causes of neurodevelopmental delay, hyperventilation episodes are documented in 60% (3/5) of dominant *RNU2-2* cases (Chiu et al., 2026) and 2/14 undiagnosed movement disorder cases (Krygier et al., 2026), but are distinctly uncommon in *RNU4-2* patients (F3; F4; F10).
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621415/report.md:1 (phenotypic_matching_rules.disease_name): # Clinical Phenotypic Profiling and Differential Diagnosis of LRRC7-Related Intellectual Developmental Disorder (MRD77 / OMIM #621415)
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621415/report.md:17 (phenotypic_matching_rules.phenotype_name): | Global developmental delay / Intellectual disability (F4, F10) | Intellectual disability (HP:0001249) / Global developmental delay (HP:0001263) | >90% (>30/33 primary cohort; 84% developmental delay noted) | ~84%–91% | J. Willim et al. (2024, DOI: 10.1038/s41467-024-52095-x, PMID: 39256359); S. Khan et al. (2026, DOI: 10.1002/jgm.70090) |
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621415/report.md:94 (phenotypic_matching_rules.rule_category): 1. **Core Anchors (High Penetrance, >90%)**: The patient must exhibit moderate-to-severe intellectual disability and marked expressive language impairment (F4). Non-verbal or severely dyspraxic speech disproportionate to motor milestones is a hallmark (F4).
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621415/report.md:94 (phenotypic_matching_rules.phenotype_status_required): 1. **Core Anchors (High Penetrance, >90%)**: The patient must exhibit moderate-to-severe intellectual disability and marked expressive language impairment (F4). Non-verbal or severely dyspraxic speech disproportionate to motor milestones is a hallmark (F4).
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_618089/report.md:114-119 (phenotypic_matching_rules.rule_category): ```
Patient with Global Developmental Delay / Intellectual Disability
  │
  ├── [Presence of Major Malformations?]
  │     ├── Complex CHD or Limb Reduction Defect ──> ARGUES AGAINST FBXO11 (Consider CdLS, RSTS)
  │     └── Intact Limb & Cardiac Anatomy ─────────> RETAIN FBXO11 ON DIFFERENTIAL
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_618089/report.md:118-119 (phenotypic_matching_rules.phenotype_status_required):   │     ├── Complex CHD or Limb Reduction Defect ──> ARGUES AGAINST FBXO11 (Consider CdLS, RSTS)
  │     └── Intact Limb & Cardiac Anatomy ─────────> RETAIN FBXO11 ON DIFFERENTIAL
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621295/report.md:143 (phenotypic_matching_rules.rule_category): 1. **Gating Neuroimaging Criterion**: The presence of symmetrical periatrial white matter volume loss mimicking periventricular leukomalacia (PVL) with deep microcalcifications in an infant or young child with motor arrest and stroke is the primary neuroimaging signature (F4, F5, F6).
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621295/report.md:25 (phenotypic_matching_rules.phenotype_status_required): | **Periatrial white matter volume loss mimicking PVL** | Periventricular leukomalacia (`HP:0006970`) / Cerebral white matter atrophy (`HP:0012762`) | **26/26** (100%)<br>**3/3** (100%)<br>**1/1** (100%) | Biallelic LoF cohort<br>Pediatric LoF series<br>Homozygous null proband | P. Iruzubieta et al. (2024, PMC11400611) (F4, F5); M.D. Stellingwerff et al. (2022, DOI: 10.1055/a-1739-2722) (F4, F5); B. Tasharrofi et al. (2024, DOI: 10.1007/s11033-024-09560-z) (F4, F5) |
- /tmp/claude-1010/-home-harshit-AOS/fbfe1d36-d52c-4734-a352-0ef46dc6b075/scratchpad/sliders_all/ws/inputs/diseases/OMIM_621304/report.md:46 (phenotypic_differential_matching.target_disease): | ***RNU4-2*-Related Neurodevelopmental Disorder (ReNU Syndrome)** | Severe global developmental delay, profound speech impairment, microcephaly, hypotonia (F2; F4) | **Episodic central hyperventilation** (HP:0002883) and prominent hyperkinetic movement disorders (chorea, dystonia) (F3; F4). Hippocampal sclerosis on MRI (3/5 vs virtually absent in ReNU) (F14). | High-penetrance primary microcephaly (>80%) without prominent episodic hyperventilation; absence of sleep-activated multifocal discharges (F4; F14; F17). | **Moderate-to-High** (Triad of hyperkinesia, respiratory dysrhythmia, and sleep apnea yields >80% specificity against *RNU4-2*) (F4). |
