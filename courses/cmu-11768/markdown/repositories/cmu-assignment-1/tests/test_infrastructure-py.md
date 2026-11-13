# Assignment 1: tests/test_infrastructure.py

[Course index](../../../../README.md) · [Original source](https://github.com/cmu-agents/assignment-1/blob/HEAD/tests/test_infrastructure.py) · [Raw file](../../../../raw/repositories/cmu-assignment-1/tests/test_infrastructure.py)

Retrieved: 2026-11-13T16:48:10.751888+00:00

```python
"""Fast checks for setup helpers that must work before student TODOs."""

from assignment.env import _tls_port_configuration


def test_runtime_port_uses_tls_and_is_not_duplicated():
    encrypted, unencrypted, extra = _tls_port_configuration(
        {
            "encrypted_ports": [8000, 9000],
            "unencrypted_ports": [7000, 8000],
            "cpu": 2,
        },
        8000,
    )

    assert encrypted == [8000, 9000]
    assert unencrypted == [7000]
    assert extra == {"cpu": 2}


def test_runtime_port_is_added_when_no_port_lists_are_given():
    encrypted, unencrypted, extra = _tls_port_configuration({}, 8000)

    assert encrypted == [8000]
    assert unencrypted == []
    assert extra == {}

```
