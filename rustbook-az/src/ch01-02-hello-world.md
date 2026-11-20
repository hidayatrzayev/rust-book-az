## Hello, World!

Rust-ı quraşdırdığınıza görə ilk Rust proqramınızı yazmağın vaxtıdır. Yeni dil
öyrənərkən ekrana `Hello, world!` mətnini çap edən kiçik proqram yazmaq
ənənədir, ona görə biz də burada eyni şeyi edəcəyik!

> Qeyd: Bu kitab komanda sətri ilə ilkin tanışlığınızın olduğunu güman edir.
> Rust kodu necə redaktə etdiyinizə, hansı alətlərdən istifadə etdiyinizə və ya
> kodunuzun harada saxlandığına xüsusi tələblər qoymur, ona görə də komanda
> sətri əvəzinə IDE istifadə etməyi üstün tutursunuzsa, sevimli IDE-nizdən
> istifadə edə bilərsiniz. Hazırda bir çox IDE-də müəyyən dərəcədə Rust dəstəyi
> var; təfərrüatlar üçün IDE-nin dokumentasiyasına baxın. Rust komandası
> `rust-analyzer` vasitəsilə əla IDE dəstəyi təmin etməyə fokuslanıb. Ətraflı
> məlumat üçün [Əlavə D-yə][devtools]<!-- ignore --> baxın.

<!-- Old headings. Do not remove or links may break. -->
<a id="creating-a-project-directory"></a>

### Layihə direktoriyasının hazırlanması

Rust kodunuzu saxlamaq üçün direktoriya yaratmaqla başlayacaqsınız. Kodunuzun
harada yerləşməsi Rust üçün fərq etmir, amma bu kitabdakı tapşırıqlar və
layihələr üçün ev direktoriyanızda _projects_ direktoriyası
yaradıb bütün layihələrinizi orada saxlamağı təklif edirik.

Terminal açın və _projects_ direktoriyasını, həmçinin _projects_
direktoriyasının içində “Hello, world!” layihəsi üçün direktoriya yaratmaq
üçün aşağıdakı komandaları daxil edin.

Linux, macOS və Windows-dakı PowerShell üçün bunu daxil edin:

```console
$ mkdir ~/projects
$ cd ~/projects
$ mkdir hello_world
$ cd hello_world
```

Windows CMD üçün bunu daxil edin:

```cmd
> mkdir "%USERPROFILE%\projects"
> cd /d "%USERPROFILE%\projects"
> mkdir hello_world
> cd hello_world
```

<!-- Old headings. Do not remove or links may break. -->
<a id="writing-and-running-a-rust-program"></a>

### Rust proqramının əsasları

Sonra yeni mənbə faylı yaradın və onu _main.rs_ adlandırın. Rust faylları
həmişə _.rs_ genişlənməsi ilə bitir. Fayl adında birdən çox söz işlədirsinizsə,
onları alt xətt simvolu ilə ayırmaq qəbul olunmuş qaydadır.
Məsələn, _helloworld.rs_ əvəzinə _hello_world.rs_ yazın.

İndi yenicə yaratdığınız _main.rs_ faylını açın və Listing 1-1-dəki kodu daxil
edin.

<Listing number="1-1" file-name="main.rs" caption="`Hello, world!` çap edən proqram">

```rust
fn main() {
    println!("Hello, world!");
}
```

</Listing>

Faylı yadda saxlayın və _~/projects/hello_world_ direktoriyasında açıq olan
terminal pəncərənizə qayıdın. Linux və ya macOS-da faylı kompilyasiya edib işə
salmaq üçün aşağıdakı komandaları daxil edin:

```console
$ rustc main.rs
$ ./main
Hello, world!
```

Windows-da `./main` əvəzinə `.\main` komandasını daxil edin:

```powershell
> rustc main.rs
> .\main
Hello, world!
```

Əməliyyat sisteminizdən asılı olmayaraq, terminalda
`Hello, world!` sətri (string) çap olunmalıdır. Bu çıxışı görmürsünüzsə, kömək almaq
üçün Quraşdırma bölməsinin
[“Problemlərin aradan qaldırılması”][troubleshooting]<!-- ignore --> hissəsinə
qayıdın.

`Hello, world!` çap olundusa, təbrik edirik! Siz rəsmi olaraq Rust proqramı
yazdınız. Bu, sizi Rust proqramçısı edir — xoş gəlmisiniz!

<!-- Old headings. Do not remove or links may break. -->

<a id="anatomy-of-a-rust-program"></a>

### Rust proqramının anatomiyası

Gəlin bu “Hello, world!” proqramını ətraflı nəzərdən keçirək. Tapmacanın
birinci parçası budur:

```rust
fn main() {

}
```

Bu sətirlər `main` adlı funksiyanı təyin edir. `main` funksiyası xüsusidir: o,
icra olunan hər Rust proqramında həmişə ilk işləyən koddur. Burada birinci
sətir `main` adlı funksiyanın elanıdır: onun parametrləri yoxdur və o, heç nə qaytarmır. Parametrlər olsaydı, onlar
mötərizələrin, yəni `()` işarəsinin içinə yazılardı.

Funksiyanın gövdəsi (function body) `{}` içinə alınır. Rust bütün funksiya
gövdələrinin fiqurlu mötərizələr içində olmasını tələb edir.
Açılan fiqurlu mötərizəni funksiyanın elanı ilə eyni sətirdə, aralarında bir
boşluq qoyaraq yerləşdirmək yaxşı üslub sayılır.

> Qeyd: Rust layihələrində standart üsluba əməl etmək istəyirsinizsə, kodunuzu
> müəyyən üslubda formatlamaq üçün `rustfmt` adlı avtomatik formatlama
> alətindən istifadə edə bilərsiniz (`rustfmt` haqqında ətraflı:
> [Əlavə D][devtools]<!-- ignore -->). Rust komandası bu aləti `rustc` kimi
> standart Rust paylanmasına daxil edib, ona görə o, artıq kompüterinizdə
> quraşdırılmış olmalıdır!

`main` funksiyasının gövdəsində aşağıdakı kod var:

```rust
println!("Hello, world!");
```

Bu sətir bu kiçik proqramdakı bütün işi görür: ekrana mətn çap edir. Burada
diqqət etməli olduğunuz üç vacib təfərrüat var.

Birincisi, `println!` Rust makrosunu çağırır. Əgər o, funksiya
çağırsaydı, `println` (`!` olmadan) kimi yazılardı. Rust makroları Rust
sintaksisini genişləndirmək üçün kod yaradan kod yazmağın bir üsuludur
və onları [20-ci fəsildə][ch20-macros]<!-- ignore --> daha ətraflı müzakirə
edəcəyik. Hələlik bilməyiniz kifayətdir ki, `!` işarəsi adi funksiya əvəzinə
makro çağırdığınızı bildirir və makrolar həmişə funksiyalarla eyni qaydalara
əməl etmir.

İkincisi, `"Hello, world!"` sətrini görürsünüz. Bu sətri `println!`-ə arqument kimi ötürürük və sətir ekrana çap olunur.

Üçüncüsü, sətri nöqtəli vergüllə, yəni `;` ilə bitiririk; bu,
ifadənin bitdiyini və növbətinin başlamağa hazır olduğunu
göstərir. Rust kodunun əksər sətirləri nöqtəli vergüllə bitir.

<!-- Old headings. Do not remove or links may break. -->
<a id="compiling-and-running-are-separate-steps"></a>

### Kompilyasiya və icra

Yenicə yaradılmış proqramı işə saldınız, gəlin indi prosesin hər addımını
nəzərdən keçirək.

Rust proqramını işə salmazdan əvvəl onu Rust kompilyatoru ilə kompilyasiya
etməlisiniz: `rustc` komandasını daxil edib ona mənbə faylınızın adını ötürün,
belə:

```console
$ rustc main.rs
```

C və ya C++ təcrübəniz varsa, bunun `gcc` və ya `clang`-a bənzədiyini
görəcəksiniz. Uğurlu kompilyasiyadan sonra Rust icra olunan binar fayl
yaradır.

Linux, macOS və Windows-dakı PowerShell-də icra olunan faylı
shell-inizdə `ls` komandasını daxil etməklə görə bilərsiniz:

```console
$ ls
main  main.rs
```

Linux və macOS-da iki fayl görəcəksiniz. Windows-da PowerShell ilə CMD-də
görəcəyiniz həmin üç faylı görəcəksiniz. Windows-da CMD ilə isə bunu daxil
edərdiniz:

```cmd
> dir /B %= the /B option says to only show the file names =%
main.exe
main.pdb
main.rs
```

Burada _.rs_ genişlənməli mənbə kodu faylı, icra olunan fayl
(Windows-da _main.exe_, digər bütün platformalarda isə _main_) və Windows
istifadə edərkən debug məlumatını saxlayan, _.pdb_ genişlənməli fayl görünür.
Buradan _main_ və ya _main.exe_ faylını belə işə salırsınız:

```console
$ ./main # or .\main on Windows
```

_main.rs_ faylınız “Hello, world!” proqramınızdırsa, bu komanda terminalınıza
`Hello,
world!` çap edir.

Ruby, Python və ya JavaScript kimi dinamik proqramlaşdırma dili ilə daha çox tanışsınızsa, proqramı ayrı addımlarla kompilyasiya edib
işə salmağa öyrəşməmiş ola bilərsiniz. Rust _əvvəlcədən kompilyasiya olunan
(ahead-of-time compiled)_ dildir; yəni proqramı kompilyasiya edib icra olunan
faylı başqasına verə bilərsiniz və o, Rust quraşdırılmamış olsa belə, onu işə
sala bilər. Kiməsə _.rb_, _.py_ və ya _.js_ faylı versəniz, onda müvafiq olaraq
Ruby, Python və ya JavaScript realizasiyası quraşdırılmış
olmalıdır. Lakin həmin dillərdə proqramı kompilyasiya edib işə salmaq üçün cəmi
bir komanda kifayətdir. Dil dizaynında hər şey kompromisdir.

Sadə proqramlar üçün yalnız `rustc` ilə kompilyasiya etmək kifayətdir, lakin
layihəniz böyüdükcə bütün seçimləri idarə etmək və kodunuzu paylaşmağı
asanlaşdırmaq istəyəcəksiniz. Növbəti bölmədə sizi real Rust proqramları
yazmağa kömək edəcək Cargo aləti ilə tanış edəcəyik.

[troubleshooting]: ch01-01-installation.html#problemlərin-aradan-qaldırılması
[devtools]: appendix-04-useful-development-tools.html
[ch20-macros]: ch20-05-macros.html
