# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T11:32:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.85 | +7.24 | +28.56 | 0.700 | -40.32 | -61.94 | 56.69 |
| B thesis-diversified (joint) ← optimiser card | 137.93 | +24.48 | +11.70 | +17.06 | 0.619 | -43.43 | -57.10 | 100.86 |
| C best expression per thesis | 90.28 | +14.88 | +5.14 | +11.13 | 0.604 | -29.31 | -36.53 | 44.76 |
| R FUNDED research stakes | 26.00 | +4.34 | +1.94 | +2.28 | 0.600 | -9.96 | -13.32 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  426 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.113 | 0.48 | 0.52 | 0.00 | 6.01 | 22.3/34.3 | 30.3/19.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.55 | 0.45 | 0.00 | 6.07 | 28.0/28.6 | 25.3/24.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.48 | 5.93 | 22.5/34.4 | 31.1/19.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.51 | 0.49 | 0.50 | 5.98 | 28.2/28.8 | 25.4/24.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 9.23 | 23.7/35.7 | 28.9/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.52 | 0.48 | 0.00 | 9.39 | 29.7/30.3 | 24.3/23.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ OTT  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.62 | 0.38 | 0.00 | 6.0 | 26.8/26.6 | 23.7/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.49 | 5.89 | 27.0/26.7 | 23.4/23.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.088 | 0.66 | 0.34 | 0.00 | 5.98 | 31.6/21.1 | 18.5/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.65 | 0.35 | 0.00 | 9.15 | 28.4/28.0 | 23.3/21.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.52 | 0.48 | 0.48 | 5.89 | 31.9/21.5 | 18.3/28.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.57 | 0.43 | 0.00 | 3.49 | 25.5/25.2 | 23.6/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Pelech: 1+ goals YES | 4 | 0.062 | 0.053 | +0.019 | +0.010 | $2.19 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 10 | 0.131 | 0.120 | +0.024 | +0.014 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Carter Yakemchuk: 1+ assists NO | 67 | 0.737 | 0.696 | +0.052 | +0.011 | $8.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Adam Pelech: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (5.28 vs 0.69 bp); despite a smaller raw edge (+0.019 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.868 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (4.55 vs 0.69 bp); despite a smaller raw edge (+0.024 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.932 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (1.14 vs 0.00 bp); despite a smaller raw edge (+0.052 vs +0.054/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis OTT:SUPPRESSED (p 0.3635): highest fidelity KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3125): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15NYIOTT-NYIAPELECH3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4683, phi -0.118)
- KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4683, phi -0.172)
- KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4218, phi -0.217)

portfolios: A EV +3.46 (adj +1.55) on $20.60, P(profit) 0.185, adj growth 12.6 bp · B EV +2.50 (adj +1.14) on $14.75, P(profit) 0.185, adj growth 9.8 bp · C EV +0.69 (adj +0.14) on $9.12, P(profit) 0.7371, adj growth 1.2 bp · R EV +0.45 (adj +0.24) on $1.00, P(profit) 0.062, adj growth 7.0 bp

## SEA @ TBL  ·  10000 joint draws  ·  352 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_SEA_win | p_overtime | goals | shots TBL/SEA | TBL/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.136 | 0.68 | 0.32 | 0.00 | 5.97 | 32.7/21.1 | 18.4/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.61 | 0.39 | 0.00 | 6.04 | 27.3/26.5 | 23.5/23.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.56 | 0.44 | 0.48 | 5.9 | 33.0/21.1 | 18.0/29.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.44 | 5.88 | 27.5/26.7 | 23.4/24.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.079 | 0.70 | 0.30 | 0.00 | 9.2 | 34.6/22.5 | 18.0/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.067 | 0.59 | 0.41 | 0.00 | 9.19 | 29.0/28.2 | 22.8/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 8 | 0.126 | 0.114 | +0.041 | +0.028 | $6.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 67 | 0.763 | 0.714 | +0.077 | +0.028 | $17.22 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ben Meyers: 1+ goals YES | 9 | 0.120 | 0.110 | +0.024 | +0.014 | $3.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.645 | 0.629 | +0.038 | +0.022 | $10.61 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: higher confidence-adjusted growth (21.76 vs 8.24 bp); despite a smaller raw edge (+0.041 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT15SEATB-TB3|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: SEA offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no; why: higher confidence-adjusted growth (8.24 vs 2.56 bp); relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.204); failure: TBL wins by 2+
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15SEATB-TB3|no has the higher standalone adjusted growth (8.24 vs 4.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.071); they share one thesis budget; relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT15SEATB-TB3|no: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: SEA offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT15SEATB-TB3|no: REINFORCING (phi 0.204); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.303): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.427): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- thesis TBL:SUPPRESSED (p 0.3554): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4793, phi -0.193)
- KXNHLSPREAD-26OCT15SEATB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3566, phi -0.749)
- KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4793, phi -0.144)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4314, phi -0.285)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.17 (adj +1.12) on $32.35, P(profit) 0.552, adj growth 8.4 bp · B EV +6.55 (adj +3.73) on $37.59, P(profit) 0.6162, adj growth 32.0 bp · C EV +2.26 (adj +0.83) on $20.00, P(profit) 0.7628, adj growth 7.5 bp · R EV +0.75 (adj +0.32) on $8.00, P(profit) 0.5337, adj growth 11.2 bp

## VAN @ FLA  ·  10000 joint draws  ·  384 bet sides mapped, 23 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.116 | 0.64 | 0.36 | 0.00 | 6.03 | 32.6/21.2 | 18.5/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 6.03 | 27.3/26.7 | 23.6/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.45 | 5.92 | 27.6/27.0 | 23.7/24.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.55 | 0.45 | 0.46 | 5.93 | 32.8/21.5 | 18.4/29.2 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.087 | 0.70 | 0.30 | 0.00 | 9.22 | 34.2/22.6 | 18.1/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.60 | 0.40 | 0.00 | 9.27 | 28.7/28.3 | 22.7/21.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver over 4.5 goals scored YES | 10 | 0.186 | 0.140 | +0.080 | +0.034 | $5.76 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Drew O'Connor: 1+ goals YES | 13 | 0.187 | 0.171 | +0.049 | +0.033 | $7.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.695 | 0.674 | +0.049 | +0.027 | $19.75 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ assists YES | 24 | 0.323 | 0.277 | +0.070 | +0.024 | $4.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: higher confidence-adjusted growth (25.92 vs 20.14 bp); despite a smaller raw edge (+0.080 vs +0.080/contract); relationships: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: REINFORCING (phi 0.164); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.017); KXNHLAST-26OCT15VANFLA-VANMROSSI23-1|yes: REINFORCING (phi 0.223); failure: FLA wins (incl. OT/SO)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 19.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.164); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes: REINFORCING (phi 0.164); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.075); failure: VAN offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (20.14 vs 7.15 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.151); relationships: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes: INTENTIONAL_DIVERSIFIER (phi -0.017); KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense succeeds (4+ goals)
- **Marco Rossi: 1+ assists YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 6.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.223); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes: REINFORCING (phi 0.223); KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.075); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3508): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4|yes less than the minimum stake; KXNHLAST-26OCT15VANFLA-VANMROSSI23-1|yes kept
- thesis VAN:WINS_BY_2PLUS (p 0.2178): highest fidelity KXNHLSPREAD-26OCT15VANFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2889): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.5716, phi -0.439)
- KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.2)
- KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4545, phi -0.238)
- KXNHLAST-26OCT15VANFLA-VANMROSSI23-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.271)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4|yes less than the minimum stake; KXNHLAST-26OCT15VANFLA-VANMROSSI23-1|yes kept

portfolios: A EV +9.85 (adj +1.88) on $32.35, P(profit) 0.5387, adj growth 14.6 bp · B EV +9.51 (adj +4.76) on $36.82, P(profit) 0.4387, adj growth 41.0 bp · C EV +8.29 (adj +3.08) on $17.84, P(profit) 0.2866, adj growth 26.5 bp · R EV +1.87 (adj +0.85) on $7.00, P(profit) 0.7545, adj growth 29.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  420 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.128 | 0.55 | 0.45 | 0.00 | 5.94 | 33.2/21.1 | 17.9/29.1 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.55 | 0.45 | 0.47 | 5.89 | 32.9/21.3 | 18.1/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.48 | 0.52 | 0.00 | 6.0 | 27.4/26.7 | 23.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.47 | 5.85 | 27.3/26.7 | 23.6/24.0 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.074 | 0.56 | 0.44 | 0.00 | 9.15 | 34.5/22.6 | 17.5/27.6 | even strength |
| NJD shot control · low event (<=4) · decided (2+) | 0.068 | 0.55 | 0.45 | 0.00 | 3.52 | 31.7/20.1 | 18.4/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Matt Rempe: 1+ goals YES | 6 | 0.090 | 0.080 | +0.026 | +0.016 | $3.59 | FUNDED_RESEARCH | $1 | NYR:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 77 | 0.825 | 0.795 | +0.042 | +0.012 | $14.46 | FUNDED_RESEARCH | $4 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.785 | 0.745 | +0.051 | +0.011 | $13.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Gabe Perreault: 1+ assists YES | 23 | 0.324 | 0.253 | +0.082 | +0.011 | $2.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no; why: higher confidence-adjusted growth (9.08 vs 1.99 bp); despite a smaller raw edge (+0.026 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: NYR offense suppressed (<= 2 goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (1.99 vs 1.38 bp); despite a smaller raw edge (+0.042 vs +0.082/contract); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.072); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.132); failure: NJD wins by 2+
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (1.38 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); failure: NYR offense succeeds (4+ goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no has the higher standalone adjusted growth (1.99 vs 1.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.132); they share one thesis budget; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3526): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT15NYRNJ-NJ3|no (same contract)
- thesis NYR:WINS (p 0.4878): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15NYRNJ-NJ3|no (same contract)
- thesis NYR:SUPPRESSED (p 0.4239): highest fidelity KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4239, phi -0.142)
- KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2792, phi -0.741)
- KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3526, phi -0.207)
- KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.9 pts; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4239, phi -0.271)

portfolios: A EV +5.81 (adj +1.57) on $32.35, P(profit) 0.3825, adj growth 12.5 bp · B EV +4.09 (adj +1.45) on $34.49, P(profit) 0.6563, adj growth 12.5 bp · C EV +1.91 (adj +0.49) on $31.39, P(profit) 0.6293, adj growth 4.3 bp · R EV +0.62 (adj +0.31) on $5.00, P(profit) 0.8325, adj growth 10.6 bp

## PHI @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.112 | 0.54 | 0.46 | 0.00 | 5.93 | 32.3/21.1 | 18.0/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.50 | 0.50 | 0.00 | 5.96 | 27.2/26.8 | 23.3/23.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.47 | 5.84 | 32.9/21.3 | 18.2/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.49 | 5.89 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.49 | 0.51 | 0.00 | 3.44 | 26.3/25.6 | 23.8/24.5 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.77 | 31.2/20.3 | 18.8/29.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.50 | 0.50 | 0.00 | 6.0 | 26.6/27.0 | 23.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.47 | 5.87 | 26.3/26.6 | 23.4/23.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.096 | 0.44 | 0.56 | 0.00 | 6.01 | 21.0/31.9 | 27.8/18.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.48 | 0.52 | 0.46 | 5.91 | 21.3/32.0 | 28.5/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.48 | 0.52 | 0.00 | 9.36 | 27.8/28.2 | 21.8/21.8 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.060 | 0.38 | 0.62 | 0.00 | 9.23 | 22.3/33.4 | 25.9/17.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.05 | 27.6/27.8 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.48 | 0.52 | 0.45 | 5.99 | 27.9/27.9 | 24.4/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 9.29 | 28.9/28.8 | 23.1/22.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.068 | 0.48 | 0.52 | 0.00 | 6.0 | 22.1/32.7 | 28.7/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.067 | 0.60 | 0.40 | 0.00 | 6.02 | 32.7/22.1 | 19.1/28.3 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.47 | 5.87 | 32.5/22.1 | 18.9/29.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.02 | 27.7/27.4 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.96 | 27.9/27.5 | 24.2/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.57 | 0.43 | 0.00 | 9.35 | 29.4/29.3 | 23.5/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.65 | 0.35 | 0.00 | 6.0 | 32.7/21.9 | 19.1/28.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.58 | 0.42 | 0.45 | 5.96 | 33.3/22.4 | 19.2/29.7 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 9.35 | 34.5/23.4 | 18.3/27.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.63 | 0.37 | 0.00 | 6.07 | 27.5/27.5 | 24.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 9.46 | 29.4/29.3 | 23.8/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.45 | 6.07 | 28.1/28.0 | 24.7/24.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.077 | 0.67 | 0.33 | 0.00 | 6.07 | 32.8/22.1 | 19.4/28.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.071 | 0.69 | 0.31 | 0.00 | 9.48 | 34.3/23.4 | 18.9/26.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.56 | 0.44 | 0.45 | 5.94 | 32.9/22.3 | 19.2/29.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.127 | 0.79 | 0.21 | 0.00 | 5.97 | 33.9/22.1 | 19.9/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.73 | 0.27 | 0.00 | 6.01 | 28.3/27.8 | 25.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.56 | 0.44 | 0.47 | 5.92 | 28.5/28.3 | 24.9/25.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.58 | 0.42 | 0.46 | 5.83 | 33.7/22.2 | 18.9/30.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.75 | 0.25 | 0.00 | 9.18 | 29.7/29.2 | 24.6/21.8 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.078 | 0.78 | 0.22 | 0.00 | 9.16 | 35.4/23.4 | 19.3/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vegas wins by over 1.5 goals NO | 47 | 0.559 | 0.512 | +0.071 | +0.024 | $8.53 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $5.75 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (5.20 vs 4.11 bp); relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: DUPLICATIVE (phi 0.754); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no has the higher standalone adjusted growth (5.20 vs 4.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.754); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: DUPLICATIVE (phi 0.754); failure: VGK wins by 2+

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis GAME:TIGHT (p 0.401): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.2919): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -1.0)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -0.754)

portfolios: A EV +3.55 (adj +1.12) on $32.35, P(profit) 0.6481, adj growth 8.6 bp · B EV +1.83 (adj +0.62) on $14.28, P(profit) 0.5586, adj growth 5.4 bp · C EV +1.74 (adj +0.60) on $11.93, P(profit) 0.5586, adj growth 5.2 bp · R EV +0.64 (adj +0.22) on $5.00, P(profit) 0.5586, adj growth 7.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
