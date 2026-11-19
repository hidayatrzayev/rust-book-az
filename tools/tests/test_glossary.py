from glossary import Term, appendix, check_glossary, lint, lint_files, parse_glossary

TERMS = [
    Term("ownership", "sahiblik"),
    Term("trait", "", keep_english=True),
    Term("crate", "", keep_english=True),
    Term("stack", "stek"),
    Term("heap", "heap", keep_english=True),
    Term("variable", "dəyişən"),
    Term("closure", "qapanma"),
]


def kinds(md, seen=None):
    return [i.kind for i in lint(md, TERMS, seen)]


def test_untranslated_english_flagged():
    assert "ingilis" in kinds("Bax: the ownership rules burada.")


def test_english_in_parentheses_ok():
    assert kinds("Bu sahiblik (ownership) qaydalarıdır.") == []


def test_english_in_code_ok():
    assert kinds("Burada `ownership` və\n\n```rust\nlet ownership = 1;\n```\n") == []


def test_inflected_az_recognised():
    # inflected form counts as a use of the term -> first use needs the parenthesis
    assert kinds("Bu sahibliyin qaydalarıdır.") == ["ilk-istifadə"]
    # once introduced, later inflected uses need nothing
    assert kinds("Bu sahiblik (ownership) haqqındadır. Sahibliyin qaydaları. Sahibliyi köçürək.") == []


def test_kept_term_needs_hyphen():
    assert kinds("Bu traitin metodudur.") == ["suffiks"]
    assert kinds("Bu trait-in metodudur.") == []
    assert kinds("Bu crateə aiddir.") == ["suffiks"]
    assert kinds("Bu crate-ə aiddir.") == []


def test_crates_io_not_flagged():
    assert kinds("Bax: [crates.io](https://crates.io/) saytı və crates.io.") == []


def test_first_use_needs_parentheses():
    assert kinds("Stek sürətlidir.") == ["ilk-istifadə"]
    assert kinds("Stek (stack) sürətlidir. Stek yenə.") == []


def test_first_use_not_triggered_by_heading_only():
    assert kinds("## Stek\n\nMətn.") == []
    assert kinds("## Stek\n\nStek (stack) mətni.") == []
    assert kinds("## Stek\n\nStek mətni.") == ["ilk-istifadə"]


def test_seen_carries_over_within_chapter():
    seen: set[str] = set()
    assert kinds("Stek (stack) mətni.", seen) == []
    assert kinds("Stek yenə.", seen) == []


def test_lint_files_groups_by_chapter(tmp_path):
    a, b, c = tmp_path / "ch01-01-a.md", tmp_path / "ch01-02-b.md", tmp_path / "ch02-00-c.md"
    a.write_text("Stek (stack) mətni.")
    b.write_text("Stek yenə.")
    c.write_text("Stek yenə.")
    found = lint_files([a, b, c], TERMS)
    assert [(p.name, i.kind) for p, i in found] == [("ch02-00-c.md", "ilk-istifadə")]


def test_line_numbers_preserved():
    md = "Salam.\n\n```rust\ncode\n```\n\nthe ownership"
    assert [i.line for i in lint(md, TERMS)] == [7]


def test_appendix_sorted_by_az():
    terms = [Term("zebra", "zeytun"), Term("closure", "qapanma"), Term("thing", "çay"), Term("stack", "stek")]
    out = appendix(terms)
    order = [out.index(x) for x in ("çay", "qapanma", "stek", "zeytun")]
    assert order == sorted(order)


def test_parse_glossary_and_keep_english():
    md = """| English | Azərbaycanca | Qeyd | Status |
| --- | --- | --- | --- |
| ownership | sahiblik | nümunə | təsdiqlənib |
| trait | —saxlanılır— | | təklif |
"""
    t = parse_glossary(md)
    assert [(x.en, x.az, x.keep_english, x.approved) for x in t] == [
        ("ownership", "sahiblik", False, True),
        ("trait", "trait", True, False),
    ]


def test_check_flags_collapsed_concepts():
    problems = check_glossary([Term("stack", "yığın"), Term("heap", "yığın")])
    assert problems and "yığın" in problems[0]


def test_same_spelling_term_not_flagged():
    assert [i.kind for i in lint("Bu iterator işləyir.", [Term("iterator", "iterator")])] == []
