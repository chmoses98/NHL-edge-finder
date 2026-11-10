# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-10T00:06:43Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.18 | +10.84 | +20.84 | 0.643 | -47.75 | -67.55 | 90.25 |
| B thesis-diversified (joint) ← optimiser card | 132.41 | +24.16 | +13.52 | +16.88 | 0.629 | -50.39 | -55.29 | 117.53 |
| C best expression per thesis | 106.16 | +16.41 | +8.57 | +8.86 | 0.569 | -34.90 | -51.24 | 74.93 |
| R FUNDED research stakes | 13.00 | +1.82 | +1.22 | +0.11 | 0.713 | -6.53 | -6.53 | 0.00 |

## NYR @ EDM  ·  10000 joint draws  ·  460 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.595 / away 0.406

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_NYR_win | p_overtime | goals | shots EDM/NYR | EDM/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.120 | 0.75 | 0.25 | 0.00 | 6.04 | 32.7/21.3 | 18.9/27.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.68 | 0.32 | 0.00 | 6.07 | 27.6/27.1 | 24.3/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.69 | 0.31 | 0.00 | 9.45 | 29.0/28.4 | 23.3/21.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.50 | 0.50 | 0.49 | 5.96 | 27.4/27.0 | 23.8/24.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.097 | 0.75 | 0.25 | 0.00 | 9.38 | 34.4/22.6 | 18.2/25.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.59 | 0.41 | 0.47 | 5.94 | 32.7/21.6 | 18.4/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 11 | 0.164 | 0.149 | +0.047 | +0.033 | $8.38 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 23 | 0.283 | 0.269 | +0.041 | +0.026 | $10.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 27 | 0.388 | 0.308 | +0.104 | +0.024 | $8.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.66) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.500 | 0.452 | +0.073 | +0.025 | $12.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.74) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (21.84 vs 8.05 bp); relationships: KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26NOV09NYREDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYREDM-EDMZHYMAN18-1|yes; why: higher confidence-adjusted growth (8.05 vs 5.36 bp); relationships: KXNHLGOAL-26NOV09NYREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26NOV09NYREDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.174); KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.198); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (6.35 vs 5.79 bp); relationships: KXNHLGOAL-26NOV09NYREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.174); KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.117); failure: EDM offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV09NYREDM-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26NOV09NYREDM-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (6.35 vs 5.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.117); they share one thesis budget; relationships: KXNHLGOAL-26NOV09NYREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.198); KXNHLAST-26NOV09NYREDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.117); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5332): highest fidelity KXNHLGOAL-26NOV09NYREDM-EDMZHYMAN18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2658): highest fidelity KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.4463): highest fidelity KXNHLGOAL-26NOV09NYREDM-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV09NYREDM-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26NOV09NYREDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2658, phi -0.14)
- KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2658, phi -0.222)
- KXNHLAST-26NOV09NYREDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 34% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5332, phi -0.33)
- KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 26% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5332, phi -0.29)

portfolios: A EV +11.42 (adj +3.05) on $50.00, P(profit) 0.5504, adj growth 23.7 bp · B EV +10.56 (adj +5.01) on $40.64, P(profit) 0.5668, adj growth 43.3 bp · C EV +6.05 (adj +2.48) on $38.62, P(profit) 0.5156, adj growth 21.7 bp · R EV +1.22 (adj +0.84) on $3.00, P(profit) 0.1642, adj growth 26.5 bp

## PHI @ VAN  ·  10000 joint draws  ·  434 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_PHI_win | p_overtime | goals | shots VAN/PHI | VAN/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.54 | 0.46 | 0.00 | 6.03 | 26.3/26.4 | 23.0/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.48 | 5.9 | 25.9/26.4 | 23.2/22.5 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.090 | 0.49 | 0.51 | 0.00 | 6.0 | 20.9/30.9 | 27.2/17.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.58 | 0.42 | 0.00 | 9.3 | 27.6/27.8 | 22.1/21.1 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.48 | 0.52 | 0.46 | 5.82 | 20.7/31.4 | 28.1/17.6 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.056 | 0.62 | 0.38 | 0.00 | 5.97 | 30.4/21.0 | 18.1/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brendan Gallagher: 1+ goals YES | 11 | 0.174 | 0.157 | +0.057 | +0.040 | $9.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 74 | 0.815 | 0.794 | +0.062 | +0.041 | $20.00 | FUNDED_RESEARCH | $5 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Arshdeep Bains: 1+ goals YES | 9 | 0.126 | 0.116 | +0.030 | +0.020 | $4.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 18 | 0.228 | 0.215 | +0.037 | +0.024 | $7.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (32.25 vs 8.27 bp); relationships: KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV09PHIVAN-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (19.66 vs 5.36 bp); despite a smaller raw edge (+0.062 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PHI offense succeeds (4+ goals)
- **Arshdeep Bains: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes has the higher standalone adjusted growth (32.25 vs 9.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes has the higher standalone adjusted growth (32.25 vs 8.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3986): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.424): highest fidelity KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5325): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV09PHIVAN-PHI2|no (same contract)
- KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.204)
- KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3597, phi -0.207)
- KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.158)
- KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.217)

portfolios: A EV +8.97 (adj +5.21) on $50.00, P(profit) 0.563, adj growth 44.7 bp · B EV +9.35 (adj +6.33) on $41.77, P(profit) 0.4084, adj growth 55.1 bp · C EV +7.45 (adj +4.73) on $41.03, P(profit) 0.6747, adj growth 41.3 bp · R EV +0.41 (adj +0.27) on $5.00, P(profit) 0.8154, adj growth 10.2 bp

## NYI @ SJS  ·  10000 joint draws  ·  476 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.442 / away 0.558

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_NYI_win | p_overtime | goals | shots SJS/NYI | SJS/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.51 | 0.49 | 0.00 | 6.05 | 27.6/28.0 | 24.4/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.48 | 0.52 | 0.48 | 5.99 | 27.5/27.7 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.50 | 0.50 | 0.00 | 9.34 | 29.2/29.3 | 23.3/22.9 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.069 | 0.41 | 0.59 | 0.00 | 5.99 | 22.0/32.9 | 29.0/19.0 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.47 | 0.53 | 0.47 | 5.86 | 22.1/32.6 | 29.2/18.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.063 | 0.56 | 0.44 | 0.00 | 5.99 | 32.4/22.1 | 19.0/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 17 | 0.214 | 0.202 | +0.034 | +0.022 | $6.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 70 | 0.774 | 0.735 | +0.059 | +0.020 | $19.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Michael Misa: 1+ goals YES | 19 | 0.229 | 0.218 | +0.028 | +0.017 | $5.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Matthew Schaefer: 1+ goals NO | 76 | 0.802 | 0.790 | +0.029 | +0.018 | $19.33 | FUNDED_RESEARCH | $5 | NYI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (7.16 vs 4.05 bp); relationships: KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV09NYISJ-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (4.23 vs 0.48 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26NOV09NYISJ-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes has the higher standalone adjusted growth (7.16 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26NOV09NYISJ-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: SJS offense suppressed (<= 2 goals)
- **Matthew Schaefer: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV09NYISJ-NYI2|no; why: higher confidence-adjusted growth (3.90 vs 0.53 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3891): highest fidelity KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3924): highest fidelity KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no (same contract)
- thesis NYI:SUPPRESSED (p 0.3849): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.216)
- KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3891, phi -0.216)
- KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.225)
- KXNHLGOAL-26NOV09NYISJ-NYIMSCHAEFER48-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3974, phi -0.181)

portfolios: A EV +4.78 (adj +2.58) on $50.00, P(profit) 0.3779, adj growth 21.8 bp · B EV +4.25 (adj +2.18) on $50.00, P(profit) 0.7637, adj growth 19.2 bp · C EV +2.91 (adj +1.36) on $26.51, P(profit) 0.829, adj growth 11.9 bp · R EV +0.19 (adj +0.11) on $5.00, P(profit) 0.8022, adj growth 4.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
