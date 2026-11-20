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
- Qeyddə **`[gündəlik]`** işarəsi: gündəlik sözdür, ilk işlənmədə də ingiliscə mötərizə yazılmır (*quraşdırmaq*, *brauzer*).

| English | Azərbaycanca | Qeyd | Status |
| ------- | ------------ | ---- | ------ |
| variable | dəyişən | Hamının işlətdiyi termin. | təsdiqlənib |
| mutable | —saxlanılır— (dəyişə bilən) | `mut`. İngiliscə qalır, ilk işlənmədə Azərbaycanca qarşılığı mötərizədə verilir: *mutable (dəyişə bilən)*. | təsdiqlənib |
| immutable | —saxlanılır— (dəyişə bilməyən) | İngiliscə qalır: *immutable (dəyişə bilməyən)*. Rust-da dəyişənlər defolt olaraq belədir. | təsdiqlənib |
| mutability | —saxlanılır— (dəyişə bilmə) | İngiliscə qalır, çünki *mutable*/*immutable* də belədir. 3-cü fəsil başlığı: "Mutability (dəyişə bilmə)". | təsdiqlənib |
| constant | sabit | `const`. | təsdiqlənib |
| shadowing | —saxlanılır— (kölgələmə) | Rust-a məxsus: eyni adlı yeni dəyişənin köhnəsini "kölgədə qoyması". | təsdiqlənib |
| function | funksiya | [gündəlik] | təsdiqlənib |
| parameter | parametr | [gündəlik] Funksiya təsvirindəki ad. | təsdiqlənib |
| argument | arqument | [gündəlik] Funksiyaya verilən real dəyər. | təsdiqlənib |
| return value | qaytarılan dəyər | | təsdiqlənib |
| statement | bəyanat | `let y = 6;` kimi dəyər qaytarmayan konstruksiya. *ifadə* yalnız expression üçündür. | təsdiqlənib |
| expression | ifadə | [gündəlik] Dəyər qaytaran konstruksiya. | təsdiqlənib |
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
| method | metod | [gündəlik] | təsdiqlənib |
| associated function | —saxlanılır— (əlaqəli funksiya) | Rust-a məxsus: *associated function (əlaqəli funksiya)*. | təsdiqlənib |
| enum | —saxlanılır— | Azərbaycan proqramçıları ingiliscə deyir: *enum-un*, *enum-lar*. Alternativ: *sayma tipi*. | təsdiqlənib |
| variant | variant | Enum-un variantı. Yazılışı ingiliscə ilə eynidir. | təsdiqlənib |
| pattern | şablon | [gündəlik] Alternativ: *nümunə*. | təsdiqlənib |
| pattern matching | şablon uyğunlaşdırılması | *şablon* (pattern) sözü ilə uyğundur. | təsdiqlənib |
| match | —saxlanılır— | `match` açar sözü: *match ifadəsi*. | təsdiqlənib |
| crate | —saxlanılır— | Dizayn sənədində nümunə kimi göstərilib: *crate-ə*. | təsdiqlənib |
| package | paket | Cargo paketi. | təsdiqlənib |
| module | modul | [gündəlik] | təsdiqlənib |
| path | yol | Modul yolu. Fayl yolu da *yol*-dur; kontekstdən aydın olur. | təsdiqlənib |
| scope | əhatə dairəsi | Alternativ: *görünmə sahəsi*. *sahə* (field) ilə qarışmasın deyə seçilməyib. | təsdiqlənib |
| vector | vektor | [gündəlik] `Vec<T>`. | təsdiqlənib |
| hash map | heş cədvəli | `HashMap<K, V>`. Alternativ: ingiliscə saxlamaq. | təsdiqlənib |
| array | massiv | | təsdiqlənib |
| tuple | —saxlanılır— | Tərcümə olunmur: *tuple-lar*, *tuple-ın*. | təsdiqlənib |
| error | xəta | [gündəlik] | təsdiqlənib |
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
| thread | axın | Ümumi anlayışdır: ilk işlənmədə *axın (thread)*. *main thread* → *əsas axın*, *spawn a thread* → *axın yaratmaq*, *thread pool* → *axın hovuzu*. `thread::spawn` kimi kod dəyişmir. *stream* ingiliscə qaldığı üçün qarışmır; *idarəetmə axını* (control flow) başqa anlayışdır. | təsdiqlənib |
| compiler | kompilyator | [gündəlik] | təsdiqlənib |
| stack | —saxlanılır— | Tərcümə olunmur: *stack-də*, *stack-dən*. Kontekstdə bunun yaddaşa aid olduğu izah edilir (məs. "yaddaşın stack hissəsi"). *heap* ilə qarışmır (Türk tərcüməsində ikisi də *yığın* idi). | təsdiqlənib |
| heap | —saxlanılır— | *stack*-dən fərqli: *heap-də*. Kontekstdə yaddaşa aid olduğu izah edilir. | təsdiqlənib |
| type | tip | [gündəlik] | təsdiqlənib |
| integer | tam ədəd | | təsdiqlənib |
| floating-point number | üzən nöqtəli ədəd | Alternativ: *həqiqi ədəd*. | təsdiqlənib |
| macro | makro | [gündəlik] `println!`, `vec!` kimi makroların adları kodda qalır. | təsdiqlənib |
| attribute | atribut | `#[derive(...)]` və s. | təsdiqlənib |
| test | test | Yazılışı ingiliscə ilə eynidir. | təsdiqlənib |
| keyword | açar söz | | təsdiqlənib |
| loop | dövr | | təsdiqlənib |
| branch | budaq | `if` budaqları. | təsdiqlənib |
| comment | şərh | | təsdiqlənib |
| library | kitabxana | [gündəlik] | təsdiqlənib |
| command line | komanda sətri | | təsdiqlənib |
| directory | direktoriya | [gündəlik] Fayl sistemi direktoriyası; ingiliscə "folder" də bu sözlə tərcümə olunur (*qovluq* yox: proqramçılar *direktoriya* deyir). Kitabın bütün mətnində və README-də bu işlədilir. `cd`, `mkdir` kimi əmrlər kodda qalır. | təsdiqlənib |

## Yeni təkliflər: ön söz, giriş və 1-ci fəsil (Task 9)

| English | Azərbaycanca | Qeyd | Status |
| ------- | ------------ | ---- | ------ |
| build | —saxlanılır— | Proqramçılar belə deyir: *build etmək*, *debug build-i*, *build sistemi*, *build aləti*. Alternativ: *yığmaq / yığım*. | təsdiqlənib |
| compile | kompilyasiya etmək | [gündəlik] İsim: *kompilyasiya*. `compiler` → *kompilyator* ilə uyğundur. | təsdiqlənib |
| package manager | paket meneceri | [gündəlik] Cargo: "Rust-ın paket meneceri və build sistemi". | təsdiqlənib |
| dependency | asılılıq | *asılılıqlar*; "kodunuzun asılı olduğu kitabxanalar". | təsdiqlənib |
| executable | icra olunan fayl | [gündəlik] "binary executable" → *icra olunan binar fayl*. | təsdiqlənib |
| binary | binar fayl | [gündəlik] Kontekstdə sadəcə *binar*: "binar faylı işə salmaq". Gələcəkdə *binary crate* → *binar crate*. | təsdiqlənib |
| source code | mənbə kodu | [gündəlik] *source file* → *mənbə faylı*. Alternativ: *qaynaq kodu*. | təsdiqlənib |
| release | reliz | [gündəlik] *reliz üçün build*, *reliz profili*. "yeni versiya" kimi adi mənada *versiya* (*buraxılış* edition üçündür). | təsdiqlənib |
| debug | —saxlanılır— | *debug build-i*, *debug məlumatı*. Alternativ: *sazlama*. | təsdiqlənib |
| optimization | optimizasiya | [gündəlik] optimizasiya etmək, optimizasiya olunmuş | təsdiqlənib |
| profile | profil | [gündəlik] Cargo profili: *dev*, *release*. | təsdiqlənib |
| stable | stabil | [gündəlik] *stabil versiya*. Alternativ: *sabit* (amma *sabit* = constant). | təsdiqlənib |
| edition | buraxılış | Rust-ın buraxılışları (2015, 2018, 2021, 2024): *Rust-ın 2015 il buraxılışı*, *2024 buraxılışı*. `edition` açarı kod kimi qalır. Kitabın nəşri isə *nəşr*. | təsdiqlənib |
| memory | yaddaş | [gündəlik] | təsdiqlənib |
| memory safety | yaddaş təhlükəsizliyi | | təsdiqlənib |
| systems programming | sistem proqramlaşdırması | [gündəlik] | təsdiqlənib |
| low-level | aşağı səviyyəli | [gündəlik] *high-level* → *yüksək səviyyəli*. | təsdiqlənib |
| zero-cost abstraction | sıfır xərcli abstraksiya | | təsdiqlənib |
| concurrency | —saxlanılır— (eyni vaxtlılıq) | Proqramçılara tanış termindir; lazım olduqda kontekstdə izah edilir: *concurrency-ni*, *concurrent proqramlaşdırma*. 16-cı fəsildə *paralellik* (parallelism) ilə fərqləndirilir. | təsdiqlənib |
| parallelism | paralellik | [gündəlik] *concurrency*-dən fərqli anlayışdır. | təsdiqlənib |
| standard library | standart kitabxana | [gündəlik] | təsdiqlənib |
| application programming interface (API) | proqramlaşdırma interfeysi (API) | İlk dəfədən sonra sadəcə *API*. | təsdiqlənib |
| integrated development environment (IDE) | inteqrasiya olunmuş inkişaf mühiti (IDE) | İlk dəfədən sonra sadəcə *IDE*. | təsdiqlənib |
| shell | —saxlanılır— | *shell-də*. Kitab *terminal* və *shell* sözlərini yanaşı işlədir; *terminal* yazılışı eynidir. | təsdiqlənib |
| linker | —saxlanılır— | Alternativ: *əlaqələndirici* (akademik səslənir). | təsdiqlənib |
| flag | —saxlanılır— (bayraq) | Komanda sətri flag-i: `--vcs` flag-i, `--release` flag-i ilə. | təsdiqlənib |
| Rustacean | —saxlanılır— | Rust icmasının özünə verdiyi zarafatyana ad: *Rustacean-lar*. | təsdiqlənib |
| version control system | versiya nəzarəti sistemi | [gündəlik] | təsdiqlənib |
| repository | repozitoriya | [gündəlik] README-də artıq işlədilib. | təsdiqlənib |
| bug | baq | [gündəlik] Proqramçı dilində *baq*; *xəta* (error) ilə fərqləndirilir. Alternativ: *səhv*. | təsdiqlənib |
| error message | xəta mesajı | [gündəlik] *warning* → *xəbərdarlıq*. | təsdiqlənib |
| refactoring | refaktorinq | [gündəlik] | təsdiqlənib |
| code review | kod revyu | [gündəlik] *kod revyusu*, *kod revyusunda*, *kod revyu zamanı*. | təsdiqlənib |
| open source | açıq mənbə | [gündəlik] *açıq mənbəli layihələr*. | təsdiqlənib |
| implementation | realizasiya | [gündəlik] Fel: *realizə etmək*. Vacibdir: 5-ci və 10-cu fəsillərdə *implement a trait* → *trait-i realizə etmək*. Alternativ: *implementasiya*. | təsdiqlənib |
| syntax | sintaksis | [gündəlik] | təsdiqlənib |
| declaration | elan | [gündəlik] "funksiyanı elan etmək". | təsdiqlənib |
| function body | funksiyanın gövdəsi | *gövdə*. | təsdiqlənib |
| data structure | data strukturu | [gündəlik] Proqramçıların gündəlik dilinə yaxın forma. | təsdiqlənib |
| collection | kolleksiya | [gündəlik] | təsdiqlənib |
| control flow | idarəetmə axını | | təsdiqlənib |
| functional programming | funksional proqramlaşdırma | | təsdiqlənib |
| object-oriented programming | obyektyönümlü proqramlaşdırma | | təsdiqlənib |
| privacy | məxfilik | 7-ci fəsil: *məxfilik qaydaları*. | təsdiqlənib |
| public | —saxlanılır— (açıq) | `pub`. *public API* → *public (açıq) API*. | təsdiqlənib |
| private | —saxlanılır— (gizli) | | təsdiqlənib |
| future | —saxlanılır— | 17-ci fəsil (`Future` trait-i). Girişdə yalnız adı çəkilir. | təsdiqlənib |
| stream | —saxlanılır— | 17-ci fəsil. *axın* thread üçündür, ona görə stream ingiliscə qalır. | təsdiqlənib |
| task | —saxlanılır— | 17-ci fəsildə async task. Adi mənada *tapşırıq*. | təsdiqlənib |
| unsafe Rust | —saxlanılır— | | təsdiqlənib |
| nightly Rust | —saxlanılır— | | təsdiqlənib |
| derivable trait | derive edilə bilən trait | `#[derive]` atributu ilə. | təsdiqlənib |
| ahead-of-time compiled | əvvəlcədən kompilyasiya olunan | | təsdiqlənib |
| cache | keş | [gündəlik] | təsdiqlənib |

## Yeni təkliflər 2: 1-ci fəsil üçün əlavə terminlər (Task 9)

| English | Azərbaycanca | Qeyd | Status |
| ------- | ------------ | ---- | ------ |
| install | quraşdırmaq | [gündəlik] *quraşdırma* (installation), *quraşdırılıb* (installed), *installer* → *quraşdırıcı*. *yükləmək* yalnız download üçündür; ikisi eyni cümlədə ayrı addımlardır. | təsdiqlənib |
| uninstall | silmək | [gündəlik] "Rust-ı silmək". | təsdiqlənib |
| update | yeniləmək | [gündəlik] *yeniləmə*. | təsdiqlənib |
| download | yükləmək | [gündəlik] İnternetdən götürmək: *yükləmə*, *yüklənmiş*. Install mənasında işlədilmir (bax *quraşdırmaq*). | təsdiqlənib |
| operating system | əməliyyat sistemi | [gündəlik] | təsdiqlənib |
| documentation | dokumentasiya | [gündəlik] Proqramçı dili. Alternativ: *sənədlər*. | təsdiqlənib |
| script | skript | [gündəlik] | təsdiqlənib |
| text editor | mətn redaktoru | [gündəlik] | təsdiqlənib |
| configuration | konfiqurasiya | [gündəlik] *konfiqurasiya faylı*. | təsdiqlənib |
| output | çıxış | [gündəlik] Proqramın/komandanın çıxışı. STYLE.md-də artıq işlədilib. | təsdiqlənib |
| prompt | —saxlanılır— | Komanda sətri prompt-u (`$`). Alternativ: *dəvət*. | təsdiqlənib |
| file extension | fayl genişlənməsi | [gündəlik] Konkret genişlənmədən danışarkən: *.rs genişlənməsi*, *.rs genişlənməli fayl*. | təsdiqlənib |
| home directory | ev direktoriyası | [gündəlik] | təsdiqlənib |
| top-level directory | kök direktoriya | [gündəlik] Layihənin kök direktoriyası. | təsdiqlənib |
| underscore | alt xətt | [gündəlik] `_`. | təsdiqlənib |
| semicolon | nöqtəli vergül | [gündəlik] `;`. | təsdiqlənib |
| curly brackets | fiqurlu mötərizələr | [gündəlik] `{}`. | təsdiqlənib |
| parentheses | mötərizələr | [gündəlik] `()`; dəqiqlik lazımdırsa *dairəvi mötərizələr*. | təsdiqlənib |
| ecosystem | ekosistem | [gündəlik] | təsdiqlənib |
| tool | alət | [gündəlik] *tooling* → *alətlər*. *build tool* → *build aləti*. | təsdiqlənib |
| formatter | formatlama aləti | [gündəlik] *format* (fel) → *formatlamaq*. | təsdiqlənib |
| code completion | kodun avtomatik tamamlanması | [gündəlik] | təsdiqlənib |
| developer | developer | Proqramçılar özləri belə deyir: *developer-lər*. *programmer* → *proqramçı*. Alternativ: hər ikisi *proqramçı*. | təsdiqlənib |
| software | proqram təminatı | [gündəlik] | təsdiqlənib |
| production | production | "production-da işlətmək". Alternativ: *real istifadə mühiti*. | təsdiqlənib |
| web server | veb server | [gündəlik] | təsdiqlənib |
| web service | veb servis | [gündəlik] | təsdiqlənib |
| browser | brauzer | [gündəlik] | təsdiqlənib |
| multithreaded | çoxaxınlı | *single-threaded* → *təkaxınlı*. *axın* (thread) ilə uyğundur. | təsdiqlənib |
| async / await | —saxlanılır— | `async`/`await` açar sözləri; anlayış kimi də ingiliscə. *asynchronous programming* → *asinxron proqramlaşdırma*. | təsdiqlənib |
| idiom | idiom | Rust idiomları. | təsdiqlənib |
| operator | operator | Yazılışı eynidir. | təsdiqlənib |
| network | şəbəkə | [gündəlik] | təsdiqlənib |
| system variable | sistem dəyişəni | `%PATH%`. *environment variable* → *mühit dəyişəni* (12-ci fəsil). | təsdiqlənib |
| commit hash | commit heşi | [gündəlik] Git commit-i: *commit-in*. | təsdiqlənib |
| dynamic language | dinamik proqramlaşdırma dili | [gündəlik] Ruby, Python, JavaScript. Adətən tam forma; eyni cümlədə təkrar olunarsa və ya kontekst aydındırsa qısaca *dinamik dil*. | təsdiqlənib |
| legacy code | legacy kod | [gündəlik] Proqramçı dili: *legacy kodu dəyişmək*. *köhnə kod* sadəcə "əvvəlki versiya" mənasında işlədilə bilər. | təsdiqlənib |
| contribute | töhfə vermək | [gündəlik] *contributor* → *töhfə verən*; *Rust icmasının töhfələri ilə*. | təsdiqlənib |
| machine learning | maşın öyrənməsi | | təsdiqlənib |
| embedded device | daxili (embedded) qurğu | İlk işlənmədə ingiliscə söz terminin içində: *daxili (embedded) qurğular*; sonra *daxili qurğu*. *embedded system* → *daxili sistem*. | təsdiqlənib |
| Internet of Things (IoT) | Əşyaların İnterneti (IoT) | Mötərizədə ingiliscə abreviatura; *IoT tətbiqləri*. | təsdiqlənib |
| benchmark | bençmark | [gündəlik] Fel: *bençmark etmək*; *bençmark testləri*. `#[bench]` kimi kod dəyişmir. | təsdiqlənib |
| troubleshooting | problemlərin aradan qaldırılması | [gündəlik] 1.1 bölməsinin başlığı; lövbər `#problemlərin-aradan-qaldırılması`. | təsdiqlənib |
