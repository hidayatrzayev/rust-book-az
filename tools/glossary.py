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
EVERYDAY = "[gündəlik]"  # note tag: everyday word, no English in parentheses on first use
# Files whose prose is not technical: no first-use parentheses at all (decided by the human).
FIRST_USE_EXEMPT = {"foreword.md", "title-page.md"}
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
    everyday: bool = False
    inline: bool = False  # English given inside the term: "daxili (embedded) qurğu"

    def __post_init__(self) -> None:
        self.everyday = self.everyday or EVERYDAY in self.note
        if self.keep_english:
            self.az = self.en
        self.inline = bool(re.search(r"\([^)]*\)\s+\S", self.az))
        base = fold(re.sub(r"\s*\([^)]*\)(?=\s+\S)", "", self.az))
        # Verbs: match the root so inflected forms count (quraşdırın, kompilyasiya edin).
        for light in (" etmək", " vermək", " olmaq"):
            if base.endswith(light) and " " not in base[: -len(light)]:
                base = base[: -len(light)]
                break
        else:
            if " " not in base and len(base) > 6 and base.endswith(("mək", "maq")):
                base = base[:-3]
                self.stems = [base]
                return
        self.stems = [base]
        # Multi-word terms inflect on the last word: xəta mesajı → xəta mesajları.
        m = re.match(r"^(.+ \w+?)s?[ıiuü]$", base)
        if m and len(m.group(1).split()[-1]) >= 3:
            self.stems.append(m.group(1))
        # Vowel drop before a vowel suffix: sətir → sətri, fikir → fikri.
        m = re.match(r"^(\w{2,})[ıiuü]([^\Waeıioöuüə\d_])$", base)
        if m and " " not in base:
            self.stems.append(m.group(1) + m.group(2))
        # k/q soften before a vowel suffix: asılılıq → asılılığı (but not baq → bağlı)
        soft = {"k": "y", "q": "ğ"}.get(base[-1:])
        if soft:
            self.stems += [base[:-1] + soft + v for v in "aıoueəiöü"]


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
        text = re.sub(r"^[ \t>]*\[[^\]]+\]:.*$", _blank, text, flags=re.M)  # reference definitions
        text = re.sub(r"\]\[[^\]]*\]", lambda m: "]" + " " * (len(m.group(0)) - 1), text)  # [text][label]
        text = re.sub(r"https?://\S+", _blank, text)
        text = re.sub(r"[\w.~-]*[/\\][\w./\\~-]*", _blank, text)  # file paths: target/release
        text = re.sub(r'(?:number|file-name)="[^"]*"', _blank, text)
        text = re.sub(r"<[^>\n]+>", _blank, text)
        text = re.sub(r"\(([^()]+)\)", lambda m: _blank(m) if _is_en_term(m.group(1), en_terms) else m.group(0), text)
        out.append(text)
    return "\n".join(out)


def _is_en_term(s: str, en_terms: set[str]) -> bool:
    s = " ".join(fold(re.sub(r"\n[ \t]*(?:>[ \t]*)*", " ", s)).split())
    return any(s == t or s in _plurals(t) for t in en_terms)


def _plurals(t: str) -> set[str]:
    return {t + "s", t + "es"} | ({t[:-1] + "ies"} if t.endswith("y") else set())


# ---------------------------------------------------------------- lint

def _en_regex(en: str) -> re.Pattern[str]:
    f = fold(en)
    alts = [_ws(f)] + [_ws(p) for p in sorted(_plurals(f))]
    return re.compile(r"(?<!\w)(?:" + "|".join(alts) + r")(?!\w)")


def _ws(literal: str) -> str:
    """Regex for `literal` where any space may also be a line break."""
    sep = r"\s+(?:>\s*)*(?:\([^)\n]*\)\s+(?:>\s*)*)?"  # a line break, or an inline (gloss)
    return sep.join(re.escape(w) for w in literal.split(" "))


def _line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def lint(md: str, terms: list[Term], seen: set[str] | None = None, first_use: bool = True) -> list[Issue]:
    """Lint one file. `seen` holds English terms already introduced earlier in the same
    chapter (updated in place), so the first-use rule is per chapter, not per file."""
    seen = set() if seen is None else seen
    issues: list[Issue] = []
    en_terms = {fold(t.en) for t in terms} | {fold(t.gloss) for t in terms if t.gloss}
    masked = mask_protected(md, en_terms)
    folded = fold(masked)
    original = fold(md)
    heading_blank = re.sub(
        r"^[ >]*#{1,6} .*$", lambda m: " " * len(m.group(0)), folded, flags=re.M
    )
    # quoted section titles (“Problemlərin aradan qaldırılması”) refer to headings: no first-use rule
    heading_blank = re.sub(r"“[^”]*”", _blank, heading_blank)

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
            if first_use and not t.everyday and t.gloss and key not in seen:
                longer = [m.span() for o in terms if o.keep_english and fold(o.en) != key and key in fold(o.en)
                          for m in re.finditer(r"(?<!\w)" + _ws(fold(o.en)) + r"(?!\w)", heading_blank)]
                first = next((m for m in re.finditer(r"(?<!\w)" + _ws(key) + r"(?:-[^\W\d_]+)?(?!\w)", heading_blank)
                              if not any(a <= m.start() and m.end() <= b for a, b in longer)), None)
                if first:
                    seen.add(key)
                    if not re.match(r"\s*\(\s*" + _ws(fold(t.gloss)) + r"[^)]*\)", original[first.end():]):
                        issues.append(Issue(_line_of(md, first.start()), "ilk-istifadə",
                                            f"`{md[first.start():first.end()]}` bu fəsildə ilk dəfə işlənir: "
                                            f"ardınca `({t.gloss})` yazılmalıdır"))
            continue
        if fold(t.az) == fold(t.en):
            continue  # same spelling in both languages (iterator, variant, test): nothing to check
        # (a) English term left in prose
        longer_kept = [m.span() for o in terms if o.keep_english and fold(t.en) in fold(o.en) and fold(o.en) != fold(t.en)
                       for m in re.finditer(r"(?<!\w)" + _ws(fold(o.en)) + r"(?!\w)", folded)]
        for m in _en_regex(t.en).finditer(folded):
            if any(a <= m.start() and m.end() <= b for a, b in longer_kept):
                continue  # part of a longer term kept in English (reference in "mutable reference")
            issues.append(Issue(_line_of(md, m.start()), "ingilis",
                                f"`{md[m.start():m.end()]}` tərcümə olunmalıdır: `{t.az}`"))
        # (c) first use of the Azerbaijani term needs the English in parentheses
        key = fold(t.en)
        if not first_use or t.everyday or key in seen:
            continue
        stem_re = re.compile(r"(?<!\w)(?:" + "|".join(_ws(s) for s in t.stems) + r")[^\W\d_]*")
        # a use inside a longer Azerbaijani term (xəta in "xəta mesajı") is that term's use
        longer_az = [m.span() for o in terms if not o.keep_english and o is not t
                     and len(fold(o.az)) > len(fold(t.az)) and any(st in fold(o.az) for st in t.stems)
                     for m in re.finditer(r"(?<!\w)(?:" + "|".join(_ws(st) for st in o.stems) + r")[^\W\d_]*",
                                          heading_blank)]
        m = next((m for m in stem_re.finditer(heading_blank)
                  if not any(a <= m.start() and m.end() <= b for a, b in longer_az)), None)
        if not m:
            continue
        seen.add(key)
        if t.inline:
            if "(" not in m.group(0):
                issues.append(Issue(_line_of(md, m.start()), "ilk-istifadə",
                                    f"`{md[m.start():m.end()]}` bu fəsildə ilk dəfə işlənir: `{t.az}` kimi yazılmalıdır"))
            continue
        after = original[m.end():]
        en_alts = "|".join(_ws(x) for x in [key, *sorted(_plurals(key))])
        light = r"(?:\s+(?:et|ver|ol|edil)[^\W\d_]*)?"
        if not re.match(r"(?:-[^\W\d_]+)?" + light + r"\s*\(\s*(?:" + en_alts + r")[^)]*\)", after):
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
        for issue in lint(p.read_text(encoding="utf-8"), terms, seen_by_chapter[chapter_key(p)],
                          first_use=p.name not in FIRST_USE_EXEMPT):
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
