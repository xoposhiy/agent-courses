# Project code: stanford-oval/genie-worksheets: experiments/agents/apartment_schedule/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/apartment_schedule/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/apartment_schedule/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
prompt_dir = os.path.join(current_dir, "prompts")

botname = "Apartment Visit Booking Bot"
starting_prompt = (
    "Hello! I am a bot that helps you book an appointment to visit an apartment. "
)
description = "You are a bot that helps customers book an appointment to visit an apartment. You need to ask the customer for their name, the name of the apartment they want to visit, the day of the visit, the start time, whether they have paid the application fee, and any special requests they have. You need to check if the booking is available and then book the appointment if it is. You should provide the customer with a booking ID if the appointment is successfully booked."

```
