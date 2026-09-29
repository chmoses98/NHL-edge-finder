"""Market ontology: how a Kalshi NHL market maps to a modelled quantity.

Two layers:
1. ``data/catalog/market_ontology.yaml`` — curated, versioned knowledge about series → family. Editing YAML,
   not code, is the normal way to onboard a new market family once discovery surfaces it.
2. Heuristic classification (``classify_market``) that works from Kalshi market *fields* (title, strike
   fields, sub-titles, rules) for series the YAML does not know. Anything it cannot place lands in
   ``UNRESOLVED`` with a reason — never silently dropped.

Support states (coverage invariant; every ticker gets exactly one):
    MODELABLE   : simulator + contract semantics produce a probability we stand behind (subject to gates)
    BUILDABLE   : semantics understood, sim output exists or is near, but pricing not wired/validated
    RESEARCH    : semantics understood, but we do not yet have a defensible model (e.g. first basket)
    UNMODELABLE : semantics understood; we will not model (e.g. awards voting, draft)
    UNRESOLVED  : we could not determine what the contract means; needs human/ontology update
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any

import yaml

from nhl_edge.config import REPO_ROOT

ONTOLOGY_PATH = REPO_ROOT / "data" / "catalog" / "market_ontology.yaml"


class Support(StrEnum):
    """How far along a market family is TECHNICALLY: can we parse it, model it, settle it?

    This is a different axis from betting authority (RESEARCH / SHADOW / LIMITED / TRUSTED) and the
    two must never be read as one. The technical state used to be called ``PRICED``, which reads as
    a completed act on a real market -- an authority claim -- and a slate row emitted
    ``"support": "MODELABLE"`` next to ``"authority": "RESEARCH"`` where ``Support.RESEARCH`` and
    ``Authority.RESEARCH`` are the same string meaning different things. ``MODELABLE`` says only
    what is true: we can model this family. It also pairs properly with BUILDABLE and UNMODELABLE.
    """

    MODELABLE = "MODELABLE"  # semantics proven against real observed markets; we can price and settle it
    BUILDABLE = "BUILDABLE"  # the simulator can produce the quantity, but the market side is unproven
    RESEARCH = "RESEARCH"  # interesting, not modelled
    UNMODELABLE = "UNMODELABLE"  # we do not expect to model this
    UNRESOLVED = "UNRESOLVED"  # we do not know what this is -- always fail closed

    @classmethod
    def parse(cls, value: str | None) -> Support | None:
        """Read a support state, accepting names persisted before the MODELABLE rename.

        The archive is append-only and already holds rows written under the old name, so those must
        keep resolving forever. Never write a legacy name back out.
        """
        if value is None:
            return None
        v = str(value).strip().upper()
        if v in _LEGACY_SUPPORT_NAMES:
            return cls(_LEGACY_SUPPORT_NAMES[v])
        try:
            return cls(v)
        except ValueError:
            return None


# Support states written before a rename. Keys are the persisted spelling, values the current one.
# The immutable archive already contains the old name; it must never stop resolving.
_LEGACY_SUPPORT_NAMES = {"PRICED": "MODELABLE"}


class Scope(StrEnum):
    GAME = "game"
    PLAYER = "player"
    SEASON = "season"
    OTHER = "other"


@dataclass
class FamilySpec:
    family: str
    scope: Scope
    stat: str | None  # e.g. margin, total, team_total, pts, reb, ast, fg3m, pra ...
    period: str = "FULL"  # FULL | P1 | P2 | P3 | SEASON | PATTERN
    support: Support = Support.UNRESOLVED
    settles_on: str = "FINAL_INCL_OT_SO"  # FINAL_INCL_OT_SO | REGULATION | PERIOD | EVENT | SEASON | OTHER
    description: str = ""
    settlement_notes: str = ""
    series_tickers: list[str] = field(default_factory=list)
    series_patterns: list[str] = field(default_factory=list)  # regexes matched against the series ticker
    title_patterns: list[str] = field(default_factory=list)


@dataclass
class Ontology:
    version: str
    families: dict[str, FamilySpec]
    series_to_family: dict[str, str]
    pattern_rules: list[tuple[re.Pattern[str], str]] = field(default_factory=list)

    def family_for_series(self, series_ticker: str) -> str | None:
        st = (series_ticker or "").upper()
        fam = self.series_to_family.get(st)
        if fam:
            return fam
        for rx, name in self.pattern_rules:
            if rx.match(st):
                return name
        return None

    @classmethod
    def load(cls, path: Path = ONTOLOGY_PATH) -> Ontology:
        raw = yaml.safe_load(path.read_text())
        fams: dict[str, FamilySpec] = {}
        s2f: dict[str, str] = {}
        for name, spec in raw["families"].items():
            fs = FamilySpec(
                family=name,
                scope=Scope(spec["scope"]),
                stat=spec.get("stat"),
                period=spec.get("period", "FULL"),
                support=Support(spec.get("support", "UNRESOLVED")),
                settles_on=str(spec.get("settles_on", "FINAL_INCL_OT_SO")),
                description=spec.get("description", ""),
                settlement_notes=spec.get("settlement_notes", ""),
                series_tickers=list(spec.get("series_tickers", [])),
                series_patterns=list(spec.get("series_patterns", [])),
                title_patterns=list(spec.get("title_patterns", [])),
            )
            fams[name] = fs
            for st in fs.series_tickers:
                s2f[st.upper()] = name
        rules: list[tuple[re.Pattern[str], str]] = []
        for name, fs in fams.items():
            for pat in fs.series_patterns:
                rules.append((re.compile(pat, re.I), name))
        return cls(version=str(raw.get("version", "0")), families=fams, series_to_family=s2f, pattern_rules=rules)


# ---- heuristic classification from market fields -----------------------------------------------

_STAT_WORDS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bsaves?\b", re.I), "saves"),
    (re.compile(r"\bshots? on goal\b|\bSOG\b|\bshots\b", re.I), "shots"),
    (re.compile(r"\bassists?\b", re.I), "assists"),
    (re.compile(r"\bpoints?\b", re.I), "points"),
    (re.compile(r"anytime (goal )?scorer|\bscores? a goal\b|\bgoals?\b", re.I), "goals"),
]
_PERIOD_WORDS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\b(first|1st)\s+period\b|\bP1\b|\b1P\b", re.I), "P1"),
    (re.compile(r"\b(second|2nd)\s+period\b|\bP2\b|\b2P\b", re.I), "P2"),
    (re.compile(r"\b(third|3rd)\s+period\b|\bP3\b|\b3P\b", re.I), "P3"),
]


_SERIES_PERIOD_RE = re.compile(r"^KXNHL(?P<per>1P|2P|3P|P1|P2|P3|1ST|2ND|3RD)")


_PER_NORM = {"1P": "P1", "2P": "P2", "3P": "P3", "1ST": "P1", "2ND": "P2", "3RD": "P3"}


def _period_from_series(series: str) -> str | None:
    m = _SERIES_PERIOD_RE.match(series or "")
    return _PER_NORM.get(m["per"], m["per"]) if m else None


def _period_from_text(*texts: str) -> str:
    for t in texts:
        for rx, per in _PERIOD_WORDS:
            if t and rx.search(t):
                return per
    return "FULL"


def _stat_from_text(*texts: str) -> str | None:
    for t in texts:
        for rx, stat in _STAT_WORDS:
            if t and rx.search(t):
                return stat
    return None


@dataclass
class Classification:
    family: str
    scope: Scope
    stat: str | None
    period: str
    support: Support
    reason: str
    via: str  # "ontology" | "heuristic" | "none"


def classify_market(market: dict[str, Any], ontology: Ontology) -> Classification:
    series = (market.get("series_ticker") or market.get("ticker", "").split("-")[0]).upper()
    title = market.get("title") or ""
    subtitle = market.get("subtitle") or market.get("yes_sub_title") or ""
    rules = market.get("rules_primary") or ""
    fam = ontology.family_for_series(series)
    if fam:
        spec = ontology.families[fam]
        period = spec.period if spec.period != "FULL" else _period_from_text(title, subtitle)
        if spec.period == "PATTERN":
            period = _period_from_series(series) or _period_from_text(title, subtitle)
        return Classification(fam, spec.scope, spec.stat, period, spec.support, f"series {series} in ontology", "ontology")

    # Heuristics for unknown series. These land in UNRESOLVED (needs ontology entry) but carry a best guess
    # so the coverage report is informative.
    period = _period_from_text(title, subtitle, rules)
    stat = _stat_from_text(title, subtitle)
    text = f"{title} {subtitle}".lower()
    if any(w in text for w in ("stanley cup", "champion", "hart", "vezina", "calder", "norris", "award", "draft", "conference", "division", "playoffs", "make the playoffs", "win total", "regular season", "presidents")):
        return Classification("season_unknown", Scope.SEASON, stat, "SEASON", Support.UNRESOLVED, f"series {series} not in ontology; season-scope words in title", "heuristic")
    if stat in {"goals", "points", "assists", "shots", "saves"} and (":" in title or "records" in text or "scores" in text):
        return Classification("player_unknown", Scope.PLAYER, stat, period, Support.UNRESOLVED, f"series {series} not in ontology; player-stat words in title", "heuristic")
    if "regulation" in text:
        return Classification("game_unknown", Scope.GAME, "reg_winner", period, Support.UNRESOLVED, f"series {series} not in ontology; regulation words in title", "heuristic")
    if "spread" in text or "by over" in text or "wins by" in text or "margin" in text or "puck line" in text:
        return Classification("game_unknown", Scope.GAME, "margin", period, Support.UNRESOLVED, f"series {series} not in ontology; spread words in title", "heuristic")
    if "total" in text or "combined" in text or "goals scored" in text:
        return Classification("game_unknown", Scope.GAME, "total", period, Support.UNRESOLVED, f"series {series} not in ontology; total words in title", "heuristic")
    if "overtime" in text or "shootout" in text:
        return Classification("game_unknown", Scope.GAME, "overtime", period, Support.UNRESOLVED, f"series {series} not in ontology; OT/SO words in title", "heuristic")
    if "win" in text or "winner" in text:
        return Classification("game_unknown", Scope.GAME, "winner", period, Support.UNRESOLVED, f"series {series} not in ontology; winner words in title", "heuristic")
    return Classification("unknown", Scope.OTHER, stat, period, Support.UNRESOLVED, f"series {series} not in ontology; no heuristic matched", "none")
