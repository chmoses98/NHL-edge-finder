# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T15:17:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +25.58 | +9.14 | +23.32 | 0.723 | -25.41 | -37.51 | 82.89 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +20.63 | +11.02 | +18.75 | 0.713 | -22.81 | -32.87 | 104.20 |
| C best expression per thesis | 150.01 | +24.00 | +11.65 | +21.37 | 0.699 | -30.00 | -42.96 | 106.96 |
| R FUNDED research stakes | 17.00 | +1.44 | +0.79 | +1.00 | 0.624 | -5.22 | -6.98 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.54 | 0.46 | 0.00 | 6.05 | 27.3/27.7 | 24.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.46 | 6.0 | 27.3/27.8 | 24.5/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.57 | 0.43 | 0.00 | 9.41 | 28.6/29.0 | 23.3/21.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.094 | 0.47 | 0.53 | 0.00 | 6.04 | 21.7/32.9 | 29.0/18.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.50 | 0.50 | 0.46 | 5.91 | 21.8/33.1 | 29.8/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.075 | 0.43 | 0.57 | 0.00 | 9.34 | 23.3/34.7 | 27.7/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 18 | 0.233 | 0.217 | +0.042 | +0.027 | $3.57 | FUNDED_RESEARCH | $1 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 18 | 0.229 | 0.214 | +0.039 | +0.024 | $2.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 14 | 0.173 | 0.163 | +0.024 | +0.015 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 67 | 0.740 | 0.700 | +0.054 | +0.014 | $6.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes; why: higher confidence-adjusted growth (9.93 vs 0.22 bp); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.169); failure: UTA offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (8.08 vs 3.74 bp); relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: MTL offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA2|no; why: higher confidence-adjusted growth (3.74 vs 0.52 bp); despite a smaller raw edge (+0.024 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.029); failure: UTA wins (incl. OT/SO)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA2|no; why: higher confidence-adjusted growth (2.07 vs 0.52 bp); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.169); KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.029); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4101): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4392): highest fidelity KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS_BY_2PLUS (p 0.3004): highest fidelity KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes (same contract)
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.371, phi -0.211)
- KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3422, phi -0.212)
- KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:WINS (p 0.4803, phi -0.207)
- KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4101, phi -0.231)

portfolios: A EV +2.34 (adj +1.10) on $14.94, P(profit) 0.5589, adj growth 10.3 bp · B EV +2.18 (adj +1.17) on $14.82, P(profit) 0.4933, adj growth 11.0 bp · C EV +3.24 (adj +1.73) on $22.02, P(profit) 0.4933, adj growth 15.9 bp · R EV +0.22 (adj +0.14) on $1.00, P(profit) 0.2326, adj growth 5.2 bp

## VGK @ DET  ·  10000 joint draws  ·  410 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.43 | 0.57 | 0.00 | 6.04 | 27.1/26.9 | 22.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.47 | 0.53 | 0.49 | 5.97 | 27.1/27.0 | 23.7/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.42 | 0.58 | 0.00 | 9.3 | 28.7/28.8 | 22.4/22.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.077 | 0.48 | 0.52 | 0.00 | 5.96 | 31.8/21.3 | 17.7/28.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.46 | 5.9 | 32.3/21.7 | 18.3/28.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.062 | 0.33 | 0.67 | 0.00 | 6.03 | 21.2/31.4 | 26.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.078 | 0.067 | +0.025 | +0.014 | $1.22 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ assists YES | 28 | 0.349 | 0.312 | +0.055 | +0.018 | $2.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (8.08 vs 3.34 bp); despite a smaller raw edge (+0.025 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.063); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (3.34 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.063); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes (same contract)
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3663, phi -0.13)
- KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3663, phi -0.279)

portfolios: A EV +1.97 (adj +0.86) on $7.73, P(profit) 0.3916, adj growth 7.6 bp · B EV +0.98 (adj +0.45) on $3.46, P(profit) 0.3916, adj growth 4.3 bp · C EV +0.68 (adj +0.22) on $3.63, P(profit) 0.3489, adj growth 2.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.244 | 0.229 | +0.043 | +0.029 | $3.29 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 55 | 0.636 | 0.591 | +0.069 | +0.023 | $3.66 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Victor Hedman: 1+ goals NO | 90 | 0.926 | 0.917 | +0.020 | +0.011 | $8.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 2+ assists NO | 72 | 0.794 | 0.750 | +0.060 | +0.015 | $5.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: higher confidence-adjusted growth (10.98 vs 4.79 bp); despite a smaller raw edge (+0.043 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV05CHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: higher confidence-adjusted growth (4.79 vs 3.71 bp); wins across more scripts (relative breadth 1.071 vs 0.856); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.061); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: REINFORCING (phi 0.238); failure: TBL wins by 2+
- **Victor Hedman: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV05CHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.061); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi 0.042); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB3|no has the higher standalone adjusted growth (4.79 vs 2.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.238); they share one thesis budget; relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV05CHITB-TB3|no: REINFORCING (phi 0.238); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.042); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · high event (8+) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.239): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.3739): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB3|no (same contract)
- thesis TBL:SUPPRESSED (p 0.2449): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB3|no (same contract)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.552, phi -0.251)
- KXNHLSPREAD-26NOV05CHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.5, phi -0.757)
- KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5652, phi -0.092)
- KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5652, phi -0.304)

portfolios: A EV +1.82 (adj +0.54) on $14.94, P(profit) 0.6532, adj growth 4.8 bp · B EV +1.76 (adj +0.83) on $20.43, P(profit) 0.6142, adj growth 7.8 bp · C EV +2.12 (adj +1.10) on $23.78, P(profit) 0.6698, adj growth 10.2 bp · R EV +0.34 (adj +0.18) on $2.00, P(profit) 0.2441, adj growth 6.9 bp

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.126 | 0.61 | 0.39 | 0.00 | 6.0 | 33.2/21.4 | 18.5/29.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.54 | 0.46 | 0.45 | 5.89 | 33.5/21.7 | 18.5/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.56 | 0.44 | 0.00 | 6.04 | 27.5/26.9 | 23.7/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.49 | 0.51 | 0.47 | 5.95 | 27.8/27.1 | 23.8/24.4 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.088 | 0.62 | 0.38 | 0.00 | 9.23 | 34.7/22.9 | 17.9/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.56 | 0.44 | 0.00 | 9.26 | 29.6/28.9 | 23.2/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 60 | 0.661 | 0.644 | +0.044 | +0.028 | $7.01 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 22 | 0.270 | 0.255 | +0.038 | +0.023 | $2.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 72 | 0.789 | 0.752 | +0.055 | +0.018 | $4.01 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dylan Holloway: 1+ goals YES | 23 | 0.272 | 0.259 | +0.030 | +0.017 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05STLNJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (7.05 vs 4.01 bp); despite a smaller raw edge (+0.044 vs +0.097/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26NOV05STLNJ-NJ3|no: REINFORCING (phi 0.152); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes; why: higher confidence-adjusted growth (6.35 vs 4.00 bp); despite a smaller raw edge (+0.038 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.942 vs 0.569); relationships: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26NOV05STLNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: STL offense suppressed (<= 2 goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: Broad expression KXNHLSPREAD-26NOV05STLNJ-NJ3|no selected over player prop KXNHLAST-26NOV05STLNJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.152); KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.145); failure: NJD wins by 2+
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (6.35 vs 3.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26NOV05STLNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.145); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.3723): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — Broad expression KXNHLSPREAD-26NOV05STLNJ-NJ3|no selected over player prop KXNHLAST-26NOV05STLNJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis STL:OFFENSE_4PLUS (p 0.3471): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4543): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4173, phi -0.252)
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4352, phi -0.251)
- KXNHLSPREAD-26NOV05STLNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3194, phi -0.754)
- KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4352, phi -0.256)
- override: Broad expression KXNHLSPREAD-26NOV05STLNJ-NJ3|no selected over player prop KXNHLAST-26NOV05STLNJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.92 (adj +0.55) on $14.94, P(profit) 0.6686, adj growth 5.1 bp · B EV +1.50 (adj +0.82) on $15.79, P(profit) 0.6526, adj growth 7.8 bp · C EV +2.01 (adj +1.06) on $16.71, P(profit) 0.6905, adj growth 9.8 bp · R EV +0.29 (adj +0.14) on $4.00, P(profit) 0.5509, adj growth 5.2 bp

## CAR @ NYI  ·  10000 joint draws  ·  420 bet sides mapped, 17 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.121 | 0.41 | 0.59 | 0.00 | 5.96 | 21.0/32.5 | 28.5/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.51 | 0.49 | 0.00 | 6.01 | 26.2/26.8 | 23.3/22.6 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.48 | 0.52 | 0.46 | 5.87 | 21.4/33.0 | 29.7/18.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.50 | 5.96 | 26.7/27.4 | 24.1/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.53 | 0.47 | 0.00 | 9.27 | 28.2/28.9 | 23.0/22.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.081 | 0.43 | 0.57 | 0.00 | 9.3 | 22.6/34.6 | 27.6/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 12 | 0.158 | 0.145 | +0.031 | +0.018 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.257 | 0.242 | +0.035 | +0.021 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 68 | 0.735 | 0.717 | +0.040 | +0.022 | $7.68 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 16 | 0.199 | 0.187 | +0.030 | +0.017 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes has the higher standalone adjusted growth (9.87 vs 5.95 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.175); relationships: KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes has the higher standalone adjusted growth (9.87 vs 5.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.209); relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NYI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes has the higher standalone adjusted growth (7.09 vs 5.08 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.145); relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CAR offense succeeds (4+ goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.31 vs 0.56 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NYI:OFFENSE_4PLUS (p 0.3867): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.31 vs 0.56 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYI:WINS_BY_2PLUS (p 0.2741): highest fidelity KXNHLSPREAD-26NOV05CARNYI-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.495): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3955, phi -0.185)
- KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3955, phi -0.222)
- KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4066, phi -0.24)
- KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3955, phi -0.212)
- override: Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.31 vs 0.56 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.76 (adj +0.48) on $14.94, P(profit) 0.5517, adj growth 4.2 bp · B EV +1.67 (adj +0.96) on $14.24, P(profit) 0.4157, adj growth 9.1 bp · C EV +1.90 (adj +0.70) on $5.05, P(profit) 0.3409, adj growth 6.4 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.7348, adj growth 2.4 bp

## PHI @ NYR  ·  10000 joint draws  ·  444 bet sides mapped, 2 +EV candidates, 2 on card


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
| Travis Konecny: 1+ assists NO | 68 | 0.748 | 0.711 | +0.052 | +0.016 | $5.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tye Kartye: 1+ assists YES | 24 | 0.301 | 0.266 | +0.049 | +0.013 | $1.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05PHINYR-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.69 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense succeeds (4+ goals)
- **Tye Kartye: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV05PHINYR-NYRTKARTYE24-1|yes; why: higher confidence-adjusted growth (1.93 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYR shot control · normal event (5-7) · decided (2+) 0.08.
- thesis PHI:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3828): highest fidelity KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes (same contract)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.238)
- KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3923, phi -0.258)

portfolios: A EV +1.39 (adj +0.39) on $10.83, P(profit) 0.3014, adj growth 3.4 bp · B EV +0.76 (adj +0.22) on $7.54, P(profit) 0.7477, adj growth 2.1 bp · C EV +1.13 (adj +0.33) on $11.20, P(profit) 0.7477, adj growth 3.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ PIT  ·  10000 joint draws  ·  424 bet sides mapped, 8 +EV candidates, 4 on card


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
| Connor Dewar: 1+ goals YES | 12 | 0.189 | 0.170 | +0.061 | +0.043 | $4.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 33 | 0.391 | 0.372 | +0.045 | +0.026 | $4.02 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Hendrix Lapierre: 1+ goals YES | 12 | 0.152 | 0.142 | +0.025 | +0.015 | $1.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 69 | 0.760 | 0.723 | +0.055 | +0.018 | $8.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (35.01 vs 3.77 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: BOS wins (incl. OT/SO)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: Player prop expression KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes because adjusted EV is 0.9 pts higher while thesis capture is 0.53 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.041); failure: PIT offense suppressed (<= 2 goals)
- **Hendrix Lapierre: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (35.01 vs 4.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05BOSPIT-PITBKINDEL81-1|no; why: higher confidence-adjusted growth (3.26 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.3121): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4448): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes — Player prop expression KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes because adjusted EV is 0.9 pts higher while thesis capture is 0.53 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis PIT:SUPPRESSED (p 0.3355): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:WINS (p 0.4798, phi -0.221)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.267)
- KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.156)
- KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4448, phi -0.213)
- override: Player prop expression KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes because adjusted EV is 0.9 pts higher while thesis capture is 0.53 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +3.75 (adj +2.36) on $14.94, P(profit) 0.4437, adj growth 22.0 bp · B EV +3.68 (adj +2.23) on $18.45, P(profit) 0.4926, adj growth 20.9 bp · C EV +3.23 (adj +2.26) on $6.71, P(profit) 0.1887, adj growth 20.5 bp · R EV +0.26 (adj +0.15) on $2.00, P(profit) 0.3909, adj growth 5.5 bp

## DAL @ CBJ  ·  10000 joint draws  ·  392 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.03 | 25.8/25.9 | 22.5/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.49 | 5.92 | 25.8/25.8 | 22.6/22.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.55 | 0.45 | 0.00 | 9.29 | 27.6/27.6 | 21.9/21.3 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 5.99 | 30.5/20.7 | 17.8/26.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.48 | 0.52 | 0.00 | 5.95 | 20.5/30.1 | 26.4/17.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.56 | 0.44 | 0.49 | 5.9 | 30.4/20.6 | 17.4/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 23 | 0.285 | 0.270 | +0.043 | +0.028 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.213 | 0.199 | +0.034 | +0.019 | $2.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Esa Lindell: 1+ goals NO | 92 | 0.950 | 0.938 | +0.025 | +0.013 | $8.24 | FUNDED_RESEARCH | $3 | DAL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.111 | 0.098 | +0.025 | +0.013 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (9.14 vs 5.26 bp); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05DALCBJ-DALELINDELL23-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (9.14 vs 5.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05DALCBJ-DALELINDELL23-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Esa Lindell: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05DALCBJ-CBJ3|yes; why: higher confidence-adjusted growth (5.15 vs 1.80 bp); despite a smaller raw edge (+0.025 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.997 vs 0.444); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: DAL offense succeeds (4+ goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (9.14 vs 4.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.019); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-DALELINDELL23-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.397): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.3064): highest fidelity KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2477): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.234)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.245)
- KXNHLGOAL-26NOV05DALCBJ-DALELINDELL23-1|no: FUNDED_RESEARCH; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3553, phi -0.106)
- KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.141)

portfolios: A EV +2.52 (adj +0.70) on $14.94, P(profit) 0.4535, adj growth 5.2 bp · B EV +1.68 (adj +0.96) on $15.44, P(profit) 0.4827, adj growth 9.1 bp · C EV +1.90 (adj +1.05) on $9.53, P(profit) 0.4379, adj growth 9.7 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.9504, adj growth 1.6 bp

## VAN @ WPG  ·  10000 joint draws  ·  408 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| WPG shot control · normal event (5-7) · decided (2+) | 0.117 | 0.62 | 0.38 | 0.00 | 6.02 | 32.6/21.1 | 18.2/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.53 | 0.47 | 0.00 | 6.06 | 27.3/26.7 | 23.2/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.50 | 5.94 | 27.4/26.8 | 23.5/24.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.49 | 5.86 | 32.8/21.4 | 18.2/29.5 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.079 | 0.62 | 0.38 | 0.00 | 9.28 | 34.4/22.7 | 17.7/26.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.58 | 0.42 | 0.00 | 9.3 | 29.1/28.5 | 22.9/22.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marco Rossi: 1+ goals YES | 15 | 0.215 | 0.194 | +0.056 | +0.035 | $3.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.229 | 0.212 | +0.049 | +0.032 | $3.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Nino Niederreiter: 1+ goals NO | 84 | 0.887 | 0.873 | +0.037 | +0.023 | $8.24 | FUNDED_RESEARCH | $3 | WPG:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 12 | 0.157 | 0.147 | +0.030 | +0.019 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (19.52 vs 15.03 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05VANWPG-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes has the higher standalone adjusted growth (19.52 vs 15.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05VANWPG-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: VAN offense suppressed (<= 2 goals)
- **Nino Niederreiter: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05VANWPG-WPG3|no; why: KXNHLSPREAD-26NOV05VANWPG-WPG3|no has the higher standalone adjusted growth (9.89 vs 9.34 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.112); relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: WPG offense succeeds (4+ goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes has the higher standalone adjusted growth (19.52 vs 7.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05VANWPG-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts WPG shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3614): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4556): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3579): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4173, phi -0.228)
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4173, phi -0.229)
- KXNHLGOAL-26NOV05VANWPG-WPGNNIEDERREITER62-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4174, phi -0.15)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4173, phi -0.184)

portfolios: A EV +2.66 (adj +1.11) on $14.94, P(profit) 0.6099, adj growth 10.4 bp · B EV +3.27 (adj +2.07) on $18.01, P(profit) 0.4826, adj growth 19.6 bp · C EV +3.28 (adj +1.70) on $17.63, P(profit) 0.2151, adj growth 15.7 bp · R EV +0.13 (adj +0.08) on $3.00, P(profit) 0.8868, adj growth 3.2 bp

## ANA @ EDM  ·  10000 joint draws  ·  456 bet sides mapped, 15 +EV candidates, 4 on card


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
| Jeff Malott: 1+ goals YES | 9 | 0.127 | 0.114 | +0.031 | +0.018 | $1.80 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.202 | 0.190 | +0.033 | +0.021 | $2.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 14 | 0.176 | 0.165 | +0.028 | +0.016 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 68 | 0.761 | 0.716 | +0.066 | +0.021 | $7.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (8.00 vs 6.63 bp); despite a smaller raw edge (+0.031 vs +0.033/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05ANAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.013); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes; why: higher confidence-adjusted growth (6.63 vs 2.38 bp); despite a smaller raw edge (+0.033 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.835 vs 0.54); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05ANAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.014); failure: ANA offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (4.63 vs 3.52 bp); despite a smaller raw edge (+0.028 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.039); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (4.34 vs 2.63 bp); despite a smaller raw edge (+0.066 vs +0.083/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV05ANAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.039); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.15, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4363): highest fidelity KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2508): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5554): highest fidelity KXNHLTOTAL-26NOV05ANAEDM-9|yes [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.151)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.196)
- KXNHLGOAL-26NOV05ANAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2508, phi -0.157)
- KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5554, phi -0.324)

portfolios: A EV +2.88 (adj +0.66) on $14.94, P(profit) 0.5839, adj growth 6.1 bp · B EV +2.14 (adj +1.07) on $13.77, P(profit) 0.3934, adj growth 10.1 bp · C EV +2.99 (adj +1.14) on $21.79, P(profit) 0.5063, adj growth 10.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ COL  ·  10000 joint draws  ·  426 bet sides mapped, 2 +EV candidates, 2 on card


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
| Nathan MacKinnon: 1+ assists NO | 39 | 0.469 | 0.427 | +0.062 | +0.020 | $3.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ assists NO | 70 | 0.792 | 0.726 | +0.078 | +0.011 | $4.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLCMAKAR8-1|no; why: higher confidence-adjusted growth (3.73 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: COL offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (1.33 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: NSH offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis COL:SUPPRESSED (p 0.2624): highest fidelity KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4751): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5423, phi -0.301)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.2 pts; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3091, phi -0.231)

portfolios: A EV +1.56 (adj +0.39) on $11.95, P(profit) 0.4689, adj growth 3.6 bp · B EV +1.03 (adj +0.24) on $8.05, P(profit) 0.4689, adj growth 2.3 bp · C EV +1.52 (adj +0.36) on $11.96, P(profit) 0.4689, adj growth 3.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
