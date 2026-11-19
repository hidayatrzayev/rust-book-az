from check_chapter import broken_anchors, compare, heading_anchors

EN = """## What Is Ownership?

Ownership is about `String` values. See [the guide](ch04-02.html#what-is-ownership).

```rust
let x = 5; // five
```

```text
let x = 5; // five
```

{{#rustdoc_include ../listings/a/src/main.rs:here}}
"""


def az_variant(**subs):
    out = EN
    for old, new in subs.items():
        out = out.replace(old.replace("__", " "), new)
    return out


def test_translated_prose_passes():
    az = EN.replace("## What Is Ownership?", "## Sahiblik nədir?").replace("Ownership is about", "Sahiblik bunlar haqqındadır:")
    assert compare(az, EN) == []


def test_fence_change_fails():
    assert compare(EN.replace("let x = 5; // five\n```\n\n```text", "let x = 6; // five\n```\n\n```text"), EN)


def test_rust_fence_comment_translation_passes():
    az = EN.replace("```rust\nlet x = 5; // five", "```rust\nlet x = 5; // beş")
    assert compare(az, EN) == []
    az = EN.replace("```text\nlet x = 5; // five", "```text\nlet x = 5; // beş")
    assert compare(az, EN)


def test_fence_lang_change_fails():
    assert compare(EN.replace("```rust", "```Rust"), EN)


def test_fence_length_change_fails():
    assert compare(EN.replace("```rust\nlet x = 5; // five\n```", "````rust\nlet x = 5; // five\n````"), EN)


def test_directive_change_fails():
    assert compare(EN.replace("a/src/main.rs:here", "b/src/main.rs:here"), EN)


def test_inline_code_changed_fails():
    assert compare(EN.replace("`String`", "`Sətir`"), EN)


def test_inline_code_reordered_passes():
    en = "A `a` then `b`."
    assert compare("B `b` sonra `a`.", en) == []
    assert compare("`a` yalnız.", en)


def test_listing_caption_may_change_but_not_number():
    en = '<Listing number="1-1" file-name="main.rs" caption="A program">\n\n</Listing>'
    assert compare(en.replace("A program", "Proqram"), en) == []
    assert compare(en.replace("1-1", "1-2"), en)


def test_ignore_marker_and_link_target():
    en = "[x](ch01.html)<!-- ignore --> y"
    assert compare("[x](ch01.html) y", en)
    assert compare("[x](ch02.html)<!-- ignore --> y", en)


def test_broken_anchor_reported(tmp_path):
    md = "## Sahiblik Nədir?\n\n[a](#what-is-ownership)\n"
    errs = broken_anchors(md, tmp_path, "x.md")
    assert errs and "what-is-ownership" in errs[0]
    assert broken_anchors("## Sahiblik Nədir?\n\n[a](#sahiblik-nədir)\n", tmp_path, "x.md") == []


def test_cross_file_anchor(tmp_path):
    (tmp_path / "ch04.md").write_text("## Sahiblik\n", encoding="utf-8")
    assert broken_anchors("[a](ch04.html#sahiblik)", tmp_path, "x.md") == []
    assert broken_anchors("[a](ch04.html#ownership)", tmp_path, "x.md")


def test_slug_keeps_azerbaijani_letters():
    assert heading_anchors("## Dəyişənlər və Dəyişkənlik") == {"dəyişənlər-və-dəyişkənlik"}


def test_slug_ignores_fenced_hashes_and_dedups():
    md = "## A\n\n```console\n# not a heading\n```\n\n## A\n"
    assert heading_anchors(md) == {"a", "a-1"}


def test_html_anchor_and_listing_ids():
    md = '<a id="old"></a>\n\n<Listing number="3-1" caption="x">\n</Listing>\n'
    assert {"old", "listing-3-1"} <= heading_anchors(md)


def test_blockquote_heading_and_generics_in_code():
    md = "> ### Where’s the `->` Operator?\n\n#### Shared Access to `Mutex<T>`\n"
    assert heading_anchors(md) == {"wheres-the---operator", "shared-access-to-mutext"}


def test_inherited_broken_anchor_not_reported(tmp_path):
    from check_chapter import check_file

    en_dir, az_dir = tmp_path / "en", tmp_path / "az"
    en_dir.mkdir(), az_dir.mkdir()
    (en_dir / "a.md").write_text("## A\n\n[x](#gone)\n", encoding="utf-8")
    (az_dir / "a.md").write_text("## B\n\n[x](#gone)\n", encoding="utf-8")
    assert check_file(az_dir / "a.md", en_dir, az_dir) == []


def test_heading_in_html_comment_ignored():
    assert heading_anchors("## A\n\n<!-- x\n# copy the output here\n-->\n") == {"a"}


def test_summary_az_only_entry_allowed(tmp_path):
    from check_chapter import check_file

    en_dir, az_dir = tmp_path / "en", tmp_path / "az"
    en_dir.mkdir(), az_dir.mkdir()
    (en_dir / "SUMMARY.md").write_text("- [A](a.md)\n", encoding="utf-8")
    (az_dir / "SUMMARY.md").write_text("- [A](a.md)\n- [Lüğət](appendix-08-glossary.md)\n", encoding="utf-8")
    assert check_file(az_dir / "SUMMARY.md", en_dir, az_dir) == []
