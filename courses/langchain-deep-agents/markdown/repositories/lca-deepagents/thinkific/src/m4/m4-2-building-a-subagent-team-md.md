# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m4/m4.2-building-a-subagent-team.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m4/m4.2-building-a-subagent-team.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m4/m4.2-building-a-subagent-team.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m4.2-building-a-subagent-team.md)

Python TypeScript

<a id="building-a-subagent-team"></a>


# Building a Subagent Team

```text
<button class="lt-tab active" data-p="sub" role="tab" aria-selected="true">Subagent Team</button>
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

<a id="p-sub"></a>


Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/tb4KN6yzwik.md)

In the previous lesson you learned about **delegation**, splitting a big job into pieces, handing each to a subagent, and stitching the results back together. In this lesson you’ll build it: an **editorial agent** that puts out a weekly music newsletter for an online distributor.

![An editor robot labeled 'main agent · editor, Sonnet 5.5' fans out to four subagent robots labeled Rock, Latin, Metal, and Alternative & Punk. A 'task' arrow points down and a 'segment' arrow points back up. Each researcher has an assigned /research/<genre>/ file folder; the editor assembles a newsletter.html file.](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m4/images/m4.2-newsletter-fanout.svg)

The main agent is the **editor**. It knows the distributor’s top four genres (**Rock, Latin, Metal, and Alternative & Punk**) and kicks off a research subagent for each one, all at once. Each researcher goes off and looks up what’s new in its genre, then hands back a short, polished segment. The editor collects the four segments, assembles them into one newsletter, and renders it as a styled HTML page.

This lab is a hands-on tour of the subagent model. You’ll see:

- how a subagent gets its task
- what it inherits from the main agent, and what it overrides
- how it keeps messy research out of the editor’s context
- how a state-backed agent filesystem hands a finished file back to your code

**The flow is:**

1. The user asks for this week’s newsletter
2. The editor calls the `task` tool once per genre
3. Each researcher searches the web, writes raw notes to `/research/<genre>/sources.md`, and returns one polished segment
4. The editor assembles the returned segments into Markdown
5. The editor calls `markdown_to_html`
6. The editor writes `/output/newsletter.html`

---

<a id="one-subagent-type-four-assignments"></a>


## One subagent type, four assignments

Notice there’s only **one kind** of researcher. We don’t write a separate Rock subagent and a separate Metal subagent, because they’d all do the same thing. Instead we define a single **`genre-researcher`** subagent type and the editor delegates to it four times, once per genre. The genre is just the task it’s handed.

A subagent is defined as a plain dictionary. Here’s the research subagent, with each field’s anatomy called out below.

A subagent is defined as a plain object. Here’s the research subagent, with each field’s anatomy called out below.

![Anatomy of a subagent. A code panel shows the genre_researcher dictionary with six fields called out: name (the handle the main agent calls), description (how the main agent chooses it), system_prompt (its own brain, never inherited), tools (override, replaces the inherited set (Tavily search only)), model (override, the cheaper Haiku), and permissions (override, scoped write access to /research/**).](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m4/images/m4.2-subagent-anatomy.svg)

![Anatomy of a subagent. A code panel shows the genreResearcher object with six fields called out: name (the handle the main agent calls), description (how the main agent chooses it), systemPrompt (its own brain, never inherited), tools (override, replaces the inherited set (Tavily search only)), model (override, the cheaper Haiku), and permissions (override, scoped write access to /research/**).](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m4/images/m4.2-subagent-anatomy-typescript.svg)

```text
# python/m4/m4_2_newsletter_agent.py
GENRE_PROMPT = """You are a music journalist researching one genre for an
online music distributor's weekly newsletter.

You will be given a single genre and an assigned research folder to work in.

How to work:
1. Use internet_search to find recent, noteworthy developments in that genre.
   Run a few searches.
2. Save the COMPLETE, verbatim output of ALL your searches to a single file:
   write_file("/research/<genre>/sources.md", ...). Paste it exactly as the
   tool returned it - do NOT summarize or trim. This raw archive stays here so
   it never clutters the editor's context.
3. Only then, from what you found, write one tight newsletter segment.

Return ONLY the finished segment as your reply:
- A markdown section: a "## <Genre>" heading followed by ~120-180 words.
- Lively but factual newsletter tone; name specific artists and releases.
- Do NOT paste raw search results into your reply: those live in your files."""

genre_researcher = {
    "name": "genre-researcher",
    "description": (
        "Research one music genre and write a short newsletter segment about "
        "what's new in it. Delegate one genre per call."
    ),
    "system_prompt": GENRE_PROMPT,         # its own brain - never inherited
    "tools": [internet_search],            # override - replaces the inherited set
    "model": model,                        # override - the cheaper Haiku 4.5
    "permissions": research_permissions,   # override - scoped write access
}
```

Setting `tools=[internet_search]` replaces the researcher’s inherited custom tools with the `internet_search` tool. Its built-in filesystem tools, such as `write_file` and `read_file`, stay because the harness always provides them, which is how the researcher can still save its notes. The diagram leaves that detail out.

To limit which filesystem tools a subagent gets, add a `FilesystemMiddleware(tools=[...])` instance to that subagent’s own `middleware` list. It replaces the default one for that subagent.

```text
// typescript/m4/m4_2_newsletter_agent.ts
const GENRE_PROMPT = context`
  You are a music journalist researching one genre for an
  online music distributor's weekly newsletter.

  You will be given a single genre and an assigned research folder to work in.

  How to work:
  1. Use internet_search to find recent, noteworthy developments in that genre.
     Run a few searches.
  2. Save the COMPLETE, verbatim output of ALL your searches to a single file:
     write_file("/research/<genre>/sources.md", ...). Paste it exactly as the
     tool returned it - do NOT summarize or trim. This raw archive stays here so
     it never clutters the editor's context.
  3. Only then, from what you found, write one tight newsletter segment.

  Return ONLY the finished segment as your reply:
  - A markdown section: a "## <Genre>" heading followed by ~120-180 words.
  - Lively but factual newsletter tone; name specific artists and releases.
  - Do NOT paste raw search results into your reply: those live in your files.`;

const genreResearcher: SubAgent = {
  name: "genre-researcher",
  description: context`
    Research one music genre and write a short newsletter segment about
    what's new in it. Delegate one genre per call.`,
  systemPrompt: GENRE_PROMPT,        // its own brain - never inherited
  tools: [internetSearch],          // override - replaces the inherited set
  model,                            // override - the cheaper Haiku 4.5
  permissions: researchPermissions, // override - scoped write access
};
```

Setting `tools: [internetSearch]` replaces the researcher’s inherited custom tools with the `internetSearch` tool. Its built-in filesystem tools, such as `write_file` and `read_file`, stay because the harness always provides them, which is how the researcher can still save its notes. The diagram leaves that detail out.

To limit which filesystem tools a subagent gets, add a `createFilesystemMiddleware({ tools: [...] })` instance to that subagent’s own `middleware` array. It replaces the default one for that subagent.

---

<a id="research-scratch-files"></a>


## Research scratch files

Each researcher gets its own scratch folder named after its genre: `/research/Rock/`, `/research/Metal/`, and so on. That folder is only a convention. The editor names it in each task prompt, and all the researchers share one filesystem. The permissions are drawn more broadly: researchers can write anywhere under `/research/**` (and nowhere else), while the editor can read that area but can’t write to it.

We set that up with filesystem **permissions**:

```text
# python/m4/m4_2_newsletter_agent.py
# Researchers may write under /research/** and are denied writes elsewhere.
research_permissions = [
    FilesystemPermission(operations=["read", "write"], paths=["/research/**"], mode="allow"),
    FilesystemPermission(operations=["write"], paths=["/**"], mode="deny"),
]

# The editor may read the research area, but must not write into it.
editor_permissions = [
    FilesystemPermission(operations=["write"], paths=["/research/**"], mode="deny"),
]
```

```text
// typescript/m4/m4_2_newsletter_agent.ts
// Researchers may write under /research/** and are denied writes elsewhere.
const researchPermissions: FilesystemPermission[] = [
  { operations: ["read", "write"], paths: ["/research/**"], mode: "allow" },
  { operations: ["write"], paths: ["/**"], mode: "deny" },
];

// The editor may read the research area, but must not write into it.
const editorPermissions: FilesystemPermission[] = [
  { operations: ["write"], paths: ["/research/**"], mode: "deny" },
];
```

Permissions are first-match-wins, so a researcher’s specific `allow` for writes under `/research/**` beats the broad write `deny`. The editor’s read-only access is enforced by denying writes to `/research/**`.

---

<a id="the-editor"></a>


## The editor

The editor is a normal Deep Agent. It gets the stronger model, a single tool (`markdown_to_html`, which the researchers don’t have), and the `genre-researcher` subagent.

```text
# python/m4/m4_2_newsletter_agent.py
EDITOR_PROMPT = f"""You are the editor of an online music distributor's weekly
newsletter. This week you are featuring the distributor's top genres:
{", ".join(TOP_GENRES)}.

Your job:
1. For EACH genre, delegate to the genre-researcher subagent using the task
   tool - fire them off in parallel. Tell each one which genre to cover and
   which assigned folder to use (/research/<genre>/), and ask for one segment.
2. Collect the four returned segments. Do NOT research genres yourself.
3. Assemble them into one Markdown newsletter: a top-level "# This Week in
   Music" title, a one-sentence intro, then the four "## <Genre>" sections.
4. Call markdown_to_html on the assembled Markdown, then write_file the
   returned HTML to /output/newsletter.html."""

# The editor gets the stronger shared model; the researcher overrode to the
# cheaper `model` (Haiku 4.5) above. Both are defined in python/models.py.
agent = create_deep_agent(
    model=strong_model,
    tools=[markdown_to_html],
    system_prompt=EDITOR_PROMPT,
    subagents=[genre_researcher],
    permissions=editor_permissions,
)
```

Because a subagent is invoked like a tool, the editor can call the `task` tool four times in a single step, with calls shaped like `task(subagent_type="genre-researcher", description="Research Rock using /research/Rock/ ...")`. All four researchers run **in parallel**, and the editor blocks until the slowest one returns. These are **synchronous** subagents, from the previous lesson.

The `markdown_to_html` tool is pure Python. It drops the assembled Markdown into a fixed, styled HTML template and returns the page as a string:

```text
# python/m4/m4_2_newsletter_agent.py
@tool
def markdown_to_html(markdown_text: str, title: str = "This Week in Music") -> str:
    """Convert a Markdown newsletter into a complete, styled HTML page.
    Returns the full HTML document as a string."""
    body = md.markdown(markdown_text, extensions=["tables", "fenced_code"])
    # Good practice: the newsletter text is derived from untrusted web search,
    # so allowlist-sanitize it (strips <script>, onerror=, etc.) before it goes
    # into the page. We clean only the body; the template itself is trusted.
    body = nh3.clean(body)
    return _HTML_TEMPLATE.format(title=title, body=body)
```

```text
// typescript/m4/m4_2_newsletter_agent.ts
const EDITOR_PROMPT = context`
  You are the editor of an online music distributor's weekly
  newsletter. This week you are featuring the distributor's top genres:
  ${TOP_GENRES.join(", ")}.

  Your job:
  1. For EACH genre, delegate to the genre-researcher subagent using the task
     tool - fire them off in parallel. Tell each one which genre to cover and
     which assigned folder to use (/research/<genre>/), and ask for one segment.
  2. Collect the four returned segments. Do NOT research genres yourself.
  3. Assemble them into one Markdown newsletter: a top-level "# This Week in
     Music" title, a one-sentence intro, then the four "## <Genre>" sections.
  4. Call markdown_to_html on the assembled Markdown, then write_file the
     returned HTML to /output/newsletter.html.`;

// The editor gets the stronger shared model; the researcher overrode to the
// cheaper `model` (Haiku 4.5) above. Both are defined in typescript/models.ts.
export const agent = createDeepAgent({
  model: strongModel,
  tools: [markdownToHtml],
  systemPrompt: EDITOR_PROMPT,
  subagents: [genreResearcher],
  permissions: editorPermissions,
});
```

Because a subagent is invoked like a tool, the editor can call the `task` tool four times in a single step, with calls shaped like `task({ subagent_type: "genre-researcher", description: "Research Rock using /research/Rock/ ..." })`. All four researchers run **in parallel**, and the editor blocks until the slowest one returns. These are **synchronous** subagents, from the previous lesson.

The `markdown_to_html` tool is a plain TypeScript function. It drops the assembled Markdown into a fixed, styled HTML template and returns the page as a string:

```text
// typescript/m4/m4_2_newsletter_agent.ts
const markdownToHtml = tool(
  async ({ markdownText, title }: { markdownText: string; title: string }) => {
    let body = (await marked.parse(markdownText)) as string;
    // Good practice: the newsletter text is derived from untrusted web search,
    // so allowlist-sanitize it (strips <script>, onerror=, etc.) before it goes
    // into the page. We clean only the body; the template itself is trusted.
    body = sanitizeHtml(body);
    return HTML_TEMPLATE(title, body);
  },
  {
    name: "markdown_to_html",
    description: context`
      Convert a Markdown newsletter into a complete, styled HTML page.
      Returns the full HTML document as a string.`,
    schema: z.object({
      markdownText: z.string(),
      title: z.string().default("This Week in Music"),
    }),
  }
);
```

---

> To run the newsletter agent, select the **Lab** tab at the top of this lesson.

---

<a id="a-note-on-the-general-purpose-subagent"></a>


## A note on the general-purpose subagent

You defined one subagent type. But every Deep Agent also ships with a built-in **`general-purpose`** subagent for free. It has the *same tools and model as the main agent* and a generic prompt. It’s the agent’s escape hatch: when a task doesn’t match any subagent you defined, the main agent can still delegate it to `general-purpose` to get context isolation, rather than doing the work inline.

It’s the one subagent that also inherits the main agent’s **skills**. You won’t call it explicitly in this lab, but it’s worth knowing it’s always there.

![LangChain](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m4/images/langchain-symbol.png)

**LangChain Blog**

[How Rippling went AI-native with Deep Agents](https://www.langchain.com/blog/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith)

Rippling’s assistant uses a supervisor coordinating 5-7 specialized subagents (read, RAG, and action types) across HR, payroll, IT, and finance. Each query triggers dynamic skill injection, scoped to only the relevant domain, cutting context size by 100-500x.

---

<a id="recap"></a>


## Recap

In this lesson you built a working subagent team:

- **One subagent type, many assignments.** A single `genre-researcher` is delegated to once per genre. The genre is just the task it’s handed.
- **Subagents inherit by default and override by exception.** Setting `tools`, `model`, or `permissions` **replaces** the inherited value rather than extending it. `system_prompt``systemPrompt` is the one field you must always provide.
- **Task in, result out.** A subagent receives one task message and returns one result message. The editor never sees a researcher’s conversation, only its final segment.
- **Private files for raw work.** Each researcher stashes its raw search results in its own `/research/<genre>/` folder and reads them back while drafting; **permissions** scope a researcher to its scratch space and give the editor read-only access there.
- **State-backed by default.** On the default `StateBackend`, the agent writes to agent state, not your disk. Trusted host code reads the finished file out of `result[“files”]``result.files`.
- Every agent also has a built-in **`general-purpose`** subagent as a fallback.

---

<a id="references"></a>


## References

**Documentation:**

- [Subagents (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-subagents-528266b9.md)
- [Context engineering (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-context-engineering-e0a127e9.md)
- [Filesystem & backends (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-backends-9df47d8f.md)
- [Tavily Search API](../../../../../readings/docs-tavily-com-8d145a9c.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/subagents.py`](../../../../../readings/github-eb4497f658fd.md): the `task` tool and how subagents are built and run

**Documentation:**

- [Subagents (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-subagents-2a904d1e.md)
- [Context engineering (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-context-engineering-de9e92ff.md)
- [Filesystem & backends (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-backends-5e451258.md)
- [Tavily Search API](../../../../../readings/docs-tavily-com-8d145a9c.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/subagents.ts`](../../../../../readings/github-cdd99e43ff67.md): the `task` tool and how subagents are built and run

**Blog:**

- [Running subagents in the background](../../../../../readings/www-langchain-com-blog-running-subagents-in-the-background-76f7f127.md)
- [How to use RLMs in Deep Agents](../../../../../readings/www-langchain-com-blog-how-to-use-rlms-in-deep-agents-8688a4c8.md)

<a id="p-lab"></a>


<a id="lab-newsletter-agent"></a>


## Lab: Newsletter Agent

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/zap33EjlmGc.md)

**Inspect your own run in LangSmith.** Notice the editor launching four researcher subagents in parallel, then assembling their segments into the final newsletter.

LangSmith Video Walkthrough

[Public video walkthrough](../../../../../videos/hzhz5WzjQPC.md)

Before running it, make sure your model API key and `TAVILY_API_KEY` are available in the PythonTypeScript environment. This lab launches four web researchers in parallel, so web results may vary and the run may consume multiple Tavily/API calls.

From the repo root:

```text
cd python
uv run python m4/m4.2_run_newsletter.py
```

From the repo root:

```text
cd typescript
pnpm tsx ./m4/m4.2_run_newsletter.ts
```

Watch the editor fire off four researchers, then assemble their segments. When it finishes, open `python/m4/output/newsletter.html``typescript/m4/output/newsletter.html` in your browser to read this week’s issue.

Everything the agent produced is stored in the default `StateBackend`, so the script mirrors it out of agent state and onto disk under `python/m4/output/``typescript/m4/output/`. The finished newsletter sits alongside each researcher’s raw `/research/<genre>/` archive:

```text
Writing agent files to disk:
  /output/newsletter.html                  ->  newsletter.html                          (6,422 chars)
  /research/Alternative & Punk/sources.md  ->  research/Alternative & Punk/sources.md   (18,867 chars)
  /research/Latin/sources.md               ->  research/Latin/sources.md                (25,353 chars)
  /research/Metal/sources.md               ->  research/Metal/sources.md                (28,213 chars)
  /research/Rock/sources.md                ->  research/Rock/sources.md                 (29,258 chars)
```

Open one of those `sources.md` files and you’ll see the point: tens of kilobytes of raw, link-heavy search results. Only each researcher’s tight ~150-word segment crossed back to the editor. The bulky, untrusted material stays quarantined in the research area, and the editor’s context stays clean.

**Inspect your own run in LangSmith.** Notice the parallel subagent calls and the `write_todos` calls. The `write_todos` tool comes from `TodoListMiddleware``todoListMiddleware`, which is opt-in in current Deep Agents versions. The lab’s editor doesn’t add it, so by default your own trace won’t show `write_todos`. To see it, add the middleware to the editor’s `middleware` list.

**Troubleshooting**

- **`anthropic.APITimeoutError: Request timed out`**: this lab’s four researchers each have to reproduce a large, verbatim search-results dump inside a `write_file` call, and they do it concurrently (that’s a heavier, slower generation than most labs, and it can occasionally outrun the default client timeouts under load).  
    
  Raise the timeouts in `python/models.py`: `init_chat_model(“anthropic:claude-haiku-4-5”, timeout=120, max_retries=2)` and `init_chat_model(“anthropic:claude-sonnet-5-5”, timeout=180, max_retries=2)`, then re-run.

**Troubleshooting**

- **`APITimeoutError: Request timed out`**: this lab’s four researchers each have to reproduce a large, verbatim search-results dump inside a `write_file` call, and they do it concurrently (that’s a heavier, slower generation than most labs, and it can occasionally outrun the default client timeouts under load).  
    
  Raise the timeouts in `typescript/models.ts`: `initChatModel(“anthropic:claude-haiku-4-5”, { timeout: 120_000, maxRetries: 2 })` and `initChatModel(“anthropic:claude-sonnet-5-5”, { timeout: 180_000, maxRetries: 2 })`, then re-run.

**Sample output** (the newsletter produced by the trace above):

[Sample newsletter output](../../../../../lesson-assets/newsletter-sample.md)

<a id="p-homework"></a>


<a id="give-each-subagent-its-own-scoped-scratch-folder"></a>


## Give Each Subagent Its Own Scoped Scratch Folder

The lab’s `genre-researcher` subagents each wrote raw search notes to their own assigned `/research/<genre>/` folder, kept out of the editor’s context by `FilesystemPermission` scoping: researchers could write under `/research/**`, the editor could not.

This homework asks you to build a small team of 2 subagent types for a domain of your choosing (e.g., trip planning, home renovation), each with its own private, permission-scoped folder under `/scratch/<name>/` to stash raw notes in before answering.

Open `python/m4/m4.2_homework.py`. The harness there already wires up the scratch folder, the permissions, and the “save your notes before answering” instruction for you; you only decide who your two subagents are.

1. **TODO 1**: for each of the two entries in `SUBAGENT_SPECS`, fill in `name`, `description` (when the main agent should call it), and `role_prompt` (who this subagent is and what its job is).
2. **TODO 2**: write the main agent’s system prompt, telling it which subagent to call for which part of the job, and a user request that should trigger delegation to both subagents.

<a id="run-it"></a>


### Run it

```text
cd python
uv run ./m4/m4.2_homework.py
```

The script prints a scratch-folder isolation check at the end: it confirms each subagent’s notes file landed only in its own folder, never the other’s.

Stuck, or want to see the finished shape before you start? `m4.2_homework_filled.py` is a reference copy with every TODO filled in (using a fitness-coaching team of a workout planner and a nutrition advisor); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** a two-subagent team with the permission and scratch-folder wiring written by hand, skipping the homework’s `build_subagents`/`scratch_permissions` helper functions, where one subagent also gets its own `model` and a restricted `tools=[...]` list instead of inheriting the main agent’s.

**Requirements:**

- Write your own `create_deep_agent(model=strong_model, system_prompt=..., subagents=[...], permissions=...)` call from scratch, in a new file under `python/m4/`. Don’t import the homework’s `build_subagents`/`scratch_permissions` helpers; write each subagent’s `FilesystemPermission` list yourself, following the same allow-then-deny pattern.
- Give each subagent its own scoped scratch folder under `/scratch/<name>/`, same idea as the homework, but wired by your own code this time.
- On one subagent only, set `model=model` (the cheaper/faster model, distinct from the main agent’s `strong_model`) and `tools=[your_tool]`, restricting it to exactly one tool of your choosing instead of inheriting the main agent’s full toolset.
- Write a system prompt and a user request that triggers delegation to both subagents, then check the trace to confirm the restricted subagent ran on the cheaper model and only ever called its one allowed tool.

**⚠ Troubleshooting:** `FilesystemPermission` rules are evaluated in order, first match wins. If you write a broad deny rule before a subagent’s own scratch-folder allow rule, the deny will match first and silently lock that subagent out of its own scratch path. Always list the narrower allow rule first, then the broader deny.

<a id="give-each-subagent-its-own-scoped-scratch-folder-1"></a>


## Give Each Subagent Its Own Scoped Scratch Folder

The lab’s `genre-researcher` subagents each wrote raw search notes to their own assigned `/research/<genre>/` folder, kept out of the editor’s context by `FilesystemPermission` scoping: researchers could write under `/research/**`, the editor could not.

This homework asks you to build a small team of 2 subagent types for a domain of your choosing (e.g., trip planning, home renovation), each with its own private, permission-scoped folder under `/scratch/<name>/` to stash raw notes in before answering.

Open `typescript/m4/m4.2_homework.ts`. The harness there already wires up the scratch folder, the permissions, and the “save your notes before answering” instruction for you; you only decide who your two subagents are.

1. **TODO 1**: for each of the two entries in `SUBAGENT_SPECS`, fill in `name`, `description` (when the main agent should call it), and `rolePrompt` (who this subagent is and what its job is).
2. **TODO 2**: write the main agent’s system prompt, telling it which subagent to call for which part of the job, and a user request that should trigger delegation to both subagents.

<a id="run-it-1"></a>


### Run it

```text
cd typescript
pnpm tsx ./m4/m4.2_homework.ts
```

The script prints a scratch-folder isolation check at the end: it confirms each subagent’s notes file landed only in its own folder, never the other’s.

Stuck, or want to see the finished shape before you start? `m4.2_homework_filled.ts` is a reference copy with every TODO filled in (using a fitness-coaching team of a workout planner and a nutrition advisor); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** a two-subagent team with the permission and scratch-folder wiring written by hand, skipping the homework’s `buildSubagents`/`scratchPermissions` helper functions, where one subagent also gets its own `model` and a restricted `tools: [...]` list instead of inheriting the main agent’s.

**Requirements:**

- Write your own `createDeepAgent({ model: strongModel, systemPrompt: ..., subagents: [...], permissions: ... })` call from scratch, in a new file under `typescript/m4/`. Don’t import the homework’s `buildSubagents`/`scratchPermissions` helpers; write each subagent’s `FilesystemPermission` list yourself, following the same allow-then-deny pattern.
- Give each subagent its own scoped scratch folder under `/scratch/<name>/`, same idea as the homework, but wired by your own code this time.
- On one subagent only, set `model: model` (the cheaper/faster model, distinct from the main agent’s `strongModel`) and `tools: [yourTool]`, restricting it to exactly one tool of your choosing instead of inheriting the main agent’s full toolset.
- Write a system prompt and a user request that triggers delegation to both subagents, then check the trace to confirm the restricted subagent ran on the cheaper model and only ever called its one allowed tool.

**⚠ Troubleshooting:** `FilesystemPermission` rules are evaluated in order, first match wins. If you write a broad deny rule before a subagent’s own scratch-folder allow rule, the deny will match first and silently lock that subagent out of its own scratch path. Always list the narrower allow rule first, then the broader deny.

<a id="p-quiz"></a>


## Check your understanding

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
