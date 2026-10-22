# Market taxonomy

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

Every game-scoped contract is converted into an explicit `ContractSpec` (`market_audit/taxonomy.py`). Authority order: Kalshi's `series_ticker` -> structured `strike_type` / `floor_strike` /
`custom_strike` -> the contract's own rules text, parsed to CROSS-CHECK the structured fields (threshold, clubs, date, period wording, overtime / shootout / void wording). A disagreement
downgrades the spec to UNRESOLVED; the ticker is used only for game scope. Result: **every game-scoped contract is PROVEN** (structured strike and rules wording agree).

| family | what YES means | overtime | shootout | void rule |
|---|---|---|---|---|
| game_winner (KXNHLGAME) | club wins the official final | counts | decides the game | postponed >48 h / cancelled: fair price |
| game_spread (KXNHLSPREAD) | club wins by MORE than x goals (x = 1.5, 2.5, ...) | counts | a shootout win is a one-goal margin, so never > 1.5 | as above |
| game_total (KXNHLTOTAL) | both clubs score MORE than x | counts | winner is credited ONE goal | as above |
| team_total (KXNHLTEAMTOTAL) | club scores MORE than x | counts | winner is credited ONE goal | as above |
| game_overtime (KXNHLOT) | an overtime period is played (opening faceoff taken) | is the event | n/a | as above |
| game_early_goal (KXNHLF10G) | a goal in the first period before 10:00 elapsed (10:00 itself excluded) | n/a | n/a | as above |
| period_winner / spread / total (KXNHL{1,2,3}P*) | club wins / wins by > x / both score > x in that period; `-TIE` leg = equal goals | never counts (P3 states it) | never counts | as above |
| player_goals / assists / points (KXNHLGOAL/AST/PTS) | official N+ stat line | counts | never counts | fair price only if the player is "active but never enters"; a scratch is NOT addressed |
| goalie_saves (KXNHLSAVE) | goalie records N+ saves | counts | n/a | same |
| first_goal (KXNHLFIRSTGOAL) | player scores the game's first goal | counts | n/a | rule silent if no goal before a shootout |

Goal-scorer families (`player_goals`, `first_goal`) are included in the research dataset and **never recommended**.

### Spec counts

| series | family | kind | period | semantics | contracts |
|---|---|---|---|---|---|
| KXNHL1P | period_winner | period_winner | P1 | PROVEN | 495 |
| KXNHL1PSPREAD | period_spread | period_spread | P1 | PROVEN | 369 |
| KXNHL1PTOTAL | period_total | period_total | P1 | PROVEN | 717 |
| KXNHL2P | period_winner | period_winner | P2 | PROVEN | 495 |
| KXNHL2PSPREAD | period_spread | period_spread | P2 | PROVEN | 406 |
| KXNHL2PTOTAL | period_total | period_total | P2 | PROVEN | 788 |
| KXNHL3P | period_winner | period_winner | P3 | PROVEN | 495 |
| KXNHL3PSPREAD | period_spread | period_spread | P3 | PROVEN | 431 |
| KXNHL3PTOTAL | period_total | period_total | P3 | PROVEN | 770 |
| KXNHLAST | player_assists | player_stat | FULL | PROVEN | 5,014 |
| KXNHLF10G | game_early_goal | early_goal | P1 | PROVEN | 165 |
| KXNHLFIRSTGOAL | first_goal | first_goal | FULL | PROVEN | 5,450 |
| KXNHLGAME | game_winner | winner | FULL | PROVEN | 396 |
| KXNHLGOAL | player_goals | player_stat | FULL | PROVEN | 8,510 |
| KXNHLOT | game_overtime | overtime | FULL | PROVEN | 165 |
| KXNHLPTS | player_points | player_stat | FULL | PROVEN | 6,394 |
| KXNHLSAVE | goalie_saves | player_stat | FULL | PROVEN | 391 |
| KXNHLSPREAD | game_spread | spread | FULL | PROVEN | 1,227 |
| KXNHLTEAMTOTAL | team_total | team_total | FULL | PROVEN | 1,650 |
| KXNHLTOTAL | game_total | total | FULL | PROVEN | 1,664 |

Out of scope by design: season champion / awards / player-season stats (a different instrument class), and parlay/combo series (none appear on the archived boards).
