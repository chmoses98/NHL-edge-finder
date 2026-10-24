# `player-minutes-1.0` collection (research only)

How the registered test in `PREREGISTRATION.md` is collected. Nothing here is wired to the projection engine, prices, stakes or routing.

* **When.** The `minutes` job of `workload_shadow.yml` runs on the same triggers as the LC shots collection (cron, the capture worker's dispatch, slate-watch's dispatch), so the
  unattended dispatch and gap alert that protect the LC records protect these too. It is `continue-on-error`, so a failure here can never fail the LC run or change its coverage logic;
  a failed `minutes` job is visible as a failed job in the run and in the uploaded logs.
* **Where.** Orphan branch `player-minutes-data` (`records/`, `outcomes/`, `coverage/`, `looks/`, `scoreboard/`, `activation.json`, append-only `MANIFEST.jsonl`). The commit step refuses any
  modification, rename or deletion of an immutable file and any change to existing manifest lines.
* **What each record holds.** See the registration. Keys of `inputs`: `last3_toi_min`, `n_known_recent_games`, `lines[]` (category ev/pp/pk, unit f1…/d1…/pp1/pp2/pk1, slot, `lines_updated_at_utc`,
  `lines_source`, our `observed_at_utc`, injury status, game-time-decision flag, identity-resolution method), `injury[]` (ESPN status, type, detail, return date), `incumbent_toi_min`,
  `incumbent_pp_min`, `incumbent_at_utc`, and the two snapshot instants. Lines exist only from 2026-09-30 (when archiving began) and only for games on the day of the capture; a player without a row
  simply has an empty list. Nothing is imputed or back-filled.
* **Outcomes.** After a recorded game is final its official ice time by state and shots are appended once to `outcomes/` (stamped `settled_at_utc`).
* **Adding a hypothesis.** Write a new preregistration and (if it needs a different prediction) a new schema/branch version; the stored `inputs` are the data for it. Do not edit the
  registered thresholds or the frozen coefficient in `data/params/minutes-v1.json`.
* **Reading the scoreboard.** `scoreboard/latest.md` on the data branch (also in the run summary). Looks are in `looks/`, each computed once on exactly its sample.

Python: `python -m nhl_edge.research.player_minutes_shadow predict|settle|score` (`src/nhl_edge/research/player_minutes_shadow.py`, tests `tests/test_player_minutes_shadow.py`).
