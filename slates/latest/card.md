# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T22:18:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 78.42 | +11.73 | +3.91 | +13.77 | 0.570 | -39.79 | -46.89 | 30.52 |
| B thesis-diversified (joint) ← optimiser card | 62.24 | +7.00 | +3.38 | +2.34 | 0.634 | -24.80 | -35.67 | 30.37 |
| C best expression per thesis | 48.98 | +5.63 | +2.51 | +11.48 | 0.581 | -28.41 | -31.43 | 22.77 |
| R FUNDED research stakes | 10.00 | +1.10 | +0.62 | +2.42 | 0.647 | -5.68 | -10.00 | 0.00 |

## WPG @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.658 / away 0.342

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_WPG_win | p_overtime | goals | shots FLA/WPG | FLA/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.65 | 0.35 | 0.00 | 6.01 | 26.9/26.7 | 23.8/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.49 | 5.94 | 26.9/26.7 | 23.5/23.5 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.103 | 0.68 | 0.32 | 0.00 | 6.01 | 31.9/21.1 | 18.5/27.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.61 | 0.39 | 0.00 | 9.3 | 28.8/28.3 | 22.9/21.8 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.57 | 0.43 | 0.47 | 5.94 | 32.4/21.5 | 18.2/29.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.57 | 0.43 | 0.00 | 3.46 | 25.5/25.3 | 23.6/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 60 | 0.679 | 0.658 | +0.063 | +0.042 | $16.39 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 64 | 0.698 | 0.682 | +0.042 | +0.026 | $13.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 68 | 0.758 | 0.716 | +0.063 | +0.021 | $11.61 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Akira Schmid: 23+ saves YES | 38 | 0.484 | 0.413 | +0.087 | +0.017 | $6.31 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | FLA:NET_HIGH_VOLUME | DIRECT (0.95) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (16.02 vs 6.64 bp); relationships: KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.152); KXNHLSAVE-26OCT30WPGFLA-FLAASCHMID40-23|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: REINFORCING (phi 0.188); KXNHLSAVE-26OCT30WPGFLA-FLAASCHMID40-23|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no; why: KXNHLSPREAD-26OCT30WPGFLA-FLA2|no has the higher standalone adjusted growth (4.79 vs 4.65 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.747); relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: REINFORCING (phi 0.188); KXNHLSAVE-26OCT30WPGFLA-FLAASCHMID40-23|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: FLA wins by 2+
- **Akira Schmid: 23+ saves YES** — thesis: FLA net faces heavy volume (33+ shots; WPG pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: FLA net faces light volume (<= 25 shots; WPG suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3408): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no — Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.411): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3124): highest fidelity KXNHLSPREAD-26OCT30WPGFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT30WPGFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT30WPGFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.229)
- KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4462, phi -0.251)
- KXNHLSPREAD-26OCT30WPGFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.364, phi -0.747)
- KXNHLSAVE-26OCT30WPGFLA-FLAASCHMID40-23|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 5% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.9 pts; fragile player expression; opposing: failure thesis FLA:NET_LOW_VOLUME (p 0.5197, phi -0.774)
- override: Player prop expression KXNHLGOAL-26OCT30WPGFLA-FLASREINHART13-1|no selected over player prop KXNHLAST-26OCT30WPGFLA-FLASREINHART13-1|no because adjusted EV is 0.3 pts higher while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.68 (adj +1.71) on $50.00, P(profit) 0.6453, adj growth 14.2 bp · B EV +4.97 (adj +2.26) on $47.92, P(profit) 0.5817, adj growth 20.7 bp · C EV +5.18 (adj +2.31) on $46.12, P(profit) 0.5793, adj growth 21.0 bp · R EV +0.78 (adj +0.43) on $8.00, P(profit) 0.6794, adj growth 15.5 bp

## SEA @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.44 | 0.56 | 0.00 | 6.05 | 28.9/28.7 | 24.7/25.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.48 | 0.52 | 0.46 | 5.97 | 28.7/28.5 | 25.3/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.46 | 0.54 | 0.00 | 9.35 | 30.1/30.0 | 23.6/24.1 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.086 | 0.51 | 0.49 | 0.00 | 5.98 | 33.9/22.7 | 19.3/30.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.50 | 0.50 | 0.49 | 5.89 | 34.0/23.0 | 19.7/30.8 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.056 | 0.53 | 0.47 | 0.00 | 9.27 | 35.4/23.8 | 18.2/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Berkly Catton: 1+ goals YES | 18 | 0.221 | 0.208 | +0.031 | +0.018 | $5.17 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 13 | 0.157 | 0.149 | +0.019 | +0.011 | $2.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 19 | 0.222 | 0.213 | +0.021 | +0.012 | $3.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 14 | 0.172 | 0.159 | +0.023 | +0.010 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (4.52 vs 1.87 bp); relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (2.18 vs 1.87 bp); despite a smaller raw edge (+0.019 vs +0.023/contract); relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: SEA offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLAST-26OCT30SEACGY-CGYYSHARANGOVICH17-1|yes; why: higher confidence-adjusted growth (1.92 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CGY offense suppressed (<= 2 goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA wins by 2+; alternative: KXNHLPTS-26OCT30SEACGY-CGYJFARABEE86-1|no; why: higher confidence-adjusted growth (1.87 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4144): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3033): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3744): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.204)
- KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.183)
- KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.407, phi -0.194)
- KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.202)

portfolios: A EV +4.05 (adj +2.20) on $28.42, P(profit) 0.5717, adj growth 16.3 bp · B EV +2.03 (adj +1.12) on $14.32, P(profit) 0.5717, adj growth 9.7 bp · C EV +0.45 (adj +0.20) on $2.86, P(profit) 0.1718, adj growth 1.7 bp · R EV +0.32 (adj +0.19) on $2.00, P(profit) 0.221, adj growth 6.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
