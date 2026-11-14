# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T00:05:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +22.90 | +6.36 | +29.76 | 0.658 | -60.98 | -65.09 | 48.02 |
| B thesis-diversified (joint) ← optimiser card | 69.82 | +10.77 | +5.08 | +4.54 | 0.671 | -37.23 | -47.75 | 44.63 |
| C best expression per thesis | 60.71 | +12.57 | +7.03 | -1.83 | 0.422 | -38.93 | -39.58 | 60.10 |
| R FUNDED research stakes | 11.00 | +1.99 | +0.79 | +3.18 | 0.657 | -5.48 | -11.00 | 0.00 |

## NYR @ VAN  ·  10000 joint draws  ·  416 bet sides mapped, 36 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.347 / away 0.653

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_NYR_win | p_overtime | goals | shots VAN/NYR | VAN/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.51 | 0.49 | 0.00 | 5.98 | 26.5/26.8 | 23.3/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.45 | 5.84 | 26.6/26.7 | 23.5/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.49 | 0.51 | 0.00 | 9.33 | 28.1/28.4 | 22.2/22.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.085 | 0.46 | 0.54 | 0.00 | 6.0 | 21.1/31.6 | 27.7/17.8 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.49 | 0.51 | 0.46 | 5.94 | 21.4/32.1 | 28.8/18.1 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.058 | 0.42 | 0.58 | 0.00 | 9.27 | 22.6/33.5 | 26.1/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York R wins by over 1.5 goals NO | 56 | 0.722 | 0.613 | +0.145 | +0.036 | $18.21 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Gabe Perreault: 1+ goals NO | 71 | 0.764 | 0.749 | +0.040 | +0.025 | $15.99 | FUNDED_RESEARCH | $4 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Mika Zibanejad: 1+ goals NO | 66 | 0.717 | 0.702 | +0.042 | +0.026 | $14.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **New York R wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes has the higher standalone adjusted growth (19.42 vs 11.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.287); relationships: KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: REINFORCING (phi 0.166); KXNHLGOAL-26NOV13NYRVAN-NYRMZIBANEJAD93-1|no: REINFORCING (phi 0.169); failure: NYR wins by 2+
- **Gabe Perreault: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes has the higher standalone adjusted growth (19.42 vs 6.85 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: REINFORCING (phi 0.166); KXNHLGOAL-26NOV13NYRVAN-NYRMZIBANEJAD93-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYR offense succeeds (4+ goals)
- **Mika Zibanejad: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes has the higher standalone adjusted growth (19.42 vs 6.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.134); relationships: KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: REINFORCING (phi 0.169); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3913): highest fidelity KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2844): highest fidelity KXNHLSPREAD-26NOV13NYRVAN-NYR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV13NYRVAN-VANMSASSON63-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3994): highest fidelity KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV13NYRVAN-NYR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.7 pts; opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.278, phi -1.0)
- KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3822, phi -0.22)
- KXNHLGOAL-26NOV13NYRVAN-NYRMZIBANEJAD93-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3822, phi -0.243)

portfolios: A EV +15.96 (adj +3.62) on $50.00, P(profit) 0.6233, adj growth 25.8 bp · B EV +6.31 (adj +2.23) on $48.21, P(profit) 0.6889, adj growth 20.0 bp · C EV +10.49 (adj +5.78) on $27.14, P(profit) 0.3017, adj growth 49.2 bp · R EV +1.47 (adj +0.45) on $9.00, P(profit) 0.5832, adj growth 16.1 bp
equivalent contracts collapsed: KXNHLGAME-26NOV13NYRVAN-NYR|no == KXNHLGAME-26NOV13NYRVAN-VAN|yes

## NSH @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NSH_win | p_overtime | goals | shots VGK/NSH | VGK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.124 | 0.73 | 0.27 | 0.00 | 5.99 | 33.4/21.6 | 19.1/28.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.64 | 0.36 | 0.00 | 6.05 | 28.0/27.5 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.49 | 0.51 | 0.48 | 5.97 | 28.1/27.6 | 24.2/24.7 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.57 | 0.43 | 0.45 | 5.88 | 33.4/21.9 | 18.8/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.70 | 0.30 | 0.00 | 9.27 | 29.5/28.9 | 23.9/22.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.083 | 0.74 | 0.26 | 0.00 | 9.32 | 35.0/23.1 | 18.8/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Braeden Bowman: 1+ goals YES | 13 | 0.173 | 0.161 | +0.036 | +0.024 | $6.25 | FUNDED_RESEARCH | $2 | VGK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brett Howden: 1+ goals YES | 18 | 0.224 | 0.211 | +0.033 | +0.021 | $6.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 21 | 0.255 | 0.243 | +0.034 | +0.021 | $6.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.070 | 0.063 | +0.016 | +0.010 | $2.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (9.96 vs 6.31 bp); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV13NSHVGK-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VGK offense suppressed (<= 2 goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.31 vs 5.65 bp); despite a smaller raw edge (+0.033 vs +0.034/contract); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV13NSHVGK-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes has the higher standalone adjusted growth (6.31 vs 5.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV13NSHVGK-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV13NSHVGK-9|yes; why: higher confidence-adjusted growth (4.35 vs 0.07 bp); despite a smaller raw edge (+0.016 vs +0.019/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.868 vs 0.372); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:OFFENSE_4PLUS (p 0.4795): highest fidelity KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.3098): highest fidelity KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4678): highest fidelity KXNHLAST-26NOV13NSHVGK-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.169)
- KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.201)
- KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.196)
- KXNHLGOAL-26NOV13NSHVGK-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4678, phi -0.127)

portfolios: A EV +6.94 (adj +2.74) on $50.00, P(profit) 0.4669, adj growth 22.3 bp · B EV +4.46 (adj +2.85) on $21.61, P(profit) 0.5583, adj growth 24.7 bp · C EV +2.07 (adj +1.25) on $33.57, P(profit) 0.6386, adj growth 10.9 bp · R EV +0.52 (adj +0.34) on $2.00, P(profit) 0.1735, adj growth 11.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
