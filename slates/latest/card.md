# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T22:47:24Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +16.25 | +2.82 | +30.74 | 0.656 | -25.85 | -50.00 | 22.02 |
| B thesis-diversified (joint) ← optimiser card | 44.92 | +6.68 | +3.29 | -3.38 | 0.497 | -23.04 | -25.26 | 30.03 |
| C best expression per thesis | 46.88 | +11.36 | +6.24 | +2.04 | 0.647 | -27.13 | -46.88 | 54.41 |
| R FUNDED research stakes | 4.00 | +0.38 | +0.26 | +1.84 | 0.751 | -4.00 | -4.00 | 0.00 |

## CAR @ PHI  ·  10000 joint draws  ·  482 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.347 / away 0.653

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.147 | 0.41 | 0.59 | 0.00 | 5.94 | 20.4/32.6 | 28.6/17.4 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.135 | 0.49 | 0.51 | 0.46 | 5.87 | 20.4/32.9 | 29.4/17.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.092 | 0.52 | 0.48 | 0.00 | 5.94 | 25.9/26.7 | 23.5/22.3 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.085 | 0.42 | 0.58 | 0.00 | 3.4 | 19.1/31.3 | 29.3/17.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.52 | 0.48 | 0.48 | 5.87 | 25.9/26.7 | 23.5/22.6 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.083 | 0.47 | 0.53 | 0.48 | 2.74 | 19.2/31.0 | 29.5/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sebastian Aho: 1+ goals NO | 67 | 0.751 | 0.729 | +0.065 | +0.044 | $15.00 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 13 | 0.185 | 0.169 | +0.047 | +0.031 | $6.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 75 | 0.807 | 0.791 | +0.043 | +0.028 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Joseph Woll: 29+ saves NO | 50 | 0.649 | 0.534 | +0.132 | +0.016 | $8.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | PHI:NET_LOW_VOLUME | STRUCTURAL (1.00) | CALIBRATION_WARNING | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no; why: higher confidence-adjusted growth (19.64 vs 11.78 bp); despite a smaller raw edge (+0.065 vs +0.146/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSAVE-26OCT11CARPHI-PHIJWOLL53-29|no: MOSTLY_INDEPENDENT (phi -0.029); failure: CAR offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes; why: Player prop expression KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes selected over broad KXNHLSPREAD-26OCT11CARPHI-CAR3|no because adjusted EV is 1.2 pts higher while thesis capture is 0.27 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26OCT11CARPHI-PHIJWOLL53-29|no: MOSTLY_INDEPENDENT (phi -0.019); failure: PHI offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26OCT11CARPHI-PHIJWOLL53-29|no: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)
- **Joseph Woll: 29+ saves NO** — thesis: PHI net faces light volume (<= 25 shots; CAR suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: PHI net faces heavy volume (33+ shots; CAR pressure)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.3236): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4207): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:WINS_BY_2PLUS (p 0.2512): highest fidelity KXNHLSPREAD-26OCT11CARPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.216)
- KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4572, phi -0.238)
- KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.208)
- KXNHLSAVE-26OCT11CARPHI-PHIJWOLL53-29|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis PHI:NET_HIGH_VOLUME (p 0.3091, phi -0.79)
- override: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes selected over broad KXNHLSPREAD-26OCT11CARPHI-CAR3|no because adjusted EV is 1.2 pts higher while thesis capture is 0.27 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +16.25 (adj +2.82) on $50.00, P(profit) 0.656, adj growth 22.0 bp · B EV +6.68 (adj +3.29) on $44.92, P(profit) 0.4971, adj growth 30.0 bp · C EV +11.36 (adj +6.24) on $46.88, P(profit) 0.6468, adj growth 54.4 bp · R EV +0.38 (adj +0.26) on $4.00, P(profit) 0.7507, adj growth 9.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11CARPHI-PHI|yes == KXNHLGAME-26OCT11CARPHI-CAR|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
