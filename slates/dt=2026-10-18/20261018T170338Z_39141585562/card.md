# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T17:03:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 87.42 | +14.90 | +4.39 | +9.82 | 0.572 | -46.88 | -46.88 | 32.61 |
| B thesis-diversified (joint) ← optimiser card | 61.54 | +6.48 | +3.41 | +3.23 | 0.646 | -37.17 | -37.17 | 29.67 |
| C best expression per thesis | 23.86 | +6.82 | +2.21 | +2.84 | 0.748 | -23.86 | -23.86 | 19.19 |
| R FUNDED research stakes | 12.00 | +0.82 | +0.36 | +0.01 | 0.703 | -5.91 | -6.08 | 0.00 |

## CBJ @ MIN  ·  10000 joint draws  ·  450 bet sides mapped, 3 +EV candidates, 3 on card

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
| Mathieu Olivier: 1+ goals YES | 13 | 0.177 | 0.160 | +0.039 | +0.022 | $5.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ goals NO | 81 | 0.848 | 0.836 | +0.028 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Cole Sillinger: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $3.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes; why: higher confidence-adjusted growth (8.91 vs 2.38 bp); relationships: KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CBJMIN-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (3.61 vs 0.94 bp); despite a smaller raw edge (+0.028 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense succeeds (4+ goals)
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (8.91 vs 2.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3023): highest fidelity KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.3328): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT18CBJMIN-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.229)
- KXNHLGOAL-26OCT18CBJMIN-MINQHUGHES43-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4478, phi -0.155)
- KXNHLGOAL-26OCT18CBJMIN-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4857, phi -0.211)

portfolios: A EV +4.80 (adj +2.70) on $37.42, P(profit) 0.3059, adj growth 20.5 bp · B EV +2.77 (adj +1.56) on $28.80, P(profit) 0.2856, adj growth 13.6 bp · C EV +1.65 (adj +0.94) on $5.85, P(profit) 0.1768, adj growth 8.1 bp · R EV +0.17 (adj +0.09) on $5.00, P(profit) 0.8484, adj growth 3.4 bp

## CAR @ CGY  ·  10000 joint draws  ·  428 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.342 / away 0.658

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.139 | 0.40 | 0.60 | 0.00 | 6.0 | 22.0/34.8 | 30.6/19.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.45 | 0.55 | 0.49 | 5.85 | 21.9/34.6 | 31.2/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.43 | 0.57 | 0.00 | 5.97 | 27.5/28.4 | 24.5/24.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.090 | 0.36 | 0.64 | 0.00 | 9.18 | 23.3/36.5 | 28.8/18.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.50 | 0.50 | 0.46 | 5.98 | 27.7/28.6 | 25.2/24.4 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.47 | 2.84 | 20.5/33.3 | 31.8/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sebastian Aho: 1+ goals NO | 66 | 0.715 | 0.699 | +0.039 | +0.023 | $15.20 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 9 | 0.118 | 0.110 | +0.022 | +0.014 | $3.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Carolina over 3.5 goals scored NO | 49 | 0.579 | 0.529 | +0.072 | +0.022 | $9.08 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Aydar Suniev: 1+ goals YES | 18 | 0.218 | 0.206 | +0.028 | +0.016 | $4.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no has the higher standalone adjusted growth (7.12 vs 5.22 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.011); relationships: KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: REINFORCING (phi 0.223); KXNHLGOAL-26OCT18CARCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CAR offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (6.09 vs 4.94 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.093); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT18CARCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CGY offense suppressed (<= 2 goals)
- **Carolina over 3.5 goals scored NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.223); KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT18CARCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: CAR offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes; why: KXNHLSPREAD-26OCT18CARCGY-CGY2|yes has the higher standalone adjusted growth (6.09 vs 3.63 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.118); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: MOSTLY_INDEPENDENT (phi -0.017); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3691): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no — Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CGY:WINS_BY_2PLUS (p 0.2355): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.3361): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT18CARCGY-CGY2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4111, phi -0.222)
- KXNHLGOAL-26OCT18CARCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.149)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4111, phi -0.98)
- KXNHLGOAL-26OCT18CARCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.207)
- override: Broad expression KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.10 (adj +1.69) on $50.00, P(profit) 0.5736, adj growth 12.1 bp · B EV +3.72 (adj +1.85) on $32.74, P(profit) 0.5963, adj growth 16.1 bp · C EV +5.17 (adj +1.27) on $18.01, P(profit) 0.6975, adj growth 11.1 bp · R EV +0.65 (adj +0.27) on $7.00, P(profit) 0.4636, adj growth 9.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT18CARCGY-CAR|no == KXNHLGAME-26OCT18CARCGY-CGY|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
