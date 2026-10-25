"""Source audit: robots evaluation, policy-link discovery, and that a refusal is recorded rather than worked around."""

from __future__ import annotations

from nhl_edge.research import source_audit as A

ROBOTS = "User-agent: *\nDisallow: /private/\nDisallow: /teams/\nCrawl-delay: 5\n\nUser-agent: nhl-edge-finder\nAllow: /teams/boston-bruins/\n"


def test_robots_verdict_is_evaluated_for_our_token_and_for_star():
    v = A.robots_verdict(ROBOTS, "nhl-edge-finder/0.1 (+x)", "https://h.example", ["/teams/boston-bruins/line-combinations", "/teams/other", "/open"])
    p = v["paths"]
    assert p["/teams/boston-bruins/line-combinations"] == {"allowed_for_us": True, "allowed_for_star": False}
    assert p["/teams/other"] == {"allowed_for_us": True, "allowed_for_star": False}            # a named group replaces the * group for that agent
    assert p["/open"]["allowed_for_star"] is True
    assert v["disallows_all_for_star"] is False and v["crawl_delay_for_us"] is not None
    assert A.robots_verdict(None, "x/1", "https://h.example", ["/a"]) == {"available": False}
    assert A.robots_verdict("User-agent: *\nDisallow: /\n", "x/1", "https://h.example", ["/a"])["disallows_all_for_star"] is True


def test_policy_links_and_keyword_hits():
    html = '<a href="/terms-of-service">Terms</a><a href="https://other.example/terms">x</a><a href="/about">a</a><a href="/privacy">p</a>'
    assert A.policy_links(html, "https://www.h.example") == ["https://www.h.example/terms-of-service", "https://www.h.example/privacy"]
    txt = A.strip_html("<script>var x=1</script><p>You may not use any robot, spider or scraper; commercial redistribution is prohibited.</p>")
    ks = {h["keyword"] for h in A.keyword_hits(txt)}
    assert {"robot", "spider", "scrap", "commercial", "redistribut", "prohibit"} <= ks and "var x" not in txt


def test_a_refusal_is_recorded_not_retried_or_worked_around():
    calls = []

    def get(url):
        calls.append(url)
        if url.endswith("robots.txt"):
            return 200, ROBOTS.encode(), {}
        if "line-combinations" in url:
            return 403, b"Access denied for this client", {"server": "cloudflare"}
        return 200, b"<html><a href='/terms'>t</a>", {"content-type": "text/html"}
    t = A.Target("h", "https://www.h.example", ["/teams/boston-bruins/line-combinations"], extra_policy_urls=[])
    r = A.audit_target(t, get, "nhl-edge-finder/0.1", pause_s=0)
    probe = r["probes"][0]
    assert probe["status"] == 403 and "Access denied" in probe["refusal_excerpt"] and probe["server"] == "cloudflare"
    assert calls.count("https://www.h.example/teams/boston-bruins/line-combinations") == 1          # exactly one request, no second attempt with other headers
    md = A.render({"run_utc": "2026-10-25T00:00:00Z", "user_agent": "u", "targets": [r]})
    assert "HTTP 403" in md and "no browser impersonation" in md


def test_the_audit_uses_the_identifying_user_agent_by_default(monkeypatch):
    seen = {}
    monkeypatch.setattr(A.httpx, "get", lambda url, headers, **k: seen.setdefault("ua", headers["User-Agent"]) and type("R", (), {"status_code": 200, "content": b"", "headers": {}})())
    A.http_get("https://x.example/robots.txt")
    assert seen["ua"].startswith("nhl-edge-finder/") and "Mozilla" not in seen["ua"]


def test_production_path_probe_uses_the_pipelines_fetch_with_html_accept_and_reports_parsing():
    class R:
        status = 200
        content = b"<html><script id=\"__NEXT_DATA__\" type=\"application/json\">{\"props\": {\"pageProps\": {\"combinations\": {\"players\": []}}}}</script></html>"

        def text(self):
            return self.content.decode()
    seen = []

    def fake_fetch(url, headers=None, max_retries=None):
        seen.append(headers)
        return R()
    out = A.production_path_probe(fake_fetch)
    assert [o["feed"] for o in out] == ["lines", "goalies"] and all(o["status"] == 200 for o in out)
    assert all("text/html" in h["Accept"] and "User-Agent" not in h for h in seen)               # content negotiation only; the identifying User-Agent comes from fetch()
