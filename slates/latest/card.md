# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T22:56:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 144.84 | +22.80 | +6.97 | +19.79 | 0.639 | -55.30 | -77.28 | 52.78 |
| B thesis-diversified (joint) ← optimiser card | 122.43 | +14.58 | +7.88 | +12.17 | 0.586 | -33.28 | -41.75 | 70.42 |
| C best expression per thesis | 64.68 | +12.69 | +6.88 | +1.82 | 0.522 | -41.40 | -41.40 | 60.27 |
| R FUNDED research stakes | 14.00 | +0.57 | +0.37 | +2.62 | 0.684 | -3.77 | -3.77 | 0.00 |

## MTL @ WPG  ·  10000 joint draws  ·  498 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.484 / away 0.516

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MTL_win | p_overtime | goals | shots WPG/MTL | WPG/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.49 | 0.51 | 0.00 | 6.0 | 27.2/27.1 | 23.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.47 | 0.53 | 0.46 | 5.94 | 27.5/27.4 | 24.1/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.46 | 0.54 | 0.00 | 9.22 | 28.6/28.7 | 22.5/22.9 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 6.0 | 32.0/21.6 | 18.4/28.3 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.52 | 0.48 | 0.48 | 5.92 | 32.0/21.8 | 18.4/28.9 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.058 | 0.40 | 0.60 | 0.00 | 6.04 | 21.8/31.8 | 27.8/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Iafallo: 1+ goals YES | 13 | 0.171 | 0.160 | +0.033 | +0.022 | $5.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Alexandre Carrier: 1+ goals YES | 4 | 0.060 | 0.054 | +0.017 | +0.011 | $2.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 18 | 0.213 | 0.204 | +0.023 | +0.013 | $3.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ goals NO | 89 | 0.916 | 0.907 | +0.019 | +0.010 | $20.00 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (8.56 vs 1.37 bp); relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT25MTLWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: WPG offense suppressed (<= 2 goals)
- **Alexandre Carrier: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25MTLWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: MTL offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT25MTLWPG-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (2.56 vs 0.00 bp); despite a smaller raw edge (+0.023 vs +0.041/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25MTLWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: MTL offense suppressed (<= 2 goals)
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT25MTLWPG-WPGMSCHEIFELE55-1|no; why: higher confidence-adjusted growth (2.50 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.023/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3718): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:OFFENSE_4PLUS (p 0.3975): highest fidelity KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.4076): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4076, phi -0.2)
- KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3853, phi -0.095)
- KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3853, phi -0.213)
- KXNHLGOAL-26OCT25MTLWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3718, phi -0.121)

portfolios: A EV +4.19 (adj +2.55) on $44.84, P(profit) 0.5431, adj growth 20.1 bp · B EV +3.40 (adj +2.12) on $32.52, P(profit) 0.3752, adj growth 18.3 bp · C EV +2.97 (adj +1.89) on $12.54, P(profit) 0.3886, adj growth 16.3 bp · R EV +0.11 (adj +0.06) on $5.00, P(profit) 0.9161, adj growth 2.1 bp

## COL @ NSH  ·  10000 joint draws  ·  464 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.325 / away 0.675

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.127 | 0.28 | 0.72 | 0.00 | 6.03 | 22.7/35.2 | 30.1/20.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.34 | 0.66 | 0.00 | 6.0 | 28.6/29.3 | 25.0/25.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.45 | 0.55 | 0.46 | 5.87 | 23.1/35.6 | 32.1/19.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.46 | 0.54 | 0.48 | 5.95 | 28.7/29.4 | 26.1/25.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.095 | 0.27 | 0.73 | 0.00 | 9.29 | 24.2/37.0 | 28.1/19.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.35 | 0.65 | 0.00 | 9.23 | 30.0/30.8 | 23.8/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 77 | 0.815 | 0.802 | +0.032 | +0.020 | $19.42 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 41 | 0.496 | 0.450 | +0.069 | +0.024 | $8.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.74) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ assists NO | 77 | 0.866 | 0.800 | +0.084 | +0.018 | $19.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Adam Edstrom: 1+ goals YES | 11 | 0.135 | 0.127 | +0.018 | +0.010 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (5.08 vs 4.92 bp); despite a smaller raw edge (+0.032 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (4.92 vs 3.38 bp); wins across more scripts (relative breadth 1.018 vs 0.879); relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: COL offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT25COLNSH-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (4.20 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: NSH offense succeeds (4+ goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH wins by 2+; alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: KXNHLSPREAD-26OCT25COLNSH-COL2|no has the higher standalone adjusted growth (3.38 vs 2.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.134); relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3001): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4215): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.1875): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.169)
- KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 26% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.316)
- KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3199, phi -0.162)
- KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4609, phi -0.213)

portfolios: A EV +6.14 (adj +1.73) on $50.00, P(profit) 0.5352, adj growth 12.7 bp · B EV +4.65 (adj +1.64) on $50.00, P(profit) 0.431, adj growth 14.7 bp · C EV +2.37 (adj +0.78) on $17.29, P(profit) 0.4958, adj growth 6.9 bp · R EV +0.21 (adj +0.13) on $5.00, P(profit) 0.8146, adj growth 4.6 bp

## MIN @ VAN  ·  10000 joint draws  ·  432 bet sides mapped, 28 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.369 / away 0.631

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| MIN shot control · normal event (5-7) · decided (2+) | 0.117 | 0.50 | 0.50 | 0.00 | 6.01 | 22.0/34.4 | 30.5/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.56 | 0.44 | 0.00 | 6.08 | 27.8/28.5 | 25.1/24.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.47 | 0.53 | 0.45 | 5.9 | 22.4/34.4 | 30.9/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.47 | 5.98 | 27.9/28.7 | 25.5/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 9.41 | 29.4/30.3 | 24.4/23.0 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.084 | 0.48 | 0.52 | 0.00 | 9.26 | 23.9/35.8 | 29.3/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marco Rossi: 1+ goals YES | 16 | 0.232 | 0.212 | +0.062 | +0.043 | $9.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 2+ goals NO | 85 | 0.915 | 0.897 | +0.056 | +0.038 | $13.19 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 58 | 0.659 | 0.638 | +0.062 | +0.041 | $13.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 51 | 0.624 | 0.543 | +0.097 | +0.016 | $3.62 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (28.04 vs 20.91 bp); relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.021); failure: VAN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV is 0.6 pts higher while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: DUPLICATIVE (phi 0.393); failure: MIN offense succeeds (4+ goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (27.41 vs 15.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.74 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: DUPLICATIVE (phi 0.393); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense succeeds (4+ goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis MIN:SUPPRESSED (p 0.3975): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5197): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no — Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV is 0.6 pts higher while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VAN:OFFENSE_4PLUS (p 0.4186): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.199)
- KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.263)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.264)
- KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.31)
- override: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV is 0.6 pts higher while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.74 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +12.47 (adj +2.69) on $50.00, P(profit) 0.6263, adj growth 20.0 bp · B EV +6.53 (adj +4.12) on $39.91, P(profit) 0.5471, adj growth 37.4 bp · C EV +7.36 (adj +4.21) on $34.85, P(profit) 0.3543, adj growth 37.1 bp · R EV +0.26 (adj +0.18) on $4.00, P(profit) 0.9148, adj growth 7.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
