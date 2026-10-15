# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T13:24:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +29.63 | +8.84 | +26.68 | 0.745 | -24.24 | -36.49 | 79.18 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +22.09 | +10.72 | +20.05 | 0.707 | -24.43 | -36.57 | 100.03 |
| C best expression per thesis | 150.00 | +25.82 | +9.85 | +21.58 | 0.689 | -32.32 | -46.27 | 87.23 |
| R FUNDED research stakes | 21.00 | +2.12 | +1.00 | +1.77 | 0.598 | -5.77 | -8.50 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  426 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.113 | 0.48 | 0.52 | 0.00 | 6.01 | 22.3/34.3 | 30.3/19.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.55 | 0.45 | 0.00 | 6.07 | 28.0/28.6 | 25.3/24.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.48 | 5.93 | 22.5/34.4 | 31.1/19.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.51 | 0.49 | 0.50 | 5.98 | 28.2/28.8 | 25.4/24.9 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 9.23 | 23.7/35.7 | 28.9/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.52 | 0.48 | 0.00 | 9.39 | 29.7/30.3 | 24.3/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tage Thompson: 1+ goals NO | 60 | 0.645 | 0.633 | +0.029 | +0.016 | $5.45 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (2.40 vs 0.46 bp); despite a smaller raw edge (+0.029 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BUF:SUPPRESSED (p 0.3784): highest fidelity KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3988, phi -0.246)

portfolios: A EV +0.28 (adj +0.16) on $6.07, P(profit) 0.6455, adj growth 1.5 bp · B EV +0.25 (adj +0.14) on $5.45, P(profit) 0.6455, adj growth 1.3 bp · C EV +0.44 (adj +0.24) on $9.40, P(profit) 0.6455, adj growth 2.2 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.6455, adj growth 1.9 bp

## NYI @ OTT  ·  10000 joint draws  ·  416 bet sides mapped, 4 +EV candidates, 4 on card


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
| Adam Pelech: 1+ goals YES | 4 | 0.062 | 0.053 | +0.019 | +0.010 | $1.11 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 10 | 0.131 | 0.120 | +0.024 | +0.014 | $1.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Warren Foegele: 1+ goals YES | 16 | 0.195 | 0.183 | +0.026 | +0.013 | $1.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Carter Yakemchuk: 1+ assists NO | 67 | 0.737 | 0.699 | +0.052 | +0.013 | $5.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Adam Pelech: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (5.28 vs 0.69 bp); despite a smaller raw edge (+0.019 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.868 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (4.55 vs 0.69 bp); despite a smaller raw edge (+0.024 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.932 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (2.77 vs 0.69 bp); despite a smaller raw edge (+0.026 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.904 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: OTT offense suppressed (<= 2 goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (1.74 vs 0.00 bp); despite a smaller raw edge (+0.052 vs +0.064/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis OTT:SUPPRESSED (p 0.3635): highest fidelity KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3125): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis OTT:OFFENSE_4PLUS (p 0.4218): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15NYIOTT-NYIAPELECH3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4683, phi -0.118)
- KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4683, phi -0.172)
- KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3635, phi -0.181)
- KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4218, phi -0.217)

portfolios: A EV +2.12 (adj +1.00) on $12.86, P(profit) 0.3423, adj growth 9.1 bp · B EV +1.68 (adj +0.78) on $10.87, P(profit) 0.3423, adj growth 7.2 bp · C EV +0.75 (adj +0.19) on $9.91, P(profit) 0.7371, adj growth 1.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ TBL  ·  10000 joint draws  ·  408 bet sides mapped, 21 +EV candidates, 4 on card


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
| Ryan Winterton: 1+ goals YES | 9 | 0.126 | 0.116 | +0.031 | +0.020 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 67 | 0.763 | 0.714 | +0.077 | +0.028 | $9.37 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ben Meyers: 1+ goals YES | 9 | 0.120 | 0.111 | +0.024 | +0.015 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.645 | 0.629 | +0.038 | +0.022 | $5.44 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: higher confidence-adjusted growth (10.13 vs 8.24 bp); despite a smaller raw edge (+0.031 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT15SEATB-TB3|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: SEA offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no; why: higher confidence-adjusted growth (8.24 vs 6.62 bp); wins across more scripts (relative breadth 1.015 vs 0.898); relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.204); failure: TBL wins by 2+
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15SEATB-TB3|no has the higher standalone adjusted growth (8.24 vs 5.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.071); they share one thesis budget; relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT15SEATB-TB3|no: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: SEA offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT15SEATB-TB3|no: REINFORCING (phi 0.204); KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.303): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.427): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2164): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- KXNHLGOAL-26OCT15SEATB-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4793, phi -0.193)
- KXNHLSPREAD-26OCT15SEATB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3566, phi -0.749)
- KXNHLGOAL-26OCT15SEATB-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4793, phi -0.144)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4314, phi -0.285)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.98 (adj +0.73) on $16.22, P(profit) 0.6978, adj growth 6.5 bp · B EV +2.63 (adj +1.39) on $19.07, P(profit) 0.6269, adj growth 13.0 bp · C EV +1.99 (adj +0.73) on $17.69, P(profit) 0.7628, adj growth 6.7 bp · R EV +0.46 (adj +0.20) on $5.00, P(profit) 0.5337, adj growth 7.3 bp

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
| Linus Karlsson: 1+ goals YES | 15 | 0.219 | 0.197 | +0.060 | +0.038 | $5.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.237 | 0.218 | +0.057 | +0.038 | $5.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 62 | 0.703 | 0.680 | +0.066 | +0.043 | $10.25 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 13 | 0.187 | 0.169 | +0.049 | +0.031 | $4.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 22.63 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.181); relationships: KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 20.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.201); relationships: KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: VAN offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (20.14 vs 17.74 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.144); relationships: KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 17.64 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.164); relationships: KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3508): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2178): highest fidelity KXNHLSPREAD-26OCT15VANFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2889): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.202)
- KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.231)
- KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4545, phi -0.233)
- KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.2)

portfolios: A EV +5.05 (adj +1.03) on $16.22, P(profit) 0.5387, adj growth 9.2 bp · B EV +6.19 (adj +3.98) on $24.91, P(profit) 0.5172, adj growth 37.1 bp · C EV +7.33 (adj +2.73) on $15.77, P(profit) 0.2866, adj growth 23.9 bp · R EV +0.31 (adj +0.20) on $3.00, P(profit) 0.7029, adj growth 7.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card


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
| Jack Hughes: 2+ assists NO | 85 | 0.910 | 0.875 | +0.051 | +0.016 | $10.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 77 | 0.825 | 0.795 | +0.042 | +0.012 | $6.28 | FUNDED_RESEARCH | $2 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 66 | 0.721 | 0.688 | +0.045 | +0.012 | $1.54 | FUNDED_RESEARCH | $1 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.785 | 0.745 | +0.051 | +0.011 | $6.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Jack Hughes: 2+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no; why: higher confidence-adjusted growth (4.66 vs 1.99 bp); relationships: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: REINFORCING (phi 0.17); KXNHLSPREAD-26OCT15NYRNJ-NJ2|no: REINFORCING (phi 0.162); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes has the higher standalone adjusted growth (2.18 vs 1.99 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.132); relationships: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no: REINFORCING (phi 0.17); KXNHLSPREAD-26OCT15NYRNJ-NJ2|no: DUPLICATIVE (phi 0.741); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: NJD wins by 2+
- **New Jersey wins by over 1.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ2|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.95 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no: REINFORCING (phi 0.162); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: DUPLICATIVE (phi 0.741); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.137); failure: NJD wins by 2+
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (1.38 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLSPREAD-26OCT15NYRNJ-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.137); failure: NYR offense succeeds (4+ goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4104): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3526): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes — Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ2|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.95 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYR:WINS (p 0.4878): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3642, phi -0.235)
- KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2792, phi -0.741)
- KXNHLSPREAD-26OCT15NYRNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2792, phi -1.0)
- KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3526, phi -0.207)
- override: Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ2|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.95 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.73 (adj +0.42) on $16.22, P(profit) 0.6493, adj growth 3.9 bp · B EV +1.53 (adj +0.42) on $24.98, P(profit) 0.5874, adj growth 4.0 bp · C EV +2.76 (adj +0.71) on $32.81, P(profit) 0.7876, adj growth 6.5 bp · R EV +0.17 (adj +0.05) on $3.00, P(profit) 0.7208, adj growth 1.8 bp

## PHI @ DET  ·  10000 joint draws  ·  396 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.112 | 0.54 | 0.46 | 0.00 | 5.93 | 32.3/21.1 | 18.0/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.50 | 0.50 | 0.00 | 5.96 | 27.2/26.8 | 23.3/23.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.47 | 5.84 | 32.9/21.3 | 18.2/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.49 | 5.89 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.49 | 0.51 | 0.00 | 3.44 | 26.3/25.6 | 23.8/24.5 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.77 | 31.2/20.3 | 18.8/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 19 | 0.233 | 0.220 | +0.032 | +0.019 | $2.87 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.173 | 0.161 | +0.025 | +0.013 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 15 | 0.183 | 0.171 | +0.024 | +0.012 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Viktor Arvidsson: 1+ assists NO | 66 | 0.729 | 0.690 | +0.053 | +0.014 | $5.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes; why: higher confidence-adjusted growth (4.83 vs 2.84 bp); relationships: KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: PHI offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes has the higher standalone adjusted growth (4.83 vs 2.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes has the higher standalone adjusted growth (4.83 vs 2.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.022); failure: PHI offense suppressed (<= 2 goals)
- **Viktor Arvidsson: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT15PHIDET-4|no; why: higher confidence-adjusted growth (1.90 vs 0.78 bp); wins across more scripts (relative breadth 0.995 vs 0.35); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: DET offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3214): highest fidelity KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4363): highest fidelity KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no (same contract)
- KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.224)
- KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.216)
- KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.23)
- KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3447, phi -0.227)

portfolios: A EV +1.78 (adj +0.82) on $14.42, P(profit) 0.477, adj growth 7.5 bp · B EV +1.45 (adj +0.66) on $12.00, P(profit) 0.4221, adj growth 6.2 bp · C EV +1.61 (adj +0.68) on $15.23, P(profit) 0.2329, adj growth 6.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ CHI  ·  10000 joint draws  ·  410 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.50 | 0.50 | 0.00 | 6.0 | 26.6/27.0 | 23.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.47 | 5.87 | 26.3/26.6 | 23.4/23.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.096 | 0.44 | 0.56 | 0.00 | 6.01 | 21.0/31.9 | 27.8/18.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.48 | 0.52 | 0.46 | 5.91 | 21.3/32.0 | 28.5/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.48 | 0.52 | 0.00 | 9.36 | 27.8/28.2 | 21.8/21.8 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.060 | 0.38 | 0.62 | 0.00 | 9.23 | 22.3/33.4 | 25.9/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 13 | 0.176 | 0.162 | +0.038 | +0.024 | $3.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Viggo Bjorck: 1+ goals NO | 83 | 0.862 | 0.853 | +0.022 | +0.013 | $10.25 | FUNDED_RESEARCH | $3 | WPG:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ goals NO | 65 | 0.694 | 0.682 | +0.028 | +0.016 | $6.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 28 | 0.321 | 0.307 | +0.026 | +0.013 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (10.75 vs 1.65 bp); relationships: KXNHLGOAL-26OCT15WPGCHI-WPGVBJORCK61-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Viggo Bjorck: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15WPGCHI-WPG3|no; why: higher confidence-adjusted growth (2.75 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense succeeds (4+ goals)
- **Connor Bedard: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15WPGCHI-CHIPKANE88-1|no; why: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHIPKANE88-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.84 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15WPGCHI-WPGVBJORCK61-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (10.75 vs 1.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15WPGCHI-WPGVBJORCK61-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3693): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4146): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15WPGCHI-CHIPKANE88-1|no — Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHIPKANE88-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.84 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:SUPPRESSED (p 0.4): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4146, phi -0.203)
- KXNHLGOAL-26OCT15WPGCHI-WPGVBJORCK61-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3851, phi -0.176)
- KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3693, phi -0.243)
- KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4146, phi -0.264)
- override: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHIPKANE88-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.84 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.23 (adj +0.78) on $16.22, P(profit) 0.4856, adj growth 7.4 bp · B EV +1.65 (adj +0.98) on $21.84, P(profit) 0.3339, adj growth 9.2 bp · C EV +2.81 (adj +1.34) on $16.87, P(profit) 0.7446, adj growth 11.8 bp · R EV +0.08 (adj +0.05) on $3.00, P(profit) 0.8621, adj growth 1.7 bp

## SJS @ NSH  ·  10000 joint draws  ·  446 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.05 | 27.6/27.8 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.48 | 0.52 | 0.45 | 5.99 | 27.9/27.9 | 24.4/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 9.29 | 28.9/28.8 | 23.1/22.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.068 | 0.48 | 0.52 | 0.00 | 6.0 | 22.1/32.7 | 28.7/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.067 | 0.60 | 0.40 | 0.00 | 6.02 | 32.7/22.1 | 19.1/28.3 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.47 | 5.87 | 32.5/22.1 | 18.9/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Collin Graf: 1+ goals YES | 13 | 0.173 | 0.160 | +0.035 | +0.022 | $3.11 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 43 | 0.571 | 0.458 | +0.124 | +0.011 | $3.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (8.58 vs 1.24 bp); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.095); failure: SJS offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15SJNSH-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (0.99 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.095); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3914): highest fidelity KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3847): highest fidelity KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no (same contract)
- KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3847, phi -0.192)
- KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3914, phi -0.297)

portfolios: A EV +2.63 (adj +0.67) on $9.78, P(profit) 0.6628, adj growth 6.1 bp · B EV +1.65 (adj +0.56) on $6.21, P(profit) 0.6628, adj growth 5.3 bp · C EV +2.84 (adj +0.97) on $10.72, P(profit) 0.6628, adj growth 8.6 bp · R EV +0.25 (adj +0.16) on $1.00, P(profit) 0.1729, adj growth 5.7 bp

## STL @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.02 | 27.7/27.4 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.96 | 27.9/27.5 | 24.2/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.57 | 0.43 | 0.00 | 9.35 | 29.4/29.3 | 23.5/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.65 | 0.35 | 0.00 | 6.0 | 32.7/21.9 | 19.1/28.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.58 | 0.42 | 0.45 | 5.96 | 33.3/22.4 | 19.2/29.7 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 9.35 | 34.5/23.4 | 18.3/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Hartman: 1+ goals YES | 19 | 0.230 | 0.216 | +0.029 | +0.015 | $2.34 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 24 | 0.309 | 0.267 | +0.056 | +0.014 | $2.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 23 | 0.269 | 0.253 | +0.026 | +0.011 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.15 vs 2.27 bp); despite a smaller raw edge (+0.029 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (3.15 vs 2.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.018); they share one thesis budget; relationships: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: MIN offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15STLMIN-STL6|yes; why: despite a smaller raw edge (+0.026 vs +0.027/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.908 vs 0.339); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4373): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3598): highest fidelity KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes (same contract)
- KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3471, phi -0.199)
- KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3471, phi -0.261)
- KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4272, phi -0.261)

portfolios: A EV +2.07 (adj +0.68) on $11.83, P(profit) 0.471, adj growth 5.9 bp · B EV +1.03 (adj +0.38) on $6.34, P(profit) 0.6163, adj growth 3.5 bp · C EV +0.89 (adj +0.43) on $6.87, P(profit) 0.4344, adj growth 3.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ EDM  ·  10000 joint draws  ·  436 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.63 | 0.37 | 0.00 | 6.07 | 27.5/27.5 | 24.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 9.46 | 29.4/29.3 | 23.8/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.45 | 6.07 | 28.1/28.0 | 24.7/24.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.077 | 0.67 | 0.33 | 0.00 | 6.07 | 32.8/22.1 | 19.4/28.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.071 | 0.69 | 0.31 | 0.00 | 9.48 | 34.3/23.4 | 18.9/26.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.56 | 0.44 | 0.45 | 5.94 | 32.9/22.3 | 19.2/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vasily Podkolzin: 2+ assists YES | 7 | 0.126 | 0.098 | +0.051 | +0.023 | $2.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 9 | 0.129 | 0.111 | +0.033 | +0.015 | $1.61 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 69 | 0.798 | 0.718 | +0.093 | +0.013 | $7.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Vasily Podkolzin: 2+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-2|yes; why: higher confidence-adjusted growth (16.64 vs 3.45 bp); alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes; why: second expression of the same thesis: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes has the higher standalone adjusted growth (16.64 vs 5.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.073); they share one thesis budget; relationships: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: EDM offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15UTAEDM-UTA2|no; why: higher confidence-adjusted growth (1.85 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4964): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3988): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.217)
- KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.154)
- KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3865, phi -0.19)

portfolios: A EV +4.98 (adj +1.99) on $13.96, P(profit) 0.2305, adj growth 17.2 bp · B EV +3.10 (adj +1.11) on $11.01, P(profit) 0.2305, adj growth 10.3 bp · C EV +2.86 (adj +1.30) on $4.18, P(profit) 0.1257, adj growth 11.4 bp · R EV +0.35 (adj +0.16) on $1.00, P(profit) 0.1291, adj growth 5.2 bp

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
| Vegas wins by over 1.5 goals NO | 47 | 0.559 | 0.512 | +0.071 | +0.024 | $4.37 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $2.95 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (5.20 vs 4.11 bp); relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: DUPLICATIVE (phi 0.754); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no has the higher standalone adjusted growth (5.20 vs 4.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.754); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: DUPLICATIVE (phi 0.754); failure: VGK wins by 2+

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis GAME:TIGHT (p 0.401): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.2919): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -1.0)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -0.754)

portfolios: A EV +1.78 (adj +0.56) on $16.22, P(profit) 0.6481, adj growth 5.0 bp · B EV +0.94 (adj +0.32) on $7.32, P(profit) 0.5586, adj growth 3.0 bp · C EV +1.54 (adj +0.53) on $10.55, P(profit) 0.5586, adj growth 4.7 bp · R EV +0.39 (adj +0.13) on $3.00, P(profit) 0.5586, adj growth 4.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
