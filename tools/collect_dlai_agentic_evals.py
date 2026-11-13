"""Archive official agentic-evaluation course pages and advertised slide files."""

import json
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from corpus import Corpus


def main():
    corpus = Corpus("courses/dlai-agentic-evals", "dlai-agentic-evals", "DeepLearning.AI / Arize: Evaluating and Improving Agentic Applications", "https://www.deeplearning.ai/courses/evaluating-and-improving-agentic-applications")
    corpus.add(corpus.data["source_url"], "Official course page", "pages", "course-page")
    forum = "https://community.deeplearning.ai/t/evals-lecture-notes/896118"
    corpus.add(forum, "Official lecture notes and maintenance warning", "pages", "lecture-notes")
    data_item = corpus.add(forum + ".json", "Official lecture-notes topic metadata", "metadata", "lecture-notes-topic")
    data = json.loads((corpus.root / data_item["raw_path"]).read_text(encoding="utf-8"))
    post = BeautifulSoup(data["post_stream"]["posts"][0]["cooked"], "html.parser")
    modules = ["Foundations of Evals", "Observing and Benchmarking Agents", "Building Evaluators You Can Trust", "Evaluating Agent Actions and Outcomes", "Improving Agentic Applications"]
    attachments = []
    for index, anchor in enumerate(post.select("a.attachment[href]"), 1):
        url = urljoin(forum, anchor["href"])
        title = f"Module {index}: " + modules[index - 1]
        item = corpus.add(url, title, "slides", f"module-{index}", expected="pdf")
        attachments.append({"module": index, "title": title, "name": anchor.get_text(" ", strip=True), "url": url, "download_status": item["download_status"]})
    announcement = "https://community.deeplearning.ai/t/new-course-enroll-in-evaluating-and-improving-agentic-applications/896149"
    corpus.add(announcement, "Official course launch announcement", "pages", "launch-announcement")
    announcement_item = corpus.add(announcement + ".json", "Course launch topic metadata", "metadata", "launch-topic")
    launch_data = json.loads((corpus.root / announcement_item["raw_path"]).read_text(encoding="utf-8"))
    print("Launch post", launch_data["post_stream"]["posts"][0]["cooked"][:7000], flush=True)
    corpus.data["notes"] = [
        "The official lecture-notes post advertises five PDF modules, but the advertised short attachment URLs must be checked against actual responses before they can be treated as available files.",
        "The instructor warns that the slide PDFs are not maintained and can omit topics or contain errors; the lecture videos are updated separately. Treat the slide archive as a dated source, not as an authoritative correction to the videos.",
        "Course code, labs, quizzes, and video access were sought only through public official sources. No enrolled platform content or subscription-only files were accessed.",
    ]
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
    corpus.finalize()
    (corpus.root / "coverage.json").write_text(json.dumps({"advertised_modules": 5, "attachments": attachments}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(corpus.data["counts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
