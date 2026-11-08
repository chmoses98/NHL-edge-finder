# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T02:38:37Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +9.37 | +2.14 | +9.85 | 0.669 | -11.81 | -32.74 | 18.60 |
| B thesis-diversified (joint) ← optimiser card | 50.00 | +10.69 | +6.44 | +4.61 | 0.572 | -50.00 | -50.00 | 56.11 |
| C best expression per thesis | 47.15 | +12.39 | +6.04 | +7.94 | 0.515 | -13.65 | -47.15 | 52.89 |
| R FUNDED research stakes | 9.00 | +1.53 | +0.83 | -0.34 | 0.348 | -9.00 | -9.00 | 0.00 |

## VAN @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.756 / away 0.244

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_VAN_win | p_overtime | goals | shots EDM/VAN | EDM/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.143 | 0.79 | 0.21 | 0.00 | 6.07 | 32.9/20.9 | 18.7/27.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.140 | 0.80 | 0.20 | 0.00 | 9.53 | 35.1/22.8 | 18.6/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.74 | 0.26 | 0.00 | 9.56 | 29.2/28.4 | 23.6/21.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.73 | 0.27 | 0.00 | 6.11 | 27.5/26.6 | 24.0/22.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.60 | 0.40 | 0.47 | 6.03 | 33.3/21.4 | 18.3/29.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.53 | 0.47 | 0.47 | 5.97 | 27.7/26.8 | 23.6/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vasily Podkolzin: 1+ goals YES | 27 | 0.348 | 0.327 | +0.064 | +0.043 | $15.50 | FUNDED_RESEARCH | $4 | EDM:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.222 | 0.205 | +0.052 | +0.035 | $8.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 11 | 0.154 | 0.142 | +0.037 | +0.025 | $6.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Edmonton wins by over 2.5 goals NO | 56 | 0.649 | 0.602 | +0.072 | +0.025 | $19.18 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (20.04 vs 3.55 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV07VANEDM-EDM3|no: INTENTIONAL_DIVERSIFIER (phi -0.182); failure: EDM offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes; why: higher confidence-adjusted growth (19.26 vs 12.54 bp); relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26NOV07VANEDM-EDM3|no: MOSTLY_INDEPENDENT (phi 0.142); failure: VAN offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (20.04 vs 12.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26NOV07VANEDM-EDM3|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: EDM offense suppressed (<= 2 goals)
- **Edmonton wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: Broad expression KXNHLSPREAD-26NOV07VANEDM-EDM3|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.182); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.142); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: EDM wins by 2+

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.14, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5968): highest fidelity KXNHLAST-26NOV07VANEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3261): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2137): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no — Broad expression KXNHLSPREAD-26NOV07VANEDM-EDM3|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2137, phi -0.215)
- KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4639, phi -0.244)
- KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2137, phi -0.145)
- KXNHLSPREAD-26NOV07VANEDM-EDM3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:WINS_BY_2PLUS (p 0.4741, phi -0.774)
- override: Broad expression KXNHLSPREAD-26NOV07VANEDM-EDM3|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.37 (adj +2.14) on $50.00, P(profit) 0.6686, adj growth 18.6 bp · B EV +10.69 (adj +6.44) on $50.00, P(profit) 0.5722, adj growth 56.1 bp · C EV +12.39 (adj +6.04) on $47.15, P(profit) 0.515, adj growth 52.9 bp · R EV +1.53 (adj +0.83) on $9.00, P(profit) 0.3479, adj growth 29.0 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07VANEDM-VAN|yes == KXNHLGAME-26NOV07VANEDM-EDM|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
