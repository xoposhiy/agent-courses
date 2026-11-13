# Project code: stanford-oval/genie-worksheets: scripts/calculate_cost.py

[Course index](../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/scripts/calculate_cost.py) · [Raw file](../../../../raw/repositories/stanford-oval-genie-worksheets/scripts/calculate_cost.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import re
from glob import glob

files = glob("baselines/bank_fraud_report.log")
total_cost = 0
for file in files:
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            cost = re.findall(r"Total cost: ([0-9]+\.[0-9]+)", line)
            # if len(cost):
            #     print(cost)
            if cost:
                total_cost += float(cost[0])

print(f"Total cost: ${total_cost:.2f}")

```
