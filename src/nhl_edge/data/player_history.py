"""Historical official NHL player-event pull for PLAYER_SIM_V1 (RESEARCH_ONLY; network, runs on a GitHub runner).

For every completed game of the requested seasons: boxscore + play-by-play + shift charts, derived per game by
:func:`nhl_edge.data.player_events.derive_game`, written as one Parquet per table per season under
``<out>/players/`` with a provenance manifest (``PLAYERS_MANIFEST.json``: URLs, counts, consistency-check failures,
share of games with usable shifts). Nothing here reads or writes the capture archive or ``main``.

Run: ``python -m nhl_edge.data.player_history --out data/history --seasons 2021,2022,2023,2024,2025``
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.config import settings
from nhl_edge.data.http import FetchError, fetch
from nhl_edge.data.player_events import SCHEMA_VERSION, check_game, derive_game
from nhl_edge.log import get_logger, kv
from nhl_edge.timeutil import iso, utcnow

log = get_logger(__name__)

TABLES = ("players", "goalies", "goals", "shots", "coice", "team_states")


def urls(game_id: int) -> dict[str, str]:
    cfg = settings()
    return {"box": f"{cfg.nhl_api_base_url}/gamecenter/{game_id}/boxscore", "pbp": f"{cfg.nhl_api_base_url}/gamecenter/{game_id}/play-by-play",
            "shifts": f"{cfg.nhl_stats_base_url}/shiftcharts?cayenneExp=gameId={game_id}"}


def fetch_game(game_id: int, meta: dict[str, Any], sample_dir: Path | None = None) -> tuple[dict[str, pd.DataFrame] | None, dict[str, Any]]:
    u = urls(game_id)
    rep: dict[str, Any] = {"game_id": game_id}
    try:
        box = fetch(u["box"], timeout=60).json()
        pbp = fetch(u["pbp"], timeout=60).json()
    except (FetchError, ValueError) as e:
        return None, rep | {"error": f"box/pbp: {str(e)[:200]}"}
    try:
        shifts = fetch(u["shifts"], timeout=60).json()
    except (FetchError, ValueError) as e:
        shifts = {"data": []}
        rep["shifts_error"] = str(e)[:200]
    if sample_dir is not None:
        sample_dir.mkdir(parents=True, exist_ok=True)
        for k, v in (("boxscore", box), ("pbp", pbp), ("shiftcharts", shifts)):
            (sample_dir / f"nhl_{k}_{game_id}.json").write_text(json.dumps(v))
    try:
        tables = derive_game(box, pbp, shifts, meta)
    except Exception as e:  # noqa: BLE001 - one malformed game must not lose a season
        return None, rep | {"error": f"derive: {type(e).__name__}: {str(e)[:200]}"}
    rep["issues"] = check_game(tables, box)
    rep["shifts_ok"] = bool(len(tables["players"]) and tables["players"]["shifts_ok"].all())
    return tables, rep


def game_list(history_root: Path, season: int) -> pd.DataFrame:
    from nhl_edge.data.history import load_nhl_games, nhl_games_url, parse_nhl_games

    g = load_nhl_games(history_root, [season])
    if not len(g):
        frames = []
        for gt in (2, 3):
            try:
                frames.append(parse_nhl_games(fetch(nhl_games_url(season, gt), timeout=120).json()))
            except (FetchError, ValueError) as e:
                log.warning(kv(event="game_list_error", season=season, game_type=gt, err=str(e)[:200]))
        g = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    if not len(g):
        return g
    return g[(g["final"]) & (g["game_type"].isin([2, 3]))].sort_values(["game_date", "game_id"]).reset_index(drop=True)


def pull_season(season: int, out_root: Path, history_root: Path, workers: int = 6, max_games: int | None = None,
                sample_dir: Path | None = None) -> dict[str, Any]:
    t0 = time.time()
    games = game_list(history_root, season)
    if max_games:
        games = games.head(int(max_games))
    rep: dict[str, Any] = {"season": season, "games_listed": int(len(games)), "errors": [], "issue_counts": {}, "schema_version": SCHEMA_VERSION}
    parts: dict[str, list[pd.DataFrame]] = {t: [] for t in TABLES}
    issues: Counter[str] = Counter()
    n_ok = n_shifts = 0
    with ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        futs = {}
        for i, r in enumerate(games.itertuples(index=False)):
            meta = {"season": int(season), "game_date": str(r.game_date)[:10], "game_type": int(r.game_type)}
            sd = sample_dir if (sample_dir is not None and i == 0) else None
            futs[ex.submit(fetch_game, int(r.game_id), meta, sd)] = int(r.game_id)
        for k, fu in enumerate(as_completed(futs)):
            tables, g = fu.result()
            if tables is None:
                rep["errors"].append(g)
                continue
            n_ok += 1
            n_shifts += int(g.get("shifts_ok", False))
            for s in g.get("issues", []):
                issues[re.sub(r"\d+", "N", s)] += 1
            for t in TABLES:
                if len(tables[t]):
                    parts[t].append(tables[t])
            if (k + 1) % 200 == 0:
                log.info(kv(event="player_history_progress", season=season, done=k + 1, total=len(futs), elapsed_s=round(time.time() - t0)))
    out = Path(out_root) / "players"
    out.mkdir(parents=True, exist_ok=True)
    rep["files"] = {}
    for t in TABLES:
        if not parts[t]:
            continue
        df = pd.concat(parts[t], ignore_index=True)
        for c in df.columns:
            if df[c].dtype == object and c not in ("for_on_ice", "against_on_ice"):
                sample = df[c].dropna()
                if len(sample) and isinstance(sample.iloc[0], bool):
                    df[c] = df[c].astype("boolean")
        p = out / f"{t}_{season}.parquet"
        df.to_parquet(p, index=False, compression="zstd")
        rep["files"][t] = {"file": p.name, "rows": int(len(df)), "bytes": p.stat().st_size}
    rep.update({"games_ok": n_ok, "games_with_shifts": n_shifts, "issue_counts": dict(issues), "n_errors": len(rep["errors"]),
                "errors": rep["errors"][:50], "elapsed_s": round(time.time() - t0, 1), "pulled_at_utc": iso(utcnow())})
    log.info(kv(event="player_history_season", season=season, ok=n_ok, shifts=n_shifts, errors=len(rep["errors"]), elapsed_s=rep["elapsed_s"]))
    return rep


def load_player_tables(history_root: Path, table: str, seasons: list[int] | None = None) -> pd.DataFrame:
    folder = Path(history_root) / "players"
    files = sorted(folder.glob(f"{table}_*.parquet"))
    if seasons is not None:
        files = [f for f in files if int(f.stem.split("_")[-1]) in set(seasons)]
    return pd.concat([pd.read_parquet(f) for f in files], ignore_index=True) if files else pd.DataFrame()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.data.player_history")
    ap.add_argument("--out", default="data/history")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--seasons", default="2021,2022,2023,2024,2025")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--max-games", type=int, default=None)
    ap.add_argument("--sample-dir", default=None, help="write the first game's raw payloads here (test fixtures)")
    a = ap.parse_args(argv)
    from nhl_edge.data.history import parse_seasons

    rc = 0
    for s in parse_seasons(a.seasons):
        rep = pull_season(s, Path(a.out), Path(a.history), a.workers, a.max_games, Path(a.sample_dir) if a.sample_dir else None)
        # one manifest per season so parallel season jobs never collide
        mpath = Path(a.out) / "players" / f"MANIFEST_{s}.json"
        mpath.parent.mkdir(parents=True, exist_ok=True)
        mpath.write_text(json.dumps(rep, indent=1, default=str))
        rc |= 0 if rep.get("games_ok") else 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
