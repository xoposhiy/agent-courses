# Project code: stanford-oval/Churro: src/churro_ocr/errors.py

[Course index](../../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/src/churro_ocr/errors.py) · [Raw file](../../../../../raw/repositories/stanford-oval-churro/src/churro_ocr/errors.py)

Retrieved: 2026-11-13T17:04:51.902331+00:00

```python
"""Public exception types for the churro-ocr package."""

from __future__ import annotations


class ChurroError(RuntimeError):
    """Base exception for package-level failures."""


class ConfigurationError(ChurroError):
    """Raised when a backend is missing required runtime configuration."""


class ProviderError(ChurroError):
    """Raised when an OCR or page detection provider returns an unusable response."""

```
