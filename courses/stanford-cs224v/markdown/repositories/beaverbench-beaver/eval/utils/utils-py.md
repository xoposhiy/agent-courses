# Project code: beaverbench/beaver: eval/utils/utils.py

[Course index](../../../../../README.md) · [Original source](https://github.com/beaverbench/beaver/blob/HEAD/eval/utils/utils.py) · [Raw file](../../../../../raw/repositories/beaverbench-beaver/eval/utils/utils.py)

Retrieved: 2026-11-13T17:04:57.605700+00:00

```python
import json

def read_json(fn):
    with open(fn) as f:
        return json.load(f)

def write_json(obj, fn):
    with open(fn, 'w') as f:
        json.dump(obj, f, indent=2)
```
