# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T02:12:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +12.23 | +2.49 | +9.40 | 0.616 | -32.74 | -32.74 | 19.74 |
| B thesis-diversified (joint) ← optimiser card | 50.00 | +12.86 | +6.52 | +4.34 | 0.568 | -17.36 | -50.00 | 57.23 |
| C best expression per thesis | 50.00 | +11.42 | +5.29 | -0.07 | 0.478 | -30.60 | -50.00 | 47.06 |
| R FUNDED research stakes | 4.00 | +0.91 | +0.60 | -4.00 | 0.348 | -4.00 | -4.00 | 0.00 |

## VAN @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.756 / away 0.244

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
| Vasily Podkolzin: 1+ goals YES | 27 | 0.348 | 0.326 | +0.065 | +0.042 | $15.42 | FUNDED_RESEARCH | $4 | EDM:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.221 | 0.204 | +0.051 | +0.035 | $9.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 10 | 0.144 | 0.130 | +0.037 | +0.024 | $5.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 58 | 0.736 | 0.628 | +0.139 | +0.031 | $19.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (19.17 vs 2.40 bp); despite a smaller raw edge (+0.065 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.192); failure: EDM offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (18.39 vs 6.32 bp); relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (18.39 vs 12.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.017); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: higher confidence-adjusted growth (8.71 vs 5.33 bp); wins across more scripts (relative breadth 1.066 vs 0.949); relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.192); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5979): highest fidelity KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3223): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2184): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2184, phi -0.226)
- KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.239)
- KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.19)
- KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5979, phi -0.33)

portfolios: A EV +12.23 (adj +2.49) on $50.00, P(profit) 0.6162, adj growth 19.7 bp · B EV +12.86 (adj +6.52) on $50.00, P(profit) 0.5678, adj growth 57.2 bp · C EV +11.42 (adj +5.29) on $50.00, P(profit) 0.4785, adj growth 47.1 bp · R EV +0.91 (adj +0.60) on $4.00, P(profit) 0.3483, adj growth 20.3 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07VANEDM-VAN|yes == KXNHLGAME-26NOV07VANEDM-EDM|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
