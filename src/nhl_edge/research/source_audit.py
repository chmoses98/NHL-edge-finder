"""Data-source access and terms audit (RESEARCH_ONLY, read-only, identifying User-Agent, one GET per document).

For each external host the pipeline reads, record what the host itself says about automated access -- ``robots.txt`` (evaluated for our own User-Agent and for ``*``, for the exact paths we fetch),
the pages it links as terms / privacy / licence / API policy (text excerpts and keyword hits) -- and whether a plain, identifying request to the paths we use is answered. Nothing is bypassed:
a refusal is recorded as a refusal. The output is evidence for a human decision; it is not a legal opinion.

    python -m nhl_edge.research.source_audit --out out/source_audit.json --md out/source_audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.robotparser
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import httpx

from nhl_edge.config import settings

POLICY_LINK_RE = re.compile(r'href="([^"#]*?(?:terms|tos|privacy|legal|licen[sc]e|conditions|copyright|api-?policy|data-?use)[^"#]*)"', re.I)
KEYWORDS = ("scrap", "robot", "spider", "crawl", "automated", "bot", "data mining", "commercial", "redistribut", "republish", "reproduc", "license", "licence", "api", "personal use",
            "non-commercial", "noncommercial", "prohibit", "permission", "written consent", "user-agent", "rate limit")


@dataclass
class Target:
    name: str
    base: str
    paths: list[str]                        # the exact paths the pipeline fetches (or would)
    home: str = "/"
    extra_policy_urls: list[str] = field(default_factory=list)


TARGETS = [
    Target("dailyfaceoff", "https://www.dailyfaceoff.com", ["/teams/boston-bruins/line-combinations", "/starting-goalies/2026-10-25"], extra_policy_urls=["/terms-of-service", "/privacy-policy"]),
    Target("nhl-api-web", "https://api-web.nhle.com", ["/v1/schedule/now", "/v1/gamecenter/2026020180/landing", "/v1/gamecenter/2026020180/right-rail"]),
    Target("nhl-stats-rest", "https://api.nhle.com", ["/stats/rest/en/team"]),
    Target("nhl.com", "https://www.nhl.com", ["/scores/htmlreports/20262027/RO020180.HTM"], extra_policy_urls=["/info/terms-of-service", "/info/terms-of-use", "/info/privacy-policy"]),
    Target("moneypuck", "https://moneypuck.com", ["/data.htm"], home="/data.htm"),
    Target("espn-site-api", "https://site.api.espn.com", ["/apis/site/v2/sports/hockey/nhl/injuries"]),
]

Getter = Callable[[str], tuple[int, bytes, dict[str, str]]]


def http_get(url: str, user_agent: str | None = None, timeout: float = 25.0) -> tuple[int, bytes, dict[str, str]]:
    ua = user_agent or settings().user_agent
    try:
        r = httpx.get(url, headers={"User-Agent": ua, "Accept": "*/*"}, timeout=timeout, follow_redirects=True)
        return r.status_code, r.content, {k.lower(): v for k, v in r.headers.items()}
    except httpx.HTTPError as e:
        return 0, f"{type(e).__name__}: {e}".encode()[:300], {}


def robots_verdict(robots_text: str | None, user_agent: str, base: str, paths: list[str]) -> dict[str, Any]:
    """Evaluate robots.txt for our User-Agent token and for ``*`` on the exact paths. ``None`` text = no robots.txt could be read (nothing is assumed)."""
    if robots_text is None:
        return {"available": False}
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(robots_text.splitlines())
    token = user_agent.split("/")[0]
    return {"available": True, "crawl_delay_for_us": rp.crawl_delay(token) or rp.crawl_delay("*"), "request_rate": str(rp.request_rate(token) or rp.request_rate("*")),
            "paths": {p: {"allowed_for_us": rp.can_fetch(token, urljoin(base, p)), "allowed_for_star": rp.can_fetch("*", urljoin(base, p))} for p in paths},
            "disallows_all_for_star": not rp.can_fetch("*", urljoin(base, "/"))}


def policy_links(html: str, base: str) -> list[str]:
    seen, out = set(), []
    for m in POLICY_LINK_RE.finditer(html):
        u = urljoin(base, m.group(1))
        if urlparse(u).netloc.split(":")[0].endswith(urlparse(base).netloc.split(":")[0].split(".", 1)[-1]) and u not in seen:
            seen.add(u)
            out.append(u)
    return out[:6]


def strip_html(html: str) -> str:
    html = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", html)).strip()


def keyword_hits(text: str, width: int = 140) -> list[dict[str, str]]:
    low, out = text.lower(), []
    for k in KEYWORDS:
        i = low.find(k)
        if i >= 0:
            out.append({"keyword": k, "context": text[max(0, i - width // 2): i + width].strip()})
    return out


def probe_path(get: Getter, base: str, path: str) -> dict[str, Any]:
    status, body, hdr = get(urljoin(base, path))
    txt = body[:200_000].decode("utf-8", "replace")
    return {"path": path, "status": status, "content_type": hdr.get("content-type"), "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()[:16],
            "has_next_data": "__NEXT_DATA__" in txt, "server": hdr.get("server"), "retry_after": hdr.get("retry-after"),
            "refusal_excerpt": txt[:200] if status in (401, 403, 429, 451) or status == 0 else None}


def audit_target(t: Target, get: Getter, user_agent: str, pause_s: float = 1.0, probe: bool = True) -> dict[str, Any]:
    rec: dict[str, Any] = {"name": t.name, "base": t.base}
    st, body, _ = get(urljoin(t.base, "/robots.txt"))
    robots = body.decode("utf-8", "replace") if st == 200 else None
    rec["robots_status"] = st
    rec["robots_excerpt"] = (robots or "")[:1500]
    rec["robots"] = robots_verdict(robots, user_agent, t.base, t.paths)
    time.sleep(pause_s)
    st, body, _ = get(urljoin(t.base, t.home))
    html = body[:400_000].decode("utf-8", "replace") if st == 200 else ""
    urls = policy_links(html, t.base) + [urljoin(t.base, p) for p in t.extra_policy_urls]
    pol = []
    for u in list(dict.fromkeys(urls))[:6]:
        time.sleep(pause_s)
        s, b, h = get(u)
        text = strip_html(b[:600_000].decode("utf-8", "replace")) if s == 200 else ""
        pol.append({"url": u, "status": s, "chars": len(text), "hits": keyword_hits(text) if text else [], "excerpt": text[:600]})
    rec["home_status"] = st
    rec["policy_pages"] = pol
    rec["probes"] = []
    if probe:
        for p in t.paths:
            time.sleep(pause_s)
            rec["probes"].append(probe_path(get, t.base, p))
    return rec


def render(rep: dict[str, Any]) -> str:
    L = [f"# Data-source access and terms audit ({rep['run_utc']})", "", f"User-Agent used: `{rep['user_agent']}` (identifying; no browser impersonation). One GET per document; a refusal is recorded, never bypassed.", ""]
    for r in rep["targets"]:
        rb = r["robots"]
        L += [f"## {r['name']} ({r['base']})", f"- robots.txt: HTTP {r['robots_status']}" + ("" if not rb.get("available") else f"; disallows everything for `*`: {rb['disallows_all_for_star']}; crawl-delay for us: {rb['crawl_delay_for_us']}")]
        for p, v in (rb.get("paths") or {}).items():
            L.append(f"  - `{p}`: allowed for us **{v['allowed_for_us']}**, for `*` {v['allowed_for_star']}")
        for p in r["probes"]:
            L.append(f"- probe `{p['path']}`: HTTP {p['status']} ({p['content_type']}, {p['bytes']} B)" + (f"; embedded page data present: {p['has_next_data']}" if p["has_next_data"] else "") + (f"; refusal: {p['refusal_excerpt']!r}" if p["refusal_excerpt"] else ""))
        for pg in r["policy_pages"]:
            L.append(f"- policy page {pg['url']}: HTTP {pg['status']}, {pg['chars']} chars; keywords: {', '.join(h['keyword'] for h in pg['hits']) or 'none'}")
            for h in pg["hits"][:8]:
                L.append(f"  - *{h['keyword']}*: …{h['context']}…")
        L.append("")
    L.append("Evidence only; reading and applying the terms is a decision for the owner.")
    return "\n".join(L) + "\n"


def run(get: Getter | None = None, targets: list[Target] | None = None, user_agent: str | None = None, pause_s: float = 1.0, probe: bool = True) -> dict[str, Any]:
    ua = user_agent or settings().user_agent
    g = get or (lambda u: http_get(u, ua))
    return {"run_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"), "user_agent": ua, "targets": [audit_target(t, g, ua, pause_s, probe) for t in (targets or TARGETS)]}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.source_audit")
    ap.add_argument("--out", required=True)
    ap.add_argument("--md")
    ap.add_argument("--no-probe", action="store_true")
    a = ap.parse_args(argv)
    rep = run(probe=not a.no_probe)
    Path(a.out).write_text(json.dumps(rep, indent=1))
    md = render(rep)
    if a.md:
        Path(a.md).write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
