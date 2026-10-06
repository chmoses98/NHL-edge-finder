# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T18:29:56Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +27.69 | +6.34 | +26.71 | 0.829 | -8.54 | -18.27 | 59.35 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +26.73 | +11.64 | +24.75 | 0.790 | -13.31 | -22.76 | 111.07 |
| C best expression per thesis | 150.01 | +20.54 | +8.20 | +19.04 | 0.755 | -15.26 | -24.54 | 77.76 |
| R FUNDED research stakes | 15.00 | +1.75 | +1.12 | +1.02 | 0.562 | -4.25 | -6.75 | 0.00 |

## NSH @ TOR  ·  10000 joint draws  ·  392 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NSH_win | p_overtime | goals | shots TOR/NSH | TOR/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.53 | 0.47 | 0.00 | 5.97 | 28.6/28.9 | 25.3/25.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.89 | 29.1/29.2 | 25.9/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.55 | 0.45 | 0.00 | 9.24 | 30.4/30.8 | 25.0/23.8 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 5.99 | 22.8/34.1 | 30.2/19.4 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.45 | 0.55 | 0.49 | 5.88 | 23.0/34.3 | 31.0/19.9 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.057 | 0.48 | 0.52 | 0.46 | 2.89 | 27.4/27.7 | 26.1/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Gavin McKenna: 1+ goals NO | 79 | 0.846 | 0.831 | +0.044 | +0.029 | $5.66 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ assists NO | 69 | 0.824 | 0.727 | +0.119 | +0.022 | $5.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ goals YES | 17 | 0.206 | 0.196 | +0.026 | +0.016 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 11 | 0.136 | 0.129 | +0.019 | +0.012 | $1.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (11.65 vs 1.64 bp); despite a smaller raw edge (+0.044 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: TOR offense succeeds (4+ goals)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (5.18 vs 1.64 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: TOR offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (3.57 vs 2.34 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: NSH offense suppressed (<= 2 goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NSHTOR-TORJTAVARES91-2|yes; why: higher confidence-adjusted growth (2.87 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.893 vs 0.784); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.392): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06NSHTOR-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.4822): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06NSHTOR-TOR2|no (same contract)
- KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3838, phi -0.171)
- KXNHLAST-26OCT06NSHTOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3838, phi -0.201)
- KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4239, phi -0.214)
- KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.392, phi -0.168)

portfolios: A EV +1.45 (adj +0.42) on $16.67, P(profit) 0.6921, adj growth 4.1 bp · B EV +1.72 (adj +0.66) on $14.29, P(profit) 0.7867, adj growth 6.3 bp · C EV +0.54 (adj +0.24) on $5.64, P(profit) 0.7373, adj growth 2.3 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.8457, adj growth 2.8 bp

## CAR @ MTL  ·  10000 joint draws  ·  396 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_CAR_win | p_overtime | goals | shots MTL/CAR | MTL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.149 | 0.49 | 0.51 | 0.00 | 6.0 | 20.7/33.3 | 29.6/17.4 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.137 | 0.48 | 0.52 | 0.46 | 5.87 | 20.9/33.7 | 30.3/17.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.097 | 0.58 | 0.42 | 0.00 | 6.02 | 26.5/27.4 | 24.2/22.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.089 | 0.50 | 0.50 | 0.00 | 9.21 | 22.1/35.1 | 28.9/16.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.54 | 0.46 | 0.47 | 5.94 | 26.3/27.3 | 24.1/22.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.072 | 0.52 | 0.48 | 0.00 | 3.44 | 19.5/31.8 | 30.0/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Chris Kreider: 1+ assists NO | 71 | 0.855 | 0.751 | +0.131 | +0.027 | $7.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Alexandre Texier: 1+ goals YES | 12 | 0.150 | 0.141 | +0.022 | +0.014 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 70 | 0.743 | 0.731 | +0.028 | +0.016 | $5.27 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 75 | 0.786 | 0.775 | +0.023 | +0.012 | $4.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06CARMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (7.78 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.058); KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: MTL offense succeeds (4+ goals)
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06CARMTL-CAR3|no; why: higher confidence-adjusted growth (3.70 vs 0.85 bp); despite a smaller raw edge (+0.023 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.058); KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: MTL offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no; why: KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no has the higher standalone adjusted growth (3.16 vs 2.81 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.003); relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: CAR offense succeeds (4+ goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.4242): highest fidelity KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis MTL:SUPPRESSED (p 0.3891): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis MTL:OFFENSE_4PLUS (p 0.3905): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3905, phi -0.167)
- KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3891, phi -0.167)
- KXNHLGOAL-26OCT06CARMTL-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3575, phi -0.221)
- KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3575, phi -0.208)
- override: Player prop expression KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.97 (adj +0.45) on $16.67, P(profit) 0.7171, adj growth 4.3 bp · B EV +1.94 (adj +0.62) on $18.87, P(profit) 0.5676, adj growth 6.0 bp · C EV +1.01 (adj +0.18) on $5.73, P(profit) 0.691, adj growth 1.7 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.7428, adj growth 1.7 bp

## OTT @ DET  ·  10000 joint draws  ·  376 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_OTT_win | p_overtime | goals | shots DET/OTT | DET/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 5.97 | 27.3/27.3 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.46 | 5.91 | 27.2/27.3 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.28 | 28.5/28.6 | 23.0/21.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.079 | 0.49 | 0.51 | 0.00 | 6.0 | 21.5/31.9 | 28.1/18.0 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.46 | 0.54 | 0.49 | 5.86 | 21.8/32.4 | 29.2/18.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.54 | 0.46 | 0.00 | 3.45 | 25.6/26.0 | 24.3/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 68 | 0.849 | 0.733 | +0.153 | +0.037 | $6.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Andrew Copp: 1+ goals YES | 18 | 0.228 | 0.215 | +0.038 | +0.025 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Viktor Arvidsson: 1+ assists NO | 66 | 0.747 | 0.701 | +0.071 | +0.025 | $6.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Alex DeBrincat: 1+ goals YES | 40 | 0.443 | 0.430 | +0.026 | +0.013 | $2.41 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | DIRECT (0.63) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (14.47 vs 5.01 bp); relationships: KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: OTT offense succeeds (4+ goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes; why: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes has the higher standalone adjusted growth (11.31 vs 8.57 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.014); relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DET offense suppressed (<= 2 goals)
- **Viktor Arvidsson: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06OTTDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (6.37 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.148); failure: DET offense succeeds (4+ goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes; why: Player prop expression KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no: INTENTIONAL_DIVERSIFIER (phi -0.148); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3797): highest fidelity KXNHLPTS-26OCT06OTTDET-DETACOPP18-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT06OTTDET-DETEFINNIE58-1|yes — Player prop expression KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis DET:SUPPRESSED (p 0.4024): highest fidelity KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4377): highest fidelity KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no (same contract)
- KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.9 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3428, phi -0.175)
- KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4024, phi -0.217)
- KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3797, phi -0.224)
- KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 37% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4024, phi -0.305)
- override: Player prop expression KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +3.89 (adj +0.61) on $16.67, P(profit) 0.6737, adj growth 5.8 bp · B EV +2.93 (adj +1.04) on $18.87, P(profit) 0.7239, adj growth 10.1 bp · C EV +3.98 (adj +1.35) on $23.00, P(profit) 0.6571, adj growth 12.7 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.4432, adj growth 1.1 bp

## UTA @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.536 / away 0.464

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_UTA_win | p_overtime | goals | shots NJD/UTA | NJD/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.45 | 0.55 | 0.00 | 6.0 | 27.8/27.6 | 23.8/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.49 | 0.51 | 0.48 | 5.91 | 28.0/27.7 | 24.3/24.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.088 | 0.52 | 0.48 | 0.00 | 5.99 | 33.1/22.1 | 18.8/29.3 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.53 | 0.47 | 0.48 | 5.93 | 33.2/22.3 | 19.1/29.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.44 | 0.56 | 0.00 | 9.24 | 29.4/29.2 | 22.8/23.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.059 | 0.46 | 0.54 | 0.50 | 2.8 | 26.3/26.2 | 24.6/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 67 | 0.842 | 0.727 | +0.156 | +0.041 | $7.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Luke Evangelista: 1+ assists NO | 64 | 0.808 | 0.692 | +0.152 | +0.036 | $7.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 17 | 0.213 | 0.200 | +0.033 | +0.020 | $2.20 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06UTANJ-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (17.51 vs 0.92 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: UTA offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06UTANJ-NJAMANTHA39-1|no; why: higher confidence-adjusted growth (12.86 vs 5.30 bp); relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: NJD offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06UTANJ-UTAALEE72-1|yes; why: higher confidence-adjusted growth (5.75 vs 1.19 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3787): highest fidelity KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.4288): highest fidelity KXNHLAST-26OCT06UTANJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT06UTANJ-NJAMANTHA39-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.4005): highest fidelity KXNHLPTS-26OCT06UTANJ-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT06UTANJ-UTAVTROCHECK16-1|no (same contract)
- KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3787, phi -0.17)
- KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.8 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3519, phi -0.199)
- KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4005, phi -0.214)

portfolios: A EV +3.86 (adj +0.76) on $16.67, P(profit) 0.6638, adj growth 7.2 bp · B EV +3.88 (adj +1.12) on $17.29, P(profit) 0.7449, adj growth 10.8 bp · C EV +2.17 (adj +0.69) on $23.00, P(profit) 0.6516, adj growth 6.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ BUF  ·  10000 joint draws  ·  400 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.495 / away 0.505

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_MIN_win | p_overtime | goals | shots BUF/MIN | BUF/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.49 | 0.51 | 0.00 | 6.03 | 28.8/28.5 | 24.8/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.48 | 5.99 | 28.9/28.7 | 25.4/25.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.48 | 0.52 | 0.00 | 9.29 | 30.5/30.2 | 23.9/24.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.085 | 0.54 | 0.46 | 0.00 | 6.06 | 34.0/22.8 | 19.5/30.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.54 | 0.46 | 0.47 | 5.94 | 34.1/23.0 | 19.8/30.8 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.068 | 0.56 | 0.44 | 0.00 | 9.22 | 35.9/24.2 | 19.0/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.147 | 0.132 | +0.052 | +0.036 | $3.02 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 13 | 0.188 | 0.172 | +0.050 | +0.034 | $3.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 20 | 0.349 | 0.249 | +0.138 | +0.038 | $2.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Olli Maatta: 1+ goals YES | 4 | 0.066 | 0.058 | +0.023 | +0.016 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (31.50 vs 18.55 bp); despite a smaller raw edge (+0.052 vs +0.138/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT06MINBUF-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MIN offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (20.99 vs 5.58 bp); relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT06MINBUF-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: BUF offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (18.55 vs 3.02 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT06MINBUF-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.036); failure: MIN offense suppressed (<= 2 goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (18.55 vs 12.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.036); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.4008): highest fidelity KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.4011): highest fidelity KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.384): highest fidelity KXNHLAST-26OCT06MINBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.165)
- KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.384, phi -0.205)
- KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.289)
- KXNHLGOAL-26OCT06MINBUF-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.115)

portfolios: A EV +6.67 (adj +2.26) on $16.67, P(profit) 0.5183, adj growth 20.5 bp · B EV +5.45 (adj +2.96) on $10.59, P(profit) 0.5634, adj growth 27.9 bp · C EV +5.33 (adj +2.12) on $22.29, P(profit) 0.469, adj growth 19.9 bp · R EV +0.54 (adj +0.38) on $1.00, P(profit) 0.1473, adj growth 14.0 bp

## NYI @ NYR  ·  10000 joint draws  ·  410 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_NYI_win | p_overtime | goals | shots NYR/NYI | NYR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.66 | 0.34 | 0.00 | 5.97 | 26.6/27.0 | 24.3/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.47 | 5.87 | 26.9/27.2 | 24.0/23.6 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.088 | 0.57 | 0.43 | 0.00 | 5.97 | 21.5/32.4 | 29.0/17.9 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.51 | 0.49 | 0.50 | 5.85 | 21.3/32.3 | 29.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.65 | 0.35 | 0.00 | 9.07 | 28.2/28.6 | 23.5/21.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.63 | 0.37 | 0.00 | 3.5 | 25.7/26.1 | 24.6/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Bo Horvat: 1+ goals NO | 69 | 0.738 | 0.725 | +0.033 | +0.020 | $5.41 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Oliver Bjorkstrand: 1+ goals NO | 83 | 0.864 | 0.854 | +0.024 | +0.014 | $6.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Matthew Schaefer: 1+ goals NO | 82 | 0.854 | 0.843 | +0.024 | +0.013 | $5.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (4.23 vs 1.39 bp); despite a smaller raw edge (+0.033 vs +0.085/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: NYI offense succeeds (4+ goals)
- **Oliver Bjorkstrand: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.35 vs 0.54 bp); despite a smaller raw edge (+0.024 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: NYR offense succeeds (4+ goals)
- **Matthew Schaefer: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no has the higher standalone adjusted growth (4.23 vs 2.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:SUPPRESSED (p 0.4901): highest fidelity KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3608): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2881, phi -0.241)
- KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4177, phi -0.148)
- KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2881, phi -0.172)

portfolios: A EV +1.29 (adj +0.31) on $16.67, P(profit) 0.5451, adj growth 3.0 bp · B EV +0.62 (adj +0.36) on $18.29, P(profit) 0.5481, adj growth 3.5 bp · C EV +0.38 (adj +0.23) on $8.01, P(profit) 0.7383, adj growth 2.1 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.7383, adj growth 2.1 bp

## STL @ CHI  ·  10000 joint draws  ·  394 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.435 / away 0.565

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_STL_win | p_overtime | goals | shots CHI/STL | CHI/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.41 | 0.59 | 0.00 | 5.99 | 26.4/26.7 | 22.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.45 | 5.91 | 26.5/26.7 | 23.4/23.1 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.34 | 0.66 | 0.00 | 5.94 | 20.9/31.3 | 26.9/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.41 | 0.59 | 0.00 | 9.24 | 27.7/28.1 | 21.7/22.4 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.45 | 0.55 | 0.47 | 5.89 | 21.3/31.8 | 28.5/18.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.42 | 0.58 | 0.00 | 3.45 | 25.0/25.2 | 23.1/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $3.49 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.738 | 0.639 | +0.131 | +0.032 | $7.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Philip Broberg: 1+ goals YES | 7 | 0.100 | 0.091 | +0.026 | +0.017 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.146 | 0.136 | +0.029 | +0.019 | $1.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06STLCHI-10|yes; why: higher confidence-adjusted growth (26.53 vs 0.33 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.944 vs 0.317); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06STLCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06STLCHI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (9.26 vs 2.77 bp); relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT06STLCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: CHI offense succeeds (4+ goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT06STLCHI-10|yes; why: higher confidence-adjusted growth (8.86 vs 0.33 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.928 vs 0.317); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT06STLCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: STL offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (26.53 vs 7.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CHI:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4578): highest fidelity KXNHLAST-26OCT06STLCHI-CHIBBYRAM24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3661): highest fidelity KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no (same contract)
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4578, phi -0.22)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.3 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3242, phi -0.242)
- KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3661, phi -0.113)
- KXNHLGOAL-26OCT06STLCHI-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4578, phi -0.183)

portfolios: A EV +2.67 (adj +0.46) on $16.67, P(profit) 0.6895, adj growth 4.4 bp · B EV +4.19 (adj +2.12) on $14.49, P(profit) 0.3622, adj growth 20.1 bp · C EV +3.65 (adj +1.74) on $23.00, P(profit) 0.6193, adj growth 16.7 bp · R EV +0.44 (adj +0.31) on $1.00, P(profit) 0.1687, adj growth 11.5 bp

## VGK @ SEA  ·  10000 joint draws  ·  382 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.395 / away 0.605

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_VGK_win | p_overtime | goals | shots SEA/VGK | SEA/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.49 | 0.51 | 0.00 | 5.98 | 26.8/27.3 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.47 | 5.88 | 27.0/27.3 | 24.1/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.104 | 0.41 | 0.59 | 0.00 | 5.96 | 21.4/32.3 | 28.3/18.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.46 | 0.54 | 0.48 | 5.85 | 21.4/32.4 | 29.0/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.52 | 0.48 | 0.00 | 9.16 | 28.2/28.6 | 23.0/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.057 | 0.50 | 0.50 | 0.00 | 3.44 | 25.5/26.0 | 24.1/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Freddy Gaudreau: 1+ goals YES | 7 | 0.114 | 0.100 | +0.040 | +0.025 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.129 | +0.034 | +0.023 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 70 | 0.760 | 0.744 | +0.045 | +0.029 | $7.55 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Vegas wins by over 2.5 goals NO | 74 | 0.819 | 0.777 | +0.065 | +0.024 | $6.79 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (19.11 vs 11.89 bp); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.084); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (11.89 vs 6.54 bp); despite a smaller raw edge (+0.034 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.095); failure: SEA offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06VGKSEA-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (9.07 vs 7.14 bp); despite a smaller raw edge (+0.045 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.13); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: higher confidence-adjusted growth (6.54 vs 6.10 bp); despite a smaller raw edge (+0.065 vs +0.072/contract); relationships: KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.084); KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.095); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.13); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3591): highest fidelity KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.402): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4912): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.17)
- KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.186)
- KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3788, phi -0.223)
- KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2913, phi -0.734)

portfolios: A EV +2.89 (adj +0.47) on $16.67, P(profit) 0.595, adj growth 4.2 bp · B EV +2.82 (adj +1.64) on $18.43, P(profit) 0.7126, adj growth 15.6 bp · C EV +2.20 (adj +1.21) on $20.94, P(profit) 0.6842, adj growth 11.4 bp · R EV +0.30 (adj +0.14) on $4.00, P(profit) 0.6437, adj growth 5.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT06VGKSEA-VGK|no == KXNHLGAME-26OCT06VGKSEA-SEA|yes

## FLA @ LAK  ·  10000 joint draws  ·  414 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_FLA_win | p_overtime | goals | shots LAK/FLA | LAK/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.60 | 0.40 | 0.00 | 6.01 | 27.1/27.1 | 24.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.47 | 5.86 | 27.0/27.0 | 23.8/23.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.083 | 0.70 | 0.30 | 0.00 | 5.94 | 32.1/21.5 | 19.1/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.61 | 0.39 | 0.00 | 9.2 | 28.5/28.4 | 23.2/21.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.56 | 0.44 | 0.48 | 5.87 | 32.0/21.7 | 18.6/28.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.52 | 0.48 | 0.48 | 2.79 | 25.7/25.5 | 24.1/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 63 | 0.797 | 0.685 | +0.151 | +0.039 | $7.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Brady Tkachuk: 1+ goals NO | 69 | 0.748 | 0.732 | +0.043 | +0.027 | $7.35 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Trevor Moore: 1+ goals YES | 19 | 0.238 | 0.224 | +0.037 | +0.023 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Alex Laferriere: 1+ assists YES | 27 | 0.373 | 0.303 | +0.089 | +0.019 | $1.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (14.64 vs 4.32 bp); relationships: KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.054); failure: LAK offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (8.68 vs 7.92 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.136); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: FLA offense succeeds (4+ goals)
- **Trevor Moore: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (8.68 vs 7.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.105); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes: REINFORCING (phi 0.164); failure: LAK offense suppressed (<= 2 goals)
- **Alex Laferriere: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (8.68 vs 3.85 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.155); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: REINFORCING (phi 0.164); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:WINS (p 0.5768): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- thesis FLA:SUPPRESSED (p 0.4908): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4015): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.2 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4015, phi -0.201)
- KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2926, phi -0.238)
- KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3792, phi -0.242)
- KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.8 pts; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3792, phi -0.285)

portfolios: A EV +2.99 (adj +0.60) on $16.67, P(profit) 0.705, adj growth 5.8 bp · B EV +3.19 (adj +1.12) on $18.87, P(profit) 0.6821, adj growth 10.8 bp · C EV +1.27 (adj +0.44) on $18.40, P(profit) 0.788, adj growth 4.3 bp · R EV +0.12 (adj +0.08) on $2.00, P(profit) 0.7481, adj growth 3.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
