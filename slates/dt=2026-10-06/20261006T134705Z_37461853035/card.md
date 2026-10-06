# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T13:47:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +25.55 | +7.58 | +23.66 | 0.759 | -18.43 | -28.79 | 69.69 |
| B thesis-diversified (joint) ← optimiser card | 148.42 | +22.81 | +8.66 | +20.43 | 0.755 | -15.71 | -24.30 | 81.47 |
| C best expression per thesis | 149.99 | +21.58 | +8.27 | +17.33 | 0.704 | -22.91 | -33.42 | 75.75 |
| R FUNDED research stakes | 21.00 | +2.58 | +1.44 | +0.23 | 0.515 | -5.67 | -7.61 | 0.00 |

## NSH @ TOR  ·  10000 joint draws  ·  388 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NSH_win | p_overtime | goals | shots TOR/NSH | TOR/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 5.99 | 28.7/29.1 | 25.4/25.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.47 | 0.53 | 0.46 | 5.92 | 28.5/28.9 | 25.6/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.52 | 0.48 | 0.00 | 9.2 | 29.9/30.4 | 24.5/23.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.085 | 0.46 | 0.54 | 0.00 | 6.0 | 22.9/34.5 | 30.4/19.6 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.47 | 0.53 | 0.47 | 5.88 | 22.9/34.3 | 30.9/19.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.54 | 0.46 | 0.00 | 3.46 | 27.5/27.7 | 25.9/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ goals YES | 17 | 0.219 | 0.206 | +0.039 | +0.026 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 79 | 0.845 | 0.826 | +0.043 | +0.025 | $6.52 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ assists NO | 68 | 0.824 | 0.721 | +0.129 | +0.025 | $6.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ goals NO | 62 | 0.660 | 0.648 | +0.023 | +0.012 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (9.72 vs 3.23 bp); despite a smaller raw edge (+0.039 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: NSH offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (8.44 vs 3.23 bp); despite a smaller raw edge (+0.043 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense succeeds (4+ goals)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (6.65 vs 3.23 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.029); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over broad KXNHLSPREAD-26OCT06NSHTOR-TOR2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.77 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.029); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.381): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3971): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06NSHTOR-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.5022): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06NSHTOR-TOR2|no (same contract)
- KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.214)
- KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.174)
- KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.9 pts; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.185)
- KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.283)
- override: Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over broad KXNHLSPREAD-26OCT06NSHTOR-TOR2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.77 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.86 (adj +0.55) on $16.87, P(profit) 0.6232, adj growth 5.0 bp · B EV +2.37 (adj +0.96) on $18.59, P(profit) 0.5766, adj growth 9.1 bp · C EV +1.95 (adj +1.05) on $26.06, P(profit) 0.2192, adj growth 9.7 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.845, adj growth 2.4 bp

## CAR @ MTL  ·  10000 joint draws  ·  408 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_CAR_win | p_overtime | goals | shots MTL/CAR | MTL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.153 | 0.50 | 0.50 | 0.00 | 5.98 | 20.8/33.6 | 29.9/17.4 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.135 | 0.49 | 0.51 | 0.45 | 5.89 | 20.8/33.2 | 29.7/17.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.094 | 0.58 | 0.42 | 0.00 | 6.08 | 26.4/27.3 | 24.0/22.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.092 | 0.47 | 0.53 | 0.00 | 9.13 | 22.2/35.3 | 28.6/16.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.55 | 0.45 | 0.48 | 5.95 | 26.1/27.1 | 23.8/22.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.59 | 0.41 | 0.00 | 9.29 | 28.1/29.3 | 23.7/21.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alexandre Texier: 1+ goals YES | 11 | 0.145 | 0.132 | +0.028 | +0.016 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 74 | 0.862 | 0.770 | +0.109 | +0.016 | $10.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Jake Evans: 1+ goals YES | 12 | 0.153 | 0.140 | +0.026 | +0.012 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 70 | 0.743 | 0.730 | +0.028 | +0.015 | $6.67 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (5.07 vs 2.98 bp); relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: MTL offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06CARMTL-MTLIDEMIDOV93-1|no; why: higher confidence-adjusted growth (3.16 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: MTL offense succeeds (4+ goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26OCT06CARMTL-CAR3|no; why: higher confidence-adjusted growth (2.98 vs 0.70 bp); despite a smaller raw edge (+0.026 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: MTL offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no; why: higher confidence-adjusted growth (2.46 vs 1.28 bp); relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis MTL:OFFENSE_4PLUS (p 0.4006): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.302): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.4189): highest fidelity KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3836, phi -0.191)
- KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4006, phi -0.187)
- KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3836, phi -0.206)
- KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3607, phi -0.236)

portfolios: A EV +2.21 (adj +0.56) on $16.87, P(profit) 0.5257, adj growth 5.3 bp · B EV +2.57 (adj +0.80) on $20.58, P(profit) 0.7297, adj growth 7.5 bp · C EV +0.80 (adj +0.40) on $11.27, P(profit) 0.7787, adj growth 3.7 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.7431, adj growth 1.6 bp

## OTT @ DET  ·  10000 joint draws  ·  386 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_OTT_win | p_overtime | goals | shots DET/OTT | DET/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.57 | 0.43 | 0.00 | 6.0 | 27.0/27.2 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.46 | 5.89 | 27.1/27.2 | 24.0/23.8 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.084 | 0.47 | 0.53 | 0.00 | 5.98 | 21.6/32.2 | 28.4/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.55 | 0.45 | 0.00 | 9.3 | 28.5/28.8 | 23.2/22.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.51 | 0.49 | 0.46 | 5.84 | 21.7/32.3 | 29.1/18.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.51 | 0.49 | 0.00 | 3.44 | 25.8/25.9 | 24.1/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carter Yakemchuk: 1+ goals NO | 89 | 0.935 | 0.920 | +0.038 | +0.023 | $7.62 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 65 | 0.823 | 0.698 | +0.157 | +0.032 | $7.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| J.T. Compher: 1+ goals YES | 15 | 0.182 | 0.170 | +0.023 | +0.011 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ assists YES | 28 | 0.345 | 0.305 | +0.051 | +0.011 | $1.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Carter Yakemchuk: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no; why: higher confidence-adjusted growth (12.73 vs 9.89 bp); despite a smaller raw edge (+0.038 vs +0.157/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: OTT offense succeeds (4+ goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (9.89 vs 0.98 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: OTT offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (2.00 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: DET offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT06OTTDET-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (1.26 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis OTT:SUPPRESSED (p 0.4379): highest fidelity KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3423): highest fidelity KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3862): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3423, phi -0.11)
- KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.3 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3423, phi -0.198)
- KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3976, phi -0.201)
- KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4379, phi -0.26)

portfolios: A EV +2.72 (adj +0.49) on $16.87, P(profit) 0.7568, adj growth 4.6 bp · B EV +2.68 (adj +0.74) on $18.78, P(profit) 0.7962, adj growth 7.2 bp · C EV +3.68 (adj +0.75) on $16.31, P(profit) 0.823, adj growth 7.1 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.9347, adj growth 2.0 bp

## UTA @ NJD  ·  10000 joint draws  ·  414 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_UTA_win | p_overtime | goals | shots NJD/UTA | NJD/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.44 | 0.56 | 0.00 | 5.97 | 27.6/27.4 | 23.5/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.46 | 5.87 | 28.0/27.7 | 24.3/24.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.088 | 0.53 | 0.47 | 0.00 | 5.98 | 32.9/22.0 | 18.8/29.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.55 | 0.45 | 0.44 | 5.89 | 33.2/22.1 | 19.0/29.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.48 | 0.52 | 0.00 | 9.28 | 29.6/29.2 | 22.8/23.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.058 | 0.47 | 0.53 | 0.50 | 2.82 | 26.5/26.3 | 24.7/25.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 67 | 0.831 | 0.720 | +0.146 | +0.034 | $10.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Luke Evangelista: 1+ goals NO | 77 | 0.815 | 0.803 | +0.033 | +0.020 | $10.17 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 17 | 0.210 | 0.196 | +0.030 | +0.016 | $2.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.148 | 0.138 | +0.020 | +0.011 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06UTANJ-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (12.10 vs 0.49 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: UTA offense succeeds (4+ goals)
- **Luke Evangelista: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (5.39 vs 3.17 bp); despite a smaller raw edge (+0.033 vs +0.126/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NJD offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06UTANJ-NJ3|no; why: higher confidence-adjusted growth (3.83 vs 1.87 bp); despite a smaller raw edge (+0.030 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06UTANJ-9|yes; why: higher confidence-adjusted growth (2.31 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.898 vs 0.371); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4261): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3833): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:WINS (p 0.5166): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06UTANJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.1 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3833, phi -0.177)
- KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3485, phi -0.187)
- KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3974, phi -0.229)
- KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4261, phi -0.183)

portfolios: A EV +2.58 (adj +0.48) on $16.87, P(profit) 0.7629, adj growth 4.6 bp · B EV +3.21 (adj +1.11) on $24.13, P(profit) 0.7715, adj growth 10.6 bp · C EV +1.46 (adj +0.74) on $24.51, P(profit) 0.7446, adj growth 6.8 bp · R EV +0.13 (adj +0.08) on $3.00, P(profit) 0.8154, adj growth 3.0 bp

## MIN @ BUF  ·  10000 joint draws  ·  396 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_MIN_win | p_overtime | goals | shots BUF/MIN | BUF/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.50 | 0.50 | 0.00 | 6.0 | 28.9/28.7 | 25.2/25.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.49 | 5.99 | 28.8/28.7 | 25.3/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.51 | 0.49 | 0.00 | 9.33 | 30.3/30.2 | 24.1/24.0 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.087 | 0.57 | 0.43 | 0.00 | 6.0 | 33.9/22.6 | 19.6/29.7 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.53 | 0.47 | 0.47 | 5.91 | 34.4/22.9 | 19.6/31.1 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.062 | 0.54 | 0.46 | 0.00 | 9.25 | 36.1/24.4 | 19.0/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 10 | 0.145 | 0.130 | +0.039 | +0.024 | $2.75 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 21 | 0.353 | 0.250 | +0.131 | +0.029 | $3.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Jiri Kulich: 1+ goals YES | 15 | 0.187 | 0.176 | +0.028 | +0.017 | $2.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Marcus Foligno: 1+ goals YES | 10 | 0.129 | 0.120 | +0.022 | +0.014 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (12.80 vs 10.30 bp); despite a smaller raw edge (+0.039 vs +0.131/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-2|yes; why: higher confidence-adjusted growth (10.30 vs 2.43 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; wins across more scripts (relative breadth 0.943 vs 0.79); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi 0.042); failure: MIN offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (4.83 vs 3.70 bp); relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: BUF offense suppressed (<= 2 goals)
- **Marcus Foligno: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (10.30 vs 4.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.042); they share one thesis budget; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.042); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4096): highest fidelity KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3794): highest fidelity KXNHLAST-26OCT06MINBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.176)
- KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.284)
- KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3794, phi -0.187)
- KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.169)

portfolios: A EV +5.82 (adj +1.79) on $16.87, P(profit) 0.4887, adj growth 16.2 bp · B EV +3.64 (adj +1.52) on $10.10, P(profit) 0.5888, adj growth 14.1 bp · C EV +4.26 (adj +1.09) on $13.06, P(profit) 0.474, adj growth 10.0 bp · R EV +0.37 (adj +0.22) on $1.00, P(profit) 0.1452, adj growth 8.1 bp

## NYI @ NYR  ·  10000 joint draws  ·  408 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_NYI_win | p_overtime | goals | shots NYR/NYI | NYR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.64 | 0.36 | 0.00 | 6.0 | 26.6/26.8 | 23.9/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.56 | 0.44 | 0.47 | 5.9 | 26.7/26.9 | 23.8/23.3 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.088 | 0.54 | 0.46 | 0.00 | 5.99 | 21.4/32.3 | 28.8/17.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.48 | 0.52 | 0.47 | 5.79 | 21.4/32.3 | 28.9/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.60 | 0.40 | 0.00 | 9.15 | 28.4/28.7 | 23.5/22.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.58 | 0.42 | 0.00 | 3.48 | 25.2/25.7 | 24.1/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kyle Palmieri: 1+ assists NO | 74 | 0.825 | 0.775 | +0.071 | +0.021 | $10.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Matt Rempe: 1+ goals YES | 7 | 0.097 | 0.085 | +0.022 | +0.011 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Bo Horvat: 1+ goals NO | 69 | 0.727 | 0.715 | +0.022 | +0.010 | $2.71 | FUNDED_RESEARCH | $1 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Kyle Palmieri: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no; why: higher confidence-adjusted growth (5.47 vs 1.10 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: REINFORCING (phi 0.208); failure: NYI offense succeeds (4+ goals)
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (3.62 vs 0.00 bp); despite a smaller raw edge (+0.023 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0005 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no; why: second expression of the same thesis: KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no has the higher standalone adjusted growth (5.47 vs 1.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.208); they share one thesis budget; relationships: KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no: REINFORCING (phi 0.208); KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:SUPPRESSED (p 0.4835): highest fidelity KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4001): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2998, phi -0.204)
- KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.383, phi -0.144)
- KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2998, phi -0.231)

portfolios: A EV +1.46 (adj +0.58) on $15.07, P(profit) 0.671, adj growth 5.3 bp · B EV +1.44 (adj +0.52) on $14.17, P(profit) 0.671, adj growth 4.9 bp · C EV +1.30 (adj +0.39) on $13.67, P(profit) 0.8249, adj growth 3.7 bp · R EV +0.03 (adj +0.01) on $1.00, P(profit) 0.7269, adj growth 0.5 bp

## STL @ CHI  ·  10000 joint draws  ·  374 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_STL_win | p_overtime | goals | shots CHI/STL | CHI/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.41 | 0.59 | 0.00 | 6.0 | 26.4/26.7 | 22.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.46 | 0.54 | 0.47 | 5.91 | 26.4/26.6 | 23.4/23.2 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.35 | 0.65 | 0.00 | 5.95 | 20.9/31.4 | 27.0/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.41 | 0.59 | 0.00 | 9.36 | 27.9/28.2 | 21.5/22.3 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.43 | 0.57 | 0.50 | 5.95 | 21.5/31.8 | 28.4/18.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.058 | 0.49 | 0.51 | 0.51 | 2.85 | 25.0/25.4 | 23.9/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.177 | 0.158 | +0.060 | +0.041 | $5.21 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 61 | 0.732 | 0.643 | +0.106 | +0.016 | $6.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Pius Suter: 1+ goals YES | 15 | 0.177 | 0.169 | +0.018 | +0.010 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 69 | 0.789 | 0.715 | +0.085 | +0.010 | $4.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06STLCHI-10|yes; why: higher confidence-adjusted growth (34.74 vs 0.75 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.295); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi 0.031); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06STLCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (2.52 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: CHI offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06STLCHI-10|yes; why: higher confidence-adjusted growth (1.65 vs 0.75 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.876 vs 0.295); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.039); failure: STL offense suppressed (<= 2 goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (1.08 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.031); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.039); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.3298): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4532): highest fidelity KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4275): highest fidelity KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes (same contract)
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4532, phi -0.228)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3298, phi -0.236)
- KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3631, phi -0.207)
- KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.4 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4275, phi -0.19)

portfolios: A EV +4.12 (adj +1.94) on $16.87, P(profit) 0.2846, adj growth 18.1 bp · B EV +4.63 (adj +2.19) on $18.56, P(profit) 0.2846, adj growth 20.2 bp · C EV +5.45 (adj +2.86) on $18.40, P(profit) 0.2846, adj growth 25.7 bp · R EV +1.04 (adj +0.71) on $2.00, P(profit) 0.1774, adj growth 24.9 bp

## VGK @ SEA  ·  10000 joint draws  ·  272 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_VGK_win | p_overtime | goals | shots SEA/VGK | SEA/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.49 | 0.51 | 0.00 | 5.99 | 26.9/27.1 | 23.5/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.46 | 5.91 | 27.0/27.3 | 24.0/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.095 | 0.40 | 0.60 | 0.00 | 5.99 | 21.3/32.3 | 28.0/18.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.48 | 0.52 | 0.48 | 5.85 | 21.4/32.5 | 29.1/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.51 | 0.49 | 0.00 | 9.25 | 28.6/29.1 | 22.8/22.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.52 | 0.48 | 0.00 | 3.44 | 25.6/26.0 | 24.2/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vegas wins by over 1.5 goals NO | 62 | 0.710 | 0.662 | +0.073 | +0.026 | $7.52 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 75 | 0.818 | 0.781 | +0.055 | +0.018 | $2.37 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (6.37 vs 4.04 bp); relationships: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: DUPLICATIVE (phi 0.738); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no has the higher standalone adjusted growth (6.37 vs 4.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.738); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: DUPLICATIVE (phi 0.738); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:WINS (p 0.4852): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2672): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.4075): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2902, phi -1.0)
- KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2902, phi -0.738)

portfolios: A EV +1.91 (adj +0.59) on $16.87, P(profit) 0.3983, adj growth 5.1 bp · B EV +1.04 (adj +0.36) on $9.89, P(profit) 0.7098, adj growth 3.4 bp · C EV +1.50 (adj +0.53) on $13.04, P(profit) 0.7098, adj growth 4.9 bp · R EV +0.30 (adj +0.11) on $3.00, P(profit) 0.7098, adj growth 3.9 bp

## FLA @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_FLA_win | p_overtime | goals | shots LAK/FLA | LAK/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.61 | 0.39 | 0.00 | 5.99 | 27.1/27.0 | 24.0/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 5.9 | 27.4/27.2 | 23.8/24.0 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.080 | 0.70 | 0.30 | 0.00 | 5.97 | 32.2/21.6 | 19.0/27.6 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.55 | 0.45 | 0.45 | 5.85 | 32.1/21.4 | 18.3/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.63 | 0.37 | 0.00 | 9.16 | 28.6/28.4 | 23.1/22.1 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.51 | 0.49 | 0.49 | 2.81 | 25.8/25.5 | 23.9/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 80 | 0.881 | 0.838 | +0.070 | +0.027 | $6.87 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 70 | 0.791 | 0.743 | +0.076 | +0.028 | $5.02 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida over 4.5 goals scored NO | 80 | 0.860 | 0.825 | +0.049 | +0.014 | $1.73 | FUNDED_RESEARCH | $1 | LAK:WINS | DIRECT (0.98) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA2|no; why: higher confidence-adjusted growth (10.55 vs 8.69 bp); despite a smaller raw edge (+0.070 vs +0.076/contract); relationships: KXNHLSPREAD-26OCT06FLALA-FLA2|no: DUPLICATIVE (phi 0.714); KXNHLTEAMTOTAL-26OCT06FLALA-FLA5|no: REINFORCING (phi 0.493); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (10.55 vs 8.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.714); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06FLALA-FLA3|no: DUPLICATIVE (phi 0.714); KXNHLTEAMTOTAL-26OCT06FLALA-FLA5|no: REINFORCING (phi 0.461); failure: FLA wins by 2+
- **Florida over 4.5 goals scored NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (10.55 vs 2.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.493); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06FLALA-FLA3|no: REINFORCING (phi 0.493); KXNHLSPREAD-26OCT06FLALA-FLA2|no: REINFORCING (phi 0.461); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:WINS (p 0.582): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- thesis LAK:WINS_BY_2PLUS (p 0.3455): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- thesis FLA:SUPPRESSED (p 0.4897): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT06FLALA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2089, phi -0.714)
- KXNHLSPREAD-26OCT06FLALA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2089, phi -1.0)
- KXNHLTEAMTOTAL-26OCT06FLALA-FLA5|no: FUNDED_RESEARCH; family MIXED; loses 2% of the draws where the thesis happens; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2917, phi -0.628)

portfolios: A EV +1.87 (adj +0.60) on $16.87, P(profit) 0.6613, adj growth 5.5 bp · B EV +1.24 (adj +0.46) on $13.62, P(profit) 0.7911, adj growth 4.4 bp · C EV +1.18 (adj +0.46) on $13.67, P(profit) 0.8814, adj growth 4.4 bp · R EV +0.45 (adj +0.16) on $5.00, P(profit) 0.7911, adj growth 6.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
