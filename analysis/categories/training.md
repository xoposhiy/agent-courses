# Model training and adaptation

Methods, data, learning signals, and systems used to change weights or learn across tasks.

Prompt search without weight updates belongs under reasoning techniques. Serving optimizations belong under runtime. RL systems stay here because their purpose is training.

[All categories](README.md) · [CSV](training.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**22 concepts**: 19 confirmed in courses; 3 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Supervised fine-tuning](#concept-sft) | method | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| [Reinforcement learning](#concept-rl) | topic | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| [Synthetic data and trajectory generation](#concept-synthetic-data) | method | 4 | 3 | 1 | S329, CMU, EVAL, CU |  | yes |
| [Human demonstrations and feedback](#concept-human-demos) | method | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| [Model training and post-training](#concept-model-training) | topic | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| [Reward modeling](#concept-reward-model) | method | 3 | 3 | 0 | S329, COL, CMU |  |  |
| [Training data selection and quality](#concept-data-curation) | topic | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| [Group relative policy optimization](#concept-grpo) | method | 2 | 2 | 0 | S329, CMU |  |  |
| [Knowledge distillation](#concept-distillation) | method | 2 | 2 | 0 | S329, CMU |  | yes |
| [Proximal policy optimization](#concept-ppo) | method | 2 | 2 | 0 | S329, CMU |  |  |
| [Reinforcement learning from human feedback](#concept-rlhf) | method | 2 | 2 | 0 | S329, COL |  | yes |
| [Credit assignment and advantage estimation](#concept-rl-credit) | method | 1 | 1 | 0 | CMU |  |  |
| [Direct preference optimization](#concept-dpo) | method | 1 | 1 | 0 | COL |  | yes |
| [Distributed and asynchronous RL systems](#concept-rl-systems) | topic | 1 | 1 | 0 | CMU |  |  |
| [Exploration and curriculum design](#concept-rl-exploration) | topic | 1 | 1 | 0 | CMU |  |  |
| [Gradient descent and backpropagation](#concept-gradient-training) | method | 1 | 1 | 0 | COL |  | yes |
| [Low-rank adaptation](#concept-lora) | method | 1 | 1 | 0 | COL |  | yes |
| [Policy gradient methods](#concept-rl-policy-gradient) | method | 1 | 1 | 0 | CMU |  |  |
| [Self-play training](#concept-self-play) | method | 1 | 0 | 1 | CU |  | yes |
| [Meta-learning](#concept-meta-learning) | topic | 0 | 0 | 0 |  |  | yes |
| [Model collapse and synthetic-data risks](#concept-model-collapse) | concept | 0 | 0 | 0 |  |  | yes |
| [Model-based reinforcement learning](#concept-model-based-rl) | method | 0 | 0 | 0 |  |  | yes |

## Course codes

- **S329**: [Engineering AI Agents](../courses/stanford-cs329z.md)
- **COL**: [Designing LLM Agents](../courses/columbia-coms4995.md)
- **CMU**: [AI Agents](../courses/cmu-11768.md)
- **LC**: [Introduction to Deep Agents](../courses/langchain-deep-agents.md)
- **S224**: [Agentic AI](../courses/stanford-cs224v.md)
- **EVAL**: [Evaluating and Improving Agentic Applications](../courses/dlai-agentic-evals.md)
- **CU**: [Building AI Agents](../courses/colorado-csci7000.md)
- **BOOK**: [Agentic Large Language Models](../courses/agentic-large-language-models.md)

## Definitions and evidence

Entries follow frequency order. Related categories are navigation links; they do not create additional category membership or frequency.

<a id="concept-sft"></a>

### Supervised fine-tuning

`sft` · Training and adaptation · original type: method

Train a model on examples of desired responses or action trajectories.

**Aliases:** SFT; instruction fine-tuning.

**Evidence:** [S329, taught, p. 71](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [COL, taught, p. 16](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 12](../../courses/cmu-11768/markdown/slides/lecture-08-sft.md); [S224, taught, p. 42](../../courses/stanford-cs224v/markdown/slides/l-churro.md); [CU, assigned, p. 2](../../courses/colorado-csci7000/markdown/readings/arxiv-2302-04761.md); [BOOK, taught, line 195](../../courses/agentic-large-language-models/markdown/chapters/chapter-03-the-large-language-model-training-pipeline.md).

<a id="concept-rl"></a>

### Reinforcement learning

`rl` · Training and adaptation · original type: topic

Learn a policy by using rewards from interaction.

**Aliases:** RL.

**Evidence:** [S329, taught, p. 80](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [COL, taught, p. 7](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 7](../../courses/cmu-11768/markdown/slides/lecture-09-rl-basics.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2512-18552.md); [BOOK, taught, line 612](../../courses/agentic-large-language-models/markdown/chapters/chapter-07-vision-action-and-world-models.md).

<a id="concept-synthetic-data"></a>

### Synthetic data and trajectory generation

`synthetic-data` · Training data and risks · original type: method

Generate tasks, examples, or agent rollouts for training or testing.

**Aliases:** synthetic data generation; synthesized trajectories.

**Evidence:** [S329, taught, p. 38](../../courses/stanford-cs329z/markdown/slides/lecture11.md); [CMU, taught, p. 51](../../courses/cmu-11768/markdown/slides/lecture-06-coding-agents.md); [EVAL, taught, p. 34](../../courses/dlai-agentic-evals/markdown/slides/module-2.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2512-18552.md); [BOOK, taught, line 455](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-human-demos"></a>

### Human demonstrations and feedback

`human-demos` · Training data and risks · original type: method

Collect human actions or feedback to train or improve an agent.

**Aliases:** human demonstrations; human feedback.

**Also relevant to:** [Agent behavior, human interaction, and interpretability](behavior.md).

**Evidence:** [S329, taught, p. 21](../../courses/stanford-cs329z/markdown/slides/lecture11.md); [COL, taught, p. 23](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 62](../../courses/cmu-11768/markdown/slides/lecture-07-computer-use-agents.md); [BOOK, taught, line 239](../../courses/agentic-large-language-models/markdown/chapters/chapter-19-synthetic-data-generation-for-training-agentic-llms.md).

<a id="concept-model-training"></a>

### Model training and post-training

`model-training` · Training and adaptation · original type: topic

Train model weights before or after initial pretraining.

**Aliases:** LLM training; posttraining.

**Evidence:** [S329, taught, p. 111](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, p. 3](../../courses/columbia-coms4995/markdown/slides/week3.md); [CMU, taught, p. 6](../../courses/cmu-11768/markdown/slides/lecture-08-sft.md); [BOOK, taught, line 12](../../courses/agentic-large-language-models/markdown/chapters/chapter-03-the-large-language-model-training-pipeline.md).

<a id="concept-reward-model"></a>

### Reward modeling

`reward-model` · RL learning signals and systems · original type: method

Learn or define a score that guides policy training.

**Aliases:** reward models; reward functions.

**Evidence:** [S329, taught, p. 89](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [COL, taught, p. 22](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 10](../../courses/cmu-11768/markdown/slides/lecture-20-search-basics.md).

<a id="concept-data-curation"></a>

### Training data selection and quality

`data-curation` · Training data and risks · original type: topic

Select and check useful tasks, demonstrations, and trajectories.

**Related terms:** data selection; data quality.

**Evidence:** [S329, taught, p. 35](../../courses/stanford-cs329z/markdown/slides/lecture12.md); [COL, taught, line 55](../../courses/columbia-coms4995/markdown/assignments/hw1.md); [CMU, taught, p. 2](../../courses/cmu-11768/markdown/slides/lecture-08-sft.md); [BOOK, taught, line 93](../../courses/agentic-large-language-models/markdown/chapters/chapter-03-the-large-language-model-training-pipeline.md).

<a id="concept-grpo"></a>

### Group relative policy optimization

`grpo` · Training and adaptation · original type: method

Compare rewards within groups of sampled outputs to update a policy.

**Aliases:** GRPO.

**Evidence:** [S329, taught, p. 95](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [CMU, taught, p. 38](../../courses/cmu-11768/markdown/slides/lecture-09-rl-basics.md).

<a id="concept-distillation"></a>

### Knowledge distillation

`distillation` · Training and adaptation · original type: method

Train a model to follow the outputs or behavior of a teacher model.

**Aliases:** on-policy distillation.

**Evidence:** [S329, taught, p. 96](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [CMU, taught, p. 22](../../courses/cmu-11768/markdown/slides/lecture-08-sft.md); [BOOK, taught, line 373](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-ppo"></a>

### Proximal policy optimization

`ppo` · Training and adaptation · original type: method

Update a policy with a clipped objective to limit policy changes.

**Aliases:** PPO.

**Evidence:** [S329, taught, p. 95](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [CMU, taught, p. 42](../../courses/cmu-11768/markdown/slides/lecture-09-rl-basics.md).

<a id="concept-rlhf"></a>

### Reinforcement learning from human feedback

`rlhf` · Training and adaptation · original type: method

Train a reward model from human preferences and use it to guide policy updates.

**Aliases:** RLHF.

**Evidence:** [S329, taught, p. 114](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, p. 23](../../courses/columbia-coms4995/markdown/slides/week5.md); [BOOK, taught, line 236](../../courses/agentic-large-language-models/markdown/chapters/chapter-03-the-large-language-model-training-pipeline.md).

<a id="concept-rl-credit"></a>

### Credit assignment and advantage estimation

`rl-credit` · RL learning signals and systems · original type: method

Estimate which actions contribute to reward and use baselines or value estimates.

**Aliases:** advantage estimation.

**Related terms:** GAE.

**Evidence:** [CMU, taught, p. 25](../../courses/cmu-11768/markdown/slides/lecture-09-rl-basics.md).

<a id="concept-dpo"></a>

### Direct preference optimization

`dpo` · Training and adaptation · original type: method

Train directly on preferred and rejected response pairs.

**Aliases:** DPO.

**Evidence:** [COL, taught, p. 7](../../courses/columbia-coms4995/markdown/slides/week5.md); [BOOK, taught, line 236](../../courses/agentic-large-language-models/markdown/chapters/chapter-03-the-large-language-model-training-pipeline.md).

<a id="concept-rl-systems"></a>

### Distributed and asynchronous RL systems

`rl-systems` · RL learning signals and systems · original type: topic

Coordinate rollout generation, training engines, and policy synchronization.

**Aliases:** async RL; agentic RL systems.

**Also relevant to:** [Runtime, deployment, and performance](runtime.md).

**Evidence:** [CMU, taught, p. 25](../../courses/cmu-11768/markdown/slides/lecture-12-rl-systems.md).

<a id="concept-rl-exploration"></a>

### Exploration and curriculum design

`rl-exploration` · RL learning signals and systems · original type: topic

Maintain useful policy exploration and select training tasks by difficulty.

**Related terms:** exploration collapse; curriculum learning.

**Evidence:** [CMU, taught, p. 47](../../courses/cmu-11768/markdown/slides/lecture-11-rl-advanced.md).

<a id="concept-gradient-training"></a>

### Gradient descent and backpropagation

`gradient-training` · Training and adaptation · original type: method

Compute loss gradients and update neural-network weights.

**Aliases:** backpropagation; gradient descent.

**Evidence:** [COL, taught, p. 24](../../courses/columbia-coms4995/markdown/slides/week2.md); [BOOK, taught, line 537](../../courses/agentic-large-language-models/markdown/chapters/chapter-02-foundations-of-language-modeling-with-llms.md).

<a id="concept-lora"></a>

### Low-rank adaptation

`lora` · Training and adaptation · original type: method

Adapt a model by training small low-rank weight updates.

**Aliases:** LoRA.

**Related terms:** parameter-efficient fine-tuning (PEFT).

**Evidence:** [COL, taught, p. 40](../../courses/columbia-coms4995/markdown/slides/week5.md); [BOOK, taught, line 311](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-rl-policy-gradient"></a>

### Policy gradient methods

`rl-policy-gradient` · RL learning signals and systems · original type: method

Update a policy using gradients of expected reward.

**Aliases:** policy gradients.

**Related terms:** REINFORCE.

**Evidence:** [CMU, taught, p. 22](../../courses/cmu-11768/markdown/slides/lecture-09-rl-basics.md).

<a id="concept-self-play"></a>

### Self-play training

`self-play` · RL learning signals and systems · original type: method

Generate training challenges through interaction between agents or roles and learn from the resulting tasks.

**Aliases:** self play.

**Related terms:** self-play SWE-RL.

**Evidence:** [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2512-18552.md); [BOOK, taught, line 158](../../courses/agentic-large-language-models/markdown/chapters/chapter-19-synthetic-data-generation-for-training-agentic-llms.md).

<a id="concept-meta-learning"></a>

### Meta-learning

`meta-learning` · Training and adaptation · original type: topic

Learn how to adapt to new tasks through shared learning structure.

**Aliases:** metalearning; learning to learn.

**Evidence:** [BOOK, taught, line 78](../../courses/agentic-large-language-models/markdown/chapters/chapter-08-metalearning.md).

<a id="concept-model-collapse"></a>

### Model collapse and synthetic-data risks

`model-collapse` · Training data and risks · original type: concept

Study how repeated training on generated data can reduce quality or diversity.

**Aliases:** synthetic data collapse.

**Also relevant to:** [Safety, security, and trust](safety-trust.md).

**Evidence:** [BOOK, taught, line 414](../../courses/agentic-large-language-models/markdown/chapters/chapter-19-synthetic-data-generation-for-training-agentic-llms.md).

<a id="concept-model-based-rl"></a>

### Model-based reinforcement learning

`model-based-rl` · RL learning signals and systems · original type: method

Use a learned or given environment model to plan or improve a policy.

**Aliases:** model based RL.

**Evidence:** [BOOK, taught, line 393](../../courses/agentic-large-language-models/markdown/chapters/chapter-07-vision-action-and-world-models.md).
