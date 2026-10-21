"""Market taxonomy: turn one archived Kalshi market row into an explicit ``ContractSpec``.

Authority order (never the ticker string alone):

1. ``series_ticker`` -> family table below (the series is Kalshi's own product identifier);
2. structured fields: ``strike_type``, ``floor_strike``, ``custom_strike`` (team uuid / player uuid);
3. ``rules_primary`` / ``rules_secondary`` text, parsed to CROSS-CHECK the structured fields (threshold, teams, date,
   period wording, overtime / shootout wording). Any disagreement downgrades the spec to ``UNRESOLVED`` -- a contract whose
   own words contradict its own strike is never settled by guesswork.

The ticker is used only for game scope (event date) and as a last-resort team-code cross-check.

The spec also records what the contract text says about the three things that decide hockey settlement disputes:
overtime, shootout and void/fair-price conditions.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any

from nhl_edge.identity.teams import TeamRegistry, registry
from nhl_edge.kalshi.ticker import parse_ticker

PROVEN, PARTIAL, UNRESOLVED = "PROVEN", "PARTIAL", "UNRESOLVED"

# series -> (family, period, kind, stat)
SERIES: dict[str, tuple[str, str, str, str | None]] = {
    "KXNHLGAME": ("game_winner", "FULL", "winner", None),
    "KXNHLSPREAD": ("game_spread", "FULL", "spread", None),
    "KXNHLTOTAL": ("game_total", "FULL", "total", None),
    "KXNHLTEAMTOTAL": ("team_total", "FULL", "team_total", None),
    "KXNHLOT": ("game_overtime", "FULL", "overtime", None),
    "KXNHLF10G": ("game_early_goal", "P1", "early_goal", None),
    "KXNHL1P": ("period_winner", "P1", "period_winner", None),
    "KXNHL2P": ("period_winner", "P2", "period_winner", None),
    "KXNHL3P": ("period_winner", "P3", "period_winner", None),
    "KXNHL1PSPREAD": ("period_spread", "P1", "period_spread", None),
    "KXNHL2PSPREAD": ("period_spread", "P2", "period_spread", None),
    "KXNHL3PSPREAD": ("period_spread", "P3", "period_spread", None),
    "KXNHL1PTOTAL": ("period_total", "P1", "period_total", None),
    "KXNHL2PTOTAL": ("period_total", "P2", "period_total", None),
    "KXNHL3PTOTAL": ("period_total", "P3", "period_total", None),
    "KXNHLFIRSTGOAL": ("first_goal", "FULL", "first_goal", None),
    "KXNHLGOAL": ("player_goals", "FULL", "player_stat", "goals"),
    "KXNHLAST": ("player_assists", "FULL", "player_stat", "assists"),
    "KXNHLPTS": ("player_points", "FULL", "player_stat", "points"),
    "KXNHLSAVE": ("goalie_saves", "FULL", "player_stat", "saves"),
}
GOAL_SCORER_FAMILIES = ("player_goals", "first_goal")  # researched, never recommended
PLAYER_KINDS = ("player_stat", "first_goal")

_SCHED_RE = re.compile(r"originally scheduled for ([A-Z][a-z]{2}) (\d{1,2}), (\d{4})")
_NAME = r"[A-Z][\w.'\-]*(?: [A-Z][\w.'\-]*)*"  # capitalised words only: 'New York R', 'St. Louis', 'Tampa Bay'
_VS_RE = re.compile(rf"\bthe (?P<a>{_NAME}) vs\.? (?P<b>{_NAME}) NHL game", re.U)
_OVER_RE = re.compile(r"(?:more than|over) (\d+(?:\.\d+)?) goals", re.I)
_PLAYER_N_RE = re.compile(r"records (\d+)\+ (goals|assists|points|saves)", re.I)
# Kalshi display names that nhl_edge.identity.teams.resolve_name() cannot resolve (verified 1:1 against the KXNHLGAME ticker
# team code on every archived game market; see DATA_QUALITY_AUDIT.md). The production contract builder survives this only
# through its ticker-tricode fallback; this audit resolves them from the contract's own wording instead.
KALSHI_NAME_ALIASES = {"New York I": "NYI", "New York R": "NYR", "Utah": "UTA"}
_MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


@dataclass
class ContractSpec:
    ticker: str
    event_ticker: str
    series: str
    family: str
    scope: str  # game | player | unsupported
    period: str  # FULL | P1 | P2 | P3
    kind: str
    stat: str | None
    threshold: float | None  # YES iff value > threshold
    subject_team_id: int | None
    team_ids: tuple[int, int] | None  # the two clubs, order = rules text order (NOT home/away)
    game_date: str | None
    team_uuid: str | None
    player_uuid: str | None
    player_name: str | None
    counts_overtime: bool
    shootout_credit: str  # one_goal | none | n/a
    void_rule: str  # none | fair_price_if_player_never_enters | fair_price_if_not_played
    is_tie_leg: bool
    semantics_status: str
    evidence: list[str] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["team_ids"] = list(self.team_ids) if self.team_ids else None
        d["evidence"] = "; ".join(self.evidence)
        d["issues"] = "; ".join(self.issues)
        return d


def _num(v: Any) -> float | None:
    if v is None or v == "" or (isinstance(v, float) and v != v):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _cs(v: Any) -> dict[str, Any]:
    if isinstance(v, dict):
        return v
    if isinstance(v, str) and v:
        try:
            out = json.loads(v)
            return out if isinstance(out, dict) else {}
        except ValueError:
            return {}
    return {}


def _rules_date(rules: str) -> date | None:
    m = _SCHED_RE.search(rules or "")
    if not m:
        return None
    try:
        return date(int(m[3]), _MONTHS[m[1]], int(m[2]))
    except (KeyError, ValueError):
        return None


def _team_name_from_subtitle(row: dict[str, Any]) -> str:
    """The team a team-leg contract is about, in Kalshi's own words ('Buffalo', 'Buffalo wins by over 3.5 goals', ...)."""
    sub = str(row.get("yes_sub_title") or "")
    for pat in (r"^(.*?) wins by over [\d.]+ goals$", r"^(.*?) over [\d.]+$"):
        m = re.match(pat, sub)
        if m:
            return m[1].strip()
    return sub.strip()


def resolve_team(name: str, reg: TeamRegistry, candidates: list[str] | None = None):
    code = KALSHI_NAME_ALIASES.get(name.strip())
    if code:
        try:
            return reg.by_abbrev(code)
        except KeyError:
            return None
    return reg.resolve_name(name.strip(), candidates)


def build_spec(row: dict[str, Any], reg: TeamRegistry | None = None) -> ContractSpec:
    reg = reg or registry()
    ticker = str(row.get("ticker") or "")
    series = str(row.get("series_ticker") or ticker.split("-")[0])
    pt = parse_ticker(ticker)
    rules = str(row.get("rules_primary") or "")
    rules2 = str(row.get("rules_secondary") or "")
    text = f"{rules} {rules2}"
    fam = SERIES.get(series)
    ev: list[str] = []
    iss: list[str] = []
    cs = _cs(row.get("custom_strike"))
    strike_type = row.get("strike_type")
    floor = _num(row.get("floor_strike"))

    if fam is None:
        return ContractSpec(ticker, str(row.get("event_ticker") or pt.event_ticker), series, "unsupported", "unsupported", "FULL", "unknown", None,
                            None, None, None, None, None, None, None, False, "n/a", "none", False, UNRESOLVED,
                            [], [f"series {series} has no entry in the audit taxonomy"])
    family, period, kind, stat = fam
    scope = "player" if kind in PLAYER_KINDS else "game"

    # --- the two clubs and the scheduled date, from the rules text (full names) ---------------------------
    ids: list[int] = []
    m = _VS_RE.search(rules)
    if m:
        for nm in (m["a"], m["b"]):
            t = resolve_team(nm, reg)
            if t is not None:
                ids.append(t.team_id)
    team_ids = (ids[0], ids[1]) if len(ids) == 2 and ids[0] != ids[1] else None
    if team_ids is None:
        iss.append("could not resolve the two clubs from rules_primary")
    rd = _rules_date(rules)
    if rd is None:
        iss.append("rules_primary has no 'originally scheduled for' date")
    elif pt.game_date and rd != pt.game_date:
        iss.append(f"rules date {rd} != ticker date {pt.game_date}")
    gdate = (rd or pt.game_date).isoformat() if (rd or pt.game_date) else None

    # --- subject team (team legs) -------------------------------------------------------------------------
    subject: int | None = None
    is_tie = False
    if kind in ("winner", "spread", "team_total", "period_winner", "period_spread"):
        if str(row.get("yes_sub_title") or "").strip().lower() == "tie":
            is_tie = True
            ev.append("yes_sub_title=Tie")
        else:
            nm = _team_name_from_subtitle(row)
            cand = [reg.by_id(t).abbrev for t in team_ids] if team_ids else None
            hit = resolve_team(nm, reg, cand)
            subject = hit.team_id if hit else None
            if subject is None:
                iss.append(f"could not resolve team from yes_sub_title {nm!r}")
            elif team_ids and subject not in team_ids:
                iss.append("subject team is not one of the two clubs in the rules")
                subject = None
            else:
                ev.append(f"team from yes_sub_title={nm!r}")
    if is_tie and kind != "period_winner":
        iss.append("Tie leg outside a period-winner market")

    # --- threshold + cross-check against the rules wording -------------------------------------------------
    threshold: float | None = None
    if kind in ("spread", "total", "team_total", "period_spread", "period_total"):
        if strike_type == "greater" and floor is not None:
            threshold = floor
            ev.append(f"strike_type=greater floor_strike={floor}")
            mm = _OVER_RE.search(rules)
            if not mm:
                iss.append("rules_primary has no 'more than/over X goals' clause to cross-check the strike")
            elif abs(float(mm[1]) - floor) > 1e-9:
                iss.append(f"rules threshold {mm[1]} != floor_strike {floor}")
        else:
            iss.append(f"unexpected strike_type={strike_type} floor={floor}")
    elif kind == "overtime":
        if not (strike_type == "greater" and floor == 0.5):
            iss.append(f"unexpected overtime strike {strike_type}/{floor}")
        threshold = 0.5
        if "overtime period is" not in text.lower() and "overtime period" not in rules.lower():
            iss.append("overtime wording missing")
    elif kind == "early_goal":
        if not (strike_type == "greater_or_equal" and floor == 1.0):
            iss.append(f"unexpected early-goal strike {strike_type}/{floor}")
        threshold = 1.0
        if "first 10 minutes" not in rules:
            iss.append("first-10-minutes wording missing")
    elif kind == "player_stat":
        if strike_type == "greater" and floor is not None:
            threshold = floor
            mm = _PLAYER_N_RE.search(rules)
            if not mm:
                iss.append("rules_primary has no 'records N+ <stat>' clause")
            else:
                if abs(float(mm[1]) - 0.5 - floor) > 1e-9:
                    iss.append(f"rules N+={mm[1]} inconsistent with floor_strike {floor}")
                if mm[2].lower() != stat:
                    iss.append(f"rules stat {mm[2]} != series stat {stat}")
        else:
            iss.append(f"unexpected player strike {strike_type}/{floor}")
    elif kind == "first_goal":
        if strike_type != "structured":
            iss.append(f"unexpected first-goal strike {strike_type}")
        if "scores the 1st goal" not in rules:
            iss.append("first-goal wording missing")

    # --- player identity (uuid only here; NHL id needs the game roster -> outcomes.py) --------------------
    player_uuid = cs.get("hockey_player")
    player_name = None
    if scope == "player":
        if not player_uuid:
            iss.append("player market without hockey_player uuid")
        mt = re.match(r"^(?P<n>.+?)(?::| - )", str(row.get("title") or "")) or re.match(r"^(?P<n>.+?): ", str(row.get("yes_sub_title") or ""))
        player_name = mt["n"].strip() if mt else None
        if not player_name:
            iss.append("could not read the player name from the title")

    # --- overtime / shootout / void semantics, read from the contract's own text --------------------------------
    low = text.lower()
    counts_ot = True
    so_credit = "n/a"
    void_rule = "none"
    if kind in ("period_winner", "period_spread", "period_total"):
        counts_ot = False  # a period market never includes OT; 3rd period says so explicitly
        if period == "P3" and "excluding overtime" not in low and "do not include overtime" not in low:
            iss.append("P3 market without an explicit overtime exclusion")
        so_credit = "n/a"
    elif kind in ("total", "team_total"):
        so_credit = "one_goal" if "shootout" in low and ("one goal" in low or "one additional goal" in low) else "none"
        if so_credit != "one_goal":
            iss.append("shootout credit not stated; defaulting to none")
    elif kind in ("winner", "spread"):
        so_credit = "one_goal"  # a shootout winner wins by exactly one goal on the official final
        ev.append("official final (incl. OT/SO); SO decides the winner by one goal")
    elif kind == "early_goal":
        counts_ot = False
    if scope == "player":
        void_rule = "fair_price_if_player_never_enters" if "never enters the game" in low else "none"
        if void_rule == "none":
            iss.append("player void rule not stated in rules_secondary")
        counts_ot = True  # official stat line: OT counts, shootout never does
    if "fair price" in low and scope == "game":
        void_rule = "fair_price_if_not_played"

    status = PROVEN if not iss else UNRESOLVED
    if team_ids is None or gdate is None:
        status = UNRESOLVED
    return ContractSpec(
        ticker=ticker, event_ticker=str(row.get("event_ticker") or pt.event_ticker), series=series, family=family, scope=scope,
        period=period, kind=kind, stat=stat, threshold=threshold, subject_team_id=subject, team_ids=team_ids, game_date=gdate,
        team_uuid=cs.get("hockey_team"), player_uuid=player_uuid, player_name=player_name, counts_overtime=counts_ot,
        shootout_credit=so_credit, void_rule=void_rule, is_tie_leg=is_tie, semantics_status=status, evidence=ev, issues=iss,
    )
