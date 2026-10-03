# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T12:23:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +32.70 | +11.57 | +30.89 | 0.739 | -26.95 | -41.58 | 104.54 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +33.69 | +14.86 | +28.05 | 0.737 | -24.56 | -36.29 | 136.71 |
| C best expression per thesis | 132.25 | +37.95 | +17.74 | +27.04 | 0.648 | -46.15 | -61.95 | 151.75 |
| R FUNDED research stakes | 26.00 | +3.21 | +1.41 | +2.74 | 0.634 | -7.10 | -9.75 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  314 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CHI_win | p_overtime | goals | shots BUF/CHI | BUF/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.139 | 0.74 | 0.26 | 0.00 | 6.02 | 33.2/21.3 | 19.0/28.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.48 | 5.92 | 33.4/21.5 | 18.4/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.0 | 27.8/27.1 | 24.2/23.4 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.094 | 0.75 | 0.25 | 0.00 | 9.24 | 35.1/22.7 | 18.6/26.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.46 | 5.89 | 28.1/27.4 | 24.2/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.66 | 0.34 | 0.00 | 9.28 | 29.5/28.5 | 23.5/22.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.163 | 0.145 | +0.046 | +0.028 | $3.93 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CHIBUF-BUF|no; why: higher confidence-adjusted growth (15.93 vs 0.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2982): highest fidelity KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4892, phi -0.222)

portfolios: A EV +1.63 (adj +0.98) on $4.14, P(profit) 0.1628, adj growth 9.0 bp · B EV +1.54 (adj +0.93) on $3.93, P(profit) 0.1628, adj growth 8.6 bp · C EV +2.73 (adj +1.65) on $6.94, P(profit) 0.1628, adj growth 14.1 bp · R EV +0.39 (adj +0.24) on $1.00, P(profit) 0.1628, adj growth 8.7 bp

## OTT @ TOR  ·  10000 joint draws  ·  344 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_OTT_win | p_overtime | goals | shots TOR/OTT | TOR/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.137 | 0.41 | 0.59 | 0.00 | 5.97 | 21.8/34.3 | 30.1/18.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.45 | 0.55 | 0.47 | 5.92 | 21.8/34.2 | 30.7/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.46 | 5.91 | 27.5/28.4 | 25.1/24.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.47 | 0.53 | 0.00 | 5.99 | 27.6/28.5 | 24.8/24.2 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.076 | 0.44 | 0.56 | 0.00 | 9.02 | 23.3/35.9 | 28.8/18.1 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.072 | 0.48 | 0.52 | 0.49 | 2.78 | 20.5/32.4 | 30.9/19.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Stephen Halliday: 1+ goals YES | 9 | 0.139 | 0.118 | +0.043 | +0.022 | $2.91 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Hayden Hodgson: 1+ goals YES | 8 | 0.120 | 0.103 | +0.035 | +0.018 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Darren Raddysh: 1+ assists NO | 59 | 0.708 | 0.618 | +0.101 | +0.011 | $4.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03OTTTOR-TOR3|no; why: higher confidence-adjusted growth (11.91 vs 1.36 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: OTT offense suppressed (<= 2 goals)
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03OTTTOR-TOR3|no; why: higher confidence-adjusted growth (8.41 vs 1.36 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)
- **Darren Raddysh: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03OTTTOR-TOR3|no; why: alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: TOR offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:SUPPRESSED (p 0.4422): highest fidelity KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3883): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.386, phi -0.159)
- KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.386, phi -0.14)
- KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.346, phi -0.251)

portfolios: A EV +4.00 (adj +1.61) on $13.18, P(profit) 0.2439, adj growth 14.4 bp · B EV +3.01 (adj +1.23) on $9.73, P(profit) 0.2439, adj growth 11.3 bp · C EV +1.36 (adj +0.15) on $8.19, P(profit) 0.7081, adj growth 1.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ TBL  ·  10000 joint draws  ·  352 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WSH_win | p_overtime | goals | shots TBL/WSH | TBL/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.67 | 0.33 | 0.00 | 6.03 | 27.1/26.6 | 23.8/22.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.116 | 0.71 | 0.29 | 0.00 | 5.98 | 32.5/21.1 | 18.5/27.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.54 | 0.46 | 0.47 | 5.92 | 27.1/26.9 | 23.7/24.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.56 | 0.44 | 0.45 | 5.93 | 32.5/21.4 | 18.2/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.29 | 28.9/28.4 | 23.0/21.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.076 | 0.73 | 0.27 | 0.00 | 9.19 | 34.0/22.4 | 18.1/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 2+ assists NO | 86 | 0.966 | 0.887 | +0.097 | +0.019 | $11.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (1.00) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.214 | 0.197 | +0.034 | +0.017 | $2.76 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ points NO | 43 | 0.648 | 0.466 | +0.201 | +0.019 | $4.44 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.82) | CALIBRATION_WARNING | D |
- **John Carlson: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (6.83 vs 3.06 bp); despite a smaller raw edge (+0.097 vs +0.201/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: REINFORCING (phi 0.256); failure: TBL offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03WSHTB-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (4.30 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: WSH offense suppressed (<= 2 goals)
- **John Carlson: 1+ points NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (3.06 vs 0.00 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-2|no: REINFORCING (phi 0.256); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3092): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3142): highest fidelity KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no (same contract)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 0% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4662, phi -0.144)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4775, phi -0.236)
- KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 24.3 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4662, phi -0.263)

portfolios: A EV +4.17 (adj +0.71) on $15.91, P(profit) 0.7244, adj growth 6.6 bp · B EV +3.79 (adj +0.69) on $18.51, P(profit) 0.7171, adj growth 6.5 bp · C EV +4.95 (adj +0.83) on $13.81, P(profit) 0.7244, adj growth 7.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  372 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.132 | 0.53 | 0.47 | 0.00 | 5.98 | 20.5/32.0 | 28.6/17.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.49 | 0.51 | 0.49 | 5.84 | 20.7/32.5 | 29.1/17.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.58 | 0.42 | 0.00 | 5.98 | 26.1/26.7 | 23.7/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.54 | 0.46 | 0.49 | 5.89 | 25.8/26.7 | 23.4/22.6 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.073 | 0.53 | 0.47 | 0.48 | 2.72 | 19.1/30.3 | 28.9/17.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.068 | 0.51 | 0.49 | 0.00 | 3.43 | 19.3/30.9 | 28.9/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 9 | 0.171 | 0.147 | +0.075 | +0.051 | $6.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Carl Grundstrom: 1+ goals YES | 8 | 0.137 | 0.119 | +0.052 | +0.034 | $4.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 9 | 0.131 | 0.117 | +0.035 | +0.021 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 75 | 0.795 | 0.780 | +0.032 | +0.017 | $9.94 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: higher confidence-adjusted growth (63.11 vs 5.59 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT03CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: PHI offense suppressed (<= 2 goals)
- **Carl Grundstrom: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (63.11 vs 30.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT03CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (63.11 vs 11.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT03CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: PHI offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: KXNHLGAME-26OCT03CARPHI-PHI|yes has the higher standalone adjusted growth (5.59 vs 3.59 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.171); relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3725): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5401): highest fidelity KXNHLGAME-26OCT03CARPHI-PHI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.4632): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4075, phi -0.214)
- KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4075, phi -0.165)
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4075, phi -0.176)
- KXNHLGOAL-26OCT03CARPHI-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3183, phi -0.211)

portfolios: A EV +4.69 (adj +2.63) on $15.91, P(profit) 0.4736, adj growth 24.3 bp · B EV +9.15 (adj +6.01) on $23.50, P(profit) 0.3764, adj growth 54.7 bp · C EV +9.90 (adj +6.42) on $17.51, P(profit) 0.1711, adj growth 53.9 bp · R EV +0.13 (adj +0.07) on $3.00, P(profit) 0.7954, adj growth 2.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-CAR|no == KXNHLGAME-26OCT03CARPHI-PHI|yes

## MTL @ PIT  ·  10000 joint draws  ·  322 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_MTL_win | p_overtime | goals | shots PIT/MTL | PIT/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| PIT shot control · normal event (5-7) · decided (2+) | 0.124 | 0.66 | 0.34 | 0.00 | 6.04 | 32.7/20.9 | 18.2/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.56 | 0.44 | 0.00 | 6.09 | 27.2/26.6 | 23.3/23.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 9.35 | 34.7/22.5 | 17.5/26.9 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.46 | 5.98 | 32.9/21.5 | 18.3/29.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.47 | 5.95 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.59 | 0.41 | 0.00 | 9.46 | 28.9/28.3 | 22.7/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.210 | 0.185 | +0.072 | +0.047 | $6.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Pittsburgh wins by over 2.5 goals YES | 16 | 0.230 | 0.192 | +0.060 | +0.023 | $1.44 | FUNDED_RESEARCH | $1 | PIT:WINS_BY_2PLUS | DIRECT (0.66) | EVIDENCE_MIXED | D |
| Montreal wins by over 1.5 goals NO | 69 | 0.762 | 0.724 | +0.058 | +0.019 | $3.21 | FUNDED_RESEARCH | $1 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sidney Crosby: 1+ goals YES | 31 | 0.362 | 0.343 | +0.037 | +0.018 | $2.71 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes; why: higher confidence-adjusted growth (38.98 vs 8.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.834 vs 0.439); relationships: KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes: REINFORCING (phi 0.2); KXNHLSPREAD-26OCT03MTLPIT-MTL2|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: PIT offense suppressed (<= 2 goals)
- **Pittsburgh wins by over 2.5 goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (38.98 vs 8.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.200); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: REINFORCING (phi 0.2); KXNHLSPREAD-26OCT03MTLPIT-MTL2|no: DUPLICATIVE (phi 0.305); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: REINFORCING (phi 0.196); failure: MTL wins (incl. OT/SO)
- **Montreal wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (38.98 vs 3.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.152); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: REINFORCING (phi 0.152); KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes: DUPLICATIVE (phi 0.305); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: REINFORCING (phi 0.172); failure: MTL wins by 2+
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (38.98 vs 3.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes: REINFORCING (phi 0.196); KXNHLSPREAD-26OCT03MTLPIT-MTL2|no: REINFORCING (phi 0.172); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, PIT shot control · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3477): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes less than the minimum stake; KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes kept
- thesis PIT:OFFENSE_4PLUS (p 0.4718): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.568): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.222)
- KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes: FUNDED_RESEARCH; family MIXED; loses 34% of the draws where the thesis happens; opposing: failure thesis MTL:WINS (p 0.432, phi -0.476)
- KXNHLSPREAD-26OCT03MTLPIT-MTL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.2375, phi -1.0)
- KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.27)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes less than the minimum stake; KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes kept

portfolios: A EV +4.38 (adj +2.05) on $15.91, P(profit) 0.5282, adj growth 18.5 bp · B EV +4.37 (adj +2.57) on $13.68, P(profit) 0.2925, adj growth 23.6 bp · C EV +6.15 (adj +4.01) on $11.83, P(profit) 0.2096, adj growth 34.2 bp · R EV +0.55 (adj +0.22) on $3.00, P(profit) 0.4687, adj growth 7.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03MTLPIT-PIT|yes == KXNHLGAME-26OCT03MTLPIT-MTL|no

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_UTA_win | p_overtime | goals | shots CBJ/UTA | CBJ/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.57 | 0.43 | 0.00 | 6.03 | 27.4/27.4 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.94 | 27.7/27.4 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.31 | 29.2/29.0 | 23.3/22.8 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.079 | 0.64 | 0.36 | 0.00 | 6.0 | 32.3/21.7 | 18.9/27.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.46 | 5.91 | 32.4/21.9 | 18.8/28.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.058 | 0.50 | 0.50 | 0.00 | 5.97 | 21.9/32.1 | 28.3/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 69 | 0.862 | 0.727 | +0.157 | +0.022 | $11.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Danton Heinen: 1+ goals YES | 10 | 0.132 | 0.120 | +0.025 | +0.014 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 83 | 0.863 | 0.851 | +0.024 | +0.011 | $11.08 | FUNDED_RESEARCH | $3 | CBJ:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (5.33 vs 0.35 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: UTA offense succeeds (4+ goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (4.28 vs 0.20 bp); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03UTACBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (2.14 vs 0.60 bp); despite a smaller raw edge (+0.024 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis UTA:SUPPRESSED (p 0.419): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CBJ:SUPPRESSED (p 0.3649): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.189)
- KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.15)
- KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4162, phi -0.154)

portfolios: A EV +2.13 (adj +0.58) on $14.98, P(profit) 0.7772, adj growth 5.5 bp · B EV +3.30 (adj +0.77) on $24.39, P(profit) 0.7749, adj growth 7.2 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.8634, adj growth 1.5 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_SEA_win | p_overtime | goals | shots EDM/SEA | EDM/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.134 | 0.71 | 0.29 | 0.00 | 6.02 | 34.0/21.8 | 19.2/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.67 | 0.33 | 0.00 | 6.04 | 28.5/28.0 | 25.1/24.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.46 | 5.98 | 33.9/22.1 | 18.9/30.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.101 | 0.72 | 0.28 | 0.00 | 9.33 | 35.6/23.4 | 19.0/27.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.54 | 0.46 | 0.50 | 6.0 | 28.5/28.0 | 24.7/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.63 | 0.37 | 0.00 | 9.39 | 30.0/29.2 | 23.8/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 18 | 0.247 | 0.224 | +0.057 | +0.034 | $5.87 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 33 | 0.462 | 0.366 | +0.116 | +0.021 | $3.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
| Connor McDavid: 2+ assists NO | 69 | 0.821 | 0.723 | +0.116 | +0.018 | $9.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Kasperi Kapanen: 1+ assists YES | 27 | 0.378 | 0.295 | +0.094 | +0.011 | $2.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (15.77 vs 1.31 bp); despite a smaller raw edge (+0.057 vs +0.094/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.123); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.098); KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (4.20 vs 3.34 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.123); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.433); KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (4.20 vs 3.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.433); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.098); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.433); KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: EDM offense succeeds (4+ goals)
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (15.77 vs 1.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, EDM shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.505): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2841): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2841, phi -0.206)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.505, phi -0.298)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.505, phi -0.285)
- KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.8 pts; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2841, phi -0.263)

portfolios: A EV +4.63 (adj +0.65) on $15.91, P(profit) 0.7227, adj growth 5.8 bp · B EV +5.29 (adj +1.59) on $21.35, P(profit) 0.7238, adj growth 14.7 bp · C EV +6.06 (adj +2.34) on $19.21, P(profit) 0.621, adj growth 20.3 bp · R EV +0.59 (adj +0.35) on $2.00, P(profit) 0.2469, adj growth 12.5 bp

## NJD @ NYI  ·  10000 joint draws  ·  338 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.57 | 0.43 | 0.00 | 5.96 | 27.8/28.0 | 24.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.50 | 0.50 | 0.48 | 5.86 | 27.9/27.9 | 24.7/24.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.073 | 0.50 | 0.50 | 0.00 | 5.98 | 22.3/32.9 | 29.1/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.59 | 0.41 | 0.00 | 9.09 | 29.4/29.4 | 23.9/23.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.47 | 0.53 | 0.47 | 5.88 | 22.6/33.3 | 30.0/19.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.49 | 0.51 | 0.52 | 2.79 | 26.6/26.8 | 25.3/25.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 68 | 0.759 | 0.717 | +0.064 | +0.022 | $6.57 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 4.5 goals scored NO | 78 | 0.844 | 0.809 | +0.052 | +0.017 | $8.15 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I wins YES | 45 | 0.529 | 0.487 | +0.062 | +0.020 | $1.45 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no; why: higher confidence-adjusted growth (4.85 vs 4.02 bp); relationships: KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no: REINFORCING (phi 0.461); KXNHLGAME-26OCT03NJNYI-NYI|yes: DUPLICATIVE (phi 0.598); failure: NJD wins by 2+
- **New Jersey over 4.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT03NJNYI-NJ2|no has the higher standalone adjusted growth (4.85 vs 4.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.461); they share one thesis budget; relationships: KXNHLSPREAD-26OCT03NJNYI-NJ2|no: REINFORCING (phi 0.461); KXNHLGAME-26OCT03NJNYI-NYI|yes: DUPLICATIVE (phi 0.383); failure: NJD offense succeeds (4+ goals)
- **New York I wins YES** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT03NJNYI-NJ2|no has the higher standalone adjusted growth (4.85 vs 3.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.598); they share one thesis budget; relationships: KXNHLSPREAD-26OCT03NJNYI-NJ2|no: DUPLICATIVE (phi 0.598); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no: DUPLICATIVE (phi 0.383); failure: NJD wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NYI:WINS (p 0.5294): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4595): highest fidelity KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT03NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2413, phi -1.0)
- KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3139, phi -0.636)
- KXNHLGAME-26OCT03NJNYI-NYI|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4706, phi -1.0)

portfolios: A EV +1.69 (adj +0.53) on $15.91, P(profit) 0.6675, adj growth 4.7 bp · B EV +1.32 (adj +0.44) on $16.17, P(profit) 0.7118, adj growth 4.1 bp · C EV +1.77 (adj +0.60) on $19.39, P(profit) 0.7587, adj growth 5.3 bp · R EV +0.51 (adj +0.17) on $6.00, P(profit) 0.7118, adj growth 6.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NJ|no == KXNHLGAME-26OCT03NJNYI-NYI|yes

## DAL @ NSH  ·  10000 joint draws  ·  324 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 5.96 | 27.0/27.1 | 23.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.49 | 5.93 | 27.3/27.5 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.56 | 0.44 | 0.00 | 9.22 | 28.4/28.5 | 22.8/22.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 5.96 | 21.3/32.0 | 28.3/18.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.44 | 0.56 | 0.50 | 5.88 | 21.6/32.2 | 28.8/18.4 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 5.93 | 31.7/21.8 | 18.9/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nashville wins YES | 45 | 0.537 | 0.491 | +0.070 | +0.024 | $4.42 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 68 | 0.754 | 0.714 | +0.058 | +0.019 | $5.02 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nashville wins YES** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: higher confidence-adjusted growth (4.92 vs 3.77 bp); relationships: KXNHLSPREAD-26OCT03DALNSH-DAL2|no: DUPLICATIVE (phi 0.616); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-NSH|yes has the higher standalone adjusted growth (4.92 vs 3.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.616); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-NSH|yes: DUPLICATIVE (phi 0.616); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NSH:WINS (p 0.537): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.3085): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- KXNHLGAME-26OCT03DALNSH-NSH|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.463, phi -1.0)
- KXNHLSPREAD-26OCT03DALNSH-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2464, phi -1.0)

portfolios: A EV +2.10 (adj +0.68) on $15.91, P(profit) 0.537, adj growth 5.7 bp · B EV +1.08 (adj +0.36) on $9.43, P(profit) 0.537, adj growth 3.4 bp · C EV +1.65 (adj +0.56) on $11.07, P(profit) 0.537, adj growth 4.9 bp · R EV +0.47 (adj +0.16) on $4.00, P(profit) 0.537, adj growth 5.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-DAL|no == KXNHLGAME-26OCT03DALNSH-NSH|yes

## BOS @ MIN  ·  10000 joint draws  ·  332 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_BOS_win | p_overtime | goals | shots MIN/BOS | MIN/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.65 | 0.35 | 0.00 | 6.02 | 29.1/28.8 | 25.9/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.53 | 0.47 | 0.47 | 5.96 | 28.6/28.5 | 25.3/25.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.103 | 0.72 | 0.28 | 0.00 | 6.03 | 34.3/22.6 | 20.0/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.68 | 0.32 | 0.00 | 9.46 | 30.4/30.0 | 25.0/23.1 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.57 | 0.43 | 0.47 | 5.94 | 34.8/23.3 | 20.0/31.4 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.074 | 0.75 | 0.25 | 0.00 | 9.27 | 35.7/24.2 | 19.8/27.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, MIN shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_STL_win | p_overtime | goals | shots COL/STL | COL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.154 | 0.71 | 0.29 | 0.00 | 6.02 | 33.7/21.3 | 18.8/28.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.54 | 0.46 | 0.48 | 5.92 | 34.1/21.8 | 18.5/30.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.114 | 0.76 | 0.24 | 0.00 | 9.31 | 35.6/22.7 | 18.6/27.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 6.04 | 28.0/27.1 | 24.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.51 | 0.49 | 0.45 | 5.95 | 28.3/27.6 | 24.3/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.68 | 0.32 | 0.00 | 9.4 | 29.9/28.9 | 23.9/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins NO | 28 | 0.372 | 0.323 | +0.077 | +0.029 | $1.12 | FUNDED_RESEARCH | $1 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 64 | 0.723 | 0.679 | +0.067 | +0.023 | $1.65 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03STLCOL-STL|yes; why: higher confidence-adjusted growth (8.92 vs 5.86 bp); relationships: KXNHLSPREAD-26OCT03STLCOL-COL3|no: DUPLICATIVE (phi 0.476); failure: COL wins (incl. OT/SO)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT03STLCOL-COL2|no; why: KXNHLSPREAD-26OCT03STLCOL-COL2|no has the higher standalone adjusted growth (5.54 vs 5.14 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.743); relationships: KXNHLGAME-26OCT03STLCOL-COL|no: DUPLICATIVE (phi 0.476); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis STL:WINS (p 0.3716): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3093): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.1808): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- KXNHLGAME-26OCT03STLCOL-COL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6284, phi -1.0)
- KXNHLSPREAD-26OCT03STLCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4097, phi -0.743)

portfolios: A EV +2.93 (adj +1.05) on $15.91, P(profit) 0.4799, adj growth 9.1 bp · B EV +0.46 (adj +0.17) on $2.77, P(profit) 0.3716, adj growth 1.7 bp · C EV +2.73 (adj +1.00) on $12.74, P(profit) 0.3716, adj growth 8.8 bp · R EV +0.37 (adj +0.13) on $2.00, P(profit) 0.3716, adj growth 5.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.60 | 0.40 | 0.00 | 6.02 | 28.1/28.2 | 25.0/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.46 | 5.92 | 28.4/28.5 | 25.2/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 9.39 | 29.7/29.9 | 24.5/22.7 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.067 | 0.65 | 0.35 | 0.00 | 6.01 | 32.9/22.2 | 19.5/28.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.066 | 0.56 | 0.44 | 0.00 | 5.98 | 22.8/33.5 | 30.2/19.1 | even strength |
| VAN shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.50 | 5.98 | 33.5/22.8 | 19.7/30.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Calgary wins by over 1.5 goals NO | 72 | 0.776 | 0.745 | +0.042 | +0.011 | $6.54 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Calgary wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03CGYVAN-CGY3|no; why: higher confidence-adjusted growth (1.45 vs 0.64 bp); alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CGY wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:WINS (p 0.569): highest fidelity KXNHLSPREAD-26OCT03CGYVAN-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CGYVAN-CGY2|no (same contract)
- KXNHLSPREAD-26OCT03CGYVAN-CGY2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:WINS_BY_2PLUS (p 0.2241, phi -1.0)

portfolios: A EV +0.36 (adj +0.10) on $6.36, P(profit) 0.7759, adj growth 0.9 bp · B EV +0.37 (adj +0.10) on $6.54, P(profit) 0.7759, adj growth 0.9 bp · C EV +0.66 (adj +0.18) on $11.56, P(profit) 0.7759, adj growth 1.6 bp · R EV +0.11 (adj +0.03) on $2.00, P(profit) 0.7759, adj growth 1.1 bp

## LAK @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 6.02 | 27.3/27.5 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.49 | 5.92 | 27.3/27.7 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.54 | 0.46 | 0.00 | 9.3 | 29.0/29.3 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.077 | 0.44 | 0.56 | 0.00 | 6.01 | 21.8/32.4 | 28.7/18.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.48 | 5.9 | 21.8/32.7 | 29.4/18.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 3.44 | 26.1/26.3 | 24.5/24.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
