# LangSmith: Evaluation

[Course index](../../README.md) · [Original source](https://docs.langchain.com/langsmith/evaluation) · [Raw file](../../raw/optional-readings/ref-1cb888b65fa5.html)

Retrieved: 2026-11-13T16:58:33.265272+00:00

# LangSmith Evaluation

Copy pageCopy page

Evaluate and test agent quality at scale with datasets, evaluators, prompts, and Studio.

Copy pageCopy page

LangSmith’s testing tools help you measure agent quality, iterate on prompts, and debug live in an interactive environment. Evaluation is the core of testing: it scores your agent’s outputs against datasets and criteria so you can benchmark versions, catch regressions, and track quality over time.
Add real traces to a dataset so a failure you saw once becomes a test you run every time.
LangSmith supports two types of evaluation based on when and where they run:

## Offline Evaluation

**Test before you ship**Run evaluations on curated datasets during development to compare versions, benchmark performance, and catch regressions.

## Online Evaluation

**Monitor in production**Evaluate real user interactions in real-time to detect issues and measure quality on live traffic.

## Set up your account

Create an account

Sign up at [smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=snippets-langsmith-account-api-key-quickstart) (no credit card required).
You can log in with **Google**, **GitHub**, or **email**.

Create an API key

Go to your [Settings page](https://smith.langchain.com/settings) > **API Keys** > **Create API Key**.
Copy the key and save it securely.

Once your account and API key are ready, [run your first evaluation](https://docs.langchain.com/langsmith/evaluation-quickstart).

## Evaluation workflow

- Offline evaluation flow
- Online evaluation flow

1

Create a dataset

Create a [dataset](https://docs.langchain.com/langsmith/manage-datasets) with [examples](https://docs.langchain.com/langsmith/evaluation-concepts#examples) from manually curated test cases, historical production traces, or synthetic data generation.

2

Define evaluators

Create [evaluators](https://docs.langchain.com/langsmith/evaluation-concepts#evaluators) to score performance:

- [Human](https://docs.langchain.com/langsmith/evaluation-concepts#human) review
- [Code](https://docs.langchain.com/langsmith/evaluation-concepts#code) rules
- [LLM-as-judge](https://docs.langchain.com/langsmith/llm-as-judge)
- [Pairwise](https://docs.langchain.com/langsmith/evaluate-pairwise) comparison

3

Run an experiment

Execute your application on the dataset to create an [experiment](https://docs.langchain.com/langsmith/evaluation-concepts#experiment). Configure [repetitions, concurrency, and caching](https://docs.langchain.com/langsmith/experiment-configuration) to optimize runs.

4

Analyze results

Compare experiments for [benchmarking](https://docs.langchain.com/langsmith/evaluation-types#benchmarking), [unit tests](https://docs.langchain.com/langsmith/evaluation-types#unit-tests), [regression tests](https://docs.langchain.com/langsmith/evaluation-types#regression-tests), or [backtesting](https://docs.langchain.com/langsmith/evaluation-types#backtesting).

1

Deploy your application

Each interaction creates a [run](https://docs.langchain.com/langsmith/evaluation-concepts#runs) without reference outputs.

2

Configure online evaluators

Set up [evaluators](https://docs.langchain.com/langsmith/online-evaluations-llm-as-judge) to run automatically on production traces: safety checks, format validation, quality heuristics, and reference-free LLM-as-judge. Apply [filters and sampling rates](https://docs.langchain.com/langsmith/online-evaluations-llm-as-judge#configure-a-sampling-rate) to control costs.

3

Monitor in real-time

Evaluators run automatically on [runs](https://docs.langchain.com/langsmith/evaluation-concepts#runs) or [threads](https://docs.langchain.com/langsmith/online-evaluations-multi-turn), providing real-time monitoring, anomaly detection, and alerting.

4

Establish a feedback loop

Add failing production traces to your [dataset](https://docs.langchain.com/langsmith/manage-datasets), create targeted evaluators, validate fixes with offline experiments, and redeploy.

For more on the differences between offline and online evaluation, refer to the [Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts#quick-reference-offline-vs-online-evaluation) page.

## Get started

## Evaluation quickstart

Get started with offline evaluation.

## Manage datasets

Create and manage datasets for evaluation through the UI or SDK.

## Run offline evaluations

Explore evaluation types, techniques, and frameworks for comprehensive testing.

## Analyze results

View and analyze evaluation results, compare experiments, filter data, and export findings.

## Run online evaluations

Monitor production quality in real-time from the Observability tab.

## Follow tutorials

Learn by following step-by-step tutorials, from simple chatbots to complex agent evaluations.

## Studio

Use an interactive environment for developing and debugging agents.

To set up a LangSmith instance, visit the [Platform setup section](https://docs.langchain.com/langsmith/platform-setup) to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.

---

[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo
