#!/usr/bin/env python3
"""Glossary loading, linting of translated chapters, and the generated glossary appendix.

    python tools/glossary.py lint rustbook-az/src/ch01-*.md
    python tools/glossary.py appendix > rustbook-az/src/appendix-08-glossary.md
    python tools/glossary.py check          # sanity-check GLOSSARY.md itself

Known limits: case folding treats `I` as `i` (English-friendly), so an Azerbaijani word that
starts with a capital dotless `I` is not recognised; inflection is matched by stem prefix only
(final k->y / q->ğ softening), so vowel-dropping stems (oğul -> oğlu) need a manual look.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_chapter import DIRECTIVE_RE, split_fences  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
GLOSSARY_PATH = ROOT / "GLOSSARY.md"
KEEP = "—saxlanılır—"
APPROVED = "təsdiqlənib"
AZ_ALPHABET = "abcçdeəfgğhxıijkqlmnoöprsştuüvyz"


def fold(s: str) -> str:
    """Lower-case without changing the string length (so offsets stay valid)."""
    s = s.replace("İ", "i")
    return "".join(c.lower() if len(c.lower()) == 1 else c for c in s)


@dataclass
class Term:
    en: str
    az: str
    note: str = ""
    approved: bool = False
    keep_english: bool = False
    gloss: str = ""  # for kept-English terms: Azerbaijani word given in parentheses on first use
    stems: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.keep_english:
            self.az = self.en
        base = fold(self.az)
        self.stems = [base]
        if base.endswith("k"):
            self.stems.append(base[:-1] + "y")
        elif base.endswith("q"):
            self.stems.append(base[:-1] + "ğ")


@dataclass
class Issue:
    line: int
    kind: str
    message: str

    def __str__(self) -> str:
        return f"{self.line}: [{self.kind}] {self.message}"


def _cells(line: str) -> list[str]:
    inner = line.strip().strip("|")
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", inner)]


def parse_glossary(text: str) -> list[Term]:
    terms: list[Term] = []
    for line in text.split("\n"):
        if not line.lstrip().startswith("|"):
            continue
        cells = _cells(line)
        if len(cells) < 4 or set("".join(cells)) <= set("-: ") or cells[0].lower() == "english":
            continue
        en, az, note, status = cells[:4]
        keep = az.startswith(KEEP)
        gloss = re.sub(r"^" + re.escape(KEEP) + r"\s*\(?|\)\s*$", "", az).strip() if keep else ""
        terms.append(Term(en=en, az=az, note=note, approved=status == APPROVED, keep_english=keep, gloss=gloss))
    return terms


def load_glossary(path: Path = GLOSSARY_PATH) -> list[Term]:
    return parse_glossary(Path(path).read_text(encoding="utf-8"))


# ---------------------------------------------------------------- masking

def _blank(m: re.Match[str]) -> str:
    return re.sub(r"[^\n]", " ", m.group(0))


def mask_protected(md: str, en_terms: set[str]) -> str:
    """Return `md` with code, directives, link targets, tags, URLs and `(English term)` blanked.

    Offsets and line numbers are preserved.
    """
    out: list[str] = []
    for is_fence, _info, text in split_fences(md):
        if is_fence:
            out.append(re.sub(r"[^\n]", " ", text))
            continue
        text = re.sub(r"<!--.*?-->", _blank, text, flags=re.S)
        text = re.sub(r"`+[^`]+`+", _blank, text)
        text = DIRECTIVE_RE.sub(_blank, text)
        text = re.sub(r"\]\([^)]*\)", lambda m: "]" + " " * (len(m.group(0)) - 1), text)
        text = re.sub(r"^([ \t>]*\[[^\]]+\]:).*$", lambda m: m.group(1) + " " * (len(m.group(0)) - len(m.group(1))), text, flags=re.M)
        text = re.sub(r"https?://\S+", _blank, text)
        text = re.sub(r'(?:number|file-name)="[^"]*"', _blank, text)
        text = re.sub(r"<[^>\n]+>", _blank, text)
        text = re.sub(r"\(([^()\n]+)\)", lambda m: _blank(m) if _is_en_term(m.group(1), en_terms) else m.group(0), text)
        out.append(text)
    return "\n".join(out)


def _is_en_term(s: str, en_terms: set[str]) -> bool:
    s = fold(s.strip())
    return any(s == t or s in _plurals(t) for t in en_terms)


def _plurals(t: str) -> set[str]:
    return {t + "s", t + "es"} | ({t[:-1] + "ies"} if t.endswith("y") else set())


# ---------------------------------------------------------------- lint

def _en_regex(en: str) -> re.Pattern[str]:
    f = fold(en)
    alts = [re.escape(f)] + [re.escape(p) for p in sorted(_plurals(f))]
    return re.compile(r"(?<!\w)(?:" + "|".join(alts) + r")(?!\w)")


def _line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def lint(md: str, terms: list[Term], seen: set[str] | None = None) -> list[Issue]:
    """Lint one file. `seen` holds English terms already introduced earlier in the same
    chapter (updated in place), so the first-use rule is per chapter, not per file."""
    seen = set() if seen is None else seen
    issues: list[Issue] = []
    en_terms = {fold(t.en) for t in terms}
    masked = mask_protected(md, en_terms)
    folded = fold(masked)
    original = fold(md)
    heading_blank = re.sub(
        r"^[ >]*#{1,6} .*$", lambda m: " " * len(m.group(0)), folded, flags=re.M
    )

    for t in terms:
        if t.keep_english:
            # (b) suffix glued on without a hyphen
            pat = re.compile(r"(?<!\w)" + re.escape(fold(t.en)) + r"([^\W\d_]+)(?!\w)(?!\.\w)")
            for m in pat.finditer(folded):
                issues.append(Issue(_line_of(md, m.start()), "suffiks",
                                    f"`{md[m.start():m.end()]}`: ingilis terminə şəkilçi defislə yazılır "
                                    f"(`{t.en}-{m.group(1)}`)"))
            # (c') kept term with a gloss: first use gets the Azerbaijani word in parentheses
            key = fold(t.en)
            if t.gloss and key not in seen:
                first = re.search(r"(?<!\w)" + re.escape(key) + r"(?:-[^\W\d_]+)?(?!\w)", heading_blank)
                if first:
                    seen.add(key)
                    if not re.match(r"\s*\(\s*" + re.escape(fold(t.gloss)) + r"[^)\n]*\)", original[first.end():]):
                        issues.append(Issue(_line_of(md, first.start()), "ilk-istifadə",
                                            f"`{md[first.start():first.end()]}` bu fəsildə ilk dəfə işlənir: "
                                            f"ardınca `({t.gloss})` yazılmalıdır"))
            continue
        if fold(t.az) == fold(t.en):
            continue  # same spelling in both languages (iterator, variant, test): nothing to check
        # (a) English term left in prose
        for m in _en_regex(t.en).finditer(folded):
            issues.append(Issue(_line_of(md, m.start()), "ingilis",
                                f"`{md[m.start():m.end()]}` tərcümə olunmalıdır: `{t.az}`"))
        # (c) first use of the Azerbaijani term needs the English in parentheses
        key = fold(t.en)
        if key in seen:
            continue
        stem_re = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(s) for s in t.stems) + r")[^\W\d_]*")
        m = stem_re.search(heading_blank)
        if not m:
            continue
        seen.add(key)
        after = original[m.end():]
        if not re.match(r"\s*\(\s*" + re.escape(key) + r"[^)\n]*\)", after):
            issues.append(Issue(_line_of(md, m.start()), "ilk-istifadə",
                                f"`{md[m.start():m.end()]}` bu fəsildə ilk dəfə işlənir: "
                                f"ardınca `({t.en})` yazılmalıdır"))
    return sorted(issues, key=lambda i: (i.line, i.kind))


def chapter_key(path: Path) -> str:
    m = re.match(r"(ch\d+)-", path.name)
    return m.group(1) if m else path.name


def lint_files(paths: list[Path], terms: list[Term]) -> list[tuple[Path, Issue]]:
    seen_by_chapter: dict[str, set[str]] = defaultdict(set)
    found: list[tuple[Path, Issue]] = []
    for p in sorted(paths):
        for issue in lint(p.read_text(encoding="utf-8"), terms, seen_by_chapter[chapter_key(p)]):
            found.append((p, issue))
    return found


# ---------------------------------------------------------------- glossary sanity + appendix

def check_glossary(terms: list[Term]) -> list[str]:
    problems = []
    by_az: dict[str, list[str]] = defaultdict(list)
    seen_en: dict[str, int] = defaultdict(int)
    for t in terms:
        by_az[fold(t.az)].append(t.en)
        seen_en[fold(t.en)] += 1
    for az, ens in by_az.items():
        if len(ens) > 1:
            problems.append(f"eyni Azərbaycanca qarşılıq bir neçə terminə verilib ({az}): {', '.join(ens)}")
    problems += [f"təkrarlanan ingilis termini: {en}" for en, n in seen_en.items() if n > 1]
    return problems


def az_sort_key(s: str) -> list[int]:
    return [AZ_ALPHABET.find(c) if c in AZ_ALPHABET else 100 + ord(c) for c in fold(s)]


def appendix(terms: list[Term]) -> str:
    rows = sorted(terms, key=lambda t: az_sort_key(t.az))
    out = [
        "## Əlavə H - Terminlər lüğəti",
        "",
        "Bu əlavə kitabda işlənən texniki terminlərin Azərbaycanca və ingiliscə qarşılıqlarını "
        "göstərir. Cədvəl `GLOSSARY.md` faylından avtomatik yaradılır. Qarşılığı tərcümə "
        "olunmayan terminlər ingiliscə qalır və Azərbaycan dili şəkilçiləri defislə yazılır "
        "(məsələn, *trait-in*, *crate-ə*).",
        "",
        "| Azərbaycanca | English |",
        "| ------------ | ------- |",
    ]
    for t in rows:
        az = (f"{t.en} ({t.gloss})" if t.gloss else t.az) + (" *(ingiliscə qalır)*" if t.keep_english else "")
        out.append(f"| {az} | {t.en} |")
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in {"lint", "appendix", "check"}:
        print(__doc__)
        return 2
    terms = load_glossary()
    cmd, rest = argv[0], argv[1:]
    if cmd == "appendix":
        sys.stdout.write(appendix(terms))
        return 0
    if cmd == "check":
        problems = check_glossary(terms)
        print("\n".join(problems))
        return 1 if problems else 0
    paths = [Path(a) for a in rest]
    found = lint_files(paths, terms)
    for p, issue in found:
        print(f"{p}:{issue}")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
