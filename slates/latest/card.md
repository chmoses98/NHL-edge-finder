# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T17:16:46Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +28.15 | +9.82 | +26.68 | 0.727 | -27.24 | -41.87 | 88.30 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +25.29 | +13.82 | +23.12 | 0.715 | -26.47 | -40.11 | 129.33 |
| C best expression per thesis | 149.99 | +20.87 | +9.92 | +19.09 | 0.699 | -25.91 | -37.83 | 92.17 |
| R FUNDED research stakes | 16.00 | +2.32 | +1.38 | +1.34 | 0.561 | -6.38 | -8.72 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  432 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.57 | 0.43 | 0.00 | 6.05 | 27.1/27.6 | 24.3/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.45 | 5.96 | 27.4/28.0 | 24.7/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.57 | 0.43 | 0.00 | 9.43 | 28.9/29.4 | 23.8/21.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.099 | 0.49 | 0.51 | 0.00 | 6.01 | 21.7/33.1 | 29.5/18.3 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.48 | 0.52 | 0.46 | 5.94 | 21.7/32.8 | 29.4/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.070 | 0.48 | 0.52 | 0.00 | 9.33 | 23.3/35.1 | 28.7/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Caufield: 1+ assists YES | 33 | 0.412 | 0.369 | +0.067 | +0.023 | $4.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 67 | 0.721 | 0.707 | +0.035 | +0.021 | $8.45 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.220 | 0.207 | +0.030 | +0.017 | $2.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Cole Caufield: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA2|no; why: higher confidence-adjusted growth (5.22 vs 0.51 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MTL offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTALCOOLEY92-1|no; why: higher confidence-adjusted growth (4.59 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.15 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MTL:OFFENSE_4PLUS (p 0.4419): highest fidelity KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3926): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.3928): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes (same contract)
- KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3443, phi -0.275)
- KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3928, phi -0.233)
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3926, phi -0.219)

portfolios: A EV +1.86 (adj +0.82) on $14.45, P(profit) 0.5051, adj growth 7.6 bp · B EV +1.60 (adj +0.76) on $14.96, P(profit) 0.4142, adj growth 7.1 bp · C EV +1.87 (adj +0.88) on $17.43, P(profit) 0.4142, adj growth 8.2 bp · R EV +0.15 (adj +0.09) on $3.00, P(profit) 0.7206, adj growth 3.4 bp

## VGK @ DET  ·  10000 joint draws  ·  412 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.435 / away 0.565

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
| Brayden McNabb: 1+ goals YES | 5 | 0.077 | 0.067 | +0.024 | +0.013 | $1.39 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ assists YES | 29 | 0.355 | 0.315 | +0.051 | +0.011 | $1.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (7.57 vs 1.21 bp); despite a smaller raw edge (+0.024 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.073); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (1.21 vs 0.00 bp); despite a smaller raw edge (+0.051 vs +0.053/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.073); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.4172): highest fidelity KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes (same contract)
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3681, phi -0.13)
- KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3681, phi -0.266)

portfolios: A EV +1.74 (adj +0.66) on $7.26, P(profit) 0.396, adj growth 5.8 bp · B EV +0.87 (adj +0.40) on $2.86, P(profit) 0.396, adj growth 3.7 bp · C EV +0.34 (adj +0.07) on $2.03, P(profit) 0.3555, adj growth 0.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  394 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.777 / away 0.223

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
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.244 | 0.228 | +0.043 | +0.027 | $3.39 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 2+ assists NO | 71 | 0.794 | 0.747 | +0.070 | +0.023 | $9.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 41 | 0.500 | 0.450 | +0.073 | +0.023 | $2.44 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Victor Hedman: 1+ goals NO | 90 | 0.926 | 0.917 | +0.020 | +0.011 | $9.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: higher confidence-adjusted growth (10.10 vs 4.75 bp); despite a smaller raw edge (+0.043 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.15); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense suppressed (<= 2 goals)
- **Nikita Kucherov: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: higher confidence-adjusted growth (5.67 vs 4.75 bp); despite a smaller raw edge (+0.070 vs +0.073/contract); wins across more scripts (relative breadth 1.03 vs 0.856); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.227); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.042); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLGAME-26NOV05CHITB-CHI|yes; why: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLGAME-26NOV05CHITB-CHI|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 1.00 (STRUCTURAL vs STRUCTURAL; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.15); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: REINFORCING (phi 0.227); KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.065); failure: TBL wins by 2+
- **Victor Hedman: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi 0.042); KXNHLSPREAD-26NOV05CHITB-TB2|no: MOSTLY_INDEPENDENT (phi 0.065); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · high event (8+) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.239): highest fidelity KXNHLTEAMTOTAL-26NOV05CHITB-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.2449): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05CHITB-TB3|no less than the minimum stake; KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no kept
- thesis GAME:TIGHT (p 0.3739): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.552, phi -0.251)
- KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5652, phi -0.304)
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.0 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.5, phi -1.0)
- KXNHLGOAL-26NOV05CHITB-TBVHEDMAN77-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5652, phi -0.092)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05CHITB-TB3|no less than the minimum stake; KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no kept
- override: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLGAME-26NOV05CHITB-CHI|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 1.00 (STRUCTURAL vs STRUCTURAL; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +2.75 (adj +0.73) on $14.70, P(profit) 0.5, adj growth 6.3 bp · B EV +2.22 (adj +0.98) on $23.89, P(profit) 0.5312, adj growth 9.3 bp · C EV +2.58 (adj +1.14) on $27.84, P(profit) 0.5312, adj growth 10.7 bp · R EV +0.17 (adj +0.05) on $1.00, P(profit) 0.5, adj growth 2.1 bp

## STL @ NJD  ·  10000 joint draws  ·  434 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.653 / away 0.347

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.133 | 0.62 | 0.38 | 0.00 | 5.98 | 33.2/21.4 | 18.6/28.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.45 | 5.89 | 33.5/21.7 | 18.5/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.56 | 0.44 | 0.00 | 6.05 | 27.7/26.9 | 23.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.50 | 0.50 | 0.43 | 5.89 | 28.0/27.2 | 24.0/24.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.078 | 0.65 | 0.35 | 0.00 | 9.18 | 35.2/23.0 | 18.1/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.56 | 0.43 | 0.00 | 9.36 | 29.4/28.6 | 22.8/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 21 | 0.267 | 0.250 | +0.045 | +0.029 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 60 | 0.661 | 0.644 | +0.044 | +0.027 | $7.70 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 1.5 goals NO | 58 | 0.673 | 0.624 | +0.076 | +0.027 | $4.98 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Connor McMichael: 1+ goals YES | 16 | 0.193 | 0.182 | +0.023 | +0.013 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: higher confidence-adjusted growth (10.29 vs 6.60 bp); despite a smaller raw edge (+0.045 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26NOV05STLNJ-NJ2|no: REINFORCING (phi 0.166); KXNHLGOAL-26NOV05STLNJ-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: STL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: higher confidence-adjusted growth (6.97 vs 6.60 bp); despite a smaller raw edge (+0.044 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26NOV05STLNJ-NJ2|no: REINFORCING (phi 0.185); KXNHLGOAL-26NOV05STLNJ-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (6.97 vs 6.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.185); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: REINFORCING (phi 0.166); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.185); KXNHLGOAL-26NOV05STLNJ-STLCMCMICHAEL77-1|yes: MOSTLY_INDEPENDENT (phi 0.108); failure: NJD wins by 2+
- **Connor McMichael: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (10.29 vs 2.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26NOV05STLNJ-NJ2|no: MOSTLY_INDEPENDENT (phi 0.108); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.338): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3736): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4458): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4465, phi -0.258)
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4179, phi -0.255)
- KXNHLSPREAD-26NOV05STLNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3271, phi -1.0)
- KXNHLGOAL-26NOV05STLNJ-STLCMCMICHAEL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4465, phi -0.203)

portfolios: A EV +2.37 (adj +0.62) on $14.70, P(profit) 0.5514, adj growth 5.5 bp · B EV +2.17 (adj +1.17) on $17.99, P(profit) 0.5965, adj growth 11.0 bp · C EV +2.34 (adj +1.25) on $19.63, P(profit) 0.6022, adj growth 11.6 bp · R EV +0.40 (adj +0.18) on $4.00, P(profit) 0.4856, adj growth 6.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05STLNJ-NJ|no == KXNHLGAME-26NOV05STLNJ-STL|yes

## CAR @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.376 / away 0.624

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
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.783 | 0.768 | +0.039 | +0.025 | $9.56 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.157 | +0.032 | +0.019 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.158 | 0.144 | +0.031 | +0.016 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.256 | 0.238 | +0.035 | +0.017 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR3|no; why: higher confidence-adjusted growth (6.97 vs 6.17 bp); despite a smaller raw edge (+0.039 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: CAR offense succeeds (4+ goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes has the higher standalone adjusted growth (8.31 vs 6.80 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.168); relationships: KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes has the higher standalone adjusted growth (8.31 vs 5.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.155); relationships: KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.38 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.3886): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR3|no — Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.38 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYI:WINS (p 0.4764): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR3|no (same contract)
- thesis NYI:WINS_BY_2PLUS (p 0.2644): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR3|no (same contract)
- KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.417, phi -0.211)
- KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.196)
- KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.182)
- KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3918, phi -0.224)
- override: Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes selected over broad KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.38 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.08 (adj +0.55) on $14.70, P(profit) 0.5505, adj growth 4.5 bp · B EV +1.97 (adj +1.12) on $16.64, P(profit) 0.4179, adj growth 10.5 bp · C EV +1.99 (adj +0.71) on $13.56, P(profit) 0.811, adj growth 6.6 bp · R EV +0.16 (adj +0.10) on $3.00, P(profit) 0.7828, adj growth 3.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CARNYI-NYI|yes == KXNHLGAME-26NOV05CARNYI-CAR|no

## PHI @ NYR  ·  10000 joint draws  ·  450 bet sides mapped, 4 +EV candidates, 4 on card

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
| Cole Knuble: 1+ goals YES | 12 | 0.150 | 0.141 | +0.023 | +0.014 | $1.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tye Kartye: 1+ assists YES | 24 | 0.306 | 0.268 | +0.053 | +0.015 | $2.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Travis Konecny: 1+ assists NO | 68 | 0.743 | 0.709 | +0.048 | +0.014 | $6.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Travis Sanheim: 1+ assists YES | 25 | 0.306 | 0.275 | +0.043 | +0.012 | $1.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Cole Knuble: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes; why: higher confidence-adjusted growth (3.78 vs 1.69 bp); despite a smaller raw edge (+0.023 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.112); failure: PHI offense suppressed (<= 2 goals)
- **Tye Kartye: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (2.67 vs 0.30 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: NYR offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05PHINYR-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.02 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi -0.044); KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); failure: PHI offense succeeds (4+ goals)
- **Travis Sanheim: 1+ assists YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes has the higher standalone adjusted growth (3.78 vs 1.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.112); they share one thesis budget; relationships: KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.079); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3829): highest fidelity KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes (same contract)
- thesis PHI:SUPPRESSED (p 0.4576): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.208)
- KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3983, phi -0.251)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.222)
- KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.269)

portfolios: A EV +2.16 (adj +0.72) on $14.70, P(profit) 0.5107, adj growth 6.5 bp · B EV +1.53 (adj +0.54) on $12.37, P(profit) 0.4819, adj growth 5.1 bp · C EV +1.45 (adj +0.54) on $12.14, P(profit) 0.342, adj growth 5.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ PIT  ·  10000 joint draws  ·  424 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.499 / away 0.501

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_BOS_win | p_overtime | goals | shots PIT/BOS | PIT/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.51 | 0.49 | 0.00 | 6.08 | 27.7/27.2 | 23.6/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.52 | 0.48 | 0.00 | 9.45 | 29.6/29.1 | 23.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.49 | 6.06 | 27.7/27.3 | 23.8/24.3 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.098 | 0.56 | 0.44 | 0.00 | 6.05 | 33.0/21.7 | 18.6/28.9 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.55 | 0.45 | 0.45 | 5.97 | 33.0/21.9 | 18.6/29.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.086 | 0.61 | 0.39 | 0.00 | 9.45 | 35.1/23.3 | 18.0/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.184 | 0.168 | +0.047 | +0.030 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 33 | 0.390 | 0.371 | +0.044 | +0.026 | $4.43 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 11 | 0.149 | 0.132 | +0.033 | +0.015 | $1.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nick Robertson: 1+ goals YES | 16 | 0.191 | 0.181 | +0.022 | +0.011 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (16.70 vs 4.83 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (16.70 vs 6.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (16.70 vs 4.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: PIT offense suppressed (<= 2 goals)
- **Nick Robertson: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (16.70 vs 2.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3079): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4534): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.209)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.28)
- KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.19)
- KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3385, phi -0.184)

portfolios: A EV +3.50 (adj +1.99) on $13.63, P(profit) 0.5714, adj growth 18.0 bp · B EV +2.50 (adj +1.48) on $11.38, P(profit) 0.5714, adj growth 13.8 bp · C EV +1.52 (adj +0.99) on $4.49, P(profit) 0.1845, adj growth 9.1 bp · R EV +0.26 (adj +0.15) on $2.00, P(profit) 0.3899, adj growth 5.3 bp

## DAL @ CBJ  ·  10000 joint draws  ·  392 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.454 / away 0.546

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.53 | 0.47 | 0.00 | 6.04 | 25.8/25.8 | 22.5/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.46 | 5.92 | 26.0/25.9 | 22.7/22.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.54 | 0.46 | 0.00 | 9.24 | 27.3/27.3 | 21.7/21.2 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.073 | 0.60 | 0.40 | 0.00 | 6.04 | 30.4/20.4 | 17.4/26.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.066 | 0.44 | 0.56 | 0.00 | 6.0 | 20.7/30.6 | 26.8/17.6 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.58 | 0.42 | 0.47 | 5.88 | 30.6/20.6 | 17.6/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 22 | 0.288 | 0.268 | +0.056 | +0.036 | $5.34 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.215 | 0.200 | +0.035 | +0.020 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 16 | 0.202 | 0.188 | +0.033 | +0.018 | $2.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.107 | 0.095 | +0.022 | +0.010 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (15.88 vs 5.94 bp); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (15.88 vs 5.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (15.88 vs 5.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.019); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (15.88 vs 2.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3957): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2583): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3941, phi -0.252)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3941, phi -0.237)
- KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3941, phi -0.194)
- KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3941, phi -0.142)

portfolios: A EV +2.90 (adj +1.38) on $14.70, P(profit) 0.4725, adj growth 12.3 bp · B EV +2.61 (adj +1.56) on $11.79, P(profit) 0.6037, adj growth 14.6 bp · C EV +2.23 (adj +1.26) on $17.98, P(profit) 0.3319, adj growth 11.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

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
| Linus Karlsson: 1+ goals YES | 16 | 0.228 | 0.209 | +0.059 | +0.039 | $4.98 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.155 | 0.141 | +0.038 | +0.025 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.211 | 0.197 | +0.042 | +0.028 | $3.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 14 | 0.185 | 0.170 | +0.037 | +0.022 | $2.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (23.61 vs 11.91 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (23.61 vs 12.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (23.61 vs 11.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (23.61 vs 8.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts WPG shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3602): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2451): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4495): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4206, phi -0.23)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4206, phi -0.194)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4206, phi -0.22)
- KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4206, phi -0.206)

portfolios: A EV +3.11 (adj +1.10) on $14.70, P(profit) 0.5397, adj growth 10.1 bp · B EV +4.29 (adj +2.78) on $14.33, P(profit) 0.581, adj growth 26.0 bp · C EV +2.55 (adj +1.54) on $7.14, P(profit) 0.3195, adj growth 14.2 bp · R EV +0.70 (adj +0.47) on $2.00, P(profit) 0.2284, adj growth 16.7 bp

## ANA @ EDM  ·  10000 joint draws  ·  462 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.370

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
| Jeff Malott: 1+ goals YES | 8 | 0.127 | 0.114 | +0.041 | +0.029 | $3.33 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 5 | 0.085 | 0.071 | +0.031 | +0.018 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 9 | 0.129 | 0.116 | +0.034 | +0.020 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.202 | 0.190 | +0.033 | +0.021 | $2.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.10 vs 6.63 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (12.88 vs 6.63 bp); despite a smaller raw edge (+0.031 vs +0.033/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: ANA offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (9.81 vs 5.15 bp); despite a smaller raw edge (+0.033 vs +0.035/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (6.63 vs 3.29 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV05ANAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.15, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4363): highest fidelity KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5554): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2508): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMLDRAISAITL29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.151)
- KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.131)
- KXNHLGOAL-26NOV05ANAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2508, phi -0.138)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.196)

portfolios: A EV +3.22 (adj +0.78) on $14.70, P(profit) 0.553, adj growth 7.3 bp · B EV +4.04 (adj +2.55) on $10.33, P(profit) 0.4482, adj growth 23.7 bp · C EV +2.26 (adj +0.98) on $12.07, P(profit) 0.708, adj growth 9.1 bp · R EV +0.49 (adj +0.34) on $1.00, P(profit) 0.1266, adj growth 12.2 bp

## NSH @ COL  ·  10000 joint draws  ·  438 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

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
| Mavrik Bourque: 1+ assists NO | 71 | 0.792 | 0.746 | +0.068 | +0.022 | $9.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ assists NO | 39 | 0.469 | 0.427 | +0.062 | +0.020 | $3.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (5.21 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: NSH offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLCMAKAR8-1|no; why: higher confidence-adjusted growth (3.73 vs 0.61 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:SUPPRESSED (p 0.4751): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- thesis COL:SUPPRESSED (p 0.2624): highest fidelity KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no (same contract)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3091, phi -0.231)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5423, phi -0.301)

portfolios: A EV +1.45 (adj +0.47) on $11.76, P(profit) 0.4689, adj growth 4.4 bp · B EV +1.49 (adj +0.48) on $13.46, P(profit) 0.3749, adj growth 4.5 bp · C EV +1.74 (adj +0.56) on $15.68, P(profit) 0.3749, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
