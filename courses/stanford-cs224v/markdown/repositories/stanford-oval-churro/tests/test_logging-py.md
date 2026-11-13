# Project code: stanford-oval/Churro: tests/test_logging.py

[Course index](../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/tests/test_logging.py) · [Raw file](../../../../raw/repositories/stanford-oval-churro/tests/test_logging.py)

Retrieved: 2026-11-13T17:04:51.902331+00:00

```python
from __future__ import annotations

from churro_ocr._internal import logging as churro_logging


def test_logger_adapter_formats_stdlib_style_messages() -> None:
    records: list[tuple[str, str]] = []

    class FakeLogger:
        def info(self, message: str) -> None:
            records.append(("info", message))

        def warning(self, message: str) -> None:
            records.append(("warning", message))

        def error(self, message: str) -> None:
            records.append(("error", message))

        def debug(self, message: str) -> None:
            records.append(("debug", message))

        def critical(self, message: str) -> None:
            records.append(("critical", message))

        def exception(self, message: str) -> None:
            records.append(("exception", message))

        def log(self, level: str, message: str) -> None:
            records.append((level, message))

    logger = churro_logging._LoggerAdapter(FakeLogger())

    logger.info("Page %s edge %s", 3, "left")
    logger.error("Failed to parse %s", "response.json")
    logger.log("INFO", "Value=%s", 42)

    assert records == [
        ("info", "Page 3 edge left"),
        ("error", "Failed to parse response.json"),
        ("INFO", "Value=42"),
    ]

```
