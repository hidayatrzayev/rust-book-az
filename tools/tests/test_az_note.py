import io
import json

import az_note
from az_note import rewrite


def test_qeyd_blockquote_becomes_note_section():
    md = "Mətn.\n\n> Qeyd: Bu qeyddir.\n> Davam edir.\n\nSonra."
    assert rewrite(md) == (
        "Mətn.\n\n"
        '<section class="note" aria-role="note">\n\n'
        "Qeyd: Bu qeyddir.\nDavam edir.\n\n</section>\n\nSonra."
    )


def test_other_blockquotes_untouched():
    md = "> ### Komanda sətri\n>\n> Qeyd: içəridə.\n\n> Sadə sitat."
    assert rewrite(md) == md


def test_english_note_untouched():
    md = "> Note: left for trpl-note."
    assert rewrite(md) == md


def test_inside_fence_untouched():
    md = "```text\n> Qeyd: kod.\n```\n> Qeyd: real."
    assert rewrite(md) == (
        "```text\n> Qeyd: kod.\n```\n"
        '<section class="note" aria-role="note">\n\nQeyd: real.\n\n</section>'
    )


def test_links_and_markers_preserved():
    md = "> Qeyd: Bax [Əlavə D][devtools]<!-- ignore -->\n> daha çox."
    out = rewrite(md)
    assert "[Əlavə D][devtools]<!-- ignore -->\ndaha çox." in out


def test_main_rewrites_nested_chapters(monkeypatch, capsys):
    book = {"items": [{"Chapter": {"content": "> Qeyd: a", "sub_items": [
        {"Chapter": {"content": "> Qeyd: b", "sub_items": []}}]}}, "Separator"]}
    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps([{}, book])))
    assert az_note.main(["az_note.py"]) == 0
    out = json.loads(capsys.readouterr().out)
    top = out["items"][0]["Chapter"]
    assert top["content"].startswith('<section class="note"')
    assert top["sub_items"][0]["Chapter"]["content"].startswith('<section class="note"')


def test_supports_any_renderer():
    assert az_note.main(["az_note.py", "supports", "html"]) == 0
