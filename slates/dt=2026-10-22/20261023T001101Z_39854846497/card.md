# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T00:11:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.05 | +5.67 | +29.08 | 0.720 | -35.93 | -54.46 | 44.48 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +26.93 | +17.33 | +20.97 | 0.637 | -44.35 | -59.19 | 156.54 |
| C best expression per thesis | 116.58 | +20.72 | +10.28 | +10.84 | 0.636 | -44.79 | -49.55 | 89.77 |
| R FUNDED research stakes | 24.00 | +2.78 | +1.64 | +3.16 | 0.521 | -8.26 | -9.75 | 0.00 |

## MIN @ CGY  ·  10000 joint draws  ·  438 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.345 / away 0.655

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_MIN_win | p_overtime | goals | shots CGY/MIN | CGY/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.43 | 0.57 | 0.00 | 6.03 | 29.2/29.5 | 25.6/25.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.49 | 0.51 | 0.49 | 5.91 | 29.5/29.7 | 26.4/26.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.085 | 0.38 | 0.62 | 0.00 | 5.98 | 23.6/34.8 | 30.3/20.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.45 | 0.55 | 0.00 | 9.18 | 31.0/31.2 | 24.7/25.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.47 | 5.88 | 23.6/34.9 | 31.5/20.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.43 | 0.57 | 0.00 | 3.45 | 28.1/28.3 | 26.2/26.4 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aydar Suniev: 1+ goals YES | 16 | 0.221 | 0.205 | +0.052 | +0.035 | $5.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ben Jones: 1+ goals NO | 86 | 0.909 | 0.895 | +0.041 | +0.027 | $12.33 | FUNDED_RESEARCH | $4 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 2+ goals NO | 87 | 0.914 | 0.899 | +0.036 | +0.021 | $12.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 59 | 0.650 | 0.634 | +0.043 | +0.027 | $9.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN3|no; why: higher confidence-adjusted growth (19.10 vs 8.32 bp); despite a smaller raw edge (+0.052 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22MINCGY-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: CGY offense suppressed (<= 2 goals)
- **Ben Jones: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22MINCGY-CGYBJONES39-1|no; why: higher confidence-adjusted growth (14.33 vs 1.27 bp); despite a smaller raw edge (+0.041 vs +0.107/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22MINCGY-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.019); failure: CGY offense succeeds (4+ goals)
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no; why: Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.99 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22MINCGY-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense succeeds (4+ goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (9.60 vs 6.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CGY:OFFENSE_4PLUS (p 0.3347): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3925): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no — Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.99 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CGY:WINS (p 0.4589): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4473, phi -0.228)
- KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3347, phi -0.146)
- KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3999, phi -0.246)
- KXNHLGOAL-26OCT22MINCGY-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3999, phi -0.261)
- override: Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.99 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.44 (adj +0.95) on $37.50, P(profit) 0.5622, adj growth 6.9 bp · B EV +3.49 (adj +2.28) on $40.11, P(profit) 0.6396, adj growth 21.4 bp · C EV +7.87 (adj +3.56) on $50.00, P(profit) 0.5155, adj growth 31.2 bp · R EV +0.19 (adj +0.12) on $4.00, P(profit) 0.909, adj growth 4.8 bp

## CAR @ EDM  ·  10000 joint draws  ·  442 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.453 / away 0.547

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CAR_win | p_overtime | goals | shots EDM/CAR | EDM/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.65 | 0.35 | 0.00 | 6.04 | 27.6/28.2 | 25.1/23.3 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.106 | 0.55 | 0.45 | 0.00 | 6.04 | 21.7/33.3 | 29.9/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.63 | 0.37 | 0.00 | 9.49 | 28.9/29.5 | 23.9/21.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.46 | 5.94 | 27.4/28.0 | 24.8/24.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.46 | 0.54 | 0.48 | 5.98 | 21.7/33.4 | 30.0/18.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.091 | 0.56 | 0.44 | 0.00 | 9.4 | 23.3/35.2 | 28.9/17.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 12 | 0.185 | 0.168 | +0.058 | +0.040 | $8.02 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 7 | 0.111 | 0.100 | +0.036 | +0.025 | $4.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 24 | 0.290 | 0.276 | +0.037 | +0.023 | $5.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 79 | 0.856 | 0.821 | +0.055 | +0.019 | $13.54 | FUNDED_RESEARCH | $4 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: higher confidence-adjusted growth (31.15 vs 7.47 bp); despite a smaller raw edge (+0.058 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.078); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: higher confidence-adjusted growth (19.04 vs 7.47 bp); despite a smaller raw edge (+0.036 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.076); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: KXNHLSPREAD-26OCT22CAREDM-CAR2|no has the higher standalone adjusted growth (7.47 vs 6.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.119); failure: EDM offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.078); KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.076); KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.119); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4849): highest fidelity KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS (p 0.5638): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- thesis CAR:SUPPRESSED (p 0.3931): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no — Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT22CAREDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.166)
- KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.138)
- KXNHLGOAL-26OCT22CAREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3106, phi -0.224)
- KXNHLSPREAD-26OCT22CAREDM-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2309, phi -0.748)
- override: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.25 (adj +1.95) on $37.50, P(profit) 0.5164, adj growth 16.3 bp · B EV +7.57 (adj +4.87) on $31.57, P(profit) 0.4638, adj growth 43.0 bp · C EV +2.12 (adj +0.77) on $20.00, P(profit) 0.7691, adj growth 7.0 bp · R EV +1.64 (adj +1.05) on $7.00, P(profit) 0.1854, adj growth 34.9 bp

## UTA @ SEA  ·  10000 joint draws  ·  458 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.393 / away 0.607

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.51 | 0.49 | 0.00 | 6.05 | 27.3/27.7 | 24.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.45 | 5.99 | 27.3/27.8 | 24.6/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.49 | 0.51 | 0.00 | 9.34 | 28.9/29.4 | 23.5/22.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.098 | 0.42 | 0.58 | 0.00 | 6.01 | 21.5/33.0 | 29.1/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.46 | 0.54 | 0.47 | 5.96 | 21.6/32.9 | 29.5/18.4 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.077 | 0.39 | 0.61 | 0.00 | 9.26 | 23.1/34.8 | 27.4/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Shane Wright: 1+ goals YES | 15 | 0.205 | 0.189 | +0.046 | +0.030 | $6.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Utah wins by over 2.5 goals NO | 72 | 0.808 | 0.762 | +0.074 | +0.028 | $16.04 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.700 | 0.683 | +0.044 | +0.027 | $14.17 | FUNDED_RESEARCH | $4 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.148 | 0.140 | +0.021 | +0.013 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: higher confidence-adjusted growth (14.52 vs 8.60 bp); despite a smaller raw edge (+0.046 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT22UTASEA-UTA3|no: MOSTLY_INDEPENDENT (phi 0.117); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22UTASEA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: SEA offense suppressed (<= 2 goals)
- **Utah wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-SEA3|yes; why: higher confidence-adjusted growth (8.60 vs 6.22 bp); wins across more scripts (relative breadth 1.031 vs 0.464); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.117); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT22UTASEA-UTAJMCBAIN22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.118); failure: UTA wins by 2+
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.60 vs 7.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.152); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT22UTASEA-UTA3|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT22UTASEA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense succeeds (4+ goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT22UTASEA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (3.12 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT22UTASEA-UTA3|no: INTENTIONAL_DIVERSIFIER (phi -0.118); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4001): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4891): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3607): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no (same contract)
- KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.222)
- KXNHLSPREAD-26OCT22UTASEA-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.3029, phi -0.739)
- KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4242, phi -0.25)
- KXNHLGOAL-26OCT22UTASEA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3607, phi -0.155)

portfolios: A EV +7.58 (adj +1.26) on $37.50, P(profit) 0.5849, adj growth 9.5 bp · B EV +4.90 (adj +2.68) on $39.58, P(profit) 0.701, adj growth 24.1 bp · C EV +4.28 (adj +2.21) on $27.73, P(profit) 0.2053, adj growth 19.4 bp · R EV +0.77 (adj +0.35) on $9.00, P(profit) 0.5931, adj growth 12.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  442 bet sides mapped, 24 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.399 / away 0.601

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 6.05 | 21.8/33.5 | 29.9/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.8 | 24.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.94 | 27.5/28.1 | 24.8/24.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.50 | 5.91 | 21.8/33.5 | 30.2/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.56 | 0.44 | 0.00 | 9.34 | 29.0/29.5 | 23.7/22.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.074 | 0.51 | 0.49 | 0.00 | 9.2 | 23.2/35.2 | 28.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Liam Ohgren: 1+ goals YES | 10 | 0.177 | 0.155 | +0.070 | +0.049 | $7.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 19 | 0.270 | 0.248 | +0.069 | +0.047 | $8.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.259 | 0.241 | +0.059 | +0.040 | $7.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Moritz Seider: 1+ goals NO | 85 | 0.898 | 0.885 | +0.040 | +0.026 | $14.66 | FUNDED_RESEARCH | $4 | DET:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: higher confidence-adjusted growth (52.22 vs 29.27 bp); relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22DETVAN-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (29.27 vs 21.39 bp); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22DETVAN-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (29.27 vs 21.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22DETVAN-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: higher confidence-adjusted growth (12.63 vs 11.25 bp); despite a smaller raw edge (+0.040 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.006 vs 0.534); relationships: KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: DET offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4129): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5383): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-DET4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.186)
- KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.246)
- KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.215)
- KXNHLGOAL-26OCT22DETVAN-DETMSEIDER53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.358, phi -0.139)

portfolios: A EV +7.77 (adj +1.51) on $37.50, P(profit) 0.6508, adj growth 11.8 bp · B EV +10.98 (adj +7.50) on $38.73, P(profit) 0.5425, adj growth 68.0 bp · C EV +6.45 (adj +3.74) on $18.85, P(profit) 0.458, adj growth 32.2 bp · R EV +0.18 (adj +0.12) on $4.00, P(profit) 0.8985, adj growth 4.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
