# Rust Proqramlaşdırma Dili: Azerbaijani translation, getting-started design

## Intent
Translate *The Rust Programming Language* (rust-lang/book) into Azerbaijani so that people
in Azerbaijan who are curious about Rust can learn it in their own language. No Azerbaijani
translation exists yet: it isn't in the book's Appendix F and there's no GitHub project or
Translations issue for it.

This design covers **getting started**: the project skeleton, the term glossary, the
translation workflow and a first translated sample. The full book (about 110 chapter files)
is translated afterwards, chapter by chapter, using what this phase sets up.

## Goals
- A repo that builds the Azerbaijani book as a website with mdBook, with Rust code listings
  rendering exactly as in the English book.
- A glossary (`GLOSSARY.md`) that fixes one Azerbaijani rendering per technical term,
  used strictly in every chapter.
- A reusable Claude skill (`rust-book-az`) that encodes the glossary rules and the
  style rules, so each later chapter is drafted the same way.
- First sample: `foreword.md`, `ch00-00-introduction.md` and chapter 1 (installation,
  Hello World, Hello Cargo) translated and reviewed.

## Non-goals (for now)
- Translating the whole book in this phase.
- Translating the print/No Starch edition (`nostarch/`), the old editions or `listings/` code.
- Getting the translation linked from Appendix F. That's a later step, once a meaningful part
  of the book is done (open a Translations issue and a PR adding a line to Appendix F).

## Anti-goals (failure even if it "works")
- The same English term translated different ways in different chapters
  (the Turkish attempt's main problem: closure → kapanma/kapanış/kapama).
- Distinct concepts collapsed into one word (Turkish: stack and heap both → *yığın*).
- Anything inside code blocks, inline code, Rust keywords, `{{#include}}`/`{{#rustdoc_include}}`
  directives, `<Listing>` tags, link targets or `<!-- ignore -->` markers changed, which would
  break the build.
- Unchecked machine translation. Every chapter is reviewed by a native speaker before it's
  marked done.

## Decisions (made with the user)
1. **Terminology**: use the terms Azerbaijani developers actually use, not academic coinages.
2. **English in parentheses**: on a term's **first use in each chapter**, e.g.
   *sahiblik (ownership)*. Later uses in the same chapter: Azerbaijani only.
3. **Glossary appendix**: the book gets an extra appendix listing every term
   (Azerbaijani ↔ English), generated from `GLOSSARY.md`.
4. **Untranslated Rust-specific terms** (candidates: *trait*, *crate*; decided per term
   in the glossary) stay in English and take Azerbaijani suffixes with a hyphen, following
   Azerbaijani spelling rules for foreign words: *trait-in*, *crate-ə*.
5. **Repo setup: approach A** (picked over B and C, see below).
6. **Workflow**: Claude drafts each chapter from the glossary and skill; the user reviews and
   corrects. Corrections feed back into `GLOSSARY.md` and the skill.

## Approaches considered
- **A. Separate repo + English book as a pinned git submodule (chosen).** Same setup as the
  active Uzbek translation (rust-lang-uz/book). Bumping the submodule shows exactly which
  English chapters changed; the book's preprocessors (`packages/mdbook-trpl`) and the
  `listings/` code come from the submodule, so listings render correctly. Cost: contributors
  need to know `git submodule update --init`.
- **B. Fork rust-lang/book, translate `src/` in place.** Simplest start, but every upstream
  merge conflicts with translated text; the main reason translations freeze on old versions.
- **C. gettext `.po` files via mdbook-i18n-helpers** (Comprehensive Rust's setup). Best
  automatic change tracking, but you translate in `.po` files instead of readable Markdown,
  with heavier tooling. Too much for one person starting out.

## Structure
```
rust-book-az/
├── rustbook-en/            git submodule → rust-lang/book, pinned to branch rust-1.99
├── rustbook-az/
│   ├── book.toml           language = "az", title "Rust Proqramlaşdırma Dili";
│   │                       preprocessors + listing paths point into ../rustbook-en
│   ├── src/                translated .md files, same file names as English
│   └── TRANSLATION_STATUS.md  per-file: not started / draft / reviewed, + English commit hash
│   └── listings/           copy of the English listings, comments translated
├── CLAUDE.md, .claude/skills/rust-book-az/   Claude Code setup (see below)
├── tools/                  check scripts
├── GLOSSARY.md             term table: English | Azerbaijani | note/example | status
├── STYLE.md                style rules (below)
├── README.md               in Azerbaijani + English: what this is, how to build, how to help
├── .github/workflows/      build with mdBook and publish to GitHub Pages on push to main
├── LICENSE-MIT, LICENSE-APACHE, COPYRIGHT   same licences as upstream
```
Files not yet translated are copied from English so the book always builds completely;
`TRANSLATION_STATUS.md` shows what's done.

## Style rules (STYLE.md seed)
- Address the reader as **siz** (polite/plural), matching the book's friendly but
  instructive tone. *(Claude's call: please confirm.)*
- Modern Azerbaijani Latin alphabet; proper letters ə, ı, ö, ü, ç, ş, ğ throughout.
- Headings translated; mdBook anchors generated from translated headings, so internal
  links get updated to match.
- Compiler output and error messages in code blocks stay in English (that's what readers will
  see on their own screens); the prose explaining them is translated.
- **Comments inside code listings are translated, following the glossary** (user's decision).
  The listings live in `rustbook-en/listings/` (627 `.rs` files, ~400 comment lines), so the
  repo keeps its own copy in `rustbook-az/listings/` and the translated chapters include from
  there. Only `//` and `/* */` comment text changes: code, string literals, identifiers,
  `// ANCHOR:` / `// ANCHOR_END:` markers and `output.txt` files stay byte-identical, so
  `mdbook test` still passes. A check script compares each translated listing to its
  English original with comments stripped and fails on any other difference.

## Working with Claude Code (user's decision)
The project is set up to be worked on with Claude Code, by the user and by any future
contributor:
- `CLAUDE.md` at the repo root: what the project is, the structure, the workflow
  (draft → review → status update), and the hard rules (glossary only, never touch code).
- The skill lives **in the repo** at `.claude/skills/rust-book-az/SKILL.md`, so anyone who
  opens the repo in Claude Code gets the same rules automatically.
- Helper scripts in `tools/`: `status` (which files are untranslated/outdated vs the pinned
  English commit), `check-chapter` (code blocks, directives and links match English
  one-to-one), `check-listings` (comment-only diff), `glossary-lint` (flags English glossary
  terms left in prose, and inconsistent renderings).

## The skill (rust-book-az)
Contents: the do-not-touch rules (code, directives, tags, links), the glossary-lookup rule
(every technical term must come from `GLOSSARY.md`; new terms are proposed to the user, not
invented silently), the first-use-in-parentheses rule, the hyphen-suffix rule, STYLE.md, and
the listing-comment rule, and a final check step (run the `tools/` checks and `mdbook build`).
Committed to the repo; refined after chapter 1 settles the rules.

## Glossary seed
About 60 core terms from chapters 1–10 (variable, function, ownership, borrowing, reference,
slice, struct, enum, pattern matching, crate, module, package, trait, generic, lifetime,
stack, heap, closure, iterator, …), each with Claude's proposed rendering and a note where
it's uncertain. The user reviews this table **before** any chapter is drafted.

## Left to the builder (Claude's calls, flagged)
- Pin to `rust-1.99` (newest release branch) rather than `main`, so the translation tracks a
  stable version.
- mdBook version: the one the book's README/rust-lang/rust currently specifies.
- GitHub Pages via GitHub Actions for publishing.

## Repo
- `github.com/hidayatrzayev/rust-book-az` (user's choice). Claude pushes there if the repo is
  attached to the session; otherwise hands over the repo for the user to push.
