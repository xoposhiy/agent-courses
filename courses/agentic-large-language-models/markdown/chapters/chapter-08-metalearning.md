# Chapter 8 Metalearning

[Course index](../../README.md) · [Original source](https://arxiv.org/html/2610.13455v1#Ch8) · [Raw file](../../raw/originals/book.html)

Retrieved: 2026-11-13T16:41:17.579179+00:00

[Contents](../../CONTENTS.md) · [Full book](../book/full-book-html.md) · [Previous chapter](chapter-07-vision-action-and-world-models.md) · [Next chapter](chapter-09-interaction-styles-for-agentic-llms.md)

<a id="Ch8"></a>


### Chapter 8 Metalearning

**What You Will Learn**

In this chapter you will learn about metalearning.
Specifically, you will be able to:

- Recognize the different *levels* of learning that are used in LLM pipelines.
- Understand the connection between in-context learning, *few-shot learning* and metalearning.
- Create a metalearning system that consists of an *inner* learning loop and an *outer* learning loop.
- Recognize the moving-target problem: why it is challenging to achieve *stable learning* in a dynamic metalearning system.

<a id="Ch8.S1"></a>


#### 8.1 Why Metalearning?

As we have seen, the self-reflecting LLM approaches are powerful, but getting the training processes to converge can be a challenge. In agentic LLM, learning occurs at multiple levels, and sometimes at the same time. In machine learning, algorithms that learn at multiple levels are said to perform metalearning. Metalearning is often described as *learning to learn*, for example, learning which prompt works better for a certain task. Metalearning can be a powerful concept, but sometimes the different learning levels interfere, and learning stops.

To help us understand why our LLM multi-level learning algorithms sometimes do not work, we will look deeper into metalearning. In this chapter we will discuss how we can improve the stability of dynamic, feedback-rich, metalearning approaches.

The term metalearning is used for multi-level learning algorithms. Metalearning algorithms learn to
learn, to quickly solve examples of new, unseen, tasks, that the model has not trained for.

<a id="Ch8.S1.SS1"></a>


##### 8.1.1 Deep Learning is Slow

<a id="Ch8.S1.SS1.p1.1"></a>


Metalearning has a long history in machine learning (see, for example, [Schmidhuber [1987]](#bibg.bib9), [Hospedales et al. [2021]](#bibg.bib4), [Huisman et al. [2021]](#bibg.bib5)). It is inspired by human learning, since humans are said to be able to learn how to learn. Another reason for its development, is speed.

<a id="Ch8.S1.SS1.p2.1"></a>


The problem is that regular deep learning is slow. Neural networks for typical deep learning tasks are large, with millions or billions of parameters, and training them requires large datasets, often with millions of examples. Training times for training a network from scratch are long, from hours to months, and only when special parallel parallel hardware (GPU) was employed, did deep learning become successful [[Krizhevsky et al., 2012](#bibg.bib3)].

At this point, researchers started dreaming about few-shot learning, methods that would achieve high accuracy by training on just a few examples.

<a id="Ch8.S1.SS2"></a>


##### 8.1.2 Achieving Few-shot Learning

In machine learning, some algorithms are better suited for certain types of problems than others. Furthermore, most training algorithms have elements that can be tuned for performance, such as the learning rate, momentum, the initialization scheme of the parameters, or, for a multi-level algorithm, even the choice of the underlying training algorithm. These elements are called *hyperparameters*, and they govern how the algorithm learns. Would we be able to learn them?

Different types of problems require different hyperparameter settings. For example, for a smooth dataset, a high learning rate may work well, or a local search algorithm, but for a peaky dataset a lower learning rate works better, or a global search algorithm. The point is that the best hyperparameter configuration in machine learning depends on the task to be solved, and that, crucially, this configuration can be learned. Learning such hyperparameters of the algorithm for different tasks is called *metalearning*. (In contrast, the learning of the regular parameters of the model is now called *base learning*.)

The aim of metalearning is to create algorithms that learn certain tasks faster.
Instead of using a generic algorithm that is not adapted to the task, starting from scratch, we should use a learning algorithm whose hyperparameters are first matched to the type of task to be solved. The metalearning approach is to first learn from a set of related tasks how to configure the learning algorithm, learning to learn a certain set of tasks faster.

When we have learned the hyperparameter configuration for such an adapted algorithm, we may hope to be able to achieve few-shot training: being able to train on just a few examples, while still achieving high accuracy on examples from a new test task.
Metalearning achieves few-shot learning by starting the training not from scratch, but from related knowledge.

<a id="Ch8.S1.SS2.p5.1"></a>


Metalearning consists of a (hyper) training loop around a (base) training loop. In classical (non-neural network) machine learning, common hyperparameters are the learning rate, or algorithm selection, where different learning algorithms are tested on training tasks [[Brazdil et al., 2022](#bibg.bib1)]. In deep learning, the initialization of the neural network weights is often used [[Finn et al., 2017](#bibg.bib6)].

In agentic LLM, we have also encountered learning at different levels (and we will continue to discuss multi-level learning in the next chapter). It is useful for us to study the theory and insights of the metalearning literature.

<a id="Ch8.S2"></a>


#### 8.2 Inner/Outer Loop

As any supervised learning approach, metalearning consists of (1) a meta-*train* phase, training on a variety of related tasks, and (2) a meta-*test* phase, testing on a new, unseen, task, to see how well it generalizes to this new *task*. The goal is to improve generalization by learning a hyperparameter setting of the training algorithm that work well on a wide variety of training tasks.

The process of training the parameters of a model is implemented as an optimization loop, in which a loss-function is used to compute a difference between training examples and current model-estimates. The training algorithm loops over the dataset, each time adjusting the parameters of the model, with the goal to minimize the sum of the loss.

The learning-to-learn concept consists of two loops: an inner training loop to optimize the model’s parameters, and an outer training loop to optimize the algorithm’s hyperparameters. The inner loop optimizes parameters over the *examples* of one task, the outer loop optimizes hyperparameters over the *set of tasks* of an application domain.

Each
base-learning task $\mathcal{T}_{i}$ has a dataset
$D_{i}$ and a learning
objective, the loss function $\mathcal{L}_{i}$. Thus $\mathcal{T}_{i}=(D_{i},\mathcal{L}_{i})$. Each dataset consists of pairs of input-examples and labels
$D_{i}=\{(x_{j},y_{j})\}$, and is split into a training and a testset $D_{i}=\{D_{i,train},D_{i,test}\}$. On each training dataset a parameterized model
$\hat{f}_{\theta_{i}}(D_{i,{train}})$ is estimated, with a loss function
$\mathcal{L}_{i}(\theta_{i},D_{i,{train}})$. The model $\hat{f}$ is approximated
with an algorithm that is governed by a set of hyperparameters
$\omega$. The particular hyperparameters vary from algorithm to
algorithm, but frequently encountered hyperparameters are the learning
rate $\alpha$, the initial parameters $\theta_{0}$, and algorithm
constants.

The inner loop optimizes the base-parameters $\theta$, and the outer loop
optimizes the hyperparameters $\omega$ to find the best performance on
the set of base tasks with the appropriate test data:

|  |  |  |
| --- | --- | --- |
|  | $$ \omega^{\star}=\underbrace{\argmin_{\omega}\mathcal{L}}_{\textrm{outer loop}}(\underbrace{\argmin_{\theta_{i}}\mathcal{L}_{\omega}(\theta_{i},D_{i,train})}_{\textrm{inner loop}}). $$ |  |

The inner loop optimizes $\theta_{i}$ within the datasets $D_{i}$ of the
tasks $\mathcal{T}_{i}$ , and the
outer loop optimizes $\omega$ across the tasks and datasets.
The outcome of the meta
optimization is a set of optimal hyperparameters $\omega^{\star}$.

After metalearning has finished, we have a hyperparameter set (tuned algorithm) that works well for a set of tasks in an application domain, and we can assume that it will generalize well, after training on just a few examples of a new task, scoring high accuracy on testing an unseen example.

<a id="Ch8.S2.SS0.SSS0.Px1"></a>


###### Transfer Learning

There is an important connection between metalearning and transfer learning. Transfer learning pretrains the neural network on a single task, and then performs a transfer of the weights to a quick finetuning phase. Transfer learning can thus be regarded as a single iteration of a network-initialization-based metalearning approach: transfer learning is metalearning with just one base learning task.

<a id="Ch8.S3"></a>


#### 8.3 LLM and Metalearning

<a id="Ch8.S3.p1.1"></a>


In the field of LLM, we encounter metalearning in many places.
A common metalearning approach is to initialize the model parameters to earlier learned knowledge, so that they may train faster on a related task. This is transfer learning, that we find in every standard LLM training pipeline, in the pretrain/finetune phases, where we take the pretrained parameters and finetune them further for a specific task. Metalearning is repeated finetuning, and large language models are a prime example of a metalearning training pipeline that achieves that major goal of machine learning: few-shot learning. In-context learning was one of the major breakthroughs of machine learning [[Brown et al., 2020](#bibg.bib8)].

When we go to agentic LLM, few-shot learning occurs in many other places as well. We will discuss both static and dynamic forms of metalearning. In static metalearning, weights in inner loops are not influenced by other loops. In dynamic metalearning, they are.

<a id="Ch8.S3.SS1"></a>


##### 8.3.1 Static LLM Metalearning

We start by reviewing some examples of static LLM metalearning.

<a id="Ch8.S3.SS1.SSS1"></a>


###### 8.3.1.1 Pretraining Pipeline

The regular LLM training pipeline is a good example of an elaborate, multi-phase, transfer learning scheme. It achieves good zero-shot performance, in the sense that it can answer many regular queries accurately—*where was Mozart born?*—based on the pretrained and finetuned knowledge.

The different phases in the pipeline are the inner optimization loops, and the choices of which weights to transfer, and the manual choices of how to finetune in the subsequent phases, can be considered as the outer loop hyperparameter choices.

This is a static form of metalearning, since the weights, once trained in a phase, are not influenced by training results of later phases. Weights are stable between phases of the pipeline. The pipeline is a purely sequential training process.

<a id="Ch8.S3.SS1.SSS2"></a>


###### 8.3.1.2 In-Context Learning

Going beyond zero-shot learning, in-context learning is a form of few-shot learning where a few training examples are provided by the user, prompting the LLM to infer a better answer. The pretrained model is the inner loop, the examples in the prompt guide the outer loop.

This is a static form of metalearning, since the values of the weights of the model are not influenced by the examples in the prompt.

<a id="Ch8.S3.SS1.SSS3"></a>


###### 8.3.1.3 Chain of Thought

Regular in-context learning provides *facts* as few-shot examples; it is content-focused.
Chain of thought provides *process-steps* as few-shot examples, it is process-focused.

Again, the pretrained model is the inner loop, the examples in the prompt guide the outer loop, and the weights of the model are static.

<a id="Ch8.S3.SS1.SSS4"></a>


###### 8.3.1.4 Static Metalearning is Stable

The regular LLM pipeline consists of transfer learning phases (inner loops), that run in sequence. Once an inner training loop has converged, that phase is not run again. The pipeline is a form of static metalearning. (The results of finetuning are not fed back into the pretrainer again, nor is the pretrainer ran with adjusted hyperparameters based on the finetuning results. The different training phases can not interfere.)

In contrast to static metalearning, there is also dynamic metalearning, where different iterations do interfere.

<a id="Ch8.S3.SS2"></a>


##### 8.3.2 Dynamic LLM Metalearning

In agentic LLMs different forms of dynamic metalearning are used. In dynamic metalearning the iterations are run concurrently, and can have destabilizing effects on each other’s convergence process.

In previous chapters, we have discussed self-reflection, and RLVR. These are approaches where an inner loop can be changed by an outer loop, and results of one inner loop may affect another inner loop. We have created a moving training target. This may cause unstable divergence of the training process. Training results may also appear brittle: they react greatly to small changes in input values or hyperparameters, such as different random seeds, different prompt reformulations, or even changes in the length of the metalearning process itself.
Furthermore, hallucinating tendencies of the base LLM may be amplified when the same model is used in different roles, such as for correction and for generation.

Let us discuss the examples of dynamic metalearning in agentic LLM.

<a id="Ch8.S3.SS2.SSS1"></a>


###### 8.3.2.1 Self-Reflection

In self-reflection (Section [6.2.4.2](chapter-06-multi-step-reasoning-in-llms.md#Ch6.S2.SS4.SSS2 "6.2.4.2 Self-Reflection ‣ 6.2.4 Agentic Harness for Prompt Improvement ‣ 6.2 Self-Reflection and State ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models")) an agentic harness performs prompt management, calling the LLM in different roles, such as, to evaluate a state, and to refine an answer.

In metalearning terms, the *model* is the inner training loop, and the *harness* the outer loop. Although the model itself is static, it is called with different prompts, and the answers of the model are used by the harness to produce new prompts. Therefore, the prompt results (outer loops) start interfering, and may interact in non-linear and non-intuitive ways.

Furthermore, when the same model is used for different roles, imperfections (biases, hallucinations) may be amplified.

<a id="Ch8.S3.SS2.SSS2"></a>


###### 8.3.2.2 RLVR

Reinforcement learning with verifiable rewards (RLVR, Section [6.2.4.3](chapter-06-multi-step-reasoning-in-llms.md#Ch6.S2.SS4.SSS3 "6.2.4.3 Reinforcement Learning with Verifiable Rewards ‣ 6.2.4 Agentic Harness for Prompt Improvement ‣ 6.2 Self-Reflection and State ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models")) is a popular training scheme for code and math applications, where inference-time reasoning results are used for finetuning at training-time.

In metalearning terms, *finetuning* is the inner loop, and inference-time *reasoning* is the outer loop. RLVR uses outer loop results in the inner loop, feeding inference results into the training phase, mixing two learning processes. Care should be taken to prevent that inference time errors, which are used as truths, are amplified in the finetuning/inference loop.

<a id="Ch8.S4"></a>


#### 8.4 Stabilizing Dynamic Metalearning

Unstable training occurs when inner/outer interference is under-damped. When this happens, oscillation between inner loops and outer loops may grow larger, instead of dying out.

<a id="Ch8.S4.p2.1"></a>


This problem can be mitigated by increased damping, or by decoupling the time by which different inner loops move. For example, the learning rates of one of the loops may be reduced, or the parameters of some of the inner loops may be kept stable for a longer time than the other loops. Another idea is to use a mixture of model types or sizes, such as in Mixture-of-Experts [[Jiang et al., 2024](#bibg.bib11)]. A student/teacher setup deliberately uses a stronger and a weaker model for the different roles. By using different models, we may hope to dampen hallucinations and interference between inner loops.

In general, when metalearning misbehaves, we should aim to create more diversity, to stimulate exploration, and to prevent greedy behavior that leads to local optima or divergent training.
These solutions often require much experimentation to build up intuition about the problem. Debugging agentic LLMs can be challenging.

<a id="Ch8.S5"></a>


#### 8.5 Concluding Remarks

As we have seen, we can understand LLM-training as a form of metalearning. Regular LLM training is a form of transfer learning, and inference-time reasoning and training, as is used in agentic LLM, use even more metalearning ideas. Although dynamic metalearning approaches (such as self-reflection) are a powerful concept, care should be taken since interference between inner and outer loops may destabilize the training process. This may happen unexpectedly, in agents that were previously behaving.

When we use a trained model in our agent that interacts with the world, and that agent is also trained using feedback from this interaction, then the model can be regarded as the base learner (inner loop) and the interaction with the world can be regarded as the metalearner (outer loop). All the preceding caveats for in-pipeline metalearning also apply for out-of-pipeline metalearning. Only now, when interacting with the real world, the consequence of errors may be more severe.

<a id="Ch8.S5.p3.1"></a>


Related fields of online machine learning, such as deep reinforcement learning, also suffer from the unstable training and the moving target problem.
The field of deep reinforcement learning has introduced many stabilization techniques, such as replay buffers and target networks [[Mnih et al., 2015](#bibg.bib7), [Hessel et al., 2018](#bibg.bib2)]. These methods typically try to decouple the periodicity of the two learning processes, often by slowing down one of them.
A similar approach is introduced in Hierarchical Reasoning Models (HRM) [[Wang et al., 2025](#bibg.bib10)]. HRM consists of a two-layer metalearning approach. Here, too, the learning is stabilized by learning at two different speeds.

Knowledge of such stabilization methods is useful when designing agentic LLM solutions. In the next part we will provide an overview of the different interaction styles by which agentic LLM interact with the world. The styles go from static to dynamic.

<a id="bibg"></a>


### References

<a id="bibg.bib1"></a>
- Brazdil et al. (2022)
  P. Brazdil, J. N. Van Rijn, C. Soares, and J. Vanschoren
  Metalearning: applications to automated machine learning and data mining.
   Springer Nature.
  Cited by: [§8.1.2](#Ch8.S1.SS2.p5.1 "8.1.2 Achieving Few-shot Learning ‣ 8.1 Why Metalearning? ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib8"></a>
- Brown et al. (2020)
  T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al.
  Language models are few-shot learners.
  Advances in neural information processing systems 33, pp. 1877–1901.
  Cited by: [§8.3](#Ch8.S3.p1.1 "8.3 LLM and Metalearning ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib6"></a>
- Finn et al. (2017)
  C. Finn, P. Abbeel, and S. Levine
  Model-agnostic meta-learning for fast adaptation of deep networks.
  In International conference on machine learning,
  pp. 1126–1135.
  Cited by: [§8.1.2](#Ch8.S1.SS2.p5.1 "8.1.2 Achieving Few-shot Learning ‣ 8.1 Why Metalearning? ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib2"></a>
- Hessel et al. (2018)
  M. Hessel, J. Modayil, H. Van Hasselt, T. Schaul, G. Ostrovski, W. Dabney, D. Horgan, B. Piot, M. Azar, and D. Silver
  Rainbow: combining improvements in deep reinforcement learning.
  In Proceedings of the AAAI conference on artificial intelligence,
  Vol. 32.
  Cited by: [§8.5](#Ch8.S5.p3.1 "8.5 Concluding Remarks ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib4"></a>
- Hospedales et al. (2021)
  T. Hospedales, A. Antoniou, P. Micaelli, and A. Storkey
  Meta-learning in neural networks: a survey.
  IEEE transactions on pattern analysis and machine intelligence 44 (9), pp. 5149–5169.
  Cited by: [§8.1.1](#Ch8.S1.SS1.p1.1 "8.1.1 Deep Learning is Slow ‣ 8.1 Why Metalearning? ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib5"></a>
- Huisman et al. (2021)
  M. Huisman, J. N. Van Rijn, and A. Plaat
  A survey of deep meta-learning.
  Artificial Intelligence Review 54 (6), pp. 4483–4541.
  Cited by: [§8.1.1](#Ch8.S1.SS1.p1.1 "8.1.1 Deep Learning is Slow ‣ 8.1 Why Metalearning? ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib11"></a>
- Jiang et al. (2024)
  A. Q. Jiang, A. Sablayrolles, A. Roux, A. Mensch, B. Savary, C. Bamford, D. S. Chaplot, D. de las Casas, E. B. Hanna, F. Bressand, G. Lengyel, G. Bour, G. Lample, L. R. Lavaud, L. Saulnier, M. Lachaux, P. Stock, S. Subramanian, S. Yang, S. Antoniak, T. L. Scao, T. Gervet, T. Lavril, T. Wang, T. Lacroix, and W. E. Sayed
  Mixtral of experts.
  External Links: 2401.04088,
  [Link](https://arxiv.org/abs/2401.04088)
  Cited by: [§8.4](#Ch8.S4.p2.1 "8.4 Stabilizing Dynamic Metalearning ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib3"></a>
- Krizhevsky et al. (2012)
  A. Krizhevsky, I. Sutskever, and G. E. Hinton
  Imagenet classification with deep convolutional neural networks.
  Advances in neural information processing systems 25.
  Cited by: [§8.1.1](#Ch8.S1.SS1.p2.1 "8.1.1 Deep Learning is Slow ‣ 8.1 Why Metalearning? ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib7"></a>
- Mnih et al. (2015)
  V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski, et al.
  Human-level control through deep reinforcement learning.
  nature 518 (7540), pp. 529–533.
  Cited by: [§8.5](#Ch8.S5.p3.1 "8.5 Concluding Remarks ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib9"></a>
- Schmidhuber (1987)
  J. Schmidhuber
  Evolutionary principles in self-referential learning, or on learning how to learn: the meta-meta-… hook.
  Ph.D. Thesis, Technische Universität München.
  Cited by: [§8.1.1](#Ch8.S1.SS1.p1.1 "8.1.1 Deep Learning is Slow ‣ 8.1 Why Metalearning? ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
<a id="bibg.bib10"></a>
- Wang et al. (2025)
  G. Wang, J. Li, Y. Sun, X. Chen, C. Liu, Y. Wu, M. Lu, S. Song, and Y. A. Yadkori
  Hierarchical reasoning model.
  arXiv preprint arXiv:2506.21734.
  Cited by: [§8.5](#Ch8.S5.p3.1 "8.5 Concluding Remarks ‣ Chapter 8 Metalearning ‣ Part II Reasoning ‣ Agentic Large Language Models").
