# Tərcümə üslubu / Style guide

*English summary at the bottom.*

## Dil və ünsiyyət tərzi

- Oxucuya **siz** (nəzakətli/cəm forma) ilə müraciət olunur; kitabın səmimi, lakin öyrədici tonu saxlanılır.
- Müasir Azərbaycan latın əlifbası: ə, ı, ö, ü, ç, ş, ğ hərfləri həmişə düzgün yazılır (`e`, `i`, `o`, `u`, `c`, `s`, `g` ilə əvəz edilmir).
- Cümlələr Azərbaycan dilinin sözsırasına uyğun qurulur (xəbər sonda), ingilis cümlə quruluşu hərfi köçürülmür.
- Eyni mənalı ifadə bütün fəsillərdə eyni cür tərcümə olunur.
- **Proqramçıların gündəlik dilinə üstünlük verilir**, formal ədəbi dilə yox: *data strukturu* (*verilənlər strukturu* yox), *direktoriya* (*qovluq* yox), *optimizasiya* (*optimallaşdırma* yox). Yeni termin təklif edərkən developerlərin real danışıqda işlətdiyi forma seçilir.

## Terminlər

- Texniki terminlər **yalnız** `GLOSSARY.md`-dən götürülür. Yeni termin lazım olarsa, tərcüməçi onu özü uydurmur: lüğətə `təklif` statuslu sətir əlavə edib insandan soruşur.
- Terminin **hər fəsildə ilk işləndiyi yerdə** ingiliscə qarşılığı mötərizədə verilir: *sahiblik (ownership)*. Eyni fəsildə sonrakı işlənmələrdə yalnız Azərbaycanca.
- **Gündəlik sözlər** (`GLOSSARY.md`-də Qeyd sütununda `[gündəlik]` işarəsi olanlar: quraşdırmaq, brauzer, mötərizələr…) mötərizəsiz yazılır, ilk işlənmədə də. Mötərizə yalnız oxucuya həqiqətən faydalı olduqda, yəni texniki terminlər üçün yazılır.
- **Titul səhifəsi və ön söz** (`title-page.md`, `foreword.md`) texniki mətn deyil: orada heç bir terminə mötərizə yazılmır.
- **Rust-a məxsus terminlər və varlıqlar ingiliscə qalır, Azərbaycanca qarşılığı mötərizədə verilir** (hər fəsildə ilk işlənmədə): *borrow checker (borc yoxlayıcısı)*, *mutable (dəyişə bilən)*. Ümumi proqramlaşdırma terminləri isə Azərbaycanca yazılır, ingiliscəsi mötərizədə: *funksiya (function)*. Hansı terminin hansı qrupa aid olduğunu `GLOSSARY.md` göstərir (`—saxlanılır— (söz)`).
- Tərcümə olunmayan Rust terminləri (`—saxlanılır—`) ingiliscə qalır, Azərbaycan şəkilçiləri **defislə** yazılır: *trait-in*, *crate-ə*, *enum-lar*.
- Terminin Azərbaycanca şəkilçi aldığı hallarda (*sahibliyin*, *dəyişənə*) lüğət formasından istifadə edilir.

## Toxunulmaz hissələr

Heç vaxt dəyişdirilmir:

- Kod bloklarının məzmunu, sətirdaxili kod (`` `...` ``), Rust açar sözləri;
- `{{#include ...}}` və `{{#rustdoc_include ...}}` göstərişləri;
- `<Listing ...>` teqinin atributları (`number`, `file-name`). **Yalnız `caption` mətni tərcümə olunur**, çünki oxucuya göstərilir;
- keçid hədəfləri (yalnız `#anchor` hissəsi tərcümə olunmuş başlığa uyğun yenilənir);
- `<!-- ignore -->` işarələri və `<a id="..."></a>` köhnə başlıq lövbərləri;
- `// ANCHOR:` / `// ANCHOR_END:` sətirləri və `output.txt` faylları.

Kompilyatorun çıxışı və xəta mesajları kod bloklarında **ingiliscə** qalır (oxucu öz ekranında məhz bunu görəcək); onları izah edən mətn tərcümə olunur.

## Qeydlər

`> Note: ` ilə başlayan qeyd blokları `> Qeyd: ` kimi yazılır (dəqiq bu formada, iki nöqtə və boşluqla); `tools/az_note.py` onları qeyd qutusuna çevirir.

## Başlıqlar

Başlıqlar tərcümə olunur. mdBook lövbərləri başlıqdan yaradıldığı üçün həmin fəsildəki və digər fəsillərdəki `#lövbər` keçidləri yeni lövbərə uyğun yenilənir. `python tools/check_chapter.py` mövcud olmayan lövbərləri tapır. Başlıqda ingiliscə mötərizə yazılmır (ilk işlənmə qaydası mətn hissəsinə aiddir).

## Kod şərhləri

Kod nümunələrindəki şərhlər (`//`, `///`, `//!`, `/* */`) **tərcümə olunur** və lüğətə uyğun yazılır. Yalnız şərh mətni dəyişir: kod, sətir literalları, identifikatorlar dəyişməz qalır. Şərhlər həm fəsil faylındakı ```` ```rust ```` bloklarında, həm də `rustbook-az/listings/` direktoriyasındakı `.rs` fayllarında tərcümə olunur. `python tools/check_listings.py` şərhdən başqa hər fərqi tapır.

## English summary

- Address the reader as *siz*; proper Azerbaijani Latin letters (ə ı ö ü ç ş ğ).
- Prefer developers' everyday Azerbaijani over formal literary language (*data strukturu*, *direktoriya*, *optimizasiya*).
- Technical terms only from `GLOSSARY.md`; new term → propose a row, never invent silently.
- General terms: Azerbaijani first, English in parentheses on first use per chapter. Rust-specific terms (borrow checker, ownership, mutable…): English kept, Azerbaijani gloss in parentheses on first use; later uses English only.
- Everyday words (tagged `[gündəlik]` in the glossary's note column) never get English in parentheses; the title page and foreword get no parentheses at all.
- Terms kept in English take hyphenated suffixes (*trait-in*, *crate-ə*).
- Never touch code, inline code, directives, `<Listing>` attributes (only `caption` text is translated), link targets (only `#anchor` follows translated headings), `<!-- ignore -->`, ANCHOR lines, `output.txt`.
- Notes: `> Note: ` becomes exactly `> Qeyd: ` (rendered as a note box by `tools/az_note.py`).
- Compiler output stays English; the prose around it is translated. Comments in code listings are translated.
