# Terminlər lüğəti / Glossary

Hər ingilis texniki termininin **bir** Azərbaycanca qarşılığı var və bütün fəsillərdə yalnız o işlədilir
(bax `STYLE.md`, `.claude/skills/rust-book-az/SKILL.md`). Cədvəl `tools/glossary.py` ilə yoxlanılır və
`rustbook-az/src/appendix-08-glossary.md` əlavəsi buradan yaradılır.

- **Status**: `təklif` – Claude-un təklifi, hələ yoxlanılmayıb; `təsdiqlənib` – insan tərəfindən təsdiqlənib.
- **`—saxlanılır—`** – termin ingiliscə qalır və Azərbaycan şəkilçiləri defislə yazılır (*trait-in*, *crate-ə*).
- Terminin ilk işləndiyi yerdə (hər fəsildə) ingiliscə qarşılığı mötərizədə verilir: *sahiblik (ownership)*.
- Eyni yazılışlı terminlər (iterator, variant, test) mötərizəsiz yazılır, çünki ingiliscə ilə eynidir.
- Kod bloklarında, sətirdaxili kodda və Rust açar sözlərində heç nə dəyişdirilmir.
- `Qeyd` sütununda qeyri-müəyyən yerlər və alternativlər göstərilir.

| English | Azərbaycanca | Qeyd | Status |
| ------- | ------------ | ---- | ------ |
| variable | dəyişən | Hamının işlətdiyi termin. | təklif |
| mutable | dəyişkən | `mut`. *Dəyişən* ilə çox oxşardır, qarışıqlıq ola bilər. Alternativ: *dəyişdirilə bilən*. | təklif |
| immutable | dəyişməz | Rust-da dəyişənlər defolt olaraq belədir. | təklif |
| mutability | dəyişkənlik | 3-cü fəsil başlığı: "Dəyişənlər və Dəyişkənlik". | təklif |
| constant | sabit | `const`. | təklif |
| shadowing | kölgələmə | Eyni adlı yeni dəyişənin köhnəsini "kölgədə qoyması". | təklif |
| function | funksiya | | təklif |
| parameter | parametr | Funksiya təsvirindəki ad. | təklif |
| argument | arqument | Funksiyaya verilən real dəyər. | təklif |
| return value | qaytarılan dəyər | | təklif |
| statement | əmr | Qeyri-müəyyən: *əmr* sözü "command" kimi də anlaşılır. Alternativlər: *təlimat*, *deyim*. *ifadə* yalnız expression üçündür. | təklif |
| expression | ifadə | Dəyər qaytaran konstruksiya. | təklif |
| value | dəyər | | təklif |
| ownership | sahiblik | Rust-ın əsas anlayışı. | təklif |
| move | ötürmə | *Köçürmə* seçilmədi, çünki Azərbaycan IT dilində "copy" mənasında da işlənir. Alternativ: *daşıma*. | təklif |
| clone | klonlama | `clone` metodu. | təklif |
| copy | kopyalama | `Copy` trait-i; *klonlama*-dan fərqli anlayışdır. | təklif |
| drop | drop | `Drop` trait-i və `drop` funksiyası adlarıdır; anlayış kimi də ingiliscə işlədilir. Alternativ: *təmizləmə*. | təklif |
| borrowing | borc alma | Qeyri-müəyyən. Alternativ: *borc götürmə*. | təklif |
| borrow checker | borc yoxlayıcısı | Alternativ: ingiliscə saxlamaq (*borrow checker-in*). | təklif |
| reference | istinad | Alternativ: *referans*. Göstərici (pointer) ilə qarışdırılmamalıdır. | təklif |
| mutable reference | dəyişkən istinad | | təklif |
| dangling reference | sallanan istinad | Boşalmış yaddaşa işarə edən istinad. Alternativ: *etibarsız istinad*. | təklif |
| slice | dilim | Python-un Azərbaycanca sənədlərindəki "dilimləmə" ilə üst-üstə düşür. | təklif |
| string | sətir | `String` və `&str` tipləri kodda olduğu kimi qalır. | təklif |
| struct | struktur | `struct` açar sözü kodda qalır. | təklif |
| field | sahə | Struktur sahəsi. | təklif |
| method | metod | | təklif |
| associated function | assosiasiyalı funksiya | Qeyri-müəyyən. Alternativ: *əlaqəli funksiya*. | təklif |
| enum | —saxlanılır— | Azərbaycan proqramçıları ingiliscə deyir: *enum-un*, *enum-lar*. Alternativ: *sayma tipi*. | təklif |
| variant | variant | Enum-un variantı. Yazılışı ingiliscə ilə eynidir. | təklif |
| pattern | şablon | Alternativ: *nümunə*. | təklif |
| pattern matching | şablonla uyğunlaşdırma | | təklif |
| match | —saxlanılır— | `match` açar sözü: *match ifadəsi*. | təklif |
| crate | —saxlanılır— | Dizayn sənədində nümunə kimi göstərilib: *crate-ə*. | təklif |
| package | paket | Cargo paketi. | təklif |
| module | modul | | təklif |
| path | yol | Modul yolu. Fayl yolu da *yol*-dur; kontekstdən aydın olur. | təklif |
| scope | əhatə dairəsi | Alternativ: *görünmə sahəsi*. *sahə* (field) ilə qarışmasın deyə seçilməyib. | təklif |
| vector | vektor | `Vec<T>`. | təklif |
| hash map | heş cədvəli | `HashMap<K, V>`. Alternativ: ingiliscə saxlamaq. | təklif |
| array | massiv | | təklif |
| tuple | kortej | Azərbaycan dilindəki Python mənbələrində belə işlənir. | təklif |
| error | xəta | | təklif |
| recoverable error | bərpa olunan xəta | `Result`. | təklif |
| unrecoverable error | bərpa olunmayan xəta | `panic!`. | təklif |
| panic | panika | | təklif |
| generic | generik | Alternativ: *ümumiləşdirilmiş*. | təklif |
| trait | —saxlanılır— | Dizayn sənədində nümunə kimi göstərilib: *trait-in*. | təklif |
| trait bound | trait məhdudiyyəti | | təklif |
| lifetime | ömür müddəti | Alternativ: ingiliscə saxlamaq. | təklif |
| closure | qapanma | Qeyri-müəyyən. Türk tərcüməsinin əsas problemi bu termindəki dəyişkənlik idi, ona görə bir qarşılıq seçilməlidir. Alternativ: ingiliscə saxlamaq (*closure-ın*). | təklif |
| iterator | iterator | Yazılışı ingiliscə ilə eynidir. | təklif |
| smart pointer | ağıllı göstərici | | təklif |
| thread | —saxlanılır— | *axın* (stream ilə qarışır) seçilmədi, *iplik* isə praktikada işlənmir: *thread-lər*. | təklif |
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
