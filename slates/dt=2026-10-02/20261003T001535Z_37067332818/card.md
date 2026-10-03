# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T00:15:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +20.89 | +6.14 | +16.19 | 0.678 | -34.86 | -44.57 | 51.61 |
| B thesis-diversified (joint) ← optimiser card | 68.97 | +17.09 | +9.20 | +9.38 | 0.613 | -40.20 | -53.18 | 79.23 |
| C best expression per thesis | 62.91 | +13.15 | +4.82 | +14.54 | 0.563 | -25.01 | -39.36 | 42.11 |
| R FUNDED research stakes | 9.00 | +1.74 | +1.08 | -1.81 | 0.449 | -9.00 | -9.00 | 0.00 |

## STL @ DAL  ·  10000 joint draws  ·  334 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.620 / away 0.380

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
| Pius Suter: 1+ goals YES | 11 | 0.158 | 0.145 | +0.041 | +0.028 | $6.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Dallas wins NO | 37 | 0.459 | 0.416 | +0.072 | +0.030 | $6.10 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Mikko Rantanen: 1+ goals NO | 68 | 0.738 | 0.723 | +0.043 | +0.027 | $20.00 | FUNDED_RESEARCH | $5 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 26 | 0.312 | 0.298 | +0.039 | +0.025 | $6.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: higher confidence-adjusted growth (16.36 vs 8.37 bp); despite a smaller raw edge (+0.041 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: STL offense suppressed (<= 2 goals)
- **Dallas wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-STL|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: REINFORCING (phi 0.152); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.19); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: REINFORCING (phi 0.182); failure: DAL wins (incl. OT/SO)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no; why: KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no has the higher standalone adjusted growth (9.34 vs 7.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.006); relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGAME-26OCT02STLDAL-DAL|no: REINFORCING (phi 0.19); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: DAL offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes has the higher standalone adjusted growth (16.36 vs 6.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGAME-26OCT02STLDAL-DAL|no: REINFORCING (phi 0.182); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.3441): highest fidelity KXNHLTEAMTOTAL-26OCT02STLDAL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3803): highest fidelity KXNHLSPREAD-26OCT02STLDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4586): highest fidelity KXNHLGAME-26OCT02STLDAL-STL|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes (same contract)
- KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.208)
- KXNHLGAME-26OCT02STLDAL-DAL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.5414, phi -1.0)
- KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4013, phi -0.231)
- KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.266)

portfolios: A EV +7.45 (adj +1.89) on $50.00, P(profit) 0.7108, adj growth 16.6 bp · B EV +5.76 (adj +3.51) on $39.77, P(profit) 0.5528, adj growth 30.4 bp · C EV +5.46 (adj +2.85) on $35.55, P(profit) 0.5025, adj growth 25.0 bp · R EV +0.68 (adj +0.35) on $7.00, P(profit) 0.7383, adj growth 12.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  358 bet sides mapped, 12 +EV candidates, 4 on card

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
| Tim Washe: 1+ goals YES | 7 | 0.114 | 0.102 | +0.040 | +0.027 | $6.14 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ assists YES | 22 | 0.363 | 0.267 | +0.132 | +0.035 | $8.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Alex Killorn: 1+ goals YES | 18 | 0.233 | 0.218 | +0.043 | +0.028 | $8.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 15 | 0.195 | 0.183 | +0.036 | +0.024 | $6.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.68 vs 14.82 bp); despite a smaller raw edge (+0.040 vs +0.132/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (14.82 vs 11.06 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (14.82 vs 11.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (9.14 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3325): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [DIRECT], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4029): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3145): highest fidelity KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4|no (same contract)
- KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.176)
- KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.292)
- KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.241)
- KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3145, phi -0.174)

portfolios: A EV +13.44 (adj +4.25) on $50.00, P(profit) 0.6689, adj growth 35.0 bp · B EV +11.33 (adj +5.69) on $29.20, P(profit) 0.6464, adj growth 48.8 bp · C EV +7.69 (adj +1.97) on $27.36, P(profit) 0.5964, adj growth 17.1 bp · R EV +1.06 (adj +0.73) on $2.00, P(profit) 0.1141, adj growth 23.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02ANAVGK-VGK|no == KXNHLGAME-26OCT02ANAVGK-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
