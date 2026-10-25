"""No request in the pipeline impersonates a browser; every fetch identifies itself."""

from __future__ import annotations

from pathlib import Path

import httpx

from nhl_edge.data import http as H

SRC = Path(__file__).resolve().parents[1] / "src"


def test_no_source_file_carries_a_browser_user_agent():
    offenders = [str(p.relative_to(SRC)) for p in SRC.rglob("*.py") if "Mozilla/" in p.read_text() or "BROWSER_HEADERS" in p.read_text()]
    assert offenders == []


def test_every_fetch_sends_the_identifying_user_agent():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["ua"] = request.headers["user-agent"]
        return httpx.Response(200, content=b"{}")
    H.fetch("https://example.invalid/x", transport=httpx.MockTransport(handler), max_retries=0)
    assert seen["ua"].startswith("nhl-edge-finder/") and "Mozilla" not in seen["ua"]
