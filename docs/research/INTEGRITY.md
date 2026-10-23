# Research integrity: how frozen inputs are protected

> RESEARCH_ONLY. Nothing here changes a model, price, stake, cap, routing or authority.

New historical seasons are routinely imported for research (2015–2021, then 2008–2014). Three things must not move when that happens: the inputs of the **production shadow arms** and **frozen walk-forward drivers**, the **evaluation cohorts** of earlier studies, and the **committed result tables and preregistrations**.

| protection | mechanism | where |
|---|---|---|
| Production shadows (`shadow_v2`, `shadow_oa`, `shadow_player`) and the frozen walk-forwards (`walk_forward`, `walk_forward_v2` default path) read only **pinned seasons** (team games and results ≥ 2022, skater tables and shots ≥ 2021). Recent seasons still flow in; older ones are held out. | `history.pinned_seasons`, a static guard that fails if any protected module calls a history loader without explicit seasons, a spy test that checks the seasons actually requested | `tests/test_research_integrity.py` |
| Research drivers that deliberately read all seasons are on a reviewed allow-list; a new full-history reader fails the test until it is added on purpose. | AST guard | same |
| Every historical data file, every production parameter file and every frozen research artifact (preregistrations, amendments, walk-forward/challenger result tables) has a registered sha256. A modified or deleted file, or an **unregistered new data/parameter file**, fails CI. | `INTEGRITY_REGISTRY.json`, `research/integrity.py` | `python -m nhl_edge.research.integrity check` |
| Cohort definitions (unexposed/exposed/fresh seasons, minimum-season counts) and the promotion thresholds are pinned to their registered literal values. | `cohort_values()` vs the registry | same |

**Adding a season** (welcome): drop the files in, run `python -m nhl_edge.research.integrity register`, review the diff of the registry in the PR. The command only appends. **Changing something frozen** is never done in place: write a new, differently named file (a new parameter version, an amendment document, a new results directory) and register that. The registry refuses to rewrite an existing entry.

This does not make a retrospective result independent: whether a season is *exposed* to a model family is recorded in each study's own preregistration and tier definitions, which are pinned here.
