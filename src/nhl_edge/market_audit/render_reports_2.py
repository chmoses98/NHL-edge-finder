"""Second half of the report renderer (see render_reports.py)."""

from __future__ import annotations

from typing import Any

from nhl_edge.market_audit.render_reports import J, R, ci, f, pc, pct, table


def taxonomy(r: R) -> None:
    rec, hv = J(r.d, "outcome_reconciliation.json"), J(r.d, "history_validation.json")
    tax = rec["taxonomy"]
    rows = [{**t, "n": f"{t['n']:,}"} for t in tax]
    oc = rec["outcomes_by_family"]
    orows = [{"family": k, **{o: f"{v.get(o, 0):,}" for o in ("YES", "NO", "VOID_FAIR_PRICE", "PLAYER_NOT_IN_BOXSCORE", "PLAYER_UNMATCHED", "RULE_SILENT", "NOT_FINAL", "DATA_INCONSISTENT")}} for k, v in sorted(oc.items())]
    r.write("MARKET_TAXONOMY.md", f"""# Market taxonomy

{r.banner}

Every game-scoped contract is converted into an explicit `ContractSpec` (`market_audit/taxonomy.py`). Authority order: Kalshi's `series_ticker` -> structured `strike_type` / `floor_strike` /
`custom_strike` -> the contract's own rules text, parsed to CROSS-CHECK the structured fields (threshold, clubs, date, period wording, overtime / shootout / void wording). A disagreement
downgrades the spec to UNRESOLVED; the ticker is used only for game scope. Result: **every game-scoped contract is PROVEN** (structured strike and rules wording agree).

| family | what YES means | overtime | shootout | void rule |
|---|---|---|---|---|
| game_winner (KXNHLGAME) | club wins the official final | counts | decides the game | postponed >48 h / cancelled: fair price |
| game_spread (KXNHLSPREAD) | club wins by MORE than x goals (x = 1.5, 2.5, ...) | counts | a shootout win is a one-goal margin, so never > 1.5 | as above |
| game_total (KXNHLTOTAL) | both clubs score MORE than x | counts | winner is credited ONE goal | as above |
| team_total (KXNHLTEAMTOTAL) | club scores MORE than x | counts | winner is credited ONE goal | as above |
| game_overtime (KXNHLOT) | an overtime period is played (opening faceoff taken) | is the event | n/a | as above |
| game_early_goal (KXNHLF10G) | a goal in the first period before 10:00 elapsed (10:00 itself excluded) | n/a | n/a | as above |
| period_winner / spread / total (KXNHL{{1,2,3}}P*) | club wins / wins by > x / both score > x in that period; `-TIE` leg = equal goals | never counts (P3 states it) | never counts | as above |
| player_goals / assists / points (KXNHLGOAL/AST/PTS) | official N+ stat line | counts | never counts | fair price only if the player is "active but never enters"; a scratch is NOT addressed |
| goalie_saves (KXNHLSAVE) | goalie records N+ saves | counts | n/a | same |
| first_goal (KXNHLFIRSTGOAL) | player scores the game's first goal | counts | n/a | rule silent if no goal before a shootout |

Goal-scorer families (`player_goals`, `first_goal`) are included in the research dataset and **never recommended**.

### Spec counts

{table(rows, [('series', 'series'), ('family', 'family'), ('kind', 'kind'), ('period', 'period'), ('semantics', 'semantics_status'), ('contracts', 'n')])}
Out of scope by design: season champion / awards / player-season stats (a different instrument class), and parlay/combo series (none appear on the archived boards).
""")
    r.write("OUTCOME_MAPPING_REPORT.md", f"""# Outcome-mapping report

{r.banner}

`market_audit/outcomes.py` is a pure function (`resolve(spec, facts)`), written independently of `nhl_edge.settlement`. It returns YES / NO, or an explicit non-decision:
`VOID_FAIR_PRICE`, `NOT_FINAL`, `DATA_INCONSISTENT`, `PLAYER_UNMATCHED`, `PLAYER_NOT_IN_BOXSCORE`, `RULE_SILENT`, `UNRESOLVED_SPEC`. It never guesses.

## Three independent checks

1. **Three-source reconciliation per game** (official final = play-by-play goals = boxscore lines, goalie scorers included): {rec['games_final'] - len(rec['games_with_reconciliation_problems'])}/{rec['games_final']} games clean.
2. **Against production settlement**: {rec['vs_production_settlement']['co_decided']:,} contracts decided by both, **{rec['vs_production_settlement']['disagreements']} disagreements**.
3. **Against Kalshi's own settlement (2025-26 history)**: {hv['markets_checked']:,} finalized winner / spread / total markets, **{hv['disagreements']} disagreements**, split by how the game ended:

{table(hv['by_series_and_ending'], [('series', 'series'), ('game ended', 'period_type'), ('markets', 'n'), ('agree', 'agree'), ('rate', 'rate')])}
The shootout rows (the discriminating cases for the "shootout = one goal" rule on totals and spreads) agree 100%. The {hv['kalshi_scalar_results']} `scalar` (fair-price) results are one postponed game; the resolver
correctly refuses to settle them ({hv['unjoined']} markets did not join to a final).

## Outcomes by family (live archive, all captured games)

{table(orows, [('family', 'family'), ('YES', 'YES'), ('NO', 'NO'), ('void', 'VOID_FAIR_PRICE'), ('not on boxscore', 'PLAYER_NOT_IN_BOXSCORE'), ('rule silent', 'RULE_SILENT'), ('not final', 'NOT_FINAL')])}
`NOT_FINAL` rows are games not yet played at the snapshot. Player contracts for a player on neither club's boxscore are held out (the text does not say a scratch voids) and never scored.

Regression tests: `tests/test_market_audit_outcomes.py` (16 cases: shootout totals/spreads, overtime, P3 excludes OT, the 10:00 boundary, name matching, goalie scorer, scratch vs zero-TOI, first-goal rule gap, not-final).
""")


def _bands(rows: list[dict[str, Any]]) -> str:
    return table([{**x, "mid": f(x["mean_mid"], 3), "freq": f(x["freq"], 3), "gap": pct(x["gap"]), "gap95": ci(x["gap_lo95"], x["gap_hi95"]), "ry": pct(x["roi_buy_yes"]), "rn": pct(x["roi_buy_no"])} for x in rows],
                 [("implied band", "band"), ("contracts", "n"), ("games", "games"), ("mean implied", "mid"), ("frequency", "freq"), ("gap (freq - implied)", "gap"), ("gap 95% CI", "gap95"), ("net ROI buy YES", "ry"), ("net ROI buy NO", "rn")])


def efficiency(r: R) -> None:
    e, pw = J(r.d, "market_efficiency.json"), J(r.d, "power_analysis.json")
    H, L = e["HIST_2025_26"], e["LIVE_2026_27"]

    def hz(rep: dict[str, Any]) -> str:
        rows = [{"kind": x["kind"], "h": x["horizon_min"], "games": x["games"], "n": x["n"], "brier": f(x["brier"]), "b": f(x["calib_slope"], 2), "se": f(x["calib_slope_se"], 2), "gap": pct(x["gap_yes_minus_mid"]),
                 "ry": f"{pct(x['roi_buy_yes'])} {ci(x['roi_yes_lo95'], x['roi_yes_hi95'])}", "rn": f"{pct(x['roi_buy_no'])} {ci(x['roi_no_lo95'], x['roi_no_hi95'])}", "sp": f(x["mean_spread"], 3)}
                for x in rep["by_kind_horizon"] if x["horizon_min"] in (1440, 60, 0)]
        return table(rows, [("market", "kind"), ("min to start", "h"), ("games", "games"), ("contracts", "n"), ("Brier", "brier"), ("calib. slope b", "b"), ("se(b)", "se"), ("gap", "gap"),
                            ("net ROI buy YES (95% CI)", "ry"), ("net ROI buy NO (95% CI)", "rn"), ("mean spread", "sp")])

    lines = table([{**x, "mid": f(x["mean_over_mid"], 3), "fr": f(x["over_freq"], 3), "gap": pct(x["gap"]), "g": ci(x["gap_lo95"], x["gap_hi95"]), "ro": pct(x["roi_over"]), "ru": pct(x["roi_under"])} for x in H["totals_by_line_T60"]],
                  [("line", "line"), ("games", "games"), ("implied P(Over)", "mid"), ("Over frequency", "fr"), ("gap", "gap"), ("95% CI", "g"), ("net ROI Over", "ro"), ("net ROI Under", "ru")])
    months = table([{**x, "gap": pct(x["gap"]), "ru": pct(x["roi_under"])} for x in H.get("totals_gap_by_month_T60", [])], [("month", "month"), ("games", "games"), ("Over gap", "gap"), ("net ROI Under", "ru")])
    sp = table([{**x, "m": f(x["mean_mid"], 3), "fr": f(x["freq"], 3), "g": pct(x["gap"]), "ry": pct(x["roi_buy_yes"]), "rn": pct(x["roi_buy_no"])} for x in H["spread_by_line_T60"]],
               [("line", "line"), ("games", "games"), ("implied", "m"), ("frequency", "fr"), ("gap", "g"), ("net ROI buy YES", "ry"), ("net ROI buy NO", "rn")])
    wh = table([{**x, "m": f(x["mean_mid"], 3), "fr": f(x["freq"], 3), "g": pct(x["gap"])} for x in H.get("winner_home_fav_T60", [])], [("home", "home"), ("favourite", "favourite"), ("contracts", "n"), ("implied", "m"), ("win frequency", "fr"), ("gap", "g")])
    mv = table([{**x, "g": pct(x["mean_residual_y_minus_mid"])} for x in H.get("move_24h_to_60m_vs_residual", [])], [("mid move T-24h to T-60m", "move_bin"), ("contracts", "n"), ("games", "games"), ("mean (outcome - mid)", "g")])
    pwr = table([{"id": k, **{"bets/game": f(v["bets_per_game"], 1), "sd": f(v["sd_of_per_game_roi"], 2)}, **{f"games for {e_}": f"{n:,}" for e_, n in v["games_needed"].items()}} for k, v in pw.items()],
                [("strategy", "id"), ("bets/game", "bets/game"), ("sd of per-game ROI", "sd")] + [(f"games to detect {e_}", f"games for {e_}") for e_ in next(iter(pw.values()))["games_needed"]])
    hf = next((x for x in H.get("winner_home_fav_T60", []) if x["home"] and x["favourite"]), None)
    hf_txt = ""
    if hf:
        se = (hf["freq"] * (1 - hf["freq"]) / hf["n"]) ** 0.5
        hf_txt = (f"The largest moneyline deviation is home favourites winning {abs(hf['gap']) * 100:.1f} points {'less' if hf['gap'] < 0 else 'more'} often than priced "
                  f"({hf['n']} contracts; about {abs(hf['gap']) / se:.1f} standard errors). The away-underdog row covers the same games, so it is one observation counted twice, not two.")
    gn = {k: v["games_needed"]["3%"] for k, v in pw.items()}
    best_gap = max((x for x in H["bands_pooled_full_game_T60"] if x["n"] > 100), key=lambda x: abs(x["gap"]))
    r.write("MARKET_EFFICIENCY_STUDY.md", f"""# Market-efficiency study (Phase C)

{r.banner}

Two separate tiers, never pooled: **HIST** = 2025-26 regular season, Kalshi candle-close bid/ask (no depth), {H['games']:,} games; **LIVE** = the 2026-27 archive, bid/ask board, {L['games']} games.
"Gap" = realised frequency minus implied probability (the pre-friction efficiency diagnostic). "Net ROI" buys the displayed ask with the quadratic taker fee (verified to the cent on routed fills).
Every interval resamples whole games. Repeated snapshots, both legs of a market and several lines of one game are never treated as independent.

## 1. Calibration and returns by market (HIST, regular season, 95% CIs)

{hz(H)}
Reading it: a calibration slope b = 1 and intercept 0 mean the mid is a calibrated probability. Buying either side of the moneyline costs about the
spread plus the fee ({pct(next(x for x in H['by_kind_horizon'] if x['kind'] == 'winner' and x['horizon_min'] == 60)['roi_buy_yes'])} / {pct(next(x for x in H['by_kind_horizon'] if x['kind'] == 'winner' and x['horizon_min'] == 60)['roi_buy_no'])} at T-60m): no mispricing is visible there.
Brier improves as puck drop approaches (price discovery): the T-24h mid is a noisier quote because the spread is wider, not because the market is "wrong". Moneyline slopes are about 1.5 standard errors below 1 in HIST and above 1 in LIVE, i.e. no stable direction.

### LIVE tier (151 games), same table

{hz(L)}
## 2. Price bands, all full-game markets pooled (HIST, T-60m)

{_bands(H['bands_pooled_full_game_T60'])}
The largest pooled-band gap is {pct(best_gap['gap'])} in band {best_gap['band']} ({best_gap['n']:,} contracts, CI {ci(best_gap['gap_lo95'], best_gap['gap_hi95'])}). A favourite-longshot pattern would show NEGATIVE gaps at low implied
probability and POSITIVE gaps at high; the low bands are within noise, and the high-probability bands are mildly positive (high-probability YES contracts, mostly low-line Overs, hit slightly more often than
priced). Gaps of one to three points are smaller than the round-trip cost on any contract, so they cannot be monetised.

### Totals by line

{lines}
### Totals gap by month (HIST) -- descriptive, post hoc

{months}
October 2025 shows a large Over gap. This was noticed AFTER looking at the full season, so it is a hypothesis (registered as M6) and the HIST tier cannot validate it; the 2026 October archive tested it once (see CANDIDATE_SIGNAL_REGISTRY.md).

### Puck line (alternate spreads) by line

{sp}
### Moneyline: home / favourite (HIST, T-60m)

{wh}
### Does a late price move predict the outcome? (HIST, T-24h to T-60m)

{mv}
## 3. Friction dominates

Typical full-game spread is 1 to 4 cents and the taker fee is `0.07 p (1-p)` per contract (1.75c at 50c). Sensitivity of the registered one-sided strategies to fees, slippage and decision time is in STRATEGY_ROBUSTNESS.md:
before the fee, the best live strategy is about break-even; after it, essentially every strategy is negative.

## 4. How much evidence would an edge need?

Independent GAMES needed to detect a true net ROI of the stated size (one-sided alpha 0.05, 80% power), from the empirical per-game dispersion of returns:

{pwr}
A season has about 1,312 games. Detecting a true +3% net ROI needs about {min(gn.values()):,} games for the lowest-variance (high-priced) strategies and about {max(gn.values()):,} for even-money bets - from most of a season to several seasons of one league, and only if the edge persists. Small edges are not discoverable from one season of Kalshi NHL data.

## Conclusion

* Moneylines: efficiently priced (HIST and LIVE); no statistically significant directional, favourite/underdog or home bias. {hf_txt}
* Full-game totals and puck lines: calibrated within about two to three points; the visible gaps are smaller than friction.
* Period, team-total, overtime, first-10-minutes and prop markets: only the LIVE tier exists (151 games); it can falsify large inefficiencies but not detect small ones.
* "Price discovery" (the mid improving toward puck drop) is not "forecastability": nothing here shows the pregame price is beatable before costs, let alone after.
""")


def matchup(r: R) -> None:
    m = J(r.d, "matchup_study.json")
    rows = [{"block": k, "feat": ", ".join(v["features"]), "dg": v["n_disc_games"], "hg": v["n_hold_games"], "z": ", ".join(f"{a}:{b:.2f}" for a, b in v["beta_z"].items()), "p": f(v["wald_p_block"], 3),
             "dll": f(v["oos_delta_logloss_vs_market"], 5), "ci": f"[{v['oos_dll_lo95']:.5f}, {v['oos_dll_hi95']:.5f}]"} for k, v in m.items()]
    r.write("MATCHUP_FACTOR_STUDY.md", f"""# Matchup-factor study (Phase D)

{r.banner}

**Question.** Do timestamp-safe, opponent-adjusted hockey factors add information beyond the Kalshi price?

**Method (`market_audit/matchup_study.py`, declared in git before any result was computed).** Independent challenger features from games dated strictly before the game: ridge opponent-adjusted
5v5 xG-rate differential and expected total (refit daily, 45-day half-life, MoneyPuck team-games), finishing, power-play/penalty-kill edge, rest, back-to-backs, timezone hours crossed.
Test: `y ~ offset(logit(mid at T-60m)) + beta * x`, FIT on the chronologically first 60% of games, SCORED once on the last 40% (never refit). Starting-goalie identity is deliberately excluded: the archive
cannot say when the starter became known, so any goalie feature risks leaking.

{table(rows, [('block', 'block'), ('features', 'feat'), ('fit games', 'dg'), ('hold-out games', 'hg'), ('in-sample z', 'z'), ('block Wald p', 'p'), ('hold-out change in log loss vs market', 'dll'), ('95% CI (games)', 'ci')])}
Negative change in log loss = the feature block improved on the market alone. **No block helps out of sample; every confidence interval includes zero**, and the rest/travel block, which shows an
in-sample coefficient near |z|=2, makes the hold-out slightly worse (the signature of overfitting a 780-game fit window). The market already prices opponent-adjusted shot quality, rest and travel to within this test's
resolution. This is consistent with the model audit: the production model is built from the same inputs and adds nothing either.

Limits: one season of market prices; features are public and standard; a stronger or non-public input (confirmed lineups, injuries timed against the repricing instant, goalie confirmation timing) is **untestable**
here because the archive does not timestamp when that information reached the market.
""")


def models(r: R) -> None:
    m = J(r.d, "model_audit.json")
    rows = []
    for k, v in m.items():
        if not v.get("n_games"):
            continue
        inc = v["incremental"]
        rows.append({"k": k.replace("|", " "), "g": v["n_games"], "n": f"{v['n_contracts']:,}", "bm": f(v["brier_model"]), "bk": f(v["brier_market"]), "d": f"{v['d_brier_model_minus_market']:+.4f}",
                     "ci": f"[{v['d_brier_lo95']:+.4f}, {v['d_brier_hi95']:+.4f}]", "an": f"{v['d_brier_anchored_minus_market']:+.4f}", "c": f(inc["c"], 2), "z": f(inc["z"], 2), "dis": f(v["mean_abs_disagreement"], 3),
                     "sig": "WORSE" if v["d_brier_lo95"] > 0 else ("better" if v["d_brier_hi95"] < 0 else "")})
    worse = sum(1 for x in rows if x["sig"] == "WORSE")
    better = sum(1 for x in rows if x["sig"] == "better")
    valid = [v for v in m.values() if v.get("n_games")]
    n_pos = sum(1 for v in valid if v["d_brier_model_minus_market"] > 0)
    max_anch = max(abs(v["d_brier_anchored_minus_market"]) for v in valid)
    lo_w = min(v["d_brier_lo95"] for v in valid if v["d_brier_lo95"] > 0)
    hi_w = max(v["d_brier_model_minus_market"] for v in valid)
    r.write("PREDICTION_ENGINE_COMPARISON.md", f"""# Prediction-engine comparison (Phase E)

{r.banner}

Same games, same instant (T-60 min), same outcomes for every forecaster. Model = last production prediction at or before the cut (asserted in code); HIST models = the walk-forward V1 / V2 (SIM2_ST) predictions
for the 2025-26 season; LIVE models = production V1 / V2 / PLAYER_SIM_V1 rows. "Market" = the mid at the same instant. Intervals resample games.

* `dBrier` = Brier(model) - Brier(market): **positive = the model is worse**.
* `c` = coefficient in `y ~ offset(logit(mid)) + c * (logit(p_model) - logit(mid))`: 0 means the model adds nothing beyond the market; 1 means its disagreements are fully right.
* "anchored" = the production 0.8-weight logit blend of model and market (labelled "not independent evidence"): it can only track the market.

{table(rows, [('forecaster / market', 'k'), ('games', 'g'), ('contracts', 'n'), ('Brier model', 'bm'), ('Brier market', 'bk'), ('dBrier', 'd'), ('95% CI', 'ci'), ('verdict', 'sig'), ('dBrier anchored', 'an'), ('c', 'c'), ('z(c)', 'z'), ('mean |model - market|', 'dis')])}
## Findings

* Across {len(rows)} family/tier comparisons the model is **significantly worse than the market in {worse}** and significantly better in **{better}**; no family has an incremental-information coefficient significantly above zero.
* Caveat: the {worse} "WORSE" verdicts are uncorrected 95% intervals over {len(rows)} overlapping comparisons (e.g. "V1 all" contains V1 winner, total and spread; the three player families are correlated), and their lower bounds are barely above zero (smallest lower bound {lo_w:+.4f}).
  Read them as "consistently not better, and possibly slightly worse", with effect sizes of at most {hi_w:.4f} Brier points - not as {worse} independent discoveries.
* The anchored blend differs from the market by at most {max_anch:.4f} Brier in any comparison: it is the market with a little model noise, not an independent forecast.
* The model's point estimate is worse than the market in {n_pos} of {len(valid)} comparisons: where model and market disagree (typically 2-5 points) the market is, on average, the more accurate.
* V1 and V2 disagree with each other in sign on a meaningful share of contracts (two of the four Oct-20 wagers), and neither beats the market, so their disagreement is better read as model uncertainty than as edge.
* PLAYER_SIM_V1 (assists / points / goals) is significantly worse than the market on the LIVE tier; goalie saves is not distinguishable.

**Statement required by the brief:** the existing projection engines are consistently no better than a market-based baseline, and in several families slightly but measurably worse (tiny effects; see the caveat above). They provide no demonstrated incremental predictive
value. No challenger improvement was manufactured; the one challenger tested (matchup factors) also failed.

Distribution-level metrics (CRPS, tail behaviour) were **not** computed: the archive stores probabilities for fixed thresholds, not full predictive distributions, so CRPS would require re-simulating from stored seeds - listed in the roadmap.
""")


def signals(r: R) -> None:
    res = J(r.d, "hypothesis_results.json")
    meta, rr = res["meta"], res["results"]
    rows = []
    for hid, v in rr.items():
        for t, x in v["tiers"].items():
            rows.append({"id": hid, "title": v["title"], "tier": t, "games": x.get("n_games"), "n": x.get("n_contracts"),
                         "roi": pct(x.get("roi")) if x.get("roi") is not None else "n/a", "ci": ci(x.get("roi_lo95"), x.get("roi_hi95")) if x.get("roi") is not None else "",
                         "gap": pct(x.get("gap")) if x.get("roi") is not None else "", "slip": pct(x.get("roi_slip_1c")) if x.get("roi") is not None else "",
                         "q": f(v["q_live_bh"], 3) if t == "LIVE" and v.get("q_live_bh") is not None else "", "cls": v["class"] if t == (list(v["tiers"])[-1]) else ""})
    counts: dict[str, int] = {}
    for v in rr.values():
        counts[v["class"]] = counts.get(v["class"], 0) + 1
    class_lists = "; ".join(f"{c}: {', '.join(k for k, v in rr.items() if v['class'] == c)}" for c in sorted(counts))
    live_se = [(v["tiers"]["LIVE"]["roi_hi95"] - v["tiers"]["LIVE"]["roi_lo95"]) / (2 * 1.96) * 100 for v in rr.values() if v["tiers"].get("LIVE", {}).get("roi") is not None]
    se_lo, se_hi = min(live_se), max(live_se)
    m1 = rr["M1"]["tiers"]
    m1_txt = ", ".join(f"{t} {pct(x['roi'])}" for t, x in m1.items())
    r.write("CANDIDATE_SIGNAL_REGISTRY.md", f"""# Candidate-signal registry (Phase F)

{r.banner}

The registry (`market_audit/hypotheses.py`, version `{meta['registry_version']}`) was committed BEFORE the live-tier tests were run (git `627b5fa7`, 2026-10-21T17:13:05Z). One decision horizon (T-60 min), selectors, sides, statistic,
the multiple-comparison correction and the evidence classes were fixed in advance. Each registered test was run **once** on the LIVE tier; the LIVE tier is now closed (games that start after the freeze belong to a separate
PROSPECTIVE tier read only at predeclared looks of 150 / 300 / 450 games).

Tiers: HIST_DISC = first 60% of 2025-26 regular-season games ({meta['tier_games']['HIST_DISC']} games), HIST_HOLD = last 40% ({meta['tier_games']['HIST_HOLD']}), LIVE = 2026-09-29..10-20 ({meta['tier_games']['LIVE']}). Statistic: net ROI
buying the selected side at the displayed ask with the taker fee; game-clustered bootstrap (4,000 resamples). `q` = Benjamini-Hochberg adjusted one-sided p over the LIVE family.

**Disclosure.** Before registration the full 2025-26 season was inspected descriptively (calibration by band, by line, by month). HIST tiers are therefore not clean for hypotheses that look suggested (M6). Only LIVE can validate.

## Result classes

{', '.join(f'{k}: {v}' for k, v in sorted(counts.items()))}. **VALIDATED: {counts.get('VALIDATED', 0)}.** The smallest LIVE q-value is {min((v['q_live_bh'] for v in rr.values() if v.get('q_live_bh') is not None), default=float('nan')):.3f}.

## Every registered test, every tier (including failures)

{table(rows, [('id', 'id'), ('hypothesis', 'title'), ('tier', 'tier'), ('games', 'games'), ('contracts', 'n'), ('net ROI', 'roi'), ('95% CI', 'ci'), ('gap', 'gap'), ('ROI at +1c slippage', 'slip'), ('q (LIVE)', 'q'), ('class', 'cls')])}
## Reading the classes honestly

* Classes are mechanical. **M14 is labelled PROMISING only because its ROI is +0.1% on its single testable tier** (95% CI roughly +/-18%, p about 0.5, negative after 1c slippage). The preregistered rule ("net ROI > 0 on every
  testable tier") is too lenient for single-tier hypotheses; this is reported as a defect of the rule, not quietly redefined. Registry v1.1 should require the lower 90% bound to be positive for PROMISING.
* **M6 (early-season Overs)** was suggested by October 2025 (positive on 39 games) and was NOT confirmed on the 2026 archive. A post-hoc pattern failing its first real out-of-sample test is the expected outcome of selection.
* **M1 (Unders)** has negative net ROI in all three tiers ({m1_txt}); it is REJECTED because the HIST_DISC upper bound is below zero.
* Classes: {class_lists}.
* Model-disagreement strategies (C1, C2) have negative net ROI on the hold-out and LIVE tiers.
* **Nothing is VALIDATED.** On the 151 LIVE games the standard error of a strategy's net ROI ranges from {se_lo:.1f} points (high-priced contracts, low variance) to {se_hi:.1f} points (small samples or even-money bets); a validated claim needs a positive lower 90% bound AND a BH q at most 0.10 AND a positive HIST_HOLD ROI, and no strategy came close.
  (All LIVE q-values are 0.976 or close because most one-sided p-values are near 1.)

Hypotheses that cannot be tested with this archive (UNTESTABLE, no data): goalie-confirmation repricing (no timestamp of when the starter became public), opponent-adjusted offensive mismatches at the player level, line-combination changes, injury news
repricing, multi-expression agreement. They are listed in the roadmap with the data each would need.
""")


def walkforward(r: R) -> None:
    th, sh = J(r.d, "thesis_replay.json"), J(r.d, "shadow_summary.json")

    def srow(k: str) -> dict[str, Any]:
        v = th[k]
        return {"sel": k.replace("|", " / "), "n": v.get("n_bets"), "g": v.get("n_games"), "px": f(v.get("mean_price"), 3), "hit": pc(v.get("hit_rate")), "roi": pct(v.get("roi_net")), "ci": ci(v.get("roi_lo95"), v.get("roi_hi95")),
                "sw": pct(v.get("stake_weighted_roi")), "cl": pct(v.get("mean_ev_adjusted_claimed"))}

    keys = [k for k in th if "|" in k and isinstance(th[k], dict) and "label" in th[k]]
    mc = th["matched_control_S2"], th["matched_control_S2_ex_goalscorer"], th["matched_control_S1"]
    qt = table([{**x, "c": pct(x["claimed_ev"]), "r": pct(x["realized_roi"]), "ci": ci(x["lo95"], x["hi95"])} for x in th["ev_quintiles_all_candidates"]],
               [("claimed adjusted-EV bin", "ev_adjusted_bin"), ("bets", "n"), ("games", "games"), ("claimed EV / contract", "c"), ("realised ROI", "r"), ("95% CI", "ci")])
    s = sh
    r.write("WALK_FORWARD_VALIDATION.md", f"""# Walk-forward validation and historical replay (Phase H)

{r.banner}

Everything here uses information available at the decision instant: prices from the board tick whose capture had COMPLETED (stamp + lag), model outputs stamped at or before the cut, chronological tiers, no refitting on
the evaluation window, fees and displayed-ask execution. Selection groups are reported separately and never summed with routed wagers.

## A. Pre-registered market-only strategies

See CANDIDATE_SIGNAL_REGISTRY.md (HIST_DISC -> HIST_HOLD -> LIVE, one look each). No-bet baseline = 0.

## B. The existing thesis workflow, replayed

Each LOGICAL bet (game | ticker | side) is scored once, at the FIRST snapshot where it met the rule, at the executable price recorded in that snapshot, with OUR independent outcome. (The archive holds 22,929 decision rows
for 2,839 logical bets; repeated snapshots are not observations.) Research selections only: stakes in the archive are research suggestions, not wagers.

{table([srow(k) for k in keys], [('selection rule / scope', 'sel'), ('bets', 'n'), ('games', 'g'), ('mean price', 'px'), ('hit rate', 'hit'), ('net ROI per $ (per contract)', 'roi'), ('95% CI (games)', 'ci'), ('research-stake-weighted ROI', 'sw'), ('claimed EV / contract', 'cl')])}
### Does the selection layer pick better contracts than comparable ones it passed over?

Matched control: for each selected bet, a non-selected candidate from the same game, same family, same side, price within 5c (2,000 draws).

{table([{'test': n, 'matched': m.get('n_matched'), 'sel': pct(m.get('selected_roi')), 'ctl': pct(m.get('control_roi_mean')), 'ctlci': ci(m.get('control_roi_lo95'), m.get('control_roi_hi95')), 'p': f(m.get('p_control_at_least_as_good'), 3)}
         for n, m in zip(('first chosen, all families', 'first chosen, ex goal-scorer', 'first FUNDED, all families'), mc, strict=True)],
        [('selection', 'test'), ('matched bets', 'matched'), ('selected ROI', 'sel'), ('control ROI (mean)', 'ctl'), ('control 95%', 'ctlci'), ('p(random comparable pick does at least as well)', 'p')])}
Reading the last column: a value near 1 means a randomly chosen comparable candidate almost always did at least as well as the selection. The selected bets do not beat comparable candidates the workflow passed over, and in the ex-goal-scorer and funded cases they do
worse. The test is conditional on the same games (so game-level luck cancels) but the matched samples are small (100-434 bets). There is no evidence that the selection layer adds skill beyond the price.

### Does claimed EV predict realised ROI? (every distinct candidate, first snapshot)

{qt}
Claimed EV is about +1% to +2.5% per contract in every bin; realised ROI is negative and NOT monotone in the claim (the highest-claim bin is among the worst). Claimed edge is not informative.

## C. Shadow expression engine over the same games (T-60 min, one decision per game)

| policy | bets | games with a bet | net ROI | 95% CI | claimed EV / contract |
|---|---:|---:|---:|---|---:|
| strict (evidence-gated; the proposed default) | {s['strict']['n_bets']} | {s['strict']['games_with_bet']} | - | - | - |
| research_unvalidated (gate waived, w=0.5, uncertainty kept) | {s['research_unvalidated']['n_bets']} | {s['research_unvalidated']['games_with_bet']} | - | - | - |
| naive_ev (gate waived, full model trust, uncertainty ignored) | {s['naive_ev'].get('n_bets')} | {s['naive_ev'].get('games_with_bet')} | {pct(s['naive_ev'].get('roi_net'))} | {ci(s['naive_ev'].get('roi_lo95'), s['naive_ev'].get('roi_hi95'))} | {pct(s['naive_ev'].get('claimed_ev_per_contract'))} |

The strict engine PASSes every game. Ignoring the evidence produces a bet in nearly every game, with a claimed edge of about {pct(s['naive_ev'].get('claimed_ev_per_contract'), 1)} per contract and a realised net ROI of {pct(s['naive_ev'].get('roi_net'))}:
that gap is what an unvalidated model costs.

## D. Controls and what is missing

* Market-only decisions: section A. Current production model: section B plus PREDICTION_ENGINE_COMPARISON.md. Random / matched-market controls: section B. No-bet baseline: 0 by definition.
* Closing-line value is observable only as the move from decision to the last pregame quote; production `evaluations` carry it, and it is not used as an input anywhere (rule 9).
* Walk-forward for HIST uses fixed chronological splits (discovery -> hold-out); the walk-forward model predictions were produced by the repository's own expanding-window procedure.
* Prospective tier: accumulating from 2026-10-21T17:13:05Z; first look at 150 independent games.
""")


def robustness(r: R) -> None:
    sens, ex, pw = J(r.d, "sensitivity.json"), J(r.d, "execution_walk.json"), J(r.d, "power_analysis.json")
    out = ""
    for key, rows in sens.items():
        piv: dict[tuple, dict] = {}
        for x in rows:
            if x["fee_mult"] == 1.0:
                piv.setdefault((x["horizon_min"],), {})[x["slip"]] = x["roi"]
        pre = {x["horizon_min"]: x["roi"] for x in rows if x["fee_mult"] == 0.0 and x["slip"] == 0.0}
        t = table([{"h": h[0], "pre": pct(pre.get(h[0])), "s0": pct(v.get(0.0)), "s1": pct(v.get(0.01)), "s2": pct(v.get(0.02))} for h, v in sorted(piv.items(), reverse=True)],
                  [("min to start", "h"), ("pre-fee ROI", "pre"), ("net, no slippage", "s0"), ("net, +1c", "s1"), ("net, +2c", "s2")])
        out += f"### {key.replace('|', ' ')}\n\n{t}\n"
    er = table([{"id": k, "g": v["games"], "t": pct(v["touch_roi"]), "o50": f"{v['n50_contracts']['full_fill_pct']}%", "v50": pct(v["n50_contracts"]["roi_net"]), "c50": f"{v['n50_contracts']['mean_vwap_minus_touch_cents']}c",
                "o200": f"{v['n200_contracts']['full_fill_pct']}%", "v200": pct(v["n200_contracts"]["roi_net"]), "c200": f"{v['n200_contracts']['mean_vwap_minus_touch_cents']}c"} for k, v in ex.items()],
               [("strategy", "id"), ("games", "g"), ("ROI at the touch", "t"), ("50 contracts: full fills", "o50"), ("ROI walking the book", "v50"), ("extra cost", "c50"), ("200 contracts: full fills", "o200"), ("ROI walking the book", "v200"), ("extra cost", "c200")])
    r.write("STRATEGY_ROBUSTNESS.md", f"""# Strategy robustness and executability

{r.banner}

Fees: Kalshi's quadratic taker schedule `0.07 p (1-p)` (reproduces the router's recorded fee to the cent). Slippage: +1c / +2c on the ask. Timing: decisions at T-60, T-10 and T-0 minutes.
Each block: ROI before fees, then net of fees at three slippage levels. Only the five full-game one-sided strategies are shown (they exist in both tiers).

{out}
## Liquidity: walking the archived order book (LIVE, four families with depth)

{er}
Orders of 50 and 200 contracts (about $25 and $100) fill fully in essentially every case and cost only ~0.04-0.2c more than the touch. **Liquidity is not the binding constraint at research stake sizes; the spread and the fee are.**
Depth for periods, overtime, first-10-minutes and props was never captured, so executability there is unobserved.

## Power: how many independent games to detect an edge

{table([{"id": k, **{e: f"{n:,}" for e, n in v["games_needed"].items()}} for k, v in pw.items()], [("strategy", "id")] + [(f"edge {e}", e) for e in next(iter(pw.values()))["games_needed"]])}
## Summary

Before any fee, most strategies are at or below zero; the best live case is about +1 point. After the fee, essentially all are negative, and one cent of slippage deletes the best case. Changing the decision time
between T-60 and T-0 changes almost nothing. Model-uncertainty sensitivity is built into the engine (uncertainty floor, V1/V2 disagreement widening); see EXPRESSION_ENGINE_SPEC.md.
""")


def case(r: R) -> None:
    c, ws = J(r.d, "oct20_case.json"), J(r.d, "wager_summary.json")
    rows = []
    for w in c["wagers"]:
        v1, v2, th = w.get("v1") or {}, w.get("v2") or {}, w.get("thesis") or {}
        rows.append({"bet": f"{w['matchup']} {w['ticker'].split('-')[0].replace('KXNHL','')} {w['ticker'].split('-')[-1]} {w['side']}", "fill": f(w["fill_price"], 3), "after": f(w["minutes_after_scheduled_start"], 1),
                     "stake": f(w["stake"], 2), "res": w["ledger_result"], "pl": f(w["net_pl"], 2), "final": w["final"], "mk": pct(w.get("ev_at_fill_market_mid")), "v1": pct(v1.get("ev_at_fill")) if v1 else "-",
                     "v2": pct(v2.get("ev_at_fill")) if v2 else "-", "th": pct(th.get("ev_at_fill_thesis_adjusted")) if th.get("ev_at_fill_thesis_adjusted") is not None else "none",
                     "n": th.get("n_snapshots", 0)})
    exp = sum((w.get("ev_at_fill_market_mid") or 0) * w["contracts"] for w in c["wagers"])
    dirs = []
    for w in c["wagers"]:
        bm = w.get("board_at_fill")
        if not bm:
            continue
        mkt = (bm["yes_bid"] + bm["yes_ask"]) / 200.0
        mkt = mkt if w["side"] == "YES" else 1 - mkt
        d1 = (w.get("v1") or {}).get("p_win")
        d2 = (w.get("v2") or {}).get("p_win")
        if d1 is None or d2 is None:
            continue
        a, b = d1 - mkt, d2 - mkt
        lab = "opposite directions" if a * b < 0 and min(abs(a), abs(b)) >= 0.01 else ("same direction" if a * b > 0 else "one of them within a point of the market")
        dirs.append(f"{w['matchup']}: V1 {a * 100:+.1f} pts, V2 {b * 100:+.1f} pts vs the market's probability of winning ({lab})")
    dir_txt = "; ".join(dirs)
    pos = [v for w in c["wagers"] for v in ((w.get("v1") or {}).get("ev_at_fill"), (w.get("v2") or {}).get("ev_at_fill")) if v is not None and v > 0]
    pos_txt = f"{100 * min(pos):.1f} to {100 * max(pos):.1f} cents" if pos else "none"
    r.write("OCT20_CASE_STUDY.md", f"""# October 20 case study (routed wagers, real fills)

{r.banner}

## What the ledger says (this corrects the premise)

The accounting ledger records **four** NHL wagers on the 2026-10-20 slate, and **two of them won**. Net result: **{c['net_pl']:+.2f}** on **{c['staked']:.2f}** staked ({c['wins']} wins, {c['losses']} losses). My independent resolver agrees with the ledger on all four
(and on all {ws.get('n')} routed wagers). The two losses were Toronto/Columbus Under 6.5 (final 6-2, total 8) and LA Kings Under 2.5 team goals (LA scored 5, one empty-net). Boston/Dallas Under 5.5 (2-3 in OT, total 5) and Anaheim Under 2.5 team goals
(Anaheim scored 2) **won**. Any analysis that treats all four as losses is analysing a different set of bets.

## The four wagers

Expected value is per contract at the ACTUAL fill price (price + taker fee), under four probability views: the market mid at the fill, V1, V2 (each the last pregame run at or before the fill) and the thesis workflow's confidence-adjusted probability.

{table(rows, [('bet', 'bet'), ('fill price', 'fill'), ('min after sched. start', 'after'), ('stake $', 'stake'), ('result', 'res'), ('net $', 'pl'), ('final', 'final'), ('EV @ market mid', 'mk'), ('EV @ V1', 'v1'), ('EV @ V2', 'v2'), ('EV @ thesis-adj.', 'th'), ('thesis snapshots', 'n')])}
## Was the decision undermined by ...?

* **Weak probabilities.** Under the market's own probability every bet had negative expected value at its fill (the half-spread plus fee, about -2% to -4% per contract). Only some model views were positive, by {pos_txt} per contract - inside the model's measured error (PREDICTION_ENGINE_COMPARISON.md: no incremental information, coefficient not distinguishable from zero).
* **Model disagreement** (each model's win probability minus the market's, for the side bought): {dir_txt}.
* **Price changes / timing.** Three of the four fills were 6 to 8 minutes AFTER the scheduled puck drop (Boston/Dallas started an hour later and was filled 53 minutes before). The last pregame model run was about 10 minutes before the scheduled start, so the
  pregame model could not have priced an in-play quote. Toronto/Columbus was filled at 0.54 against a displayed NO ask of 0.53 (the Over mid had already fallen from 0.485).
* **Alternative scripts.** For Toronto/Columbus the forecast gave the realised script (OPEN_GAME) 19% and the most likely script (BACK_AND_FORTH) 26%; the Under 6.5 cannot win in an 8-goal game. Toronto was on the second night of a back-to-back and still scored six.
* **Matchup adjustments.** The production context knew the confirmed goalies, rest and back-to-back flags (shown in `data/oct20_case.json`); the audit finds no incremental information in those factors beyond the market.
* **Unjustified confidence.** Only one of the four wagers (Toronto/Columbus) was ever a candidate in the thesis workflow; it was FUNDED_RESEARCH in 3 of 13 snapshots at a **$2** research stake and labelled EVIDENCE_MIXED. The routed stake was **$35**. The other three have no thesis decision at all, so they
  did not come from the model-generated recommendations; the ledger carries no provenance field, so "independent handicapping" cannot be separated from other sources.

## How much can four bets say?

Market-implied expected P/L on these four at the fills was about **{exp:+.2f}** dollars (the cost of fees and spread) against a realised **{c['net_pl']:+.2f}**. Across all {ws.get('n')} routed wagers the market-implied expectation is {ws.get('expected_pl_at_market_mid'):+.2f} with a standard
deviation of {ws.get('sd_pl_at_market'):.0f}; the realised {ws.get('net_pl'):+.2f} is {ws.get('z_realized_vs_expected'):+.2f} standard deviations from it. **The results are indistinguishable from paying fees on fairly priced contracts.**
Four bets, all Unders, all driven by one correlated factor (scoring environment), are one observation of that factor, not four.
""")


def render_all(r: R) -> None:
    for fn in (taxonomy, efficiency, matchup, models, signals, walkforward, robustness, case, executive, readme):
        fn(r)


def executive(r: R) -> None:
    cov = J(r.d, "coverage_report.json")
    reg, ma = J(r.d, "hypothesis_results.json"), J(r.d, "model_audit.json")
    th, ws, sh, ef = J(r.d, "thesis_replay.json"), J(r.d, "wager_summary.json"), J(r.d, "shadow_summary.json"), J(r.d, "market_efficiency.json")
    t, g = cov["totals"], cov["games"]
    rr = reg["results"]
    cls: dict[str, int] = {}
    for v in rr.values():
        cls[v["class"]] = cls.get(v["class"], 0) + 1
    hist = ef["HIST_2025_26"]["by_kind_horizon"]

    def one(kind: str, h: int = 60) -> dict[str, Any]:
        return next(x for x in hist if x["kind"] == kind and x["horizon_min"] == h)

    w = one("winner")
    worse = [k for k, v in ma.items() if v.get("n_games") and v["d_brier_lo95"] > 0]
    inc_sig = [k for k, v in ma.items() if v.get("n_games") and v["incremental"]["z"] == v["incremental"]["z"] and v["incremental"]["z"] > 1.96]
    s2, s1 = th["S2_first_chosen|all"], th["S1_first_FUNDED|all"]
    nv = sh["naive_ev"]
    r.write("EXECUTIVE_REPORT.md", f"""# NHL SIFT historical market audit - executive report

{r.banner}

## Bottom line

**With the archive that exists, there is no repeatable, executable, statistically defensible betting advantage in the NHL Kalshi markets, and the existing projection engines add no demonstrated value over the market price.** That is a finding about
a {g['final']}-game sample and a mature, fee-heavy market; it is not proof that no edge exists anywhere. The honest default for the betting engine is PASS, and the infrastructure built here is what would let a real edge be recognised, prospectively, if one appears.

## What the data actually is

* {g['final']} independent final games (2026-09-29..2026-10-20), {t['unique_game_scoped_contracts_in_archive']:,} game-scoped contracts, {t['decided_with_usable_pregame_quote']:,} settled contracts with a usable pregame quote, {cov['ticks']['n_market_ticks']:,} board ticks. The "thousands of captures"
  are repeated looks at the same games; the archive branch has {J(r.d, 'integrity_report.json')['files_on_disk']:,} files, {J(r.d, 'integrity_report.json')['manifest_entries']:,} of them in the hash-verified ledger (not ~18,000).
* A second, separate tier: 1,312 regular-season games of 2025-26 Kalshi candle history (moneyline / total / puck line, no depth).
* Order-book depth exists for 4 of 14 market families; Kalshi's own settlement is absent for live contracts.

## Answers to the success questions

**A. Which families are most efficiently priced?** Moneylines: net ROI of buying either side at T-60m is {pct(w['roi_buy_yes'])} / {pct(w['roi_buy_no'])}, i.e. exactly the spread plus fee, with no statistically significant directional, home or favourite bias. Full-game totals and puck lines are
calibrated to within about 2-3 points. Brier improves toward puck drop (price discovery).

**B. Persistent, executable inefficiencies?** None found. Of {len(rr)} preregistered hypotheses: {', '.join(f'{v} {k}' for k, v in sorted(cls.items()))}. **VALIDATED: {cls.get('VALIDATED', 0)}.** Before fees the best live full-game strategy is about +1 point and the rest are at or below zero (HIST: all negative); after the taker fee essentially all are negative; liquidity is not the constraint (50-200 contract orders fill fully for ~0.1c).

**C. Matchup factors beyond the market?** None. Opponent-adjusted xG, rest, back-to-backs, travel, finishing and special teams all fail out of sample (every hold-out interval includes zero; the one in-sample signal, away back-to-back |z|~2.4, worsens hold-out log loss).

**D. Which projection engines are useful?** None demonstrably. The model's point estimate is worse than the market in nearly every comparison (nominally significant in {len(worse)} of {sum(1 for v in ma.values() if v.get('n_games'))}, uncorrected and overlapping, Brier gaps of at most a few thousandths) and significantly better in none; {len(inc_sig)} families show a significant incremental-information coefficient.

**E. Signals surviving chronological out-of-sample testing?** None. The one pattern suggested by the history (early-season Overs, +10.9% on 39 games) failed its first real out-of-sample test (-4.3% on 140 live games).

**F. How to choose among expression types?** The framework (EXPRESSION_ENGINE_SPEC.md) ranks every contract on both sides by lower-bound net EV and script resilience, de-duplicates correlated risk, and gives the model weight only to the extent its incremental information has been shown. Today that weight is ~0, so it
PASSes all {sh['games']} games. Ignoring the evidence ("naive EV") bets in {nv['games_with_bet']} of {sh['games']} games, claims {pct(nv['claimed_ev_per_contract'])} per contract and realises {pct(nv['roi_net'])} (95% CI {ci(nv['roi_lo95'], nv['roi_hi95'])}).

**G. Maximum acceptable price?** Each card carries it: the price at which the LOWER probability bound just covers price + fee. With the probability anchored on the market it is below the current ask in every case.

**H. Uncertainty and correlation?** Both enter selection: a 2.5-point calibration floor, widening with V1/V2 disagreement; one position per risk factor (a total Under and a team-total Under are one bet).

**I. Evidence to exceed research stakes?** RISK_MANAGEMENT_FRAMEWORK.md: a frozen strategy, positive net ROI after +1c slippage on the prospective tier at predeclared looks (150/300/450 games), calibration no worse than the market, executability from captured depth, a confirming later window, and explicit approval.
Detecting a +3% edge needs hundreds to thousands of independent games depending on price; only a much larger edge could qualify within a season.

**J. Minimal-intervention operation?** A resumable, idempotent pipeline, a daily scorecard with CRITICAL/WARN alarms and a one-line-per-day evidence ledger, shipped as a manual-dispatch workflow (schedule commented out).

## The existing workflows, measured

* Thesis workflow (research selections, scored once per logical bet at first-selection price): first-chosen {pct(s2['roi_net'])} over {s2['n_games']} games ({s2['n_bets']} bets), first-funded {pct(s1['roi_net'])}; it does not beat comparable candidates it rejected, and its claimed EV does not predict realised ROI.
* Routed wagers ({ws.get('n')} wagers, real fills, reported separately): staked {ws.get('staked'):.0f}, net {ws.get('net_pl'):+.2f}. The market-implied expectation at the fills was {ws.get('expected_pl_at_market_mid'):+.2f} (fees and spread); the shortfall is {ws.get('z_realized_vs_expected'):+.1f} standard deviations - indistinguishable from fair-price trading.
* **October 20**: the ledger shows two wins and two losses, not four losses (net {J(r.d, 'oct20_case.json').get('net_pl', 0):+.2f}). See OCT20_CASE_STUDY.md.

## Limitations

{g['final']} games / ~3 weeks of one season; no live Kalshi settlement or trades; depth for four families; the history tier has no depth; HIST was inspected descriptively before registration (only LIVE could validate); starting-goalie and news timing are untestable; CRPS not computed; sample sizes cannot detect edges under roughly 5-10%.

## Implemented, tested, and gated

Code `src/nhl_edge/market_audit/` (26 modules), tests `tests/test_market_audit_*.py`, workflow `market_audit.yml` (manual only). No production path imports any of it. See IMPLEMENTATION_ROADMAP.md for decisions that need approval.
""")


def readme(r: R) -> None:
    r.write("README.md", f"""# NHL SIFT historical market audit

{r.banner}

Start with **EXECUTIVE_REPORT.md**. Resume work from **PROGRESS.md**. Reproduce everything with `python -m nhl_edge.market_audit.pipeline` (see HISTORICAL_RECONSTRUCTION.md).

| document | phase |
|---|---|
| EXECUTIVE_REPORT.md | summary, answers A-J |
| DATA_INVENTORY.md, CAPTURE_COVERAGE.md, DATA_QUALITY_AUDIT.md, HISTORICAL_RECONSTRUCTION.md | A - inventory, coverage, quality, lineage |
| MARKET_TAXONOMY.md, OUTCOME_MAPPING_REPORT.md | B - taxonomy and the deterministic outcome engine |
| MARKET_EFFICIENCY_STUDY.md | C - calibration, bands, lines, friction, power |
| MATCHUP_FACTOR_STUDY.md | D - factors beyond the market |
| PREDICTION_ENGINE_COMPARISON.md, OCT20_CASE_STUDY.md | E - model audit; routed-wager case study |
| CANDIDATE_SIGNAL_REGISTRY.md | F - pre-registered hypotheses, every result |
| EXPRESSION_ENGINE_SPEC.md | G - shadow market-expression engine |
| WALK_FORWARD_VALIDATION.md, STRATEGY_ROBUSTNESS.md | H - replay, controls, fees / slippage / liquidity |
| RISK_MANAGEMENT_FRAMEWORK.md | I |
| AUTOMATION_AND_MONITORING_PLAN.md, IMPLEMENTATION_ROADMAP.md | J and next steps |
| `data/*.json`, `data/wager_audit.csv`, `data/lineage.json` | machine-readable results |
""")
