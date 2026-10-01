"""Market-family reliability: a research label per contract family, DERIVED from evaluation artifacts (never hand-set).

Evidence read (all committed, all from completed seasons, so point-in-time safe for any 2026-27 run):

* walk-forward, held-out season 2025-26 (never used for a modelling choice): ``docs/research/player_sim_v1/eval.json``
  -- n, Brier vs the role / season-rate baselines, ECE (player families, saves ladder, first goal);
* historical Kalshi benchmark at T-10m: ``docs/research/player_sim_v1/market_benchmark.json`` (player goals / assists
  / points: model Brier minus Kalshi-mid Brier on two-sided quotes <= 10c) and ``docs/research/market_benchmark.json``
  (moneyline / totals / puck line: DATA_ONLY_V2 vs the Kalshi mid, the largest-n horizon);
* prospective SHADOW evidence: the ``evaluations`` / ``evaluations_player`` ledger partitions observed AT OR BEFORE the
  run's cutoff (never the derived ``eval/report*.json``, which is overwritten and would leak later games into a
  retrospective run). Distinct games are counted, not rows (one contract is predicted many times a day).

Rules (thresholds fixed a priori; precedence top to bottom):

    CALIBRATION_WARNING  held-out EXCESS ECE > 0.010, or >= 30 prospective games with excess ECE > 0.05, where
                         excess ECE = ECE - noise floor and floor(n) = sqrt(2/pi) * sqrt(0.25 * 10 bins / n) is the ECE a
                         perfectly calibrated forecaster shows from sampling noise alone (~0.035 at n = 1,300; the Kalshi
                         market's own moneyline ECE on those rows is 0.029, so raw ECE would flag the market too)
    EVIDENCE_STRONGER    held-out n >= 5,000, ECE <= 0.010, beats its simple baseline, AND ties or beats the Kalshi mid
                         (Brier difference <= 0) on >= 1,000 benchmark rows
    EVIDENCE_MIXED       some depth (>= 1,000 held-out or benchmark rows) but not STRONGER (e.g. market better, or no
                         market benchmark, or not better than a simple baseline)
    EVIDENCE_THIN        anything else (no artifact, or small samples)

A family with fewer than 30 prospective games always carries the note ``SMALL_PROSPECTIVE_SAMPLE`` -- small samples
stay labelled small. The label changes confidence (the edge haircut in ``thesis.expression``); it never overrides a
model probability.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from nhl_edge.config import REPO_ROOT

STRONGER = "EVIDENCE_STRONGER"
MIXED = "EVIDENCE_MIXED"
THIN = "EVIDENCE_THIN"
WARNING = "CALIBRATION_WARNING"

ECE_WARN = 0.010  # excess over the noise floor
ECE_STRONG = 0.010
N_WF_STRONG = 5000
N_MKT_STRONG = 1000
N_DEPTH = 1000
PROSPECTIVE_GAMES_MIN = 30
PROSPECTIVE_ECE_WARN = 0.05

PLAYER_EVAL = REPO_ROOT / "docs" / "research" / "player_sim_v1" / "eval.json"
PLAYER_MKT = REPO_ROOT / "docs" / "research" / "player_sim_v1" / "market_benchmark.json"
GAME_MKT = REPO_ROOT / "docs" / "research" / "market_benchmark.json"
FINAL_KEY = "final (PLAYER_SIM_V1: fringe prior + goal co-presence k=10)"
HELD_OUT = "2025"

PLAYER_MAP = {"player_goals": ("goals 1+", "goals"), "player_assists": ("assists 1+", "assists"), "player_points": ("points 1+", "points")}
GAME_MAP = {"game_winner": ("moneyline", None), "game_total": ("totals", None), "team_total": ("totals", "proxy: full-game totals benchmark"),
            "game_spread": ("puck_line", None)}


def _load(p: Path) -> dict[str, Any] | None:
    try:
        return json.loads(Path(p).read_text())
    except (OSError, json.JSONDecodeError):
        return None


def historical_evidence(player_eval: Path = PLAYER_EVAL, player_mkt: Path = PLAYER_MKT, game_mkt: Path = GAME_MKT) -> dict[str, dict[str, Any]]:
    """family -> {wf_n, wf_ece, wf_beats_baseline, mkt_n, mkt_delta (model - market Brier), sources}."""
    out: dict[str, dict[str, Any]] = {}
    pe = _load(player_eval) or {}
    held = ((pe.get(FINAL_KEY) or {}).get(HELD_OUT)) or {}
    pm = ((_load(player_mkt) or {}).get("benchmark") or {}).get("T-10m") or {}
    by_stat = pm.get("by_stat") or {}
    for fam, (wf_key, mkt_key) in PLAYER_MAP.items():
        v = (held.get("skaters") or {}).get(wf_key) or {}
        m = v.get("PLAYER_SIM_V1") or {}
        base = min([x["brier"] for k, x in v.items() if isinstance(x, dict) and k != "PLAYER_SIM_V1" and "brier" in x] or [float("inf")])
        b = by_stat.get(mkt_key) or {}
        out[fam] = {"wf_n": m.get("n"), "wf_ece": m.get("ece"), "wf_beats_baseline": (m.get("brier", float("inf")) < base) if m else None,
                    "mkt_n": b.get("n"), "mkt_delta": (b["brier_model"] - b["brier_market"]) if b.get("n") else None,
                    "sources": [f"{player_eval.name} {HELD_OUT} '{wf_key}'", f"{player_mkt.name} T-10m by_stat '{mkt_key}'"]}
    g = (held.get("goalies") or {}).get("pooled_ladder", {}).get("PLAYER_SIM_V1") or {}
    gb = (held.get("goalies") or {}).get("pooled_ladder", {})
    base = min([x["brier"] for k, x in gb.items() if isinstance(x, dict) and k != "PLAYER_SIM_V1" and "brier" in x] or [float("inf")])
    out["goalie_saves"] = {"wf_n": g.get("n"), "wf_ece": g.get("ece"), "wf_beats_baseline": (g.get("brier", float("inf")) < base) if g else None, "mkt_n": None,
                           "mkt_delta": None, "sources": [f"{player_eval.name} {HELD_OUT} goalies pooled ladder", "no settled KXNHLSAVE history (no market benchmark)"]}
    fg = (held.get("first_goal") or {}).get("first_scorer") or {}
    out["first_goal"] = {"wf_n": fg.get("n"), "wf_ece": fg.get("ece"), "wf_beats_baseline": (fg.get("brier_skill_vs_constant", 0) > 0) if fg else None, "mkt_n": None,
                         "mkt_delta": None, "sources": [f"{player_eval.name} {HELD_OUT} first scorer", "no first-goal market benchmark artifact"]}
    gm = _load(game_mkt) or {}
    for fam, (key, note) in GAME_MAP.items():
        blk = gm.get(key) or {}
        best = None
        for h, v in blk.items():
            if not isinstance(v, dict):
                continue
            subs = [v] if "MARKET" in v else [x for x in v.values() if isinstance(x, dict) and "MARKET" in x]
            n = sum(int(s.get("n") or 0) for s in subs)
            if subs and (best is None or n > best[0]):
                best = (n, h, subs)
        if best is None:
            continue
        n, h, subs = best
        d = sum(s["n"] * (s["V2 (SIM2_ST)"]["brier"] - s["MARKET"]["brier"]) for s in subs if "V2 (SIM2_ST)" in s) / max(n, 1)
        e = sum(s["n"] * (s["V2 (SIM2_ST)"].get("ece") or 0) for s in subs if "V2 (SIM2_ST)" in s) / max(n, 1)
        out[fam] = {"wf_n": n, "wf_ece": e, "wf_beats_baseline": None, "mkt_n": n, "mkt_delta": d,
                    "sources": [f"{game_mkt.name} '{key}' {h} (DATA_ONLY_V2 vs Kalshi mid; historical, not prospective)"] + ([note] if note else [])}
    return out


def prospective_evidence(ledger: Any, cutoff: datetime) -> dict[str, dict[str, Any]]:
    """Distinct settled games / rows / ECE per family from evaluation partitions observed at or before ``cutoff``."""
    import gzip

    from nhl_edge.archive.ledger import entry_observed_at
    from nhl_edge.evaluation.metrics import ece

    acc: dict[str, dict[str, Any]] = {}
    if ledger is None:
        return acc
    try:
        entries = [e for e in ledger.manifest() if e.kind in ("evaluations", "evaluations_player") and entry_observed_at(e) <= cutoff]
    except Exception:  # noqa: BLE001 - no archive, no prospective evidence
        return acc
    seen: set[tuple[str, str]] = set()
    for e in entries:
        key = "p_player" if e.kind == "evaluations_player" else "p_data_only"
        with gzip.open(ledger.root / e.path, "rt", encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                r = json.loads(line)
                if not r.get("pregame") or r.get(key) is None:
                    continue
                k = (str(r.get("prediction_id")), str(r.get("settlement_key")))
                if k in seen:
                    continue
                seen.add(k)
                a = acc.setdefault(str(r.get("family")), {"games": set(), "p": [], "y": []})
                a["games"].add(str(r.get("game_id")))
                a["p"].append(float(r[key]))
                a["y"].append(int(r["y"]))
    out = {}
    for fam, a in acc.items():
        out[fam] = {"n_games": len(a["games"]), "n_rows": len(a["p"]), "ece": ece(a["p"], a["y"]) if len(a["p"]) >= 20 else None}
    return out


def ece_noise_floor(n: int, bins: int = 10) -> float:
    return float((2.0 / 3.141592653589793) ** 0.5 * (0.25 * bins / max(n, 1)) ** 0.5)


def label_family(hist: dict[str, Any] | None, pros: dict[str, Any] | None) -> dict[str, Any]:
    h = hist or {}
    p = pros or {}
    notes: list[str] = []
    wf_n, wf_ece, beats, mkt_n, mkt_d = h.get("wf_n") or 0, h.get("wf_ece"), h.get("wf_beats_baseline"), h.get("mkt_n") or 0, h.get("mkt_delta")
    if wf_n:
        notes.append(f"held-out n {wf_n}, ECE {wf_ece:.4f} (noise floor {ece_noise_floor(wf_n):.4f})" + ("" if beats is None else f", {'beats' if beats else 'does not beat'} simple baseline"))
    if mkt_n:
        notes.append(f"vs Kalshi mid: Brier {'+' if mkt_d > 0 else ''}{mkt_d:.4f} ({'market better' if mkt_d > 0 else 'model ties/better'}, n {mkt_n})")
    else:
        notes.append("no historical market benchmark")
    pg = int(p.get("n_games") or 0)
    notes.append(f"prospective: {pg} games / {int(p.get('n_rows') or 0)} rows" + ("" if p.get("ece") is None else f", ECE {p['ece']:.3f}"))
    flags = ["SMALL_PROSPECTIVE_SAMPLE"] if pg < PROSPECTIVE_GAMES_MIN else []
    excess = (wf_ece - ece_noise_floor(wf_n)) if (wf_ece is not None and wf_n) else None
    p_excess = ((p.get("ece") or 0) - ece_noise_floor(int(p.get("n_rows") or 0))) if p.get("ece") is not None else None
    if (excess is not None and excess > ECE_WARN) or (pg >= PROSPECTIVE_GAMES_MIN and p_excess is not None and p_excess > PROSPECTIVE_ECE_WARN):
        lab = WARNING
    elif wf_n >= N_WF_STRONG and wf_ece is not None and wf_ece <= ECE_STRONG and beats is True and mkt_n >= N_MKT_STRONG and mkt_d is not None and mkt_d <= 0:
        lab = STRONGER
    elif wf_n >= N_DEPTH or mkt_n >= N_DEPTH:
        lab = MIXED
    else:
        lab = THIN
    return {"label": lab, "flags": flags, "evidence": "; ".join(notes), "sources": h.get("sources") or ["no evaluation artifact for this family"]}


def reliability_table(ledger: Any = None, cutoff: datetime | None = None, families: list[str] | None = None) -> dict[str, dict[str, Any]]:
    hist = historical_evidence()
    pros = prospective_evidence(ledger, cutoff) if (ledger is not None and cutoff is not None) else {}
    fams = sorted(set(families or []) | set(hist) | set(pros))
    return {f: label_family(hist.get(f), pros.get(f)) for f in fams}


# ------------------------------------------------------------------------------------------------ bucket calibration
BUCKET_Z = 2.0


def bucket_tables(player_eval: Path = PLAYER_EVAL) -> dict[tuple[str, int | None], list[dict[str, Any]]]:
    """(family, N for an N+ ladder rung or None) -> held-out 2025-26 calibration buckets (mean_pred, hit_rate, gap, se)."""
    pe = _load(player_eval) or {}
    held = ((pe.get(FINAL_KEY) or {}).get(HELD_OUT)) or {}
    out: dict[tuple[str, int | None], list[dict[str, Any]]] = {}
    for fam, stat in (("player_goals", "goals"), ("player_assists", "assists"), ("player_points", "points")):
        for k in (1, 2, 3):
            b = ((held.get("skaters") or {}).get(f"{stat} {k}+") or {}).get("buckets")
            if b:
                out[(fam, k)] = b
    sv = ((held.get("goalies") or {}).get("pooled_ladder") or {}).get("buckets")
    if sv:
        out[("goalie_saves", None)] = sv
    fg = (held.get("first_goal") or {}).get("first_scorer_buckets")
    if fg:
        out[("first_goal", None)] = fg
    return out


def _bucket_bounds(label: str) -> tuple[float, float] | None:
    try:
        lo, hi = str(label).rstrip("%").split("-")
        return float(lo) / 100.0, float(hi) / 100.0
    except ValueError:
        return None


def bucket_flag(tables: dict[tuple[str, int | None], list[dict[str, Any]]], family: str, threshold: float | None, p_yes: float, side: str) -> dict[str, Any] | None:
    """Held-out calibration evidence in the bucket the model's YES probability falls in. ``against`` is True when the bet
    side relies on the direction the model is measurably wrong in (YES where the model over-predicts YES by >= 2 se, NO
    where it under-predicts YES by >= 2 se). This lowers CONFIDENCE only; the model probability is never recalibrated."""
    k = None if family in ("goalie_saves", "first_goal") else (int(round((threshold or 0.5) + 0.5)) if threshold is not None else 1)
    b = tables.get((family, k))
    if not b:
        return None
    for row in b:
        bb = _bucket_bounds(row.get("bucket"))
        if bb and bb[0] <= p_yes < bb[1] and row.get("n", 0) >= 50 and row.get("se"):
            z = float(row["gap"]) / float(row["se"])
            against = (side == "yes" and z <= -BUCKET_Z) or (side == "no" and z >= BUCKET_Z)
            return {"bucket": row["bucket"], "n": int(row["n"]), "mean_pred": round(float(row["mean_pred"]), 4), "hit_rate": round(float(row["hit_rate"]), 4),
                    "gap": round(float(row["gap"]), 4), "z": round(z, 1), "against_measured_bias": bool(against),
                    "text": (f"held-out 2025-26 '{family}{'' if k is None else f' {k}+'}' bucket {row['bucket']}: model {row['mean_pred']:.3f} vs observed {row['hit_rate']:.3f} "
                             f"(gap {row['gap']:+.3f}, z {z:+.1f}, n {row['n']})" + ("; this side bets on the model's measured bias -> CALIBRATION_WARNING" if against else ""))}
    return None
