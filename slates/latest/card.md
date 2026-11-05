# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T19:28:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +24.90 | +7.45 | +23.91 | 0.741 | -22.28 | -34.59 | 67.55 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +24.77 | +12.99 | +22.57 | 0.717 | -26.73 | -38.68 | 121.91 |
| C best expression per thesis | 150.01 | +23.06 | +10.45 | +20.90 | 0.697 | -29.38 | -42.08 | 95.98 |
| R FUNDED research stakes | 14.00 | +1.94 | +1.16 | -0.55 | 0.459 | -5.20 | -7.38 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  432 bet sides mapped, 4 +EV candidates, 4 on card

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
| Lawson Crouse: 1+ goals YES | 18 | 0.225 | 0.211 | +0.035 | +0.021 | $3.16 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ assists YES | 33 | 0.413 | 0.369 | +0.068 | +0.024 | $3.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Utah wins by over 2.5 goals NO | 79 | 0.841 | 0.813 | +0.039 | +0.011 | $6.11 | FUNDED_RESEARCH | $2 | MTL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Utah wins by over 1.5 goals NO | 68 | 0.739 | 0.707 | +0.044 | +0.012 | $1.79 | FUNDED_RESEARCH | $1 | MTL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes; why: higher confidence-adjusted growth (6.33 vs 0.29 bp); alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV05UTAMTL-UTA3|no: INTENTIONAL_DIVERSIFIER (phi -0.149); KXNHLSPREAD-26NOV05UTAMTL-UTA2|no: INTENTIONAL_DIVERSIFIER (phi -0.171); failure: UTA offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA3|no; why: higher confidence-adjusted growth (5.40 vs 1.78 bp); relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV05UTAMTL-UTA3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26NOV05UTAMTL-UTA2|no: REINFORCING (phi 0.187); failure: MTL offense suppressed (<= 2 goals)
- **Utah wins by over 2.5 goals NO** — thesis: MTL wins (incl. OT/SO); alternative: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes has the higher standalone adjusted growth (5.40 vs 1.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.149); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26NOV05UTAMTL-UTA2|no: DUPLICATIVE (phi 0.733); failure: UTA wins by 2+
- **Utah wins by over 1.5 goals NO** — thesis: MTL wins (incl. OT/SO); alternative: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes has the higher standalone adjusted growth (5.40 vs 1.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.187); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.171); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: REINFORCING (phi 0.187); KXNHLSPREAD-26NOV05UTAMTL-UTA3|no: DUPLICATIVE (phi 0.733); failure: UTA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.398): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4339): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [DIRECT], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS (p 0.5335): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3901, phi -0.226)
- KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3462, phi -0.271)
- KXNHLSPREAD-26NOV05UTAMTL-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2606, phi -0.733)
- KXNHLSPREAD-26NOV05UTAMTL-UTA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2606, phi -1.0)

portfolios: A EV +1.78 (adj +0.70) on $15.42, P(profit) 0.4793, adj growth 6.5 bp · B EV +1.69 (adj +0.71) on $14.58, P(profit) 0.5224, adj growth 6.7 bp · C EV +1.77 (adj +0.80) on $9.23, P(profit) 0.5463, adj growth 7.3 bp · R EV +0.16 (adj +0.05) on $3.00, P(profit) 0.7394, adj growth 1.7 bp

## VGK @ DET  ·  10000 joint draws  ·  414 bet sides mapped, 2 +EV candidates, 2 on card

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
| Brayden McNabb: 1+ goals YES | 5 | 0.078 | 0.069 | +0.025 | +0.015 | $1.59 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 2+ assists NO | 88 | 0.927 | 0.898 | +0.040 | +0.011 | $9.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-2|yes; why: higher confidence-adjusted growth (9.67 vs 0.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.889 vs 0.772); alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-2|no: MOSTLY_INDEPENDENT (phi -0.012); failure: VGK offense suppressed (<= 2 goals)
- **Lucas Raymond: 2+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (2.75 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.4209): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis DET:SUPPRESSED (p 0.4279): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3615, phi -0.123)
- KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3568, phi -0.238)

portfolios: A EV +1.21 (adj +0.65) on $8.18, P(profit) 0.078, adj growth 6.0 bp · B EV +1.15 (adj +0.57) on $10.81, P(profit) 0.078, adj growth 5.3 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  398 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.783 / away 0.217

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.163 | 0.83 | 0.17 | 0.00 | 6.03 | 32.6/20.5 | 18.5/26.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.129 | 0.85 | 0.15 | 0.00 | 9.33 | 34.7/21.9 | 18.2/25.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.60 | 0.40 | 0.46 | 5.85 | 33.2/21.0 | 17.9/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.79 | 0.21 | 0.00 | 5.99 | 27.1/26.3 | 24.0/22.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.77 | 0.23 | 0.00 | 9.28 | 28.7/27.7 | 23.3/20.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.55 | 0.45 | 0.44 | 5.93 | 27.4/26.6 | 23.3/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 2.5 goals NO | 54 | 0.635 | 0.585 | +0.077 | +0.028 | $7.65 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.235 | 0.222 | +0.034 | +0.022 | $2.89 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Andrei Vasilevskiy: 19+ saves YES | 50 | 0.650 | 0.536 | +0.133 | +0.019 | $5.22 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SHOT_CONTROL | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 58 | 0.641 | 0.608 | +0.044 | +0.011 | $5.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLGAME-26NOV05CHITB-CHI|yes; why: higher confidence-adjusted growth (6.75 vs 4.34 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.159); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); KXNHLAST-26NOV05CHITB-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.173); failure: TBL wins by 2+
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB3|no has the higher standalone adjusted growth (6.75 vs 6.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.159); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB3|no: REINFORCING (phi 0.159); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV05CHITB-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.175); failure: CHI offense suppressed (<= 2 goals)
- **Andrei Vasilevskiy: 19+ saves YES** — thesis: CHI controls shots (share >= 0.55); alternative: KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no; why: higher confidence-adjusted growth (3.14 vs 1.36 bp); relationships: KXNHLSPREAD-26NOV05CHITB-TB3|no: INTENTIONAL_DIVERSIFIER (phi -0.065); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV05CHITB-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.036); failure: TBL net faces light volume (<= 25 shots; CHI suppressed)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV05CHITB-6|no; why: higher confidence-adjusted growth (1.09 vs 0.49 bp); wins across more scripts (relative breadth 0.964 vs 0.788); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV05CHITB-TB3|no: INTENTIONAL_DIVERSIFIER (phi -0.173); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.175); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi 0.036); failure: CHI offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · high event (8+) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.3732): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB3|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.2364): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB3|no (same contract)
- thesis CHI:WINS (p 0.2811): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB3|no (same contract)
- KXNHLSPREAD-26NOV05CHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.5022, phi -0.755)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.556, phi -0.282)
- KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.5 pts; fragile player expression; opposing: failure thesis TBL:NET_LOW_VOLUME (p 0.6641, phi -0.466)
- KXNHLAST-26NOV05CHITB-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2364, phi -0.29)

portfolios: A EV +2.98 (adj +0.55) on $15.42, P(profit) 0.5603, adj growth 5.2 bp · B EV +3.32 (adj +0.99) on $21.47, P(profit) 0.6148, adj growth 9.3 bp · C EV +3.26 (adj +0.86) on $24.68, P(profit) 0.5208, adj growth 7.9 bp · R EV +0.28 (adj +0.10) on $2.00, P(profit) 0.6349, adj growth 3.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CHITB-TB|no == KXNHLGAME-26NOV05CHITB-CHI|yes

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 12 +EV candidates, 4 on card

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
| Robert Thomas: 1+ goals YES | 19 | 0.263 | 0.244 | +0.062 | +0.043 | $5.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 25 | 0.304 | 0.289 | +0.041 | +0.026 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 60 | 0.652 | 0.637 | +0.035 | +0.021 | $5.79 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 23 | 0.271 | 0.259 | +0.028 | +0.017 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (24.69 vs 7.64 bp); relationships: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (24.69 vs 7.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: STL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26NOV05STLNJ-STL|yes; why: KXNHLGAME-26NOV05STLNJ-STL|yes has the higher standalone adjusted growth (4.69 vs 3.96 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.204); relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (24.69 vs 3.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3357): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4354): highest fidelity KXNHLGAME-26NOV05STLNJ-STL|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.2236): highest fidelity KXNHLGAME-26NOV05STLNJ-STL|yes [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05STLNJ-STLDHOLLOWAY81-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.26)
- KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.271)
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4373, phi -0.249)
- KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.255)

portfolios: A EV +3.10 (adj +0.82) on $15.42, P(profit) 0.5476, adj growth 7.2 bp · B EV +2.98 (adj +1.96) on $17.76, P(profit) 0.5156, adj growth 18.4 bp · C EV +4.15 (adj +2.35) on $17.54, P(profit) 0.4884, adj growth 21.5 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.6516, adj growth 2.5 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05STLNJ-NJ|no == KXNHLGAME-26NOV05STLNJ-STL|yes

## CAR @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.373 / away 0.627

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
| Ondrej Palat: 1+ goals YES | 11 | 0.158 | 0.144 | +0.041 | +0.027 | $3.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.159 | +0.032 | +0.021 | $2.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.783 | 0.768 | +0.039 | +0.025 | $7.37 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 68 | 0.734 | 0.718 | +0.039 | +0.023 | $6.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR3|no; why: higher confidence-adjusted growth (14.79 vs 4.90 bp); despite a smaller raw edge (+0.041 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR3|no; why: higher confidence-adjusted growth (7.70 vs 4.90 bp); despite a smaller raw edge (+0.032 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYI offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no; why: higher confidence-adjusted growth (6.97 vs 5.45 bp); relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR3|no; why: higher confidence-adjusted growth (5.45 vs 4.90 bp); despite a smaller raw edge (+0.039 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CAR:SUPPRESSED (p 0.3656): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.3886): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4764): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR3|no (same contract)
- KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.182)
- KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.196)
- KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.417, phi -0.211)
- KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.417, phi -0.244)

portfolios: A EV +3.23 (adj +0.57) on $15.42, P(profit) 0.5505, adj growth 4.7 bp · B EV +2.46 (adj +1.56) on $19.57, P(profit) 0.2927, adj growth 14.8 bp · C EV +1.66 (adj +0.68) on $22.69, P(profit) 0.6203, adj growth 6.3 bp · R EV +0.10 (adj +0.07) on $2.00, P(profit) 0.7828, adj growth 2.5 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CARNYI-NYI|yes == KXNHLGAME-26NOV05CARNYI-CAR|no

## PHI @ NYR  ·  10000 joint draws  ·  452 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.572 / away 0.428

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
| Tye Kartye: 1+ assists YES | 23 | 0.306 | 0.266 | +0.064 | +0.023 | $3.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Travis Sanheim: 1+ assists YES | 25 | 0.306 | 0.275 | +0.043 | +0.012 | $1.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 68 | 0.718 | 0.707 | +0.022 | +0.012 | $5.20 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Tye Kartye: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV05PHINYR-NYRTKARTYE24-1|yes; why: higher confidence-adjusted growth (6.31 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.078); failure: NYR offense suppressed (<= 2 goals)
- **Travis Sanheim: 1+ assists YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (1.69 vs 1.18 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV05PHINYR-NYR4|no; why: higher confidence-adjusted growth (1.42 vs 0.17 bp); despite a smaller raw edge (+0.022 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.869); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.078); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYR:OFFENSE_4PLUS (p 0.3829): highest fidelity KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3983): highest fidelity KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3983, phi -0.251)
- KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.269)
- KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3829, phi -0.226)

portfolios: A EV +2.39 (adj +0.84) on $15.42, P(profit) 0.516, adj growth 7.5 bp · B EV +1.32 (adj +0.48) on $10.24, P(profit) 0.463, adj growth 4.5 bp · C EV +1.78 (adj +0.65) on $13.83, P(profit) 0.463, adj growth 6.0 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.7176, adj growth 1.2 bp

## BOS @ PIT  ·  10000 joint draws  ·  440 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.498 / away 0.502

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
| Connor Dewar: 1+ goals YES | 13 | 0.177 | 0.163 | +0.040 | +0.025 | $3.10 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 11 | 0.140 | 0.130 | +0.023 | +0.013 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nick Robertson: 1+ goals YES | 15 | 0.183 | 0.173 | +0.024 | +0.014 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 69 | 0.756 | 0.721 | +0.051 | +0.016 | $7.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (11.48 vs 3.66 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.033); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (11.48 vs 3.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: BOS wins (incl. OT/SO)
- **Nick Robertson: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (11.48 vs 3.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.034); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05BOSPIT-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (2.58 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3079): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4534): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:SUPPRESSED (p 0.3385): highest fidelity KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no (same contract)
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.208)
- KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:WINS (p 0.4747, phi -0.192)
- KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.179)
- KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4534, phi -0.208)

portfolios: A EV +1.80 (adj +0.98) on $15.42, P(profit) 0.6498, adj growth 9.2 bp · B EV +2.03 (adj +1.08) on $14.10, P(profit) 0.3593, adj growth 10.2 bp · C EV +2.14 (adj +1.11) on $19.47, P(profit) 0.583, adj growth 10.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CBJ  ·  10000 joint draws  ·  400 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.461 / away 0.539

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
| Charlie Coyle: 1+ goals YES | 23 | 0.283 | 0.267 | +0.041 | +0.025 | $3.63 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.210 | 0.198 | +0.030 | +0.018 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Cole Sillinger: 1+ goals YES | 14 | 0.178 | 0.164 | +0.030 | +0.015 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 26 | 0.298 | 0.287 | +0.024 | +0.014 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (7.39 vs 4.72 bp); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05DALCBJ-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes; why: higher confidence-adjusted growth (4.72 vs 0.36 bp); despite a smaller raw edge (+0.030 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05DALCBJ-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: CBJ offense suppressed (<= 2 goals)
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (7.39 vs 4.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05DALCBJ-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-DALAHYRY25-1|yes; why: higher confidence-adjusted growth (2.04 vs 0.77 bp); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3817): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis DAL:OFFENSE_4PLUS (p 0.3656): highest fidelity KXNHLGOAL-26NOV05DALCBJ-DALRHINTZ24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-DALRHINTZ24-1|yes (same contract)
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.245)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.236)
- KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.217)
- KXNHLGOAL-26NOV05DALCBJ-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.4158, phi -0.27)

portfolios: A EV +1.96 (adj +1.12) on $12.31, P(profit) 0.5302, adj growth 10.4 bp · B EV +1.59 (adj +0.91) on $10.09, P(profit) 0.5302, adj growth 8.6 bp · C EV +1.66 (adj +0.99) on $11.26, P(profit) 0.435, adj growth 9.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 17 +EV candidates, 4 on card

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
| Linus Karlsson: 1+ goals YES | 16 | 0.231 | 0.212 | +0.062 | +0.043 | $5.38 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.218 | 0.202 | +0.049 | +0.033 | $4.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.152 | 0.139 | +0.035 | +0.022 | $2.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Dylan Samberg: 1+ goals YES | 5 | 0.074 | 0.064 | +0.021 | +0.011 | $1.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (27.65 vs 16.47 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05VANWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (27.65 vs 16.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05VANWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (27.65 vs 9.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05VANWPG-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: VAN offense suppressed (<= 2 goals)
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VANWPG-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (4.92 vs 0.33 bp); despite a smaller raw edge (+0.020 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3572): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.242): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.356): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no (same contract)
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.205)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.226)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.206)
- KXNHLGOAL-26NOV05VANWPG-WPGDSAMBERG54-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.356, phi -0.105)

portfolios: A EV +2.47 (adj +0.45) on $15.42, P(profit) 0.5677, adj growth 3.8 bp · B EV +4.31 (adj +2.85) on $13.12, P(profit) 0.5237, adj growth 26.6 bp · C EV +3.12 (adj +1.97) on $9.08, P(profit) 0.3891, adj growth 18.0 bp · R EV +0.73 (adj +0.50) on $2.00, P(profit) 0.2311, adj growth 18.2 bp

## ANA @ EDM  ·  10000 joint draws  ·  464 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.134 | 0.58 | 0.42 | 0.00 | 9.62 | 29.7/29.6 | 23.8/22.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.61 | 0.39 | 0.00 | 6.12 | 27.9/27.8 | 24.7/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.50 | 0.50 | 0.47 | 6.07 | 27.9/28.1 | 24.6/24.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.070 | 0.67 | 0.33 | 0.00 | 9.6 | 34.7/23.9 | 18.7/27.0 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.069 | 0.68 | 0.32 | 0.00 | 6.07 | 32.5/22.4 | 19.8/27.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.065 | 0.53 | 0.47 | 0.00 | 6.11 | 22.5/33.5 | 29.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 8 | 0.127 | 0.114 | +0.042 | +0.029 | $3.21 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.199 | 0.188 | +0.030 | +0.019 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Sam Colangelo: 1+ goals YES | 13 | 0.163 | 0.152 | +0.025 | +0.014 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 30 | 0.421 | 0.333 | +0.107 | +0.018 | $2.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.56 vs 5.32 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (5.32 vs 1.62 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: ANA offense suppressed (<= 2 goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (5.32 vs 3.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.020); they share one thesis budget; relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: ANA offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05ANAEDM-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (3.30 vs 2.92 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2727): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5286): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3593, phi -0.154)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3593, phi -0.201)
- KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3593, phi -0.169)
- KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5286, phi -0.324)

portfolios: A EV +3.47 (adj +0.63) on $15.42, P(profit) 0.5913, adj growth 5.7 bp · B EV +3.26 (adj +1.70) on $10.21, P(profit) 0.4186, adj growth 15.9 bp · C EV +2.61 (adj +0.80) on $11.36, P(profit) 0.7289, adj growth 7.4 bp · R EV +0.49 (adj +0.34) on $1.00, P(profit) 0.127, adj growth 12.3 bp

## NSH @ COL  ·  10000 joint draws  ·  440 bet sides mapped, 1 +EV candidates, 1 on card

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
| Mavrik Bourque: 1+ assists NO | 72 | 0.796 | 0.750 | +0.062 | +0.016 | $8.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (3.01 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: NSH offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:SUPPRESSED (p 0.4705): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3136, phi -0.2)

portfolios: A EV +0.52 (adj +0.14) on $6.17, P(profit) 0.7959, adj growth 1.3 bp · B EV +0.68 (adj +0.18) on $8.04, P(profit) 0.7959, adj growth 1.7 bp · C EV +0.91 (adj +0.24) on $10.87, P(profit) 0.7959, adj growth 2.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
