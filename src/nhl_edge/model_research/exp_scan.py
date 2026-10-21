"""M-SCAN-1: systematic-error scan of V1 on the walk-forward games (EXPLORATORY; registered with disclosure, see PREREGS)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from nhl_edge.model_research import registry
from nhl_edge.model_research.wf_data import load_wf
from nhl_edge.model_research.wf_scan import scan

PREREG = {
    "hypothesis": "V1 residuals (regulation goals - V1 expected goals) are systematically related to information V1 already holds: early-season games, back-to-backs, rest, finishing "
                  "talent, offensive/defensive xG levels, lam_sum, lam_diff, season.",
    "motivation": "Operator questions: are we overvaluing recent scoring trends / finishing, mishandling rest and early-season uncertainty, miscalibrated?",
    "method": "17 pre-listed (feature, target) OLS tests with HC1 SE on 2,624 WF games, standardised features, Benjamini-Hochberg q=0.10 over all 17 (wf_scan.features).",
    "baseline": "zero residual (V1 unbiased)",
    "decision_rule": "A feature is a CANDIDATE class-A pattern if BH-adjusted p < 0.10. A candidate is not an improvement until a rolling challenger beats V1 (see M-CAL-1).",
    "protocol": {"data": "walk_forward_36570274279_games.csv, 2,624 games; no train/test split (diagnostic)", "independent_unit": "game"},
    "tier": "EXPLORATORY",
    "disclosure": "Registered AFTER the first execution of the scan (the 17-feature list was written before executing and was not edited afterwards). The result is therefore descriptive.",
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = scan(load_wf(a.repo))
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "wf_scan.json").write_text(json.dumps(r.to_dict("records"), indent=1))
    reg = a.repo / "docs/research/nhl-model-improvement/experiment_registry.jsonl"
    ents = registry.read(reg)
    if not any(e["id"] == "M-SCAN-1" for e in ents):
        registry.append(reg, "PREREG", "M-SCAN-1", PREREG, a.repo)
    if not any(e["id"] == "M-SCAN-1" and e["type"] == "RESULT" for e in registry.read(reg)):
        sig = r[r["bh_sig_q10"]]
        registry.append(reg, "RESULT", "M-SCAN-1", {
            "metrics": {"n_tests": int(len(r)), "significant_bh_q10": sig[["test", "coef_per_sd", "se", "t", "p", "p_bh"]].to_dict("records"),
                        "null_findings": r[~r["bh_sig_q10"]]["test"].tolist()},
            "decision": "CANDIDATE_PATTERNS_NOT_IMPROVEMENT",
            "interpretation": "Three candidate class-A patterns: total residual falls with lam_sum (total rates over-dispersed across games), falls with the sum of finishing factors (finishing "
                              "persistence over-weighted for totals) and margin residual rises with lam_diff (matchup differences under-weighted). Early-season, back-to-back, rest and "
                              "home/away-season effects show NO evidence. Magnitudes are ~0.15-0.2 goals per SD of the feature against a per-game SD of 2.3, so the effects are immaterial for "
                              "pricing (see M-CAL-1: correcting them does not improve scores).",
            "reproduction": "python -m nhl_edge.model_research.exp_scan --repo . --out docs/research/nhl-model-improvement/data",
            "results_file": "docs/research/nhl-model-improvement/data/wf_scan.json"}, a.repo)
    print(r.round(4).to_string())


if __name__ == "__main__":
    main()
