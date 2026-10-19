# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T11:24:44Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 120.00 | +26.98 | +6.40 | +13.61 | 0.635 | -56.07 | -75.54 | 40.41 |
| B thesis-diversified (joint) ← optimiser card | 56.66 | +9.37 | +3.92 | -0.07 | 0.498 | -22.45 | -32.67 | 34.20 |
| C best expression per thesis | 39.47 | +6.82 | +2.25 | +2.06 | 0.711 | -29.25 | -39.47 | 19.74 |
| R FUNDED research stakes | 15.00 | +2.37 | +1.08 | +0.87 | 0.527 | -7.52 | -10.81 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  414 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.57 | 0.43 | 0.00 | 6.03 | 26.8/27.3 | 24.1/22.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.104 | 0.49 | 0.51 | 0.00 | 6.03 | 21.2/32.6 | 28.9/17.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.47 | 5.96 | 26.5/27.0 | 23.8/23.2 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.45 | 0.55 | 0.46 | 5.98 | 21.3/32.8 | 29.3/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.59 | 0.41 | 0.00 | 9.36 | 28.5/29.0 | 23.5/22.0 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.079 | 0.51 | 0.49 | 0.00 | 9.32 | 22.8/34.3 | 28.0/17.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.016 | $4.02 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.125 | 0.109 | +0.029 | +0.013 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Alexis Lafreniere: 2+ assists YES | 7 | 0.101 | 0.085 | +0.026 | +0.011 | $2.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_MIXED | D |
| Jackson LaCombe: 1+ assists YES | 45 | 0.530 | 0.485 | +0.063 | +0.018 | $6.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.72) | EVIDENCE_MIXED | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes; why: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes has the higher standalone adjusted growth (7.87 vs 5.64 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.083); relationships: KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.072); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes; why: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes has the higher standalone adjusted growth (7.87 vs 4.27 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.057); relationships: KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.073); failure: ANA offense suppressed (<= 2 goals)
- **Alexis Lafreniere: 2+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (3.57 vs 0.00 bp); despite a smaller raw edge (+0.026 vs +0.026/contract); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NYR offense suppressed (<= 2 goals)
- **Jackson LaCombe: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes; why: Player prop expression KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes selected over player prop KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.72 vs 0.35 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.072); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.384): highest fidelity KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes — Player prop expression KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes selected over player prop KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.72 vs 0.35 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYR:OFFENSE_4PLUS (p 0.4328): highest fidelity KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3927, phi -0.166)
- KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3927, phi -0.171)
- KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3553, phi -0.214)
- KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3927, phi -0.325)
- override: Player prop expression KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes selected over player prop KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.72 vs 0.35 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +12.14 (adj +4.32) on $50.00, P(profit) 0.4993, adj growth 25.9 bp · B EV +3.63 (adj +1.62) on $16.28, P(profit) 0.3189, adj growth 14.0 bp · C EV +2.66 (adj +1.11) on $7.26, P(profit) 0.2568, adj growth 9.6 bp · R EV +0.47 (adj +0.30) on $2.00, P(profit) 0.1311, adj growth 8.8 bp

## COL @ PHI  ·  10000 joint draws  ·  376 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.137 | 0.39 | 0.61 | 0.00 | 6.0 | 21.4/33.4 | 29.2/18.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.46 | 0.54 | 0.47 | 5.86 | 21.5/33.8 | 30.5/18.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.45 | 0.55 | 0.00 | 5.94 | 26.9/27.8 | 24.1/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.48 | 0.52 | 0.48 | 5.88 | 27.0/27.9 | 24.7/23.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.080 | 0.36 | 0.64 | 0.00 | 9.08 | 22.6/35.2 | 27.8/18.0 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.071 | 0.41 | 0.59 | 0.00 | 3.46 | 20.0/32.2 | 29.9/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 9 | 0.140 | 0.120 | +0.044 | +0.024 | $5.50 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Colorado over 4.5 goals scored NO | 70 | 0.790 | 0.740 | +0.075 | +0.025 | $10.91 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 68 | 0.798 | 0.718 | +0.102 | +0.023 | $7.01 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 5.5 goals scored NO | 86 | 0.911 | 0.883 | +0.043 | +0.015 | $12.08 | FUNDED_RESEARCH | $4 | PHI:WINS | DIRECT (1.00) | EVIDENCE_MIXED | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT19COLPHI-COL2|no; why: higher confidence-adjusted growth (14.32 vs 5.64 bp); despite a smaller raw edge (+0.044 vs +0.113/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT19COLPHI-COL3|no: MOSTLY_INDEPENDENT (phi 0.105); KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no: MOSTLY_INDEPENDENT (phi -0.006); failure: PHI offense suppressed (<= 2 goals)
- **Colorado over 4.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-COL2|no; why: higher confidence-adjusted growth (6.80 vs 5.64 bp); despite a smaller raw edge (+0.075 vs +0.113/contract); relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.536); KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no: DUPLICATIVE (phi 0.604); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no has the higher standalone adjusted growth (6.80 vs 5.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.536); they share one thesis budget; relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.105); KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: REINFORCING (phi 0.536); KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no: DUPLICATIVE (phi 0.438); failure: COL wins by 2+
- **Colorado over 5.5 goals scored NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no; why: Broad expression KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no selected over player prop KXNHLAST-26OCT19COLPHI-COLCMAKAR8-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.77 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: DUPLICATIVE (phi 0.604); KXNHLSPREAD-26OCT19COLPHI-COL3|no: DUPLICATIVE (phi 0.438); failure: high-event game (8+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.3909): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — Broad expression KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no selected over player prop KXNHLAST-26OCT19COLPHI-COLCMAKAR8-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.77 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)
- thesis GAME:TIGHT (p 0.4494): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- thesis PHI:WINS (p 0.4467): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4637, phi -0.185)
- KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.649)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.3 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3194, phi -0.735)
- KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no: FUNDED_RESEARCH; family MIXED; loses 0% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.224, phi -0.489)
- override: Broad expression KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no selected over player prop KXNHLAST-26OCT19COLPHI-COLCMAKAR8-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.77 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +13.04 (adj +1.65) on $50.00, P(profit) 0.65, adj growth 12.5 bp · B EV +5.31 (adj +2.20) on $35.50, P(profit) 0.7473, adj growth 19.3 bp · C EV +3.72 (adj +1.04) on $27.33, P(profit) 0.6338, adj growth 9.2 bp · R EV +1.73 (adj +0.74) on $11.00, P(profit) 0.7473, adj growth 24.5 bp

## SJS @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.05 | 28.0/28.4 | 25.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.45 | 5.91 | 28.0/28.3 | 25.1/24.5 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.088 | 0.48 | 0.52 | 0.00 | 5.98 | 22.2/33.6 | 29.8/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.53 | 0.47 | 0.00 | 9.37 | 29.8/30.0 | 24.0/23.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.45 | 0.55 | 0.51 | 5.92 | 22.6/33.9 | 30.4/19.5 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.059 | 0.51 | 0.49 | 0.00 | 9.32 | 24.1/35.2 | 28.6/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 6.5 goals scored NO | 46 | 0.520 | 0.488 | +0.043 | +0.010 | $4.88 | FUNDED_RESEARCH | $2 | SJS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Full Game: Over 6.5 goals scored NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: wins across more scripts (relative breadth 0.741 vs 0.389); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, SJS shot control · normal event (5-7) · decided (2+) 0.09.
- thesis SJS:SUPPRESSED (p 0.4022): highest fidelity KXNHLTOTAL-26OCT19SJTOR-7|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no (same contract)
- KXNHLTOTAL-26OCT19SJTOR-7|no: FUNDED_RESEARCH; family MIXED; loses 17% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2767, phi -0.644)

portfolios: A EV +1.79 (adj +0.43) on $20.00, P(profit) 0.5202, adj growth 2.1 bp · B EV +0.44 (adj +0.10) on $4.88, P(profit) 0.5202, adj growth 0.9 bp · C EV +0.44 (adj +0.10) on $4.88, P(profit) 0.5202, adj growth 0.9 bp · R EV +0.18 (adj +0.04) on $2.00, P(profit) 0.5202, adj growth 1.4 bp

## PIT @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.63 | 0.37 | 0.00 | 6.05 | 27.2/27.0 | 24.0/23.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.62 | 0.38 | 0.00 | 9.45 | 28.9/28.5 | 23.0/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.47 | 6.03 | 27.4/27.3 | 23.9/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.085 | 0.68 | 0.32 | 0.00 | 6.0 | 32.2/21.3 | 18.7/27.6 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.54 | 0.46 | 0.47 | 5.96 | 32.2/21.7 | 18.3/28.8 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.071 | 0.70 | 0.30 | 0.00 | 9.38 | 34.0/23.2 | 18.6/26.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
