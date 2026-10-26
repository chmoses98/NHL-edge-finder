"""Replays one real production run instant through the CURRENT code against a copy of the archive (hard links) and dumps the player_tm_shadow / predictions_player rows written by that run.

    PYTHONPATH=src python scripts/team_minutes_replay.py 2026-10-25T18:18:12Z [n_sims]

Paths below are the scratch locations used for the team-minutes evidence (archive checkout at /tmp/claude-0/arch); edit SRC / DATA / OUT for another machine."""
# ruff: noqa: E701, E702, E401, E402
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

os.environ["NHL_EDGE_PLAYER_SHADOW"] = "1"; os.environ["NHL_EDGE_V2_SHADOW"] = "1"
from nhl_edge.archive.ledger import Ledger
from nhl_edge.workflows.simulate import run_simulate

SRC = Path("/tmp/claude-0/arch"); DATA = Path("/home/user/wt-pm/data"); OUT = Path("/tmp/claude-0/tm/replay")
inst = sys.argv[1]; n_sims = int(sys.argv[2]) if len(sys.argv) > 2 else 300
now = datetime.fromisoformat(inst.replace("Z", "+00:00"))
dst = OUT / inst.replace(":", "")
if dst.exists(): shutil.rmtree(dst)
dst.mkdir(parents=True)
for e in SRC.iterdir():
    if e.name == ".git": continue
    subprocess.run(["cp", "-al", str(e), str(dst / e.name)], check=True)
t0 = time.time()
rc = run_simulate(dst, DATA, date=None, n_sims=n_sims, now=now)
dt = time.time() - t0
led = Ledger(dst)
tm = [r for r in led.iter_rows("player_tm_shadow") if r.get("_observed_at_utc") == inst]
pp = [r for r in led.iter_rows("predictions_player") if r.get("_observed_at_utc") == inst]
(OUT / f"{inst.replace(':','')}.tm.json").write_text(json.dumps(tm)); (OUT / f"{inst.replace(':','')}.pp.json").write_text(json.dumps(pp))
print(json.dumps({"instant": inst, "rc": rc, "seconds": round(dt, 1), "tm_rows": len(tm), "published_rows": len(pp), "games": sorted({r['game_id'] for r in tm})}))
