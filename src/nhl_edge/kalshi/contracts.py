"""Turn a Kalshi NHL market object into a ``Contract``: an explicit, testable statement of what YES means.

Authoritative fields (in priority order):
1. ``strike_type`` + ``floor_strike``/``cap_strike`` (numeric thresholds; Kalshi sends them as numbers or strings).
2. ``custom_strike`` (``{'hockey_team': <uuid>}`` / ``{'hockey_player': <uuid>}``) -> entity identity.
3. ``yes_sub_title`` / ``title`` / ``rules_primary`` -> team names, period words, 'originally scheduled for' date,
   regulation / overtime wording.
4. Ticker (event suffix) -> game date + tricodes, as a cross-check. Kalshi tricodes are short (``SJ``, ``TB``,
   ``NJ``, ``LA``) and are resolved through the identity alias table.

Observed live shapes (docs/probe/samples, 2026-09-29):
- winner:  strike_type=structured, custom_strike.hockey_team, title 'San Jose wins', rules 'If San Jose wins the San
           Jose vs Dallas NHL game originally scheduled for Oct 5, 2026 ...'  (no regulation wording => incl. OT/SO)
- spread:  strike_type=greater, floor_strike=2.5, title 'Vancouver wins by over 2.5 goals'
- total:   strike_type=greater, floor_strike=8.5, title 'Full Game: Over 8.5 goals scored'
Anything else is returned with ``semantics_confidence='low'`` and support downgraded to UNRESOLVED.
"""

from __future__ import annotations

import ast
import re
from datetime import date
from typing import Any

from nhl_edge.identity.teams import TeamIdentityError, TeamRegistry, registry
from nhl_edge.kalshi.ontology import Ontology, Support, classify_market
from nhl_edge.kalshi.ticker import parse_ticker
from nhl_edge.schemas.market import Contract

_SCHED_RE = re.compile(r"originally scheduled for ([A-Z][a-z]{2}) (\d{1,2}), (\d{4})")
_VS_RE = re.compile(r"the (?P<a>.+?) vs\.? (?P<b>.+?) NHL game", re.I)
_MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
_H2H_RE = re.compile(r"\bmore\b.*\bthan\b", re.I)
_REG_RE = re.compile(r"\bregulation\b|\bin regulation\b|\bwithin regulation\b|\b3 periods\b|\bthree periods\b", re.I)
_OT_INCL_RE = re.compile(r"including (any )?overtime|incl(uding|\.) (OT|overtime)|overtime and shootout", re.I)


def _num(v: Any) -> float | None:
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _custom_strike(m: dict[str, Any]) -> dict[str, Any]:
    cs = m.get("custom_strike")
    if isinstance(cs, dict):
        return cs
    if isinstance(cs, str):
        try:
            v = ast.literal_eval(cs)
            return v if isinstance(v, dict) else {}
        except (ValueError, SyntaxError):
            return {}
    return {}


def scheduled_date_from_rules(rules: str | None) -> date | None:
    m = _SCHED_RE.search(rules or "")
    if not m:
        return None
    try:
        return date(int(m[3]), _MONTHS[m[1]], int(m[2]))
    except (KeyError, ValueError):
        return None


def teams_from_rules(rules: str | None, reg: TeamRegistry) -> tuple[int | None, int | None]:
    """'the San Jose vs Dallas NHL game' -> (first_team_id, second_team_id). Order is Kalshi's, not proven home/away."""
    m = _VS_RE.search(rules or "")
    if not m:
        return None, None
    a = reg.resolve_name(m["a"])
    b = reg.resolve_name(m["b"])
    return (a.team_id if a else None), (b.team_id if b else None)


def settles_on_from_text(default: str, title: str, rules: str) -> tuple[str, str | None]:
    """Cross-check the family's settlement basis against the market's own words. Returns (settles_on, note)."""
    text = f"{title} {rules}"
    if _REG_RE.search(text) and default == "FINAL_INCL_OT_SO":
        return "REGULATION", "market text mentions regulation; family default was FINAL_INCL_OT_SO -> using REGULATION"
    if _OT_INCL_RE.search(text) and default == "REGULATION":
        return "FINAL_INCL_OT_SO", "market text says overtime included; family default was REGULATION"
    return default, None


def _team_id_or_none(reg: TeamRegistry, code: str, notes: list[str]) -> int | None:
    try:
        return reg.by_abbrev(code).team_id
    except TeamIdentityError as e:
        notes.append(f"unknown team code {code!r} ({e}); not an NHL club or an identity gap")
        return None


def build_contract(m: dict[str, Any], ontology: Ontology | None = None, reg: TeamRegistry | None = None) -> Contract:
    ontology = ontology or Ontology.load()
    reg = reg or registry()
    cls = classify_market(m, ontology)
    ticker = m.get("ticker", "")
    pt = parse_ticker(ticker, reg.tricodes | set(k for k in reg.by_abbrev_map))
    notes: list[str] = list(pt.notes)
    title = m.get("title") or ""
    ysub = m.get("yes_sub_title") or ""
    rules = m.get("rules_primary") or ""
    strike_type = m.get("strike_type")
    floor = _num(m.get("floor_strike"))
    cap = _num(m.get("cap_strike"))
    cs = _custom_strike(m)
    spec = ontology.families.get(cls.family)
    settles_default = spec.settles_on if spec else "FINAL_INCL_OT_SO"
    settles_on, s_note = settles_on_from_text(settles_default, title, rules)
    if s_note:
        notes.append(s_note)

    team_id: int | None = None
    threshold: float | None = None
    comparator: str | None = None
    upper: float | None = None
    conf = "low"
    support = cls.support

    # The two clubs in the game, from the rules text first (full names, unambiguous) and the ticker second.
    rule_a, rule_b = teams_from_rules(rules, reg)
    game_team_ids = [t for t in (rule_a, rule_b) if t is not None]
    if len(game_team_ids) < 2:
        for code in (pt.away_tricode, pt.home_tricode):
            if code:
                tid = _team_id_or_none(reg, code, notes)
                if tid is not None and tid not in game_team_ids:
                    game_team_ids.append(tid)
    candidates_abbrev = [reg.by_id(t).abbrev for t in game_team_ids]

    if cls.scope.value == "game":
        if cls.stat in ("winner", "reg_winner", "margin", "team_total", "margin_bucket"):
            hit = reg.resolve_name(ysub or title, candidates_abbrev or None)
            if hit is None and pt.market_suffix:
                # market suffix names the team (…-SJ, …-VAN3): strip trailing digits
                code = re.sub(r"\d+$", "", pt.market_suffix.upper())
                if code:
                    tid = _team_id_or_none(reg, code, notes)
                    hit = reg.by_id(tid) if tid is not None else None
            team_id = hit.team_id if hit else None
        if cls.stat in ("winner", "reg_winner") and strike_type == "structured" and team_id is not None:
            comparator, threshold, conf = "gt", 0.0, "high" if cs.get("hockey_team") else "medium"
        elif cls.stat == "margin" and strike_type == "greater" and floor is not None and team_id is not None:
            comparator, threshold, conf = "gt", floor, "high"
        elif cls.stat == "total" and strike_type == "greater" and floor is not None:
            comparator, threshold, conf = "gt", floor, "high"
        elif cls.stat == "team_total" and strike_type == "greater" and floor is not None and team_id is not None:
            comparator, threshold, conf = "gt", floor, "high"
        elif cls.stat in ("overtime", "shootout", "btts") and strike_type in ("structured", None, ""):
            comparator, threshold, conf = "ge", 1.0, "medium"
        elif strike_type == "between" and floor is not None and cap is not None:
            comparator, threshold, upper, conf = "in_range", floor, cap, "medium"
            notes.append("range market: verify inclusive/exclusive bounds in rules")
        elif strike_type == "greater_or_equal" and floor is not None:
            comparator, threshold, conf = "ge", floor, "medium"
        elif strike_type == "less" and floor is not None:
            comparator, threshold, conf = "lt", floor, "medium"
        else:
            notes.append(f"unrecognised game-market shape strike_type={strike_type} stat={cls.stat}")
        if _H2H_RE.search(title) and cls.stat not in ("winner", "reg_winner"):
            conf = "low"
            notes.append("head-to-head phrasing; not a threshold contract")
    elif cls.scope.value == "player":
        if strike_type in ("greater", "structured") and floor is not None:
            comparator, threshold, conf = "gt", floor, "medium"
        elif strike_type == "greater_or_equal" and floor is not None:
            comparator, threshold, conf = "ge", floor, "medium"
        else:
            notes.append(f"unrecognised player-market shape strike_type={strike_type} stat={cls.stat}")
    elif cls.scope.value == "season":
        if strike_type == "greater_or_equal" and floor is not None:
            comparator, threshold, conf = "ge", floor, "medium"
        elif strike_type == "structured" and cs.get("hockey_team"):
            comparator, threshold, conf = "gt", 0.0, "medium"

    sched = scheduled_date_from_rules(rules)
    if sched and pt.game_date and sched != pt.game_date:
        notes.append(f"rules date {sched} != ticker date {pt.game_date}")
        conf = "low"
    game_date = (sched or pt.game_date).isoformat() if (sched or pt.game_date) else None
    if cls.period in ("P1", "P2", "P3") and "period" not in rules.lower() and rules:
        notes.append("period market rules do not mention a period; verify")
    if conf == "low" and support in (Support.MODELABLE, Support.BUILDABLE):
        support = Support.UNRESOLVED
        notes.append("support downgraded: semantics not proven")
    if settles_on != settles_default and support == Support.MODELABLE:
        support = Support.BUILDABLE
        notes.append("support downgraded to BUILDABLE: settlement basis differs from the family default; NEEDS_RULE_REVIEW")

    opp = None
    if team_id is not None and len(game_team_ids) == 2 and team_id in game_team_ids:
        opp = [t for t in game_team_ids if t != team_id][0]
    entity_uuid = cs.get("hockey_player") or cs.get("hockey_team")
    return Contract(
        ticker=ticker, event_ticker=m.get("event_ticker") or pt.event_ticker, series_ticker=m.get("series_ticker") or pt.series_ticker,
        family=cls.family, scope=cls.scope.value, stat=cls.stat, period=cls.period, settles_on=settles_on, game_id=None,
        game_date=game_date, team_id=team_id, opponent_team_id=opp, game_team_ids=sorted(game_team_ids), player_id=None, threshold=threshold, comparator=comparator,
        upper=upper, support=str(support), semantics_confidence=conf, notes=notes,
        entity_name=player_name_from_title(title, ysub) if cls.scope.value == "player" else None,
        kalshi_entity_uuid=str(entity_uuid) if entity_uuid else None, title=title or None, rules_primary=rules or None,
    )


_PLAYER_TITLE_RE = re.compile(r"^(?P<name>[A-Z][\w.'\-]+(?: [A-Z][\w.'\-]+){1,3}?) (?:records|scores|to record|to score|anytime)\b", re.U)
_PLAYER_SUB_RE = re.compile(r"^(?P<name>[A-Z][\w.'\-]+(?: [A-Z][\w.'\-]+){1,3}?): \d", re.U)


def player_name_from_title(title: str, yes_sub_title: str = "") -> str | None:
    m = _PLAYER_TITLE_RE.match(title or "")
    if m:
        return m["name"].strip()
    m = _PLAYER_SUB_RE.match(yes_sub_title or "")
    return m["name"].strip() if m else None


def game_key(contract: Contract) -> tuple[str, frozenset[int]] | None:
    """(game_date, {team ids}) — the join key to the NHL schedule. Order-free on purpose: the ticker's team order
    is Kalshi's convention, the schedule decides home/away."""
    ids = set(contract.game_team_ids) or {t for t in (contract.team_id, contract.opponent_team_id) if t is not None}
    if contract.game_date and len(ids) == 2:
        return contract.game_date, frozenset(ids)
    return None
