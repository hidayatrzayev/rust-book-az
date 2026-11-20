# Giriş

> Qeyd: Kitabın bu nəşri [No Starch Press][nsp] tərəfindən çap və elektron
> kitab formatında buraxılan [The Rust Programming Language][nsprust] kitabı ilə
> eynidir.

[nsprust]: https://nostarch.com/rust-programming-language-3rd-edition
[nsp]: https://nostarch.com/

Rust haqqında giriş kitabı olan _Rust Proqramlaşdırma Dili_ kitabına xoş
gəlmisiniz. Rust proqramlaşdırma dili daha sürətli və daha etibarlı proqram
təminatı yazmağınıza kömək edir. Proqramlaşdırma dillərinin
dizaynında yüksək səviyyəli erqonomika ilə aşağı səviyyəli
idarəetmə çox vaxt bir-biri ilə ziddiyyət təşkil edir; Rust bu ziddiyyətə meydan
oxuyur. Güclü texniki imkanlarla əla developer təcrübəsi arasında tarazlıq
yaradaraq, Rust sizə aşağı səviyyəli təfərrüatları — məsələn, yaddaşdan
istifadəni — ənənəvi olaraq belə idarəetmə ilə bağlı olan çətinliklər olmadan
idarə etmək imkanı verir.

## Rust kimin üçündür

Rust müxtəlif səbəblərdən bir çox insan üçün idealdır. Ən vacib qruplardan bir
neçəsinə baxaq.

### Developer komandaları

Rust sistem proqramlaşdırması üzrə bilikləri müxtəlif
səviyyədə olan böyük developer komandalarının birgə işi üçün məhsuldar alət olduğunu sübut edir. Aşağı səviyyəli kodda müxtəlif incə baqlar
yaranmağa meyllidir; əksər digər dillərdə onları yalnız geniş testlər və
təcrübəli developerlərin diqqətli kod revyusu ilə tutmaq olar. Rust-da isə
nəzarətçi rolunu kompilyator oynayır: tərkibində bu kimi çətin tutulan
baqlar, o cümlədən concurrency (eyni vaxtlılıq) ilə bağlı baqlar olan kodu
kompilyasiya etməkdən imtina edir. Kompilyatorla birlikdə işləyərək, komanda
vaxtını baqların arxasınca qaçmağa deyil, proqramın məntiqinə fokuslanmağa sərf
edə bilər.

Rust həmçinin sistem proqramlaşdırması dünyasına müasir developer alətləri
gətirir:

- Cargo — Rust ilə birlikdə gələn build aləti və asılılıqları (dependencies)
  idarə edən alət — asılılıqları əlavə etməyi, kompilyasiya etməyi və idarə
  etməyi bütün Rust ekosistemində problemsiz və eyni cür edir.
- `rustfmt` formatlama aləti developerlər arasında vahid kod
  üslubunu təmin edir.
- Rust Language Server inteqrasiya olunmuş inkişaf mühitlərində (Integrated
  Development Environment, IDE) kodun avtomatik tamamlanmasını və redaktorda
  kodun yanında göstərilən xəta mesajlarını təmin edir.

Rust ekosistemindəki bu və digər alətlərdən istifadə edərək, developerlər sistem
səviyyəli kod yazarkən də məhsuldar ola bilərlər.

### Tələbələr

Rust tələbələr və sistem anlayışlarını öyrənməyə maraq göstərənlər üçündür.
Rust-dan istifadə edərək, bir çox insan əməliyyat sistemlərinin hazırlanması kimi mövzuları öyrənib. İcma çox qonaqpərvərdir və
tələbələrin suallarını məmnuniyyətlə cavablandırır. Bu kitab kimi səylər
vasitəsilə Rust komandaları sistem anlayışlarını daha çox insan, xüsusən
proqramlaşdırmaya yeni başlayanlar üçün daha əlçatan etmək istəyir.

### Şirkətlər

Böyük və kiçik yüzlərlə şirkət Rust-ı production-da müxtəlif tapşırıqlar üçün
istifadə edir: komanda sətri (command line) alətləri, veb servislər, DevOps alətləri, daxili (embedded) qurğular, audio və video
analizi və transkodlaşdırma, kriptovalyutalar, bioinformatika, axtarış
sistemləri, Əşyaların İnterneti (Internet of Things, IoT) tətbiqləri, maşın
öyrənməsi (machine learning) və hətta Firefox brauzerinin əsas
hissələri.

### Açıq mənbə developerləri

Rust, Rust proqramlaşdırma dilini, icmasını, developer alətlərini və
kitabxanalarını inkişaf etdirmək istəyən insanlar üçündür. Rust
dilinə töhfə verməyinizi çox istərdik.

### Sürətə və stabilliyə dəyər verən insanlar

Rust sürətli və stabil dil arzulayan insanlar üçündür. Sürət dedikdə
həm Rust kodunun nə qədər tez işləyə bildiyini, həm də Rust-ın proqramları nə
qədər tez yazmağa imkan verdiyini nəzərdə tuturuq. Rust kompilyatorunun
yoxlamaları yeni imkanlar əlavə edildikdə və refaktorinq zamanı
stabilliyi təmin edir. Bu, belə yoxlamaları olmayan dillərdəki kövrək legacy
koddan fərqlidir; developerlər çox vaxt belə kodu dəyişməkdən
qorxurlar. Rust təhlükəsiz kodun eyni zamanda sürətli olmasına çalışır. Bunun
üçün o, sıfır xərcli abstraksiyalardan (zero-cost abstractions) istifadə edir:
bunlar yüksək səviyyəli imkanlardır, amma aşağı səviyyəli koda kompilyasiya
olunur və əl ilə yazılmış kod qədər sürətli işləyir.

Rust dili bir çox başqa istifadəçiləri də dəstəkləməyə ümid edir; burada adı
çəkilənlər ən böyük maraqlı tərəflərdən sadəcə bəziləridir. Ümumilikdə Rust-ın
ən böyük ambisiyası təhlükəsizlik _və_ məhsuldarlıq, sürət _və_ erqonomika təmin
edərək, proqramçıların onilliklərdir razılaşdığı kompromisləri aradan
qaldırmaqdır. Rust-ı sınayın və onun seçimlərinin sizə uyğun olub-olmadığını
görün.

## Bu kitab kimin üçündür

Bu kitab sizin artıq başqa bir proqramlaşdırma dilində kod yazdığınızı güman
edir, amma hansı dil olduğu barədə heç bir fərziyyə irəli sürmür. Materialı müxtəlif
proqramlaşdırma təcrübəsi olan insanlar üçün geniş şəkildə əlçatan etməyə
çalışmışıq. Proqramlaşdırmanın _nə_ olduğu və ya bu barədə necə düşünmək
lazım olduğu haqqında çox danışmırıq. Proqramlaşdırmada tamamilə yenisinizsə,
xüsusi olaraq proqramlaşdırmaya giriş təqdim edən kitab oxumağınız daha
faydalı olar.

## Bu kitabdan necə istifadə etməli

Ümumiyyətlə, bu kitab sizin onu əvvəldən sonadək ardıcıl oxuduğunuzu güman edir.
Sonrakı fəsillər əvvəlki fəsillərdəki anlayışlar üzərində qurulur; əvvəlki
fəsillər müəyyən mövzunun təfərrüatlarına girməyə bilər, amma həmin mövzuya
sonrakı fəsildə yenidən qayıdacağıq.

Bu kitabda iki növ fəsil tapacaqsınız: anlayış fəsilləri və layihə fəsilləri.
Anlayış fəsillərində Rust-ın hər hansı bir cəhəti haqqında öyrənəcəksiniz.
Layihə fəsillərində isə indiyədək öyrəndiklərinizi tətbiq edərək, birlikdə kiçik
proqramlar yazacağıq. 2-ci, 12-ci və 21-ci fəsillər layihə fəsilləridir;
qalanları anlayış fəsilləridir.

**1-ci fəsil** Rust-ı necə quraşdırmağı, “Hello, world!” proqramını
necə yazmağı və Rust-ın paket meneceri və build aləti olan
Cargo-dan necə istifadə etməyi izah edir. **2-ci fəsil** Rust-da proqram
yazmağa praktiki girişdir: burada ədəd tapma oyunu yazacaqsınız. Burada
anlayışları ümumi şəkildə əhatə edirik, sonrakı fəsillər isə əlavə təfərrüatlar
verəcək. Dərhal işə girişmək istəyirsinizsə, 2-ci fəsil məhz bunun üçündür.
Növbəti mövzuya keçməzdən əvvəl hər təfərrüatı öyrənməyi üstün tutan xüsusilə
diqqətli oxucusunuzsa, 2-ci fəsli ötürüb, birbaşa digər proqramlaşdırma
dillərindəkinə bənzəyən Rust imkanlarını əhatə edən **3-cü fəslə** keçə
bilərsiniz; sonra öyrəndiyiniz təfərrüatları tətbiq edən layihə üzərində
işləmək istədikdə 2-ci fəslə qayıda bilərsiniz.

**4-cü fəsildə** Rust-ın ownership (sahiblik) sistemi haqqında öyrənəcəksiniz.
**5-ci fəsil** strukturları (structs) və metodları müzakirə edir.
**6-cı fəsil** enum-ları, `match` ifadələrini, həmçinin `if let`
və `let...else` idarəetmə axını (control flow) konstruksiyalarını əhatə edir.
Öz tiplərinizi yaratmaq üçün strukturlardan və enum-lardan istifadə
edəcəksiniz.

**7-ci fəsildə** Rust-ın modul sistemi, həmçinin kodunuzu və onun
açıq (public) proqramlaşdırma interfeysini (Application Programming Interface,
API) təşkil etmək üçün məxfilik (privacy) qaydaları haqqında öyrənəcəksiniz.
**8-ci fəsil** standart kitabxananın təqdim etdiyi bəzi
geniş yayılmış kolleksiya data strukturlarını
müzakirə edir: vektorlar, sətirlər (strings) və heş cədvəlləri (hash
maps). **9-cu fəsil** Rust-ın xətaların emalı fəlsəfəsini və üsullarını
araşdırır.

**10-cu fəsil** bir neçə tipə aid ola bilən kodu təyin etmək gücü verən
generic-lərə, trait-lərə və lifetime-lara (ömür müddəti) dərindən nəzər salır.
**11-ci fəsil** tamamilə testlərə həsr olunub; Rust-ın təhlükəsizlik
zəmanətlərinə baxmayaraq, proqramınızın məntiqinin düzgün olmasını təmin etmək
üçün testlər lazımdır. **12-ci fəsildə** fayllarda mətn axtaran `grep` komanda
sətri alətinin funksionallığının bir hissəsinin öz realizasiyamızı yazacağıq. Bunun üçün əvvəlki fəsillərdə müzakirə etdiyimiz
bir çox anlayışdan istifadə edəcəyik.

**13-cü fəsil** closure-ları və iteratorları, yəni Rust-ın funksional
proqramlaşdırma dillərindən gələn imkanlarını
araşdırır. **14-cü fəsildə** Cargo-ya daha ətraflı baxacaq və kitabxanalarınızı
başqaları ilə paylaşmağın ən yaxşı təcrübələrindən danışacağıq. **15-ci fəsil**
standart kitabxananın təqdim etdiyi smart pointer-ləri (ağıllı göstəricilər) və
onların funksionallığını təmin edən trait-ləri müzakirə edir.

**16-cı fəsildə** concurrent proqramlaşdırmanın müxtəlif modellərini nəzərdən
keçirəcək və Rust-ın bir neçə axında (threads) qorxmadan proqramlaşdırmağa necə
kömək etdiyindən danışacağıq. **17-ci fəsildə** bunun üzərinə Rust-ın async və
await sintaksisini, həmçinin task-ları, future-ləri, stream-ləri və
onların imkan verdiyi yüngül concurrency modelini araşdıraraq davam edirik.

**18-ci fəsil** Rust idiomlarının sizə tanış ola biləcək obyektyönümlü
proqramlaşdırma (object-oriented programming) prinsipləri ilə necə müqayisə
olunduğuna baxır. **19-cu fəsil** Rust proqramlarında fikirləri çatdırmağın
güclü üsulları olan şablonlar və şablon uyğunlaşdırılması (pattern
matching) üzrə məlumat bələdçisidir. **20-ci fəsildə** maraqlı qabaqcıl
mövzulardan ibarət rəngarəng toplu var: unsafe Rust, makrolar,
həmçinin lifetime-lar, trait-lər, tiplər, funksiyalar və
closure-lar haqqında əlavə məlumat.

**21-ci fəsildə** aşağı səviyyəli çoxaxınlı (multithreaded) veb server realizə edəcəyimiz layihəni tamamlayacağıq!

Nəhayət, bəzi əlavələrdə dil haqqında məlumat kitabçası formatında faydalı
məlumatlar var. **Əlavə A** Rust-ın açar sözlərini (keywords), **Əlavə B**
Rust-ın operatorlarını və simvollarını, **Əlavə C** standart kitabxananın
təqdim etdiyi derive edilə bilən trait-ləri (derivable traits), **Əlavə D** bəzi
faydalı developer alətlərini əhatə edir, **Əlavə E** isə Rust buraxılışlarını izah edir. **Əlavə F**-də kitabın tərcümələrini tapa bilərsiniz,
**Əlavə G**-də isə Rust-ın necə yaradıldığını və nightly Rust-ın nə olduğunu
izah edəcəyik.

Bu kitabı oxumağın yanlış üsulu yoxdur: irəli keçmək istəyirsinizsə, buyurun!
Çaşqınlıq yaşasanız, əvvəlki fəsillərə qayıtmalı ola bilərsiniz. Amma sizə necə
uyğundursa, elə edin.

<span id="ferris"></span>

Rust öyrənmə prosesinin vacib hissəsi kompilyatorun göstərdiyi xəta
mesajlarını oxumağı öyrənməkdir: bu mesajlar sizi işləyən koda doğru
istiqamətləndirəcək. Buna görə də kompilyasiya olunmayan bir çox nümunəni, hər
vəziyyətdə kompilyatorun sizə göstərəcəyi xəta mesajı ilə birlikdə təqdim
edəcəyik. Bilin ki, təsadüfi bir nümunəni daxil edib işə salsanız, o,
kompilyasiya olunmaya bilər! İşə salmağa çalışdığınız nümunənin xəta verməli
olub-olmadığını görmək üçün ətrafdakı mətni mütləq oxuyun. Əksər hallarda sizi
kompilyasiya olunmayan istənilən kodun düzgün versiyasına yönəldəcəyik. Ferris
də işləməli olmayan kodu ayırd etməyə kömək edəcək:

| Ferris                                                                                                              | Mənası                                    |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| <img src="img/ferris/does_not_compile.svg" class="ferris-explain" alt="Sual işarəli Ferris"/>                       | Bu kod kompilyasiya olunmur!              |
| <img src="img/ferris/panics.svg" class="ferris-explain" alt="Əllərini yuxarı qaldıran Ferris"/>                     | Bu kod panic edir!                        |
| <img src="img/ferris/not_desired_behavior.svg" class="ferris-explain" alt="Bir caynağını qaldırıb çiyin çəkən Ferris"/> | Bu kod istənilən davranışı göstərmir.     |

Əksər hallarda sizi kompilyasiya olunmayan istənilən kodun düzgün versiyasına
yönəldəcəyik.

## Mənbə kodu

Bu kitabın yaradıldığı mənbə fayllarını [GitHub-da][book] tapa bilərsiniz.

[book]: https://github.com/rust-lang/book/tree/main/src
