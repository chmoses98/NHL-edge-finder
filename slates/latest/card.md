# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T16:17:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +27.52 | +9.19 | +24.54 | 0.717 | -30.61 | -44.93 | 81.21 |
| B thesis-diversified (joint) ← optimiser card | 149.05 | +23.76 | +12.75 | +22.21 | 0.704 | -29.47 | -43.86 | 118.62 |
| C best expression per thesis | 150.00 | +24.78 | +11.76 | +22.11 | 0.685 | -35.05 | -49.05 | 106.52 |
| R FUNDED research stakes | 11.00 | +1.58 | +0.94 | -0.60 | 0.491 | -6.68 | -7.81 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  422 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.56 | 0.44 | 0.00 | 6.09 | 27.3/27.7 | 24.4/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.54 | 0.46 | 0.45 | 6.0 | 27.4/27.7 | 24.5/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.29 | 28.7/29.2 | 23.4/22.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.093 | 0.50 | 0.50 | 0.00 | 6.01 | 21.6/33.0 | 29.4/18.3 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.48 | 0.52 | 0.49 | 5.93 | 21.9/33.1 | 29.8/18.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.076 | 0.49 | 0.51 | 0.00 | 9.24 | 23.3/34.8 | 28.3/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 18 | 0.227 | 0.211 | +0.036 | +0.021 | $3.30 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 13 | 0.162 | 0.153 | +0.025 | +0.015 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Noah Dobson: 1+ assists YES | 32 | 0.401 | 0.355 | +0.065 | +0.020 | $3.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_MIXED | D |
| Chris Kreider: 1+ goals YES | 19 | 0.229 | 0.213 | +0.028 | +0.012 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV05UTAMTL-2|yes; why: higher confidence-adjusted growth (6.17 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05UTAMTL-MTLCKREIDER22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: UTA offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (4.17 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes: MOSTLY_INDEPENDENT (phi 0.069); KXNHLGOAL-26NOV05UTAMTL-MTLCKREIDER22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: MTL offense suppressed (<= 2 goals)
- **Noah Dobson: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes has the higher standalone adjusted growth (4.17 vs 3.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.069); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.069); KXNHLGOAL-26NOV05UTAMTL-MTLCKREIDER22-1|yes: MOSTLY_INDEPENDENT (phi 0.114); failure: MTL offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes has the higher standalone adjusted growth (4.17 vs 2.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes: MOSTLY_INDEPENDENT (phi 0.114); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.393): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.309): highest fidelity KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4363): highest fidelity KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes (same contract)
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3884, phi -0.236)
- KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3464, phi -0.201)
- KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3464, phi -0.273)
- KXNHLGOAL-26NOV05UTAMTL-MTLCKREIDER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3464, phi -0.208)

portfolios: A EV +2.57 (adj +1.13) on $14.19, P(profit) 0.6041, adj growth 10.2 bp · B EV +1.88 (adj +0.89) on $10.37, P(profit) 0.4302, adj growth 8.3 bp · C EV +1.42 (adj +0.84) on $7.67, P(profit) 0.3562, adj growth 7.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ DET  ·  10000 joint draws  ·  404 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.44 | 0.56 | 0.00 | 6.0 | 27.0/26.9 | 23.1/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.45 | 5.88 | 27.4/27.1 | 23.8/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.41 | 0.59 | 0.00 | 9.32 | 28.6/28.6 | 21.8/23.0 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.077 | 0.52 | 0.48 | 0.00 | 6.01 | 31.8/21.3 | 18.1/28.0 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.47 | 5.9 | 31.9/21.6 | 18.4/28.5 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.065 | 0.37 | 0.63 | 0.00 | 6.05 | 21.6/31.8 | 27.4/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.077 | 0.066 | +0.024 | +0.012 | $1.36 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ assists YES | 29 | 0.355 | 0.318 | +0.051 | +0.013 | $2.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.24 vs 1.83 bp); despite a smaller raw edge (+0.024 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.073); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (1.83 vs 0.00 bp); despite a smaller raw edge (+0.051 vs +0.053/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.073); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.4172): highest fidelity KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes (same contract)
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3681, phi -0.13)
- KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3681, phi -0.266)

portfolios: A EV +1.79 (adj +0.68) on $7.44, P(profit) 0.396, adj growth 5.9 bp · B EV +0.97 (adj +0.40) on $3.48, P(profit) 0.396, adj growth 3.7 bp · C EV +0.55 (adj +0.14) on $3.30, P(profit) 0.3555, adj growth 1.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  394 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.171 | 0.83 | 0.17 | 0.00 | 6.04 | 32.8/20.4 | 18.4/27.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.124 | 0.83 | 0.17 | 0.00 | 9.26 | 34.6/21.8 | 17.9/25.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.60 | 0.40 | 0.48 | 5.94 | 33.1/20.8 | 17.8/29.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.79 | 0.21 | 0.00 | 6.0 | 27.2/26.4 | 24.0/22.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.79 | 0.21 | 0.00 | 9.32 | 29.0/28.0 | 23.7/20.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.54 | 0.46 | 0.50 | 5.98 | 27.3/26.6 | 23.3/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.244 | 0.229 | +0.043 | +0.029 | $4.06 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 2+ assists NO | 71 | 0.794 | 0.747 | +0.070 | +0.023 | $10.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 42 | 0.500 | 0.458 | +0.063 | +0.020 | $2.15 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Victor Hedman: 1+ goals NO | 90 | 0.926 | 0.917 | +0.020 | +0.011 | $10.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: higher confidence-adjusted growth (11.03 vs 3.71 bp); despite a smaller raw edge (+0.043 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.15); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense suppressed (<= 2 goals)
- **Nikita Kucherov: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: higher confidence-adjusted growth (5.67 vs 3.71 bp); wins across more scripts (relative breadth 1.03 vs 0.856); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.227); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.042); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: higher confidence-adjusted growth (3.71 vs 1.49 bp); despite a smaller raw edge (+0.063 vs +0.079/contract); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.15); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: REINFORCING (phi 0.227); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.065); failure: TBL wins by 2+
- **Victor Hedman: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi 0.042); KXNHLSPREAD-26NOV05CHITB-TB2|no: MOSTLY_INDEPENDENT (phi 0.065); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · high event (8+) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.239): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.2449): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05CHITB-TB3|no less than the minimum stake; KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no kept
- thesis GAME:TIGHT (p 0.3739): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.552, phi -0.251)
- KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5652, phi -0.304)
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.5, phi -1.0)
- KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5652, phi -0.092)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05CHITB-TB3|no less than the minimum stake; KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no kept

portfolios: A EV +1.97 (adj +0.51) on $15.06, P(profit) 0.6532, adj growth 4.6 bp · B EV +2.38 (adj +1.12) on $26.49, P(profit) 0.5312, adj growth 10.5 bp · C EV +3.30 (adj +1.54) on $36.60, P(profit) 0.5312, adj growth 14.1 bp · R EV +0.14 (adj +0.05) on $1.00, P(profit) 0.5, adj growth 1.8 bp

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.139 | 0.61 | 0.39 | 0.00 | 6.01 | 33.4/21.3 | 18.3/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.58 | 0.42 | 0.00 | 6.01 | 27.6/27.0 | 23.7/23.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.47 | 5.91 | 33.5/21.6 | 18.4/30.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.46 | 5.92 | 27.6/27.0 | 23.8/24.4 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.081 | 0.63 | 0.37 | 0.00 | 9.22 | 35.1/22.8 | 17.9/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.55 | 0.45 | 0.00 | 9.24 | 29.6/28.8 | 23.1/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 21 | 0.270 | 0.252 | +0.049 | +0.030 | $4.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Connor McMichael: 1+ goals YES | 16 | 0.195 | 0.184 | +0.025 | +0.014 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 23 | 0.270 | 0.258 | +0.028 | +0.015 | $2.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 61 | 0.658 | 0.643 | +0.031 | +0.017 | $5.83 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05STLNJ-STL2|yes; why: higher confidence-adjusted growth (11.18 vs 4.34 bp); despite a smaller raw edge (+0.049 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.956 vs 0.55); relationships: KXNHLGOAL-26NOV05STLNJ-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: STL offense suppressed (<= 2 goals)
- **Connor McMichael: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (11.18 vs 3.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.018); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: STL offense suppressed (<= 2 goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (11.18 vs 2.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05STLNJ-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: STL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05STLNJ-STL2|yes; why: KXNHLSPREAD-26NOV05STLNJ-STL2|yes has the higher standalone adjusted growth (4.34 vs 2.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.165); relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05STLNJ-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: NJD offense succeeds (4+ goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3375): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4517): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS_BY_2PLUS (p 0.2408): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no (same contract)
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4488, phi -0.263)
- KXNHLGOAL-26NOV05STLNJ-STLCMCMICHAEL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4488, phi -0.201)
- KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4488, phi -0.253)
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4176, phi -0.246)

portfolios: A EV +2.64 (adj +0.84) on $15.06, P(profit) 0.4759, adj growth 7.0 bp · B EV +1.91 (adj +1.11) on $15.00, P(profit) 0.4802, adj growth 10.4 bp · C EV +2.72 (adj +1.26) on $13.00, P(profit) 0.6394, adj growth 11.4 bp · R EV +0.10 (adj +0.05) on $2.00, P(profit) 0.6578, adj growth 1.9 bp

## CAR @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 13 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.126 | 0.41 | 0.59 | 0.00 | 6.06 | 21.1/33.0 | 28.6/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.49 | 0.51 | 0.00 | 6.03 | 26.5/27.2 | 23.6/22.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.43 | 0.57 | 0.49 | 5.93 | 21.3/33.0 | 29.7/18.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.54 | 0.46 | 0.48 | 5.95 | 26.9/27.5 | 24.4/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.50 | 0.50 | 0.00 | 9.31 | 28.2/28.9 | 22.8/22.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.079 | 0.42 | 0.58 | 0.00 | 9.3 | 22.4/34.4 | 27.2/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.177 | 0.163 | +0.039 | +0.025 | $3.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 68 | 0.736 | 0.718 | +0.040 | +0.023 | $10.10 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.260 | 0.241 | +0.038 | +0.019 | $2.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: higher confidence-adjusted growth (11.01 vs 10.70 bp); despite a smaller raw edge (+0.039 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.935 vs 0.577); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: NYI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes has the higher standalone adjusted growth (6.10 vs 5.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.146); relationships: KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CAR offense succeeds (4+ goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes has the higher standalone adjusted growth (10.70 vs 4.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.210); relationships: KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NYI:OFFENSE_4PLUS (p 0.3887): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — Broad expression KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.56 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:WINS_BY_2PLUS (p 0.2707): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4828): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.396, phi -0.18)
- KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4158, phi -0.237)
- KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.396, phi -0.241)
- override: Broad expression KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.56 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.17 (adj +0.50) on $15.06, P(profit) 0.5516, adj growth 4.0 bp · B EV +2.07 (adj +1.20) on $16.51, P(profit) 0.3388, adj growth 11.2 bp · C EV +2.27 (adj +0.83) on $5.78, P(profit) 0.3373, adj growth 7.5 bp · R EV +0.17 (adj +0.10) on $3.00, P(profit) 0.7355, adj growth 3.6 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CARNYI-NYI|yes == KXNHLGAME-26NOV05CARNYI-CAR|no

## PHI @ NYR  ·  10000 joint draws  ·  446 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_PHI_win | p_overtime | goals | shots NYR/PHI | NYR/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 5.98 | 26.1/26.1 | 22.9/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.54 | 0.46 | 0.47 | 5.92 | 26.4/26.3 | 23.0/23.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.078 | 0.62 | 0.38 | 0.00 | 6.01 | 30.9/20.8 | 18.0/26.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.58 | 0.42 | 0.00 | 9.16 | 27.8/27.8 | 22.3/21.5 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.55 | 0.45 | 0.45 | 5.86 | 31.2/21.1 | 17.9/27.9 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.065 | 0.46 | 0.54 | 0.00 | 6.0 | 20.9/30.8 | 27.1/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Konecny: 1+ assists NO | 68 | 0.748 | 0.711 | +0.052 | +0.016 | $7.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tye Kartye: 1+ assists YES | 24 | 0.301 | 0.263 | +0.049 | +0.010 | $1.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05PHINYR-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.69 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense succeeds (4+ goals)
- **Tye Kartye: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV05PHINYR-NYRTKARTYE24-1|yes; why: higher confidence-adjusted growth (1.26 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYR shot control · normal event (5-7) · decided (2+) 0.08.
- thesis PHI:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3828): highest fidelity KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes (same contract)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.238)
- KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3923, phi -0.258)

portfolios: A EV +1.40 (adj +0.34) on $10.92, P(profit) 0.3014, adj growth 3.0 bp · B EV +0.90 (adj +0.25) on $9.29, P(profit) 0.7477, adj growth 2.3 bp · C EV +1.24 (adj +0.34) on $12.81, P(profit) 0.7477, adj growth 3.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ PIT  ·  10000 joint draws  ·  424 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_BOS_win | p_overtime | goals | shots PIT/BOS | PIT/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.52 | 0.48 | 0.00 | 6.04 | 27.5/27.2 | 23.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.47 | 0.53 | 0.47 | 6.01 | 27.5/27.2 | 23.8/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.50 | 0.50 | 0.00 | 9.46 | 29.2/28.8 | 22.7/22.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 6.01 | 33.4/21.7 | 18.6/29.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.51 | 0.49 | 0.49 | 5.93 | 32.9/21.9 | 18.6/29.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.085 | 0.58 | 0.42 | 0.00 | 9.38 | 34.9/23.1 | 17.9/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.189 | 0.172 | +0.051 | +0.034 | $4.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 2+ goals YES | 6 | 0.092 | 0.081 | +0.029 | +0.017 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 33 | 0.391 | 0.372 | +0.045 | +0.026 | $3.33 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 70 | 0.760 | 0.725 | +0.045 | +0.010 | $6.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (20.29 vs 1.97 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: BOS wins (incl. OT/SO)
- **Rickard Rakell: 2+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (20.29 vs 9.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: DUPLICATIVE (phi 0.399); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.033); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (20.29 vs 6.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: DUPLICATIVE (phi 0.399); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.041); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05BOSPIT-PITBKINDEL81-1|no; why: higher confidence-adjusted growth (1.15 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.3121): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4448): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:SUPPRESSED (p 0.3355): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:WINS (p 0.4798, phi -0.221)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.194)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.267)
- KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4448, phi -0.213)

portfolios: A EV +3.12 (adj +1.81) on $15.06, P(profit) 0.4437, adj growth 16.8 bp · B EV +3.32 (adj +1.92) on $16.35, P(profit) 0.4437, adj growth 17.8 bp · C EV +2.38 (adj +1.58) on $6.47, P(profit) 0.1887, adj growth 14.1 bp · R EV +0.13 (adj +0.08) on $1.00, P(profit) 0.3909, adj growth 2.9 bp

## DAL @ CBJ  ·  10000 joint draws  ·  392 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 6.02 | 25.8/25.8 | 22.4/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.48 | 5.94 | 25.8/25.8 | 22.6/22.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.52 | 0.48 | 0.00 | 9.23 | 27.4/27.5 | 21.6/21.1 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.074 | 0.62 | 0.38 | 0.00 | 6.03 | 30.2/20.3 | 17.4/25.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.064 | 0.47 | 0.54 | 0.00 | 5.98 | 20.6/30.2 | 26.5/17.4 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.58 | 0.42 | 0.48 | 5.84 | 30.8/20.5 | 17.5/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 22 | 0.288 | 0.269 | +0.057 | +0.037 | $5.85 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cole Sillinger: 1+ goals YES | 14 | 0.178 | 0.163 | +0.030 | +0.014 | $1.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.108 | 0.096 | +0.023 | +0.011 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.209 | 0.195 | +0.029 | +0.015 | $2.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: higher confidence-adjusted growth (16.47 vs 4.58 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.325); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CBJ offense suppressed (<= 2 goals)
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (16.47 vs 3.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (16.47 vs 3.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes has the higher standalone adjusted growth (4.58 vs 3.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.169); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3926): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2522): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.2978): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3866, phi -0.247)
- KXNHLGOAL-26NOV05DALCBJ-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3866, phi -0.205)
- KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3866, phi -0.146)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3866, phi -0.231)

portfolios: A EV +3.46 (adj +1.50) on $15.06, P(profit) 0.3972, adj growth 12.6 bp · B EV +2.52 (adj +1.46) on $11.19, P(profit) 0.5876, adj growth 13.6 bp · C EV +2.47 (adj +1.45) on $9.00, P(profit) 0.3327, adj growth 13.0 bp · R EV +0.49 (adj +0.32) on $2.00, P(profit) 0.2885, adj growth 11.5 bp

## VAN @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| WPG shot control · normal event (5-7) · decided (2+) | 0.120 | 0.60 | 0.40 | 0.00 | 6.0 | 32.5/21.0 | 18.0/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.55 | 0.45 | 0.00 | 6.03 | 27.1/26.7 | 23.3/23.4 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.46 | 5.93 | 32.9/21.4 | 18.3/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.52 | 0.48 | 0.49 | 5.94 | 27.5/27.0 | 23.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.57 | 0.43 | 0.00 | 9.33 | 28.6/28.0 | 22.2/22.4 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.072 | 0.63 | 0.37 | 0.00 | 9.19 | 34.4/22.7 | 17.8/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 17 | 0.228 | 0.210 | +0.049 | +0.030 | $4.40 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.211 | 0.197 | +0.042 | +0.028 | $4.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 14 | 0.185 | 0.170 | +0.037 | +0.022 | $3.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 12 | 0.155 | 0.143 | +0.028 | +0.015 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (13.29 vs 11.91 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (13.29 vs 11.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (13.29 vs 8.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (13.29 vs 4.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts WPG shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3602): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2451): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4495): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4206, phi -0.23)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4206, phi -0.22)
- KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4206, phi -0.206)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4206, phi -0.194)

portfolios: A EV +2.61 (adj +0.79) on $15.06, P(profit) 0.6228, adj growth 7.0 bp · B EV +3.47 (adj +2.14) on $13.87, P(profit) 0.581, adj growth 19.9 bp · C EV +2.91 (adj +1.48) on $9.45, P(profit) 0.3848, adj growth 13.3 bp · R EV +0.54 (adj +0.34) on $2.00, P(profit) 0.2284, adj growth 11.7 bp

## ANA @ EDM  ·  10000 joint draws  ·  456 bet sides mapped, 18 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.146 | 0.62 | 0.38 | 0.00 | 9.75 | 29.7/29.7 | 24.0/22.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.63 | 0.37 | 0.00 | 6.12 | 27.9/27.9 | 24.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.53 | 0.47 | 0.47 | 6.09 | 28.1/28.2 | 24.8/24.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.070 | 0.68 | 0.32 | 0.00 | 9.67 | 34.6/23.8 | 18.8/26.5 | even strength |
| balanced shots · high event (8+) · tight (1-goal/OT) | 0.068 | 0.52 | 0.48 | 0.58 | 9.86 | 29.8/29.8 | 23.0/23.1 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.066 | 0.54 | 0.46 | 0.00 | 9.63 | 24.0/34.5 | 27.9/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 9 | 0.127 | 0.116 | +0.031 | +0.021 | $2.83 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 6 | 0.085 | 0.077 | +0.021 | +0.013 | $1.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.202 | 0.189 | +0.033 | +0.019 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.319 | 0.306 | +0.035 | +0.022 | $4.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (10.35 vs 5.86 bp); despite a smaller raw edge (+0.031 vs +0.033/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (6.21 vs 5.86 bp); despite a smaller raw edge (+0.021 vs +0.033/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes; why: higher confidence-adjusted growth (5.86 vs 2.38 bp); despite a smaller raw edge (+0.033 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.835 vs 0.54); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: ANA offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (5.15 vs 3.52 bp); despite a smaller raw edge (+0.035 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.15, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4363): highest fidelity KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5554): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2508): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMLDRAISAITL29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.151)
- KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.131)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.196)
- KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2508, phi -0.228)

portfolios: A EV +3.22 (adj +0.55) on $15.06, P(profit) 0.5639, adj growth 5.0 bp · B EV +2.53 (adj +1.61) on $11.55, P(profit) 0.571, adj growth 14.9 bp · C EV +3.00 (adj +1.41) on $25.30, P(profit) 0.3409, adj growth 12.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ COL  ·  10000 joint draws  ·  432 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NSH_win | p_overtime | goals | shots COL/NSH | COL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.152 | 0.76 | 0.24 | 0.00 | 6.01 | 34.8/22.2 | 20.0/29.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.117 | 0.79 | 0.21 | 0.00 | 9.31 | 36.8/23.6 | 19.5/27.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.59 | 0.41 | 0.47 | 5.97 | 35.3/22.6 | 19.5/31.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.71 | 0.29 | 0.00 | 6.07 | 29.2/28.4 | 25.7/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.71 | 0.29 | 0.00 | 9.44 | 30.9/30.0 | 25.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.51 | 0.49 | 0.47 | 5.98 | 29.2/28.5 | 25.2/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ assists NO | 70 | 0.792 | 0.744 | +0.078 | +0.029 | $10.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ assists NO | 39 | 0.469 | 0.427 | +0.062 | +0.020 | $4.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (9.06 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: NSH offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLCMAKAR8-1|no; why: higher confidence-adjusted growth (3.73 vs 0.61 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:SUPPRESSED (p 0.4751): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- thesis COL:SUPPRESSED (p 0.2624): highest fidelity KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no (same contract)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3091, phi -0.231)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5423, phi -0.301)

portfolios: A EV +1.58 (adj +0.54) on $12.05, P(profit) 0.4689, adj growth 5.1 bp · B EV +1.82 (adj +0.65) on $14.95, P(profit) 0.3749, adj growth 6.1 bp · C EV +2.50 (adj +0.89) on $20.62, P(profit) 0.3749, adj growth 8.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
