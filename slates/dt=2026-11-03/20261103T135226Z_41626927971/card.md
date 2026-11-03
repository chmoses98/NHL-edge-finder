# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-03T13:52:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +29.38 | +10.51 | +25.26 | 0.709 | -30.15 | -44.38 | 93.09 |
| B thesis-diversified (joint) ← optimiser card | 149.15 | +26.19 | +14.83 | +22.33 | 0.667 | -39.47 | -53.43 | 134.20 |
| C best expression per thesis | 150.00 | +31.84 | +15.02 | +26.02 | 0.666 | -45.86 | -62.40 | 129.98 |
| R FUNDED research stakes | 26.00 | +3.59 | +1.69 | +1.33 | 0.536 | -9.40 | -10.65 | 0.00 |

## UTA @ TOR  ·  10000 joint draws  ·  430 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_UTA_win | p_overtime | goals | shots TOR/UTA | TOR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.50 | 0.50 | 0.00 | 6.1 | 28.3/28.8 | 25.1/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.53 | 0.47 | 0.00 | 9.54 | 30.2/30.7 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.49 | 5.97 | 28.4/28.9 | 25.6/25.0 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.099 | 0.48 | 0.52 | 0.00 | 6.06 | 22.5/34.4 | 30.6/19.1 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.46 | 0.54 | 0.49 | 5.98 | 22.8/34.6 | 31.0/19.5 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.085 | 0.42 | 0.58 | 0.00 | 9.47 | 24.4/36.5 | 29.0/19.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.183 | 0.161 | +0.067 | +0.044 | $7.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 17 | 0.223 | 0.206 | +0.043 | +0.026 | $5.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 11 | 0.148 | 0.135 | +0.031 | +0.018 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.688 | 0.673 | +0.032 | +0.017 | $9.37 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV03UTATOR-TORMRIELLY44-1|yes; why: higher confidence-adjusted growth (40.33 vs 0.66 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: TOR offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes; why: higher confidence-adjusted growth (10.21 vs 1.72 bp); relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes has the higher standalone adjusted growth (10.21 vs 6.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03UTATOR-UTA2|no; why: higher confidence-adjusted growth (2.88 vs 0.66 bp); despite a smaller raw edge (+0.032 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.4359): highest fidelity KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4429): highest fidelity KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3505): highest fidelity KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no (same contract)
- KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3495, phi -0.196)
- KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3505, phi -0.2)
- KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3505, phi -0.173)
- KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4429, phi -0.241)

portfolios: A EV +5.91 (adj +3.77) on $20.88, P(profit) 0.4651, adj growth 34.4 bp · B EV +7.02 (adj +4.47) on $25.80, P(profit) 0.4651, adj growth 40.2 bp · C EV +8.66 (adj +5.59) on $31.63, P(profit) 0.3717, adj growth 47.9 bp · R EV +0.14 (adj +0.08) on $3.00, P(profit) 0.6878, adj growth 2.8 bp

## WPG @ MTL  ·  10000 joint draws  ·  366 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_WPG_win | p_overtime | goals | shots MTL/WPG | MTL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.64 | 0.36 | 0.00 | 6.02 | 27.1/27.1 | 24.1/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.47 | 5.92 | 27.1/27.1 | 23.9/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.63 | 0.37 | 0.00 | 9.26 | 28.7/28.7 | 23.3/21.8 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.075 | 0.67 | 0.33 | 0.00 | 5.95 | 31.7/21.2 | 18.5/27.2 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.067 | 0.56 | 0.44 | 0.00 | 6.01 | 21.6/31.7 | 28.4/18.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.44 | 0.56 | 0.46 | 5.9 | 21.8/32.3 | 29.0/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Winnipeg over 5.5 goals scored YES | 4 | 0.073 | 0.054 | +0.030 | +0.011 | $1.48 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.25) | EVIDENCE_MIXED | D |
| Jake Evans: 1+ goals YES | 15 | 0.188 | 0.175 | +0.029 | +0.016 | $3.20 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Winnipeg over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG5|yes; why: higher confidence-adjusted growth (6.59 vs 0.79 bp); despite a smaller raw edge (+0.030 vs +0.031/contract); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03WPGMTL-MTLJEVANS71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.019); failure: MTL wins (incl. OT/SO)
- **Jake Evans: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (4.21 vs 1.39 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes: INTENTIONAL_DIVERSIFIER (phi -0.019); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis GAME:HIGH_EVENT (p 0.2668): highest fidelity KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes [FRAGILE], best adjusted EV KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.444): highest fidelity KXNHLGOAL-26NOV03WPGMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03WPGMTL-MTLJEVANS71-1|yes (same contract)
- KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes: FUNDED_RESEARCH; family MIXED; loses 75% of the draws where the thesis happens; opposing: failure thesis MTL:WINS (p 0.5747, phi -0.295)
- KXNHLGOAL-26NOV03WPGMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.347, phi -0.224)

portfolios: A EV +3.01 (adj +1.24) on $6.95, P(profit) 0.2495, adj growth 10.1 bp · B EV +1.64 (adj +0.72) on $4.68, P(profit) 0.2495, adj growth 6.5 bp · C EV +2.29 (adj +1.00) on $6.55, P(profit) 0.2495, adj growth 8.7 bp · R EV +0.71 (adj +0.26) on $1.00, P(profit) 0.0729, adj growth 7.7 bp

## DET @ TBL  ·  10000 joint draws  ·  404 bet sides mapped, 8 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.64 | 0.36 | 0.00 | 5.98 | 27.2/26.9 | 24.0/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.46 | 5.92 | 27.3/27.0 | 23.6/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.70 | 0.30 | 0.00 | 9.22 | 29.1/28.7 | 23.9/21.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.73 | 0.27 | 0.00 | 6.02 | 32.4/21.6 | 19.2/27.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.59 | 0.41 | 0.48 | 5.92 | 32.4/21.5 | 18.5/28.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.061 | 0.73 | 0.27 | 0.00 | 9.25 | 34.1/22.9 | 18.8/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 88 | 0.925 | 0.910 | +0.037 | +0.022 | $14.03 | FUNDED_RESEARCH | $4 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 31 | 0.361 | 0.347 | +0.036 | +0.022 | $4.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 66 | 0.738 | 0.694 | +0.062 | +0.018 | $7.69 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (11.28 vs 3.60 bp); despite a smaller raw edge (+0.037 vs +0.105/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV03DETTB-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26NOV03DETTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.073); failure: TBL offense succeeds (4+ goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03DETTB-DET5|yes; why: higher confidence-adjusted growth (4.82 vs 3.46 bp); despite a smaller raw edge (+0.036 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.941 vs 0.556); relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26NOV03DETTB-TB3|no: REINFORCING (phi 0.178); failure: DET offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB2|no; why: Broad expression KXNHLSPREAD-26NOV03DETTB-TB3|no selected over player prop KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.073); KXNHLGOAL-26NOV03DETTB-DETADEBRINCAT93-1|yes: REINFORCING (phi 0.178); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3019): highest fidelity KXNHLTEAMTOTAL-26NOV03DETTB-DET4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03DETTB-DETADEBRINCAT93-1|yes — Broad expression KXNHLTEAMTOTAL-26NOV03DETTB-DET4|yes selected over broad KXNHLTEAMTOTAL-26NOV03DETTB-DET5|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.51 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis TBL:SUPPRESSED (p 0.3221): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no — Broad expression KXNHLSPREAD-26NOV03DETTB-TB3|no selected over player prop KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4306): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03DETTB-TB3|no (same contract)
- KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4658, phi -0.108)
- KXNHLGOAL-26NOV03DETTB-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4817, phi -0.302)
- KXNHLSPREAD-26NOV03DETTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3838, phi -0.755)
- override: Broad expression KXNHLSPREAD-26NOV03DETTB-TB3|no selected over player prop KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26NOV03DETTB-DET4|yes selected over broad KXNHLTEAMTOTAL-26NOV03DETTB-DET5|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.51 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.37 (adj +0.64) on $20.88, P(profit) 0.6841, adj growth 5.6 bp · B EV +1.82 (adj +0.88) on $26.39, P(profit) 0.741, adj growth 8.3 bp · C EV +3.38 (adj +1.06) on $22.83, P(profit) 0.5593, adj growth 9.3 bp · R EV +0.35 (adj +0.16) on $6.00, P(profit) 0.6911, adj growth 6.0 bp

## STL @ NYR  ·  10000 joint draws  ·  382 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_STL_win | p_overtime | goals | shots NYR/STL | NYR/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.04 | 26.7/26.7 | 23.4/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.49 | 5.94 | 26.7/26.7 | 23.4/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.55 | 0.45 | 0.00 | 9.31 | 28.5/28.4 | 22.9/22.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.072 | 0.63 | 0.37 | 0.00 | 6.04 | 31.4/21.3 | 18.5/27.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.48 | 0.52 | 0.00 | 6.0 | 21.4/31.7 | 27.9/18.1 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.48 | 5.88 | 31.6/21.4 | 18.3/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tye Kartye: 1+ goals YES | 16 | 0.197 | 0.184 | +0.028 | +0.015 | $2.89 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03STLNYR-NYRJMILLER8-1|yes; why: higher confidence-adjusted growth (3.25 vs 0.72 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4118): highest fidelity KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes (same contract)
- KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3717, phi -0.202)

portfolios: A EV +0.56 (adj +0.30) on $3.46, P(profit) 0.1969, adj growth 2.6 bp · B EV +0.47 (adj +0.25) on $2.89, P(profit) 0.1969, adj growth 2.2 bp · C EV +0.66 (adj +0.35) on $4.04, P(profit) 0.1969, adj growth 3.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ PHI  ·  10000 joint draws  ·  412 bet sides mapped, 18 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_MIN_win | p_overtime | goals | shots PHI/MIN | PHI/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 5.97 | 27.1/27.5 | 24.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.46 | 5.88 | 27.1/27.4 | 24.2/23.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.092 | 0.47 | 0.53 | 0.00 | 5.94 | 21.7/32.7 | 28.9/18.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.48 | 0.52 | 0.48 | 5.87 | 21.7/32.8 | 29.4/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.54 | 0.46 | 0.00 | 9.2 | 28.8/29.1 | 23.4/22.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.48 | 2.74 | 25.7/26.0 | 24.5/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Philadelphia wins by over 1.5 goals YES | 20 | 0.289 | 0.242 | +0.078 | +0.031 | $4.32 | FUNDED_RESEARCH | $2 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nick Seeler: 1+ goals YES | 3 | 0.047 | 0.045 | +0.015 | +0.013 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 63 | 0.687 | 0.670 | +0.040 | +0.024 | $9.68 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 17 | 0.214 | 0.199 | +0.034 | +0.019 | $3.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26NOV03MINPHI-PHI3|yes; why: higher confidence-adjusted growth (12.30 vs 7.95 bp); relationships: KXNHLGOAL-26NOV03MINPHI-PHINSEELER24-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: REINFORCING (phi 0.167); KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.149); failure: MIN wins (incl. OT/SO)
- **Nick Seeler: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.30 vs 11.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.111); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: PHI offense suppressed (<= 2 goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.30 vs 5.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.167); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.167); KXNHLGOAL-26NOV03MINPHI-PHINSEELER24-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: MIN offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.30 vs 5.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.149); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26NOV03MINPHI-PHINSEELER24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26NOV03MINPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3697): highest fidelity KXNHLTEAMTOTAL-26NOV03MINPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4415): highest fidelity KXNHLSPREAD-26NOV03MINPHI-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4788, phi -0.611)
- KXNHLGOAL-26NOV03MINPHI-PHINSEELER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4132, phi -0.104)
- KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3363, phi -0.272)
- KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4132, phi -0.217)

portfolios: A EV +4.62 (adj +0.70) on $20.88, P(profit) 0.5958, adj growth 6.1 bp · B EV +3.76 (adj +2.17) on $19.34, P(profit) 0.3853, adj growth 19.5 bp · C EV +3.07 (adj +1.21) on $8.33, P(profit) 0.289, adj growth 10.6 bp · R EV +0.92 (adj +0.40) on $5.00, P(profit) 0.289, adj growth 14.0 bp
equivalent contracts collapsed: KXNHLGAME-26NOV03MINPHI-MIN|no == KXNHLGAME-26NOV03MINPHI-PHI|yes

## VGK @ PIT  ·  10000 joint draws  ·  400 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_VGK_win | p_overtime | goals | shots PIT/VGK | PIT/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.48 | 0.52 | 0.00 | 6.04 | 27.2/27.4 | 23.8/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.46 | 5.98 | 27.2/27.3 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.48 | 0.52 | 0.00 | 9.29 | 28.8/28.9 | 22.9/22.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.068 | 0.54 | 0.46 | 0.00 | 5.99 | 32.2/21.7 | 18.6/28.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.062 | 0.40 | 0.60 | 0.00 | 6.03 | 22.0/32.3 | 27.9/18.9 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.55 | 0.45 | 0.47 | 5.96 | 32.6/21.9 | 18.7/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.165 | 0.154 | +0.027 | +0.016 | $3.05 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ assists NO | 54 | 0.618 | 0.571 | +0.060 | +0.014 | $5.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV03VGKPIT-3|yes; why: higher confidence-adjusted growth (4.56 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: MOSTLY_INDEPENDENT (phi -0.019); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV03VGKPIT-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (1.71 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4032): highest fidelity KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.3774): highest fidelity KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no (same contract)
- KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3774, phi -0.204)
- KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4032, phi -0.269)

portfolios: A EV +1.54 (adj +0.58) on $11.63, P(profit) 0.6841, adj growth 5.2 bp · B EV +1.23 (adj +0.49) on $8.87, P(profit) 0.6841, adj growth 4.5 bp · C EV +1.72 (adj +0.69) on $12.40, P(profit) 0.6841, adj growth 6.0 bp · R EV +0.20 (adj +0.11) on $1.00, P(profit) 0.165, adj growth 4.0 bp

## DAL @ WSH  ·  10000 joint draws  ·  402 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_DAL_win | p_overtime | goals | shots WSH/DAL | WSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.56 | 0.44 | 0.00 | 5.98 | 25.9/26.0 | 22.8/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.96 | 26.1/26.2 | 23.0/22.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.60 | 0.40 | 0.00 | 9.35 | 27.6/27.7 | 22.2/20.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.50 | 0.50 | 0.00 | 5.95 | 20.7/30.8 | 27.1/17.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.47 | 0.53 | 0.46 | 5.86 | 20.6/30.8 | 27.5/17.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.062 | 0.65 | 0.35 | 0.00 | 6.02 | 30.4/20.8 | 18.1/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.235 | 0.219 | +0.045 | +0.029 | $5.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Miro Heiskanen: 1+ goals NO | 87 | 0.904 | 0.893 | +0.026 | +0.015 | $14.03 | FUNDED_RESEARCH | $4 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 12 | 0.151 | 0.142 | +0.024 | +0.015 | $2.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Alex Ovechkin: 1+ goals YES | 22 | 0.257 | 0.247 | +0.025 | +0.015 | $3.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03DALWSH-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (11.49 vs 2.64 bp); relationships: KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26NOV03DALWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: WSH offense suppressed (<= 2 goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DALWSH-DALMHEISKANEN4-1|no; why: higher confidence-adjusted growth (4.80 vs 1.15 bp); despite a smaller raw edge (+0.026 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV03DALWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: DAL offense succeeds (4+ goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV03DALWSH-2|yes; why: higher confidence-adjusted growth (4.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV03DALWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: DAL offense suppressed (<= 2 goals)
- **Alex Ovechkin: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.49 vs 2.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis WSH:OFFENSE_4PLUS (p 0.4079): highest fidelity KXNHLGOAL-26NOV03DALWSH-WSHAOVECHKIN8-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:OFFENSE_4PLUS (p 0.3461): highest fidelity KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4333): highest fidelity KXNHLAST-26NOV03DALWSH-DALMHEISKANEN4-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV03DALWSH-DALMHEISKANEN4-1|no (same contract)
- KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.38, phi -0.234)
- KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3461, phi -0.157)
- KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.4333, phi -0.199)
- KXNHLGOAL-26NOV03DALWSH-WSHAOVECHKIN8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.38, phi -0.229)

portfolios: A EV +2.21 (adj +1.13) on $20.88, P(profit) 0.3518, adj growth 10.4 bp · B EV +2.71 (adj +1.67) on $26.10, P(profit) 0.4967, adj growth 15.3 bp · C EV +3.34 (adj +1.86) on $19.28, P(profit) 0.3556, adj growth 16.1 bp · R EV +0.12 (adj +0.07) on $4.00, P(profit) 0.9042, adj growth 2.6 bp

## COL @ CBJ  ·  10000 joint draws  ·  408 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_COL_win | p_overtime | goals | shots CBJ/COL | CBJ/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.46 | 0.54 | 0.00 | 6.01 | 28.0/28.4 | 24.6/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.45 | 5.94 | 28.1/28.5 | 25.3/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.47 | 0.53 | 0.00 | 9.34 | 29.5/29.9 | 23.8/23.4 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.091 | 0.38 | 0.62 | 0.00 | 6.0 | 22.2/33.9 | 29.8/19.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.43 | 0.57 | 0.46 | 5.87 | 22.6/34.1 | 30.5/19.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.059 | 0.39 | 0.61 | 0.00 | 9.22 | 23.5/35.2 | 28.2/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Monahan: 1+ goals YES | 15 | 0.180 | 0.172 | +0.021 | +0.013 | $2.52 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (2.59 vs 0.22 bp); alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3645): highest fidelity KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes (same contract)
- KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4172, phi -0.211)

portfolios: A EV +0.36 (adj +0.21) on $2.67, P(profit) 0.1804, adj growth 1.9 bp · B EV +0.34 (adj +0.20) on $2.52, P(profit) 0.1804, adj growth 1.8 bp · C EV +0.48 (adj +0.28) on $3.52, P(profit) 0.1804, adj growth 2.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ NJD  ·  10000 joint draws  ·  410 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_EDM_win | p_overtime | goals | shots NJD/EDM | NJD/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.50 | 0.50 | 0.00 | 6.03 | 28.0/27.7 | 24.1/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.51 | 0.49 | 0.00 | 9.5 | 29.8/29.6 | 23.4/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.44 | 5.95 | 28.3/27.9 | 24.6/25.0 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.096 | 0.54 | 0.46 | 0.00 | 6.01 | 33.6/22.0 | 18.9/29.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.50 | 0.50 | 0.46 | 6.02 | 33.6/22.5 | 19.3/30.2 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 9.4 | 35.5/23.5 | 18.1/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 11 | 0.156 | 0.142 | +0.039 | +0.025 | $4.58 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 23 | 0.288 | 0.269 | +0.046 | +0.026 | $5.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 9 | 0.129 | 0.112 | +0.033 | +0.016 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.114 | 0.099 | +0.029 | +0.014 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (13.35 vs 8.28 bp); despite a smaller raw edge (+0.039 vs +0.046/contract); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV03EDMNJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes; why: higher confidence-adjusted growth (8.28 vs 4.48 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.881 vs 0.331); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03EDMNJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.028); failure: EDM offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (8.28 vs 6.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03EDMNJ-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (8.28 vs 5.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4208): highest fidelity KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS_BY_2PLUS (p 0.2823): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3153): highest fidelity KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes (same contract)
- KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3635, phi -0.179)
- KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3635, phi -0.252)
- KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3635, phi -0.155)
- KXNHLGOAL-26NOV03EDMNJ-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3635, phi -0.16)

portfolios: A EV +4.43 (adj +1.07) on $20.88, P(profit) 0.5355, adj growth 9.2 bp · B EV +4.28 (adj +2.41) on $15.02, P(profit) 0.5323, adj growth 21.8 bp · C EV +5.09 (adj +1.83) on $29.20, P(profit) 0.5889, adj growth 16.0 bp · R EV +0.68 (adj +0.43) on $2.00, P(profit) 0.1563, adj growth 14.4 bp

## CAR @ NSH  ·  10000 joint draws  ·  392 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_CAR_win | p_overtime | goals | shots NSH/CAR | NSH/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.143 | 0.38 | 0.62 | 0.00 | 6.02 | 21.6/34.5 | 30.1/18.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.47 | 0.53 | 0.46 | 6.0 | 21.9/34.8 | 31.2/18.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 9.35 | 23.0/35.8 | 28.1/17.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.45 | 0.55 | 0.00 | 6.03 | 27.3/28.3 | 24.5/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.45 | 0.55 | 0.00 | 9.38 | 29.1/30.1 | 23.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.50 | 0.50 | 0.47 | 5.97 | 27.6/28.6 | 25.3/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Drury: 1+ goals YES | 9 | 0.131 | 0.116 | +0.036 | +0.020 | $3.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.171 | 0.158 | +0.033 | +0.020 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Nashville over 4.5 goals scored YES | 15 | 0.211 | 0.176 | +0.053 | +0.017 | $1.53 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.717 | 0.703 | +0.032 | +0.017 | $9.50 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Jack Drury: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes has the higher standalone adjusted growth (11.37 vs 10.20 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.153); relationships: KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: REINFORCING (phi 0.17); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes has the higher standalone adjusted growth (11.37 vs 7.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.186); relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: REINFORCING (phi 0.23); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: NSH offense suppressed (<= 2 goals)
- **Nashville over 4.5 goals scored YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: REINFORCING (phi 0.17); KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: REINFORCING (phi 0.23); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: CAR wins (incl. OT/SO)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03CARNSH-CAR2|no; why: KXNHLSPREAD-26NOV03CARNSH-CAR2|no has the higher standalone adjusted growth (3.79 vs 3.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis GAME:HIGH_EVENT (p 0.3104): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes — Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NSH:OFFENSE_4PLUS (p 0.3814): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes (same contract)
- thesis NSH:WINS (p 0.45): highest fidelity KXNHLSPREAD-26NOV03CARNSH-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.18)
- KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.211)
- KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.55, phi -0.466)
- KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4625, phi -0.228)
- override: Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.36 (adj +0.87) on $20.88, P(profit) 0.5069, adj growth 7.5 bp · B EV +2.93 (adj +1.57) on $17.54, P(profit) 0.3516, adj growth 14.2 bp · C EV +3.16 (adj +1.15) on $12.22, P(profit) 0.6662, adj growth 10.0 bp · R EV +0.47 (adj +0.18) on $4.00, P(profit) 0.7756, adj growth 6.4 bp

## ANA @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.124 | 0.40 | 0.60 | 0.00 | 6.07 | 21.5/33.5 | 29.2/18.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.112 | 0.39 | 0.61 | 0.00 | 9.49 | 23.2/35.6 | 27.9/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.48 | 0.52 | 0.00 | 6.1 | 27.2/28.0 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.47 | 0.54 | 0.00 | 9.55 | 28.8/29.5 | 23.1/22.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.47 | 0.53 | 0.46 | 5.99 | 21.9/34.0 | 30.5/18.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.50 | 0.50 | 0.51 | 6.03 | 27.5/28.1 | 24.7/24.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
