# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T12:32:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +26.58 | +6.84 | +25.92 | 0.759 | -21.23 | -33.73 | 61.23 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +22.45 | +10.33 | +20.09 | 0.710 | -24.78 | -35.66 | 95.99 |
| C best expression per thesis | 150.01 | +25.63 | +8.03 | +24.11 | 0.720 | -27.39 | -41.82 | 71.45 |
| R FUNDED research stakes | 22.00 | +2.10 | +1.04 | +1.65 | 0.619 | -6.07 | -7.77 | 0.00 |

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
| Owen Power: 1+ goals NO | 88 | 0.913 | 0.899 | +0.026 | +0.011 | $10.88 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (2.88 vs 0.71 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BUF:SUPPRESSED (p 0.3784): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3988, phi -0.128)

portfolios: A EV +0.19 (adj +0.09) on $6.64, P(profit) 0.9134, adj growth 0.8 bp · B EV +0.32 (adj +0.14) on $10.88, P(profit) 0.9134, adj growth 1.3 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.09 (adj +0.04) on $3.00, P(profit) 0.9134, adj growth 1.5 bp

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
| Ondrej Palat: 1+ goals YES | 9 | 0.131 | 0.119 | +0.035 | +0.024 | $3.18 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ assists YES | 27 | 0.350 | 0.300 | +0.066 | +0.016 | $2.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Carter Yakemchuk: 1+ assists NO | 67 | 0.737 | 0.699 | +0.052 | +0.013 | $6.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (13.57 vs 0.69 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.932 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15NYIOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (2.76 vs 0.69 bp); wins across more scripts (relative breadth 0.917 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT offense suppressed (<= 2 goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (1.74 vs 0.00 bp); despite a smaller raw edge (+0.052 vs +0.054/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT15NYIOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis OTT:OFFENSE_4PLUS (p 0.4218): highest fidelity KXNHLAST-26OCT15NYIOTT-OTTJSPENCE10-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15NYIOTT-OTTJSPENCE10-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3635): highest fidelity KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3125): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4683, phi -0.172)
- KXNHLAST-26OCT15NYIOTT-OTTJSPENCE10-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3635, phi -0.263)
- KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4218, phi -0.217)

portfolios: A EV +3.21 (adj +1.29) on $16.47, P(profit) 0.4342, adj growth 11.5 bp · B EV +2.27 (adj +1.05) on $12.10, P(profit) 0.3493, adj growth 9.7 bp · C EV +1.81 (adj +0.45) on $14.54, P(profit) 0.8337, adj growth 4.0 bp · R EV +0.36 (adj +0.25) on $1.00, P(profit) 0.1306, adj growth 8.8 bp

## SEA @ TBL  ·  10000 joint draws  ·  408 bet sides mapped, 20 +EV candidates, 4 on card


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
| John Carlson: 1+ goals NO | 83 | 0.879 | 0.863 | +0.039 | +0.023 | $9.05 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 67 | 0.763 | 0.714 | +0.077 | +0.028 | $9.06 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 4.5 goals scored NO | 67 | 0.757 | 0.709 | +0.071 | +0.023 | $2.98 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.645 | 0.629 | +0.038 | +0.022 | $4.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: higher confidence-adjusted growth (8.65 vs 8.24 bp); despite a smaller raw edge (+0.039 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT15SEATB-TB3|no: MOSTLY_INDEPENDENT (phi 0.117); KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no; why: higher confidence-adjusted growth (8.24 vs 5.38 bp); wins across more scripts (relative breadth 1.015 vs 0.898); relationships: KXNHLGOAL-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.117); KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no: REINFORCING (phi 0.548); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.204); failure: TBL wins by 2+
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: Broad expression KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.71 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLSPREAD-26OCT15SEATB-TB3|no: REINFORCING (phi 0.548); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.245); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT15SEATB-TB3|no: REINFORCING (phi 0.204); KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no: REINFORCING (phi 0.245); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.303): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3554): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- thesis GAME:TIGHT (p 0.427): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- KXNHLGOAL-26OCT15SEATB-TBJCARLSON74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4314, phi -0.15)
- KXNHLSPREAD-26OCT15SEATB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3566, phi -0.749)
- KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4314, phi -0.651)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4314, phi -0.285)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.71 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.95 (adj +0.70) on $16.59, P(profit) 0.6978, adj growth 6.1 bp · B EV +2.02 (adj +0.88) on $25.38, P(profit) 0.647, adj growth 8.3 bp · C EV +1.96 (adj +0.72) on $17.40, P(profit) 0.7628, adj growth 6.6 bp · R EV +0.58 (adj +0.24) on $7.00, P(profit) 0.6865, adj growth 9.0 bp

## VAN @ FLA  ·  10000 joint draws  ·  384 bet sides mapped, 22 +EV candidates, 4 on card


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
| Linus Karlsson: 1+ goals YES | 15 | 0.219 | 0.199 | +0.060 | +0.040 | $5.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.237 | 0.219 | +0.057 | +0.039 | $5.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 13 | 0.187 | 0.171 | +0.049 | +0.033 | $4.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 62 | 0.703 | 0.680 | +0.066 | +0.043 | $10.86 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 25.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.181); relationships: KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 22.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.201); relationships: KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (25.92 vs 19.06 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.164); relationships: KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (20.14 vs 17.74 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.144); relationships: KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense succeeds (4+ goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3508): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2178): highest fidelity KXNHLSPREAD-26OCT15VANFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2889): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.202)
- KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.231)
- KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4306, phi -0.2)
- KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4545, phi -0.233)

portfolios: A EV +5.24 (adj +1.08) on $16.59, P(profit) 0.5387, adj growth 9.6 bp · B EV +6.84 (adj +4.57) on $27.19, P(profit) 0.5172, adj growth 42.4 bp · C EV +8.29 (adj +2.94) on $22.89, P(profit) 0.7749, adj growth 25.9 bp · R EV +0.31 (adj +0.20) on $3.00, P(profit) 0.7029, adj growth 7.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  420 bet sides mapped, 7 +EV candidates, 4 on card


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
| Matt Rempe: 1+ goals YES | 6 | 0.090 | 0.081 | +0.026 | +0.017 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 24 | 0.324 | 0.277 | +0.071 | +0.024 | $3.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 13 | 0.164 | 0.150 | +0.026 | +0.012 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 62 | 0.673 | 0.653 | +0.036 | +0.017 | $6.52 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (10.53 vs 6.78 bp); despite a smaller raw edge (+0.026 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: NYR offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no; why: higher confidence-adjusted growth (6.78 vs 1.99 bp); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NYR offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NJDHAMILTON7-2|yes; why: higher confidence-adjusted growth (2.79 vs 0.12 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.914 vs 0.812); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no; why: higher confidence-adjusted growth (2.69 vs 1.99 bp); despite a smaller raw edge (+0.036 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: NJD offense succeeds (4+ goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3526): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:WINS (p 0.4878): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4104): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4239, phi -0.142)
- KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4239, phi -0.271)
- KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4104, phi -0.186)
- KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3642, phi -0.26)

portfolios: A EV +1.96 (adj +0.60) on $16.59, P(profit) 0.6666, adj growth 5.6 bp · B EV +2.69 (adj +1.30) on $14.37, P(profit) 0.4531, adj growth 12.0 bp · C EV +3.25 (adj +1.08) on $28.48, P(profit) 0.6638, adj growth 9.6 bp · R EV +0.11 (adj +0.05) on $2.00, P(profit) 0.6728, adj growth 1.9 bp

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
| Christian Dvorak: 1+ goals YES | 19 | 0.233 | 0.220 | +0.032 | +0.019 | $3.05 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.173 | 0.163 | +0.025 | +0.014 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 15 | 0.183 | 0.171 | +0.024 | +0.012 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Viktor Arvidsson: 1+ assists NO | 66 | 0.729 | 0.690 | +0.053 | +0.014 | $6.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes; why: higher confidence-adjusted growth (4.83 vs 3.42 bp); relationships: KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: PHI offense suppressed (<= 2 goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes has the higher standalone adjusted growth (4.83 vs 3.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes has the higher standalone adjusted growth (4.83 vs 2.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.022); failure: PHI offense suppressed (<= 2 goals)
- **Viktor Arvidsson: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15PHIDET-DETDLARKIN71-1|no; why: higher confidence-adjusted growth (1.90 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: DET offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3214): highest fidelity KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4363): highest fidelity KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no (same contract)
- KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.224)
- KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.216)
- KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.23)
- KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3447, phi -0.227)

portfolios: A EV +1.82 (adj +0.86) on $14.76, P(profit) 0.477, adj growth 7.9 bp · B EV +1.57 (adj +0.74) on $12.93, P(profit) 0.4495, adj growth 6.8 bp · C EV +1.58 (adj +0.67) on $14.99, P(profit) 0.2329, adj growth 5.9 bp · R EV +0.16 (adj +0.09) on $1.00, P(profit) 0.2329, adj growth 3.4 bp

## WPG @ CHI  ·  10000 joint draws  ·  410 bet sides mapped, 3 +EV candidates, 3 on card


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
| Connor Bedard: 1+ assists NO | 52 | 0.660 | 0.563 | +0.123 | +0.025 | $8.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ goals NO | 65 | 0.694 | 0.680 | +0.028 | +0.014 | $6.07 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 28 | 0.321 | 0.307 | +0.026 | +0.013 | $3.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (5.59 vs 2.05 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.147); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no; why: second expression of the same thesis: KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no has the higher standalone adjusted growth (5.59 vs 2.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (1.65 vs 0.49 bp); alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.147); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4146): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3693): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes (same contract)
- KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.0 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3693, phi -0.256)
- KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3693, phi -0.243)
- KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4146, phi -0.264)

portfolios: A EV +2.07 (adj +0.59) on $16.37, P(profit) 0.605, adj growth 5.5 bp · B EV +2.54 (adj +0.67) on $17.93, P(profit) 0.605, adj growth 6.3 bp · C EV +3.64 (adj +0.86) on $18.89, P(profit) 0.6605, adj growth 7.7 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.6938, adj growth 1.6 bp

## SJS @ NSH  ·  10000 joint draws  ·  446 bet sides mapped, 3 +EV candidates, 3 on card


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
| Collin Graf: 1+ goals YES | 13 | 0.173 | 0.151 | +0.035 | +0.013 | $2.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.798 | 0.718 | +0.093 | +0.013 | $7.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 43 | 0.571 | 0.458 | +0.124 | +0.011 | $2.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (3.08 vs 1.24 bp); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.095); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (1.82 vs 0.99 bp); despite a smaller raw edge (+0.093 vs +0.124/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.055); failure: SJS offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15SJNSH-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (0.99 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.095); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.055); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3914): highest fidelity KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3847): highest fidelity KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no (same contract)
- KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3847, phi -0.192)
- KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3914, phi -0.196)
- KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3914, phi -0.297)

portfolios: A EV +3.56 (adj +0.60) on $16.59, P(profit) 0.5772, adj growth 5.3 bp · B EV +2.29 (adj +0.40) on $12.38, P(profit) 0.5772, adj growth 3.7 bp · C EV +2.12 (adj +0.41) on $7.93, P(profit) 0.6628, adj growth 3.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 2 +EV candidates, 2 on card


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
| Ryan Hartman: 1+ assists YES | 24 | 0.309 | 0.267 | +0.056 | +0.014 | $2.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Adam Jiricek: 1+ assists NO | 72 | 0.777 | 0.746 | +0.043 | +0.012 | $6.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT15STLMIN-MINRHARTMAN38-2|yes; why: higher confidence-adjusted growth (2.27 vs 0.06 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; wins across more scripts (relative breadth 0.913 vs 0.763); alternative not eligible: confidence-adjusted EV +0.0017 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense suppressed (<= 2 goals)
- **Adam Jiricek: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15STLMIN-STLCMCMICHAEL77-1|no; why: higher confidence-adjusted growth (1.63 vs 0.20 bp); alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4373): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.4272): highest fidelity KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no (same contract)
- KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3471, phi -0.261)
- KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3598, phi -0.193)

portfolios: A EV +1.76 (adj +0.45) on $12.83, P(profit) 0.3086, adj growth 3.8 bp · B EV +0.91 (adj +0.24) on $9.07, P(profit) 0.8474, adj growth 2.2 bp · C EV +1.46 (adj +0.38) on $14.51, P(profit) 0.8474, adj growth 3.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Vegas wins by over 1.5 goals NO | 47 | 0.559 | 0.512 | +0.071 | +0.024 | $4.64 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $3.13 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (5.20 vs 4.11 bp); relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: DUPLICATIVE (phi 0.754); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no has the higher standalone adjusted growth (5.20 vs 4.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.754); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: DUPLICATIVE (phi 0.754); failure: VGK wins by 2+

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis GAME:TIGHT (p 0.401): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.2919): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -1.0)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -0.754)

portfolios: A EV +1.82 (adj +0.58) on $16.59, P(profit) 0.6481, adj growth 5.1 bp · B EV +1.00 (adj +0.34) on $7.77, P(profit) 0.5586, adj growth 3.1 bp · C EV +1.52 (adj +0.52) on $10.38, P(profit) 0.5586, adj growth 4.6 bp · R EV +0.39 (adj +0.13) on $3.00, P(profit) 0.5586, adj growth 4.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
