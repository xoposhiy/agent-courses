# MaxRL

[Course index](../../README.md) · [Original source](https://proceedings.mlr.press/v306/tajwar26a.html) · [Raw file](../../raw/optional-readings/ref-245b19b46cbb.html)

Retrieved: 2026-11-13T16:59:54.242324+00:00

# Maximum Likelihood Reinforcement Learning

Fahim Tajwar, Guanning Zeng, Yueer Zhou, Yuda Song, Daman Arora, Yiding Jiang, Jeff Schneider, Ruslan Salakhutdinov, Haiwen Feng, Andrea Zanette

*Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306:118190-118245, 2026.

#### Abstract

Reinforcement learning (RL) is the method of choice for training models in setups where the objective function can only be evaluated by sampling from the model. Our key observation is that when the feedback is terminal and binary, models implicitly induce a likelihood over correct rollouts. Maximum likelihood would be the natural framework in such settings, but RL is used instead as a workaround to the non-differentiability. We prove that the standard, expected-reward RL formulation is only a first-order approximation of the likelihood. To remedy this mismatch, we introduce **Maximum Likelihood Reinforcement Learning (MaxRL)**, a compute-indexed family of sample-based objectives that interpolate between expected-reward RL and maximum likelihood as sampling compute is scaled. The resulting objective is a one-line change to standard RL implementations. MaxRL Pareto-dominates existing methods in all tested models and tasks, achieves up to $\mathbf{20\times}$ gains in test-time scaling efficiency over GRPO, and scales more favorably with additional training data and compute.

#### Cite this Paper

---

BibTeX

`@InProceedings{pmlr-v306-tajwar26a,
title = {Maximum Likelihood Reinforcement Learning},
author = {Tajwar, Fahim and Zeng, Guanning and Zhou, Yueer and Song, Yuda and Arora, Daman and Jiang, Yiding and Schneider, Jeff and Salakhutdinov, Ruslan and Feng, Haiwen and Zanette, Andrea},
booktitle = {Proceedings of the 43rd International Conference on Machine Learning},
pages = {118190--118245},
year = {2026},
editor = {Zhang, Tong and Dudik, Miroslav and Jaggi, Martin and Agarwal, Alekh and Li, Sharon and Schuurmans, Dale and Zhu, Jerry and Berkenkamp, Felix and Dong, Hanze and Bietti, Alberto},
volume = {306},
series = {Proceedings of Machine Learning Research},
month = {06--11 Jul},
publisher = {PMLR},
pdf = {https://raw.githubusercontent.com/mlresearch/v306/main/assets/tajwar26a/tajwar26a.pdf},
url = {https://proceedings.mlr.press/v306/tajwar26a.html},
abstract = {Reinforcement learning (RL) is the method of choice for training models in setups where the objective function can only be evaluated by sampling from the model. Our key observation is that when the feedback is terminal and binary, models implicitly induce a likelihood over correct rollouts. Maximum likelihood would be the natural framework in such settings, but RL is used instead as a workaround to the non-differentiability. We prove that the standard, expected-reward RL formulation is only a first-order approximation of the likelihood. To remedy this mismatch, we introduce Maximum Likelihood Reinforcement Learning (MaxRL), a compute-indexed family of sample-based objectives that interpolate between expected-reward RL and maximum likelihood as sampling compute is scaled. The resulting objective is a one-line change to standard RL implementations. MaxRL Pareto-dominates existing methods in all tested models and tasks, achieves up to $\mathbf{20\times}$ gains in test-time scaling efficiency over GRPO, and scales more favorably with additional training data and compute.}
}`

Copy to Clipboard
Download

Endnote

`%0 Conference Paper
%T Maximum Likelihood Reinforcement Learning
%A Fahim Tajwar
%A Guanning Zeng
%A Yueer Zhou
%A Yuda Song
%A Daman Arora
%A Yiding Jiang
%A Jeff Schneider
%A Ruslan Salakhutdinov
%A Haiwen Feng
%A Andrea Zanette
%B Proceedings of the 43rd International Conference on Machine Learning
%C Proceedings of Machine Learning Research
%D 2026
%E Tong Zhang
%E Miroslav Dudik
%E Martin Jaggi
%E Alekh Agarwal
%E Sharon Li
%E Dale Schuurmans
%E Jerry Zhu
%E Felix Berkenkamp
%E Hanze Dong
%E Alberto Bietti
%F pmlr-v306-tajwar26a
%I PMLR
%P 118190--118245
%U https://proceedings.mlr.press/v306/tajwar26a.html
%V 306
%X Reinforcement learning (RL) is the method of choice for training models in setups where the objective function can only be evaluated by sampling from the model. Our key observation is that when the feedback is terminal and binary, models implicitly induce a likelihood over correct rollouts. Maximum likelihood would be the natural framework in such settings, but RL is used instead as a workaround to the non-differentiability. We prove that the standard, expected-reward RL formulation is only a first-order approximation of the likelihood. To remedy this mismatch, we introduce Maximum Likelihood Reinforcement Learning (MaxRL), a compute-indexed family of sample-based objectives that interpolate between expected-reward RL and maximum likelihood as sampling compute is scaled. The resulting objective is a one-line change to standard RL implementations. MaxRL Pareto-dominates existing methods in all tested models and tasks, achieves up to $\mathbf{20\times}$ gains in test-time scaling efficiency over GRPO, and scales more favorably with additional training data and compute.`

Copy to Clipboard
Download

APA

`Tajwar, F., Zeng, G., Zhou, Y., Song, Y., Arora, D., Jiang, Y., Schneider, J., Salakhutdinov, R., Feng, H. & Zanette, A.. (2026). Maximum Likelihood Reinforcement Learning. Proceedings of the 43rd International Conference on Machine Learning, in Proceedings of Machine Learning Research 306:118190-118245 Available from https://proceedings.mlr.press/v306/tajwar26a.html.`

Copy to Clipboard
Download

---

#### Related Material

- [Download PDF](ref-245b19b46cbb-pdf.md)
- [OpenReview](https://openreview.net/forum?id=EeuLO2BjFN)
- [Software](https://github.com/tajwarfahim/maxrl)
