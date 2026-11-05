# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T21:03:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +25.86 | +8.57 | +25.55 | 0.746 | -22.04 | -34.01 | 78.78 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +24.19 | +12.66 | +22.34 | 0.725 | -24.03 | -35.19 | 119.39 |
| C best expression per thesis | 150.00 | +23.08 | +10.62 | +21.35 | 0.701 | -27.79 | -40.38 | 98.12 |
| R FUNDED research stakes | 14.00 | +1.64 | +0.93 | +0.45 | 0.637 | -5.96 | -7.26 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  434 bet sides mapped, 7 +EV candidates, 4 on card

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
| Lawson Crouse: 1+ goals YES | 18 | 0.225 | 0.211 | +0.035 | +0.021 | $2.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ assists YES | 33 | 0.413 | 0.369 | +0.068 | +0.024 | $3.60 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 67 | 0.719 | 0.706 | +0.034 | +0.020 | $7.01 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 20 | 0.235 | 0.224 | +0.024 | +0.013 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes; why: higher confidence-adjusted growth (6.33 vs 2.11 bp); relationships: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (5.40 vs 2.06 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: MTL offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA3|no; why: higher confidence-adjusted growth (4.12 vs 1.78 bp); despite a smaller raw edge (+0.034 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: UTA offense succeeds (4+ goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes has the higher standalone adjusted growth (6.33 vs 2.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.398): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:OFFENSE_4PLUS (p 0.4339): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [DIRECT], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS (p 0.5335): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3901, phi -0.226)
- KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3462, phi -0.271)
- KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.398, phi -0.241)
- KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3901, phi -0.221)

portfolios: A EV +1.64 (adj +0.64) on $14.21, P(profit) 0.4793, adj growth 6.1 bp · B EV +1.72 (adj +0.85) on $14.88, P(profit) 0.5263, adj growth 8.0 bp · C EV +2.33 (adj +1.15) on $19.71, P(profit) 0.4888, adj growth 10.7 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7191, adj growth 2.2 bp

## VGK @ DET  ·  10000 joint draws  ·  414 bet sides mapped, 4 +EV candidates, 4 on card

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
| Brayden McNabb: 1+ goals YES | 5 | 0.078 | 0.069 | +0.025 | +0.015 | $1.51 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 2+ assists NO | 88 | 0.927 | 0.898 | +0.040 | +0.011 | $8.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Mark Stone: 1+ assists NO | 56 | 0.624 | 0.590 | +0.047 | +0.012 | $3.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Lucas Raymond: 1+ assists NO | 58 | 0.642 | 0.609 | +0.045 | +0.011 | $1.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (9.67 vs 0.34 bp); despite a smaller raw edge (+0.025 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-2|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: INTENTIONAL_DIVERSIFIER (phi -0.065); KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: VGK offense suppressed (<= 2 goals)
- **Lucas Raymond: 2+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (2.75 vs 1.19 bp); despite a smaller raw edge (+0.040 vs +0.045/contract); relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no: DUPLICATIVE (phi 0.376); failure: DET offense succeeds (4+ goals)
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05VGKDET-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (1.38 vs 0.01 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-2|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: VGK offense succeeds (4+ goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05VGKDET-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (1.19 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-2|no: DUPLICATIVE (phi 0.376); KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3615): highest fidelity KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no (same contract)
- thesis DET:SUPPRESSED (p 0.4279): highest fidelity KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4209): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3615, phi -0.123)
- KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3568, phi -0.238)
- KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4209, phi -0.272)
- KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3568, phi -0.293)

portfolios: A EV +1.50 (adj +0.62) on $14.21, P(profit) 0.4569, adj growth 5.9 bp · B EV +1.52 (adj +0.65) on $15.58, P(profit) 0.6201, adj growth 6.2 bp · C EV +0.67 (adj +0.17) on $8.57, P(profit) 0.4043, adj growth 1.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Tampa Bay wins by over 1.5 goals NO | 40 | 0.494 | 0.445 | +0.077 | +0.028 | $5.23 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.236 | 0.222 | +0.035 | +0.021 | $2.32 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Andrei Vasilevskiy: 19+ saves YES | 51 | 0.644 | 0.547 | +0.117 | +0.020 | $5.38 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SHOT_CONTROL | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Arvid Soderblom: 28+ saves NO | 52 | 0.621 | 0.549 | +0.084 | +0.011 | $4.02 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: higher confidence-adjusted growth (6.96 vs 5.62 bp); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.154); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: INTENTIONAL_DIVERSIFIER (phi -0.166); failure: TBL wins by 2+
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB2|no has the higher standalone adjusted growth (6.96 vs 6.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.154); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.154); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: MOSTLY_INDEPENDENT (phi -0.035); failure: CHI offense suppressed (<= 2 goals)
- **Andrei Vasilevskiy: 19+ saves YES** — thesis: CHI controls shots (share >= 0.55); alternative: KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no; why: higher confidence-adjusted growth (3.41 vs 1.15 bp); relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: MOSTLY_INDEPENDENT (phi 0.007); failure: TBL net faces light volume (<= 25 shots; CHI suppressed)
- **Arvid Soderblom: 28+ saves NO** — thesis: CHI net faces light volume (<= 25 shots; TBL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.166); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI net faces heavy volume (33+ shots; TBL pressure)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · high event (8+) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.3689): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.2364): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.2805): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.5057, phi -1.0)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5564, phi -0.249)
- KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis TBL:NET_LOW_VOLUME (p 0.6705, phi -0.466)
- KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.1 pts; fragile player expression; opposing: failure thesis CHI:NET_HIGH_VOLUME (p 0.3405, phi -0.701)

portfolios: A EV +2.82 (adj +0.60) on $14.21, P(profit) 0.6081, adj growth 5.7 bp · B EV +3.19 (adj +0.88) on $16.95, P(profit) 0.7122, adj growth 8.3 bp · C EV +2.24 (adj +0.62) on $12.92, P(profit) 0.4943, adj growth 5.7 bp · R EV +0.37 (adj +0.13) on $2.00, P(profit) 0.4943, adj growth 4.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CHITB-CHI|yes == KXNHLGAME-26NOV05CHITB-TB|no

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

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
| Robert Thomas: 1+ goals YES | 20 | 0.263 | 0.246 | +0.052 | +0.035 | $4.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 25 | 0.304 | 0.289 | +0.041 | +0.026 | $3.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 60 | 0.652 | 0.635 | +0.035 | +0.018 | $4.75 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 23 | 0.271 | 0.258 | +0.028 | +0.015 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (15.88 vs 7.64 bp); relationships: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (15.88 vs 7.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: STL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26NOV05STLNJ-STL|yes; why: KXNHLGAME-26NOV05STLNJ-STL|yes has the higher standalone adjusted growth (4.69 vs 3.06 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.204); relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (15.88 vs 2.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3357): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4354): highest fidelity KXNHLGAME-26NOV05STLNJ-STL|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2678): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.26)
- KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.271)
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4373, phi -0.249)
- KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.255)

portfolios: A EV +2.94 (adj +0.78) on $14.21, P(profit) 0.5476, adj growth 7.0 bp · B EV +2.16 (adj +1.36) on $14.82, P(profit) 0.5156, adj growth 12.8 bp · C EV +3.25 (adj +1.68) on $15.61, P(profit) 0.5208, adj growth 15.5 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.6516, adj growth 2.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05STLNJ-NJ|no == KXNHLGAME-26NOV05STLNJ-STL|yes

## CAR @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.366 / away 0.634

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
| Sebastian Aho: 1+ goals NO | 67 | 0.734 | 0.717 | +0.049 | +0.031 | $8.54 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.158 | 0.147 | +0.031 | +0.020 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.157 | +0.032 | +0.019 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 14 | 0.179 | 0.167 | +0.031 | +0.019 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR3|no; why: higher confidence-adjusted growth (10.08 vs 4.90 bp); despite a smaller raw edge (+0.049 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: CAR offense succeeds (4+ goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (8.40 vs 7.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.123); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (8.40 vs 6.80 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.138); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: NYI offense suppressed (<= 2 goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (8.40 vs 5.93 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.162); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CAR:SUPPRESSED (p 0.3656): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2799): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.3886): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.417, phi -0.244)
- KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.182)
- KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.196)
- KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.199)

portfolios: A EV +3.10 (adj +0.56) on $14.21, P(profit) 0.5505, adj growth 4.8 bp · B EV +2.12 (adj +1.33) on $15.19, P(profit) 0.3891, adj growth 12.6 bp · C EV +1.94 (adj +0.97) on $13.33, P(profit) 0.7622, adj growth 9.0 bp · R EV +0.21 (adj +0.14) on $3.00, P(profit) 0.7342, adj growth 5.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CARNYI-NYI|yes == KXNHLGAME-26NOV05CARNYI-CAR|no

## PHI @ NYR  ·  10000 joint draws  ·  452 bet sides mapped, 3 +EV candidates, 3 on card

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
| Tye Kartye: 1+ assists YES | 23 | 0.306 | 0.266 | +0.064 | +0.023 | $2.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 17 | 0.209 | 0.197 | +0.029 | +0.017 | $1.95 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Travis Sanheim: 1+ assists YES | 25 | 0.306 | 0.275 | +0.043 | +0.012 | $1.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Tye Kartye: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (6.31 vs 0.30 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: NYR offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes; why: higher confidence-adjusted growth (4.30 vs 1.69 bp); despite a smaller raw edge (+0.029 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.122); failure: PHI offense suppressed (<= 2 goals)
- **Travis Sanheim: 1+ assists YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes has the higher standalone adjusted growth (4.30 vs 1.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.122); they share one thesis budget; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.122); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYR:OFFENSE_4PLUS (p 0.3829): highest fidelity KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3983, phi -0.251)
- KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.232)
- KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.269)

portfolios: A EV +2.58 (adj +0.98) on $12.34, P(profit) 0.5997, adj growth 8.7 bp · B EV +1.30 (adj +0.52) on $6.19, P(profit) 0.4489, adj growth 4.9 bp · C EV +1.51 (adj +0.65) on $6.85, P(profit) 0.4489, adj growth 6.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ PIT  ·  10000 joint draws  ·  440 bet sides mapped, 6 +EV candidates, 4 on card

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
| Connor Dewar: 1+ goals YES | 13 | 0.177 | 0.163 | +0.040 | +0.025 | $2.84 | FUNDED_RESEARCH | $1 | PIT:WINS_BY_2PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.140 | 0.125 | +0.034 | +0.019 | $1.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Hendrix Lapierre: 1+ goals YES | 11 | 0.140 | 0.130 | +0.023 | +0.013 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 69 | 0.756 | 0.721 | +0.051 | +0.016 | $7.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (11.48 vs 7.97 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.033); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (11.48 vs 7.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: BOS wins (incl. OT/SO)
- **Hendrix Lapierre: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (11.48 vs 3.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.039); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05BOSPIT-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (2.58 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi -0.039); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3079): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4534): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.3385): highest fidelity KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no (same contract)
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.208)
- KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:WINS (p 0.4747, phi -0.192)
- KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.166)
- KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4534, phi -0.208)

portfolios: A EV +2.26 (adj +1.11) on $14.21, P(profit) 0.6159, adj growth 10.5 bp · B EV +2.25 (adj +1.19) on $13.40, P(profit) 0.358, adj growth 11.2 bp · C EV +2.29 (adj +1.07) on $18.01, P(profit) 0.5526, adj growth 9.9 bp · R EV +0.29 (adj +0.18) on $1.00, P(profit) 0.1775, adj growth 6.7 bp

## DAL @ CBJ  ·  10000 joint draws  ·  400 bet sides mapped, 3 +EV candidates, 3 on card

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
| Cole Sillinger: 1+ goals YES | 13 | 0.178 | 0.163 | +0.040 | +0.025 | $2.70 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.283 | 0.269 | +0.041 | +0.026 | $3.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.210 | 0.198 | +0.030 | +0.018 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (10.90 vs 8.14 bp); despite a smaller raw edge (+0.040 vs +0.041/contract); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes has the higher standalone adjusted growth (10.90 vs 8.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: higher confidence-adjusted growth (4.72 vs 3.18 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.293); alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3817): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.217)
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.245)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.236)

portfolios: A EV +2.07 (adj +1.27) on $9.80, P(profit) 0.5302, adj growth 11.8 bp · B EV +1.74 (adj +1.07) on $8.34, P(profit) 0.5302, adj growth 10.1 bp · C EV +1.60 (adj +0.96) on $6.68, P(profit) 0.3476, adj growth 8.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ WPG  ·  10000 joint draws  ·  406 bet sides mapped, 20 +EV candidates, 4 on card

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
| Linus Karlsson: 1+ goals YES | 16 | 0.231 | 0.212 | +0.062 | +0.043 | $5.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.218 | 0.202 | +0.049 | +0.033 | $3.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.152 | 0.140 | +0.035 | +0.023 | $2.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ goals NO | 85 | 0.895 | 0.882 | +0.036 | +0.023 | $8.54 | FUNDED_RESEARCH | $3 | WPG:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (27.65 vs 16.47 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05VANWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (27.65 vs 16.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05VANWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (27.65 vs 11.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05VANWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: higher confidence-adjusted growth (10.07 vs 4.64 bp); despite a smaller raw edge (+0.036 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.002 vs 0.545); relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3572): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.356): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.242): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.205)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.226)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.206)
- KXNHLGOAL-26NOV05VANWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4261, phi -0.127)

portfolios: A EV +2.28 (adj +0.41) on $14.21, P(profit) 0.5677, adj growth 3.5 bp · B EV +4.03 (adj +2.74) on $19.92, P(profit) 0.4883, adj growth 25.8 bp · C EV +3.20 (adj +1.99) on $20.22, P(profit) 0.386, adj growth 18.3 bp · R EV +0.13 (adj +0.08) on $3.00, P(profit) 0.8948, adj growth 3.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05VANWPG-VAN|yes == KXNHLGAME-26NOV05VANWPG-WPG|no

## ANA @ EDM  ·  10000 joint draws  ·  466 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

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
| Jeff Malott: 1+ goals YES | 8 | 0.122 | 0.109 | +0.037 | +0.024 | $2.45 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Jackson LaCombe: 1+ goals YES | 10 | 0.142 | 0.128 | +0.035 | +0.021 | $2.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Sam Colangelo: 1+ goals YES | 13 | 0.166 | 0.155 | +0.029 | +0.017 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.199 | 0.185 | +0.029 | +0.016 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (15.80 vs 3.92 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Jackson LaCombe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (10.23 vs 3.92 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (5.18 vs 3.92 bp); despite a smaller raw edge (+0.028 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (3.92 vs 1.17 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.433): highest fidelity KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5288): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2668): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMRNUGENTHOPKINS93-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.148)
- KXNHLGOAL-26NOV05ANAEDM-ANAJLACOMBE2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.164)
- KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.175)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.206)

portfolios: A EV +3.14 (adj +1.10) on $14.21, P(profit) 0.5482, adj growth 10.2 bp · B EV +2.54 (adj +1.56) on $8.52, P(profit) 0.4959, adj growth 14.6 bp · C EV +2.09 (adj +0.71) on $10.72, P(profit) 0.7069, adj growth 6.6 bp · R EV +0.44 (adj +0.28) on $1.00, P(profit) 0.1223, adj growth 10.1 bp

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
| Nathan MacKinnon: 1+ assists NO | 39 | 0.473 | 0.429 | +0.066 | +0.022 | $3.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ assists NO | 72 | 0.796 | 0.750 | +0.062 | +0.016 | $7.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 2+ assists NO | 76 | 0.828 | 0.787 | +0.055 | +0.014 | $4.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.156 | 0.148 | +0.018 | +0.010 | $1.23 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (4.50 vs 2.40 bp); relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: DUPLICATIVE (phi 0.431); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: COL offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (3.01 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: NSH offense succeeds (4+ goals)
- **Nathan MacKinnon: 2+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no has the higher standalone adjusted growth (4.50 vs 2.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.431); they share one thesis budget; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: DUPLICATIVE (phi 0.431); KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: COL offense succeeds (4+ goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV05NSHCOL-10|yes; why: higher confidence-adjusted growth (1.98 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.907 vs 0.32); alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi 0.007); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis COL:SUPPRESSED (p 0.256): highest fidelity KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:SUPPRESSED (p 0.4705): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3136): highest fidelity KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes (same contract)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5392, phi -0.308)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3136, phi -0.2)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5392, phi -0.283)
- KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.216)

portfolios: A EV +1.54 (adj +0.50) on $14.21, P(profit) 0.5365, adj growth 4.7 bp · B EV +1.62 (adj +0.51) on $16.22, P(profit) 0.4574, adj growth 4.8 bp · C EV +1.96 (adj +0.65) on $17.38, P(profit) 0.4574, adj growth 6.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
