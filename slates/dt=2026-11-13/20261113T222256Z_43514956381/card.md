# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-13T22:22:56Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +21.09 | +5.30 | +20.73 | 0.687 | -45.42 | -61.00 | 41.22 |
| B thesis-diversified (joint) ← optimiser card | 78.46 | +15.72 | +8.41 | +2.42 | 0.629 | -39.19 | -54.81 | 72.45 |
| C best expression per thesis | 61.66 | +12.71 | +7.27 | -1.91 | 0.435 | -40.11 | -40.28 | 62.01 |
| R FUNDED research stakes | 14.00 | +1.72 | +0.57 | +2.29 | 0.653 | -7.10 | -8.69 | 0.00 |

## NYR @ VAN  ·  10000 joint draws  ·  412 bet sides mapped, 33 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.352 / away 0.648

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_NYR_win | p_overtime | goals | shots VAN/NYR | VAN/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.51 | 0.49 | 0.00 | 5.99 | 26.3/26.7 | 23.2/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.54 | 0.46 | 0.47 | 5.87 | 26.5/26.7 | 23.4/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.50 | 0.50 | 0.00 | 9.33 | 28.0/28.3 | 22.3/22.0 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.086 | 0.46 | 0.54 | 0.00 | 6.0 | 21.1/31.7 | 27.7/17.8 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.45 | 5.94 | 21.4/32.0 | 28.7/18.2 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.056 | 0.60 | 0.40 | 0.00 | 6.0 | 31.2/21.4 | 18.4/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 16 | 0.242 | 0.220 | +0.073 | +0.051 | $13.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| New York R wins by over 1.5 goals NO | 56 | 0.722 | 0.613 | +0.145 | +0.036 | $10.36 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York R over 3.5 goals scored NO | 46 | 0.609 | 0.509 | +0.132 | +0.032 | $8.73 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Gabe Perreault: 1+ goals NO | 71 | 0.764 | 0.749 | +0.040 | +0.025 | $17.14 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NYRVAN-VANMSASSON63-1|yes; why: KXNHLGOAL-26NOV13NYRVAN-VANMSASSON63-1|yes has the higher standalone adjusted growth (47.32 vs 39.10 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.013); relationships: KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: MOSTLY_INDEPENDENT (phi 0.142); KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: VAN offense suppressed (<= 2 goals)
- **New York R wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes has the higher standalone adjusted growth (16.30 vs 11.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.287); relationships: KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.142); KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no: REINFORCING (phi 0.547); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: REINFORCING (phi 0.166); failure: NYR wins by 2+
- **New York R over 3.5 goals scored NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes has the higher standalone adjusted growth (16.30 vs 8.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.323); relationships: KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: REINFORCING (phi 0.547); KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: REINFORCING (phi 0.218); failure: NYR offense succeeds (4+ goals)
- **Gabe Perreault: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes; why: KXNHLSPREAD-26NOV13NYRVAN-VAN3|yes has the higher standalone adjusted growth (16.30 vs 6.85 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: REINFORCING (phi 0.166); KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no: REINFORCING (phi 0.218); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3913): highest fidelity KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2844): highest fidelity KXNHLSPREAD-26NOV13NYRVAN-NYR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV13NYRVAN-VANMSASSON63-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3994): highest fidelity KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV13NYRVAN-NYR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV13NYRVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3851, phi -0.232)
- KXNHLSPREAD-26NOV13NYRVAN-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.7 pts; opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.278, phi -1.0)
- KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3822, phi -0.982)
- KXNHLGOAL-26NOV13NYRVAN-NYRGPERREAULT94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3822, phi -0.22)

portfolios: A EV +14.12 (adj +3.24) on $50.00, P(profit) 0.6233, adj growth 24.8 bp · B EV +11.69 (adj +5.84) on $49.61, P(profit) 0.5918, adj growth 50.4 bp · C EV +10.71 (adj +6.08) on $27.47, P(profit) 0.3026, adj growth 51.6 bp · R EV +1.58 (adj +0.49) on $10.00, P(profit) 0.6219, adj growth 17.4 bp
equivalent contracts collapsed: KXNHLGAME-26NOV13NYRVAN-NYR|no == KXNHLGAME-26NOV13NYRVAN-VAN|yes

## NSH @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.587 / away 0.413

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NSH_win | p_overtime | goals | shots VGK/NSH | VGK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.64 | 0.36 | 0.00 | 6.03 | 27.9/27.5 | 24.4/23.8 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.119 | 0.73 | 0.27 | 0.00 | 5.99 | 33.1/21.5 | 19.1/28.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.49 | 0.51 | 0.48 | 5.98 | 27.7/27.4 | 24.0/24.4 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.57 | 0.43 | 0.45 | 5.87 | 33.3/21.9 | 18.7/29.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.70 | 0.30 | 0.00 | 9.29 | 29.4/28.9 | 24.0/22.2 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.085 | 0.75 | 0.25 | 0.00 | 9.32 | 35.0/23.0 | 18.7/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 6 | 0.091 | 0.082 | +0.027 | +0.018 | $4.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 21 | 0.255 | 0.243 | +0.034 | +0.021 | $6.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.070 | 0.063 | +0.016 | +0.010 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Victor Olofsson: 1+ goals NO | 74 | 0.780 | 0.769 | +0.027 | +0.015 | $15.82 | FUNDED_RESEARCH | $4 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (11.36 vs 5.65 bp); despite a smaller raw edge (+0.027 vs +0.034/contract); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV13NSHVGK-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (5.65 vs 2.56 bp); despite a smaller raw edge (+0.034 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV13NSHVGK-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: VGK offense suppressed (<= 2 goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV13NSHVGK-9|yes; why: higher confidence-adjusted growth (4.35 vs 0.07 bp); despite a smaller raw edge (+0.016 vs +0.019/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.894 vs 0.369); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NSH offense suppressed (<= 2 goals)
- **Victor Olofsson: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no selected over player prop KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.91 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV13NSHVGK-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:OFFENSE_4PLUS (p 0.4795): highest fidelity KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3098): highest fidelity KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4678): highest fidelity KXNHLAST-26NOV13NSHVGK-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV13NSHVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.126)
- KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.196)
- KXNHLGOAL-26NOV13NSHVGK-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4678, phi -0.127)
- KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4795, phi -0.2)
- override: Player prop expression KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no selected over player prop KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.91 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.97 (adj +2.06) on $50.00, P(profit) 0.5185, adj growth 16.4 bp · B EV +4.03 (adj +2.57) on $28.85, P(profit) 0.3698, adj growth 22.1 bp · C EV +2.00 (adj +1.19) on $34.19, P(profit) 0.6498, adj growth 10.4 bp · R EV +0.14 (adj +0.08) on $4.00, P(profit) 0.7803, adj growth 2.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
