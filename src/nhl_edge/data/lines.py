"""DailyFaceoff line combinations -> point-in-time deployment observations (PLAYER_SIM_V1, RESEARCH_ONLY).

``https://www.dailyfaceoff.com/teams/{slug}/line-combinations`` embeds a ``__NEXT_DATA__`` JSON whose
``props.pageProps.combinations`` holds, per team: ``updatedAt`` (when DailyFaceoff last changed the lines),
``sourceName`` (e.g. "Warmups (<reporter>)", "Practice", "Projected"), and ``players`` rows with
``categoryIdentifier`` (ev / pp / pk / oi) + ``groupIdentifier`` (f1..f4, d1..d3, g1/g2, pp1/pp2, pk1/pk2, ir) +
``jerseyNumber`` + ``name`` + ``injuryStatus`` + ``gameTimeDecision``.

The page carries NO historical lines, so these observations exist only from the day this repository started archiving
them (the ``context/lines`` kind). Historical backtests never use them; they use the previous game's shift-derived
deployment instead (docs/POINT_IN_TIME.md). Resolution to NHL player ids is by (team, jersey number) and verified by
last name; a mismatch is left unresolved, never guessed.
"""

from __future__ import annotations

import json
import re
import unicodedata
from typing import Any

NEXT_DATA_RE = re.compile(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', re.S)

# DailyFaceoff team slugs keyed by NHL abbreviation (full club names, lower-case, hyphenated).
DFO_SLUGS: dict[str, str] = {
    "ANA": "anaheim-ducks", "BOS": "boston-bruins", "BUF": "buffalo-sabres", "CAR": "carolina-hurricanes", "CBJ": "columbus-blue-jackets",
    "CGY": "calgary-flames", "CHI": "chicago-blackhawks", "COL": "colorado-avalanche", "DAL": "dallas-stars", "DET": "detroit-red-wings",
    "EDM": "edmonton-oilers", "FLA": "florida-panthers", "LAK": "los-angeles-kings", "MIN": "minnesota-wild", "MTL": "montreal-canadiens",
    "NJD": "new-jersey-devils", "NSH": "nashville-predators", "NYI": "new-york-islanders", "NYR": "new-york-rangers", "OTT": "ottawa-senators",
    "PHI": "philadelphia-flyers", "PIT": "pittsburgh-penguins", "SEA": "seattle-kraken", "SJS": "san-jose-sharks", "STL": "st-louis-blues",
    "TBL": "tampa-bay-lightning", "TOR": "toronto-maple-leafs", "UTA": "utah-mammoth", "VAN": "vancouver-canucks", "VGK": "vegas-golden-knights",
    "WPG": "winnipeg-jets", "WSH": "washington-capitals",
}


def fold(s: str | None) -> str:
    """Accent- and case-insensitive letters only ('Stützle' -> 'stutzle')."""
    s = unicodedata.normalize("NFKD", s or "")
    return re.sub(r"[^a-z]", "", "".join(ch for ch in s if not unicodedata.combining(ch)).lower())


def parse_line_page(html: str | bytes) -> dict[str, Any] | None:
    """Raw page -> the ``combinations`` dict, or None when the page shape is not recognised."""
    text = html.decode("utf-8", "replace") if isinstance(html, bytes) else html
    m = NEXT_DATA_RE.search(text)
    if not m:
        return None
    try:
        nd = json.loads(m.group(1))
    except json.JSONDecodeError:
        return None
    c = ((nd.get("props") or {}).get("pageProps") or {}).get("combinations")
    return c if isinstance(c, dict) and isinstance(c.get("players"), list) else None


def line_rows(combo: dict[str, Any], team_abbrev: str, observed_at_utc: str) -> list[dict[str, Any]]:
    """One row per (player, deployment slot). ``unit`` is f1..f4 / d1..d3 / g1.. / pp1 / pp2 / pk1 / pk2 / ir."""
    rows = []
    for p in combo.get("players") or []:
        rows.append({
            "team_abbrev": team_abbrev, "category": p.get("categoryIdentifier"), "unit": p.get("groupIdentifier"),
            "slot": p.get("positionIdentifier"), "jersey": p.get("jerseyNumber"), "name": p.get("name"), "injury_status": p.get("injuryStatus"),
            "game_time_decision": bool(p.get("gameTimeDecision")), "dfo_player_id": p.get("playerId"),
            "lines_updated_at_utc": combo.get("updatedAt"), "lines_source": combo.get("sourceName"), "observed_at_utc": observed_at_utc,
        })
    return rows


def resolve_line_rows(rows: list[dict[str, Any]], roster: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Attach ``player_id`` by (team, jersey) verified by folded last name; ``resolution`` records how (or why not)."""
    by_num: dict[tuple[str, int], list[dict[str, Any]]] = {}
    by_name: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for r in roster:
        if r.get("sweater") is not None:
            by_num.setdefault((r.get("team_abbrev"), int(r["sweater"])), []).append(r)
        by_name.setdefault((r.get("team_abbrev"), fold(r.get("last_name"))), []).append(r)
    out = []
    for r in rows:
        last = fold((r.get("name") or "").split(" ")[-1]) if r.get("name") else ""
        cand = by_num.get((r["team_abbrev"], int(r["jersey"]))) if r.get("jersey") is not None else None
        pid, how = None, "unresolved"
        if cand and len(cand) == 1 and (not last or fold(cand[0].get("last_name")).endswith(last) or last.endswith(fold(cand[0].get("last_name")))):
            pid, how = cand[0]["player_id"], "jersey+name"
        else:
            nm = by_name.get((r["team_abbrev"], last)) or []
            if len(nm) == 1:
                pid, how = nm[0]["player_id"], "name_only" if not cand else "name_only_jersey_conflict"
            elif len(nm) > 1:
                how = "ambiguous_name"
        out.append(r | {"player_id": pid, "resolution": how})
    return out


def is_confirmed_source(source: str | None) -> bool:
    """Warmups / morning skate / official lineup sources describe tonight; 'Projected' or practice lines do not."""
    s = (source or "").lower()
    return any(k in s for k in ("warmup", "warm-up", "morning skate", "line rushes", "official", "lineup"))
