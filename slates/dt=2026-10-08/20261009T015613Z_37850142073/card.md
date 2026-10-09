# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T01:56:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +7.66 | +1.52 | +4.98 | 0.682 | -14.36 | -30.95 | 13.18 |
| B thesis-diversified (joint) ← optimiser card | 41.07 | +5.31 | +2.49 | +4.75 | 0.661 | -21.42 | -41.07 | 21.82 |
| C best expression per thesis | 41.44 | +3.84 | +1.38 | +5.29 | 0.742 | -21.26 | -21.26 | 12.35 |
| R FUNDED research stakes | 4.00 | +0.23 | +0.14 | +2.01 | 0.704 | -4.00 | -4.00 | 0.00 |

## TOR @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.601 / away 0.400

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.153 | 0.76 | 0.24 | 0.00 | 5.99 | 34.0/21.4 | 19.1/29.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.59 | 0.41 | 0.48 | 5.92 | 34.3/21.7 | 18.7/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.04 | 28.4/27.7 | 25.0/24.0 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.105 | 0.77 | 0.23 | 0.00 | 9.28 | 36.0/23.0 | 18.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.47 | 0.49 | 5.96 | 28.4/27.7 | 24.5/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.73 | 0.27 | 0.00 | 9.35 | 30.1/29.2 | 24.6/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 8 | 0.112 | 0.103 | +0.027 | +0.017 | $4.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Darren Raddysh: 1+ assists NO | 63 | 0.721 | 0.673 | +0.075 | +0.027 | $16.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ goals NO | 65 | 0.704 | 0.690 | +0.038 | +0.024 | $13.08 | FUNDED_RESEARCH | $4 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ assists YES | 31 | 0.383 | 0.344 | +0.058 | +0.019 | $6.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (8.37 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.069); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: TOR offense suppressed (<= 2 goals)
- **Darren Raddysh: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no; why: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no has the higher standalone adjusted growth (7.14 vs 6.89 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.035); relationships: KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.069); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: REINFORCING (phi 0.166); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no; why: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no has the higher standalone adjusted growth (7.14 vs 5.51 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.062); relationships: KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no: REINFORCING (phi 0.166); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: TOR offense succeeds (4+ goals)
- **Ivan Barbashev: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (3.56 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.5076): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.5093): highest fidelity KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2885): highest fidelity KXNHLGOAL-26OCT08TORVGK-VGKJEICHEL9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08TORVGK-VGKJEICHEL9-1|no (same contract)
- KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.5076, phi -0.177)
- KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2861, phi -0.26)
- KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2861, phi -0.277)
- KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.268)

portfolios: A EV +7.66 (adj +1.52) on $50.00, P(profit) 0.6825, adj growth 13.2 bp · B EV +5.31 (adj +2.49) on $41.07, P(profit) 0.6607, adj growth 21.8 bp · C EV +3.84 (adj +1.38) on $41.44, P(profit) 0.7424, adj growth 12.3 bp · R EV +0.23 (adj +0.14) on $4.00, P(profit) 0.7044, adj growth 5.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
