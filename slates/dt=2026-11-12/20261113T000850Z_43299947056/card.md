# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-13T00:08:50Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.28 | +10.23 | +23.63 | 0.680 | -37.51 | -53.49 | 89.36 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +29.02 | +14.74 | +23.73 | 0.665 | -41.67 | -55.84 | 130.55 |
| C best expression per thesis | 129.52 | +18.81 | +7.39 | +16.31 | 0.664 | -34.27 | -47.19 | 64.92 |
| R FUNDED research stakes | 14.00 | +2.66 | +1.70 | +0.84 | 0.544 | -9.14 | -10.21 | 0.00 |

## DET @ FLA  ·  10000 joint draws  ·  420 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.634 / away 0.366

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.60 | 0.40 | 0.00 | 6.02 | 27.5/27.4 | 24.3/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.50 | 5.93 | 27.7/27.6 | 24.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.63 | 0.37 | 0.00 | 9.38 | 29.3/29.0 | 23.7/22.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.68 | 0.32 | 0.00 | 5.98 | 32.1/21.4 | 18.9/27.5 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.57 | 0.43 | 0.48 | 5.89 | 32.5/22.2 | 19.1/29.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 5.98 | 22.1/32.3 | 28.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Schwindt: 1+ goals YES | 8 | 0.107 | 0.099 | +0.021 | +0.013 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.683 | 0.669 | +0.037 | +0.023 | $14.14 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Niko Mikkola: 1+ goals YES | 5 | 0.070 | 0.064 | +0.017 | +0.010 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 13 | 0.161 | 0.152 | +0.023 | +0.014 | $3.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes; why: higher confidence-adjusted growth (5.07 vs 1.99 bp); despite a smaller raw edge (+0.021 vs +0.024/contract); relationships: KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV12DETFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (4.89 vs 1.14 bp); despite a smaller raw edge (+0.037 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV12DETFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: FLA offense succeeds (4+ goals)
- **Niko Mikkola: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes; why: higher confidence-adjusted growth (4.54 vs 1.99 bp); despite a smaller raw edge (+0.017 vs +0.024/contract); relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: FLA offense suppressed (<= 2 goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (3.42 vs 1.14 bp); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV12DETFLA-FLANMIKKOLA77-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3447): highest fidelity KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no (same contract)
- thesis DET:SUPPRESSED (p 0.4488): highest fidelity KXNHLAST-26NOV12DETFLA-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12DETFLA-DETLRAYMOND23-1|no (same contract)
- thesis FLA:OFFENSE_4PLUS (p 0.4446): highest fidelity KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3447, phi -0.146)
- KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.238)
- KXNHLGOAL-26NOV12DETFLA-FLANMIKKOLA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3447, phi -0.101)
- KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4488, phi -0.193)

portfolios: A EV +2.85 (adj +0.77) on $30.00, P(profit) 0.5547, adj growth 6.7 bp · B EV +2.83 (adj +1.75) on $22.85, P(profit) 0.303, adj growth 15.3 bp · C EV +2.14 (adj +1.02) on $30.14, P(profit) 0.5791, adj growth 8.9 bp · R EV +0.23 (adj +0.14) on $4.00, P(profit) 0.6835, adj growth 4.9 bp

## BUF @ CHI  ·  10000 joint draws  ·  422 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.417 / away 0.583

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_BUF_win | p_overtime | goals | shots CHI/BUF | CHI/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.51 | 0.49 | 0.00 | 6.02 | 27.2/27.7 | 24.1/23.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.115 | 0.45 | 0.55 | 0.00 | 6.01 | 21.6/33.2 | 29.2/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.49 | 5.94 | 21.7/33.4 | 30.0/18.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 5.91 | 27.1/27.8 | 24.6/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.47 | 0.53 | 0.00 | 9.24 | 28.3/29.3 | 23.0/22.5 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.076 | 0.43 | 0.57 | 0.00 | 9.26 | 23.0/34.5 | 27.4/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo over 3.5 goals scored NO | 51 | 0.600 | 0.552 | +0.072 | +0.025 | $7.15 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 24 | 0.287 | 0.274 | +0.034 | +0.021 | $6.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 60 | 0.653 | 0.638 | +0.036 | +0.021 | $8.30 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Rasmus Dahlin: 1+ goals NO | 80 | 0.836 | 0.826 | +0.025 | +0.015 | $12.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (5.45 vs 4.28 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.249); KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: REINFORCING (phi 0.184); failure: BUF offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: higher confidence-adjusted growth (5.11 vs 2.31 bp); despite a smaller raw edge (+0.034 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no has the higher standalone adjusted growth (5.45 vs 4.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.249); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: REINFORCING (phi 0.249); KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: BUF offense succeeds (4+ goals)
- **Rasmus Dahlin: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no has the higher standalone adjusted growth (5.45 vs 3.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.184); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: REINFORCING (phi 0.184); KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BUF:SUPPRESSED (p 0.3878): highest fidelity KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no (same contract)
- thesis CHI:WINS (p 0.4913): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2738): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3889, phi -0.977)
- KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4045, phi -0.253)
- KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3889, phi -0.251)
- KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3889, phi -0.181)

portfolios: A EV +3.35 (adj +1.07) on $30.00, P(profit) 0.5544, adj growth 8.2 bp · B EV +2.67 (adj +1.37) on $33.81, P(profit) 0.5562, adj growth 12.3 bp · C EV +2.73 (adj +1.19) on $20.05, P(profit) 0.7126, adj growth 10.4 bp · R EV +0.45 (adj +0.20) on $5.00, P(profit) 0.4496, adj growth 7.1 bp

## WPG @ DAL  ·  10000 joint draws  ·  416 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.591 / away 0.409

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.60 | 0.40 | 0.00 | 5.99 | 26.1/25.8 | 22.8/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.47 | 5.9 | 26.1/26.0 | 22.7/22.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.102 | 0.68 | 0.32 | 0.00 | 5.98 | 30.7/20.4 | 17.8/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.15 | 27.6/27.2 | 22.0/21.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.60 | 0.40 | 0.48 | 5.96 | 31.2/20.9 | 17.9/27.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.61 | 0.39 | 0.00 | 3.47 | 24.8/24.7 | 23.1/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Morrissey: 1+ assists NO | 59 | 0.743 | 0.640 | +0.136 | +0.033 | $18.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Jamie Benn: 1+ goals YES | 16 | 0.200 | 0.189 | +0.030 | +0.019 | $5.17 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 27 | 0.318 | 0.305 | +0.034 | +0.021 | $6.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ assists YES | 30 | 0.362 | 0.329 | +0.047 | +0.014 | $5.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12WPGDAL-WPGJMORRISSEY44-1|no; why: higher confidence-adjusted growth (10.29 vs 0.31 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.094); failure: WPG offense succeeds (4+ goals)
- **Jamie Benn: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes; why: higher confidence-adjusted growth (5.58 vs 4.70 bp); despite a smaller raw edge (+0.030 vs +0.034/contract); relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: DAL offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes has the higher standalone adjusted growth (5.58 vs 4.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: DAL offense suppressed (<= 2 goals)
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12WPGDAL-WPGNPIONK4-1|yes; why: higher confidence-adjusted growth (1.94 vs 0.91 bp); alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: INTENTIONAL_DIVERSIFIER (phi -0.094); KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:SUPPRESSED (p 0.4737): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no (same contract)
- thesis DAL:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3102): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes (same contract)
- KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3102, phi -0.22)
- KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3527, phi -0.185)
- KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3527, phi -0.241)
- KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4737, phi -0.298)

portfolios: A EV +4.16 (adj +1.32) on $30.00, P(profit) 0.5071, adj growth 12.0 bp · B EV +6.63 (adj +2.31) on $35.33, P(profit) 0.5371, adj growth 20.7 bp · C EV +6.37 (adj +1.99) on $31.44, P(profit) 0.7967, adj growth 17.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.456 / away 0.544

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_STL_win | p_overtime | goals | shots UTA/STL | UTA/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 6.0 | 27.1/27.0 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.49 | 5.94 | 27.3/27.0 | 23.7/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.102 | 0.61 | 0.39 | 0.00 | 6.05 | 32.4/21.4 | 18.5/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.52 | 0.48 | 0.00 | 9.34 | 29.1/28.7 | 22.8/23.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.45 | 5.92 | 32.6/21.5 | 18.4/29.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 9.2 | 33.9/22.8 | 17.9/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 18 | 0.246 | 0.228 | +0.056 | +0.038 | $10.23 | FUNDED_RESEARCH | $3 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 13 | 0.182 | 0.168 | +0.044 | +0.030 | $7.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Liam O'Brien: 1+ goals YES | 7 | 0.095 | 0.087 | +0.020 | +0.013 | $2.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Kevin Stenlund: 1+ goals YES | 8 | 0.104 | 0.097 | +0.019 | +0.012 | $2.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12STLUTA-UTABHAYTON27-1|yes; why: higher confidence-adjusted growth (20.21 vs 4.68 bp); despite a smaller raw edge (+0.056 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-UTALOBRIEN38-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV12STLUTA-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 16.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-UTALOBRIEN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV12STLUTA-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense suppressed (<= 2 goals)
- **Liam O'Brien: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 4.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV12STLUTA-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: UTA offense suppressed (<= 2 goals)
- **Kevin Stenlund: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 3.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12STLUTA-UTALOBRIEN38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4237): highest fidelity KXNHLTEAMTOTAL-26NOV12STLUTA-UTA5|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3627): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.231)
- KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.187)
- KXNHLGOAL-26NOV12STLUTA-UTALOBRIEN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.129)
- KXNHLGOAL-26NOV12STLUTA-UTAKSTENLUND82-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.156)

portfolios: A EV +7.57 (adj +3.86) on $30.00, P(profit) 0.5801, adj growth 33.5 bp · B EV +6.81 (adj +4.55) on $23.39, P(profit) 0.5041, adj growth 39.7 bp · C EV +3.23 (adj +2.20) on $10.99, P(profit) 0.2462, adj growth 18.9 bp · R EV +0.88 (adj +0.60) on $3.00, P(profit) 0.2462, adj growth 20.4 bp

## NYI @ LAK  ·  10000 joint draws  ·  364 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NYI_win | p_overtime | goals | shots LAK/NYI | LAK/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 5.98 | 27.8/27.6 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.86 | 27.8/27.5 | 24.4/24.6 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.086 | 0.60 | 0.40 | 0.00 | 5.98 | 32.9/22.3 | 19.3/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.50 | 5.87 | 33.1/22.2 | 19.0/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.25 | 29.4/29.2 | 23.9/22.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 2.83 | 26.4/26.2 | 24.7/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Lee: 1+ goals YES | 8 | 0.132 | 0.118 | +0.047 | +0.032 | $7.30 | FUNDED_RESEARCH | $2 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 65 | 0.851 | 0.717 | +0.185 | +0.051 | $18.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 27 | 0.312 | 0.301 | +0.029 | +0.017 | $5.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Erik Haula: 1+ goals YES | 15 | 0.178 | 0.170 | +0.019 | +0.011 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (28.42 vs 3.04 bp); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV12NYILA-LAEHAULA56-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: LAK offense suppressed (<= 2 goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (25.96 vs 2.89 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26NOV12NYILA-LAEHAULA56-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); failure: LAK offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (3.04 vs 1.29 bp); despite a smaller raw edge (+0.029 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26NOV12NYILA-LAEHAULA56-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: LAK offense suppressed (<= 2 goals)
- **Erik Haula: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes has the higher standalone adjusted growth (3.04 vs 2.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.386): highest fidelity KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.395): highest fidelity KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no (same contract)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.16)
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.181)
- KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.261)
- KXNHLGOAL-26NOV12NYILA-LAEHAULA56-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.204)

portfolios: A EV +8.35 (adj +3.21) on $30.00, P(profit) 0.4443, adj growth 29.0 bp · B EV +10.08 (adj +4.76) on $34.61, P(profit) 0.4568, adj growth 42.6 bp · C EV +4.35 (adj +0.99) on $36.90, P(profit) 0.7843, adj growth 8.9 bp · R EV +1.10 (adj +0.76) on $2.00, P(profit) 0.1318, adj growth 25.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
