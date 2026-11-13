# τ-bench task fixes

[Course index](../../README.md) · [Original source](https://taubench.com/blog/tau3-task-fixes.html) · [Raw file](../../raw/optional-readings/ref-197ad5ccda9a.html)

Retrieved: 2026-11-13T16:56:29.491017+00:00

Engineering

# τ³-Bench: Fixing Airline + Retail

February 2026

By [Victor Barres](https://taubench.com/authors/victor-barres.html) and [Ben Shi](https://taubench.com/authors/ben-shi.html)

TL;DR

We audited and fixed **50+ tasks** across the airline and retail domains in τ-bench. Fixes addressed incorrect expected actions, ambiguous user instructions, impossible constraints, and missing fallback behaviors.

Since its release, τ-bench has seen widespread adoption as a benchmark for evaluating tool-using language agents. Along with that adoption, the community has been invaluable in identifying issues — from annotation errors to underspecified tasks — in the original **airline** (50 tasks) and **retail** (114 tasks) domains.

As we prepared for the τ³ release, we set out to address this feedback head-on. The majority of fixes were **obtained directly from [τ-Bench Verified](arxiv-2512-07850.md)** (Cuadron et al., SABER), which systematically identified annotation errors and underspecified tasks in the original benchmark. We collaborated closely with the team at Amazon on this effort — going back and forth on proposed revisions until reaching consensus on each fix. We also incorporated additional fixes from **community pull requests**, including several from Anthropic, and integrated everything into the official task set.

This post summarizes what we fixed and how it changed model scores.

## What We Fixed

Fixes fell into five broad categories:

27
airline tasks fixed

26
retail tasks fixed

### 1. Incorrect Expected Actions

The most impactful category. Several tasks included expected actions that were **wrong according to the domain's own policy**. For example:

- **Incorrect delayed flight compensation** (airline tasks 2, 27, 38): Tasks expected the agent to offer compensation for delayed flights, but the policy only allows compensation for silver/gold members, insured passengers, or business flyers. Regular economy passengers with no insurance shouldn't receive compensation — yet the expected actions said otherwise.
- **Incorrect cancellation actions** (airline tasks 9, 37): Tasks expected cancellation of reservations that didn't meet any of the cancellation criteria (not within 24 hours, no airline cancellation, not business class, no travel insurance).
- **Invalid PayPal refunds** (retail tasks 12, 13): Expected actions included refunding to PayPal, which isn't a supported refund method in the retail domain.

### 2. Ambiguous User Instructions

Many tasks had user simulation instructions that left key information underspecified, causing the simulated user to behave unpredictably across trials:

- **Economy vs. basic economy confusion** (airline tasks 15, 16): The user asked for "economy" but the expected actions assumed basic economy. We added explicit disambiguation.
- **"Similar" vs. "same" item** (retail tasks 0, 1): Users asking for a "similar" keyboard during an exchange led models to search broadly. Changed to "the same one" to match the expected exchange behavior.
- **Missing cancellation reasons** (retail task 76): The user's reason for cancellation was implicit, causing agents to ask follow-up questions that diverged from the expected flow.
- **Quantity precision** (retail tasks 2, 3, 4): Users asking "how many t-shirts" without the word "exactly" led agents to give approximate answers. Added precision.

### 3. Impossible or Contradictory Constraints

Some tasks asked agents to do things that were structurally impossible:

- **Impossible payment constraint** (airline task 14): The task required using a Mastercard, but the user profile contained no Mastercard. We replaced the constraint with a valid payment method.
- **Location contradiction** (airline task 42): The user's address said Boston but the scenario described them as being in a different city.
- **Invalid same-item exchange** (retail tasks 18, 91): Tasks expected exchanging an item for the exact same item (same SKU), which the retail system doesn't support as a valid exchange.

### 4. Missing Fallback Behaviors

Several tasks didn't specify what the user should do when the agent's search didn't return the expected results:

- **Speaker search fallback** (retail task 62): If the product search returned no matching speakers, the user had no instructions for how to proceed.
- **Boots exchange fallback** (retail task 54): Similar issue — no guidance when the desired exchange item wasn't available.
- **Non-modifiable order fallback** (retail task 20): The user needed instructions for what to do if their order couldn't be modified.

### 5. Policy Loophole Prevention

Some tasks could be "solved" by agents using clever workarounds that violated the spirit of the task:

- **Cabin upgrade loophole** (airline task 45): An agent could upgrade cabin class and then change flights as a workaround to modify a basic economy booking, which should be disallowed.
- **Cancel-and-rebook workaround** (airline task 13): Instead of correctly refusing to modify a basic economy flight, an agent could cancel and rebook — the task needed to explicitly test that the agent refuses modification.
- **Destination change via modification** (airline task 29): The policy requires cancel+rebook when changing destinations, but the task didn't enforce this.

🔧 All Task Fixes

Domain:
All
Airline
Retail

Category:
All
Incorrect Action
Ambiguity
Constraint
Fallback
Loophole
Data Fix
Tool

| Task | Domain | Category | Description |
| --- | --- | --- | --- |

## Before & After Results

We re-ran all three models on both domains after applying the fixes. The chart below shows pass^1 and pass^4 scores before and after:

📊 Before vs. After Task Fixes

Metric:
pass^1
pass^4
4 trials per task

The most dramatic improvement is in **airline**, where pass^1 increased by **+14.0 to +20.0 points** depending on the model. This is largely because many of the original airline tasks penalized agents for *correctly* following the policy — once those incorrect expected actions were removed, all models saw substantial gains.

Retail improvements were more modest (**-0.4 to +5.5 points** on pass^1) because the original retail tasks had fewer outright incorrect expected actions. Most retail fixes addressed ambiguity and missing fallback behaviors, which primarily reduced variance across trials rather than uniformly boosting scores.

An interesting pattern: **pass^4 improvements were often even larger than pass^1 improvements** in airline, particularly for GPT-5.2 (high), which went from 50.0% to 72.0% — a +22 point gain. This suggests the fixes disproportionately helped tasks where the model was intermittently succeeding, by removing evaluation noise that turned some correct completions into false negatives.

The updated tasks are now live on the [leaderboard](https://taubench.com/#leaderboard), and all trajectory data is available in the [trajectory visualizer](https://taubench.com/#trajectory-visualizer). The fixes are also reflected in the open-source [repository](https://github.com/sierra-research/tau2-bench).

## Citation

```
@misc{cuadron2025sabersmallactionsbig,
  title={SABER: Small Actions, Big Errors -- Safeguarding Mutating Steps in LLM Agents},
  author={Alejandro Cuadron and Pengfei Yu and Yang Liu and Arpit Gupta},
  year={2025},
  eprint={2512.07850},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2512.07850}
}

@misc{barres2025tau2,
  title={$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment},
  author={Victor Barres and Honghua Dong and Soham Ray and Xujie Si and Karthik Narasimhan},
  year={2025},
  eprint={2506.07982},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2506.07982}
}
```

[← Back to τ-bench Leaderboard](https://taubench.com/)
