"""Point-in-time NHL availability capture (pf_core.availability observations).

Sources and certainty mapping (never upgraded):

| source (source id)                      | what                                    | kind     | status                        | certainty |
|------------------------------------------|-----------------------------------------|----------|-------------------------------|-----------|
| dailyfaceoff_goalies                     | goalie status "Confirmed"               | starter  | STARTING                      | CONFIRMED |
| dailyfaceoff_goalies                     | "Likely"/"Probable"/"Projected"/null    | starter  | PROBABLE                      | PROJECTED |
| dailyfaceoff_lines                       | projected lines / PP units (any source) | line     | ACTIVE (+ unit, PP unit)      | PROJECTED |
| dailyfaceoff_lines                       | DailyFaceoff injured-list flag          | injury   | OUT / QUESTIONABLE            | PROJECTED |
| espn_injuries                            | Out / IR / Suspension, Day-To-Day       | injury   | OUT / QUESTIONABLE            | REPORTED  |
| nhl_api_pbp_rosterspots (live, optional) | official pregame dressed roster / scratch| lineup  | ACTIVE / INACTIVE             | CONFIRMED |

All except the last are read from the repo's own capture worker archive (`data-archive` branch: context/lines,
context/goalie_observations, context/injuries, context/schedule) with the ORIGINAL fetch time as `captured_utc`
(the moment the worker fetched the page, never the moment this module ran). `--live-fetch` additionally fetches the
same public pages directly (fresher at 16:00/18:00 ET) with the repo's fetchers; those observations carry our own fetch
time. Everything is written as immutable pf_core snapshots (`availability/nhl/<date>/<HHMMSS>Z_<hash>.jsonl.gz`).

An observation is attached to the TEAM'S NEXT GAME that starts after its capture time; pf_core.availability.asof then
refuses anything captured at/after the start of the event.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Any

import numpy as np
import pandas as pd

from pf_core import availability as av

from nhl import data

from . import common as C

SRC_LINES = "dailyfaceoff_lines"
SRC_GOALIES = "dailyfaceoff_goalies"
SRC_ESPN = "espn_injuries"
SRC_OFFICIAL = "nhl_api_pbp_rosterspots"
URL_LINES = "https://www.dailyfaceoff.com/teams/{slug}/line-combinations"
URL_GOALIES = "https://www.dailyfaceoff.com/starting-goalies/{date}"
URL_ESPN = "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/injuries"
URL_PBP = "https://api-web.nhle.com/v1/gamecenter/{game_id}/play-by-play"

ESPN_STATUS = {"out": "OUT", "injured reserve": "OUT", "suspension": "OUT", "day-to-day": "QUESTIONABLE",
               "questionable": "QUESTIONABLE", "doubtful": "DOUBTFUL", "probable": "PROBABLE"}
DFO_INJ = {"out": "OUT", "ir": "OUT", "dtd": "QUESTIONABLE"}
GOALIE_STATUS = {"CONFIRMED": ("STARTING", "CONFIRMED"), "PROBABLE": ("PROBABLE", "PROJECTED"),
                 "PROJECTED": ("PROBABLE", "PROJECTED")}


# --------------------------------------------------------------------------- player identity
class PlayerRef:
    """name -> NHL player id from the official box-score history (abbreviated "N. Nesterenko" names)."""

    def __init__(self, players: pd.DataFrame, goalies: pd.DataFrame):
        p = players[["player_id", "name", "team_id", "game_date", "position"]].copy()
        g = goalies[["player_id", "name", "team_id", "game_date"]].copy()
        g["position"] = "G"
        d = pd.concat([p, g], ignore_index=True).sort_values("game_date").drop_duplicates("player_id", keep="last")
        d["last"] = d["name"].map(C.last_name)
        d["ini"] = d["name"].map(C.first_initial)
        self.df = d.reset_index(drop=True)
        self.by_key: dict[tuple[str, str], list[int]] = defaultdict(list)
        for i, r in enumerate(self.df.itertuples()):
            self.by_key[(r.last, r.ini)].append(i)

    def resolve(self, name: str | None, team_id: int | None = None, goalie: bool | None = None) -> tuple[int | None, str]:
        if not name:
            return None, "no_name"
        key = (C.last_name(name), C.first_initial(name))
        idx = self.by_key.get(key, [])
        if not idx:
            return None, "unknown_player"
        c = self.df.iloc[idx]
        if goalie is not None:
            c2 = c[(c["position"] == "G") == goalie]
            c = c2 if len(c2) else c
        if team_id is not None:
            t = c[c["team_id"] == team_id]
            if len(t) == 1:
                return int(t["player_id"].iloc[0]), "name_team"
            if len(t) > 1:
                return None, "ambiguous_name_team"
        if len(c) == 1:
            return int(c["player_id"].iloc[0]), "name_only"
        return None, "ambiguous_name"


def player_ref() -> PlayerRef:
    return PlayerRef(data.load_kind("players"), data.load_kind("goalies"))


# --------------------------------------------------------------------------- schedule linking
class NextGame:
    """The team's next game starting strictly after a capture time (from the schedule snapshot)."""

    def __init__(self, sched: pd.DataFrame):
        self.by_team: dict[int, list[tuple[datetime, int]]] = defaultdict(list)
        self.start: dict[int, str] = {}
        for r in sched.itertuples():
            if not C.is_regular(r.game_id):
                continue
            st = r.start.to_pydatetime()
            self.start[int(r.game_id)] = C.iso(st)
            for t in (r.home_team_id, r.away_team_id):
                if pd.notna(t):
                    self.by_team[int(t)].append((st, int(r.game_id)))
        for v in self.by_team.values():
            v.sort()

    def after(self, team_id: int, captured: datetime) -> int | None:
        for st, gid in self.by_team.get(int(team_id), []):
            if st > captured:
                return gid
        return None


def _clean_su(su, cap: datetime) -> tuple[str | None, dict]:
    d = C.parse_ts(su)
    if d is None:
        return None, {}
    if d > cap:
        return None, {"source_updated_raw": str(su), "note": "source timestamp after our capture; dropped"}
    return C.iso(d), {}


# --------------------------------------------------------------------------- converters (pure)
def line_observations(rows: pd.DataFrame, nxt: NextGame, ref: PlayerRef, abbr: dict[int, str],
                      slugs: dict[str, str] | None = None) -> tuple[list[av.Observation], dict]:
    """DailyFaceoff line-combination rows (context/lines schema) -> one `line` observation per skater per capture
    (EV line, PP unit, PK unit in `detail`) and one `injury` observation per player on DailyFaceoff's injured list."""
    st = {"rows": int(len(rows)), "line_obs": 0, "injury_obs": 0, "unresolved": 0, "no_event": 0}
    out: list[av.Observation] = []
    if rows.empty:
        return out, st
    r = rows.copy()
    if "team_id" not in r or r["team_id"].isna().any():
        ab2id = {v: k for k, v in abbr.items()}
        r["team_id"] = r.get("team_id", pd.Series(index=r.index, dtype=float)).fillna(r["team_abbrev"].map(ab2id))
    for (tid, cap_s), g in r.groupby(["team_id", "observed_at_utc"], sort=False):
        cap = C.parse_ts(cap_s)
        if cap is None or pd.isna(tid):
            continue
        tid = int(tid)
        gid = nxt.after(tid, cap)
        if gid is None:
            st["no_event"] += len(g)
            continue
        ab = abbr.get(tid, str(g["team_abbrev"].iloc[0]))
        url = URL_LINES.format(slug=(slugs or {}).get(ab, ab.lower()))
        per: dict[Any, dict] = {}
        for x in g.itertuples():
            pid = x.player_id if pd.notna(getattr(x, "player_id", np.nan)) else None
            how = getattr(x, "resolution", None) or "archive"
            if pid is None:
                pid, how = ref.resolve(x.name, tid, goalie=False)
            if pid is None:
                st["unresolved"] += 1
                continue
            pid = int(pid)
            d = per.setdefault(pid, {"name": x.name, "gtd": False, "resolution": how, "src": x.lines_source,
                                     "upd": x.lines_updated_at_utc, "inj": None, "dfo_id": getattr(x, "dfo_player_id", None)})
            d["gtd"] = d["gtd"] or bool(x.game_time_decision)
            if x.category == "ev" and x.unit != "g":
                d["ev_unit"], d["slot"] = x.unit, x.slot
            elif x.category == "pp":
                d["pp_unit"] = x.unit
            elif x.category == "pk":
                d["pk_unit"] = x.unit
            elif x.category == "oi":
                d["inj"] = str(x.injury_status).lower() if pd.notna(x.injury_status) else None
        for pid, d in per.items():
            su, extra = _clean_su(d["upd"], cap)
            base = dict(sport=C.SPORT, event_id=str(gid), event_start_utc=nxt.start[gid], entity_id=str(pid),
                        entity_name=d["name"], team=ab, source=SRC_LINES, captured_utc=C.iso(cap), source_updated_utc=su,
                        source_url=url)
            if "ev_unit" in d:
                out.append(av.Observation(**base, kind="line", status="ACTIVE", certainty="PROJECTED", detail={
                    "ev_unit": d["ev_unit"], "slot": d.get("slot"), "pp_unit": d.get("pp_unit"), "pk_unit": d.get("pk_unit"),
                    "lines_source": d["src"], "game_time_decision": d["gtd"], "identity": d["resolution"], **extra}))
                st["line_obs"] += 1
            if d["inj"] in DFO_INJ:
                out.append(av.Observation(**base, kind="injury", status=DFO_INJ[d["inj"]], certainty="PROJECTED", detail={
                    "dfo_injury_status": d["inj"], "lines_source": d["src"], "identity": d["resolution"], **extra}))
                st["injury_obs"] += 1
    return out, st


def goalie_observations(rows: pd.DataFrame, sched_start: dict[int, str], ref: PlayerRef, abbr: dict[int, str]) \
        -> tuple[list[av.Observation], dict]:
    """DailyFaceoff starting-goalie rows (context/goalie_observations schema; post-start boxscore rows are skipped)."""
    st = {"rows": int(len(rows)), "starter_obs": 0, "unresolved": 0, "no_event": 0, "skipped_other_source": 0}
    out: list[av.Observation] = []
    if rows.empty:
        return out, st
    for x in rows.itertuples():
        if x.source != "dailyfaceoff":
            st["skipped_other_source"] += 1
            continue
        gid = pd.to_numeric(x.game_id, errors="coerce")
        if pd.isna(gid) or int(gid) not in sched_start:
            st["no_event"] += 1
            continue
        gid, tid = int(gid), int(x.team_id)
        cap = C.parse_ts(x.observed_at_utc)
        if cap is None or x.status not in GOALIE_STATUS:
            continue
        pid, how = (int(x.player_id), "archive") if pd.notna(x.player_id) else ref.resolve(x.player_name, tid, goalie=True)
        if pid is None:
            st["unresolved"] += 1
            continue
        status, cert = GOALIE_STATUS[x.status]
        su, extra = _clean_su(getattr(x, "source_reported_at_utc", None), cap)
        date = getattr(x, "game_date_et", None) or sched_start[gid][:10]
        out.append(av.Observation(
            sport=C.SPORT, event_id=str(gid), event_start_utc=sched_start[gid], entity_id=str(pid), entity_name=x.player_name,
            team=abbr.get(tid, str(tid)), kind="starter", status=status, certainty=cert, source=SRC_GOALIES,
            captured_utc=C.iso(cap), source_updated_utc=su, source_url=URL_GOALIES.format(date=date),
            detail={"dfo_status": x.status, "identity": how, **extra}))
        st["starter_obs"] += 1
    return out, st


def injury_observations(rows: pd.DataFrame, nxt: NextGame, ref: PlayerRef, abbr: dict[int, str]) \
        -> tuple[list[av.Observation], dict]:
    """ESPN injury feed rows (context/injuries schema) -> `injury` observations (certainty REPORTED) on the team's next game."""
    st = {"rows": int(len(rows)), "injury_obs": 0, "unresolved": 0, "no_event": 0, "unknown_status": 0}
    out: list[av.Observation] = []
    if rows.empty:
        return out, st
    rows = rows.rename(columns={"_observed_at_utc": "ledger_observed_utc"})
    for x in rows.itertuples():
        cap = C.parse_ts(getattr(x, "ledger_observed_utc", None))
        if cap is None or pd.isna(x.team_id):
            continue
        tid = int(x.team_id)
        status = ESPN_STATUS.get(str(x.status).strip().lower())
        if status is None:
            st["unknown_status"] += 1
            continue
        gid = nxt.after(tid, cap)
        if gid is None:
            st["no_event"] += 1
            continue
        pid, how = ref.resolve(x.player_name, tid)
        if pid is None:
            st["unresolved"] += 1
            continue
        out.append(av.Observation(
            sport=C.SPORT, event_id=str(gid), event_start_utc=nxt.start[gid], entity_id=str(pid), entity_name=x.player_name,
            team=abbr.get(tid, str(tid)), kind="injury", status=status, certainty="REPORTED", source=SRC_ESPN,
            captured_utc=C.iso(cap), source_updated_utc=None, source_url=URL_ESPN,
            detail={"espn_status": x.status, "type": getattr(x, "type", None), "detail": getattr(x, "detail", None),
                    "return_date": getattr(x, "return_date", None), "reported": getattr(x, "reported", None),
                    "identity": how}))
        st["injury_obs"] += 1
    return out, st


# --------------------------------------------------------------------------- official pregame roster (live, optional)
MIN_SKATERS, MAX_SKATERS = 17, 19


def roster_spots_observations(payload: dict, captured: datetime, candidates: dict[int, dict[str, str]], abbr: dict[int, str],
                              start_utc: str) -> tuple[list[av.Observation], dict]:
    """Official NHL play-by-play `rosterSpots` before the game -> CONFIRMED dressed skaters / INACTIVE scratches.

    The pre-game payload shape is NOT assumed: the roster is accepted only when the game has not started and each
    team lists 17-19 skaters and at least one goalie (a full-roster dump or a half-posted lineup is rejected, counted and
    never turned into a confirmation or a scratch). Goalies are never confirmed from dressed status (the backup is
    dressed too); a projected goalie missing from a complete roster is INACTIVE.
    `candidates` = team_id -> {player_id(str): name} of players we intend to project (scratch detection scope)."""
    st = {"game_state": payload.get("gameState"), "spots": len(payload.get("rosterSpots") or []), "teams_accepted": 0,
          "teams_rejected": 0, "dressed_obs": 0, "scratch_obs": 0}
    out: list[av.Observation] = []
    if payload.get("gameState") not in ("FUT", "PRE"):
        st["rejected_reason"] = f"game state {payload.get('gameState')!r} is not pregame"
        return out, st
    by_team: dict[int, list[dict]] = defaultdict(list)
    for s in payload.get("rosterSpots") or []:
        if s.get("teamId") is not None:
            by_team[int(s["teamId"])].append(s)
    gid = str(payload.get("id"))
    for tid, spots in by_team.items():
        sk = [s for s in spots if s.get("positionCode") != "G"]
        gl = [s for s in spots if s.get("positionCode") == "G"]
        if not (MIN_SKATERS <= len(sk) <= MAX_SKATERS and len(gl) >= 1):
            st["teams_rejected"] += 1
            continue
        st["teams_accepted"] += 1
        dressed = {str(s["playerId"]) for s in spots}
        ab = abbr.get(tid, str(tid))
        base = dict(sport=C.SPORT, event_id=gid, event_start_utc=start_utc, team=ab, source=SRC_OFFICIAL,
                    captured_utc=C.iso(captured), source_url=URL_PBP.format(game_id=gid))
        for s in sk:
            nm = " ".join(str((s.get(k) or {}).get("default", "")) for k in ("firstName", "lastName")).strip()
            out.append(av.Observation(**base, entity_id=str(s["playerId"]), entity_name=nm, kind="lineup", status="ACTIVE",
                                      certainty="CONFIRMED", detail={"position": s.get("positionCode"),
                                                                     "sweater": s.get("sweaterNumber")}))
            st["dressed_obs"] += 1
        for pid, nm in candidates.get(tid, {}).items():
            if pid not in dressed:
                out.append(av.Observation(**base, entity_id=pid, entity_name=nm, kind="lineup", status="INACTIVE",
                                          certainty="CONFIRMED", detail={"reason": "not on the official pregame roster"}))
                st["scratch_obs"] += 1
    return out, st


# --------------------------------------------------------------------------- ingest from the capture-worker archive
def dfo_slugs() -> dict[str, str]:
    try:
        import sys
        src = str(data.ROOT / "src")
        if src not in sys.path:
            sys.path.insert(0, src)
        from nhl_edge.data.lines import DFO_SLUGS
        return dict(DFO_SLUGS)
    except Exception:  # noqa: BLE001 - only used to build a source_url
        return {}


def _write_groups(groups: dict[Any, list[av.Observation]], out_root: str) -> dict:
    s = {"snapshots": 0, "observations": 0, "written": 0, "duplicate_snapshots": 0, "rejected": 0, "errors": []}
    for key, obs in sorted(groups.items(), key=lambda kv: str(kv[0])):
        if not obs:
            continue
        r = av.write_snapshot(obs, out_root, C.SPORT, min(o.captured_utc for o in obs))
        s["snapshots"] += 1
        s["observations"] += len(obs)
        s["written"] += r["written"]
        s["rejected"] += r["rejected"]
        s["duplicate_snapshots"] += int(r["duplicate"])
        s["errors"] += r.get("errors", [])[:2]
    return s


def ingest_archive(archive: str, out_root: str, now: datetime, lookback_h: float = 48.0) -> dict[str, Any]:
    """Convert the capture worker's DailyFaceoff / ESPN archive rows captured in [now - lookback, now] into pf_core
    availability snapshots (one snapshot per source per worker run). Idempotent: identical content is a no-op."""
    since = now - timedelta(hours=lookback_h)
    sched = C.schedule_asof(archive, now, back_days=int(lookback_h / 24) + 3)
    if sched.empty:
        return {"error": "no schedule snapshot in the archive window", "written": 0}
    nxt, ref, abbr = NextGame(sched), player_ref(), C.abbrev_by_id()
    slugs = dfo_slugs()
    stats: dict[str, Any] = {"lookback_h": lookback_h}
    # DailyFaceoff lines (+ DailyFaceoff injured-list flags)
    lines = C.read_kind(archive, "context/lines", since, now)
    if len(lines):
        lines = lines[lines["observed_at_utc"].map(lambda t: (C.parse_ts(t) or now) <= now)]
    groups: dict[str, list[av.Observation]] = {}
    lst = {"rows": 0, "line_obs": 0, "injury_obs": 0, "unresolved": 0, "no_event": 0}
    for run, g in (lines.groupby("_run_id", sort=False) if len(lines) else []):
        obs, st = line_observations(g, nxt, ref, abbr, slugs=slugs)
        groups[str(run)] = obs
        for k in lst:
            lst[k] += st.get(k, 0)
    stats["lines"] = {**lst, **_write_groups(groups, out_root)}
    # DailyFaceoff starting goalies
    gl = C.read_kind(archive, "context/goalie_observations", since, now)
    groups, gst = {}, {"rows": 0, "starter_obs": 0, "unresolved": 0, "no_event": 0, "skipped_other_source": 0}
    if len(gl):
        gl = gl[gl["observed_at_utc"].map(lambda t: (C.parse_ts(t) or now) <= now)]
    sched_start = {int(r.game_id): C.iso(r.start.to_pydatetime()) for r in sched.itertuples() if C.is_regular(r.game_id)}
    for run, g in (gl.groupby("_run_id", sort=False) if len(gl) else []):
        obs, st = goalie_observations(g, sched_start, ref, abbr)
        groups[str(run)] = obs
        for k in gst:
            gst[k] += st.get(k, 0)
    stats["goalies"] = {**gst, **_write_groups(groups, out_root)}
    # ESPN injuries
    inj = C.read_kind(archive, "context/injuries", since, now)
    groups, ist = {}, {"rows": 0, "injury_obs": 0, "unresolved": 0, "no_event": 0, "unknown_status": 0}
    if len(inj):
        inj = inj[inj["_observed_at_utc"].map(lambda t: (C.parse_ts(t) or now) <= now)]
    for run, g in (inj.groupby("_run_id", sort=False) if len(inj) else []):
        obs, st = injury_observations(g, nxt, ref, abbr)
        groups[str(run)] = obs
        for k in ist:
            ist[k] += st.get(k, 0)
    stats["injuries"] = {**ist, **_write_groups(groups, out_root)}
    stats["written"] = sum(stats[k]["written"] for k in ("lines", "goalies", "injuries"))
    newest = {}
    for name, df, col in (("lines", lines, "observed_at_utc"), ("goalies", gl, "observed_at_utc"), ("injuries", inj, "_observed_at_utc")):
        if len(df):
            newest[name] = max(df[col])
    stats["newest_source_capture_utc"] = newest
    return stats


# --------------------------------------------------------------------------- as-of loading + participation
def load_rows(out_root: str, now: datetime, back_days: int = 3) -> list[dict]:
    days = [(now - timedelta(days=d)).strftime("%Y-%m-%d") for d in range(back_days, -1, -1)]
    return av.load_snapshots(out_root, C.SPORT, days)


def capture_index(rows: list[dict]) -> dict:
    """Capture instants per full-list feed, to detect a cleared injury designation:
    ESPN is one league-wide list per capture; DailyFaceoff injured lists come with each team's line capture."""
    idx: dict = {"espn": set(), "dfo": defaultdict(set)}
    for r in rows:
        if r["source"] == SRC_ESPN:
            idx["espn"].add(r["captured_utc"])
        elif r["source"] == SRC_LINES and r["kind"] == "line":
            idx["dfo"][(r["event_id"], r["team"])].add(r["captured_utc"])
    return idx


def _cleared(inj: dict, idx: dict | None, cutoff: str) -> bool:
    """A listed designation is withdrawn when the same feed was captured again (before the cut-off) without listing the player."""
    if idx is None:
        return False
    if inj["source"] == SRC_ESPN:
        later = [t for t in idx["espn"] if inj["captured_utc"] < t < cutoff and t < inj["event_start_utc"]]
    elif inj["source"] == SRC_LINES:
        later = [t for t in idx["dfo"].get((inj["event_id"], inj["team"]), ()) if inj["captured_utc"] < t < cutoff]
    else:
        return False
    return bool(later)


def participation(latest: dict, event_id: str, entity_id: str, cutoff_utc: str, *, goalie: bool = False,
                  idx: dict | None = None) -> av.Participation:
    """pf_core resolution plus conservative NHL handling:
      * a designation from a full-list feed (ESPN, DailyFaceoff injured list) that a LATER capture no longer lists is
        treated as cleared (the latest-per-key rule alone would keep a stale OUT alive for the whole freshness window);
      * a DailyFaceoff injured-list flag (OUT / day-to-day) newer than the lineup slot caps a skater at UNCERTAIN;
      * a game-time-decision flag on the lineup slot caps LIKELY_ACTIVE at UNCERTAIN;
      * a REPORTED (unofficial) OUT that a lineup slot captured AT OR AFTER it contradicts is UNCERTAIN, not CONFIRMED_OUT
        (measured: such conflicts dressed in most cases). CONFIRMED scratches/inactives are never softened."""
    inj = latest.get((event_id, entity_id, "injury"))
    if inj is not None and _cleared(inj, idx, cutoff_utc):
        latest = {k: v for k, v in latest.items() if k != (event_id, entity_id, "injury")}
        inj = None
    p = av.resolve_participation(latest, event_id, entity_id, cutoff_utc, requires_lineup=goalie)
    line = latest.get((event_id, entity_id, "line"))
    reasons = list(p.reasons)
    if p.status == av.CONFIRMED_OUT and p.certainty == "REPORTED" and line is not None and line["captured_utc"] >= (inj or {}).get("captured_utc", "9"):
        reasons.append("lineup slot captured after the injury designation contradicts it")
        return av.Participation(av.UNCERTAIN, "REPORTED", p.source, p.captured_utc, p.age_minutes, reasons)
    if p.status not in (av.LIKELY_ACTIVE, av.CONFIRMED_ACTIVE) or p.certainty == "CONFIRMED":
        return p
    if inj is not None and inj.get("source") == SRC_LINES and inj["status"] in ("OUT", "QUESTIONABLE", "DOUBTFUL"):
        reasons.append(f"DailyFaceoff injured list: {inj['detail'].get('dfo_injury_status')}")
        return av.Participation(av.UNCERTAIN, p.certainty, p.source, p.captured_utc, p.age_minutes, reasons)
    if line is not None and line.get("detail", {}).get("game_time_decision"):
        reasons.append("DailyFaceoff marks a game-time decision")
        return av.Participation(av.UNCERTAIN, p.certainty, p.source, p.captured_utc, p.age_minutes, reasons)
    return p


def participation_dict(p: av.Participation) -> dict:
    return {"status": p.status, "certainty": p.certainty, "source": p.source, "captured_utc": p.captured_utc,
            "reasons": list(p.reasons)}


# --------------------------------------------------------------------------- P(start) for the saves projection
PRIOR_HIT, PRIOR_N = 9.0, 10.0   # Beta prior mean 0.9 with weight 10: the data decides once a few dozen team-games exist


def start_probability_table(archive: str, now: datetime, lead_buckets=((0, 3), (3, 8), (8, 36)), back_days: int = 30) -> dict:
    """P(named goalie starts | DailyFaceoff status, hours to puck drop), estimated from OUR archive: for every team-game
    already played, the last observation captured >= `lead` hours before the start vs the boxscore starter.
    Returns {status: {bucket: {"n", "hits", "p"}}}; p = (hits + 9) / (n + 10) so a thin sample cannot claim certainty."""
    now_ = now
    gobs = C.read_kind(archive, "context/goalie_observations", now_ - timedelta(days=back_days), now_)
    if gobs.empty:
        return {}
    gobs = gobs[gobs["source"] == "dailyfaceoff"].copy()
    gobs["game_id"] = pd.to_numeric(gobs["game_id"], errors="coerce")
    gobs = gobs.dropna(subset=["game_id", "team_id"])
    gobs["game_id"] = gobs["game_id"].astype("int64")
    gobs["team_id"] = gobs["team_id"].astype("int64")
    gobs["obs"] = pd.to_datetime(gobs["observed_at_utc"], utc=True)
    sched = C.schedule_asof(archive, now_, back_days=back_days + 3)[["game_id", "start"]]
    gobs = gobs.merge(sched, on="game_id")
    gobs = gobs[gobs["obs"] < gobs["start"]]
    gobs["lead_h"] = (gobs["start"] - gobs["obs"]).dt.total_seconds() / 3600
    gl = data.load_kind("goalies")
    starters = gl[gl["starter"]][["game_id", "team_id", "player_id", "name"]]
    starters = starters.assign(sl=starters["name"].map(C.last_name), si=starters["name"].map(C.first_initial))
    st = starters.rename(columns={"player_id": "act_id"})
    out: dict[str, dict] = {}
    gobs["pl"] = gobs["player_name"].map(C.last_name)
    gobs["pi"] = gobs["player_name"].map(C.first_initial)
    for lo, hi in lead_buckets:
        b = gobs[(gobs["lead_h"] >= lo) & (gobs["lead_h"] < hi)]
        b = b.sort_values("obs").groupby(["game_id", "team_id"], as_index=False).tail(1)
        j = b.merge(st[["game_id", "team_id", "sl", "si"]], on=["game_id", "team_id"])
        j["hit"] = (j["pl"] == j["sl"]) & (j["pi"] == j["si"])
        for status, g in j.groupby("status"):
            n, h = int(len(g)), int(g["hit"].sum())
            out.setdefault(status, {})[f"{lo}-{hi}h"] = {"n": n, "hits": h, "p": round((h + PRIOR_HIT) / (n + PRIOR_N), 4)}
    return out


def p_start(table: dict, dfo_status: str | None, hours_to_start: float) -> tuple[float | None, str]:
    """P(the named goalie starts). None when DailyFaceoff names nobody; the prior alone when no completed team-game has
    carried this status at this lead time yet (stated in the basis, so a thin sample is never presented as measured)."""
    if not dfo_status:
        return None, "no DailyFaceoff status"
    for key, v in (table.get(dfo_status) or {}).items():
        lo, hi = (float(x) for x in key.rstrip("h").split("-"))
        if lo <= hours_to_start < hi:
            return v["p"], f"{dfo_status} @ {key} before start: {v['hits']}/{v['n']} named goalies started (prior {PRIOR_HIT:.0f}/{PRIOR_N:.0f})"
    return round(PRIOR_HIT / PRIOR_N, 4), f"{dfo_status}: prior only ({PRIOR_HIT:.0f}/{PRIOR_N:.0f}); no completed team-game with this status at this lead yet"
