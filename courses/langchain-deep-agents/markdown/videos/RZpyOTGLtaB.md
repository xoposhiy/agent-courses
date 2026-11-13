# Lab 2 (respond)

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/RZpyOTGLtaB) · [Raw file](../../raw/videos/RZpyOTGLtaB.html)

Retrieved: 2026-11-13T16:57:37.806837+00:00

[00:00] **Speaker**: This lab puts the respond decision to work in a real agent. Let's walk through the code

[00:06] **Speaker**: At the top here, we define two tools

[00:09] **Speaker**: ask_user takes a question  and a  list of choices. It doesn't actually collect input itself. It just returns a placeholder string

[00:16] **Speaker**: send_email sends an email and returns a confirmation  Neither tool does anything risky on its own. The interesting part is how we gate them.

[00:25] **Speaker**: The system prompt tells the agent one rule that matters here

[00:28] **Speaker**: If the request depends on a choice only the user can make,  to call ask user with the question and choices before drafting anything else

[00:37] **Speaker**: Now let's look at interrupt on.

[00:39] **Speaker**: ask_user only allows  the respond decision,  since there's nothing to approve, edit, or reject. A question isn't an action, so the only sensible response is an answer  send email, however

[00:51] **Speaker**: allows approve, edit, and reject since sending an email is a real side effect worth reviewing

[00:58] **Speaker**: We invoke the agent with a task

[01:00] **Speaker**: To email this professor that the user will be late, but first check whether to apologize or ask for an extension. Since that's a judgment call only the user can make, the agent should call ask before drafting the email  The resume loop handles both tools differently  When the pending request is ask user, we show the choices  with Questionnaire Select

[01:21] **Speaker**: which is just the UI layer for this demo.

[01:23] **Speaker**: And we package the user's pick as type respond messages selected. That message goes back to the model as if ask_user had returned it, and the model now has an answer to work from.

[01:33] **Speaker**: When the pending request is send email

[01:37] **Speaker**: we prompt for approve, edit, or reject, the same way you saw in lab one, and build the matching decision dictionary. Each pass through the loop calls agent.invoke again

[01:47] **Speaker**: so the agent picks up right where it paused.  It'll interrupt twice, once for ask user and once for send email. The loop keeps running until there are no more interrupts, and we print the final email once send email has actually run. Let's take a look

[02:04] **Speaker**: So here's our list of choices, and I'm using my arrow keys to switch between them.

[02:11] **Speaker**: I'm going to ask for a short extension on the deadline.

[02:15] **Speaker**: Now we can choose approve, edit, or reject. Let's approve it And here we have our email
