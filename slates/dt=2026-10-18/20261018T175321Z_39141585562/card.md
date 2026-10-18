# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T17:53:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +17.40 | +4.44 | +19.79 | 0.649 | -40.27 | -58.00 | 33.40 |
| B thesis-diversified (joint) ← optimiser card | 87.39 | +8.87 | +4.59 | +5.28 | 0.638 | -32.99 | -45.94 | 40.28 |
| C best expression per thesis | 72.46 | +8.64 | +3.49 | +4.41 | 0.529 | -30.24 | -31.82 | 30.74 |
| R FUNDED research stakes | 17.00 | +1.38 | +0.61 | +2.27 | 0.702 | -5.23 | -10.91 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  450 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.627 / away 0.372

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
| Mathieu Olivier: 1+ goals YES | 13 | 0.177 | 0.163 | +0.039 | +0.025 | $6.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ goals NO | 81 | 0.848 | 0.836 | +0.028 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 54 | 0.589 | 0.574 | +0.032 | +0.017 | $9.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Cole Sillinger: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $3.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes; why: higher confidence-adjusted growth (11.01 vs 2.38 bp); relationships: KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no; why: higher confidence-adjusted growth (3.61 vs 2.70 bp); despite a smaller raw edge (+0.028 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no; why: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no has the higher standalone adjusted growth (2.70 vs 2.57 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.206); relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: MIN offense succeeds (4+ goals)
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (11.01 vs 2.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3023): highest fidelity KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.3328): highest fidelity KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:SUPPRESSED (p 0.4857): highest fidelity KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT18CBJMIN-CBJVNICHUSHKIN43-1|no (same contract)
- KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.229)
- KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.155)
- KXNHLGOAL-26OCT18CBJMIN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.294)
- KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.211)

portfolios: A EV +7.02 (adj +2.55) on $50.00, P(profit) 0.4152, adj growth 20.5 bp · B EV +3.48 (adj +2.06) on $38.75, P(profit) 0.6284, adj growth 18.0 bp · C EV +5.32 (adj +1.90) on $40.42, P(profit) 0.714, adj growth 16.5 bp · R EV +0.17 (adj +0.09) on $5.00, P(profit) 0.8484, adj growth 3.4 bp

## CAR @ CGY  ·  10000 joint draws  ·  422 bet sides mapped, 17 +EV candidates, 4 on card

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
| Sebastian Aho: 1+ goals NO | 65 | 0.719 | 0.699 | +0.053 | +0.033 | $20.00 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 9 | 0.120 | 0.112 | +0.025 | +0.016 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Calgary over 2.5 goals scored YES | 48 | 0.569 | 0.522 | +0.071 | +0.024 | $9.88 | FUNDED_RESEARCH | $3 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina over 4.5 goals scored NO | 69 | 0.772 | 0.726 | +0.068 | +0.021 | $15.22 | FUNDED_RESEARCH | $4 | CGY:WINS | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: higher confidence-adjusted growth (11.04 vs 6.74 bp); despite a smaller raw edge (+0.053 vs +0.140/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no: REINFORCING (phi 0.197); failure: CAR offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes; why: higher confidence-adjusted growth (6.21 vs 5.20 bp); despite a smaller raw edge (+0.025 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: REINFORCING (phi 0.182); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CGY offense suppressed (<= 2 goals)
- **Calgary over 2.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY3|yes; why: higher confidence-adjusted growth (5.20 vs 3.36 bp); wins across more scripts (relative breadth 0.879 vs 0.483); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: REINFORCING (phi 0.182); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CGY offense suppressed (<= 2 goals)
- **Carolina over 4.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.197); KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3809): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no — Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CGY:OFFENSE_4PLUS (p 0.3323): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes (same contract)
- thesis CGY:WINS (p 0.454): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.229)
- KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4421, phi -0.186)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.4421, phi -0.978)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.65)
- override: Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.38 (adj +1.89) on $50.00, P(profit) 0.5976, adj growth 12.9 bp · B EV +5.38 (adj +2.53) on $48.64, P(profit) 0.6997, adj growth 22.3 bp · C EV +3.32 (adj +1.59) on $32.04, P(profit) 0.4113, adj growth 14.3 bp · R EV +1.21 (adj +0.52) on $12.00, P(profit) 0.6637, adj growth 18.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT18CARCGY-CAR|no == KXNHLGAME-26OCT18CARCGY-CGY|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
