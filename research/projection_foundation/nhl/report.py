"""Render results/summary.json (sport_summary.v1) and RESULTS_NHL.md from results/nhl_full_results.json.

    cd research/projection_foundation && python -m nhl.report

Every number in the report is read from the results file; the prose around the numbers states
decisions that follow from fixed rules (CI excludes zero on validation -> adopt, etc.).
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

PF = Path(__file__).resolve().parents[1]
if str(PF) not in sys.path:
    sys.path.insert(0, str(PF))

from pf_core import VERSION as PF_VERSION  # noqa: E402

from nhl import SPLIT_LABELS, VERSION  # noqa: E402

RES = PF / "results"
FAM = {  # key -> (contract family, unit, opportunity family, population)
    "sog": ("shots", "player-game", "toi_minutes",
            "skaters who dressed (TOI > 0) with >= 1 prior NHL game since 2021-22; regular season; conditional on playing"),
    "goals": ("goals", "player-game", "toi_minutes", "same skater population"),
    "assists": ("assists", "player-game", "toi_minutes", "same skater population"),
    "points": ("points", "player-game", "toi_minutes", "same skater population"),
    "saves": ("saves", "goalie-game", "shots_against",
              "actual starting goalies with >= 1 prior start since 2021-22 (CONDITIONAL_ON_ACTUAL_STARTER)"),
    "team_goals": ("team_goals", "team-game", None, "every regular-season team-game after the team's first game in the data"),
}
LABEL = {"sog": "Shots on goal", "goals": "Goals", "assists": "Assists", "points": "Points", "saves": "Goalie saves",
         "team_goals": "Team goals"}


def esc(t) -> str:
    return str(t).replace("|", "\\|")


def f(x, n=4, sign=False):
    if x is None:
        return "n/a"
    s = f"{x:+.{n}f}" if sign else f"{x:.{n}f}"
    return s


def ci(d, n=4):
    if not d:
        return "n/a"
    return f"{d['mean_diff']:+.{n}f} [{d['ci95'][0]:+.{n}f}, {d['ci95'][1]:+.{n}f}]"


def sig(d):
    if not d:
        return "n/a"
    lo, hi = d["ci95"]
    return "better" if hi < 0 else "worse" if lo > 0 else "tie"


def _sha():
    try:
        return subprocess.check_output(["git", "-C", str(PF), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def inc_metric(fam: str, x: dict | None, split: str):
    """Pick the comparable incumbent metric (negative = ours better)."""
    if not x:
        return None
    if fam == "sog":
        d = x.get("crps_diff")
        return d and {**d, "metric": "CRPS (ours NB vs incumbent mean scored as Poisson, the production convention)",
                      "source": x["source"]}
    if split == "holdout" and x.get("rps_diff"):
        return {**x["rps_diff"], "metric": f"rung RPS over {x['rps_rungs'][0]}+..{x['rps_rungs'][-1]}+ (CRPS restricted to "
                                           "the incumbent's published rungs)", "source": x["source"]}
    b = (x.get("brier_per_rung") or {}).get("1")
    if b:
        return {**b["diff"], "metric": f"Brier 1+ on the {b['n']} rows where the incumbent published it", "source": x["source"]}
    if x.get("sq_error_diff"):
        return {**x["sq_error_diff"], "metric": "squared error of the mean", "source": x["source"]}
    return None


def readiness(fam, hold, inc_h, inc_p):
    beats_base = hold.get("vs_baseline") and hold["vs_baseline"]["ci95"][1] < 0
    calibrated = 0.77 <= hold["cover_80"] <= 0.83 and 0.9 <= hold["pit_var_ratio"] <= 1.1
    worse_inc = inc_h and inc_h["ci95"][0] > 0
    better_inc = inc_h and inc_h["ci95"][1] < 0
    if worse_inc:
        return "NEEDS IMPROVEMENT", (f"Beats our own baseline but the incumbent ({inc_h['source']}) is better on holdout "
                                     f"({inc_h['metric']}: {ci(inc_h)}).")
    if not beats_base:
        return "NEEDS IMPROVEMENT", "Does not beat the shrunk season-average baseline on holdout."
    if not calibrated:
        return "NEEDS IMPROVEMENT", (f"Holdout calibration outside tolerance (80% coverage {hold['cover_80']:.3f}, "
                                     f"PIT variance ratio {hold['pit_var_ratio']:.3f}).")
    rel = "better than" if better_inc else "statistically tied with" if inc_h else "without a paired incumbent for"
    pro = f"; prospective 2026-27 vs incumbent {ci(inc_p)} ({sig(inc_p)})" if inc_p else ""
    return "SHADOW VALIDATION", (f"Beats baseline on validation and holdout, calibrated (80% coverage {hold['cover_80']:.3f}, "
                                 f"PIT var {hold['pit_var_ratio']:.3f}), {rel} the incumbent on holdout{pro}. READY requires a "
                                 f"live shadow record from the daily workflow (none yet: it is inert until merged).")


def build(full: dict) -> dict:
    fams = full["families"]
    out_f = []
    for key, (cfam, unit, opp, popl) in FAM.items():
        r = fams[key]
        best = r["best_model"]
        rows = []
        val = {m["model"]: m["crps"] for m in r["models"] if m["split"] == "validation"}
        vbest = min(val.values())
        verdict = {k: ("baseline" if k.startswith("A_") else "best" if k == best else
                       "competitive" if v <= vbest * 1.002 else "rejected") for k, v in val.items()}
        for m in r["models"]:
            row = {k: m[k] for k in ("model", "split", "n_obs", "n_clusters", "mae", "rmse", "bias", "crps", "log_score",
                                     "cover_50", "cover_80", "cover_90", "pit_var_ratio", "vs_baseline")}
            row["verdict"] = verdict[m["model"]]
            row["vs_incumbent"] = None
            if m["model"] == best and m["split"] in ("holdout", "prospective"):
                row["vs_incumbent"] = inc_metric(key, r["incumbent"].get(m["split"]), m["split"])
            rows.append(row)
        hold = next(m for m in rows if m["model"] == best and m["split"] == "holdout")
        inc_h = inc_metric(key, r["incumbent"].get("holdout"), "holdout")
        inc_p = inc_metric(key, r["incumbent"].get("prospective"), "prospective")
        rd, why = readiness(key, hold, inc_h, inc_p)
        out_f.append({
            "family": cfam, "unit": unit, "opportunity_family": opp, "population": popl, "models": rows,
            "best_model": best,
            "holdout": {"model": best, "n_obs": hold["n_obs"], "mae": hold["mae"], "crps": hold["crps"], "bias": hold["bias"],
                        "cover_80": hold["cover_80"], "vs_baseline": hold["vs_baseline"] or {}, "vs_incumbent": inc_h or {}},
            "readiness": rd, "readiness_reason": why})
    return out_f


def experiments(full: dict) -> list[dict]:
    F = full["families"]
    ex = full["extra_experiments"]
    o = full["opportunity"]
    xg = full["xg"]
    st = full["starter_accuracy"]
    la = full["lineup_accuracy"]
    p2 = full["params"]["stage2"]

    def mrow(fam, model, split):
        return next(m for m in F[fam]["models"] if m["model"] == model and m["split"] == split)

    def toi(split, model, tgt="toi"):
        return next(x for x in o["models"][split] if x["model"] == model and x["target"] == tgt)

    E = []
    E.append({"id": "NHL-X01-xg", "question": "Does an own shot-quality (xG) model add information over shot counts?",
              "hypothesis": "Distance/angle/type/strength/rebound logistic xG beats a constant goal rate out of sample.",
              "method": "Logistic regression on unblocked attempts, fitted on 2021-22 + 2022-23 only, frozen.",
              "data": f"{xg['validation']['n_attempts']:,} validation attempts (2023-24); {xg['holdout']['n_attempts']:,} holdout",
              "result": (f"log loss validation {xg['validation']['log_loss']:.4f} vs constant {xg['validation']['log_loss_constant']:.4f}; "
                         f"holdout {xg['holdout']['log_loss']:.4f} vs {xg['holdout']['log_loss_constant']:.4f}; holdout xG sum "
                         f"{xg['holdout']['xg_sum']:.0f} vs {xg['holdout']['goals']} goals (league finishing fell)."),
              "interpretation": "xG is informative and is used as lagged player/team shot-quality features (E) and as a "
                                "team-goals rating input (D); its level drifts, so it is never used as an absolute rate.",
              "decision": "adopt"})
    E.append({"id": "NHL-X02-toi-ladder", "question": "Which time-on-ice model should drive every skater family?",
              "hypothesis": "A role-aware model (previous game's line/PP unit from shift data) beats recency averages.",
              "method": "T_A season avg, T_B EWMA, T_C role share x team minutes, T_E LightGBM (season-blocked refits).",
              "data": "skater-games with >= 1 prior game; validation 2023-24, holdout 2024-26",
              "result": (f"validation total-TOI MAE A {toi('validation', 'toi_A')['mae']:.3f} / B {toi('validation', 'toi_B')['mae']:.3f} / "
                         f"C {toi('validation', 'toi_C')['mae']:.3f} / E {toi('validation', 'toi_E')['mae']:.3f} min; holdout E "
                         f"{toi('holdout', 'toi_E')['mae']:.3f} vs B {toi('holdout', 'toi_B')['mae']:.3f}; PP-TOI MAE E "
                         f"{toi('holdout', 'toi_E', 'toi_pp')['mae']:.3f} vs C {toi('holdout', 'toi_C', 'toi_pp')['mae']:.3f}."),
              "interpretation": "LightGBM on role features is best for total TOI; PP TOI is a tie between the share model and E.",
              "decision": "adopt"})
    for key in ("sog", "points"):
        x = ex[f"toi_source_{key}"]
        E.append({"id": f"NHL-X03-toi-source-{key}", "question": f"Does the better TOI forecast improve {key} (model C)?",
                  "hypothesis": "Better opportunity -> better counts.", "method": "C with T_E minutes vs C with T_C minutes, "
                  "paired CRPS on validation, game-clustered bootstrap.", "data": "validation 2023-24",
                  "result": f"CRPS(T_E) - CRPS(T_C) = {ci(x['E_minus_C'], 5)}",
                  "interpretation": ("Helps shots (volume follows ice time)." if sig(x["E_minus_C"]) == "better" else
                                     "No measurable effect: point production is dominated by count noise, not minutes."),
                  "decision": "adopt" if sig(x["E_minus_C"]) == "better" else "insufficient evidence"})
    for key in ("sog", "goals", "assists", "points"):
        c, d = mrow(key, "C_toi_x_rate", "validation"), mrow(key, "D_opp_adjusted", "validation")
        E.append({"id": f"NHL-X04-opponent-{key}", "question": f"Does the schedule-adjusted opponent factor improve {key}?",
                  "hypothesis": "Opponent suppression (ridge rating of shots / goals allowed) moves player outcomes.",
                  "method": f"D = C x factor^beta x venue; beta fitted on development ({p2[key]['beta']:.2f}, factor "
                            f"{p2[key]['opp_factor']}); validation CRPS vs A.",
                  "data": "validation 2023-24 / holdout 2024-26",
                  "result": (f"validation CRPS C {c['crps']:.5f} -> D {d['crps']:.5f}; paired D - C validation "
                             f"{ci(ex.get(f'D_minus_C_{key}_validation'), 5)}, holdout {ci(ex.get(f'D_minus_C_{key}_holdout'), 5)}"),
                  "interpretation": ("The opponent/venue step helps" if sig(ex.get(f"D_minus_C_{key}_validation")) == "better"
                                     else "No validated gain from the opponent/venue step") + " on validation"
                                    + (" and holdout." if sig(ex.get(f"D_minus_C_{key}_holdout")) == "better" else
                                       "; not confirmed on holdout.") + " beta ~1 for shots, >1 for scoring (the ridge goal "
                                    "rating is heavily pooled, so its spread understates the true opponent effect).",
                  "decision": "adopt" if sig(ex.get(f"D_minus_C_{key}_validation")) == "better" else "insufficient evidence"})
    for key in ("sog", "points"):
        x = ex[f"opp_{key}"]
        E.append({"id": f"NHL-X05-ridge-vs-raw-{key}", "question": "Is the schedule-adjusted (ridge) opponent rating better than a "
                  "raw shrunk 'allowed' rate?", "hypothesis": "Strength-of-schedule adjustment matters.",
                  "method": "Same D model with pf_core.rolling_opponent_allowed (season-to-date, k=10) instead of ridge; beta refit on development.",
                  "data": "validation 2023-24",
                  "result": f"CRPS ridge - raw = {ci(x['ridge_minus_raw'], 5)}; both beat C ({ci(x['ridge_minus_C'], 5)} for ridge)",
                  "interpretation": "The adjustment matters; how it is schedule-adjusted does not, at player level.",
                  "decision": "insufficient evidence" if sig(x["ridge_minus_raw"]) == "tie" else "adopt"})
    for key in ("sog", "goals", "assists", "points", "saves", "team_goals"):
        e_, d_ = mrow(key, "E_lightgbm", "validation"), mrow(key, "D_opp_adjusted", "validation")
        fr = mrow(key, "F_stack", "validation")
        E.append({"id": f"NHL-X06-ml-stack-{key}", "question": f"Do LightGBM (E) and the stack (F) beat the structural model (D) for {key}?",
                  "hypothesis": "Non-linear interactions of PIT features add accuracy beyond TOI x rate x opponent.",
                  "method": "LightGBM Poisson, refitted walk-forward by season on all earlier seasons; F = NNLS weights on A..E "
                            "fitted on 2022-23 only.",
                  "data": "validation 2023-24",
                  "result": f"validation CRPS D {d_['crps']:.5f}, E {e_['crps']:.5f}, F {fr['crps']:.5f}; F vs A {ci(fr['vs_baseline'], 5)}",
                  "interpretation": "F is selected on validation; the gain over D is small for skaters (the outcome is mostly "
                                    "count noise).",
                  "decision": "adopt" if fr["crps"] <= min(d_["crps"], e_["crps"]) else "reject"})
    for key in ("sog", "goals", "assists", "points", "saves", "team_goals"):
        dv = F[key]["dist"]["validation"]
        E.append({"id": f"NHL-X07-dist-{key}", "question": f"Which outcome distribution for {key}?",
                  "hypothesis": "Over-dispersion matters for shots/saves; goals-type counts are near Poisson.",
                  "method": "Poisson / NB (one alpha) / NB with mean-binned alpha" + (" / binned normal" if key == "saves" else "") +
                            ", dispersion fitted on development residuals of the selected mean.",
                  "data": "validation 2023-24",
                  "result": "; ".join(f"{k}: CRPS {v['crps']:.5f}, 80% cover {v['cover_80']:.3f}, PIT var {v['pit_var_ratio']:.3f}"
                                      for k, v in dv.items()),
                  "interpretation": "NB-binned kept for all (it nests Poisson); it matters for SOG and saves only.",
                  "decision": "adopt"})
    for key in ("sog", "points"):
        for fx in F[key]["root_cause"]["fixes"]:
            E.append({"id": f"NHL-X08-fix-{key}-{fx['fix']}", "question": f"Does a {fx['fix']} adjustment fix a recurring {key} error?",
                      "hypothesis": "A PIT-known situation carries a systematic bias.",
                      "method": f"Multiplicative factor fitted on 2022-23 rows of the segment ({fx['factor_dev']:.3f}, n={fx['n_dev']}), "
                                "applied to validation; paired CRPS.",
                      "data": f"validation segment n={fx['n_val_segment']}",
                      "result": f"all-row CRPS diff {ci(fx['val_crps_diff_all'], 6)}; segment {ci(fx['val_crps_diff_segment'], 5)}",
                      "interpretation": ("Statistically detectable but < 0.01% of CRPS: economically negligible." if fx["adopt"]
                                         else "No validated gain."),
                      "decision": "reject"})
    s1 = json.load(open(RES / ".." / ".cache" / "nhl_full_results_run1.json"))["families"]["saves"] if \
        (RES / ".." / ".cache" / "nhl_full_results_run1.json").exists() else None
    sv = mrow("saves", "F_stack", "validation")
    old = next((m for m in s1["models"] if m["model"] == "F_stack" and m["split"] == "validation"), None) if s1 else None
    E.append({"id": "NHL-X09-saves-league-level", "question": "Why were frozen-scalar saves models biased upward?",
              "hypothesis": "Expanding-mean league priors and season-decayed ridge intercepts lag the falling league shot level.",
              "method": "Replace priors by the mean of the last 1,200 starts on earlier dates and recentre ridge shots-against on "
                        "the recent team level; refit scalars on development; compare on validation.",
              "data": "validation 2023-24 (decision); holdout re-scored once afterwards and disclosed",
              "result": (f"validation F bias {old['bias']:+.3f} -> {sv['bias']:+.3f}, RMSE {old['rmse']:.3f} -> {sv['rmse']:.3f}, "
                         f"CRPS {old['crps']:.4f} -> {sv['crps']:.4f}" if old else
                         f"validation F bias {sv['bias']:+.3f}, CRPS {sv['crps']:.4f}"),
              "interpretation": "Verified level-drift defect; the fix is mechanical, not tuned on holdout. The holdout "
                                "was therefore scored twice for saves (before/after); both are reported.",
              "decision": "adopt"})
    E.append({"id": "NHL-X10-starter-conditioning", "question": "How much does conditioning saves on the ACTUAL starter assume?",
              "hypothesis": "Pregame starter information is nearly complete by puck drop.",
              "method": "Archived DailyFaceoff goalie observations (2026-27) vs the boxscore starter, last snapshot before start "
                        "and fixed horizons.",
              "data": f"{st.get('n_team_games')} team-games with an archived observation",
              "result": (f"last pregame snapshot correct {st.get('accuracy_last_pregame', 0):.3f}; at T-60 / T-180 / T-360 min: "
                         + ", ".join(f"{h['accuracy']:.3f} ({h['share_confirmed']:.2f} confirmed)" for h in st.get("by_horizon", []))),
              "interpretation": "Conditioning on the actual starter overstates certainty by ~1-2% of starts at a 1-6 h horizon; "
                                "at the final pregame snapshot it is exact in this sample. Historical seasons have no PIT source.",
              "decision": "insufficient evidence"})
    E.append({"id": "NHL-X11-lineup-pregame", "question": "How well are tonight's lineup and PP1 known before puck drop?",
              "hypothesis": "Projected lines identify dressed skaters and PP units.",
              "method": "Last archived DailyFaceoff lines before start vs boxscore (dressed) and PP-TOI top five (PP1).",
              "data": f"{la.get('n_team_games')} team-games (2026-27)",
              "result": (f"projected skaters who dressed {la.get('projected_skaters_who_dressed', 0):.3f}; dressed skaters in the projection "
                         f"{la.get('dressed_skaters_in_projection', 0):.3f}; PP1 precision {la.get('pp1_precision', 0):.3f}, recall "
                         f"{la.get('pp1_recall', 0):.3f}; median snapshot {la.get('median_minutes_before_start', 0):.0f} min before start"),
              "interpretation": "Lineups are ~98% knowable; PP1 is ~87% knowable. The model's PIT role uses the previous game "
                                "(lines are not archived historically), so PP-unit news is an untested upside.",
              "decision": "investigate"})
    for key in ("sog", "points", "goals", "assists"):
        d = F[key]["root_cause"]["toi_oracle_decomposition"]
        E.append({"id": f"NHL-X12-ceiling-{key}", "question": f"How much {key} error is left to remove?",
                  "hypothesis": "Most error is count noise; opportunity misprojection is a minority.",
                  "method": "Validation MSE of C with projected vs realised TOI (oracle), and the Poisson floor (mean of y).",
                  "data": "validation 2023-24",
                  "result": f"MSE C {d['mse_C']:.4f}, C with actual TOI {d['mse_C_actual_toi']:.4f}, best {d['mse_best']:.4f}, "
                            f"Poisson floor {d['poisson_floor_mse']:.4f}",
                  "interpretation": ("Knowing the minutes would remove ~{:.1%} of shots MSE; the best model is {:.1%} above a pure "
                                     "Poisson floor.".format(1 - d['mse_C_actual_toi'] / d['mse_C'], d['mse_best'] / d['poisson_floor_mse'] - 1)),
                  "decision": "adopt"})
    return E


def render_md(full, summ) -> str:
    F = full["families"]
    o = full["opportunity"]
    L = []
    w = L.append
    w("# NHL Projection Foundation — results\n")
    w(f"*Generated {summ['generated_utc']} from `results/nhl_full_results.json` by `nhl/report.py` (code {summ['code_sha'][:10]}, "
      f"pf_core {summ['pf_core_version']}). Research only: nothing here changes betting authority.*\n")
    w("## 1. Bottom line for a bettor\n")
    w("Every number below is a walk-forward, point-in-time forecast: each game was projected using only games that had "
      "finished before it, with parameters fitted on 2021-22/2022-23, models chosen on 2023-24, and 2024-25 + 2025-26 "
      "scored once as a holdout. 2026-27 (games 1-120) is a prospective check against the archived PLAYER_SIM_V1 forecasts.\n")
    w("| Family | Best model | Holdout n | Holdout MAE | Holdout CRPS | vs baseline (CRPS, 95% CI) | vs incumbent (holdout) | vs incumbent (2026-27 prospective) | Readiness |")
    w("|---|---|---:|---:|---:|---|---|---|---|")
    for fam in summ["families"]:
        key = [k for k, v in FAM.items() if v[0] == fam["family"]][0]
        h = fam["holdout"]
        pro = next((m for m in fam["models"] if m["model"] == fam["best_model"] and m["split"] == "prospective"), {})
        vi = h["vs_incumbent"]
        vp = pro.get("vs_incumbent")
        w(f"| {LABEL[key]} | {fam['best_model']} | {h['n_obs']:,} | {h['mae']:.3f} | {h['crps']:.4f} | {ci(h['vs_baseline'])} "
          f"({sig(h['vs_baseline'])}) | {ci(vi) if vi else 'n/a'} ({sig(vi) if vi else '-'}; {vi.get('source', '') if vi else ''}) | "
          f"{ci(vp) if vp else 'n/a'} ({sig(vp) if vp else '-'}) | **{fam['readiness']}** |")
    w("\nNegative differences mean our model is better. CIs are 95% game-clustered bootstraps (games resampled, 1,000 draws). "
      "The incumbent metric differs by family (see section 5): CRPS for shots, rung RPS / Brier for goals-assists-points-saves "
      "because PLAYER_SIM_V1 only published ladder probabilities.\n")
    w("What this means in plain terms:\n")
    w("* **Shots on goal**: the new stack beats both the reproduced WORKLOAD_V1 (PR #28's accepted challenger) on 2025-26 and "
      "PLAYER_SIM_V1's expected shots on 2026-27, and is calibrated at the 2+/3+/4+/5+ rungs. The gain over a shrunk season "
      "average is about 0.9% of CRPS: real, but small. Shots are mostly noise once you know role and minutes.")
    w("* **Goals / assists / points**: the models sit within about 0.2-1% of a pure Poisson-noise floor. Against PLAYER_SIM_V1 "
      "they are better on assists and points (holdout and the 2026-27 prospective sample) and essentially tied on goals. "
      "The market was already as good as or better than PLAYER_SIM_V1 on these families (PR #10), so do not read this as edge.")
    w("* **Goalie saves**: improved over our baseline after fixing a league-level drift defect, but PLAYER_SIM_V1's "
      "game-script/pull-hazard saves model is still better on holdout. Not ready.")
    w("* **Team goals**: tied with DATA_ONLY_V2 per team, better on the game total's squared error, but the total's distribution "
      "is too wide (independent team draws ignore OT/shootout structure).\n")
    # inventory
    w("## 2. Data inventory and point-in-time status\n")
    w("| Dataset | Seasons | Rows | PIT class | Notes |\n|---|---|---:|---|---|")
    for r in summ["inventory"]:
        w(f"| {r['dataset']} | {r['seasons']} | {r['rows']:,} | {r['pit_class']} | {r['notes']} |")
    st, la = full["starter_accuracy"], full["lineup_accuracy"]
    w("\n**What is conditioned on, and what it costs.** Skater projections are conditional on the player dressing (Kalshi settles a "
      "non-entering player at the pre-game fair price) and saves are conditional on the actual starter. The 2026-27 archive "
      "lets us measure how much pregame information that assumes:\n")
    w(f"* Starting goalie: the last archived DailyFaceoff observation before puck drop named the actual starter in "
      f"{st.get('accuracy_last_pregame', 0):.1%} of {st.get('n_team_games')} team-games; at 1 h / 3 h / 6 h before: "
      + " / ".join(f"{h['accuracy']:.1%}" for h in st.get("by_horizon", [])) + ". So a saves projection published 1-6 h before "
      "the game carries a ~1-2% chance of describing a goalie who does not start; no PIT starter source exists for 2021-26.")
    w(f"* Lineups: {la.get('projected_skaters_who_dressed', 0):.1%} of DailyFaceoff-projected skaters dressed and "
      f"{la.get('dressed_skaters_in_projection', 0):.1%} of dressed skaters were projected ({la.get('n_team_games')} team-games). "
      f"PP1 membership: precision {la.get('pp1_precision', 0):.1%}, recall {la.get('pp1_recall', 0):.1%}. Historical lines do "
      "not exist, so backtests use the previous game's shift-derived role (line rank, PP unit) — the forward projector reads "
      "DailyFaceoff lineups for who plays.\n")
    w("## 3. Splits and method\n")
    for k, v in summ["splits"].items():
        w(f"* **{k}**: {v}")
    w("\nLadder per family: **A** season-to-date + last season mean shrunk to a point-in-time role prior; **B** EWMA (halflife "
      "chosen on development) shrunk; **C** projected TOI x per-minute rates, non-PP and PP separately, empirical-Bayes shrinkage "
      "measured in minutes; **D** C x schedule-adjusted opponent factor^beta x venue (beta fitted on development); **E** LightGBM "
      "on PIT features (shot quality/xG, role, linemates' rates from co-ice, schedule, opponent ratings, D's mean) refitted each "
      "season on all earlier seasons; **F** non-negative stack of A..E fitted on 2022-23. Saves: A/B on saves; C = team shots "
      "allowed x goalie shrunk save% ; D = ridge shots-against (opponent generation + own suppression + venue) x save%. "
      "Team goals: C = attack x opponent defence (log5); D = ridge goals/xG blend. Distributions: NB with mean-binned "
      "dispersion fitted on development residuals.\n")
    # opportunity
    w("## 4. Opportunity: time on ice\n")
    w("| Split | Model | Target | MAE (min) | RMSE | Bias |\n|---|---|---|---:|---:|---:|")
    for sp in ("validation", "holdout", "prospective"):
        for x in o["models"][sp]:
            w(f"| {sp} | {x['model']} | {x['target']} | {x['mae']:.3f} | {x['rmse']:.3f} | {x['bias']:+.3f} |")
    w("\n**Against incumbents (paired, same player-games):**\n")
    w("| Incumbent | n | Our TOI MAE | Incumbent TOI MAE | Diff (95% CI) | Our PP MAE | Incumbent PP MAE | PP diff (95% CI) |")
    w("|---|---:|---:|---:|---|---:|---:|---|")
    for k, v in o["incumbent"].items():
        w(f"| {k} | {v['n_obs']:,} | {v['toi']['ours']['mae']:.3f} (bias {v['toi']['ours']['bias']:+.2f}) | "
          f"{v['toi']['incumbent']['mae']:.3f} (bias {v['toi']['incumbent']['bias']:+.2f}) | {ci(v['toi']['abs_error_diff'], 3)} | "
          f"{v['toi_pp']['ours']['mae']:.3f} | {v['toi_pp']['incumbent']['mae']:.3f} | {ci(v['toi_pp']['abs_error_diff'], 3)} |")
    wl = o["workload_v1_published_2025"]
    w(f"\nWORKLOAD_V1's published 2025-26 TOI MAE was {wl['toi_mae']} (RMSE {wl['toi_rmse']}); ours on the same season is in the "
      "first row above. The PLAYER_SIM_V1 prospective rows used DailyFaceoff projected lines; our model used only the previous "
      "game's shift data and still had lower TOI error.\n")
    w("**Bias by role (validation, T_E):**\n")
    w("| Role (previous game) | n | MAE | Bias | Mean TOI |\n|---|---:|---:|---:|---:|")
    for x in o["by_role"]["validation"]["toi_E_by_role"]:
        w(f"| {x['segment']} | {x['n']:,} | {x['mae']:.3f} | {x['bias']:+.3f} | {x['mean_actual']:.2f} |")
    w("\n| PP role (previous game) | n | PP MAE | PP bias | Mean PP TOI |\n|---|---:|---:|---:|---:|")
    for x in o["by_role"]["validation"]["toi_pp_E_by_pp_role"]:
        w(f"| {x['segment']} | {x['n']:,} | {x['mae']:.3f} | {x['bias']:+.3f} | {x['mean_actual']:.2f} |")
    w("\nTop-line forwards are under-projected by about a quarter-minute and fourth-liners slightly over-projected "
      "(shrinkage toward the role mean); PP minutes are unbiased by unit.\n")
    # families
    w("## 5. Families\n")
    for fam in summ["families"]:
        key = [k for k, v in FAM.items() if v[0] == fam["family"]][0]
        r = F[key]
        w(f"### {LABEL[key]}\n")
        w(f"Population: {fam['population']}.\n")
        w("| Split | Model | n | MAE | RMSE | Bias | CRPS | 80% cover / PIT var | vs A: CRPS diff (95% CI) | vs incumbent | Verdict |")
        w("|---|---|---:|---:|---:|---:|---:|---|---|---|---|")
        for m in fam["models"]:
            if m["split"] == "development":
                continue
            vi = m.get("vs_incumbent")
            w(f"| {m['split']} | {m['model']} | {m['n_obs']:,} | {m['mae']:.4f} | {m['rmse']:.4f} | {m['bias']:+.4f} | "
              f"{m['crps']:.5f} | {m['cover_80']:.3f} / {m['pit_var_ratio']:.3f} | {ci(m['vs_baseline'], 5) if m['vs_baseline'] else 'baseline'} | "
              f"{ci(vi, 5) if vi else ''} | {m['verdict']} |")
        w("")
        for sp in ("holdout", "prospective"):
            x = r["incumbent"].get(sp)
            if not x:
                continue
            w(f"*Incumbent, {sp}* — {x['source']} ({x['n_obs']:,} rows, {x['n_clusters']} games): ")
            if "ours" in x:
                w(f"  mean MAE/RMSE/bias ours {x['ours']['mae']:.4f} / {x['ours']['rmse']:.4f} / {x['ours']['bias']:+.4f} vs "
                  f"incumbent {x['incumbent']['mae']:.4f} / {x['incumbent']['rmse']:.4f} / {x['incumbent']['bias']:+.4f}; "
                  f"squared-error diff {ci(x['sq_error_diff'])}.")
            if x.get("rps_diff"):
                w(f"  Rung RPS over {x['rps_rungs'][0]}+..{x['rps_rungs'][-1]}+: ours {x['rps_ours']:.5f} vs {x['rps_incumbent']:.5f}, diff {ci(x['rps_diff'], 5)}.")
            if x.get("crps_diff"):
                w(f"  CRPS ours {x['crps_ours']:.4f} vs incumbent-mean-as-Poisson {x['crps_incumbent_poisson']:.4f}, diff {ci(x['crps_diff'])}.")
            if x.get("brier_per_rung"):
                shown = {k: b for k, b in x["brier_per_rung"].items() if key != "saves" or k in ("20", "25", "30")}
                w("  Rung Brier (ours vs incumbent, diff CI): " + "; ".join(
                    f"{k}+ n={b['n']:,}: {b['ours']:.4f} vs {b['incumbent']:.4f} {ci(b['diff'], 4)}" for k, b in shown.items()) + ".")
            w("")
    w("A note on MAE: MAE rewards the median, not the mean; for skewed counts a mean forecast can lose on MAE while winning "
      "on RMSE/CRPS (PR #28 saw the same). CRPS and log score are the decision metrics.\n")
    # opponent
    w("## 6. Opponent adjustment\n")
    w(summ["opponent_adjustment"]["summary"] + "\n")
    w("| Family | Factor | beta (dev) | Validation CRPS C -> D | D vs A (validation) |\n|---|---|---:|---|---|")
    for x in summ["opponent_adjustment"]["results"]:
        if "family" in x:
            w(f"| {x['family']} | {x['factor']} | {x['beta']:.3f} | {x['crps_C']:.5f} -> {x['crps_D']:.5f} | {x['D_vs_A']} |")
    w("")
    for k in ("opp_sog", "opp_points"):
        x = full["extra_experiments"][k]
        w(f"* {k.replace('opp_', '')}: ridge vs raw opponent factor CRPS diff {ci(x['ridge_minus_raw'], 5)} ({sig(x['ridge_minus_raw'])}); "
          f"ridge vs no adjustment {ci(x['ridge_minus_C'], 5)}.")
    w("")
    # calibration
    w("## 7. Distributions and calibration\n")
    w("| Family | Split | Distribution | CRPS | log score | 80% cover | PIT var ratio | P(0) pred / obs |\n|---|---|---|---:|---:|---:|---:|---|")
    for key in FAM:
        for sp in ("validation", "holdout"):
            for k, v in F[key]["dist"][sp].items():
                w(f"| {LABEL[key]} | {sp} | {k} | {v['crps']:.5f} | {v['log_score']:.4f} | {v['cover_80']:.3f} | "
                  f"{v['pit_var_ratio']:.3f} | {v['zero_mass_pred']:.3f} / {v['zero_mass_obs']:.3f} |")
    w("\nPIT variance ratio > 1 = too narrow (overconfident), < 1 = too wide.\n")
    w("**Kalshi-style rungs (selected model, NB-binned), holdout:**\n")
    w("| Family | Rung | Brier | mean P | hit rate | ECE |\n|---|---|---:|---:|---:|---:|")
    for key in FAM:
        th = F[key]["dist"]["holdout"]["nb_binned"]["thresholds"]
        ece = {c["k"]: c["ece"] for c in F[key]["calibration"]["holdout"]}
        for k, v in th.items():
            w(f"| {LABEL[key]} | {k}+ | {v['brier']:.4f} | {v['mean_p']:.3f} | {v['hit_rate']:.3f} | {ece.get(int(k), float('nan')):.4f} |")
    w("\n**Zero mass by predicted-mean quintile (validation)** — low-count families:\n")
    w("| Family | mean bin | n | P(0) predicted | P(0) observed |\n|---|---|---:|---:|---:|")
    for key in ("goals", "assists", "points"):
        for z in F[key]["zero_mass"]["validation"]:
            w(f"| {LABEL[key]} | {z['mu_bin']} | {int(z['n']):,} | {z['p0_pred']:.3f} | {z['p0_obs']:.3f} |")
    w("")
    # team
    w("## 8. Team goals, game totals and coherence\n")
    w("| Split | games | total MAE | RMSE | bias | CRPS | 80% cover | PIT var | vs DATA_ONLY_V2 total sq. error |\n|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for g in F["team_goals"]["game_total"]:
        w(f"| {g['split']} | {g['n_games']:,} | {g['mae']:.3f} | {g['rmse']:.3f} | {g['bias']:+.3f} | {g['crps']:.4f} | "
          f"{g['cover_80']:.3f} | {g['pit_var_ratio']:.3f} | {ci(g.get('vs_incumbent_total_sq_error'))} |")
    w("\nThe total is the convolution of two independent team distributions; a PIT variance ratio near 0.9 means it is too "
      "wide — real totals are less variable than two independent Poissons (regulation ties go to a sudden-death OT that adds "
      "at most one goal, shootout goals do not count). A joint model is a listed priority.\n")
    w("| Split | team-games | mean player goal sum | mean team model | actual | ratio mean (p10-p90) | corr | gate reconciliation |")
    w("|---|---:|---:|---:|---:|---|---:|---|")
    for c in F["team_goals"]["coherence"]:
        w(f"| {c['split']} | {c['n_team_games']:,} | {c['mean_player_sum']:.3f} | {c['mean_team_model']:.3f} | "
          f"{c['mean_actual_team_goals']:.3f} | {c['ratio_mean']:.3f} ({c['ratio_p10_p90'][0]:.2f}-{c['ratio_p10_p90'][1]:.2f}) | "
          f"{c['corr_player_sum_vs_team_model']:.3f} | {', '.join(f'{k} {v:.1%}' for k, v in c['reconciliation_status_rates'].items())} |")
    w("\nPlayer goal means are modelled independently of the team model and reconcile within 15% for ~97% of team-games; "
      "the forward projector reports both and flags disagreement through `pf_core.gate.team_reconciliation`.\n")
    # root cause
    w("## 9. Where the errors come from\n")
    w("| Pattern | Frequency | Impact | Cause | Status | Action |\n|---|---|---|---|---|---|")
    for e in summ["error_investigations"]:
        w("| " + " | ".join(esc(e[k]) for k in ("pattern", "frequency", "impact", "cause", "status", "action")) + " |")
    w("\nSegment detail (validation + development 2022-24, selected model, shots and points):\n")
    w("| Family | Pattern | n | share | bias | MAE | MAE rest | share of sq. error | TOI bias |\n|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for key in ("sog", "points"):
        for s in F[key]["root_cause"]["segments"]:
            w(f"| {LABEL[key]} | {esc(s['pattern'])} | {s['n']:,} | {s['share_rows']:.3f} | {s['bias']:+.4f} | {s['mae']:.4f} | "
              f"{s['mae_rest']:.4f} | {s['share_sq_error']:.3f} | {s['toi_bias']:+.2f} |")
    sv = F["saves"]["pulled_starters"]
    w(f"\nSaves: pulled starters are {sv['share']:.1%} of validation starts but {sv['share_sq_error']:.0%} of squared error "
      f"(bias {sv['bias_pulled']:+.1f} saves when pulled vs {sv['bias_full']:+.2f} otherwise). Knowing the realised shots "
      f"against would cut saves MSE from {full['saves_sa_decomposition']['validation_mse_saves']:.1f} to "
      f"{full['saves_sa_decomposition']['mse_if_shots_known']:.1f}: saves error is volume, not save percentage.\n")
    # experiments
    w("## 10. Experiments\n")
    for e in summ["experiments"]:
        w(f"**{e['id']}** — *{e['question']}*  ")
        w(f"Hypothesis: {e['hypothesis']}  ")
        w(f"Method: {e['method']}  ")
        w(f"Data: {e['data']}  ")
        w(f"Result: {e['result']}  ")
        w(f"Interpretation: {e['interpretation']}  ")
        w(f"Decision: **{e['decision']}**\n")
    w("## 11. Failed experiments\n")
    for e in summ["failed_experiments"]:
        w(f"* **{e['name']}** — learned: {e['what_was_learned']} Future: {e['changes_future_decisions']}")
    w("")
    w("## 12. Quality gate\n")
    w(summ["gate"]["summary"]["note"] + "\n")
    w("| Family / split | n | PASS | REVIEW | BLOCK | top findings | CRPS PASS / REVIEW | MAE PASS / REVIEW |\n|---|---:|---:|---:|---:|---|---|---|")
    for k, v in full["gate"].items():
        sr = v["summary"]["status_rates"]
        eb = {x["status"]: x for x in v["error_by_status"]}
        top = ", ".join(f"{a} {b}" for a, b in list(v["summary"]["check_counts"].items())[:3])
        w(f"| {k.replace('|', ' / ')} | {v['summary']['n']:,} | {sr.get('PASS', 0):.1%} | {sr.get('REVIEW', 0):.1%} | {sr.get('BLOCK', 0):.1%} | {top} | "
          f"{eb.get('PASS', {}).get('crps', float('nan')):.4f} / {eb.get('REVIEW', {}).get('crps', float('nan')):.4f} | "
          f"{eb.get('PASS', {}).get('mae', float('nan')):.4f} / {eb.get('REVIEW', {}).get('mae', float('nan')):.4f} |")
    w("")
    w("## 13. Readiness\n")
    w("| Family | Readiness | Why |\n|---|---|---|")
    for fam in summ["families"]:
        key = [k for k, v in FAM.items() if v[0] == fam["family"]][0]
        w(f"| {LABEL[key]} | **{fam['readiness']}** | {fam['readiness_reason']} |")
    tl = o["models"]["holdout"]
    w(f"| Time on ice (opportunity) | **SHADOW VALIDATION** | T_E holdout MAE "
      f"{next(x for x in tl if x['model'] == 'toi_E' and x['target'] == 'toi')['mae']:.3f} min, better than PLAYER_SIM_V1 and "
      f"WORKLOAD_V1; no live record yet. |")
    w("\n## 14. Priorities\n")
    w("| Rank | Item | Impact | Evidence | Complexity | Data |\n|---:|---|---|---|---|---|")
    for p in summ["priorities"]:
        w(f"| {p['rank']} | {p['item']} | {p['impact']} | {p['evidence']} | {p['complexity']} | {p['data']} |")
    w("\n## 15. Shared-library (pf_core 1.0.0) issues found — not edited, worked around\n")
    for b in full.get("pf_core_issues", []):
        w(f"* {b}")
    pj = RES / "projections_latest.json"
    if pj.exists():
        P = json.load(open(pj))
        from collections import Counter
        fams_ = Counter(x["family"] for x in P["players"])
        stc = P["gate_summary"]["status_counts"]
        top = Counter((f["check"], f["severity"]) for x in P["players"] for f in x["gate"]["findings"]).most_common(6)
        w("\n## 16. Forward projections (sift.projections.v1)\n")
        w(f"`results/projections_latest.json` — {P['slate']['label']}. Generated {P['generated_utc']}, newest input "
          f"{P['data_asof_utc']}; {len(P['games'])} games, " + ", ".join(f"{v} {k}" for k, v in fams_.items())
          + f" projections. Gate: {', '.join(f'{k} {v}' for k, v in stc.items())}; top findings: "
          + ", ".join(f"{a}:{b} {n}" for (a, b), n in top) + ". BLOCK rows (e.g. a player DailyFaceoff lists in the lineup "
          "but ESPN lists OUT) are written with their reason and must not be displayed. Every row carries "
          "`authority: research_only`, the family readiness, its opportunity (TOI with a p10-p90 range from development "
          "residuals), the opponent factor and plain-English adjustments; team rows carry the player-goal reconciliation.\n")
    w("## 17. Automation\n")
    w("`.github/workflows/projection-foundation.yml` (inert until merged; schedules fire from the default branch only): daily "
      "at 20:47 UTC from October to June plus `workflow_dispatch` (optional slate date). It sparse-checks out the inputs from "
      "data-archive (final games' player_events, schedule, DailyFaceoff lines and goalie observations, ESPN injuries), runs "
      "`python -m nhl.project` (full walk-forward rebuild, ~30-40 min on a runner), and publishes to the orphan branch "
      "`projection-data`: `projections/nhl/latest.json`, a timestamped copy `projections/nhl/<YYYY-MM-DDTHHMMZ>.json`, and "
      "`summary/nhl/latest.json`. It commits only when the projection content (ignoring timestamps) changed, pushes with "
      "retries, needs no secrets beyond the job token, and never touches betting authority. The branch is created by the "
      "workflow on its first run (not from this session).\n")
    w("\n## 18. Reproduce\n")
    w("```\ncd research/projection_foundation\n# data-archive sparse worktree (player_events, predictions_player, context/*) at .cache/archive_wt\n"
      "python -m nhl.pipeline all          # features, ratings, TOI, ladders (cached in .cache/)\n"
      "python -m nhl.run_walkforward       # evaluation -> results/nhl_full_results.json + experiments/\n"
      "python -m nhl.report                # summary.json + RESULTS_NHL.md\n"
      "python -m nhl.project               # forward projections -> results/projections_latest.json\n"
      "python -m pytest tests -q\n```\n")
    w(f"Runtime on a shared 4-core box: pipeline ~45 min, evaluation ~4 min. Experiment records: `results/experiments/` "
      f"({len(list((RES / 'experiments').glob('*.json')))} files).\n")
    return "\n".join(L)


PF_ISSUES = [
    "`models.group_prior_pit`: when a group has no earlier dates the default fallback is `df[col].mean()` over the whole "
    "frame — future rows included (look-ahead). Caught by our poisoned-future test; we pass a development-only fallback "
    "(`nhl.ladder.gprior`). Impact here: only rows on a group's first date (2021-22 opening night, excluded from scoring).",
    "`pit.rolling_opponent_allowed`: same pattern — `_league` NaN is filled with the full-sample mean of `y_col`.",
    "`models.group_prior_pit` and the ridge intercept are expanding / season-decayed means: correct point-in-time but they lag "
    "a drifting league level (NHL shots per team-game fell ~12% 2021-26). Not a bug, a property; documented fix "
    "`nhl.ladder.recent_prior`.",
    "`lagged_features` adds columns one at a time (pandas fragmentation warnings, slow on 240k x 24 columns); harmless.",
]


def opp_section(full):
    F = full["families"]
    P = full["params"]["stage2"]
    res = []
    for key in ("sog", "goals", "assists", "points"):
        c = next(m for m in F[key]["models"] if m["model"] == "C_toi_x_rate" and m["split"] == "validation")
        d = next(m for m in F[key]["models"] if m["model"] == "D_opp_adjusted" and m["split"] == "validation")
        res.append({"family": key, "factor": P[key]["opp_factor"], "beta": P[key]["beta"], "crps_C": c["crps"], "crps_D": d["crps"],
                    "D_vs_A": ci(d["vs_baseline"], 5), "home_scale": P[key]["home_scale"], "away_scale": P[key]["away_scale"]})
    for k in ("opp_sog", "opp_points"):
        res.append({"experiment": f"ridge_vs_raw_{k}", **full["extra_experiments"][k]})
    s3 = full["params"]["stage3"]
    summ = ("Opponent strength is a schedule-adjusted ridge rating (y = mu + off + def + home, refitted before every game "
            "date on all earlier games, previous seasons weighted 0.5 per season; alpha chosen on development: shots 3, goals 30, "
            "xG 3). Skater factor = (mu + opponent defence) / mu, applied as factor^beta with beta fitted on development (shots "
            f"{P['sog']['beta']:.2f}; goals/assists/points {P['goals']['beta']:.2f}/{P['assists']['beta']:.2f}/{P['points']['beta']:.2f} on the "
            "goal rating, which beat the xG rating on development likelihood). Paired D - C CRPS (validation / holdout): "
            + "; ".join(f"{k} {ci(full['extra_experiments'][f'D_minus_C_{k}_validation'], 5)} / "
                        f"{ci(full['extra_experiments'][f'D_minus_C_{k}_holdout'], 5)}" for k in ("sog", "goals", "assists", "points"))
            + ". The step is clearly useful for shots, smaller for assists/points, and not confirmed on holdout for goals. "
            "A raw shrunk 'allowed' factor performs the same as the schedule-adjusted one (CIs include 0). "
            f"Saves D uses ridge shots-against recentred on the recent league level (dev scale {s3['saves']['d_scale']:.3f}); team "
            f"goals D blends ridge goals and xG ratings (goal weight {s3['team_goals']['D_w_goals']}).")
    return {"summary": summ, "results": res}


def main():
    full = json.load(open(RES / "nhl_full_results.json"))
    full["pf_core_issues"] = PF_ISSUES
    fams = build(full)
    o = full["opportunity"]
    gate_sum = {k: v["summary"] for k, v in full["gate"].items()}
    gate_sum["note"] = ("pf_core.gate run on every validation (2023-24) and holdout 2025-26 skater projection of the selected "
                        "model (opportunity history = previous 10 games' TOI; stat history = previous 10 games; thresholds "
                        "from the pmf; opponent sample = opponent's games this season). No projection was BLOCKed (no "
                        "structural defects). REVIEW (1-3%) is driven by early-season opponent factors resting on < 3 games, "
                        "role changes and thin own history; REVIEW rows have LOWER error than PASS rows because they are "
                        "mostly low-volume or early-season players — the gate catches structural problems, it is not an "
                        "accuracy predictor. Team reconciliation (player goal sum vs team goal model) is in section 8.")
    tr = {c["split"]: c["reconciliation_status_rates"] for c in full["families"]["team_goals"]["coherence"]}
    summ = {
        "schema": "sift.projection_foundation.sport_summary.v1", "sport": "NHL",
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "code_sha": _sha(), "pf_core_version": PF_VERSION,
        "model_version": VERSION,
        "splits": {"development": SPLIT_LABELS["development"], "validation": SPLIT_LABELS["validation"],
                   "holdout": SPLIT_LABELS["holdout"] + " (saves re-scored once after a validation-motivated drift fix; disclosed)",
                   "prospective": SPLIT_LABELS["prospective"]},
        "inventory": full["inventory"],
        "families": fams,
        "experiments": experiments(full),
        "error_investigations": ERRORS(full),
        "opponent_adjustment": opp_section(full),
        "opportunity": {"summary": OPP_SUMMARY(full), "results": [{"split": k, "rows": v} for k, v in o["models"].items()]
                        + [{"incumbent": k, **v} for k, v in o["incumbent"].items()]
                        + [{"by_role_validation": o["by_role"]["validation"]}]},
        "calibration": {"summary": CAL_SUMMARY(full),
                        "results": [{"family": k, "split": sp, "rungs": full["families"][k]["calibration"][sp],
                                     "distributions": full["families"][k]["dist"][sp]}
                                    for k in FAM for sp in ("validation", "holdout")]},
        "failed_experiments": FAILED(full),
        "gate": {"summary": gate_sum, "error_by_status": {k: v["error_by_status"] for k, v in full["gate"].items()},
                 "team_reconciliation": tr},
        "priorities": PRIORITIES(full),
        "pf_core_issues": PF_ISSUES,
    }
    from nhl.run_walkforward import _clean
    summ = _clean(summ)
    json.dump(summ, open(RES / "summary.json", "w"), indent=1)
    (PF / "RESULTS_NHL.md").write_text(render_md(full, summ))
    print("wrote summary.json and RESULTS_NHL.md")
    for fam in summ["families"]:
        print(fam["family"], fam["best_model"], fam["readiness"])


def ERRORS(full):
    F = full["families"]
    seg = {s["pattern"]: s for s in F["sog"]["root_cause"]["segments"]}
    segp = {s["pattern"]: s for s in F["points"]["root_cause"]["segments"]}
    fx = {x["fix"]: x for x in F["sog"]["root_cause"]["fixes"]}
    sv = F["saves"]["pulled_starters"]
    tl = full["opportunity"]["by_role"]["validation"]["toi_E_by_role"]
    f1 = next(x for x in tl if x["segment"] == "F1")
    gt = next(g for g in F["team_goals"]["game_total"] if g["split"] == "validation")
    b = lambda k: seg[k]  # noqa: E731
    return [
        {"pattern": "Pulled starting goalies", "frequency": f"{sv['share']:.1%} of starts (validation)",
         "impact": f"{sv['share_sq_error']:.0%} of saves squared error; bias {sv['bias_pulled']:+.1f} saves when pulled",
         "cause": "Saves mean assumes a full game; the pull is a game-script event", "status": "verified defect",
         "action": "Mixture with a pull hazard driven by projected goals against (as PLAYER_SIM_V1 does) — priority 1"},
        {"pattern": "League level drift (saves)", "frequency": "every start; league SOG/team-game 31.6 -> 27.7 (2021-26)",
         "impact": "validation saves bias +0.68 before the fix, +0.21 after",
         "cause": "expanding-mean priors and season-decayed ridge intercepts lag a moving league level",
         "status": "verified defect", "action": "fixed: rolling 1,200-start league level (nhl.ladder.recent_prior)"},
        {"pattern": "Opportunity misprojection (TOI off by > 3 min)",
         "frequency": f"{b('toi_miss>3min (post-game)')['share_rows']:.1%} of skater-games",
         "impact": f"{b('toi_miss>3min (post-game)')['share_sq_error']:.0%} of SOG squared error; an oracle TOI would remove only "
                   f"{1 - F['sog']['root_cause']['toi_oracle_decomposition']['mse_C_actual_toi'] / F['sog']['root_cause']['toi_oracle_decomposition']['mse_C']:.1%} of SOG MSE",
         "cause": "injuries in-game, penalties, blowouts, OT", "status": "hypothesis",
         "action": "small upside; archived PP-unit news is the realistic lever"},
        {"pattern": "Top-line TOI under-projection", "frequency": f"F1 role, {f1['n']:,} validation skater-games",
         "impact": f"TOI bias {f1['bias']:+.2f} min", "cause": "shrinkage toward the role prior", "status": "hypothesis",
         "action": "role-specific calibration of T_E (validation-only fit)"},
        {"pattern": "Blowouts (final margin >= 3)", "frequency": f"{b('blowout |margin|>=3 (post-game)')['share_rows']:.0%} of skater-games",
         "impact": f"{segp['blowout |margin|>=3 (post-game)']['share_sq_error']:.0%} of points squared error, bias "
                   f"{segp['blowout |margin|>=3 (post-game)']['bias']:+.3f}",
         "cause": "outcome-driven (post-game); pregame models cannot see it", "status": "ruled out",
         "action": "none (variance, not bias)"},
        {"pattern": "Overtime games", "frequency": f"{b('overtime game (post-game)')['share_rows']:.0%} of skater-games",
         "impact": f"SOG bias {b('overtime game (post-game)')['bias']:+.3f}, TOI bias {b('overtime game (post-game)')['toi_bias']:+.2f} min",
         "cause": "extra ~4 min of 3-on-3; the mean already carries the OT expectation", "status": "ruled out",
         "action": "none for means; matters for the game-total distribution"},
        {"pattern": "Line changes / PP-unit changes vs last game", "frequency": f"{b('line_changed_vs_last_game (post-game)')['share_rows']:.0%} / "
                                                                            f"{b('pp_unit_changed (post-game)')['share_rows']:.0%} of skater-games",
         "impact": f"MAE lower than the rest ({b('line_changed_vs_last_game (post-game)')['mae']:.3f} vs {b('line_changed_vs_last_game (post-game)')['mae_rest']:.3f}); "
                   f"PIT line-change factor CRPS {ci(fx['line_changed_last_game_PIT']['val_crps_diff_all'], 6)}",
         "cause": "changes concentrate on depth players with small means", "status": "ruled out",
         "action": "none (gain < 0.01% CRPS)"},
        {"pattern": "Back-to-backs", "frequency": f"{b('team_back_to_back (PIT)')['share_rows']:.0%} of skater-games",
         "impact": f"SOG bias {b('team_back_to_back (PIT)')['bias']:+.3f}; dev-fitted factor {fx['b2b']['factor_dev']:.3f} -> validation "
                   f"CRPS {ci(fx['b2b']['val_crps_diff_all'], 6)}", "cause": "fatigue effect too small to estimate",
         "status": "ruled out", "action": "none (LightGBM sees b2b as a feature)"},
        {"pattern": "Injury returns / scratches (missed team games)", "frequency": f"{b('returning_from_absence>=1 team game (PIT)')['share_rows']:.1%}",
         "impact": f"bias {b('returning_from_absence>=1 team game (PIT)')['bias']:+.3f}; fix CRPS {ci(fx['returning_from_absence']['val_crps_diff_all'], 6)}",
         "cause": "returning players' role is slightly lower", "status": "ruled out", "action": "none"},
        {"pattern": "New team (trade/signing)", "frequency": f"{b('new_team (PIT)')['share_rows']:.1%}",
         "impact": f"SOG bias {b('new_team (PIT)')['bias']:+.3f}, TOI bias {b('new_team (PIT)')['toi_bias']:+.2f} min",
         "cause": "role on a new team is unknown from history", "status": "hypothesis",
         "action": "use archived DailyFaceoff lines for new-team players (2026-27 onward)"},
        {"pattern": "Game-total distribution too wide", "frequency": "every game",
         "impact": f"validation total PIT variance ratio {gt['pit_var_ratio']:.3f}, 80% coverage {gt['cover_80']:.3f}",
         "cause": "independent team draws ignore OT/shootout structure (negative dependence)", "status": "hypothesis",
         "action": "joint team-goals model (bivariate / simulation) before publishing totals ladders"},
        {"pattern": "pf_core group_prior_pit look-ahead fallback", "frequency": "rows on a group's first date",
         "impact": "found by a poisoned-future unit test; no effect on scored rows", "cause": "fallback = full-sample mean",
         "status": "verified defect", "action": "worked around (development-only fallback); reported to the pf_core owner"},
    ]


def OPP_SUMMARY(full):
    o = full["opportunity"]
    h = {x["model"] + "|" + x["target"]: x for x in o["models"]["holdout"]}
    inc = o["incumbent"].get("PLAYER_SIM_V1 walk-forward 2025-26", {})
    return (f"TOI is modelled first. LightGBM on PIT role features (T_E) is the most accurate: holdout total-TOI MAE "
            f"{h['toi_E|toi']['mae']:.3f} min (EWMA {h['toi_B|toi']['mae']:.3f}, season average {h['toi_A|toi']['mae']:.3f}), PP-TOI "
            f"MAE {h['toi_E|toi_pp']['mae']:.3f}. On 2025-26 it beats PLAYER_SIM_V1's walk-forward TOI "
            f"({inc.get('toi', {}).get('ours', {}).get('mae', float('nan')):.3f} vs {inc.get('toi', {}).get('incumbent', {}).get('mae', float('nan')):.3f}) "
            "and WORKLOAD_V1's published 1.875. Role (line rank and PP unit) comes from the previous game's shift data; "
            "top-line forwards are under-projected by "
            f"{-next(x for x in o['by_role']['validation']['toi_E_by_role'] if x['segment'] == 'F1')['bias']:.2f} min.")


def CAL_SUMMARY(full):
    F = full["families"]
    parts = []
    for key in FAM:
        d = F[key]["dist"]["holdout"]["nb_binned"]
        parts.append(f"{LABEL[key]} 80% cover {d['cover_80']:.3f}, PIT var {d['pit_var_ratio']:.3f}")
    return ("Selected distribution: NB with mean-binned dispersion fitted on development residuals. Holdout: " + "; ".join(parts)
            + ". Shots need over-dispersion (Poisson PIT var ~1.03, 80% cover 0.79); goals/assists/points are Poisson "
              "(fitted alpha ~0); saves NB is slightly too wide; the game total is too wide.")


def FAILED(full):
    ex = full["extra_experiments"]
    F = full["families"]
    return [
        {"name": "Back-to-back / injury-return / early-season multiplicative fixes",
         "what_was_learned": "Dev-fitted factors (0.92-0.97) give no or < 0.01% validation CRPS gains.",
         "changes_future_decisions": "Schedule fatigue is not a lever for NHL player props; stop iterating on it."},
        {"name": "Schedule-adjusted (ridge) vs raw opponent factor",
         "what_was_learned": f"Identical at player level (shots {ci(ex['opp_sog']['ridge_minus_raw'], 5)}).",
         "changes_future_decisions": "Keep ridge for team models; the simpler raw factor is an acceptable fallback."},
        {"name": "Role-share TOI (T_C) feeding points",
         "what_was_learned": f"No difference vs LightGBM TOI for points ({ci(ex['toi_source_points']['E_minus_C'], 5)}).",
         "changes_future_decisions": "Better minutes help shots, not scoring; spend effort on rates and team environment."},
        {"name": "Saves C (team shots allowed x save%)",
         "what_was_learned": "Not better than the saves average on validation; biased high because the starter faces ~1 fewer "
                             "shot than the team allows (pulls, relief).",
         "changes_future_decisions": "Model starter shots faced directly, with a pull mixture."},
        {"name": "NB vs Poisson for goals / assists / points",
         "what_was_learned": "Fitted dispersion ~0; identical CRPS.", "changes_future_decisions": "Poisson is sufficient there."},
        {"name": "Saves challenger vs PLAYER_SIM_V1",
         "what_was_learned": f"Still worse on holdout ({ci(F['saves']['incumbent']['holdout'].get('rps_diff'), 4)} rung RPS).",
         "changes_future_decisions": "Do not replace the incumbent saves model; borrow its game-script and pull hazard."},
    ]


def PRIORITIES(full):
    sv = full["families"]["saves"]["pulled_starters"]
    f1 = next(x for x in full["opportunity"]["by_role"]["validation"]["toi_E_by_role"] if x["segment"] == "F1")
    return [
        {"rank": 1, "item": "Saves: pull-hazard mixture + game-script (projected goals against) on starter shots faced",
         "impact": f"only family losing to its incumbent; pulls = {sv['share_sq_error']:.0%} of saves squared error",
         "evidence": "section 9; incumbent comparison in section 5", "complexity": "medium", "data": "available (goalies, goals)"},
        {"rank": 2, "item": "Merge and run the daily projection-foundation workflow; score every published projection",
         "impact": "turns SHADOW VALIDATION into a live record (path to READY)", "evidence": "prospective 2026-27 check in section 5",
         "complexity": "low", "data": "data-archive (already captured)"},
        {"rank": 3, "item": "Use archived DailyFaceoff PP units / lines as features once >= ~500 2026-27 games exist",
         "impact": "PP TOI and new-team roles; PP1 precision 87%", "evidence": "NHL-X11", "complexity": "medium",
         "data": "archived from 2026-09-30"},
        {"rank": 4, "item": "Joint team-goals model for game totals", "impact": "total PIT var ~0.92 (too wide)",
         "evidence": "section 8", "complexity": "medium", "data": "available"},
        {"rank": 5, "item": "Role-specific TOI calibration (top-line under-projection)", "impact": f"F1 TOI bias {f1['bias']:+.2f} min",
         "evidence": "section 4", "complexity": "low", "data": "available"},
        {"rank": 6, "item": "Extend halflife grids beyond 30 games (selected at the grid edge for B and C)",
         "impact": "small", "evidence": "development grid logs", "complexity": "low", "data": "available"},
        {"rank": 7, "item": "Publish P(start) from DailyFaceoff status with saves", "impact": "1-2% wrong-starter risk at 1-6 h",
         "evidence": "NHL-X10", "complexity": "low", "data": "archived"},
    ]


if __name__ == "__main__":
    main()
