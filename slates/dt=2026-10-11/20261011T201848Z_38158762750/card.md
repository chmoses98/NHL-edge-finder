# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T20:18:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +33.07 | +6.13 | +35.74 | 0.690 | -50.39 | -74.41 | 40.81 |
| B thesis-diversified (joint) ← optimiser card | 124.95 | +16.53 | +10.43 | +13.93 | 0.605 | -43.54 | -54.86 | 92.27 |
| C best expression per thesis | 117.16 | +19.07 | +10.33 | +14.02 | 0.606 | -36.22 | -61.33 | 91.26 |
| R FUNDED research stakes | 15.00 | +1.70 | +1.02 | -1.06 | 0.494 | -9.16 | -9.40 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  500 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.656 / away 0.344

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_SEA_win | p_overtime | goals | shots WSH/SEA | WSH/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 6.04 | 27.6/27.2 | 24.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.48 | 5.95 | 27.8/27.5 | 24.2/24.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.099 | 0.67 | 0.33 | 0.00 | 6.03 | 32.6/21.6 | 18.9/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.64 | 0.36 | 0.00 | 9.27 | 29.0/28.7 | 23.4/21.9 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.53 | 0.47 | 0.44 | 5.86 | 33.1/21.9 | 18.8/29.7 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.062 | 0.68 | 0.32 | 0.00 | 9.3 | 34.1/23.1 | 18.3/26.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Shane Wright: 1+ goals YES | 14 | 0.189 | 0.176 | +0.041 | +0.027 | $6.97 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 9 | 0.128 | 0.117 | +0.032 | +0.021 | $5.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 19 | 0.245 | 0.229 | +0.044 | +0.028 | $9.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Washington wins by over 2.5 goals NO | 70 | 0.767 | 0.731 | +0.053 | +0.017 | $15.62 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (12.60 vs 4.53 bp); relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: MOSTLY_INDEPENDENT (phi 0.122); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (12.60 vs 11.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: MOSTLY_INDEPENDENT (phi 0.089); failure: SEA offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (10.37 vs 2.52 bp); despite a smaller raw edge (+0.044 vs +0.085/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: INTENTIONAL_DIVERSIFIER (phi -0.183); failure: WSH offense suppressed (<= 2 goals)
- **Washington wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: Broad expression KXNHLSPREAD-26OCT11SEAWSH-WSH3|no selected over player prop KXNHLAST-26OCT11SEAWSH-WSHJKYROU25-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.089); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.183); failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3227): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4424): highest fidelity KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3518): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH3|no (same contract)
- KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4627, phi -0.232)
- KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4627, phi -0.171)
- KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3518, phi -0.233)
- KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.3553, phi -0.741)
- override: Broad expression KXNHLSPREAD-26OCT11SEAWSH-WSH3|no selected over player prop KXNHLAST-26OCT11SEAWSH-WSHJKYROU25-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.18 (adj +1.53) on $50.00, P(profit) 0.7114, adj growth 12.0 bp · B EV +6.75 (adj +4.02) on $36.75, P(profit) 0.4668, adj growth 34.7 bp · C EV +5.29 (adj +2.99) on $34.27, P(profit) 0.3912, adj growth 25.9 bp · R EV +0.84 (adj +0.46) on $6.00, P(profit) 0.1892, adj growth 15.5 bp

## VAN @ NYR  ·  10000 joint draws  ·  400 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.700 / away 0.300

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
| Drew O'Connor: 1+ goals YES | 13 | 0.182 | 0.168 | +0.044 | +0.030 | $7.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 60 | 0.675 | 0.654 | +0.058 | +0.037 | $20.00 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 19 | 0.239 | 0.226 | +0.038 | +0.025 | $7.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.213 | 0.201 | +0.033 | +0.021 | $5.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (16.03 vs 8.40 bp); relationships: KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11VANNYR-NYR3|no; why: higher confidence-adjusted growth (12.64 vs 7.84 bp); despite a smaller raw edge (+0.058 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (16.03 vs 8.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (16.03 vs 6.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYR shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3044): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3223): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4245): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR3|no (same contract)
- KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4857, phi -0.22)
- KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.462, phi -0.223)
- KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4857, phi -0.235)
- KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4857, phi -0.243)

portfolios: A EV +8.76 (adj +2.01) on $50.00, P(profit) 0.5318, adj growth 12.8 bp · B EV +7.00 (adj +4.57) on $41.53, P(profit) 0.4174, adj growth 40.0 bp · C EV +7.57 (adj +3.83) on $50.00, P(profit) 0.7178, adj growth 34.2 bp · R EV +0.47 (adj +0.30) on $5.00, P(profit) 0.6749, adj growth 10.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11VANNYR-VAN|yes == KXNHLGAME-26OCT11VANNYR-NYR|no

## CAR @ PHI  ·  10000 joint draws  ·  482 bet sides mapped, 28 +EV candidates, 3 on card

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
| David Jiricek: 1+ goals NO | 92 | 0.953 | 0.944 | +0.028 | +0.018 | $16.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 75 | 0.807 | 0.791 | +0.043 | +0.028 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11CARPHI-PHI2|yes; why: higher confidence-adjusted growth (19.64 vs 11.64 bp); despite a smaller raw edge (+0.065 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.998 vs 0.559); relationships: KXNHLGOAL-26OCT11CARPHI-PHIDJIRICEK55-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: CAR offense succeeds (4+ goals)
- **David Jiricek: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT11CARPHI-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (10.93 vs 0.15 bp); alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense succeeds (4+ goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT11CARPHI-PHIDJIRICEK55-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis CAR:SUPPRESSED (p 0.4207): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:OFFENSE_4PLUS (p 0.3236): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2512): highest fidelity KXNHLSPREAD-26OCT11CARPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-PHI2|yes (same contract)
- KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.216)
- KXNHLGOAL-26OCT11CARPHI-PHIDJIRICEK55-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3236, phi -0.102)
- KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.208)
- override: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +16.14 (adj +2.59) on $50.00, P(profit) 0.5963, adj growth 16.0 bp · B EV +2.78 (adj +1.84) on $46.67, P(profit) 0.5763, adj growth 17.6 bp · C EV +6.21 (adj +3.51) on $32.89, P(profit) 0.3555, adj growth 31.1 bp · R EV +0.38 (adj +0.26) on $4.00, P(profit) 0.7507, adj growth 9.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11CARPHI-PHI|yes == KXNHLGAME-26OCT11CARPHI-CAR|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
