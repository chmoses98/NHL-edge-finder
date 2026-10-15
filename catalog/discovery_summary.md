# Kalshi NHL discovery summary

- discovered_at: `2026-10-15T21:46:14Z`  ontology: `2026.09.29.2`  requests: 165
- series enumerated: 15154; NHL series: 78; markets scanned: 4842

## Support states (coverage invariant)

| support | markets |
|---|---:|
| MODELABLE | 583 |
| BUILDABLE | 14 |
| RESEARCH | 3352 |
| UNMODELABLE | 548 |
| UNRESOLVED | 345 |

## NHL series

| series | family | support | fee | unopened | open | closed | settled | strike_types | parse |
|---|---|---|---|---:|---:|---:|---:|---|---|
| KXCANADACUP | season_champion | RESEARCH | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXCONNSMYTHE | season_awards | UNMODELABLE | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXESPYNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNBANHL | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 300 | 0 | 0 | custom | {'low': 300} |
| KXNEXTTEAMNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 263 | 0 | 0 | structured | {'low': 263} |
| KXNHL | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHL1P | period_winner | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | structured | {'high': 42} |
| KXNHL1PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL1PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 28 | 0 | 0 | greater | {'high': 28} |
| KXNHL1PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | greater | {'high': 42} |
| KXNHL1STTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2OT | game_multi_overtime | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2P | period_winner | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | structured | {'high': 42} |
| KXNHL2PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 28 | 0 | 0 | greater | {'high': 28} |
| KXNHL2PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | greater | {'high': 42} |
| KXNHL30COMEBACK | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3P | period_winner | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | structured | {'high': 42} |
| KXNHL3PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 28 | 0 | 0 | greater | {'high': 28} |
| KXNHL3PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 42 | 0 | 0 | greater | {'high': 42} |
| KXNHL4NATIONS | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLADAMS | season_awards | UNMODELABLE | quadratic/1 | 0 | 32 | 0 | 0 | custom | {'low': 32} |
| KXNHLANYGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLAST | player_assists | RESEARCH | quadratic/1 | 0 | 369 | 0 | 0 | greater | {'high': 369} |
| KXNHLATLANTIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLCALDER | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured,custom | {'low': 40} |
| KXNHLCENTRAL | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLDRAFTPICK | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLDRAFTTOP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLEAST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLEXPANSION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXNHLF10G | game_early_goal | RESEARCH | quadratic/1 | 0 | 14 | 0 | 0 | greater_or_equal | {'high': 14} |
| KXNHLFINALSEXACT | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLFIRSTGOAL | first_goal | RESEARCH | quadratic/1 | 0 | 405 | 0 | 0 | structured | {'high': 405} |
| KXNHLGAME | game_winner | MODELABLE | quadratic_with_maker_fees/1 | 0 | 92 | 0 | 0 | structured | {'high': 92} |
| KXNHLGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 704 | 0 | 0 | greater | {'high': 704} |
| KXNHLHART | season_awards | UNMODELABLE | quadratic/1 | 0 | 29 | 0 | 0 | structured | {'low': 29} |
| KXNHLLINDSAY | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 28 | 0 | 0 | structured | {'low': 28} |
| KXNHLMENTION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLMETROPOLITAN | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLMVP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTGM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 33 | 0 | 0 | structured | {'low': 33} |
| KXNHLNORRIS | season_awards | UNMODELABLE | quadratic/1 | 0 | 30 | 0 | 0 | structured | {'low': 30} |
| KXNHLOT | game_overtime | BUILDABLE | quadratic/1 | 0 | 14 | 0 | 0 | greater | {'high': 14} |
| KXNHLOVERTIME | game_overtime | BUILDABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPACIFIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLPLAYOFF | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPLAYOFFGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPRES | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPRICE | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPSEASONGOALS | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 17 | 0 | 0 | greater | {'low': 17} |
| KXNHLPTS | player_points | RESEARCH | quadratic/1 | 0 | 524 | 0 | 0 | greater | {'high': 524} |
| KXNHLRECORDWORST | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLRETIRE | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLRICHARD | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLROSS | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLSAVE | goalie_saves | RESEARCH | quadratic/1 | 0 | 22 | 0 | 0 | greater | {'high': 22} |
| KXNHLSAVES | goalie_saves | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSEASONGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 87 | 0 | 0 | greater,structured | {'low': 87} |
| KXNHLSEASONPPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 90 | 0 | 0 | greater | {'low': 90} |
| KXNHLSEASONPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 320 | 0 | 0 | greater_or_equal | {'low': 320} |
| KXNHLSERIES | playoff_series | RESEARCH | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESGAMES | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESOT | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSCORE | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSPREAD | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOAL | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOALS | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSPREAD | game_spread | MODELABLE | quadratic/1 | 0 | 108 | 0 | 0 | greater | {'high': 108} |
| KXNHLTEAMTOTAL | team_total | MODELABLE | quadratic/1 | 0 | 140 | 0 | 0 | greater | {'high': 140} |
| KXNHLTOTAL | game_total | MODELABLE | quadratic/1 | 0 | 243 | 0 | 0 | greater | {'high': 243} |
| KXNHLVEZINA | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLWEST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLWINS | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLWSTREAK | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXTEAMSINSC | season_champion | RESEARCH | quadratic/1 | 0 | 256 | 0 | 0 | custom | {'low': 256} |

## Title templates per series

### KXCANADACUP — Canada winning Stanley Cup
- (1) Will a Canadian team win the NAME® by the end of the # season?
- samples: KXCANADACUP-30
- sample fields: `{"ticker": "KXCANADACUP-30", "event_ticker": "KXCANADACUP-30", "market_type": "binary", "title": "Will a Canadian team win the Stanley Cup\u00ae by the end of the 2030 season?", "subtitle": "Before 2031", "yes_sub_title": "Before 2031", "no_sub_title": "Before 2031", "status": "active", "open_time": "2025-06-13T14:00:00Z", "close_time": "2030-06-30T03:59:00Z", "expected_expiration_time": "2030-06-30T14:00:00Z", "result": "", "rules_primary": "If a Canadian hockey team wins the Stanley Cup\u00ae after Issuance and before Jun 30, 2030, then the market resolves to Yes."}`

### KXCONNSMYTHE — Conn Smythe trophy

### KXESPYNHL — BEST NHL PLAYER‬

### KXNBANHL — NBA + NHL Champion Combo
- (14) NAME/NHL Champion: NAME/NAME
- (4) NAME/NHL Champion: NAME/Washington
- (4) NAME/NHL Champion: NAME/Vegas
- (4) NAME/NHL Champion: NAME/Montreal
- (4) NAME/NHL Champion: NAME/Minnesota
- (4) NAME/NHL Champion: NAME/Florida
- (4) NAME/NHL Champion: NAME/Edmonton
- (4) NAME/NHL Champion: NAME/Dallas
- samples: KXNBANHL-27-TORWSH, KXNBANHL-27-TORVGK, KXNBANHL-27-TORUTA, KXNBANHL-27-TORTB, KXNBANHL-27-TORSJ, KXNBANHL-27-TORNJ
- sample fields: `{"ticker": "KXNBANHL-27-TORWSH", "event_ticker": "KXNBANHL-27", "market_type": "binary", "title": "Pro Basketball/NHL Champion: Toronto/Washington", "yes_sub_title": "Basketball: Toronto / Hockey: Washington", "no_sub_title": "Basketball: Toronto / Hockey: Washington", "strike_type": "custom", "custom_strike": {"basketball_team": "96c447dd-2cdd-4c58-a151-ef0df87de981", "hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-10-15T16:00:00Z", "close_time": "2027-08-07T14:00:00Z", "expected_expiration_time": "2027-07-31T14:00:00Z", "result": "", "rules_prim`

### KXNEXTTEAMNHL — Next Team NHL
- (230) What will be NAME's next team?
- (33) What will be Connor McDavid's next team?
- samples: KXNEXTTEAMNHL-26PLAINE92-WSH, KXNEXTTEAMNHL-26PLAINE92-WPG, KXNEXTTEAMNHL-26PLAINE92-VGK, KXNEXTTEAMNHL-26PLAINE92-VAN, KXNEXTTEAMNHL-26PLAINE92-UTA, KXNEXTTEAMNHL-26PLAINE92-TOR
- sample fields: `{"ticker": "KXNEXTTEAMNHL-26PLAINE92-WSH", "event_ticker": "KXNEXTTEAMNHL-26PLAINE92", "market_type": "binary", "title": "What will be Patrik Laine's next team?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-11T19:00:00Z", "close_time": "2026-11-01T04:59:00Z", "expected_expiration_time": "2026-11-01T15:00:00Z", "result": "", "rules_primary": "If Patrik Laine's next team is Washington Capitals before Nov 1, 2026, then `

### KXNHL — Stanley Cup
- (30) NAME win the #-# NAME® Finals?
- (1) NAME. NAME win the #-# NAME® Finals?
- (1) Will Montréal Canadiens win the #-# NAME® Finals?
- samples: KXNHL-27-WSH, KXNHL-27-WPG, KXNHL-27-VGK, KXNHL-27-VAN, KXNHL-27-UTA, KXNHL-27-TOR
- sample fields: `{"ticker": "KXNHL-27-WSH", "event_ticker": "KXNHL-27", "market_type": "binary", "title": "Will Washington Capitals win the 2026-27 Stanley Cup\u00ae Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-06-15T03:40:00Z", "close_time": "2029-06-30T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals wins the 2026-27 Stanley Cup\u00ae Finals, then the marke`

### KXNHL1P — NHL 1st Period Winner
- (14) #st period tie
- (4) NAME wins the #st period
- (1) Washington wins the #st period
- (1) Boston wins the #st period
- (1) Anaheim wins the #st period
- (1) Pittsburgh wins the #st period
- (1) Colorado wins the #st period
- (1) Vegas wins the #st period
- samples: KXNHL1P-26OCT17NJWSH-WSH, KXNHL1P-26OCT17NJWSH-TIE, KXNHL1P-26OCT17NJWSH-NJ, KXNHL1P-26OCT16BOSANA-TIE, KXNHL1P-26OCT16BOSANA-BOS, KXNHL1P-26OCT16BOSANA-ANA
- sample fields: `{"ticker": "KXNHL1P-26OCT17NJWSH-WSH", "event_ticker": "KXNHL1P-26OCT17NJWSH", "market_type": "binary", "title": "Washington wins the 1st period", "yes_sub_title": "Washington", "no_sub_title": "Washington", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If Washington wins the 1st period of the New Jersey vs Washington NHL game originally scheduled for Oct 17, 20`

### KXNHL1PBTTS — NHL Both Teams to Score in 1st Period

### KXNHL1PSPREAD — 1st Period Spread
- (4) NAME wins #st Period by over # goals
- (1) Washington wins #st Period by over # goals
- (1) Boston wins #st Period by over # goals
- (1) Anaheim wins #st Period by over # goals
- (1) Pittsburgh wins #st Period by over # goals
- (1) Colorado wins #st Period by over # goals
- (1) Vegas wins #st Period by over # goals
- (1) Calgary wins #st Period by over # goals
- samples: KXNHL1PSPREAD-26OCT17NJWSH-WSH2, KXNHL1PSPREAD-26OCT17NJWSH-NJ2, KXNHL1PSPREAD-26OCT16BOSANA-BOS2, KXNHL1PSPREAD-26OCT16BOSANA-ANA2, KXNHL1PSPREAD-26OCT16PITCOL-PIT2, KXNHL1PSPREAD-26OCT16PITCOL-COL2
- sample fields: `{"ticker": "KXNHL1PSPREAD-26OCT17NJWSH-WSH2", "event_ticker": "KXNHL1PSPREAD-26OCT17NJWSH", "market_type": "binary", "title": "Washington wins 1st Period by over 1.5 goals", "yes_sub_title": "Washington wins by over 1.5 goals", "no_sub_title": "Washington wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If Washington wins `

### KXNHL1PTOTAL — NHL 1st Period Total
- (42) #st Period: Over # goals scored
- samples: KXNHL1PTOTAL-26OCT17NJWSH-3, KXNHL1PTOTAL-26OCT17NJWSH-2, KXNHL1PTOTAL-26OCT17NJWSH-1, KXNHL1PTOTAL-26OCT16BOSANA-3, KXNHL1PTOTAL-26OCT16BOSANA-2, KXNHL1PTOTAL-26OCT16BOSANA-1
- sample fields: `{"ticker": "KXNHL1PTOTAL-26OCT17NJWSH-3", "event_ticker": "KXNHL1PTOTAL-26OCT17NJWSH", "market_type": "binary", "title": "1st Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 1st Period of the New Jersey vs Washington NHL game originally scheduled for Oct 17, 202`

### KXNHL1STTEAM — All NHL First Team

### KXNHL2OT — NHL Double Overtime

### KXNHL2P — NHL 2nd Period Winner
- (14) #nd period tie
- (4) NAME wins the #nd period
- (1) Washington wins the #nd period
- (1) Boston wins the #nd period
- (1) Anaheim wins the #nd period
- (1) Pittsburgh wins the #nd period
- (1) Colorado wins the #nd period
- (1) Vegas wins the #nd period
- samples: KXNHL2P-26OCT17NJWSH-WSH, KXNHL2P-26OCT17NJWSH-TIE, KXNHL2P-26OCT17NJWSH-NJ, KXNHL2P-26OCT16BOSANA-TIE, KXNHL2P-26OCT16BOSANA-BOS, KXNHL2P-26OCT16BOSANA-ANA
- sample fields: `{"ticker": "KXNHL2P-26OCT17NJWSH-WSH", "event_ticker": "KXNHL2P-26OCT17NJWSH", "market_type": "binary", "title": "Washington wins the 2nd period", "yes_sub_title": "Washington", "no_sub_title": "Washington", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If Washington wins the 2nd period of the New Jersey vs Washington NHL game originally scheduled for Oct 17, 20`

### KXNHL2PBTTS — NHL Both Teams to Score in 2nd Period

### KXNHL2PSPREAD — 2nd Period Spread
- (4) NAME wins #nd Period by over # goals
- (1) Washington wins #nd Period by over # goals
- (1) Boston wins #nd Period by over # goals
- (1) Anaheim wins #nd Period by over # goals
- (1) Pittsburgh wins #nd Period by over # goals
- (1) Colorado wins #nd Period by over # goals
- (1) Vegas wins #nd Period by over # goals
- (1) Calgary wins #nd Period by over # goals
- samples: KXNHL2PSPREAD-26OCT17NJWSH-WSH2, KXNHL2PSPREAD-26OCT17NJWSH-NJ2, KXNHL2PSPREAD-26OCT16BOSANA-BOS2, KXNHL2PSPREAD-26OCT16BOSANA-ANA2, KXNHL2PSPREAD-26OCT16PITCOL-PIT2, KXNHL2PSPREAD-26OCT16PITCOL-COL2
- sample fields: `{"ticker": "KXNHL2PSPREAD-26OCT17NJWSH-WSH2", "event_ticker": "KXNHL2PSPREAD-26OCT17NJWSH", "market_type": "binary", "title": "Washington wins 2nd Period by over 1.5 goals", "yes_sub_title": "Washington wins by over 1.5 goals", "no_sub_title": "Washington wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If Washington wins `

### KXNHL2PTOTAL — 2nd Period Total
- (42) #nd Period: Over # goals scored
- samples: KXNHL2PTOTAL-26OCT17NJWSH-3, KXNHL2PTOTAL-26OCT17NJWSH-2, KXNHL2PTOTAL-26OCT17NJWSH-1, KXNHL2PTOTAL-26OCT16BOSANA-3, KXNHL2PTOTAL-26OCT16BOSANA-2, KXNHL2PTOTAL-26OCT16BOSANA-1
- sample fields: `{"ticker": "KXNHL2PTOTAL-26OCT17NJWSH-3", "event_ticker": "KXNHL2PTOTAL-26OCT17NJWSH", "market_type": "binary", "title": "2nd Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 2nd Period of the New Jersey vs Washington NHL game originally scheduled for Oct 17, 202`

### KXNHL30COMEBACK — NHL 3-0 Series Comeback

### KXNHL3P — NHL 3rd Period Winner
- (14) #rd period tie
- (4) NAME wins the #rd period
- (1) Washington wins the #rd period
- (1) Boston wins the #rd period
- (1) Anaheim wins the #rd period
- (1) Pittsburgh wins the #rd period
- (1) Colorado wins the #rd period
- (1) Vegas wins the #rd period
- samples: KXNHL3P-26OCT17NJWSH-WSH, KXNHL3P-26OCT17NJWSH-TIE, KXNHL3P-26OCT17NJWSH-NJ, KXNHL3P-26OCT16BOSANA-TIE, KXNHL3P-26OCT16BOSANA-BOS, KXNHL3P-26OCT16BOSANA-ANA
- sample fields: `{"ticker": "KXNHL3P-26OCT17NJWSH-WSH", "event_ticker": "KXNHL3P-26OCT17NJWSH", "market_type": "binary", "title": "Washington wins the 3rd period", "yes_sub_title": "Washington", "no_sub_title": "Washington", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If Washington wins the 3rd period (excluding overtime) of the New Jersey vs Washington NHL game originally sch`

### KXNHL3PBTTS — NHL Both Teams to Score in 3rd Period

### KXNHL3PSPREAD — NHL 3rd Period Spread
- (4) NAME wins #rd Period by over # goals
- (1) Washington wins #rd Period by over # goals
- (1) Boston wins #rd Period by over # goals
- (1) Anaheim wins #rd Period by over # goals
- (1) Pittsburgh wins #rd Period by over # goals
- (1) Colorado wins #rd Period by over # goals
- (1) Vegas wins #rd Period by over # goals
- (1) Calgary wins #rd Period by over # goals
- samples: KXNHL3PSPREAD-26OCT17NJWSH-WSH2, KXNHL3PSPREAD-26OCT17NJWSH-NJ2, KXNHL3PSPREAD-26OCT16BOSANA-BOS2, KXNHL3PSPREAD-26OCT16BOSANA-ANA2, KXNHL3PSPREAD-26OCT16PITCOL-PIT2, KXNHL3PSPREAD-26OCT16PITCOL-COL2
- sample fields: `{"ticker": "KXNHL3PSPREAD-26OCT17NJWSH-WSH2", "event_ticker": "KXNHL3PSPREAD-26OCT17NJWSH", "market_type": "binary", "title": "Washington wins 3rd Period by over 1.5 goals", "yes_sub_title": "Washington wins by over 1.5 goals", "no_sub_title": "Washington wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If Washington wins `

### KXNHL3PTOTAL — 3rd Period Total
- (42) #rd Period: Over # goals scored
- samples: KXNHL3PTOTAL-26OCT17NJWSH-3, KXNHL3PTOTAL-26OCT17NJWSH-2, KXNHL3PTOTAL-26OCT17NJWSH-1, KXNHL3PTOTAL-26OCT16BOSANA-3, KXNHL3PTOTAL-26OCT16BOSANA-2, KXNHL3PTOTAL-26OCT16BOSANA-1
- sample fields: `{"ticker": "KXNHL3PTOTAL-26OCT17NJWSH-3", "event_ticker": "KXNHL3PTOTAL-26OCT17NJWSH", "market_type": "binary", "title": "3rd Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 3rd Period of the New Jersey vs Washington NHL game originally scheduled for Oct 17, 202`

### KXNHL4NATIONS — 4 nations face off

### KXNHLADAMS — NHL Jack Adams Award
- (29) NAME: NAME wins
- (1) NAME: Todd McLellan wins
- (1) NAME: Peter DeBoer wins
- (1) NAME: NAME. Louis wins
- samples: KXNHLADAMS-27-TMCL, KXNHLADAMS-27-TGRE, KXNHLADAMS-27-SKEE, KXNHLADAMS-27-SCAR, KXNHLADAMS-27-SARN, KXNHLADAMS-27-RWAR
- sample fields: `{"ticker": "KXNHLADAMS-27-TMCL", "event_ticker": "KXNHLADAMS-27", "market_type": "binary", "title": "Jack Adams Award: Todd McLellan wins", "subtitle": "::", "yes_sub_title": "Todd McLellan", "no_sub_title": "Todd McLellan", "strike_type": "custom", "custom_strike": {"Person": "Todd McLellan"}, "status": "active", "open_time": "2026-09-28T22:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Todd McLellan wins the NHL Jack Adams Award in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLANYGOAL — Pro Hockey Goalscorer

### KXNHLAST — Pro Hockey Assists
- (345) NAME: #+ assists
- (3) Connor McDavid: #+ assists
- (2) Jonathan Lekkerimäki: #+ assists
- (2) Ryan O'Reilly: #+ assists
- (2) Alex DeBrincat: #+ assists
- (2) Jared McCann: #+ assists
- (2) J.T. Miller: #+ assists
- (2) Ryan McLeod: #+ assists
- samples: KXNHLAST-26OCT15CGYVGK-VGKWKARLSSON71-2, KXNHLAST-26OCT15CGYVGK-VGKWKARLSSON71-1, KXNHLAST-26OCT15UTAEDM-EDMRSHEA6-2, KXNHLAST-26OCT15UTAEDM-EDMRSHEA6-1, KXNHLAST-26OCT15UTAEDM-UTAKYAMAMOTO56-1, KXNHLAST-26OCT15PHIDET-DETBCHIAROT8-1
- sample fields: `{"ticker": "KXNHLAST-26OCT15CGYVGK-VGKWKARLSSON71-2", "event_ticker": "KXNHLAST-26OCT15CGYVGK", "market_type": "binary", "title": "William Karlsson: 2+ assists", "yes_sub_title": "William Karlsson: 2+", "no_sub_title": "William Karlsson: 2+", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_player": "10814396-96db-4b0b-85a3-5107f874ed10", "hockey_team": "d599b5cc-5e06-4679-9303-4d5dad7c4cce"}, "status": "active", "open_time": "2026-10-15T21:10:00Z", "close_time": "2026-10-18T02:00:00Z", "expected_expiration_time": "2026-10-16T08:00:00Z", "result": "", "rules_primary": "`

### KXNHLATLANTIC — NHL Atlantic Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLATLANTIC-27-TOR, KXNHLATLANTIC-27-TB, KXNHLATLANTIC-27-OTT, KXNHLATLANTIC-27-MTL, KXNHLATLANTIC-27-FLA, KXNHLATLANTIC-27-DET
- sample fields: `{"ticker": "KXNHLATLANTIC-27-TOR", "event_ticker": "KXNHLATLANTIC-27", "market_type": "binary", "title": "Will the Toronto Maple Leafs win the Atlantic Division?", "yes_sub_title": "Toronto Maple Leafs", "no_sub_title": "Toronto Maple Leafs", "strike_type": "structured", "custom_strike": {"hockey_team": "f61f9daa-407b-4c46-96e8-feee19cd6f51"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Toronto Maple Leafs win the 2026-27 NHL Atlantic Division, then the `

### KXNHLCALDER — NHL Calder Memorial Trophy
- (36) NAME: NAME wins
- (1) NAME: Viggo Björck wins
- (1) NAME: NAME-Nygård wins
- (1) NAME: Gavin McKenna wins
- (1) NAME: Adam Engström wins
- samples: KXNHLCALDER-27-ZBUIUM24, KXNHLCALDER-27-VEKLUND, KXNHLCALDER-27-VBJORCK, KXNHLCALDER-27-TLINDSTEIN, KXNHLCALDER-27-TIGINLA, KXNHLCALDER-27-TCONNELLY
- sample fields: `{"ticker": "KXNHLCALDER-27-ZBUIUM24", "event_ticker": "KXNHLCALDER-27", "market_type": "binary", "title": "Calder Memorial Trophy: Zeev Buium wins", "subtitle": "::", "yes_sub_title": "Zeev Buium", "no_sub_title": "Zeev Buium", "strike_type": "structured", "custom_strike": {"hockey_player": "4e4ad45c-1cda-4e0b-89c3-4e6c27740027"}, "status": "active", "open_time": "2026-09-30T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zeev Buium wins the NHL Calder Memorial Trophy in the 2026-27 NHL season, then the ma`

### KXNHLCENTRAL — NHL Central Division Winner
- (7) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLCENTRAL-27-WPG, KXNHLCENTRAL-27-UTA, KXNHLCENTRAL-27-STL, KXNHLCENTRAL-27-NSH, KXNHLCENTRAL-27-MIN, KXNHLCENTRAL-27-DAL
- sample fields: `{"ticker": "KXNHLCENTRAL-27-WPG", "event_ticker": "KXNHLCENTRAL-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Central Division?", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Central Division, then the market resolves to Yes."}`

### KXNHLDRAFTPICK — Pro Hockey Draft Pick

### KXNHLDRAFTTOP — Pro Hockey Top Pick

### KXNHLEAST — Eastern Conference Championship
- (16) Will the NAME win the NAME?
- samples: KXNHLEAST-27-WSH, KXNHLEAST-27-TOR, KXNHLEAST-27-TB, KXNHLEAST-27-PIT, KXNHLEAST-27-PHI, KXNHLEAST-27-OTT
- sample fields: `{"ticker": "KXNHLEAST-27-WSH", "event_ticker": "KXNHLEAST-27", "market_type": "binary", "title": "Will the Washington Capitals win the Eastern Conference Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Eastern Conference Finals, t`

### KXNHLEXPANSION — NHL Expansion
- (1) NAME receive an NHL expansion team before #?
- samples: KXNHLEXPANSION-27JAN01HOU-Y
- sample fields: `{"ticker": "KXNHLEXPANSION-27JAN01HOU-Y", "event_ticker": "KXNHLEXPANSION-27JAN01HOU", "market_type": "binary", "title": "Will Houston receive an NHL expansion team before 2027?", "yes_sub_title": "Houston to get an expansion team before 2027", "no_sub_title": "Houston to get an expansion team before 2027", "status": "active", "open_time": "2026-09-01T01:00:00Z", "close_time": "2027-01-01T04:59:00Z", "expected_expiration_time": "2027-01-01T15:00:00Z", "result": "", "rules_primary": "If the NHL officially announces the award of an expansion team franchise to Houston before Jan 1, 2027, then the`

### KXNHLF10G — NHL Goal in First 10 Minutes
- (14) Either team to score in the first # minutes
- samples: KXNHLF10G-26OCT17NJWSH-Y, KXNHLF10G-26OCT16BOSANA-Y, KXNHLF10G-26OCT16PITCOL-Y, KXNHLF10G-26OCT15CGYVGK-Y, KXNHLF10G-26OCT15UTAEDM-Y, KXNHLF10G-26OCT15SJNSH-Y
- sample fields: `{"ticker": "KXNHLF10G-26OCT17NJWSH-Y", "event_ticker": "KXNHLF10G-26OCT17NJWSH", "market_type": "binary", "title": "Either team to score in the first 10 minutes", "yes_sub_title": "Goal in first 10 min", "no_sub_title": "Goal in first 10 min", "strike_type": "greater_or_equal", "floor_strike": 1, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If at least 1 goal is scored by either New Jersey or Washington during the first 10 minutes of the first period (from 0:00 `

### KXNHLFINALSEXACT — NHL Championship Series Score

### KXNHLFIRSTGOAL — NHL First Goal
- (380) NAME: NAME
- (1) NAME. Ivany: NAME
- (1) Brayden McNabb: NAME
- (1) MacKenzie Weegar: NAME
- (1) Jack McBain: NAME
- (1) Connor McDavid: NAME
- (1) Dylan DeMelo: NAME
- (1) Mason McTavish: NAME
- samples: KXNHLFIRSTGOAL-26OCT15SJNSH-SJNALLAN5, KXNHLFIRSTGOAL-26OCT15WPGCHI-WPGJSTIVANY6, KXNHLFIRSTGOAL-26OCT15WPGCHI-CHIFNAZAR91, KXNHLFIRSTGOAL-26OCT15WPGCHI-CHIEDELMASTRO38, KXNHLFIRSTGOAL-26OCT15SJNSH-NSHRSCHAEFER49, KXNHLFIRSTGOAL-26OCT15SEATB-TBELILLEBERG78
- sample fields: `{"ticker": "KXNHLFIRSTGOAL-26OCT15SJNSH-SJNALLAN5", "event_ticker": "KXNHLFIRSTGOAL-26OCT15SJNSH", "market_type": "binary", "title": "Nolan Allan: First Goalscorer", "yes_sub_title": "Nolan Allan", "no_sub_title": "Nolan Allan", "strike_type": "structured", "custom_strike": {"hockey_player": "044ca494-6f16-4cc7-a859-a1bc7a51bf6d", "hockey_team": "eb4bc183-5966-40eb-8bdb-3dd922ad1752"}, "status": "active", "open_time": "2026-10-15T19:52:00Z", "close_time": "2026-10-18T00:00:00Z", "expected_expiration_time": "2026-10-16T06:00:00Z", "result": "", "rules_primary": "If Nolan Allan scores the 1st go`

### KXNHLGAME — NHL Game
- (12) NAME wins
- (4) Philadelphia wins
- (4) Toronto wins
- (3) Ottawa wins
- (3) Florida wins
- (3) Buffalo wins
- (3) Vegas wins
- (3) Vancouver wins
- samples: KXNHLGAME-26OCT21FLAOTT-OTT, KXNHLGAME-26OCT21FLAOTT-FLA, KXNHLGAME-26OCT21PHIBUF-PHI, KXNHLGAME-26OCT21PHIBUF-BUF, KXNHLGAME-26OCT20TBVGK-VGK, KXNHLGAME-26OCT20TBVGK-TB
- sample fields: `{"ticker": "KXNHLGAME-26OCT21FLAOTT-OTT", "event_ticker": "KXNHLGAME-26OCT21FLAOTT", "market_type": "binary", "title": "Ottawa wins", "yes_sub_title": "Ottawa", "no_sub_title": "Ottawa", "strike_type": "structured", "custom_strike": {"hockey_team": "a2478063-2ded-4657-923b-e59de696ad21"}, "status": "active", "open_time": "2026-10-15T01:06:00Z", "close_time": "2026-10-23T23:30:00Z", "expected_expiration_time": "2026-10-22T02:30:00Z", "result": "", "rules_primary": "If Ottawa wins the Florida vs Ottawa NHL game originally scheduled for Oct 21, 2026, then the market resolves to Yes."}`

### KXNHLGOAL — NHL Goalscorer
- (660) NAME: #+ goals
- (3) Connor McDavid: #+ goals
- (3) Ryan O'Reilly: #+ goals
- (3) Alex DeBrincat: #+ goals
- (2) Jack McBain: #+ goals
- (2) Mason McTavish: #+ goals
- (2) Connor McMichael: #+ goals
- (2) Michael McCarron: #+ goals
- samples: KXNHLGOAL-26OCT15VANFLA-VANVMANCINI90-1, KXNHLGOAL-26OCT15SJNSH-SJNALLAN5-1, KXNHLGOAL-26OCT15WPGCHI-WPGJSTIVANY6-1, KXNHLGOAL-26OCT15WPGCHI-CHIFNAZAR91-1, KXNHLGOAL-26OCT15WPGCHI-CHIEDELMASTRO38-1, KXNHLGOAL-26OCT15SJNSH-NSHRSCHAEFER49-1
- sample fields: `{"ticker": "KXNHLGOAL-26OCT15VANFLA-VANVMANCINI90-1", "event_ticker": "KXNHLGOAL-26OCT15VANFLA", "market_type": "binary", "title": "Victor Mancini: 1+ goals", "yes_sub_title": "Victor Mancini: 1+", "no_sub_title": "Victor Mancini: 1+", "strike_type": "greater", "floor_strike": 0.5, "custom_strike": {"hockey_player": "10965e73-81a5-407b-b0aa-5ec354eacad3", "hockey_team": "2d6db4a4-99f2-4547-85f3-9913404577f9"}, "status": "active", "open_time": "2026-10-15T20:37:00Z", "close_time": "2026-10-17T23:00:00Z", "expected_expiration_time": "2026-10-16T05:00:00Z", "result": "", "rules_primary": "If Vict`

### KXNHLHART — NHL Hart Memorial Trophy
- (28) Who will win NAME?
- (1) NAME: NAME wins
- samples: KXNHLHART-27-ALAFRENIERE13, KXNHLHART-27-WNYLANDER88, KXNHLHART-27-SCROSBY87, KXNHLHART-27-QHUGHES43, KXNHLHART-27-PDOROFEYEV16, KXNHLHART-27-NSUZUKI14
- sample fields: `{"ticker": "KXNHLHART-27-ALAFRENIERE13", "event_ticker": "KXNHLHART-27", "market_type": "binary", "title": "Hart Memorial Trophy: Alexis Lafreniere wins", "yes_sub_title": "Alexis Lafreniere", "no_sub_title": "Alexis Lafreniere", "strike_type": "structured", "custom_strike": {"hockey_player": "10ed52fe-025d-4478-ac36-6a104f1fae78"}, "status": "active", "open_time": "2026-10-14T23:00:00Z", "close_time": "2027-06-30T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Alexis Lafreniere wins the NHL Hart Memorial Trophy in the 2026-27 NHL season, then`

### KXNHLLINDSAY — NHL Ted Lindsay Winner
- (26) NAME: NAME wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLLINDSAY-27-WNYLANDER88, KXNHLLINDSAY-27-SCROSBY87, KXNHLLINDSAY-27-QHUGHES43, KXNHLLINDSAY-27-PDOROFEYEV16, KXNHLLINDSAY-27-NSUZUKI14, KXNHLLINDSAY-27-NMACKINNON29
- sample fields: `{"ticker": "KXNHLLINDSAY-27-WNYLANDER88", "event_ticker": "KXNHLLINDSAY-27", "market_type": "binary", "title": "Ted Lindsay Award: William Nylander wins", "subtitle": "::", "yes_sub_title": "William Nylander", "no_sub_title": "William Nylander", "strike_type": "structured", "custom_strike": {"hockey_player": "1d6e76e2-3553-4992-b4f1-14e075811859"}, "status": "active", "open_time": "2026-10-08T02:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If William Nylander wins the NHL Ted Lindsay Award in the 2026-27 NHL `

### KXNHLMENTION — NHL Announcer Mentions

### KXNHLMETROPOLITAN — NHL Metropolitan Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLMETROPOLITAN-27-WSH, KXNHLMETROPOLITAN-27-PIT, KXNHLMETROPOLITAN-27-PHI, KXNHLMETROPOLITAN-27-NYR, KXNHLMETROPOLITAN-27-NYI, KXNHLMETROPOLITAN-27-NJ
- sample fields: `{"ticker": "KXNHLMETROPOLITAN-27-WSH", "event_ticker": "KXNHLMETROPOLITAN-27", "market_type": "binary", "title": "Will the Washington Capitals win the Metropolitan Division?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Metropolitan Div`

### KXNHLMVP — NHL Hart Memorial Trophy Winner

### KXNHLNEXTGM — Next NHL GM

### KXNHLNEXTTEAM — NHL Next Team
- (31) NAME' next team before Nov #, #: NAME
- (1) NAME' next team before Nov #, #: St. NAME
- (1) NAME' next team before Nov #, #: Retires / NAME
- samples: KXNHLNEXTTEAM-26QHUGHES43-WSH, KXNHLNEXTTEAM-26QHUGHES43-WPG, KXNHLNEXTTEAM-26QHUGHES43-VGK, KXNHLNEXTTEAM-26QHUGHES43-VAN, KXNHLNEXTTEAM-26QHUGHES43-UTA, KXNHLNEXTTEAM-26QHUGHES43-TOR
- sample fields: `{"ticker": "KXNHLNEXTTEAM-26QHUGHES43-WSH", "event_ticker": "KXNHLNEXTTEAM-26QHUGHES43", "market_type": "binary", "title": "Quinn Hughes' next team before Nov 1, 2026: Washington Capitals", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-26T00:00:00Z", "close_time": "2026-11-01T04:59:00Z", "expected_expiration_time": "2026-11-01T15:00:00Z", "result": "", "rules_primary": "If Quinn Hughes' \nnext team is the Washington Ca`

### KXNHLNORRIS — NHL James Norris Memorial Trophy
- (28) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Charlie McAvoy wins
- samples: KXNHLNORRIS-27-ZWERENSKI8, KXNHLNORRIS-27-VHEDMAN77, KXNHLNORRIS-27-THARLEY55, KXNHLNORRIS-27-STHEODORE27, KXNHLNORRIS-27-RSANDIN38, KXNHLNORRIS-27-RJOSI59
- sample fields: `{"ticker": "KXNHLNORRIS-27-ZWERENSKI8", "event_ticker": "KXNHLNORRIS-27", "market_type": "binary", "title": "James Norris Memorial Trophy: Zach Werenski wins", "subtitle": "::", "yes_sub_title": "Zach Werenski", "no_sub_title": "Zach Werenski", "strike_type": "structured", "custom_strike": {"hockey_player": "036e0c69-c86a-4ab1-8f63-c6d55b72fe09"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zach Werenski wins the NHL James Norris Memorial Trophy in the 2026-`

### KXNHLOT — NHL Overtime
- (14) Game goes to overtime
- samples: KXNHLOT-26OCT17NJWSH-1, KXNHLOT-26OCT16BOSANA-1, KXNHLOT-26OCT16PITCOL-1, KXNHLOT-26OCT15CGYVGK-1, KXNHLOT-26OCT15UTAEDM-1, KXNHLOT-26OCT15SJNSH-1
- sample fields: `{"ticker": "KXNHLOT-26OCT17NJWSH-1", "event_ticker": "KXNHLOT-26OCT17NJWSH", "market_type": "binary", "title": "Game goes to overtime", "yes_sub_title": "Game goes to overtime", "no_sub_title": "Game goes to overtime", "strike_type": "greater", "floor_strike": 0.5, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If at least 1 overtime period is played in the New Jersey vs Washington NHL game originally scheduled for Oct 17, 2026, then the market resolves to Yes."}`

### KXNHLOVERTIME — NHL Overtime

### KXNHLPACIFIC — NHL Pacific Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLPACIFIC-27-VGK, KXNHLPACIFIC-27-VAN, KXNHLPACIFIC-27-SJ, KXNHLPACIFIC-27-SEA, KXNHLPACIFIC-27-LA, KXNHLPACIFIC-27-EDM
- sample fields: `{"ticker": "KXNHLPACIFIC-27-VGK", "event_ticker": "KXNHLPACIFIC-27", "market_type": "binary", "title": "Will the Vegas Golden Knights win the Pacific Division?", "yes_sub_title": "Vegas Golden Knights", "no_sub_title": "Vegas Golden Knights", "strike_type": "structured", "custom_strike": {"hockey_team": "d599b5cc-5e06-4679-9303-4d5dad7c4cce"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Vegas Golden Knights win the 2026-27 NHL Pacific Division, then the `

### KXNHLPLAYOFF — Playoff Qualifier
- (30) Will the NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the St. NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the Montréal Canadiens qualify for the playoffs in the #-# NHL season?
- samples: KXNHLPLAYOFF-27-WSH, KXNHLPLAYOFF-27-WPG, KXNHLPLAYOFF-27-VGK, KXNHLPLAYOFF-27-VAN, KXNHLPLAYOFF-27-UTA, KXNHLPLAYOFF-27-TOR
- sample fields: `{"ticker": "KXNHLPLAYOFF-27-WSH", "event_ticker": "KXNHLPLAYOFF-27", "market_type": "binary", "title": "Will the Washington Capitals qualify for the playoffs in the 2026-27 NHL season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals qualify for the playoffs `

### KXNHLPLAYOFFGOALS — NHL Playoffs Goal Leader (by Round)

### KXNHLPRES — NHL President's Trophy Winner
- (30) Will the NAME win the Presidents' Trophy?
- (1) Will the St. NAME win the Presidents' Trophy?
- (1) Will the Montréal Canadiens win the Presidents' Trophy?
- samples: KXNHLPRES-27-WSH, KXNHLPRES-27-WPG, KXNHLPRES-27-VGK, KXNHLPRES-27-VAN, KXNHLPRES-27-UTA, KXNHLPRES-27-TOR
- sample fields: `{"ticker": "KXNHLPRES-27-WSH", "event_ticker": "KXNHLPRES-27", "market_type": "binary", "title": "Will the Washington Capitals win the Presidents' Trophy?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-14T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Presidents' Trophy, then the market`

### KXNHLPRICE — NHL Ticket Prices

### KXNHLPSEASONGOALS — Player Goals Scored in Season
- (17) NAME: #+ goals in #-# NHL regular season?
- samples: KXNHLPSEASONGOALS-27MCELEBRINI71-60, KXNHLPSEASONGOALS-27MCELEBRINI71-55, KXNHLPSEASONGOALS-27MCELEBRINI71-50, KXNHLPSEASONGOALS-27MCELEBRINI71-45, KXNHLPSEASONGOALS-27MCELEBRINI71-40, KXNHLPSEASONGOALS-27MCELEBRINI71-35
- sample fields: `{"ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71-60", "event_ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71", "market_type": "binary", "title": "Macklin Celebrini: 60+ goals in 2026-27 NHL regular season?", "subtitle": "Macklin Celebrini", "yes_sub_title": "60+ goals", "no_sub_title": "60+ goals", "strike_type": "greater", "floor_strike": 59.5, "custom_strike": {"hockey_player": "264560c4-3624-4c01-924e-879a08799f16"}, "status": "active", "open_time": "2026-10-09T01:30:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Mac`

### KXNHLPTS — Pro Hockey Points
- (487) NAME: #+ points
- (3) Connor McDavid: #+ points
- (3) Ryan O'Reilly: #+ points
- (3) Alex DeBrincat: #+ points
- (2) J.J. Moser: #+ points
- (2) Jonathan Lekkerimäki: #+ points
- (2) MacKenzie Weegar: #+ points
- (2) Mason McTavish: #+ points
- samples: KXNHLPTS-26OCT15CGYVGK-VGKWKARLSSON71-2, KXNHLPTS-26OCT15CGYVGK-VGKWKARLSSON71-1, KXNHLPTS-26OCT15UTAEDM-EDMRSHEA6-2, KXNHLPTS-26OCT15UTAEDM-EDMRSHEA6-1, KXNHLPTS-26OCT15UTAEDM-EDMMEKHOLM14-2, KXNHLPTS-26OCT15UTAEDM-EDMMEKHOLM14-1
- sample fields: `{"ticker": "KXNHLPTS-26OCT15CGYVGK-VGKWKARLSSON71-2", "event_ticker": "KXNHLPTS-26OCT15CGYVGK", "market_type": "binary", "title": "William Karlsson: 2+ points", "yes_sub_title": "William Karlsson: 2+", "no_sub_title": "William Karlsson: 2+", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_player": "10814396-96db-4b0b-85a3-5107f874ed10", "hockey_team": "d599b5cc-5e06-4679-9303-4d5dad7c4cce"}, "status": "active", "open_time": "2026-10-15T21:10:00Z", "close_time": "2026-10-18T02:00:00Z", "expected_expiration_time": "2026-10-16T08:00:00Z", "result": "", "rules_primary": "I`

### KXNHLRECORDWORST — Worst NHL Record
- (30) Will the NAME have the worst regular season record in the #-# season?
- (1) Will the St. NAME have the worst regular season record in the #-# season?
- (1) Will the Montréal Canadiens have the worst regular season record in the #-# season?
- samples: KXNHLRECORDWORST-27-WSH, KXNHLRECORDWORST-27-WPG, KXNHLRECORDWORST-27-VGK, KXNHLRECORDWORST-27-VAN, KXNHLRECORDWORST-27-UTA, KXNHLRECORDWORST-27-TOR
- sample fields: `{"ticker": "KXNHLRECORDWORST-27-WSH", "event_ticker": "KXNHLRECORDWORST-27", "market_type": "binary", "title": "Will the Washington Capitals have the worst regular season record in the 2026-27 season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-29T16:00:00Z", "close_time": "2027-05-31T14:00:00Z", "expected_expiration_time": "2027-05-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals have the `

### KXNHLRETIRE — NHL Retire

### KXNHLRICHARD — NHL Maurice "Rocket" Richard Trophy
- (37) Maurice "Rocket" NAME: NAME wins
- (1) Maurice "Rocket" NAME: Nathan MacKinnon wins
- (1) Maurice "Rocket" NAME: Connor McDavid wins
- (1) Maurice "Rocket" NAME: Alex DeBrincat wins
- samples: KXNHLRICHARD-27-ZHYMAN18, KXNHLRICHARD-27-WNYLANDER88, KXNHLRICHARD-27-WJOHNSTON53, KXNHLRICHARD-27-TTHOMPSON72, KXNHLRICHARD-27-SSTAMKOS91, KXNHLRICHARD-27-SREINHART13
- sample fields: `{"ticker": "KXNHLRICHARD-27-ZHYMAN18", "event_ticker": "KXNHLRICHARD-27", "market_type": "binary", "title": "Maurice \"Rocket\" Richard Trophy: Zach Hyman wins", "subtitle": "::", "yes_sub_title": "Zach Hyman", "no_sub_title": "Zach Hyman", "strike_type": "structured", "custom_strike": {"hockey_player": "2c3d67df-721b-4ea4-8aee-dea4a9715c82"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zach Hyman wins the NHL Maurice \"Rocket\" Richard Award in the 2026-27 `

### KXNHLROSS — NHL Art Ross Trophy
- (38) NAME: NAME wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLROSS-27-WNYLANDER88, KXNHLROSS-27-WJOHNSTON53, KXNHLROSS-27-TTHOMPSON72, KXNHLROSS-27-TSTUTZLE18, KXNHLROSS-27-SREINHART13, KXNHLROSS-27-SJARVIS24
- sample fields: `{"ticker": "KXNHLROSS-27-WNYLANDER88", "event_ticker": "KXNHLROSS-27", "market_type": "binary", "title": "Art Ross Trophy: William Nylander wins", "subtitle": "::", "yes_sub_title": "William Nylander", "no_sub_title": "William Nylander", "strike_type": "structured", "custom_strike": {"hockey_player": "1d6e76e2-3553-4992-b4f1-14e075811859"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If William Nylander wins the NHL Art Ross Trophy in the 2026-27 NHL season, th`

### KXNHLSAVE — Goaltender Saves
- (21) NAME: #+ saves
- (1) Leevi Meriläinen: #+ saves
- samples: KXNHLSAVE-26OCT15UTAEDM-UTAKVEJMELKA70-30, KXNHLSAVE-26OCT15UTAEDM-UTAKVEJMELKA70-28, KXNHLSAVE-26OCT15UTAEDM-UTAKVEJMELKA70-24, KXNHLSAVE-26OCT15CGYVGK-VGKCHART79-21, KXNHLSAVE-26OCT15PHIDET-PHIJWOLL53-26, KXNHLSAVE-26OCT15CGYVGK-CGYDWOLF32-27
- sample fields: `{"ticker": "KXNHLSAVE-26OCT15UTAEDM-UTAKVEJMELKA70-30", "event_ticker": "KXNHLSAVE-26OCT15UTAEDM", "market_type": "binary", "title": "Karel Vejmelka: 30+ saves", "yes_sub_title": "Karel Vejmelka: 30+", "no_sub_title": "Karel Vejmelka: 30+", "strike_type": "greater", "floor_strike": 29.5, "custom_strike": {"hockey_player": "a12a14aa-b7f5-42a5-a13e-e0a3d11618ad", "hockey_team": "7d20591d-c6fa-4b85-8d69-ff05fb3649ac"}, "status": "active", "open_time": "2026-10-15T20:22:00Z", "close_time": "2026-10-18T01:00:00Z", "expected_expiration_time": "2026-10-16T07:00:00Z", "result": "", "rules_primary": "I`

### KXNHLSAVES — Pro Hockey Saves

### KXNHLSEASONGOALS — Player to score X Goals in Season
- (81) NAME: #+ goals in #-# NHL regular season?
- (2) Nathan MacKinnon: #+ goals in #-# NHL regular season?
- (2) Connor McDavid: #+ goals in #-# NHL regular season?
- (2) Alex DeBrincat: #+ goals in #-# NHL regular season?
- samples: KXNHLSEASONGOALS-27C40-BTKACHUK8, KXNHLSEASONGOALS-27C20-WSMITH2, KXNHLSEASONGOALS-27C20-SCROSBY87, KXNHLSEASONGOALS-27C20-PKANE88, KXNHLSEASONGOALS-27C20-MSCHAEFER48, KXNHLSEASONGOALS-27C20-FNAZAR91
- sample fields: `{"ticker": "KXNHLSEASONGOALS-27C40-BTKACHUK8", "event_ticker": "KXNHLSEASONGOALS-27C40", "market_type": "binary", "title": "Brady Tkachuk: 40+ goals in 2026-27 NHL regular season?", "subtitle": "Brady Tkachuk:: FLA Panthers", "yes_sub_title": "Brady Tkachuk", "no_sub_title": "Brady Tkachuk", "strike_type": "greater", "floor_strike": 39.5, "custom_strike": {"hockey_player": "3d7e2b4d-d4a8-4fe2-904f-fbfb0773ed66"}, "status": "active", "open_time": "2026-10-14T16:35:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If B`

### KXNHLSEASONPPTS — Season Player Points
- (84) NAME: #+ points in #-# NHL regular season?
- (3) Nathan MacKinnon: #+ points in #-# NHL regular season?
- (3) Connor McDavid: #+ points in #-# NHL regular season?
- samples: KXNHLSEASONPPTS-27C110-ZWERENSKI8, KXNHLSEASONPPTS-27C110-WNYLANDER88, KXNHLSEASONPPTS-27C110-WJOHNSTON53, KXNHLSEASONPPTS-27C110-TSTUTZLE18, KXNHLSEASONPPTS-27C110-SCROSBY87, KXNHLSEASONPPTS-27C110-NSUZUKI14
- sample fields: `{"ticker": "KXNHLSEASONPPTS-27C110-ZWERENSKI8", "event_ticker": "KXNHLSEASONPPTS-27C110", "market_type": "binary", "title": "Zach Werenski: 110+ points in 2026-27 NHL regular season?", "subtitle": "Zach Werenski:: Columbus Blue Jackets", "yes_sub_title": "Zach Werenski", "no_sub_title": "Zach Werenski", "strike_type": "greater", "floor_strike": 109.5, "custom_strike": {"hockey_player": "036e0c69-c86a-4ab1-8f63-c6d55b72fe09"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_pr`

### KXNHLSEASONPTS — NHL Season Point Totals
- (10) Will the WSH Capitals NHL team earn at least # points in the #-# regular season?
- (10) Will the WPG Jets NHL team earn at least # points in the #-# regular season?
- (10) Will the VGK NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the VAN Canucks NHL team earn at least # points in the #-# regular season?
- (10) Will the UTA Mammoth NHL team earn at least # points in the #-# regular season?
- (10) Will the TOR NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the TB Lightning NHL team earn at least # points in the #-# regular season?
- (10) Will the STL Blues NHL team earn at least # points in the #-# regular season?
- samples: KXNHLSEASONPTS-27WSH-95, KXNHLSEASONPTS-27WSH-90, KXNHLSEASONPTS-27WSH-85, KXNHLSEASONPTS-27WSH-80, KXNHLSEASONPTS-27WSH-75, KXNHLSEASONPTS-27WSH-70
- sample fields: `{"ticker": "KXNHLSEASONPTS-27WSH-95", "event_ticker": "KXNHLSEASONPTS-27WSH", "market_type": "binary", "title": "Will the WSH Capitals NHL team earn at least 95 points in the 2026-27 regular season?", "yes_sub_title": "95+ points", "no_sub_title": "95+ points", "strike_type": "greater_or_equal", "floor_strike": 95, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-26T00:47:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-18T14:00:00Z", "result": "", "rules_primary": "If the WSH Capitals earn at le`

### KXNHLSERIES — NHL Series Winner

### KXNHLSERIESGAMES — NHL Series Total Games

### KXNHLSERIESOT — NHL Series Overtime

### KXNHLSERIESSCORE — NHL Series Exact Score

### KXNHLSERIESSPREAD — NHL Series Game Spread

### KXNHLSERIESTOTALGOAL — NHL Series Total Goals

### KXNHLSERIESTOTALGOALS — NHL Series Total Goals

### KXNHLSPREAD — NHL Spread
- (14) NAME wins by over # goals
- (4) Utah wins by over # goals
- (4) Edmonton wins by over # goals
- (4) Vegas wins by over # goals
- (4) Pittsburgh wins by over # goals
- (4) Boston wins by over # goals
- (4) St. Louis wins by over # goals
- (4) Nashville wins by over # goals
- samples: KXNHLSPREAD-26OCT17EDMUTA-UTA3, KXNHLSPREAD-26OCT17EDMUTA-UTA2, KXNHLSPREAD-26OCT17EDMUTA-EDM3, KXNHLSPREAD-26OCT17EDMUTA-EDM2, KXNHLSPREAD-26OCT17PITVGK-VGK3, KXNHLSPREAD-26OCT17PITVGK-VGK2
- sample fields: `{"ticker": "KXNHLSPREAD-26OCT17EDMUTA-UTA3", "event_ticker": "KXNHLSPREAD-26OCT17EDMUTA", "market_type": "binary", "title": "Utah wins by over 2.5 goals", "yes_sub_title": "Utah wins by over 2.5 goals", "no_sub_title": "Utah wins by over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "custom_strike": {"hockey_team": "7d20591d-c6fa-4b85-8d69-ff05fb3649ac"}, "status": "active", "open_time": "2026-10-15T04:06:00Z", "close_time": "2026-10-20T02:00:00Z", "expected_expiration_time": "2026-10-18T05:00:00Z", "result": "", "rules_primary": "If Utah wins by over 2.5 goals in the Edmonton vs `

### KXNHLTEAMTOTAL — NHL Team Goals Scored During Game
- (20) NAME over # goals scored
- (5) Washington over # goals scored
- (5) Boston over # goals scored
- (5) Anaheim over # goals scored
- (5) Pittsburgh over # goals scored
- (5) Colorado over # goals scored
- (5) Vegas over # goals scored
- (5) Calgary over # goals scored
- samples: KXNHLTEAMTOTAL-26OCT17NJWSH-WSH6, KXNHLTEAMTOTAL-26OCT17NJWSH-WSH5, KXNHLTEAMTOTAL-26OCT17NJWSH-WSH4, KXNHLTEAMTOTAL-26OCT17NJWSH-WSH3, KXNHLTEAMTOTAL-26OCT17NJWSH-WSH2, KXNHLTEAMTOTAL-26OCT17NJWSH-NJ6
- sample fields: `{"ticker": "KXNHLTEAMTOTAL-26OCT17NJWSH-WSH6", "event_ticker": "KXNHLTEAMTOTAL-26OCT17NJWSH", "market_type": "binary", "title": "Washington over 5.5 goals scored", "yes_sub_title": "Washington over 5.5", "no_sub_title": "Washington over 5.5", "strike_type": "greater", "floor_strike": 5.5, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-10-15T19:05:00Z", "close_time": "2026-10-19T17:00:00Z", "expected_expiration_time": "2026-10-17T20:00:00Z", "result": "", "rules_primary": "If Washington scores over 5.5 goals in the New Jersey vs `

### KXNHLTOTAL — NHL Total Goals
- (243) NAME: Over # goals scored
- samples: KXNHLTOTAL-26OCT17EDMUTA-9, KXNHLTOTAL-26OCT17EDMUTA-8, KXNHLTOTAL-26OCT17EDMUTA-7, KXNHLTOTAL-26OCT17EDMUTA-6, KXNHLTOTAL-26OCT17EDMUTA-5, KXNHLTOTAL-26OCT17EDMUTA-4
- sample fields: `{"ticker": "KXNHLTOTAL-26OCT17EDMUTA-9", "event_ticker": "KXNHLTOTAL-26OCT17EDMUTA", "market_type": "binary", "title": "Full Game: Over 8.5 goals scored", "yes_sub_title": "Over 8.5 goals scored", "no_sub_title": "Over 8.5 goals scored", "strike_type": "greater", "floor_strike": 8.5, "status": "active", "open_time": "2026-10-15T04:06:00Z", "close_time": "2026-10-20T02:00:00Z", "expected_expiration_time": "2026-10-18T05:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 8.5 goals in the Edmonton vs Utah NHL game originally scheduled for Oct 17, 2026, then the mar`

### KXNHLVEZINA — NHL Vezina Trophy
- (40) NAME: NAME wins
- samples: KXNHLVEZINA-27-YASKAROV30, KXNHLVEZINA-27-ULUUKKONEN1, KXNHLVEZINA-27-TDEMKO35, KXNHLVEZINA-27-SSKINNER74, KXNHLVEZINA-27-SMONTEMBEAULT35, KXNHLVEZINA-27-SKNIGHT30
- sample fields: `{"ticker": "KXNHLVEZINA-27-YASKAROV30", "event_ticker": "KXNHLVEZINA-27", "market_type": "binary", "title": "Vezina Trophy: Yaroslav Askarov wins", "subtitle": "::", "yes_sub_title": "Yaroslav Askarov", "no_sub_title": "Yaroslav Askarov", "strike_type": "structured", "custom_strike": {"hockey_player": "d9975a58-bdda-4de9-9933-549069713e00"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Yaroslav Askarov wins the NHL Vezina Trophy in the 2026-27 NHL season, the`

### KXNHLWEST — Western Conference Champion
- (15) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLWEST-27-WPG, KXNHLWEST-27-VGK, KXNHLWEST-27-VAN, KXNHLWEST-27-UTA, KXNHLWEST-27-STL, KXNHLWEST-27-SJ
- sample fields: `{"ticker": "KXNHLWEST-27-WPG", "event_ticker": "KXNHLWEST-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Western Conference Finals?", "subtitle": "Winnipeg Jets", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Western Conference Fina`

### KXNHLWINS — NHL wins 

### KXNHLWSTREAK — Longest NHL win streak in regular season
- (30) Will the NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the St. NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the Montréal Canadiens have the longest winning streak in the #-# NHL regular season?
- samples: KXNHLWSTREAK-27-WSH, KXNHLWSTREAK-27-WPG, KXNHLWSTREAK-27-VGK, KXNHLWSTREAK-27-VAN, KXNHLWSTREAK-27-UTA, KXNHLWSTREAK-27-TOR
- sample fields: `{"ticker": "KXNHLWSTREAK-27-WSH", "event_ticker": "KXNHLWSTREAK-27", "market_type": "binary", "title": "Will the Washington Capitals have the longest winning streak in the 2026-27 NHL regular season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals has the longes`

### KXTEAMSINSC — Teams in Stanley Cup
- (1) Will WSH Capitals vs WPG Jets be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VGK NAME be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VAN Canucks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs UTA Mammoth be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs STL Blues be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SJ Sharks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SEA Kraken be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs NSH Predators be the matchup in the #-# NAME?
- samples: KXTEAMSINSC-27-WSHWPG, KXTEAMSINSC-27-WSHVGK, KXTEAMSINSC-27-WSHVAN, KXTEAMSINSC-27-WSHUTA, KXTEAMSINSC-27-WSHSTL, KXTEAMSINSC-27-WSHSJ
- sample fields: `{"ticker": "KXTEAMSINSC-27-WSHWPG", "event_ticker": "KXTEAMSINSC-27", "market_type": "binary", "title": "Will WSH Capitals vs WPG Jets be the matchup in the 2026-27 Stanley Cup Final?", "yes_sub_title": "WSH Capitals vs WPG Jets", "no_sub_title": "WSH Capitals vs WPG Jets", "strike_type": "custom", "custom_strike": {"Matchup": "WSH Capitals vs WPG Jets"}, "status": "active", "open_time": "2026-09-11T22:00:00Z", "close_time": "2027-06-15T14:00:00Z", "expected_expiration_time": "2027-06-15T14:00:00Z", "result": "", "rules_primary": "If WSH Capitals vs WPG Jets is confirmed to be the matchup in t`

## UNRESOLVED samples

- `KXNBANHL-27-TORWSH` — Pro Basketball/NHL Champion: Toronto/Washington — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORVGK` — Pro Basketball/NHL Champion: Toronto/Vegas — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORUTA` — Pro Basketball/NHL Champion: Toronto/Utah — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORTB` — Pro Basketball/NHL Champion: Toronto/Tampa Bay — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORSJ` — Pro Basketball/NHL Champion: Toronto/San Jose — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORNJ` — Pro Basketball/NHL Champion: Toronto/New Jersey — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORMTL` — Pro Basketball/NHL Champion: Toronto/Montreal — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORMIN` — Pro Basketball/NHL Champion: Toronto/Minnesota — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORFLA` — Pro Basketball/NHL Champion: Toronto/Florida — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TOREDM` — Pro Basketball/NHL Champion: Toronto/Edmonton — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORDAL` — Pro Basketball/NHL Champion: Toronto/Dallas — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORCOL` — Pro Basketball/NHL Champion: Toronto/Colorado — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-TORCAR` — Pro Basketball/NHL Champion: Toronto/Carolina — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASWSH` — Pro Basketball/NHL Champion: San Antonio/Washington — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASWPG` — Pro Basketball/NHL Champion: San Antonio/Winnipeg — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASVGK` — Pro Basketball/NHL Champion: San Antonio/Vegas — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASVAN` — Pro Basketball/NHL Champion: San Antonio/Vancouver — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASUTA` — Pro Basketball/NHL Champion: San Antonio/Utah — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASTOR` — Pro Basketball/NHL Champion: San Antonio/Toronto — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASTB` — Pro Basketball/NHL Champion: San Antonio/Tampa Bay — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASSTL` — Pro Basketball/NHL Champion: San Antonio/St. Louis — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASSJ` — Pro Basketball/NHL Champion: San Antonio/San Jose — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASSEA` — Pro Basketball/NHL Champion: San Antonio/Seattle — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASPIT` — Pro Basketball/NHL Champion: San Antonio/Pittsburgh — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASPHI` — Pro Basketball/NHL Champion: San Antonio/Philadelphia — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASOTT` — Pro Basketball/NHL Champion: San Antonio/Ottawa — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASNYR` — Pro Basketball/NHL Champion: San Antonio/New York R — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASNYI` — Pro Basketball/NHL Champion: San Antonio/New York I — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASNSH` — Pro Basketball/NHL Champion: San Antonio/Nashville — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASNJ` — Pro Basketball/NHL Champion: San Antonio/New Jersey — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASMTL` — Pro Basketball/NHL Champion: San Antonio/Montreal — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASMIN` — Pro Basketball/NHL Champion: San Antonio/Minnesota — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASLA` — Pro Basketball/NHL Champion: San Antonio/Los Angeles — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASFLA` — Pro Basketball/NHL Champion: San Antonio/Florida — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASEDM` — Pro Basketball/NHL Champion: San Antonio/Edmonton — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASDET` — Pro Basketball/NHL Champion: San Antonio/Detroit — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASDAL` — Pro Basketball/NHL Champion: San Antonio/Dallas — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASCOL` — Pro Basketball/NHL Champion: San Antonio/Colorado — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASCHI` — Pro Basketball/NHL Champion: San Antonio/Chicago — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASCGY` — Pro Basketball/NHL Champion: San Antonio/Calgary — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASCBJ` — Pro Basketball/NHL Champion: San Antonio/Columbus — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASCAR` — Pro Basketball/NHL Champion: San Antonio/Carolina — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASBUF` — Pro Basketball/NHL Champion: San Antonio/Buffalo — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASBOS` — Pro Basketball/NHL Champion: San Antonio/Boston — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-SASANA` — Pro Basketball/NHL Champion: San Antonio/Anaheim — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PORVGK` — Pro Basketball/NHL Champion: Portland/Vegas — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PORTB` — Pro Basketball/NHL Champion: Portland/Tampa Bay — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PORMIN` — Pro Basketball/NHL Champion: Portland/Minnesota — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PORFLA` — Pro Basketball/NHL Champion: Portland/Florida — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-POREDM` — Pro Basketball/NHL Champion: Portland/Edmonton — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PORCOL` — Pro Basketball/NHL Champion: Portland/Colorado — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PORCAR` — Pro Basketball/NHL Champion: Portland/Carolina — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PHIWSH` — Pro Basketball/NHL Champion: Philadelphia/Washington — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PHIVGK` — Pro Basketball/NHL Champion: Philadelphia/Vegas — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PHIUTA` — Pro Basketball/NHL Champion: Philadelphia/Utah — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PHITOR` — Pro Basketball/NHL Champion: Philadelphia/Toronto — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PHITB` — Pro Basketball/NHL Champion: Philadelphia/Tampa Bay — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PHISTL` — Pro Basketball/NHL Champion: Philadelphia/St. Louis — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PHISJ` — Pro Basketball/NHL Champion: Philadelphia/San Jose — series KXNBANHL not in ontology; season-scope words in title
- `KXNBANHL-27-PHIPIT` — Pro Basketball/NHL Champion: Philadelphia/Pittsburgh — series KXNBANHL not in ontology; season-scope words in title

## Series decisions (hockey-related)

- NHL  `KXNHLMETROPOLITAN` NHL Metropolitan Division Winner — ticker prefix KXNHL
- NHL  `KXNHLPLAYOFFGOALS` NHL Playoffs Goal Leader (by Round) — ticker prefix KXNHL
- NHL  `KXNHLSERIESTOTALGOAL` NHL Series Total Goals — ticker prefix KXNHL
- NHL  `KXNHLGOAL` NHL Goalscorer — ticker prefix KXNHL
- NHL  `KXNHLFINALSEXACT` NHL Championship Series Score — ticker prefix KXNHL
- NHL  `KXNHLRICHARD` NHL Maurice "Rocket" Richard Trophy — ticker prefix KXNHL
- NHL  `KXNHLSERIESSCORE` NHL Series Exact Score — ticker prefix KXNHL
- NHL  `KXNHLPACIFIC` NHL Pacific Division Winner — ticker prefix KXNHL
- NHL  `KXNHL1P` NHL 1st Period Winner — ticker prefix KXNHL
- NHL  `KXNHL1PSPREAD` 1st Period Spread — ticker prefix KXNHL
- skip `KXWOMHOCKEYTOTAL` Winter Olympics Men's Hockey Goal Total — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHL1STTEAM` All NHL First Team — ticker prefix KXNHL
- NHL  `KXNHLVEZINA` NHL Vezina Trophy — ticker prefix KXNHL
- skip `KXNCAAHOCKEY` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLNEXTGM` Next NHL GM — ticker prefix KXNHL
- NHL  `KXNHLPTS` Pro Hockey Points — ticker prefix KXNHL
- NHL  `KXNHLPSEASONGOALS` Player Goals Scored in Season — ticker prefix KXNHL
- NHL  `KXNHLTEAMTOTAL` NHL Team Goals Scored During Game — ticker prefix KXNHL
- skip `KXLIIGA` Liiga Champion — non-NHL hockey marker 'LIIGA'
- skip `KXEUCHLGAME` Champions League Hockey — non-NHL hockey marker 'CHL'
- NHL  `KXNHLSPREAD` NHL Spread — ticker prefix KXNHL
- NHL  `KXNHLTOTAL` NHL Total Goals — ticker prefix KXNHL
- NHL  `KXCONNSMYTHE` Conn Smythe trophy — NHL trophy/futures marker
- skip `KXDEL` DEL Champion — non-NHL hockey marker 'DEL '
- NHL  `KXNHLRETIRE` NHL Retire — ticker prefix KXNHL
- NHL  `KXNHL2P` NHL 2nd Period Winner — ticker prefix KXNHL
- skip `KXWOMHOCKEYMVP` Men's Winter Olympics Hockey MVP — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLWINS` NHL wins  — ticker prefix KXNHL
- skip `KXELH` ELH Champion — no NHL marker
- NHL  `KXNHLNORRIS` NHL James Norris Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLAST` Pro Hockey Assists — ticker prefix KXNHL
- NHL  `KXNHL2PBTTS` NHL Both Teams to Score in 2nd Period — ticker prefix KXNHL
- NHL  `KXNHLSERIESTOTALGOALS` NHL Series Total Goals — ticker prefix KXNHL
- NHL  `KXNHL4NATIONS` 4 nations face off — ticker prefix KXNHL
- NHL  `KXNHLANYGOAL` Pro Hockey Goalscorer — ticker prefix KXNHL
- NHL  `KXNHLLINDSAY` NHL Ted Lindsay Winner — ticker prefix KXNHL
- NHL  `KXNHL2OT` NHL Double Overtime — ticker prefix KXNHL
- skip `KXWOMHOCKEY` Winter Olympics Men's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLSAVE` Goaltender Saves — ticker prefix KXNHL
- NHL  `KXNHLCENTRAL` NHL Central Division Winner — ticker prefix KXNHL
- NHL  `KXNHL2PTOTAL` 2nd Period Total — ticker prefix KXNHL
- skip `KXDELGAME` DEL Game — non-NHL hockey marker 'DEL '
- NHL  `KXNHLPRES` NHL President's Trophy Winner — ticker prefix KXNHL
- NHL  `KXNHL3P` NHL 3rd Period Winner — ticker prefix KXNHL
- NHL  `KXNHLGAME` NHL Game — ticker prefix KXNHL
- NHL  `KXNHLSEASONPTS` NHL Season Point Totals — ticker prefix KXNHL
- skip `KXNL` National League Champion — no NHL marker
- skip `KXKHL` KHL Champion — non-NHL hockey marker 'KHL'
- NHL  `KXNHLSAVES` Pro Hockey Saves — ticker prefix KXNHL
- NHL  `KXNHLSERIESSPREAD` NHL Series Game Spread — ticker prefix KXNHL
- NHL  `KXESPYNHL` BEST NHL PLAYER‬ — title mentions NHL
- skip `KXLIIGAGAME` Liiga Game — non-NHL hockey marker 'LIIGA'
- NHL  `KXNHLMENTION` NHL Announcer Mentions — ticker prefix KXNHL
- NHL  `KXNHLPRICE` NHL Ticket Prices — ticker prefix KXNHL
- NHL  `KXNHLSERIESOT` NHL Series Overtime — ticker prefix KXNHL
- skip `KXWO-HOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLEAST` Eastern Conference Championship — ticker prefix KXNHL
- NHL  `KXNHLNEXTTEAM` NHL Next Team — ticker prefix KXNHL
- skip `KXEARNINGSMENTIONHLT` HILTON — no NHL marker
- skip `KXIIHFCHAMP` IIHF World Championship winner — non-NHL hockey marker 'IIHF'
- NHL  `KXNBANHL` NBA + NHL Champion Combo — title mentions NHL
- NHL  `KXNHLSEASONGOALS` Player to score X Goals in Season — ticker prefix KXNHL
- skip `KXSHL` SHL Champion — non-NHL hockey marker 'SHL'
- NHL  `KXNHLSERIESGAMES` NHL Series Total Games — ticker prefix KXNHL
- NHL  `KXNHLEXPANSION` NHL Expansion — ticker prefix KXNHL
- NHL  `KXNEXTTEAMNHL` Next Team NHL — title mentions NHL
- NHL  `KXNHLCALDER` NHL Calder Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLOVERTIME` NHL Overtime — ticker prefix KXNHL
- NHL  `KXNHLATLANTIC` NHL Atlantic Division Winner — ticker prefix KXNHL
- NHL  `KXNHLHART` NHL Hart Memorial Trophy — ticker prefix KXNHL
- skip `KXWOMHOCKEYGOAL` Olympic Hockey Goalscorer — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLADAMS` NHL Jack Adams Award — ticker prefix KXNHL
- skip `KXNLGAME` National League Game — no NHL marker
- NHL  `KXNHLSERIES` NHL Series Winner — ticker prefix KXNHL
- skip `KXIIHFGAME` IIHF Game — non-NHL hockey marker 'IIHF'
- NHL  `KXNHLDRAFTTOP` Pro Hockey Top Pick — ticker prefix KXNHL
- skip `KXNCAAHOCKEYGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLOT` NHL Overtime — ticker prefix KXNHL
- skip `KXNCAAH` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- skip `KXNCAAHGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- NHL  `KXNHL1PBTTS` NHL Both Teams to Score in 1st Period — ticker prefix KXNHL
- NHL  `KXNHL1PTOTAL` NHL 1st Period Total — ticker prefix KXNHL
- skip `KXIIHF` Who will win IIHF championship? — non-NHL hockey marker 'IIHF'
- skip `KXWOHOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLWEST` Western Conference Champion — ticker prefix KXNHL
- skip `KXWOMHOCKEYFGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- skip `KXWOMHOCKEYSPREAD` Winter Olympics Men's Hockey Spread — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLDRAFTPICK` Pro Hockey Draft Pick — ticker prefix KXNHL
- NHL  `KXNHLSEASONPPTS` Season Player Points — ticker prefix KXNHL
- NHL  `KXNHLRECORDWORST` Worst NHL Record — ticker prefix KXNHL
- NHL  `KXNHL3PSPREAD` NHL 3rd Period Spread — ticker prefix KXNHL
- NHL  `KXCANADACUP` Canada winning Stanley Cup — NHL trophy/futures marker
- skip `KXWOWHOCKEY` Winter Olympics Women's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXTEAMSINSC` Teams in Stanley Cup — NHL trophy/futures marker
- skip `KXELHGAME` ELH Game — no NHL marker
- NHL  `KXNHL3PBTTS` NHL Both Teams to Score in 3rd Period — ticker prefix KXNHL
- skip `KXAHLGAME` AHL Game — non-NHL hockey marker 'AHL'
- skip `KXSHLGAME` SHL Game — non-NHL hockey marker 'SHL'
- skip `KXINTHOCKEY` International Hockey — no NHL marker
- NHL  `KXNHLMVP` NHL Hart Memorial Trophy Winner — ticker prefix KXNHL
- NHL  `KXNHLWSTREAK` Longest NHL win streak in regular season — ticker prefix KXNHL
- NHL  `KXNHLROSS` NHL Art Ross Trophy — ticker prefix KXNHL
- NHL  `KXNHL30COMEBACK` NHL 3-0 Series Comeback — ticker prefix KXNHL
- skip `KXKHLGAME` KHL Game — non-NHL hockey marker 'KHL'
- NHL  `KXNHL` Stanley Cup — ticker prefix KXNHL
- skip `KXWOMHOCKEYFIRSTGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- skip `KXAHL` AHL Champion — non-NHL hockey marker 'AHL'
- NHL  `KXNHL3PTOTAL` 3rd Period Total — ticker prefix KXNHL
- NHL  `KXNHLFIRSTGOAL` NHL First Goal — ticker prefix KXNHL
- NHL  `KXNHL2PSPREAD` 2nd Period Spread — ticker prefix KXNHL
- NHL  `KXNHLF10G` NHL Goal in First 10 Minutes — ticker prefix KXNHL
- NHL  `KXNHLPLAYOFF` Playoff Qualifier — ticker prefix KXNHL
