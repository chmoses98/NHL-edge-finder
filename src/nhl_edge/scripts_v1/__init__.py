"""NHL_SCRIPT_V1: the hockey-native game-script layer that SIFT reads (RESEARCH_ONLY).

This package never simulates. It reads the SAME joint PLAYER_SIM_V1 draw the thesis card already uses
(``thesis.engine.GameDistribution``) and adds, per modelled game:

    a small, mutually exclusive script partition (7 scripts, precedence rules)     scripts_v1.taxonomy
      -> per-script game summaries (who wins, goals, shots, saves, PP share)      scripts_v1.summary
      -> P(selection wins | script) and EV(selection | script, ask, fee)          scripts_v1.survival
      -> script survival + robustness tier                                        scripts_v1.survival
      -> research-candidate ranking + exposure (correlation) groups               scripts_v1.candidates
      -> the realised script of a final game (postgame only)                      scripts_v1.taxonomy.realized
      -> immutable forecasts / postmortems for the learning loop                  workflows.learning

Why a second taxonomy next to ``thesis.scripts``: the thesis card's primary partition is 18 cells
(shot control x environment x margin). That is right for portfolio construction but too fine to read, and many cells
mean the same thing to a person. NHL_SCRIPT_V1 is a COARSENING of the same per-draw features into seven scripts a
person can hold in their head; it reuses ``thesis.features.DrawFeatures`` (and therefore ``from_actual`` for the
realised game), so there is still exactly one simulator and one feature definition.

AUTHORITY: RESEARCH_ONLY. Nothing here places, routes or sizes a real wager. Research candidates are research
observations with a governance status; their stakes (if any) are the existing whole-dollar research stakes.
"""

SCRIPT_VERSION = "NHL_SCRIPT_V1"
SCRIPT_METHODOLOGY = "nhl-script-1.0"
REALIZED_VERSION = "nhl-realized-script-1.0"
SURVIVAL_VERSION = "nhl-survival-1.0"
CANDIDATE_RULES_VERSION = "nhl-candidates-1.0"
AUTHORITY = "RESEARCH_ONLY"
