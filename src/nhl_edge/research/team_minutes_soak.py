"""Evaluates the pre-stated soak of the team-minute shadow (RESEARCH_ONLY): every NO-GO trigger of ``docs/research/team_minutes/GO_NO_GO.md``, with the thresholds exactly as written there.

Triggers (paired, game-clustered 95% intervals; the shadow compares ``team-minutes-1.0`` with the published ``team-minutes-0`` on the same row):
  T1  the upper bound of the change in total-TOI MSE (candidate minus published) is above 0, or the same for power-play TOI MSE;
  T2  the candidate's total-TOI or PP-TOI mean bias is larger in magnitude than the published template's;
  T3a more than 2% of the shadow rows used the league-clock fallback;
  T3b a shadow error (error count in a run's manifest entry, or a marker row) in more than one run in ten;
  T4  a published field other than the four listed in CONTRACT_AND_ROLLBACK.md section 2 changed -- checked here as: no published row carries ``meta_team_minutes_version`` /
      ``*_legacy`` fields while the template is published, every shadow row says the template is published, the registry on disk still publishes the template with no approval, and the
      published ``meta_expected_*`` of every contract-linked player equals the shadow's published-template arm.
The soak is complete at 100 settled games (games with at least one paired skater outcome). Before that, T1/T2 are reported as interim. ``activation_evidence_complete`` is true only when the
soak is complete and no trigger fails. Nothing here activates anything or writes to the archive.

    python -m nhl_edge.research.team_minutes_soak --archive <archive> --since 2026-10-28T00:11:43Z --out out/soak.json [--md out/soak.md]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.research import player_diagnosis as PD
from nhl_edge.research import team_minutes_shadow as S
from nhl_edge.timeutil import parse_iso

SOAK_GAMES = 100
MAX_FALLBACK_SHARE = 0.02
MAX_ERROR_RUN_FRACTION = 0.10          # "more than one run in ten"
LEGACY = "team-minutes-0"


def manifest_entries(archive: Path, kinds: tuple[str, ...], since: str) -> list[dict[str, Any]]:
    man = Path(archive) / "manifest.jsonl"
    out = []
    if not man.exists():
        return out
    for line in man.read_text().splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("kind") in kinds and (e.get("observed_at_utc") or "") >= since:
            out.append(e)
    return out


def run_health(archive: Path, since: str) -> dict[str, Any]:
    sim = manifest_entries(archive, ("predictions_player",), since)
    tm = manifest_entries(archive, ("player_tm_shadow",), since)
    err_runs = [e for e in tm if (e.get("meta") or {}).get("n_errors") or (e.get("meta") or {}).get("candidate_available") is False or (e.get("meta") or {}).get("default_reason")]
    runs = max(len(sim), len(tm))
    return {"runs_with_player_shadow": len(sim), "runs_with_tm_shadow_records": len(tm), "runs_with_error_or_marker": len(err_runs),
            "error_run_fraction": float(len(err_runs) / runs) if runs else None, "published_allocations_in_manifest": sorted({str((e.get("meta") or {}).get("published_allocation")) for e in tm}),
            "first_tm_record_utc": min((e["observed_at_utc"] for e in tm), default=None), "last_tm_record_utc": max((e["observed_at_utc"] for e in tm), default=None)}


def published_integrity(archive: Path, since: str, shadow: pd.DataFrame, registry_path: Path | None = None) -> dict[str, Any]:
    """T4: nothing but the shadow differs from the template at the published surface."""
    from nhl_edge import projection_registry as PR
    from nhl_edge.archive.ledger import Ledger

    n = n_pinned = n_mismatch = n_compared = 0
    by_key = {}
    if len(shadow):
        for r in shadow.itertuples(index=False):
            by_key[(str(r.game_id), int(r.player_id), str(r.predicted_at_utc))] = r
    for r in Ledger(archive).iter_rows("predictions_player", dt_from=since[:10]):
        if (r.get("_observed_at_utc") or "") < since:
            continue
        n += 1
        if any(k.startswith("meta_team_minutes") or k.endswith("_legacy") for k in r):
            n_pinned += 1
        s = by_key.get((str(r.get("game_id")), int(r["player_id"]) if r.get("player_id") is not None else -1, str(r.get("predicted_at_utc"))))
        if s is not None and r.get("meta_expected_toi_min") is not None:
            n_compared += 1
            if (round(s.legacy_toi, 2), round(s.legacy_pp, 2), round(s.legacy_sog, 2)) != (r["meta_expected_toi_min"], r["meta_expected_pp_toi_min"], r["meta_expected_shots"]):
                n_mismatch += 1
    model, why = PR.published_team_minutes(registry_path)
    entry = PR.team_minutes_entry(registry_path) or {}
    alloc = set(shadow["published_allocation"].astype(str)) if len(shadow) and "published_allocation" in shadow.columns else set()
    problems = []
    if n_pinned:
        problems.append(f"{n_pinned} published rows carry allocation/legacy fields while the template is published")
    if n_mismatch:
        problems.append(f"{n_mismatch} of {n_compared} compared published rows differ from the shadow's template arm")
    if alloc - {LEGACY}:
        problems.append(f"shadow rows report published allocation {sorted(alloc - {LEGACY})}")
    if model != LEGACY or entry.get("approval") is not None:
        problems.append(f"registry publishes {model!r} / approval {entry.get('approval')!r}")
    return {"published_rows_since": n, "rows_with_allocation_or_legacy_fields": n_pinned, "published_vs_shadow_template_arm": {"compared": n_compared, "mismatches": n_mismatch},
            "registry_published": model, "registry_approval_present": entry.get("approval") is not None, "shadow_published_allocations": sorted(alloc), "problems": problems}


def evaluate(archive: Path, since: str, n_boot: int = PD.N_BOOT, registry_path: Path | None = None) -> dict[str, Any]:
    rows = S.load_rows(archive, [])
    if len(rows):
        rows = rows[rows["predicted_at_utc"].map(lambda t: str(t) >= since)]
    actuals = S.load_actuals(archive)
    health = run_health(archive, since)
    res: dict[str, Any] = {"since": since, "soak_target_games": SOAK_GAMES, "n_shadow_rows": int(len(rows)), "run_health": health}
    cmp = S.compare(rows, actuals, n_boot) if len(rows) else {"n_games": 0, "n_paired_with_outcome": 0, "note": "no shadow rows yet"}
    res["comparison"] = cmp
    n_games = int(cmp.get("n_games", 0))
    r = cmp.get("results")
    trig: dict[str, Any] = {}
    final = n_games >= SOAK_GAMES
    if r:
        v = r["cand_minus_legacy"]
        t1 = {"mse_toi_upper95": v["mse_toi"]["hi95"], "mse_pp_upper95": v["mse_pp"]["hi95"]}
        trig["T1_mse_upper_bound_above_zero"] = {**t1, "fails": bool(t1["mse_toi_upper95"] > 0 or t1["mse_pp_upper95"] > 0), "final": final}
        t2 = {"bias_toi": {"published": r["legacy"]["bias"]["toi"], "candidate": r["cand"]["bias"]["toi"]}, "bias_pp": {"published": r["legacy"]["bias"]["pp"], "candidate": r["cand"]["bias"]["pp"]}}
        trig["T2_candidate_bias_larger_in_magnitude"] = {**t2, "fails": bool(abs(t2["bias_toi"]["candidate"]) > abs(t2["bias_toi"]["published"]) or abs(t2["bias_pp"]["candidate"]) > abs(t2["bias_pp"]["published"])), "final": final}
    else:
        trig["T1_mse_upper_bound_above_zero"] = {"fails": None, "final": False, "note": "not estimable yet (fewer than 30 paired player-games)"}
        trig["T2_candidate_bias_larger_in_magnitude"] = {"fails": None, "final": False, "note": "not estimable yet"}
    fb = float(rows["clock_fallback"].astype(bool).mean()) if len(rows) and "clock_fallback" in rows.columns else None           # over ALL shadow rows since the merge, paired with an outcome or not
    trig["T3a_clock_fallback_share_above_2pct"] = {"share": fb, "n_rows": int(len(rows)), "threshold": MAX_FALLBACK_SHARE, "fails": None if fb is None else bool(fb > MAX_FALLBACK_SHARE)}
    ef = health["error_run_fraction"]
    trig["T3b_error_runs_above_one_in_ten"] = {"error_run_fraction": ef, "threshold": MAX_ERROR_RUN_FRACTION, "fails": None if ef is None else bool(ef > MAX_ERROR_RUN_FRACTION)}
    integ = published_integrity(archive, since, rows, registry_path)
    trig["T4_published_surface_changed"] = {**integ, "fails": bool(integ["problems"])}
    res["triggers"] = trig
    res["settled_games"] = n_games
    res["soak_complete"] = final
    failed = [k for k, t in trig.items() if t.get("fails") is True]
    undetermined = [k for k, t in trig.items() if t.get("fails") is None]
    res["triggers_failed"] = failed
    res["triggers_undetermined"] = undetermined
    res["activation_evidence_complete"] = bool(final and not failed and not undetermined)
    return res


def markdown(res: dict[str, Any]) -> str:
    c, t, h = res["comparison"], res["triggers"], res["run_health"]
    L = [f"# Team-minute soak ({res['since']} -> now)", "", f"settled games with paired outcomes: **{res['settled_games']} / {res['soak_target_games']}** · shadow rows: {res['n_shadow_rows']} · paired skater-games: {c.get('n_paired_with_outcome', 0)}",
         f"runs with player shadow: {h['runs_with_player_shadow']} · runs with shadow records: {h['runs_with_tm_shadow_records']} · runs with error/marker: {h['runs_with_error_or_marker']}", ""]
    r = c.get("results")
    if r:
        d = r["cand_minus_legacy"]
        f = lambda k: f"{d[k]['delta']:+.3f} [{d[k]['lo95']:+.3f}, {d[k]['hi95']:+.3f}]"  # noqa: E731
        L += ["| | published (`team-minutes-0`) | candidate (`team-minutes-1.0`) | candidate - published (95%) |", "|---|---:|---:|---:|",
              f"| total TOI bias | {r['legacy']['bias']['toi']:+.3f} | {r['cand']['bias']['toi']:+.3f} | |", f"| total TOI MSE | {r['legacy']['mse']['toi']:.3f} | {r['cand']['mse']['toi']:.3f} | {f('mse_toi')} |",
              f"| PP TOI bias | {r['legacy']['bias']['pp']:+.3f} | {r['cand']['bias']['pp']:+.3f} | |", f"| PP TOI MSE | {r['legacy']['mse']['pp']:.3f} | {r['cand']['mse']['pp']:.3f} | {f('mse_pp')} |",
              f"| SH TOI MSE | {r['legacy']['mse']['sh']:.3f} | {r['cand']['mse']['sh']:.3f} | {f('mse_sh')} |",
              f"| shots deviance | {r['legacy']['sog_poisson_deviance']:.4f} | {r['cand']['sog_poisson_deviance']:.4f} | {d['sog_poisson_deviance']['delta']:+.4f} [{d['sog_poisson_deviance']['lo95']:+.4f}, {d['sog_poisson_deviance']['hi95']:+.4f}] |", ""]
    L += ["| trigger | status | detail |", "|---|---|---|"]
    for k, v in t.items():
        st = "n/a yet" if v.get("fails") is None else ("**FAIL**" if v["fails"] else "ok") + ("" if v.get("final", True) else " (interim)")
        detail = {kk: vv for kk, vv in v.items() if kk not in ("fails", "final", "problems") and not isinstance(vv, dict)}
        L.append(f"| {k} | {st} | {json.dumps(detail, default=str)[:160]}{'; problems: ' + '; '.join(v['problems']) if v.get('problems') else ''} |")
    L += ["", f"soak complete: {res['soak_complete']} · triggers failed: {res['triggers_failed'] or 'none'} · undetermined: {res['triggers_undetermined'] or 'none'} · **activation evidence complete: {res['activation_evidence_complete']}**"]
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--since", required=True, help="UTC instant of the shadow merge; earlier rows are not part of the soak")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--md", type=Path, default=None)
    ap.add_argument("--n-boot", type=int, default=PD.N_BOOT)
    a = ap.parse_args(argv)
    parse_iso(a.since)
    res = evaluate(a.archive, a.since, a.n_boot)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=1, sort_keys=True, default=str))
    md = markdown(res)
    if a.md:
        a.md.write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
