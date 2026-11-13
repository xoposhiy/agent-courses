# Code: lecture5-frameworks: tinycal/__main__.py

[Course index](../../../../README.md) · [Original source](https://github.com/cs329z/lecture5-frameworks/blob/HEAD/tinycal/__main__.py) · [Raw file](../../../../raw/repositories/cs329z-lecture5-frameworks/tinycal/__main__.py)

Retrieved: 2026-11-13T16:20:40.422150+00:00

```python
"""Run the calendar server: `python -m tinycal [--port 8765] [--no-browser]`."""

import argparse
import webbrowser

from .server import serve


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the tinycal calendar server.")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true", help="don't open the UI in a browser")
    args = parser.parse_args()

    url = f"http://localhost:{args.port}"
    print(f"tinycal running at {url}  (Ctrl+C to stop)")
    if not args.no_browser:
        webbrowser.open(url)
    try:
        serve(args.port)
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()

```
