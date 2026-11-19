# Terminlər lüğəti / Glossary

Hər ingilis texniki termininin **bir** Azərbaycanca qarşılığı var və bütün fəsillərdə yalnız o işlədilir
(bax `STYLE.md`, `.claude/skills/rust-book-az/SKILL.md`). Cədvəl `tools/glossary.py` ilə yoxlanılır və
`rustbook-az/src/appendix-08-glossary.md` əlavəsi buradan yaradılır.

- **Status**: `təklif` – Claude-un təklifi, hələ yoxlanılmayıb; `təsdiqlənib` – insan tərəfindən təsdiqlənib.
- **`—saxlanılır—`** – termin ingiliscə qalır və Azərbaycan şəkilçiləri defislə yazılır (*trait-in*, *crate-ə*).
- Terminin ilk işləndiyi yerdə (hər fəsildə) ingiliscə qarşılığı mötərizədə verilir: *sahiblik (ownership)*.
- **Rust-a məxsus terminlər və varlıqlar** ingiliscə qalır, Azərbaycanca qarşılığı mötərizədə verilir (*borrow checker (borc yoxlayıcısı)*). Ümumi proqramlaşdırma terminləri (funksiya, massiv, kompilyator…) Azərbaycanca yazılır.
- `—saxlanılır— (söz)` – termin ingiliscə qalır, ilk işlənmədə Azərbaycanca qarşılığı mötərizədə verilir: *mutable (dəyişə bilən)*.
- Eyni yazılışlı terminlər (iterator, variant, test) mötərizəsiz yazılır, çünki ingiliscə ilə eynidir.
- Kod bloklarında, sətirdaxili kodda və Rust açar sözlərində heç nə dəyişdirilmir.
- `Qeyd` sütununda qeyri-müəyyən yerlər və alternativlər göstərilir.

| English | Azərbaycanca | Qeyd | Status |
| ------- | ------------ | ---- | ------ |
| variable | dəyişən | Hamının işlətdiyi termin. | təklif |
| mutable | —saxlanılır— (dəyişə bilən) | `mut`. İngiliscə qalır, ilk işlənmədə Azərbaycanca qarşılığı mötərizədə verilir: *mutable (dəyişə bilən)*. | təsdiqlənib |
| immutable | —saxlanılır— (dəyişə bilməyən) | İngiliscə qalır: *immutable (dəyişə bilməyən)*. Rust-da dəyişənlər defolt olaraq belədir. | təsdiqlənib |
| mutability | —saxlanılır— (dəyişə bilmə) | İngiliscə qalır, çünki *mutable*/*immutable* də belədir. 3-cü fəsil başlığı: "Mutability (dəyişə bilmə)". | təklif |
| constant | sabit | `const`. | təklif |
| shadowing | —saxlanılır— (kölgələmə) | Rust-a məxsus: eyni adlı yeni dəyişənin köhnəsini "kölgədə qoyması". | təklif |
| function | funksiya | | təklif |
| parameter | parametr | Funksiya təsvirindəki ad. | təklif |
| argument | arqument | Funksiyaya verilən real dəyər. | təklif |
| return value | qaytarılan dəyər | | təklif |
| statement | bəyanat | `let y = 6;` kimi dəyər qaytarmayan konstruksiya. *ifadə* yalnız expression üçündür. | təsdiqlənib |
| expression | ifadə | Dəyər qaytaran konstruksiya. | təklif |
| value | dəyər | | təklif |
| ownership | —saxlanılır— (sahiblik) | Rust-a məxsus anlayış: *ownership (sahiblik)*. | təklif |
| move | ötürmə | *Köçürmə* seçilmədi, çünki Azərbaycan IT dilində "copy" mənasında da işlənir. Alternativ: *daşıma*. | təklif |
| clone | klonlama | `clone` metodu. | təklif |
| copy | kopyalama | `Copy` trait-i; *klonlama*-dan fərqli anlayışdır. | təklif |
| drop | drop | `Drop` trait-i və `drop` funksiyası adlarıdır; anlayış kimi də ingiliscə işlədilir. Alternativ: *təmizləmə*. | təklif |
| borrowing | —saxlanılır— (borc alma) | Rust-a məxsus anlayış. Alternativ gloss: *borc götürmə*. | təklif |
| borrow checker | —saxlanılır— (borc yoxlayıcısı) | Rust-a məxsus: *borrow checker (borc yoxlayıcısı)*. | təsdiqlənib |
| reference | istinad | Alternativ: *referans*. Göstərici (pointer) ilə qarışdırılmamalıdır. | təklif |
| mutable reference | —saxlanılır— (dəyişə bilən istinad) | Rust-a məxsus; *mutable (dəyişə bilən)* ilə uyğundur. | təklif |
| dangling reference | —saxlanılır— (boşda qalan istinad) | Rust-a məxsus: *dangling reference (boşda qalan istinad)*. Boşalmış yaddaşa işarə edən istinad. | təsdiqlənib |
| slice | dilim | Python-un Azərbaycanca sənədlərindəki "dilimləmə" ilə üst-üstə düşür. | təklif |
| string | sətir | `String` və `&str` tipləri kodda olduğu kimi qalır. | təklif |
| struct | struktur | `struct` açar sözü kodda qalır. | təklif |
| field | sahə | Struktur sahəsi. | təklif |
| method | metod | | təklif |
| associated function | —saxlanılır— (əlaqəli funksiya) | Rust-a məxsus: *associated function (əlaqəli funksiya)*. | təsdiqlənib |
| enum | —saxlanılır— | Azərbaycan proqramçıları ingiliscə deyir: *enum-un*, *enum-lar*. Alternativ: *sayma tipi*. | təklif |
| variant | variant | Enum-un variantı. Yazılışı ingiliscə ilə eynidir. | təklif |
| pattern | şablon | Alternativ: *nümunə*. | təklif |
| pattern matching | şablon uyğunlaşdırılması | *şablon* (pattern) sözü ilə uyğundur. | təsdiqlənib |
| match | —saxlanılır— | `match` açar sözü: *match ifadəsi*. | təklif |
| crate | —saxlanılır— | Dizayn sənədində nümunə kimi göstərilib: *crate-ə*. | təklif |
| package | paket | Cargo paketi. | təklif |
| module | modul | | təklif |
| path | yol | Modul yolu. Fayl yolu da *yol*-dur; kontekstdən aydın olur. | təklif |
| scope | əhatə dairəsi | Alternativ: *görünmə sahəsi*. *sahə* (field) ilə qarışmasın deyə seçilməyib. | təklif |
| vector | vektor | `Vec<T>`. | təklif |
| hash map | heş cədvəli | `HashMap<K, V>`. Alternativ: ingiliscə saxlamaq. | təklif |
| array | massiv | | təklif |
| tuple | —saxlanılır— | Tərcümə olunmur: *tuple-lar*, *tuple-ın*. | təsdiqlənib |
| error | xəta | | təklif |
| recoverable error | bərpa olunan xəta | `Result`. | təklif |
| unrecoverable error | bərpa olunmayan xəta | `panic!`. | təklif |
| panic | —saxlanılır— | Termin kimi ingiliscə qalır (*panic-lər*, `panic!` makrosu). Mətndə anlayışı izah edərkən adi dildə *panika* sözündən istifadə etmək olar (məs. "proqram panikaya düşür"), amma termin özü *panic* yazılır. | təsdiqlənib |
| generic | —saxlanılır— | Tərcümə olunmur: *generic-lər*, *generic-ə*. | təsdiqlənib |
| trait | —saxlanılır— | Dizayn sənədində nümunə kimi göstərilib: *trait-in*. | təklif |
| trait bound | —saxlanılır— (trait məhdudiyyəti) | Rust-a məxsus. | təklif |
| lifetime | —saxlanılır— (ömür müddəti) | Rust-a məxsus; `'a` kimi annotasiyalar kodda qalır. | təklif |
| closure | —saxlanılır— | Tərcümə olunmur: *closure-lar*, *closure-ın*. Türk tərcüməsində bu termin *kapanma/kapanış/kapama* kimi üç cür verilmişdi; ingiliscə saxlamaq bu problemi aradan qaldırır. | təsdiqlənib |
| iterator | iterator | Yazılışı ingiliscə ilə eynidir. | təklif |
| smart pointer | ağıllı göstərici | | təklif |
| thread | —saxlanılır— | Tərcümə olunmur: *thread-lər*, *thread-in*. *axın* (stream ilə qarışır) və *iplik* işlənmədiyi üçün seçilmədi. | təsdiqlənib |
| compiler | kompilyator | | təklif |
| stack | stek | *heap* ilə qarışmasın (Türk tərcüməsində ikisi də *yığın* idi). Alternativ: *yığın*. | təklif |
| heap | —saxlanılır— | *stek*-dən fərqli: *heap-də*. Alternativ: *yığın*; seçilsə *stack* üçün *stek* qalır. | təklif |
| type | tip | | təklif |
| integer | tam ədəd | | təklif |
| floating-point number | üzən nöqtəli ədəd | Alternativ: *həqiqi ədəd*. | təklif |
| macro | makro | | təklif |
| attribute | atribut | `#[derive(...)]` və s. | təklif |
| test | test | Yazılışı ingiliscə ilə eynidir. | təklif |
| keyword | açar söz | | təklif |
| loop | dövr | | təklif |
| branch | budaq | `if` budaqları. | təklif |
| comment | şərh | | təklif |
| library | kitabxana | | təklif |
| command line | komanda sətri | | təklif |
| directory | direktoriya | Fayl sistemi direktoriyası; ingiliscə "folder" də bu sözlə tərcümə olunur (*qovluq* yox: proqramçılar *direktoriya* deyir). Kitabın bütün mətnində və README-də bu işlədilir. `cd`, `mkdir` kimi əmrlər kodda qalır. | təsdiqlənib |
