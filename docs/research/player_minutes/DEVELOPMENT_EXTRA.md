# Further ice-time research on top of WORKLOAD_V1 (development evidence only)

**Evidence status.** 2022–2025 are exposed development seasons; this selects nothing that is frozen and validates nothing. It is kept apart from the prospective `player-minutes-1.0` records. The frozen specification (usage window = last 3 games, coefficient 0.23) is unchanged.

Method: `src/nhl_edge/research/minutes_extra_research.py` — each variant is stacked on WORKLOAD_V1's total ice time, fitted on earlier seasons only (2023 → scored 2024; 2023–24 → scored 2025), n = 94,456 skater-games, game-clustered paired bootstrap (raw: `development_extra.json`).

| variant (stacked on WORKLOAD_V1 total ice time) | change in MSE | paired interval (min²) |
|---|---|---|
| usage, last 1 game | −1.07 % | −0.078 … −0.051 |
| **usage, last 3 games (the frozen specification)** | **−1.10 %** | −0.079 … −0.055 |
| usage, last 5 games | −0.39 % | −0.031 … −0.016 |
| usage, last 10 games | +0.01 % | −0.003 … +0.004 |
| usage last 3 + last 10 | −1.12 % | −0.080 … −0.056 |
| usage last 3 + team back-to-back + opponent back-to-back | −1.09 % | −0.078 … −0.055 |
| usage last 3 + home | −1.10 % | −0.079 … −0.055 |
| usage last 3 + usage × defenseman | −1.05 % | −0.075 … −0.052 |

**Reading.** The frozen last-3 window is the best single recent-usage window; the signal is short-memory (last 1 ≈ last 3, last 5 about a third as useful, last 10 nothing). Rest/back-to-back, venue and a position interaction add nothing measurable on top of it, and adding a long-window term improves the in-sample-selected variant by 0.02 percentage points, which is not worth a hypothesis. Conclusion: **no new ice-time hypothesis is warranted from history alone**; the next candidates are the lineup/role inputs already stored in the prospective records, which can only be evaluated prospectively. Nothing here is promoted or wired to anything.
