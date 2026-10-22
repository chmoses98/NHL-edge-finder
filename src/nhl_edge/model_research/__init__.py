"""NHL model-improvement research (RESEARCH_ONLY, shadow).

Offline analysis over read-only copies of the ``data-archive`` / ``accounting-data`` branches and the committed
``data/history`` seasons. Nothing here is imported by a production path, places or routes a wager, changes a model,
a stake or a cap. Challengers are evaluated chronologically and recorded in an append-only experiment registry.
"""

RESEARCH_VERSION = "nhl-model-research-1.0"

# The prospective evaluation window opens at the first game that STARTS after this instant (prior audit registry
# freeze, ``docs/research/nhl-market-audit/PROGRESS.md``). No development code in this package reads a game that starts
# later than ``DEV_LAST_GAME_DATE_ET``.
PROSPECTIVE_FREEZE_UTC = "2026-10-21T17:13:05Z"
DEV_LAST_GAME_DATE_ET = "2026-10-20"
