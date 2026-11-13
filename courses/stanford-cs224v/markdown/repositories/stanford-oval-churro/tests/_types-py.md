# Project code: stanford-oval/Churro: tests/_types.py

[Course index](../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/tests/_types.py) · [Raw file](../../../../raw/repositories/stanford-oval-churro/tests/_types.py)

Retrieved: 2026-11-13T17:04:51.902331+00:00

```python
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pathlib import Path

type RGBColor = tuple[int, int, int]
type RGBAColor = tuple[int, int, int, int]
type ImageColor = str | RGBColor | RGBAColor


class ImportFailurePatcher(Protocol):
    def __call__(
        self,
        *,
        failing_name: str,
        exception_type: type[ImportError] = ImportError,
    ) -> None: ...


class WriteImageFile(Protocol):
    def __call__(
        self,
        *,
        size: tuple[int, int] = (10, 10),
        filename: str = "sample.png",
        mode: str = "RGB",
        color: ImageColor = "white",
    ) -> Path: ...


class HasKey(Protocol):
    key: str


class ReadableBody(Protocol):
    def read(self) -> bytes: ...


__all__ = [
    "HasKey",
    "ImageColor",
    "ImportFailurePatcher",
    "RGBAColor",
    "RGBColor",
    "ReadableBody",
    "WriteImageFile",
]

```
