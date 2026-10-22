# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T23:42:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +24.17 | +5.67 | +24.84 | 0.730 | -26.31 | -40.85 | 49.01 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +24.98 | +15.70 | +20.78 | 0.667 | -37.98 | -49.82 | 144.18 |
| C best expression per thesis | 150.00 | +21.49 | +10.51 | +18.76 | 0.653 | -37.75 | -50.37 | 94.06 |
| R FUNDED research stakes | 20.00 | +2.15 | +1.35 | +1.19 | 0.583 | -6.99 | -9.35 | 0.00 |

## VGK @ STL  ·  10000 joint draws  ·  502 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.468 / away 0.532

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_VGK_win | p_overtime | goals | shots STL/VGK | STL/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 6.03 | 26.7/27.1 | 23.7/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.91 | 26.6/26.8 | 23.6/23.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.090 | 0.39 | 0.61 | 0.00 | 6.01 | 21.0/31.6 | 27.5/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.52 | 0.48 | 0.00 | 9.27 | 28.3/28.5 | 22.7/22.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.43 | 0.57 | 0.48 | 5.93 | 20.9/31.7 | 28.3/17.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.057 | 0.38 | 0.62 | 0.00 | 9.23 | 22.8/33.7 | 26.3/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 22 | 0.273 | 0.257 | +0.041 | +0.025 | $4.70 | FUNDED_RESEARCH | $2 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Raphael Lavoie: 1+ goals YES | 9 | 0.123 | 0.108 | +0.027 | +0.013 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| William Karlsson: 1+ assists NO | 73 | 0.806 | 0.761 | +0.062 | +0.017 | $11.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Ivan Barbashev: 1+ goals YES | 21 | 0.244 | 0.234 | +0.022 | +0.013 | $2.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22VGKSTL-STLPBROBERG6-1|yes; why: higher confidence-adjusted growth (7.66 vs 3.01 bp); despite a smaller raw edge (+0.041 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22VGKSTL-VGKRLAVOIE36-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT22VGKSTL-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: STL offense suppressed (<= 2 goals)
- **Raphael Lavoie: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22VGKSTL-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (3.87 vs 2.04 bp); relationships: KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT22VGKSTL-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense suppressed (<= 2 goals)
- **William Karlsson: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no; why: higher confidence-adjusted growth (3.24 vs 2.07 bp); relationships: KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT22VGKSTL-VGKRLAVOIE36-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT22VGKSTL-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: VGK offense succeeds (4+ goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22VGKSTL-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (2.04 vs 0.66 bp); despite a smaller raw edge (+0.022 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22VGKSTL-VGKRLAVOIE36-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.3829): highest fidelity KXNHLAST-26OCT22VGKSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3956): highest fidelity KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3895): highest fidelity KXNHLGOAL-26OCT22VGKSTL-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22VGKSTL-VGKIBARBASHEV49-1|yes (same contract)
- KXNHLGOAL-26OCT22VGKSTL-STLRTHOMAS18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4071, phi -0.235)
- KXNHLGOAL-26OCT22VGKSTL-VGKRLAVOIE36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3956, phi -0.152)
- KXNHLAST-26OCT22VGKSTL-VGKWKARLSSON71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3895, phi -0.216)
- KXNHLGOAL-26OCT22VGKSTL-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3956, phi -0.221)

portfolios: A EV +3.23 (adj +1.18) on $25.00, P(profit) 0.5063, adj growth 10.6 bp · B EV +2.63 (adj +1.17) on $21.15, P(profit) 0.4375, adj growth 10.8 bp · C EV +2.75 (adj +1.22) on $25.15, P(profit) 0.4084, adj growth 11.0 bp · R EV +0.35 (adj +0.22) on $2.00, P(profit) 0.2728, adj growth 7.5 bp

## WPG @ DAL  ·  10000 joint draws  ·  510 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.643 / away 0.357

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.64 | 0.36 | 0.00 | 6.04 | 26.0/25.9 | 23.0/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.50 | 0.50 | 0.46 | 5.9 | 26.1/25.9 | 22.7/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.097 | 0.72 | 0.28 | 0.00 | 5.93 | 30.8/20.3 | 17.8/26.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.55 | 0.45 | 0.43 | 5.86 | 31.0/20.4 | 17.4/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.62 | 0.38 | 0.00 | 9.19 | 27.6/27.1 | 21.8/21.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 3.45 | 24.6/24.7 | 22.9/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dylan Samberg: 1+ goals YES | 3 | 0.054 | 0.048 | +0.022 | +0.016 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 22 | 0.266 | 0.253 | +0.034 | +0.021 | $4.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.164 | 0.154 | +0.026 | +0.016 | $2.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 66 | 0.711 | 0.697 | +0.035 | +0.021 | $10.44 | FUNDED_RESEARCH | $3 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (17.65 vs 5.30 bp); despite a smaller raw edge (+0.022 vs +0.034/contract); relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT22WPGDAL-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: WPG offense suppressed (<= 2 goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (5.30 vs 1.88 bp); despite a smaller raw edge (+0.034 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT22WPGDAL-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes has the higher standalone adjusted growth (5.30 vs 4.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: WPG offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22WPGDAL-DALTSEGUIN91-1|no; why: higher confidence-adjusted growth (4.58 vs 2.90 bp); despite a smaller raw edge (+0.035 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT22WPGDAL-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2888): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3693): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4421): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.106)
- KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.28)
- KXNHLGOAL-26OCT22WPGDAL-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4924, phi -0.203)
- KXNHLGOAL-26OCT22WPGDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4169, phi -0.242)

portfolios: A EV +1.69 (adj +0.56) on $25.00, P(profit) 0.6884, adj growth 5.1 bp · B EV +3.20 (adj +2.15) on $19.51, P(profit) 0.3581, adj growth 19.5 bp · C EV +1.78 (adj +0.98) on $23.87, P(profit) 0.6584, adj growth 8.8 bp · R EV +0.16 (adj +0.09) on $3.00, P(profit) 0.7111, adj growth 3.5 bp

## MIN @ CGY  ·  10000 joint draws  ·  438 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.357 / away 0.643

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
| Aydar Suniev: 1+ goals YES | 17 | 0.221 | 0.206 | +0.042 | +0.026 | $4.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 2+ goals NO | 87 | 0.914 | 0.899 | +0.036 | +0.021 | $11.87 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 10 | 0.141 | 0.125 | +0.034 | +0.019 | $2.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ben Jones: 1+ goals NO | 87 | 0.909 | 0.897 | +0.031 | +0.019 | $11.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN3|no; why: higher confidence-adjusted growth (10.02 vs 8.32 bp); despite a smaller raw edge (+0.042 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CGY offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no; why: Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.99 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: MIN offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes has the higher standalone adjusted growth (10.02 vs 8.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: CGY offense suppressed (<= 2 goals)
- **Ben Jones: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22MINCGY-CGYBJONES39-1|no; why: higher confidence-adjusted growth (7.36 vs 1.27 bp); despite a smaller raw edge (+0.031 vs +0.107/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CGY offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CGY:OFFENSE_4PLUS (p 0.3347): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3925): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no — Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.99 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CGY:WINS (p 0.4589): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22MINCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4473, phi -0.228)
- KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3999, phi -0.246)
- KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4473, phi -0.173)
- KXNHLGOAL-26OCT22MINCGY-CGYBJONES39-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3347, phi -0.146)
- override: Player prop expression KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-2|no selected over broad KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.99 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.22 (adj +0.80) on $25.00, P(profit) 0.62, adj growth 6.7 bp · B EV +2.81 (adj +1.68) on $30.87, P(profit) 0.3273, adj growth 15.7 bp · C EV +5.38 (adj +2.13) on $39.05, P(profit) 0.5101, adj growth 19.2 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.9142, adj growth 2.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22MINCGY-MIN|no == KXNHLGAME-26OCT22MINCGY-CGY|yes

## CAR @ EDM  ·  10000 joint draws  ·  442 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.460 / away 0.540

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
| Alex Formenton: 1+ goals YES | 12 | 0.185 | 0.168 | +0.058 | +0.040 | $6.17 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 7 | 0.111 | 0.100 | +0.036 | +0.025 | $3.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 24 | 0.290 | 0.276 | +0.037 | +0.023 | $4.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 79 | 0.856 | 0.821 | +0.055 | +0.019 | $10.42 | FUNDED_RESEARCH | $3 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
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

portfolios: A EV +4.17 (adj +1.30) on $25.00, P(profit) 0.5164, adj growth 11.6 bp · B EV +5.83 (adj +3.75) on $24.30, P(profit) 0.4638, adj growth 34.1 bp · C EV +2.50 (adj +0.85) on $22.25, P(profit) 0.7691, adj growth 7.8 bp · R EV +1.11 (adj +0.71) on $5.00, P(profit) 0.1854, adj growth 25.1 bp

## UTA @ SEA  ·  10000 joint draws  ·  458 bet sides mapped, 19 +EV candidates, 4 on card

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
| Shane Wright: 1+ goals YES | 15 | 0.205 | 0.190 | +0.046 | +0.031 | $5.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.020 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.700 | 0.683 | +0.044 | +0.027 | $12.35 | FUNDED_RESEARCH | $4 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 18 | 0.218 | 0.207 | +0.028 | +0.017 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22UTASEA-SEA3|yes; why: higher confidence-adjusted growth (15.74 vs 6.22 bp); despite a smaller raw edge (+0.046 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.897 vs 0.464); relationships: KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22UTASEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (15.74 vs 8.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22UTASEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22UTASEA-SEA3|yes; why: higher confidence-adjusted growth (7.31 vs 6.22 bp); despite a smaller raw edge (+0.044 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.012 vs 0.464); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22UTASEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: UTA offense succeeds (4+ goals)
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (15.74 vs 4.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4001): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3607): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2807): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.222)
- KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.169)
- KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4242, phi -0.25)
- KXNHLGOAL-26OCT22UTASEA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.196)

portfolios: A EV +4.82 (adj +0.87) on $25.00, P(profit) 0.5952, adj growth 6.8 bp · B EV +3.65 (adj +2.38) on $23.75, P(profit) 0.4139, adj growth 21.8 bp · C EV +3.80 (adj +2.26) on $24.24, P(profit) 0.3041, adj growth 20.2 bp · R EV +0.27 (adj +0.17) on $4.00, P(profit) 0.6997, adj growth 6.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  442 bet sides mapped, 22 +EV candidates, 4 on card

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
| Filip Chytil: 1+ goals YES | 19 | 0.270 | 0.248 | +0.069 | +0.047 | $7.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.259 | 0.241 | +0.059 | +0.040 | $6.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 11 | 0.165 | 0.147 | +0.048 | +0.030 | $4.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Moritz Seider: 1+ goals NO | 85 | 0.898 | 0.885 | +0.040 | +0.026 | $11.91 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (29.27 vs 21.39 bp); relationships: KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22DETVAN-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (29.27 vs 21.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22DETVAN-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (29.27 vs 19.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22DETVAN-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: higher confidence-adjusted growth (12.63 vs 11.25 bp); despite a smaller raw edge (+0.040 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.006 vs 0.534); relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4129): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5383): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.246)
- KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.215)
- KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.177)
- KXNHLGOAL-26OCT22DETVAN-DETMSEIDER53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.358, phi -0.139)

portfolios: A EV +5.04 (adj +0.96) on $25.00, P(profit) 0.6508, adj growth 8.2 bp · B EV +6.87 (adj +4.57) on $30.43, P(profit) 0.5488, adj growth 42.3 bp · C EV +5.28 (adj +3.07) on $15.44, P(profit) 0.458, adj growth 27.2 bp · R EV +0.14 (adj +0.09) on $3.00, P(profit) 0.8985, adj growth 3.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
