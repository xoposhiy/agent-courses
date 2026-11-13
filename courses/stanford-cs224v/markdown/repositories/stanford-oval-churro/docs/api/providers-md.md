# Project code: stanford-oval/Churro: docs/api/providers.md

[Course index](../../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/docs/api/providers.md) · [Raw file](../../../../../raw/repositories/stanford-oval-churro/docs/api/providers.md)

Retrieved: 2026-11-13T17:04:51.902331+00:00

# Provider APIs

`churro_ocr.providers` is a convenience namespace. It re-exports backend builders, provider option dataclasses, and page-detection helpers from the owning modules below.

Use the canonical module that owns each symbol:

| Convenience import | Canonical reference |
| --- | --- |
| `build_ocr_backend(...)` | `churro_ocr.providers.builder` |
| `OCRBackendSpec`, `OCRModelProfile`, `LiteLLMTransportConfig`, `HuggingFaceOptions`, `OpenAICompatibleOptions`, `AzureDocumentIntelligenceOptions`, `MistralOptions`, `resolve_ocr_profile(...)` | `churro_ocr.providers.specs` |
| `AzurePageDetector`, `LLMPageDetector`, `locate_text_block_bbox_with_llm(...)`, `locate_text_block_bbox_with_llm_sync(...)` | `churro_ocr.providers.page_detection` |

## `churro_ocr.providers.builder`

```{eval-rst}
.. automodule:: churro_ocr.providers.builder
   :members: build_ocr_backend
```

## `churro_ocr.providers.specs`

```{eval-rst}
.. automodule:: churro_ocr.providers.specs
   :members:
   :show-inheritance:
```

## `churro_ocr.providers.page_detection`

```{eval-rst}
.. automodule:: churro_ocr.providers.page_detection
   :members:
   :show-inheritance:
```
