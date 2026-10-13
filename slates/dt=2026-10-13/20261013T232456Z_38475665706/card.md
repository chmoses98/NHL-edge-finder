# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T23:24:56Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +32.44 | +6.84 | +31.80 | 0.849 | -7.52 | -17.78 | 63.52 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +29.17 | +15.49 | +26.39 | 0.746 | -21.83 | -33.46 | 146.20 |
| C best expression per thesis | 150.00 | +26.22 | +9.43 | +25.24 | 0.793 | -13.41 | -24.21 | 89.18 |
| R FUNDED research stakes | 16.00 | +2.66 | +1.84 | -1.28 | 0.401 | -5.42 | -8.56 | 0.00 |

## STL @ OTT  ·  10000 joint draws  ·  468 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.472 / away 0.528

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_STL_win | p_overtime | goals | shots OTT/STL | OTT/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.51 | 0.49 | 0.00 | 6.01 | 26.8/26.3 | 22.9/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.47 | 5.94 | 26.6/26.2 | 23.0/23.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.108 | 0.58 | 0.42 | 0.00 | 6.01 | 31.9/20.7 | 17.6/27.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.47 | 5.93 | 32.1/21.0 | 17.9/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.47 | 0.53 | 0.00 | 9.26 | 28.1/27.6 | 21.4/22.1 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.067 | 0.58 | 0.42 | 0.00 | 9.08 | 33.4/22.1 | 17.1/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael Amadio: 1+ goals YES | 13 | 0.178 | 0.165 | +0.041 | +0.027 | $3.16 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Stephen Halliday: 1+ goals YES | 11 | 0.148 | 0.138 | +0.031 | +0.021 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 9 | 0.118 | 0.110 | +0.023 | +0.014 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 71 | 0.838 | 0.745 | +0.114 | +0.021 | $8.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (13.36 vs 3.40 bp); despite a smaller raw edge (+0.041 vs +0.099/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13STLOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13STLOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: OTT offense suppressed (<= 2 goals)
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (8.85 vs 3.40 bp); despite a smaller raw edge (+0.031 vs +0.099/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13STLOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: OTT offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (5.05 vs 3.40 bp); despite a smaller raw edge (+0.023 vs +0.099/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13STLOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13STLOTT-OTTABURAKOVSKY95-1|no; why: higher confidence-adjusted growth (4.69 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13STLOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT13STLOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3877): highest fidelity KXNHLAST-26OCT13STLOTT-OTTJSPENCE10-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-OTTJSPENCE10-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3723): highest fidelity KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13STLOTT-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3994): highest fidelity KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no (same contract)
- KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3952, phi -0.198)
- KXNHLGOAL-26OCT13STLOTT-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3952, phi -0.177)
- KXNHLGOAL-26OCT13STLOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3952, phi -0.157)
- KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3877, phi -0.169)

portfolios: A EV +3.68 (adj +0.61) on $15.00, P(profit) 0.557, adj growth 5.6 bp · B EV +3.27 (adj +1.51) on $15.60, P(profit) 0.384, adj growth 14.3 bp · C EV +1.93 (adj +0.45) on $11.11, P(profit) 0.427, adj growth 4.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NYI  ·  10000 joint draws  ·  436 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.647 / away 0.352

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_VAN_win | p_overtime | goals | shots NYI/VAN | NYI/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.126 | 0.68 | 0.32 | 0.00 | 6.02 | 32.8/21.2 | 18.5/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.63 | 0.37 | 0.00 | 5.99 | 27.4/26.9 | 23.8/23.4 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.55 | 0.45 | 0.49 | 5.92 | 33.2/21.5 | 18.3/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.47 | 5.9 | 27.7/27.2 | 24.0/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.63 | 0.37 | 0.00 | 9.22 | 29.2/28.5 | 23.2/22.4 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.080 | 0.71 | 0.29 | 0.00 | 9.2 | 34.8/22.8 | 18.4/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 13 | 0.185 | 0.169 | +0.047 | +0.031 | $3.51 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.219 | 0.203 | +0.040 | +0.023 | $2.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.016 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Adam Pelech: 1+ goals YES | 5 | 0.073 | 0.063 | +0.020 | +0.010 | $1.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (17.28 vs 8.04 bp); relationships: KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT13VANNYI-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13VANNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI3|no; why: higher confidence-adjusted growth (8.04 vs 3.15 bp); despite a smaller raw edge (+0.040 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT13VANNYI-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13VANNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (8.04 vs 5.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13VANNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Adam Pelech: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13VANNYI-NYICRITCHIE64-1|yes; why: higher confidence-adjusted growth (4.33 vs 1.08 bp); despite a smaller raw edge (+0.020 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT13VANNYI-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3174): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3313): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4291): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.202)
- KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.235)
- KXNHLGOAL-26OCT13VANNYI-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.183)
- KXNHLGOAL-26OCT13VANNYI-NYIAPELECH3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3313, phi -0.107)

portfolios: A EV +1.67 (adj +0.37) on $15.00, P(profit) 0.6974, adj growth 3.5 bp · B EV +2.61 (adj +1.61) on $9.09, P(profit) 0.4887, adj growth 15.1 bp · C EV +1.30 (adj +0.67) on $14.61, P(profit) 0.6672, adj growth 6.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ CHI  ·  10000 joint draws  ·  448 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.415 / away 0.585

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.43 | 0.57 | 0.00 | 6.02 | 26.9/27.3 | 23.4/23.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 6.02 | 21.2/32.7 | 28.1/18.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.46 | 5.95 | 26.8/27.4 | 24.1/23.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.42 | 0.58 | 0.49 | 5.94 | 21.3/32.6 | 29.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.46 | 0.54 | 0.00 | 9.34 | 28.2/28.9 | 22.1/22.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.075 | 0.32 | 0.68 | 0.00 | 9.27 | 22.7/34.4 | 26.3/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.182 | 0.165 | +0.055 | +0.038 | $4.23 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 53 | 0.735 | 0.595 | +0.188 | +0.048 | $8.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Connor Dewar: 1+ goals YES | 12 | 0.166 | 0.153 | +0.038 | +0.026 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ assists YES | 27 | 0.334 | 0.300 | +0.050 | +0.016 | $2.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (27.39 vs 2.68 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13PITCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (20.32 vs 3.49 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: CHI offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (12.82 vs 0.42 bp); despite a smaller raw edge (+0.038 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: PIT offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ assists YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (27.39 vs 2.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.362): highest fidelity KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4247): highest fidelity KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4347): highest fidelity KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4247, phi -0.214)
- KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.362, phi -0.228)
- KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3451, phi -0.191)
- KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4247, phi -0.269)

portfolios: A EV +3.38 (adj +0.70) on $15.00, P(profit) 0.7159, adj growth 6.7 bp · B EV +6.03 (adj +2.71) on $17.99, P(profit) 0.4767, adj growth 25.7 bp · C EV +6.06 (adj +2.80) on $20.80, P(profit) 0.6992, adj growth 26.4 bp · R EV +0.86 (adj +0.59) on $2.00, P(profit) 0.182, adj growth 20.9 bp

## MIN @ WPG  ·  10000 joint draws  ·  474 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MIN_win | p_overtime | goals | shots WPG/MIN | WPG/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.54 | 0.46 | 0.00 | 5.99 | 28.2/28.1 | 24.7/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.88 | 28.3/28.4 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.55 | 0.45 | 0.00 | 9.28 | 30.0/30.0 | 24.2/23.6 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.070 | 0.56 | 0.44 | 0.00 | 5.98 | 33.1/22.4 | 19.2/29.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.070 | 0.45 | 0.55 | 0.00 | 5.96 | 22.7/33.4 | 29.5/19.5 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.45 | 0.55 | 0.47 | 5.83 | 22.4/32.9 | 29.4/19.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Neal Pionk: 1+ goals NO | 86 | 0.932 | 0.913 | +0.064 | +0.044 | $8.54 | FUNDED_RESEARCH | $3 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 4 | 0.067 | 0.057 | +0.025 | +0.014 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.135 | 0.125 | +0.029 | +0.019 | $2.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 22 | 0.305 | 0.258 | +0.073 | +0.026 | $2.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13MINWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (39.23 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13MINWPG-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense succeeds (4+ goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (10.07 vs 7.97 bp); despite a smaller raw edge (+0.025 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.06); failure: MIN offense suppressed (<= 2 goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (8.10 vs 7.97 bp); despite a smaller raw edge (+0.029 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13MINWPG-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (7.97 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.06); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4173): highest fidelity KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13MINWPG-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.3874): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3878, phi -0.116)
- KXNHLGOAL-26OCT13MINWPG-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.126)
- KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.146)
- KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.274)

portfolios: A EV +2.19 (adj +0.82) on $15.00, P(profit) 0.5819, adj growth 7.9 bp · B EV +2.83 (adj +1.53) on $14.80, P(profit) 0.4172, adj growth 14.6 bp · C EV +2.01 (adj +0.75) on $18.43, P(profit) 0.7264, adj growth 7.1 bp · R EV +0.22 (adj +0.15) on $3.00, P(profit) 0.9322, adj growth 6.1 bp

## COL @ DAL  ·  10000 joint draws  ·  454 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.517 / away 0.483

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_COL_win | p_overtime | goals | shots DAL/COL | DAL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.46 | 0.54 | 0.00 | 6.0 | 26.8/27.2 | 23.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.9 | 26.9/27.4 | 24.2/23.5 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.101 | 0.40 | 0.60 | 0.00 | 6.01 | 21.2/32.7 | 28.7/18.2 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.44 | 0.56 | 0.48 | 5.88 | 21.5/32.8 | 29.3/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.45 | 0.55 | 0.00 | 9.29 | 28.4/28.9 | 22.6/22.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.067 | 0.41 | 0.59 | 0.00 | 9.18 | 22.7/34.3 | 27.4/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zachary L'Heureux: 1+ goals YES | 9 | 0.136 | 0.122 | +0.040 | +0.026 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 20 | 0.256 | 0.241 | +0.045 | +0.030 | $3.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 9 | 0.116 | 0.108 | +0.020 | +0.013 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 58 | 0.630 | 0.616 | +0.033 | +0.019 | $5.14 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (16.47 vs 11.33 bp); despite a smaller raw edge (+0.040 vs +0.045/contract); relationships: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (11.33 vs 2.51 bp); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: COL offense suppressed (<= 2 goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13COLDAL-DALTHARLEY55-2|yes; why: higher confidence-adjusted growth (3.95 vs 0.96 bp); despite a smaller raw edge (+0.020 vs +0.026/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.931 vs 0.799); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no; why: Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV is 0.6 pts higher while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT13COLDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3802): highest fidelity KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no — Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV is 0.6 pts higher while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DAL:SUPPRESSED (p 0.4216): highest fidelity KXNHLAST-26OCT13COLDAL-DALRHINTZ24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13COLDAL-DALRHINTZ24-1|no (same contract)
- KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.18)
- KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.232)
- KXNHLGOAL-26OCT13COLDAL-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.4216, phi -0.163)
- KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4057, phi -0.286)
- override: Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV is 0.6 pts higher while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.87 (adj +0.69) on $15.00, P(profit) 0.4812, adj growth 6.5 bp · B EV +2.49 (adj +1.60) on $12.96, P(profit) 0.4306, adj growth 15.1 bp · C EV +1.92 (adj +0.88) on $14.96, P(profit) 0.5913, adj growth 8.3 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.6302, adj growth 2.4 bp

## VGK @ NSH  ·  10000 joint draws  ·  486 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_VGK_win | p_overtime | goals | shots NSH/VGK | NSH/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.53 | 0.47 | 0.00 | 6.02 | 27.5/28.0 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.87 | 27.7/28.2 | 24.9/24.5 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.47 | 0.53 | 0.00 | 5.97 | 22.1/33.5 | 29.9/18.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.47 | 0.53 | 0.47 | 5.89 | 22.1/33.3 | 29.8/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.37 | 29.2/29.5 | 23.8/22.6 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.060 | 0.48 | 0.52 | 0.00 | 9.18 | 23.8/35.0 | 28.2/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Wilsby: 1+ goals YES | 4 | 0.065 | 0.055 | +0.022 | +0.012 | $1.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 71 | 0.762 | 0.748 | +0.037 | +0.023 | $8.54 | FUNDED_RESEARCH | $3 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Brady Skjei: 1+ assists YES | 23 | 0.308 | 0.262 | +0.066 | +0.019 | $2.38 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.070 | 0.063 | +0.016 | +0.010 | $1.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes; why: higher confidence-adjusted growth (7.95 vs 4.32 bp); despite a smaller raw edge (+0.022 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT13VGKNSH-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (5.85 vs 3.28 bp); relationships: KXNHLGOAL-26OCT13VGKNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT13VGKNSH-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense succeeds (4+ goals)
- **Brady Skjei: 1+ assists YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13VGKNSH-VGK3|no; why: higher confidence-adjusted growth (4.32 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13VGKNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT13VGKNSH-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NSH offense suppressed (<= 2 goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (4.29 vs 0.08 bp); despite a smaller raw edge (+0.016 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13VGKNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4121): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3848): highest fidelity KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3696): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13VGKNSH-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3975, phi -0.117)
- KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.231)
- KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3975, phi -0.259)
- KXNHLGOAL-26OCT13VGKNSH-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4121, phi -0.121)

portfolios: A EV +2.49 (adj +0.55) on $15.00, P(profit) 0.5206, adj growth 5.1 bp · B EV +1.98 (adj +0.98) on $13.07, P(profit) 0.3326, adj growth 9.2 bp · C EV +1.16 (adj +0.49) on $11.61, P(profit) 0.7616, adj growth 4.6 bp · R EV +0.15 (adj +0.10) on $3.00, P(profit) 0.7616, adj growth 3.6 bp

## TOR @ UTA  ·  10000 joint draws  ·  478 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.590 / away 0.410

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TOR_win | p_overtime | goals | shots UTA/TOR | UTA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.140 | 0.68 | 0.32 | 0.00 | 6.02 | 34.5/21.9 | 19.3/29.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.57 | 0.43 | 0.49 | 5.95 | 34.7/22.1 | 18.9/31.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.106 | 0.71 | 0.29 | 0.00 | 9.33 | 36.2/23.3 | 18.7/27.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.63 | 0.37 | 0.00 | 6.03 | 28.6/27.7 | 24.6/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.54 | 0.46 | 0.47 | 5.97 | 28.7/27.8 | 24.6/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.61 | 0.39 | 0.00 | 9.32 | 30.3/29.3 | 23.8/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 70 | 0.788 | 0.739 | +0.073 | +0.024 | $8.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Easton Cowan: 1+ assists YES | 24 | 0.310 | 0.270 | +0.057 | +0.017 | $2.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 62 | 0.669 | 0.655 | +0.032 | +0.019 | $4.82 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 64 | 0.683 | 0.671 | +0.027 | +0.015 | $5.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (6.43 vs 3.32 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: UTA offense succeeds (4+ goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13TORUTA-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (3.44 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no: INTENTIONAL_DIVERSIFIER (phi -0.081); failure: TOR offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTANSCHMALTZ8-1|no; why: higher confidence-adjusted growth (3.32 vs 1.92 bp); relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no; why: Player prop expression KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.081); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: TOR offense succeeds (4+ goals)

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.14, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · high event (8+) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3266): highest fidelity KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3113): highest fidelity KXNHLGOAL-26OCT13TORUTA-UTANSCHMALTZ8-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.4531): highest fidelity KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no — Player prop expression KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.189)
- KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4531, phi -0.283)
- KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.243)
- KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3266, phi -0.293)
- override: Player prop expression KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.81 (adj +0.55) on $15.00, P(profit) 0.6823, adj growth 5.2 bp · B EV +1.82 (adj +0.70) on $20.43, P(profit) 0.5307, adj growth 6.6 bp · C EV +1.41 (adj +0.48) on $13.76, P(profit) 0.5916, adj growth 4.5 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.6686, adj growth 2.2 bp

## CGY @ ANA  ·  10000 joint draws  ·  494 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.391

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_CGY_win | p_overtime | goals | shots ANA/CGY | ANA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.132 | 0.72 | 0.28 | 0.00 | 6.0 | 34.5/22.4 | 19.9/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.69 | 0.31 | 0.00 | 6.0 | 29.6/28.8 | 26.2/25.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.55 | 0.45 | 0.44 | 5.96 | 35.1/22.8 | 19.7/31.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.52 | 0.48 | 0.49 | 5.96 | 29.2/28.5 | 25.1/25.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.092 | 0.75 | 0.25 | 0.00 | 9.3 | 36.4/23.8 | 19.6/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.69 | 0.31 | 0.00 | 9.37 | 30.9/30.0 | 24.8/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 2+ goals YES | 2 | 0.044 | 0.038 | +0.023 | +0.017 | $1.47 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 10 | 0.140 | 0.128 | +0.033 | +0.022 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 11 | 0.149 | 0.138 | +0.032 | +0.021 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Nikita Nesterenko: 1+ assists NO | 74 | 0.807 | 0.769 | +0.054 | +0.015 | $8.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (27.05 vs 5.50 bp); despite a smaller raw edge (+0.023 vs +0.092/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: MOSTLY_INDEPENDENT (phi -0.048); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (10.98 vs 5.50 bp); despite a smaller raw edge (+0.033 vs +0.092/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (9.31 vs 5.50 bp); despite a smaller raw edge (+0.032 vs +0.092/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: MOSTLY_INDEPENDENT (phi -0.034); failure: ANA offense suppressed (<= 2 goals)
- **Nikita Nesterenko: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13CGYANA-ANANNESTERENKO13-1|no; why: higher confidence-adjusted growth (2.73 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: ANA offense succeeds (4+ goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.497): highest fidelity KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.3057): highest fidelity KXNHLPTS-26OCT13CGYANA-CGYKBAHL7-1|yes [FRAGILE], best adjusted EV KXNHLPTS-26OCT13CGYANA-CGYKBAHL7-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.2944): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.13)
- KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.147)
- KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.137)
- KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.497, phi -0.181)

portfolios: A EV +7.59 (adj +1.16) on $15.00, P(profit) 0.6415, adj growth 10.0 bp · B EV +3.61 (adj +2.28) on $14.83, P(profit) 0.3029, adj growth 21.2 bp · C EV +1.87 (adj +0.32) on $3.35, P(profit) 0.4775, adj growth 3.0 bp · R EV +1.07 (adj +0.79) on $1.00, P(profit) 0.0442, adj growth 24.7 bp

## EDM @ LAK  ·  10000 joint draws  ·  480 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.462 / away 0.538

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_EDM_win | p_overtime | goals | shots LAK/EDM | LAK/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.47 | 0.53 | 0.00 | 6.01 | 27.8/27.9 | 24.2/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.51 | 0.49 | 0.48 | 5.91 | 28.1/28.1 | 24.7/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.45 | 0.55 | 0.00 | 9.36 | 29.4/29.4 | 22.9/23.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.077 | 0.43 | 0.57 | 0.00 | 6.02 | 22.2/33.1 | 29.0/19.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.46 | 0.54 | 0.48 | 5.96 | 22.3/33.1 | 29.6/19.1 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 6.03 | 32.6/22.2 | 19.1/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artemi Panarin: 2+ assists NO | 82 | 0.910 | 0.862 | +0.080 | +0.032 | $8.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Andre Lee: 1+ goals YES | 8 | 0.111 | 0.102 | +0.025 | +0.017 | $1.79 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 15 | 0.191 | 0.180 | +0.033 | +0.021 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ assists YES | 28 | 0.353 | 0.312 | +0.059 | +0.018 | $2.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (16.26 vs 5.80 bp); despite a smaller raw edge (+0.080 vs +0.115/contract); relationships: KXNHLGOAL-26OCT13EDMLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT13EDMLA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: LAK offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (7.60 vs 3.07 bp); despite a smaller raw edge (+0.026 vs +0.103/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT13EDMLA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: LAK offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes; why: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (7.64 vs 7.04 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.012); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13EDMLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.084); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes; why: Player prop expression KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.50 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT13EDMLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT13EDMLA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.084); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4138): highest fidelity KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes — Player prop expression KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.50 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis LAK:OFFENSE_4PLUS (p 0.3679): highest fidelity KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes (same contract)
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3679, phi -0.251)
- KXNHLGOAL-26OCT13EDMLA-LAALEE47-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4138, phi -0.157)
- KXNHLGOAL-26OCT13EDMLA-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3893, phi -0.199)
- KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3893, phi -0.253)
- override: Player prop expression KXNHLAST-26OCT13EDMLA-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.50 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.15 (adj +0.61) on $15.00, P(profit) 0.7121, adj growth 5.6 bp · B EV +2.29 (adj +1.12) on $14.97, P(profit) 0.4908, adj growth 10.7 bp · C EV +4.06 (adj +1.03) on $18.76, P(profit) 0.7627, adj growth 9.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ SJS  ·  10000 joint draws  ·  536 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.467 / away 0.533

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BOS_win | p_overtime | goals | shots SJS/BOS | SJS/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 6.04 | 27.2/27.2 | 23.6/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.49 | 0.51 | 0.47 | 5.98 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.47 | 0.53 | 0.00 | 9.37 | 28.6/28.6 | 22.3/22.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.081 | 0.54 | 0.46 | 0.00 | 6.03 | 32.1/21.6 | 18.4/28.3 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.55 | 0.45 | 0.45 | 5.94 | 32.3/21.7 | 18.6/29.0 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.059 | 0.44 | 0.56 | 0.00 | 6.04 | 21.7/31.9 | 27.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 14 | 0.185 | 0.172 | +0.036 | +0.024 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Marat Khusnutdinov: 1+ goals YES | 11 | 0.148 | 0.137 | +0.031 | +0.020 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.215 | 0.203 | +0.035 | +0.023 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ goals NO | 74 | 0.791 | 0.777 | +0.038 | +0.024 | $8.54 | FUNDED_RESEARCH | $3 | BOS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13BOSSJ-BOSHLINDHOLM27-1|yes; why: higher confidence-adjusted growth (9.81 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: BOS offense suppressed (<= 2 goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes has the higher standalone adjusted growth (9.81 vs 8.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: BOS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (7.70 vs 5.38 bp); despite a smaller raw edge (+0.035 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.028); failure: SJS offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no; why: Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.90 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.028); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.401): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.385): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no — Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.90 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SJS:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.189)
- KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.171)
- KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3796, phi -0.207)
- KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.401, phi -0.213)
- override: Player prop expression KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no selected over player prop KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.90 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.59 (adj +0.78) on $15.00, P(profit) 0.6451, adj growth 7.4 bp · B EV +2.24 (adj +1.45) on $16.25, P(profit) 0.4243, adj growth 13.7 bp · C EV +4.50 (adj +1.56) on $22.61, P(profit) 0.7267, adj growth 14.8 bp · R EV +0.15 (adj +0.09) on $3.00, P(profit) 0.7912, adj growth 3.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
