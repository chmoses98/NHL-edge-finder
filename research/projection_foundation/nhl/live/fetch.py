"""Optional live top-up of the availability feeds (runs on GitHub Actions, where DailyFaceoff / ESPN / NHL are reachable).

The capture worker already archives these pages every 5-15 minutes while games are near; this module fetches the SAME
public pages directly at run time so the 16:00 / 18:00 ET runs see goalie confirmations that landed after the worker's
last push. It reuses the repo's own fetchers and parsers (`nhl_edge.data.{http,goalies,lines,context}`) and records our
own fetch time as `captured_utc`. Every source is independent: a failure is recorded in the stats (and surfaces in
coverage / freshness) and never aborts the others.

`get(url, headers) -> (bytes, fetched_at_utc_iso)` is injectable so the parsing path is tested on recorded payloads.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta
from typing import Any, Callable

import pandas as pd

from pf_core import availability as av

from nhl import data

from . import availability as A
from . import common as C

HTML_HEADERS = {"Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8"}      # content negotiation only; the identifying User-Agent is set by nhl_edge.data.http.fetch


def _default_get() -> Callable[[str, dict | None], tuple[bytes, str]]:
    src = str(data.ROOT / "src")
    if src not in sys.path:
        sys.path.insert(0, src)
    from nhl_edge.data.http import fetch

    def get(url: str, headers: dict | None = None) -> tuple[bytes, str]:
        f = fetch(url, headers=headers, max_retries=2)
        return f.content, f.fetched_at_utc
    return get


def _dfo_goalie_rows(content: bytes, fetched: str, date_et: str, sched: pd.DataFrame, abbr_by_id: dict[int, str]) -> tuple[pd.DataFrame, dict]:
    """DailyFaceoff starting-goalies page -> rows in the archive's context/goalie_observations schema."""
    src = str(data.ROOT / "src")
    if src not in sys.path:
        sys.path.insert(0, src)
    from nhl_edge.data.goalies import extract_next_data, strip_market_fields  # noqa: F401
    from nhl_edge.goalies.state import parse_dailyfaceoff_next_data
    from nhl_edge.identity.teams import registry
    from nhl_edge.timeutil import parse_iso

    nd = extract_next_data(content.decode("utf-8", "replace"))
    pp = nd.get("props", {}).get("pageProps", {})
    reg = registry()

    def resolve(name: str):
        t = reg.resolve_name(name)
        return t.team_id if t else None

    obs, problems = parse_dailyfaceoff_next_data(pp, parse_iso(fetched), resolve)
    by_key = {}
    for r in sched.itertuples():
        by_key[(r.game_date_et, int(r.home_team_id))] = int(r.game_id)
        by_key[(r.game_date_et, int(r.away_team_id))] = int(r.game_id)
    rows = []
    for o in obs:
        d = o.model_dump(mode="json")
        _, date, tid = str(d["game_id"]).split(":")
        gid = by_key.get((date, int(tid)))
        if gid is None:
            problems.append(f"no NHL game for team {tid} on {date}")
            continue
        rows.append({**d, "game_id": gid, "game_date_et": date})
    return pd.DataFrame(rows), {"n": len(rows), "problems": problems[:5], "page_date": pp.get("date")}


def fetch_and_write(out_root: str, now: datetime, archive: str, get: Callable | None = None,
                    horizon_h: float = 30.0, official_h: float = 3.0) -> dict[str, Any]:
    """Fetch DailyFaceoff goalies + lines, ESPN injuries and (games within `official_h`) the official pregame roster."""
    get = get or _default_get()
    stats: dict[str, Any] = {"errors": []}
    sched = C.schedule_asof(archive, now, back_days=4)
    if sched.empty:
        return {"error": "no schedule snapshot", "errors": ["no schedule snapshot"], "written": 0}
    nxt, ref, abbr = A.NextGame(sched), A.player_ref(), C.abbrev_by_id()
    sched_start = {int(r.game_id): C.iso(r.start.to_pydatetime()) for r in sched.itertuples() if C.is_regular(r.game_id)}
    upcoming = sched[(sched["start"] > pd.Timestamp(now)) & (sched["start"] <= pd.Timestamp(now + timedelta(hours=horizon_h)))
                     & sched["game_id"].map(C.is_regular)]
    stats["upcoming_games"] = int(len(upcoming))
    dates = sorted({C.et_date(now), C.et_date(now + timedelta(days=1))})

    # 1. DailyFaceoff starting goalies
    obs_all: list[av.Observation] = []
    for d in dates:
        try:
            content, fetched = get(A.URL_GOALIES.format(date=d), dict(HTML_HEADERS))
            rows, meta = _dfo_goalie_rows(content, fetched, d, sched, abbr)
            obs, st = A.goalie_observations(rows, sched_start, ref, abbr) if len(rows) else ([], {})
            obs_all += obs
            stats[f"goalies_{d}"] = {**meta, **st, "fetched_at_utc": fetched}
        except Exception as e:  # noqa: BLE001
            stats["errors"].append(f"goalies {d}: {type(e).__name__}: {str(e)[:160]}")
    stats["goalies_write"] = A._write_groups({"live_goalies": obs_all}, out_root)

    # 2. ESPN injuries
    try:
        content, fetched = get(A.URL_ESPN, None)
        src = str(data.ROOT / "src")
        if src not in sys.path:
            sys.path.insert(0, src)
        from nhl_edge.data.context import parse_espn_injuries
        rows = pd.DataFrame(parse_espn_injuries(json.loads(content.decode("utf-8"))))
        rows["_observed_at_utc"] = fetched
        obs, st = A.injury_observations(rows, nxt, ref, abbr)
        stats["injuries"] = {**st, "fetched_at_utc": fetched}
        stats["injuries_write"] = A._write_groups({"live_injuries": obs}, out_root)
    except Exception as e:  # noqa: BLE001
        stats["errors"].append(f"injuries: {type(e).__name__}: {str(e)[:160]}")

    # 3. DailyFaceoff line combinations for teams playing within the horizon
    try:
        src = str(data.ROOT / "src")
        if src not in sys.path:
            sys.path.insert(0, src)
        from nhl_edge.data.lines import DFO_SLUGS, line_rows, parse_line_page
        teams = {int(t): abbr[int(t)] for r in upcoming.itertuples() for t in (r.home_team_id, r.away_team_id)}
        frames, errs = [], 0
        for tid, ab in sorted(teams.items()):
            slug = DFO_SLUGS.get(ab)
            if not slug:
                continue
            try:
                content, fetched = get(A.URL_LINES.format(slug=slug), dict(HTML_HEADERS))
                combo = parse_line_page(content)
                if combo is None:
                    errs += 1
                    continue
                df = pd.DataFrame(line_rows(combo, ab, fetched))
                df["team_id"] = tid
                df["player_id"] = float("nan")
                df["resolution"] = None
                frames.append(df)
            except Exception:  # noqa: BLE001
                errs += 1
        obs, st = A.line_observations(pd.concat(frames, ignore_index=True), nxt, ref, abbr, slugs={k: v for k, v in DFO_SLUGS.items()}) \
            if frames else ([], {})
        stats["lines"] = {**st, "teams": len(teams), "page_errors": errs}
        stats["lines_write"] = A._write_groups({"live_lines": obs}, out_root)
    except Exception as e:  # noqa: BLE001
        stats["errors"].append(f"lines: {type(e).__name__}: {str(e)[:160]}")

    # 4. official pregame roster (play-by-play rosterSpots), only shortly before the start
    soon = upcoming[upcoming["start"] <= pd.Timestamp(now + timedelta(hours=official_h))]
    off: list[av.Observation] = []
    off_stats = {"games": int(len(soon)), "teams_accepted": 0, "teams_rejected": 0, "dressed_obs": 0, "scratch_obs": 0,
                 "not_pregame": 0, "states": {}}
    cand_by_game = _candidates(out_root, now, soon)
    for r in soon.itertuples():
        try:
            content, fetched = get(A.URL_PBP.format(game_id=int(r.game_id)), None)
            payload = json.loads(content.decode("utf-8"))
            o, st = A.roster_spots_observations(payload, C.parse_ts(fetched), cand_by_game.get(int(r.game_id), {}), abbr,
                                                C.iso(r.start.to_pydatetime()))
            off += o
            off_stats["states"][str(st.get("game_state"))] = off_stats["states"].get(str(st.get("game_state")), 0) + 1
            for k in ("teams_accepted", "teams_rejected", "dressed_obs", "scratch_obs"):
                off_stats[k] += st.get(k, 0)
            if st.get("rejected_reason"):
                off_stats["not_pregame"] += 1
        except Exception as e:  # noqa: BLE001
            stats["errors"].append(f"official {int(r.game_id)}: {type(e).__name__}: {str(e)[:120]}")
    stats["official"] = off_stats
    stats["official_write"] = A._write_groups({"live_official": off}, out_root)
    stats["written"] = sum(stats.get(k, {}).get("written", 0) for k in ("goalies_write", "injuries_write", "lines_write", "official_write"))
    return stats


def _candidates(out_root: str, now: datetime, games: pd.DataFrame) -> dict[int, dict[int, dict[str, str]]]:
    """game -> team_id -> {player_id: name} of skaters with a projected line observation (scope for scratch detection)."""
    rows = A.load_rows(out_root, now)
    ids = {str(int(g)) for g in games["game_id"]}
    out: dict[int, dict[int, dict[str, str]]] = {}
    tid_by_ab = {v: k for k, v in C.abbrev_by_id().items()}
    for r in rows:
        if r["kind"] == "line" and r["event_id"] in ids:
            out.setdefault(int(r["event_id"]), {}).setdefault(tid_by_ab.get(r["team"], -1), {})[r["entity_id"]] = r["entity_name"]
    return out
