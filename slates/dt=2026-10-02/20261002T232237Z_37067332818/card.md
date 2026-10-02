# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T23:22:37Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +32.48 | +10.55 | +25.61 | 0.672 | -41.12 | -62.27 | 86.35 |
| B thesis-diversified (joint) ← optimiser card | 115.66 | +26.35 | +13.30 | +18.52 | 0.640 | -37.60 | -61.42 | 115.76 |
| C best expression per thesis | 83.50 | +17.45 | +8.59 | +7.01 | 0.556 | -37.06 | -52.14 | 73.85 |
| R FUNDED research stakes | 9.00 | +1.52 | +1.01 | -1.81 | 0.338 | -9.00 | -9.00 | 0.00 |

## BOS @ WPG  ·  10000 joint draws  ·  346 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_BOS_win | p_overtime | goals | shots WPG/BOS | WPG/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.51 | 0.49 | 0.00 | 5.99 | 27.3/27.0 | 23.3/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.52 | 0.48 | 0.47 | 5.9 | 27.2/27.0 | 23.8/24.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.088 | 0.56 | 0.44 | 0.00 | 6.01 | 32.4/21.4 | 18.3/28.6 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.49 | 5.92 | 32.4/21.9 | 18.7/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 9.22 | 29.0/28.7 | 22.8/23.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.50 | 0.50 | 0.50 | 2.81 | 26.1/25.8 | 24.3/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marat Khusnutdinov: 1+ goals YES | 9 | 0.145 | 0.130 | +0.049 | +0.034 | $8.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.217 | +0.040 | +0.026 | $8.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 70 | 0.836 | 0.741 | +0.121 | +0.026 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 30 | 0.339 | 0.328 | +0.024 | +0.013 | $5.00 | FUNDED_RESEARCH | $2 | WPG:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (28.11 vs 9.75 bp); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BOS offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes has the higher standalone adjusted growth (28.11 vs 9.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: BOS offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (7.51 vs 1.09 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: BOS offense succeeds (4+ goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-WPGGVILARDI13-1|yes; why: Player prop expression KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes selected over player prop KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.50 vs 0.25 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BOS:OFFENSE_4PLUS (p 0.3523): highest fidelity KXNHLAST-26OCT02BOSWPG-BOSELINDHOLM28-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4201): highest fidelity KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no (same contract)
- KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.189)
- KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.222)
- KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.6 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3523, phi -0.186)
- KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4128, phi -0.279)
- override: Player prop expression KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes selected over player prop KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.50 vs 0.25 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +12.42 (adj +4.72) on $50.00, P(profit) 0.3772, adj growth 38.0 bp · B EV +9.72 (adj +5.01) on $41.46, P(profit) 0.5416, adj growth 43.4 bp · C EV +4.85 (adj +3.26) on $20.42, P(profit) 0.3414, adj growth 27.7 bp · R EV +0.15 (adj +0.08) on $2.00, P(profit) 0.3387, adj growth 2.6 bp

## STL @ DAL  ·  10000 joint draws  ·  334 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.623 / away 0.378

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_STL_win | p_overtime | goals | shots DAL/STL | DAL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.55 | 0.45 | 0.00 | 5.98 | 25.9/25.6 | 22.4/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.47 | 5.95 | 26.0/25.8 | 22.6/22.6 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.093 | 0.61 | 0.39 | 0.00 | 6.0 | 30.9/20.4 | 17.5/26.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.57 | 0.43 | 0.00 | 9.21 | 27.7/27.6 | 22.1/21.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.50 | 5.92 | 31.0/20.5 | 17.4/27.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.057 | 0.63 | 0.37 | 0.00 | 9.21 | 32.3/21.7 | 16.9/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 11 | 0.158 | 0.145 | +0.041 | +0.028 | $6.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 68 | 0.738 | 0.723 | +0.043 | +0.027 | $18.26 | FUNDED_RESEARCH | $5 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 74 | 0.874 | 0.777 | +0.121 | +0.024 | $18.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Dylan Holloway: 1+ goals YES | 26 | 0.312 | 0.298 | +0.039 | +0.025 | $7.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: higher confidence-adjusted growth (16.36 vs 8.37 bp); despite a smaller raw edge (+0.041 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: STL offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (8.37 vs 7.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.190); relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: DAL offense succeeds (4+ goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02STLDAL-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (6.72 vs 0.26 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: STL offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes has the higher standalone adjusted growth (16.36 vs 6.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.3441): highest fidelity KXNHLTEAMTOTAL-26OCT02STLDAL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3803): highest fidelity KXNHLSPREAD-26OCT02STLDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4586): highest fidelity KXNHLGAME-26OCT02STLDAL-STL|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes (same contract)
- KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.208)
- KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4013, phi -0.231)
- KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3441, phi -0.177)
- KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.266)

portfolios: A EV +7.63 (adj +2.16) on $50.00, P(profit) 0.6178, adj growth 18.8 bp · B EV +7.34 (adj +3.47) on $50.00, P(profit) 0.7901, adj growth 31.1 bp · C EV +4.17 (adj +2.36) on $16.37, P(profit) 0.5167, adj growth 20.3 bp · R EV +0.31 (adj +0.20) on $5.00, P(profit) 0.7383, adj growth 7.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  358 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.645 / away 0.355

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.66 | 0.34 | 0.00 | 6.03 | 28.1/28.2 | 25.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.50 | 5.97 | 28.0/28.1 | 24.8/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.66 | 0.34 | 0.00 | 9.35 | 29.5/29.6 | 24.3/22.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.62 | 0.38 | 0.00 | 6.04 | 22.5/33.4 | 30.2/18.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.48 | 0.52 | 0.47 | 5.9 | 22.5/33.5 | 30.2/19.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.061 | 0.70 | 0.30 | 0.00 | 6.02 | 32.6/22.3 | 19.7/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 7 | 0.114 | 0.102 | +0.040 | +0.027 | $6.11 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 18 | 0.233 | 0.218 | +0.043 | +0.028 | $8.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ assists YES | 23 | 0.363 | 0.270 | +0.121 | +0.028 | $6.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Judd Caulfield: 1+ goals YES | 8 | 0.109 | 0.101 | +0.024 | +0.016 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.68 vs 11.06 bp); despite a smaller raw edge (+0.040 vs +0.043/contract); relationships: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.029); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (11.06 vs 9.14 bp); despite a smaller raw edge (+0.043 vs +0.121/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (11.06 vs 9.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (11.06 vs 6.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3325): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4029): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3145): highest fidelity KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT02ANAVGK-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.176)
- KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.241)
- KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.292)
- KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.166)

portfolios: A EV +12.42 (adj +3.67) on $50.00, P(profit) 0.6689, adj growth 29.6 bp · B EV +9.28 (adj +4.82) on $24.20, P(profit) 0.6009, adj growth 41.2 bp · C EV +8.43 (adj +2.97) on $46.71, P(profit) 0.4726, adj growth 25.8 bp · R EV +1.06 (adj +0.73) on $2.00, P(profit) 0.1141, adj growth 23.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02ANAVGK-VGK|no == KXNHLGAME-26OCT02ANAVGK-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
