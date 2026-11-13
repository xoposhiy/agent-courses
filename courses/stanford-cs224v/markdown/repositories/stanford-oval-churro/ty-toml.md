# Project code: stanford-oval/Churro: ty.toml

[Course index](../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/ty.toml) · [Raw file](../../../raw/repositories/stanford-oval-churro/ty.toml)

Retrieved: 2026-11-13T17:04:51.902331+00:00

```toml
[src]
include = ["src", "tests"]

[rules]
unused-ignore-comment = "error"
unused-type-ignore-comment = "error"
redundant-cast = "error"
possibly-unresolved-reference = "warn"

[environment]
python-version = "3.12"

[terminal]
error-on-warning = true
output-format = "concise"

[[overrides]]
include = ["tests/**"]

[overrides.rules]
possibly-unresolved-reference = "ignore"

```
