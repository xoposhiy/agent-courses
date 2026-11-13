"""Share request pacing across course collectors running on the same machine."""

from contextlib import contextmanager
from pathlib import Path
import os
import time


@contextmanager
def paced_host(host: str, interval: float = 3.1):
    """Keep one request active per host and leave time between request starts."""
    directory = Path(__file__).resolve().parent.parent / ".cache" / "network"
    directory.mkdir(parents=True, exist_ok=True)
    filename = "".join(character if character.isalnum() else "-" for character in host)
    lock_path = directory / f"{filename}.lock"
    timestamp_path = directory / f"{filename}.timestamp"
    with lock_path.open("a+b") as handle:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"0")
            handle.flush()
        if os.name == "nt":
            import msvcrt
            while True:
                try:
                    handle.seek(0)
                    msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                    break
                except OSError:
                    time.sleep(0.2)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            try:
                last_request = float(timestamp_path.read_text(encoding="ascii"))
            except (OSError, ValueError):
                last_request = 0
            time.sleep(max(0, interval - (time.time() - last_request)))
            timestamp_path.write_text(str(time.time()), encoding="ascii")
            yield
        finally:
            if os.name == "nt":
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
