# Project code: stanford-oval/Churro: docs/api/churro_ocr.md

[Course index](../../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/docs/api/churro_ocr.md) · [Raw file](../../../../../raw/repositories/stanford-oval-churro/docs/api/churro_ocr.md)

Retrieved: 2026-11-13T17:04:51.902331+00:00

# `churro_ocr`

`churro_ocr` is a convenience namespace. It re-exports the most common classes and helpers from the package's owning modules so application code can import from one place.

Use the canonical module pages below when you need exact signatures and field definitions:

| Convenience import | Canonical reference |
| --- | --- |
| `DocumentOCRPipeline`, `DocumentOCRResult` | [`churro_ocr.document`](document-md.md) |
| `OCRClient`, `OCRResult`, `OCRBackend`, `BatchOCRBackend` | [`churro_ocr.ocr`](ocr-md.md) |
| `DocumentPage`, `DocumentPageDetector`, `PageCandidate`, `PageDetectionRequest`, `PageDetectionResult`, `PageDetector`, `PageDetectionBackend` | [`churro_ocr.page_detection`](page_detection-md.md) |
| `DEFAULT_OCR_TEMPLATE`, `CHURRO_3B_MODEL_ID`, `CHURRO_3B_XML_TEMPLATE` | [`Template APIs`](templates-md.md) |
| `ChurroError`, `ConfigurationError`, `ProviderError` | root package convenience import path |

The root package is intentionally documented as a convenience-import page instead of a second full API target. That keeps each public symbol anchored to one canonical module in the generated reference.
