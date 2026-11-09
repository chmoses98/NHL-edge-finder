# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-09T21:33:27Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +28.39 | +12.06 | +24.04 | 0.632 | -53.83 | -70.64 | 99.17 |
| B thesis-diversified (joint) ← optimiser card | 137.49 | +25.18 | +15.37 | +17.69 | 0.612 | -50.86 | -71.23 | 133.86 |
| C best expression per thesis | 113.12 | +16.66 | +9.48 | +11.13 | 0.578 | -40.75 | -55.98 | 82.97 |
| R FUNDED research stakes | 13.00 | +1.46 | +0.97 | +0.81 | 0.695 | -6.28 | -6.28 | 0.00 |

## NYR @ EDM  ·  10000 joint draws  ·  460 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.595 / away 0.406

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_NYR_win | p_overtime | goals | shots EDM/NYR | EDM/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.121 | 0.75 | 0.25 | 0.00 | 6.03 | 32.8/21.4 | 19.0/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.68 | 0.32 | 0.00 | 6.08 | 27.4/27.0 | 24.2/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.68 | 0.32 | 0.00 | 9.48 | 29.2/28.6 | 23.4/22.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.098 | 0.76 | 0.24 | 0.00 | 9.37 | 34.3/22.5 | 18.2/25.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.49 | 0.51 | 0.49 | 5.98 | 27.4/27.0 | 23.8/24.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.60 | 0.40 | 0.47 | 5.93 | 32.6/21.6 | 18.5/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 11 | 0.164 | 0.147 | +0.047 | +0.030 | $7.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 23 | 0.283 | 0.269 | +0.041 | +0.026 | $9.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 69 | 0.744 | 0.729 | +0.038 | +0.024 | $19.59 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.500 | 0.452 | +0.073 | +0.025 | $13.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.74) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (18.65 vs 8.05 bp); relationships: KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV09NYREDM-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYREDM-EDMZHYMAN18-1|yes; why: higher confidence-adjusted growth (8.05 vs 2.34 bp); relationships: KXNHLGOAL-26NOV09NYREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV09NYREDM-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.198); failure: EDM offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV09NYREDM-NYROBJORKSTRAND28-1|no; why: higher confidence-adjusted growth (6.04 vs 0.34 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV09NYREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: NYR offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV09NYREDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (5.79 vs 3.14 bp); despite a smaller raw edge (+0.073 vs +0.094/contract); relationships: KXNHLGOAL-26NOV09NYREDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.198); KXNHLGOAL-26NOV09NYREDM-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5332): highest fidelity KXNHLGOAL-26NOV09NYREDM-EDMZHYMAN18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.4463): highest fidelity KXNHLGOAL-26NOV09NYREDM-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV09NYREDM-NYRPDOROFEYEV16-1|no (same contract)
- thesis EDM:SUPPRESSED (p 0.2658): highest fidelity KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no (same contract)
- KXNHLGOAL-26NOV09NYREDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2658, phi -0.14)
- KXNHLGOAL-26NOV09NYREDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2658, phi -0.222)
- KXNHLGOAL-26NOV09NYREDM-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.333, phi -0.233)
- KXNHLAST-26NOV09NYREDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 26% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5332, phi -0.29)

portfolios: A EV +13.09 (adj +5.43) on $50.00, P(profit) 0.5519, adj growth 44.2 bp · B EV +7.95 (adj +4.38) on $50.00, P(profit) 0.6127, adj growth 38.1 bp · C EV +5.08 (adj +2.55) on $43.55, P(profit) 0.5355, adj growth 22.3 bp · R EV +0.27 (adj +0.17) on $5.00, P(profit) 0.7435, adj growth 6.0 bp

## PHI @ VAN  ·  10000 joint draws  ·  434 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.447 / away 0.553

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_PHI_win | p_overtime | goals | shots VAN/PHI | VAN/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.54 | 0.46 | 0.00 | 6.04 | 26.1/26.3 | 23.0/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.46 | 5.89 | 25.9/26.2 | 23.0/22.6 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.086 | 0.48 | 0.52 | 0.00 | 6.0 | 20.8/31.1 | 27.3/17.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 9.32 | 27.4/27.8 | 22.1/20.9 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.50 | 0.50 | 0.48 | 5.81 | 20.6/31.0 | 27.7/17.5 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 5.97 | 30.4/21.0 | 18.2/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brendan Gallagher: 1+ goals YES | 11 | 0.174 | 0.157 | +0.057 | +0.040 | $9.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 73 | 0.811 | 0.789 | +0.067 | +0.046 | $20.00 | FUNDED_RESEARCH | $5 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.228 | 0.212 | +0.048 | +0.032 | $9.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Arshdeep Bains: 1+ goals YES | 9 | 0.126 | 0.116 | +0.030 | +0.020 | $4.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (32.25 vs 15.15 bp); relationships: KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: VAN offense suppressed (<= 2 goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV09PHIVAN-PHI2|no; why: higher confidence-adjusted growth (24.32 vs 5.14 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: PHI offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes has the higher standalone adjusted growth (32.25 vs 15.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)
- **Arshdeep Bains: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes has the higher standalone adjusted growth (32.25 vs 9.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3986): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.424): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5325): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV09PHIVAN-PHI2|no (same contract)
- KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.204)
- KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3597, phi -0.207)
- KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.217)
- KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.158)

portfolios: A EV +7.07 (adj +1.77) on $50.00, P(profit) 0.6367, adj growth 14.7 bp · B EV +10.55 (adj +7.21) on $43.82, P(profit) 0.4407, adj growth 62.8 bp · C EV +7.60 (adj +4.88) on $40.94, P(profit) 0.6727, adj growth 42.8 bp · R EV +0.45 (adj +0.31) on $5.00, P(profit) 0.811, adj growth 11.7 bp

## NYI @ SJS  ·  10000 joint draws  ·  438 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.440 / away 0.560

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_NYI_win | p_overtime | goals | shots SJS/NYI | SJS/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.52 | 0.48 | 0.00 | 6.03 | 27.6/27.8 | 24.2/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.47 | 5.96 | 27.6/27.8 | 24.4/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.50 | 0.50 | 0.00 | 9.38 | 29.3/29.5 | 23.5/23.2 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.071 | 0.40 | 0.60 | 0.00 | 6.01 | 22.1/32.9 | 28.9/19.1 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.47 | 0.53 | 0.47 | 5.88 | 22.0/32.8 | 29.4/18.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.063 | 0.57 | 0.43 | 0.00 | 6.02 | 32.5/22.2 | 19.1/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 17 | 0.224 | 0.209 | +0.044 | +0.029 | $8.57 | FUNDED_RESEARCH | $3 | SJS:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 19 | 0.240 | 0.227 | +0.040 | +0.026 | $7.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 21 | 0.257 | 0.244 | +0.035 | +0.022 | $7.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 68 | 0.760 | 0.718 | +0.065 | +0.022 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (12.41 vs 9.01 bp); relationships: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); failure: SJS offense suppressed (<= 2 goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes has the higher standalone adjusted growth (12.41 vs 9.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes has the higher standalone adjusted growth (12.41 vs 6.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV09NYISJ-SJISTENBERG41-2|no; why: higher confidence-adjusted growth (5.26 vs 0.03 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0014 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3891): highest fidelity KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3924): highest fidelity KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no (same contract)
- thesis NYI:SUPPRESSED (p 0.3849): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.214)
- KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.223)
- KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.223)
- KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3891, phi -0.214)

portfolios: A EV +8.22 (adj +4.86) on $50.00, P(profit) 0.5221, adj growth 40.2 bp · B EV +6.68 (adj +3.78) on $43.67, P(profit) 0.4875, adj growth 33.0 bp · C EV +3.98 (adj +2.05) on $28.63, P(profit) 0.8231, adj growth 17.8 bp · R EV +0.73 (adj +0.49) on $3.00, P(profit) 0.2237, adj growth 15.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
