#!/usr/bin/env python3
"""Probe every candidate data source from wherever this runs and record exactly what came back.

Stdlib only, on purpose: this must run before ``pip install`` and must never depend on parsers that
might be wrong. It writes ``probe_results.json`` (one row per URL: status, latency, size, content
type, top-level keys / CSV header) and trimmed ``samples/<name>.json`` so parsers can be written
against the REAL shape rather than a remembered one.

Usage: python scripts/probe_sources.py OUT_DIR [--date YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

UA = "nhl-edge-finder-probe/0.1 (+https://github.com/chmoses98/NHL-edge-finder)"
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def probes(date: str, kalshi_hosts: list[str]) -> list[dict]:
    season_prev = "20252026"
    season_cur = "20262027"
    p: list[dict] = [
        # ---- official NHL api-web -------------------------------------------------------------
        {"name": "nhl_schedule_date", "url": f"https://api-web.nhle.com/v1/schedule/{date}", "sample": True},
        {"name": "nhl_schedule_now", "url": "https://api-web.nhle.com/v1/schedule/now", "sample": True},
        {"name": "nhl_score_now", "url": "https://api-web.nhle.com/v1/score/now", "sample": True},
        {"name": "nhl_score_date", "url": f"https://api-web.nhle.com/v1/score/{date}", "sample": True},
        {"name": "nhl_standings_now", "url": "https://api-web.nhle.com/v1/standings/now", "sample": True},
        {"name": "nhl_roster_tor", "url": "https://api-web.nhle.com/v1/roster/TOR/current", "sample": True},
        {"name": "nhl_club_schedule_tor", "url": "https://api-web.nhle.com/v1/club-schedule-season/TOR/now", "sample": True},
        {"name": "nhl_club_schedule_tor_2025", "url": "https://api-web.nhle.com/v1/club-schedule-season/TOR/20252026", "sample": True},
        {"name": "nhl_club_stats_tor", "url": "https://api-web.nhle.com/v1/club-stats/TOR/now", "sample": True},
        {"name": "nhl_boxscore_final_2025", "url": "https://api-web.nhle.com/v1/gamecenter/2025020001/boxscore", "sample": True},
        {"name": "nhl_landing_final_2025", "url": "https://api-web.nhle.com/v1/gamecenter/2025020001/landing", "sample": True},
        {"name": "nhl_pbp_final_2025", "url": "https://api-web.nhle.com/v1/gamecenter/2025020001/play-by-play", "sample": True},
        {"name": "nhl_right_rail_2025", "url": "https://api-web.nhle.com/v1/gamecenter/2025020001/right-rail", "sample": True},
        {"name": "nhl_boxscore_ot_sample", "url": "https://api-web.nhle.com/v1/gamecenter/2025020004/boxscore", "sample": True},
        {"name": "nhl_schedule_calendar", "url": f"https://api-web.nhle.com/v1/schedule-calendar/{date}", "sample": True},
        {"name": "nhl_season_list", "url": "https://api-web.nhle.com/v1/season", "sample": True},
        # ---- official NHL stats REST ----------------------------------------------------------
        {"name": "nhl_stats_team", "url": "https://api.nhle.com/stats/rest/en/team", "sample": True},
        {"name": "nhl_stats_team_summary_prev", "url": f"https://api.nhle.com/stats/rest/en/team/summary?limit=-1&cayenneExp=seasonId={season_prev}%20and%20gameTypeId=2", "sample": True},
        {"name": "nhl_stats_team_summary_cur", "url": f"https://api.nhle.com/stats/rest/en/team/summary?limit=-1&cayenneExp=seasonId={season_cur}%20and%20gameTypeId=2", "sample": True},
        {"name": "nhl_stats_goalie_summary_prev", "url": f"https://api.nhle.com/stats/rest/en/goalie/summary?limit=-1&cayenneExp=seasonId={season_prev}%20and%20gameTypeId=2", "sample": True},
        {"name": "nhl_stats_goalie_summary_cur", "url": f"https://api.nhle.com/stats/rest/en/goalie/summary?limit=-1&cayenneExp=seasonId={season_cur}%20and%20gameTypeId=2", "sample": True},
        {"name": "nhl_stats_season", "url": "https://api.nhle.com/stats/rest/en/season", "sample": True},
        {"name": "nhl_stats_game_prev", "url": f"https://api.nhle.com/stats/rest/en/game?cayenneExp=season={season_prev}%20and%20gameType=2&limit=5", "sample": True},
        # ---- MoneyPuck -----------------------------------------------------------------------
        {"name": "mp_teams_2025", "url": "https://moneypuck.com/moneypuck/playerData/seasonSummary/2025/regular/teams.csv", "sample": True},
        {"name": "mp_teams_2026", "url": "https://moneypuck.com/moneypuck/playerData/seasonSummary/2026/regular/teams.csv", "sample": True},
        {"name": "mp_goalies_2025", "url": "https://moneypuck.com/moneypuck/playerData/seasonSummary/2025/regular/goalies.csv", "sample": True},
        {"name": "mp_goalies_2026", "url": "https://moneypuck.com/moneypuck/playerData/seasonSummary/2026/regular/goalies.csv", "sample": True},
        {"name": "mp_skaters_2025", "url": "https://moneypuck.com/moneypuck/playerData/seasonSummary/2025/regular/skaters.csv", "sample": True, "max_bytes": 400_000},
        {"name": "mp_lines_2025", "url": "https://moneypuck.com/moneypuck/playerData/seasonSummary/2025/regular/lines.csv", "sample": True, "max_bytes": 400_000},
        {"name": "mp_all_teams_gbg", "url": "https://moneypuck.com/moneypuck/playerData/careers/gameByGame/all_teams.csv", "sample": True, "max_bytes": 600_000},
        {"name": "mp_team_gbg_tor", "url": "https://moneypuck.com/moneypuck/playerData/careers/gameByGame/regular/teams/TOR.csv", "sample": True, "max_bytes": 400_000},
        {"name": "mp_shots_2024_zip_head", "url": "https://moneypuck.com/data/shots/shots_2024.zip", "method": "HEAD"},
        {"name": "mp_shots_2025_zip_head", "url": "https://moneypuck.com/data/shots/shots_2025.zip", "method": "HEAD"},
        {"name": "mp_shots_pt_2024_head", "url": "https://peter-tanner.com/moneypuck/downloads/shots_2024.zip", "method": "HEAD"},
        {"name": "mp_shots_pt_2025_head", "url": "https://peter-tanner.com/moneypuck/downloads/shots_2025.zip", "method": "HEAD"},
        {"name": "mp_shots_pt_2007_2023_head", "url": "https://peter-tanner.com/moneypuck/downloads/shots_2007-2023.zip", "method": "HEAD"},
        {"name": "mp_predictions_page", "url": "https://moneypuck.com/predictions.htm", "max_bytes": 20_000, "ua": BROWSER_UA},
        # ---- optional enrichment / fallbacks ---------------------------------------------------
        {"name": "espn_nhl_scoreboard", "url": f"https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?dates={date.replace('-', '')}&limit=100", "sample": True},
        {"name": "espn_nhl_teams", "url": "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams?limit=50", "sample": True},
        {"name": "dailyfaceoff_goalies", "url": "https://www.dailyfaceoff.com/starting-goalies", "max_bytes": 30_000, "ua": BROWSER_UA},
        {"name": "dailyfaceoff_goalies_date", "url": f"https://www.dailyfaceoff.com/starting-goalies/{date}", "max_bytes": 30_000, "ua": BROWSER_UA},
        {"name": "rotowire_goalies", "url": "https://www.rotowire.com/hockey/nhl-lineups.php", "max_bytes": 30_000, "ua": BROWSER_UA},
        {"name": "nhl_injuries_espn", "url": "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/injuries", "sample": True},
    ]
    for host in kalshi_hosts:
        tag = host.split("//")[1].split(".")[0].replace("-", "_")
        base = f"{host}/trade-api/v2"
        p += [
            {"name": f"kalshi_{tag}_exchange_status", "url": f"{base}/exchange/status", "sample": True},
            {"name": f"kalshi_{tag}_series_sports", "url": f"{base}/series?category=Sports&limit=200&include_product_metadata=true", "sample": True, "max_bytes": 3_000_000, "kalshi_series_scan": True},
            {"name": f"kalshi_{tag}_series_kxnhlgame", "url": f"{base}/series/KXNHLGAME", "sample": True},
            {"name": f"kalshi_{tag}_markets_kxnhlgame_open", "url": f"{base}/markets?series_ticker=KXNHLGAME&status=open&limit=200", "sample": True},
            {"name": f"kalshi_{tag}_markets_kxnhlgame_unopened", "url": f"{base}/markets?series_ticker=KXNHLGAME&status=unopened&limit=200", "sample": True},
            {"name": f"kalshi_{tag}_markets_kxnhlgame_settled", "url": f"{base}/markets?series_ticker=KXNHLGAME&status=settled&limit=50", "sample": True},
            {"name": f"kalshi_{tag}_events_kxnhlgame", "url": f"{base}/events?series_ticker=KXNHLGAME&limit=50&with_nested_markets=true", "sample": True},
            {"name": f"kalshi_{tag}_markets_kxnhlspread_open", "url": f"{base}/markets?series_ticker=KXNHLSPREAD&status=open&limit=100", "sample": True},
            {"name": f"kalshi_{tag}_markets_kxnhltotal_open", "url": f"{base}/markets?series_ticker=KXNHLTOTAL&status=open&limit=100", "sample": True},
            {"name": f"kalshi_{tag}_filters_by_sport", "url": f"{base}/search/filters_by_sport", "sample": True},
        ]
    return p


def fetch(url: str, method: str = "GET", ua: str = UA, max_bytes: int = 5_000_000, timeout: float = 45.0) -> dict:
    req = urllib.request.Request(url, method=method, headers={"User-Agent": ua, "Accept": "application/json, text/csv, */*"})
    t0 = time.monotonic()
    row: dict = {"url": url, "method": method, "ok": False}
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(max_bytes + 1) if method != "HEAD" else b""
            row.update(status=r.status, content_type=r.headers.get("Content-Type"), content_length=r.headers.get("Content-Length"),
                       last_modified=r.headers.get("Last-Modified"), truncated=len(body) > max_bytes, ok=200 <= r.status < 300)
            body = body[:max_bytes]
    except urllib.error.HTTPError as e:
        body = b""
        try:
            body = e.read(2000)
        except Exception:  # noqa: BLE001
            pass
        row.update(status=e.code, error=f"HTTPError {e.code}", body_head=body[:300].decode("utf-8", "replace"))
    except Exception as e:  # noqa: BLE001
        body = b""
        row.update(status=None, error=f"{type(e).__name__}: {str(e)[:200]}")
    row["latency_ms"] = round((time.monotonic() - t0) * 1000)
    row["bytes"] = len(body)
    row["sha256"] = hashlib.sha256(body).hexdigest() if body else None
    row["_body"] = body
    return row


def describe(body: bytes, content_type: str | None) -> tuple[dict, object]:
    """(description, trimmed sample)."""
    text = body.decode("utf-8", "replace")
    stripped = text.lstrip()
    if stripped.startswith(("{", "[")):
        try:
            obj = json.loads(text)
        except json.JSONDecodeError as e:
            return {"kind": "json-invalid", "err": str(e)[:100]}, text[:2000]
        return {"kind": "json", "top_keys": list(obj.keys())[:40] if isinstance(obj, dict) else f"list[{len(obj)}]"}, trim(obj)
    if "csv" in (content_type or "") or "," in text[:500] and "\n" in text[:5000] and "<" not in text[:50]:
        rows = list(csv.reader(io.StringIO(text)))
        return {"kind": "csv", "header": rows[0][:80] if rows else [], "n_rows_in_sample": max(0, len(rows) - 1)}, rows[:6]
    if stripped[:15].lower().startswith(("<!doctype", "<html")):
        return {"kind": "html", "title": _title(text)}, text[:3000]
    return {"kind": "other"}, text[:1000]


def _title(html: str) -> str | None:
    i = html.lower().find("<title>")
    if i < 0:
        return None
    j = html.lower().find("</title>", i)
    return html[i + 7 : j][:200] if j > i else None


def trim(obj: object, depth: int = 0, max_list: int = 3) -> object:
    if isinstance(obj, dict):
        return {k: trim(v, depth + 1, max_list) for k, v in list(obj.items())[:60]}
    if isinstance(obj, list):
        return [trim(v, depth + 1, max_list) for v in obj[:max_list]] + ([f"... {len(obj) - max_list} more"] if len(obj) > max_list else [])
    if isinstance(obj, str):
        return obj[:300]
    return obj


def scan_series_for_nhl(body: bytes) -> dict:
    """List every series whose ticker/title/tags mention hockey or NHL (first page only; discovery does the full walk)."""
    try:
        obj = json.loads(body)
    except json.JSONDecodeError:
        return {"error": "not json"}
    out = []
    for s in obj.get("series", []) if isinstance(obj, dict) else []:
        blob = json.dumps(s).upper()
        if "NHL" in blob or "HOCKEY" in blob:
            out.append({k: s.get(k) for k in ("ticker", "title", "category", "tags", "frequency", "fee_type", "fee_multiplier", "contract_url", "product_metadata")})
    return {"n_series_page": len(obj.get("series", [])) if isinstance(obj, dict) else 0, "cursor": obj.get("cursor") if isinstance(obj, dict) else None, "hockey_like": out}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("out", type=Path)
    ap.add_argument("--date", default=datetime.now(UTC).strftime("%Y-%m-%d"))
    ap.add_argument("--kalshi-hosts", default="https://api.elections.kalshi.com,https://external-api.kalshi.com")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "samples").mkdir(exist_ok=True)
    results = []
    for spec in probes(a.date, a.kalshi_hosts.split(",")):
        row = fetch(spec["url"], spec.get("method", "GET"), spec.get("ua", UA), spec.get("max_bytes", 5_000_000))
        body = row.pop("_body")
        row["name"] = spec["name"]
        row["probed_at_utc"] = datetime.now(UTC).isoformat(timespec="seconds")
        if body:
            desc, sample = describe(body, row.get("content_type"))
            row.update(desc)
            if spec.get("sample"):
                (a.out / "samples" / f"{spec['name']}.json").write_text(json.dumps(sample, indent=1, default=str)[:120_000])
            if spec.get("kalshi_series_scan"):
                row["nhl_scan"] = scan_series_for_nhl(body)
                (a.out / "samples" / f"{spec['name']}_nhl_scan.json").write_text(json.dumps(row["nhl_scan"], indent=1)[:200_000])
        results.append(row)
        print(f"{row['name']:42s} {str(row.get('status')):5s} {row['latency_ms']:6d}ms {row['bytes']:9d}B {row.get('kind','')} {row.get('error','')}")
    (a.out / "probe_results.json").write_text(json.dumps(results, indent=1, default=str))
    lines = ["# Source probe", "", f"probed {datetime.now(UTC).isoformat(timespec='seconds')} for date {a.date}", "", "| name | status | ms | bytes | kind | note |", "|---|---:|---:|---:|---|---|"]
    for r in results:
        note = r.get("error") or (", ".join(r.get("top_keys", [])[:8]) if r.get("kind") == "json" else ", ".join(r.get("header", [])[:8]))
        lines.append(f"| {r['name']} | {r.get('status')} | {r['latency_ms']} | {r['bytes']} | {r.get('kind','')} | {str(note)[:120]} |")
    (a.out / "probe_results.md").write_text("\n".join(lines) + "\n")
    n_ok = sum(1 for r in results if r["ok"])
    print(f"\n{n_ok}/{len(results)} probes OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
