# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T12:29:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +23.13 | +6.89 | +22.15 | 0.625 | -52.82 | -65.51 | 52.05 |
| B thesis-diversified (joint) ← optimiser card | 71.39 | +11.44 | +4.28 | +7.69 | 0.544 | -27.47 | -41.94 | 37.55 |
| C best expression per thesis | 61.63 | +8.93 | +3.10 | -0.66 | 0.478 | -27.72 | -27.72 | 27.45 |
| R FUNDED research stakes | 13.00 | +1.08 | +0.53 | +0.18 | 0.624 | -4.76 | -7.86 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PIT_win | p_overtime | goals | shots WSH/PIT | WSH/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.46 | 0.00 | 6.05 | 27.2/27.5 | 24.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.49 | 5.99 | 27.3/27.7 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.55 | 0.45 | 0.00 | 9.43 | 28.8/29.0 | 23.0/22.2 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.081 | 0.47 | 0.53 | 0.00 | 6.01 | 21.6/32.5 | 28.7/18.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.46 | 5.93 | 21.9/32.6 | 29.2/18.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.065 | 0.49 | 0.51 | 0.00 | 9.44 | 23.6/34.6 | 27.8/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Rickard Rakell: 1+ goals YES | 28 | 0.346 | 0.326 | +0.052 | +0.032 | $10.34 | FUNDED_RESEARCH | $3 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.174 | 0.150 | +0.046 | +0.023 | $5.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.257 | 0.235 | +0.046 | +0.024 | $7.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Washington wins by over 1.5 goals NO | 63 | 0.689 | 0.657 | +0.043 | +0.011 | $5.73 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (10.52 vs 10.25 bp); relationships: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLSPREAD-26OCT07PITWSH-WSH2|no: REINFORCING (phi 0.163); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes has the higher standalone adjusted growth (10.52 vs 10.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT07PITWSH-WSH2|no: MOSTLY_INDEPENDENT (phi 0.138); failure: PIT offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT07PITWSH-5|yes; why: higher confidence-adjusted growth (7.66 vs 0.12 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.894 vs 0.756); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT07PITWSH-WSH2|no: INTENTIONAL_DIVERSIFIER (phi -0.197); failure: WSH offense suppressed (<= 2 goals)
- **Washington wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLPTS-26OCT07PITWSH-WSHATUCH89-1|no; why: Broad expression KXNHLSPREAD-26OCT07PITWSH-WSH2|no selected over player prop KXNHLPTS-26OCT07PITWSH-WSHATUCH89-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.98 vs 0.76 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: REINFORCING (phi 0.163); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.197); failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4131): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4538): highest fidelity KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes (same contract)
- thesis PIT:WINS (p 0.4751): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT07PITWSH-WSHATUCH89-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3705, phi -0.261)
- KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3705, phi -0.208)
- KXNHLGOAL-26OCT07PITWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.332, phi -0.222)
- KXNHLSPREAD-26OCT07PITWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.3106, phi -1.0)
- override: Broad expression KXNHLSPREAD-26OCT07PITWSH-WSH2|no selected over player prop KXNHLPTS-26OCT07PITWSH-WSHATUCH89-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.98 vs 0.76 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +12.34 (adj +4.96) on $50.00, P(profit) 0.5052, adj growth 38.9 bp · B EV +5.87 (adj +3.08) on $29.19, P(profit) 0.5998, adj growth 26.7 bp · C EV +4.12 (adj +2.16) on $26.82, P(profit) 0.518, adj growth 18.8 bp · R EV +0.66 (adj +0.36) on $5.00, P(profit) 0.3461, adj growth 12.1 bp

## COL @ WPG  ·  10000 joint draws  ·  416 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_COL_win | p_overtime | goals | shots WPG/COL | WPG/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.42 | 0.58 | 0.00 | 6.02 | 27.7/28.4 | 24.3/24.6 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 6.01 | 22.1/34.2 | 29.8/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.46 | 5.93 | 28.0/28.7 | 25.4/24.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.48 | 5.92 | 22.6/34.5 | 31.1/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.44 | 0.56 | 0.00 | 9.28 | 29.4/30.2 | 23.5/23.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.077 | 0.36 | 0.64 | 0.00 | 9.35 | 23.8/36.0 | 28.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Morrissey: 2+ goals NO | 97 | 0.995 | 0.987 | +0.022 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 2+ points NO | 53 | 0.708 | 0.571 | +0.161 | +0.023 | $9.60 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.94) | CALIBRATION_WARNING | D |
| Nathan MacKinnon: 1+ assists NO | 38 | 0.543 | 0.417 | +0.147 | +0.021 | $3.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.75) | CALIBRATION_WARNING | D |
| Colorado wins by over 1.5 goals NO | 59 | 0.667 | 0.626 | +0.061 | +0.019 | $8.78 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Josh Morrissey: 2+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT07COLWPG-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26OCT07COLWPG-COL2|no: MOSTLY_INDEPENDENT (phi -0.024); failure: WPG offense succeeds (4+ goals)
- **Nathan MacKinnon: 2+ points NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT07COLWPG-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (4.80 vs 3.85 bp); relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT07COLWPG-COLNMACKINNON29-1|no: REINFORCING (phi 0.503); KXNHLSPREAD-26OCT07COLWPG-COL2|no: REINFORCING (phi 0.28); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no; why: second expression of the same thesis: KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no has the higher standalone adjusted growth (4.80 vs 3.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.503); they share one thesis budget; relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no: REINFORCING (phi 0.503); KXNHLSPREAD-26OCT07COLWPG-COL2|no: REINFORCING (phi 0.188); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no; why: second expression of the same thesis: KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no has the higher standalone adjusted growth (4.80 vs 3.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.280); they share one thesis budget; relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no: REINFORCING (phi 0.28); KXNHLAST-26OCT07COLWPG-COLNMACKINNON29-1|no: REINFORCING (phi 0.188); failure: COL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis COL:SUPPRESSED (p 0.3522): highest fidelity KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no less than the minimum stake; KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no kept
- thesis WPG:WINS (p 0.4464): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: FUNDED_RESEARCH; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3482, phi -0.073)
- KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.3 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4302, phi -0.4)
- KXNHLAST-26OCT07COLWPG-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.8 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4302, phi -0.285)
- KXNHLSPREAD-26OCT07COLWPG-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3325, phi -1.0)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no less than the minimum stake; KXNHLPTS-26OCT07COLWPG-COLNMACKINNON29-2|no kept
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no less than the minimum stake; KXNHLAST-26OCT07COLWPG-COLNMACKINNON29-1|no kept

portfolios: A EV +10.80 (adj +1.93) on $50.00, P(profit) 0.6316, adj growth 13.2 bp · B EV +5.57 (adj +1.20) on $42.20, P(profit) 0.6601, adj growth 10.9 bp · C EV +4.81 (adj +0.94) on $34.81, P(profit) 0.7038, adj growth 8.6 bp · R EV +0.41 (adj +0.17) on $8.00, P(profit) 0.663, adj growth 6.5 bp

## EDM @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_EDM_win | p_overtime | goals | shots ANA/EDM | ANA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.47 | 0.53 | 0.00 | 6.07 | 29.0/28.9 | 24.9/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 9.56 | 30.6/30.3 | 23.8/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.48 | 6.04 | 29.0/28.7 | 25.3/25.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.55 | 0.45 | 0.00 | 6.08 | 34.0/23.0 | 19.6/29.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.45 | 5.98 | 33.9/23.0 | 19.9/30.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 9.41 | 35.9/24.6 | 18.8/28.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
