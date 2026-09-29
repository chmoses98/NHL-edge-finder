# Source probe

probed 2026-09-29T04:21:28+00:00 for date 2026-09-29

| name | status | ms | bytes | kind | note |
|---|---:|---:|---:|---|---|
| nhl_schedule_date | 200 | 62 | 84310 | json | nextStartDate, previousStartDate, gameWeek, oddsPartners, preSeasonStartDate, regularSeasonStartDate, regularSeasonEndDa |
| nhl_schedule_now | 200 | 93 | 84310 | json | nextStartDate, previousStartDate, gameWeek, oddsPartners, preSeasonStartDate, regularSeasonStartDate, regularSeasonEndDa |
| nhl_score_now | 200 | 77 | 18390 | json | prevDate, currentDate, nextDate, gameWeek, oddsPartners, games |
| nhl_score_date | 200 | 36 | 18390 | json | prevDate, currentDate, nextDate, gameWeek, oddsPartners, games |
| nhl_standings_now | 200 | 76 | 51555 | json | wildCardIndicator, standingsDateTimeUtc, standings |
| nhl_roster_tor | 200 | 75 | 10390 | json | forwards, defensemen, goalies |
| nhl_club_schedule_tor | 200 | 90 | 188381 | json | previousSeason, currentSeason, clubTimezone, clubUTCOffset, games |
| nhl_club_schedule_tor_2025 | 200 | 50 | 184101 | json | previousSeason, currentSeason, nextSeason, clubTimezone, clubUTCOffset, games |
| nhl_club_stats_tor | 200 | 94 | 17323 | json | season, gameType, skaters, goalies |
| nhl_boxscore_final_2025 | 200 | 244 | 13529 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_landing_final_2025 | 200 | 390 | 11355 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_pbp_final_2025 | 200 | 227 | 146277 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_right_rail_2025 | 200 | 315 | 4550 | json | seasonSeries, seasonSeriesWins, gameInfo, gameVideo, linescore, shotsByPeriod, teamGameStats, gameReports |
| nhl_boxscore_ot_sample | 200 | 249 | 13147 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_schedule_calendar | 200 | 93 | 12704 | json | endDate, nextStartDate, previousStartDate, startDate, teams |
| nhl_season_list | 200 | 50 | 982 | json | l, i, s, t, [, 1, 0, 9 |
| nhl_stats_team | 200 | 63 | 6664 | json | data, total |
| nhl_stats_team_summary_prev | 200 | 87 | 16854 | json | data, total |
| nhl_stats_team_summary_cur | 200 | 46 | 21 | json | data, total |
| nhl_stats_goalie_summary_prev | 200 | 120 | 38937 | json | data, total |
| nhl_stats_goalie_summary_cur | 200 | 49 | 21 | json | data, total |
| nhl_stats_season | 200 | 111 | 65173 | json | data, total |
| nhl_stats_game_prev | 200 | 86 | 1259 | json | data, total |
| mp_teams_2025 | 200 | 144 | 99689 | csv | team, season, name, team, position, situation, games_played, xGoalsPercentage |
| mp_teams_2026 | 404 | 46 | 196 | html | HTTPError 404 |
| mp_goalies_2025 | 200 | 57 | 93386 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_goalies_2026 | 200 | 41 | 489 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_skaters_2025 | 200 | 90 | 400000 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_lines_2025 | 200 | 98 | 400000 | csv | lineId, season, name, team, position, situation, games_played, icetime |
| mp_all_teams_gbg | 200 | 98 | 600000 | csv | team, season, name, gameId, playerTeam, opposingTeam, home_or_away, gameDate |
| mp_team_gbg_tor | 200 | 88 | 400000 | csv | team, season, name, gameId, playerTeam, opposingTeam, home_or_away, gameDate |
| mp_shots_2024_zip_head | 404 | 44 | 0 |  | HTTPError 404 |
| mp_shots_2025_zip_head | 404 | 36 | 0 |  | HTTPError 404 |
| mp_shots_pt_2024_head | 200 | 88 | 0 |  |  |
| mp_shots_pt_2025_head | 200 | 48 | 0 |  |  |
| mp_shots_pt_2007_2023_head | 404 | 89 | 0 |  | HTTPError 404 |
| mp_predictions_page | 200 | 47 | 20000 | html |  |
| espn_nhl_scoreboard | 200 | 219 | 72293 | json | leagues, events, provider |
| espn_nhl_teams | 200 | 79 | 136961 | json | sports |
| dailyfaceoff_goalies | 200 | 67 | 79561 | html |  |
| dailyfaceoff_goalies_date | 200 | 208 | 143349 | html |  |
| rotowire_goalies | 200 | 533 | 323650 | html |  |
| nhl_schedule_oct05 | 200 | 78 | 89222 | json | nextStartDate, previousStartDate, gameWeek, preSeasonStartDate, regularSeasonStartDate, regularSeasonEndDate, playoffEnd |
| nhl_injuries_espn | 200 | 77 | 1208735 | json | timestamp, status, season, injuries |
| kalshi_api_exchange_status | 200 | 115 | 667 | json | exchange_active, exchange_index_statuses, intra_exchange_transfers_active, trading_active |
| kalshi_api_series_sports | 200 | 243 | 3000000 | json-invalid |  |
| kalshi_api_series_kxnhlgame | 200 | 58 | 1569 | json | series |
| kalshi_api_markets_kxnhlgame_open | 200 | 140 | 157586 | json | cursor, markets |
| kalshi_api_markets_kxnhlgame_unopened | 200 | 74 | 27 | json | cursor, markets |
| kalshi_api_markets_kxnhlgame_settled | 200 | 125 | 99699 | json | cursor, markets |
| kalshi_api_events_kxnhlgame | 200 | 90 | 210321 | json | cursor, events, milestones |
| kalshi_api_markets_kxnhlspread_open | 200 | 60 | 124059 | json | cursor, markets |
| kalshi_api_markets_kxnhltotal_open | 200 | 86 | 203870 | json | cursor, markets |
| kalshi_api_filters_by_sport | 200 | 51 | 17500 | json | filters_by_sports, sport_ordering |
| kalshi_external_api_exchange_status | 200 | 94 | 667 | json | exchange_active, exchange_index_statuses, intra_exchange_transfers_active, trading_active |
| kalshi_external_api_series_sports | 200 | 455 | 3000000 | json-invalid |  |
| kalshi_external_api_series_kxnhlgame | 200 | 112 | 1569 | json | series |
| kalshi_external_api_markets_kxnhlgame_open | 200 | 201 | 157586 | json | cursor, markets |
| kalshi_external_api_markets_kxnhlgame_unopened | 200 | 105 | 27 | json | cursor, markets |
| kalshi_external_api_markets_kxnhlgame_settled | 200 | 153 | 99699 | json | cursor, markets |
| kalshi_external_api_events_kxnhlgame | 200 | 163 | 210321 | json | cursor, events, milestones |
| kalshi_external_api_markets_kxnhlspread_open | 200 | 152 | 124059 | json | cursor, markets |
| kalshi_external_api_markets_kxnhltotal_open | 200 | 162 | 203877 | json | cursor, markets |
| kalshi_external_api_filters_by_sport | 200 | 121 | 17500 | json | filters_by_sports, sport_ordering |
