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

## Yeni təkliflər: ön söz, giriş və 1-ci fəsil (Task 9)

| English | Azərbaycanca | Qeyd | Status |
| ------- | ------------ | ---- | ------ |
| build | —saxlanılır— | Proqramçılar belə deyir: *build etmək*, *debug build-i*, *build sistemi*, *build aləti*. Alternativ: *yığmaq / yığım*. | təsdiqlənib |
| compile | kompilyasiya etmək | İsim: *kompilyasiya*. `compiler` → *kompilyator* ilə uyğundur. | təsdiqlənib |
| package manager | paket meneceri | Cargo: "Rust-ın paket meneceri və build sistemi". | təsdiqlənib |
| dependency | asılılıq | *asılılıqlar*; "kodunuzun asılı olduğu kitabxanalar". | təsdiqlənib |
| executable | icra olunan fayl | "binary executable" → *icra olunan binar fayl*. | təsdiqlənib |
| binary | binar fayl | Kontekstdə sadəcə *binar*: "binar faylı işə salmaq". Gələcəkdə *binary crate* → *binar crate*. | təsdiqlənib |
| source code | mənbə kodu | *source file* → *mənbə faylı*. Alternativ: *qaynaq kodu*. | təsdiqlənib |
| release | reliz | *reliz üçün build*, *reliz profili*. "yeni versiya" kimi adi mənada *versiya* (*buraxılış* edition üçündür). | təsdiqlənib |
| debug | —saxlanılır— | *debug build-i*, *debug məlumatı*. Alternativ: *sazlama*. | təsdiqlənib |
| optimization | optimizasiya | optimizasiya etmək, optimizasiya olunmuş | təsdiqlənib |
| profile | profil | Cargo profili: *dev*, *release*. | təsdiqlənib |
| stable | stabil | *stabil versiya*. Alternativ: *sabit* (amma *sabit* = constant). | təsdiqlənib |
| edition | buraxılış | Rust-ın buraxılışları (2015, 2018, 2021, 2024): *Rust-ın 2015 il buraxılışı*, *2024 buraxılışı*. `edition` açarı kod kimi qalır. Kitabın nəşri isə *nəşr*. | təsdiqlənib |
| memory | yaddaş | | təsdiqlənib |
| memory safety | yaddaş təhlükəsizliyi | | təsdiqlənib |
| systems programming | sistem proqramlaşdırması | | təsdiqlənib |
| low-level | aşağı səviyyəli | *high-level* → *yüksək səviyyəli*. | təsdiqlənib |
| zero-cost abstraction | sıfır xərcli abstraksiya | | təsdiqlənib |
| concurrency | —saxlanılır— (eyni vaxtlılıq) | Proqramçılara tanış termindir; lazım olduqda kontekstdə izah edilir: *concurrency-ni*, *concurrent proqramlaşdırma*. 16-cı fəsildə *paralellik* (parallelism) ilə fərqləndirilir. | təsdiqlənib |
| parallelism | paralellik | *concurrency*-dən fərqli anlayışdır. | təsdiqlənib |
| standard library | standart kitabxana | | təsdiqlənib |
| application programming interface (API) | proqramlaşdırma interfeysi (API) | İlk dəfədən sonra sadəcə *API*. | təsdiqlənib |
| integrated development environment (IDE) | inteqrasiya olunmuş inkişaf mühiti (IDE) | İlk dəfədən sonra sadəcə *IDE*. | təsdiqlənib |
| shell | —saxlanılır— | *shell-də*. Kitab *terminal* və *shell* sözlərini yanaşı işlədir; *terminal* yazılışı eynidir. | təsdiqlənib |
| linker | —saxlanılır— | Alternativ: *əlaqələndirici* (akademik səslənir). | təsdiqlənib |
| flag | —saxlanılır— (bayraq) | Komanda sətri flag-i: `--vcs` flag-i, `--release` flag-i ilə. | təsdiqlənib |
| Rustacean | —saxlanılır— | Rust icmasının özünə verdiyi zarafatyana ad: *Rustacean-lar*. | təsdiqlənib |
| version control system | versiya nəzarəti sistemi | | təsdiqlənib |
| repository | repozitoriya | README-də artıq işlədilib. | təsdiqlənib |
| bug | baq | Proqramçı dilində *baq*; *xəta* (error) ilə fərqləndirilir. Alternativ: *səhv*. | təsdiqlənib |
| error message | xəta mesajı | *warning* → *xəbərdarlıq*. | təsdiqlənib |
| refactoring | refaktorinq | | təsdiqlənib |
| code review | —saxlanılır— | *code review-da*, *code review zamanı*. | təsdiqlənib |
| open source | açıq mənbə | *açıq mənbəli layihələr*. | təsdiqlənib |
| implementation | realizasiya | Fel: *realizə etmək*. Vacibdir: 5-ci və 10-cu fəsillərdə *implement a trait* → *trait-i realizə etmək*. Alternativ: *implementasiya*. | təsdiqlənib |
| syntax | sintaksis | | təsdiqlənib |
| declaration | elan | "funksiyanı elan etmək". | təsdiqlənib |
| function body | funksiyanın gövdəsi | *gövdə*. | təsdiqlənib |
| data structure | data strukturu | Proqramçıların gündəlik dilinə yaxın forma. | təsdiqlənib |
| collection | kolleksiya | | təsdiqlənib |
| control flow | idarəetmə axını | | təsdiqlənib |
| functional programming | funksional proqramlaşdırma | | təsdiqlənib |
| object-oriented programming | obyektyönümlü proqramlaşdırma | | təsdiqlənib |
| privacy | məxfilik | 7-ci fəsil: *məxfilik qaydaları*. | təsdiqlənib |
| public | —saxlanılır— (açıq) | `pub`. *public API* → *public (açıq) API*. | təsdiqlənib |
| private | —saxlanılır— (gizli) | | təsdiqlənib |
| future | —saxlanılır— | 17-ci fəsil (`Future` trait-i). Girişdə yalnız adı çəkilir. | təsdiqlənib |
| stream | —saxlanılır— | 17-ci fəsil. | təsdiqlənib |
| task | —saxlanılır— | 17-ci fəsildə async task. Adi mənada *tapşırıq*. | təsdiqlənib |
| unsafe Rust | —saxlanılır— | | təsdiqlənib |
| nightly Rust | —saxlanılır— | | təsdiqlənib |
| derivable trait | derive edilə bilən trait | `#[derive]` atributu ilə. | təsdiqlənib |
| ahead-of-time compiled | əvvəlcədən kompilyasiya olunan | | təsdiqlənib |
| cache | keş | | təsdiqlənib |

## Yeni təkliflər 2: 1-ci fəsil üçün əlavə terminlər (Task 9)

| English | Azərbaycanca | Qeyd | Status |
| ------- | ------------ | ---- | ------ |
| install | quraşdırmaq | *quraşdırma* (installation), *quraşdırılıb* (installed), *installer* → *quraşdırıcı*. *yükləmək* yalnız download üçündür; ikisi eyni cümlədə ayrı addımlardır. | təsdiqlənib |
| uninstall | silmək | "Rust-ı silmək". | təklif |
| update | yeniləmək | *yeniləmə*. | təklif |
| download | yükləmək | İnternetdən götürmək: *yükləmə*, *yüklənmiş*. Install mənasında işlədilmir (bax *quraşdırmaq*). | təsdiqlənib |
| operating system | əməliyyat sistemi | | təklif |
| documentation | dokumentasiya | Proqramçı dili. Alternativ: *sənədlər*. | təklif |
| script | skript | | təklif |
| text editor | mətn redaktoru | | təklif |
| configuration | konfiqurasiya | *konfiqurasiya faylı*. | təklif |
| output | çıxış | Proqramın/komandanın çıxışı. STYLE.md-də artıq işlədilib. | təklif |
| prompt | —saxlanılır— | Komanda sətri prompt-u (`$`). Alternativ: *dəvət*. | təklif |
| file extension | genişlənmə | *.rs genişlənməsi*. Alternativ: *uzantı*. | təklif |
| home directory | ev direktoriyası | | təklif |
| top-level directory | kök direktoriya | Layihənin kök direktoriyası. | təklif |
| underscore | alt xətt | `_`. | təklif |
| semicolon | nöqtəli vergül | `;`. | təklif |
| curly brackets | fiqurlu mötərizələr | `{}`. | təklif |
| parentheses | mötərizələr | `()`; dəqiqlik lazımdırsa *dairəvi mötərizələr*. | təklif |
| ecosystem | ekosistem | | təklif |
| tool | alət | *tooling* → *alətlər*. *build tool* → *build aləti*. | təklif |
| formatter | formatlama aləti | *format* (fel) → *formatlamaq*. | təklif |
| code completion | kodun avtomatik tamamlanması | | təklif |
| developer | developer | Proqramçılar özləri belə deyir: *developer-lər*. *programmer* → *proqramçı*. Alternativ: hər ikisi *proqramçı*. | təklif |
| software | proqram təminatı | | təklif |
| production | production | "production-da işlətmək". Alternativ: *real istifadə mühiti*. | təklif |
| web server | veb server | | təklif |
| web service | veb servis | | təklif |
| browser | brauzer | | təklif |
| multithreaded | çox thread-li | *thread* ilə uyğundur. *single-threaded* → *tək thread-li*. | təklif |
| async / await | —saxlanılır— | `async`/`await` açar sözləri; anlayış kimi də ingiliscə. *asynchronous programming* → *asinxron proqramlaşdırma*. | təklif |
| idiom | idiom | Rust idiomları. | təklif |
| operator | operator | Yazılışı eynidir. | təklif |
| network | şəbəkə | | təklif |
| system variable | sistem dəyişəni | `%PATH%`. *environment variable* → *mühit dəyişəni* (12-ci fəsil). | təklif |
| commit hash | commit heşi | Git commit-i: *commit-in*. | təklif |
| dynamic language | dinamik dil | Ruby, Python, JavaScript. | təklif |
| legacy code | köhnə kod | Alternativ: *legacy kod*. | təklif |
| contribute | töhfə vermək | *contributor* → *töhfə verən*. | təklif |
| machine learning | maşın öyrənməsi | | təklif |
| embedded device | embedded qurğu | Alternativ: *daxili sistem qurğusu*. | təklif |
| Internet of Things | Əşyaların İnterneti | | təklif |
| benchmark | —saxlanılır— | *benchmark etmək*. Alternativ: *performans ölçümü*. | təklif |
| troubleshooting | problemlərin həlli | 1.1 bölməsinin başlığı. | təklif |
