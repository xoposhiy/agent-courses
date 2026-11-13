# Course code: gemini.py

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/activities/gemini.py) · [Raw file](../../raw/activities/gemini.py)

Retrieved: 2026-11-13T16:40:57.574551+00:00

```python
from google import genai

API_KEY = "<your_api_key_here>"  # better: os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

def ask_gemini(prompt, model="gemini-3.5-flash-lite", temperature=1.0):
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={"temperature": temperature},
    )
    return response.text


if __name__ == "__main__":
    print(ask_gemini("Explain softmax temperature in two sentences."))
```
