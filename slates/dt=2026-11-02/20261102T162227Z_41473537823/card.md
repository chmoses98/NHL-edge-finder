# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T16:22:27Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +18.95 | +7.52 | +16.79 | 0.616 | -50.94 | -68.79 | 60.25 |
| B thesis-diversified (joint) ← optimiser card | 121.82 | +11.25 | +6.14 | +11.27 | 0.608 | -34.42 | -49.34 | 54.77 |
| C best expression per thesis | 62.45 | +8.12 | +3.67 | +12.25 | 0.603 | -31.50 | -38.39 | 32.37 |
| R FUNDED research stakes | 15.00 | +0.95 | +0.62 | -0.79 | 0.474 | -7.39 | -8.61 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  426 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_VGK_win | p_overtime | goals | shots BOS/VGK | BOS/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.52 | 0.48 | 0.00 | 6.02 | 27.2/27.5 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.47 | 6.0 | 27.3/27.6 | 24.4/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.54 | 0.46 | 0.00 | 9.37 | 28.7/29.0 | 23.0/22.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.092 | 0.47 | 0.53 | 0.00 | 6.03 | 21.6/32.5 | 28.7/18.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.48 | 0.52 | 0.47 | 5.95 | 21.7/32.8 | 29.3/18.5 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.058 | 0.46 | 0.54 | 0.00 | 9.21 | 23.3/34.3 | 27.7/17.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ FLA  ·  10000 joint draws  ·  422 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.57 | 0.43 | 0.00 | 6.04 | 27.1/27.1 | 23.9/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.45 | 5.97 | 27.3/27.2 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.57 | 0.43 | 0.00 | 9.37 | 28.6/28.6 | 22.7/22.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.074 | 0.66 | 0.34 | 0.00 | 5.99 | 31.7/21.2 | 18.6/27.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.54 | 0.46 | 0.49 | 5.87 | 31.9/21.6 | 18.6/28.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.064 | 0.51 | 0.49 | 0.00 | 6.0 | 21.5/31.6 | 27.9/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 63 | 0.702 | 0.683 | +0.056 | +0.037 | $16.86 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.676 | 0.661 | +0.040 | +0.024 | $13.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 12 | 0.155 | 0.143 | +0.027 | +0.016 | $4.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 35 | 0.399 | 0.385 | +0.033 | +0.019 | $7.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (12.99 vs 5.58 bp); relationships: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (12.99 vs 5.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: FLA offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes; why: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes has the higher standalone adjusted growth (5.62 vs 5.06 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.175); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes; why: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.59 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis FLA:SUPPRESSED (p 0.3462): highest fidelity KXNHLSPREAD-26NOV02DETFLA-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:OFFENSE_4PLUS (p 0.3655): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes (same contract)
- thesis DET:WINS (p 0.4432): highest fidelity KXNHLSPREAD-26NOV02DETFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4318, phi -0.242)
- KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4318, phi -0.248)
- KXNHLGOAL-26NOV02DETFLA-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4271, phi -0.177)
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4271, phi -0.31)
- override: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.59 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.78 (adj +2.51) on $50.00, P(profit) 0.476, adj growth 20.0 bp · B EV +3.87 (adj +2.40) on $41.78, P(profit) 0.6209, adj growth 21.5 bp · C EV +3.50 (adj +1.72) on $27.54, P(profit) 0.7024, adj growth 15.4 bp · R EV +0.43 (adj +0.28) on $5.00, P(profit) 0.7024, adj growth 10.4 bp

## COL @ CHI  ·  10000 joint draws  ·  434 bet sides mapped, 7 +EV candidates, 4 on card


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
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.269 | 0.254 | +0.036 | +0.022 | $7.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 77 | 0.812 | 0.800 | +0.030 | +0.018 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 54 | 0.623 | 0.576 | +0.065 | +0.019 | $14.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Frank Nazar: 1+ goals YES | 18 | 0.215 | 0.204 | +0.025 | +0.013 | $4.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (5.82 vs 2.54 bp); relationships: KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.16); KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (4.23 vs 3.54 bp); despite a smaller raw edge (+0.030 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: COL offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.17 vs 2.80 bp); despite a smaller raw edge (+0.065 vs +0.066/contract); relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.16); KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: CHI offense succeeds (4+ goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (5.82 vs 2.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.314): highest fidelity KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.2857): highest fidelity KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no (same contract)
- thesis CHI:SUPPRESSED (p 0.4713): highest fidelity KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4713, phi -0.267)
- KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.512, phi -0.176)
- KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.314, phi -0.269)
- KXNHLGOAL-26NOV02COLCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4713, phi -0.235)

portfolios: A EV +6.45 (adj +2.30) on $50.00, P(profit) 0.5461, adj growth 19.4 bp · B EV +4.20 (adj +1.98) on $46.22, P(profit) 0.7134, adj growth 17.3 bp · C EV +4.01 (adj +1.58) on $29.42, P(profit) 0.5051, adj growth 13.8 bp · R EV +0.19 (adj +0.12) on $5.00, P(profit) 0.8123, adj growth 4.1 bp

## CGY @ SJS  ·  10000 joint draws  ·  438 bet sides mapped, 4 +EV candidates, 4 on card


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
| Ivar Stenberg: 1+ goals NO | 76 | 0.824 | 0.806 | +0.051 | +0.034 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 24 | 0.281 | 0.270 | +0.028 | +0.017 | $5.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 19 | 0.227 | 0.215 | +0.027 | +0.015 | $4.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Collin Graf: 1+ assists YES | 26 | 0.319 | 0.287 | +0.046 | +0.014 | $4.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02CGYSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (14.38 vs 0.15 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV02CGYSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02CGYSJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (3.28 vs 2.05 bp); despite a smaller raw edge (+0.028 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26NOV02CGYSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.032); failure: SJS offense suppressed (<= 2 goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes has the higher standalone adjusted growth (3.28 vs 2.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26NOV02CGYSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: SJS offense suppressed (<= 2 goals)
- **Collin Graf: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes has the higher standalone adjusted growth (3.28 vs 2.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4478): highest fidelity KXNHLAST-26NOV02CGYSJ-SJCGRAF51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3356): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4478, phi -0.184)
- KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3356, phi -0.21)
- KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3356, phi -0.2)
- KXNHLAST-26NOV02CGYSJ-SJCGRAF51-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3356, phi -0.239)

portfolios: A EV +5.72 (adj +2.71) on $50.00, P(profit) 0.5688, adj growth 20.8 bp · B EV +3.19 (adj +1.76) on $33.82, P(profit) 0.5369, adj growth 15.9 bp · C EV +0.62 (adj +0.37) on $5.49, P(profit) 0.2812, adj growth 3.2 bp · R EV +0.33 (adj +0.22) on $5.00, P(profit) 0.8237, adj growth 8.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
