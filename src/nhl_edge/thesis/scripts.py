"""Game-script taxonomy: deterministic, interpretable labels computed from simulated (or official) game outcomes.

No clustering: every label is a fixed rule on :class:`~nhl_edge.thesis.features.DrawFeatures`, so assignments are
prospectively reproducible (same draw -> same label) and the same rule classifies the real game afterwards.

Thresholds are frozen a priori from COMPLETED regular seasons 2021-22 .. 2025-26 of the repository's official event
history (6,560 games), never from any slate (``docs/research/THESIS_ENGINE.md`` section 3 has the derivation):

* scoring environment, non-shootout total goals: LOW <= 4 (22.9% of games), NORMAL 5-7 (51.5%), HIGH >= 8 (25.6%);
* shot control, a team's share of shots on goal: >= 0.55 (27.6% of games for the home side), <= 0.45 (30.3%);
  sd of the share 0.088;
* net volume, shots on goal against one net: LOW <= 25 (~ lower tercile, 26), HIGH >= 33 (~ upper tercile, 32);
* margin shape: TIGHT = one-goal final or overtime; DECIDED = 2+ goals.

The PRIMARY partition (used for bet-to-script contributions, which therefore reconcile exactly to every contract's
unconditional probability) is SHOT_CONTROL x ENVIRONMENT x MARGIN = 3 x 3 x 2 = 18 scripts. It describes HOW the game
was played; who won is reported conditional on the script, so "TOR shot control . low event . tight" with a high NYI
win rate is the "TOR pressure / NYI goalie steals it" script. Every other dimension below is reported as an overlay.

Caveat stated in the docs: simulated shots on goal come from the goalie-saves layer (negative binomial on the
pre-game expected shots, moved by the simulated score margin), not from a possession process, so SHOT CONTROL in the
simulation reflects expected shot share, noise and score effects -- the trailing team shoots more.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from nhl_edge.thesis.features import DrawFeatures

ENV_LOW_MAX = 4
ENV_HIGH_MIN = 8
CONTROL_SHARE = 0.55
VOLUME_LOW_MAX = 25
VOLUME_HIGH_MIN = 33
BLOWOUT_MIN = 4
PP_DRIVEN_MIN_GOALS = 2
THRESHOLDS = {"env_low_max_goals": ENV_LOW_MAX, "env_high_min_goals": ENV_HIGH_MIN, "control_shot_share": CONTROL_SHARE,
              "net_volume_low_max_shots": VOLUME_LOW_MAX, "net_volume_high_min_shots": VOLUME_HIGH_MIN, "blowout_min_margin": BLOWOUT_MIN,
              "pp_driven_min_goals": PP_DRIVEN_MIN_GOALS,
              "provenance": "frozen from completed regular seasons 2021-22..2025-26 official events (6,560 games); never fit to a slate"}
MAJOR_SCRIPT_MIN_FREQ = 0.03  # a script is "major" when it occurs in >= 3% of draws


# ------------------------------------------------------------------------------------------------ dimensions
def control_labels(f: DrawFeatures) -> np.ndarray:
    """0 = HOME shot control, 1 = BALANCED, 2 = AWAY shot control."""
    s = f.home_shot_share
    return np.where(s >= CONTROL_SHARE, 0, np.where(s <= 1 - CONTROL_SHARE, 2, 1)).astype(np.int8)


def env_labels(f: DrawFeatures) -> np.ndarray:
    """0 = LOW, 1 = NORMAL, 2 = HIGH (non-shootout total goals)."""
    t = f.total
    return np.where(t <= ENV_LOW_MAX, 0, np.where(t >= ENV_HIGH_MIN, 2, 1)).astype(np.int8)


def margin_labels(f: DrawFeatures) -> np.ndarray:
    """0 = TIGHT (one-goal final or OT/SO), 1 = DECIDED (2+)."""
    return np.where((np.abs(f.final_margin) <= 1) | f.ot, 0, 1).astype(np.int8)


def shape_labels(f: DrawFeatures) -> np.ndarray:
    """0 = OT_OR_SO, 1 = ONE_GOAL_REG, 2 = TWO_THREE_GOALS, 3 = BLOWOUT (4+)."""
    m = np.abs(f.final_margin)
    return np.where(f.ot, 0, np.where(m <= 1, 1, np.where(m < BLOWOUT_MIN, 2, 3))).astype(np.int8)


def volume_labels(net_faced: np.ndarray) -> np.ndarray:
    """0 = LOW, 1 = MID, 2 = HIGH shots on goal against one net."""
    return np.where(net_faced <= VOLUME_LOW_MAX, 0, np.where(net_faced >= VOLUME_HIGH_MIN, 2, 1)).astype(np.int8)


@dataclass
class Taxonomy:
    """Names of every dimension, with the team abbreviations filled in."""

    home: str
    away: str

    @property
    def control(self) -> tuple[str, ...]:
        return (f"{self.home} shot control", "balanced shots", f"{self.away} shot control")

    env = ("low event (<=4)", "normal event (5-7)", "high event (8+)")
    margin = ("tight (1-goal/OT)", "decided (2+)")
    shape = ("OT/SO", "one-goal regulation", "2-3 goal margin", "blowout (4+)")
    volume = ("low", "mid", "high")

    def primary_name(self, code: int) -> str:
        c, e, m = primary_parts(code)
        return f"{self.control[c]} · {self.env[e]} · {self.margin[m]}"

    def primary_key(self, code: int) -> str:
        c, e, m = primary_parts(code)
        return f"C{('H', 'B', 'A')[c]}|E{('L', 'N', 'H')[e]}|M{('T', 'D')[m]}"


N_PRIMARY = 18


def primary_labels(f: DrawFeatures) -> np.ndarray:
    """Primary script code 0..17 = control * 6 + env * 2 + margin."""
    return (control_labels(f).astype(np.int16) * 6 + env_labels(f) * 2 + margin_labels(f)).astype(np.int16)


def primary_parts(code: int) -> tuple[int, int, int]:
    return int(code) // 6, (int(code) % 6) // 2, int(code) % 2


# ------------------------------------------------------------------------------------------------ overlays
def overlay_tags(f: DrawFeatures) -> dict[str, np.ndarray]:
    """Non-exclusive special-situation tags (boolean per draw), keyed by stable names with team abbreviations."""
    out: dict[str, np.ndarray] = {}
    ctrl = control_labels(f)
    for home in (True, False):
        s = f.side(home)
        ab, opp_ctrl = s["abbrev"], (2 if home else 0)
        out[f"GOALIE_STEAL_{ab}"] = s["win"] & (ctrl == opp_ctrl)
        out[f"NET_VOLUME_HIGH_{ab}"] = s["net_faced"] >= VOLUME_HIGH_MIN
        out[f"NET_VOLUME_LOW_{ab}"] = s["net_faced"] <= VOLUME_LOW_MAX
        out[f"PP_DRIVEN_{ab}"] = (s["pp"] >= PP_DRIVEN_MIN_GOALS) & (2 * s["pp"] >= s["goals"])
        out[f"COMEBACK_{ab}"] = s["win"] & (s["max_deficit"] >= 1)
    out["EMPTY_NET_MATERIAL"] = (f.home_en + f.away_en) >= 1
    out["OT_OR_LATE_TIGHT"] = f.ot | f.tight_late
    return out


# ------------------------------------------------------------------------------------------------ distribution
@dataclass
class ScriptDistribution:
    labels: np.ndarray  # primary code per draw
    freq: np.ndarray  # (18,)
    taxonomy: Taxonomy
    summaries: list[dict[str, Any]] = field(default_factory=list)
    dims: dict[str, dict[str, float]] = field(default_factory=dict)

    def onehot(self) -> np.ndarray:
        oh = np.zeros((len(self.labels), N_PRIMARY), dtype=np.float32)
        oh[np.arange(len(self.labels)), self.labels] = 1.0
        return oh

    def major(self) -> list[int]:
        return [int(s) for s in np.argsort(-self.freq) if self.freq[s] >= MAJOR_SCRIPT_MIN_FREQ]


def _m(x: np.ndarray | None, mask: np.ndarray, nd: int = 2) -> float | None:
    if x is None or not mask.any():
        return None
    return round(float(np.mean(x[mask])), nd)


def build_distribution(f: DrawFeatures, player_lift: dict[str, np.ndarray] | None = None) -> ScriptDistribution:
    """Primary scripts with their frequency and key simulated characteristics; overlay and dimension marginals.

    ``player_lift``: optional {player label: per-draw 1+ point indicator} used to report which players are most
    involved in each script (lift = P(point | script) / P(point))."""
    tx = Taxonomy(f.home_abbrev, f.away_abbrev)
    lab = primary_labels(f)
    n = max(f.n, 1)
    freq = np.bincount(lab, minlength=N_PRIMARY).astype(float) / n
    tags = overlay_tags(f)
    win_h = f.winner == 1
    pp_tot = (f.home_pp + f.away_pp).astype(float)
    en_tot = (f.home_en + f.away_en).astype(float)
    goals_tot = f.total.astype(float)
    base_pt = {k: float(v.mean()) for k, v in (player_lift or {}).items()}
    summaries = []
    for s in range(N_PRIMARY):
        m = lab == s
        if not m.any():
            continue
        g = goals_tot[m].sum()
        involve = []
        for k, v in (player_lift or {}).items():
            if base_pt.get(k, 0) > 0:
                involve.append((k, float(v[m].mean()) / base_pt[k], float(v[m].mean())))
        involve.sort(key=lambda t: -t[1])
        summaries.append({
            "code": s, "key": tx.primary_key(s), "name": tx.primary_name(s), "frequency": round(float(freq[s]), 4), "major": bool(freq[s] >= MAJOR_SCRIPT_MIN_FREQ),
            f"p_{f.home_abbrev}_win": round(float(win_h[m].mean()), 4), f"p_{f.away_abbrev}_win": round(float((~win_h)[m].mean()), 4),
            f"{f.home_abbrev}_goals": _m(f.home_goals, m), f"{f.away_abbrev}_goals": _m(f.away_goals, m), "total_goals": _m(goals_tot, m),
            f"{f.home_abbrev}_shots": _m(f.home_shots, m, 1), f"{f.away_abbrev}_shots": _m(f.away_shots, m, 1),
            f"{f.home_abbrev}_starter_saves": _m(f.home_saves, m, 1), f"{f.away_abbrev}_starter_saves": _m(f.away_saves, m, 1),
            "pp_goal_share": round(float(pp_tot[m].sum() / g), 3) if g > 0 else None, "en_goal_share": round(float(en_tot[m].sum() / g), 3) if g > 0 else None,
            "p_overtime": round(float(f.ot[m].mean()), 3),
            "driver": ("special teams" if g > 0 and pp_tot[m].sum() / g >= 0.30 else "late empty net" if g > 0 and en_tot[m].sum() / g >= 0.12 else "even strength"),
            "tags": {k: round(float(v[m].mean()), 3) for k, v in tags.items() if v[m].mean() >= 0.15},
            "players_most_involved": [{"player": k, "p_point": round(p, 3), "lift": round(li, 2)} for k, li, p in involve[:3]],
        })
    summaries.sort(key=lambda d: -d["frequency"])
    dims = {
        "shot_control": dict(zip(tx.control, (np.bincount(control_labels(f), minlength=3) / n).round(4).tolist())),
        "environment": dict(zip(tx.env, (np.bincount(env_labels(f), minlength=3) / n).round(4).tolist())),
        "margin": dict(zip(tx.margin, (np.bincount(margin_labels(f), minlength=2) / n).round(4).tolist())),
        "shape": dict(zip(tx.shape, (np.bincount(shape_labels(f), minlength=4) / n).round(4).tolist())),
        f"{f.home_abbrev}_net_volume": dict(zip(tx.volume, (np.bincount(volume_labels(f.home_net_faced), minlength=3) / n).round(4).tolist())),
        f"{f.away_abbrev}_net_volume": dict(zip(tx.volume, (np.bincount(volume_labels(f.away_net_faced), minlength=3) / n).round(4).tolist())),
        "overlays": {k: round(float(v.mean()), 4) for k, v in tags.items()},
    }
    return ScriptDistribution(lab, freq, tx, summaries, dims)
