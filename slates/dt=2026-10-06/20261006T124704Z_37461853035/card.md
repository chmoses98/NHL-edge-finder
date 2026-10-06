# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T12:47:04Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +24.58 | +9.50 | +20.15 | 0.699 | -26.14 | -36.83 | 86.13 |
| B thesis-diversified (joint) ← optimiser card | 149.03 | +21.88 | +8.96 | +19.84 | 0.728 | -19.46 | -29.58 | 83.62 |
| C best expression per thesis | 150.00 | +20.96 | +8.17 | +14.47 | 0.648 | -30.54 | -42.19 | 72.66 |
| R FUNDED research stakes | 24.00 | +3.04 | +1.58 | +2.24 | 0.572 | -6.58 | -8.37 | 0.00 |

## NSH @ TOR  ·  10000 joint draws  ·  388 bet sides mapped, 9 +EV candidates, 4 on card


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
| Gavin McKenna: 1+ goals NO | 78 | 0.845 | 0.825 | +0.053 | +0.033 | $7.22 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 17 | 0.219 | 0.203 | +0.039 | +0.023 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ assists NO | 67 | 0.824 | 0.711 | +0.138 | +0.025 | $7.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ goals NO | 62 | 0.660 | 0.648 | +0.023 | +0.012 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR3|no; why: higher confidence-adjusted growth (14.66 vs 2.38 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR3|no; why: higher confidence-adjusted growth (7.94 vs 2.38 bp); despite a smaller raw edge (+0.039 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: NSH offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR3|no; why: higher confidence-adjusted growth (6.54 vs 2.38 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.029); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR3|no; why: Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over broad KXNHLSPREAD-26OCT06NSHTOR-TOR2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.77 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.029); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.381): highest fidelity KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3971): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06NSHTOR-TOR3|no (same contract)
- thesis NSH:WINS (p 0.5022): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06NSHTOR-TOR3|no (same contract)
- KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.174)
- KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.214)
- KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.4 pts; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.185)
- KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.283)
- override: Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over broad KXNHLSPREAD-26OCT06NSHTOR-TOR2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.77 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.25 (adj +0.68) on $19.82, P(profit) 0.5897, adj growth 6.2 bp · B EV +2.76 (adj +1.05) on $20.27, P(profit) 0.5766, adj growth 10.0 bp · C EV +2.31 (adj +1.17) on $36.52, P(profit) 0.2188, adj growth 10.5 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.845, adj growth 3.3 bp

## CAR @ MTL  ·  10000 joint draws  ·  408 bet sides mapped, 7 +EV candidates, 4 on card


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
| Alexandre Texier: 1+ goals YES | 11 | 0.145 | 0.132 | +0.028 | +0.016 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 73 | 0.862 | 0.760 | +0.118 | +0.016 | $11.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Jake Evans: 1+ goals YES | 12 | 0.153 | 0.140 | +0.026 | +0.012 | $1.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 74 | 0.782 | 0.769 | +0.028 | +0.015 | $8.80 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (5.07 vs 2.98 bp); relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: MTL offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06CARMTL-MTLIDEMIDOV93-1|no; why: higher confidence-adjusted growth (3.05 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: MTL offense succeeds (4+ goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26OCT06CARMTL-CAR3|no; why: higher confidence-adjusted growth (2.98 vs 0.70 bp); despite a smaller raw edge (+0.026 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: MTL offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no; why: higher confidence-adjusted growth (2.77 vs 2.46 bp); despite a smaller raw edge (+0.028 vs +0.028/contract); relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis MTL:OFFENSE_4PLUS (p 0.4006): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.302): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.4189): highest fidelity KXNHLGOAL-26OCT06CARMTL-CARLSTANKOVEN22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3836, phi -0.191)
- KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.7 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4006, phi -0.187)
- KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3836, phi -0.206)
- KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3607, phi -0.209)

portfolios: A EV +1.94 (adj +0.68) on $19.82, P(profit) 0.5712, adj growth 6.4 bp · B EV +3.05 (adj +0.91) on $24.24, P(profit) 0.7585, adj growth 8.5 bp · C EV +1.13 (adj +0.58) on $17.41, P(profit) 0.813, adj growth 5.1 bp · R EV +0.11 (adj +0.06) on $3.00, P(profit) 0.7817, adj growth 2.2 bp

## OTT @ DET  ·  10000 joint draws  ·  386 bet sides mapped, 3 +EV candidates, 3 on card


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
| Carter Yakemchuk: 1+ goals NO | 88 | 0.935 | 0.916 | +0.047 | +0.029 | $9.58 | FUNDED_RESEARCH | $3 | OTT:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 67 | 0.823 | 0.701 | +0.138 | +0.015 | $7.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| J.T. Compher: 1+ goals YES | 15 | 0.182 | 0.170 | +0.023 | +0.011 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Carter Yakemchuk: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no; why: higher confidence-adjusted growth (18.44 vs 2.39 bp); despite a smaller raw edge (+0.047 vs +0.138/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: OTT offense succeeds (4+ goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06OTTDET-OTT3|no; why: higher confidence-adjusted growth (2.39 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: OTT offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (2.00 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis OTT:SUPPRESSED (p 0.4379): highest fidelity KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3862): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3423, phi -0.11)
- KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3423, phi -0.198)
- KXNHLGOAL-26OCT06OTTDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3976, phi -0.201)

portfolios: A EV +2.40 (adj +0.62) on $18.54, P(profit) 0.8142, adj growth 5.9 bp · B EV +2.23 (adj +0.60) on $18.66, P(profit) 0.8142, adj growth 5.7 bp · C EV +3.09 (adj +0.34) on $15.43, P(profit) 0.823, adj growth 3.1 bp · R EV +0.16 (adj +0.10) on $3.00, P(profit) 0.9347, adj growth 3.8 bp

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
| Lawson Crouse: 1+ goals YES | 16 | 0.210 | 0.195 | +0.040 | +0.025 | $4.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 67 | 0.831 | 0.710 | +0.146 | +0.025 | $11.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Luke Evangelista: 1+ goals NO | 77 | 0.815 | 0.803 | +0.033 | +0.020 | $11.27 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.148 | 0.138 | +0.020 | +0.011 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06UTANJ-NJ3|no; why: higher confidence-adjusted growth (9.87 vs 1.87 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06UTANJ-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (6.20 vs 0.49 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: UTA offense succeeds (4+ goals)
- **Luke Evangelista: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no; why: Player prop expression KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no selected over player prop KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.91 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT06UTANJ-3|yes; why: higher confidence-adjusted growth (2.31 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.898 vs 0.793); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3833): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4261): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no — Player prop expression KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no selected over player prop KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.91 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis UTA:WINS (p 0.5166): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06UTANJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3974, phi -0.229)
- KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.6 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3833, phi -0.177)
- KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3485, phi -0.187)
- KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4261, phi -0.183)
- override: Player prop expression KXNHLGOAL-26OCT06UTANJ-NJLEVANGELISTA77-1|no selected over player prop KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.91 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.07 (adj +1.05) on $19.82, P(profit) 0.5301, adj growth 9.9 bp · B EV +4.08 (adj +1.44) on $28.13, P(profit) 0.756, adj growth 13.4 bp · C EV +5.95 (adj +1.82) on $32.58, P(profit) 0.7445, adj growth 16.2 bp · R EV +0.13 (adj +0.08) on $3.00, P(profit) 0.8154, adj growth 3.0 bp

## MIN @ BUF  ·  10000 joint draws  ·  396 bet sides mapped, 4 +EV candidates, 4 on card


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
| Yakov Trenin: 1+ goals YES | 10 | 0.145 | 0.131 | +0.039 | +0.025 | $3.53 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 15 | 0.187 | 0.176 | +0.028 | +0.017 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Marcus Foligno: 1+ goals YES | 10 | 0.129 | 0.119 | +0.022 | +0.013 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Peyton Krebs: 1+ goals YES | 12 | 0.150 | 0.141 | +0.022 | +0.014 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (14.16 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (4.83 vs 3.70 bp); relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.036); failure: BUF offense suppressed (<= 2 goals)
- **Marcus Foligno: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (3.73 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: MIN offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (4.83 vs 3.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BUF:OFFENSE_4PLUS (p 0.4096): highest fidelity KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.4005): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.176)
- KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3794, phi -0.187)
- KXNHLGOAL-26OCT06MINBUF-MINMFOLIGNO17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.169)
- KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3794, phi -0.192)

portfolios: A EV +3.13 (adj +1.95) on $12.62, P(profit) 0.4802, adj growth 17.6 bp · B EV +2.49 (adj +1.56) on $9.99, P(profit) 0.4802, adj growth 14.3 bp · C EV +0.78 (adj +0.48) on $4.45, P(profit) 0.1866, adj growth 4.3 bp · R EV +0.37 (adj +0.24) on $1.00, P(profit) 0.1452, adj growth 8.6 bp

## NYI @ NYR  ·  10000 joint draws  ·  408 bet sides mapped, 1 +EV candidates, 1 on card


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
| Matt Rempe: 1+ goals YES | 7 | 0.097 | 0.088 | +0.022 | +0.013 | $1.81 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (5.48 vs 0.00 bp); despite a smaller raw edge (+0.023 vs +0.042/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4001): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.383, phi -0.144)

portfolios: A EV +0.73 (adj +0.43) on $2.41, P(profit) 0.0971, adj growth 3.8 bp · B EV +0.55 (adj +0.32) on $1.81, P(profit) 0.0971, adj growth 3.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ CHI  ·  10000 joint draws  ·  374 bet sides mapped, 3 +EV candidates, 3 on card


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
| Ryan Greene: 1+ goals YES | 11 | 0.177 | 0.153 | +0.060 | +0.036 | $4.96 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ goals YES | 7 | 0.099 | 0.088 | +0.024 | +0.013 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 2+ assists NO | 91 | 0.963 | 0.926 | +0.047 | +0.011 | $11.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06STLCHI-10|yes; why: higher confidence-adjusted growth (26.93 vs 0.75 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.295); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT06STLCHI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi -0.025); failure: CHI offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06STLCHI-10|yes; why: higher confidence-adjusted growth (5.62 vs 0.75 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.896 vs 0.295); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT06STLCHI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)
- **Patrick Kane: 2+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.18 vs 0.10 bp); despite a smaller raw edge (+0.047 vs +0.096/contract); alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.3298): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4275): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CHI:SUPPRESSED (p 0.4532): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4532, phi -0.228)
- KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3631, phi -0.125)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3298, phi -0.164)

portfolios: A EV +4.78 (adj +2.67) on $17.34, P(profit) 0.2607, adj growth 23.7 bp · B EV +3.75 (adj +2.00) on $18.07, P(profit) 0.2607, adj growth 18.4 bp · C EV +4.12 (adj +2.46) on $7.96, P(profit) 0.1774, adj growth 21.3 bp · R EV +1.04 (adj +0.62) on $2.00, P(profit) 0.1774, adj growth 21.4 bp

## VGK @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


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
| Vegas wins by over 1.5 goals NO | 62 | 0.710 | 0.662 | +0.073 | +0.026 | $8.33 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 75 | 0.818 | 0.781 | +0.055 | +0.018 | $2.62 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (6.37 vs 4.04 bp); relationships: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: DUPLICATIVE (phi 0.738); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no has the higher standalone adjusted growth (6.37 vs 4.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.738); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: DUPLICATIVE (phi 0.738); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:WINS (p 0.4852): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2672): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.4075): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2902, phi -1.0)
- KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2902, phi -0.738)

portfolios: A EV +2.24 (adj +0.69) on $19.82, P(profit) 0.3983, adj growth 5.8 bp · B EV +1.15 (adj +0.40) on $10.96, P(profit) 0.7098, adj growth 3.8 bp · C EV +2.00 (adj +0.71) on $17.40, P(profit) 0.7098, adj growth 6.3 bp · R EV +0.42 (adj +0.15) on $4.00, P(profit) 0.7098, adj growth 5.3 bp

## FLA @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 3 on card


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
| Florida wins by over 2.5 goals NO | 80 | 0.881 | 0.838 | +0.070 | +0.027 | $8.60 | FUNDED_RESEARCH | $3 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 70 | 0.791 | 0.743 | +0.076 | +0.028 | $6.64 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Los Angeles wins by over 1.5 goals YES | 27 | 0.345 | 0.305 | +0.062 | +0.021 | $1.66 | FUNDED_RESEARCH | $1 | LAK:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA2|no; why: higher confidence-adjusted growth (10.55 vs 8.69 bp); despite a smaller raw edge (+0.070 vs +0.076/contract); relationships: KXNHLSPREAD-26OCT06FLALA-FLA2|no: DUPLICATIVE (phi 0.714); KXNHLSPREAD-26OCT06FLALA-LA2|yes: REINFORCING (phi 0.267); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (10.55 vs 8.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.714); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06FLALA-FLA3|no: DUPLICATIVE (phi 0.714); KXNHLSPREAD-26OCT06FLALA-LA2|yes: DUPLICATIVE (phi 0.373); failure: FLA wins by 2+
- **Los Angeles wins by over 1.5 goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (10.55 vs 4.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.267); they share one thesis budget; relationships: KXNHLSPREAD-26OCT06FLALA-FLA3|no: REINFORCING (phi 0.267); KXNHLSPREAD-26OCT06FLALA-FLA2|no: DUPLICATIVE (phi 0.373); failure: tight game (one-goal final or OT)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:WINS (p 0.582): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- thesis FLA:SUPPRESSED (p 0.4897): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3455): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- KXNHLSPREAD-26OCT06FLALA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2089, phi -0.714)
- KXNHLSPREAD-26OCT06FLALA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2089, phi -1.0)
- KXNHLSPREAD-26OCT06FLALA-LA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4456, phi -0.651)

portfolios: A EV +2.05 (adj +0.73) on $19.82, P(profit) 0.6508, adj growth 6.8 bp · B EV +1.82 (adj +0.68) on $16.90, P(profit) 0.7911, adj growth 6.4 bp · C EV +1.58 (adj +0.61) on $18.25, P(profit) 0.8814, adj growth 5.8 bp · R EV +0.69 (adj +0.25) on $6.00, P(profit) 0.7911, adj growth 9.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
