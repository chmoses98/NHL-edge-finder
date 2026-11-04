# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T13:12:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 66.64 | +11.59 | +5.55 | +5.19 | 0.545 | -66.64 | -66.64 | 38.76 |
| B thesis-diversified (joint) ← optimiser card | 46.95 | +8.34 | +4.94 | +6.58 | 0.583 | -46.95 | -46.95 | 42.85 |
| C best expression per thesis | 36.38 | +5.88 | +3.58 | -8.91 | 0.479 | -36.38 | -36.38 | 31.00 |
| R FUNDED research stakes | 7.00 | +0.64 | +0.37 | +0.98 | 0.746 | -7.00 | -7.00 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  390 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_OTT_win | p_overtime | goals | shots BUF/OTT | BUF/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.56 | 0.44 | 0.00 | 6.03 | 27.3/27.4 | 24.0/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.99 | 27.4/27.5 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.56 | 0.44 | 0.00 | 9.38 | 28.9/28.6 | 23.0/22.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.072 | 0.61 | 0.39 | 0.00 | 6.04 | 32.3/21.9 | 19.0/28.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.55 | 0.45 | 0.43 | 5.94 | 32.2/21.9 | 18.6/28.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.48 | 0.52 | 0.00 | 6.04 | 21.9/32.3 | 28.4/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Doan: 1+ goals YES | 19 | 0.231 | 0.218 | +0.030 | +0.017 | $5.23 | FUNDED_RESEARCH | $2 | BUF:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.014 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Josh Doan: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV04OTTBUF-BUFJDOAN91-1|yes; why: higher confidence-adjusted growth (4.06 vs 0.00 bp); despite a smaller raw edge (+0.030 vs +0.042/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: BUF offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (2.98 vs 1.26 bp); despite a smaller raw edge (+0.024 vs +0.030/contract); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFJDOAN91-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3907): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4457): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04OTTBUF-BUFJDOAN91-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3424, phi -0.19)
- KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3879, phi -0.21)

portfolios: A EV +2.52 (adj +1.43) on $16.64, P(profit) 0.3738, adj growth 10.9 bp · B EV +1.37 (adj +0.78) on $9.09, P(profit) 0.3738, adj growth 6.8 bp · C EV +0.59 (adj +0.33) on $3.82, P(profit) 0.1833, adj growth 2.8 bp · R EV +0.30 (adj +0.17) on $2.00, P(profit) 0.2308, adj growth 5.5 bp

## CHI @ FLA  ·  10000 joint draws  ·  410 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_CHI_win | p_overtime | goals | shots FLA/CHI | FLA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.142 | 0.73 | 0.27 | 0.00 | 6.05 | 32.6/20.8 | 18.3/27.7 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.58 | 0.42 | 0.46 | 5.86 | 33.2/21.1 | 18.0/29.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.62 | 0.38 | 0.00 | 6.01 | 27.2/26.4 | 23.4/23.1 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.103 | 0.75 | 0.25 | 0.00 | 9.31 | 34.2/22.2 | 17.9/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.55 | 0.45 | 0.46 | 5.93 | 27.0/26.4 | 23.1/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.63 | 0.37 | 0.00 | 9.43 | 28.8/28.1 | 22.7/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.283 | 0.264 | +0.062 | +0.042 | $12.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.152 | 0.134 | +0.035 | +0.017 | $4.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 61 | 0.669 | 0.652 | +0.043 | +0.025 | $17.23 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 12 | 0.160 | 0.141 | +0.033 | +0.014 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes; why: higher confidence-adjusted growth (22.21 vs 5.05 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.904 vs 0.783); relationships: KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (22.21 vs 6.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CHI offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no; why: higher confidence-adjusted growth (6.05 vs 2.79 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: FLA offense succeeds (4+ goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (22.21 vs 3.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3154): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.3016): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.3742): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4736, phi -0.276)
- KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4736, phi -0.197)
- KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4927, phi -0.221)
- KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4736, phi -0.206)

portfolios: A EV +9.07 (adj +4.12) on $50.00, P(profit) 0.4615, adj growth 27.9 bp · B EV +6.96 (adj +4.16) on $37.86, P(profit) 0.4252, adj growth 36.1 bp · C EV +5.29 (adj +3.25) on $32.56, P(profit) 0.4026, adj growth 28.2 bp · R EV +0.34 (adj +0.20) on $5.00, P(profit) 0.6694, adj growth 7.0 bp

## SJS @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.60 | 0.40 | 0.00 | 5.97 | 27.9/27.6 | 24.5/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 5.91 | 28.1/27.6 | 24.3/24.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.104 | 0.67 | 0.33 | 0.00 | 5.99 | 33.5/22.2 | 19.6/28.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.57 | 0.43 | 0.46 | 5.86 | 33.5/22.1 | 18.9/30.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.60 | 0.40 | 0.00 | 9.29 | 29.6/29.0 | 23.6/23.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 3.44 | 26.3/26.2 | 24.7/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 6.07 | 28.2/28.4 | 25.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.48 | 5.98 | 28.3/28.4 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.65 | 0.35 | 0.00 | 9.38 | 30.1/30.2 | 24.9/23.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 5.98 | 22.8/33.6 | 30.3/19.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.066 | 0.69 | 0.31 | 0.00 | 6.05 | 33.3/22.7 | 20.0/28.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.51 | 0.49 | 0.42 | 5.88 | 22.6/33.5 | 30.2/19.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
