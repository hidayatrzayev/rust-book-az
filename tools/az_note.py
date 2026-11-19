"""mdBook preprocessor: Azerbaijani semantic notes.

The upstream `trpl-note` preprocessor only recognises blockquotes that start
with the literal English text `> Note: `. The translation writes `> Qeyd: `
instead, so this preprocessor turns such blockquotes into the same markup
`trpl-note` produces:

    > Qeyd: Bu qeyddir.          <section class="note" aria-role="note">
    > Davam edir.          →
                                 Qeyd: Bu qeyddir.
                                 Davam edir.

                                 </section>

Fenced code blocks are left alone. Stdlib only, so it runs on any Python 3.8+.

    mdbook calls:  python3 ../tools/az_note.py supports <renderer>
                   python3 ../tools/az_note.py   (book JSON on stdin)
"""

import json
import re
import sys

MARKER = "Qeyd: "
OPEN = '<section class="note" aria-role="note">'
CLOSE = "</section>"
_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_QUOTE = re.compile(r"^ {0,3}> ?")


def _unquote(line):
    return _QUOTE.sub("", line, count=1)


def rewrite(md):
    """Return `md` with every `> Qeyd: ` blockquote turned into a note section."""
    lines = md.split("\n")
    out = []
    fence = None
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _FENCE.match(line)
        if fence is not None:
            out.append(line)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            i += 1
            continue
        if m:
            fence = m.group(1)
            out.append(line)
            i += 1
            continue
        if _QUOTE.match(line):
            # Take the whole blockquote; only its first line decides.
            block = []
            while i < len(lines) and _QUOTE.match(lines[i]):
                block.append(lines[i])
                i += 1
            if _unquote(block[0]).startswith(MARKER):
                out.extend([OPEN, ""] + [_unquote(b) for b in block] + ["", CLOSE])
            else:
                out.extend(block)
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def _walk(node):
    if isinstance(node, dict):
        chapter = node.get("Chapter")
        if isinstance(chapter, dict) and isinstance(chapter.get("content"), str):
            chapter["content"] = rewrite(chapter["content"])
        for value in node.values():
            _walk(value)
    elif isinstance(node, list):
        for value in node:
            _walk(value)


def main(argv):
    if len(argv) > 1 and argv[1] == "supports":
        return 0  # renderer-independent Markdown rewrite
    _context, book = json.load(sys.stdin)
    _walk(book)
    json.dump(book, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
