"""Recognize access responses that must not be presented as source content."""

from urllib.parse import urlsplit


def access_page_reason(url: str, title: str = "", text: str = "") -> str | None:
    parsed = urlsplit(url)
    path = parsed.path.rstrip("/").lower()
    host = parsed.netloc.lower()
    if host.endswith("openreview.net") and path == "/challenge":
        return "OpenReview returned a browser-verification challenge, not the paper page."
    normalized_title = " ".join(title.lower().split())
    titles = {
        "just a moment...", "just a moment", "verifying your browser",
        "access denied", "attention required! | cloudflare", "security verification",
        "checking your browser - recaptcha",
    }
    if normalized_title in titles:
        return "The response title identifies an access or browser-verification page."
    if len(text) < 5000:
        normalized = " ".join(text.lower().split())
        if "complete the check below to continue to openreview" in normalized:
            return "The response asks for OpenReview browser verification instead of showing the paper."
        if "enable javascript and cookies to continue" in normalized:
            return "The response is a browser-verification page."
        if "cookies must be enabled" in normalized and "reload this page to continue" in normalized:
            return "The response is a cookie-verification page instead of the requested content."
    return None
