"""Score stage: pf_core prospective scorecards plus NHL-specific paired comparison, promotion status and segment checks.

promotion_status (per family, challenger vs the incumbent on IDENTICAL settled player-games, game-clustered 95% CI):
  "better"                  CI of the loss difference is entirely below 0 AND at least MIN_PAIRED_N settled player-games
  "worse"                   CI entirely above 0 AND at least MIN_PAIRED_N player-games
  "not yet distinguishable" anything else (small sample, CI contains 0)
  "no incumbent"            no paired forecasts exist for the family
Only "better" makes a family eligible for a promotion review; nothing here promotes anything by itself.

Primary loss per family (the incumbent only publishes what it publishes):
  goals / assists / points / saves   ranked probability score over the rungs the incumbent published (sum of Brier terms);
                                     challenger probabilities come from its pmf, the incumbent's from its archived ladder
  shots                              CRPS: challenger pmf vs a Poisson with the incumbent's expected shots (as in the study)
  toi_minutes                        absolute error of the mean (both sides publish a mean only)
  team_goals                         no incumbent exists in the live archive (DATA_ONLY_V2 publishes market rungs only)
"""
from __future__ import annotations

import json
from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd

from pf_core import dists, metrics, prospective as pr

from . import common as C

MIN_PAIRED_N = 1000
FAM_ORDER = ["shots", "goals", "assists", "points", "saves", "team_goals", "toi_minutes"]
LOSS_NAME = {"goals": "rung RPS", "assists": "rung RPS", "points": "rung RPS", "saves": "rung RPS", "shots": "CRPS (incumbent as Poisson)",
             "toi_minutes": "absolute error", "team_goals": "n/a"}


def status_from_ci(n: int, ci: list[float] | None, min_n: int = MIN_PAIRED_N) -> str:
    if ci is None or n == 0:
        return "no incumbent"
    if n >= min_n and ci[1] < 0:
        return "better"
    if n >= min_n and ci[0] > 0:
        return "worse"
    return "not yet distinguishable"


def _pge(probs: list[float], lo: int, k: int) -> float:
    i = k - lo
    if i <= 0:
        return 1.0
    if i >= len(probs):
        return 0.0
    return float(np.sum(probs[i:]))


def paired_losses(fam: str, ch: pd.DataFrame, inc: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, str] | None:
    """Per-row (challenger loss, incumbent loss) on identical keys. Negative challenger-minus-incumbent = challenger better."""
    y = ch["actual"].to_numpy(float)
    if fam == "toi_minutes" or (fam in ("goals", "assists", "points", "saves") and inc["ladder"].map(lambda d: bool(d)).sum() == 0):
        return np.abs(ch["mean"].to_numpy(float) - y), np.abs(inc["mean"].to_numpy(float) - y), "absolute error"
    if fam == "shots":
        d = dists.poisson(np.maximum(inc["mean"].to_numpy(float), 1e-4), K=20)
        cp = np.array([list(p) + [0.0] * (21 - len(p)) for p in ch["probs"]])[:, :21] if len(ch) else np.zeros((0, 21))
        cp = cp / cp.sum(axis=1, keepdims=True)
        return dists.DistBatch(0, cp).crps(y), d.crps(y), "CRPS (incumbent as Poisson)"
    la, lb = [], []
    for (_, c), (_, i), yy in zip(ch.iterrows(), inc.iterrows(), y):
        rungs = {int(k): v for k, v in (i["ladder"] or {}).items()}
        if not rungs:
            la.append(np.nan)
            lb.append(np.nan)
            continue
        la.append(sum((_pge(c["probs"], int(c["lo"] or 0), k) - float(yy >= k)) ** 2 for k in rungs))
        lb.append(sum((p - float(yy >= k)) ** 2 for k, p in rungs.items()))
    a, b = np.array(la), np.array(lb)
    m = np.isfinite(a) & np.isfinite(b)
    return a[m], b[m], "rung RPS", m


def promotion(settled: pd.DataFrame, fcs: pd.DataFrame) -> list[dict[str, Any]]:
    """Per-family paired comparison + promotion_status. `settled` = pf_core settlements, `fcs` = forecast archive (ladders)."""
    rows = []
    if settled.empty:
        return [{"family": f, "promotion_status": "no incumbent", "n_paired": 0, "n_games": 0, "loss": LOSS_NAME[f],
                 "reason": "nothing settled yet"} for f in FAM_ORDER]
    ladder = {}
    if not fcs.empty and "ladder" in fcs:
        ladder = dict(zip(fcs["forecast_id"], fcs["ladder"]))
    s = settled[~settled["void"].astype(bool)].copy()
    s["ladder"] = s["forecast_id"].map(lambda x: ladder.get(x) if isinstance(ladder.get(x), dict) else {})
    for fam in FAM_ORDER:
        g = s[s["family"] == fam]
        base = {"family": fam, "loss": LOSS_NAME[fam], "min_paired_n": MIN_PAIRED_N}
        if g.empty or "challenger" not in set(g["model_role"]):
            rows.append({**base, "promotion_status": "no incumbent", "n_paired": 0, "n_games": 0,
                         "reason": "no settled challenger forecasts"})
            continue
        ch = g[g["model_role"] == "challenger"].set_index(["game_id", "entity_id"])
        inc = g[g["model_role"] == "incumbent"].set_index(["game_id", "entity_id"])
        keys = ch.index.intersection(inc.index)
        if len(keys) == 0:
            rows.append({**base, "promotion_status": "no incumbent", "n_paired": 0, "n_games": 0,
                         "n_challenger": int(len(ch)), "reason": "no incumbent forecast on the same player-games"})
            continue
        ch, inc = ch.loc[keys].reset_index(), inc.loc[keys].reset_index()
        res = paired_losses(fam, ch, inc)
        if res is None:
            continue
        a, b, name = res[:3]
        mask = res[3] if len(res) > 3 else np.ones(len(a), bool)
        cl = ch["game_id"].to_numpy()[mask]
        n = int(len(a))
        if n < 2:
            rows.append({**base, "promotion_status": "not yet distinguishable", "n_paired": n, "n_games": int(len(set(cl))),
                         "loss": name, "reason": "fewer than 2 paired player-games"})
            continue
        r = metrics.cluster_bootstrap_diff(a, b, cl, n_boot=1000)
        st = status_from_ci(n, r["ci95"])
        mae_a = np.abs(ch["mean"].to_numpy(float) - ch["actual"].to_numpy(float))
        mae_b = np.abs(inc["mean"].to_numpy(float) - inc["actual"].to_numpy(float))
        rm = metrics.cluster_bootstrap_diff(mae_a, mae_b, ch["game_id"].to_numpy(), n_boot=500)
        rows.append({**base, "loss": name, "n_paired": n, "n_games": int(r["n_clusters"]), "mean_diff": r["mean_diff"],
                     "ci95": r["ci95"], "mae_diff": {"mean_diff": rm["mean_diff"], "ci95": rm["ci95"]},
                     "promotion_status": st, "promotion_review_eligible": st == "better",
                     "reason": (f"paired game-clustered CI {'excludes' if st in ('better', 'worse') else 'does not exclude (or n < ' + str(MIN_PAIRED_N) + ')'} 0; "
                                f"n={n} settled player-games")})
    return rows


def segments(settled: pd.DataFrame, fcs: pd.DataFrame) -> dict[str, Any]:
    """Availability-related checks: did the named starter start, did projected skaters dress, error by participation/gate."""
    out: dict[str, Any] = {}
    if settled.empty or fcs.empty:
        return out
    extra = fcs.set_index("forecast_id")
    ch = settled[settled["model_role"] == "challenger"].copy()
    ch["p_start"] = ch["forecast_id"].map(extra["p_start"]) if "p_start" in extra else np.nan
    ch["dfo_status"] = ch["forecast_id"].map(extra["dfo_status"]) if "dfo_status" in extra else None
    sv = ch[ch["family"] == "saves"]
    if len(sv):
        g = sv.assign(started=~sv["void"].astype(bool))
        out["goalie_start"] = {
            "n": int(len(g)), "hit_rate": round(float(g["started"].mean()), 4),
            "mean_p_start": None if g["p_start"].isna().all() else round(float(g["p_start"].mean()), 4),
            "by_participation": {str(k): {"n": int(len(v)), "started": round(float(v["started"].mean()), 4)}
                                 for k, v in g.groupby(g["participation"].fillna("NA"))},
            "by_dfo_status": {str(k): {"n": int(len(v)), "started": round(float(v["started"].mean()), 4)}
                              for k, v in g.groupby(g["dfo_status"].fillna("none (unverified)"))}}
    sk = ch[ch["family"].isin(["shots", "goals", "assists", "points"])]
    if len(sk):
        one = sk[sk["family"] == "shots"]
        out["skater_dressed"] = {"n": int(len(one)), "dressed_rate": round(float((~one["void"].astype(bool)).mean()), 4),
                                 "by_participation": {str(k): {"n": int(len(v)), "dressed": round(float((~v["void"].astype(bool)).mean()), 4)}
                                                      for k, v in one.groupby(one["participation"].fillna("NA"))}}
    live = ch[~ch["void"].astype(bool)]
    seg = {}
    for fam, g in live.groupby("family"):
        for key, col in (("gate", "gate_status"), ("participation", "participation")):
            for val, v in g.groupby(g[col].fillna("NA")):
                if len(v) >= 5:
                    e = v["mean"].astype(float) - v["actual"].astype(float)
                    seg.setdefault(fam, {}).setdefault(key, {})[str(val)] = {"n": int(len(v)), "mae": round(float(e.abs().mean()), 4),
                                                                              "bias": round(float(e.mean()), 4)}
    out["error_by_segment"] = seg
    return out


def render(card: dict[str, Any]) -> str:
    lines = ["", "### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)", "",
             f"A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least "
             f"{MIN_PAIRED_N:,} settled player-games; otherwise it is **not yet distinguishable**. Research only.", "",
             "| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |",
             "|---|---|---|---|---|---|"]
    ready = card.get("readiness", {})
    for p in card.get("promotion", []):
        ci = p.get("ci95")
        d = f"{p['mean_diff']:+.4f} [{ci[0]:+.4f}, {ci[1]:+.4f}]" if ci else "—"
        lines.append(f"| {p['family']} | {p.get('loss', '')} | {p.get('n_paired', 0)} ({p.get('n_games', 0)}) | {d} | "
                     f"**{p['promotion_status']}** | {ready.get(p['family'], '—')} |")
    seg = card.get("segments") or {}
    if "goalie_start" in seg:
        g = seg["goalie_start"]
        lines += ["", f"**Goalie starter check**: {g['n']} projected goalie-games, named goalie started {g['hit_rate']:.1%} "
                      f"(mean published P(start) {g['mean_p_start'] if g['mean_p_start'] is not None else 'n/a'})."]
        for k, v in g["by_participation"].items():
            lines.append(f"- participation {k}: n={v['n']}, started {v['started']:.1%}")
    if "skater_dressed" in seg:
        s = seg["skater_dressed"]
        lines += ["", f"**Skater lineup check**: {s['n']} projected skaters, {s['dressed_rate']:.1%} dressed."]
        for k, v in s["by_participation"].items():
            lines.append(f"- participation {k}: n={v['n']}, dressed {v['dressed']:.1%}")
    cs = card.get("capture_stats") or {}
    if cs:
        lines += ["", f"**Availability capture**: mean coverage {cs.get('mean_coverage')}, newest capture age "
                      f"{cs.get('newest_age_minutes_median')} min (median over recent runs), runs summarised: {cs.get('runs')}."]
    return "\n".join(lines) + "\n"


def capture_stats(out_root: str, n_runs: int = 12) -> dict[str, Any]:
    import glob
    import os
    fs = sorted(glob.glob(os.path.join(out_root, "runs", "nhl", "*", "*_project.json")))[-n_runs:]
    covs, ages, pst = [], [], []
    for f in fs:
        try:
            d = json.load(open(f))
        except (OSError, ValueError):
            continue
        c = d.get("coverage") or {}
        if c.get("mean_coverage") is not None:
            covs.append(c["mean_coverage"])
        a = [v.get("newest_age_minutes") for v in (c.get("events") or {}).values() if v.get("newest_age_minutes") is not None]
        if a:
            ages.append(float(np.median(a)))
        pst.append(d.get("archive", {}).get("challenger", {}))
    return {"runs": len(fs), "mean_coverage": round(float(np.mean(covs)), 4) if covs else None,
            "newest_age_minutes_median": round(float(np.median(ages)), 1) if ages else None,
            "recent_project_runs": [{k: v for k, v in x.items() if k in ("written", "unchanged", "late_rejected")} for x in pst][-5:]}


def score(out_root: str, summary_path: str, now: datetime, step_summary: str | None = None) -> dict[str, Any]:
    """Write the daily (7d) / weekly (28d) / season scorecards and return their headline numbers."""
    summary = json.load(open(summary_path))
    ref = pr.reference_from_summary(summary)
    readiness = {f["family"]: f["readiness"] for f in summary["families"]}
    readiness["toi_minutes"] = "SHADOW VALIDATION"
    cs = capture_stats(out_root)
    fcs = pr.load_forecasts(out_root, C.SPORT)
    settled_all = pr.load_settlements(out_root, C.SPORT)
    res = {}
    for tag, days in (("daily", 7), ("weekly", 28), ("season", None)):
        card = pr.scorecard(C.SPORT, out_root, ref, now_utc=C.iso(now), window_days=days, capture_stats=cs)
        s = settled_all
        if days and not s.empty:
            s = s[pd.to_datetime(s["game_start_utc"], utc=True) >= pd.Timestamp(now) - pd.Timedelta(days=days)]
        card["promotion"] = promotion(s, fcs)
        card["segments"] = segments(s, fcs)
        card["readiness"] = readiness
        card["capture_stats"] = cs
        card["promotion_rule"] = {"min_paired_n": MIN_PAIRED_N, "ci": "game-clustered bootstrap 95%",
                                  "better": "CI entirely below 0 and n >= min_paired_n", "otherwise": "not yet distinguishable"}
        path = pr.write_scorecard(card, out_root, tag=tag)
        md = pr.render_markdown(card, title=f"NHL projection scorecard ({tag})") + render(card)
        md_path = path.replace(".json", ".md")
        open(md_path, "w").write(md)
        res[tag] = {"path": path, "settled": card["settlement"]["settled"], "void": card["settlement"]["void"],
                    "promotion": {p["family"]: p["promotion_status"] for p in card["promotion"]},
                    "alerts": {a["family"]: a["status"] for a in card["alerts"]}}
        if step_summary:
            with open(step_summary, "a") as f:
                f.write(md + "\n")
    return res
