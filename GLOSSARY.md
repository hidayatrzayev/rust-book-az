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
| variable | dəyişən | Hamının işlətdiyi termin. | təsdiqlənib |
| mutable | —saxlanılır— (dəyişə bilən) | `mut`. İngiliscə qalır, ilk işlənmədə Azərbaycanca qarşılığı mötərizədə verilir: *mutable (dəyişə bilən)*. | təsdiqlənib |
| immutable | —saxlanılır— (dəyişə bilməyən) | İngiliscə qalır: *immutable (dəyişə bilməyən)*. Rust-da dəyişənlər defolt olaraq belədir. | təsdiqlənib |
| mutability | —saxlanılır— (dəyişə bilmə) | İngiliscə qalır, çünki *mutable*/*immutable* də belədir. 3-cü fəsil başlığı: "Mutability (dəyişə bilmə)". | təsdiqlənib |
| constant | sabit | `const`. | təsdiqlənib |
| shadowing | —saxlanılır— (kölgələmə) | Rust-a məxsus: eyni adlı yeni dəyişənin köhnəsini "kölgədə qoyması". | təsdiqlənib |
| function | funksiya | | təsdiqlənib |
| parameter | parametr | Funksiya təsvirindəki ad. | təsdiqlənib |
| argument | arqument | Funksiyaya verilən real dəyər. | təsdiqlənib |
| return value | qaytarılan dəyər | | təsdiqlənib |
| statement | bəyanat | `let y = 6;` kimi dəyər qaytarmayan konstruksiya. *ifadə* yalnız expression üçündür. | təsdiqlənib |
| expression | ifadə | Dəyər qaytaran konstruksiya. | təsdiqlənib |
| value | dəyər | | təsdiqlənib |
| ownership | —saxlanılır— (sahiblik) | Rust-a məxsus anlayış: *ownership (sahiblik)*. | təsdiqlənib |
| move | ötürmə | *Köçürmə* seçilmədi, çünki Azərbaycan IT dilində "copy" mənasında da işlənir. Alternativ: *daşıma*. | təsdiqlənib |
| clone | klonlama | `clone` metodu. | təsdiqlənib |
| copy | kopyalama | `Copy` trait-i; *klonlama*-dan fərqli anlayışdır. | təsdiqlənib |
| drop | drop | `Drop` trait-i və `drop` funksiyası adlarıdır; anlayış kimi də ingiliscə işlədilir. Alternativ: *təmizləmə*. | təsdiqlənib |
| borrowing | —saxlanılır— (borc alma) | Rust-a məxsus anlayış. Alternativ gloss: *borc götürmə*. | təsdiqlənib |
| borrow checker | —saxlanılır— (borc yoxlayıcısı) | Rust-a məxsus: *borrow checker (borc yoxlayıcısı)*. | təsdiqlənib |
| reference | istinad | Alternativ: *referans*. Göstərici (pointer) ilə qarışdırılmamalıdır. | təsdiqlənib |
| mutable reference | —saxlanılır— (dəyişə bilən istinad) | Rust-a məxsus; *mutable (dəyişə bilən)* ilə uyğundur. | təsdiqlənib |
| dangling reference | —saxlanılır— (boşda qalan istinad) | Rust-a məxsus: *dangling reference (boşda qalan istinad)*. Boşalmış yaddaşa işarə edən istinad. | təsdiqlənib |
| slice | dilim | Python-un Azərbaycanca sənədlərindəki "dilimləmə" ilə üst-üstə düşür. | təsdiqlənib |
| string | sətir | `String` və `&str` tipləri kodda olduğu kimi qalır. | təsdiqlənib |
| struct | struktur | `struct` açar sözü kodda qalır. | təsdiqlənib |
| field | sahə | Struktur sahəsi. | təsdiqlənib |
| method | metod | | təsdiqlənib |
| associated function | —saxlanılır— (əlaqəli funksiya) | Rust-a məxsus: *associated function (əlaqəli funksiya)*. | təsdiqlənib |
| enum | —saxlanılır— | Azərbaycan proqramçıları ingiliscə deyir: *enum-un*, *enum-lar*. Alternativ: *sayma tipi*. | təsdiqlənib |
| variant | variant | Enum-un variantı. Yazılışı ingiliscə ilə eynidir. | təsdiqlənib |
| pattern | şablon | Alternativ: *nümunə*. | təsdiqlənib |
| pattern matching | şablon uyğunlaşdırılması | *şablon* (pattern) sözü ilə uyğundur. | təsdiqlənib |
| match | —saxlanılır— | `match` açar sözü: *match ifadəsi*. | təsdiqlənib |
| crate | —saxlanılır— | Dizayn sənədində nümunə kimi göstərilib: *crate-ə*. | təsdiqlənib |
| package | paket | Cargo paketi. | təsdiqlənib |
| module | modul | | təsdiqlənib |
| path | yol | Modul yolu. Fayl yolu da *yol*-dur; kontekstdən aydın olur. | təsdiqlənib |
| scope | əhatə dairəsi | Alternativ: *görünmə sahəsi*. *sahə* (field) ilə qarışmasın deyə seçilməyib. | təsdiqlənib |
| vector | vektor | `Vec<T>`. | təsdiqlənib |
| hash map | heş cədvəli | `HashMap<K, V>`. Alternativ: ingiliscə saxlamaq. | təsdiqlənib |
| array | massiv | | təsdiqlənib |
| tuple | —saxlanılır— | Tərcümə olunmur: *tuple-lar*, *tuple-ın*. | təsdiqlənib |
| error | xəta | | təsdiqlənib |
| recoverable error | bərpa olunan xəta | `Result`. | təsdiqlənib |
| unrecoverable error | bərpa olunmayan xəta | `panic!`. | təsdiqlənib |
| panic | —saxlanılır— | Termin kimi ingiliscə qalır (*panic-lər*, `panic!` makrosu). Mətndə anlayışı izah edərkən adi dildə *panika* sözündən istifadə etmək olar (məs. "proqram panikaya düşür"), amma termin özü *panic* yazılır. | təsdiqlənib |
| generic | —saxlanılır— | Tərcümə olunmur: *generic-lər*, *generic-ə*. | təsdiqlənib |
| trait | —saxlanılır— | Dizayn sənədində nümunə kimi göstərilib: *trait-in*. | təsdiqlənib |
| trait bound | —saxlanılır— (trait məhdudiyyəti) | Rust-a məxsus. | təsdiqlənib |
| lifetime | —saxlanılır— (ömür müddəti) | Rust-a məxsus; `'a` kimi annotasiyalar kodda qalır. | təsdiqlənib |
| closure | —saxlanılır— | Tərcümə olunmur: *closure-lar*, *closure-ın*. Türk tərcüməsində bu termin *kapanma/kapanış/kapama* kimi üç cür verilmişdi; ingiliscə saxlamaq bu problemi aradan qaldırır. | təsdiqlənib |
| iterator | iterator | Yazılışı ingiliscə ilə eynidir. | təsdiqlənib |
| smart pointer | ağıllı göstərici | | təsdiqlənib |
| thread | —saxlanılır— | Tərcümə olunmur: *thread-lər*, *thread-in*. *axın* (stream ilə qarışır) və *iplik* işlənmədiyi üçün seçilmədi. | təsdiqlənib |
| compiler | kompilyator | | təsdiqlənib |
| stack | —saxlanılır— | Tərcümə olunmur: *stack-də*, *stack-dən*. Kontekstdə bunun yaddaşa aid olduğu izah edilir (məs. "yaddaşın stack hissəsi"). *heap* ilə qarışmır (Türk tərcüməsində ikisi də *yığın* idi). | təsdiqlənib |
| heap | —saxlanılır— | *stack*-dən fərqli: *heap-də*. Kontekstdə yaddaşa aid olduğu izah edilir. | təsdiqlənib |
| type | tip | | təsdiqlənib |
| integer | tam ədəd | | təsdiqlənib |
| floating-point number | üzən nöqtəli ədəd | Alternativ: *həqiqi ədəd*. | təsdiqlənib |
| macro | makro | `println!`, `vec!` kimi makroların adları kodda qalır. | təsdiqlənib |
| attribute | atribut | `#[derive(...)]` və s. | təsdiqlənib |
| test | test | Yazılışı ingiliscə ilə eynidir. | təsdiqlənib |
| keyword | açar söz | | təsdiqlənib |
| loop | dövr | | təsdiqlənib |
| branch | budaq | `if` budaqları. | təsdiqlənib |
| comment | şərh | | təsdiqlənib |
| library | kitabxana | | təsdiqlənib |
| command line | komanda sətri | | təsdiqlənib |
| directory | direktoriya | Fayl sistemi direktoriyası; ingiliscə "folder" də bu sözlə tərcümə olunur (*qovluq* yox: proqramçılar *direktoriya* deyir). Kitabın bütün mətnində və README-də bu işlədilir. `cd`, `mkdir` kimi əmrlər kodda qalır. | təsdiqlənib |
