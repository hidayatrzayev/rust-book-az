from check_listings import check_pair, strip_comments


def test_comment_only_change_passes():
    assert strip_comments("let x = 5; // five") == strip_comments("let x = 5; // beş")


def test_code_change_fails():
    assert strip_comments("let x = 5;") != strip_comments("let x = 6;")


def test_anchor_change_fails():
    assert strip_comments("// ANCHOR: here\n") != strip_comments("// ANCHOR: burada\n")


def test_url_in_string_not_comment():
    assert '"http://a"' in strip_comments('let u = "http://a"; // c')


def test_block_and_doc_comments():
    out = strip_comments("/* a\nb */\n/// doc\n//! inner\nfn f() {}")
    assert "doc" not in out and "inner" not in out and "a\nb" not in out
    assert "fn f() {}" in out


def test_raw_string_and_char_literals():
    src = 'let a = r#"// not "a" comment"#; let c = \'"\'; // real'
    out = strip_comments(src)
    assert 'r#"// not "a" comment"#' in out and "real" not in out


def test_nested_block_comment():
    assert strip_comments("a /* x /* y */ z */ b") == strip_comments("a /* q */ b")


def test_lifetime_not_char_literal():
    out = strip_comments("fn f<'a>(x: &'a str) {} // tail")
    assert "tail" not in out and "&'a str" in out


def test_non_rs_file_byte_compare(tmp_path):
    en, az = tmp_path / "en", tmp_path / "az"
    for d, txt in ((en, "ok\n"), (az, "OK\n")):
        d.mkdir()
        (d / "output.txt").write_text(txt)
    assert check_pair(az / "output.txt", en / "output.txt")


def test_rs_comment_translation_passes(tmp_path):
    en, az = tmp_path / "en.rs", tmp_path / "az.rs"
    en.write_text("fn main() {\n    let x = 5; // five\n}\n")
    az.write_text("fn main() {\n    let x = 5; // beş\n}\n")
    assert check_pair(az, en) == []
    az.write_text("fn main() {\n    let x = 6; // beş\n}\n")
    assert check_pair(az, en)
