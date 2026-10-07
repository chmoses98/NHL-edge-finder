"""SIFT-facing NHL research layer for the explorer export (additive; contract 1.1.1 unchanged).

Everything here rides on slots the contract already has:

* opponent-adjusted team metrics (``met_nhl.oa_*``): ordinary metric registry entries with
  ``supports.opponent_adjustment = true``; their observations carry the adjusted number in ``value`` AND
  ``adjusted_value`` and the raw same-games number in ``extensions.raw_value`` -- so a raw rank can never be mistaken
  for an adjusted rank (they are different metric ids) and the raw number is never overwritten;
* ``event_research.extensions.nhl_scripts_v1``: the NHL_SCRIPT_V1 block of the game (scripts, compact
  script-conditioned market matrix, research candidates), or an explicit NOT_SIMULATED status;
* ``event_research.extensions.nhl_matchup_v1``: ranked "What Matters" findings, each labelled with its BASIS
  (OPPONENT_ADJUSTED / MODEL / AVAILABILITY / CONTEXT / RAW) and whether it may be cited as betting evidence;
* ``event_research.context.notes``: deterministic one-line summaries, which the handicap packet already carries;
* ``metric_registry`` entry ``met_nhl.model_learning_stage`` whose ``extensions.learning_v1`` is the scorecard (the
  registry is loaded on every sport page, so the LEARNING status costs no extra request).

BETTING-EVIDENCE RULE (tested): only findings with basis OPPONENT_ADJUSTED, MODEL or AVAILABILITY have
``evidence_eligible = true``. RAW statistics (raw xG%, CF%, goals, save %, PP%, PK%, form) are CONTEXT only.
"""

from __future__ import annotations

from typing import Any

from edge_finder_contract import research as R

from nhl_edge.features.opponent_adjust import OPP_ADJ_VERSION, AdjFit, fit_all
from nhl_edge.features.opponent_adjust import methodology as oa_methodology

SPORT = "NHL"
OA_WINDOW_LABEL = "5v5 recency-weighted"
EVIDENCE_BASES = ("OPPONENT_ADJUSTED", "MODEL", "AVAILABILITY")
#: slug, metric key, field, name, short, higher_is_better, unit, description
OA_METRICS = [
    ("oa_xgf60_5v5", "xg", "off", "Opponent-adjusted 5v5 xGF/60", "adj xGF/60", True, "xG per 60",
     "Expected goals the team generates per 60 minutes of 5v5 play against a league-average defense on neutral ice."),
    ("oa_xga60_5v5", "xg", "def", "Opponent-adjusted 5v5 xGA/60", "adj xGA/60", False, "xG per 60",
     "Expected goals the team allows per 60 minutes of 5v5 play to a league-average offense on neutral ice."),
    ("oa_xgf_pct_5v5", "xg", "share", "Opponent-adjusted 5v5 xG share", "adj xGF%", True, "share",
     "Adjusted offense / (adjusted offense + adjusted defense) for 5v5 expected goals."),
    ("oa_cf_pct_5v5", "cf", "share", "Opponent-adjusted 5v5 shot-attempt share", "adj CF%", True, "share",
     "Shot-attempt (Corsi) share with each opponent's offense and defense removed."),
    ("oa_hdxgf_pct_5v5", "hdxg", "share", "Opponent-adjusted 5v5 high-danger xG share", "adj HDxGF%", True, "share",
     "High-danger expected-goals share with each opponent's offense and defense removed."),
    ("oa_gf60_5v5", "g", "off", "Opponent-adjusted 5v5 goals for/60", "adj GF/60", True, "goals per 60",
     "5v5 goals scored per 60 against a league-average defense (finishing and chance creation, opponent removed)."),
    ("oa_ga60_5v5", "g", "def", "Opponent-adjusted 5v5 goals against/60", "adj GA/60", False, "goals per 60",
     "5v5 goals allowed per 60 to a league-average offense (defense and goaltending, opponent removed)."),
]
LIM_OA = ("opponent adjustment nhl-oppadj-1.0 is a RESEARCH layer: weighted ridge offense/defense effects on 5v5 rates, walk-forward "
          "sanity-checked only, not a DATA_ONLY_V1 input; special teams and save percentage are not adjusted")


def _r(x: Any, n: int = 4) -> float | None:
    return None if x is None else round(float(x), n)


# ------------------------------------------------------------------------------------------------ opponent adjustment
def adjusted_fits(team_games: list[dict], as_of: str, season: int | None) -> dict[str, AdjFit]:
    """Fit every adjusted metric on regular-season 5v5 rows dated strictly before ``as_of`` (current + previous season)."""
    if season is None:
        return {}
    rows = [r for r in team_games if r.get("situation") == "5on5" and r.get("game_type") == 2]
    if not rows:
        return {}
    # season of the cutoff: if the current season has no 5v5 rows yet, the most recent season with rows is "current"
    have = sorted({int(r["season"]) for r in rows})
    s = season if season in have else have[-1]
    fits = fit_all(rows, as_of=as_of[:10], season=s, metrics=("xg", "cf", "hdxg", "g"))
    return {k: v for k, v in fits.items() if v.mu is not None}


def oa_value(a: Any, field: str) -> tuple[float | None, float | None, float | None]:
    """(adjusted, raw, se) for one team and field."""
    if field == "off":
        return a.off_adj, a.off_raw, a.off_se
    if field == "def":
        return a.def_adj, a.def_raw, a.def_se
    return a.share_adj, a.share_raw, None


def publish_adjusted(c: Any, fits: dict[str, AdjFit], *, reg_metric: Any, make_ranking: Any, team_obs: dict, team_rank_refs: dict,
                     team_ids: list[int], tname: dict, abbrev: dict, team_pid: Any, now: str) -> list[str]:
    """Register ``met_nhl.oa_*`` metrics, rank the teams by the ADJUSTED value and attach observations to team profiles.
    Returns the published metric ids."""
    if not fits:
        return []
    window = R.window("CUSTOM", label=OA_WINDOW_LABEL)
    as_of = next(iter(fits.values())).as_of + "T00:00:00Z"
    q = c.q("RESEARCH", "computed by nhl research-export (features/opponent_adjust.py) from MoneyPuck 5v5 team game logs", data_as_of=as_of,
            limitations=[LIM_OA], production=True)
    out = []
    for slug, key, field, name, short, hib, unit, desc in OA_METRICS:
        f = fits.get(key)
        if f is None:
            continue
        mid = reg_metric(slug, name=name, short=short, description=desc + " Weighted ridge regression rate = mu + OFF(team) + DEF(opponent) + home, "
                         "fit on games before the cutoff (this + last season, recency-weighted). The raw rate on the same games and weights is "
                         "kept in each observation's extensions.raw_value.", entity_type="TEAM", category="opponent_adjusted",
                         subcategory="5v5", stat_type="PERCENT" if field == "share" else "RATE", source="nhl research-export opponent adjustment",
                         quality=q, hib=hib, unit=unit, supports=R.supports(rank=True, percentile=True, opponent_adjustment=True, schedule_adjustment=True),
                         windows=[OA_WINDOW_LABEL], universe="NHL teams (32 active clubs)", update="every research export",
                         limitations=[LIM_OA], ext={"basis": "OPPONENT_ADJUSTED", "version": OPP_ADJ_VERSION, "methodology": oa_methodology()})
        vals, raw = [], {}
        for tid in team_ids:
            a = f.teams.get(tid)
            if a is None or a.status == "INSUFFICIENT":
                continue
            adj, rv, se = oa_value(a, field)
            if adj is None:
                continue
            raw[tid] = (rv, se, a)
            vals.append({"entity_id": team_pid(tid), "display_name": tname.get(tid, str(tid)), "short_name": abbrev.get(tid), "value": _r(adj),
                         "adjusted_value": _r(adj), "sample_size": a.games, "path": R.team_path(team_pid(tid)), "_tid": tid})
        rk = make_ranking(mid, universe="NHL teams, opponent-adjusted 5v5", entity_type="TEAM", window=window, as_of=as_of, hib=hib, values=vals,
                          quality=q, ufilter="active NHL teams with >= 10 games in the window")
        for v in vals:
            tid = v["_tid"]
            rv, se, a = raw[tid]
            ctx = R.context_from_ranking(rk, v["entity_id"]) if rk else None
            o = R.observation(sport=SPORT, metric_id=mid, entity_id=v["entity_id"], entity_type="TEAM", value=v["value"], adjusted_value=v["value"],
                              window=window, as_of=as_of, source="nhl research-export opponent adjustment (nhl-oppadj-1.0)", quality_status="RESEARCH",
                              unit=unit, sample_size=a.games, context=ctx,
                              extensions={"basis": "OPPONENT_ADJUSTED", "raw_value": _r(rv), "raw_basis": "RAW (same games and weights, not adjusted)",
                                          "standard_error": _r(se), "games_current_season": a.games_current, "status": a.status,
                                          "schedule_effect": _r(None if rv is None else rv - v["value"]), "version": OPP_ADJ_VERSION})
            team_obs[tid].append(o)
            if rk and ctx:
                team_rank_refs[tid].append({"ranking_id": rk["ranking_id"], "metric_id": mid, "window_label": OA_WINDOW_LABEL, "split": None,
                                            "path": R.ranking_path(rk["ranking_id"])})
        out.append(mid)
    return out


# ------------------------------------------------------------------------------------------------ What Matters
def _pct(rank: int | None, size: int | None) -> float | None:
    if not rank or not size or size < 2:
        return None
    return 1.0 - (rank - 1) / (size - 1)  # 1 best .. 0 worst


def _obs(team_obs: dict, tid: int | None, mid: str) -> dict | None:
    if tid is None:
        return None
    return next((o for o in team_obs.get(tid, []) if o["metric_id"] == mid), None)


def _rk(o: dict | None) -> tuple[int | None, int | None]:
    ctx = (o or {}).get("context") or {}
    return ctx.get("rank"), ctx.get("universe_size")


def matchup_findings(*, home: str, away: str, home_tid: int | None, away_tid: int | None, team_obs: dict, mid: Any, packet_game: dict | None,
                     injuries: dict[str, int], scripts: dict | None) -> dict[str, Any]:
    """Ranked findings for one game. ``mid``: slug -> metric id. Every finding states its basis; raw statistics are context."""
    F: list[dict[str, Any]] = []

    def add(fid: str, title: str, text: str, basis: str, importance: float, *, team: str | None = None, values: dict | None = None,
            metric_ids: list[str] | None = None, source: str = "") -> None:
        F.append({"id": fid, "title": title, "text": text, "basis": basis, "evidence_eligible": basis in EVIDENCE_BASES,
                  "importance": round(max(0.0, min(1.0, importance)), 3), "team": team, "values": values or {}, "metric_ids": metric_ids or [],
                  "source": source})

    # opponent-adjusted 5v5 offense vs defense, both directions
    for att, att_tid, dfn, dfn_tid in ((home, home_tid, away, away_tid), (away, away_tid, home, home_tid)):
        o_off, o_def = _obs(team_obs, att_tid, mid("oa_xgf60_5v5")), _obs(team_obs, dfn_tid, mid("oa_xga60_5v5"))
        if o_off and o_def:
            r1, n1 = _rk(o_off)
            r2, n2 = _rk(o_def)
            p_off, p_def = _pct(r1, n1), _pct(r2, n2)
            if p_off is None or p_def is None:
                continue
            score = (p_off + (1.0 - p_def)) / 2.0 - 0.5  # + = attack advantage
            word = "advantage" if score > 0.08 else ("disadvantage" if score < -0.08 else "even matchup")
            add(f"oa_5v5_{att}", f"{att} 5v5 attack vs {dfn} defense",
                f"{att}'s opponent-adjusted 5v5 chance creation ranks {r1} of {n1} ({o_off['value']:.2f} xGF/60); {dfn}'s adjusted 5v5 defense ranks "
                f"{r2} of {n2} ({o_def['value']:.2f} xGA/60): {word} for {att}.", "OPPONENT_ADJUSTED", 0.35 + 1.3 * abs(score), team=att,
                values={"att_rank": r1, "def_rank": r2, "att_value": o_off["value"], "def_value": o_def["value"], "score": round(score, 3)},
                metric_ids=[mid("oa_xgf60_5v5"), mid("oa_xga60_5v5")], source=f"{OPP_ADJ_VERSION} (RESEARCH)")
    # adjusted share gap
    oh, oa = _obs(team_obs, home_tid, mid("oa_xgf_pct_5v5")), _obs(team_obs, away_tid, mid("oa_xgf_pct_5v5"))
    if oh and oa:
        gap = oh["value"] - oa["value"]
        lead = home if gap > 0 else away
        add("oa_share_gap", "Adjusted 5v5 territorial edge",
            f"{lead} holds the better opponent-adjusted 5v5 xG share ({max(oh['value'], oa['value']):.1%} vs {min(oh['value'], oa['value']):.1%}).",
            "OPPONENT_ADJUSTED", 0.3 + 4.0 * abs(gap), team=lead, values={"home": oh["value"], "away": oa["value"]},
            metric_ids=[mid("oa_xgf_pct_5v5")], source=f"{OPP_ADJ_VERSION} (RESEARCH)")
    pg = packet_game or {}
    gt = pg.get("goaltending") or {}
    for side, ab in (("home", home), ("away", away)):
        g = gt.get(side) or {}
        st, nm, fac = g.get("status"), g.get("player_name"), g.get("factor")
        if not st:
            continue
        if st != "CONFIRMED":
            add(f"goalie_status_{side}", f"{ab} starter not confirmed", f"{ab}'s starter is {str(st).lower()}" + (f" ({nm})" if nm else "") +
                "; the model prices a confidence-weighted mix of plausible starters.", "AVAILABILITY", 0.75 if st == "UNKNOWN" else 0.55, team=ab,
                values={"status": st, "name": nm, "confidence": g.get("confidence")}, source="goalie status timeline (DailyFaceoff + boxscore)")
        if fac is not None and abs(float(fac) - 1.0) >= 0.04:
            better = float(fac) < 1.0
            add(f"goalie_factor_{side}", f"{nm or ab} in net", f"{nm or ab+' starter'} ({str(st).lower()}): the model's goalie factor is {float(fac):.2f}, i.e. "
                f"{abs(1 - float(fac)):.0%} {'fewer' if better else 'more'} goals than expected allowed (regressed GA/xGA, a model input).",
                "MODEL", 0.25 + 2.5 * abs(1.0 - float(fac)), team=ab, values={"factor": _r(fac, 3), "status": st},
                source="DATA_ONLY_V1 goalie factor (regressed GA/xGA; raw save results, not opponent-adjusted)")
    ctx = pg.get("context") or {}
    for side, ab in (("home", home), ("away", away)):
        if ctx.get(f"{side}_b2b"):
            add(f"b2b_{side}", f"{ab} on a back-to-back", f"{ab} played yesterday: the model lowers its offense ~3.5% and raises goals against ~2.5%.",
                "MODEL", 0.5, team=ab, values={"rest_days": ctx.get(f"{side}_rest_days")}, source="features/ratings.py back-to-back adjustment")
    sim = (pg.get("model") or {}).get("sim") or {}
    if sim.get("home_lambda") is not None and sim.get("p_home_win") is not None:
        ph = float(sim["p_home_win"])
        fav = home if ph >= 0.5 else away
        add("model_projection", "Model projection", f"DATA_ONLY_V1 projects {home} {float(sim['home_lambda']):.2f} - {away} {float(sim['away_lambda']):.2f} expected goals; "
            f"{fav} wins {max(ph, 1 - ph):.0%} of simulations.", "MODEL", 0.3 + 1.2 * abs(ph - 0.5), team=fav,
            values={"home_lambda": _r(sim.get("home_lambda"), 3), "away_lambda": _r(sim.get("away_lambda"), 3), "p_home_win": _r(ph),
                    "total_mean": _r(sim.get("total_mean"), 3)}, source="DATA_ONLY_V1 (nhl-sim-1.1)")
    for ab, n in injuries.items():
        if n >= 2:
            add(f"injuries_{ab}", f"{ab} injuries", f"{ab} lists {n} players out or doubtful (name-matched; injuries are not modelled in V1 beyond lineups).",
                "AVAILABILITY", 0.25 + 0.05 * min(n, 6), team=ab, values={"n": n}, source="ESPN injury list (archive context/injuries)")
    # raw special teams: CONTEXT ONLY
    for slug, lab in (("pp_pct", "power play"), ("pk_pct", "penalty kill")):
        oh, oa = _obs(team_obs, home_tid, mid(slug)), _obs(team_obs, away_tid, mid(slug))
        if oh and oa and oh.get("value") is not None and oa.get("value") is not None:
            add(f"raw_{slug}", f"Special teams ({lab}, raw)", f"Raw {lab}: {home} {oh['value']:.1%} vs {away} {oa['value']:.1%}. Not opponent-adjusted: context, "
                "not betting evidence.", "RAW", 0.15, values={"home": oh["value"], "away": oa["value"]}, metric_ids=[mid(slug)],
                source="NHL official team summary (raw)")
    if scripts and scripts.get("most_likely"):
        ml = scripts["most_likely"]
        add("script_most_likely", "Most likely script", f"Most likely script: {ml['label']} ({ml['probability']:.0%} of simulations); "
            f"{len(scripts.get('scripts') or [])} scripts reconcile to 100%.", "MODEL", 0.3, values=ml, source="NHL_SCRIPT_V1 on the PLAYER_SIM_V1 joint draw")
    F.sort(key=lambda x: (-x["importance"], x["id"]))
    top = [f for f in F if f["basis"] != "RAW"][:5]
    return {"version": "nhl-matchup-1.0", "findings": F, "what_matters": [f["id"] for f in top], "evidence_bases": list(EVIDENCE_BASES),
            "rule": "only OPPONENT_ADJUSTED, MODEL and AVAILABILITY findings may be cited as betting evidence; RAW statistics are context"}


# ------------------------------------------------------------------------------------------------ scripts extension
TIER_CODE = {"ROBUST": "R", "MODERATE": "M", "FRAGILE": "F", "DOES_NOT_SURVIVE": "X", "UNAVAILABLE": "U"}
MAX_CANDIDATES = 12


def _q3(x: Any) -> float | None:
    return None if x is None else round(float(x), 3)


def _side_row(sd: dict | None) -> list | None:
    if not sd:
        return None
    return [sd.get("ask_cents"), _q3(sd.get("cost")), _q3(sd.get("delta")), _q3(sd.get("ev_adjusted")), _q3(sd.get("mass_survived")),
            TIER_CODE.get(sd.get("tier"), "U"), sd.get("survives"), sd.get("failure_script")]


def scripts_extension(gr: dict | None, *, generated_at: str | None, start_time_utc: str | None, event_tickers: set[str]) -> dict[str, Any]:
    """Compact, versioned ``extensions.nhl_scripts_v1`` for one event (or an explicit status when there is none)."""
    if not gr:
        return {"status": "NOT_SIMULATED", "script_version": "NHL_SCRIPT_V1",
                "reason": "the NHL model simulates a game on its game day; this event is not in the latest simulated slate"}
    pre = None
    if generated_at and start_time_utc:
        pre = generated_at < start_time_utc
    cands = []
    for c in (gr.get("candidates") or [])[:MAX_CANDIDATES]:
        sv = dict(c["survival"])
        sv.pop("bet_id", None)
        cands.append({**{k: c[k] for k in ("rank", "bet_id", "ticker", "side", "title", "family", "team", "opponent", "price", "p_model", "p_conservative",
                                          "p_market_mid", "edge_vs_mid", "ev_raw", "ev_adjusted", "bet_up_to_cents", "uncertainty", "robustness",
                                          "robustness_word", "family_reliability", "benchmark_category", "expression_fidelity", "primary_thesis",
                                          "thesis_concentration", "dependencies", "governance", "exposure_group", "duplicate_of", "research_score",
                                          "authority")},
                      "survival": sv, "supporting": c["supporting"][:3], "opposing": c["opposing"][:3], "relations": c["relations"][:2]})
    markets = [[m["ticker"], m.get("family"), m.get("team"), _q3(m.get("p_yes")), _q3(m.get("p_yes_mid")), [_q3(x) for x in m.get("p_yes_by_script") or []],
                _side_row(m.get("yes")), _side_row(m.get("no"))]
               for m in gr.get("markets") or [] if m["ticker"] in event_tickers]
    return {
        "status": "OK", "script_version": gr["script_version"], "methodology_version": gr["methodology_version"], "survival_version": gr["survival_version"],
        "candidate_rules_version": gr["candidate_rules_version"], "authority": gr["authority"], "generated_at": generated_at, "pregame": pre,
        "n_draws": gr["n_draws"], "draw_source": gr.get("draw_source"), "script_order": gr["script_order"], "scripts": gr["scripts"],
        "most_likely": gr.get("most_likely"), "probability_check": gr.get("probability_check"),
        "market_columns": ["ticker", "family", "team", "p_yes", "p_yes_mid", "p_yes_by_script", "yes", "no"],
        "side_columns": ["ask_cents", "cost", "delta", "ev_adjusted", "mass_survived", "tier", "survives", "failure_script"],
        "tier_codes": {v: k for k, v in TIER_CODE.items()},
        "markets": markets, "unpriced": gr.get("unpriced") or [], "candidates": cands, "candidates_total": len(gr.get("candidates") or []),
        "candidate_summary": gr.get("candidate_summary"), "context": gr.get("context"), "rules": gr.get("rules"),
    }


def script_notes(ext: dict[str, Any]) -> list[str]:
    """Deterministic one-liners for event_research.context.notes (the handicap packet carries these)."""
    if ext.get("status") != "OK":
        return []
    sc = sorted(ext["scripts"], key=lambda s: (-s["probability"], s["code"]))
    out = ["NHL_SCRIPT_V1 game scripts (simulated, sum 100%): " + "; ".join(f"{s['label']} {s['probability']:.0%}" for s in sc)]
    for c in ext["candidates"][:3]:
        if c["governance"]["status"] == "REJECTED":
            continue
        sv = c["survival"]
        fail = next((s["label"] for s in sc if s["id"] == sv.get("failure_script")), None)
        out.append(f"Research candidate (RESEARCH_ONLY): {c['title']} {c['side'].upper()} at {c['price']['ask_cents']}c, fair {c['p_model']:.1%} "
                   f"(conservative {c['p_conservative']:.1%}), bet up to {c['bet_up_to_cents']}c, {c['robustness_word'].lower()} — survives "
                   f"{(sv.get('mass_survived') or 0):.0%} of simulated games" + (f", fails mainly if {fail}" if fail else "") +
                   f"; {c['governance']['status_word'].lower()}")
    return out


# ------------------------------------------------------------------------------------------------ learning metric
def learning_extension(rep: dict | None, eval_status: dict | None) -> dict[str, Any]:
    """Compact scorecard for ``met_nhl.model_learning_stage.extensions.learning_v1``."""
    st = (eval_status or {}).get("steps") or {}
    job = {"evaluated_at": (eval_status or {}).get("evaluated_at_utc"), "learning_step": st.get("learning"), "steps": st}
    if not rep:
        return {"status": "UNAVAILABLE", "reason": "no eval/report_learning.json in the archive yet (the evaluate job writes it after settlement)", "job": job}
    failed = isinstance(st.get("learning"), str) and st["learning"].startswith("FAILED")
    keep = ("version", "generated_at_utc", "authority", "versions", "counts", "stage", "probability", "windows", "projection", "scripts",
            "research_candidates", "script_candidates", "actual_wagers", "unknowns")
    out = {k: rep.get(k) for k in keep}
    out["status"] = "STALE_LAST_RUN_FAILED" if failed else "OK"
    out["job"] = job
    return out


def register_learning(reg_metric: Any, c: Any, ext: dict[str, Any], now: str) -> str:
    stage = ((ext.get("stage") or {}).get("stage")) or "UNAVAILABLE"
    q = c.q("RESEARCH" if ext.get("status") == "OK" else "UNKNOWN", "NHL-edge-finder evaluate job (eval/report_learning.json)",
            data_as_of=ext.get("generated_at_utc"), limitations=["small samples are published with their n; maturity gates never use ROI"])
    return reg_metric("model_learning_stage", name="NHL model learning stage", short="Learning", entity_type="MATCHUP", category="model_quality",
                      description=f"Evidence maturity of the NHL research engine (currently {stage}). EARLY_LEARNING -> CALIBRATION_BUILDING -> "
                      "EVIDENCE_EMERGING -> VALIDATED, by documented sample and calibration gates; a status, never betting authority. "
                      "extensions.learning_v1 holds the scorecard.", stat_type="OTHER", source="NHL-edge-finder learning loop", quality=q, hib=None,
                      unit=None, supports=R.supports(), windows=[], universe="the NHL research engine", update="every evaluate run",
                      limitations=["research candidates are scored as shadow positions; actual routed wagers are never mixed in"],
                      ext={"learning_v1": ext})
