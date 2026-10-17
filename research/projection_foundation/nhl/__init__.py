"""NHL Projection Foundation (research only).

Isolated challenger stack for skater / goalie / team projections, built on the shared
`pf_core` library. Nothing here is imported by production code (`src/nhl_edge`), and
nothing here carries betting authority.

Modules
  data        load official player-event history (+ the 2026-27 archive) into tidy tables
  inventory   data-availability matrix with point-in-time classification
  features    leakage-safe skater / goalie / team features (role from co-ice, xG, schedule)
  xg          shot-quality (expected goals) model fitted on development seasons only
  ladder      A..F candidate models per family
  incumbent   PLAYER_SIM_V1 archived prospective predictions joined to outcomes
  evaluate    metrics, distributions, calibration, gate
  project     forward projections in sift.projections.v1
"""
VERSION = "pf-nhl-1.0.0"
SPLITS = {
    "development": [2021, 2022],
    "validation": [2023],
    "holdout": [2024, 2025],
    "prospective": [2026],
}
SPLIT_LABELS = {
    "development": "2021-22, 2022-23 regular seasons (fit shrinkage, betas, dispersion, stack weights)",
    "validation": "2023-24 regular season (model and distribution selection)",
    "holdout": "2024-25 and 2025-26 regular seasons (evaluated once for frozen candidates)",
    "prospective": "2026-27 regular season to date (games 2026020001-2026020120, archived; overlaps PLAYER_SIM_V1)",
}


def split_of(season: int) -> str:
    for k, v in SPLITS.items():
        if season in v:
            return k
    return "other"
