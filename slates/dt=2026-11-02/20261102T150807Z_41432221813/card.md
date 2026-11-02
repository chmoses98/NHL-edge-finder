# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T15:08:07Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 133.37 | +19.14 | +8.08 | +7.09 | 0.538 | -62.31 | -69.61 | 58.49 |
| B thesis-diversified (joint) ← optimiser card | 113.75 | +13.36 | +6.84 | +6.25 | 0.645 | -39.35 | -45.32 | 60.40 |
| C best expression per thesis | 84.54 | +9.50 | +4.63 | +11.15 | 0.555 | -33.48 | -39.90 | 40.98 |
| R FUNDED research stakes | 11.00 | +1.82 | +1.06 | -3.26 | 0.498 | -11.00 | -11.00 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  430 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_VGK_win | p_overtime | goals | shots BOS/VGK | BOS/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 6.02 | 27.3/27.5 | 24.2/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.47 | 6.02 | 27.3/27.8 | 24.5/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.49 | 0.51 | 0.00 | 9.36 | 28.9/29.2 | 23.0/22.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.090 | 0.49 | 0.51 | 0.00 | 6.02 | 21.7/32.5 | 28.7/18.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.48 | 0.52 | 0.49 | 6.02 | 21.9/32.8 | 29.4/18.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.066 | 0.46 | 0.54 | 0.00 | 9.36 | 23.2/34.5 | 27.5/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 5 | 0.072 | 0.066 | +0.019 | +0.012 | $2.88 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS3|yes; why: higher confidence-adjusted growth (6.32 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.023/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0005 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BOS:WINS_BY_2PLUS (p 0.2948): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02VGKBOS-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3597, phi -0.147)

portfolios: A EV +1.80 (adj +1.15) on $5.04, P(profit) 0.0724, adj growth 8.7 bp · B EV +1.03 (adj +0.66) on $2.88, P(profit) 0.0724, adj growth 5.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.36 (adj +0.23) on $1.00, P(profit) 0.0724, adj growth 7.4 bp

## DET @ FLA  ·  10000 joint draws  ·  408 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.0 | 27.0/26.8 | 23.8/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.53 | 0.47 | 0.48 | 5.95 | 27.1/27.0 | 23.7/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.60 | 0.40 | 0.00 | 9.24 | 28.6/28.5 | 23.1/22.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.072 | 0.66 | 0.34 | 0.00 | 6.03 | 31.9/21.5 | 18.7/27.4 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.46 | 5.92 | 31.8/21.5 | 18.4/28.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.061 | 0.50 | 0.50 | 0.00 | 6.02 | 21.8/32.2 | 28.5/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 63 | 0.705 | 0.685 | +0.059 | +0.039 | $17.03 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.128 | 0.114 | +0.032 | +0.019 | $4.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.676 | 0.660 | +0.040 | +0.023 | $12.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Detroit over 3.5 goals scored YES | 29 | 0.361 | 0.321 | +0.057 | +0.016 | $5.68 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (14.63 vs 5.09 bp); relationships: KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLASBENNETT9-1|yes; why: higher confidence-adjusted growth (8.67 vs 1.61 bp); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: MOSTLY_INDEPENDENT (phi -0.038); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (14.63 vs 5.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Detroit over 3.5 goals scored YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3439): highest fidelity KXNHLSPREAD-26NOV02DETFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:OFFENSE_4PLUS (p 0.3511): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes — Broad expression KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis DET:WINS (p 0.4426): highest fidelity KXNHLSPREAD-26NOV02DETFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4327, phi -0.241)
- KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3439, phi -0.161)
- KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4327, phi -0.244)
- KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:SUPPRESSED (p 0.4308, phi -0.654)
- override: Broad expression KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.77 (adj +3.29) on $50.00, P(profit) 0.3614, adj growth 18.9 bp · B EV +5.01 (adj +2.73) on $40.42, P(profit) 0.6194, adj growth 24.4 bp · C EV +3.86 (adj +2.02) on $28.50, P(profit) 0.7595, adj growth 18.1 bp · R EV +0.83 (adj +0.41) on $7.00, P(profit) 0.7054, adj growth 14.5 bp

## COL @ CHI  ·  10000 joint draws  ·  426 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_COL_win | p_overtime | goals | shots CHI/COL | CHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.155 | 0.28 | 0.72 | 0.00 | 6.04 | 21.4/34.2 | 29.2/19.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.113 | 0.23 | 0.77 | 0.00 | 9.36 | 23.2/36.4 | 28.0/18.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.43 | 0.57 | 0.48 | 5.98 | 21.9/34.8 | 31.4/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.100 | 0.33 | 0.67 | 0.00 | 6.06 | 27.6/28.7 | 24.1/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.48 | 0.52 | 0.46 | 5.91 | 27.6/28.6 | 25.1/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.33 | 0.67 | 0.00 | 9.37 | 29.2/30.2 | 23.3/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.269 | 0.253 | +0.047 | +0.031 | $11.41 | FUNDED_RESEARCH | $3 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 61 | 0.693 | 0.646 | +0.066 | +0.020 | $17.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 54 | 0.623 | 0.576 | +0.065 | +0.019 | $12.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Frank Nazar: 1+ goals YES | 18 | 0.215 | 0.204 | +0.025 | +0.013 | $4.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (12.05 vs 2.54 bp); relationships: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.17); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.16); KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (3.67 vs 3.17 bp); relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.17); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.128); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no; why: second expression of the same thesis: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no has the higher standalone adjusted growth (3.67 vs 3.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.132); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.16); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: CHI offense succeeds (4+ goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (12.05 vs 2.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.128); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.314): highest fidelity KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4713): highest fidelity KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no (same contract)
- thesis COL:SUPPRESSED (p 0.2857): highest fidelity KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no (same contract)
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4713, phi -0.267)
- KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.314, phi -0.269)
- KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.314, phi -0.269)
- KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4713, phi -0.235)

portfolios: A EV +7.06 (adj +2.83) on $50.00, P(profit) 0.5461, adj growth 24.4 bp · B EV +6.38 (adj +2.93) on $46.40, P(profit) 0.7203, adj growth 25.6 bp · C EV +5.23 (adj +2.36) on $36.04, P(profit) 0.5305, adj growth 20.6 bp · R EV +0.63 (adj +0.42) on $3.00, P(profit) 0.2685, adj growth 14.0 bp

## CGY @ SJS  ·  10000 joint draws  ·  424 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_CGY_win | p_overtime | goals | shots SJS/CGY | SJS/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.60 | 0.40 | 0.00 | 6.06 | 28.8/28.7 | 25.5/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.47 | 5.92 | 28.8/28.8 | 25.5/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.57 | 0.43 | 0.00 | 9.32 | 29.9/29.8 | 24.3/23.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.074 | 0.66 | 0.34 | 0.00 | 6.02 | 33.7/22.7 | 20.0/29.1 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.46 | 5.98 | 33.9/23.0 | 19.8/30.6 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.058 | 0.55 | 0.45 | 0.00 | 6.03 | 22.9/33.3 | 30.0/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dmitry Orlov: 1+ goals NO | 91 | 0.934 | 0.927 | +0.019 | +0.011 | $20.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 19 | 0.227 | 0.214 | +0.027 | +0.013 | $4.05 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Dmitry Orlov: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (2.48 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJDORLOV9-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4478): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02CGYSJ-SJDORLOV9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4478, phi -0.105)
- KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3356, phi -0.2)

portfolios: A EV +1.51 (adj +0.81) on $28.33, P(profit) 0.2274, adj growth 6.5 bp · B EV +0.95 (adj +0.52) on $24.05, P(profit) 0.2122, adj growth 4.7 bp · C EV +0.41 (adj +0.25) on $20.00, P(profit) 0.9345, adj growth 2.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
