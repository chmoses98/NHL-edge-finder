"""Probe the free sources PLAYER_SIM_V1 may use for live deployment (lines, PP units) and save raw samples as parser
fixtures. RESEARCH_ONLY; runs on a GitHub runner (the dev container reaches none of these hosts).

usage: python scripts/probe_player_sources.py --out docs/probe/samples/player_sources
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from nhl_edge.data.http import BROWSER_HEADERS, FetchError, fetch

DFO_TEAMS = ("edmonton-oilers", "boston-bruins", "vegas-golden-knights")
KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
STATS = "https://api.nhle.com/stats/rest/en"
TARGETS = {
    **{f"dfo_lines_{t}": (f"https://www.dailyfaceoff.com/teams/{t}/line-combinations", True) for t in DFO_TEAMS},
    **{f"kalshi_series_{s}": (f"{KALSHI}/series/{s}", False) for s in ("KXNHLPTS", "KXNHLGOAL", "KXNHLAST", "KXNHLSAVE", "KXNHLFIRSTGOAL")},
    "kalshi_markets_KXNHLPTS_settled": (f"{KALSHI}/markets?series_ticker=KXNHLPTS&status=settled&limit=20", False),
    "kalshi_markets_KXNHLSAVE_settled": (f"{KALSHI}/markets?series_ticker=KXNHLSAVE&status=settled&limit=20", False),
    "nhl_stats_skater_timeonice_game": (f"{STATS}/skater/timeonice?isAggregate=false&isGame=true&start=0&limit=5&cayenneExp=seasonId=20252026%20and%20gameTypeId=2", False),
    "nhl_stats_skater_summary_game": (f"{STATS}/skater/summary?isAggregate=false&isGame=true&start=0&limit=5&cayenneExp=seasonId=20252026%20and%20gameTypeId=2", False),
    "rotowire_nhl_lineups": ("https://www.rotowire.com/hockey/nhl-lineups.php", True),
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="docs/probe/samples/player_sources")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    report = {}
    for name, (url, browser) in TARGETS.items():
        try:
            f = fetch(url, headers=BROWSER_HEADERS if browser else None, timeout=60, max_retries=2)
        except FetchError as e:
            report[name] = {"url": url, "error": str(e)[:300]}
            continue
        body = f.content
        ext = "html" if b"<html" in body[:2000].lower() else "json"
        (out / f"{name}.{ext}").write_bytes(body[:3_000_000])
        rec = {"url": url, "status": f.status, "bytes": len(body), "fetched_at_utc": f.fetched_at_utc}
        if ext == "html":
            m = re.search(rb'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', body, re.S)
            if m:
                (out / f"{name}.next_data.json").write_bytes(m.group(1))
                try:
                    nd = json.loads(m.group(1))
                    rec["next_data_keys"] = list(((nd.get("props") or {}).get("pageProps") or {}).keys())[:40]
                except json.JSONDecodeError:
                    rec["next_data_keys"] = "undecodable"
        report[name] = rec
    (out / "PROBE.json").write_text(json.dumps(report, indent=1))
    print(json.dumps(report, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
