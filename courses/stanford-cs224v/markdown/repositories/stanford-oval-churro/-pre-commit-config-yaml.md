# Project code: stanford-oval/Churro: .pre-commit-config.yaml

[Course index](../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/.pre-commit-config.yaml) · [Raw file](../../../raw/repositories/stanford-oval-churro/.pre-commit-config.yaml)

Retrieved: 2026-11-13T17:04:51.902331+00:00

```yaml
minimum_pre_commit_version: 4.0.0
default_install_hook_types:
  - pre-commit
  - pre-push

repos:
  - repo: local
    hooks:
      - id: format
        name: pixi format
        entry: pixi run format
        language: system
        pass_filenames: false
        stages:
          - pre-commit
        files: ^(src/|tests/|pyproject\.toml|pixi\.lock|pytest\.ini|ruff\.toml|ty\.toml)

      - id: lint
        name: pixi lint
        entry: pixi run lint
        language: system
        pass_filenames: false
        stages:
          - pre-commit
        files: ^(src/|tests/|pyproject\.toml|pixi\.lock|pytest\.ini|ruff\.toml|ty\.toml)

      - id: typecheck
        name: pixi typecheck
        entry: pixi run typecheck
        language: system
        pass_filenames: false
        stages:
          - pre-commit
        files: ^(src/|tests/|pyproject\.toml|pixi\.lock|pytest\.ini|ruff\.toml|ty\.toml)

      - id: test
        name: pixi test
        entry: pixi run test
        language: system
        pass_filenames: false
        stages:
          - pre-push
        files: ^(src/|tests/|pyproject\.toml|pixi\.lock|pytest\.ini|ruff\.toml|ty\.toml)

      - id: docs-build
        name: pixi docs-build
        entry: pixi run docs-build
        language: system
        pass_filenames: false
        stages:
          - manual

      - id: package-check
        name: pixi package-check
        entry: pixi run package-check
        language: system
        pass_filenames: false
        stages:
          - manual

```
