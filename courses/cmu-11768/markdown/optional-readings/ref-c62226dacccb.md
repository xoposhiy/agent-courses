# Berkeley Function-Calling Leaderboard V4

[Course index](../../README.md) · [Original source](https://gorilla.cs.berkeley.edu/leaderboard.html) · [Raw file](../../raw/optional-readings/ref-c62226dacccb.html)

Retrieved: 2026-11-13T16:54:43.561964+00:00

[Home](https://gorilla.cs.berkeley.edu/index.html)
[Blog](ref-79b96b09b5d7.md)
[Try it Out!](ref-c62226dacccb.md)
[Leaderboard](ref-c62226dacccb.md)

# UC Berkeley Logo Berkeley Function-Calling Leaderboard

## BFCL: From Tool Use to Agentic Evaluation of Large Language Models

The Berkeley Function Calling Leaderboard (BFCL) V4
evaluates the
LLM's ability to call functions (aka tools) accurately. This
leaderboard consists of real-world data and will be updated periodically. For more information on the
evaluation dataset and methodology, please refer to our blogs: [BFCL-v1](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html) introducing AST as an
evaluation metric,
[BFCL-v2](https://gorilla.cs.berkeley.edu/blogs/12_bfcl_v2_live.html) introducing enterprise and OSS-contributed functions,
[BFCL-v3](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html) introducing multi-turn interactions, and
[BFCL-v4](ref-79b96b09b5d7.md) introducing holistic agentic evaluation. Checkout [code and
data](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard).

***Last Updated:
2026-04-12      [[Change
Log]](https://github.com/ShishirPatil/gorilla/blob/main/berkeley-function-call-leaderboard/CHANGELOG.md)***

Search

**FC** = native support for function/tool calling.
**Prompt** = walk-around for function calling, using model's normal text generation capability.

**Cost** is calculated as an estimate of the cost for the entire benchmark, in USD.
**Latency** is measured in seconds.

**Overall Accuracy** is the **unweighted** average of all the sub-categories.
For details on score composition, please refer to our [blog](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html#leaderboard-composition).

**Format sensitivity** test cases are only supported for prompt (non-FC) models.

Click on column header to sort. If you would like to add
your model or contribute test-cases, please contact us via [discord](https://discord.gg/grXXvj9Whz).

Models are evaluated using commit **f7cf735**.
All the model response we obtained is available [here](https://github.com/HuanzhiMao/BFCL-Result).
To reproduce the results, please either checkout our codebase at
[this
checkpoint](https://github.com/ShishirPatil/gorilla/commit/f7cf7359b7ac615a0b294831c5ba2bc95ee4a000),
or install the PyPI package `pip install bfcl-eval==2025.12.17`.

## Wagon Wheel

The following chart shows the comparison of the models based on a few
metrics. You can select and deselect which models to compare. More
information on each metric can be found in the
[blog](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html#benchmarking).

Select Models to Compare
Clear All

Search models...


## Function Calling Demo

In this demo for function calling, you can enter a prompt and a
function and see the output. There will be two outputs (and two output
boxes accordingly): one in the actual code format (the top one) and
the other in the OpenAI compatible format (the bottom one). Note that
the OpenAI compatible format output is only available if the actual
code output has valid syntax and can be parsed. We also provide you a
few examples to try out and get a sense of the input format and the
output.

Example 1
Example 2
Example 3

Model:

Gorilla OpenFunctions-v2

Temperature:

0.7


Submit

Output will be shown here:

OpenAI compatible format output:

👍
👎
Report Issue

## Contact Us

## Citation

```
@inproceedings{patil2025bfcl,
title={The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models}, 
author={Patil, Shishir G. and Mao, Huanzhi and Cheng-Jie Ji, Charlie and Yan, Fanjia and Suresh, Vishnu and Stoica, Ion and E. Gonzalez, Joseph},
booktitle={Forty-second International Conference on Machine Learning},
year={2025},
}
```
