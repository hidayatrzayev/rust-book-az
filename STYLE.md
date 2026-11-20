# Tərcümə üslubu / Style guide

*English summary at the bottom.*

## Dil və ünsiyyət tərzi

- Oxucuya **siz** (nəzakətli/cəm forma) ilə müraciət olunur; kitabın səmimi, lakin öyrədici tonu saxlanılır.
- Müasir Azərbaycan latın əlifbası: ə, ı, ö, ü, ç, ş, ğ hərfləri həmişə düzgün yazılır (`e`, `i`, `o`, `u`, `c`, `s`, `g` ilə əvəz edilmir).
- Cümlələr Azərbaycan dilinin sözsırasına uyğun qurulur (xəbər sonda), ingilis cümlə quruluşu hərfi köçürülmür.
- Eyni mənalı ifadə bütün fəsillərdə eyni cür tərcümə olunur.
- **Vurğu (kursiv)** ingilis sözünün tərcüməsinə mexaniki köçürülmür: Azərbaycan cümləsində məntiqi vurğunu daşıyan söz kursivlə yazılır. *what programming **is*** → *proqramlaşdırmanın **nə** olduğu*; *safety **and** productivity* → *təhlükəsizlik **və** məhsuldarlıq*.
- Kitabın adı mətndə *Rust Proqramlaşdırma Dili* yazılır. İngiliscə *The Rust Programming Language* yalnız çap olunmuş ingiliscə nəşrdən (No Starch Press) danışılanda saxlanılır.
- **Proqramçıların gündəlik dilinə üstünlük verilir**, formal ədəbi dilə yox: *data strukturu* (*verilənlər strukturu* yox), *direktoriya* (*qovluq* yox), *optimizasiya* (*optimallaşdırma* yox). Yeni termin təklif edərkən developerlərin real danışıqda işlətdiyi forma seçilir.

## Terminlər

- Texniki terminlər **yalnız** `GLOSSARY.md`-dən götürülür. Yeni termin lazım olarsa, tərcüməçi onu özü uydurmur: lüğətə `təklif` statuslu sətir əlavə edib insandan soruşur.
- Terminin **hər fəsildə ilk işləndiyi yerdə** ingiliscə qarşılığı mötərizədə verilir: *sahiblik (ownership)*. Eyni fəsildə sonrakı işlənmələrdə yalnız Azərbaycanca.
- **Gündəlik sözlər** (`GLOSSARY.md`-də Qeyd sütununda `[gündəlik]` işarəsi olanlar: quraşdırmaq, brauzer, mötərizələr…) mötərizəsiz yazılır, ilk işlənmədə də. Mötərizə yalnız oxucuya həqiqətən faydalı olduqda, yəni texniki terminlər üçün yazılır.
- **Titul səhifəsi və ön söz** (`title-page.md`, `foreword.md`) texniki mətn deyil: orada heç bir terminə mötərizə yazılmır.
- **Rust-a məxsus terminlər və varlıqlar ingiliscə qalır, Azərbaycanca qarşılığı mötərizədə verilir** (hər fəsildə ilk işlənmədə): *borrow checker (borc yoxlayıcısı)*, *mutable (dəyişə bilən)*. Ümumi proqramlaşdırma terminləri isə Azərbaycanca yazılır, ingiliscəsi mötərizədə: *funksiya (function)*. Hansı terminin hansı qrupa aid olduğunu `GLOSSARY.md` göstərir (`—saxlanılır— (söz)`).
- Tərcümə olunmayan Rust terminləri (`—saxlanılır—`) ingiliscə qalır, Azərbaycan şəkilçiləri **defislə** yazılır: *trait-in*, *crate-ə*, *enum-lar*. Şəkilçi sözün **ingiliscə tələffüzünə** görə seçilir: *crate-i* ("kreyt"), *future-lər* ("fyuçer").
- **İngiliscə terminlər mətndə kursivlə** yazılır: ingiliscə saxlanılan terminlər (*trait*, *crate*, *build*, *Rustacean*…), sadə söz kimi yazılmış açar sözlər (*async*, *await*) və *developer*, *production*, *legacy* kimi ingilis sözləri. Kursiv yalnız sözün özünü əhatə edir, şəkilçi defisdən sonra düz yazılır: *trait*-lər, *developer*-lərin. Mötərizədəki ingiliscə qarşılıqlar (*kod revyusu (code review)*), xüsusi adlar (Rust, Cargo, Git, Linux, Ferris, IDE, API), başlıqlar və kod (`match`) kursivlə yazılmır.
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

## Durğu işarələri

Rəsmi normativ mənbə (AMEA-nın *Azərbaycan dilinin orfoqrafiya qaydaları*, 2017 layihəsi; 1977-ci il *Azərbaycan dilində durğu işarələri*) durğu işarələrini tam əhatə etmir, ona görə qaydalar aşağıdakı mənbələrə əsaslanır: AMEA orfoqrafiya qaydaları layihəsi (edebiyyat-az.com, 2018), az.wikipedia.org “Vergül” və “Dırnaq işarəsi”, Təhsil Nazirliyinin pedaqoji dərsliyi, mir.az “Feili bağlama”.

- **Bağlayıcılar**: *amma, ancaq, lakin, hətta, yəni, çünki* cümlə daxilində özündən əvvəl vergül tələb edir; *ki*-dən sonra vergül qoyulur (*Bilin ki, …*). *və* birləşdirmə bağlayıcısından əvvəl vergül qoyulmur.
- **Ara sözlər** (*məsələn, əslində, beləliklə, ümumiyyətlə, yəqin, görünür, çox güman ki…*): cümlənin əvvəlində sonra, ortasında hər iki tərəfdən vergül. *sanki*, *elə bil* vergülsüz.
- **Şərt budağı** (*-sa/-sə*, *əgər*): budaq cümlədən sonra vergül.
- **Mübtəda *o / bu***: ardınca feildən başqa söz gəlirsə vergül (*O, artıq sizdə var*; *Bu, sizi … edir*); feildən əvvəl vergül yoxdur (*O getdi*). Təyin kimi (*bu gün*, *bu dəfə*) vergülsüz.
- **Feli bağlama**: tərzi-hərəkət / səbəb-məqsəd mənalı feli bağlama tərkibi xəbərdən başqa üzvlərlə ayrılırsa, ondan sonra vergül (*Kompilyatorla birlikdə işləyərək, komanda…*). Bilavasitə xəbərin yanında gəlirsə vergül yoxdur (*`--vcs=git` istifadə edərək dəyişə bilərsiniz*). *-ıb/-ib* həmcins xəbər olduqda (öz tamamlığı ilə ayrıca hərəkət) sonra vergül (*komandasını daxil edib, ona … ötürün*); sıx cüt hərəkətdə (*kompilyasiya edib işə salmaq*) vergül yoxdur. Mənbələr bu sahədə tam razı deyil; bu kitab yuxarıdakı qaydanı izləyir.
- **Dırnaq**: “ ” (ingilis qoşa dırnaq, müasir praktikada əsas forma); daxili sitat üçün ‘ ’. Dırnaqdakı ada artırılan şəkilçi dırnaqdan kənarda yazılır: “Hello, world!” proqramı, “Quraşdırma”nın.
- **Defis**: rəqəm və abreviaturadan sonra şəkilçi defislə (*2-ci*, *1-1-dəki*, *IDE-nin*, *API-ni*); ingiliscə saxlanılan terminlərdən sonra da defis (bax “Terminlər”).
- **Tire**: əlavə izah üçün hər iki tərəfdən boşluqla ( — ).
- Durğu işarələri yeni sətrə keçirilmir.

## Redaktə dərsləri (Girişin yoxlanmasından)

İnsan yoxlamasında edilən düzəlişlərdən çıxan qaydalar. Hər yeni fəsildə tətbiq olunur.

**Cümlə quruluşu**
- Uzun feli sifət / feli bağlama zəncirləri (*…edən …olan …yaradan X*) qısa cümlələrə bölünür; hər cümlədə bir fikir. İngiliscə tire arasındakı izah (*Cargo, the … tool, makes …*) Azərbaycanca ayrıca cümlə olur:
  - ✗ *Cargo — Rust ilə birlikdə gələn build aləti və asılılıqları idarə edən alət — asılılıqları … eyni cür edir.*
  - ✓ *Cargo Rust ilə birlikdə gələn build aləti və asılılıq (dependency) meneceridir. Onun sayəsində asılılıqları … idarə etmək asandır və bütün Rust ekosistemində eyni cür işləyir.*
- Əvvəl məqsəd, sonra vasitə: ✓ *Rust təhlükəsiz kodun eyni zamanda sürətli olmasına çalışır. Bunun üçün o, sıfır xərcli abstraksiyalardan (zero-cost abstractions) istifadə edir: …*
- Vurğulanan üzv xəbərdən əvvəl: ✓ *Rust-da isə nəzarətçi rolunu kompilyator oynayır: …*
- Miqdar sözü sifətlərdən əvvəl: ✓ *Yüzlərlə böyük və kiçik şirkət* (✗ *Böyük və kiçik yüzlərlə şirkət*).
- Eyni söz mübtəda və tamamlıq kimi yan-yana gəlmir (✗ *Rust, Rust proqramlaşdırma dilini…*); geri istinad olunur: ✓ *Rust həm də dilin özünü, icmasını … inkişaf etdirmək istəyən insanlar üçündür.* Adi isim mübtədadan sonra vergül qoyulmur.

**Söz seçimi**
- Hərfi tərcümə yox, mənanın təbii ifadəsi: *stakeholders* → ✗ *maraqlı tərəflər*, ✓ *burada onlardan yalnız ən əsaslarını qeyd etdik*; *hopes to support* → ✓ *faydalı olmağa ümid edir*.
- Kitab dili sözləri yox, sadə sözlər: *ehtiva etmək* → *tərkibində … olmaq*; *gatekeeper* → *nəzarətçi* (✗ *qapıçı*); *assume* → *güman etmək* (✗ *fərz etmək*); *makes no assumptions* → *heç bir fərziyyə irəli sürmür* (✗ *fərziyyə etmir*); *such* → *bu kimi* (✗ *belə*); *build our own implementation of* → *özümüz realizə edəcəyik*.
- Tavtologiya yoxdur: ✗ *inteqrasiya olunmuş inkişaf mühiti … inteqrasiyasını*; ✗ *fərz edir … fərziyyə etmir*; ✗ *səyahəti … səyahəti*.
- Felin idarəsi düzgün: *ümid etmək* + yönlük hal (*olmağa ümid edir*).
- *buraxılış* yalnız *edition* deməkdir; "released" → *çıxmış / çıxıb*.
- Kitabın adı mətndə *Rust Proqramlaşdırma Dili*.

**İngiliscə qarşılıqlar**
- Mötərizə yalnız texniki terminlərə; gündəlik sözlərə (`[gündəlik]`) yox; titul səhifəsi və ön sözdə heç yox.
- Birləşmədə Azərbaycanca əvvəl, ingiliscə terminin içində: *açıq (public) proqramlaşdırma interfeysi*, *daxili (embedded) qurğular*, *asılılıq (dependency) meneceri*.
- Açılmış ingilis abreviaturaları böyük hərflə: *(Integrated Development Environment, IDE)*, *(Application Programming Interface, API)*.
- Mətndəki ingilis terminləri kursivlə, yalnız söz: *trait*-lər; şəkilçi tələffüzə görə (*future*-lər, *closure*-lar — sonuncu insan qərarı).
- Vurğu kursivi Azərbaycan cümləsinin məntiqi vurğusuna düşür: *proqramlaşdırmanın _nə_ olduğu*.

## Başlıqlar

Başlıqlar tərcümə olunur. mdBook lövbərləri başlıqdan yaradıldığı üçün həmin fəsildəki və digər fəsillərdəki `#lövbər` keçidləri yeni lövbərə uyğun yenilənir. `python tools/check_chapter.py` mövcud olmayan lövbərləri tapır. Başlıqda ingiliscə mötərizə yazılmır (ilk işlənmə qaydası mətn hissəsinə aiddir).

## Kod şərhləri

Kod nümunələrindəki şərhlər (`//`, `///`, `//!`, `/* */`) **tərcümə olunur** və lüğətə uyğun yazılır. Yalnız şərh mətni dəyişir: kod, sətir literalları, identifikatorlar dəyişməz qalır. Şərhlər həm fəsil faylındakı ```` ```rust ```` bloklarında, həm də `rustbook-az/listings/` direktoriyasındakı `.rs` fayllarında tərcümə olunur. `python tools/check_listings.py` şərhdən başqa hər fərqi tapır.

## English summary

- Address the reader as *siz*; proper Azerbaijani Latin letters (ə ı ö ü ç ş ğ).
- The book's title in prose is *Rust Proqramlaşdırma Dili*; the English title only when the printed English edition (No Starch Press) is meant.
- Emphasis (italics) goes on the word that carries the stress in the Azerbaijani sentence, not on the literal translation of the English italic word (*what programming is* → *proqramlaşdırmanın _nə_ olduğu*).
- Prefer developers' everyday Azerbaijani over formal literary language (*data strukturu*, *direktoriya*, *optimizasiya*).
- Technical terms only from `GLOSSARY.md`; new term → propose a row, never invent silently.
- General terms: Azerbaijani first, English in parentheses on first use per chapter. Rust-specific terms (borrow checker, ownership, mutable…): English kept, Azerbaijani gloss in parentheses on first use; later uses English only.
- Everyday words (tagged `[gündəlik]` in the glossary's note column) never get English in parentheses; the title page and foreword get no parentheses at all.
- English terms in prose are italic, word only, suffix upright after the hyphen (*trait*-lər, *developer*-lərin); not English in parentheses, names (Rust, Cargo, Git, IDE, API), headings or code.
- Terms kept in English take hyphenated suffixes (*trait-in*, *crate-ə*), chosen by the English pronunciation (*crate-i*, *future-lər*).
- Never touch code, inline code, directives, `<Listing>` attributes (only `caption` text is translated), link targets (only `#anchor` follows translated headings), `<!-- ignore -->`, ANCHOR lines, `output.txt`.
- Notes: `> Note: ` becomes exactly `> Qeyd: ` (rendered as a note box by `tools/az_note.py`).
- Punctuation: see “Durğu işarələri” (comma before amma/lakin/çünki/yəni, after ki and -sa clauses, after detached converb phrases; “ ” quotes with suffixes outside; hyphen after numbers/abbreviations).
- Lessons from the introduction review (split long participle chains, no literal or bookish wording, no tautology, quantifier before adjectives, Title Case for spelled-out abbreviations, Azerbaijani first in phrases like *açıq (public) …*): see “Redaktə dərsləri”.
- Compiler output stays English; the prose around it is translated. Comments in code listings are translated.
