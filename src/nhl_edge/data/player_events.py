"""Official NHL player-event data for PLAYER_SIM_V1 (RESEARCH_ONLY): pure parsers + one per-game derivation.

Three official NHL payloads per completed game, all free and unauthenticated:

* ``api-web.nhle.com/v1/gamecenter/{id}/boxscore``  -> per-player official line (goals, assists, points, SOG, TOI,
  PP goals, PIM, shifts) and per-goalie line (saves, shots against, goals against, starter flag, TOI). This is the
  settlement-grade record: Kalshi player props settle on the official stat line.
* ``api-web.nhle.com/v1/gamecenter/{id}/play-by-play`` -> every goal with scorer, primary and secondary assist,
  ``situationCode`` (skaters + goalie-in-net for both sides) and game clock; every unblocked / blocked shot attempt
  with shooter, coordinates, shot type. Shootout plays (``periodType == "SO"``) are dropped: a shootout "goal" is
  not a goal for any player statistic.
* ``api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId={id}`` -> every shift (player, period, start, end).

From those :func:`derive_game` builds, for ONE game:

* ``players``   one row per skater: official line + A1/A2 split + time on ice by team strength state (EV / PP / SH /
  EA = own goalie pulled / EN = opponent goalie pulled) + on-ice goals for/against by strength + shots by strength.
* ``goalies``   one row per goalie appearance (official saves / shots against / goals against / starter / TOI).
* ``goals``     one row per (non-shootout) goal: time, strength for the scoring team, score before, scorer, A1, A2,
  goalie in net, the skaters of BOTH teams on the ice (from shifts), empty-net flag.
* ``shots``     one row per shot attempt (goal / shot-on-goal / missed / blocked): shooter, x, y, type, strength,
  seconds since the team's previous attempt (rebound proxy). Inputs to the shot-quality (xG) model.
* ``coice``     one row per same-team skater pair that shared >= 60 s of ice: shared seconds at EV / PP / SH.

The strength timeline comes from ``situationCode`` on play-by-play events: the state holding in second ``k`` is the
code of the last event at or before ``k`` in that period. A penalty that expires between events is therefore
attributed to the power play until the next event (typically seconds). Documented in docs/research/PLAYER_SIM_V1.md.

Everything here is a pure function over parsed JSON so it is tested from fixtures; the network seam lives in
``nhl_edge.data.player_history`` and the live settle job.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

import numpy as np
import pandas as pd

SCHEMA_VERSION = "nhl-player-events-1.0"
STATES: tuple[str, ...] = ("EV", "PP", "SH", "EA", "EN")
PERIOD_S = 1200
MIN_SHARED_S = 60
SHOT_EVENTS = {"goal": "GOAL", "shot-on-goal": "SOG", "missed-shot": "MISS", "blocked-shot": "BLOCK"}


def mmss(v: Any) -> int | None:
    """'12:34' -> 754 seconds; None for anything unparseable."""
    if v is None:
        return None
    try:
        m, s = str(v).split(":")
        return int(m) * 60 + int(s)
    except (ValueError, TypeError):
        return None


def game_seconds(period: int, t_in_period: int) -> int:
    """Seconds from the opening faceoff. Every period (including a playoff OT) is laid out on a 20-minute grid."""
    return (int(period) - 1) * PERIOD_S + int(t_in_period)


def parse_situation(code: Any) -> dict[str, int] | None:
    """NHL ``situationCode`` 'AGAS HSHG': away goalie in net, away skaters, home skaters, home goalie in net."""
    s = str(code or "")
    if len(s) != 4 or not s.isdigit():
        return None
    return {"away_g": int(s[0]), "away_sk": int(s[1]), "home_sk": int(s[2]), "home_g": int(s[3])}


def team_state(sit: dict[str, int] | None, home: bool) -> str | None:
    """Strength state for one team: EN (opponent net empty), EA (own net empty / extra attacker), PP, SH, EV."""
    if sit is None:
        return None
    own_sk, opp_sk = (sit["home_sk"], sit["away_sk"]) if home else (sit["away_sk"], sit["home_sk"])
    own_g, opp_g = (sit["home_g"], sit["away_g"]) if home else (sit["away_g"], sit["home_g"])
    if own_sk <= 1 or opp_sk <= 0:  # penalty shot
        return "EV"
    if opp_g == 0:
        return "EN"
    if own_g == 0:
        return "EA"
    if own_sk > opp_sk:
        return "PP"
    if own_sk < opp_sk:
        return "SH"
    return "EV"


# ---------------------------------------------------------------------------------------------------------------------
# boxscore
# ---------------------------------------------------------------------------------------------------------------------
def _name(v: Any) -> str | None:
    if isinstance(v, dict):
        return v.get("default")
    return v if isinstance(v, str) else None


def _frac(v: Any) -> tuple[int | None, int | None]:
    """'17/19' -> (17, 19)."""
    try:
        a, b = str(v).split("/")
        return int(a), int(b)
    except (ValueError, TypeError):
        return None, None


def parse_box_players(box: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """(skater rows, goalie rows) from a boxscore. ``team_id`` from the side the player is listed under."""
    skaters: list[dict[str, Any]] = []
    goalies: list[dict[str, Any]] = []
    pbg = box.get("playerByGameStats") or {}
    for side in ("homeTeam", "awayTeam"):
        team = box.get(side) or {}
        tid = team.get("id")
        st = pbg.get(side) or {}
        for grp in ("forwards", "defense"):
            for p in st.get(grp) or []:
                skaters.append({
                    "player_id": p.get("playerId"), "team_id": tid, "is_home": side == "homeTeam", "sweater": p.get("sweaterNumber"),
                    "name": _name(p.get("name")), "position": p.get("position"), "goals": p.get("goals"), "assists": p.get("assists"),
                    "points": p.get("points"), "sog": p.get("sog") if p.get("sog") is not None else p.get("shots"), "pp_goals": p.get("powerPlayGoals"),
                    "pim": p.get("pim"), "shifts": p.get("shifts"), "toi_s": mmss(p.get("toi")), "plus_minus": p.get("plusMinus"),
                })
        for g in st.get("goalies") or []:
            ev_sv, ev_sa = _frac(g.get("evenStrengthShotsAgainst"))
            pp_sv, pp_sa = _frac(g.get("powerPlayShotsAgainst"))
            sh_sv, sh_sa = _frac(g.get("shorthandedShotsAgainst"))
            sv, sa = _frac(g.get("saveShotsAgainst"))
            saves = g.get("saves") if g.get("saves") is not None else sv
            shots_against = g.get("shotsAgainst") if g.get("shotsAgainst") is not None else sa
            goalies.append({
                "player_id": g.get("playerId"), "team_id": tid, "is_home": side == "homeTeam", "sweater": g.get("sweaterNumber"),
                "name": _name(g.get("name")), "starter": bool(g.get("starter", False)), "toi_s": mmss(g.get("toi")), "saves": saves,
                "shots_against": shots_against, "goals_against": g.get("goalsAgainst"), "decision": g.get("decision"),
                "ev_saves": ev_sv, "ev_sa": ev_sa, "pp_saves": pp_sv, "pp_sa": pp_sa, "sh_saves": sh_sv, "sh_sa": sh_sa,
            })
    return skaters, goalies


# ---------------------------------------------------------------------------------------------------------------------
# play-by-play
# ---------------------------------------------------------------------------------------------------------------------
def _plays(pbp: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for p in pbp.get("plays") or []:
        if not isinstance(p, dict):
            continue
        pdsc = p.get("periodDescriptor") or {}
        per = pdsc.get("number")
        ptype = pdsc.get("periodType")
        t = mmss(p.get("timeInPeriod"))
        if per is None or t is None:
            continue
        out.append(p | {"_period": int(per), "_ptype": ptype, "_t": game_seconds(int(per), t)})
    out.sort(key=lambda p: (p["_period"], p["_t"], p.get("sortOrder") or 0))
    return out


def state_timeline(plays: list[dict[str, Any]], n_seconds: int) -> tuple[np.ndarray, np.ndarray]:
    """(home_state_idx, away_state_idx) per game second, index into STATES; -1 where unknown (no event yet)."""
    h = np.full(n_seconds, -1, dtype=np.int8)
    a = np.full(n_seconds, -1, dtype=np.int8)
    by_period: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for p in plays:
        if p["_ptype"] != "SO":
            by_period[p["_period"]].append(p)
    for per, ps in by_period.items():
        start = (per - 1) * PERIOD_S
        end = min(start + PERIOD_S, n_seconds)
        codes = [(p["_t"], parse_situation(p.get("situationCode"))) for p in ps]
        codes = [(t, s) for t, s in codes if s is not None]
        if not codes:
            continue
        cur = codes[0][1]
        j = 0
        for k in range(start, end):
            while j < len(codes) and codes[j][0] <= k:
                cur = codes[j][1]
                j += 1
            h[k] = STATES.index(team_state(cur, True))
            a[k] = STATES.index(team_state(cur, False))
    return h, a


def parse_goals(plays: list[dict[str, Any]], home_id: int, away_id: int) -> list[dict[str, Any]]:
    goals = []
    hs = as_ = 0
    for p in plays:
        if p.get("typeDescKey") != "goal" or p["_ptype"] == "SO":
            continue
        d = p.get("details") or {}
        tid = d.get("eventOwnerTeamId")
        home = tid == home_id
        sit = parse_situation(p.get("situationCode"))
        goals.append({
            "period": p["_period"], "period_type": p["_ptype"], "t_s": p["_t"], "team_id": tid, "is_home": home,
            "scorer_id": d.get("scoringPlayerId"), "a1_id": d.get("assist1PlayerId"), "a2_id": d.get("assist2PlayerId"),
            "goalie_in_net_id": d.get("goalieInNetId"), "situation_code": p.get("situationCode"), "strength": team_state(sit, home),
            "score_for_before": hs if home else as_, "score_against_before": as_ if home else hs, "shot_type": d.get("shotType"),
            "x": d.get("xCoord"), "y": d.get("yCoord"),
        })
        if home:
            hs += 1
        else:
            as_ += 1
    return goals


def parse_shots(plays: list[dict[str, Any]], home_id: int, player_team: dict[int, Any] | None = None) -> list[dict[str, Any]]:
    """Every non-shootout shot attempt, with the seconds since the same team's previous attempt (rebound proxy).
    A blocked-shot event may be owned by the blocking team; the shooter's team comes from ``player_team`` then."""
    out = []
    last_t: dict[Any, int] = {}
    for p in plays:
        kind = SHOT_EVENTS.get(p.get("typeDescKey") or "")
        if kind is None or p["_ptype"] == "SO":
            continue
        d = p.get("details") or {}
        tid = d.get("eventOwnerTeamId")
        shooter = d.get("scoringPlayerId") if kind == "GOAL" else d.get("shootingPlayerId")
        if kind == "BLOCK" and player_team and shooter in player_team:
            tid = player_team[shooter]
        home = tid == home_id
        sit = parse_situation(p.get("situationCode"))
        prev = last_t.get(tid)
        out.append({
            "period": p["_period"], "t_s": p["_t"], "team_id": tid, "is_home": home, "shooter_id": shooter, "kind": kind,
            "x": d.get("xCoord"), "y": d.get("yCoord"), "shot_type": d.get("shotType"), "zone": d.get("zoneCode"),
            "strength": team_state(sit, home), "since_prev_s": (p["_t"] - prev) if prev is not None else None,
            "goalie_in_net_id": d.get("goalieInNetId"),
        })
        last_t[tid] = p["_t"]
    return out


# ---------------------------------------------------------------------------------------------------------------------
# shifts
# ---------------------------------------------------------------------------------------------------------------------
def parse_shifts(payload: Any) -> list[dict[str, Any]]:
    """Shift rows (typeCode 517 or no typeCode) -> [{player_id, team_id, start_s, end_s}] in game seconds."""
    data = payload.get("data") if isinstance(payload, dict) else payload
    out = []
    for r in data or []:
        if not isinstance(r, dict):
            continue
        tc = r.get("typeCode")
        if tc not in (None, 517):
            continue
        per = r.get("period")
        s, e = mmss(r.get("startTime")), mmss(r.get("endTime"))
        if per is None or s is None or e is None or r.get("playerId") is None:
            continue
        if e < s:
            continue
        out.append({"player_id": int(r["playerId"]), "team_id": r.get("teamId"), "start_s": game_seconds(int(per), s),
                    "end_s": game_seconds(int(per), e)})
    return out


def presence(shifts: list[dict[str, Any]], n_seconds: int) -> dict[int, np.ndarray]:
    """player -> boolean[n_seconds]; second k is on-ice when a shift covers [k, k+1)."""
    pres: dict[int, np.ndarray] = {}
    for r in shifts:
        arr = pres.setdefault(r["player_id"], np.zeros(n_seconds, dtype=bool))
        s, e = max(0, r["start_s"]), min(n_seconds, r["end_s"])
        if e > s:
            arr[s:e] = True
    return pres


def on_ice_at(shifts: list[dict[str, Any]], t_s: int, team_id: Any, exclude: set[int]) -> list[int]:
    """Skaters of ``team_id`` on the ice for an event at ``t_s``: shift start < t <= end (a goal ends the shift)."""
    return sorted({r["player_id"] for r in shifts if r["team_id"] == team_id and r["start_s"] < t_s <= r["end_s"] and r["player_id"] not in exclude})


# ---------------------------------------------------------------------------------------------------------------------
# one game
# ---------------------------------------------------------------------------------------------------------------------
def derive_game(box: dict[str, Any], pbp: dict[str, Any], shifts_payload: Any, meta: dict[str, Any] | None = None) -> dict[str, pd.DataFrame]:
    """All PLAYER_SIM_V1 tables for one completed game. ``meta`` columns (season, game_date, ...) are stamped on every
    row. Missing shifts never drop the official lines: TOI-by-strength / on-ice columns are then null and
    ``shifts_ok`` is False."""
    meta = dict(meta or {})
    if not meta.get("game_date"):
        meta["game_date"] = str(box.get("gameDate") or pbp.get("gameDate") or "")[:10] or None
    gid = int(box.get("id") or pbp.get("id"))
    home_id = (box.get("homeTeam") or {}).get("id") or (pbp.get("homeTeam") or {}).get("id")
    away_id = (box.get("awayTeam") or {}).get("id") or (pbp.get("awayTeam") or {}).get("id")
    skaters, goalies = parse_box_players(box)
    plays = _plays(pbp)
    max_t = max([p["_t"] for p in plays if p["_ptype"] != "SO"] + [3 * PERIOD_S])
    n_sec = int(max(3 * PERIOD_S, ((max_t - 1) // PERIOD_S + 1) * PERIOD_S)) if max_t > 3 * PERIOD_S else 3 * PERIOD_S
    hstate, astate = state_timeline(plays, n_sec)
    goals = parse_goals(plays, home_id, away_id)
    shots = parse_shots(plays, home_id, {sk["player_id"]: sk["team_id"] for sk in skaters})
    shifts = parse_shifts(shifts_payload)
    goalie_ids = {g["player_id"] for g in goalies}
    shifts_sk = [r for r in shifts if r["player_id"] not in goalie_ids]
    shifts_ok = len(shifts_sk) > 0
    pres = presence(shifts_sk, n_sec) if shifts_ok else {}

    # goals: on-ice skaters of both teams
    for g in goals:
        if shifts_ok:
            opp = away_id if g["is_home"] else home_id
            g["for_on_ice"] = on_ice_at(shifts_sk, g["t_s"], g["team_id"], set())
            g["against_on_ice"] = on_ice_at(shifts_sk, g["t_s"], opp, set())
        else:
            g["for_on_ice"], g["against_on_ice"] = None, None
        g["empty_net"] = g["strength"] == "EN"

    # A1 / A2 counts, shots by strength
    a1 = defaultdict(int)
    a2 = defaultdict(int)
    for g in goals:
        if g["a1_id"]:
            a1[g["a1_id"]] += 1
        if g["a2_id"]:
            a2[g["a2_id"]] += 1
    sog_by = defaultdict(lambda: defaultdict(int))
    att_by = defaultdict(lambda: defaultdict(int))
    for s in shots:
        if s["shooter_id"] is None or s["strength"] is None:
            continue
        att_by[s["shooter_id"]][s["strength"]] += 1
        if s["kind"] in ("GOAL", "SOG"):
            sog_by[s["shooter_id"]][s["strength"]] += 1

    # on-ice GF / GA by strength
    gf = defaultdict(lambda: defaultdict(int))
    ga = defaultdict(lambda: defaultdict(int))
    for g in goals:
        if g["for_on_ice"] is None:
            continue
        for p in g["for_on_ice"]:
            gf[p][g["strength"]] += 1
        opp_state = {"PP": "SH", "SH": "PP", "EN": "EA", "EA": "EN"}.get(g["strength"], "EV")
        for p in g["against_on_ice"]:
            ga[p][opp_state] += 1

    rows = []
    for sk in skaters:
        pid = sk["player_id"]
        r = dict(sk)
        r["a1"], r["a2"] = a1.get(pid, 0), a2.get(pid, 0)
        st = hstate if sk["is_home"] else astate
        arr = pres.get(pid)
        for i, s in enumerate(STATES):
            r[f"toi_{s.lower()}_s"] = int((arr & (st == i)).sum()) if arr is not None else None
            r[f"gf_{s.lower()}"] = gf[pid].get(s, 0) if shifts_ok else None
            r[f"ga_{s.lower()}"] = ga[pid].get(s, 0) if shifts_ok else None
            r[f"sog_{s.lower()}"] = sog_by[pid].get(s, 0)
            r[f"att_{s.lower()}"] = att_by[pid].get(s, 0)
        r["toi_ot_s"] = int(arr[3 * PERIOD_S:].sum()) if arr is not None else None
        r["toi_shift_s"] = int(arr.sum()) if arr is not None else None
        r["shifts_ok"] = shifts_ok
        rows.append(r)

    # co-ice pairs
    coice = []
    if shifts_ok:
        for tid, st in ((home_id, hstate), (away_id, astate)):
            ids = sorted({sk["player_id"] for sk in skaters if sk["team_id"] == tid and sk["player_id"] in pres})
            if len(ids) < 2:
                continue
            P = np.stack([pres[i] for i in ids]).astype(np.float32)
            mats = {s: (P * (st == STATES.index(s))) @ P.T for s in ("EV", "PP", "SH")}
            tot = P @ P.T
            for i in range(len(ids)):
                for j in range(i + 1, len(ids)):
                    if tot[i, j] >= MIN_SHARED_S:
                        coice.append({"team_id": tid, "p1": ids[i], "p2": ids[j], "shared_s": int(tot[i, j]), "shared_ev_s": int(mats["EV"][i, j]),
                                      "shared_pp_s": int(mats["PP"][i, j]), "shared_sh_s": int(mats["SH"][i, j])})

    # team seconds by state (context for rates)
    team_state_s = []
    for tid, st, home in ((home_id, hstate, True), (away_id, astate, False)):
        team_state_s.append({"team_id": tid, "is_home": home, **{f"sec_{s.lower()}": int((st == i).sum()) for i, s in enumerate(STATES)},
                             "sec_unknown": int((st < 0).sum()), "n_seconds": n_sec})

    base = {"game_id": gid, "home_team_id": home_id, "away_team_id": away_id, "schema_version": SCHEMA_VERSION} | meta
    out = {
        "players": pd.DataFrame([base | r for r in rows]),
        "goalies": pd.DataFrame([base | g for g in goalies]),
        "goals": pd.DataFrame([base | g for g in goals]),
        "shots": pd.DataFrame([base | s for s in shots]),
        "coice": pd.DataFrame([base | c for c in coice]),
        "team_states": pd.DataFrame([base | t for t in team_state_s]),
    }
    return out


def check_game(tables: dict[str, pd.DataFrame], box: dict[str, Any]) -> list[str]:
    """Consistency checks between the derived tables and the official boxscore (reported, never 'fixed')."""
    issues = []
    pl, gl = tables["players"], tables["goals"]
    if len(pl):
        if (pl["a1"] + pl["a2"] != pl["assists"].fillna(-1)).any():
            n = int((pl["a1"] + pl["a2"] != pl["assists"].fillna(-1)).sum())
            issues.append(f"a1+a2 != official assists for {n} players")
        g_pbp = gl.groupby("scorer_id").size() if len(gl) else pd.Series(dtype=int)
        g_off = pl.set_index("player_id")["goals"]
        diff = [p for p, v in g_off.items() if int(v or 0) != int(g_pbp.get(p, 0))]
        if diff:
            issues.append(f"pbp goals != official goals for {len(diff)} players")
    for side, key in (("homeTeam", True), ("awayTeam", False)):
        sc = (box.get(side) or {}).get("score")
        lpt = (box.get("gameOutcome") or {}).get("lastPeriodType")
        if sc is None or not len(gl):
            continue
        n = int((gl["is_home"] == key).sum())
        other = (box.get("awayTeam" if key else "homeTeam") or {}).get("score")
        expected = sc - (1 if (lpt == "SO" and other is not None and sc > other) else 0)
        if n != expected:
            issues.append(f"{side} pbp goals {n} != official {expected}")
    return issues
