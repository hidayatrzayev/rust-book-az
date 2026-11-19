# Rust Book Azerbaijani Translation: Getting-Started Implementation Plan

> **For the agent:** work through the tasks in order yourself, in this session (no subagents). Tick each `- [x]` box as you finish it and commit at the end of each task.

**Goal:** A `hidayatrzayev/rust-book-az` repo that builds the Azerbaijani Rust book with mdBook, enforces glossary/code-safety rules with check scripts, is set up for Claude Code, and contains the reviewed glossary plus a translated foreword, introduction and chapter 1.

**Architecture:** English book pinned as git submodule `rustbook-en` (branch `rust-1.99`, commit `852f28bd5f7e7fbe3ce447df4ba7742ab4af1713`). Translation is a standalone mdBook in `rustbook-az/` whose `src/` and `listings/` mirror the English layout (so relative `../listings/...` include paths stay unchanged) and whose preprocessors run from `../rustbook-en/packages/mdbook-trpl`. Python check scripts in `tools/` compare each Azerbaijani file to its English counterpart.

**Tech Stack:** mdBook 0.5.1, mdbook-trpl (from submodule), Python 3.11+ stdlib + pytest, GitHub Actions + GitHub Pages.

**Spec:** `docs/design.md`

## Global Constraints
- Submodule: `rustbook-en` → `https://github.com/rust-lang/book.git`, branch `rust-1.99`.
- mdBook version: `0.5.1` (same as upstream CI).
- `book.toml`: `language = "az"`, `title = "Rust Proqramlaşdırma Dili"`.
- File names in `rustbook-az/src/` and `rustbook-az/listings/` identical to English.
- Never change: code (fenced blocks and inline code), `{{#include}}` / `{{#rustdoc_include}}` directives, `<Listing ...>` tag attributes, link targets, `<!-- ignore -->` markers, `// ANCHOR:` / `// ANCHOR_END:` lines, `output.txt` files, string literals and identifiers in listings.
- Listing comments **are** translated, using the glossary.
- English term in parentheses on first use per chapter only: `sahiblik (ownership)`.
- Untranslated English terms take Azerbaijani suffixes with a hyphen: `trait-in`, `crate-ə`.
- Reader addressed as `siz`. Compiler output stays English.
- Licences: MIT + Apache-2.0, copied from upstream with COPYRIGHT.

## Review Focus
1. Translated heading changes its mdBook anchor → in-book `#anchor` links break. `check-chapter` must report links to anchors that don't exist in the target az file (test in Task 3).
2. A string literal containing `//` (e.g. `"http://..."`) in a listing → must not be treated as a comment by `check-listings` (test in Task 2).
3. Multi-line `/* */` and doc comments `///` / `//!` → treated as comments, translatable (test in Task 2).
4. Fenced code block with a different fence length or language tag in az (e.g. ```` ```rust ```` → ```` ```Rust ````) → reported as a code change (test in Task 3).
5. Glossary term inflected with Azerbaijani suffixes (`sahibliyin`, `trait-in`) → `glossary-lint` must recognise the stem and not flag it as inconsistent (test in Task 4).

---

### Task 1: Repo skeleton that builds

**Files:**
- Create: `.gitmodules` (submodule `rustbook-en`), `rustbook-az/book.toml`, `rustbook-az/src/**` (copied from `rustbook-en/src`), `rustbook-az/listings/**` (copied from `rustbook-en/listings`), `rustbook-az/ferris.css`, `rustbook-az/ferris.js`, `rustbook-az/theme/**` (copied), `README.md` (Azerbaijani first, English second: what it is, build, help), `LICENSE-MIT`, `LICENSE-APACHE`, `COPYRIGHT`, `.gitignore` (`book/`, `target/`, `__pycache__/`)

**Interfaces:**
- Produces: `rustbook-az/` buildable with `mdbook build rustbook-az`; all later tasks diff `rustbook-az/X` against `rustbook-en/X`.

- [x] **Step 1:** `git init`, add submodule pinned to the commit above, copy `src/`, `listings/`, `ferris.*`, `theme/` from it.
- [x] **Step 2:** Write `book.toml` from upstream's, with the constraint values, `git-repository-url = "https://github.com/hidayatrzayev/rust-book-az"`, and preprocessor commands pointing at `../rustbook-en/packages/mdbook-trpl/Cargo.toml`. Drop the `[output.html.redirect]` table.
- [x] **Step 3: Verify:** `mdbook build rustbook-az` exits 0; `grep -c "Listing 2-1" rustbook-az/book/ch02-00-guessing-game-tutorial.html` ≥ 1 (listings resolve).
- [x] **Step 4: Commit** `chore: skeleton with pinned English source`.

### Task 2: `tools/check_listings.py`

**Files:** Create `tools/check_listings.py`, `tools/tests/test_check_listings.py`

**Interfaces:**
- Produces: `strip_comments(source: str) -> str` (removes `//`, `///`, `//!` comment text and `/* */` blocks but keeps lines starting `// ANCHOR` / `// ANCHOR_END` verbatim; respects string and char literals, raw strings `r#"..."#`); CLI `python tools/check_listings.py [paths...]` (default: all `rustbook-az/listings/**/*.rs`) exits 1 and prints `path:line` on any mismatch between `strip_comments(az)` and `strip_comments(en)`; also byte-compares every non-`.rs` file (incl. `output.txt`, `Cargo.toml`).

- [x] **Step 1: Failing tests:**
  - `test_comment_only_change_passes`: en `let x = 5; // five`, az `let x = 5; // beş` → equal after strip.
  - `test_code_change_fails`: `let x = 5;` vs `let x = 6;` → differ.
  - `test_anchor_change_fails`: `// ANCHOR: here` vs `// ANCHOR: burada` → differ.
  - `test_url_in_string_not_comment`: `let u = "http://a"; // c` → strip result contains `"http://a"`.
  - `test_block_and_doc_comments`: `/* a\nb */`, `/// doc`, `//! inner` all stripped.
  - `test_non_rs_file_byte_compare`: differing `output.txt` → reported.
- [x] **Step 2:** `pytest tools/tests/test_check_listings.py` → FAIL (module missing).
- [x] **Step 3:** Implement with a small char-level scanner (states: code, string, raw string, char, line comment, block comment with nesting).
- [x] **Step 4:** Tests PASS; `python tools/check_listings.py` on the untouched copy exits 0.
- [x] **Step 5: Commit** `feat: listing comment-only checker`.

### Task 3: `tools/check_chapter.py`

**Files:** Create `tools/check_chapter.py`, `tools/tests/test_check_chapter.py`

**Interfaces:**
- Consumes: `strip_comments` from Task 2 — fences tagged `rust` (incl. `rust,ignore` etc.) are compared after `strip_comments`, so translated comments inside inline code blocks pass; all other fences compare verbatim.
- Produces: `extract_protected(md: str) -> list[tuple[str, str]]` returning ordered `(kind, text)` for kinds `fence` (whole fenced block incl. fence line), `inline_code`, `directive` (`{{#...}}`), `listing_tag` (`<Listing ...>` opening tag), `link_target` (URL/ref part of `[x](y)` and `[x]: y` definitions), `ignore_marker`; `heading_anchors(md: str) -> set[str]` using mdBook's slug rule (lowercase, strip punctuation except `-`/`_`, spaces→`-`, Unicode letters kept); CLI `python tools/check_chapter.py <az.md>...` compares against `rustbook-en/src/<same name>`, exits 1 listing each differing item; also reports `#anchor` links (same file or `other.md#anchor`) whose anchor isn't in that az file's `heading_anchors`.
- Inline code must match the English file as a multiset (order may change with Azerbaijani word order; count and content may not).

- [x] **Step 1: Failing tests:**
  - `test_translated_prose_passes`: only prose and headings changed → no errors.
  - `test_fence_change_fails`: code inside ```` ```rust ```` changed → error.
  - `test_rust_fence_comment_translation_passes`: ```` ```rust ```` block `let x = 5; // five` → `// beş` → no error; same in a ```` ```text ```` block → error.
  - `test_fence_lang_change_fails`: ```` ```rust ```` → ```` ```Rust ```` → error.
  - `test_directive_change_fails`: `{{#rustdoc_include ../listings/a.rs}}` path changed → error.
  - `test_broken_anchor_reported`: az heading `## Sahiblik Nədir?` with link `#what-is-ownership` → error naming the anchor; with `#sahiblik-nədir` → OK.
  - `test_slug_keeps_azerbaijani_letters`: `heading_anchors("## Dəyişənlər və Dəyişkənlik")` == `{"dəyişənlər-və-dəyişkənlik"}`.
- [x] **Step 2:** Run → FAIL.
- [x] **Step 3:** Implement (line-based fence detection, regex for the rest).
- [x] **Step 4:** Tests PASS; `python tools/check_chapter.py rustbook-az/src/*.md` on the untouched copy exits 0.
- [x] **Step 5: Commit** `feat: chapter structure checker`.

### Task 4: Glossary, lint and generated appendix

**Files:** Create `GLOSSARY.md`, `tools/glossary.py`, `tools/tests/test_glossary.py`, `rustbook-az/src/appendix-08-glossary.md` (generated), Modify `rustbook-az/src/SUMMARY.md` (add appendix after `appendix-07`).

**Interfaces:**
- `GLOSSARY.md` is one Markdown table: `| English | Azərbaycanca | Qeyd | Status |`, Status ∈ `təklif` (proposed) / `təsdiqlənib` (approved). Azərbaycanca = `—saxlanılır—` means kept in English.
- Produces: `load_glossary(path) -> list[Term]` (`Term(en: str, az: str, note: str, approved: bool, keep_english: bool)`); `lint(md: str, terms) -> list[Issue]` flagging (a) an English glossary term in prose outside code/parentheses for terms not kept in English, (b) a kept-English term followed by a suffix without hyphen (`traitin`), (c) first prose occurrence of a translated term in the file lacking `(english)`; CLI `python tools/glossary.py lint <az.md>...` and `python tools/glossary.py appendix > rustbook-az/src/appendix-08-glossary.md`.
- Matching is case-insensitive and by stem prefix (`sahiblik` matches `sahibliyin`, `sahibliyi` via a per-term `stems` list derived from the az form minus final consonant softening k→y, q→ğ).

- [ ] **Step 1: Failing tests:** `test_untranslated_english_flagged` ("the ownership rules" in prose → issue), `test_english_in_parentheses_ok`, `test_english_in_code_ok`, `test_inflected_az_recognised` (`sahibliyin` counts as use of `sahiblik`), `test_kept_term_needs_hyphen` (`traitin` → issue, `trait-in` → OK), `test_first_use_needs_parentheses`, `test_appendix_sorted_by_az`.
- [ ] **Step 2:** Run → FAIL. **Step 3:** Implement. **Step 4:** PASS.
- [ ] **Step 5:** Fill `GLOSSARY.md` with ≈60 core terms from chapters 1–10 (status `təklif`), each with a note where uncertain. Must include distinct renderings for stack vs heap, and entries for: variable, mutable/immutability, constant, shadowing, function, statement, expression, ownership, move, clone, copy, drop, borrowing, reference, mutable reference, dangling reference, slice, string, struct, field, method, associated function, enum, variant, pattern, match, crate, package, module, path, scope, vector, hash map, error, panic, generic, trait, trait bound, lifetime, closure, iterator, smart pointer, thread, compiler, borrow checker, type, integer, float, tuple, array, macro, attribute, test.
- [ ] **Step 6:** Generate appendix; `mdbook build rustbook-az` exits 0.
- [ ] **Step 7: Commit** `feat: glossary, lint and glossary appendix`.

### Task 5: Status tracking

**Files:** Create `rustbook-az/TRANSLATION_STATUS.md`, `tools/status.py`, `tools/tests/test_status.py`

**Interfaces:**
- `TRANSLATION_STATUS.md` table: `| Fayl | Status | İngiliscə commit |`, Status ∈ `başlanmayıb` / `qaralama` / `yoxlanılıb` (not started / draft / reviewed); one row per `src/*.md`.
- Produces: CLI `python tools/status.py` prints counts per status and lists `KÖHNƏLİB` (outdated) files whose recorded commit ≠ latest commit touching that English file in the submodule (`git -C rustbook-en log -1 --format=%H -- src/<file>`); `python tools/status.py set <file> <status>` updates the row and stamps the current commit.
- [ ] **Steps:** tests `test_outdated_detected`, `test_set_stamps_commit` (temp git repo fixture) → FAIL → implement → PASS → generate initial file (all `başlanmayıb`) → commit `feat: translation status tracking`.

### Task 6: Claude Code setup and style guide

**Files:** Create `CLAUDE.md`, `STYLE.md`, `.claude/skills/rust-book-az/SKILL.md`

- `STYLE.md`: the Global Constraints' language rules, written in Azerbaijani with English summary.
- `SKILL.md` frontmatter: `name: rust-book-az`, `model: opus`, description "Use when translating or reviewing any chapter or listing of the Rust book into Azerbaijani in this repo." Before writing it, check the exact frontmatter format for `model` in the Claude Code skills docs (https://code.claude.com/docs/en/skills.md) and follow it. Body, in order: read `GLOSSARY.md` + `STYLE.md`; translate one file at a time; never touch protected items (list); new term → stop and propose a glossary row (status `təklif`) instead of inventing; translate comments in that chapter's listings; run `check_chapter`, `check_listings`, `glossary lint`, `mdbook build`; set status to `qaralama`; only the human sets `yoxlanılıb`; when the human corrects a term, update `GLOSSARY.md` in the same commit.
- `CLAUDE.md`: purpose, structure tree, commands (build, serve, tests, checks, status, submodule bump procedure), pointer to the skill.
- `CLAUDE.md` also states the model split: setup and tooling work runs on Sonnet; glossary work and translation run on Opus (the skill enforces this for translation).
- [ ] **Verify:** a fresh Claude Code session in the repo lists `rust-book-az` among skills; starting a session with `claude --model sonnet` and invoking the skill switches it to Opus for that work; `pytest tools` passes. **Commit** `docs: Claude Code setup and style guide`.

### Task 7: CI and GitHub Pages

**Files:** Create `.github/workflows/ci.yml`

- On push/PR: checkout with submodules, install mdBook 0.5.1 (same curl as upstream), `pytest tools`, `check_listings`, `check_chapter` on all az src, `glossary.py lint` on files with status ≠ `başlanmayıb`, `mdbook build rustbook-az`. On push to `main`: deploy `rustbook-az/book` with `actions/upload-pages-artifact` + `actions/deploy-pages`.
- [ ] **Verify:** `act` not required; validate YAML with `python -c "import yaml,sys;yaml.safe_load(open(sys.argv[1]))" .github/workflows/ci.yml`. **Commit** `ci: build, checks and Pages deploy`.

### Task 8: Glossary review gate (human)

> Run Tasks 8–9 on Opus (`claude --model opus`). Tasks 1–7 are fine on Sonnet.

- [ ] Send `GLOSSARY.md` to the user; apply every correction; flip reviewed rows to `təsdiqlənib`. **No chapter is drafted before this.** Commit `docs: glossary reviewed`.

### Task 9: First sample translation

**Files:** Modify `rustbook-az/src/{foreword,ch00-00-introduction,ch01-00-getting-started,ch01-01-installation,ch01-02-hello-world,ch01-03-hello-cargo}.md`, `rustbook-az/src/SUMMARY.md` (translated titles), `rustbook-az/TRANSLATION_STATUS.md`
(Chapter 1 has no `{{#include}}` listings; its code is inline and stays unchanged except comments inside fenced blocks, which are translated.)

- [ ] Translate following the skill.
- [ ] Verify all checks + `mdbook build` pass; set status `qaralama`; send rendered pages to the user for review; apply corrections (and glossary/skill updates); set `yoxlanılıb`. Commit `feat: translate foreword, introduction, chapter 1`.

### Task 10: Publish

- [ ] Create `hidayatrzayev/rust-book-az` on GitHub (`gh repo create hidayatrzayev/rust-book-az --public --source . --push` if `gh` is installed and logged in; otherwise the user creates the empty repo on github.com and Claude runs `git remote add origin … && git push -u origin main`). Enable Pages with source "GitHub Actions" (`gh api -X POST repos/hidayatrzayev/rust-book-az/pages -f build_type=workflow`, or the user does it under Settings → Pages).
