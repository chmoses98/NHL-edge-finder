# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T02:25:33Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.36 | +10.31 | +25.99 | 0.658 | -57.77 | -83.45 | 78.48 |
| B thesis-diversified (joint) ← optimiser card | 120.31 | +24.17 | +15.21 | +11.57 | 0.606 | -50.42 | -64.38 | 130.70 |
| C best expression per thesis | 89.64 | +15.36 | +7.94 | +14.35 | 0.612 | -43.60 | -52.43 | 69.04 |
| R FUNDED research stakes | 14.00 | +3.16 | +2.09 | -3.00 | 0.438 | -7.98 | -10.95 | 0.00 |

## UTA @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.543 / away 0.457

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_UTA_win | p_overtime | goals | shots VGK/UTA | VGK/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 5.99 | 27.2/27.1 | 24.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.56 | 0.44 | 0.45 | 5.96 | 27.2/27.2 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.61 | 0.39 | 0.00 | 9.32 | 28.7/28.8 | 23.2/21.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.077 | 0.66 | 0.34 | 0.00 | 5.99 | 31.9/21.5 | 18.8/27.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.52 | 0.48 | 0.45 | 5.88 | 31.7/21.4 | 18.1/28.4 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.064 | 0.56 | 0.44 | 0.00 | 6.04 | 21.9/32.0 | 28.4/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 4 | 0.085 | 0.072 | +0.042 | +0.030 | $6.00 | FUNDED_RESEARCH | $2 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 16 | 0.221 | 0.205 | +0.052 | +0.035 | $9.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $6.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 17 | 0.221 | 0.206 | +0.041 | +0.026 | $7.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (44.18 vs 19.02 bp); despite a smaller raw edge (+0.042 vs +0.052/contract); relationships: KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11UTAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV11UTAVGK-VGKBMCNABB3-1|yes; why: higher confidence-adjusted growth (19.02 vs 7.17 bp); despite a smaller raw edge (+0.052 vs +0.104/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11UTAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes has the higher standalone adjusted growth (19.02 vs 13.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.019); they share one thesis budget; relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: VGK offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV11UTAVGK-UTAMWEEGAR52-1|yes; why: higher confidence-adjusted growth (9.68 vs 2.54 bp); despite a smaller raw edge (+0.041 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11UTAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VGK:OFFENSE_4PLUS (p 0.4529): highest fidelity KXNHLAST-26NOV11UTAVGK-VGKSTHEODORE27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3447): highest fidelity KXNHLAST-26NOV11UTAVGK-UTAMWEEGAR52-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3378, phi -0.125)
- KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3378, phi -0.192)
- KXNHLGOAL-26NOV11UTAVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3378, phi -0.163)
- KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4316, phi -0.248)

portfolios: A EV +14.82 (adj +5.09) on $50.00, P(profit) 0.5017, adj growth 37.0 bp · B EV +12.71 (adj +8.68) on $29.95, P(profit) 0.5386, adj growth 73.4 bp · C EV +4.68 (adj +3.10) on $17.14, P(profit) 0.393, adj growth 26.7 bp · R EV +1.98 (adj +1.40) on $2.00, P(profit) 0.085, adj growth 43.4 bp

## NSH @ ANA  ·  10000 joint draws  ·  474 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_NSH_win | p_overtime | goals | shots ANA/NSH | ANA/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.74 | 0.26 | 0.00 | 9.46 | 30.0/29.4 | 24.6/22.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.71 | 0.29 | 0.00 | 6.13 | 28.3/28.0 | 25.4/23.6 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.111 | 0.79 | 0.21 | 0.00 | 6.06 | 33.9/22.0 | 19.8/28.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.109 | 0.81 | 0.19 | 0.00 | 9.4 | 35.6/23.5 | 19.5/26.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.58 | 0.42 | 0.47 | 5.98 | 34.3/22.2 | 19.0/30.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.51 | 0.49 | 0.46 | 6.04 | 28.3/27.8 | 24.5/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Beckett Sennecke: 1+ goals YES | 33 | 0.413 | 0.391 | +0.067 | +0.045 | $15.47 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 11 | 0.157 | 0.144 | +0.040 | +0.027 | $6.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 18 | 0.235 | 0.220 | +0.045 | +0.030 | $8.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 62 | 0.689 | 0.669 | +0.053 | +0.033 | $19.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (19.84 vs 10.75 bp); relationships: KXNHLGOAL-26NOV11NSHANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV11NSHANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.031); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes has the higher standalone adjusted growth (19.84 vs 15.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV11NSHANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes has the higher standalone adjusted growth (19.84 vs 12.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV11NSHANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV11NSHANA-ANA3|yes; why: higher confidence-adjusted growth (10.24 vs 6.07 bp); despite a smaller raw edge (+0.053 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.465); relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.031); KXNHLGOAL-26NOV11NSHANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV11NSHANA-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.5711): highest fidelity KXNHLSPREAD-26NOV11NSHANA-NSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:SUPPRESSED (p 0.4555): highest fidelity KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.453): highest fidelity KXNHLSPREAD-26NOV11NSHANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV11NSHANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.24)
- KXNHLGOAL-26NOV11NSHANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.157)
- KXNHLGOAL-26NOV11NSHANA-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.179)
- KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3175, phi -0.253)

portfolios: A EV +8.16 (adj +3.12) on $50.00, P(profit) 0.5812, adj growth 24.7 bp · B EV +8.73 (adj +5.79) on $49.42, P(profit) 0.5076, adj growth 50.8 bp · C EV +5.70 (adj +3.42) on $39.41, P(profit) 0.5346, adj growth 29.9 bp · R EV +0.78 (adj +0.53) on $4.00, P(profit) 0.4129, adj growth 18.4 bp

## PIT @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.429 / away 0.571

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_PIT_win | p_overtime | goals | shots SJS/PIT | SJS/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.49 | 0.51 | 0.00 | 6.03 | 27.4/27.6 | 23.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.48 | 0.52 | 0.47 | 5.95 | 27.7/28.0 | 24.6/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.49 | 0.51 | 0.00 | 9.37 | 29.2/29.3 | 22.9/23.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.39 | 0.61 | 0.00 | 6.06 | 22.0/32.5 | 28.2/19.1 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.47 | 0.53 | 0.46 | 5.91 | 22.3/33.1 | 29.6/19.1 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.057 | 0.43 | 0.57 | 0.00 | 9.23 | 23.3/34.7 | 27.9/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Erik Karlsson: 1+ goals NO | 82 | 0.855 | 0.845 | +0.025 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | PIT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Pittsburgh over 3.5 goals scored NO | 50 | 0.569 | 0.532 | +0.051 | +0.015 | $3.12 | FUNDED_RESEARCH | $1 | PIT:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals NO | 64 | 0.703 | 0.669 | +0.047 | +0.013 | $7.33 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Alexander Wennberg: 1+ assists NO | 67 | 0.771 | 0.696 | +0.085 | +0.010 | $10.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Erik Karlsson: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no has the higher standalone adjusted growth (4.84 vs 3.47 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.123); relationships: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.176); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh over 3.5 goals scored NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: REINFORCING (phi 0.176); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: REINFORCING (phi 0.531); KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT3|no; why: Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.531); KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: PIT wins by 2+
- **Alexander Wennberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV11PITSJ-7|no; why: higher confidence-adjusted growth (1.03 vs 0.93 bp); wins across more scripts (relative breadth 1.007 vs 0.739); relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4037): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [DIRECT], best adjusted EV KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes — Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PIT:SUPPRESSED (p 0.3636): highest fidelity KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no — Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:WINS (p 0.4876): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.175)
- KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.978)
- KXNHLSPREAD-26NOV11PITSJ-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2971, phi -1.0)
- KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4037, phi -0.221)
- override: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.38 (adj +2.10) on $50.00, P(profit) 0.5315, adj growth 16.8 bp · B EV +2.74 (adj +0.74) on $40.94, P(profit) 0.6164, adj growth 6.5 bp · C EV +4.98 (adj +1.42) on $33.09, P(profit) 0.6398, adj growth 12.4 bp · R EV +0.39 (adj +0.16) on $8.00, P(profit) 0.6193, adj growth 5.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
