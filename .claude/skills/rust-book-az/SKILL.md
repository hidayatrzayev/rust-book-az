---
name: rust-book-az
description: Use when translating or reviewing any chapter or listing of the Rust book into Azerbaijani in this repo.
model: opus
---

# Translating the Rust book into Azerbaijani

The `model: opus` setting above applies only to the turn in which this skill is invoked (Claude Code
resumes the session model on the next prompt). Translation and glossary work belong on Opus, so if
you are continuing a chapter in a later turn on another model, say so and ask to switch with `/model`.

Translate **one file at a time**. English source: `rustbook-en/src/<file>.md` (pinned submodule, never
edit it). Target: `rustbook-az/src/<file>.md` (same file name; it starts as a copy of the English text).

## Steps

1. **Read first**: `GLOSSARY.md` and `STYLE.md` in full, and `rustbook-az/TRANSLATION_STATUS.md` for the file's status.
2. **Translate prose and headings** into Azerbaijani following `STYLE.md` (address the reader as *siz*).
3. **Protected items: never change** (the checks fail if you do):
   - fenced code blocks and inline code (`` `...` ``), including Rust keywords; compiler output stays English;
   - `{{#include}}` / `{{#rustdoc_include}}` directives;
   - `<Listing ...>` attributes (`number`, `file-name`); only the `caption` text is translated;
   - link targets, `<!-- ignore -->` markers, `<a id="..."></a>` anchors;
   - in listings: code, string literals, identifiers, `// ANCHOR:` / `// ANCHOR_END:` lines, `output.txt`.
4. **Terms**: every technical term comes from `GLOSSARY.md`, one rendering only. If you need a term that
   is not there, **stop and propose a new row** (status `təklif`) to the human; never invent a rendering
   silently, and do not translate the passage until it is decided.
5. **First use per chapter**: write the English in parentheses, *sahiblik (ownership)*; later uses in the
   same chapter are Azerbaijani only. Terms marked `—saxlanılır—` stay English with a hyphenated suffix: *trait-in*, *crate-ə*.
6. **Headings and anchors**: headings are translated, so mdBook anchors change. Update every `#anchor`
   link to a translated heading (in this file and in others) to the new anchor.
7. **Listing comments**: translate `//`, `///`, `//!`, `/* */` comments in the chapter's listings in
   `rustbook-az/listings/<chapter>/` (and inside `rust` fences in the chapter file), following the glossary.
8. **Check** (all must pass):
   ```bash
   python tools/check_chapter.py rustbook-az/src/<file>.md
   python tools/check_listings.py
   python tools/glossary.py lint rustbook-az/src/<chapter files>.md
   mdbook build rustbook-az
   ```
   Pass all files of the chapter to `glossary.py lint` so the first-use rule is tracked per chapter.
9. **Status**: `python tools/status.py set <file> qaralama`. Only the human sets `yoxlanılıb`.
10. **Corrections**: when the human corrects a term, update `GLOSSARY.md` (set `təsdiqlənib`), regenerate
    the appendix (`python tools/glossary.py appendix > rustbook-az/src/appendix-08-glossary.md`) and, if it
    changes a rule, this skill or `STYLE.md`, all in the same commit.
