#!/usr/bin/env python3
"""Check that rustbook-az/listings differ from rustbook-en/listings only in comment text.

Comment text (`//`, `///`, `//!`, `/* */`) may change. Everything else, including
`// ANCHOR:` / `// ANCHOR_END:` lines, string literals and all non-.rs files,
must stay byte-identical.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AZ_DIR = ROOT / "rustbook-az" / "listings"
EN_DIR = ROOT / "rustbook-en" / "listings"
SKIP_DIRS = {"target", ".git"}


def _is_ident_char(c: str) -> bool:
    return c.isalnum() or c == "_"


def strip_comments(source: str) -> str:
    """Remove comment text, keeping code, literals and ANCHOR lines.

    Trailing whitespace is removed and lines that end up empty are dropped, so a
    translated comment may wrap differently from the original.
    """
    out: list[str] = []
    i, n = 0, len(source)
    while i < n:
        c = source[i]
        two = source[i : i + 2]

        if two == "//":
            end = source.find("\n", i)
            end = n if end == -1 else end
            line_start = source.rfind("\n", 0, i) + 1
            before = source[line_start:i]
            if not before.strip() and source[i:end].lstrip("/ ").startswith("ANCHOR"):
                out.append(source[i:end])
            i = end
        elif two == "/*":
            depth, i = 1, i + 2
            while i < n and depth:
                if source[i : i + 2] == "/*":
                    depth, i = depth + 1, i + 2
                elif source[i : i + 2] == "*/":
                    depth, i = depth - 1, i + 2
                else:
                    i += 1
            out.append(" ")
        elif c in "rb" and (i == 0 or not _is_ident_char(source[i - 1])) and _raw_string_end(source, i) is not None:
            end = _raw_string_end(source, i)
            out.append(source[i:end])
            i = end
        elif c == '"' or (c == "b" and source[i + 1 : i + 2] == '"' and (i == 0 or not _is_ident_char(source[i - 1]))):
            start = i
            i += 2 if c == "b" else 1
            while i < n and source[i] != '"':
                i += 2 if source[i] == "\\" else 1
            i += 1
            out.append(source[start:i])
        elif c == "'":
            end = _char_literal_end(source, i)
            if end is None:  # lifetime or label
                out.append(c)
                i += 1
            else:
                out.append(source[i:end])
                i = end
        else:
            out.append(c)
            i += 1

    lines = (line.rstrip() for line in "".join(out).split("\n"))
    return "\n".join(line for line in lines if line)


def _raw_string_end(s: str, i: int) -> int | None:
    j = i + 1 if s[i] == "r" else i + 2 if s[i : i + 2] == "br" else -1
    if j == -1:
        return None
    hashes = 0
    while j < len(s) and s[j] == "#":
        hashes, j = hashes + 1, j + 1
    if j >= len(s) or s[j] != '"':
        return None
    close = '"' + "#" * hashes
    end = s.find(close, j + 1)
    return len(s) if end == -1 else end + len(close)


def _char_literal_end(s: str, i: int) -> int | None:
    """Return the index after a char literal starting at s[i] == "'", else None."""
    if s[i + 1 : i + 2] == "\\":
        end = s.find("'", i + 3)
        return None if end == -1 else end + 1
    if s[i + 2 : i + 3] == "'" and s[i + 1 : i + 2] not in ("", "'"):
        return i + 3
    return None


def check_pair(az: Path, en: Path) -> list[str]:
    """Return a list of problems (empty if az is an allowed translation of en)."""
    if not en.exists():
        return [f"{az}: no English original at {en}"]
    if az.suffix != ".rs":
        return [] if az.read_bytes() == en.read_bytes() else [f"{az}: differs from English (must be byte-identical)"]
    a, e = strip_comments(az.read_text(encoding="utf-8")), strip_comments(en.read_text(encoding="utf-8"))
    if a == e:
        return []
    al, el = a.split("\n"), e.split("\n")
    for k in range(max(len(al), len(el))):
        if (al[k] if k < len(al) else None) != (el[k] if k < len(el) else None):
            return [f"{az}: non-comment difference near stripped line {k + 1}: az={al[k] if k < len(al) else '<missing>'!r} en={el[k] if k < len(el) else '<missing>'!r}"]
    return [f"{az}: differs from English"]


def main(argv: list[str]) -> int:
    if argv:
        files = [Path(a).resolve() for a in argv]
    else:
        files = [p for p in AZ_DIR.rglob("*") if p.is_file() and not (set(p.relative_to(AZ_DIR).parts) & SKIP_DIRS)]
    problems: list[str] = []
    for az in sorted(files):
        rel = az.relative_to(AZ_DIR)
        for msg in check_pair(az, EN_DIR / rel):
            problems.append(msg)
    # files present in English but missing in az
    if not argv:
        for en in EN_DIR.rglob("*"):
            if en.is_file() and not (set(en.relative_to(EN_DIR).parts) & SKIP_DIRS):
                if not (AZ_DIR / en.relative_to(EN_DIR)).exists():
                    problems.append(f"{AZ_DIR / en.relative_to(EN_DIR)}: missing (exists in English)")
    for p in problems:
        print(p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
