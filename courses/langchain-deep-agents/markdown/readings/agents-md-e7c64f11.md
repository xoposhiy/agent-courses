# Assigned reference: 

[Course index](../../README.md) · [Original source](https://agents.md/) · [Raw file](../../raw/readings/agents-md-e7c64f11.html)

Retrieved: 2026-11-13T16:57:44.786197+00:00

# AGENTS.md

A simple, open format for guiding coding agents,   
used by over [60k open-source projects](https://github.com/search?q=path%3AAGENTS.md+NOT+is%3Afork+NOT+is%3Aarchived&type=code).

Think of AGENTS.md as a **README for agents**: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project.

[Explore Examples](agents-md-e7c64f11.md)[View on GitHub](https://github.com/agentsmd/agents.md)

```
# AGENTS.md


## Setup commands


- Install deps: `pnpm install`


- Start dev server: `pnpm dev`


- Run tests: `pnpm test`


## Code style


- TypeScript strict mode


- Single quotes, no semicolons


- Use functional patterns where possible
```

## Why AGENTS.md?

README.md files are for humans: quick starts, project descriptions, and contribution guidelines.

AGENTS.md complements this by containing the extra, sometimes detailed context coding agents need: build steps, tests, and conventions that might clutter a README or aren’t relevant to human contributors.

We intentionally kept it separate to:

Give agents a clear, predictable place for instructions.

Keep READMEs concise and focused on human contributors.

Provide precise, agent-focused guidance that complements existing README and docs.

Rather than introducing another proprietary file, we chose a name and format that could work for anyone. If you’re building or using coding agents and find this helpful, feel free to adopt it.

## One AGENTS.md works across many agents

Your agent definitions are compatible with a growing ecosystem of AI coding agents and tools:

[Codexfrom OpenAI](https://openai.com/codex/)[Julesfrom Google](https://jules.google)[Factory](https://factory.ai)[Aider](https://aider.chat/docs/usage/conventions.html#always-load-conventions)[goose](https://github.com/block/goose)[opencode](https://opencode.ai/docs/rules/)[Zed](https://zed.dev/docs/ai/rules)[Warp](https://docs.warp.dev/knowledge-and-collaboration/rules#project-scoped-rules-1)[![VS Code logo](../../raw/assets/cb8799efd90c1581.svg)![VS Code logo](../../raw/assets/e36bb1672acb7851.svg)

VS Code](https://code.visualstudio.com/docs/editor/artificial-intelligence)[![Devin logo](../../raw/assets/13c4c27687e7aaf2.svg)![Devin logo](../../raw/assets/bd6099a3e76e8b13.svg)

Devinfrom Cognition](https://devin.ai)[Autopilot & Coded Agentsfrom UiPath](https://uipath.github.io/uipath-python)[Juniefrom JetBrains](https://jetbrains.com/junie)[Codexfrom OpenAI](https://openai.com/codex/)[Julesfrom Google](https://jules.google)[Factory](https://factory.ai)[Aider](https://aider.chat/docs/usage/conventions.html#always-load-conventions)[goose](https://github.com/block/goose)[opencode](https://opencode.ai/docs/rules/)[Zed](https://zed.dev/docs/ai/rules)[Warp](https://docs.warp.dev/knowledge-and-collaboration/rules#project-scoped-rules-1)[![VS Code logo](../../raw/assets/cb8799efd90c1581.svg)![VS Code logo](../../raw/assets/e36bb1672acb7851.svg)

VS Code](https://code.visualstudio.com/docs/editor/artificial-intelligence)[![Devin logo](../../raw/assets/13c4c27687e7aaf2.svg)![Devin logo](../../raw/assets/bd6099a3e76e8b13.svg)

Devinfrom Cognition](https://devin.ai)[Autopilot & Coded Agentsfrom UiPath](https://uipath.github.io/uipath-python)[Juniefrom JetBrains](https://jetbrains.com/junie)

[Amp](https://ampcode.com)[Cursor](https://cursor.com)[RooCode](https://roocode.com)[Gemini CLIfrom Google](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/configuration.md#available-settings-in-settingsjson)[Kilo Code](https://kilocode.ai/)[Phoenix](https://phoenix.new/)[Semgrep](https://semgrep.dev)[Coding agentfrom GitHub Copilot](https://gh.io/coding-agent-docs)[![Ona logo](../../raw/assets/bba6e5d9612dd2aa.svg)![Ona logo](../../raw/assets/614d0fee63ca71b0.svg)

Ona](https://ona.com)[![Windsurf logo](../../raw/assets/9a567f7ecbfcc806.svg)![Windsurf logo](../../raw/assets/d122528b2c575326.svg)

Windsurffrom Cognition](https://windsurf.com)[Augment Code](https://docs.augmentcode.com/cli/overview)[Amp](https://ampcode.com)[Cursor](https://cursor.com)[RooCode](https://roocode.com)[Gemini CLIfrom Google](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/configuration.md#available-settings-in-settingsjson)[Kilo Code](https://kilocode.ai/)[Phoenix](https://phoenix.new/)[Semgrep](https://semgrep.dev)[Coding agentfrom GitHub Copilot](https://gh.io/coding-agent-docs)[![Ona logo](../../raw/assets/bba6e5d9612dd2aa.svg)![Ona logo](../../raw/assets/614d0fee63ca71b0.svg)

Ona](https://ona.com)[![Windsurf logo](../../raw/assets/9a567f7ecbfcc806.svg)![Windsurf logo](../../raw/assets/d122528b2c575326.svg)

Windsurffrom Cognition](https://windsurf.com)[Augment Code](https://docs.augmentcode.com/cli/overview)

View all supported agents

## Examples

```
# Sample AGENTS.md file


## Dev environment tips


- Use `pnpm dlx turbo run where <project_name>` to jump to a package instead of scanning with `ls`.


- Run `pnpm install --filter <project_name>` to add the package to your workspace so Vite, ESLint, and TypeScript can see it.


- Use `pnpm create vite@latest <project_name> -- --template react-ts` to spin up a new React + Vite package with TypeScript checks ready.


- Check the name field inside each package's package.json to confirm the right name—skip the top-level one.


## Testing instructions


- Find the CI plan in the .github/workflows folder.


- Run `pnpm turbo run test --filter <project_name>` to run every check defined for that package.


- From the package root you can just call `pnpm test`. The commit should pass all tests before you merge.


- To focus on one step, add the Vitest pattern: `pnpm vitest run -t "<test name>"`.


- Fix any test or type errors until the whole suite is green.


- After moving files or changing imports, run `pnpm lint --filter <project_name>` to be sure ESLint and TypeScript rules still pass.


- Add or update tests for the code you change, even if nobody asked.


## PR instructions


- Title format: [<project_name>] <Title>


- Always run `pnpm lint` and `pnpm test` before committing.
```

[### openai/codex

General-purpose CLI tooling for AI coding agents.

Rust

![Contributor avatar](../../raw/assets/9cda3a294b1c5605.png)![Contributor avatar](../../raw/assets/9e41126b9e86de5e.png)![Contributor avatar](../../raw/assets/15ee49fad4bce144.png)

+ 723](https://github.com/openai/codex/blob/-/AGENTS.md)[### apache/airflow

Platform to programmatically author, schedule, and monitor workflows.

Python

![Contributor avatar](../../raw/assets/aadbfa74f8ac8569.png)![Contributor avatar](../../raw/assets/b563c7a269d4d7b8.png)![Contributor avatar](../../raw/assets/e26fc7652005dd30.png)

+ 4801](https://github.com/apache/airflow/blob/-/AGENTS.md)[### temporalio/sdk-java

Java SDK for Temporal, workflow orchestration defined in code.

Java

![Contributor avatar](../../raw/assets/5802b4cc71cf52dc.png)![Contributor avatar](../../raw/assets/3323ee57ec53508f.png)![Contributor avatar](../../raw/assets/227d56b252c0c0ac.png)

+ 164](https://github.com/temporalio/sdk-java/blob/-/AGENTS.md)[### PlutoLang/Pluto

A superset of Lua 5.4 with a focus on general-purpose programming.

C++

![Contributor avatar](../../raw/assets/61906c75109a2369.png)![Contributor avatar](../../raw/assets/52de077874f2a9f9.png)![Contributor avatar](../../raw/assets/a2c0d3cf54317f6e.png)

+ 8](https://github.com/PlutoLang/Pluto/blob/-/AGENTS.md)

[View 60k+ examples on GitHub](https://github.com/search?q=path%3AAGENTS.md+NOT+is%3Afork+NOT+is%3Aarchived&type=code)

## How to use AGENTS.md?

### 1. Add AGENTS.md

Create an AGENTS.md file at the root of the repository. Most coding agents can even scaffold one for you if you ask nicely.

### 2. Cover what matters

Add sections that help an agent work effectively with your project. Popular choices:

- Project overview
- Build and test commands
- Code style guidelines
- Testing instructions
- Security considerations

### 3. Add extra instructions

Commit messages or pull request guidelines, security gotchas, large datasets, deployment steps: anything you’d tell a new teammate belongs here too.

### 4. Large monorepo? Use nested AGENTS.md files for subprojects

Place another AGENTS.md inside each package. Agents automatically read the nearest file in the directory tree, so the closest one takes precedence and every subproject can ship tailored instructions. For example, at time of writing the main OpenAI repo has 88 AGENTS.md files.

## About

AGENTS.md emerged from collaborative efforts across the AI software development ecosystem, including [OpenAI Codex](https://openai.com/codex/), [Amp](https://ampcode.com), [Jules from Google](https://jules.google), [Cursor](https://cursor.com), and [Factory](https://factory.ai).

We’re committed to helping maintain and evolve this as an open format that benefits the entire developer community, regardless of which coding agent you use.

AGENTS.md is now stewarded by the [Agentic AI Foundation](https://aaif.io) under the Linux Foundation. [Learn more →](https://openai.com/index/agentic-ai-foundation/)

## FAQ

### Are there required fields?

No. AGENTS.md is just standard Markdown. Use any headings you like; the agent simply parses the text you provide.

### What if instructions conflict?

The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything.

### Will the agent run testing commands found in AGENTS.md automatically?

Yes—if you list them. The agent will attempt to execute relevant programmatic checks and fix failures before finishing the task.

### Can I update it later?

Absolutely. Treat AGENTS.md as living documentation.

### How do I migrate existing docs to AGENTS.md?

Rename existing files to AGENTS.md and create symbolic links for backward compatibility:

```
mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md
```

### How do I configure Aider?

Configure Aider to use AGENTS.md in `.aider.conf.yml`:

```
read: AGENTS.md
```

### How do I configure Gemini CLI?

Configure Gemini CLI to use AGENTS.md in `.gemini/settings.json`:

```
{ "context": { "fileName": "AGENTS.md" }, }
```
