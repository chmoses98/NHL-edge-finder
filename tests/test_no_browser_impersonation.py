"""No request in the pipeline impersonates a browser; every fetch identifies itself."""

from __future__ import annotations

from pathlib import Path

import httpx

from nhl_edge.data import http as H

ROOT = Path(__file__).resolve().parents[1]


def test_no_code_or_workflow_in_the_repository_carries_a_browser_user_agent():
    """Whole repository (source, research code, scripts, workflows); docs and this file are exempt because they discuss the removed header."""
    offenders = []
    for pat in ("src/**/*.py", "research/**/*.py", "scripts/**/*.py", "tests/**/*.py", ".github/**/*.yml"):
        for p in ROOT.glob(pat):
            if p.name == Path(__file__).name or "__pycache__" in p.parts:
                continue
            t = p.read_text()
            if "Mozilla/" in t or "BROWSER_HEADERS" in t:
                offenders.append(str(p.relative_to(ROOT)))
    assert offenders == []


def test_a_caller_cannot_override_the_user_agent():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["ua"] = request.headers["user-agent"]
        seen["accept"] = request.headers["accept"]
        return httpx.Response(200, content=b"{}")
    H.fetch("https://example.invalid/x", headers={"User-Agent": "Mozilla/5.0", "user-agent": "Chrome", "Accept": "*/*"}, transport=httpx.MockTransport(handler), max_retries=0)
    assert seen["ua"].startswith("nhl-edge-finder/") and seen["accept"] == "*/*"                 # Accept is negotiable; the User-Agent is not


def test_call_sites_send_the_identifying_user_agent_and_the_right_accept(monkeypatch):
    calls = []

    def spy(url, **kw):
        calls.append((url, kw.get("headers")))
        raise H.FetchError("stop")
    import nhl_edge.data.goalies as G
    import nhl_edge.data.history as Y
    monkeypatch.setattr(G, "fetch", spy)
    monkeypatch.setattr(Y, "fetch", spy)
    G.fetch_dailyfaceoff("2026-10-25")
    try:
        Y.fetch_bytes("https://example.invalid/f.csv", 5.0)
    except H.FetchError:
        pass
    assert calls[0][1] == H.HTML_HEADERS and calls[1][1] == H.ANY_HEADERS
    assert all("User-Agent" not in (h or {}) for _, h in calls)


def test_projection_foundation_capture_uses_html_accept_and_no_browser_header():
    import importlib.util

    spec = importlib.util.spec_from_file_location("pf_fetch_src", ROOT / "research/projection_foundation/nhl/live/fetch.py")
    text = (ROOT / "research/projection_foundation/nhl/live/fetch.py").read_text()
    assert spec is not None and "HTML_HEADERS" in text and "Mozilla" not in text and "BROWSER_HEADERS" not in text


def test_every_fetch_sends_the_identifying_user_agent():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["ua"] = request.headers["user-agent"]
        return httpx.Response(200, content=b"{}")
    H.fetch("https://example.invalid/x", transport=httpx.MockTransport(handler), max_retries=0)
    assert seen["ua"].startswith("nhl-edge-finder/") and "Mozilla" not in seen["ua"]


def test_html_pages_are_requested_with_an_html_accept_not_json():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["accept"] = request.headers["accept"]
        return httpx.Response(200, content=b"<html></html>")
    H.fetch("https://example.invalid/x", headers=H.HTML_HEADERS, transport=httpx.MockTransport(handler), max_retries=0)
    assert seen["accept"].startswith("text/html")
    import nhl_edge.data.context as C
    import nhl_edge.data.goalies as G
    import nhl_edge.data.history as Y
    assert C.HTML_HEADERS is G.HTML_HEADERS is H.HTML_HEADERS and Y.ANY_HEADERS is H.ANY_HEADERS
