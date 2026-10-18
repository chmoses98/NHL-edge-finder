# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T20:22:32Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +17.18 | +3.14 | +19.78 | 0.694 | -32.39 | -49.41 | 24.66 |
| B thesis-diversified (joint) ← optimiser card | 94.18 | +10.06 | +4.86 | +11.93 | 0.592 | -29.40 | -39.44 | 43.77 |
| C best expression per thesis | 66.24 | +8.29 | +4.34 | +13.77 | 0.568 | -39.00 | -39.00 | 38.52 |
| R FUNDED research stakes | 13.00 | +1.26 | +0.57 | +1.32 | 0.640 | -5.69 | -7.55 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  450 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.630 / away 0.370

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_CBJ_win | p_overtime | goals | shots MIN/CBJ | MIN/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 5.98 | 28.6/28.5 | 25.8/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.55 | 0.45 | 0.45 | 5.92 | 28.7/28.8 | 25.6/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.67 | 0.33 | 0.00 | 9.25 | 30.3/30.2 | 25.0/22.9 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.070 | 0.62 | 0.38 | 0.00 | 6.01 | 22.7/33.2 | 30.2/18.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.069 | 0.68 | 0.32 | 0.00 | 6.04 | 33.2/22.6 | 19.9/28.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.66 | 0.34 | 0.00 | 3.51 | 27.3/27.5 | 26.0/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 13 | 0.177 | 0.164 | +0.039 | +0.026 | $6.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 72 | 0.810 | 0.763 | +0.076 | +0.029 | $19.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Kirill Kaprizov: 1+ goals NO | 53 | 0.589 | 0.573 | +0.042 | +0.026 | $12.22 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 2+ assists NO | 72 | 0.799 | 0.750 | +0.065 | +0.015 | $11.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (12.15 vs 0.63 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no: MOSTLY_INDEPENDENT (phi 0.02); failure: CBJ offense suppressed (<= 2 goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT18CBJMIN-4|no; why: higher confidence-adjusted growth (9.27 vs 0.14 bp); wins across more scripts (relative breadth 0.991 vs 0.361); alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no; why: higher confidence-adjusted growth (5.84 vs 2.70 bp); despite a smaller raw edge (+0.042 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no: REINFORCING (phi 0.206); failure: MIN offense succeeds (4+ goals)
- **Quinn Hughes: 2+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (5.84 vs 2.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.206); they share one thesis budget; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.206); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3023): highest fidelity KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.4857): highest fidelity KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no (same contract)
- thesis MIN:SUPPRESSED (p 0.3328): highest fidelity KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.229)
- KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3023, phi -0.207)
- KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.294)
- KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.324)

portfolios: A EV +6.29 (adj +1.48) on $50.00, P(profit) 0.6745, adj growth 12.0 bp · B EV +5.89 (adj +2.85) on $50.00, P(profit) 0.5111, adj growth 25.3 bp · C EV +5.11 (adj +2.75) on $40.94, P(profit) 0.5666, adj growth 24.3 bp · R EV +0.31 (adj +0.19) on $4.00, P(profit) 0.5892, adj growth 6.5 bp

## CAR @ CGY  ·  10000 joint draws  ·  466 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.343 / away 0.657

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.140 | 0.39 | 0.61 | 0.00 | 5.96 | 21.9/34.6 | 30.2/19.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.47 | 0.53 | 0.48 | 5.84 | 21.9/34.4 | 31.1/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.47 | 0.53 | 0.00 | 6.05 | 27.6/28.6 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.49 | 0.51 | 0.46 | 5.92 | 27.6/28.6 | 25.1/24.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.088 | 0.36 | 0.64 | 0.00 | 9.21 | 23.3/36.0 | 28.5/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.44 | 0.56 | 0.00 | 9.19 | 29.1/30.2 | 23.6/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nikolaj Ehlers: 1+ goals NO | 72 | 0.785 | 0.768 | +0.051 | +0.034 | $15.00 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 65 | 0.719 | 0.700 | +0.053 | +0.034 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Calgary over 2.5 goals scored YES | 48 | 0.569 | 0.522 | +0.071 | +0.024 | $8.88 | FUNDED_RESEARCH | $3 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 69 | 0.792 | 0.723 | +0.087 | +0.018 | $5.30 | FUNDED_RESEARCH | $2 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV is 0.7 pts higher while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.165); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no has the higher standalone adjusted growth (12.73 vs 11.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.164); failure: CAR offense succeeds (4+ goals)
- **Calgary over 2.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (7.67 vs 5.20 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.449); relationships: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.402); failure: CGY offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: Broad expression KXNHLSPREAD-26OCT18CARCGY-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: REINFORCING (phi 0.165); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.164); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: REINFORCING (phi 0.402); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3809): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV is 0.7 pts higher while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CGY:WINS_BY_2PLUS (p 0.2405): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.3323): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes (same contract)
- KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.22)
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.233)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.4421, phi -0.978)
- KXNHLSPREAD-26OCT18CARCGY-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.7 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3216, phi -0.744)
- override: Player prop expression KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV is 0.7 pts higher while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLSPREAD-26OCT18CARCGY-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.89 (adj +1.66) on $50.00, P(profit) 0.685, adj growth 12.7 bp · B EV +4.17 (adj +2.01) on $44.18, P(profit) 0.6842, adj growth 18.5 bp · C EV +3.18 (adj +1.59) on $25.30, P(profit) 0.8113, adj growth 14.2 bp · R EV +0.96 (adj +0.38) on $9.00, P(profit) 0.4544, adj growth 13.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT18CARCGY-CAR|no == KXNHLGAME-26OCT18CARCGY-CGY|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
