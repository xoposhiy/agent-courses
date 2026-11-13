# HW3

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/HW3.html) · [Raw file](../../raw/assignments/hw3.html)

Retrieved: 2026-11-13T16:40:50.257580+00:00

COMS 4995-15

# Introduction to Designing LLM Agents

[← Back to Course Home](../pages/index.md)

# Homework 3: Build Your First Agent

**Released:** Monday, October 12

**Due:** Monday, November 2 @ 11:59 PM ET (submit on Gradescope)

## Overview

You will build a conversational agent that embodies a celebrity: a politician, actor, musician, influencer, or any public figure with enough reliable information online to build a memory store.

Your agent must (1) store information about the celebrity from public sources, (2) decide what to say using that information, (3) respond in the celebrity's style, (4) say it doesn't know when asked about something the celebrity wouldn't know, and (5) end the conversation with an in-character goodbye. Users chat with it through a web app where they can start new conversations and continue old ones.

The skeleton repo defines the module boundaries and function interfaces. Keep your implementation consistent with them.

**Starter Code**

Download the skeleton repo for HW3.

[Download celebrity\_agent.zip](archive-celebrity-agent.md)

**You may add any functionality beyond the skeleton, as long as your agent meets the core requirements.**

## Implementation Instructions

### Part 1: Memory Store

**Goal:** Build a searchable memory of the celebrity from public web content.

- Collect public sources (Wikipedia pages, interview transcripts, profiles, talks).
- Split the sources into `MemoryChunk`s and store them in a `MemoryStore`.
- Implement `MemoryStore.retrieve(query)`. You may reuse your retriever from HW2 Part 3.
- Build and load the store with `build_memory_store(...)` and `load_memory_store(...)`.

**Output:** the chunks relevant to a query, with metadata.

### Part 2: Content Module

**Goal:** Decide what the response says.

- Work out what information the user's message needs. Follow-ups ("what happened after that?") depend on the conversation so far.
- Turn the retrieved chunks into a content plan in `make_content_plan(user_message, retrieved, history)`.
- `content_step(memory, user_message, history)` runs retrieval and planning together.

**Output:** a grounded content plan for the style module.

### Part 3: Style Module

**Goal:** Say it the way the celebrity would.

- Write a style specification: tone, sentence structure, typical phrasing, conversational habits.
- Turn the content plan into a response in `stylize(content_plan)`.
- Add no factual claims beyond the content plan.

**Output:** the final user-facing message.

### Part 4: Guardrails

**Goal:** Say "I don't know" when the celebrity wouldn't know.

- Pick a knowledge cutoff date, such as their death, their retirement, or your most recent source. The agent should not know about later events.
- Decide what falls outside their expertise. A pop star should not debug Python or interpret a lab result.
- Detect both in `out_of_scope(user_message, history)` and respond in character in `decline(user_message)`.

### Part 5: Conversations and Sign-off

**Goal:** Track multiple conversations and end each one naturally.

- Save conversations to disk in `conversations.py` so users can start new ones and continue old ones, even after the app restarts.
- End a conversation automatically at a natural endpoint (e.g., the user says "thanks" or "bye") in `should_end(user_message, history)`. Ended conversations are read-only.
- Add an in-character sign-off in `add_signoff(response)`.
- Run one full turn in `respond(memory, conversation, user_message)`.

### Part 6: Web App

**Goal:** Build a web interface for chatting with your agent.

- Frontend: a frontend framework of your choice, in `frontend/`. Some options are [React](../references/react.md), [Vue](../references/vue.md), and [Svelte](../references/svelte.md).
- Backend: a server of your choice that exposes your agent and conversation store. Some options are [FastAPI](../references/fastapi.md) and [Flask](../references/flask.md).
- Users must be able to start a conversation, browse past ones, continue one, and see when the agent has ended one.
- Put the install and launch commands in `README.md`.

## Submission Guidelines

Zip the `celebrity_agent` folder. It should launch after unzipping by following `README.md`. Leave out installed dependencies (e.g. `node_modules/`, virtual environments), build output, and your API key.

**Your writeup, `celebrity_agent.pdf`, should explain each design choice and why you made it, covering:**

- Celebrity: who, why, and what defines their voice.
- Data: your sources and how you collected them.
- Memory store: cleaning, chunking, indexing, and retrieval.
- Content module: query parsing, retrieval strategy, and what happens when nothing relevant is found.
- Style module: style specification, prompt engineering, and how you preserve content.
- Guardrails: your knowledge cutoff and why, what counts as outside their expertise, how you detect both, and questions your guardrails get wrong.
- Conversations: storage, how earlier turns reach the agent, and ending logic.
- Web app: framework, how the frontend and backend connect, and a screenshot of the conversation list.
- A short transcript showing retrieval, stylized output, a declined question, and a natural goodbye.
- Any other design decisions (temperature, response length, model choice, etc.) and why.

**Due Date:** Monday, November 2 @ 11:59 PM ET (submit on Gradescope under "HW 3")

**Files to Upload:**

- `celebrity_agent.zip` — your code.
- `celebrity_agent.pdf` — your writeup.

**Late policy:** Late days apply automatically; otherwise late work is not accepted.
