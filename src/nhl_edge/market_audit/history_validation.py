"""Validate the outcome resolver against Kalshi's OWN settlement on the 2025-26 history archive.

The live archive never records a settled ``result`` (the capture requests live statuses only), so settlement semantics
cannot be validated there. ``data/history/kalshi/markets_*.jsonl.gz`` holds finalized markets with ``result`` yes/no/scalar.
This module runs the SAME ``outcomes.resolve`` rules (winner / spread / total) against official NHL finals and counts
disagreements, with the shootout games reported separately because they are what discriminates the shootout-credit rule.
"""

from __future__ import annotations

import gzip
import json
import re
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.identity.teams import registry
from nhl_edge.kalshi.ticker import parse_ticker
from nhl_edge.market_audit.outcomes import GameFacts, resolve
from nhl_edge.market_audit.taxonomy import PROVEN, ContractSpec, resolve_team

_KIND = {"KXNHLGAME": "winner", "KXNHLSPREAD": "spread", "KXNHLTOTAL": "total"}


def load_history_games(history_dir: Path) -> pd.DataFrame:
    frames = [pd.read_parquet(p) for p in sorted((Path(history_dir) / "nhl").glob("games_*.parquet"))]
    g = pd.concat(frames, ignore_index=True)
    return g[g["final"]].drop_duplicates("game_id")


def _read_markets(history_dir: Path, series: str) -> list[dict[str, Any]]:
    p = Path(history_dir) / "kalshi" / f"markets_{series}.jsonl.gz"
    return [json.loads(x) for x in gzip.open(p, "rt")]


def validate(history_dir: Path) -> pd.DataFrame:
    reg = registry()
    games = load_history_games(history_dir)
    by_key = {(r.game_date, frozenset((int(r.home_team_id), int(r.away_team_id)))): r for r in games.itertuples()}
    known = reg.tricodes | set(reg.by_abbrev_map)
    rows: list[dict[str, Any]] = []
    for series, kind in _KIND.items():
        for m in _read_markets(history_dir, series):
            res = str(m.get("result") or "")
            pt = parse_ticker(m["ticker"], known)
            rec = {"series": series, "ticker": m["ticker"], "kalshi_result": res, "status": m.get("status")}
            try:
                away, home = reg.by_abbrev(pt.away_tricode or ""), reg.by_abbrev(pt.home_tricode or "")
            except KeyError:
                rows.append({**rec, "mine": "NO_TEAM_JOIN"})
                continue
            g = by_key.get((pt.game_date.isoformat() if pt.game_date else "", frozenset((home.team_id, away.team_id))))
            if g is None:
                rows.append({**rec, "mine": "NO_GAME_JOIN"})
                continue
            subject = None
            if kind in ("winner", "spread"):
                code = re.sub(r"\d+$", "", pt.market_suffix)
                try:
                    subject = reg.by_abbrev(code).team_id
                except KeyError:
                    t = resolve_team(str(m.get("yes_sub_title") or "").split(" wins")[0], reg)
                    subject = t.team_id if t else None
            thr = float(m["floor_strike"]) if m.get("floor_strike") not in (None, "") else None
            spec = ContractSpec(m["ticker"], m.get("event_ticker", ""), series, "x", "game", "FULL", kind, None, thr, subject,
                                (home.team_id, away.team_id), pt.game_date.isoformat() if pt.game_date else None, None, None, None,
                                True, "one_goal", "none", False, PROVEN)
            facts = GameFacts(str(g.game_id), int(g.home_team_id), int(g.away_team_id), True, int(g.home_score), int(g.away_score),
                              None, None, g.last_period_type)
            if kind in ("winner", "spread") and subject is None:
                rows.append({**rec, "mine": "NO_SUBJECT"})
                continue
            out = resolve(spec, facts)
            rows.append({**rec, "mine": out.outcome, "game_id": g.game_id, "period_type": g.last_period_type,
                         "total": int(g.home_score) + int(g.away_score), "threshold": thr})
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    d = df[df["kalshi_result"].isin(["yes", "no"]) & df["mine"].isin(["YES", "NO"])].copy()
    d["agree"] = d["kalshi_result"].str.upper() == d["mine"]
    return d.groupby(["series", "period_type"]).agg(n=("agree", "size"), agree=("agree", "sum")).assign(rate=lambda x: x.agree / x.n).reset_index()
