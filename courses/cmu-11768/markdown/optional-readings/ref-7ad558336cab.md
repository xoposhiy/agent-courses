# OpenHands SDK

[Course index](../../README.md) · [Original source](https://docs.openhands.dev/sdk) · [Raw file](../../raw/optional-readings/ref-7ad558336cab.html)

Retrieved: 2026-11-13T16:58:45.342254+00:00

# Software Agent SDK

Copy pageCopy page

Build AI agents that write software. A clean, modular SDK with production-ready tools.

Copy pageCopy page

The OpenHands Software Agent SDK is a set of Python and REST APIs for building **agents that work with code**.
You can use the OpenHands Software Agent SDK for:

- One-off tasks, like building a README for your repo
- Routine maintenance tasks, like updating dependencies
- Major tasks that involve multiple agents, like refactors and rewrites
- OpenAI-compatible access to an OpenHands agent from chat UIs, IDEs, voice platforms, and other clients

You can even use the SDK to build new developer experiences—it’s the engine behind [Agent Canvas](https://docs.openhands.dev/openhands/usage/agent-canvas/overview) and [OpenHands Cloud](https://docs.openhands.dev/openhands/usage/cloud/openhands-cloud).
Get started with some examples or keep reading to learn more.

## Features

## Single Python API

A unified Python API that enables you to run agents locally or in the cloud, define custom agent behaviors, and create custom tools.

## Pre-defined Tools

Ready-to-use tools for executing Bash commands, editing files, browsing the web, integrating with MCP, and more.

## REST-based Agent Server

A production-ready server that runs agents anywhere, including Docker and Kubernetes, while connecting seamlessly to the Python API.

## OpenAI-Compatible Endpoint

Access the OpenHands agent via OpenAI-compatible Chat Completions and Responses endpoints for chat UIs, IDEs, voice platforms, and other OpenAI-style clients.

## Why OpenHands Software Agent SDK?

### Emphasis on coding

While other agent SDKs (e.g. [LangChain](https://python.langchain.com/docs/tutorials/agents/)) are focused on more general use cases, like delivering chat-based support or automating back-office tasks, OpenHands is purpose-built for software engineering.
While some folks do use OpenHands to solve more general tasks (code is a powerful tool!), most of us use OpenHands to work with code.

### State-of-the-Art Performance

OpenHands is a top performer across a wide variety of benchmarks, including SWE-bench, SWT-bench, and multi-SWE-bench. The SDK includes a number of state-of-the-art agentic features developed by our research team, including:

- Task planning and decomposition
- Automatic context compression
- Security analysis
- Strong agent-computer interfaces

OpenHands has attracted researchers from a wide variety of academic institutions, and is [becoming the preferred harness](https://x.com/Alibaba_Qwen/status/1947766835023335516) for evaluating LLMs on coding tasks.

### Free and Open Source

OpenHands is also the leading open source framework for coding agents. It’s MIT-licensed, and can work with any LLM—including big proprietary LLMs like Claude and OpenAI, as well as open source LLMs like Qwen and Devstral.
Other SDKs (e.g. [Claude Code](https://github.com/anthropics/claude-agent-sdk-python)) are proprietary and lock you into a particular model. Given how quickly models are evolving, it’s best to stay model-agnostic!

## Get Started

## Getting Started Guide

Install the SDK, run your first agent, and explore the guides.

## Learn the SDK

## Core Concepts

Understand the SDK’s architecture: agents, tools, workspaces, and more.

## API Reference

Explore the complete SDK API and source code.

## Build with Examples

## Standalone SDK

Build local agents with custom tools and capabilities.

## Remote Execution

Run agents on remote servers with Docker sandboxing.

## GitHub Workflows

Automate repository tasks with agent-powered workflows.

## Community

## Join Slack

Connect with the OpenHands community on Slack.

## GitHub Repository

Contribute to the SDK or report issues on GitHub.

Was this page helpful?

YesNo
