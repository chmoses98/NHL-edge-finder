"""Team-minute allocation behind the PLAYER_SIM_V1 ice-time projection (RESEARCH_ONLY shadow arm; no price, stake, cap or route reads it).

``build_roster`` turns a player's share of his team's time in a strength state into minutes with ``minutes[state] = share[state] x team_minutes[state]``.
Two allocations exist side by side:

``LEGACY`` (``team-minutes-0``, the published default) -- the template that was hard-coded in ``workflows/shadow_player.py``:
    EV 50.6, PP 4.4 x p_pp / 0.215, SH 4.4, EA 0.6, EN 0.6, OT 1.2 (sum 61.8). Measured against 8,078 regulation team-games it is wrong in four ways: PP/SH are ~14% low, SH ignores the
    opponent's power play, OT is added on top of EV/PP/SH minutes that already contain overtime seconds, and the states do not partition the game clock.

``team-minutes-1.0`` (the candidate; activation needs an approval record in ``data/registry/projection-registry.json``) -- one physical clock budget per team-game
    (all values are CLOCK minutes of the team, not skater-minutes):

        PP_A  = c_pp x ppmin_A            (ppmin = V2's own expected PP minutes for A in this matchup)
        SH_A  = c_pp x ppmin_B            (A is short-handed exactly when B has the power play: PP_A + SH_B and PP_B + SH_A are the same minutes)
        EA_A  = EN_B = league mean        (A's net is empty exactly when B's opponent net is empty)
        EV_A  = 60 + E[OT] - PP_A - SH_A - EA_A - EN_A   (strength states partition the game clock; penalty time comes out of even strength, as in nhl-features-2.0)

    followed by a per-state share-normalisation factor kappa_s (fitted so that the dressed players' expected skater-minutes by state match the observed skater-minutes;
    kappa is ~1 where the shares sum to the number of skaters on the ice; EN (1.15) and EA (0.85) absorb the overtime-padded denominators of the recorded shares).
    The clock identities (PP_A = SH_B, EA_A = EN_B, partition of 60 + E[OT]) hold exactly in ``clock()``; ``allocate()`` then multiplies each state by its own kappa, so the
    PROJECTED minutes satisfy them only up to kappa (a bounded, tested deviation), which is what the share definition requires.
    ``minutes[state] = kappa_s x clock_s``; ``ot`` is a memo (overtime seconds are already inside EV/PP/SH in the player tables), so the allocation carries ``ot = 0``.

Nothing here touches shares, rates or the simulation: goals, assists and points use shares, never minutes, so they are unchanged by construction (tested bit for bit).
"""

from __future__ import annotations

import hashlib
import json
import math
import numbers
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from nhl_edge.config import REPO_ROOT

PARAMS_PATH = REPO_ROOT / "data" / "params" / "team-minutes-1.0.json"
LEGACY_VERSION = "team-minutes-0"
CANDIDATE_VERSION = "team-minutes-1.0"
STATES = ("ev", "pp", "sh", "ea", "en", "ot")
PP_CLIP = (2.0, 9.0)            # clock minutes of power play per team-game; outside this the inputs are broken and the league mean is used instead
LEGACY_LEAGUE_P_PP = 0.215


def legacy(p_pp: float) -> dict[str, float]:
    """The template ``workflows.shadow_player`` used before this module (verbatim)."""
    return {"ev": 50.6, "pp": 4.4 * p_pp / LEGACY_LEAGUE_P_PP, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}


@dataclass(frozen=True)
class AllocationParams:
    version: str
    regulation_min: float
    ot_min: float                 # expected overtime clock minutes per game (unconditional)
    pp_per_ppmin: float           # PP clock minutes per unit of V2 ppmin
    league_pp_min: float          # PP clock minutes per team-game when ppmin is unavailable
    ea_min: float                 # EA == EN by symmetry
    kappa: dict[str, float]       # share-normalisation by state: ev, pp, sh, ea, en
    provenance: dict[str, Any] = field(default_factory=dict)

    def fingerprint(self) -> str:
        body = {k: v for k, v in asdict(self).items() if k != "provenance"}
        return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self) | {"fingerprint": self.fingerprint()}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> AllocationParams:
        return cls(str(d["version"]), float(d["regulation_min"]), float(d["ot_min"]), float(d["pp_per_ppmin"]), float(d["league_pp_min"]), float(d["ea_min"]),
                   {k: float(v) for k, v in d["kappa"].items()}, dict(d.get("provenance") or {}))


def load_params(path: Path | None = None) -> AllocationParams:
    """Loads and VALIDATES the fingerprinted parameter file: the fingerprint is required and must match, every number must be finite and in a plausible range."""
    d = json.loads(Path(path or PARAMS_PATH).read_text())
    p = AllocationParams.from_dict(d)
    if not d.get("fingerprint") or d["fingerprint"] != p.fingerprint():
        raise ValueError(f"team-minutes parameter file fingerprint missing or mismatched: {d.get('fingerprint')} != {p.fingerprint()}")
    nums = {"regulation_min": (p.regulation_min, 59.99, 60.01), "ot_min": (p.ot_min, 0.0, 3.0), "pp_per_ppmin": (p.pp_per_ppmin, 0.5, 2.0), "league_pp_min": (p.league_pp_min, 3.0, 8.0),
            "ea_min": (p.ea_min, 0.0, 2.0)} | {f"kappa.{k}": (v, 0.5, 2.0) for k, v in p.kappa.items()}
    bad = [k for k, (v, lo, hi) in nums.items() if not (math.isfinite(v) and lo <= v <= hi)]
    if bad or set(p.kappa) != {"ev", "pp", "sh", "ea", "en"}:
        raise ValueError(f"team-minutes parameters out of range or incomplete: {bad or sorted(p.kappa)}")
    return p


def _ok(x: Any) -> bool:
    return isinstance(x, numbers.Real) and not isinstance(x, bool) and math.isfinite(float(x)) and x > 0


def clock(ppmin_for: float | None, ppmin_against: float | None, prm: AllocationParams) -> dict[str, float | bool]:
    """Physical clock minutes of ONE team in this game by strength state (EV + PP + SH + EA + EN = 60 + E[OT]); ``fallback`` says the league mean replaced a missing input."""
    fallback = not (_ok(ppmin_for) and _ok(ppmin_against))                      # half a matchup is not trusted: both teams then get the league clock (PP_A == SH_B still holds)
    pp_for = prm.league_pp_min if fallback else prm.pp_per_ppmin * float(ppmin_for)
    pp_opp = prm.league_pp_min if fallback else prm.pp_per_ppmin * float(ppmin_against)
    lo, hi = PP_CLIP
    if not (lo <= pp_for <= hi and lo <= pp_opp <= hi):
        pp_for = pp_opp = prm.league_pp_min
        fallback = True
    ea = en = prm.ea_min
    ev = prm.regulation_min + prm.ot_min - (pp_for + pp_opp) - (ea + en)          # grouped so both teams of one game get the bit-identical even-strength clock
    return {"ev": ev, "pp": pp_for, "sh": pp_opp, "ea": ea, "en": en, "ot": prm.ot_min, "fallback": fallback}


def allocate(ppmin_for: float | None, ppmin_against: float | None, prm: AllocationParams) -> dict[str, float]:
    """The ``team_minutes`` dict ``build_roster`` expects: kappa_s x clock_s; ``ot`` is a memo and is 0 (already inside EV/PP/SH)."""
    c = clock(ppmin_for, ppmin_against, prm)
    out = {s: float(prm.kappa[s] * c[s]) for s in ("ev", "pp", "sh", "ea", "en")}
    out["ot"] = 0.0
    return out


def project_player(share: dict[str, float], profile: Any, priors: Any, tm: dict[str, float]) -> dict[str, float]:
    """The published ice-time / shots fields of one skater under the team-minute dictionary ``tm`` -- exactly the arithmetic of ``players.roster.build_roster``
    (``expected_toi_min`` per state, their sum, and ``expected_sog``), so a second allocation can be evaluated beside the published one without rebuilding the roster
    (identity with ``build_roster`` is a test)."""
    import numpy as np

    exp = {s: float(share[s] * tm.get(s, 0.0)) for s in STATES}
    sog = float(sum(exp[s] * (profile.sog60[s] if np.isfinite(profile.sog60.get(s, np.nan)) else priors.ixg60.get((profile.pos, s), 0) * 10) / 60.0 for s in ("ev", "pp", "sh")))
    return {"toi": float(sum(exp.values())), **exp, "sog": sog}
