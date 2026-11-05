# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T21:57:07Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.96 | +26.73 | +8.69 | +25.99 | 0.743 | -23.26 | -36.25 | 79.47 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +25.04 | +13.53 | +22.98 | 0.718 | -26.02 | -38.11 | 127.32 |
| C best expression per thesis | 150.00 | +20.07 | +10.13 | +18.43 | 0.699 | -25.21 | -36.42 | 94.99 |
| R FUNDED research stakes | 15.00 | +2.37 | +1.36 | +1.29 | 0.542 | -6.38 | -7.98 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  440 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 6.01 | 27.1/27.5 | 24.2/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.49 | 5.99 | 27.4/27.6 | 24.4/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.57 | 0.43 | 0.00 | 9.41 | 28.8/29.1 | 23.4/22.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.096 | 0.49 | 0.51 | 0.00 | 5.99 | 21.8/33.2 | 29.4/18.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.49 | 0.51 | 0.44 | 5.93 | 21.8/33.0 | 29.6/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.072 | 0.50 | 0.50 | 0.00 | 9.35 | 23.3/34.8 | 28.1/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 18 | 0.225 | 0.210 | +0.035 | +0.020 | $2.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ assists YES | 33 | 0.413 | 0.369 | +0.068 | +0.024 | $3.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 67 | 0.719 | 0.706 | +0.034 | +0.020 | $7.23 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 20 | 0.235 | 0.224 | +0.024 | +0.013 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes; why: higher confidence-adjusted growth (5.61 vs 2.11 bp); relationships: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (5.40 vs 2.06 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: MTL offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA3|no; why: higher confidence-adjusted growth (4.12 vs 1.78 bp); despite a smaller raw edge (+0.034 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: UTA offense succeeds (4+ goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes has the higher standalone adjusted growth (5.61 vs 2.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.398): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:OFFENSE_4PLUS (p 0.4339): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [DIRECT], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS (p 0.5335): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3901, phi -0.226)
- KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3462, phi -0.271)
- KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.398, phi -0.241)
- KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3901, phi -0.221)

portfolios: A EV +1.76 (adj +0.67) on $15.22, P(profit) 0.4793, adj growth 6.3 bp · B EV +1.75 (adj +0.84) on $15.19, P(profit) 0.5263, adj growth 7.9 bp · C EV +1.87 (adj +0.90) on $15.90, P(profit) 0.4888, adj growth 8.5 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7191, adj growth 2.2 bp

## VGK @ DET  ·  10000 joint draws  ·  414 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.433 / away 0.567

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.42 | 0.58 | 0.00 | 6.03 | 27.0/27.0 | 23.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.49 | 5.95 | 27.2/27.3 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.42 | 0.58 | 0.00 | 9.31 | 28.7/28.6 | 21.9/23.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 5.99 | 31.6/21.3 | 17.8/27.9 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.50 | 0.50 | 0.44 | 5.89 | 32.1/21.7 | 18.2/28.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.059 | 0.38 | 0.62 | 0.00 | 6.0 | 21.5/31.7 | 27.4/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.078 | 0.070 | +0.025 | +0.016 | $1.67 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (11.31 vs 0.34 bp); despite a smaller raw edge (+0.025 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.4209): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3615, phi -0.123)

portfolios: A EV +0.92 (adj +0.61) on $1.98, P(profit) 0.078, adj growth 5.6 bp · B EV +0.77 (adj +0.51) on $1.67, P(profit) 0.078, adj growth 4.8 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.46 (adj +0.31) on $1.00, P(profit) 0.078, adj growth 10.4 bp

## CHI @ TBL  ·  10000 joint draws  ·  398 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.783 / away 0.217

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.173 | 0.84 | 0.16 | 0.00 | 6.02 | 32.7/20.4 | 18.4/27.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.126 | 0.84 | 0.16 | 0.00 | 9.31 | 34.6/21.6 | 17.9/25.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.61 | 0.39 | 0.47 | 5.89 | 33.6/20.9 | 17.9/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.78 | 0.22 | 0.00 | 5.99 | 27.2/26.2 | 23.9/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.55 | 0.45 | 0.47 | 5.91 | 27.3/26.4 | 23.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.78 | 0.22 | 0.00 | 9.39 | 28.7/27.8 | 23.5/20.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 40 | 0.494 | 0.445 | +0.077 | +0.028 | $5.54 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.236 | 0.222 | +0.035 | +0.021 | $2.75 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Andrei Vasilevskiy: 19+ saves YES | 51 | 0.644 | 0.544 | +0.117 | +0.016 | $4.58 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SHOT_CONTROL | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 58 | 0.645 | 0.610 | +0.048 | +0.013 | $6.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: higher confidence-adjusted growth (6.96 vs 5.62 bp); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.154); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLAST-26NOV05CHITB-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.192); failure: TBL wins by 2+
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB2|no has the higher standalone adjusted growth (6.96 vs 6.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.154); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.154); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV05CHITB-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.177); failure: CHI offense suppressed (<= 2 goals)
- **Andrei Vasilevskiy: 19+ saves YES** — thesis: CHI controls shots (share >= 0.55); alternative: KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no; why: higher confidence-adjusted growth (2.37 vs 0.20 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV05CHITB-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.046); failure: TBL net faces light volume (<= 25 shots; CHI suppressed)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV05CHITB-6|no; why: higher confidence-adjusted growth (1.55 vs 0.08 bp); wins across more scripts (relative breadth 0.951 vs 0.82); alternative not eligible: confidence-adjusted EV +0.0029 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.192); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.177); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi 0.046); failure: CHI offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · high event (8+) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.3689): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.2364): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.2413): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.5057, phi -1.0)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5564, phi -0.249)
- KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis TBL:NET_LOW_VOLUME (p 0.6705, phi -0.466)
- KXNHLAST-26NOV05CHITB-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2364, phi -0.289)

portfolios: A EV +3.00 (adj +0.64) on $15.22, P(profit) 0.6212, adj growth 5.9 bp · B EV +3.03 (adj +0.94) on $19.11, P(profit) 0.7334, adj growth 8.9 bp · C EV +1.64 (adj +0.55) on $12.13, P(profit) 0.4943, adj growth 5.2 bp · R EV +0.37 (adj +0.13) on $2.00, P(profit) 0.4943, adj growth 4.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CHITB-CHI|yes == KXNHLGAME-26NOV05CHITB-TB|no

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.660 / away 0.340

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.131 | 0.65 | 0.35 | 0.00 | 5.98 | 33.3/21.3 | 18.5/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.57 | 0.43 | 0.00 | 5.99 | 27.5/26.9 | 23.7/23.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.44 | 5.91 | 33.8/21.6 | 18.4/30.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.47 | 0.53 | 0.46 | 5.93 | 27.6/27.1 | 23.8/24.3 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.089 | 0.69 | 0.31 | 0.00 | 9.3 | 35.0/23.1 | 18.3/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 9.17 | 29.6/28.8 | 23.0/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 20 | 0.263 | 0.246 | +0.052 | +0.035 | $4.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 25 | 0.304 | 0.289 | +0.041 | +0.026 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 59 | 0.652 | 0.634 | +0.045 | +0.027 | $7.72 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Dougie Hamilton: 1+ assists YES | 29 | 0.345 | 0.315 | +0.040 | +0.010 | $2.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (15.88 vs 7.64 bp); relationships: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (15.88 vs 7.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: STL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26NOV05STLNJ-STL|yes; why: higher confidence-adjusted growth (6.59 vs 4.69 bp); despite a smaller raw edge (+0.045 vs +0.100/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: NJD offense succeeds (4+ goals)
- **Dougie Hamilton: 1+ assists YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV05STLNJ-9|yes; why: higher confidence-adjusted growth (1.11 vs 0.39 bp); wins across more scripts (relative breadth 0.91 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0050 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3357): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4354): highest fidelity KXNHLGAME-26NOV05STLNJ-STL|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2678): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.26)
- KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.271)
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4373, phi -0.249)
- KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3527, phi -0.262)

portfolios: A EV +3.22 (adj +0.77) on $15.22, P(profit) 0.5712, adj growth 7.0 bp · B EV +2.56 (adj +1.54) on $18.21, P(profit) 0.5435, adj growth 14.5 bp · C EV +2.78 (adj +1.68) on $19.74, P(profit) 0.5435, adj growth 15.7 bp · R EV +0.15 (adj +0.09) on $2.00, P(profit) 0.6516, adj growth 3.3 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05STLNJ-NJ|no == KXNHLGAME-26NOV05STLNJ-STL|yes

## CAR @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.365 / away 0.635

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.120 | 0.43 | 0.57 | 0.00 | 6.03 | 21.1/32.8 | 28.8/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.48 | 0.52 | 0.00 | 6.03 | 26.5/27.2 | 23.5/23.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.48 | 0.52 | 0.46 | 5.96 | 21.3/32.7 | 29.5/18.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.49 | 0.51 | 0.48 | 5.97 | 26.7/27.5 | 24.2/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.50 | 0.50 | 0.00 | 9.38 | 28.1/28.9 | 22.6/22.0 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.078 | 0.41 | 0.59 | 0.00 | 9.39 | 22.6/34.6 | 27.0/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 20 | 0.256 | 0.241 | +0.045 | +0.030 | $3.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.734 | 0.717 | +0.049 | +0.031 | $8.81 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.158 | 0.147 | +0.031 | +0.020 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 14 | 0.179 | 0.168 | +0.031 | +0.020 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes; why: higher confidence-adjusted growth (11.44 vs 6.75 bp); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR3|no; why: higher confidence-adjusted growth (10.08 vs 4.90 bp); despite a smaller raw edge (+0.049 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: CAR offense succeeds (4+ goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (11.44 vs 7.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NYI offense suppressed (<= 2 goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (11.44 vs 6.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.3886): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3656): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4764): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR3|no (same contract)
- KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.224)
- KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.417, phi -0.244)
- KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.182)
- KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.199)

portfolios: A EV +3.32 (adj +0.60) on $15.22, P(profit) 0.5505, adj growth 5.0 bp · B EV +2.56 (adj +1.66) on $17.63, P(profit) 0.4564, adj growth 15.7 bp · C EV +2.15 (adj +1.20) on $20.68, P(profit) 0.6914, adj growth 11.3 bp · R EV +0.21 (adj +0.14) on $3.00, P(profit) 0.7342, adj growth 5.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CARNYI-CAR|no == KXNHLGAME-26NOV05CARNYI-NYI|yes

## PHI @ NYR  ·  10000 joint draws  ·  452 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.567 / away 0.433

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_PHI_win | p_overtime | goals | shots NYR/PHI | NYR/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.55 | 0.45 | 0.00 | 6.03 | 26.5/26.4 | 23.2/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.47 | 5.88 | 26.2/26.3 | 22.9/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.57 | 0.43 | 0.00 | 9.19 | 27.8/27.7 | 22.3/21.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.073 | 0.64 | 0.36 | 0.00 | 6.0 | 30.5/20.6 | 17.8/26.3 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.56 | 0.44 | 0.44 | 5.86 | 31.1/20.9 | 17.8/27.7 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.065 | 0.50 | 0.50 | 0.00 | 5.96 | 21.0/30.6 | 27.0/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tye Kartye: 1+ assists YES | 23 | 0.306 | 0.266 | +0.064 | +0.023 | $3.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 17 | 0.209 | 0.198 | +0.029 | +0.018 | $2.92 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Cole Knuble: 1+ goals YES | 12 | 0.150 | 0.141 | +0.023 | +0.014 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 67 | 0.743 | 0.702 | +0.058 | +0.016 | $8.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Tye Kartye: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (6.31 vs 0.30 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: NYR offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes; why: higher confidence-adjusted growth (4.95 vs 3.78 bp); relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.243); failure: PHI offense suppressed (<= 2 goals)
- **Cole Knuble: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes has the higher standalone adjusted growth (4.95 vs 3.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: PHI offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05PHINYR-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.68 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.243); KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYR:OFFENSE_4PLUS (p 0.3829): highest fidelity KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4576): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3983, phi -0.251)
- KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.232)
- KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.208)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.222)

portfolios: A EV +2.58 (adj +0.95) on $15.22, P(profit) 0.5221, adj growth 8.8 bp · B EV +2.33 (adj +0.98) on $16.49, P(profit) 0.415, adj growth 9.3 bp · C EV +2.36 (adj +0.94) on $20.79, P(profit) 0.4132, adj growth 8.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ PIT  ·  10000 joint draws  ·  440 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_BOS_win | p_overtime | goals | shots PIT/BOS | PIT/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.52 | 0.48 | 0.00 | 6.1 | 27.6/27.2 | 23.6/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.53 | 0.47 | 0.00 | 9.46 | 29.6/29.1 | 23.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.49 | 6.06 | 27.8/27.5 | 24.1/24.4 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.097 | 0.56 | 0.44 | 0.00 | 6.04 | 33.1/21.7 | 18.5/29.0 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.087 | 0.59 | 0.41 | 0.00 | 9.44 | 34.9/23.2 | 17.9/27.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.56 | 0.44 | 0.45 | 5.97 | 32.9/21.8 | 18.6/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.177 | 0.162 | +0.050 | +0.035 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.140 | 0.125 | +0.034 | +0.019 | $2.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 69 | 0.756 | 0.721 | +0.051 | +0.016 | $7.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| David Pastrnak: 1+ goals NO | 61 | 0.653 | 0.641 | +0.026 | +0.014 | $3.71 | FUNDED_RESEARCH | $1 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (22.78 vs 7.97 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (22.78 vs 7.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.036); failure: BOS wins (incl. OT/SO)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05BOSPIT-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (2.58 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense succeeds (4+ goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (1.89 vs 0.98 bp); despite a smaller raw edge (+0.026 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3079): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.3385): highest fidelity KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no (same contract)
- thesis BOS:SUPPRESSED (p 0.3633): highest fidelity KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no (same contract)
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.208)
- KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:WINS (p 0.4747, phi -0.192)
- KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4534, phi -0.208)
- KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4159, phi -0.274)

portfolios: A EV +2.88 (adj +1.52) on $15.22, P(profit) 0.6159, adj growth 14.3 bp · B EV +2.85 (adj +1.66) on $16.85, P(profit) 0.2893, adj growth 15.5 bp · C EV +2.41 (adj +1.43) on $16.04, P(profit) 0.583, adj growth 13.3 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6528, adj growth 0.9 bp

## DAL @ CBJ  ·  10000 joint draws  ·  404 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.462 / away 0.538

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.02 | 26.0/25.8 | 22.4/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.49 | 5.95 | 25.9/25.9 | 22.5/22.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.53 | 0.47 | 0.00 | 9.25 | 27.3/27.4 | 21.8/21.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.074 | 0.60 | 0.40 | 0.00 | 5.96 | 30.3/20.3 | 17.3/26.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.069 | 0.45 | 0.55 | 0.00 | 6.01 | 20.8/30.7 | 26.8/17.8 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.58 | 0.42 | 0.49 | 5.91 | 30.2/20.4 | 17.3/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Sillinger: 1+ goals YES | 13 | 0.178 | 0.163 | +0.040 | +0.025 | $2.80 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.283 | 0.267 | +0.041 | +0.025 | $3.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.210 | 0.198 | +0.030 | +0.018 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.108 | 0.098 | +0.023 | +0.012 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (10.90 vs 7.39 bp); despite a smaller raw edge (+0.040 vs +0.041/contract); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes has the higher standalone adjusted growth (10.90 vs 7.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26NOV05DALCBJ-DAL3|no; why: higher confidence-adjusted growth (4.72 vs 0.98 bp); despite a smaller raw edge (+0.030 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes has the higher standalone adjusted growth (10.90 vs 4.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3817): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.217)
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.245)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.236)
- KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.141)

portfolios: A EV +2.74 (adj +1.62) on $12.43, P(profit) 0.5819, adj growth 15.0 bp · B EV +2.13 (adj +1.26) on $9.75, P(profit) 0.5819, adj growth 11.9 bp · C EV +1.30 (adj +0.78) on $5.45, P(profit) 0.3476, adj growth 7.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ WPG  ·  10000 joint draws  ·  406 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.653 / away 0.347

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.56 | 0.44 | 0.00 | 6.05 | 27.4/26.7 | 23.4/23.5 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.112 | 0.62 | 0.38 | 0.00 | 6.01 | 32.8/21.2 | 18.3/28.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.50 | 0.50 | 0.48 | 6.0 | 27.5/27.0 | 23.8/24.2 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.56 | 0.44 | 0.46 | 5.96 | 32.5/21.2 | 17.9/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.31 | 28.6/28.2 | 22.3/22.2 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.079 | 0.60 | 0.40 | 0.00 | 9.24 | 34.2/22.6 | 17.6/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 16 | 0.231 | 0.212 | +0.062 | +0.043 | $5.15 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.218 | 0.202 | +0.049 | +0.033 | $3.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.152 | 0.140 | +0.035 | +0.023 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Winnipeg over 3.5 goals scored NO | 47 | 0.563 | 0.514 | +0.075 | +0.026 | $5.14 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (27.65 vs 16.47 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no: MOSTLY_INDEPENDENT (phi 0.0); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (27.65 vs 16.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no: MOSTLY_INDEPENDENT (phi 0.029); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (27.65 vs 11.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no: MOSTLY_INDEPENDENT (phi 0.032); failure: VAN offense suppressed (<= 2 goals)
- **Winnipeg over 3.5 goals scored NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: higher confidence-adjusted growth (6.08 vs 4.64 bp); wins across more scripts (relative breadth 0.898 vs 0.545); relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.032); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3572): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.356): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.242): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.205)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.226)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.206)
- KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4261, phi -0.977)

portfolios: A EV +2.53 (adj +0.50) on $15.22, P(profit) 0.5677, adj growth 4.3 bp · B EV +4.54 (adj +2.84) on $16.74, P(profit) 0.4883, adj growth 26.6 bp · C EV +3.20 (adj +1.85) on $21.20, P(profit) 0.6528, adj growth 17.3 bp · R EV +1.04 (adj +0.61) on $4.00, P(profit) 0.6636, adj growth 22.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05VANWPG-VAN|yes == KXNHLGAME-26NOV05VANWPG-WPG|no

## ANA @ EDM  ·  10000 joint draws  ·  466 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.626 / away 0.374

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.134 | 0.62 | 0.38 | 0.00 | 9.65 | 29.5/29.5 | 23.7/22.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.60 | 0.40 | 0.00 | 6.12 | 28.0/28.0 | 24.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.47 | 6.05 | 28.0/27.9 | 24.6/24.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 9.52 | 34.7/23.9 | 18.9/27.1 | even strength |
| balanced shots · high event (8+) · tight (1-goal/OT) | 0.065 | 0.50 | 0.50 | 0.60 | 9.78 | 30.0/30.0 | 23.4/23.6 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.064 | 0.66 | 0.34 | 0.00 | 6.08 | 32.9/22.1 | 19.5/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 9 | 0.122 | 0.113 | +0.027 | +0.017 | $1.93 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Sam Colangelo: 1+ goals YES | 13 | 0.166 | 0.155 | +0.029 | +0.017 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.199 | 0.187 | +0.029 | +0.017 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 30 | 0.349 | 0.336 | +0.035 | +0.021 | $3.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.37 vs 4.55 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (5.18 vs 4.55 bp); despite a smaller raw edge (+0.028 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (4.55 vs 4.50 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (4.55 vs 4.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.433): highest fidelity KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5288): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2668): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMLDRAISAITL29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.148)
- KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.175)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.206)
- KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.254)

portfolios: A EV +2.31 (adj +0.37) on $15.22, P(profit) 0.6135, adj growth 3.3 bp · B EV +1.70 (adj +1.04) on $9.44, P(profit) 0.6203, adj growth 9.8 bp · C EV +1.56 (adj +0.55) on $8.31, P(profit) 0.7069, adj growth 5.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ COL  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NSH_win | p_overtime | goals | shots COL/NSH | COL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.148 | 0.75 | 0.25 | 0.00 | 6.04 | 34.7/22.2 | 19.9/29.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.120 | 0.76 | 0.24 | 0.00 | 9.41 | 37.0/23.8 | 19.4/28.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.58 | 0.42 | 0.50 | 5.98 | 35.4/22.8 | 19.6/31.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.69 | 0.31 | 0.00 | 6.07 | 29.1/28.2 | 25.6/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.73 | 0.27 | 0.00 | 9.44 | 30.9/29.8 | 24.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.48 | 6.03 | 29.4/28.6 | 25.2/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 2+ assists NO | 76 | 0.828 | 0.787 | +0.055 | +0.014 | $6.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.156 | 0.148 | +0.018 | +0.010 | $1.25 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 40 | 0.473 | 0.431 | +0.056 | +0.015 | $1.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 2+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (2.40 vs 1.93 bp); despite a smaller raw edge (+0.055 vs +0.056/contract); relationships: KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: DUPLICATIVE (phi 0.431); failure: COL offense succeeds (4+ goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV05NSHCOL-10|yes; why: higher confidence-adjusted growth (1.98 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.907 vs 0.32); alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: NSH offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no; why: second expression of the same thesis: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no has the higher standalone adjusted growth (2.40 vs 1.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.431); they share one thesis budget; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: DUPLICATIVE (phi 0.431); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis COL:SUPPRESSED (p 0.256): highest fidelity KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3136): highest fidelity KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes (same contract)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5392, phi -0.283)
- KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.216)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5392, phi -0.308)

portfolios: A EV +1.47 (adj +0.44) on $13.79, P(profit) 0.527, adj growth 3.9 bp · B EV +0.81 (adj +0.26) on $8.93, P(profit) 0.5529, adj growth 2.4 bp · C EV +0.78 (adj +0.25) on $9.76, P(profit) 0.8541, adj growth 2.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
