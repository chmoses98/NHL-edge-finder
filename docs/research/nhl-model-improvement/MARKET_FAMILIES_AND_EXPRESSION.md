# Market families and market-expression research

> RESEARCH ONLY. Market-efficiency numbers are those of the reproduced prior audit (`docs/research/nhl-market-audit/MARKET_EFFICIENCY_STUDY.md`; the cold re-run reproduces them identically). This report adds the cost-of-expression analysis, the corrected shadow engine and its replay. Season futures, awards and player-season markets are a different instrument class (months of horizon, different settlement) and are excluded from every statistic here. Goal-scorer families (`player_goals`, `first_goal`) are researched but **never recommended**.

## 1. Family-by-family evidence (net ROI = buy the displayed ask with the taker fee `0.07·p·(1−p)`; T-60 min; 95% CIs resample games)

| family | tier / games | net ROI buy YES | net ROI buy NO | calibration | reading |
|---|---|---|---|---|---|
| moneyline (winner) | HIST 1,312 / LIVE 151 | −4.3% [−4.7, −4.0] / −4.0% | −4.3% / −4.3% | gap ≈ 0 | cost = half-spread + fee; no mispricing |
| full-game total | HIST 1,198 / LIVE 151 | −3.2% [−6.2, −0.3] / −2.5% [−9.4, +4.1] | −8.5% [−12.1, −4.5] / −3.7% [−11.9, +4.9] | HIST gap +1.0% (lines 2.5 and 4.5 +3.4 / +2.4 pts, uncorrected CI > 0) | slightly low-priced Overs at some lines; still negative net |
| puck line / alt spreads | HIST 1,198 / LIVE 151 | −13.2% / −4.8% | −2.4% [−4.2, −0.7] / −2.9% | gap −0.8% | YES on "wins by >2.5" is the worst-priced leg in HIST |
| team total | LIVE 151 | −5.0% [−12.3, +2.1] | −3.0% [−8.4, +2.5] | gap −0.2% | wide CIs |
| period winner | LIVE 151 | −6.9% [−8.2, −5.5] | −4.6% [−5.3, −3.9] | slope 1.17 (SE 0.26) | tie leg, 3-way |
| period total | LIVE 151 | −1.9% [−7.2, +3.5] | −9.8% [−17.8, −1.9] | gap +1.5% | |
| period spread | LIVE 151 | +8.3% [−5.5, +22.2] | −6.4% [−8.6, −4.1] | gap +3.5% | positive point estimate, CI spans 0; not registered before looking |
| overtime | LIVE 140 | −2.5% | −4.1% | gap +1.4% | very wide CIs |
| early goal | LIVE 151 | −9.1% | +0.1% [−17.4, +17.6] | gap −2.8% | the (now POINT_POSITIVE) M14 |
| player stat (points, assists, saves) | LIVE 151 / 15,268 contracts | −10.5% | −2.5% | slope 1.00 | model worse than market (prior audit) |
| first goal / goal scorer | LIVE 115–128 | n/a | −3.2% | slope 0.45 | never recommended |

Frictions: spreads are 1–4 cents on liquid families (0.5–2 cents half-spread) plus 1.2–1.75 cents of fee; order-book depth exists for four families only and 50–200-contract orders fill fully for ≈ 0.1 cent (prior audit). **No family shows a repeatable, executable inefficiency**; the registry (v1.1 labels): 0 VALIDATED, 0 PROMISING_V11, 3 UNPROFITABLE_AT_ASK (M1, M3, M5), 1 POINT_POSITIVE (M14), 12 INCONCLUSIVE — and 12 of 16 hypotheses have at least one tier too small to detect an ROI below 10%.

Not covered, and why: alternate totals/spreads as *separate* strategies (pooled into the total/spread rows); player shots (no Kalshi shots market in the archive; PLAYER_SIM stores shots only as expectations); in-play pricing (not archived).

## 2. The cost of expressing a thesis

A thesis is not a bet. For one real game (TOR @ CBJ, T-60 board on 2026-10-20) and a "lower-scoring than the market expects" thesis, the cost of each expression — how far above the market's own probability the true win probability must be before a taker buy breaks even — is:

| expression | price paid | fee | break-even probability | market-implied | **edge the thesis must supply** |
|---|---|---|---|---|---|
| Under 6.5 total (buy NO) | 0.50 | 1.75c | 0.5175 | 0.495 | **+2.25 pts** |
| Under 5.5 total (buy NO) | 0.40 | 1.68c | 0.4168 | 0.395 | +2.18 pts |
| CBJ team total Under 2.5 (buy NO) | 0.32 | 1.52c | 0.3352 | 0.305 | **+3.02 pts** (spread 3c) |
| TOR team total Under 3.5 (buy NO) | 0.64 | 1.61c | 0.6561 | 0.635 | +2.11 pts |
| CBJ moneyline (buy YES) | 0.61 | 1.67c | 0.6267 | 0.605 | +2.17 pts |
| "TOR wins by >1.5" (buy NO) | 0.78 | 1.20c | 0.7920 | 0.775 | +1.70 pts |

Every expression asks for 2–3 points of genuine edge before it breaks even; the *thinnest* markets (team totals, 3-cent spreads) are the most expensive and the *deepest-price* legs (puck-line NO at 0.78) the cheapest in points, but cheaper expressions also pay less when right. Because no model advantage over the market has been demonstrated (the fitted incremental weight c ≈ 0.27 would turn a typical 5-point model-minus-market gap into ≈ 1.3 points, and its Brier benefit is not distinguishable from zero), **none of these clears its break-even**; the best expression of an unsupported thesis is **PASS**.

## 3. The shadow expression engine (`market_audit/expression_engine.py`, default PASS)

Per game it ranks the eligible expressions on both sides: probability `p_hat = mid + w·(p_model − mid)` with `w = max(0, c_lo90)` (the audited incremental-information coefficient minus 1.28 SE; ≈ 0 today), uncertainty `se² = 0.025² + (½|p_V1 − p_V2|)²` with `p_low = p_hat − 1.28·se`, net EV at the **executable** price using `p_low`, a "maximum acceptable price" (break-even root with `p_low`), script survival ≥ 0.5, depth ≥ 25, one position per risk factor, and a side-specific VALIDATED gate. It returns PASS when nothing clears.

**Corrections from the independent review** (details in `PR52_INDEPENDENT_REVIEW.md`): the v1.0 uncertainty term double-counted the model weight and made BET impossible for every input; input/units/crossed-book gate; side-specific evidence; reported correlation skips. Regression tests use realistic books (`tests/test_market_audit_engine_v11.py`).

**Replay on the 151 LIVE games with the corrected engine** (`data/shadow_summary_fixed_engine.json`):

| policy | bets | games with a bet | net ROI (95% CI) | claimed EV / contract |
|---|---|---|---|---|
| `strict` (evidence gate + audited weight) | **0** | 0 (PASS 100%) | — | — |
| `research_unvalidated` (gate waived, w = 0.5) | 190 | 108 | **−16.5% [−30.4%, −2.6%]** | +5.1% |
| `naive_ev` (gate waived, w = 1, uncertainty ignored) | 299 | 150 | −7.5% [−19.2%, +4.2%] | +10.5% |

The strict engine recommends zero wagers because *no family has evidence*, not because of a bug. The counterfactual that waives the gate and trusts the model at half weight would have lost 16.5% — the first quantitative evidence (rather than a mechanical PASS) that trusting these models on these markets costs money (largest buckets: player assists −16.3% on 104 bets, player points −9.8% on 59; game-scoped bets are few).

## 4. Script resilience and expression choice

`script_survival` (share of NHL_SCRIPT_V1 draw mass in which a bet stays +EV) is a design input. The scripts themselves are calibrated within sampling error (see `MATCHUP_AND_SCRIPT_STUDY.md`) but their lift over base rates is marginal (paired Brier −0.0099, 95% CI −0.021…+0.0001, n = 99), so **survival is an explanatory aid, not evidence of edge**. Whether survival predicts *realised* betting performance was not testable: with no VALIDATED strategy and a corrected engine that selects nothing, there is no selected-bet sample with survival values to test (the prior audit's thesis-selection replay: −5.8% first-chosen, −9.1% first-funded, claimed EV does not predict realised ROI).

## 5. How SIFT should communicate uncertainty and PASS

Show the market-implied probability and the model's, the *break-even* probability after fee and executable price, and the evidence class of the family (INCONCLUSIVE / UNPROFITABLE_AT_ASK …). Say "PASS — no expression clears its cost on the available evidence" as a first-class outcome. Never present model-minus-market gaps below ~5 points as edge: the models' disagreement with the market is, on average, a loss of Brier (V1 − mid ≈ +0.0014…+0.0045).
