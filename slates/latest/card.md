# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T19:33:17Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +29.60 | +10.61 | +28.28 | 0.741 | -26.50 | -41.06 | 96.39 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +30.88 | +17.55 | +27.91 | 0.729 | -29.35 | -44.12 | 163.76 |
| C best expression per thesis | 149.99 | +27.18 | +12.72 | +25.05 | 0.698 | -34.17 | -49.71 | 115.22 |
| R FUNDED research stakes | 19.00 | +2.71 | +1.44 | +1.65 | 0.612 | -6.82 | -8.32 | 0.00 |

## NYR @ SEA  ·  10000 joint draws  ·  450 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.450 / away 0.550

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_NYR_win | p_overtime | goals | shots SEA/NYR | SEA/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 6.04 | 27.5/27.4 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.94 | 27.5/27.5 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.57 | 0.43 | 0.00 | 9.45 | 29.0/28.9 | 23.1/22.3 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.071 | 0.62 | 0.38 | 0.00 | 6.02 | 32.0/21.7 | 18.9/27.4 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.068 | 0.50 | 0.50 | 0.00 | 5.99 | 21.8/32.1 | 28.4/18.5 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.55 | 0.45 | 0.49 | 5.91 | 32.1/21.9 | 18.7/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 10 | 0.150 | 0.136 | +0.044 | +0.030 | $3.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 11 | 0.153 | 0.140 | +0.037 | +0.023 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 15 | 0.194 | 0.181 | +0.035 | +0.023 | $3.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.712 | 0.696 | +0.036 | +0.020 | $7.68 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: higher confidence-adjusted growth (20.17 vs 7.95 bp); despite a smaller raw edge (+0.044 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV07NYRSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: higher confidence-adjusted growth (11.25 vs 7.95 bp); despite a smaller raw edge (+0.037 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV07NYRSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: SEA offense suppressed (<= 2 goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: higher confidence-adjusted growth (8.25 vs 7.95 bp); despite a smaller raw edge (+0.035 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (7.95 vs 4.18 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV07NYRSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5415): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3233): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.17)
- KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.176)
- KXNHLGOAL-26NOV07NYRSEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.186)
- KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3681, phi -0.246)

portfolios: A EV +1.98 (adj +0.65) on $16.38, P(profit) 0.607, adj growth 5.8 bp · B EV +3.55 (adj +2.32) on $17.49, P(profit) 0.4213, adj growth 21.6 bp · C EV +1.68 (adj +0.61) on $14.71, P(profit) 0.7527, adj growth 5.7 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.7115, adj growth 2.3 bp

## MTL @ TOR  ·  10000 joint draws  ·  432 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MTL_win | p_overtime | goals | shots TOR/MTL | TOR/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.11 | 29.0/29.1 | 25.8/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 9.47 | 30.5/30.4 | 24.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.47 | 6.06 | 28.9/29.0 | 25.5/25.5 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.071 | 0.47 | 0.53 | 0.00 | 6.07 | 23.0/34.0 | 30.0/19.7 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 6.09 | 33.9/23.0 | 19.9/29.5 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.49 | 0.51 | 0.47 | 5.94 | 23.2/34.0 | 30.4/20.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brandon Duhaime: 1+ goals YES | 7 | 0.106 | 0.096 | +0.032 | +0.021 | $2.56 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 2+ assists NO | 83 | 0.917 | 0.869 | +0.077 | +0.029 | $9.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Teddy Blueger: 1+ goals YES | 12 | 0.169 | 0.148 | +0.042 | +0.021 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 48 | 0.620 | 0.522 | +0.123 | +0.025 | $5.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Brandon Duhaime: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes; why: higher confidence-adjusted growth (14.20 vs 8.28 bp); despite a smaller raw edge (+0.032 vs +0.042/contract); relationships: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.026); failure: TOR offense suppressed (<= 2 goals)
- **Nick Suzuki: 2+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no; why: higher confidence-adjusted growth (13.61 vs 5.50 bp); despite a smaller raw edge (+0.077 vs +0.123/contract); relationships: KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: DUPLICATIVE (phi 0.384); failure: MTL offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (8.28 vs 0.83 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (5.50 vs 0.83 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: DUPLICATIVE (phi 0.384); KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4641): highest fidelity KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3655): highest fidelity KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3264, phi -0.124)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4176, phi -0.229)
- KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3264, phi -0.194)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.0 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4176, phi -0.288)

portfolios: A EV +3.88 (adj +1.65) on $16.38, P(profit) 0.7213, adj growth 15.4 bp · B EV +4.08 (adj +1.74) on $19.95, P(profit) 0.7213, adj growth 16.3 bp · C EV +3.57 (adj +1.09) on $13.22, P(profit) 0.6831, adj growth 9.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ OTT  ·  10000 joint draws  ·  434 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.478 / away 0.522

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_UTA_win | p_overtime | goals | shots OTT/UTA | OTT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 6.02 | 27.0/27.0 | 23.5/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.54 | 0.46 | 0.51 | 5.96 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.52 | 0.48 | 0.00 | 9.5 | 29.0/28.7 | 22.6/22.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.083 | 0.61 | 0.39 | 0.00 | 6.08 | 32.1/21.6 | 18.6/27.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.55 | 0.45 | 0.47 | 5.97 | 32.0/21.6 | 18.4/28.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.057 | 0.45 | 0.55 | 0.00 | 6.0 | 21.5/31.8 | 27.9/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 17 | 0.212 | 0.199 | +0.032 | +0.019 | $2.75 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals YES | 25 | 0.298 | 0.285 | +0.035 | +0.022 | $3.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 16 | 0.201 | 0.185 | +0.032 | +0.015 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Fabian Zetterlund: 1+ goals YES | 20 | 0.240 | 0.227 | +0.029 | +0.016 | $2.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTAALEE72-1|yes; why: higher confidence-adjusted growth (5.50 vs 0.70 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)
- **Dylan Cozens: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (5.21 vs 3.62 bp); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes has the higher standalone adjusted growth (5.21 vs 3.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes has the higher standalone adjusted growth (5.21 vs 3.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.3923): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4332): highest fidelity KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3856): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTACKELLER9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTACKELLER9-1|no (same contract)
- KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3856, phi -0.214)
- KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.223)
- KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.199)
- KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.211)

portfolios: A EV +2.09 (adj +1.18) on $13.23, P(profit) 0.6651, adj growth 10.8 bp · B EV +1.69 (adj +0.96) on $10.81, P(profit) 0.6651, adj growth 9.0 bp · C EV +1.67 (adj +0.99) on $17.16, P(profit) 0.4473, adj growth 9.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  430 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.430 / away 0.570

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.0 | 27.6/28.0 | 24.5/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.51 | 0.49 | 0.48 | 5.94 | 27.6/28.0 | 24.6/24.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.086 | 0.49 | 0.51 | 0.00 | 6.0 | 22.0/33.0 | 29.1/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.17 | 29.0/29.2 | 23.6/22.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.47 | 5.92 | 21.9/33.0 | 29.5/18.6 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.055 | 0.60 | 0.40 | 0.00 | 6.03 | 32.2/22.3 | 19.2/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I wins by over 1.5 goals YES | 22 | 0.298 | 0.257 | +0.066 | +0.025 | $2.52 | FUNDED_RESEARCH | $1 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Adam Pelech: 1+ goals YES | 4 | 0.061 | 0.054 | +0.018 | +0.012 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| New Jersey wins by over 1.5 goals NO | 65 | 0.739 | 0.692 | +0.073 | +0.026 | $8.62 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 11 | 0.140 | 0.132 | +0.023 | +0.015 | $2.39 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **New York I wins by over 1.5 goals YES** — thesis: NYI wins by 2+; alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: higher confidence-adjusted growth (7.33 vs 6.72 bp); despite a smaller raw edge (+0.066 vs +0.073/contract); relationships: KXNHLGOAL-26NOV07NJNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLSPREAD-26NOV07NJNYI-NJ2|no: DUPLICATIVE (phi 0.387); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: NJD wins (incl. OT/SO)
- **Adam Pelech: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NYI offense suppressed (<= 2 goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes has the higher standalone adjusted growth (7.33 vs 6.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.387); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes: DUPLICATIVE (phi 0.387); KXNHLGOAL-26NOV07NJNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.148); failure: NJD wins by 2+
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07NJNYI-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (4.47 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26NOV07NJNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26NOV07NJNYI-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.148); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:WINS_BY_2PLUS (p 0.2981): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NYI:WINS (p 0.5198): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3918): highest fidelity KXNHLTEAMTOTAL-26NOV07NJNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07NJNYI-NYI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4802, phi -0.626)
- KXNHLGOAL-26NOV07NJNYI-NYIAPELECH3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.384, phi -0.101)
- KXNHLSPREAD-26NOV07NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.261, phi -1.0)
- KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4138, phi -0.177)

portfolios: A EV +3.58 (adj +0.70) on $16.38, P(profit) 0.4883, adj growth 6.4 bp · B EV +2.64 (adj +1.22) on $14.71, P(profit) 0.4437, adj growth 11.4 bp · C EV +2.18 (adj +1.02) on $6.76, P(profit) 0.3327, adj growth 9.1 bp · R EV +0.61 (adj +0.22) on $4.00, P(profit) 0.739, adj growth 8.1 bp

## CHI @ CAR  ·  10000 joint draws  ·  462 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.782 / away 0.218

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CHI_win | p_overtime | goals | shots CAR/CHI | CAR/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.205 | 0.79 | 0.21 | 0.00 | 6.04 | 34.4/20.2 | 18.0/29.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.160 | 0.81 | 0.19 | 0.00 | 9.39 | 36.3/21.7 | 17.7/27.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.152 | 0.57 | 0.43 | 0.49 | 5.97 | 34.5/20.7 | 17.5/30.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 3.48 | 32.9/19.1 | 18.0/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.070 | 0.74 | 0.26 | 0.00 | 6.03 | 28.0/26.6 | 24.0/23.2 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.52 | 2.9 | 33.0/19.1 | 17.6/31.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dillon Boucher: 1+ goals YES | 5 | 0.089 | 0.077 | +0.036 | +0.024 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.703 | 0.680 | +0.067 | +0.044 | $9.89 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.243 | 0.227 | +0.042 | +0.026 | $3.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.153 | 0.136 | +0.036 | +0.019 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Dillon Boucher: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (23.40 vs 9.45 bp); despite a smaller raw edge (+0.036 vs +0.042/contract); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGAME-26NOV07CHICAR-CAR|no; why: higher confidence-adjusted growth (18.05 vs 8.19 bp); despite a smaller raw edge (+0.067 vs +0.102/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26NOV07CHICAR-CAR|no; why: higher confidence-adjusted growth (9.45 vs 8.19 bp); despite a smaller raw edge (+0.042 vs +0.102/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (9.45 vs 7.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.20, CAR shot control · high event (8+) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15.
- thesis CAR:SUPPRESSED (p 0.2461): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.2753): highest fidelity KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.313): highest fidelity KXNHLGAME-26NOV07CHICAR-CAR|no [STRUCTURAL], best adjusted EV KXNHLGAME-26NOV07CHICAR-CAR|no (same contract)
- KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.159)
- KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5519, phi -0.228)
- KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.253)
- KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.178)

portfolios: A EV +4.91 (adj +1.07) on $16.38, P(profit) 0.5763, adj growth 9.0 bp · B EV +4.37 (adj +2.74) on $18.82, P(profit) 0.4181, adj growth 25.6 bp · C EV +4.20 (adj +2.09) on $23.20, P(profit) 0.4113, adj growth 19.2 bp · R EV +0.32 (adj +0.21) on $3.00, P(profit) 0.7034, adj growth 7.8 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07CHICAR-CHI|yes == KXNHLGAME-26NOV07CHICAR-CAR|no

## SJS @ DAL  ·  10000 joint draws  ·  456 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.722 / away 0.278

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.68 | 0.32 | 0.00 | 6.01 | 26.6/26.2 | 23.5/22.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.114 | 0.75 | 0.25 | 0.00 | 6.01 | 31.5/20.6 | 18.3/26.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.54 | 0.46 | 0.44 | 5.93 | 26.4/26.0 | 22.9/23.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.57 | 0.43 | 0.45 | 5.87 | 31.5/21.0 | 17.8/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.69 | 0.31 | 0.00 | 9.23 | 28.2/27.6 | 22.7/21.2 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.073 | 0.78 | 0.22 | 0.00 | 9.22 | 33.6/21.9 | 17.9/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mikko Rantanen: 1+ goals NO | 63 | 0.688 | 0.672 | +0.041 | +0.026 | $8.54 | FUNDED_RESEARCH | $3 | DAL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Jacob Trouba: 1+ goals YES | 5 | 0.074 | 0.065 | +0.020 | +0.012 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| San Jose over 3.5 goals scored YES | 23 | 0.295 | 0.257 | +0.052 | +0.015 | $1.72 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas over 3.5 goals scored NO | 41 | 0.513 | 0.443 | +0.086 | +0.016 | $1.75 | FUNDED_RESEARCH | $1 | DAL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07SJDAL-SJ2|yes; why: higher confidence-adjusted growth (6.28 vs 3.85 bp); despite a smaller raw edge (+0.041 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.56); relationships: KXNHLGOAL-26NOV07SJDAL-SJJTROUBA65-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no: REINFORCING (phi 0.223); failure: DAL offense succeeds (4+ goals)
- **Jacob Trouba: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes; why: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes has the higher standalone adjusted growth (6.65 vs 5.96 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.103); relationships: KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no: MOSTLY_INDEPENDENT (phi 0.012); failure: SJS offense suppressed (<= 2 goals)
- **San Jose over 3.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.49 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV07SJDAL-SJJTROUBA65-1|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no: INTENTIONAL_DIVERSIFIER (phi 0.125); failure: SJS offense suppressed (<= 2 goals)
- **Dallas over 3.5 goals scored NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no has the higher standalone adjusted growth (6.28 vs 2.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.223); they share one thesis budget; relationships: KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.223); KXNHLGOAL-26NOV07SJDAL-SJJTROUBA65-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes: INTENTIONAL_DIVERSIFIER (phi 0.125); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.2843): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes — Broad expression KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.49 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:WINS_BY_2PLUS (p 0.1799): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.366): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4779, phi -0.223)
- KXNHLGOAL-26NOV07SJDAL-SJJTROUBA65-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4988, phi -0.126)
- KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.4988, phi -0.645)
- KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.8 pts; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4779, phi -0.983)
- override: Broad expression KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.49 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.22 (adj +0.51) on $16.38, P(profit) 0.491, adj growth 3.9 bp · B EV +1.75 (adj +0.79) on $13.28, P(profit) 0.503, adj growth 7.4 bp · C EV +2.63 (adj +1.07) on $18.29, P(profit) 0.7329, adj growth 9.7 bp · R EV +0.61 (adj +0.22) on $5.00, P(profit) 0.5108, adj growth 7.8 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07SJDAL-SJ|yes == KXNHLGAME-26NOV07SJDAL-DAL|no

## TBL @ MIN  ·  10000 joint draws  ·  428 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_TBL_win | p_overtime | goals | shots MIN/TBL | MIN/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.50 | 0.50 | 0.50 | 6.0 | 27.8/27.9 | 24.6/24.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.48 | 0.52 | 0.00 | 6.0 | 27.6/27.9 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.47 | 0.53 | 0.00 | 9.45 | 29.5/29.6 | 23.1/23.4 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.40 | 0.60 | 0.00 | 5.99 | 22.0/32.8 | 28.7/19.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.48 | 0.52 | 0.47 | 5.96 | 22.5/33.0 | 29.8/19.2 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.059 | 0.48 | 0.52 | 0.00 | 6.04 | 32.2/22.0 | 18.4/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.138 | 0.125 | +0.043 | +0.029 | $3.53 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Bobby Brink: 1+ goals YES | 14 | 0.187 | 0.170 | +0.038 | +0.022 | $2.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ assists NO | 52 | 0.615 | 0.565 | +0.077 | +0.028 | $8.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Blake Coleman: 1+ goals YES | 20 | 0.242 | 0.231 | +0.031 | +0.019 | $2.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (20.94 vs 7.96 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN offense suppressed (<= 2 goals)
- **Bobby Brink: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (7.96 vs 4.88 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (6.65 vs 3.04 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: MIN offense succeeds (4+ goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes has the higher standalone adjusted growth (7.96 vs 4.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.384): highest fidelity KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.388): highest fidelity KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3573): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.169)
- KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.203)
- KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.384, phi -0.287)
- KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.228)

portfolios: A EV +3.29 (adj +1.41) on $16.38, P(profit) 0.6302, adj growth 13.2 bp · B EV +3.93 (adj +2.18) on $17.59, P(profit) 0.3963, adj growth 20.3 bp · C EV +2.83 (adj +1.25) on $16.14, P(profit) 0.6954, adj growth 11.3 bp · R EV +0.44 (adj +0.31) on $1.00, P(profit) 0.1383, adj growth 11.2 bp

## DET @ COL  ·  10000 joint draws  ·  454 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.664 / away 0.336

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DET_win | p_overtime | goals | shots COL/DET | COL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.74 | 0.26 | 0.00 | 5.99 | 28.6/28.2 | 25.7/23.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.112 | 0.76 | 0.24 | 0.00 | 6.01 | 33.7/22.1 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.47 | 5.99 | 28.4/28.0 | 24.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.73 | 0.27 | 0.00 | 9.37 | 30.0/29.7 | 24.8/22.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.088 | 0.80 | 0.20 | 0.00 | 9.32 | 35.9/23.7 | 19.8/27.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.60 | 0.40 | 0.44 | 5.98 | 34.2/22.6 | 19.3/30.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artturi Lehkonen: 1+ assists YES | 28 | 0.344 | 0.309 | +0.050 | +0.015 | $2.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **Artturi Lehkonen: 1+ assists YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes; why: higher confidence-adjusted growth (2.44 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0005 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.5356): highest fidelity KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2617, phi -0.236)

portfolios: A EV +0.97 (adj +0.30) on $5.75, P(profit) 0.3437, adj growth 2.6 bp · B EV +0.42 (adj +0.13) on $2.51, P(profit) 0.3437, adj growth 1.2 bp · C EV +0.63 (adj +0.19) on $3.74, P(profit) 0.3437, adj growth 1.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ LAK  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_PIT_win | p_overtime | goals | shots LAK/PIT | LAK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.57 | 0.42 | 0.00 | 5.99 | 27.7/27.5 | 24.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.43 | 5.93 | 27.3/27.4 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.58 | 0.42 | 0.00 | 9.24 | 29.0/29.0 | 23.4/22.4 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 6.02 | 32.4/22.0 | 19.3/28.2 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.46 | 5.9 | 32.2/22.0 | 18.9/28.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 6.02 | 21.7/31.7 | 27.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.069 | +0.022 | +0.015 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.126 | 0.111 | +0.030 | +0.015 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ goals NO | 77 | 0.814 | 0.802 | +0.032 | +0.019 | $9.89 | FUNDED_RESEARCH | $3 | PIT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Andre Lee: 1+ goals YES | 10 | 0.125 | 0.118 | +0.019 | +0.011 | $1.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07PITLA-PIT2|no; why: higher confidence-adjusted growth (10.09 vs 0.07 bp); despite a smaller raw edge (+0.022 vs +0.024/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV07PITLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.021); failure: LAK offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (5.50 vs 1.25 bp); alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07PITLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07PITLA-PIT2|no; why: higher confidence-adjusted growth (4.85 vs 0.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07PITLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: PIT offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07PITLA-PIT2|no; why: higher confidence-adjusted growth (2.97 vs 0.07 bp); despite a smaller raw edge (+0.019 vs +0.024/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:WINS_BY_2PLUS (p 0.2416): highest fidelity KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.357): highest fidelity KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.4268): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.357, phi -0.132)
- KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4178, phi -0.192)
- KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3534, phi -0.187)
- KXNHLGOAL-26NOV07PITLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.357, phi -0.165)

portfolios: A EV +2.04 (adj +1.21) on $16.38, P(profit) 0.6359, adj growth 11.1 bp · B EV +1.98 (adj +1.22) on $15.01, P(profit) 0.2751, adj growth 11.3 bp · C EV +1.06 (adj +0.53) on $9.10, P(profit) 0.7167, adj growth 4.8 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.814, adj growth 2.8 bp

## VAN @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.750 / away 0.250

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_VAN_win | p_overtime | goals | shots EDM/VAN | EDM/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.147 | 0.80 | 0.20 | 0.00 | 6.08 | 33.2/21.1 | 18.9/28.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.141 | 0.80 | 0.20 | 0.00 | 9.49 | 34.8/22.3 | 18.3/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.73 | 0.27 | 0.00 | 9.52 | 29.1/28.3 | 23.6/21.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.73 | 0.27 | 0.00 | 6.12 | 27.3/26.6 | 24.1/22.8 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.59 | 0.41 | 0.45 | 6.0 | 33.4/21.3 | 18.2/29.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.54 | 0.46 | 0.48 | 6.02 | 27.7/27.1 | 23.8/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brendan Gallagher: 1+ goals YES | 9 | 0.144 | 0.129 | +0.048 | +0.033 | $3.98 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 15 | 0.221 | 0.197 | +0.062 | +0.038 | $4.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.348 | 0.328 | +0.065 | +0.044 | $7.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.212 | 0.197 | +0.043 | +0.028 | $3.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (26.91 vs 22.75 bp); despite a smaller raw edge (+0.048 vs +0.062/contract); relationships: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (22.75 vs 11.55 bp); relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (20.31 vs 0.27 bp); despite a smaller raw edge (+0.065 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: EDM offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (22.75 vs 11.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3223): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5979): highest fidelity KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes (same contract)
- thesis GAME:TIGHT (p 0.3727): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no (same contract)
- KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.19)
- KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.239)
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2184, phi -0.226)
- KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.218)

portfolios: A EV +3.64 (adj +1.93) on $16.38, P(profit) 0.5713, adj growth 18.2 bp · B EV +6.47 (adj +4.25) on $19.83, P(profit) 0.6603, adj growth 39.5 bp · C EV +6.74 (adj +3.88) on $27.67, P(profit) 0.4929, adj growth 34.9 bp · R EV +0.50 (adj +0.35) on $1.00, P(profit) 0.1436, adj growth 12.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
