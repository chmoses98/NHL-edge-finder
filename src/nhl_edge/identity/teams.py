"""Canonical NHL team identity.

The canonical key is the official NHL ``team_id`` (as used by api-web.nhle.com and api.nhle.com/stats). Every
source resolves into it: the NHL API by id or abbreviation, MoneyPuck by abbreviation, Kalshi by the ticker tricode
and by the team name in ``yes_sub_title``/``title``. Name matching is a *last resort* for sources that carry no
code, never the primary mechanism, and it must hit exactly one team.

Historical identity (verified against api-web 2026-09-29): Arizona (ARI, team_id 53) played through 2023-24; the
hockey operations moved to Utah as "Utah Hockey Club" (team_id 59, our code UHC) for 2024-25, renamed Utah Mammoth
with a NEW team_id 68 from 2025-26 (the current UTA). All three rows exist so historical seasons resolve without
renaming the past; ``successor`` maps ARI/UHC -> UTA only when a caller explicitly asks for it. MoneyPuck labels
all Utah seasons "UTA", which the alias table maps to the current club.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from nhl_edge.config import REPO_ROOT

TEAMS_CSV = REPO_ROOT / "data" / "identity" / "teams.csv"

# Abbreviations other sources use for the same club. MoneyPuck and older NHL feeds differ from api-web.
ABBREV_ALIASES = {
    "T.B": "TBL", "TB": "TBL", "N.J": "NJD", "NJ": "NJD", "L.A": "LAK", "LA": "LAK", "S.J": "SJS", "SJ": "SJS",
    "MON": "MTL", "WAS": "WSH", "CAL": "CGY", "VEG": "VGK", "LV": "VGK", "WIN": "WPG", "CLB": "CBJ", "PHX": "ARI",
    "UTAH": "UTA", "NAS": "NSH", "TAM": "TBL", "NJ.": "NJD",
}

SUCCESSOR = {"ARI": "UTA", "UHC": "UTA"}


class TeamIdentityError(KeyError):
    pass


@dataclass(frozen=True)
class Team:
    team_id: int
    abbrev: str
    city: str
    nickname: str
    name: str
    conference: str
    division: str
    timezone: str
    aliases: tuple[str, ...] = ()
    active_from: int | None = None
    active_to: int | None = None  # None == currently active

    @property
    def active(self) -> bool:
        return self.active_to is None

    def name_keys(self) -> set[str]:
        keys = {self.city.lower(), self.nickname.lower(), self.name.lower(), self.abbrev.lower()}
        keys |= {a.lower() for a in self.aliases}
        return keys


@dataclass
class TeamRegistry:
    teams: dict[int, Team]
    by_abbrev_map: dict[str, Team] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for t in self.teams.values():
            self.by_abbrev_map[t.abbrev.upper()] = t
        for alias, ab in ABBREV_ALIASES.items():
            if ab in self.by_abbrev_map:
                self.by_abbrev_map.setdefault(alias.upper(), self.by_abbrev_map[ab])

    @property
    def tricodes(self) -> set[str]:
        return {t.abbrev for t in self.teams.values()}

    @property
    def active_teams(self) -> list[Team]:
        return sorted((t for t in self.teams.values() if t.active), key=lambda t: t.abbrev)

    def by_id(self, team_id: int | str) -> Team:
        try:
            tid = int(team_id)
        except (TypeError, ValueError) as e:
            raise TeamIdentityError(f"bad team_id {team_id!r}") from e
        if tid not in self.teams:
            raise TeamIdentityError(f"unknown NHL team_id {tid}")
        return self.teams[tid]

    def by_abbrev(self, abbrev: str) -> Team:
        key = (abbrev or "").strip().upper()
        if key in self.by_abbrev_map:
            return self.by_abbrev_map[key]
        raise TeamIdentityError(f"unknown NHL abbreviation {abbrev!r}")

    def by_tricode(self, code: str) -> Team:  # NBA-compatible name used by shared Kalshi code
        return self.by_abbrev(code)

    def resolve_name(self, text: str, candidates: list[str] | None = None) -> Team | None:
        """Resolve a free-text team reference. Exactly one hit required; ``candidates`` (abbrevs) narrows the search.

        Word-bounded matching: 'Kings' must not match inside 'Vikings'; 'Wild' inside 'Wildcats'."""
        t = (text or "").lower()
        if not t:
            return None
        pool = [self.by_abbrev(c) for c in candidates] if candidates else list(self.teams.values())
        hits: list[Team] = []
        for team in pool:
            for k in team.name_keys():
                if len(k) <= 3 and not candidates:
                    continue  # bare abbreviations only count when the candidate set is explicit
                if re.search(rf"(?<![a-z]){re.escape(k)}(?![a-z])", t):
                    hits.append(team)
                    break
        hits = list(dict.fromkeys(hits))
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1 and not candidates:
            # 'New York' is ambiguous between NYI/NYR unless the nickname is present.
            named = [h for h in hits if re.search(rf"(?<![a-z]){re.escape(h.nickname.lower())}(?![a-z])", t)]
            if len(named) == 1:
                return named[0]
        return None

    def successor(self, abbrev: str) -> Team:
        """The current franchise that inherited an inactive club's roster (ARI -> UTA). Explicit, never implicit."""
        t = self.by_abbrev(abbrev)
        return self.by_abbrev(SUCCESSOR[t.abbrev]) if t.abbrev in SUCCESSOR else t


def load_registry(path: Path = TEAMS_CSV) -> TeamRegistry:
    teams: dict[int, Team] = {}
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            tid = int(row["team_id"])
            teams[tid] = Team(
                team_id=tid, abbrev=row["abbrev"].upper(), city=row["city"], nickname=row["nickname"], name=row["name"],
                conference=row["conference"], division=row["division"], timezone=row["timezone"],
                aliases=tuple(a for a in (row.get("aliases") or "").split("|") if a),
                active_from=int(row["active_from"]) if row.get("active_from") else None,
                active_to=int(row["active_to"]) if row.get("active_to") else None,
            )
    return TeamRegistry(teams)


@lru_cache(maxsize=1)
def registry() -> TeamRegistry:
    return load_registry()
