# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T18:43:22Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +18.26 | +4.24 | +16.15 | 0.626 | -43.41 | -46.76 | 32.59 |
| B thesis-diversified (joint) ← optimiser card | 82.59 | +7.34 | +3.77 | +8.30 | 0.636 | -30.51 | -38.06 | 33.66 |
| C best expression per thesis | 86.63 | +11.26 | +3.88 | +8.90 | 0.655 | -23.95 | -38.13 | 34.48 |
| R FUNDED research stakes | 14.00 | +1.17 | +0.49 | +0.94 | 0.699 | -5.16 | -7.91 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  450 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.625 / away 0.375

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
| Mathieu Olivier: 1+ goals YES | 13 | 0.177 | 0.161 | +0.039 | +0.023 | $6.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ goals NO | 81 | 0.848 | 0.836 | +0.028 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 54 | 0.589 | 0.574 | +0.032 | +0.017 | $9.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Cole Sillinger: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $3.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes; why: higher confidence-adjusted growth (9.94 vs 2.38 bp); relationships: KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (3.61 vs 2.76 bp); despite a smaller raw edge (+0.028 vs +0.086/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no; why: Player prop expression KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.80 vs 0.67 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: MIN offense succeeds (4+ goals)
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (9.94 vs 2.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3023): highest fidelity KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.3328): highest fidelity KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no (same contract)
- thesis CBJ:SUPPRESSED (p 0.4857): highest fidelity KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no (same contract)
- KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.229)
- KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.155)
- KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.294)
- KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.211)
- override: Player prop expression KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.80 vs 0.67 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +8.05 (adj +2.51) on $50.00, P(profit) 0.5194, adj growth 20.1 bp · B EV +3.38 (adj +1.94) on $38.40, P(profit) 0.6408, adj growth 16.9 bp · C EV +4.92 (adj +1.77) on $44.95, P(profit) 0.4534, adj growth 15.5 bp · R EV +0.17 (adj +0.09) on $5.00, P(profit) 0.8484, adj growth 3.4 bp

## CAR @ CGY  ·  10000 joint draws  ·  454 bet sides mapped, 21 +EV candidates, 4 on card

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
| Sebastian Aho: 1+ goals NO | 65 | 0.719 | 0.700 | +0.053 | +0.034 | $15.00 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.785 | 0.769 | +0.041 | +0.025 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Calgary over 2.5 goals scored YES | 48 | 0.569 | 0.522 | +0.071 | +0.024 | $8.87 | FUNDED_RESEARCH | $3 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 69 | 0.792 | 0.723 | +0.087 | +0.018 | $5.32 | FUNDED_RESEARCH | $2 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no; why: higher confidence-adjusted growth (11.13 vs 7.29 bp); relationships: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.164); failure: CAR offense succeeds (4+ goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.165); failure: CAR offense succeeds (4+ goals)
- **Calgary over 2.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY3|yes; why: higher confidence-adjusted growth (5.20 vs 3.36 bp); wins across more scripts (relative breadth 0.879 vs 0.483); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.039); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.402); failure: CGY offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: Broad expression KXNHLSPREAD-26OCT18CARCGY-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.164); KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: REINFORCING (phi 0.165); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: REINFORCING (phi 0.402); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3809): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CGY:WINS (p 0.454): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no — Broad expression KXNHLSPREAD-26OCT18CARCGY-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CGY:OFFENSE_4PLUS (p 0.3323): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes (same contract)
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.233)
- KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.22)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.4421, phi -0.978)
- KXNHLSPREAD-26OCT18CARCGY-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.7 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3216, phi -0.744)
- override: Player prop expression KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLSPREAD-26OCT18CARCGY-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.21 (adj +1.73) on $50.00, P(profit) 0.5752, adj growth 12.5 bp · B EV +3.96 (adj +1.83) on $44.19, P(profit) 0.6842, adj growth 16.7 bp · C EV +6.34 (adj +2.11) on $41.68, P(profit) 0.7072, adj growth 19.0 bp · R EV +1.00 (adj +0.40) on $9.00, P(profit) 0.4142, adj growth 14.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT18CARCGY-CAR|no == KXNHLGAME-26OCT18CARCGY-CGY|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
