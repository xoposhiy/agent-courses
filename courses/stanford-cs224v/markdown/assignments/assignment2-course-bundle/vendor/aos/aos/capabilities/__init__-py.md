# Homework 2 bundle: vendor/aos/aos/capabilities/__init__.py

[Course index](../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/capabilities/__init__.py) · [Raw file](../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/capabilities/__init__.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""Registry of workers: the coding agent, the wrapped external systems and the user's own.

``AOS_WORKERS`` adds workers without editing AOS: a comma-separated list of ``module:Class`` or
``path/to/file.py:Class`` entries, each a ``Worker`` subclass. A class whose constructor takes an
``llm`` parameter receives AOS's client (its calls are then costed like the coding agent's).
"""

from __future__ import annotations

import importlib
import importlib.util
import inspect
import os
from pathlib import Path

from ..coding_agent import CodingAgent
from ..worker import Worker
from .datastorm import DataStorm
from .forma import SatIR, Verdict
from .grill import Grill
from .historygenie import HistoryGenie
from .sliders import Sliders
from .storm import Storm


def all_workers(llm) -> dict[str, Worker]:
    workers: list[Worker] = [
        CodingAgent(llm), Grill(), Storm(), Sliders(), DataStorm(), HistoryGenie(), SatIR(), Verdict(),
    ]
    workers += custom_workers(llm)
    return {w.name: w for w in workers}


def available_workers(llm) -> dict[str, Worker]:
    return {name: w for name, w in all_workers(llm).items() if w.available()[0]}


def custom_workers(llm, spec: str | None = None) -> list[Worker]:
    """Instantiate the workers named in ``AOS_WORKERS`` (or ``spec``); a later entry overrides an earlier worker of the same name."""
    spec = os.environ.get("AOS_WORKERS", "") if spec is None else spec
    workers = []
    for item in (s.strip() for s in spec.split(",")):
        if not item:
            continue
        target, sep, class_name = item.rpartition(":")
        if not sep:
            raise RuntimeError(f"AOS_WORKERS entry {item!r} must look like module:Class or path/to/file.py:Class")
        try:
            if target.endswith(".py"):
                loader = importlib.util.spec_from_file_location(Path(target).stem, target)
                module = importlib.util.module_from_spec(loader)
                loader.loader.exec_module(module)
            else:
                module = importlib.import_module(target)
            cls = getattr(module, class_name)
        except Exception as exc:
            raise RuntimeError(f"AOS_WORKERS: cannot load {item!r}: {type(exc).__name__}: {exc}") from None
        if not (inspect.isclass(cls) and issubclass(cls, Worker)) or not cls.name:
            raise RuntimeError(f"AOS_WORKERS: {item!r} is not a Worker subclass with a name")
        workers.append(cls(llm) if "llm" in inspect.signature(cls).parameters else cls())
    return workers

```
