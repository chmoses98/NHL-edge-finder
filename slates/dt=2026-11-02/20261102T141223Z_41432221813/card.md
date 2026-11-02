# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T14:12:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 105.04 | +17.83 | +7.04 | +3.86 | 0.510 | -58.51 | -75.95 | 48.72 |
| B thesis-diversified (joint) ← optimiser card | 80.68 | +10.85 | +5.20 | +11.13 | 0.557 | -30.65 | -36.79 | 45.98 |
| C best expression per thesis | 53.25 | +6.86 | +3.23 | +5.14 | 0.679 | -25.81 | -25.81 | 28.67 |
| R FUNDED research stakes | 9.00 | +1.40 | +0.79 | -1.26 | 0.328 | -9.00 | -9.00 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  424 bet sides mapped, 1 +EV candidates, 1 on card


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
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLPTS-26NOV02VGKBOS-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (6.32 vs 0.14 bp); despite a smaller raw edge (+0.019 vs +0.079/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: BOS offense suppressed (<= 2 goals)

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
| Sam Reinhart: 1+ goals NO | 63 | 0.705 | 0.685 | +0.059 | +0.039 | $17.08 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.128 | 0.112 | +0.032 | +0.016 | $3.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.676 | 0.660 | +0.040 | +0.023 | $12.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 2+ goals YES | 7 | 0.093 | 0.086 | +0.018 | +0.011 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (14.63 vs 5.09 bp); relationships: KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLASBENNETT9-1|yes; why: higher confidence-adjusted growth (6.53 vs 1.61 bp); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (14.63 vs 5.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: FLA offense succeeds (4+ goals)
- **Alex DeBrincat: 2+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes; why: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.19 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3439): highest fidelity KXNHLSPREAD-26NOV02DETFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:OFFENSE_4PLUS (p 0.3511): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes — Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.19 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DET:WINS (p 0.4426): highest fidelity KXNHLSPREAD-26NOV02DETFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4327, phi -0.241)
- KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3439, phi -0.161)
- KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4327, phi -0.244)
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4308, phi -0.222)
- override: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-2|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.19 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +8.77 (adj +3.29) on $50.00, P(profit) 0.3614, adj growth 18.9 bp · B EV +4.36 (adj +2.59) on $36.72, P(profit) 0.5874, adj growth 23.2 bp · C EV +3.86 (adj +2.02) on $28.50, P(profit) 0.7595, adj growth 18.1 bp · R EV +0.46 (adj +0.30) on $5.00, P(profit) 0.7054, adj growth 11.1 bp

## COL @ CHI  ·  10000 joint draws  ·  426 bet sides mapped, 4 +EV candidates, 4 on card


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
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.269 | 0.253 | +0.036 | +0.021 | $7.44 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 61 | 0.693 | 0.646 | +0.066 | +0.020 | $16.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 54 | 0.623 | 0.576 | +0.065 | +0.019 | $13.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Chicago over 4.5 goals scored YES | 12 | 0.162 | 0.138 | +0.034 | +0.011 | $3.64 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5|yes; why: higher confidence-adjusted growth (5.18 vs 2.32 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.945 vs 0.581); relationships: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.17); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.16); KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5|yes: REINFORCING (phi 0.197); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (3.67 vs 3.17 bp); relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.17); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5|yes: INTENTIONAL_DIVERSIFIER (phi -0.222); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no; why: second expression of the same thesis: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no has the higher standalone adjusted growth (3.67 vs 3.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.132); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.16); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5|yes: INTENTIONAL_DIVERSIFIER (phi -0.226); failure: CHI offense succeeds (4+ goals)
- **Chicago over 4.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (5.18 vs 2.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.197); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.197); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.222); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.226); failure: COL wins (incl. OT/SO)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.314): highest fidelity KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4713): highest fidelity KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4713, phi -0.267)
- KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.314, phi -0.269)
- KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.314, phi -0.269)
- KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5|yes: FUNDED_RESEARCH; family MIXED; loses 49% of the draws where the thesis happens; opposing: failure thesis COL:WINS (p 0.6329, phi -0.439)

portfolios: A EV +7.26 (adj +2.60) on $50.00, P(profit) 0.681, adj growth 21.1 bp · B EV +5.47 (adj +1.95) on $41.08, P(profit) 0.6541, adj growth 17.2 bp · C EV +3.01 (adj +1.21) on $24.75, P(profit) 0.8101, adj growth 10.6 bp · R EV +0.58 (adj +0.26) on $3.00, P(profit) 0.3545, adj growth 8.4 bp

## CGY @ SJS  ·  10000 joint draws  ·  424 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_CGY_win | p_overtime | goals | shots SJS/CGY | SJS/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.60 | 0.40 | 0.00 | 6.06 | 28.8/28.7 | 25.5/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.47 | 5.92 | 28.8/28.8 | 25.5/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.57 | 0.43 | 0.00 | 9.32 | 29.9/29.8 | 24.3/23.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.074 | 0.66 | 0.34 | 0.00 | 6.02 | 33.7/22.7 | 20.0/29.1 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.46 | 5.98 | 33.9/23.0 | 19.8/30.6 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.058 | 0.55 | 0.45 | 0.00 | 6.03 | 22.9/33.3 | 30.0/19.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
