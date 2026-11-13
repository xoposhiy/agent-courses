"""Archive public DLAI video transcripts and record account-only lesson access."""

import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

from corpus import Corpus


ROOT = Path("courses/dlai-agentic-evals")
COURSE = "https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications"


def page_props(binary):
    page = BeautifulSoup(binary, "html.parser")
    return json.loads(page.select_one("script#__NEXT_DATA__").string)["props"]["pageProps"]


def record_page(corpus, url, lesson, response, category):
    path = ROOT / "raw/lessons" / (lesson["slug"] + ".html")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(response.content)
    record = {"id": lesson["slug"], "title": lesson["name"], "url": url, "category": category, "retrieved_at": datetime.now(timezone.utc).isoformat(), "http_status": response.status_code, "final_url": response.url, "content_type": response.headers.get("Content-Type", ""), "raw_path": path.relative_to(ROOT).as_posix(), "bytes": len(response.content), "sha256": hashlib.sha256(response.content).hexdigest(), "download_status": "downloaded" if response.ok else "failed", "conversion_status": "pending", "notes": [], "lesson_type": lesson["type"], "access_control": lesson.get("accessControl"), "required_user_tier": lesson.get("requiredUserTier")}
    corpus.data["materials"].append(record)
    return record


def main():
    corpus = Corpus(ROOT, "dlai-agentic-evals", "DeepLearning.AI / Arize: Evaluating and Improving Agentic Applications", "https://www.deeplearning.ai/courses/evaluating-and-improving-agentic-applications")
    course_item = next(item for item in corpus.data["materials"] if item["url"] == corpus.data["source_url"])
    course_page = BeautifulSoup((ROOT / course_item["raw_path"]).read_bytes(), "html.parser")
    hrefs = {a["href"].split("/lesson/", 1)[1].split("/", 1)[0]: a["href"] for a in course_page.select("a[href]") if a["href"].startswith(COURSE + "/lesson/")}
    first_url = hrefs["53tpudpi"]
    first_response = corpus.request(first_url)
    first_props = page_props(first_response.content)
    course = next(query["state"]["data"] for query in first_props["trpcState"]["json"]["queries"] if query["queryKey"][0] == ["course", "getCourseBySlug"])
    lessons = course["lessons"]
    catalog_path = ROOT / "raw/metadata/course-outline.json"
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(json.dumps(course, indent=2, ensure_ascii=False), encoding="utf-8")
    catalog_binary = catalog_path.read_bytes()
    catalog = {"id": "course-outline", "title": "Public course outline and access flags", "url": first_url, "category": "metadata", "retrieved_at": datetime.now(timezone.utc).isoformat(), "raw_path": catalog_path.relative_to(ROOT).as_posix(), "bytes": len(catalog_binary), "sha256": hashlib.sha256(catalog_binary).hexdigest(), "download_status": "downloaded", "conversion_status": "not_applicable", "conversion_method": "public-page-course-metadata", "notes": ["Extracted from the anonymous page's __NEXT_DATA__ JSON. This is catalog metadata, not notebook or assessment content."]}
    corpus.data["materials"].append(catalog)
    videos = [lesson for lesson in lessons.values() if lesson["type"] == "video"]
    def fetch(pair):
        lesson, url = pair
        try:
            return lesson, url, requests.get(url, timeout=(15, 40)), None
        except Exception as error:
            return lesson, url, None, error
    with ThreadPoolExecutor(max_workers=4) as workers:
        results = list(workers.map(fetch, [(lesson, hrefs[lesson["slug"]]) for lesson in videos]))
    transcripts = 0
    captions_total = 0
    for lesson, url, response, error in results:
        if error:
            corpus.record_gap(url, lesson["name"], "lessons", "Public page request failed: " + str(error))
            continue
        item = record_page(corpus, url, lesson, response, "lessons")
        try:
            props = page_props(response.content)
            if props.get("session") is not None:
                raise ValueError("Expected an anonymous response")
            captions = next((query["state"]["data"]["captions"] for query in props["trpcState"]["json"]["queries"] if query["queryKey"][0] == ["course", "getLessonVideoSubtitle"]), [])
            plain = props.get("captions", "").strip()
            if not plain:
                raise ValueError("The anonymous page contains no lesson transcript")
            if captions:
                caption_path = ROOT / "raw/transcripts" / (lesson["slug"] + ".json")
                caption_path.parent.mkdir(parents=True, exist_ok=True)
                caption_path.write_text(json.dumps(captions, indent=2, ensure_ascii=False), encoding="utf-8")
                binary = caption_path.read_bytes()
                item["assets"] = [{"url": url + "#transcript", "raw_path": caption_path.relative_to(ROOT).as_posix(), "bytes": len(binary), "sha256": hashlib.sha256(binary).hexdigest()}]
                body = "\n\n".join(f"[{int(cue['startInSeconds'] // 60):02d}:{int(cue['startInSeconds'] % 60):02d}] {cue['text']}" for cue in captions)
                normalize = lambda text: " ".join(text.split())
                item["plain_caption_matches_timed_cues"] = normalize(plain) == normalize(" ".join(cue["text"] for cue in captions))
                item["caption_cues"] = len(captions)
                captions_total += len(captions)
            else:
                body = plain
            item.update(conversion_status="converted", conversion_method="anonymous-public-page-transcript", anonymous_source=True, transcript_words=len(plain.split()))
            item["notes"] = ["Complete transcript supplied in the public anonymous lesson HTML (__NEXT_DATA__). Original HTML and timed caption JSON are preserved. Video media was not downloaded."]
            corpus.write_markdown(item, body)
            transcripts += 1
            page = BeautifulSoup(response.content, "html.parser")
            for anchor in page.select("a[href]"):
                href = urljoin(url, anchor["href"])
                if href.startswith(COURSE + "/lesson/"):
                    hrefs[href.split("/lesson/", 1)[1].split("/", 1)[0]] = href
        except Exception as problem:
            item["conversion_status"] = "failed"
            item["notes"].append(str(problem))
        corpus.save()
    # Browser inspection confirms that non-video content opens a login modal.
    remaining = [lesson for lesson in lessons.values() if lesson["type"] in ("reading_material", "notebook")]
    with ThreadPoolExecutor(max_workers=4) as workers:
        results = list(workers.map(fetch, [(lesson, hrefs[lesson["slug"]]) for lesson in remaining]))
    for lesson, url, response, error in results:
        if error:
            corpus.record_gap(url, lesson["name"], "restricted", "Anonymous viewer request failed: " + str(error))
            continue
        item = record_page(corpus, url, lesson, response, "restricted")
        item.update(download_status="requires_login", conversion_status="not_available")
        item["notes"] = ["The anonymous browser opens 'Log In to Continue'. The saved HTML is a viewer/catalog shell and is not represented as lesson text or notebook code. No account was used or created."]
        corpus.save()
    for lesson in lessons.values():
        if lesson["type"] not in ("graded_notebook", "quiz"):
            continue
        url = hrefs.get(lesson["slug"], COURSE + "/lesson/" + lesson["slug"])
        item = corpus.record_gap(url, lesson["name"], "restricted", "The public course catalog marks this item locked with requiredUserTier=pro. Subscription-only assessment content was not requested.", "requires_subscription")
        item.update(lesson_type=lesson["type"], access_control=lesson.get("accessControl"), required_user_tier=lesson.get("requiredUserTier"), source_catalog=catalog["raw_path"])
    # The landing page contains several article cards; archive its whole main content.
    main_content = course_page.select_one("main") or course_page.body
    for element in main_content.select("script, style, nav, footer, noscript, svg"):
        element.decompose()
    for anchor in main_content.select("a[href]"):
        anchor["href"] = urljoin(corpus.data["source_url"], anchor["href"])
    for image in main_content.select("img"):
        source = image.get("src") or image.get("data-src")
        if not source or source.startswith("data:"):
            continue
        source_url = urljoin(corpus.data["source_url"], source)
        response = corpus.request(source_url)
        if response.ok and response.headers.get("Content-Type", "").startswith("image/"):
            mime = response.headers["Content-Type"].split(";", 1)[0]
            extension = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp", "image/svg+xml": ".svg"}.get(mime, ".bin")
            dest = ROOT / "raw/assets" / (hashlib.sha256(source_url.encode()).hexdigest()[:16] + extension)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(response.content)
            image["src"] = "@@ROOT@@/" + dest.relative_to(ROOT).as_posix()
        else:
            image["src"] = source_url
    old_id = course_item["id"]
    course_item["id"] = old_id.removeprefix("pages/")
    corpus.write_markdown(course_item, markdownify(str(main_content), heading_style="ATX", bullets="-"))
    course_item["id"] = old_id
    corpus.data["notes"].extend([
        f"All {transcripts} public video transcripts were captured from anonymous server-rendered lesson HTML, including timed captions where supplied. No video binaries were downloaded.",
        "The remaining eight readings and six ungraded notebook labs require login in the anonymous browser. Five graded notebook labs and five quizzes are marked Pro-only in the public catalog. These are recorded as access gaps, not converted from generic help or sign-in text.",
        "No separate official public repository for this specific November 2026 course was found in targeted title/provider searches. The older 'Evaluating AI Agents' course was not substituted.",
    ])
    for item in corpus.data["materials"]:
        if not item["id"].startswith(item["category"] + "/"):
            item["id"] = item["category"] + "/" + item["id"]
    corpus.finalize()
    contents = ["# Course contents", "", "[Course index](README.md) · [Access gaps](GAPS.md)", "", "## Module slide decks", ""]
    for item in corpus.data["materials"]:
        if item["category"] == "slides" and item.get("markdown_path"):
            contents.append(f"- [{item['title']}]({item['markdown_path']})")
    contents += ["", "## Public video transcripts", ""]
    for lesson in sorted(videos, key=lambda lesson: lesson["index"]):
        item = next((item for item in corpus.data["materials"] if item["url"] == hrefs[lesson["slug"]] and item["category"] == "lessons"), None)
        if item and item.get("markdown_path"):
            contents.append(f"- [{item['title']}]({item['markdown_path']})")
    (ROOT / "CONTENTS.md").write_text("\n".join(contents) + "\n", encoding="utf-8")
    readme = ROOT / "README.md"
    readme.write_text(readme.read_text(encoding="utf-8").replace("[Manifest](manifest.json)", "[Course contents](CONTENTS.md) · [Manifest](manifest.json)", 1), encoding="utf-8")
    coverage_path = ROOT / "coverage.json"
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    coverage.update(catalog_lessons=len(lessons), video_lessons=len(videos), public_transcripts=transcripts, timed_caption_cues=captions_total, login_only_readings=8, login_only_ungraded_labs=6, pro_graded_labs=5, pro_quizzes=5, lesson_urls_missing_from_public_navigation=[lesson["slug"] for lesson in lessons.values() if lesson["slug"] not in hrefs])
    coverage_path.write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(coverage, indent=2), flush=True)


if __name__ == "__main__":
    main()
