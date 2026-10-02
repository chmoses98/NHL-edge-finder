"""DIAGNOSTIC "what would have happened under the new rules?" replay of a past slate (RESEARCH_ONLY).

For each game of ``--date`` the replay re-runs ``nhl simulate`` at the decision instant of the game's FINAL production
card (the latest complete pregame thesis-card snapshot; ``--cutoff`` for slates without one), on a link-copy of the
archive, so only information observed before that instant is visible (``nhl simulate`` reads archive partitions
observed at or before ``--now``; params / history end before the season). It does this twice:

* NEW rules: this checkout's code (expression fidelity preference, research governance, research stakes);
* OLD rules (optional ``--old-src``): the pre-change code, in a subprocess with ``PYTHONPATH=<old src>``, which also
  checks that the replay reproduces what production logged (determinism / point-in-time check).

and compares old funded card vs new funded card, shadow-only bets, bets removed by the expression-fidelity rule or the
market-disagreement gate, broad-market substitutions, exposure / correlation, and realized P/L where contracts have
settled in the archive. Nothing is tuned and nothing here is evidence that the new rules are better: two slates prove
nothing; the purpose is to verify that the architecture behaves as intended.

    python -m nhl_edge.research.rules_replay --archive <ARCHIVE COPY> --date 2026-10-01 --work <scratch> \
        --old-src <old checkout>/src --out docs/research/repair_pass/replay_2026-10-01
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from nhl_edge.thesis.fidelity import from_logged
from nhl_edge.timeutil import iso, parse_iso


def link_copy(src: Path, dst: Path) -> Path:
    """Hard-link every immutable ledger partition file (``.../dt=*/...``) and really copy everything else (manifest,
    STATUS files, slates/latest, eval/...), so a replay writing into ``dst`` can never modify ``src``."""
    if dst.exists():
        shutil.rmtree(dst)
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d != ".git"]
        rel = Path(root).relative_to(src)
        (dst / rel).mkdir(parents=True, exist_ok=True)
        immutable = any(part.startswith("dt=") for part in rel.parts)
        for f in files:
            s, d = Path(root) / f, dst / rel / f
            if immutable and not f.endswith(".tmp"):
                os.link(s, d)
            else:
                shutil.copy2(s, d)
    return dst


def production_final_cutoffs(archive: Path, date: str) -> tuple[dict[str, dict[str, Any]], dict[str, datetime]]:
    """gid -> final production snapshot info for the slate's games; and gid -> scheduled start."""
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.workflows.settle import latest_schedule
    from nhl_edge.workflows.thesis_postmortem import final_snapshots

    led = Ledger(archive)
    sched = latest_schedule(led)
    gids = sorted(g for g, r in sched.items() if str(r.get("game_date_et")) == date and r.get("status") not in ("postponed", "canceled"))
    starts = {g: parse_iso(sched[g]["start_time_utc"]) for g in gids}
    games = [r for r in led.iter_rows("thesis_games") if str(r.get("game_id")) in gids]
    dec = [r for r in led.iter_rows("thesis_decisions") if str(r.get("game_id")) in gids]
    return {g: v for g, v in final_snapshots(games, dec, starts).items() if g in gids}, starts


def _run_new(arch: Path, data: Path, now: str, date: str) -> dict[str, Any]:
    from nhl_edge.research.thesis_replay import replay

    t0 = time.perf_counter()
    res = replay(arch, data, now, date)
    pk = json.loads((Path(res["slate_dir"]) / "packet.json").read_text()) if res.get("slate_dir") else {}
    return {"rc": res["rc"], "seconds": round(time.perf_counter() - t0, 1), "thesis_card": pk.get("thesis_card"), "slate_dir": res.get("slate_dir")}


def _run_old(arch: Path, data: Path, now: str, date: str, old_src: Path) -> dict[str, Any]:
    env = dict(os.environ, PYTHONPATH=str(old_src))
    t0 = time.perf_counter()
    p = subprocess.run([sys.executable, "-m", "nhl_edge.research.thesis_replay", "--archive", str(arch), "--data", str(data), "--now", now, "--date", date],
                       env=env, capture_output=True, text=True, timeout=1800)
    stamp = parse_iso(now).strftime("%Y%m%dT%H%M%SZ")
    slates = sorted((arch / "slates" / f"dt={date}").glob(f"{stamp}_*"))
    pk = json.loads((slates[-1] / "packet.json").read_text()) if slates else {}
    return {"rc": p.returncode, "seconds": round(time.perf_counter() - t0, 1), "thesis_card": pk.get("thesis_card"), "stderr_tail": (p.stderr or "")[-600:]}


def _outcomes(archive: Path) -> dict[str, str]:
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.workflows.evaluate import best_settlements

    return {t: r.outcome.value for t, r in best_settlements(Ledger(archive)).items()}


def _pl(stake: float, cost: float | None, ticker: str, side: str, outcomes: dict[str, str]) -> tuple[str, float | None]:
    o = outcomes.get(ticker)
    if o not in ("YES", "NO"):
        return ("UNSETTLED" if o is None else o), (None if o is None else 0.0)
    won = (o == "YES") == (side.lower() == "yes")
    if not cost or not stake:
        return ("WON" if won else "LOST"), 0.0
    return ("WON" if won else "LOST"), round(stake * ((1.0 if won else 0.0) - cost) / cost, 2)


def _card_view(g: dict[str, Any], outcomes: dict[str, str], old: bool) -> dict[str, Any]:
    bets = []
    for e in g.get("card") or []:
        c = e["contract"]
        cost = (e.get("executable_price") or {}).get("cost_per_contract")
        rg = e.get("research_governance") or {}
        nominal = float(e["recommended_stake"]["dollars"])
        research = None if old else int(rg.get("research_stake_dollars") or 0)
        res_n, pl_n = _pl(nominal, cost, c["ticker"], c["side"], outcomes)
        _, pl_r = _pl(research or 0.0, cost, c["ticker"], c["side"], outcomes)
        rels = e.get("same_game_relationships") or {}
        # the old code has no fidelity field: reconstruct it from the logged P(bet | thesis) (same draws, same thesis)
        fd = e.get("expression_fidelity") if isinstance(e.get("expression_fidelity"), dict) and "fidelity_class" in e["expression_fidelity"] else \
            from_logged(e.get("primary_thesis"), c["family"])
        bets.append({"bet_id": e["bet_id"], "family": c["family"], "price_cents": (e.get("executable_price") or {}).get("ask_cents"), "cost": cost,
                     "p_model": e["fair_probability"]["p_model_joint_draw"], "p_adjusted": e["fair_probability"]["p_confidence_adjusted"],
                     "p_kalshi_mid": e["fair_probability"].get("p_kalshi_mid"), "ev_adjusted": e["estimated_edge"]["ev_adjusted_per_contract"],
                     "thesis": (e.get("primary_thesis") or {}).get("key"), "nominal_stake": nominal, "research_status": None if old else rg.get("status"),
                     "research_label": None if old else rg.get("label"), "research_stake": research, "fidelity": fd.get("fidelity_class"),
                     "thesis_capture": fd.get("thesis_capture"), "result": res_n, "pl_nominal": pl_n, "pl_research": None if old else pl_r,
                     "phis": {k: v.get("phi") for k, v in rels.items() if isinstance(v, dict) and "phi" in v}})
    return {"bets": bets, "overrides": [o for o in ((g.get("review") or {}).get("overrides") or []) if o.get("applied")] if not old else []}


def _exposure(bets: list[dict[str, Any]], key: str) -> dict[str, Any]:
    on = [b for b in bets if (b.get(key) or 0) > 0]
    tot = sum(float(b[key]) for b in on)
    by_t: dict[str, float] = defaultdict(float)
    for b in on:
        by_t[b["thesis"] or "?"] += float(b[key])
    phis = [abs(float(v)) for b in on for o, v in b["phis"].items() if v is not None and any(o == x["bet_id"] for x in on)]
    settled = [b for b in on if b["result"] in ("WON", "LOST", "VOID", "PUSH", "UNSETTLEABLE")]
    pl_key = "pl_research" if key == "research_stake" else "pl_nominal"
    st_set = sum(float(b[key]) for b in settled)
    pl = sum(float(b[pl_key] or 0) for b in settled)
    return {"n_bets": len(on), "stake": round(tot, 2), "n_player_props": sum(1 for b in on if b["family"].startswith(("player_", "goalie_", "first_goal"))),
            "largest_thesis_share": round(max(by_t.values()) / tot, 3) if tot else None, "mean_abs_phi_pairs": round(sum(phis) / len(phis), 3) if phis else None,
            "n_settled": len(settled), "settled_stake": round(st_set, 2), "realized_pl": round(pl, 2), "roi_settled": round(pl / st_set, 4) if st_set else None}


def compare(date: str, finals: dict[str, dict[str, Any]], runs: dict[str, dict[str, Any]], game_cutoff: dict[str, str], outcomes: dict[str, str],
            logged: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    games_out = {}
    agg = {"old": [], "new": []}
    for gid, cut in sorted(game_cutoff.items()):
        r = runs[cut]
        new_g = next((g for g in ((r["new"].get("thesis_card") or {}).get("games") or []) if str(g["game_id"]) == gid), None)
        old_g = next((g for g in (((r.get("old") or {}).get("thesis_card") or {}).get("games") or []) if str(g["game_id"]) == gid), None)
        new_v = _card_view(new_g or {}, outcomes, old=False)
        old_v = _card_view(old_g or {}, outcomes, old=True) if old_g is not None else None
        if old_v is None and logged.get(gid):  # no old-code replay: the production log is the old card
            old_v = {"bets": [{"bet_id": d["bet_id"], "family": d["family"], "price_cents": d.get("executable_price_cents"), "cost": d.get("cost_per_contract"),
                               "p_model": d.get("p_model"), "p_adjusted": d.get("p_adjusted"), "p_kalshi_mid": d.get("p_kalshi_mid"), "ev_adjusted": d.get("ev_adjusted"),
                               "thesis": (d.get("primary_thesis") or {}).get("key"), "nominal_stake": d.get("stake_dollars"), "research_stake": None,
                               "fidelity": from_logged(d.get("primary_thesis"), d["family"])["fidelity_class"],
                               "thesis_capture": (d.get("primary_thesis") or {}).get("p_bet_given_thesis"),
                               **dict(zip(("result", "pl_nominal"), _pl(d.get("stake_dollars") or 0, d.get("cost_per_contract"), d["ticker"], d["side"], outcomes))),
                               "pl_research": None, "phis": {k: v.get("phi") for k, v in (d.get("joint_relationships") or {}).items()}} for d in logged[gid]], "overrides": []}
        new_ids = {b["bet_id"] for b in new_v["bets"]}
        funded = [b for b in new_v["bets"] if b["research_status"] == "FUNDED_RESEARCH"]
        shadow = [b for b in new_v["bets"] if b["research_status"] != "FUNDED_RESEARCH"]
        rs = (new_g or {}).get("research_status") or {}
        repro = None
        if old_v is not None and logged.get(gid):
            lg = {d["bet_id"]: d for d in logged[gid]}
            ob = {b["bet_id"]: b for b in old_v["bets"]}
            repro = {"same_bets": sorted(lg) == sorted(ob), "max_abs_p_model_diff": max([abs(float(ob[k]["p_model"]) - float(lg[k]["p_model"])) for k in ob if k in lg] or [0.0]),
                     "logged": sorted(lg), "replayed_old_code": sorted(ob)}
        games_out[gid] = {
            "cutoff": cut, "final_production_snapshot": {k: v for k, v in (finals.get(gid) or {}).items() if k in ("snapshot_id", "decided_at_utc", "status", "n_chosen")},
            "old_card": old_v, "new_optimiser_card": new_v["bets"], "new_funded": [b["bet_id"] for b in funded],
            "shadow_only": {b["bet_id"]: b["research_label"] for b in shadow},
            "removed_by_expression_fidelity": [o["replaced"] for o in new_v["overrides"]],
            "removed_by_market_disagreement_gate": [k for k, v in rs.items() if "LARGE_MARKET_DISAGREEMENT_UNCORROBORATED" in (v.get("label") or "")],
            "broad_market_substitutions": [o["text"] for o in new_v["overrides"]],
            "old_not_in_new": sorted({b["bet_id"] for b in (old_v or {}).get("bets", [])} - new_ids), "new_not_in_old": sorted(new_ids - {b["bet_id"] for b in (old_v or {}).get("bets", [])}),
            "exposure_old_nominal": _exposure((old_v or {}).get("bets", []), "nominal_stake"), "exposure_new_nominal": _exposure(new_v["bets"], "nominal_stake"),
            "exposure_new_funded": _exposure(new_v["bets"], "research_stake"), "reproduction_check": repro}
        agg["old"] += (old_v or {}).get("bets", [])
        agg["new"] += new_v["bets"]
    return {"date": date, "authority": "RESEARCH_ONLY", "diagnostic_only": True, "games": games_out,
            "slate": {"old_nominal": _exposure(agg["old"], "nominal_stake"), "new_nominal": _exposure(agg["new"], "nominal_stake"),
                      "new_funded_research": _exposure(agg["new"], "research_stake"),
                      "n_shadow_only": sum(len(v["shadow_only"]) for v in games_out.values()),
                      "n_removed_by_expression_fidelity": sum(len(v["removed_by_expression_fidelity"]) for v in games_out.values()),
                      "n_removed_by_market_disagreement_gate": sum(len(v["removed_by_market_disagreement_gate"]) for v in games_out.values())},
            "note": ("DIAGNOSTIC ONLY. Replayed at each game's final production decision instant on pregame data; no hindsight substitution. Realized P/L "
                     "covers settled contracts only. This is NOT evidence that the new rules are better: it verifies that the architecture behaves as intended.")}


def run(archive: Path, data: Path, date: str, work: Path, old_src: Path | None, cutoffs: list[str] | None) -> dict[str, Any]:
    finals, starts = production_final_cutoffs(archive, date)
    game_cutoff: dict[str, str] = {}
    if cutoffs:
        cs = sorted(parse_iso(c) for c in cutoffs)
        for g, st in starts.items():
            pre = [c for c in cs if c < st]
            if pre:
                game_cutoff[g] = iso(pre[-1])
    else:
        for g, v in finals.items():
            if v.get("status") == "OK":
                game_cutoff[g] = v["decided_at_utc"]
    logged = {g: v.get("chosen") or [] for g, v in finals.items() if v.get("status") == "OK"}
    runs: dict[str, dict[str, Any]] = {}
    for cut in sorted(set(game_cutoff.values())):
        tag = parse_iso(cut).strftime("%Y%m%dT%H%M%SZ")
        new_arch = link_copy(archive, work / f"new_{tag}")
        runs[cut] = {"new": _run_new(new_arch, data, cut, date)}
        if old_src is not None:
            old_arch = link_copy(archive, work / f"old_{tag}")
            runs[cut]["old"] = _run_old(old_arch, data, cut, date, old_src)
            shutil.rmtree(old_arch, ignore_errors=True)
        shutil.rmtree(new_arch, ignore_errors=True)
    out = compare(date, finals, runs, game_cutoff, _outcomes(archive), logged)
    out["runs"] = {c: {k: {kk: vv for kk, vv in v.items() if kk != "thesis_card"} for k, v in r.items()} for c, r in runs.items()}
    out["cards"] = {c: {k: (v.get("thesis_card") or {}).get("status") for k, v in r.items()} for c, r in runs.items()}
    return out


def markdown(rep: dict[str, Any]) -> str:
    s = rep["slate"]
    f = lambda x: "-" if x is None else (f"{x:+.2f}" if isinstance(x, float) else str(x))  # noqa: E731  (P/L, signed)
    p = lambda x: "-" if x is None else (f"{x:.3f}" if isinstance(x, float) else str(x))  # noqa: E731  (probabilities / ratios)
    L = [f"# Rules replay {rep['date']} — DIAGNOSTIC ONLY ({rep['authority']})", "", f"_{rep['note']}_", "",
         "| card | bets | stake | player props | largest thesis share | mean abs phi | settled | settled stake | realized P/L | ROI (settled) |",
         "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for lab, k in (("OLD (nominal optimiser card)", "old_nominal"), ("NEW optimiser card (nominal)", "new_nominal"), ("NEW FUNDED research ($)", "new_funded_research")):
        v = s[k]
        L.append(f"| {lab} | {v['n_bets']} | {v['stake']:.2f} | {v['n_player_props']} | {p(v['largest_thesis_share'])} | {p(v['mean_abs_phi_pairs'])} | {v['n_settled']} | "
                 f"{v['settled_stake']:.2f} | {v['realized_pl']:+.2f} | {f(v['roi_settled'])} |")
    L += ["", f"shadow-only (on the optimiser card, not funded): {s['n_shadow_only']} · removed by the expression-fidelity rule: {s['n_removed_by_expression_fidelity']} · "
          f"removed by the market-disagreement gate: {s['n_removed_by_market_disagreement_gate']}", ""]
    for gid, g in rep["games"].items():
        L += [f"## {gid} · cutoff {g['cutoff']}", ""]
        rc = g.get("reproduction_check")
        if rc:
            L.append(f"reproduction of the production card by the old code: same bets {rc['same_bets']}, max |p_model diff| {rc['max_abs_p_model_diff']:.4f}")
        L += ["", "| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |", "|---|---|---:|---:|---:|---:|---|---:|---|---|---:|"]
        for b in (g["old_card"] or {}).get("bets", []):
            L.append(f"| OLD | {b['bet_id']} | {p(b['p_model'])} | {p(b['p_adjusted'])} | {p(b['p_kalshi_mid'])} | {f(b['ev_adjusted'])} | {b['fidelity'] or '-'} "
                     f"({p(b['thesis_capture'])}) | {p(b['nominal_stake'])} | - | {b['result']} | {f(b['pl_nominal'])} |")
        for b in g["new_optimiser_card"]:
            L.append(f"| NEW | {b['bet_id']} | {p(b['p_model'])} | {p(b['p_adjusted'])} | {p(b['p_kalshi_mid'])} | {f(b['ev_adjusted'])} | {b['fidelity'] or '-'} "
                     f"({p(b['thesis_capture'])}) | {p(b['nominal_stake'])} | {b['research_label']} ${b['research_stake']} | {b['result']} | {f(b['pl_research'])} |")
        for t in g["broad_market_substitutions"]:
            L.append(f"- substitution: {t}")
        L.append("")
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--archive", required=True, help="a production archive copy (read only; never modified)")
    ap.add_argument("--data", default="data")
    ap.add_argument("--date", required=True)
    ap.add_argument("--work", required=True, help="scratch directory for the link-copies")
    ap.add_argument("--old-src", default=None, help="src/ of the pre-change code (optional; enables the old-code replay and reproduction check)")
    ap.add_argument("--cutoff", action="append", default=[], help="explicit decision instants (slates without a production thesis card)")
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    rep = run(Path(a.archive), Path(a.data), a.date, Path(a.work), Path(a.old_src) if a.old_src else None, a.cutoff or None)
    rep["generated_at_utc"] = iso(datetime.now().astimezone() - timedelta(0))
    if a.out:
        d = Path(a.out)
        d.mkdir(parents=True, exist_ok=True)
        (d / "replay.json").write_text(json.dumps(rep, indent=1, default=str))
        (d / "replay.md").write_text(markdown(rep))
    print(markdown(rep))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
