"""Compare a regenerated walk-forward result with the committed one (Phase-1 reproducibility evidence).

    python -m nhl.live.repro_check COMMITTED_full_results.json NEW_full_results.json [COMMITTED_summary.json NEW_summary.json]

Per (family, model, split): exact matches and the largest absolute / relative difference of n_obs, mae, rmse, bias, crps,
log_score, cover_50/80/90, pit_var_ratio. Splits other than 'prospective' are fixed historical data; 'prospective' (2026-27
to date) grows every day and is reported separately. Exit status 0 always: the numbers are the deliverable.
"""
from __future__ import annotations

import json
import sys

FIELDS = ("n_obs", "mae", "rmse", "bias", "crps", "log_score", "cover_50", "cover_80", "cover_90", "pit_var_ratio")


def compare(a: dict, b: dict) -> dict:
    out: dict = {}
    for fam, ra in a["families"].items():
        rb = b["families"].get(fam)
        if rb is None:
            continue
        mb = {(m["model"], m["split"]): m for m in rb["models"]}
        for m in ra["models"]:
            o = mb.get((m["model"], m["split"]))
            if o is None:
                continue
            for k in FIELDS:
                x, y = m.get(k), o.get(k)
                if x is None or y is None:
                    continue
                d = abs(x - y)
                r = out.setdefault(m["split"], {"n": 0, "exact": 0, "max_abs": 0.0, "max_rel": 0.0, "worst": None})
                r["n"] += 1
                r["exact"] += int(d <= 5e-6 * max(1.0, abs(x)))      # results are stored rounded to 6 decimals
                rel = d / max(abs(x), 1e-12)
                if rel > r["max_rel"]:
                    r["max_rel"], r["max_abs"], r["worst"] = rel, d, f"{fam}/{m['model']}/{k}: {x} vs {y}"
        r = out.setdefault("best_model_agrees", {"same": 0, "total": 0, "diff": []})
        r["total"] += 1
        r["same"] += int(ra.get("best_model") == rb.get("best_model"))
        if ra.get("best_model") != rb.get("best_model"):
            r["diff"].append(f"{fam}: {ra.get('best_model')} vs {rb.get('best_model')}")
    # by model letter: A..D are deterministic ridge/shrinkage ladders, E is LightGBM, F stacks A..E
    by: dict = {}
    for fam, ra in a["families"].items():
        rb = b["families"].get(fam)
        if rb is None:
            continue
        mb = {(m["model"], m["split"]): m for m in rb["models"]}
        for m in ra["models"]:
            o = mb.get((m["model"], m["split"]))
            if o is None or m["split"] == "prospective":
                continue
            r = by.setdefault(m["model"][0], {"n": 0, "exact": 0, "max_abs_crps": 0.0, "max_abs_mae": 0.0})
            for k in ("mae", "rmse", "bias", "crps", "log_score", "cover_80"):
                if m.get(k) is not None and o.get(k) is not None:
                    r["n"] += 1
                    r["exact"] += int(abs(m[k] - o[k]) <= 5e-6 * max(1.0, abs(m[k])))
            r["max_abs_crps"] = max(r["max_abs_crps"], abs(m["crps"] - o["crps"]))
            r["max_abs_mae"] = max(r["max_abs_mae"], abs(m["mae"] - o["mae"]))
    out["by_model_excluding_prospective"] = by
    head = {}
    for fam, ra in a["families"].items():
        rb = b["families"].get(fam)
        pick = lambda r: next(m for m in r["models"] if m["split"] == "holdout" and m["model"] == ra["best_model"])  # noqa: E731
        ma, mb_ = pick(ra), pick(rb)
        head[fam] = {k: [ma[k], mb_[k]] for k in ("n_obs", "mae", "crps", "bias", "cover_80")}
    out["holdout_best_model_committed_vs_rerun"] = head
    return out


def main(argv=None) -> int:
    a = argv or sys.argv[1:]
    res = compare(json.load(open(a[0])), json.load(open(a[1])))
    print(json.dumps(res, indent=1))
    if len(a) >= 4:
        sa, sb = json.load(open(a[2])), json.load(open(a[3]))
        fa = {f["family"]: f for f in sa["families"]}
        fb = {f["family"]: f for f in sb["families"]}
        rows = {}
        for fam in fa:
            ha, hb = fa[fam].get("holdout") or {}, fb.get(fam, {}).get("holdout") or {}
            rows[fam] = {"best_model": [fa[fam]["best_model"], fb.get(fam, {}).get("best_model")],
                         "readiness": [fa[fam]["readiness"], fb.get(fam, {}).get("readiness")],
                         "holdout_identical": {k: ha.get(k) == hb.get(k) for k in ("n_obs", "mae", "crps", "bias", "cover_80")}}
        print(json.dumps({"summary_json_holdout": rows}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
