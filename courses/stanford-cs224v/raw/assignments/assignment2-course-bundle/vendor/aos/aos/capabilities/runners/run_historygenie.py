"""Transcribe image-based documents to markdown with HistoryGenie's vision-LLM OCR.

Executed with external/historygenie/.venv/bin/python (historygenie-core + pymupdf + pillow).
Reads API_KEY, BASE_URL and AOS_MODEL from the environment.
"""

import argparse
import asyncio
import importlib.util
import json
import os
import sys
from io import BytesIO
from pathlib import Path

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"}


def collect(paths):
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(f for f in p.rglob("*") if f.suffix.lower() in IMAGE_SUFFIXES | {".pdf"}))
        elif p.is_file():
            files.append(p)
    return files


def load_ocr_class(repo: Path):
    """Import engine/ocr/llm_ocr.py on its own; the engine package pulls in cloud dependencies."""
    spec = importlib.util.spec_from_file_location("llm_ocr", repo / "engine" / "ocr" / "llm_ocr.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CloudFunctionLLMOCR


def page_images(path: Path, dpi: int):
    from PIL import Image

    if path.suffix.lower() == ".pdf":
        import fitz

        doc = fitz.open(path)
        for page in doc:
            yield Image.open(BytesIO(page.get_pixmap(dpi=dpi).tobytes("png")))
    else:
        yield Image.open(path)


USAGE = {"calls": 0, "input_tokens": 0, "output_tokens": 0}


def track_usage(kwargs, completion_response, start_time, end_time):
    usage = getattr(completion_response, "usage", None)
    if usage is not None:
        USAGE["calls"] += 1
        USAGE["input_tokens"] += int(getattr(usage, "prompt_tokens", 0) or 0)
        USAGE["output_tokens"] += int(getattr(usage, "completion_tokens", 0) or 0)


async def transcribe(files, out: Path, model: str, dpi: int, repo: Path) -> list[str]:
    import litellm
    from historygenie_core.llm import models as hg_models

    litellm.success_callback = [track_usage]

    hg_models.MODEL_MAP[model] = [{
        "provider_model": f"openai/{model}",
        "max_completion_tokens": None,
        "static_params": {"api_base": os.environ["BASE_URL"], "api_key": os.environ["API_KEY"]},
    }]
    ocr = load_ocr_class(repo)(engine=model)
    written = []
    for path in files:
        parts = []
        for n, image in enumerate(page_images(path, dpi), start=1):
            text = await ocr.process_image(image.convert("RGB"))
            parts.append(f"## Page {n}\n\n{text.strip()}\n")
            print(f"HistoryGenie: {path.name} page {n}: {len(text)} chars")
        target = out / f"{path.stem}.md"
        target.write_text(f"# {path.name}\n\n" + "\n".join(parts))
        written.append(str(target))
    return written


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--dpi", type=int, default=200)
    args = ap.parse_args()
    os.environ.setdefault("LITELLM_DISABLE_CACHE", "true")
    os.environ.pop("GOOGLE_CLOUD_PROJECT", None)
    files = collect(args.inputs)
    if not files:
        raise SystemExit(f"no PDF or image files found in {args.inputs}")
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    model = os.environ.get("AOS_MODEL", "gemini-3.6-flash")
    written = asyncio.run(transcribe(files, out, model, args.dpi, Path.cwd()))
    (out / "usage.json").write_text(json.dumps({"model": model, **USAGE, "cost_usd": None}, indent=2))
    print(f"HistoryGenie transcribed {len(written)} document(s) into {out}; {USAGE}")


if __name__ == "__main__":
    main()
