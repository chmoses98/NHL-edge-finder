# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T14:47:03Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +29.75 | +8.32 | +27.44 | 0.773 | -16.88 | -27.41 | 76.37 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +25.19 | +10.47 | +23.30 | 0.770 | -15.87 | -26.33 | 99.18 |
| C best expression per thesis | 149.99 | +21.87 | +8.07 | +19.61 | 0.750 | -15.93 | -25.02 | 75.80 |
| R FUNDED research stakes | 21.00 | +1.76 | +0.97 | +1.22 | 0.613 | -4.69 | -6.10 | 0.00 |

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
| Mavrik Bourque: 1+ goals YES | 17 | 0.219 | 0.204 | +0.039 | +0.025 | $3.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 79 | 0.845 | 0.826 | +0.043 | +0.025 | $8.90 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 11 | 0.134 | 0.127 | +0.018 | +0.010 | $1.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 62 | 0.660 | 0.647 | +0.023 | +0.011 | $3.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (8.81 vs 3.23 bp); despite a smaller raw edge (+0.039 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: NSH offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NSHTOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (8.44 vs 3.36 bp); despite a smaller raw edge (+0.043 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06NSHTOR-9|yes; why: higher confidence-adjusted growth (2.18 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.884 vs 0.363); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NSHTOR-TORAMATTHEWS34-1|no; why: Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT06NSHTOR-TORAMATTHEWS34-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.83 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.381): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3971): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT06NSHTOR-TORAMATTHEWS34-1|no — Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT06NSHTOR-TORAMATTHEWS34-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.83 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NSH:WINS (p 0.5022): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06NSHTOR-TOR2|no (same contract)
- KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.214)
- KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.174)
- KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3971, phi -0.17)
- KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.283)
- override: Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT06NSHTOR-TORAMATTHEWS34-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.83 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.92 (adj +0.55) on $17.66, P(profit) 0.6232, adj growth 5.0 bp · B EV +1.46 (adj +0.86) on $16.44, P(profit) 0.3086, adj growth 8.1 bp · C EV +1.95 (adj +0.89) on $24.02, P(profit) 0.5975, adj growth 8.4 bp · R EV +0.16 (adj +0.09) on $3.00, P(profit) 0.845, adj growth 3.5 bp

## CAR @ MTL  ·  10000 joint draws  ·  408 bet sides mapped, 4 +EV candidates, 4 on card


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
| Alexandre Texier: 1+ goals YES | 11 | 0.145 | 0.132 | +0.028 | +0.016 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 74 | 0.862 | 0.770 | +0.109 | +0.016 | $8.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Jake Evans: 1+ goals YES | 12 | 0.153 | 0.140 | +0.026 | +0.012 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Logan Stankoven: 1+ goals NO | 74 | 0.773 | 0.764 | +0.020 | +0.010 | $4.44 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (5.07 vs 2.98 bp); relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06CARMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (3.16 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: MTL offense succeeds (4+ goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26OCT06CARMTL-CAR3|no; why: higher confidence-adjusted growth (2.98 vs 0.70 bp); despite a smaller raw edge (+0.026 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no: MOSTLY_INDEPENDENT (phi 0.032); failure: MTL offense suppressed (<= 2 goals)
- **Logan Stankoven: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no; why: higher confidence-adjusted growth (1.28 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.032); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis MTL:OFFENSE_4PLUS (p 0.4006): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.302): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.4189): highest fidelity KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no (same contract)
- KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3836, phi -0.191)
- KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4006, phi -0.187)
- KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3836, phi -0.206)
- KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3607, phi -0.223)

portfolios: A EV +2.17 (adj +0.79) on $17.66, P(profit) 0.2729, adj growth 7.3 bp · B EV +2.14 (adj +0.64) on $16.63, P(profit) 0.7502, adj growth 6.1 bp · C EV +0.47 (adj +0.23) on $6.96, P(profit) 0.8033, adj growth 2.2 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.7735, adj growth 1.0 bp

## OTT @ DET  ·  10000 joint draws  ·  386 bet sides mapped, 8 +EV candidates, 4 on card


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
| Carter Yakemchuk: 1+ goals NO | 87 | 0.935 | 0.916 | +0.057 | +0.038 | $6.68 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 68 | 0.823 | 0.724 | +0.128 | +0.028 | $6.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Jordan Spence: 1+ assists YES | 26 | 0.345 | 0.300 | +0.072 | +0.027 | $3.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| J.T. Compher: 1+ goals YES | 15 | 0.182 | 0.170 | +0.023 | +0.011 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Carter Yakemchuk: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no; why: higher confidence-adjusted growth (30.64 vs 8.33 bp); despite a smaller raw edge (+0.057 vs +0.128/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: OTT offense succeeds (4+ goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (8.33 vs 3.13 bp); relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: OTT offense succeeds (4+ goals)
- **Jordan Spence: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT06OTTDET-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (7.72 vs 0.28 bp); despite a smaller raw edge (+0.072 vs +0.081/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: OTT offense suppressed (<= 2 goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (2.00 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis OTT:SUPPRESSED (p 0.4379): highest fidelity KXNHLAST-26OCT06OTTDET-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3423): highest fidelity KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3862): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3423, phi -0.11)
- KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.3 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3423, phi -0.198)
- KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4379, phi -0.26)
- KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3976, phi -0.201)

portfolios: A EV +3.62 (adj +0.85) on $17.66, P(profit) 0.7568, adj growth 8.1 bp · B EV +2.81 (adj +1.01) on $18.33, P(profit) 0.4304, adj growth 9.8 bp · C EV +3.36 (adj +0.96) on $25.00, P(profit) 0.8811, adj growth 9.1 bp · R EV +0.13 (adj +0.09) on $2.00, P(profit) 0.9347, adj growth 3.4 bp

## UTA @ NJD  ·  10000 joint draws  ·  414 bet sides mapped, 10 +EV candidates, 4 on card


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
| Vincent Trocheck: 1+ assists NO | 67 | 0.831 | 0.720 | +0.146 | +0.034 | $8.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 16 | 0.210 | 0.196 | +0.040 | +0.027 | $3.31 | FUNDED_RESEARCH | $1 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 65 | 0.802 | 0.690 | +0.136 | +0.024 | $8.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 12 | 0.148 | 0.138 | +0.020 | +0.011 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06UTANJ-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (12.10 vs 0.49 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06UTANJ-NJ3|no; why: higher confidence-adjusted growth (10.85 vs 1.87 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (5.84 vs 2.36 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT06UTANJ-3|yes; why: higher confidence-adjusted growth (2.31 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.898 vs 0.793); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3833): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4261): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:WINS (p 0.5166): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06UTANJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.1 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3833, phi -0.177)
- KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3974, phi -0.229)
- KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.2 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3485, phi -0.213)
- KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4261, phi -0.183)

portfolios: A EV +2.90 (adj +0.55) on $17.66, P(profit) 0.7551, adj growth 5.4 bp · B EV +4.67 (adj +1.39) on $22.25, P(profit) 0.7662, adj growth 13.3 bp · C EV +3.21 (adj +1.02) on $18.50, P(profit) 0.7445, adj growth 9.6 bp · R EV +0.24 (adj +0.16) on $1.00, P(profit) 0.2097, adj growth 5.8 bp

## MIN @ BUF  ·  10000 joint draws  ·  396 bet sides mapped, 7 +EV candidates, 4 on card


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
| Ryan Hartman: 1+ assists YES | 20 | 0.353 | 0.247 | +0.142 | +0.036 | $3.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.145 | 0.130 | +0.039 | +0.024 | $2.34 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 15 | 0.187 | 0.176 | +0.028 | +0.017 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Marcus Foligno: 1+ goals YES | 10 | 0.129 | 0.120 | +0.022 | +0.014 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (16.60 vs 1.68 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi 0.042); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (16.60 vs 12.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.128); they share one thesis budget; relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MIN offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (4.83 vs 3.70 bp); relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: BUF offense suppressed (<= 2 goals)
- **Marcus Foligno: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (16.60 vs 4.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.042); they share one thesis budget; relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.042); KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4096): highest fidelity KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes (same contract)
- KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.3 pts; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.284)
- KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.176)
- KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3794, phi -0.187)
- KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.169)

portfolios: A EV +7.42 (adj +2.21) on $17.66, P(profit) 0.4519, adj growth 19.2 bp · B EV +3.84 (adj +1.54) on $9.44, P(profit) 0.5888, adj growth 14.4 bp · C EV +3.74 (adj +1.21) on $17.30, P(profit) 0.4693, adj growth 11.3 bp · R EV +0.37 (adj +0.22) on $1.00, P(profit) 0.1452, adj growth 8.1 bp

## NYI @ NYR  ·  10000 joint draws  ·  408 bet sides mapped, 2 +EV candidates, 2 on card


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
| Matt Rempe: 1+ goals YES | 7 | 0.097 | 0.090 | +0.022 | +0.016 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Bo Horvat: 1+ goals NO | 69 | 0.727 | 0.715 | +0.022 | +0.010 | $3.96 | FUNDED_RESEARCH | $1 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (7.71 vs 0.10 bp); despite a smaller raw edge (+0.023 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYIMMACCELLI63-1|no; why: higher confidence-adjusted growth (1.10 vs 0.36 bp); despite a smaller raw edge (+0.022 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:SUPPRESSED (p 0.4835): highest fidelity KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4001): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.383, phi -0.144)
- KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2998, phi -0.231)

portfolios: A EV +0.85 (adj +0.55) on $8.71, P(profit) 0.7538, adj growth 5.1 bp · B EV +0.65 (adj +0.43) on $5.71, P(profit) 0.0971, adj growth 4.0 bp · C EV +0.14 (adj +0.07) on $4.55, P(profit) 0.7269, adj growth 0.6 bp · R EV +0.03 (adj +0.01) on $1.00, P(profit) 0.7269, adj growth 0.5 bp

## STL @ CHI  ·  10000 joint draws  ·  374 bet sides mapped, 6 +EV candidates, 4 on card


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
| Ryan Greene: 1+ goals YES | 11 | 0.177 | 0.159 | +0.060 | +0.042 | $4.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Adam Jiricek: 1+ goals NO | 90 | 0.941 | 0.929 | +0.035 | +0.023 | $8.90 | FUNDED_RESEARCH | $3 | STL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ goals YES | 7 | 0.099 | 0.090 | +0.024 | +0.016 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 61 | 0.732 | 0.643 | +0.106 | +0.016 | $6.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06STLCHI-10|yes; why: higher confidence-adjusted growth (36.84 vs 0.75 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.295); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: CHI offense suppressed (<= 2 goals)
- **Adam Jiricek: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (14.06 vs 0.04 bp); alternative not eligible: confidence-adjusted EV +0.0017 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: STL offense succeeds (4+ goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes; why: higher confidence-adjusted growth (7.88 vs 1.65 bp); relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT06STLCHI-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: STL offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06STLCHI-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (2.52 vs 0.73 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0074 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT06STLCHI-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.3298): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4532): highest fidelity KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4275): highest fidelity KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes (same contract)
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4532, phi -0.228)
- KXNHLGOAL-26OCT06STLCHI-STLAJIRICEK36-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4275, phi -0.112)
- KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3631, phi -0.125)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3298, phi -0.236)

portfolios: A EV +3.53 (adj +1.73) on $17.66, P(profit) 0.6244, adj growth 16.4 bp · B EV +4.44 (adj +2.50) on $21.62, P(profit) 0.2607, adj growth 23.5 bp · C EV +4.21 (adj +2.28) on $14.05, P(profit) 0.2846, adj growth 21.0 bp · R EV +0.11 (adj +0.08) on $3.00, P(profit) 0.9408, adj growth 3.0 bp

## VGK @ SEA  ·  10000 joint draws  ·  390 bet sides mapped, 12 +EV candidates, 4 on card


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
| Ryan Winterton: 1+ goals YES | 10 | 0.144 | 0.129 | +0.038 | +0.023 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 67 | 0.726 | 0.711 | +0.040 | +0.025 | $7.90 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Vegas wins by over 1.5 goals NO | 62 | 0.710 | 0.662 | +0.073 | +0.026 | $5.73 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Freddy Gaudreau: 1+ goals YES | 8 | 0.114 | 0.099 | +0.028 | +0.014 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: higher confidence-adjusted growth (11.86 vs 6.37 bp); despite a smaller raw edge (+0.038 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06VGKSEA-VGKJEICHEL9-2|no; why: KXNHLAST-26OCT06VGKSEA-VGKJEICHEL9-2|no has the higher standalone adjusted growth (7.32 vs 6.40 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.018); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (6.37 vs 4.04 bp); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26OCT06VGKSEA-VGKJEICHEL9-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.105); failure: VGK wins by 2+
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no has the higher standalone adjusted growth (6.37 vs 5.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.105); they share one thesis budget; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06VGKSEA-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: MOSTLY_INDEPENDENT (phi 0.105); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4075): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3504): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4852): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4256, phi -0.167)
- KXNHLGOAL-26OCT06VGKSEA-VGKJEICHEL9-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3781, phi -0.251)
- KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2902, phi -1.0)
- KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4256, phi -0.163)

portfolios: A EV +3.14 (adj +0.53) on $17.66, P(profit) 0.6858, adj growth 4.8 bp · B EV +2.41 (adj +1.25) on $17.33, P(profit) 0.6294, adj growth 11.8 bp · C EV +1.83 (adj +0.61) on $19.04, P(profit) 0.6694, adj growth 5.8 bp · R EV +0.35 (adj +0.15) on $4.00, P(profit) 0.5475, adj growth 5.8 bp

## FLA @ LAK  ·  10000 joint draws  ·  414 bet sides mapped, 17 +EV candidates, 3 on card


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
| Florida wins by over 1.5 goals NO | 70 | 0.791 | 0.743 | +0.076 | +0.028 | $7.94 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 1+ assists NO | 64 | 0.788 | 0.685 | +0.132 | +0.029 | $7.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Matthew Tkachuk: 1+ goals NO | 71 | 0.763 | 0.746 | +0.038 | +0.021 | $6.37 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Florida wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (10.55 vs 8.69 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.714); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.112); KXNHLGOAL-26OCT06FLALA-FLAMTKACHUK19-1|no: REINFORCING (phi 0.173); failure: FLA wins by 2+
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (8.23 vs 1.60 bp); relationships: KXNHLSPREAD-26OCT06FLALA-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.112); KXNHLGOAL-26OCT06FLALA-FLAMTKACHUK19-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: LAK offense succeeds (4+ goals)
- **Matthew Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (10.55 vs 5.03 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.149); relationships: KXNHLSPREAD-26OCT06FLALA-FLA2|no: REINFORCING (phi 0.173); KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:WINS (p 0.582): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- thesis FLA:SUPPRESSED (p 0.4897): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3455): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- KXNHLSPREAD-26OCT06FLALA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2089, phi -1.0)
- KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4056, phi -0.207)
- KXNHLGOAL-26OCT06FLALA-FLAMTKACHUK19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2917, phi -0.231)

portfolios: A EV +3.21 (adj +0.56) on $17.66, P(profit) 0.814, adj growth 5.3 bp · B EV +2.78 (adj +0.85) on $22.25, P(profit) 0.6045, adj growth 8.2 bp · C EV +2.95 (adj +0.80) on $20.57, P(profit) 0.6826, adj growth 7.7 bp · R EV +0.32 (adj +0.14) on $4.00, P(profit) 0.6333, adj growth 5.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
