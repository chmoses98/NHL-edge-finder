"""Resolve a Kalshi NHL player contract to an official NHL player id (fail-closed).

Observed live shapes (2026-09-29 production board, docs/KALSHI_MARKET_MAP.md):

    KXNHLPTS-26SEP29CHIVGK-CHIBBYRAM24-1          title "Bowen Byram: 1+ points"      floor_strike 0.5
    KXNHLGOAL-26SEP29CHIVGK-CHIAMANGIAPANE26-2     title "Andrew Mangiapane: 2+ goals"  floor_strike 1.5
    KXNHLSAVE-26SEP29CHIVGK-CHISKNIGHT30-26        title "Spencer Knight: 26+ saves"    floor_strike 25.5
    KXNHLFIRSTGOAL-26SEP29CHIVGK-CHIALEVSHUNOV55   title "Artyom Levshunov: First Goalscorer"

Market suffix = <Kalshi team code><first initial><LAST NAME, possibly truncated (MTLJSLAFKOVSK20)><jersey>[-<threshold>].
The team code must be one of the two codes in the event suffix. Resolution: (team, jersey) against the point-in-time
roster, confirmed by the first initial and the last-name fragment, cross-checked with the title's full name. Any
mismatch or ambiguity returns no player id and a reason: the contract stays unpriced rather than priced for the wrong
person.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from nhl_edge.data.lines import fold
from nhl_edge.identity.teams import TeamIdentityError, TeamRegistry, registry
from nhl_edge.kalshi.ticker import parse_ticker

SUFFIX_RE = re.compile(r"^(?P<body>[A-Z]+?)(?P<num>\d{1,2})(?:-(?P<thr>\d+))?$")


@dataclass(frozen=True)
class PlayerRef:
    team_code: str | None
    team_id: int | None
    initial: str | None
    last_fragment: str | None
    jersey: int | None
    threshold_suffix: int | None
    name: str | None


def parse_player_market(ticker: str, title: str | None = None, reg: TeamRegistry | None = None) -> PlayerRef | None:
    reg = reg or registry()
    pt = parse_ticker(ticker, reg.tricodes | set(reg.by_abbrev_map))
    m = SUFFIX_RE.match(pt.market_suffix or "")
    if not m:
        return None
    body = m["body"]
    codes = [c for c in (pt.away_tricode, pt.home_tricode) if c]
    if pt.away_tricode and pt.home_tricode:
        teams = pt.away_tricode + pt.home_tricode
        codes += [teams[:k] for k in range(2, len(teams) - 1)] + [teams[k:] for k in range(2, len(teams) - 1)]
    code = None
    for c in sorted(set(codes), key=len, reverse=True):
        if body.startswith(c) and len(body) > len(c) + 1:
            try:
                reg.by_abbrev(c)
            except TeamIdentityError:
                continue
            code = c
            break
    if code is None:
        return None
    rest = body[len(code):]
    name = title.split(":")[0].strip() if title and ":" in title else None
    try:
        tid = reg.by_abbrev(code).team_id
    except TeamIdentityError:
        tid = None
    return PlayerRef(code, tid, rest[0], rest[1:], int(m["num"]), int(m["thr"]) if m["thr"] else None, name)


def resolve_player(ref: PlayerRef, roster: list[dict[str, Any]]) -> tuple[int | None, str]:
    """``roster`` rows: {player_id, team_id, sweater, first_name, last_name, position}. Returns (player_id, how)."""
    if ref.team_id is None:
        return None, "team code not resolvable"
    team = [r for r in roster if r.get("team_id") == ref.team_id]
    if not team:
        return None, "no roster for team"
    frag = fold(ref.last_fragment)
    full_last = fold(ref.name.split(" ", 1)[1]) if ref.name and " " in ref.name else None

    def name_ok(r: dict[str, Any]) -> bool:
        ln = fold(r.get("last_name"))
        fn = fold(r.get("first_name"))
        if not ln:
            return False
        frag_ok = ln.startswith(frag) or frag.startswith(ln) or (len(frag) >= 4 and frag in ln)
        init_ok = not ref.initial or not fn or fn[0] == ref.initial.lower()
        return frag_ok and init_ok

    by_num = [r for r in team if r.get("sweater") is not None and int(r["sweater"]) == ref.jersey]
    hits = [r for r in by_num if name_ok(r)]
    if len(hits) == 1:
        return int(hits[0]["player_id"]), "team+jersey+name"
    by_name = [r for r in team if name_ok(r) and (full_last is None or fold(r.get("last_name")) == full_last or full_last.startswith(fold(r.get("last_name"))))]
    if len(by_name) == 1:
        return int(by_name[0]["player_id"]), "team+name (jersey differs)"
    if len(by_name) > 1:
        return None, "ambiguous name on team"
    return None, "no roster match"
