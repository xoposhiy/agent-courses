# Homework 1 public teaching repository: rare_disease_diagnosis.ipynb

[Course index](../../../README.md) · [Original source](https://github.com/stanford-oval/cs224vf26-assignment1-public/blob/HEAD/rare_disease_diagnosis.ipynb) · [Raw file](../../../raw/repositories/cs224vf26-assignment1-public/rare_disease_diagnosis.ipynb)

Retrieved: 2026-11-13T16:58:36.902200+00:00

## Cell 1

```python
%load_ext autoreload
%autoreload 2
```

## Cell 2

# Finding the patient: understanding the scale of real-world problems

We have a real-world task for you all! 

You are assigned a rare disease and a cohort of patients, each described by a set of [Human Phenotype Ontology (HPO)](https://hpo.jax.org) terms. Exactly one patient has that particular rare disease. 
The task is to figure out which patient has that disease!


The central goal of this assignment is to understand **how literature research systems reach their conclusions, where they fail, and how to investigate those failures**. You should be able to explain how the system found its evidence, interpreted it, and used it to produce a ranking.

You will start with retrieval-augmented generation (RAG): retrieving relevant passages and asking a model to answer using those passages. 

Then you will then work through **GRILL** and inspect its intermediate outputs to understand what each contributes.

**GRILL** searches and reads the literature while maintaining a *belief ledger*: hypotheses, evidence for and against them, and unresolved questions. You will trace how it moves from an initial question to competing hypotheses and chooses what to investigate next.


To understand teh scale of the problem, we already run the analysis on the rag systems, and GRILL and find that RAG is only at 39% accuracy and GRILL at 53%. 

| System | top@1 | top@2 |
|--------|------:|------:|
| RAG    | 39%   | 53%   |
| GRILL  | 55%   | 70%   |

Note: we ran RAG with web-search results (providing top-6 results) and running GRILL for 2 rounds (<$2)

All the LLM runs, including Grill have been stored for you -- you don't have to use credits.

### How to work through this notebook

Cells marked **TODO** are yours. The remaining cells run as given and expose the stages you will inspect.

## Cell 3

---
# Part 0 — Setup

Run the setup cells with the project's environment. Read GRILL.md and SLIDERS.md, and locate the relevant implementation. The notebook identifies vendor/grill/src/ledger.py

## Cell 4

```python
import os, sys, json, math, textwrap, warnings
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path.cwd()
if ROOT.name == "notebook":
    ROOT = ROOT.parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))
warnings.filterwarnings("ignore")

import rdx
from rdx import extract as X, grill as G

print("python     ", sys.version.split()[0])
print("root       ", ROOT)
print("GRILL at   ", G.GRILL_ROOT)
```

```text
python      3.12.3
root        /mnt/data/oval/assignment-cs224v
GRILL at    /mnt/data/oval/assignment-cs224v/vendor/grill

```

## Cell 5

### The disease you were assigned

**TODO 0:** You are given a unique disease to investigate.

## Cell 6

```python
# ---------------------------------------------------------------------
# YOUR DISEASE. Change this line, and nothing else, to re-target the
# notebook. It must match the disease you ran setup_disease.py for.
# ---------------------------------------------------------------------
# TODO: change this to your disease ID, e.g. "OMIM:620851"
DISEASE = "OMIM:620851"
# ---------------------------------------------------------------------

from rdx import load_hpo
from rdx.phenopackets import PhenopacketStore
from rdx.disease import DiseaseBrief

hpo   = load_hpo("data")                              # ~4 s
store = PhenopacketStore.load(ontology=hpo.ontology)  # ~7 s
brief = DiseaseBrief.resolve(DISEASE, store, hpo)

TARGET = DISEASE            # the rest of the notebook uses this name

print(brief.summary())
```

```text
ReNU syndrome  (OMIM:620851)
  gene                 RNU4-2  RNA, U4 small nuclear 2
                       snRNA, 12q24.23, NCBI Gene 26834
                       also called NEDHAFA, RENU, RNU4-1B, RNU4B1, RNU4C
  curated HPO terms    198
  case reports         3 PMIDs
  curated from         3 references
  literature query     "RNU4-2" OR "ReNU syndrome"

```

## Cell 7

---

# 1 Using RAG

Retrieval Augmented Generation (RAG) is an artificial intelligence technique that improves LLMs responses by fetching relevant data from an external knowledge base before generating an answer.

We will start with obtaining search query results. Then we will feed the LLM with the fetched result and ask it to describe the disease. Finally, we will ask it to rank patients.

## 1.1 Searching with API

The initial search returns titles, URLs, and short snippets. It does not mean the model has read those pages or their full papers. A search snippet can omit qualifications or combine surrounding material in misleading ways.

## Cell 8

```python
import urllib.request

## Step 1: First build your query

query = f"{brief.gene} gene {brief.label}"

## Step 2: Make an API call to the web search API
# We have already pre-fetched the results for your disease.
sim = json.loads((ROOT / "assignments" / DISEASE.replace(":", "_") / "rag_simulation.json").read_text())
hits = sim["search"]["hits"]

## Step 3: Print the search query results
print(f"query sent to the search engine: {sim['search']['query']!r}")
print(f"generated {sim['generated']}\n")
print(f"the {len(hits)} results, exactly as returned:\n")
for i, h in enumerate(hits, 1):
    print(f"[{i}] {h['title']}")
    print(f"    {h['link']}")
    print(textwrap.fill(h.get('snippet', ''), 90, initial_indent="    ", subsequent_indent="    "))
    print()
```

```text
query sent to the search engine: 'RNU4-2 gene ReNU syndrome'
generated 2026-09-28 20:48

the 6 results, exactly as returned:

[1] RNU4-2–Related Autosomal Dominant Neurodevelopmental ...
    https://www.ncbi.nlm.nih.gov/books/NBK622730/
    RNU4-2–related autosomal dominant neurodevelopmental disorder (ReNU syndrome) is
    characterized by moderate-to-severe developmental delay (DD) ...

[2] De novo variants in the RNU4-2 snRNA cause a frequent ...
    https://www.nature.com/articles/s41586-024-07773-7
    by Y Chen · 2024 · Cited by 179 — Biallelic variants in the noncoding RNA gene RNU4-2
    cause a recessive neurodevelopmental syndrome with distinct white matter changes.
    Article ...

[3] RNU4-2 / ReNU Syndrome | Join Research Today for Hope
    https://www.renusyndrome.org/
    ReNU syndrome is a spliceosomal disorder with a defined mutational hotspot and growing
    global dataset, creating a uniquely actionable opportunity for ...

[4] RNU4-2 | UDN
    https://undiagnosed.hms.harvard.edu/genes/rnu4-2/
    In 2024, an international group of researchers found that de novo changes in RNU4-2
    cause a neurodevelopmental condition called ReNU syndrome.

[5] From RNU4-2 Variants to Clinical Phenotypes
    https://www.neurology.org/doi/10.1212/NXG.0000000000200312
    by P Di Letto · 2025 · Cited by 7 — ReNU syndrome, also known as NDD with hypotonia,
    brain anomalies, distinctive facies, and absent language (NEDHAFA). RNU4-2 variants
    exhibited ...

[6] RNU4-2 - ReNU syndrome
    https://rarechromo.org/media/singlegeneinfo/Single%20Gene%20Disorder%20Guides/ReNU%20syndrome%20FTNW.pdf
    ReNU syndrome is caused by specific changes (known as pathogenic variants) to the DNA
    sequence of the RNU4-2 gene. Genes are instructions that have important ...


```

## Cell 9

**TODO 1.1**: Write the about what kinds of urls do you see? Are they databases, published articles, blogpost, news reporting etc.

## Cell 10

## 1.2 What a context to the LLM looks like

In the cell above you see six titles, six links, six snippets of a sentence or two. That is all the
retrieval step returns; nobody has read a paper yet. 

The next cell turns it into the **context** for the model

A **system** message gives the LLM high-priority instructions about how it should behave. A **user** message contains the user’s request or input that the LLM should respond to.

This is the task we will give the LLM:

```
Task: In about 150 words, describe the gene RNU4-2 and its relation to ReNU syndrome:
what the gene product is, what it does in the cell, and how variants in it cause disease.
Every sentence needs a citation like [2].
```

## Cell 11

```python
"""A LLM call asking it to generate describe the disease based on 
retrieved information. (Beware, these might contain hallucinations!)
"""

# Build the context
context = sim["context"]

# A LLM call usually consists of System Message, User Message and the Assistant's reply.
# System message provides the high-level prompt to the llm for a conversation.

messages = [
    {"role": "system",
     "content": "Use only the numbered sources given. Cite each claim as [n]. "
                "If the sources do not support a statement, say it is not covered."},
    {"role": "user",
     "content": f"Sources:\n\n{context}\n\n"
                f"Task: In about 150 words, describe the gene {brief.gene} and its "
                f"relation to {brief.label}: what the gene product is, what it does "
                f"in the cell, and how variants in it cause disease. Every sentence "
                f"needs a citation like [2]."},
]
for m in messages:
    print(f"--- {m['role']} ({len(m['content'])} chars) ---")
    print(textwrap.indent(m["content"], "  "))
    print()
```

```text
--- system (126 chars) ---
  Use only the numbered sources given. Cite each claim as [n]. If the sources do not support a statement, say it is not covered.

--- user (1815 chars) ---
  Sources:

  [1] RNU4-2–Related Autosomal Dominant Neurodevelopmental ...
  https://www.ncbi.nlm.nih.gov/books/NBK622730/
  RNU4-2–related autosomal dominant neurodevelopmental disorder (ReNU syndrome) is characterized by moderate-to-severe developmental delay (DD) ...

  [2] De novo variants in the RNU4-2 snRNA cause a frequent ...
  https://www.nature.com/articles/s41586-024-07773-7
  by Y Chen · 2024 · Cited by 179 — Biallelic variants in the noncoding RNA gene RNU4-2 cause a recessive neurodevelopmental syndrome with distinct white matter changes. Article ...

  [3] RNU4-2 / ReNU Syndrome | Join Research Today for Hope
  https://www.renusyndrome.org/
  ReNU syndrome is a spliceosomal disorder with a defined mutational hotspot and growing global dataset, creating a uniquely actionable opportunity for ...

  [4] RNU4-2 | UDN
  https://undiagnosed.hms.harvard.edu/genes/rnu4-2/
  In 2024, an international group of researchers found that de novo changes in RNU4-2 cause a neurodevelopmental condition called ReNU syndrome.

  [5] From RNU4-2 Variants to Clinical Phenotypes
  https://www.neurology.org/doi/10.1212/NXG.0000000000200312
  by P Di Letto · 2025 · Cited by 7 — ReNU syndrome, also known as NDD with hypotonia, brain anomalies, distinctive facies, and absent language (NEDHAFA). RNU4-2 variants exhibited ...

  [6] RNU4-2 - ReNU syndrome
  https://rarechromo.org/media/singlegeneinfo/Single%20Gene%20Disorder%20Guides/ReNU%20syndrome%20FTNW.pdf
  ReNU syndrome is caused by specific changes (known as pathogenic variants) to the DNA sequence of the RNU4-2 gene. Genes are instructions that have important ...

  Task: In about 150 words, describe the gene RNU4-2 and its relation to ReNU syndrome: what the gene product is, what it does in the cell, and how variants in it cause disease. Every sentence needs a citation like [2].


```

## Cell 12

## 1.3 Now lets ask an LLM about the disease by providing it information from search results

## Cell 13

This is the answer generated through RAG.

## Cell 14

```python
answer = sim["gene_rag"]["answer"]
print(f"tokens in: {sim['gene_rag']['tokens_in']}   out: {sim['gene_rag']['tokens_out']}\n")
print(textwrap.fill(answer, 90))
```

```text
tokens in: 588   out: 1584

*RNU4-2* is a noncoding RNA gene that encodes a small nuclear RNA (snRNA) product [2].
While its complete mechanism of action in the cell is not explicitly detailed in the
provided sources, the condition it causes is identified as a spliceosomal disorder,
implicating it in spliceosome function [3].   ReNU syndrome is caused by pathogenic
variants, or specific changes in the DNA sequence, of the *RNU4-2* gene [6]. Disease-
causing alterations frequently occur as *de novo* mutations situated at a defined
mutational hotspot [3, 4]. Primarily recognized as an autosomal dominant
neurodevelopmental disorder, ReNU syndrome presents with moderate-to-severe developmental
delay and is also known as neurodevelopmental disorder with hypotonia, brain anomalies,
distinctive facies, and absent language (NEDHAFA) [1, 5]. Additionally, biallelic variants
in *RNU4-2* have been reported to cause a recessive neurodevelopmental syndrome marked by
distinct white matter changes [2].

```

## Cell 15

## 1.4 What happens when the don't provide this context?

## Cell 16

Now we ask LLM the same question, but ask it to generate answerr through its memory.

## Cell 17

```python
print("the question, with no sources:\n")
print(textwrap.indent(sim["gene_closed"]["messages"][0]["content"], "  "))
print("\nthe answer:\n")
print(textwrap.fill(sim["gene_closed"]["answer"], 90))
```

```text
the question, with no sources:

  In about 150 words, describe the gene RNU4-2 and its relation to ReNU syndrome: what the gene product is, what it does, how variants cause disease. Give the year the disease was first described and cite the paper.

the answer:

The ***RNU4-2*** gene encodes U4 small nuclear RNA (snRNA), an essential non-coding RNA
component of the major spliceosome. In normal cellular function, U4 snRNA base-pairs with
U6 snRNA to form the U4/U6 di-snRNP complex. This complex acts as a regulatory chaperone,
maintaining U6 in an inactive conformation until the spliceosome is properly assembled on
pre-mRNA introns for splicing.  ReNU syndrome is a neurodevelopmental disorder
characterized by severe intellectual disability, microcephaly, speech loss, and motor
impairment. It is caused by recurrent, *de novo* mutations clustering within a highly
conserved 18-base-pair region (stem II) of *RNU4-2* (most commonly single-base insertions
like n.64_65insT). These variants disrupt critical U4/U6 RNA base-pairing, impairing
spliceosome assembly and catalytic activation, which leads to widespread transcript mis-
splicing across the genome.  The disorder was first described in **2024**.  **Citation:**
Greene, D., et al. (2024). "Mutations in the U4 snRNA gene *RNU4-2* cause one of the most
prevalent monogenic neurodevelopmental disorders." *Nature*, 632(8025), 579–587.

```

## Cell 18

**TODO 1.2:** After reading the two response in 1.3 and 1.4, What is the stylistic difference betweent the two responses? What is the content difference in the two responses? Which response do you prefer? 

## Cell 19

# 2 The cohort: real published patients

Now that we have some information about the disease, lets look into the patients data.

We use [GA4GH Phenopacket
Store](https://github.com/monarch-initiative/phenopacket-store), a database with 10,377
individuals across 780 Mendelian diseases, each curated from a published case
report, each carrying HPO terms, an OMIM diagnosis, the causative variant and
the PMID it came from.

A **disease phenotype** is the set of observable signs, symptoms, physical traits, or lab results caused by a medical condition.a

**Explicit negatives.** 87% of these patients have at least one *excluded*
finding. For example: A clinician looked for phenotype: nystagmus and recorded its absence.

## Cell 20

## 2.1 Let's look at the patient cohort

In the output below you will see fields `obs` and `excl`.

`obs` means observered phenotypes
`excl` means explcuded phenotypes (explicit negatives)

## Cell 21

```python
from rdx import render_patient, cohort_overlap
from rdx.assignments import load_assignment

disease, cohort = load_assignment(DISEASE)
fields = sorted(json.loads((ROOT / "assignments" / DISEASE.replace(":", "_") / "cohort.json").read_text())[0])
print(f"{len(cohort)} patients, fields on disk: {fields}\n")
print(f"{'id':<5} {'obs':>4} {'excl':>5} {'age':>6} {'sex':<7}")
for p in cohort.patients:
    print(f"{p.patient_id:<5} {len(p.terms):4d} {len(p.excluded):5d} "
          f"{str(p.age_years):>6} {str(p.sex):<7}")
```

```text
10 patients, fields on disk: ['age_years', 'excluded', 'patient_id', 'sex', 'terms']

id     obs  excl    age sex    
P01      9    37    3.4 female 
P02     10    90    1.6 female 
P03     24     3    2.3 male   
P04      8     0   11.0 female 
P05     16     5   11.0 male   
P06     31    40    1.7 male   
P07      9     1    6.0 male   
P08     13    23    8.0 female 
P09      8     7    0.7 female 
P10     24   130    5.0 male   

```

## Cell 22

## 2.2 What one patient actually looks like to you.

Now lets take a closer look at one of the patients information. Remember all these phenotypes are already canonicalized. 

In NLP, **canonicalization** means converting different forms of the same underlying text into one standard, consistent representation. For example, `"USA"`, `"U.S.A."`, and `"United States"` might all be mapped to a single canonical form like `"United States"`. Or, `“Homo sapiens”` and `“human”` look like different labels, but they refer to the same species.

## Cell 23

```python
# feel free to change the index and check other patients
p = cohort.patients[2]
print(render_patient(p, hpo.ontology))
print("\n  recorded ABSENT:")
for t in p.excluded[:8]:
    print(f"    - {t}  {hpo.label(t)}")
if len(p.excluded) > 8:
    print(f"    ... and {len(p.excluded) - 8} more")
```

```text
### Patient P03
- age: 2.3 years
- sex: male
- phenotypes:
    - HP:0010804  Tented upper lip vermilion
    - HP:0000179  Thick lower lip vermilion
    - HP:0000341  Narrow forehead
    - HP:0000294  Low anterior hairline
    - HP:0000293  Full cheeks
    - HP:0000286  Epicanthus
    - HP:0000582  Upslanted palpebral fissure
    - HP:0000527  Long eyelashes
    - HP:0000664  Synophrys
    - HP:0003196  Short nose
    - HP:0011451  Primary microcephaly
    - HP:0001276  Hypertonia
    - HP:0000316  Hypertelorism
    - HP:0000639  Nystagmus
    - HP:0000365  Hearing impairment
    - HP:0001263  Global developmental delay
    - HP:0001249  Intellectual disability
    - HP:0002353  EEG abnormality
    - HP:0032792  Tonic seizure
    - HP:0001272  Cerebellar atrophy
    - HP:0033725  Thin corpus callosum
    - HP:0033454  Tube feeding
    - HP:0001903  Anemia
    - HP:0001873  Thrombocytopenia

  recorded ABSENT:
    - HP:0002307  Drooling
    - HP:0001252  Hypotonia
    - HP:0002317  Unsteady gait

```

## Cell 24

# 3 Patient matching with RAG

We now provide the patient data to the LLM and try to see what response do we get. But first we build the context.

## Cell 25

```python
rank_run = json.loads((ROOT / "assignments" / DISEASE.replace(":", "_") / "rag_match.json").read_text())
rank_messages = rank_run["messages"]

for m in rank_messages:
    print(f"--- {m['role']} ({len(m['content']):,} chars) ---")
    body = m["content"]
    print(textwrap.indent(body if m["role"] == "system" else body[:1500] + "\n  [... snippets and the remaining patients ...]", "  "))
    print()
```

```text
This time the model is asked for a RANKED top five, in a fixed JSON shape, so the
answer can be scored. Same six snippets; the patients now include what was looked
for and recorded ABSENT, which the report-reading step later will also see.

--- system (330 chars) ---
  You are a clinical geneticist. You are given evidence about one rare disease and a cohort of patients described by HPO terms. Exactly one patient has the disease. Use only that evidence as your knowledge of the disease. Be explicit about which findings in the report drove each placement, and about findings that argue against it.

--- user (8,392 chars) ---
  WEB SEARCH RESULTS FOR ReNU syndrome (RNU4-2, OMIM:620851):

  [1] RNU4-2–Related Autosomal Dominant Neurodevelopmental ...
  https://www.ncbi.nlm.nih.gov/books/NBK622730/
  RNU4-2–related autosomal dominant neurodevelopmental disorder (ReNU syndrome) is characterized by moderate-to-severe developmental delay (DD) ...

  [2] De novo variants in the RNU4-2 snRNA cause a frequent ...
  https://www.nature.com/articles/s41586-024-07773-7
  by Y Chen · 2024 · Cited by 179 — Biallelic variants in the noncoding RNA gene RNU4-2 cause a recessive neurodevelopmental syndrome with distinct white matter changes. Article ...

  [3] RNU4-2 / ReNU Syndrome | Join Research Today for Hope
  https://www.renusyndrome.org/
  ReNU syndrome is a spliceosomal disorder with a defined mutational hotspot and growing global dataset, creating a uniquely actionable opportunity for ...

  [4] RNU4-2 | UDN
  https://undiagnosed.hms.harvard.edu/genes/rnu4-2/
  In 2024, an international group of researchers found that de novo changes in RNU4-2 cause a neurodevelopmental condition called ReNU syndrome.

  [5] From RNU4-2 Variants to Clinical Phenotypes
  https://www.neurology.org/doi/10.1212/NXG.0000000000200312
  by P Di Letto · 2025 · Cited by 7 — ReNU syndrome, also known as NDD with hypotonia, brain anomalies, distinctive facies, and absent language (NEDHAFA). RNU4-2 variants exhibited ...

  [6] RNU4-2 - ReNU syndrome
  https://rarechromo.org/media/singlegeneinfo/Single%20Gene%20Disorder%20Guides/ReNU%20syndrome%20FTNW.pdf
  ReNU syndrome 
    [... snippets and the remaining patients ...]


```

## Cell 26

## 3.1 Running LLMs.

You will observe that in some cases, running the LLM multple times over the same context gives different results! Here we run the LLM three times on the same patient cohort.

You will observe that for each patient, the model has a for and against, and an assigned probability.

## Cell 27

```python
import pandas as pd
rows = []
for r in rank_run["rounds"]:
    for pos, c in enumerate(r["ranking"][:5], 1):
        rows.append({"round": r["round"], "position": pos, "patient": c["patient_id"],
                     "probability": c["probability"], "for": c["for"], "against": c["against"]})
ranking = pd.DataFrame(rows).set_index(["round", "position"])

display(ranking.style
          .set_properties(subset=["for", "against"],
                          **{"white-space": "normal", "text-align": "left", "max-width": "420px"})
          .format({"probability": "{:.2f}"})
          .set_caption(f"three rounds, same prompt: the model's top five for {brief.label}"))
```

three rounds, same prompt: the model's top five for ReNU syndrome

|  |  | patient | probability | for | against |
| --- | --- | --- | --- | --- | --- |
| round | position |  |  |  |  |
| 1 | 1 | P06 | 0.80 | Matches the hallmark NEDHAFA profile with absent speech, white matter hypoplasia, delayed myelination, corpus callosum hypoplasia, progressive microcephaly, facial hypotonia, and characteristic craniofacial dysmorphisms. | Atypical features present include diabetes insipidus and tortuous cerebral arteries, and systemic hypotonia is restricted to facial hypotonia. |
| 2 | P02 | 0.10 | Exhibits early neurodevelopmental delay, microcephaly, hypotonia, failure to thrive, feeding difficulties, and dysmorphic facial features. | Presents with delayed rather than completely absent speech, and neuroimaging anomalies characteristic of ReNU syndrome are not reported. |
| 3 | P01 | 0.05 | Features severe intellectual disability, profound motor delay, generalized hypotonia, and absent speech consistent with NEDHAFA. | Has unilateral renal agenesis and atrial septal defect, while numerous characteristic craniofacial dysmorphisms are explicitly recorded as absent. |
| 4 | P10 | 0.03 | Demonstrates global developmental delay, hypotonia, feeding difficulties, and corpus callosum thinning with dysmorphic facies. | Delayed myelination and corpus callosum hypoplasia are explicitly absent, cleft palate is atypical, and speech is delayed rather than absent. |
| 5 | P05 | 0.02 | Displays global developmental delay, intellectual disability, hypotonia, seizures, and cerebellar brain anomalies. | Lacks documentation of white matter abnormalities and absent speech, exhibiting behavioral disturbances not emphasized in the core ReNU phenotype. |
| 2 | 1 | P06 | 0.85 | Matches the core NEDHAFA presentation with absent speech, progressive microcephaly, brain anomalies (hypoplasia of the corpus callosum, delayed myelination, cerebral white matter hypoplasia), hypotonia, and characteristic craniofacial dysmorphisms (open mouth, tented upper lip vermilion, horizontal eyebrows). | Systemic hypotonia is restricted to facial hypotonia in the observed terms, and patient exhibits diabetes insipidus and tortuous cerebral arteries which are atypical features. |
| 2 | P01 | 0.07 | Shares core features of severe intellectual disability, complete absence of speech, and generalized hypotonia. | Has major congenital malformations (unilateral renal agenesis, atrial septal defect) and extensive recorded absences of typical craniofacial dysmorphic signs. |
| 3 | P02 | 0.04 | Presents with global developmental delay, microcephaly, hypotonia, and early feeding difficulties. | Presents with delayed rather than completely absent speech/language development and lacks documented structural brain abnormalities. |
| 4 | P10 | 0.02 | Features global developmental delay, hypotonia, and brain anomalies including a thin corpus callosum. | Has only moderate intellectual disability with severe ID recorded as absent, speech is delayed rather than absent, and presents with cleft palate. |
| 5 | P05 | 0.01 | Exhibits hypotonia, developmental delay/intellectual disability, and brain anomalies (cerebellar atrophy). | Lacks the characteristic white matter/corpus callosum defects and absent speech, and exhibits behavioral features like aggression and self-injury. |
| 3 | 1 | P06 | 0.82 | Matches all core domains of ReNU syndrome/NEDHAFA, including absent speech (absent language), facial hypotonia, distinctive white matter changes/brain anomalies (delayed myelination, hypoplasia of the corpus callosum and cerebral white matter), and characteristic craniofacial features. | Presence of diabetes insipidus and tortuous cerebral arteries are unusual features not highlighted in standard ReNU syndrome descriptions. |
| 2 | P01 | 0.07 | Displays hypotonia, severe intellectual disability, and absent speech, aligning with the severe neurodevelopmental and language deficits of ReNU syndrome. | Lacks reported brain anomalies, has unilateral renal agenesis and atrial septal defect, and a large battery of dysmorphic facial features are explicitly recorded as absent. |
| 3 | P10 | 0.05 | Features hypotonia, corpus callosum anomaly (thin corpus callosum), and distinctive craniofacial dysmorphisms. | Speech is delayed rather than absent, and severe intellectual disability and hypoplasia of the corpus callosum are documented as absent. |
| 4 | P02 | 0.03 | Presents with global developmental delay, hypotonia, microcephaly, and feeding difficulties seen in neurodevelopmental syndromes. | Speech is delayed rather than absent, and brain imaging anomalies are not reported. |
| 5 | P03 | 0.02 | Exhibits microcephaly, thin corpus callosum, severe developmental impairment, and facial features such as a tented upper lip vermilion and narrow forehead. | Presents with hypertonia while hypotonia is explicitly recorded as absent, arguing against the core NEDHAFA presentation. |

## Cell 28

**TODO 3.1:** Did repeated runs agree? They if do not disagree, do their reasoning match, please describe. If they do not match, how does their reasoning differ?

**TODO 3.2:** What is the differentiating factor in each round between the first and the second ranks?

## Cell 29

# 4 GRILL: Using Hypotheses to Guide Search

A basic literature-search system can find papers and return a list of links. GRILL goes a step further: it uses what it finds to decide **what to search for next**.

Instead of treating search as a one-time query, GRILL treats it as an iterative process. It starts with questions, searches for relevant information, forms possible explanations or claims, and then looks for evidence that supports or contradicts those claims. New evidence can lead to new hypotheses and new questions. This process continues until GRILL either reaches a sufficiently clear answer or runs out of its search budget.

You can think of GRILL as maintaining a structured research notebook while it searches.

GRILL keeps track of three main types of records:

| Record type | What it means |
|---|---|
| **Direction** | An open question or area that still needs investigation. Directions form the search **frontier**: the set of things GRILL could explore next. The `EXPLORE` step spends search budget on these directions. |
| **Hypothesis** | A possible claim or explanation that GRILL wants to test. A hypothesis moves through several stages: `proposed → screened → pooled` or `binned`, depending on what GRILL learns about it. |
| **Evidence** | A specific observation from a source that is connected to a hypothesis. Evidence is labeled as either **supporting** or **contradicting** the hypothesis. |

For example, suppose GRILL is investigating the question:

> Why do some large language models perform better when given examples in the prompt?

A **direction** might be: “Does the number of examples matter?”

From its search, GRILL might create the **hypothesis**:

> Providing more examples improves performance up to a certain point.

It could then collect **supporting evidence** from one study showing that performance improves with additional examples, and **contradicting evidence** from another study showing that too many examples can reduce performance.

Based on this evidence, GRILL may refine the hypothesis or create a new direction, such as:

> Does the usefulness of additional examples depend on the model size?

This is the main idea behind GRILL: **search produces hypotheses, hypotheses guide further search, and evidence is used to evaluate those hypotheses.**

### What to examine in this part

There are five aspects of GRILL to investigate. Each one corresponds to a TODO in the exercise.

1. **Where do directions come from?**  
   Understand how GRILL decides which open questions should be added to the search frontier.

2. **What does a hypothesis actually contain?**  
   Look at how hypotheses are represented in the system and what information GRILL stores about each one.

3. **What happens if the verifier only searches for supporting evidence?**  
   Normally, a good research process should look for both evidence that supports a hypothesis and evidence that challenges it. Investigate how GRILL's behavior changes if it only tries to confirm its hypotheses.

4. **What happens if deep hypothesis testing is skipped?**  
   Examine what GRILL loses if hypotheses are accepted or rejected without a more thorough search for evidence.

5. **How is the search budget allocated?**  
   GRILL cannot search indefinitely. Investigate how it decides which directions or hypotheses deserve more search effort and when to stop exploring them.

### Files to use

`GRILL.md` explains the intended design and behavior of the system.

`vendor/grill/src/ledger.py` contains the implementation of the ledger that keeps track of directions, hypotheses, evidence, and their state.

Use `GRILL.md` to understand **what GRILL is supposed to do**, and use `ledger.py` to understand **how those ideas are represented in code**.

## Cell 30

## 4.1 Summary of the GRILL run

In the output you will see how many directions and hypothesis did grill come up with. How many evidences it found and how much did it cost us.

## Cell 31

```python
G.add_grill_to_path()
import shutil
from src.ledger import Ledger, SourceRef, POOLED, BINNED, SCREENED, PROPOSED
from src.orchestrator import Orchestrator, Config
from src import metrics

GRILL_MODE = "read"          # "read" | "stub" | "live"

if GRILL_MODE == "read":
    # A finished run, shipped with the assignment. Nothing executes in it, so
    # it is safe inside the repository -- unlike a live run, see 2.6.
    RUN_DIR = ROOT / "assignments" / DISEASE.replace(":", "_") / "grill_run"
else:
    RUN_DIR = G.run_dir_for(f"renu_{GRILL_MODE}")

run = G.GrillRun(RUN_DIR)
print(run)
```

```text
<GrillRun grill_run: 58 directions, 18 hypotheses (7 pooled), 108 evidence, $0.57>

```

## Cell 32

### 4.2 Where Directions Come From

In GRILL, a **direction** is an open question that the system has decided is worth spending part of its search budget on.

Directions can come from four different sources. Looking at where they came from helps you understand how the search process developed.

| Origin | Where it comes from |
|---|---|
| **Seed** | Created during `INIT`, before any literature search happens. These come from the PRIOR executor's `open_questions` and serve as the starting questions for the search. |
| **Agent** | Created during `EXPLORE`. After investigating one funded direction, GRILL may discover new questions that are worth following up on. |
| **Corrective** | Created when a hypothesis is found to be conflicted or refuted. Instead of simply discarding the failed hypothesis, GRILL turns the problem into a new question to investigate. These directions have `tests_hypothesis_id` set, which links them back to the hypothesis they are trying to resolve. |
| **Human** | Added directly by a person through GRILL's steering mechanism. These directions have `origin == "human"`. |

The **corrective directions** are especially important because they show how GRILL responds to failure.

Suppose GRILL proposes a hypothesis such as:

> “Treatment X improves symptom Y.”

During deeper testing, it might find strong evidence that contradicts this claim. A simpler search system might just reject the hypothesis and move on.

GRILL does something different. It creates a new direction such as:

> “Why is the evidence about Treatment X and symptom Y conflicting?”

In other words, **a failed hypothesis does not disappear from the research process. It becomes a new question that GRILL can investigate.**

This is an important part of GRILL's design: negative or conflicting evidence can change the direction of the search rather than simply ending it.

## Cell 33

## 4.3 Now we will look at the initial questions generated by GRILL
`promise`: This is the confidence that the LLM has on this direction. Note LLMs are known to not be well calibrated. 

`funded`: This means how many directions is the agent pursuing.

[1] Xiong, Miao, et al. "Can llms express their uncertainty? an empirical evaluation of confidence elicitation in llms." International Conference on Learning Representations. Vol. 2024. 2024.

## Cell 34

```python
import pandas as pd
from collections import Counter

D = run.directions_table()
ledger_raw = run.ledger_json

def classify(d):
    if d["tests"]:
        return "corrective"
    if d["origin"] == "human":
        return "human"
    if d["parent"] is None and "seed" in (ledger_raw["directions"][d["id"]].get("rationale") or ""):
        return "seed"
    return "agent"

for d in D:
    d["kind"] = classify(d)
print(f"{len(D)} directions:", dict(Counter(d["kind"] for d in D)))

# One ranking, not three samples. Promise is the number the allocator sorts
# by, so this is the order in which directions were offered money.
directions = (pd.DataFrame(D)
              .assign(funded=lambda t: t.spent > 0)
              .sort_values("promise", ascending=False)
              .reset_index(drop=True))
directions.index = directions.index + 1
directions.index.name = "rank"
ranked = directions.to_dict("records")          # later cells iterate this

cols = ["id", "kind", "promise", "spent", "n_hypotheses", "funded", "question"]
print(f"{int(directions.funded.sum())} of {len(directions)} directions were ever funded. "
      f"Promise decides which; the rest are the frontier that never got a turn.\n")

def show_directions(frame):
    """Full question text, wrapped; funded rows highlighted."""
    return (frame[cols].style
            .set_properties(subset=["question"],
                            **{"white-space": "normal", "text-align": "left", "max-width": "640px"})
            .format({"promise": "{:.2f}", "spent": "${:.2f}"})
            .apply(lambda r: ["background-color: #fff3cd" if r.funded else "" for _ in r], axis=1))

show_directions(directions)
```

```text
58 directions: {'seed': 4, 'agent': 43, 'corrective': 11}
4 of 58 directions were ever funded. Promise decides which; the rest are the frontier that never got a turn.


```

|  | id | kind | promise | spent | n\_hypotheses | funded | question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rank |  |  |  |  |  |  |  |
| 1 | d1 | seed | 0.95 | $0.02 | 3 | True | What are the exact numerator/denominator frequencies for specific HPO terms across the first published cohorts (Greene et al. Nature 2024, Chen et al. Nature 2024)? |
| 2 | d19 | agent | 0.95 | $0.02 | 3 | True | What are the exact numerator and denominator frequencies for specific brain MRI malformations (e.g., corpus callosum hypoplasia, delayed myelination, simplified gyral pattern) across Greene et al., Chen et al., and Barbour et al. cohorts? |
| 3 | d2 | seed | 0.92 | $0.01 | 3 | True | What specific dysmorphic features or clinical signs distinguish ReNU syndrome from Rett syndrome (MECP2) and Angelman syndrome (UBE3A/15q11-q13)? |
| 4 | d3 | seed | 0.90 | $0.01 | 4 | True | Are there clinical features that have been consistently evaluated and confirmed absent across cohorts (pertinent negatives)? |
| 5 | d55 | agent | 0.88 | $0.00 | 0 | False | What is the exact prevalence and sensitivity of congenital talipes equinovarus versus postnatal hip dysplasia across systematically phenotyped RNU4-2 multi-center cohorts? |
| 6 | d53 | agent | 0.88 | $0.00 | 0 | False | How accurately can automated computer-vision facial phenotyping tools (e.g., Face2Gene/GestaltMatcher) discriminate ReNU syndrome from Rett syndrome (MECP2) and Angelman syndrome (UBE3A)? |
| 7 | d50 | agent | 0.85 | $0.00 | 0 | False | What proportion of RNU4-2 patients present with normal brain MRI, and does normal callosal anatomy correlate with specific non-hotspot genotypes (such as 5' stem-loop variants)? |
| 8 | d41 | agent | 0.85 | $0.00 | 0 | False | What are the exact patient-level numerators and denominators for corpus callosum hypoplasia versus simplified gyral pattern specifically in the Greene et al. (2024) and Barbour et al. cohorts? |
| 9 | d46 | agent | 0.85 | $0.00 | 0 | False | What is the true population-wide penetrance of neuroimaging abnormalities in ReNU syndrome when stratifying by variant position (e.g., T-loop n.64\_65insT vs. stem III vs. maternal/milder variants)? |
| 10 | d45 | corrective | 0.85 | $0.00 | 0 | False | Resolve the conflict over: Overall neuroimaging abnormality penetrance in ReNU syndrome exceeds 90% in systematically imaged cohorts (specifically 41/45 in Chen et al.), but findings are predominantly composed of non-specific white matter reduction, delayed myelination (HP:0002188), and ventriculomegaly (HP:0002119) rather than major cortical migration defects. |
| 11 | d51 | agent | 0.85 | $0.00 | 0 | False | Does the sub-localization of RNU4-2 pathogenic variants (e.g., T-loop/quasi-pseudoknot vs. stem III vs. biallelic non-critical regions) correlate with the presence or absence of periventricular gray matter heterotopia? |
| 12 | d56 | corrective | 0.85 | $0.00 | 0 | False | Resolve the conflict over: The structural brain MRI triad of corpus callosum hypoplasia/thinning, ventriculomegaly, and reduced white matter volume is present in over 85% of ReNU syndrome patients past infancy, providing an objective neuroradiological separator from Rett syndrome and Angelman syndrome, which typically show normal neuroimaging or non-specific cerebral volume reduction. |
| 13 | d57 | agent | 0.85 | $0.00 | 0 | False | What is the exact co-occurrence frequency of all three components of the neuroradiological triad (corpus callosum hypoplasia, ventriculomegaly, and white matter reduction) in a large multi-center cohort of ReNU syndrome patients? |
| 14 | d48 | corrective | 0.85 | $0.00 | 0 | False | Resolve the conflict over: Hypoplasia or thinning of the corpus callosum (HP:0002079) is the predominant specific structural neuroimaging biomarker in ReNU syndrome, manifesting in approximately 85% of individuals undergoing brain MRI assessment. |
| 15 | d44 | agent | 0.82 | $0.00 | 0 | False | How do quantitative 3D facial imaging or automated dysmorphology tools (e.g., GestaltMatcher/Face2Gene) compare facial feature embeddings between ReNU syndrome, Angelman syndrome, and Rett syndrome? |
| 16 | d49 | agent | 0.80 | $0.00 | 0 | False | Does quantitative volumetric or morphometric corpus callosum analysis (e.g., regional thickness of isthmus/splenium relative to total cortical volume) differentiate ReNU syndrome from other syndromic microcephalies? |
| 17 | d58 | agent | 0.80 | $0.00 | 0 | False | How effectively can blinded neuroradiologists distinguish ReNU syndrome from Rett and Angelman syndrome MRI scans using a standardized diagnostic score based on white matter and callosal metrics? |
| 18 | d54 | agent | 0.79 | $0.00 | 0 | False | Does the facial gestalt of ReNU syndrome attenuate or coarsen across chronological age from infancy into adulthood? |
| 19 | d42 | agent | 0.78 | $0.00 | 0 | False | Does the frequency or severity of brain MRI malformations (e.g., delayed myelination vs. structural callosal agenesis) correlate with specific RNU4-2 structural subdomains (stem III versus T-loop)? |
| 20 | d43 | agent | 0.78 | $0.00 | 0 | False | What is the precise comparative prevalence of structural bone anomalies (clubfoot and hip dysplasia) in ReNU syndrome versus MECP2-negative Rett-like and Angelman-like cohorts? |
| 21 | d52 | agent | 0.78 | $0.00 | 0 | False | What specific transcripts involved in radial glial migration or neuronal motility show aberrant alternative 5' splice site usage in RNU4-2 mutant neural progenitor models? |
| 22 | d47 | agent | 0.78 | $0.00 | 0 | False | Are frontal simplified gyral patterns and gray matter heterotopias in ReNU syndrome true neuronal migration defects or secondary consequences of prenatal microcephalic brain growth arrest? |
| 23 | d29 | corrective | 0.74 | $0.00 | 0 | False | Resolve the conflict over: Microcephaly (HP:0000252) in ReNU syndrome is primarily postnatally acquired and rarely manifests as a detectable fetal CNS anomaly in the prenatal period. |
| 24 | d27 | corrective | 0.73 | $0.00 | 0 | False | Resolve the conflict over: The reported penetrance of epilepsy and seizures (HP:0001250) in ReNU syndrome varies significantly between initial cohorts due to differences in patient age at evaluation rather than true biological heterogeneity, with younger cohorts under-reporting seizure frequency. |
| 25 | d23 | corrective | 0.71 | $0.00 | 0 | False | Resolve the conflict over: The recurrent single-base insertion n.64\_65insT accounts for consistently 70% to 75% of pathogenic RNU4-2 variants across unselected global neurodevelopmental cohorts, with the remaining ~25% comprising distinct single-nucleotide substitutions. |
| 26 | d20 | agent | 0.68 | $0.00 | 0 | False | How do the specific frequencies of craniofacial dysmorphic features (bulbous nasal tip, downturned corners of mouth, cupped ears) compare between carriers of n.64\_65insT and carriers of non-insertion single-nucleotide variants across published cohorts? |
| 27 | d25 | agent | 0.65 | $0.00 | 0 | False | Are non-n.64\_65insT variants in RNU4-2 underdetected by targeted single-variant screening assays compared to genome sequencing? |
| 28 | d31 | agent | 0.65 | $0.00 | 0 | False | What proportion of neonates with RNU4-2 variants have occipitofrontal circumference below -2 SD at birth versus developing microcephaly during infancy? |
| 29 | d28 | agent | 0.63 | $0.00 | 0 | False | Does time-to-event (Kaplan-Meier) analysis of seizure onset across combined international ReNU cohorts resolve the discrepancy between initial cohort frequencies when stratified by specific RNU4-2 variant (n.64\_65insT vs other SNVs)? |
| 30 | d30 | agent | 0.61 | $0.00 | 0 | False | What is the gestational age of onset for head circumference deceleration in fetuses with RNU4-2 pathogenic variants? |
| 31 | d38 | corrective | 0.60 | $0.00 | 0 | False | Resolve the conflict over: True developmental milestone regression (as seen classically in Rett syndrome) is consistently absent in individuals with RNU4-2-related neurodevelopmental disorder (ReNU syndrome), making documented post-infancy loss of previously acquired motor or communicative milestones a strong negative predictor for ReNU syndrome. |
| 32 | d24 | agent | 0.59 | $0.00 | 0 | False | Does the relative frequency of RNU4-2 n.64\_65insT versus non-coding point substitutions vary significantly by parental ancestry or maternal age? |
| 33 | d32 | corrective | 0.59 | $0.00 | 0 | False | Resolve the conflict over: Congenital macrocephaly (HP:0000256) is consistently absent in heterozygous RNU4-2-related disorder, such that the presence of macrocephaly or accelerated head circumference trajectory excludes dominant ReNU syndrome. |
| 34 | d22 | agent | 0.58 | $0.00 | 0 | False | How do pertinent negatives differentiate autosomal dominant ReNU syndrome from the newly identified biallelic/recessive RNU4-2 neurodevelopmental disorder? |
| 35 | d18 | agent | 0.55 | $0.00 | 0 | False | Build on the confirmed prior: Stereotypic hand movements (HP:0000733) and hypotonia (HP:0001252) frequently lead to clinical suspicion of Rett-like or Angelman-like disorders, but lack of classic developmental regression typical of MECP2-related Rett syndrome differentiates ReNU syndrome. |
| 36 | d21 | agent | 0.53 | $0.00 | 0 | False | What is the systematic frequency of specific non-neurological negative findings (e.g., absence of major structural congenital heart disease or renal agenesis) in dominant RNU4-2 cohorts? |
| 37 | d35 | corrective | 0.52 | $0.00 | 0 | False | Re-investigate (refuted): Complete absence of neuroimaging anomalies on high-resolution brain MRI is an exclusionary finding for dominant ReNU syndrome in individuals past infancy. |
| 38 | d39 | agent | 0.52 | $0.00 | 0 | False | Is neurological regression in ReNU syndrome strictly genotype-specific (e.g., restricted to n.66A>G or other non-insertion variants) or an underreported consequence of epileptic encephalopathy across broader cohorts? |
| 39 | d26 | agent | 0.51 | $0.00 | 0 | False | What is the detailed quantitative linguistic profile and upper boundary of expressive language attainment in individuals carrying non-hotspot or inherited RNU4-2 variants? |
| 40 | d9 | corrective | 0.50 | $0.00 | 0 | False | Resolve the conflict over: Phenotypic severity correlates with specific variant positions within the 18-nt conserved region (such as the recurrent n.64\_65insT or specific single nucleotide changes), where certain single-base substitutions show mildly variable expressivity compared to the classical insertion. |
| 41 | d17 | agent | 0.48 | $0.00 | 0 | False | Build on the confirmed prior: Characteristic craniofacial dysmorphisms including prominent/cupped/dysplastic ears (HP:0000377), bulbous nasal tip (HP:0000414), wide mouth (HP:0000154) with downturned corners (HP:0002714), and full cheeks occur in 60-80% of assessed patients. |
| 42 | d36 | agent | 0.47 | $0.00 | 0 | False | What is the true population-wide penetrance of normal cranial MRI among all molecularly confirmed dominant RNU4-2 cases in large international cohorts? |
| 43 | d34 | agent | 0.47 | $0.00 | 0 | False | Do HPO entries of macrocephaly in RNU4-2 large biobank datasets reflect misattribution, relative macrocephaly secondary to severe somatic wasting, or true absolute macrocephaly? |
| 44 | d33 | agent | 0.47 | $0.00 | 0 | False | What is the exact prevalence and longitudinal trajectory of OFC (occipitofrontal circumference) Z-scores stratified specifically by variant locus (e.g., n.64\_65insT vs stem III/T-loop variants) in RNU4-2? |
| 45 | d4 | seed | 0.46 | $0.00 | 0 | False | Does the severity of microcephaly, epilepsy, or structural brain anomalies differ significantly between individuals harboring n.64\_65insT versus other recurrent non-coding point mutations? |
| 46 | d16 | agent | 0.46 | $0.00 | 0 | False | Build on the confirmed prior: Microcephaly (HP:0000252), predominantly postnatal or secondary, is present in approximately 70-85% of affected individuals across primary cohorts. |
| 47 | d15 | agent | 0.46 | $0.00 | 0 | False | How quantitatively distinguishable is the craniofacial gestalt of ReNU syndrome (RNU4-2) from that of the newly identified RNU2-2-related neurodevelopmental disorder using objective automated 3D facial analysis? |
| 48 | d37 | agent | 0.45 | $0.00 | 0 | False | How do quantitative volumetric MRI measures compare to qualitative neuroradiology evaluations in detecting subtle white matter and corpus callosum reduction in ReNU syndrome? |
| 49 | d40 | agent | 0.45 | $0.00 | 0 | False | How do quantitative splicing defect severity scores (from saturation genome editing) correlate with the presence of epilepsy and episodic neurological decline in RNU4-2-related disorders? |
| 50 | d6 | corrective | 0.44 | $0.00 | 0 | False | Resolve the conflict over: Severe global developmental delay / intellectual disability (HP:0001263 / HP:0010864) and severe speech/language impairment (HP:0000750) are present in nearly 100% of reported individuals (e.g., >95% in initial cohorts of Chen et al. 2024 and Greene et al. 2024). |
| 51 | d14 | agent | 0.43 | $0.00 | 0 | False | What is the exact penetrance and prevalence of each specific dysmorphic HPO feature across meta-analyzed cohorts totaling >100 individuals with RNU4-2 variants? |
| 52 | d12 | agent | 0.42 | $0.00 | 0 | False | What proportion of ReNU syndrome individuals have true congenital microcephaly at birth versus progressive secondary postnatal microcephaly? |
| 53 | d7 | agent | 0.40 | $0.00 | 0 | False | What proportion of RNU4-2 variant carriers have mild rather than moderate-to-severe intellectual disability, stratified by variant location (T-loop vs. stem II/k-turn/Sm-binding site)? |
| 54 | d8 | agent | 0.40 | $0.00 | 0 | False | What is the true penetrance and transmission rate of RNU4-2 variants among mildly affected or mosaic transmitting parents in familial cohorts? |
| 55 | d5 | agent | 0.40 | $0.00 | 0 | False | Does long-term surveillance reveal any subtle or late-onset loss of acquired motor/verbal skills in older cohorts of ReNU syndrome patients? |
| 56 | d11 | agent | 0.38 | $0.00 | 0 | False | Do peripheral blood DNA methylation episignatures consistently stratify cognitive and structural severity in non-n.64\_65insT single-nucleotide RNU4-2 variants? |
| 57 | d10 | agent | 0.38 | $0.00 | 0 | False | To what degree do secondary structural stability metrics (e.g., in vitro RNA duplex melting temperatures and cryo-EM tri-snRNP assembly kinetics) predict clinical severity compared to categorical linear positions? |
| 58 | d13 | agent | 0.36 | $0.00 | 0 | False | Does the trajectory of head circumference deceleration differ between the recurrent n.64\_65insT insertion and non-insertion variants in RNU4-2? |

## Cell 35

## 4.4 Now let's take a closer look at all generated hypotheses

Each hyoptheses gets a verdict of:

**Supported**: If on investigation we find evidence that supports the hypothesis.

**Refuted**: If all the evidences found for the hyopthesis refute the hypothesis.

**Conflicted**: If there are multiple evidences that support and refute the hypothesis.

## Cell 36

```python
H = run.hypotheses_table()

rank_of = {r.id: int(i) for i, r in directions.iterrows()}
question_of = dict(zip(directions.id, directions.question))

hyps = (pd.DataFrame(H)
        .rename(columns={"direction": "direction_id",
                         "n_support": "evidence_for",
                         "n_against": "evidence_against",
                         "text": "hypothesis"})
        .assign(direction_rank=lambda t: t.direction_id.map(rank_of),
                direction=lambda t: t.direction_id.map(question_of))
        .sort_values(["direction_rank", "confidence"], ascending=[True, False])
        .set_index(["direction_rank", "direction_id", "id"]))

hcols = ["status", "verdict", "confidence", "evidence_for", "evidence_against",
         "attempts", "hypothesis", "direction"]

def show_hypotheses(frame):
    """Every hypothesis in full, grouped under the direction that proposed it.
    Green: pooled. Red: refuted. Unshaded: binned as conflicted."""
    return (frame[hcols].style
            .set_properties(subset=["hypothesis", "direction"],
                            **{"white-space": "normal", "text-align": "left", "max-width": "520px"})
            .format({"confidence": "{:.2f}"})
            .apply(lambda r: ["background-color: #e6f4ea" if r.status == "pooled"
                              else "background-color: #fdecea" if r.verdict == "refuted"
                              else "" for _ in r], axis=1))

print(f"{len(hyps)} hypotheses from {hyps.index.get_level_values('direction_id').nunique()} directions, "
      f"ordered by the rank of the direction that proposed them")
show_hypotheses(hyps)
```

```text
18 hypotheses from 4 directions, ordered by the rank of the direction that proposed them

```

|  |  |  | status | verdict | confidence | evidence\_for | evidence\_against | attempts | hypothesis | direction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| direction\_rank | direction\_id | id |  |  |  |  |  |  |  |  |
| 1.000000 | d1 | h6 | binned | conflicted | 0.55 | 4 | 2 | 1 | The reported penetrance of epilepsy and seizures (HP:0001250) in ReNU syndrome varies significantly between initial cohorts due to differences in patient age at evaluation rather than true biological heterogeneity, with younger cohorts under-reporting seizure frequency. | What are the exact numerator/denominator frequencies for specific HPO terms across the first published cohorts (Greene et al. Nature 2024, Chen et al. Nature 2024)? |
| h7 | binned | conflicted | 0.45 | 5 | 1 | 1 | Microcephaly (HP:0000252) in ReNU syndrome is primarily postnatally acquired and rarely manifests as a detectable fetal CNS anomaly in the prenatal period. | What are the exact numerator/denominator frequencies for specific HPO terms across the first published cohorts (Greene et al. Nature 2024, Chen et al. Nature 2024)? |
| h8 | binned | conflicted | 0.45 | 2 | 2 | 1 | The recurrent single-base insertion n.64\_65insT accounts for consistently 70% to 75% of pathogenic RNU4-2 variants across unselected global neurodevelopmental cohorts, with the remaining ~25% comprising distinct single-nucleotide substitutions. | What are the exact numerator/denominator frequencies for specific HPO terms across the first published cohorts (Greene et al. Nature 2024, Chen et al. Nature 2024)? |
| 2.000000 | d19 | h15 | pooled | supported | 0.92 | 4 | 0 | 0 | True neuronal migration defects such as periventricular nodular heterotopia (HP:0000762) occur in less than 5-10% of ReNU syndrome individuals, making the presence of extensive lissencephaly or subcortical band heterotopia an argument against an isolated RNU4-2 etiology. | What are the exact numerator and denominator frequencies for specific brain MRI malformations (e.g., corpus callosum hypoplasia, delayed myelination, simplified gyral pattern) across Greene et al., Chen et al., and Barbour et al. cohorts? |
| h13 | binned | conflicted | 0.72 | 6 | 2 | 1 | Hypoplasia or thinning of the corpus callosum (HP:0002079) is the predominant specific structural neuroimaging biomarker in ReNU syndrome, manifesting in approximately 85% of individuals undergoing brain MRI assessment. | What are the exact numerator and denominator frequencies for specific brain MRI malformations (e.g., corpus callosum hypoplasia, delayed myelination, simplified gyral pattern) across Greene et al., Chen et al., and Barbour et al. cohorts? |
| h14 | binned | conflicted | 0.72 | 5 | 2 | 1 | Overall neuroimaging abnormality penetrance in ReNU syndrome exceeds 90% in systematically imaged cohorts (specifically 41/45 in Chen et al.), but findings are predominantly composed of non-specific white matter reduction, delayed myelination (HP:0002188), and ventriculomegaly (HP:0002119) rather than major cortical migration defects. | What are the exact numerator and denominator frequencies for specific brain MRI malformations (e.g., corpus callosum hypoplasia, delayed myelination, simplified gyral pattern) across Greene et al., Chen et al., and Barbour et al. cohorts? |
| 3.000000 | d2 | h16 | pooled | supported | 0.92 | 6 | 0 | 0 | The combination of hooded upper eyelids, full cheeks, a tented philtrum, and an open mouth with an everted lower lip vermilion constitutes a distinctive facial gestalt in ReNU syndrome that differentiates it from both classical Rett syndrome (MECP2) and Angelman syndrome (UBE3A/15q11-q13), which typically lack this specific perioral and periorbital dysmorphic constellation. | What specific dysmorphic features or clinical signs distinguish ReNU syndrome from Rett syndrome (MECP2) and Angelman syndrome (UBE3A/15q11-q13)? |
| h18 | pooled | supported | 0.85 | 3 | 0 | 0 | Congenital/early structural orthopedic abnormalities (such as clubfoot/talipes equinovarus and hip dysplasia) occur in a substantial minority of ReNU syndrome patients, serving as discriminatory physical signs that argue strongly against typical MECP2-related Rett syndrome and Angelman syndrome when present at or near birth. | What specific dysmorphic features or clinical signs distinguish ReNU syndrome from Rett syndrome (MECP2) and Angelman syndrome (UBE3A/15q11-q13)? |
| h17 | binned | conflicted | 0.45 | 4 | 1 | 1 | The structural brain MRI triad of corpus callosum hypoplasia/thinning, ventriculomegaly, and reduced white matter volume is present in over 85% of ReNU syndrome patients past infancy, providing an objective neuroradiological separator from Rett syndrome and Angelman syndrome, which typically show normal neuroimaging or non-specific cerebral volume reduction. | What specific dysmorphic features or clinical signs distinguish ReNU syndrome from Rett syndrome (MECP2) and Angelman syndrome (UBE3A/15q11-q13)? |
| 4.000000 | d3 | h11 | pooled | supported | 0.92 | 7 | 0 | 0 | Normal expressive language acquisition (phrase speech or fluent sentence production) by age 5 is confirmed absent across dominant ReNU syndrome cohorts, functioning as an obligatory pertinent negative. | Are there clinical features that have been consistently evaluated and confirmed absent across cohorts (pertinent negatives)? |
| h9 | binned | conflicted | 0.45 | 3 | 2 | 1 | True developmental milestone regression (as seen classically in Rett syndrome) is consistently absent in individuals with RNU4-2-related neurodevelopmental disorder (ReNU syndrome), making documented post-infancy loss of previously acquired motor or communicative milestones a strong negative predictor for ReNU syndrome. | Are there clinical features that have been consistently evaluated and confirmed absent across cohorts (pertinent negatives)? |
| h10 | binned | conflicted | 0.35 | 3 | 3 | 1 | Congenital macrocephaly (HP:0000256) is consistently absent in heterozygous RNU4-2-related disorder, such that the presence of macrocephaly or accelerated head circumference trajectory excludes dominant ReNU syndrome. | Are there clinical features that have been consistently evaluated and confirmed absent across cohorts (pertinent negatives)? |
| h12 | binned | refuted | 0.20 | 2 | 1 | 1 | Complete absence of neuroimaging anomalies on high-resolution brain MRI is an exclusionary finding for dominant ReNU syndrome in individuals past infancy. | Are there clinical features that have been consistently evaluated and confirmed absent across cohorts (pertinent negatives)? |
| nan | nan | h4 | pooled | supported | 0.92 | 3 | 0 | 0 | Stereotypic hand movements (HP:0000733) and hypotonia (HP:0001252) frequently lead to clinical suspicion of Rett-like or Angelman-like disorders, but lack of classic developmental regression typical of MECP2-related Rett syndrome differentiates ReNU syndrome. | nan |
| h2 | pooled | supported | 0.88 | 4 | 0 | 0 | Microcephaly (HP:0000252), predominantly postnatal or secondary, is present in approximately 70-85% of affected individuals across primary cohorts. | nan |
| h3 | pooled | supported | 0.85 | 6 | 0 | 0 | Characteristic craniofacial dysmorphisms including prominent/cupped/dysplastic ears (HP:0000377), bulbous nasal tip (HP:0000414), wide mouth (HP:0000154) with downturned corners (HP:0002714), and full cheeks occur in 60-80% of assessed patients. | nan |
| h1 | binned | conflicted | 0.65 | 4 | 3 | 1 | Severe global developmental delay / intellectual disability (HP:0001263 / HP:0010864) and severe speech/language impairment (HP:0000750) are present in nearly 100% of reported individuals (e.g., >95% in initial cohorts of Chen et al. 2024 and Greene et al. 2024). | nan |
| h5 | binned | conflicted | 0.65 | 5 | 2 | 1 | Phenotypic severity correlates with specific variant positions within the 18-nt conserved region (such as the recurrent n.64\_65insT or specific single nucleotide changes), where certain single-base substitutions show mildly variable expressivity compared to the classical insertion. | nan |

## Cell 37

### 4.5 What to do when a hypothesis is wrong?

When a hypothesis is wrong, we convert them into new directions. Every `"binned"` claim becomes a new question.

## Cell 38

```python

hyp_of = {h["id"]: h for h in H}
rank_of = {r.id: int(i) for i, r in directions.iterrows()}

rows = []
for d in D:
    if not d["tests"]:
        continue
    h = hyp_of.get(d["tests"], {})
    rows.append({
        "failed_hypothesis": d["tests"],
        "its_verdict":       h.get("verdict"),
        "its_confidence":    h.get("confidence"),
        "evidence_for":      h.get("n_support"),
        "evidence_against":  h.get("n_against"),
        "the_claim":         h.get("text"),
        "why_binned":        h.get("bin_reason"),
        "new_direction":     d["id"],
        "rank":              rank_of.get(d["id"]),
        "promise":           d["promise"],
        "funded":            d["spent"] > 0,
        "the_question":      d["question"],
    })

if not rows:
    print("No corrective directions in this run: nothing was contested.")
else:
    corrective = (pd.DataFrame(rows)
                  .sort_values("rank")
                  .set_index(["failed_hypothesis", "new_direction"]))
    print(f"{len(corrective)} binned hypotheses became directions. "
          f"{int(corrective.funded.sum())} of them were funded. "
          f"The best-ranked sits at rank {int(corrective['rank'].min())} of {len(directions)}.")

ccols = ["its_verdict", "its_confidence", "evidence_for", "evidence_against",
         "rank", "promise", "funded", "the_claim", "why_binned", "the_question"]

def show_corrective(frame):
    return (frame[ccols].style
            .set_properties(subset=["the_claim", "why_binned", "the_question"],
                            **{"white-space": "normal", "text-align": "left", "max-width": "420px"})
            .format({"its_confidence": "{:.2f}", "promise": "{:.2f}"})
            .apply(lambda r: ["background-color: #fff3cd" if r.funded else "" for _ in r], axis=1))

show_corrective(corrective)
```

```text
11 binned hypotheses became directions. 0 of them were funded. The best-ranked sits at rank 10 of 58.

```

|  |  | its\_verdict | its\_confidence | evidence\_for | evidence\_against | rank | promise | funded | the\_claim | why\_binned | the\_question |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| failed\_hypothesis | new\_direction |  |  |  |  |  |  |  |  |  |  |
| h14 | d45 | conflicted | 0.72 | 5 | 2 | 10 | 0.85 | False | Overall neuroimaging abnormality penetrance in ReNU syndrome exceeds 90% in systematically imaged cohorts (specifically 41/45 in Chen et al.), but findings are predominantly composed of non-specific white matter reduction, delayed myelination (HP:0002188), and ventriculomegaly (HP:0002119) rather than major cortical migration defects. | contested (5 for / 2 against): Penetrance estimate discrepancy: Chen et al. (2024) and Orphanet cite 91% (41/45) and Okamoto et al. (2025) cite 100% (9/9), whereas GeneReviews (Barbosa et al., 2026) summarizes abnormal brain MRI penetrance across cohorts at 85%, falling below the asserted >90% threshold.; Presence of cortical migration and gyration defects: Valenzuela & Codina (2024) and Orphanet report frontal simplified gyral patterns and heterotopias, indicating that while white matter reduction and ventriculomegaly predominate, migration and sulcation abnormalities are not completely absent. | Resolve the conflict over: Overall neuroimaging abnormality penetrance in ReNU syndrome exceeds 90% in systematically imaged cohorts (specifically 41/45 in Chen et al.), but findings are predominantly composed of non-specific white matter reduction, delayed myelination (HP:0002188), and ventriculomegaly (HP:0002119) rather than major cortical migration defects. |
| h17 | d56 | conflicted | 0.45 | 4 | 1 | 12 | 0.85 | False | The structural brain MRI triad of corpus callosum hypoplasia/thinning, ventriculomegaly, and reduced white matter volume is present in over 85% of ReNU syndrome patients past infancy, providing an objective neuroradiological separator from Rett syndrome and Angelman syndrome, which typically show normal neuroimaging or non-specific cerebral volume reduction. | contested (4 for / 1 against): GeneReviews sets the overall rate of \*any\* brain MRI abnormality at 85%, which contradicts the hypothesis that the full triad specifically occurs in >85% of patients.; Orphanet notes that MRI abnormalities occur in 91% of patients but presents findings disjunctively ('corpus callosum abnormalities and/or ventriculomegaly'), indicating that the full triad is not present in every abnormal scan. | Resolve the conflict over: The structural brain MRI triad of corpus callosum hypoplasia/thinning, ventriculomegaly, and reduced white matter volume is present in over 85% of ReNU syndrome patients past infancy, providing an objective neuroradiological separator from Rett syndrome and Angelman syndrome, which typically show normal neuroimaging or non-specific cerebral volume reduction. |
| h13 | d48 | conflicted | 0.72 | 6 | 2 | 14 | 0.85 | False | Hypoplasia or thinning of the corpus callosum (HP:0002079) is the predominant specific structural neuroimaging biomarker in ReNU syndrome, manifesting in approximately 85% of individuals undergoing brain MRI assessment. | contested (6 for / 2 against): Corpus callosum thinning/hypoplasia is non-specific: it is observed widely across secondary spliceosomal neurodevelopmental disorders (such as RNU2-2 and RNU5B-1) as well as non-spliceosomal microcephalic syndromic disorders.; Neuroimaging reports describe callosal hypoplasia alongside concurrent generalized cerebral volume loss, polymicrogyria, and ventriculomegaly, suggesting that callosal thinning frequently represents secondary white matter reduction rather than an isolated commissural biomarker.; Multiple diagnostic phenotyping studies identify the distinct facial gestalt and digital anomalies (e.g. hypoplastic distal phalanges) as more specific discriminative features than structural brain MRI anomalies. | Resolve the conflict over: Hypoplasia or thinning of the corpus callosum (HP:0002079) is the predominant specific structural neuroimaging biomarker in ReNU syndrome, manifesting in approximately 85% of individuals undergoing brain MRI assessment. |
| h7 | d29 | conflicted | 0.45 | 5 | 1 | 23 | 0.74 | False | Microcephaly (HP:0000252) in ReNU syndrome is primarily postnatally acquired and rarely manifests as a detectable fetal CNS anomaly in the prenatal period. | contested (5 for / 1 against): Chen et al. (2025) report that both identified prenatal cases of ReNU syndrome presented with microcephaly on prenatal imaging and designate microcephaly as a 'key prenatal feature', directly contradicting the premise that it rarely manifests as a detectable fetal CNS anomaly.; Valenzuela et al. (2024) observed congenital microcephaly in only 2 of 10 assessed individuals, supporting the observation that most individuals develop microcephaly postnatally, yet prenatal sonography in affected fetuses has successfully detected microcephaly before birth. | Resolve the conflict over: Microcephaly (HP:0000252) in ReNU syndrome is primarily postnatally acquired and rarely manifests as a detectable fetal CNS anomaly in the prenatal period. |
| h6 | d27 | conflicted | 0.55 | 4 | 2 | 24 | 0.73 | False | The reported penetrance of epilepsy and seizures (HP:0001250) in ReNU syndrome varies significantly between initial cohorts due to differences in patient age at evaluation rather than true biological heterogeneity, with younger cohorts under-reporting seizure frequency. | contested (4 for / 2 against): Studies confirm age-dependent seizure onset with a median onset of 3 years and delayed onset up to 13 years, meaning younger cohorts will under-ascertain penetrance.; Saturation genome editing and genotypic characterizations show that clinical severity and seizure manifestations are significantly influenced by specific variant mechanics and splice-site disruption, refuting the exclusivity claim that variance is strictly an age artifact rather than biological heterogeneity. | Resolve the conflict over: The reported penetrance of epilepsy and seizures (HP:0001250) in ReNU syndrome varies significantly between initial cohorts due to differences in patient age at evaluation rather than true biological heterogeneity, with younger cohorts under-reporting seizure frequency. |
| h8 | d23 | conflicted | 0.45 | 2 | 2 | 25 | 0.71 | False | The recurrent single-base insertion n.64\_65insT accounts for consistently 70% to 75% of pathogenic RNU4-2 variants across unselected global neurodevelopmental cohorts, with the remaining ~25% comprising distinct single-nucleotide substitutions. | contested (2 for / 2 against): Chen et al. (Nature 2024) observed that n.64\_65insT accounts for 77.4% (89/115) of pathogenic variants, which contradicts the proposed upper limit of 75%.; Bertoli (2025) observed that n.64\_65insT accounts for 71.4% (20/28) of pathogenic variants, demonstrating that while the insertion remains the major allele, the exact proportion fluctuates between cohorts (71% to 78%) rather than remaining constrained strictly within 70% to 75%. | Resolve the conflict over: The recurrent single-base insertion n.64\_65insT accounts for consistently 70% to 75% of pathogenic RNU4-2 variants across unselected global neurodevelopmental cohorts, with the remaining ~25% comprising distinct single-nucleotide substitutions. |
| h9 | d38 | conflicted | 0.45 | 3 | 2 | 31 | 0.60 | False | True developmental milestone regression (as seen classically in Rett syndrome) is consistently absent in individuals with RNU4-2-related neurodevelopmental disorder (ReNU syndrome), making documented post-infancy loss of previously acquired motor or communicative milestones a strong negative predictor for ReNU syndrome. | contested (3 for / 2 against): Most literature describes ReNU syndrome as an early-onset, static neurodevelopmental disorder without milestone loss, contrasting it with Rett syndrome.; Emerging case reports and clinical reviews (e.g., Kuroda et al., 2025; GeneReviews) document true neurological regression triggered by infection or intractable epilepsy in patients with non-canonical variants such as n.66A>G. | Resolve the conflict over: True developmental milestone regression (as seen classically in Rett syndrome) is consistently absent in individuals with RNU4-2-related neurodevelopmental disorder (ReNU syndrome), making documented post-infancy loss of previously acquired motor or communicative milestones a strong negative predictor for ReNU syndrome. |
| h10 | d32 | conflicted | 0.35 | 3 | 3 | 33 | 0.59 | False | Congenital macrocephaly (HP:0000256) is consistently absent in heterozygous RNU4-2-related disorder, such that the presence of macrocephaly or accelerated head circumference trajectory excludes dominant ReNU syndrome. | contested (3 for / 3 against): Most studies and prenatal cohorts describe microcephaly as a hallmark or secondary manifestation of ReNU syndrome, but large-scale cohort summaries and snRNA screening studies record relative macrocephaly or macrocephaly in subsets of probands or spliceosomal snRNA neurodevelopmental cohorts.; Normal head circumference is documented in confirmed recurrent RNU4-2 mutation carriers, demonstrating that head growth anomalies exist along a spectrum rather than a binary exclusion rule. | Resolve the conflict over: Congenital macrocephaly (HP:0000256) is consistently absent in heterozygous RNU4-2-related disorder, such that the presence of macrocephaly or accelerated head circumference trajectory excludes dominant ReNU syndrome. |
| h12 | d35 | refuted | 0.20 | 2 | 1 | 37 | 0.52 | False | Complete absence of neuroimaging anomalies on high-resolution brain MRI is an exclusionary finding for dominant ReNU syndrome in individuals past infancy. | refuted: While structural neuroimaging abnormalities (such as hypoplasia of the corpus callosum, delayed myelination/decreased white matter volume, and ventriculomegaly) are frequent and characteristic features of dominant ReNU syndrome (NEDHAFA), the literature documents that neuroradiological abnormalities are observed in 'many' rather than all affected individuals globally. Stating that a completely normal brain MRI is an absolute exclusionary criterion overstates the penetrance of detectable gross structural anomalies and risks erroneously ruling out patients who exhibit typical dysmorphisms, neurodevelopmental delay, and microcephaly without overt structural malformations. | Re-investigate (refuted): Complete absence of neuroimaging anomalies on high-resolution brain MRI is an exclusionary finding for dominant ReNU syndrome in individuals past infancy. |
| h5 | d9 | conflicted | 0.65 | 5 | 2 | 40 | 0.50 | False | Phenotypic severity correlates with specific variant positions within the 18-nt conserved region (such as the recurrent n.64\_65insT or specific single nucleotide changes), where certain single-base substitutions show mildly variable expressivity compared to the classical insertion. | contested (5 for / 2 against): Nava et al. (2025) and Kuroda et al. (2025) document clear structural genotype-phenotype distinctions between T-loop (more severe) and stem III (less severe) variants.; Saleem et al. (2026) and Bruselles et al. (2025) report that deep phenotyping reveals broad phenotypic overlap and severe manifestations across multiple positions, cautioning that linear genotype-to-severity mapping is insufficient for individual clinical prediction. | Resolve the conflict over: Phenotypic severity correlates with specific variant positions within the 18-nt conserved region (such as the recurrent n.64\_65insT or specific single nucleotide changes), where certain single-base substitutions show mildly variable expressivity compared to the classical insertion. |
| h1 | d6 | conflicted | 0.65 | 4 | 3 | 50 | 0.44 | False | Severe global developmental delay / intellectual disability (HP:0001263 / HP:0010864) and severe speech/language impairment (HP:0000750) are present in nearly 100% of reported individuals (e.g., >95% in initial cohorts of Chen et al. 2024 and Greene et al. 2024). | contested (4 for / 3 against): Frequency of GDD in Hayashi et al. 2025 is 93.8% (15/16), contradicting the assertion that GDD is present in >95% to nearly 100% of all cohorts.; Orphanet and GeneReviews report mild-to-profound intellectual disability and documented transmission from mildly affected parents, refuting the claim that severe intellectual disability and severe speech impairment are strictly present in 100% of cases. | Resolve the conflict over: Severe global developmental delay / intellectual disability (HP:0001263 / HP:0010864) and severe speech/language impairment (HP:0000750) are present in nearly 100% of reported individuals (e.g., >95% in initial cohorts of Chen et al. 2024 and Greene et al. 2024). |

## Cell 39

**Todo 4.1:** Select at least 2 refuted or conflicted hypothesis and explain why did the LLM refute/conflict the hypothesis: (1) Was the evidence truly against the hypothesis or (2) It was there missing information.

## Cell 40

## 4.6 Report Generation

We have seen how Grill generates directions, then funds some of the promising directions and generates hyopthesis.
For each hypothesis, we try to actively look for supporting and refuting evidence. 

**Looking for refuting evidence is very important because by default LLMs actively try to look for support!**

## Cell 41

```python
from IPython.display import Markdown, display

report = (RUN_DIR / "answer.md").read_text()
print(f"{len(report):,} characters. Read it as a clinician would: what would you use to pick the patient?\n")
display(Markdown(report))
```

```text
25,333 characters. Read it as a clinician would: what would you use to pick the patient?


```

```text
<IPython.core.display.Markdown object>
```

## Cell 42

**TODO 4.2:** Even thought the GRILL report is big, is there  any thing that it misses compared to the report generated by the RAG system or direct LLM call in sec 1.3 and 1.4?

**TODO 4.3:**: Given this report, and the patient cohort data can you guess which patient has this disease?

## Cell 43

# 5 Ranking the patients

We will now rank the patient according to the generated grill report.

## Cell 44

```python
report_run = json.loads((ROOT / "assignments" / DISEASE.replace(":", "_") / "report_match.json").read_text())
report_messages = report_run["messages"]

print(f"Same task as before, same ten patients, same output shape. Only the evidence changes:")
print(f"the six snippets are replaced by GRILL's report, {report_run['report_chars']:,} characters.\n")
for m in report_messages:
    print(f"--- {m['role']} ({len(m['content']):,} chars) ---")
    body = m["content"]
    if m["role"] == "user":
        head, _, tail = body.partition("COHORT (")
        body = head[:1200] + "\n  [... the rest of the report ...]\n\nCOHORT (" + tail[:900] + "\n  [... remaining patients ...]"
    print(textwrap.indent(body, "  "))
    print()
```

```text
Same task as before, same ten patients, same output shape. Only the evidence changes:
the six snippets are replaced by GRILL's report, 25,333 characters.

--- system (335 chars) ---
  You are a clinical geneticist. You are given a literature report on one rare disease and a cohort of patients described by HPO terms. Exactly one patient has the disease. Use only the report as your knowledge of the disease. Be explicit about which findings in the report drove each placement, and about findings that argue against it.

--- user (32,091 chars) ---
  REPORT ON ReNU syndrome (RNU4-2, OMIM:620851):

  # Clinical Identification of ReNU Syndrome (RNU4-2; OMIM #620851) from Phenotype Alone

  ## Executive Summary & Clinical Recognition Framework

  ReNU syndrome (OMIM #620851) is an autosomal dominant neurodevelopmental disorder caused by monoallelic, predominantly de novo pathogenic variants in *RNU4-2*, which encodes the small nuclear RNA (snRNA) U4 of the major spliceosome (F1, F5, F14). Due to its high prevalence among previously unsolved neurodevelopmental delay cohorts—accounting for 0.4% to 2.9% of unexplained neurodevelopmental disorder cases and upwards of 5.3% of exome-negative cohorts (F4, F11, F14)—clinicians face the practical challenge of picking affected individuals out of patient groups presenting with non-specific severe neurodevelopmental delay, microcephaly, hypotonia, and stereotypic behaviors (F1, F4, F10).

  Clinical identification rests upon a defined multi-feature constellation:
  1. **A distinctive craniofacial gestalt** featuring hooded upper eyelids, full cheeks, a tented philtrum, wide mouth with downturned corners, and prominent or cupped ears (F4, F6).
  2. **Congenital skeletal and orthopedic anomalies** (e.g., t
    [... the rest of the report ...]

  COHORT (10 patients; exactly one has the disease):

  P01 (age 3.4, female)
    observed: Unilateral renal agenesis, Atrial septal defect, Hypertelorism, Strabismus, Delayed ability to walk, Absent speech, Severe intellectual disability, Lower limb muscle weakness, Hypotonia
    recorded ABSENT: Absent crus of helix, Overfolded helix, Renal cortical cysts, Retrognathia, Deep philtrum, Exaggerated cupid's bow, Everted lower lip vermilion, Thin vermilion border, Thick vermilion border, Narrow mouth, Open mouth, Broad forehead, Narrow forehead, High forehead, Highly arched eyebrow, Synophrys, Upslanted palpebral fissure, Short palpebral fissure, Epicanthus, Wide nasal bridge, Depressed nasal bridge, Anteverted nares, Round face, Facial asymmetry, Long face (+12 more)

  P02 (age 1.6, female)
    observed: Microcephaly, Intellectual disability, Global developmental delay, Hypotonia, Feeding difficulties, Fail
    [... remaining patients ...]


```

## Cell 45

## 5.1 Running with LLM

We again send the same report to the LLM three times, and we might again get different ranking each time.

## Cell 46

```python
rows = []
for r in report_run["rounds"]:
    for pos, c in enumerate(r["ranking"][:5], 1):
        rows.append({"round": r["round"], "position": pos, "patient": c["patient_id"],
                     "probability": c["probability"], "for": c["for"], "against": c["against"]})
report_ranking = pd.DataFrame(rows).set_index(["round", "position"])

display(report_ranking.style
          .set_properties(subset=["for", "against"],
                          **{"white-space": "normal", "text-align": "left", "max-width": "420px"})
          .format({"probability": "{:.2f}"})
          .set_caption(f"three rounds with the GRILL report: the model's top five for {brief.label}"))
```

three rounds with the GRILL report: the model's top five for ReNU syndrome

|  |  | patient | probability | for | against |
| --- | --- | --- | --- | --- | --- |
| round | position |  |  |  |  |
| 1 | 1 | P06 | 0.88 | Demonstrates core triad and imaging features described in the report: progressive (postnatal) microcephaly, absent speech, motor stereotypy, hypoplasia of the corpus callosum, delayed CNS myelination, aplasia/hypoplasia of cerebral white matter, facial hypotonia, and characteristic craniofacial dysmorphism (tented philtrum, tented upper lip vermilion). Age is 1.7 years, which explains the recorded absence of seizures given the median age of epileptogenesis is ~3 years. | Diabetes insipidus, blepharophimosis, and tortuous cerebral arteries are atypical/not highlighted in the report; ventriculomegaly is recorded absent. |
| 2 | P03 | 0.05 | Presents with thin corpus callosum, tented upper lip vermilion, full cheeks, global developmental delay, intellectual disability, seizures, and microcephaly. | Microcephaly is congenital/primary rather than secondary/postnatal; hypotonia is explicitly recorded absent while hypertonia is present (contradicting the core generalized hypotonia); features atypical cerebellar atrophy, anemia, and thrombocytopenia. |
| 3 | P02 | 0.03 | Presents with microcephaly, generalized hypotonia, global developmental delay, and severe speech/language delay in infancy. | Motor stereotypy is recorded absent; lacks the key craniofacial gestalt (has micrognathia and low-set ears); neuroimaging findings are not reported. |
| 4 | P10 | 0.02 | Exhibits thin corpus callosum, hypotonia, global developmental delay, and speech/language delay. | Hooded eyelid and delayed CNS myelination are explicitly recorded absent; exhibits cleft palate and narrow mouth (rather than wide mouth); lacks microcephaly. |
| 5 | P07 | 0.01 | Presents with microcephaly, intellectual disability, speech delay, motor delay, and seizures. | Lacks the characteristic dysmorphic gestalt and neuroimaging anomalies (corpus callosum hypoplasia, delayed myelination) highlighted as hallmarks in the report. |
| 2 | 1 | P06 | 0.92 | Demonstrates core characteristic features outlined in the report: tented philtrum (a cardinal craniofacial sign), progressive microcephaly (matching postnatal head circumference deceleration), absent speech, motor stereotypy (stereotypic hand movements), hypoplasia of the corpus callosum, delayed CNS myelination, decreased cerebral white matter volume, and facial hypotonia/GDD. The absence of seizures is fully consistent with the patient's young age (1.7 years), as the report notes seizures exhibit an age-dependent onset with a median age of ~3 years. | Displays diabetes insipidus, blepharophimosis, and tortuous cerebral arteries which are not highlighted in the report; ventriculomegaly is recorded as absent. |
| 2 | P03 | 0.04 | Presents with thin corpus callosum, tented upper lip vermilion, full cheeks, primary microcephaly, tonic seizures, and global developmental delay/intellectual disability. | Generalized hypotonia is recorded as explicitly absent (with hypertonia observed instead), contrasting with hypotonia being a core penetrant feature; features cerebellar atrophy, anemia, and thrombocytopenia which are not typical of ReNU syndrome. |
| 3 | P10 | 0.02 | Shows thin corpus callosum, generalized hypotonia, feeding difficulties, and global developmental delay. | Hooded eyelid and delayed CNS myelination are explicitly recorded as absent; displays a narrow mouth and cleft palate, directly contradicting the characteristic wide mouth described for ReNU syndrome. |
| 4 | P02 | 0.01 | Manifests microcephaly, global developmental delay, severe speech delay, feeding difficulties, and hypotonia. | Motor stereotypy is recorded as absent; lacks distinctive craniofacial gestalt (has micrognathia and low-set ears rather than hooded eyelids, tented philtrum, or wide mouth) and neuroimaging hallmarks. |
| 5 | P07 | 0.01 | Has microcephaly, seizures, gross motor delay, delayed speech, and intellectual disability. | Lacks reported craniofacial gestalt features, neuroimaging confirmation (callosal thinning, myelination delay), hypotonia, or stereotypic movements. |
| 3 | 1 | P06 | 0.92 | Matches the core phenotypic hallmark of ReNU syndrome across multiple systems: progressive (postnatal) microcephaly, absent speech, motor stereotypies, tented philtrum (a key facial gestalt marker), and the classic neuroimaging profile including hypoplasia/thinning of the corpus callosum, delayed CNS myelination, and aplasia/hypoplasia of cerebral white matter. Age (1.7 years) also aligns with the latency of seizure presentation (median onset ~3 years). | Has diabetes insipidus and tortuous cerebral arteries which are not described in the report; ventriculomegaly is recorded as absent (though the report notes neuroimaging findings are variable and not obligate biomarkers). |
| 2 | P03 | 0.04 | Presents with global developmental delay, intellectual disability, thin corpus callosum, full cheeks, tented upper lip, microcephaly, and seizures/EEG abnormalities. | Hypotonia is recorded as absent with hypertonia observed (generalized hypotonia is a core feature of ReNU syndrome); has primary rather than secondary/progressive microcephaly; presents with cerebellar atrophy, anemia, and thrombocytopenia which are not typical features described in the report. |
| 3 | P02 | 0.02 | Exhibits microcephaly, global developmental delay, intellectual disability, generalized hypotonia, and delayed speech and language development. | Motor stereotypy is explicitly recorded as absent; lacks specific ReNU facial dysmorphisms (tented philtrum, hooded eyelids, prominent/cupped ears); lacks neuroimaging confirmation such as callosal thinning. |
| 4 | P10 | 0.01 | Presents with global developmental delay, intellectual disability, hypotonia, delayed speech, and thin corpus callosum. | Hooded eyelid and delayed CNS myelination are explicitly recorded as absent; presents with cleft palate and narrow mouth (the report highlights wide mouth); has moderate rather than profound speech/intellectual impairment. |
| 5 | P07 | 0.01 | Features microcephaly, global neurodevelopmental delay, delayed speech, and seizures. | Lacks the characteristic craniofacial gestalt (tented philtrum, hooded eyelids, cupped ears), documented neuroimaging abnormalities (corpus callosum hypoplasia/delayed myelination), and hypotonia or orthopedic abnormalities. |

## Cell 47

**TODO 5.1:** Did repeated runs agree? They if do not disagree, do their reasoning match, please describe. If they do not match, how does their reasoning differ?

**TODO 5.2:** What is the differentiating factor in each round between the first and the second ranks?

**TODO 5.3:** How does the ranking differ from RAG generated ranking in section 3?

**TODO 5.4:** Based on the information gather, which patient is likely to have the disease (take your best guess!)

## Cell 48

# 6 Evaluation

Now you have seen how simple RAG works, how with a more extensive method of searching we can enrich the context. But how do we tell which one is correct?

Fortunately, for this task we have the ground truth. After running the cell below, we will learn the answer and the ranking from RAG and Grill report.

## Cell 49

```python
import csv

key_path = ROOT / "data" / "assignment_targets.csv"
if not key_path.exists():
    print("No answer key in this copy. Submit your ranking; it will be scored for you.")
else:
    my_dir = DISEASE.replace(":", "_")
    row = next(r for r in csv.DictReader(key_path.open()) if r["directory"] == my_dir)
    TARGET_PATIENT = row["target_patient_id"]

    print(f"{row['disease']} ({row['gene']}): the patient with the disease is {TARGET_PATIENT}")
    print(f"source case report: PMID:{row['source_pmid']}   phenopacket: {row['phenopacket']}\n")

    def rank_of(run):
        out = []
        for r in run["rounds"]:
            ids = [c["patient_id"] for c in r["ranking"][:5]]
            out.append(ids.index(TARGET_PATIENT) + 1 if TARGET_PATIENT in ids else None)
        return out

    scored = pd.DataFrame({
        "RAG":  rank_of(rank_run),
        "GRILL report":  rank_of(report_run),
    }, index=[f"round {i}" for i in (1, 2, 3)])
    display(scored.style.format(lambda v: "not in top 5" if v is None or pd.isna(v) else f"rank {int(v)}")
                        .set_caption(f"where {TARGET_PATIENT} landed in each ranking"))

    # The true patient, as you saw them.
    p = cohort.get(TARGET_PATIENT)
    print(f"\n{TARGET_PATIENT}: age {p.age_years}, {p.sex}, {len(p.terms)} findings, {len(p.excluded)} recorded absent")
    for t in p.terms:
        print(f"    {t}  {hpo.label(t)}")
```

```text
ReNU syndrome (RNU4-2): the patient with the disease is P06
source case report: PMID:39369315   phenopacket: PMID_39369315_Participant_9


```

where P06 landed in each ranking

|  | RAG | GRILL report |
| --- | --- | --- |
| round 1 | rank 1 | rank 1 |
| round 2 | rank 1 | rank 1 |
| round 3 | rank 1 | rank 1 |

```text

P06: age 1.7, male, 31 findings, 40 recorded absent
    HP:0033454  Tube feeding
    HP:0001263  Global developmental delay
    HP:0000639  Nystagmus
    HP:0001508  Failure to thrive
    HP:0002019  Constipation
    HP:0000253  Progressive microcephaly
    HP:0001344  Absent speech
    HP:0001270  Motor delay
    HP:0000873  Diabetes insipidus
    HP:0000729  Autistic behavior
    HP:0000733  Motor stereotypy
    HP:0002079  Hypoplasia of the corpus callosum
    HP:0002188  Delayed CNS myelination
    HP:0002307  Drooling
    HP:0000737  Irritability
    HP:0001288  Gait disturbance
    HP:0000194  Open mouth
    HP:0010804  Tented upper lip vermilion
    HP:0011825  Tented philtrum
    HP:0000286  Epicanthus
    HP:0000297  Facial hypotonia
    HP:0000581  Blepharophimosis
    HP:0011228  Horizontal eyebrow
    HP:0000348  High forehead
    HP:0000385  Small earlobe
    HP:0000341  Narrow forehead
    HP:0006532  Recurrent pneumonia
    HP:0031061  Impaired toileting ability
    HP:0000736  Short attention span
    HP:0012429  Aplasia/Hypoplasia of the cerebral white matter
    HP:0004938  Tortuous cerebral arteries

```

## Cell 50

## 6.1 Analysing Failures

Write your code for evaluating why did RAG or GRILL get the ranking wrong.

For grill:
- Assignment (Root)
  - `grill_run/`
    - `tasks/`  # contains step wise output information and associated metadata.
    - `ledger.json`  # detailed information on what the agent was trying to do
    -  ...

We recommend going through `tasks` to understand what the agent was getting wrong.

We also recommend looking at the `ledger.json`, so that you understand the reasoning, direction, hypothesis, budget etc that the agent was trying to do.

**TODO 6.1: Write your code below for analysis and then write your findings on why did any system fail.**

## Cell 51

```python

```
