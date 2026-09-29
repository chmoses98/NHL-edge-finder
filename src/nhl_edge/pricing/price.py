"""Price a ``Contract`` from one game's joint simulation draws. One draw, every market: coherent by construction."""

from __future__ import annotations

from dataclasses import dataclass

from nhl_edge.schemas.market import Contract
from nhl_edge.sim.engine import SimResult


@dataclass(frozen=True)
class Priced:
    p: float | None
    se: float | None
    supported: bool
    reason: str


def _cmp(res: SimResult, values, contract: Contract) -> tuple[float, float]:
    c, t, u = contract.comparator, contract.threshold, contract.upper
    if c == "gt":
        return res.p(values > t)
    if c == "ge":
        return res.p(values >= t)
    if c == "lt":
        return res.p(values < t)
    if c == "le":
        return res.p(values <= t)
    if c == "eq":
        return res.p(values == t)
    if c == "in_range" and u is not None:
        return res.p((values >= t) & (values <= u))
    raise ValueError(f"comparator {c!r}")


def price_contract(contract: Contract, res: SimResult, home_team_id: int, away_team_id: int) -> Priced:
    if contract.support not in ("MODELABLE", "BUILDABLE"):
        return Priced(None, None, False, f"support {contract.support}")
    if contract.scope != "game":
        return Priced(None, None, False, f"scope {contract.scope} not priced by the game simulator")
    if contract.settles_on not in ("FINAL_INCL_OT_SO", "REGULATION"):
        return Priced(None, None, False, f"settlement basis {contract.settles_on} not priced")
    reg = contract.settles_on == "REGULATION"
    home = None
    if contract.team_id is not None:
        if contract.team_id == home_team_id:
            home = True
        elif contract.team_id == away_team_id:
            home = False
        else:
            return Priced(None, None, False, "contract team is not in this game")
    stat = contract.stat
    try:
        if stat in ("winner", "reg_winner"):
            if home is None:
                return Priced(None, None, False, "winner contract without a team")
            p, se = (res.p_reg_win(home) if reg else res.p_win(home))
        elif stat == "margin":
            if home is None:
                return Priced(None, None, False, "margin contract without a team")
            vals = (res.home_reg - res.away_reg) if reg else res.margin
            p, se = _cmp(res, vals if home else -vals, contract)
        elif stat == "margin_bucket":
            if home is None or contract.comparator != "in_range":
                return Priced(None, None, False, "margin bucket needs a team and a range")
            vals = (res.home_reg - res.away_reg) if reg else res.margin
            p, se = _cmp(res, vals if home else -vals, contract)
        elif stat == "total":
            vals = (res.home_reg + res.away_reg) if reg else res.total
            p, se = _cmp(res, vals, contract)
        elif stat == "team_total":
            if home is None:
                return Priced(None, None, False, "team total without a team")
            vals = (res.home_reg if home else res.away_reg) if reg else res.team_final(home)
            p, se = _cmp(res, vals, contract)
        elif stat == "overtime":
            p, se = res.p_overtime()
        elif stat == "shootout":
            p, se = res.p_shootout()
        elif stat == "btts":
            p, se = res.p_btts()
        else:
            return Priced(None, None, False, f"stat {stat!r} not priced")
    except ValueError as e:
        return Priced(None, None, False, str(e))
    return Priced(float(p), float(se), True, "priced from joint draws")
