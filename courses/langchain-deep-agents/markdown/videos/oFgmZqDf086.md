# Lab 2 (LS Walkthrough)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/oFgmZqDf086) · [Raw file](../../raw/videos/oFgmZqDf086.html)

Retrieved: 2026-11-13T16:57:39.126059+00:00

[00:00] **Speaker 4**: so this run took 87 seconds and almost 94,000 tokens. Lab one ran for roughly 12 seconds at 34,000 tokens. This run took longer than Lab One because the agent explored the database schema, installed a dependency, and iterated through a few errors before producing the final chart

[00:21] **Speaker**: So the agent's first move was to explore. Before writing any code, it ran a shell command to list the database tables

[00:28] **Speaker**: And the result came back with all the table names.

[00:32] **Speaker**: Album,  track,  genre, and so on

[00:37] **Speaker**: Then it checked the schema for the three tables that it needed.   This is the agent figuring out how to join the data before writing a single line of Python.           so once I understood the schema, it wrote the full charting script to create genre.py and then ran it

[00:59] **Speaker**: running it

[01:00] **Speaker**: And it failed  This attempt used Python similar to Lab 1 and had the same error exit code.

[01:08] **Speaker**: Trying again with Python 3

[01:12] **Speaker**: which also failed, but for a different reason

[01:16] **Speaker**: Matplotlib wasn't installed

[01:20] **Speaker**: And here the agent installed matplotlib itself.

[01:24] **Speaker**: and then rerun the script.

[01:29] **Speaker**: Some checking

[01:31] **Speaker**: And here we go

[01:33] **Speaker**: So this whole trace is a self-correction loop playing out in full, exploring, writing, hitting errors, fixing them, and then finally succeeding
