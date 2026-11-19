# Rust Proqramlaşdırma Dili

*[English version below](#english)*

Bu repozitoriya [*The Rust Programming Language*](https://github.com/rust-lang/book) kitabının Azərbaycan dilinə tərcüməsidir. Məqsəd Rust-a maraq göstərən Azərbaycanlıların onu ana dilində öyrənə bilməsidir.

Tərcümə hələ **başlanğıc mərhələsindədir**: layihənin quruluşu, terminlər lüğəti (`GLOSSARY.md`) və ilk nümunə (ön söz, giriş və 1-ci fəsil) hazırlanır. Hansı faylların hazır olduğunu `rustbook-az/TRANSLATION_STATUS.md` göstərir.

## Kitabı yığmaq

```bash
git clone --recurse-submodules https://github.com/hidayatrzayev/rust-book-az
cd rust-book-az
# artıq klonlamısınızsa: git submodule update --init
cargo install mdbook --version 0.5.1 --locked
mdbook serve rustbook-az --open
```

İngilis dilindəki orijinal `rustbook-en/` direktoriyasında git submodule kimi saxlanılır; kitabın preprosessorları və kod nümunələri oradan istifadə olunur.

## Necə kömək etmək olar

- `rustbook-az/TRANSLATION_STATUS.md` faylında `qaralama` statuslu fəsilləri oxuyub səhvləri və qəliz yerləri bildirin.
- `GLOSSARY.md` faylındakı terminlərə öz təklifinizi issue kimi yazın.
- Tərcümə qaydaları üçün `STYLE.md` faylına baxın. Kod, `{{#include}}` göstərişləri və keçidlər heç vaxt dəyişdirilmir.

## English

This repository is an Azerbaijani translation of [*The Rust Programming Language*](https://github.com/rust-lang/book), so that people in Azerbaijan can learn Rust in their own language.

The translation is in its **getting-started phase**: project skeleton, term glossary (`GLOSSARY.md`) and a first sample (foreword, introduction, chapter 1). See `rustbook-az/TRANSLATION_STATUS.md` for per-file progress.

### Build

```bash
git clone --recurse-submodules https://github.com/hidayatrzayev/rust-book-az
cd rust-book-az
cargo install mdbook --version 0.5.1 --locked
mdbook serve rustbook-az --open
```

The English book is pinned as the `rustbook-en` git submodule (branch `rust-1.99`); the preprocessors and listings come from it.

### Help

Review `draft` chapters, suggest glossary terms via issues, and read `STYLE.md` before translating. Code, include directives and link targets are never changed.

## Licence

MIT or Apache-2.0, same as upstream. See `LICENSE-MIT`, `LICENSE-APACHE` and `COPYRIGHT`.
