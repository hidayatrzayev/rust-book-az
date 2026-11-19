#!/usr/bin/env python3
"""Translation progress per file, and which translated files are outdated vs the pinned English book.

    python tools/status.py                      # counts per status + outdated files
    python tools/status.py set <file> <status>  # status: başlanmayıb | qaralama | yoxlanılıb
    python tools/status.py init                 # add rows for new src/*.md files (keeps existing rows)
"""
from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_chapter import AZ_ONLY  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "rustbook-az" / "TRANSLATION_STATUS.md"
AZ_SRC = ROOT / "rustbook-az" / "src"
EN_REPO = ROOT / "rustbook-en"
NOT_STARTED, DRAFT, REVIEWED = "başlanmayıb", "qaralama", "yoxlanılıb"
STATUSES = (NOT_STARTED, DRAFT, REVIEWED)
HEADER = """# Tərcümə statusu

`başlanmayıb` – İngilis mətni olduğu kimi kopyalanıb; `qaralama` – Claude tərcümə edib, insan yoxlamayıb;
`yoxlanılıb` – ana dilli oxucu yoxlayıb. Cədvəl `python tools/status.py set <fayl> <status>` ilə yenilənir.
Üçüncü sütun tərcümə zamanı ingiliscə faylı sonuncu dəyişən commit-dir; fərqli olarsa `python tools/status.py`
faylı `KÖHNƏLİB` kimi göstərir.

| Fayl | Status | İngiliscə commit |
| ---- | ------ | ---------------- |
"""


@dataclass
class Row:
    file: str
    status: str
    commit: str


def latest_commit(en_repo: Path, name: str) -> str:
    """Latest commit touching `src/<name>` in the English repo ('' if unknown)."""
    r = subprocess.run(["git", "-C", str(en_repo), "log", "-1", "--format=%H", "--", f"src/{name}"],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def load_rows(path: Path) -> list[Row]:
    rows = []
    for line in Path(path).read_text(encoding="utf-8").split("\n"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[1] in STATUSES:
            rows.append(Row(*cells))
    return rows


def write_rows(path: Path, rows: list[Row]) -> None:
    body = "".join(f"| {r.file} | {r.status} | {r.commit} |\n" for r in rows)
    Path(path).write_text(HEADER + body, encoding="utf-8")


def init_rows(az_src: Path, en_repo: Path, existing: dict[str, Row]) -> list[Row]:
    rows = []
    for p in sorted(az_src.glob("*.md")):
        if p.name in AZ_ONLY:
            continue
        rows.append(existing.get(p.name) or Row(p.name, NOT_STARTED, latest_commit(en_repo, p.name)))
    return rows


def outdated(rows: list, en_repo: Path) -> list:
    return [r for r in rows if r.status != NOT_STARTED and r.commit != latest_commit(en_repo, r.file)]


def set_status(path: Path, name: str, status: str, en_repo: Path = EN_REPO) -> None:
    if status not in STATUSES:
        raise ValueError(f"status {' | '.join(STATUSES)} olmalıdır, `{status}` yox")
    rows = load_rows(path)
    for r in rows:
        if r.file == name:
            r.status, r.commit = status, latest_commit(en_repo, name)
            write_rows(path, rows)
            return
    raise ValueError(f"{path} faylında `{name}` sətri yoxdur (əvvəl `init` işlədin)")


def main(argv: list[str]) -> int:
    try:
        if argv[:1] == ["init"]:
            existing = {r.file: r for r in load_rows(STATUS_PATH)} if STATUS_PATH.exists() else {}
            write_rows(STATUS_PATH, init_rows(AZ_SRC, EN_REPO, existing))
            return 0
        if argv[:1] == ["set"] and len(argv) == 3:
            set_status(STATUS_PATH, argv[1], argv[2])
            return 0
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    if argv:
        print(__doc__)
        return 2
    rows = load_rows(STATUS_PATH)
    for s in STATUSES:
        print(f"{s}: {sum(r.status == s for r in rows)}")
    old = outdated(rows, EN_REPO)
    for r in old:
        print(f"KÖHNƏLİB: {r.file} (ingiliscə mətn tərcümədən sonra dəyişib)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
