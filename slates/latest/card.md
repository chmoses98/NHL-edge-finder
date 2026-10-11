# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T21:58:07Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +24.78 | +4.69 | +19.90 | 0.660 | -57.53 | -81.23 | 27.49 |
| B thesis-diversified (joint) ← optimiser card | 89.92 | +11.06 | +7.36 | +1.56 | 0.648 | -30.36 | -50.02 | 65.30 |
| C best expression per thesis | 78.48 | +12.92 | +7.68 | +5.76 | 0.622 | -28.54 | -49.31 | 67.75 |
| R FUNDED research stakes | 9.00 | +0.77 | +0.51 | +4.81 | 0.505 | -3.16 | -9.00 | 0.00 |

## VAN @ NYR  ·  10000 joint draws  ·  402 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.703 / away 0.297

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_VAN_win | p_overtime | goals | shots NYR/VAN | NYR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.66 | 0.34 | 0.00 | 5.97 | 26.7/26.4 | 23.6/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.45 | 5.92 | 26.6/26.4 | 23.1/23.4 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.095 | 0.73 | 0.27 | 0.00 | 6.02 | 31.4/20.7 | 18.3/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.66 | 0.34 | 0.00 | 9.31 | 28.2/28.1 | 22.9/21.2 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.59 | 0.41 | 0.51 | 5.87 | 31.8/21.2 | 18.2/28.3 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.061 | 0.73 | 0.27 | 0.00 | 9.22 | 33.0/21.9 | 17.5/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 12 | 0.182 | 0.165 | +0.055 | +0.038 | $9.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 61 | 0.675 | 0.657 | +0.048 | +0.031 | $20.00 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 19 | 0.239 | 0.226 | +0.038 | +0.025 | $7.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.213 | 0.201 | +0.033 | +0.021 | $5.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (27.39 vs 8.40 bp); relationships: KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11VANNYR-NYR3|no; why: higher confidence-adjusted growth (8.89 vs 7.84 bp); despite a smaller raw edge (+0.048 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (27.39 vs 8.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (27.39 vs 6.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYR shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3044): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3223): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4245): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR3|no (same contract)
- KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4857, phi -0.22)
- KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.462, phi -0.223)
- KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4857, phi -0.235)
- KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4857, phi -0.243)

portfolios: A EV +8.64 (adj +1.91) on $50.00, P(profit) 0.4915, adj growth 9.5 bp · B EV +8.27 (adj +5.52) on $43.25, P(profit) 0.4174, adj growth 47.7 bp · C EV +8.11 (adj +4.42) on $50.00, P(profit) 0.6636, adj growth 38.8 bp · R EV +0.38 (adj +0.25) on $5.00, P(profit) 0.6749, adj growth 8.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11VANNYR-VAN|yes == KXNHLGAME-26OCT11VANNYR-NYR|no

## CAR @ PHI  ·  10000 joint draws  ·  482 bet sides mapped, 28 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.343 / away 0.657

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
| David Jiricek: 1+ goals NO | 92 | 0.953 | 0.944 | +0.028 | +0.018 | $16.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 75 | 0.807 | 0.791 | +0.043 | +0.028 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no; why: higher confidence-adjusted growth (19.64 vs 11.78 bp); despite a smaller raw edge (+0.065 vs +0.146/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11CARPHI-PHIDJIRICEK55-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: CAR offense succeeds (4+ goals)
- **David Jiricek: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT11CARPHI-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (10.93 vs 0.15 bp); alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense succeeds (4+ goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT11CARPHI-PHIDJIRICEK55-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis CAR:SUPPRESSED (p 0.4207): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:OFFENSE_4PLUS (p 0.3236): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2512): highest fidelity KXNHLSPREAD-26OCT11CARPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.216)
- KXNHLGOAL-26OCT11CARPHI-PHIDJIRICEK55-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3236, phi -0.102)
- KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.208)
- override: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +16.14 (adj +2.78) on $50.00, P(profit) 0.5963, adj growth 17.9 bp · B EV +2.78 (adj +1.84) on $46.67, P(profit) 0.5763, adj growth 17.6 bp · C EV +4.81 (adj +3.26) on $28.48, P(profit) 0.7936, adj growth 28.9 bp · R EV +0.38 (adj +0.26) on $4.00, P(profit) 0.7507, adj growth 9.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11CARPHI-PHI|yes == KXNHLGAME-26OCT11CARPHI-CAR|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
