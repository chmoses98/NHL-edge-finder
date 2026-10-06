# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T15:47:04Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +28.22 | +7.25 | +27.30 | 0.822 | -10.04 | -19.64 | 68.02 |
| B thesis-diversified (joint) ← optimiser card | 149.02 | +25.56 | +10.39 | +23.46 | 0.791 | -12.30 | -21.64 | 99.18 |
| C best expression per thesis | 149.99 | +20.75 | +7.90 | +18.93 | 0.761 | -14.03 | -23.57 | 75.07 |
| R FUNDED research stakes | 17.00 | +2.31 | +1.44 | -1.15 | 0.484 | -4.34 | -6.78 | 0.00 |

## NSH @ TOR  ·  10000 joint draws  ·  388 bet sides mapped, 14 +EV candidates, 4 on card


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
| Gavin McKenna: 1+ goals NO | 78 | 0.845 | 0.828 | +0.053 | +0.035 | $7.41 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 17 | 0.219 | 0.206 | +0.039 | +0.026 | $2.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 61 | 0.660 | 0.646 | +0.033 | +0.019 | $4.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Alexander Kerfoot: 1+ goals YES | 13 | 0.161 | 0.152 | +0.023 | +0.014 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (16.98 vs 3.52 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: TOR offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (9.72 vs 3.23 bp); despite a smaller raw edge (+0.039 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: NSH offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NSHTOR-TORKMARCHENKO86-1|no; why: Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT06NSHTOR-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.83 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense succeeds (4+ goals)
- **Alexander Kerfoot: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes has the higher standalone adjusted growth (9.72 vs 3.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.381): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3971): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT06NSHTOR-TORKMARCHENKO86-1|no — Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT06NSHTOR-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.83 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NSH:WINS (p 0.5022): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.174)
- KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.214)
- KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3803, phi -0.283)
- KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.197)
- override: Player prop expression KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT06NSHTOR-TORKMARCHENKO86-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.83 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.03 (adj +0.54) on $16.67, P(profit) 0.6399, adj growth 4.9 bp · B EV +1.63 (adj +1.04) on $16.43, P(profit) 0.6919, adj growth 10.0 bp · C EV +1.40 (adj +0.79) on $20.34, P(profit) 0.6063, adj growth 7.5 bp · R EV +0.13 (adj +0.09) on $2.00, P(profit) 0.845, adj growth 3.5 bp

## CAR @ MTL  ·  10000 joint draws  ·  394 bet sides mapped, 8 +EV candidates, 4 on card


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
| Alexandre Texier: 1+ goals YES | 11 | 0.151 | 0.138 | +0.034 | +0.021 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 12 | 0.158 | 0.142 | +0.031 | +0.015 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 73 | 0.853 | 0.763 | +0.109 | +0.019 | $7.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 74 | 0.782 | 0.769 | +0.028 | +0.015 | $6.39 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (9.53 vs 4.42 bp); relationships: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.07); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: MTL offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26OCT06CARMTL-CAR3|no; why: higher confidence-adjusted growth (4.42 vs 0.70 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MTL offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06CARMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (4.31 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.07); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: MTL offense succeeds (4+ goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no; why: KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no has the higher standalone adjusted growth (2.89 vs 2.77 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.016); relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis MTL:OFFENSE_4PLUS (p 0.4006): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.302): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.4189): highest fidelity KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3836, phi -0.171)
- KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3836, phi -0.212)
- KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4006, phi -0.189)
- KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3607, phi -0.209)

portfolios: A EV +3.20 (adj +1.11) on $16.67, P(profit) 0.7141, adj growth 10.4 bp · B EV +2.47 (adj +0.95) on $18.29, P(profit) 0.7665, adj growth 9.0 bp · C EV +0.66 (adj +0.34) on $7.96, P(profit) 0.7801, adj growth 3.2 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7817, adj growth 1.5 bp

## OTT @ DET  ·  10000 joint draws  ·  390 bet sides mapped, 9 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_OTT_win | p_overtime | goals | shots DET/OTT | DET/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.55 | 0.45 | 0.00 | 5.99 | 27.0/27.2 | 23.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.49 | 0.51 | 0.48 | 5.94 | 27.0/27.3 | 24.1/23.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.48 | 0.52 | 0.00 | 5.93 | 21.9/32.4 | 28.6/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.54 | 0.46 | 0.00 | 9.22 | 28.5/28.5 | 22.8/22.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.46 | 0.54 | 0.45 | 5.83 | 21.3/32.0 | 28.7/18.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.060 | 0.62 | 0.38 | 0.00 | 5.97 | 31.7/21.8 | 18.9/27.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carter Yakemchuk: 1+ goals NO | 86 | 0.931 | 0.912 | +0.063 | +0.044 | $6.00 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 67 | 0.844 | 0.728 | +0.159 | +0.042 | $6.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Viktor Arvidsson: 1+ assists NO | 67 | 0.795 | 0.707 | +0.109 | +0.022 | $6.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Carter Yakemchuk: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (37.63 vs 3.83 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.06); KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: OTT offense succeeds (4+ goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (18.30 vs 3.83 bp); relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.06); KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: OTT offense succeeds (4+ goals)
- **Viktor Arvidsson: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06OTTDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (4.80 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis DET:SUPPRESSED (p 0.4006): highest fidelity KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4415): highest fidelity KXNHLAST-26OCT06OTTDET-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTTSTUTZLE18-2|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3478): highest fidelity KXNHLGOAL-26OCT06OTTDET-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06OTTDET-OTTMAMADIO22-1|yes (same contract)
- KXNHLGOAL-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3478, phi -0.118)
- KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.9 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3478, phi -0.179)
- KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.5 pts; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3781, phi -0.206)

portfolios: A EV +3.76 (adj +0.57) on $16.67, P(profit) 0.7376, adj growth 5.4 bp · B EV +2.83 (adj +0.87) on $18.33, P(profit) 0.6313, adj growth 8.6 bp · C EV +2.16 (adj +0.56) on $19.17, P(profit) 0.7743, adj growth 5.4 bp · R EV +0.14 (adj +0.10) on $2.00, P(profit) 0.931, adj growth 4.0 bp

## UTA @ NJD  ·  10000 joint draws  ·  414 bet sides mapped, 8 +EV candidates, 3 on card


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
| Vincent Trocheck: 1+ assists NO | 67 | 0.831 | 0.723 | +0.146 | +0.038 | $7.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Luke Evangelista: 1+ assists NO | 65 | 0.802 | 0.690 | +0.136 | +0.024 | $7.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 17 | 0.210 | 0.197 | +0.030 | +0.017 | $2.01 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06UTANJ-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (14.50 vs 0.56 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: UTA offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06UTANJ-NJAMANTHA39-1|no; why: higher confidence-adjusted growth (5.84 vs 2.82 bp); relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: NJD offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06UTANJ-NJ3|no; why: higher confidence-adjusted growth (4.45 vs 1.87 bp); despite a smaller raw edge (+0.030 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NJD:SUPPRESSED (p 0.4261): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3833): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:WINS (p 0.5166): highest fidelity KXNHLSPREAD-26OCT06UTANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06UTANJ-NJ3|no (same contract)
- KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.6 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3833, phi -0.177)
- KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.2 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3485, phi -0.213)
- KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3974, phi -0.229)

portfolios: A EV +3.66 (adj +0.63) on $16.67, P(profit) 0.6547, adj growth 5.9 bp · B EV +3.67 (adj +0.93) on $18.00, P(profit) 0.7297, adj growth 8.9 bp · C EV +2.35 (adj +0.58) on $15.25, P(profit) 0.738, adj growth 5.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ BUF  ·  10000 joint draws  ·  396 bet sides mapped, 10 +EV candidates, 4 on card


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
| Ryan Hartman: 1+ assists YES | 20 | 0.353 | 0.247 | +0.142 | +0.036 | $3.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.145 | 0.131 | +0.039 | +0.025 | $2.22 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Peyton Krebs: 1+ goals YES | 11 | 0.150 | 0.139 | +0.033 | +0.022 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 15 | 0.187 | 0.176 | +0.028 | +0.017 | $1.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (16.60 vs 3.46 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (16.60 vs 14.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.128); they share one thesis budget; relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes; why: higher confidence-adjusted growth (9.90 vs 4.83 bp); relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.036); failure: BUF offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes has the higher standalone adjusted growth (9.90 vs 4.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.036); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4096): highest fidelity KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3789): highest fidelity KXNHLAST-26OCT06MINBUF-MINMSHABANOV49-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-MINMSHABANOV49-1|no (same contract)
- KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.3 pts; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.284)
- KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3789, phi -0.176)
- KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3794, phi -0.192)
- KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3794, phi -0.187)

portfolios: A EV +4.59 (adj +0.96) on $16.67, P(profit) 0.4674, adj growth 8.6 bp · B EV +3.84 (adj +1.66) on $9.38, P(profit) 0.5998, adj growth 15.7 bp · C EV +3.99 (adj +1.36) on $20.83, P(profit) 0.4468, adj growth 12.8 bp · R EV +0.37 (adj +0.24) on $1.00, P(profit) 0.1452, adj growth 8.6 bp

## NYI @ NYR  ·  10000 joint draws  ·  408 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_NYI_win | p_overtime | goals | shots NYR/NYI | NYR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.63 | 0.37 | 0.00 | 5.99 | 26.7/26.9 | 24.1/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.55 | 0.45 | 0.45 | 5.89 | 26.6/27.0 | 23.8/23.2 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.090 | 0.55 | 0.45 | 0.00 | 5.92 | 21.3/32.0 | 28.6/17.7 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.48 | 0.52 | 0.45 | 5.89 | 21.6/32.6 | 29.2/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.62 | 0.38 | 0.00 | 9.23 | 28.0/28.4 | 23.2/21.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.61 | 0.39 | 0.00 | 3.47 | 25.7/25.9 | 24.3/23.5 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Oliver Bjorkstrand: 1+ goals NO | 83 | 0.864 | 0.854 | +0.024 | +0.014 | $7.99 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Bo Horvat: 1+ goals NO | 69 | 0.735 | 0.721 | +0.030 | +0.016 | $5.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 27 | 0.342 | 0.299 | +0.059 | +0.015 | $2.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Oliver Bjorkstrand: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.43 vs 0.16 bp); alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: NYR offense succeeds (4+ goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYIMMACCELLI63-1|no; why: higher confidence-adjusted growth (2.77 vs 0.91 bp); despite a smaller raw edge (+0.030 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NYI offense succeeds (4+ goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NYINYR-NYRJMILLER8-1|yes; why: higher confidence-adjusted growth (2.38 vs 0.09 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:SUPPRESSED (p 0.479): highest fidelity KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4105): highest fidelity KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3766): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4105, phi -0.181)
- KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3063, phi -0.232)
- KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3766, phi -0.259)

portfolios: A EV +1.54 (adj +0.51) on $16.67, P(profit) 0.3424, adj growth 4.6 bp · B EV +0.89 (adj +0.37) on $15.68, P(profit) 0.7113, adj growth 3.6 bp · C EV +0.70 (adj +0.25) on $8.28, P(profit) 0.7349, adj growth 2.4 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8641, adj growth 1.3 bp

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
| Ryan Greene: 1+ goals YES | 11 | 0.177 | 0.159 | +0.060 | +0.042 | $4.31 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.732 | 0.637 | +0.125 | +0.030 | $7.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Philip Broberg: 1+ goals YES | 7 | 0.099 | 0.090 | +0.024 | +0.016 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 15 | 0.177 | 0.169 | +0.018 | +0.010 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06STLCHI-10|yes; why: higher confidence-adjusted growth (36.84 vs 0.75 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.295); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06STLCHI-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (8.07 vs 1.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CHI offense succeeds (4+ goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes; why: higher confidence-adjusted growth (7.88 vs 1.65 bp); relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLDHOLLOWAY81-2|yes; why: higher confidence-adjusted growth (1.65 vs 1.42 bp); wins across more scripts (relative breadth 0.876 vs 0.697); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.3298): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4532): highest fidelity KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.4275): highest fidelity KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes (same contract)
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4532, phi -0.228)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3298, phi -0.236)
- KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3631, phi -0.125)
- KXNHLGOAL-26OCT06STLCHI-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3631, phi -0.207)

portfolios: A EV +3.16 (adj +1.78) on $16.67, P(profit) 0.1774, adj growth 17.0 bp · B EV +4.54 (adj +2.37) on $15.07, P(profit) 0.3579, adj growth 22.3 bp · C EV +4.40 (adj +2.26) on $21.92, P(profit) 0.7505, adj growth 21.4 bp · R EV +1.04 (adj +0.73) on $2.00, P(profit) 0.1774, adj growth 25.7 bp

## VGK @ SEA  ·  10000 joint draws  ·  390 bet sides mapped, 13 +EV candidates, 4 on card


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
| Ryan Winterton: 1+ goals YES | 10 | 0.144 | 0.132 | +0.038 | +0.025 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 67 | 0.726 | 0.711 | +0.040 | +0.025 | $7.06 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Vegas wins by over 2.5 goals NO | 74 | 0.818 | 0.776 | +0.064 | +0.023 | $7.32 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Freddy Gaudreau: 1+ goals YES | 8 | 0.114 | 0.100 | +0.028 | +0.015 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: higher confidence-adjusted growth (14.55 vs 6.37 bp); despite a smaller raw edge (+0.038 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06VGKSEA-VGKJEICHEL9-2|no; why: KXNHLAST-26OCT06VGKSEA-VGKJEICHEL9-2|no has the higher standalone adjusted growth (7.32 vs 6.40 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.018); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.15); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no has the higher standalone adjusted growth (6.37 vs 6.21 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.738); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT06VGKSEA-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.15); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.095); failure: VGK wins by 2+
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no has the higher standalone adjusted growth (6.37 vs 6.18 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.105); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06VGKSEA-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.095); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4075): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3504): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4852): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4256, phi -0.167)
- KXNHLGOAL-26OCT06VGKSEA-VGKJEICHEL9-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3781, phi -0.251)
- KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2902, phi -0.738)
- KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4256, phi -0.163)

portfolios: A EV +2.03 (adj +0.46) on $16.67, P(profit) 0.7349, adj growth 4.4 bp · B EV +2.35 (adj +1.30) on $18.15, P(profit) 0.6932, adj growth 12.3 bp · C EV +1.56 (adj +0.52) on $16.23, P(profit) 0.6694, adj growth 5.0 bp · R EV +0.29 (adj +0.13) on $4.00, P(profit) 0.6192, adj growth 5.1 bp

## FLA @ LAK  ·  10000 joint draws  ·  414 bet sides mapped, 22 +EV candidates, 3 on card


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
| Mats Zuccarello: 1+ assists NO | 63 | 0.788 | 0.682 | +0.141 | +0.036 | $7.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 70 | 0.791 | 0.743 | +0.076 | +0.028 | $7.70 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 49 | 0.607 | 0.528 | +0.100 | +0.020 | $4.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (12.21 vs 4.81 bp); relationships: KXNHLSPREAD-26OCT06FLALA-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.112); KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.046); failure: LAK offense succeeds (4+ goals)
- **Florida wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: higher confidence-adjusted growth (8.69 vs 7.57 bp); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.112); KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.186); failure: FLA wins by 2+
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no; why: second expression of the same thesis: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no has the higher standalone adjusted growth (12.21 vs 3.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.046); they share one thesis budget; relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.046); KXNHLSPREAD-26OCT06FLALA-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.186); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.3815): highest fidelity KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4056): highest fidelity KXNHLTEAMTOTAL-26OCT06FLALA-LA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.582): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4056, phi -0.207)
- KXNHLSPREAD-26OCT06FLALA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2089, phi -1.0)
- KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.2 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4056, phi -0.273)

portfolios: A EV +3.26 (adj +0.69) on $16.67, P(profit) 0.814, adj growth 6.6 bp · B EV +3.35 (adj +0.90) on $19.69, P(profit) 0.7504, adj growth 8.7 bp · C EV +3.53 (adj +1.24) on $20.01, P(profit) 0.6617, adj growth 11.8 bp · R EV +0.21 (adj +0.08) on $2.00, P(profit) 0.7911, adj growth 3.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
