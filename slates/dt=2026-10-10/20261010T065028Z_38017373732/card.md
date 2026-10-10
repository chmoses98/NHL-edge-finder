# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-10T06:50:28Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +26.57 | +8.30 | +25.86 | 0.699 | -36.36 | -51.74 | 70.96 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +23.59 | +10.02 | +19.31 | 0.668 | -33.04 | -46.98 | 89.19 |
| C best expression per thesis | 105.71 | +19.64 | +8.87 | +10.14 | 0.622 | -37.77 | -48.56 | 76.97 |
| R FUNDED research stakes | 37.00 | +6.05 | +2.13 | +4.62 | 0.653 | -9.77 | -13.43 | 0.00 |

## PHI @ BOS  ·  10000 joint draws  ·  220 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_PHI_win | p_overtime | goals | shots BOS/PHI | BOS/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 5.99 | 26.9/26.9 | 23.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.48 | 5.87 | 26.9/27.0 | 23.8/23.6 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.079 | 0.65 | 0.35 | 0.00 | 5.94 | 31.6/21.2 | 18.6/27.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.58 | 0.42 | 0.00 | 9.2 | 28.4/28.3 | 22.9/22.1 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.56 | 0.44 | 0.44 | 5.83 | 31.9/21.4 | 18.2/28.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.47 | 2.84 | 25.7/25.5 | 24.1/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 12 | 0.183 | 0.166 | +0.055 | +0.038 | $8.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 61 | 0.673 | 0.654 | +0.046 | +0.028 | $12.57 | FUNDED_RESEARCH | $4 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Travis Sanheim: 1+ goals YES | 7 | 0.098 | 0.088 | +0.023 | +0.014 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ goals NO | 74 | 0.790 | 0.775 | +0.036 | +0.021 | $14.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10PHIBOS-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (28.14 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: PHI offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (7.29 vs 5.38 bp); relationships: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense succeeds (4+ goals)
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (28.14 vs 6.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: PHI offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no has the higher standalone adjusted growth (7.29 vs 5.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BOS shot control · normal event (5-7) · decided (2+) 0.08.
- thesis PHI:OFFENSE_4PLUS (p 0.3107): highest fidelity KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.3883): highest fidelity KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10PHIBOS-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4679, phi -0.244)
- KXNHLGOAL-26OCT10PHIBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3862, phi -0.272)
- KXNHLGOAL-26OCT10PHIBOS-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4679, phi -0.161)
- KXNHLGOAL-26OCT10PHIBOS-BOSJPETERKA10-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3862, phi -0.211)

portfolios: A EV +3.79 (adj +2.48) on $20.83, P(profit) 0.2615, adj growth 23.0 bp · B EV +6.39 (adj +4.19) on $39.04, P(profit) 0.651, adj growth 36.8 bp · C EV +5.64 (adj +3.79) on $28.44, P(profit) 0.731, adj growth 32.5 bp · R EV +0.29 (adj +0.18) on $4.00, P(profit) 0.6727, adj growth 6.4 bp

## VAN @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_VAN_win | p_overtime | goals | shots NJD/VAN | NJD/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.135 | 0.65 | 0.35 | 0.00 | 5.98 | 34.1/21.9 | 19.2/29.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.54 | 0.46 | 0.47 | 5.91 | 34.3/22.0 | 18.9/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.56 | 0.44 | 0.00 | 6.0 | 28.5/27.6 | 24.2/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.50 | 0.50 | 0.46 | 5.92 | 28.5/27.6 | 24.3/25.2 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.090 | 0.64 | 0.36 | 0.00 | 9.2 | 35.8/23.2 | 18.3/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.55 | 0.45 | 0.00 | 9.34 | 29.8/29.0 | 23.0/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 2.5 goals YES | 7 | 0.137 | 0.101 | +0.062 | +0.026 | $2.28 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
| Vancouver wins by over 1.5 goals YES | 14 | 0.230 | 0.182 | +0.081 | +0.034 | $2.61 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 51 | 0.663 | 0.560 | +0.136 | +0.033 | $1.38 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 64 | 0.781 | 0.686 | +0.125 | +0.030 | $12.50 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT10VANNJ-VAN2|yes; why: higher confidence-adjusted growth (21.04 vs 19.48 bp); despite a smaller raw edge (+0.062 vs +0.081/contract); relationships: KXNHLSPREAD-26OCT10VANNJ-VAN2|yes: DUPLICATIVE (phi 0.728); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: REINFORCING (phi 0.284); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.211); failure: NJD wins (incl. OT/SO)
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 19.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.728); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes: DUPLICATIVE (phi 0.728); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: DUPLICATIVE (phi 0.389); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.289); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 9.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.284); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes: REINFORCING (phi 0.284); KXNHLSPREAD-26OCT10VANNJ-VAN2|yes: DUPLICATIVE (phi 0.389); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: DUPLICATIVE (phi 0.742); failure: NJD wins by 2+
- **New Jersey wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (21.04 vs 8.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.211); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes: REINFORCING (phi 0.211); KXNHLSPREAD-26OCT10VANNJ-VAN2|yes: REINFORCING (phi 0.289); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: DUPLICATIVE (phi 0.742); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.2297): highest fidelity KXNHLGAME-26OCT10VANNJ-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes (same contract)
- thesis VAN:WINS (p 0.4384): highest fidelity KXNHLGAME-26OCT10VANNJ-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3397): highest fidelity KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT10VANNJ-VAN3|yes: FUNDED_RESEARCH; family MIXED; loses 41% of the draws where the thesis happens; opposing: failure thesis NJD:WINS (p 0.5616, phi -0.45)
- KXNHLSPREAD-26OCT10VANNJ-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.5616, phi -0.618)
- KXNHLSPREAD-26OCT10VANNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.8 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3369, phi -1.0)
- KXNHLSPREAD-26OCT10VANNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.6 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3369, phi -0.742)
- override: override declined: the joint re-optimisation gives KXNHLGAME-26OCT10VANNJ-NJ|no less than the minimum stake; KXNHLSPREAD-26OCT10VANNJ-VAN3|yes kept

portfolios: A EV +5.79 (adj +1.35) on $20.83, P(profit) 0.5577, adj growth 11.9 bp · B EV +6.06 (adj +2.06) on $18.77, P(profit) 0.7812, adj growth 18.4 bp · C EV +4.15 (adj +1.75) on $4.98, P(profit) 0.1366, adj growth 15.0 bp · R EV +2.40 (adj +0.83) on $7.00, P(profit) 0.6631, adj growth 27.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10VANNJ-VAN|yes == KXNHLGAME-26OCT10VANNJ-NJ|no

## EDM @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_EDM_win | p_overtime | goals | shots SJS/EDM | SJS/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.118 | 0.48 | 0.52 | 0.00 | 9.53 | 29.1/29.5 | 23.1/23.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.49 | 0.51 | 0.00 | 6.1 | 27.5/27.8 | 24.1/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.49 | 0.51 | 0.48 | 6.02 | 27.6/28.0 | 24.5/24.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.092 | 0.42 | 0.58 | 0.00 | 6.07 | 21.7/32.8 | 28.6/18.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.083 | 0.40 | 0.60 | 0.00 | 9.45 | 23.5/35.1 | 27.7/18.3 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.46 | 0.54 | 0.47 | 6.05 | 22.1/33.2 | 29.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| San Jose over 3.5 goals scored YES | 38 | 0.449 | 0.409 | +0.052 | +0.013 | $4.67 | FUNDED_RESEARCH | $2 | SJS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **San Jose over 3.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10EDMSJ-SJ3|yes; why: higher confidence-adjusted growth (1.49 vs 1.21 bp); wins across more scripts (relative breadth 0.739 vs 0.475); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.439): highest fidelity KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4|yes (same contract)
- KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.3518, phi -0.664)

portfolios: A EV +1.09 (adj +0.27) on $8.33, P(profit) 0.4485, adj growth 2.1 bp · B EV +0.61 (adj +0.15) on $4.67, P(profit) 0.4485, adj growth 1.3 bp · C EV +0.67 (adj +0.17) on $5.14, P(profit) 0.4485, adj growth 1.4 bp · R EV +0.26 (adj +0.06) on $2.00, P(profit) 0.4485, adj growth 2.1 bp

## MIN @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_MIN_win | p_overtime | goals | shots FLA/MIN | FLA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.44 | 0.56 | 0.00 | 6.02 | 28.2/28.0 | 24.2/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.47 | 0.53 | 0.45 | 5.93 | 28.1/27.9 | 24.5/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.46 | 0.54 | 0.00 | 9.37 | 29.8/29.5 | 23.1/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.52 | 0.48 | 0.00 | 6.0 | 33.1/22.4 | 19.0/29.3 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.54 | 0.46 | 0.45 | 5.91 | 33.2/22.5 | 19.4/29.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.055 | 0.46 | 0.54 | 0.49 | 5.9 | 22.9/33.2 | 29.8/19.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins YES | 45 | 0.526 | 0.486 | +0.059 | +0.018 | $5.35 | FUNDED_RESEARCH | $2 | MIN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 68 | 0.745 | 0.710 | +0.050 | +0.015 | $6.13 | FUNDED_RESEARCH | $2 | MIN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 42 | 0.485 | 0.450 | +0.048 | +0.013 | $5.22 | FUNDED_RESEARCH | $2 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins YES** — thesis: MIN wins (incl. OT/SO); alternative: KXNHLGAME-26OCT10MINFLA-FLA|no; why: best adjusted growth among the thesis's expressions; relationships: KXNHLSPREAD-26OCT10MINFLA-FLA2|no: DUPLICATIVE (phi 0.617); KXNHLTOTAL-26OCT10MINFLA-7|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 1.5 goals NO** — thesis: MIN wins (incl. OT/SO); alternative: KXNHLGAME-26OCT10MINFLA-FLA|no; why: KXNHLGAME-26OCT10MINFLA-FLA|no has the higher standalone adjusted growth (2.98 vs 2.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.617); relationships: KXNHLGAME-26OCT10MINFLA-MIN|yes: DUPLICATIVE (phi 0.617); KXNHLTOTAL-26OCT10MINFLA-7|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: FLA wins by 2+
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes; why: KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes has the higher standalone adjusted growth (2.27 vs 1.44 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.456); relationships: KXNHLGAME-26OCT10MINFLA-MIN|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLSPREAD-26OCT10MINFLA-FLA2|no: MOSTLY_INDEPENDENT (phi -0.017); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:WINS (p 0.5265): highest fidelity KXNHLGAME-26OCT10MINFLA-MIN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10MINFLA-MIN|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.4175): highest fidelity KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10MINFLA-MIN|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:WINS_BY_2PLUS (p 0.3034): highest fidelity KXNHLGAME-26OCT10MINFLA-MIN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10MINFLA-MIN|yes (same contract)
- KXNHLGAME-26OCT10MINFLA-MIN|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.4735, phi -1.0)
- KXNHLSPREAD-26OCT10MINFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.255, phi -1.0)
- KXNHLTOTAL-26OCT10MINFLA-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:SUPPRESSED (p 0.4023, phi -0.524)

portfolios: A EV +2.55 (adj +0.72) on $20.83, P(profit) 0.5733, adj growth 5.6 bp · B EV +1.69 (adj +0.49) on $16.71, P(profit) 0.6331, adj growth 4.4 bp · C EV +0.99 (adj +0.25) on $5.86, P(profit) 0.4279, adj growth 2.2 bp · R EV +0.61 (adj +0.18) on $6.00, P(profit) 0.6331, adj growth 6.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10MINFLA-FLA|no == KXNHLGAME-26OCT10MINFLA-MIN|yes

## UTA @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_UTA_win | p_overtime | goals | shots BUF/UTA | BUF/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.54 | 0.46 | 0.00 | 6.03 | 27.7/27.6 | 24.1/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.47 | 5.98 | 27.3/27.2 | 23.8/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.50 | 0.50 | 0.00 | 9.36 | 28.9/29.0 | 22.8/22.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.082 | 0.58 | 0.42 | 0.00 | 6.03 | 32.4/21.8 | 18.6/28.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.55 | 0.45 | 0.46 | 5.93 | 32.1/21.7 | 18.5/28.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.062 | 0.45 | 0.55 | 0.00 | 5.99 | 21.7/31.7 | 27.6/18.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_DET_win | p_overtime | goals | shots MTL/DET | MTL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.64 | 0.36 | 0.00 | 5.99 | 26.9/27.4 | 24.5/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.49 | 5.95 | 27.4/27.7 | 24.4/23.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.095 | 0.59 | 0.41 | 0.00 | 5.96 | 21.7/32.7 | 29.6/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.66 | 0.34 | 0.00 | 9.29 | 28.7/29.0 | 23.8/21.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.50 | 0.50 | 0.48 | 5.83 | 21.8/32.7 | 29.3/18.7 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 9.18 | 23.3/34.7 | 29.0/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Montreal wins by over 2.5 goals NO | 70 | 0.762 | 0.729 | +0.047 | +0.014 | $11.89 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Montreal wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT10DETMTL-MTL2|no; why: higher confidence-adjusted growth (2.05 vs 0.98 bp); wins across more scripts (relative breadth 0.995 vs 0.873); relationships: only recommended bet in this game; failure: MTL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4331): highest fidelity KXNHLSPREAD-26OCT10DETMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DETMTL-MTL3|no (same contract)
- KXNHLSPREAD-26OCT10DETMTL-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3601, phi -0.745)

portfolios: A EV +1.15 (adj +0.31) on $16.67, P(profit) 0.6399, adj growth 2.5 bp · B EV +0.79 (adj +0.23) on $11.89, P(profit) 0.762, adj growth 2.0 bp · C EV +0.87 (adj +0.25) on $13.09, P(profit) 0.762, adj growth 2.2 bp · R EV +0.20 (adj +0.06) on $3.00, P(profit) 0.762, adj growth 2.1 bp

## NSH @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NSH_win | p_overtime | goals | shots OTT/NSH | OTT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.130 | 0.68 | 0.32 | 0.00 | 5.99 | 33.7/21.7 | 19.1/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.60 | 0.40 | 0.00 | 6.01 | 28.3/27.6 | 24.5/24.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.55 | 0.45 | 0.47 | 5.97 | 34.0/22.3 | 19.1/30.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.53 | 0.47 | 0.47 | 5.89 | 28.4/27.7 | 24.5/25.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.090 | 0.71 | 0.29 | 0.00 | 9.29 | 35.3/23.2 | 18.6/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.63 | 0.37 | 0.00 | 9.38 | 29.9/29.2 | 23.7/22.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_DAL_win | p_overtime | goals | shots PIT/DAL | PIT/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.04 | 26.6/26.5 | 23.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.47 | 5.96 | 26.4/26.4 | 23.1/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.55 | 0.45 | 0.00 | 9.38 | 28.4/28.1 | 22.3/21.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 6.03 | 31.2/20.7 | 17.8/27.0 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.53 | 0.47 | 0.48 | 5.98 | 31.2/20.8 | 17.7/27.9 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.060 | 0.67 | 0.33 | 0.00 | 9.35 | 32.9/22.3 | 17.5/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pittsburgh wins by over 1.5 goals YES | 23 | 0.319 | 0.272 | +0.076 | +0.029 | $4.72 | FUNDED_RESEARCH | $2 | PIT:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 2.5 goals YES | 14 | 0.205 | 0.170 | +0.057 | +0.021 | $1.43 | FUNDED_RESEARCH | $1 | PIT:WINS_BY_2PLUS | DIRECT (0.64) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 77 | 0.850 | 0.805 | +0.067 | +0.022 | $18.16 | FUNDED_RESEARCH | $5 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh over 2.5 goals scored YES | 58 | 0.666 | 0.618 | +0.069 | +0.021 | $1.59 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Pittsburgh wins by over 1.5 goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT10DALPIT-PIT3|yes; why: higher confidence-adjusted growth (10.16 vs 7.91 bp); relationships: KXNHLSPREAD-26OCT10DALPIT-PIT3|yes: DUPLICATIVE (phi 0.743); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: REINFORCING (phi 0.287); KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes: DUPLICATIVE (phi 0.449); failure: DAL wins (incl. OT/SO)
- **Pittsburgh wins by over 2.5 goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes has the higher standalone adjusted growth (10.16 vs 7.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.743); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: DUPLICATIVE (phi 0.743); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: REINFORCING (phi 0.213); KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes: DUPLICATIVE (phi 0.359); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes has the higher standalone adjusted growth (10.16 vs 6.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.287); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: REINFORCING (phi 0.287); KXNHLSPREAD-26OCT10DALPIT-PIT3|yes: REINFORCING (phi 0.213); KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes: REINFORCING (phi 0.392); failure: DAL wins by 2+
- **Pittsburgh over 2.5 goals scored YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes has the higher standalone adjusted growth (10.16 vs 4.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.449); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: DUPLICATIVE (phi 0.449); KXNHLSPREAD-26OCT10DALPIT-PIT3|yes: DUPLICATIVE (phi 0.359); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: REINFORCING (phi 0.392); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3185): highest fidelity KXNHLSPREAD-26OCT10DALPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DALPIT-PIT2|yes (same contract)
- thesis PIT:WINS (p 0.5407): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DALPIT-PIT2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4338): highest fidelity KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10DALPIT-PIT2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT10DALPIT-PIT2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4593, phi -0.63)
- KXNHLSPREAD-26OCT10DALPIT-PIT3|yes: FUNDED_RESEARCH; family MIXED; loses 36% of the draws where the thesis happens; opposing: failure thesis DAL:WINS (p 0.4593, phi -0.468)
- KXNHLSPREAD-26OCT10DALPIT-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2467, phi -0.735)
- KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:SUPPRESSED (p 0.3437, phi -0.978)
- override: override declined: the joint re-optimisation gives KXNHLGAME-26OCT10DALPIT-DAL|no less than the minimum stake; KXNHLSPREAD-26OCT10DALPIT-PIT3|yes kept

portfolios: A EV +4.24 (adj +1.24) on $20.83, P(profit) 0.4988, adj growth 10.5 bp · B EV +3.78 (adj +1.36) on $25.91, P(profit) 0.3185, adj growth 12.1 bp · C EV +2.72 (adj +1.05) on $8.65, P(profit) 0.3185, adj growth 9.1 bp · R EV +1.55 (adj +0.57) on $9.00, P(profit) 0.3185, adj growth 18.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10DALPIT-PIT|yes == KXNHLGAME-26OCT10DALPIT-DAL|no

## CAR @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_CAR_win | p_overtime | goals | shots CHI/CAR | CHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.170 | 0.33 | 0.67 | 0.00 | 6.04 | 20.4/33.4 | 28.8/17.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.141 | 0.46 | 0.54 | 0.47 | 5.89 | 20.7/33.8 | 30.4/17.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.124 | 0.31 | 0.69 | 0.00 | 9.29 | 21.9/35.2 | 27.4/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.083 | 0.40 | 0.60 | 0.00 | 6.04 | 26.0/27.2 | 23.1/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.51 | 0.49 | 0.47 | 5.95 | 26.0/27.0 | 23.6/22.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.075 | 0.36 | 0.64 | 0.00 | 3.49 | 19.6/32.4 | 30.1/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Chicago over 3.5 goals scored YES | 26 | 0.346 | 0.298 | +0.073 | +0.025 | $2.23 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 67 | 0.750 | 0.708 | +0.065 | +0.022 | $8.11 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Chicago over 3.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR3|no; why: higher confidence-adjusted growth (6.66 vs 5.01 bp); relationships: KXNHLSPREAD-26OCT10CARCHI-CAR3|no: REINFORCING (phi 0.355); failure: CHI offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT10CARCHI-CAR2|no; why: higher confidence-adjusted growth (5.01 vs 2.36 bp); despite a smaller raw edge (+0.065 vs +0.088/contract); wins across more scripts (relative breadth 1.035 vs 0.917); relationships: KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes: REINFORCING (phi 0.355); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.3362): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes (same contract)
- thesis CHI:WINS (p 0.409): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2073): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CHI:SUPPRESSED (p 0.4513, phi -0.66)
- KXNHLSPREAD-26OCT10CARCHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3642, phi -0.762)

portfolios: A EV +4.77 (adj +1.19) on $20.83, P(profit) 0.486, adj growth 9.0 bp · B EV +1.36 (adj +0.46) on $10.34, P(profit) 0.7503, adj growth 4.4 bp · C EV +2.86 (adj +0.97) on $19.55, P(profit) 0.7636, adj growth 8.5 bp · R EV +0.55 (adj +0.19) on $4.00, P(profit) 0.7503, adj growth 6.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10CARCHI-CHI|yes == KXNHLGAME-26OCT10CARCHI-CAR|no

## CBJ @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CBJ_win | p_overtime | goals | shots STL/CBJ | STL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.54 | 0.46 | 0.00 | 6.0 | 26.8/27.0 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.50 | 5.86 | 27.0/27.3 | 24.0/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.58 | 0.42 | 0.00 | 9.24 | 28.5/28.9 | 23.4/22.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.077 | 0.49 | 0.51 | 0.00 | 5.96 | 21.5/32.4 | 28.6/18.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.47 | 0.53 | 0.45 | 5.83 | 21.5/32.1 | 28.7/18.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.52 | 0.48 | 0.00 | 3.47 | 25.6/25.9 | 24.1/23.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TOR_win | p_overtime | goals | shots COL/TOR | COL/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.188 | 0.77 | 0.23 | 0.00 | 6.04 | 36.8/22.1 | 19.8/31.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.157 | 0.78 | 0.22 | 0.00 | 9.35 | 38.5/23.6 | 19.5/29.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.139 | 0.58 | 0.42 | 0.48 | 5.96 | 37.1/22.6 | 19.4/33.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.079 | 0.73 | 0.27 | 0.00 | 6.01 | 30.2/28.7 | 26.1/25.5 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.073 | 0.73 | 0.27 | 0.00 | 3.45 | 35.6/21.2 | 20.1/33.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.39 | 31.7/30.3 | 25.4/23.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.19, COL shot control · high event (8+) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.14.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_TBL_win | p_overtime | goals | shots NYI/TBL | NYI/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 6.0 | 26.6/26.9 | 23.7/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.50 | 0.50 | 0.49 | 5.93 | 27.1/27.2 | 23.9/23.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.45 | 0.55 | 0.00 | 5.94 | 21.6/31.7 | 27.9/18.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.52 | 0.48 | 0.00 | 9.15 | 28.4/28.4 | 22.6/22.6 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.47 | 0.53 | 0.47 | 5.82 | 21.6/32.0 | 28.4/18.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.51 | 2.83 | 25.5/25.6 | 24.2/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.840 | 0.798 | +0.068 | +0.025 | $18.16 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I wins by over 1.5 goals YES | 21 | 0.287 | 0.246 | +0.065 | +0.024 | $4.51 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes; why: higher confidence-adjusted growth (7.79 vs 7.41 bp); wins across more scripts (relative breadth 0.997 vs 0.529); relationships: KXNHLSPREAD-26OCT10TBNYI-NYI2|yes: REINFORCING (phi 0.276); failure: TBL wins by 2+
- **New York I wins by over 1.5 goals YES** — thesis: NYI wins by 2+; alternative: KXNHLSPREAD-26OCT10TBNYI-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT10TBNYI-TB3|no has the higher standalone adjusted growth (7.79 vs 7.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.276); they share one thesis budget; relationships: KXNHLSPREAD-26OCT10TBNYI-TB3|no: REINFORCING (phi 0.276); failure: TBL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:WINS (p 0.5144): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10TBNYI-TB3|no (same contract)
- thesis NYI:WINS_BY_2PLUS (p 0.2868): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10TBNYI-TB3|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3603): highest fidelity KXNHLTEAMTOTAL-26OCT10TBNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10TBNYI-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT10TBNYI-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.265, phi -0.726)
- KXNHLSPREAD-26OCT10TBNYI-NYI2|yes: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.4856, phi -0.616)

portfolios: A EV +3.19 (adj +0.74) on $20.83, P(profit) 0.5144, adj growth 6.4 bp · B EV +2.91 (adj +1.08) on $22.67, P(profit) 0.8403, adj growth 9.8 bp · C EV +1.75 (adj +0.64) on $20.00, P(profit) 0.8403, adj growth 6.0 bp · R EV +0.17 (adj +0.06) on $2.00, P(profit) 0.8403, adj growth 2.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10TBNYI-TB|no == KXNHLGAME-26OCT10TBNYI-NYI|yes

## ANA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.48 | 0.52 | 0.00 | 6.06 | 28.7/29.2 | 25.4/25.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.110 | 0.43 | 0.57 | 0.00 | 6.04 | 22.5/34.6 | 30.6/19.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.48 | 0.52 | 0.47 | 6.03 | 28.7/29.2 | 25.7/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.46 | 0.54 | 0.00 | 9.4 | 30.0/30.8 | 24.2/24.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.47 | 0.53 | 0.45 | 5.98 | 22.7/34.5 | 31.0/19.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.080 | 0.38 | 0.62 | 0.00 | 9.28 | 24.2/36.3 | 28.8/19.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## LAK @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_LAK_win | p_overtime | goals | shots VGK/LAK | VGK/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.62 | 0.38 | 0.00 | 6.0 | 27.5/27.1 | 23.9/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.50 | 0.50 | 0.47 | 5.87 | 27.4/27.1 | 23.9/24.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.090 | 0.67 | 0.33 | 0.00 | 5.99 | 32.5/21.6 | 18.9/28.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.60 | 0.40 | 0.48 | 5.86 | 32.6/21.6 | 18.6/29.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.63 | 0.37 | 0.00 | 9.18 | 28.8/28.8 | 23.5/22.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.62 | 0.38 | 0.00 | 3.42 | 26.2/26.0 | 24.5/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, VGK shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
