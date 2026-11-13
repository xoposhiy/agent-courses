# DrRepair

[Course index](../../README.md) · [Original source](https://proceedings.mlr.press/v119/yasunaga20a.html) · [Raw file](../../raw/optional-readings/ref-2adaa3d79c8f.html)

Retrieved: 2026-11-13T16:55:47.581670+00:00

# Graph-based, Self-Supervised Program Repair from Diagnostic Feedback

Michihiro Yasunaga, Percy Liang

*Proceedings of the 37th International Conference on Machine Learning*, PMLR 119:10799-10808, 2020.

#### Abstract

We consider the problem of learning to repair programs from diagnostic feedback (e.g., compiler error messages). Program repair is challenging for two reasons: First, it requires reasoning and tracking symbols across source code and diagnostic feedback. Second, labeled datasets available for program repair are relatively small. In this work, we propose novel solutions to these two challenges. First, we introduce a program-feedback graph, which connects symbols relevant to program repair in source code and diagnostic feedback, and then apply a graph neural network on top to model the reasoning process. Second, we present a self-supervised learning paradigm for program repair that leverages unlabeled programs available online to create a large amount of extra program repair examples, which we use to pre-train our models. We evaluate our proposed approach on two applications: correcting introductory programming assignments (DeepFix dataset) and correcting the outputs of program synthesis (SPoC dataset). Our final system, DrRepair, significantly outperforms prior work, achieving 68.2% full repair rate on DeepFix (+22.9% over the prior best), and 48.4% synthesis success rate on SPoC (+3.7% over the prior best).

#### Cite this Paper

---

BibTeX

`@InProceedings{pmlr-v119-yasunaga20a,
title = {Graph-based, Self-Supervised Program Repair from Diagnostic Feedback},
author = {Yasunaga, Michihiro and Liang, Percy},
booktitle = {Proceedings of the 37th International Conference on Machine Learning},
pages = {10799--10808},
year = {2020},
editor = {III, Hal Daumé and Singh, Aarti},
volume = {119},
series = {Proceedings of Machine Learning Research},
month = {13--18 Jul},
publisher = {PMLR},
pdf = {http://proceedings.mlr.press/v119/yasunaga20a/yasunaga20a.pdf},
url = {https://proceedings.mlr.press/v119/yasunaga20a.html},
abstract = {We consider the problem of learning to repair programs from diagnostic feedback (e.g., compiler error messages). Program repair is challenging for two reasons: First, it requires reasoning and tracking symbols across source code and diagnostic feedback. Second, labeled datasets available for program repair are relatively small. In this work, we propose novel solutions to these two challenges. First, we introduce a program-feedback graph, which connects symbols relevant to program repair in source code and diagnostic feedback, and then apply a graph neural network on top to model the reasoning process. Second, we present a self-supervised learning paradigm for program repair that leverages unlabeled programs available online to create a large amount of extra program repair examples, which we use to pre-train our models. We evaluate our proposed approach on two applications: correcting introductory programming assignments (DeepFix dataset) and correcting the outputs of program synthesis (SPoC dataset). Our final system, DrRepair, significantly outperforms prior work, achieving 68.2% full repair rate on DeepFix (+22.9% over the prior best), and 48.4% synthesis success rate on SPoC (+3.7% over the prior best).}
}`

Copy to Clipboard
Download

Endnote

`%0 Conference Paper
%T Graph-based, Self-Supervised Program Repair from Diagnostic Feedback
%A Michihiro Yasunaga
%A Percy Liang
%B Proceedings of the 37th International Conference on Machine Learning
%C Proceedings of Machine Learning Research
%D 2020
%E Hal Daumé III
%E Aarti Singh
%F pmlr-v119-yasunaga20a
%I PMLR
%P 10799--10808
%U https://proceedings.mlr.press/v119/yasunaga20a.html
%V 119
%X We consider the problem of learning to repair programs from diagnostic feedback (e.g., compiler error messages). Program repair is challenging for two reasons: First, it requires reasoning and tracking symbols across source code and diagnostic feedback. Second, labeled datasets available for program repair are relatively small. In this work, we propose novel solutions to these two challenges. First, we introduce a program-feedback graph, which connects symbols relevant to program repair in source code and diagnostic feedback, and then apply a graph neural network on top to model the reasoning process. Second, we present a self-supervised learning paradigm for program repair that leverages unlabeled programs available online to create a large amount of extra program repair examples, which we use to pre-train our models. We evaluate our proposed approach on two applications: correcting introductory programming assignments (DeepFix dataset) and correcting the outputs of program synthesis (SPoC dataset). Our final system, DrRepair, significantly outperforms prior work, achieving 68.2% full repair rate on DeepFix (+22.9% over the prior best), and 48.4% synthesis success rate on SPoC (+3.7% over the prior best).`

Copy to Clipboard
Download

APA

`Yasunaga, M. & Liang, P.. (2020). Graph-based, Self-Supervised Program Repair from Diagnostic Feedback. Proceedings of the 37th International Conference on Machine Learning, in Proceedings of Machine Learning Research 119:10799-10808 Available from https://proceedings.mlr.press/v119/yasunaga20a.html.`

Copy to Clipboard
Download

---

#### Related Material

- [Download PDF](ref-2adaa3d79c8f-pdf.md)
- [Software](https://github.com/michiyasunaga/DrRepair)
