# rust-book-az

Azerbaijani translation of *The Rust Programming Language* (rust-lang/book), built with mdBook.
Design: `docs/design.md`. Plan: `docs/plan.md`. Translation rules: `STYLE.md`, `GLOSSARY.md`,
and the skill `.claude/skills/rust-book-az/SKILL.md` (use it for any translation or review work).

## Structure

```
rustbook-en/          git submodule → rust-lang/book, branch rust-1.99 (read-only; preprocessors + original text)
rustbook-az/
  book.toml           language "az"; preprocessors run from ../rustbook-en/packages/mdbook-trpl
  src/                translated .md (same file names as English; untranslated ones are English copies)
  listings/           copy of English listings; only comment text may differ
  TRANSLATION_STATUS.md   per file: başlanmayıb / qaralama / yoxlanılıb + English commit
tools/                check scripts + tests (Python 3.11+, stdlib; pytest for tests)
GLOSSARY.md           term table; STYLE.md style rules
.github/workflows/ci.yml   checks, build, Pages deploy
```

## Hard rules

- Technical terms only from `GLOSSARY.md`; new terms are proposed to the human, not invented.
- Never change code, inline code, `{{#include}}` directives, `<Listing>` attributes (except `caption`), link targets, `<!-- ignore -->`.
- Only a human marks a file `yoxlanılıb`. Workflow per file: draft → checks → `qaralama` → human review → corrections feed back into `GLOSSARY.md`/skill.
- Never edit `rustbook-en/`.

## Commands

```bash
git submodule update --init                       # after cloning
uv venv .venv --python 3.14 && uv pip install --python .venv/bin/python pytest pyyaml   # once
cargo install mdbook --version 0.5.1 --locked     # once
mdbook build rustbook-az                          # build  (mdbook serve rustbook-az --open to preview)
python -m pytest tools                            # tests for the tools
python tools/check_listings.py                    # listings differ only in comments
python tools/check_chapter.py [files]             # code/directives/links match English, anchors exist
python tools/glossary.py lint <files>             # glossary rules (pass a whole chapter's files together)
python tools/glossary.py check                    # glossary itself (no two terms share a rendering)
python tools/glossary.py appendix > rustbook-az/src/appendix-08-glossary.md
python tools/status.py                            # counts + files outdated vs. the pinned English book
python tools/status.py set <file> <status>
```

`tools/az_note.py` is an mdBook preprocessor (wired in `book.toml`): it renders `> Qeyd: ` blockquotes as note boxes,
because upstream `trpl-note` only recognises `> Note: `. Translated notes always start with `> Qeyd: `.

### Bumping the English submodule

1. `git -C rustbook-en fetch && git -C rustbook-en checkout <new rev>`; `git add rustbook-en`.
2. `python tools/status.py` lists `KÖHNƏLİB` files; `git -C rustbook-en diff <old>..<new> -- src listings` shows what changed.
3. Copy new/changed files into `rustbook-az/src` and `rustbook-az/listings` (never overwrite translated ones blindly; merge by hand), then `python tools/status.py init`.
4. Run all checks and `mdbook build rustbook-az`.

## Models

Setup and tooling work runs on Sonnet. Glossary work and translation run on Opus (the skill sets `model: opus`
for the turn it is invoked in; start a session with `claude --model opus` for longer translation sessions).
