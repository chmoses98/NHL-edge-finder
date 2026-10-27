# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T12:11:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +22.39 | +6.15 | +10.70 | 0.566 | -49.29 | -67.01 | 40.20 |
| B thesis-diversified (joint) ← optimiser card | 117.16 | +13.77 | +5.66 | +6.90 | 0.632 | -31.36 | -43.74 | 49.53 |
| C best expression per thesis | 90.76 | +10.30 | +3.24 | +12.67 | 0.590 | -25.77 | -32.15 | 28.45 |
| R FUNDED research stakes | 26.00 | +2.42 | +0.91 | +0.80 | 0.614 | -7.68 | -8.75 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  442 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CBJ_win | p_overtime | goals | shots PHI/CBJ | PHI/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.56 | 0.44 | 0.00 | 5.98 | 26.5/26.8 | 23.5/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.49 | 5.83 | 26.8/27.1 | 23.9/23.5 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.086 | 0.48 | 0.52 | 0.00 | 5.97 | 21.0/31.8 | 27.9/17.8 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.52 | 0.48 | 0.47 | 5.89 | 20.9/31.8 | 28.4/17.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.070 | 0.52 | 0.48 | 0.00 | 3.42 | 25.3/25.7 | 23.9/23.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.50 | 0.50 | 0.48 | 2.8 | 24.7/25.1 | 23.6/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 8 | 0.120 | 0.107 | +0.035 | +0.022 | $5.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 84 | 0.884 | 0.871 | +0.035 | +0.021 | $20.00 | FUNDED_RESEARCH | $5 | CBJ:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.118 | 0.102 | +0.033 | +0.017 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Noah Cates: 1+ goals YES | 12 | 0.155 | 0.142 | +0.028 | +0.014 | $3.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (13.64 vs 2.22 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PHI offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no; why: higher confidence-adjusted growth (7.94 vs 3.28 bp); despite a smaller raw edge (+0.035 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense succeeds (4+ goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (7.83 vs 3.25 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT27CBJPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (3.90 vs 2.22 bp); relationships: KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CBJ shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:SUPPRESSED (p 0.4691): highest fidelity KXNHLSPREAD-26OCT27CBJPHI-CBJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT27CBJPHI-CBJAFANTILLI19-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.3066): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.2481): highest fidelity KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT27CBJPHI-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26OCT27CBJPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4307, phi -0.168)
- KXNHLGOAL-26OCT27CBJPHI-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3066, phi -0.147)
- KXNHLGOAL-26OCT27CBJPHI-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4691, phi -0.134)
- KXNHLGOAL-26OCT27CBJPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4307, phi -0.18)

portfolios: A EV +5.24 (adj +1.19) on $35.71, P(profit) 0.4962, adj growth 9.1 bp · B EV +5.23 (adj +3.04) on $32.70, P(profit) 0.3263, adj growth 26.5 bp · C EV +3.35 (adj +1.23) on $37.38, P(profit) 0.7475, adj growth 10.7 bp · R EV +0.21 (adj +0.13) on $5.00, P(profit) 0.8844, adj growth 4.7 bp

## BOS @ CAR  ·  10000 joint draws  ·  444 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_BOS_win | p_overtime | goals | shots CAR/BOS | CAR/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.160 | 0.64 | 0.36 | 0.00 | 6.08 | 34.7/21.2 | 18.4/30.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.142 | 0.64 | 0.36 | 0.00 | 9.39 | 36.2/22.8 | 17.7/28.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.142 | 0.54 | 0.46 | 0.48 | 5.98 | 34.5/21.4 | 18.2/30.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.089 | 0.56 | 0.44 | 0.00 | 6.05 | 28.0/27.0 | 23.6/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.58 | 0.42 | 0.00 | 9.32 | 29.7/28.6 | 22.8/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.51 | 0.49 | 0.50 | 5.99 | 28.0/26.9 | 23.6/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 9.5 goals scored YES | 7 | 0.120 | 0.092 | +0.045 | +0.018 | $2.99 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.37) | EVIDENCE_MIXED | D |
| Boston over 4.5 goals scored YES | 15 | 0.210 | 0.175 | +0.051 | +0.016 | $1.50 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Boston over 3.5 goals scored YES | 31 | 0.388 | 0.344 | +0.063 | +0.019 | $1.32 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Boston over 1.5 goals scored YES | 76 | 0.814 | 0.784 | +0.041 | +0.012 | $6.96 | FUNDED_RESEARCH | $2 | BOS:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Full Game: Over 9.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes; why: higher confidence-adjusted growth (9.79 vs 4.27 bp); despite a smaller raw edge (+0.045 vs +0.051/contract); relationships: KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes: REINFORCING (phi 0.37); KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes: REINFORCING (phi 0.342); KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS2|yes: REINFORCING (phi 0.164); failure: BOS offense suppressed (<= 2 goals)
- **Boston over 4.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT27BOSCAR-10|yes has the higher standalone adjusted growth (9.79 vs 4.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.370); they share one thesis budget; relationships: KXNHLTOTAL-26OCT27BOSCAR-10|yes: REINFORCING (phi 0.37); KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes: DUPLICATIVE (phi 0.648); KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS2|yes: REINFORCING (phi 0.247); failure: CAR wins (incl. OT/SO)
- **Boston over 3.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT27BOSCAR-10|yes has the higher standalone adjusted growth (9.79 vs 3.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.342); they share one thesis budget; relationships: KXNHLTOTAL-26OCT27BOSCAR-10|yes: REINFORCING (phi 0.342); KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes: DUPLICATIVE (phi 0.648); KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS2|yes: DUPLICATIVE (phi 0.381); failure: BOS offense suppressed (<= 2 goals)
- **Boston over 1.5 goals scored YES** — thesis: BOS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes has the higher standalone adjusted growth (4.27 vs 1.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.247); they share one thesis budget; relationships: KXNHLTOTAL-26OCT27BOSCAR-10|yes: REINFORCING (phi 0.164); KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes: REINFORCING (phi 0.247); KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes: DUPLICATIVE (phi 0.381); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · high event (8+) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis GAME:HIGH_EVENT (p 0.3267): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes less than the minimum stake; KXNHLTOTAL-26OCT27BOSCAR-10|yes kept
- thesis BOS:OFFENSE_4PLUS (p 0.3773): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes (same contract)
- thesis BOS:WINS (p 0.4279): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTOTAL-26OCT27BOSCAR-10|yes: FUNDED_RESEARCH; family MIXED; loses 63% of the draws where the thesis happens; opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.263)
- KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes: FUNDED_RESEARCH; family MIXED; loses 44% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.5721, phi -0.466)
- KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.654)
- KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis BOS:SUPPRESSED (p 0.4034, phi -0.582)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes less than the minimum stake; KXNHLTOTAL-26OCT27BOSCAR-10|yes kept
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes kept

portfolios: A EV +9.72 (adj +3.29) on $35.71, P(profit) 0.407, adj growth 17.6 bp · B EV +2.92 (adj +1.05) on $12.76, P(profit) 0.407, adj growth 9.0 bp · C EV +2.64 (adj +0.98) on $5.45, P(profit) 0.2559, adj growth 8.5 bp · R EV +1.23 (adj +0.43) on $5.00, P(profit) 0.407, adj growth 13.2 bp

## LAK @ CHI  ·  10000 joint draws  ·  410 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_LAK_win | p_overtime | goals | shots CHI/LAK | CHI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.48 | 0.52 | 0.00 | 5.97 | 26.7/27.2 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.47 | 5.89 | 26.8/27.3 | 23.9/23.5 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.43 | 0.57 | 0.00 | 5.96 | 21.1/32.4 | 28.4/17.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.46 | 0.54 | 0.47 | 5.84 | 21.5/32.7 | 29.2/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.50 | 0.50 | 0.00 | 9.14 | 28.2/28.9 | 22.8/22.1 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.060 | 0.38 | 0.62 | 0.00 | 9.09 | 22.6/33.9 | 26.7/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Patrick Kane: 1+ assists NO | 55 | 0.690 | 0.580 | +0.123 | +0.012 | $7.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT27LACHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (1.33 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4363): highest fidelity KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no (same contract)
- KXNHLAST-26OCT27LACHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.0 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3406, phi -0.253)

portfolios: A EV +3.09 (adj +0.31) on $14.29, P(profit) 0.6901, adj growth 2.4 bp · B EV +1.72 (adj +0.17) on $7.93, P(profit) 0.6901, adj growth 1.5 bp · C EV +1.72 (adj +0.17) on $7.93, P(profit) 0.6901, adj growth 1.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ STL  ·  10000 joint draws  ·  432 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_MTL_win | p_overtime | goals | shots STL/MTL | STL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.59 | 0.41 | 0.00 | 6.05 | 26.8/26.7 | 23.6/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.53 | 0.47 | 0.47 | 5.96 | 27.1/27.1 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.63 | 0.37 | 0.00 | 9.39 | 28.7/28.3 | 22.8/21.6 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.68 | 0.32 | 0.00 | 6.05 | 31.8/21.3 | 18.6/27.3 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.55 | 0.45 | 0.44 | 5.96 | 31.8/21.4 | 18.1/28.3 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.060 | 0.73 | 0.27 | 0.00 | 9.33 | 33.4/22.7 | 18.2/25.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Noah Dobson: 1+ goals NO | 87 | 0.902 | 0.890 | +0.024 | +0.012 | $20.00 | FUNDED_RESEARCH | $5 | MTL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Noah Dobson: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT27MTLSTL-MTL2|no; why: higher confidence-adjusted growth (3.14 vs 0.37 bp); despite a smaller raw edge (+0.024 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MTL:SUPPRESSED (p 0.4358): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT27MTLSTL-MTLNDOBSON53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3448, phi -0.143)

portfolios: A EV +0.39 (adj +0.20) on $14.29, P(profit) 0.902, adj growth 1.9 bp · B EV +0.55 (adj +0.28) on $20.00, P(profit) 0.902, adj growth 2.6 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.14 (adj +0.07) on $5.00, P(profit) 0.902, adj growth 2.6 bp

## NYI @ NSH  ·  10000 joint draws  ·  418 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_NYI_win | p_overtime | goals | shots NSH/NYI | NSH/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.55 | 0.45 | 0.00 | 6.0 | 27.9/28.0 | 24.7/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.49 | 5.96 | 27.9/28.2 | 24.8/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.55 | 0.45 | 0.00 | 9.32 | 29.3/29.5 | 23.7/23.0 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.079 | 0.47 | 0.53 | 0.00 | 5.97 | 22.2/33.1 | 29.5/18.9 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.45 | 0.55 | 0.48 | 5.91 | 22.1/32.8 | 29.3/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.059 | 0.61 | 0.39 | 0.00 | 5.99 | 32.6/22.4 | 19.4/28.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ DAL  ·  10000 joint draws  ·  426 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NJD_win | p_overtime | goals | shots DAL/NJD | DAL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 6.02 | 26.8/26.9 | 23.8/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.48 | 5.9 | 26.9/26.9 | 23.6/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.60 | 0.40 | 0.00 | 9.16 | 28.0/28.1 | 22.7/21.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.075 | 0.51 | 0.49 | 0.00 | 5.99 | 21.2/31.7 | 28.0/17.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.48 | 0.52 | 0.48 | 5.86 | 21.6/31.9 | 28.4/18.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.065 | 0.69 | 0.31 | 0.00 | 5.94 | 31.0/21.0 | 18.4/26.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## FLA @ WPG  ·  10000 joint draws  ·  440 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_FLA_win | p_overtime | goals | shots WPG/FLA | WPG/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.56 | 0.44 | 0.00 | 6.01 | 26.8/26.7 | 23.4/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.46 | 5.89 | 26.6/27.0 | 23.6/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.54 | 0.46 | 0.00 | 9.24 | 28.3/28.3 | 22.6/22.1 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.48 | 0.52 | 0.00 | 6.01 | 21.5/31.9 | 28.1/18.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.49 | 0.51 | 0.47 | 5.9 | 21.5/31.5 | 28.1/18.3 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.060 | 0.62 | 0.38 | 0.00 | 5.96 | 31.4/21.3 | 18.5/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 79 | 0.850 | 0.817 | +0.048 | +0.016 | $20.00 | FUNDED_RESEARCH | $5 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA2|no; why: higher confidence-adjusted growth (3.43 vs 0.95 bp); alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis WPG:WINS (p 0.5296): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27FLAWPG-FLA3|no (same contract)
- KXNHLSPREAD-26OCT27FLAWPG-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2511, phi -0.726)

portfolios: A EV +0.86 (adj +0.28) on $14.29, P(profit) 0.8497, adj growth 2.6 bp · B EV +1.20 (adj +0.39) on $20.00, P(profit) 0.8497, adj growth 3.5 bp · C EV +1.20 (adj +0.39) on $20.00, P(profit) 0.8497, adj growth 3.5 bp · R EV +0.30 (adj +0.10) on $5.00, P(profit) 0.8497, adj growth 3.5 bp

## MIN @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_MIN_win | p_overtime | goals | shots UTA/MIN | UTA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.59 | 0.41 | 0.00 | 6.05 | 28.4/28.4 | 25.2/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.44 | 5.97 | 27.8/27.9 | 24.6/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.59 | 0.41 | 0.00 | 9.3 | 29.8/29.6 | 24.2/22.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.65 | 0.35 | 0.00 | 6.01 | 33.4/22.5 | 19.7/29.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.57 | 0.43 | 0.46 | 5.93 | 33.4/22.6 | 19.5/29.9 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.059 | 0.67 | 0.33 | 0.00 | 9.26 | 34.8/23.8 | 19.0/26.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_OTT_win | p_overtime | goals | shots VGK/OTT | VGK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.63 | 0.37 | 0.00 | 6.05 | 26.7/26.6 | 23.6/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.46 | 5.88 | 26.7/26.7 | 23.5/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.63 | 0.37 | 0.00 | 9.34 | 28.2/28.2 | 22.8/21.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.078 | 0.70 | 0.30 | 0.00 | 6.03 | 31.0/20.9 | 18.2/26.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.57 | 0.43 | 0.45 | 5.89 | 31.4/21.1 | 17.9/27.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.56 | 0.44 | 0.00 | 5.94 | 21.3/31.6 | 28.2/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_VAN_win | p_overtime | goals | shots ANA/VAN | ANA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.148 | 0.66 | 0.34 | 0.00 | 6.06 | 34.1/21.4 | 18.7/29.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.140 | 0.71 | 0.29 | 0.00 | 9.53 | 35.9/22.8 | 18.1/27.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.54 | 0.46 | 0.48 | 5.99 | 34.5/21.6 | 18.4/30.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.64 | 0.36 | 0.00 | 6.09 | 28.0/27.0 | 24.1/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.61 | 0.39 | 0.00 | 9.52 | 29.7/28.7 | 23.0/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.50 | 0.50 | 0.47 | 5.94 | 28.1/27.3 | 24.1/24.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BUF_win | p_overtime | goals | shots SJS/BUF | SJS/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.01 | 27.7/27.9 | 24.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.46 | 5.93 | 27.6/27.9 | 24.6/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.56 | 0.44 | 0.00 | 9.4 | 29.3/29.6 | 23.8/22.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.082 | 0.50 | 0.50 | 0.00 | 6.02 | 22.0/32.8 | 28.8/18.6 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.48 | 0.52 | 0.46 | 6.03 | 22.5/33.0 | 29.5/19.3 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.060 | 0.46 | 0.54 | 0.00 | 9.34 | 23.5/34.4 | 27.7/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 2.5 goals NO | 77 | 0.837 | 0.801 | +0.054 | +0.018 | $19.94 | FUNDED_RESEARCH | $5 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose wins by over 1.5 goals YES | 25 | 0.317 | 0.281 | +0.054 | +0.018 | $3.83 | FUNDED_RESEARCH | $1 | SJS:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes; why: higher confidence-adjusted growth (4.36 vs 3.55 bp); wins across more scripts (relative breadth 1.031 vs 0.525); relationships: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: DUPLICATIVE (phi 0.301); failure: BUF wins by 2+
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no has the higher standalone adjusted growth (4.36 vs 3.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: DUPLICATIVE (phi 0.301); failure: BUF wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:WINS (p 0.5311): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF3|no (same contract)
- thesis SJS:WINS_BY_2PLUS (p 0.3168): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF3|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3858): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF3|no (same contract)
- KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.266, phi -0.734)
- KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4689, phi -0.64)

portfolios: A EV +3.09 (adj +0.88) on $35.71, P(profit) 0.5812, adj growth 6.7 bp · B EV +2.16 (adj +0.73) on $23.77, P(profit) 0.8365, adj growth 6.4 bp · C EV +1.38 (adj +0.47) on $20.00, P(profit) 0.8365, adj growth 4.2 bp · R EV +0.55 (adj +0.18) on $6.00, P(profit) 0.8365, adj growth 6.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
