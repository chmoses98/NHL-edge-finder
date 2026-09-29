"""NHL Edge Finder: Kalshi NHL market research workstation.

CURRENT AUTHORITY: RESEARCH_ONLY. Nothing in this package places, recommends, sizes or routes a wager.
"""

__version__ = "0.1.0"

# Model families. Bump a version whenever semantics change materially; never reuse a version for new logic.
DATA_ONLY_MODEL_VERSION = "DATA_ONLY_V1"
MARKET_ANCHORED_MODEL_VERSION = "MARKET_ANCHORED_V1"
SIM_VERSION = "nhl-sim-1.1"  # 1.1: late-window goalie-pull multipliers normalised (no double counting of empty-net goals)
FEATURE_VERSION = "nhl-features-1.0"
AUTHORITY = "RESEARCH_ONLY"

# DATA_ONLY_V2: SHADOW / RESEARCH_ONLY candidate arm (2026-09-29). New versions, so every V1 constant above is frozen:
# special teams + goalie true talent (features 2.0) and a state-dependent, period-resolved simulator (sim 2.0).
DATA_ONLY_V2_MODEL_VERSION = "DATA_ONLY_V2"
SIM_V2_VERSION = "nhl-sim-2.0"
FEATURE_V2_VERSION = "nhl-features-2.0"
