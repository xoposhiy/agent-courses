# Project code: beaverbench/beaver: eval/dailsql/nltk_downloader.py

[Course index](../../../../../README.md) · [Original source](https://github.com/beaverbench/beaver/blob/HEAD/eval/dailsql/nltk_downloader.py) · [Raw file](../../../../../raw/repositories/beaverbench-beaver/eval/dailsql/nltk_downloader.py)

Retrieved: 2026-11-13T17:04:57.605700+00:00

```python
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')
```
