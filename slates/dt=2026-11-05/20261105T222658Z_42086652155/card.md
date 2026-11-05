# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T22:26:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +27.04 | +9.19 | +26.28 | 0.751 | -21.93 | -34.93 | 84.47 |
| B thesis-diversified (joint) ← optimiser card | 150.02 | +24.92 | +13.51 | +22.97 | 0.728 | -23.75 | -36.08 | 127.67 |
| C best expression per thesis | 149.05 | +19.26 | +9.37 | +18.19 | 0.717 | -20.28 | -30.51 | 88.81 |
| R FUNDED research stakes | 19.00 | +2.60 | +1.39 | +1.57 | 0.602 | -6.52 | -8.31 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  440 bet sides mapped, 6 +EV candidates, 4 on card

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
| Lawson Crouse: 1+ goals YES | 18 | 0.225 | 0.210 | +0.035 | +0.020 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ assists YES | 33 | 0.413 | 0.367 | +0.068 | +0.021 | $3.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 67 | 0.719 | 0.704 | +0.034 | +0.019 | $6.14 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 13 | 0.156 | 0.149 | +0.018 | +0.011 | $1.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes; why: higher confidence-adjusted growth (5.61 vs 0.46 bp); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: UTA offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (4.32 vs 2.06 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.025); failure: MTL offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA3|no; why: higher confidence-adjusted growth (3.62 vs 1.78 bp); despite a smaller raw edge (+0.034 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: UTA offense succeeds (4+ goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA3|no; why: higher confidence-adjusted growth (2.06 vs 1.78 bp); despite a smaller raw edge (+0.018 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.398): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4339): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [DIRECT], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS (p 0.5335): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3901, phi -0.226)
- KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3462, phi -0.271)
- KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.398, phi -0.241)
- KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3462, phi -0.183)

portfolios: A EV +1.65 (adj +0.60) on $14.26, P(profit) 0.4793, adj growth 5.6 bp · B EV +1.49 (adj +0.69) on $12.68, P(profit) 0.4888, adj growth 6.6 bp · C EV +1.46 (adj +0.68) on $12.45, P(profit) 0.4888, adj growth 6.4 bp · R EV +0.10 (adj +0.05) on $2.00, P(profit) 0.7191, adj growth 2.1 bp

## VGK @ DET  ·  10000 joint draws  ·  414 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.432 / away 0.568

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
| Brayden McNabb: 1+ goals YES | 5 | 0.078 | 0.070 | +0.025 | +0.016 | $1.57 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Mark Stone: 1+ assists NO | 56 | 0.624 | 0.590 | +0.047 | +0.012 | $3.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (11.31 vs 0.34 bp); despite a smaller raw edge (+0.025 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: VGK offense suppressed (<= 2 goals)
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05VGKDET-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (1.38 vs 0.00 bp); despite a smaller raw edge (+0.047 vs +0.067/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3615): highest fidelity KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4209): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3615, phi -0.123)
- KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4209, phi -0.272)

portfolios: A EV +1.32 (adj +0.69) on $7.56, P(profit) 0.6621, adj growth 6.4 bp · B EV +1.01 (adj +0.56) on $5.09, P(profit) 0.6621, adj growth 5.2 bp · C EV +0.24 (adj +0.06) on $2.99, P(profit) 0.6243, adj growth 0.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  398 bet sides mapped, 12 +EV candidates, 4 on card

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
| Tampa Bay wins by over 1.5 goals NO | 40 | 0.494 | 0.445 | +0.077 | +0.028 | $5.02 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.236 | 0.222 | +0.035 | +0.021 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Andrei Vasilevskiy: 19+ saves YES | 51 | 0.644 | 0.544 | +0.117 | +0.016 | $4.37 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SHOT_CONTROL | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Arvid Soderblom: 28+ saves NO | 54 | 0.621 | 0.573 | +0.064 | +0.016 | $4.95 | FUNDED_RESEARCH | $2 | CHI:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no; why: higher confidence-adjusted growth (6.96 vs 4.29 bp); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.154); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: INTENTIONAL_DIVERSIFIER (phi -0.166); failure: TBL wins by 2+
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB2|no has the higher standalone adjusted growth (6.96 vs 6.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.154); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.154); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: MOSTLY_INDEPENDENT (phi -0.035); failure: CHI offense suppressed (<= 2 goals)
- **Andrei Vasilevskiy: 19+ saves YES** — thesis: CHI controls shots (share >= 0.55); alternative: KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no; why: higher confidence-adjusted growth (2.37 vs 2.19 bp); relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: MOSTLY_INDEPENDENT (phi 0.007); failure: TBL net faces light volume (<= 25 shots; CHI suppressed)
- **Arvid Soderblom: 28+ saves NO** — thesis: CHI net faces light volume (<= 25 shots; TBL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.166); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI net faces heavy volume (33+ shots; TBL pressure)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · high event (8+) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.3689): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.2364): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.2413): highest fidelity KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.5057, phi -1.0)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5564, phi -0.249)
- KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis TBL:NET_LOW_VOLUME (p 0.6705, phi -0.466)
- KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis CHI:NET_HIGH_VOLUME (p 0.3405, phi -0.701)

portfolios: A EV +2.69 (adj +0.45) on $14.26, P(profit) 0.5617, adj growth 4.1 bp · B EV +2.85 (adj +0.84) on $16.54, P(profit) 0.7122, adj growth 8.0 bp · C EV +1.67 (adj +0.59) on $17.79, P(profit) 0.4814, adj growth 5.6 bp · R EV +0.60 (adj +0.19) on $4.00, P(profit) 0.4943, adj growth 7.0 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CHITB-CHI|yes == KXNHLGAME-26NOV05CHITB-TB|no

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 16 +EV candidates, 4 on card

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
| Robert Thomas: 1+ goals YES | 20 | 0.263 | 0.246 | +0.052 | +0.035 | $4.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 25 | 0.304 | 0.289 | +0.041 | +0.026 | $3.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 59 | 0.652 | 0.634 | +0.045 | +0.027 | $6.60 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 23 | 0.271 | 0.259 | +0.028 | +0.017 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (15.88 vs 7.64 bp); relationships: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (15.88 vs 7.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: STL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26NOV05STLNJ-STL|yes; why: higher confidence-adjusted growth (6.59 vs 4.69 bp); despite a smaller raw edge (+0.045 vs +0.100/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (15.88 vs 3.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3357): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4354): highest fidelity KXNHLGAME-26NOV05STLNJ-STL|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3527): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.26)
- KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.271)
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4373, phi -0.249)
- KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.255)

portfolios: A EV +2.95 (adj +0.79) on $14.26, P(profit) 0.5476, adj growth 7.0 bp · B EV +2.28 (adj +1.46) on $16.24, P(profit) 0.5156, adj growth 13.8 bp · C EV +2.31 (adj +1.39) on $16.37, P(profit) 0.5435, adj growth 13.2 bp · R EV +0.15 (adj +0.09) on $2.00, P(profit) 0.6516, adj growth 3.3 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05STLNJ-NJ|no == KXNHLGAME-26NOV05STLNJ-STL|yes

## CAR @ NYI  ·  10000 joint draws  ·  424 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.363 / away 0.637

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.119 | 0.43 | 0.57 | 0.00 | 6.02 | 21.1/32.5 | 28.4/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.48 | 0.52 | 0.00 | 6.02 | 26.4/27.1 | 23.5/23.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.46 | 0.54 | 0.45 | 5.99 | 21.3/32.8 | 29.4/18.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.49 | 0.51 | 0.46 | 5.97 | 26.8/27.5 | 24.1/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.48 | 0.52 | 0.00 | 9.35 | 28.3/28.8 | 22.8/22.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.084 | 0.40 | 0.60 | 0.00 | 9.26 | 22.4/34.6 | 27.2/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sebastian Aho: 1+ goals NO | 67 | 0.733 | 0.715 | +0.048 | +0.029 | $8.07 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 14 | 0.180 | 0.169 | +0.032 | +0.020 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.157 | +0.032 | +0.019 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.153 | 0.144 | +0.026 | +0.016 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR2|no; why: higher confidence-adjusted growth (8.84 vs 6.47 bp); despite a smaller raw edge (+0.048 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CAR offense succeeds (4+ goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (9.93 vs 7.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.130); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (9.93 vs 6.80 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (9.93 vs 5.14 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.127); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:HIGH_EVENT (p 0.2786): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.3798): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.474): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no (same contract)
- KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4179, phi -0.239)
- KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3998, phi -0.208)
- KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3998, phi -0.205)
- KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3998, phi -0.164)

portfolios: A EV +2.76 (adj +0.50) on $14.26, P(profit) 0.5401, adj growth 4.1 bp · B EV +1.88 (adj +1.17) on $14.16, P(profit) 0.3958, adj growth 11.1 bp · C EV +1.13 (adj +0.54) on $12.67, P(profit) 0.5406, adj growth 5.2 bp · R EV +0.21 (adj +0.13) on $3.00, P(profit) 0.7332, adj growth 4.8 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CARNYI-NYI|yes == KXNHLGAME-26NOV05CARNYI-CAR|no

## PHI @ NYR  ·  10000 joint draws  ·  452 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

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
| Tye Kartye: 1+ assists YES | 23 | 0.306 | 0.266 | +0.064 | +0.023 | $2.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 17 | 0.209 | 0.198 | +0.029 | +0.018 | $2.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 67 | 0.743 | 0.702 | +0.058 | +0.016 | $7.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 68 | 0.718 | 0.706 | +0.022 | +0.011 | $4.12 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Tye Kartye: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (6.31 vs 0.30 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.078); failure: NYR offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes; why: higher confidence-adjusted growth (4.95 vs 1.69 bp); despite a smaller raw edge (+0.029 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.243); KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: PHI offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05PHINYR-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.68 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.243); KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV05PHINYR-NYR4|no; why: higher confidence-adjusted growth (1.13 vs 0.17 bp); despite a smaller raw edge (+0.022 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.869); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.078); KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYR:OFFENSE_4PLUS (p 0.3829): highest fidelity KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4576): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3983, phi -0.251)
- KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.232)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.222)
- KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3829, phi -0.226)

portfolios: A EV +2.42 (adj +0.89) on $14.26, P(profit) 0.5221, adj growth 8.3 bp · B EV +1.99 (adj +0.80) on $17.56, P(profit) 0.4132, adj growth 7.6 bp · C EV +1.96 (adj +0.78) on $17.24, P(profit) 0.4132, adj growth 7.4 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.7176, adj growth 1.1 bp

## BOS @ PIT  ·  10000 joint draws  ·  440 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.499 / away 0.501

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
| Connor Dewar: 1+ goals YES | 12 | 0.177 | 0.162 | +0.050 | +0.035 | $3.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.140 | 0.125 | +0.034 | +0.019 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 69 | 0.756 | 0.721 | +0.051 | +0.016 | $6.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| David Pastrnak: 1+ goals NO | 61 | 0.653 | 0.641 | +0.026 | +0.014 | $3.40 | FUNDED_RESEARCH | $1 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (22.78 vs 7.97 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (22.78 vs 7.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.036); failure: BOS wins (incl. OT/SO)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05BOSPIT-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (2.58 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense succeeds (4+ goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no; why: Player prop expression KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.82 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3079): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.3633): highest fidelity KXNHLAST-26NOV05BOSPIT-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no — Player prop expression KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.82 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PIT:SUPPRESSED (p 0.3385): highest fidelity KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no (same contract)
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.208)
- KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:WINS (p 0.4747, phi -0.192)
- KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4534, phi -0.208)
- KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4159, phi -0.274)
- override: Player prop expression KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.82 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.05 (adj +1.02) on $14.26, P(profit) 0.449, adj growth 9.7 bp · B EV +2.61 (adj +1.52) on $15.44, P(profit) 0.2893, adj growth 14.3 bp · C EV +2.32 (adj +1.24) on $13.63, P(profit) 0.5526, adj growth 11.7 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6528, adj growth 0.9 bp

## DAL @ CBJ  ·  10000 joint draws  ·  404 bet sides mapped, 6 +EV candidates, 4 on card

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
| Cole Sillinger: 1+ goals YES | 12 | 0.178 | 0.161 | +0.051 | +0.034 | $3.43 | FUNDED_RESEARCH | $1 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 7 | 0.108 | 0.098 | +0.034 | +0.023 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 16 | 0.210 | 0.197 | +0.041 | +0.027 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.283 | 0.267 | +0.041 | +0.025 | $3.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (21.94 vs 11.28 bp); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes has the higher standalone adjusted growth (21.94 vs 16.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: higher confidence-adjusted growth (11.28 vs 3.18 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.293); alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes has the higher standalone adjusted growth (21.94 vs 7.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3817): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.217)
- KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.141)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.236)
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.245)

portfolios: A EV +4.34 (adj +2.87) on $14.12, P(profit) 0.5819, adj growth 26.7 bp · B EV +3.60 (adj +2.38) on $11.68, P(profit) 0.5819, adj growth 22.4 bp · C EV +2.26 (adj +1.49) on $14.24, P(profit) 0.3476, adj growth 14.1 bp · R EV +0.40 (adj +0.27) on $1.00, P(profit) 0.1783, adj growth 9.9 bp

## VAN @ WPG  ·  10000 joint draws  ·  406 bet sides mapped, 21 +EV candidates, 4 on card

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
| Linus Karlsson: 1+ goals YES | 16 | 0.231 | 0.212 | +0.062 | +0.043 | $4.72 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.218 | 0.202 | +0.049 | +0.033 | $3.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.152 | 0.140 | +0.035 | +0.023 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Winnipeg over 3.5 goals scored NO | 47 | 0.563 | 0.514 | +0.075 | +0.026 | $4.71 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
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

portfolios: A EV +2.37 (adj +0.47) on $14.26, P(profit) 0.5677, adj growth 4.1 bp · B EV +4.16 (adj +2.60) on $15.33, P(profit) 0.4883, adj growth 24.5 bp · C EV +2.66 (adj +1.54) on $17.57, P(profit) 0.6528, adj growth 14.5 bp · R EV +1.04 (adj +0.61) on $4.00, P(profit) 0.6636, adj growth 22.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05VANWPG-VAN|yes == KXNHLGAME-26NOV05VANWPG-WPG|no

## ANA @ EDM  ·  10000 joint draws  ·  466 bet sides mapped, 15 +EV candidates, 4 on card

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
| Jeff Malott: 1+ goals YES | 9 | 0.122 | 0.113 | +0.027 | +0.017 | $1.76 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Sam Colangelo: 1+ goals YES | 13 | 0.166 | 0.156 | +0.029 | +0.018 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.199 | 0.188 | +0.029 | +0.018 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 30 | 0.349 | 0.336 | +0.035 | +0.021 | $3.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.37 vs 5.23 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (5.97 vs 5.23 bp); despite a smaller raw edge (+0.028 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (5.23 vs 4.50 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (5.23 vs 4.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.433): highest fidelity KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.2668): highest fidelity KXNHLPTS-26NOV05ANAEDM-EDMLDRAISAITL29-3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5288): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.148)
- KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.175)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.206)
- KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.254)

portfolios: A EV +3.06 (adj +0.46) on $14.26, P(profit) 0.6296, adj growth 4.2 bp · B EV +1.61 (adj +1.02) on $8.95, P(profit) 0.6203, adj growth 9.6 bp · C EV +1.93 (adj +0.62) on $7.99, P(profit) 0.7214, adj growth 5.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ COL  ·  10000 joint draws  ·  440 bet sides mapped, 4 +EV candidates, 4 on card

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
| Mavrik Bourque: 1+ assists NO | 72 | 0.796 | 0.755 | +0.062 | +0.021 | $8.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 2+ assists NO | 76 | 0.828 | 0.787 | +0.055 | +0.014 | $5.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.156 | 0.148 | +0.018 | +0.010 | $1.18 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 40 | 0.473 | 0.431 | +0.056 | +0.015 | $1.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (5.13 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NSH offense succeeds (4+ goals)
- **Nathan MacKinnon: 2+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (2.40 vs 1.93 bp); despite a smaller raw edge (+0.055 vs +0.056/contract); relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: DUPLICATIVE (phi 0.431); failure: COL offense succeeds (4+ goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26NOV05NSHCOL-NSH2|yes; why: higher confidence-adjusted growth (1.98 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: NSH offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no; why: second expression of the same thesis: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no has the higher standalone adjusted growth (2.40 vs 1.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.431); they share one thesis budget; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: DUPLICATIVE (phi 0.431); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:SUPPRESSED (p 0.4705): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- thesis COL:SUPPRESSED (p 0.256): highest fidelity KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3136): highest fidelity KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes (same contract)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3136, phi -0.2)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5392, phi -0.283)
- KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.216)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5392, phi -0.308)

portfolios: A EV +1.42 (adj +0.45) on $14.26, P(profit) 0.5365, adj growth 4.2 bp · B EV +1.43 (adj +0.47) on $16.35, P(profit) 0.6963, adj growth 4.5 bp · C EV +1.32 (adj +0.44) on $16.11, P(profit) 0.7069, adj growth 4.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
