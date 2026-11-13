# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m4/m4.3-dynamic-subagents.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m4/m4.3-dynamic-subagents.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m4/m4.3-dynamic-subagents.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m4.3-dynamic-subagents.md)

Python TypeScript

<a id="dynamic-subagents"></a>


# Dynamic Subagents

```text
<button class="lt-tab active" data-p="ds" role="tab" aria-selected="true">Dynamic Subagents</button>
```

```text
<button class="lt-tab" data-p="lab" role="tab" aria-selected="false">Lab</button>
```

```text
<button class="lt-tab" data-p="quiz" role="tab" aria-selected="false">Quiz</button>
```

```text
<button class="lt-tab" data-p="homework" role="tab" aria-selected="false">Homework</button>
```

<a id="p-ds"></a>


Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/u4S3dWlvLnJ.md)

Lesson Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/u4S3dWlvLnJ.md)

<a id="from-one-subagent-to-many"></a>


## From one subagent to many

In the last lesson, delegation meant the model calling the `task` tool once per subagent: one `genre-researcher` call for Rock, one for Metal, and so on for all four genres. At that scale it works fine. Four items is a short list, so the model can track them itself and even send all four calls in parallel within the same turn.

Now say the job is 1,000 sales transcripts, same task on every one: summarize it. There’s no longer a short list the model can enumerate in its head, and someone still has to track which ones are done.

Leaving that to the model brings back the problem that breaks agents at scale. The model would have to keep track of which transcripts are done while its context window keeps shrinking.

What happens if you leave this to the model?

In practice, a model asked to take on all 1,000 transcripts itself wouldn’t just cleanly fail. Depending on the model, it would more likely:

- Refuse outright, saying it can’t process that many in one pass.
- Try to chunk the work into rough ranges across subagent calls, e.g. transcripts 0-100, then 100-200, and so on, hoping it remembers where it left off.
- Try to fire off everything in batches of roughly 20 calls at a time, since that’s close to the practical ceiling on how many tool calls a model can issue in parallel.

None of these guarantee every transcript actually gets touched; each one still leaves the bookkeeping to the model.

<a id="programmatic-orchestration"></a>


### Programmatic orchestration

Dynamic subagents solve this with [programmatic orchestration](../../../../../readings/www-langchain-com-blog-introducing-dynamic-subagents-in-deep-agents-f27164f7.md). Instead of issuing subagent tasks through tool calls turn by turn, the model writes a short script that orchestrates and calls subagents. It leans on code patterns it already knows: looping, branching, concurrency. That script runs in a lightweight interpreter.

Here’s that same difference written as code:

```text
# the model enumerates each item itself, and has to remember its own place
task(description="summarize transcript 1 of 1,000")
task(description="summarize transcript 2 of 1,000")
# ...however many calls it takes, nothing guarantees it reaches transcript 1,000...
```

```text
# written once, run by code: the loop is the guarantee, not the model's memory
for transcript in transcripts:
    task(description=f"summarize {transcript}")
```

```text
// the model enumerates each item itself, and has to remember its own place
task({ description: "summarize transcript 1 of 1,000" });
task({ description: "summarize transcript 2 of 1,000" });
// ...however many calls it takes, nothing guarantees it reaches transcript 1,000...
```

```text
// written once, run by code: the loop is the guarantee, not the model's memory
for (const transcript of transcripts) {
  task({ description: `summarize ${transcript}` });
}
```

`task()` itself didn’t change; it’s the same subagent call either way. The change is in *where the decision to keep going lives*:

- **First version:** in the model, however many calls it takes.
- **Second version:** in code run in an interpreter.

**Dynamic subagents** is Deep Agents’ name for that programmatic orchestration: subagents dispatched by code, not by the model, one turn at a time.

That loop doesn’t have to be a literal `for`: it could be a map over a list, a parallel fan-out, or a branching pipeline. What matters is that code fixes the shape, so the model never has to reconstruct it from memory on every turn.

Same subagent primitive, two different scales

small, fixed N (shown in Module 4)  main agent         sub 1 sub 2 sub 3 sub 4 …all 4, dispatched in one step…  the model enumerates the 4 items itself; 4 is easy to hold in context

large / open-ended N (dynamic subagents)  for item in items: task(item)       sub 1 sub 2 sub N …however many there are, at once…  code enumerates the list; N could be 1,000, and the model never tracks it

The subagent on the right is doing the exact same job as the one on the left; even the fan-out pattern is the same. The difference is *who enumerated the list*. At 4 items, the model could hold that itself. At 1,000, only code reliably can.

This shift guarantees two properties that turn-by-turn delegation cannot:

- **Deterministic coverage at scale.** A model deciding turn by turn whether it’s covered everything can quietly stop at 75 of 500 items and call it done; a `for batch in batches` loop touches every batch.
  - On a long-context benchmark called OOLONG, a plain agent at 128k tokens often gave up outright, reporting it couldn’t compute the result. An interpreter-enabled agent on the same benchmark did dramatically better (numbers under “Recursive language models” below).
- **Reliable complex orchestration.** Orchestration written as code is more reliable than a model reproducing it as a sequence of tool calls. This matters most for fan-out-and-synthesize work, multi-phase pipelines, and conditional branching. A script can branch, run steps in parallel, or run them in order, whatever the task needs, instead of being limited to one round of tool calls per model turn.

---

<a id="the-interpreter-can-call-task-too"></a>


## The interpreter can call `task()` too

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/zAcqMsknYmD.md)

Lesson Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/zAcqMsknYmD.md)

The [code interpreter](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m2/m2.4-interpreter.html) exposes a global `task()` function that bridges straight to the exact same `task` tool a main agent would call directly.

Concretely, in Deep Agents:

- `task` takes a `description` and a `subagent_type`.
- When the interpreter (`CodeInterpreterMiddleware`) has subagents configured, it freezes a `task()` function into its global scope. Calling it from JavaScript inside the interpreter invokes that same underlying tool.
- Each call still runs a fresh, isolated invocation of that subagent: a clean state with no memory of prior runs, executed end to end. Nothing about *what* gets invoked changes based on *who* called `task`, the model directly or a script running in the interpreter.

`task()` is the subagent-side equivalent of [programmatic tool calling](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m2/m2.4-interpreter.html) (PTC): the same idea, applied to subagents instead of ordinary tools.

<a id="dg-ci-dispatch"></a>


<a id="dg-ci-dispatch-stage"></a>


<a id="ci-arrow"></a>
   <a id="ci-arrow-pink"></a>
   <a id="ci-arrow-light"></a>
   <a id="ci-arrow-teal"></a>

task() dispatch, called from inside the interpreter

<a id="dg-ci-dispatch-s0"></a>
  main agent

<a id="dg-ci-dispatch-s1"></a>
  invoke  Code Interpreter

<a id="dg-ci-dispatch-s2"></a>
  task()

task()

task()

Subagent A isolated state

Subagent B isolated state

Subagent C isolated state

<a id="dg-ci-dispatch-s3"></a>

<a id="dg-ci-dispatch-agg"></a>
  aggregate(a, b, c)

<a id="dg-ci-dispatch-zoom"></a>
     function aggregate(a, b, c) { return [a,b,c].flatMap(r=>r.issues); }

<a id="dg-ci-dispatch-s5"></a>
  combined result

```text
<strong id="dg-ci-dispatch-tag">Setup</strong>
<span id="dg-ci-dispatch-cap">A request comes in that reads like an orchestration job. The main agent decides to write code rather than delegate turn by turn.</span>
```

```text
<button class="sd-btn" id="dg-ci-dispatch-prev" disabled title="Previous">&#8592;</button>
<button class="sd-btn" id="dg-ci-dispatch-next" title="Next">&#8594;</button>
```

<a id="dg-ci-dispatch-dots"></a>

Best viewed on a wider screen

```javascript

(function () {
  var steps = [
    { tag: 'Setup', caption: 'A request comes in that reads like an orchestration job. The main agent decides to write code rather than delegate turn by turn.' },
    { tag: 'Invoke', caption: 'The main agent calls the eval tool and hands it a script. From here, the script runs inside the interpreter and is in control.' },
    { tag: 'Dispatch', caption: 'The script calls task() three times, once per item. Each call runs a fresh, isolated invocation of that subagent.' },
    { tag: 'Aggregate', caption: 'Each subagent runs end to end and returns its result to the script, not to the main agent. The script combines them itself, in code.' },
    { tag: 'Zoom in', caption: 'That combine step is just an ordinary function the model wrote, not a fourth subagent call. Code decides how the pieces fit together.\n\nThis example uses the fan-out-and-synthesize pattern; see "Common orchestration patterns" below for more.' },
    { tag: 'Result', caption: 'Only the combined result crosses back out of the interpreter. The main agent sees one clean result, not three separate subagent transcripts.' }
  ];
  var id = 'dg-ci-dispatch';
  var ZOOM_STEP = 4;
  var cumulative = [0, 1, 2, 3].map(function (i) { return document.getElementById(id + '-s' + i); });
  var agg     = document.getElementById(id + '-agg');
  var zoom    = document.getElementById(id + '-zoom');
  var s5      = document.getElementById(id + '-s5');
  var tagEl   = document.getElementById(id + '-tag');
  var capEl   = document.getElementById(id + '-cap');
  var prevBtn = document.getElementById(id + '-prev');
  var nextBtn = document.getElementById(id + '-next');
  var dots    = document.querySelectorAll('#' + id + '-dots .sd-dot');
  var stage   = document.getElementById(id + '-stage');
  if (cumulative.some(function (o) { return !o; }) || !agg || !zoom || !s5 || !stage) return;
  var current = 0;

  function render() {
    cumulative.forEach(function (o, i) { o.classList.toggle('step-hidden', i > current); });
    agg.classList.toggle('step-hidden', current < 3);
    zoom.classList.toggle('step-hidden', current !== ZOOM_STEP);
    s5.classList.toggle('step-hidden', current < 5);

    var dimmed = current === ZOOM_STEP;
    cumulative.forEach(function (o) { o.classList.toggle('step-dim', dimmed); });

    tagEl.textContent = steps[current].tag;
    capEl.textContent = steps[current].caption;
    prevBtn.disabled = current === 0;
    nextBtn.disabled = current === steps.length - 1;
    dots.forEach(function (d, i) { d.classList.toggle('active', i === current); });
  }

  function advance() { if (current < steps.length - 1) { current++; render(); } }
  function retreat() { if (current > 0) { current--; render(); } }

  render();
  prevBtn.addEventListener('click', retreat);
  nextBtn.addEventListener('click', advance);
  dots.forEach(function (d, i) { d.addEventListener('click', function () { current = i; render(); }); });
  stage.addEventListener('click', advance);
  stage.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); advance(); }
    if (e.key === 'ArrowLeft')                   { e.preventDefault(); retreat(); }
  });
  var tx = 0;
  stage.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
  stage.addEventListener('touchend', function (e) {
    var dx = e.changedTouches[0].clientX - tx;
    if (Math.abs(dx) > 40) dx < 0 ? advance() : retreat();
  });
})();

```

**Governance note.** [`interrupt_on`](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m1/m1.8-hitl.html) pauses a tool call for human approval before it runs, but only when the model makes that call directly. A `task()` call made by code inside `eval` skips the check, so an `interrupt_on` gate on the parent agent’s `task` tool won’t catch it.

To approve orchestration before it runs, gate the `eval` tool itself. Gates set in a subagent’s own spec still work, since they run inside that subagent’s own invocation.


---

<a id="setup"></a>


## Setup

The interpreter runtime behind dynamic subagents is currently **beta**, and needs Python 3.11+.

```text
pip install -U "deepagents[quickjs]"
```

```text
import os

from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

agent = create_deep_agent(
    model=model,
    middleware=[CodeInterpreterMiddleware()],
)
```

Dynamic subagent dispatch is **on by default**, since `CodeInterpreterMiddleware(subagents=True)` is the default; disable it with `subagents=False`. It’s triggered by the word **“workflow”** in the prompt:

- **“Workflow”** (a hardcoded trigger word): `CodeInterpreterMiddleware` injects a literal instruction into the system prompt on every model call → if the request uses the word “workflow”, write orchestration code that dispatches subagents with `task()` and assembles their results (instead of delegating one at a time).

`python {4} result = await agent.ainvoke({ "messages": [{ "role": "user", "content": "Run a workflow that reviews every file in src/routes/ and summarizes the top risks." }] })`

For a single, direct delegation, phrase the request plainly instead, to avoid triggering orchestration you didn’t need.

The interpreter runtime behind dynamic subagents is currently **beta**, and needs Node.js 24.15+.

```text
npm install deepagents @langchain/quickjs
```

```text
import { initChatModel } from "langchain";

import { createDeepAgent } from "deepagents";
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";

const model = await initChatModel("openrouter:nvidia/nemotron-3-ultra-550b-a55b:free");

const agent = createDeepAgent({
  model,
  middleware: [createCodeInterpreterMiddleware()],
});
```

Dynamic subagent dispatch is **on by default**, since `createCodeInterpreterMiddleware({ subagents: true })` is the default; disable it with `{ subagents: false }`. It’s triggered by the word **“workflow”** in the prompt:

- **“Workflow”** (a hardcoded trigger word): `createCodeInterpreterMiddleware` injects a literal instruction into the system prompt on every model call → if the request uses the word “workflow”, write orchestration code that dispatches subagents with `task()` and assembles their results (instead of delegating one at a time).

`typescript {4} const result = await agent.invoke({ messages: [{ role: "user", content: "Run a workflow that reviews every file in src/routes/ and summarizes the top risks.", }], });`

For a single, direct delegation, phrase the request plainly instead, to avoid triggering orchestration you didn’t need.

For zero-setup testing, LangChain’s [`dcode`](https://docs.langchain.com/oss/python/deepagents/code/overview) (an open source terminal coding agent built on the Deep Agents SDK) ships with the interpreter pre-enabled:

```text
curl -LsSf https://langch.in/dcode | bash
dcode
```

---

<a id="how-the-model-picks-a-pattern"></a>


## How the model picks a pattern

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/w4fw6n6CPp4.md)

Lesson Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/w4fw6n6CPp4.md)

The dispatch instructions are added to the system prompt on every model call. One of them sets a cue: when a request mentions a “workflow”, the model should write dispatch code instead of delegating one call at a time. This is prompt guidance, so the model usually follows it, though nothing forces it to.

Past that point, the model is writing ordinary code. It might branch by category, fan out in parallel, loop until nothing new turns up, or run an elimination bracket, depending on how it reasons about the shape of the task as it writes the script.

That reasoning tends to settle into a handful of recognizable shapes:

- Mixed-type inputs often lead to a **branch** (e.g., a folder containing both PDFs and spreadsheets, where the script checks each file’s type and routes it to different handling code)
- A pile of uniform items often leads to a **parallel map** (e.g., 60 book files that all need the same scan, dispatched as one call per file)
- An open-ended search often leads to a **loop** (e.g., querying a database repeatedly, stopping only once a query returns no new results)

The six shapes below are common outcomes of that reasoning, not configuration options you set anywhere.

The model picks the shape fresh each time it writes the script, not from a fixed rule, so the same task can occasionally come out differently between runs.

For more consistent results, steer the model directly. Describe the orchestration shape you want in the system prompt, or put a worked orchestration example in a [skill](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m3/m3.2-skills.html) for the model to read before it writes its own.

The model still writes the script itself, but now it works from a pattern you gave it instead of inventing one from scratch.


---

<a id="common-orchestration-patterns"></a>


## Common orchestration patterns

Pattern

Shape

Tends to show up when

Classify and actRoute each item to a specialist by typeMixed inputs need different handling

Good for triaging support tickets, error logs, or user feedback, any batch of items that need different handling depending on their type.

<a id="cta-arrow"></a>

Task

Classifier

bug

feature

question

Agent A bug-fixer

Agent B feature-analyst

 Agent C support-agent

**What you configure:**

```text
subagents = [
    {"name": "bug-fixer", "description": "Fixes reported bugs."},
    {"name": "feature-analyst", "description": "Analyzes feature requests."},
    {"name": "support-agent", "description": "Answers general support questions."},
]
# passed to create_deep_agent(..., subagents=subagents), see Setup above
```

**What you configure:**

```text
const subagents = [
  { name: "bug-fixer", description: "Fixes reported bugs." },
  { name: "feature-analyst", description: "Analyzes feature requests." },
  { name: "support-agent", description: "Answers general support questions." },
];
// passed to createDeepAgent({ ..., subagents }), see Setup above
```

**What the agent writes:**

```text
const SPECIALIST = { bug: "bug-fixer", feature: "feature-analyst", question: "support-agent" };

const handled = await Promise.all(
  tickets.map((ticket) =>
    task({
      description: `Handle this ${ticket.category}:\n${ticket.text}`,
      subagentType: SPECIALIST[ticket.category],
    }),
  ),
);
```


Fan-out and synthesizeSame work across many items in parallel, then combineIndependent units, one combined report

Good for code review across a directory, analyzing a batch of documents, or running the same check across many services.

<a id="fos-arrow"></a>
   <a id="fos-arrow-light"></a>

Task files (glob)

Agent A reviewer

Agent B reviewer

Agent C reviewer

 Result issues

**What you configure:**

```text
subagents = [
    {"name": "reviewer", "description": "Reviews one file for authentication issues."},
]
# passed to create_deep_agent(..., subagents=subagents), see Setup above
```

**What you configure:**

```text
const subagents = [
  { name: "reviewer", description: "Reviews one file for authentication issues." },
];
// passed to createDeepAgent({ ..., subagents }), see Setup above
```

**What the agent writes:**

```text
const files = (await tools.glob({ pattern: "src/routes/**/*.ts" })).split("\n").filter(Boolean);

const reviews = await Promise.all(
  files.map((file) =>
    task({
      description: `Review ${file} for authentication issues. Cite line numbers.`,
      subagentType: "reviewer",
      responseSchema: issuesSchema, // -> { issues: [{ file, line, severity }] }
    }),
  ),
);

const issues = reviews.flatMap((r) => r.issues);
```


Adversarial verificationFind, then independently verify before keepingFalse positives are costly

Good for security audits or compliance checks, anywhere a false positive is costly enough to be worth a second, independent pass.

<a id="adv-arrow"></a>
   <a id="adv-arrow-light"></a>

Task

Agent A reviewer: audit

Findings

Agent B verifier

Agent C verifier

Agent D verifier

confirmed

confirmed

✕ dropped

 Result confirmed

**What you configure:**

```text
subagents = [
    {"name": "reviewer", "description": "Audits code and reports findings."},
    {"name": "verifier", "description": "Independently confirms or refutes one finding."},
]
# passed to create_deep_agent(..., subagents=subagents), see Setup above
```

**What you configure:**

```text
const subagents = [
  { name: "reviewer", description: "Audits code and reports findings." },
  { name: "verifier", description: "Independently confirms or refutes one finding." },
];
// passed to createDeepAgent({ ..., subagents }), see Setup above
```

**What the agent writes:**

```text
const { findings } = await task({
  description: "Audit the payments module for vulnerabilities.",
  subagentType: "reviewer",
  responseSchema: findingsSchema, // -> { findings: [{ id, file, line, description }] }
});

const verdicts = await Promise.all(
  findings.map((f) =>
    task({
      description: `Verify ${f.file}:${f.line} (${f.description}). Confirm or refute.`,
      subagentType: "verifier",
      responseSchema: verdictSchema, // -> { confirmed: boolean }
    }),
  ),
);

const confirmed = findings.filter((_, i) => verdicts[i]?.confirmed);
```


Generate and filterProduce several options, score, keep the bestExploring options beats one-shot

Good for exploring an idea space where the first attempt might not be the best one, drafting titles, proposing fixes, or brainstorming approaches, when it’s cheaper to generate a few options and score them than to get one right on the first try.

<a id="gaf-arrow"></a>
   <a id="gaf-arrow-light"></a>

Task

Generator A candidate

Generator B candidate

Generator C candidate

Scorer score + filter

 Result best of N

**What you configure:**

```text
subagents = [
    {"name": "generator", "description": "Drafts one candidate option."},
    {"name": "scorer", "description": "Scores a candidate from 0-10."},
]
# passed to create_deep_agent(..., subagents=subagents), see Setup above
```

**What you configure:**

```text
const subagents = [
  { name: "generator", description: "Drafts one candidate option." },
  { name: "scorer", description: "Scores a candidate from 0-10." },
];
// passed to createDeepAgent({ ..., subagents }), see Setup above
```

**What the agent writes:**

```text
const candidates = await Promise.all(
  Array.from({ length: 5 }, (_, i) =>
    task({
      description: `Draft a title for this post. Attempt ${i + 1}, be distinct from a typical headline.`,
      subagentType: "generator",
    }),
  ),
);

const scored = await Promise.all(
  candidates.map((title) =>
    task({
      description: `Score this title from 0-10 for clarity and click-worthiness:\n${title}`,
      subagentType: "scorer",
      responseSchema: scoreSchema, // -> { score: number }
    }),
  ),
);

const best = candidates.filter((_, i) => scored[i].score >= 8);
```


TournamentHead-to-head judging, winners advanceSubjective or relative criteria

Good for picking the best of several candidates when you can’t score them independently, only compare two at a time, style rewrites, competing implementations, or anywhere the criteria are subjective.

<a id="trn-arrow"></a>

Agent A writer

Agent B writer

Agent C writer

Agent D writer

Judge round 1

Judge round 1

Winner

Winner

Judge final round

Result best rewrite

**What you configure:**

```text
subagents = [
    {"name": "writer", "description": "Writes one candidate rewrite."},
    {"name": "judge", "description": "Compares two candidates and picks the better one."},
]
# passed to create_deep_agent(..., subagents=subagents), see Setup above
```

**What you configure:**

```text
const subagents = [
  { name: "writer", description: "Writes one candidate rewrite." },
  { name: "judge", description: "Compares two candidates and picks the better one." },
];
// passed to createDeepAgent({ ..., subagents }), see Setup above
```

**What the agent writes:**

```text
const rewrites = await Promise.all(
  Array.from({ length: 4 }, (_, i) =>
    task({
      description: `Rewrite processOrder for clarity. Attempt ${i + 1}.`,
      subagentType: "writer",
    }),
  ),
);

let bracket = rewrites;
while (bracket.length > 1) {
  const next = [];
  for (let i = 0; i < bracket.length; i += 2) {
    const { winner } = await task({
      description: `Compare these two rewrites and pick the better one:\n\nA:\n${bracket[i]}\n\nB:\n${bracket[i + 1]}`,
      subagentType: "judge",
      responseSchema: winnerSchema, // -> { winner: "A" | "B" }
    });
    next.push(winner === "A" ? bracket[i] : bracket[i + 1]);
  }
  bracket = next;
}

const best = bracket[0];
```


Loop until doneRepeat passes until one turns up nothing newScope is unknown, you want completeness

Good for open-ended discovery where you don’t know the scope up front: finding every bug in a codebase, every mention of a topic across a wiki, anywhere “keep looking” is a better instruction than “look N times.”

<a id="lud-arrow"></a>
   <a id="lud-arrow-light"></a>

Task

Finder one pass

new? anything found

yes: loop again

no

 Result all findings

**What you configure:**

```text
subagents = [
    {"name": "finder", "description": "Searches for findings not already collected."},
]
# passed to create_deep_agent(..., subagents=subagents), see Setup above
```

**What you configure:**

```text
const subagents = [
  { name: "finder", description: "Searches for findings not already collected." },
];
// passed to createDeepAgent({ ..., subagents }), see Setup above
```

**What the agent writes:**

```text
const seen = new Set();
let dry = 0;

while (dry < 2) {
  const { findings } = await task({
    description: "Search the codebase for unhandled promise rejections not yet in the findings list.",
    subagentType: "finder",
    responseSchema: findingsSchema, // -> { findings: [{ file, line }] }
  });

  const fresh = findings.filter((f) => !seen.has(`${f.file}:${f.line}`));
  if (fresh.length === 0) {
    dry++;
    continue;
  }
  dry = 0;
  fresh.forEach((f) => seen.add(`${f.file}:${f.line}`));
}
```


---

<a id="recursive-language-models-rlms"></a>


## Recursive language models (RLMs)

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/cWHoC1vEmlB.md)

Lesson Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/cWHoC1vEmlB.md)

Deep Agents implements a documented technique called the **recursive language model (RLM)**, introduced by Alex Zhang, Tim Kraska, and Omar Khattab at MIT CSAIL ([paper](../../../../../readings/arxiv-2512-24601-full-text.md)).

> **Core insight:** instead of a model treating a long context as one monolithic input, split it into pieces, call each piece, and combine the results, recursing on any piece still too big to handle directly.

<a id="dg-rlm-recurse"></a>


<a id="dg-rlm-recurse-stage"></a>


<a id="rlm-arrow"></a>
   <a id="rlm-arrow-light"></a>

Split, call, combine the RLM core loop

context

call A (half 1)

call B (half 2)

<a id="dg-rlm-recurse-lineA2C"></a>

<a id="dg-rlm-recurse-callC"></a>
   call C: combine(A, B)

<a id="dg-rlm-recurse-s0"></a>
   call A (still large)    A1  A2

<a id="dg-rlm-recurse-s1"></a>
    call A3: combine(A1, A2)

<a id="dg-rlm-recurse-s2"></a>

```text
<strong id="dg-rlm-recurse-tag">Split, call</strong>
<span id="dg-rlm-recurse-cap">Split the context, call each half.</span>
```

```text
<button class="sd-btn" id="dg-rlm-recurse-prev" disabled title="Previous">&#8592;</button>
<button class="sd-btn" id="dg-rlm-recurse-next" title="Next">&#8594;</button>
```

<a id="dg-rlm-recurse-dots"></a>

Best viewed on a wider screen

```javascript

(function () {
  var steps = [
    { tag: 'Split, call', caption: 'Split the context, call each half.' },
    { tag: 'Combine in a third call', caption: 'Both results feed into a third call, call C, which combines them.' },
    { tag: 'Recursing on a piece', caption: 'If a half is still too big to handle in one call, that call recurses the same way: split again, call, combine, until each piece is small enough. Call C can’t run yet; it’s waiting on A.' },
    { tag: 'A1 and A2 hit the base case', caption: 'A1 and A2 are small enough to answer directly now, so they combine into call A3. Call C is still waiting on that result.' },
    { tag: 'The loop closes', caption: 'Call A3’s result feeds back up into call C. The loop closes: recursion bottoms out; it doesn’t split forever.' }
  ];
  var id = 'dg-rlm-recurse';
  var overlay0 = document.getElementById(id + '-s0');
  var overlay1 = document.getElementById(id + '-s1');
  var overlay2 = document.getElementById(id + '-s2');
  var callC   = document.getElementById(id + '-callC');
  var lineA2C = document.getElementById(id + '-lineA2C');
  var tagEl   = document.getElementById(id + '-tag');
  var capEl   = document.getElementById(id + '-cap');
  var prevBtn = document.getElementById(id + '-prev');
  var nextBtn = document.getElementById(id + '-next');
  var dots    = document.querySelectorAll('#' + id + '-dots .sd-dot');
  var stage   = document.getElementById(id + '-stage');
  if (!overlay0 || !overlay1 || !overlay2 || !stage) return;
  var current = 0;

  function render() {
    overlay0.classList.toggle('step-hidden', current < 2);
    overlay1.classList.toggle('step-hidden', current < 3);
    overlay2.classList.toggle('step-hidden', current < 4);
    if (callC) {
      callC.style.opacity = (current === 1 || current === 4) ? '1' : '0';
      callC.querySelector('rect').setAttribute('stroke-width', current === 4 ? '2.5' : '1.5');
    }
    if (lineA2C) {
      lineA2C.style.opacity = current === 1 ? '1' : '0';
    }
    tagEl.textContent = steps[current].tag;
    capEl.textContent = steps[current].caption;
    prevBtn.disabled = current === 0;
    nextBtn.disabled = current === steps.length - 1;
    dots.forEach(function (d, i) { d.classList.toggle('active', i === current); });
  }

  function advance() { if (current < steps.length - 1) { current++; render(); } }
  function retreat() { if (current > 0) { current--; render(); } }

  render();
  prevBtn.addEventListener('click', retreat);
  nextBtn.addEventListener('click', advance);
  dots.forEach(function (d, i) { d.addEventListener('click', function () { current = i; render(); }); });
  stage.addEventListener('click', advance);
  stage.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); advance(); }
    if (e.key === 'ArrowLeft')                    { e.preventDefault(); retreat(); }
  });
})();

```

Deep Agents’ dynamic subagents use that same divide-and-conquer technique, but dispatch full agents rather than recursing on the same model call. The LangChain team’s more precise term for that is **recursive agents (RA)**; “RLM” is the popular shorthand you’ll see used for the pattern generally.

The paper reports RLMs handling inputs “up to two orders of magnitude beyond a model’s context window,” with median gains on GPT-5 ranging from 13% (vs. Claude Code) to 130% (vs. CodeAct with sub-calls) across four long-context tasks.

Our own testing

The OOLONG benchmark (long-context reasoning and aggregation) is the same shape of test the paper runs, and running it ourselves against the interpreter-enabled agent from this lesson agrees with the paper’s direction, at more than one context length:

| Context length | Without interpreter | With interpreter |
| --- | --- | --- |
| 64k tokens | 0.58 | 0.67 |
| 128k tokens | 0.44 | 0.79 |

Same caveat as the paper’s own framing: an untuned smoke test, not a finished benchmark, but the gap agrees with the direction the paper reports. ([source](../../../../../readings/www-langchain-com-blog-how-to-use-rlms-in-deep-agents-8688a4c8.md))


---

<a id="when-to-use-dynamic-subagents"></a>


## When to use dynamic subagents

<a id="versus-a-plain-subagent-team"></a>


### *(versus a plain subagent team)*

**Reach for dynamic subagents when:**

- The number of units of work is large or only known at runtime (pages, rows, files, transcripts)
- You need a **guarantee** that every unit gets covered, not a best-effort pass
- The orchestration itself is non-trivial: branching, parallel fan-out, or a pipeline shape the model would otherwise have to reconstruct every turn

**Stick with an ordinary subagent team when:**

- There’s a small, fixed number of specialized roles (a researcher per genre, a reviewer, an analyst)
- You’re delegating *by role*, not fanning out over a large, uniform collection of items


---

<a id="recap"></a>


## Recap

- **Dynamic subagents** means subagents dispatched from a script running in a **[code interpreter](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m2/m2.4-interpreter.html)**, instead of the model calling `task` turn by turn.
- The interpreter’s `task()` calls the same `task` tool the main agent uses directly. Every dispatch is still a full agent with its own tools and state, whether the model or a script starts it.
- The word **“workflow”** in a prompt is the cue for code-based dispatch. The injected instructions tell the model to write `task()` code when a request mentions a workflow. The orchestration *shape* it writes comes from how the model reasons about the task.
- What you get is **deterministic coverage** and **reliable complex orchestration**, both hard to get from a model deciding turn by turn.
- These patterns implement a documented technique, the **recursive language model (RLM)**: split a long context into pieces, call each, combine, recurse on anything still too big. LangChain’s more precise term for the Deep Agents version is **recursive agents (RA)**.

---

<a id="references"></a>


## References

**Paper:**

- [Recursive Language Models (Zhang, Kraska, Khattab)](../../../../../readings/arxiv-2512-24601-full-text.md)

**Blog:**

- [Introducing Dynamic Subagents in Deep Agents](../../../../../readings/www-langchain-com-blog-introducing-dynamic-subagents-in-deep-agents-f27164f7.md)
- [How to use RLMs in Deep Agents](../../../../../readings/www-langchain-com-blog-how-to-use-rlms-in-deep-agents-8688a4c8.md)
- [Running subagents in the background](../../../../../readings/www-langchain-com-blog-running-subagents-in-the-background-76f7f127.md)

**Documentation:**

- [Deep Agents overview](../../../../../readings/docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md)
- [Subagents (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-subagents-528266b9.md)
- [Context engineering (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-context-engineering-e0a127e9.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/subagents.py`](../../../../../readings/github-eb4497f658fd.md): the `task` tool and how subagents are built and run
- [`libs/partners/quickjs`](../../../../../readings/github-41b96b4615a9.md): the interpreter whose `task()` function calls the same tool

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/subagents.ts`](../../../../../readings/github-cdd99e43ff67.md): the `task` tool and how subagents are built and run
- [`libs/providers/quickjs`](../../../../../readings/github-fee995f0f2d6.md): the interpreter whose `task()` function calls the same tool

<a id="p-lab"></a>


<a id="lab-the-corrupted-trojan-war-manuscript"></a>


## Lab: The Corrupted Trojan War Manuscript

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/WxjRmqB2NMI.md)

**Inspect your own run in LangSmith.** Notice the main agent splitting the manuscript into 60 books, dispatching `book-scanner` subagents in large batches, and assembling their findings into the final grouped report.

LangSmith Video Walkthrough

[Public video walkthrough](../../../../../videos/Lcb1iPZ0vPi.md)

A mischievous editor spliced 14 anachronistic sentences into a combined, public-domain translation of the Iliad, Odyssey, and Aeneid: 60 books, about 2MB of text and far too large for one context window. Your job is to find every one of them. A couple of examples:

- “Telemachus updated his status to ‘it’s complicated’ before the suitors arrived.”
- “Circe’s swine wore tiny name tags that read ‘Hello, my name is.’”

The corpus (`python/m4/data/epic_corpus.txt`) and the answer key used for self-checking (`epic_corpus_key.json`) are already checked into the repo.

Books are split on normalized `=== EPIC BOOK N ===` headers.

`python/m4/m4_3_manuscript_agent.py` gives the main agent the interpreter (via `CodeInterpreterMiddleware`) and one `book-scanner` subagent. It also gets a `FilesystemBackend` scoped read-only to that one file.

Its system prompt tells it to write a workflow: read the manuscript, split it into its 60 books, and dispatch one `book-scanner` call per book. The corpus itself never enters the main model’s context. Only each scanner’s short list of findings does.

**Default to a cheaper model (e.g. haiku, nemotron)** because we’re calling a lot of subagents and this is more expensive than a simple agent loop. With Sonnet as the main agent’s model, a full run is roughly $2-3.

**1. Sync your environment**, from the repo’s `python/` directory:

```text
uv sync
```

**2. Run the lab:**

```text
uv run python m4/m4.3_run_manuscript.py
```

**This takes 5-10 minutes to run.** It’s dispatching 60 real subagent calls, one per book, so don’t worry if it looks like it’s hanging; let it finish.

This dispatches 60 subagent calls, one per book. The task prompt asks the model to send them in two rounds of 30. The agent prints a combined report grouped by book, and the script then checks that report against `epic_corpus_key.json`. The key ships openly alongside the corpus, so treat this self-check as quick feedback while you work through the lab.

**Use the self-check line to judge whether your run succeeded. The total count in the report can run high.** The model sometimes flags a passage that isn’t a seeded corruption at all, just odd phrasing in the real 19th-century translations, so the raw count can come out above 14. As long as the self-check reads 14/14, every seeded corruption was found.

**Example output** (from a real run):

```text
## Anachronism Report — /epic_corpus.txt

All 60 books were scanned in two parallel batches of 30 subagents each.

### ILIAD BOOK 2
> "A vending machine hummed faintly beside the Scaean gates."

### ILIAD BOOK 9
> "Patroclus adjusted his smartwatch before donning the borrowed armor."
> "Achilles paused to check his bronze pager before returning to the battle line."

### ILIAD BOOK 16
> "Somewhere beyond the ships, a food truck sold roasted chestnuts to the Myrmidons."

### ILIAD BOOK 23
> "Hector paused to refresh his podcast feed before facing Achilles."

### ODYSSEY BOOK 1
> "Telemachus updated his status to 'it's complicated' before the suitors arrived."

### ODYSSEY BOOK 5
> "Odysseus checked his phone for a signal before addressing the Cyclops."

### ODYSSEY BOOK 12
> "The sirens' song briefly buffered (because the free version has ads) before resuming its melody."
> "Circe's swine wore tiny name tags that read 'Hello, my name is.'"

### ODYSSEY BOOK 20
> "Penelope scrolled through a catalog of suitors on her tablet."

### AENEID BOOK 2
> "Dido kept a small espresso machine in the corner of her palace."
> "Aeneas glanced at Google Maps of the Mediterranean before setting sail."

### AENEID BOOK 7
> "A traffic light blinked uselessly at the gates of Latium."

### AENEID BOOK 11
> "Turnus paused to check the weather forecast before the final duel."

Summary: 14 anachronistic sentences across 11 books.

Self-check: 14/14 seeded corruptions appear in the report.
```

Above 14?

Occasionally a run flags a couple extra passages that aren’t planted corruptions, just odd-sounding phrasing in the real public-domain translations (e.g. “picnic” in Odyssey Book 11, “station hand” in Book 17). Some variance above 14 is normal.


Below 14?

Every run dispatches one `book-scanner` call per book, all 60, so coverage is guaranteed. A count below 14 just means one of those calls missed its book’s planted sentence, which is an ordinary model recall limit. The book itself was still scanned.

<a id="lab-the-corrupted-trojan-war-manuscript-1"></a>


## Lab: The Corrupted Trojan War Manuscript

**The TypeScript version of this lab was made available on September 10, 2026.** Pull the latest changes from the repo root to access it:

```text
git pull
```

Lab Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/WxjRmqB2NMI.md)

**Inspect your own run in LangSmith.** Notice the main agent splitting the manuscript into 60 books, dispatching `book-scanner` subagents in large batches, and assembling their findings into the final grouped report.

LangSmith Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/Lcb1iPZ0vPi.md)

A mischievous editor spliced 14 anachronistic sentences into a combined, public-domain translation of the Iliad, Odyssey, and Aeneid: 60 books, about 2MB of text and far too large for one context window. Your job is to find every one of them. A couple of examples:

- “Telemachus updated his status to ‘it’s complicated’ before the suitors arrived.”
- “Circe’s swine wore tiny name tags that read ‘Hello, my name is.’”

The corpus (`typescript/m4/data/epic_corpus.txt`) and the answer key used for self-checking (`epic_corpus_key.json`) are already checked into the repo.

Books are split on normalized `=== EPIC BOOK N ===` headers.

`typescript/m4/m4_3_manuscript_agent.ts` gives the main agent the interpreter (via `createCodeInterpreterMiddleware()`) and one `book-scanner` subagent. It also gets a `FilesystemBackend` scoped read-only to that one file.

Its system prompt tells it to write a workflow: read the manuscript, split it into its 60 books, and dispatch one `book-scanner` call per book. The corpus itself never enters the main model’s context. Only each scanner’s short list of findings does.

**Default to a cheaper model (e.g. haiku, nemotron)** because we’re calling a lot of subagents and this is more expensive than a simple agent loop. With Sonnet as the main agent’s model, a full run is roughly $2-3.

**1. Install dependencies**, from the repo’s `typescript/` directory:

```text
pnpm install
```

**2. Run the lab:**

```text
pnpm tsx ./m4/m4.3_run_manuscript.ts
```

**This takes 5-10 minutes to run.** It’s dispatching 60 real subagent calls, one per book, so don’t worry if it looks like it’s hanging; let it finish.

This dispatches 60 subagent calls, one per book. The model decides how to batch them when it writes the workflow. The agent prints a combined report grouped by book, and the script then checks that report against `epic_corpus_key.json`. The key ships openly alongside the corpus, so treat this self-check as quick feedback while you work through the lab.

**Example output** (from a real run):

```text
Every single flagged sentence has been confirmed directly in the file. The AENEID BOOK 12 flagging was a false positive (period-appropriate language). Here is the final compiled report:

---

## 🏛️ Anachronistic Sentences Found in the Manuscript

All 60 books were scanned. **14 corrupted sentences** were found across **11 books**. Each has been verified directly against the source file.

---

### ILIAD BOOK 2 — Line 1167
> *"A vending machine hummed faintly beside the Scaean gates."*

---

### ILIAD BOOK 9 — Lines 4966 & 5254
> *"Patroclus adjusted his smartwatch before donning the borrowed armor."*
> *"Achilles paused to check his bronze pager before returning to the battle line."*

---

### ILIAD BOOK 16 — Line 9726
> *"Somewhere beyond the ships, a food truck sold roasted chestnuts to the Myrmidons."*

---

### ILIAD BOOK 23 — Line 13915
> *"Hector paused to refresh his podcast feed before facing Achilles."*

---

### ODYSSEY BOOK 1 — Line 15778
> *"Telemachus updated his status to 'it's complicated' before the suitors arrived."*

---

### ODYSSEY BOOK 5 — Line 18055
> *"Odysseus checked his phone for a signal before addressing the Cyclops."*

---

### ODYSSEY BOOK 12 — Lines 21640 & 21800
> *"The sirens' song briefly buffered (because the free version has ads) before resuming its melody."*
> *"Circe's swine wore tiny name tags that read 'Hello, my name is.'"*

---

### ODYSSEY BOOK 20 — Line 25986
> *"Penelope scrolled through a catalog of suitors on her tablet."*

---

### AENEID BOOK 2 — Lines 32575 & 32854
> *"Dido kept a small espresso machine in the corner of her palace."*
> *"Aeneas glanced at Google Maps of the Mediterranean before setting sail."*

---

### AENEID BOOK 7 — Line 36577
> *"A traffic light blinked uselessly at the gates of Latium."*

---

### AENEID BOOK 11 — Line 39534
> *"Turnus paused to check the weather forecast before the final duel."*

---

**Summary:** 14 anachronistic sentences confirmed across 11 books (5 in the Iliad, 5 in the Odyssey, 4 in the Aeneid). Every corrupted sentence follows the same pattern: a single injected sentence appended to an otherwise authentic passage, referencing unmistakably modern technology.

Self-check: 14/14 seeded corruptions appear in the report.
```

Above 14?

Occasionally a run flags a couple extra passages that aren’t planted corruptions, just odd-sounding phrasing in the real public-domain translations (e.g. “picnic” in Odyssey Book 11, “station hand” in Book 17). Some variance above 14 is normal.


Below 14?

Every run dispatches one `book-scanner` call per book, all 60, so coverage is guaranteed. A count below 14 just means one of those calls missed its book’s planted sentence, which is an ordinary model recall limit. The book itself was still scanned.

<a id="p-quiz"></a>


## Check your understanding

## Check your understanding

<a id="p-homework"></a>


<a id="write-your-own-dynamic-subagent-workflow"></a>


## Write Your Own Dynamic Subagent Workflow

The lab gave the main agent a 2MB manuscript split into labeled books and had it write a “workflow” that dispatched one `book-scanner` subagent per book, so the full corpus never entered the main model’s own context. This homework asks you to do the same shape of thing on a scenario of your own choosing: a synthetic corpus of your own, split into your own labeled sections, and a subagent that scans each section for something other than anachronisms.

A few starting points, if you want one:

- A *Sherlock Holmes* story, split by chapter, scanned for clues the detective mentions but never actually explains.
- The script of *Bee Movie* or *Shrek*, split by scene, scanned for lines that don’t match the character who supposedly says them.
- Your own corrupted classic, like the lab’s, but seeded with a different kind of error: wrong units, swapped character names, continuity errors between chapters.

Open `python/m4/m4.3_homework.py`.

1. **TODO 1**: write your own corpus, a single string split into at least 5 labeled sections using a consistent header format (like the lab’s `=== EPIC BOOK N ===`).
2. **TODO 2**: write the section-scanner’s system prompt (what should it flag in one section?) and the main agent’s system prompt, telling it to run a workflow that splits your corpus and dispatches one scanner call per section.

<a id="run-it"></a>


### Run it

```text
cd python
uv run ./m4/m4.3_homework.py
```

This uses the code interpreter (`langchain_quickjs`), same as the lab. Make sure you’ve run `uv sync` from `python/` so it’s installed.

Stuck, or want to see the finished shape before you start? `m4.3_homework_filled.py` is a reference copy with every TODO filled in (using a support-ticket log scanned for billing complaints); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** the same scanning workflow, but with a second subagent type that independently verifies each finding before it’s kept, using the “adversarial verification” pattern from the orchestration table above instead of a single fan-out pass.

**Requirements:**

- Add a second subagent, e.g. `finding-verifier`, alongside `section-scanner`, to your own `subagents=[...]` list.
- Write the verifier’s system prompt yourself: it only ever sees one finding at a time (not the whole section) and must independently confirm or refute it.
- Rewrite `MAIN_PROMPT` to describe a two-stage workflow: dispatch one `section-scanner` call per section with a `response_schema` for structured findings, then dispatch one `finding-verifier` call per finding with its own `response_schema`, and report only the confirmed findings.
- Run it, and check the trace: did the model actually dispatch both stages (a `section-scanner` call per section, then a separate `finding-verifier` call per finding), or did it just report the scanner’s findings directly? If it skipped the verification stage, that’s a prompt-engineering problem to solve, not a bug. Sharpen `MAIN_PROMPT` until you see both subagent types get dispatched.

<a id="write-your-own-dynamic-subagent-workflow-1"></a>


## Write Your Own Dynamic Subagent Workflow

**The TypeScript version of this homework assignment was made available on September 10, 2026.** Pull the latest changes from the repo root to access it:

```text
git pull
```

The lab gave the main agent a 2MB manuscript split into labeled books and had it write a “workflow” that dispatched one `book-scanner` subagent per book, so the full corpus never entered the main model’s own context. This homework asks you to do the same shape of thing on a scenario of your own choosing: a synthetic corpus of your own, split into your own labeled sections, and a subagent that scans each section for something other than anachronisms.

A few starting points, if you want one:

- A *Sherlock Holmes* story, split by chapter, scanned for clues the detective mentions but never actually explains.
- The script of *Bee Movie* or *Shrek*, split by scene, scanned for lines that don’t match the character who supposedly says them.
- Your own corrupted classic, like the lab’s, but seeded with a different kind of error: wrong units, swapped character names, continuity errors between chapters.

Open `typescript/m4/m4.3_homework.ts`.

1. **TODO 1**: write your own corpus, a single string split into at least 5 labeled sections using a consistent header format (like the lab’s `=== EPIC BOOK N ===`).
2. **TODO 2**: write the section-scanner’s system prompt (what should it flag in one section?) and the main agent’s system prompt, telling it to run a workflow that splits your corpus and dispatches one scanner call per section.

<a id="run-it-1"></a>


### Run it

```text
cd typescript
pnpm tsx ./m4/m4.3_homework.ts
```

This uses the code interpreter (`@langchain/quickjs`), same as the lab. Make sure you’ve run `pnpm install` from `typescript/` so it’s installed.

Stuck, or want to see the finished shape before you start? `m4.3_homework_filled.ts` is a reference copy with every TODO filled in (using a support-ticket log scanned for billing complaints); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** the same scanning workflow, but with a second subagent type that independently verifies each finding before it’s kept, using the “adversarial verification” pattern from the orchestration table above instead of a single fan-out pass.

**Requirements:**

- Add a second subagent, e.g. `finding-verifier`, alongside `section-scanner`, to your own `subagents: [...]` list.
- Write the verifier’s system prompt yourself: it only ever sees one finding at a time (not the whole section) and must independently confirm or refute it.
- Rewrite `mainPrompt` to describe a two-stage workflow: dispatch one `section-scanner` call per section with a `responseSchema` for structured findings, then dispatch one `finding-verifier` call per finding with its own `responseSchema`, and report only the confirmed findings.
- Run it, and check the trace: did the model actually dispatch both stages (a `section-scanner` call per section, then a separate `finding-verifier` call per finding), or did it just report the scanner’s findings directly? If it skipped the verification stage, that’s a prompt-engineering problem to solve, not a bug. Sharpen `mainPrompt` until you see both subagent types get dispatched.

```javascript

(function () {
  var tabs = document.querySelectorAll('.lt-tab');
  function show(p) {
    tabs.forEach(function (t) {
      var on = t.getAttribute('data-p') === p;
      t.classList.toggle('active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    document.querySelectorAll('.lt-panel').forEach(function (panel) {
      panel.classList.toggle('active', panel.id === 'p-' + p);
    });
  }
  tabs.forEach(function (t) {
    t.addEventListener('click', function () { show(t.getAttribute('data-p')); });
  });
})();

```
