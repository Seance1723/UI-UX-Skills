#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

src = Path(__file__).resolve().parents[1]
out = src.parent / "ui-ux-master-deployment.zip"
if out.exists():
    out.unlink()
exclude_dirs = {".git", "graphify-out", "__pycache__"}
exclude_suffixes = {".pyc"}

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for path in src.rglob("*"):
        rel = path.relative_to(src)
        if set(rel.parts) & exclude_dirs:
            continue
        if path.suffix in exclude_suffixes:
            continue
        if path.is_file():
            z.write(path, Path("ui-ux-master") / rel)

print(out)
with tempfile.TemporaryDirectory() as td:
    with zipfile.ZipFile(out) as z:
        z.extractall(td)
    pkg = Path(td) / "ui-ux-master"
    res = subprocess.run(
        [sys.executable, "scripts/validate_skill.py", "--release"],
        cwd=pkg,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    print(res.stdout)
    raise SystemExit(res.returncode)
