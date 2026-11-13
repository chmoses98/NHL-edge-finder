# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-13T23:05:11Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +21.86 | +5.82 | +20.88 | 0.691 | -60.61 | -60.71 | 45.31 |
| B thesis-diversified (joint) ← optimiser card | 84.61 | +15.58 | +8.25 | +6.07 | 0.535 | -39.55 | -54.41 | 71.30 |
| C best expression per thesis | 61.74 | +14.46 | +7.88 | -6.24 | 0.450 | -27.99 | -43.55 | 67.36 |
| R FUNDED research stakes | 15.00 | +1.76 | +0.59 | +1.29 | 0.653 | -8.10 | -8.36 | 0.00 |

## NYR @ VAN  ·  10000 joint draws  ·  416 bet sides mapped, 33 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.352 / away 0.648

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
| Linus Karlsson: 1+ goals YES | 16 | 0.239 | 0.218 | +0.070 | +0.049 | $12.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| New York R wins by over 1.5 goals NO | 56 | 0.722 | 0.613 | +0.145 | +0.036 | $10.74 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York R over 3.5 goals scored NO | 46 | 0.609 | 0.509 | +0.132 | +0.032 | $8.62 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Gabe Perreault: 1+ goals NO | 71 | 0.764 | 0.749 | +0.040 | +0.025 | $17.25 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NYRVAN-VANMSASSON63-1|yes; why: KXNHLGOAL-26NOV13NYRVAN-VANMSASSON63-1|yes has the higher standalone adjusted growth (44.62 vs 35.76 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.011); relationships: KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **New York R wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR2|no; why: KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR2|no has the higher standalone adjusted growth (22.94 vs 11.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.297); relationships: KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.139); KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no: REINFORCING (phi 0.547); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: REINFORCING (phi 0.166); failure: NYR wins by 2+
- **New York R over 3.5 goals scored NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR2|no; why: KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR2|no has the higher standalone adjusted growth (22.94 vs 8.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.384); relationships: KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: REINFORCING (phi 0.547); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: REINFORCING (phi 0.218); failure: NYR offense succeeds (4+ goals)
- **Gabe Perreault: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR2|no; why: KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR2|no has the higher standalone adjusted growth (22.94 vs 6.85 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.195); relationships: KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: REINFORCING (phi 0.166); KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no: REINFORCING (phi 0.218); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3913): highest fidelity KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2844): highest fidelity KXNHLSPREAD-26NOV13NYRVAN-NYR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV13NYRVAN-VANMSASSON63-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3994): highest fidelity KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV13NYRVAN-NYR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3851, phi -0.228)
- KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.7 pts; opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.278, phi -1.0)
- KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3822, phi -0.982)
- KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3822, phi -0.22)

portfolios: A EV +14.12 (adj +3.24) on $50.00, P(profit) 0.6233, adj growth 24.8 bp · B EV +11.29 (adj +5.52) on $49.43, P(profit) 0.5906, adj growth 47.7 bp · C EV +12.15 (adj +6.68) on $27.54, P(profit) 0.3295, adj growth 56.9 bp · R EV +1.58 (adj +0.49) on $10.00, P(profit) 0.6219, adj growth 17.4 bp
equivalent contracts collapsed: KXNHLGAME-26NOV13NYRVAN-NYR|no == KXNHLGAME-26NOV13NYRVAN-VAN|yes

## NSH @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.590 / away 0.410

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
| Braeden Bowman: 1+ goals YES | 13 | 0.173 | 0.161 | +0.036 | +0.024 | $6.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brett Howden: 1+ goals YES | 18 | 0.224 | 0.211 | +0.033 | +0.021 | $6.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 21 | 0.255 | 0.243 | +0.034 | +0.021 | $6.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Victor Olofsson: 1+ goals NO | 74 | 0.780 | 0.769 | +0.027 | +0.015 | $16.01 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (9.96 vs 6.31 bp); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense suppressed (<= 2 goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.31 vs 5.65 bp); despite a smaller raw edge (+0.033 vs +0.034/contract); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes has the higher standalone adjusted growth (6.31 vs 5.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: VGK offense suppressed (<= 2 goals)
- **Victor Olofsson: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no selected over player prop KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.91 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: VGK offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:OFFENSE_4PLUS (p 0.4795): highest fidelity KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3098): highest fidelity KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4678): highest fidelity KXNHLAST-26NOV13NSHVGK-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV13NSHVGK-NSHMBOURQUE22-1|no (same contract)
- KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.169)
- KXNHLGOAL-26NOV13NSHVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.201)
- KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.196)
- KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4795, phi -0.2)
- override: Player prop expression KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no selected over player prop KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.91 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.74 (adj +2.58) on $50.00, P(profit) 0.4669, adj growth 20.5 bp · B EV +4.30 (adj +2.73) on $35.18, P(profit) 0.4577, adj growth 23.6 bp · C EV +2.31 (adj +1.20) on $34.20, P(profit) 0.6878, adj growth 10.5 bp · R EV +0.18 (adj +0.10) on $5.00, P(profit) 0.7803, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
