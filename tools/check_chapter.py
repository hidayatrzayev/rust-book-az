#!/usr/bin/env python3
"""Check that a translated chapter keeps every protected item of its English original.

Protected items: fenced code blocks (comments inside `rust` fences may be translated),
inline code, `{{#...}}` directives, `<Listing>` tags (except the caption text),
link targets (the `#anchor` part is checked against the az headings instead),
`<!-- ignore -->` markers and `<a id>` anchors.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_listings import strip_comments  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
AZ_SRC = ROOT / "rustbook-az" / "src"
EN_SRC = ROOT / "rustbook-en" / "src"

FENCE_RE = re.compile(r"^(?P<prefix>[ \t>]*)(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
DIRECTIVE_RE = re.compile(r"\{\{#[^}]*\}\}")
LISTING_RE = re.compile(r"<Listing\b[^>]*>")
CAPTION_RE = re.compile(r'\s+caption="[^"]*"')
IGNORE_RE = re.compile(r"<!--\s*ignore\s*-->")
HTML_ANCHOR_RE = re.compile(r"<a\s+id=\"([^\"]+)\"\s*>")
INLINE_CODE_RE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)", re.S)
INLINE_LINK_RE = re.compile(r"\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
LINK_DEF_RE = re.compile(r"^[ \t>]*\[([^\]]+)\]:\s*(\S+)", re.M)
LINK_REF_RE = re.compile(r"\]\[([^\]]+)\]")
HEADING_RE = re.compile(r"^(?:[ ]{0,3}>[ ]?)*[ ]{0,3}(#{1,6})[ \t]+(.*?)[ \t]*#*[ \t]*$")


def split_fences(md: str) -> list[tuple[bool, str, str]]:
    """Split into (is_fence, info, text) chunks; prose chunks keep their newlines."""
    chunks: list[tuple[bool, str, str]] = []
    prose: list[str] = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if not m:
            prose.append(lines[i])
            i += 1
            continue
        if prose:
            chunks.append((False, "", "\n".join(prose)))
            prose = []
        fence, info = m.group("fence"), m.group("info").strip()
        j = i + 1
        while j < len(lines):
            c = FENCE_RE.match(lines[j])
            if c and c.group("fence")[0] == fence[0] and len(c.group("fence")) >= len(fence) and not c.group("info").strip():
                break
            j += 1
        end = min(j, len(lines) - 1)
        chunks.append((True, info, "\n".join(lines[i : end + 1])))
        i = end + 1
    if prose:
        chunks.append((False, "", "\n".join(prose)))
    return chunks


def _prose(md: str) -> str:
    return "\n".join(t for is_fence, _, t in split_fences(md) if not is_fence)


def extract_protected(md: str) -> list[tuple[str, str]]:
    """Ordered (kind, text) for every protected item in `md`."""
    items: list[tuple[str, str]] = []
    for is_fence, _info, text in split_fences(md):
        if is_fence:
            items.append(("fence", text))
            continue
        spots: list[tuple[int, str, str]] = []
        for m in DIRECTIVE_RE.finditer(text):
            spots.append((m.start(), "directive", m.group(0)))
        for m in LISTING_RE.finditer(text):
            spots.append((m.start(), "listing_tag", m.group(0)))
        for m in IGNORE_RE.finditer(text):
            spots.append((m.start(), "ignore_marker", m.group(0)))
        for m in HTML_ANCHOR_RE.finditer(text):
            spots.append((m.start(), "html_anchor", m.group(1)))
        for m in INLINE_CODE_RE.finditer(text):
            spots.append((m.start(), "inline_code", m.group(0)))
        for m in INLINE_LINK_RE.finditer(text):
            spots.append((m.start(), "link_target", m.group(1)))
        for m in LINK_DEF_RE.finditer(text):
            spots.append((m.start(), "link_label", m.group(1)))
            spots.append((m.start(), "link_target", m.group(2)))
        for m in LINK_REF_RE.finditer(text):
            spots.append((m.start(), "link_label", m.group(1)))
        items.extend((k, t) for _, k, t in sorted(spots, key=lambda s: s[0]))
    return items


def slugify(text: str) -> str:
    """mdBook 0.5 `id_from_content`."""
    return "".join(
        ch if (ch.isalnum() or ch in "_-") else "-" if ch.isspace() else ""
        for ch in text.strip().lower()
    )


def _heading_text(raw: str) -> str:
    raw = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", raw)  # links/images -> text
    raw = re.sub(r"\[([^\]]*)\]\[[^\]]*\]", r"\1", raw)
    parts = re.split(r"(`+[^`]*`+)", raw)
    out = []
    for part in parts:
        if part.startswith("`"):
            out.append(part.strip("`"))  # inline code -> its text, kept verbatim
        else:
            part = re.sub(r"(?<![\w])_+([^_]+?)_+(?![\w])", r"\1", part)  # _emphasis_
            part = re.sub(r"\*+([^*]+?)\*+", r"\1", part)
            out.append(re.sub(r"<[^>]+>", "", part))  # html tags
    return "".join(out)


def heading_anchors(md: str) -> set[str]:
    """All anchors a file defines: headings (mdBook slugs, deduplicated), `<a id>`, Listing ids."""
    anchors: set[str] = set()
    used: set[str] = set()
    prose = re.sub(r"<!--.*?-->", "", _prose(md), flags=re.S)  # headings in comments don't render
    for line in prose.split("\n"):
        m = HEADING_RE.match(line)
        if not m:
            continue
        base = slugify(_heading_text(m.group(2)))
        cand, k = base, 0
        while cand in used:
            k += 1
            cand = f"{base}-{k}"
        used.add(cand)
        anchors.add(cand)
    anchors.update(HTML_ANCHOR_RE.findall(prose))
    for tag in LISTING_RE.findall(prose):
        n = re.search(r'number="([^"]+)"', tag)
        if n:
            anchors.add(f"listing-{n.group(1)}")
    return anchors


def _normalise(kind: str, text: str) -> str:
    if kind == "listing_tag":
        return CAPTION_RE.sub("", text)
    if kind == "link_target":
        return text.split("#", 1)[0]  # anchors are validated against the az headings
    if kind == "fence":
        lines = text.split("\n")
        info = FENCE_RE.match(lines[0]).group("info").strip()
        if info.split(",")[0].strip() == "rust":
            body = "\n".join(lines[1:-1]) if len(lines) > 1 else ""
            closing = lines[-1] if len(lines) > 1 else ""
            return lines[0] + "\n" + strip_comments(body) + "\n" + closing
    return text


# Kinds whose relative order must not change vs. English.
ORDERED = {"fence", "directive", "listing_tag"}


def compare(az_md: str, en_md: str) -> list[str]:
    problems: list[str] = []
    az, en = extract_protected(az_md), extract_protected(en_md)
    for kind in sorted({k for k, _ in az} | {k for k, _ in en}):
        a = [_normalise(k, t) for k, t in az if k == kind]
        e = [_normalise(k, t) for k, t in en if k == kind]
        if kind in ORDERED:
            if a != e:
                problems += _ordered_diff(kind, a, e)
        else:
            ca, ce = Counter(a), Counter(e)
            for t in (ce - ca):
                problems.append(f"{kind}: missing or changed in az: {_short(t)}")
            for t in (ca - ce):
                problems.append(f"{kind}: not in English original: {_short(t)}")
    return problems


def _ordered_diff(kind: str, a: list[str], e: list[str]) -> list[str]:
    out = []
    if len(a) != len(e):
        out.append(f"{kind}: az has {len(a)} item(s), English has {len(e)}")
    for k, (x, y) in enumerate(zip(a, e), 1):
        if x != y:
            out.append(f"{kind} #{k} differs from English:\n    az: {_short(x)}\n    en: {_short(y)}")
    return out


def _short(t: str, n: int = 90) -> str:
    t = t.replace("\n", "⏎")
    return t if len(t) <= n else t[: n - 1] + "…"


def broken_anchors(az_md: str, src_dir: Path, this_file: str) -> list[str]:
    """Links `file.html#anchor` / `#anchor` whose anchor isn't defined in the az target."""
    out: list[str] = []
    cache: dict[str, set[str] | None] = {}

    def anchors_of(name: str) -> set[str] | None:
        if name not in cache:
            p = src_dir / name
            cache[name] = heading_anchors(p.read_text(encoding="utf-8")) if p.exists() else None
        return cache[name]

    cache[this_file] = heading_anchors(az_md)
    for kind, text in extract_protected(az_md):
        if kind != "link_target" or "#" not in text or re.match(r"^[a-z][a-z0-9+.-]*:|^//", text, re.I):
            continue
        path, anchor = text.split("#", 1)
        if not anchor:
            continue
        if path == "":
            target = this_file
        elif path.endswith(".html") and "/" not in path:
            target = path[:-5] + ".md"
        elif path.endswith(".md") and "/" not in path:
            target = path
        else:
            continue
        found = anchors_of(target)
        if found is not None and anchor not in found:
            out.append(f"broken anchor: {text} (no heading/anchor `{anchor}` in {target})")
    return out


def check_file(az: Path, en_dir: Path = EN_SRC, az_dir: Path | None = None) -> list[str]:
    en = en_dir / az.name
    if not en.exists():
        return [f"no English original at {en}"]
    az_md = az.read_text(encoding="utf-8")
    en_md = en.read_text(encoding="utf-8")
    problems = compare(az_md, en_md)
    # Anchors that are already broken upstream are not the translator's fault.
    inherited = {b.split(" (")[0] for b in broken_anchors(en_md, en_dir, az.name)}
    problems += [b for b in broken_anchors(az_md, az_dir or az.parent, az.name) if b.split(" (")[0] not in inherited]
    return problems


def main(argv: list[str]) -> int:
    files = [Path(a).resolve() for a in argv] or sorted(AZ_SRC.glob("*.md"))
    failed = False
    for az in files:
        problems = check_file(az)
        for p in problems:
            print(f"{az.name}: {p}")
        failed |= bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
