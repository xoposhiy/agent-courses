# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m0/m0.2-setup-agent.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m0/m0.2-setup-agent.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m0/m0.2-setup-agent.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m0.2-setup-agent.md)

<a id="getting-set-up-coding-agent"></a>


# Getting Set Up (Coding Agent)

Follow these steps to get your AI environment ready for the course.

<a id="setup"></a>


## Setup

<a id="prerequisites"></a>


### Prerequisites

- Node.js (used to install skills): [nodejs.org](https://nodejs.org)

<a id="setup-your-ai-environment"></a>


### Setup Your AI Environment

You may choose to use a coding agent or AI tool when taking the course. We recommend using [dcode](https://docs.langchain.com/oss/python/deepagents/code/overview), an open source coding agent built on the Deep Agents SDK. The following can make it more effective:

<a id="course-tutor"></a>


#### Course Tutor

The Deep Agents Course Skill allows you to take the course from within your favorite AI tool.

<a id="coding-agent-setup"></a>


##### Coding Agent Setup

```text
cd lca-deepagents
npx skills add langchain-ai/lca-tutors/lca-deepagents
```

Open your coding agent and verify that `/lca-deepagents` exists as a skill.

<a id="setup-with-browser-based-ai-chat-interface"></a>


##### Setup with Browser-based AI Chat Interface

If you are using a browser-based AI Chat Interface, most can load skills from zip files. For this, you will need to zip the `lca-deepagents` directory found in the [repository of course tutors](https://github.com/langchain-ai/lca-tutors):

```text
git clone --depth 1 https://github.com/langchain-ai/lca-tutors.git
cd lca-tutors
zip -r lca-deepagents.zip lca-deepagents
```

<a id="using-the-tutor"></a>


##### Using the Tutor

Invoke the tutor with `/lca-deepagents`, or optionally pass a lesson ID to jump straight to a specific point in the course (e.g. `/lca-deepagents m2.3`).

What it does:

- Teaches lesson content and advances you through the full curriculum.
- Walks you through the course labs and quizzes
- Allows you to specify and adjust how frequently it checks-in with you
- Asks you questions about main ideas, critical concepts, and common misconceptions

<a id="langchain-skills"></a>


#### LangChain Skills

Install the LangChain skills to give your coding agent deep knowledge of Deep Agents, LangGraph, and the LangChain ecosystem. Run this from the repo root:

```text
cd lca-deepagents
npx skills add langchain-ai/langchain-skills --skill '*' --yes
```

This installs skills including `deep-agents-core`, `deep-agents-memory`, `deep-agents-orchestration`, and more.

<a id="langchain-docs-mcp-server"></a>


#### LangChain Docs MCP Server

Gives your coding agent direct access to LangChain, LangGraph, and LangSmith documentation, including search and a loaded skill that covers core concepts. Add it once and it is available in all your projects.

[Full setup instructions](https://docs.langchain.com/use-these-docs#use-our-mcp-servers)

<a id="langsmith-skills"></a>


#### LangSmith Skills

On-demand capabilities for querying traces, generating datasets, and defining evaluators, directly from within your agent session.

[Full setup instructions](https://docs.langchain.com/langsmith/skills)

<a id="deep-agents-source"></a>


#### Deep Agents source

Deep Agents is open source. Cloning the [repo](../../../../../readings/github-191947403d65.md) and pointing your coding agent to it gives it direct access to the source. That’s useful when exploring internals or debugging.

---
