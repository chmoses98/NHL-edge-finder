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


SCOPE_KEYWORDS = ("application programming", " api", "apis", "data feed", "services", "the site", "scrap", "automated", "robot", "spider", "commercial", "personal", "non-commercial", "internal",
                  "redistribut", "republish", "derivative", "database", "compil", "written consent", "permission", "license", "licence", "statistic")


def passages(text: str, keywords: tuple[str, ...] = SCOPE_KEYWORDS, width: int = 420, max_n: int = 60) -> list[dict[str, str]]:
    """Distinct passages of a policy text around each occurrence of a scope-related keyword (overlapping hits merged), in document order, so a human can read how the terms define their scope."""
    low, spans = text.lower(), []
    for k in keywords:
        i = low.find(k)
        while i >= 0:
            spans.append((max(0, i - width // 3), min(len(text), i + width), k))
            i = low.find(k, i + width)
    spans.sort()
    out, last_end = [], -1
    for a, b, k in spans:
        if a <= last_end:
            continue
        out.append({"keyword": k, "text": text[a:b].strip()})
        last_end = b
        if len(out) >= max_n:
            break
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


CONTACT_LINK_RE = re.compile(r'href="([^"#]*?(?:contact|about|advertis|partner|licens|press|media|support|help|feedback|data|api)[^"#]*)"', re.I)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
MAILTO_RE = re.compile(r'mailto:([^"?]+)', re.I)


def contact_discovery(get: Getter, base: str, pause_s: float = 1.0, max_pages: int = 6) -> dict[str, Any]:
    """Publicly listed contact channels of a site: mailto links and addresses in the text of its home page and of the contact / about / advertising / licensing / partner pages it links.
    One GET per page. Only what the site itself publishes is recorded; nothing is guessed (no addresses are constructed from names or patterns)."""
    status, body, _ = get(base)
    html = body[:600_000].decode("utf-8", "replace") if status == 200 else ""
    links = list(dict.fromkeys(urljoin(base, m.group(1)) for m in CONTACT_LINK_RE.finditer(html)))
    host = urlparse(base).netloc.split(":")[0].removeprefix("www.")
    links = [u for u in links if urlparse(u).netloc.split(":")[0].removeprefix("www.").endswith(host)][:max_pages]
    found: dict[str, list[str]] = {}
    pages = [{"url": base, "status": status}]
    for url, text in [(base, html)] + [(u, None) for u in links]:
        if text is None:
            time.sleep(pause_s)
            st, b, _ = get(url)
            pages.append({"url": url, "status": st})
            text = b[:600_000].decode("utf-8", "replace") if st == 200 else ""
        for e in set(MAILTO_RE.findall(text)) | set(EMAIL_RE.findall(strip_html(text))):
            e = e.strip().lower()
            if not e.endswith((".png", ".jpg", ".svg", ".gif", ".webp")):
                found.setdefault(e, []).append(url)
    return {"base": base, "pages": pages, "contact_links": links, "emails": {e: sorted(set(u)) for e, u in sorted(found.items())}}


def production_path_probe(fetch_fn: Callable[..., Any] | None = None) -> list[dict[str, Any]]:
    """The same DailyFaceoff requests the pipeline makes, through the pipeline's own ``fetch`` (its headers, its parsers): does the production code path still get usable pages?"""
    from nhl_edge.data.goalies import extract_next_data
    from nhl_edge.data.http import HTML_HEADERS, FetchError
    from nhl_edge.data.http import fetch as real_fetch
    from nhl_edge.data.lines import parse_line_page

    f = fetch_fn or real_fetch
    day = datetime.now(UTC).strftime("%Y-%m-%d")
    out = []
    for name, url in (("lines", "https://www.dailyfaceoff.com/teams/boston-bruins/line-combinations"), ("goalies", f"https://www.dailyfaceoff.com/starting-goalies/{day}")):
        try:
            r = f(url, headers=HTML_HEADERS, max_retries=0)
            parsed = parse_line_page(r.content) is not None if name == "lines" else bool(extract_next_data(r.text()).get("props"))
            out.append({"feed": name, "url": url, "status": r.status, "bytes": len(r.content), "parsed_by_production_parser": parsed})
        except (FetchError, ValueError, KeyError) as e:
            out.append({"feed": name, "url": url, "status": None, "error": str(e)[:200], "parsed_by_production_parser": False})
    return out


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
    if rep.get("production_path"):
        L += ["## Production code path (the pipeline's own fetch + parsers)"]
        for p in rep["production_path"]:
            L.append(f"- {p['feed']}: HTTP {p['status']}, {p.get('bytes')} B, parsed by the production parser: **{p['parsed_by_production_parser']}**" + (f" — {p['error']}" if p.get("error") else ""))
        L.append("")
    for ex in rep.get("excerpts") or []:
        L += [f"## Scope-related passages: {ex['url']} (HTTP {ex['status']}, {ex['chars']} bytes)"]
        L += [f"- [{p['keyword']}] {p['text']}" for p in ex["passages"]] or ["- (none read)"]
        L.append("")
    for c in rep.get("contacts") or []:
        L += [f"## Publicly listed contact channels: {c['base']}", "- pages read: " + ", ".join(f"{p['url']} ({p['status']})" for p in c["pages"])]
        L += [f"- `{e}` (listed on: {', '.join(u)})" for e, u in c["emails"].items()] or ["- no email address listed on the pages read"]
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
    ap.add_argument("--excerpts", nargs="*", default=None, help="policy page URLs whose scope-related passages are printed")
    ap.add_argument("--contacts", nargs="*", default=None, help="base URLs whose publicly listed contact channels are collected")
    ap.add_argument("--production-path", action="store_true", help="also run the pipeline's own DailyFaceoff fetch + parsers once")
    a = ap.parse_args(argv)
    rep = run(probe=not a.no_probe)
    if a.production_path:
        rep["production_path"] = production_path_probe()
    if a.excerpts:
        rep["excerpts"] = []
        for u in a.excerpts:
            st, b, _ = http_get(u, rep["user_agent"])
            rep["excerpts"].append({"url": u, "status": st, "chars": len(b), "passages": passages(strip_html(b[:900_000].decode("utf-8", "replace"))) if st == 200 else []})
    if a.contacts:
        rep["contacts"] = [contact_discovery(lambda u: http_get(u, rep["user_agent"]), b) for b in a.contacts]
    Path(a.out).write_text(json.dumps(rep, indent=1))
    md = render(rep)
    if a.md:
        Path(a.md).write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
