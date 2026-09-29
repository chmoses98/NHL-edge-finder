"""Historical NHL dataset puller: MoneyPuck team game-by-game rows + official NHL results -> Parquet.

Design
------
- The network layer is one thin seam (:func:`fetch_bytes`); every parser is a pure function over bytes/JSON so it
  can be tested from small fixtures without network access (this repo's dev container has none to these hosts).
- MoneyPuck ``all_teams.csv`` is one ~tens-of-MB file covering every season since 2008, one row per team per game
  per situation. We keep the configured seasons (default 2022+) and the situations the DATA_ONLY_V1 features can
  use (``all``, ``5on5``, ``5on4``, ``4on5``), add canonical identity columns, and write one Parquet per season.
- Official results (winner, final score, REG/OT/SO) come from the NHL stats REST ``/game`` list, one request per
  season per game type. MoneyPuck's ``goalsFor`` is used for ratings, never for settlement-style labels.
- ``MANIFEST.json`` records provenance for both: source URL, retrieval instant, sha256 of each raw download, row
  counts, schema version. Errors are recorded there rather than raised so one bad source does not lose the other.

Season naming: MoneyPuck ``season`` is the START year (2025 == NHL 2025-26 == stats ``season=20252026``). Every
``season`` column written here uses the MoneyPuck/start-year convention; ``season_id`` carries the 8-digit form.

Outputs (``out_root/``)::

    moneypuck/team_games_<season>.parquet   raw MoneyPuck columns + normalised identity columns
    nhl/games_<season>.parquet              one row per game (regular season + playoffs, ``game_type`` 2/3)
    MANIFEST.json

Run: ``python -m nhl_edge.data.history --out data/history --seasons 2022,2023,2024,2025``
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import time
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.config import settings
from nhl_edge.data.http import BROWSER_HEADERS, fetch
from nhl_edge.identity.teams import TeamIdentityError, registry
from nhl_edge.log import get_logger, kv
from nhl_edge.timeutil import iso, utcnow

log = get_logger(__name__)

SCHEMA_VERSION = "nhl-history-1.0"
MONEYPUCK_ALL_TEAMS_URL = "https://moneypuck.com/moneypuck/playerData/careers/gameByGame/all_teams.csv"
NHL_STATS_GAME_PATH = "/game?cayenneExp=season={season_id}%20and%20gameType={game_type}&limit=-1"
KEEP_SITUATIONS: tuple[str, ...] = ("all", "5on5", "5on4", "4on5")
DEFAULT_SEASONS: tuple[int, ...] = (2022, 2023, 2024, 2025)
NHL_GAME_TYPES: tuple[int, ...] = (2, 3)  # 2 regular season, 3 playoffs
MONEYPUCK_TIMEOUT_S = 600.0
NHL_TIMEOUT_S = 180.0
PARQUET_COMPRESSION = "zstd"

# Columns the ratings code (nhl_edge.features.ratings.prepare_gamelog) and this module require in the CSV.
MP_REQUIRED_COLUMNS = (
    "team", "season", "gameId", "opposingTeam", "home_or_away", "gameDate", "situation",
    "xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst", "iceTime",
)
MP_DROP_COLUMNS = ("name", "position")  # constant / redundant ("Team Level")
MP_STRING_COLUMNS = ("team", "playerTeam", "opposingTeam", "home_or_away", "situation")
MP_IDENTITY_COLUMNS = [
    "season", "game_id", "game_date", "game_type", "team_abbrev", "team_id", "opp_abbrev", "opp_team_id", "home",
    "mp_team", "mp_opposing_team", "schema_version",
]

NHL_GAME_COLUMNS = [
    "game_id", "season", "season_id", "game_type", "game_date", "start_time_et", "home_team_id", "away_team_id",
    "home_abbrev", "away_abbrev", "home_score", "away_score", "total", "home_win", "period", "last_period_type",
    "game_state_id", "final", "schema_version",
]


# --------------------------------------------------------------------------------------------------------------
# seasons / urls
# --------------------------------------------------------------------------------------------------------------
def parse_seasons(text: str | Iterable[int | str]) -> list[int]:
    """'2022,2023' or [2022, '2023'] -> [2022, 2023]. A MoneyPuck season is its start year (2025 == 2025-26)."""
    items = text.split(",") if isinstance(text, str) else list(text)
    out: list[int] = []
    for s in items:
        t = str(s).strip()
        if not t:
            continue
        if not t.isdigit() or len(t) != 4:
            raise ValueError(f"bad season {s!r}; expected a 4-digit start year like 2024")
        out.append(int(t))
    return sorted(set(out))


def season_id(season: int) -> int:
    """MoneyPuck/start-year season -> NHL 8-digit season id (2025 -> 20252026)."""
    return int(season) * 10000 + int(season) + 1


def nhl_games_url(season: int, game_type: int, base_url: str | None = None) -> str:
    base = (base_url or settings().nhl_stats_base_url).rstrip("/")
    return base + NHL_STATS_GAME_PATH.format(season_id=season_id(season), game_type=int(game_type))


def last_period_type(period: int | None, game_type: int | None) -> str | None:
    """NHL stats ``period`` -> REG/OT/SO. Regular season: 3 REG, 4 OT, 5+ SO. Playoffs never go to a shootout, so any
    period beyond 3 is OT. ``None`` (or < 3) means the game has not finished regulation."""
    if period is None:
        return None
    try:
        p = int(period)
    except (TypeError, ValueError):
        return None
    if p < 3:
        return None
    if p == 3:
        return "REG"
    if game_type == 3:
        return "OT"
    return "OT" if p == 4 else "SO"


# --------------------------------------------------------------------------------------------------------------
# network seam
# --------------------------------------------------------------------------------------------------------------
def fetch_bytes(url: str, timeout_s: float) -> tuple[bytes, str]:
    """GET ``url`` (no cache TTL: history pulls always hit the source). Returns (content, fetched_at_utc).
    Monkeypatched in tests; the dev container cannot reach moneypuck.com or nhle.com."""
    f = fetch(url, ttl_s=0.0, headers=BROWSER_HEADERS, timeout=timeout_s)
    return f.content, f.fetched_at_utc


def sha256_hex(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


# --------------------------------------------------------------------------------------------------------------
# MoneyPuck parsing (pure)
# --------------------------------------------------------------------------------------------------------------
def _resolve_abbrev(raw: str) -> tuple[str | None, int | None]:
    try:
        t = registry().by_abbrev(raw)
    except TeamIdentityError:
        return None, None
    return t.abbrev, t.team_id


def parse_moneypuck_csv(text: str | bytes, seasons: Iterable[int] | None = None,
                        situations: Sequence[str] | None = KEEP_SITUATIONS) -> pd.DataFrame:
    """MoneyPuck team game-by-game CSV -> DataFrame (raw columns kept, identity columns added).

    ``seasons`` keeps only those start years (None keeps all); ``situations`` keeps only those rows (None keeps all).
    Added columns: ``game_id`` (int), ``game_date`` (YYYY-MM-DD), ``game_type`` (from the game id: 02 regular,
    03 playoffs), ``team_abbrev``/``team_id`` and ``opp_abbrev``/``opp_team_id`` (canonical via the identity
    registry; None when unresolvable), ``home`` (bool), ``mp_team``/``mp_opposing_team`` (the raw MoneyPuck codes,
    e.g. 'T.B'). The raw ``team``/``opposingTeam``/``gameDate``/``gameId`` columns are left untouched so
    :func:`nhl_edge.features.ratings.prepare_gamelog` accepts the frame directly.
    """
    buf: io.BytesIO | io.StringIO = io.BytesIO(text) if isinstance(text, bytes) else io.StringIO(text)
    df = pd.read_csv(buf, low_memory=False)
    missing = [c for c in MP_REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"MoneyPuck CSV missing required columns: {missing}")
    df = df.drop(columns=[c for c in MP_DROP_COLUMNS if c in df.columns])

    df["season"] = pd.to_numeric(df["season"], errors="coerce")
    df["gameId"] = pd.to_numeric(df["gameId"], errors="coerce")
    df["gameDate"] = pd.to_numeric(df["gameDate"], errors="coerce")
    df = df.dropna(subset=["season", "gameId", "gameDate"]).copy()
    df["season"] = df["season"].astype("int64")
    df["gameId"] = df["gameId"].astype("int64")
    df["gameDate"] = df["gameDate"].astype("int64")
    for c in MP_STRING_COLUMNS:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()

    if seasons is not None:
        keep = {int(s) for s in seasons}
        df = df[df["season"].isin(keep)]
    if situations is not None:
        df = df[df["situation"].isin(set(situations))]
    df = df.copy()

    for c in df.columns:
        if c not in MP_STRING_COLUMNS and df[c].dtype == object:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    df["game_id"] = df["gameId"]
    df["game_date"] = df["gameDate"].map(lambda v: f"{v // 10000:04d}-{(v // 100) % 100:02d}-{v % 100:02d}")
    df["game_type"] = ((df["gameId"] // 10000) % 100).astype("int64")
    df["home"] = df["home_or_away"].str.upper() == "HOME"
    df["mp_team"] = df["team"]
    df["mp_opposing_team"] = df["opposingTeam"]
    resolved = {raw: _resolve_abbrev(raw) for raw in pd.unique(pd.concat([df["mp_team"], df["mp_opposing_team"]]))}
    df["team_abbrev"] = df["mp_team"].map(lambda r: resolved[r][0])
    df["team_id"] = df["mp_team"].map(lambda r: resolved[r][1]).astype("Int64")
    df["opp_abbrev"] = df["mp_opposing_team"].map(lambda r: resolved[r][0])
    df["opp_team_id"] = df["mp_opposing_team"].map(lambda r: resolved[r][1]).astype("Int64")
    df["schema_version"] = SCHEMA_VERSION

    df = df.drop_duplicates(subset=["game_id", "mp_team", "situation"], keep="last")
    df = df.sort_values(["season", "gameDate", "game_id", "mp_team", "situation"]).reset_index(drop=True)
    front = [c for c in MP_IDENTITY_COLUMNS if c in df.columns]
    return df[front + [c for c in df.columns if c not in front]]


def unresolved_abbrevs(df: pd.DataFrame) -> dict[str, int]:
    """Raw MoneyPuck team codes that did not resolve in the registry -> row count (for the manifest)."""
    if df.empty:
        return {}
    bad = df.loc[df["team_abbrev"].isna(), "mp_team"].value_counts()
    return {str(k): int(v) for k, v in bad.items()}


# --------------------------------------------------------------------------------------------------------------
# NHL stats parsing (pure)
# --------------------------------------------------------------------------------------------------------------
def _int_or_none(v: Any) -> int | None:
    if v is None or (isinstance(v, float) and v != v):
        return None
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def parse_nhl_games(payload: Any) -> pd.DataFrame:
    """``/stats/rest/en/game`` payload ({"data": [...]}, or a bare list) -> one row per game.

    ``final`` is ``gameStateId == 7``; ``last_period_type`` REG/OT/SO from ``period`` (see :func:`last_period_type`);
    ``home_win`` is None unless the game is final with both scores present. Team abbreviations come from the identity
    registry (None for an unknown team id, which never drops the row).
    """
    data = payload.get("data") if isinstance(payload, dict) else payload
    rows: list[dict[str, Any]] = []
    reg = registry()
    for g in data or []:
        gid = _int_or_none(g.get("id"))
        if gid is None:
            continue
        sid = _int_or_none(g.get("season")) or season_id(int(str(gid)[:4]))
        gt = _int_or_none(g.get("gameType"))
        if gt is None:
            gt = (gid // 10000) % 100
        period = _int_or_none(g.get("period"))
        state = _int_or_none(g.get("gameStateId"))
        final = state == 7
        hs, as_ = _int_or_none(g.get("homeScore")), _int_or_none(g.get("visitingScore"))
        home_id, away_id = _int_or_none(g.get("homeTeamId")), _int_or_none(g.get("visitingTeamId"))

        def _ab(tid: int | None) -> str | None:
            if tid is None:
                return None
            try:
                return reg.by_id(tid).abbrev
            except TeamIdentityError:
                return None

        scored = final and hs is not None and as_ is not None
        rows.append({
            "game_id": gid, "season": sid // 10000, "season_id": sid, "game_type": gt,
            "game_date": str(g.get("gameDate") or "")[:10] or None, "start_time_et": g.get("easternStartTime"),
            "home_team_id": home_id, "away_team_id": away_id, "home_abbrev": _ab(home_id), "away_abbrev": _ab(away_id),
            "home_score": hs, "away_score": as_, "total": (hs + as_) if scored else None,
            "home_win": (hs > as_) if scored else None, "period": period, "last_period_type": last_period_type(period, gt),
            "game_state_id": state, "final": final, "schema_version": SCHEMA_VERSION,
        })
    df = pd.DataFrame(rows, columns=NHL_GAME_COLUMNS)
    for c in ("home_score", "away_score", "total", "period", "game_state_id", "home_team_id", "away_team_id"):
        df[c] = df[c].astype("Int64")
    df["home_win"] = df["home_win"].astype("boolean")
    df["final"] = df["final"].astype(bool)
    df = df.drop_duplicates(subset=["game_id"], keep="last")
    return df.sort_values(["game_date", "game_id"]).reset_index(drop=True)


# --------------------------------------------------------------------------------------------------------------
# parquet i/o
# --------------------------------------------------------------------------------------------------------------
def moneypuck_path(out_root: Path, season: int) -> Path:
    return Path(out_root) / "moneypuck" / f"team_games_{int(season)}.parquet"


def nhl_path(out_root: Path, season: int) -> Path:
    return Path(out_root) / "nhl" / f"games_{int(season)}.parquet"


def manifest_path(out_root: Path) -> Path:
    return Path(out_root) / "MANIFEST.json"


def write_parquet(df: pd.DataFrame, path: Path) -> int:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, engine="pyarrow", index=False, compression=PARQUET_COMPRESSION)
    return int(len(df))


def read_parquet(path: Path) -> pd.DataFrame:
    return pd.read_parquet(path, engine="pyarrow")


def _available_seasons(folder: Path, prefix: str) -> list[int]:
    if not folder.exists():
        return []
    out = []
    for p in folder.glob(f"{prefix}_*.parquet"):
        tail = p.stem[len(prefix) + 1:]
        if tail.isdigit():
            out.append(int(tail))
    return sorted(out)


def load_team_games(out_root: Path, seasons: Iterable[int] | None = None) -> pd.DataFrame:
    """Concatenate ``moneypuck/team_games_<season>.parquet`` (all seasons on disk when ``seasons`` is None)."""
    root = Path(out_root)
    ss = list(seasons) if seasons is not None else _available_seasons(root / "moneypuck", "team_games")
    frames = [read_parquet(moneypuck_path(root, s)) for s in ss if moneypuck_path(root, s).exists()]
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=MP_IDENTITY_COLUMNS + list(MP_REQUIRED_COLUMNS))


def load_nhl_games(out_root: Path, seasons: Iterable[int] | None = None) -> pd.DataFrame:
    root = Path(out_root)
    ss = list(seasons) if seasons is not None else _available_seasons(root / "nhl", "games")
    frames = [read_parquet(nhl_path(root, s)) for s in ss if nhl_path(root, s).exists()]
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=NHL_GAME_COLUMNS)


# --------------------------------------------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------------------------------------------
def _read_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        log.warning(kv(event="history_manifest_unreadable", path=str(path)))
        return {}


def _moneypuck_season_summary(df: pd.DataFrame) -> dict[str, Any]:
    all_rows = df[df["situation"] == "all"]
    return {
        "rows": int(len(df)), "games": int(df["game_id"].nunique()), "teams": int(df["mp_team"].nunique()),
        "situations": sorted(df["situation"].unique().tolist()),
        "date_min": str(df["game_date"].min()) if len(df) else None, "date_max": str(df["game_date"].max()) if len(df) else None,
        "n_regular_team_games": int((all_rows["game_type"] == 2).sum()), "n_playoff_team_games": int((all_rows["game_type"] == 3).sum()),
        "unresolved_abbrevs": unresolved_abbrevs(df),
    }


def _nhl_season_summary(df: pd.DataFrame) -> dict[str, Any]:
    return {
        "rows": int(len(df)), "n_final": int(df["final"].sum()) if len(df) else 0,
        "game_types": {str(k): int(v) for k, v in df["game_type"].value_counts().sort_index().items()} if len(df) else {},
        "last_period_type": {str(k): int(v) for k, v in df["last_period_type"].value_counts().items()} if len(df) else {},
        "date_min": str(df["game_date"].min()) if len(df) else None, "date_max": str(df["game_date"].max()) if len(df) else None,
    }


def run_history(out_root: Path, seasons: Sequence[int] = DEFAULT_SEASONS, *, do_moneypuck: bool = True, do_nhl: bool = True,
                game_types: Sequence[int] = NHL_GAME_TYPES, situations: Sequence[str] = KEEP_SITUATIONS,
                moneypuck_url: str = MONEYPUCK_ALL_TEAMS_URL, moneypuck_timeout_s: float = MONEYPUCK_TIMEOUT_S,
                nhl_timeout_s: float = NHL_TIMEOUT_S) -> dict[str, Any]:
    """Pull MoneyPuck team game logs and NHL results for ``seasons`` into ``out_root`` and write MANIFEST.json.

    Returns the manifest dict. Failures are recorded under ``manifest["errors"]`` (and logged) instead of raised,
    so a MoneyPuck outage still leaves the NHL results on disk and vice versa. Existing manifest entries for seasons
    not touched by this run are preserved.
    """
    out_root = Path(out_root)
    seasons = parse_seasons(seasons)
    t0 = time.time()
    manifest = _read_manifest(manifest_path(out_root))
    manifest.setdefault("moneypuck", {"seasons": {}})
    manifest.setdefault("nhl", {"seasons": {}})
    manifest["schema_version"] = SCHEMA_VERSION
    manifest["seasons_requested"] = seasons
    manifest["season_convention"] = "start year (2025 == NHL 2025-26 == stats season 20252026)"
    errors: list[dict[str, Any]] = []

    if do_moneypuck:
        mp = manifest["moneypuck"]
        mp.update({"source_url": moneypuck_url, "situations_kept": list(situations), "compression": PARQUET_COMPRESSION})
        try:
            log.info(kv(event="history_moneypuck_fetch", url=moneypuck_url))
            content, fetched_at = fetch_bytes(moneypuck_url, moneypuck_timeout_s)
            mp.update({"retrieved_at_utc": fetched_at, "sha256": sha256_hex(content), "bytes": len(content)})
            df = parse_moneypuck_csv(content, seasons=seasons, situations=situations)
            for s in seasons:
                d = df[df["season"] == s]
                if d.empty:
                    errors.append({"source": "moneypuck", "season": s, "error": "no rows for season in all_teams.csv"})
                    log.warning(kv(event="history_moneypuck_empty_season", season=s))
                    continue
                path = moneypuck_path(out_root, s)
                n = write_parquet(d, path)
                summ = _moneypuck_season_summary(d)
                summ.update({"file": str(path.relative_to(out_root)), "bytes_on_disk": path.stat().st_size, "retrieved_at_utc": fetched_at})
                mp["seasons"][str(s)] = summ
                log.info(kv(event="history_moneypuck_written", season=s, rows=n, path=str(path)))
        except Exception as e:  # noqa: BLE001 - recorded, never fatal for the other source
            errors.append({"source": "moneypuck", "error": f"{type(e).__name__}: {e}"[:400]})
            log.error(kv(event="history_moneypuck_error", err=f"{type(e).__name__}: {e}"[:200]))

    if do_nhl:
        nh = manifest["nhl"]
        nh.update({"source_url_template": settings().nhl_stats_base_url.rstrip("/") + NHL_STATS_GAME_PATH,
                   "game_types": list(game_types), "compression": PARQUET_COMPRESSION})
        for s in seasons:
            frames: list[pd.DataFrame] = []
            fetches: dict[str, Any] = {}
            for gt in game_types:
                url = nhl_games_url(s, gt)
                try:
                    content, fetched_at = fetch_bytes(url, nhl_timeout_s)
                    payload = json.loads(content.decode("utf-8"))
                    part = parse_nhl_games(payload)
                    fetches[str(gt)] = {"url": url, "retrieved_at_utc": fetched_at, "sha256": sha256_hex(content), "bytes": len(content), "rows": int(len(part))}
                    frames.append(part)
                except Exception as e:  # noqa: BLE001
                    errors.append({"source": "nhl", "season": s, "game_type": gt, "error": f"{type(e).__name__}: {e}"[:400]})
                    log.error(kv(event="history_nhl_error", season=s, game_type=gt, err=f"{type(e).__name__}: {e}"[:200]))
            if not frames:
                continue
            df = pd.concat(frames, ignore_index=True).drop_duplicates(subset=["game_id"], keep="last")
            df = df[df["season"] == s].sort_values(["game_date", "game_id"]).reset_index(drop=True)
            path = nhl_path(out_root, s)
            n = write_parquet(df, path)
            summ = _nhl_season_summary(df)
            summ.update({"file": str(path.relative_to(out_root)), "bytes_on_disk": path.stat().st_size, "fetches": fetches})
            nh["seasons"][str(s)] = summ
            log.info(kv(event="history_nhl_written", season=s, rows=n, path=str(path)))

    manifest["generated_at_utc"] = iso(utcnow())
    manifest["elapsed_s"] = round(time.time() - t0, 1)
    manifest["errors"] = errors
    manifest["n_errors"] = len(errors)
    mp_path = manifest_path(out_root)
    mp_path.parent.mkdir(parents=True, exist_ok=True)
    mp_path.write_text(json.dumps(manifest, indent=2, default=str))
    log.info(kv(event="history_done", seasons=",".join(map(str, seasons)), n_errors=len(errors), elapsed_s=manifest["elapsed_s"]))
    return manifest


def main(argv: Sequence[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.data.history", description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", default="data/history", help="output root (default data/history)")
    ap.add_argument("--seasons", default=",".join(map(str, DEFAULT_SEASONS)), help="comma list of start years (2025 == 2025-26)")
    ap.add_argument("--skip-moneypuck", action="store_true")
    ap.add_argument("--skip-nhl", action="store_true")
    ap.add_argument("--moneypuck-url", default=MONEYPUCK_ALL_TEAMS_URL)
    ap.add_argument("--timeout", type=float, default=MONEYPUCK_TIMEOUT_S, help="MoneyPuck download timeout (s)")
    a = ap.parse_args(argv)
    manifest = run_history(Path(a.out), parse_seasons(a.seasons), do_moneypuck=not a.skip_moneypuck, do_nhl=not a.skip_nhl,
                           moneypuck_url=a.moneypuck_url, moneypuck_timeout_s=a.timeout)
    print(json.dumps({k: manifest.get(k) for k in ("generated_at_utc", "seasons_requested", "n_errors", "errors")}, indent=2))
    return 1 if manifest.get("n_errors") else 0


if __name__ == "__main__":
    sys.exit(main())
