# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T17:46:34Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +32.18 | +5.55 | +37.18 | 0.687 | -54.14 | -75.73 | 35.29 |
| B thesis-diversified (joint) ← optimiser card | 124.02 | +17.17 | +10.10 | +12.71 | 0.588 | -44.85 | -55.88 | 88.83 |
| C best expression per thesis | 118.72 | +17.90 | +10.17 | +15.75 | 0.584 | -41.00 | -61.97 | 89.24 |
| R FUNDED research stakes | 20.00 | +2.25 | +1.21 | +1.11 | 0.577 | -7.25 | -11.89 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  498 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_SEA_win | p_overtime | goals | shots WSH/SEA | WSH/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.58 | 0.42 | 0.00 | 6.0 | 27.8/27.4 | 24.3/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.49 | 5.93 | 27.5/27.2 | 24.0/24.3 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.097 | 0.66 | 0.34 | 0.00 | 6.0 | 32.7/21.5 | 18.8/28.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.61 | 0.39 | 0.00 | 9.19 | 29.3/28.7 | 23.5/22.4 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.55 | 0.45 | 0.46 | 5.95 | 32.6/21.9 | 18.8/28.8 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.059 | 0.66 | 0.34 | 0.00 | 9.4 | 34.4/23.2 | 18.2/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Shane Wright: 1+ goals YES | 14 | 0.192 | 0.177 | +0.043 | +0.029 | $7.39 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.247 | 0.234 | +0.036 | +0.023 | $8.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.136 | 0.123 | +0.029 | +0.017 | $3.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Washington wins by over 2.5 goals NO | 70 | 0.774 | 0.735 | +0.059 | +0.020 | $19.36 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH3|no; why: higher confidence-adjusted growth (14.38 vs 4.25 bp); despite a smaller raw edge (+0.043 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: MOSTLY_INDEPENDENT (phi 0.11); failure: SEA offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (6.99 vs 1.79 bp); despite a smaller raw edge (+0.036 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: INTENTIONAL_DIVERSIFIER (phi -0.206); failure: WSH offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (14.38 vs 6.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: MOSTLY_INDEPENDENT (phi 0.096); failure: SEA offense suppressed (<= 2 goals)
- **Washington wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: Broad expression KXNHLSPREAD-26OCT11SEAWSH-WSH3|no selected over player prop KXNHLAST-26OCT11SEAWSH-WSHJKYROU25-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.93 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.206); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.096); failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3404): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4352): highest fidelity KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4379): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.233)
- KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3473, phi -0.24)
- KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.178)
- KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.3407, phi -0.751)
- override: Broad expression KXNHLSPREAD-26OCT11SEAWSH-WSH3|no selected over player prop KXNHLAST-26OCT11SEAWSH-WSHJKYROU25-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.93 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.24 (adj +1.29) on $50.00, P(profit) 0.7044, adj growth 9.7 bp · B EV +6.25 (adj +3.50) on $38.87, P(profit) 0.4673, adj growth 30.3 bp · C EV +5.26 (adj +2.93) on $35.74, P(profit) 0.3935, adj growth 25.4 bp · R EV +1.00 (adj +0.53) on $7.00, P(profit) 0.1917, adj growth 18.1 bp

## VAN @ NYR  ·  10000 joint draws  ·  394 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.696 / away 0.304

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
| Drew O'Connor: 1+ goals YES | 13 | 0.182 | 0.168 | +0.044 | +0.030 | $7.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 60 | 0.675 | 0.654 | +0.058 | +0.037 | $20.00 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 19 | 0.239 | 0.226 | +0.038 | +0.025 | $7.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| New York R wins by over 2.5 goals NO | 65 | 0.743 | 0.694 | +0.077 | +0.028 | $14.25 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (16.03 vs 8.40 bp); relationships: KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT11VANNYR-NYR3|no: MOSTLY_INDEPENDENT (phi 0.115); failure: VAN offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11VANNYR-NYR3|no; why: higher confidence-adjusted growth (12.64 vs 7.84 bp); despite a smaller raw edge (+0.058 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLSPREAD-26OCT11VANNYR-NYR3|no: MOSTLY_INDEPENDENT (phi 0.119); failure: NYR offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (16.03 vs 8.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLSPREAD-26OCT11VANNYR-NYR3|no: MOSTLY_INDEPENDENT (phi 0.12); failure: VAN offense suppressed (<= 2 goals)
- **New York R wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-NYR4|no; why: Broad expression KXNHLSPREAD-26OCT11VANNYR-NYR3|no selected over player prop KXNHLAST-26OCT11VANNYR-NYRJMILLER8-1|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.12); failure: NYR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYR shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3044): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3223): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no — Broad expression KXNHLSPREAD-26OCT11VANNYR-NYR3|no selected over player prop KXNHLAST-26OCT11VANNYR-NYRJMILLER8-1|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4245): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR3|no (same contract)
- KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4857, phi -0.22)
- KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.462, phi -0.223)
- KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4857, phi -0.235)
- KXNHLSPREAD-26OCT11VANNYR-NYR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.3804, phi -0.75)
- override: Broad expression KXNHLSPREAD-26OCT11VANNYR-NYR3|no selected over player prop KXNHLAST-26OCT11VANNYR-NYRJMILLER8-1|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.76 (adj +2.01) on $50.00, P(profit) 0.5318, adj growth 12.8 bp · B EV +7.34 (adj +4.33) on $48.96, P(profit) 0.6695, adj growth 37.9 bp · C EV +7.19 (adj +3.66) on $50.00, P(profit) 0.6636, adj growth 32.4 bp · R EV +0.94 (adj +0.47) on $9.00, P(profit) 0.5259, adj growth 16.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11VANNYR-VAN|yes == KXNHLGAME-26OCT11VANNYR-NYR|no

## CAR @ PHI  ·  10000 joint draws  ·  476 bet sides mapped, 25 +EV candidates, 3 on card

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
| Sebastian Aho: 1+ goals NO | 68 | 0.751 | 0.732 | +0.056 | +0.036 | $15.00 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.185 | 0.171 | +0.037 | +0.023 | $6.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 75 | 0.807 | 0.790 | +0.043 | +0.027 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no; why: higher confidence-adjusted growth (13.90 vs 8.79 bp); relationships: KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: CAR offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes; why: Player prop expression KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes selected over broad KXNHLSPREAD-26OCT11CARPHI-CAR3|no because adjusted EV is 0.4 pts higher while thesis capture is 0.27 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV is 0.4 pts higher while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.3236): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4207): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV is 0.4 pts higher while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:WINS_BY_2PLUS (p 0.2512): highest fidelity KXNHLGAME-26OCT11CARPHI-PHI|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.216)
- KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4572, phi -0.238)
- KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.208)
- override: Player prop expression KXNHLGOAL-26OCT11CARPHI-PHISCOUTURIER14-1|yes selected over broad KXNHLSPREAD-26OCT11CARPHI-CAR3|no because adjusted EV is 0.4 pts higher while thesis capture is 0.27 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT11CARPHI-CARSAHO20-1|no because adjusted EV is 0.4 pts higher while thesis capture is 0.90 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +15.18 (adj +2.25) on $50.00, P(profit) 0.5963, adj growth 12.9 bp · B EV +3.58 (adj +2.27) on $36.19, P(profit) 0.6733, adj growth 20.7 bp · C EV +5.46 (adj +3.58) on $32.98, P(profit) 0.3115, adj growth 31.5 bp · R EV +0.32 (adj +0.21) on $4.00, P(profit) 0.7507, adj growth 7.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11CARPHI-PHI|yes == KXNHLGAME-26OCT11CARPHI-CAR|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
