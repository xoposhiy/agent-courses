# Lab 2 [Sales Agent]

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/Jtj7x5djEv6) · [Raw file](../../raw/videos/Jtj7x5djEv6.html)

Retrieved: 2026-11-13T16:57:37.165936+00:00

[00:00] **Speaker 5**: This is the second sandbox lab. It's the same pattern as lab one, but with two new things. Uploading a file into the sandbox before the agent runs and reading a file back out after it finishes  The Chinook database is a SQLite file sitting in the M2 directory. The agent needs it inside the sandbox, but the sandbox starts empty, so we have to upload it explicitly

[00:22] **Speaker**: First, we create the sandbox the same way that we did in lab one

[00:26] **Speaker**: Then after we call

[00:28] **Speaker**: Back end upload files with the database contents.  This seeds the sandbox file system so the agent finds Chinook DB when it goes looking for it

[00:35] **Speaker**: The loop here checks each upload result for errors. If the upload failed, we raise before the agent even starts

[00:43] **Speaker**: The system prompt here tells the agent three things

[00:45] **Speaker**: that the database is at ChinookDB

[00:48] **Speaker**: to use SQLite 3 and Matplotlib to answer with charts

[00:51] **Speaker**: and to install any packages it needs with pip before importing them.  That last instruction is important. The sandbox is a fresh environment with no pre-installed data science libraries. The agent has to install them itself     the request here is specific. Query revenue by genre, produce a donut chart, group anything under three percent into an other slice, and to label each slice with name and percentage with no overlapping labels.

[01:17] **Speaker**: Detailed chart instructions like this help the agent get it right without multiple rounds of feedback    After invoke   we call this to pull the PNG bytes out of the sandbox directly, then write them to disk.

[01:30] **Speaker**: And this is the same cleanup as lab one. The sandbox always gets deleted

[01:37] **Speaker**: This one will take even longer than lab one. The agent queries the database, installs Matplotlib, writes and runs a charting script, and may iterate if the output doesn't look right  Great. So that took a while, and I sped this video up, but now we can see the summary

[01:54] **Speaker**: We have the revenue by genre

[01:55] **Speaker**: And I'll show you the donut in just a second

[02:00] **Speaker**: Here we seeded the sandbox

[02:01] **Speaker**: with upload_files, and the agent does its work with execute. You retrieve the result with sandbox_read, and the agent never touches your local machine. Now for the moment you've been waiting for, here's the donut

[02:14] **Speaker 6**: a donut showing each genre's share of total Chinook sales revenue. The agent produced this entirely inside the sandbox, queried the database, installed its own dependencies, wrote a charting script, ran it, and the file came back to us through sandbox read
