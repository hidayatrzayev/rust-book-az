## Hello, Cargo!

Cargo Rust-ın *build* sistemi və paket meneceridir. Rust-çıların çoxu Rust
layihələrini idarə etmək üçün bu alətdən istifadə edir, çünki Cargo sizin
əvəzinizə bir çox işi görür: kodunuzu *build* edir, kodunuzun asılı olduğu
kitabxanaları yükləyir və həmin kitabxanaları *build* edir. (Kodunuzun ehtiyac
duyduğu kitabxanaları _asılılıqlar_ adlandırırıq.)

İndiyədək yazdığımız kimi ən sadə Rust proqramlarının heç bir asılılığı yoxdur.
“Hello, world!” layihəsini Cargo ilə *build* etsəydik, o, Cargo-nun yalnız
kodunuzu *build* edən hissəsindən istifadə edərdi. Daha mürəkkəb Rust proqramları
yazdıqca asılılıqlar əlavə edəcəksiniz və layihəyə Cargo ilə başlasanız,
asılılıq əlavə etmək xeyli asan olacaq.

Rust layihələrinin böyük əksəriyyəti Cargo ilə işlədiyi üçün kitabın qalan
hissəsi sizin də ondan istifadə etdiyinizi güman edir.
[“Quraşdırma”][installation]<!-- ignore --> bölməsində müzakirə olunan rəsmi
quraşdırıcılardan istifadə etmisinizsə, Cargo Rust ilə birlikdə quraşdırılıb.
Rust-ı başqa üsulla quraşdırmısınızsa, terminalınıza aşağıdakını daxil edərək
Cargo-nun quraşdırılıb-quraşdırılmadığını yoxlayın:

```console
$ cargo --version
```

Versiya nömrəsi görürsünüzsə, deməli, Cargo var! `command
not found` kimi xəta görürsünüzsə, Cargo-nu ayrıca necə quraşdıracağınızı
öyrənmək üçün quraşdırma üsulunuzun dokumentasiyasına baxın.

### Cargo ilə layihə yaratmaq

Gəlin Cargo ilə yeni layihə yaradaq və onun ilkin “Hello, world!” layihəmizdən
nə ilə fərqləndiyinə baxaq. _projects_ direktoriyanıza (və ya kodunuzu saxlamaq
qərarına gəldiyiniz yerə) qayıdın. Sonra istənilən əməliyyat sistemində
aşağıdakını işə salın:

```console
$ cargo new hello_cargo
$ cd hello_cargo
```

Birinci komanda _hello_cargo_ adlı yeni direktoriya və layihə yaradır.
Layihəmizi _hello_cargo_ adlandırdıq və Cargo onun fayllarını eyni adlı
direktoriyada yaradır.

_hello_cargo_ direktoriyasına keçin və fayllara baxın. Cargo-nun bizim üçün iki
fayl və bir direktoriya yaratdığını görəcəksiniz: _Cargo.toml_ faylı və içində
_main.rs_ faylı olan _src_ direktoriyası.

O, həmçinin _.gitignore_ faylı ilə birlikdə yeni Git repozitoriyası da yaradıb. `cargo new` komandasını mövcud Git repozitoriyasının
içində işə salsanız, Git faylları yaradılmayacaq; bu davranışı
`cargo new --vcs=git` istifadə edərək dəyişə bilərsiniz.

> Qeyd: Git geniş yayılmış versiya nəzarəti sistemidir. `--vcs` *flag*-i ilə `cargo new`-un başqa versiya nəzarəti sistemindən
> istifadə etməsini və ya heç bir versiya nəzarəti sistemindən istifadə
> etməməsini təyin edə bilərsiniz. Mövcud seçimləri görmək üçün
> `cargo new --help` komandasını işə salın.

_Cargo.toml_ faylını seçdiyiniz mətn redaktorunda açın. O, Listing 1-2-dəki
koda bənzəməlidir.

<Listing number="1-2" file-name="Cargo.toml" caption="`cargo new` tərəfindən yaradılmış *Cargo.toml* faylının məzmunu">

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2024"

[dependencies]
```

</Listing>

Bu fayl Cargo-nun konfiqurasiya formatı olan
[_TOML_][toml]<!-- ignore --> (_Tom’s Obvious, Minimal Language_) formatındadır.

Birinci sətir, `[package]`, bölmə başlığıdır: o, sonrakı bəyanatların
(statements) paketi konfiqurasiya etdiyini göstərir. Bu fayla daha çox məlumat
əlavə etdikcə başqa bölmələr də əlavə edəcəyik.

Sonrakı üç sətir Cargo-nun proqramınızı kompilyasiya etmək üçün ehtiyac duyduğu
konfiqurasiya məlumatını təyin edir: ad, versiya və istifadə olunacaq Rust
buraxılışı. `edition` açarından [Əlavə E-də][appendix-e]<!-- ignore -->
danışacağıq.

Son sətir, `[dependencies]`, layihənizin asılılıqlarını sadalayacağınız
bölmənin başlanğıcıdır. Rust-da kod paketləri _crate_ adlanır. Bu layihə
üçün başqa *crate*-lərə ehtiyacımız olmayacaq, amma 2-ci fəsildəki ilk layihədə
olacaq, ona görə də asılılıqlar bölməsindən o zaman istifadə edəcəyik.

İndi _src/main.rs_ faylını açın və baxın:

<span class="filename">Fayl adı: src/main.rs</span>

```rust
fn main() {
    println!("Hello, world!");
}
```

Cargo sizin üçün eynilə Listing 1-1-də yazdığımız kimi “Hello, world!” proqramı
yaradıb! İndiyədək bizim layihə ilə Cargo-nun yaratdığı layihə arasındakı
fərqlər bunlardır: Cargo kodu _src_ direktoriyasına yerləşdirib, bizim isə kök
direktoriyada _Cargo.toml_ konfiqurasiya faylımız var.

Cargo mənbə fayllarınızın _src_ direktoriyasının içində olmasını gözləyir.
Layihənin kök direktoriyası yalnız README faylları, lisenziya məlumatı,
konfiqurasiya faylları və kodunuzla əlaqəsi olmayan digər şeylər üçündür.
Cargo-dan istifadə layihələrinizi səliqəli saxlamağa kömək edir. Hər şeyin öz
yeri var və hər şey öz yerindədir.

“Hello, world!” layihəsində etdiyimiz kimi Cargo-dan istifadə etməyən layihəyə
başlamısınızsa, onu Cargo istifadə edən layihəyə çevirə bilərsiniz. Layihə
kodunu _src_ direktoriyasına köçürün və uyğun _Cargo.toml_ faylı yaradın. Həmin
_Cargo.toml_ faylını əldə etməyin asan üsulu `cargo init` komandasını işə
salmaqdır; o, faylı sizin üçün avtomatik yaradacaq.

### Cargo layihəsinin build edilməsi və işə salınması

İndi “Hello, world!” proqramını Cargo ilə *build* edib işə saldıqda nəyin fərqli
olduğuna baxaq! _hello_cargo_ direktoriyanızda aşağıdakı komandanı daxil edərək
layihənizi *build* edin:

```console
$ cargo build
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs
```

Bu komanda icra olunan faylı cari direktoriyanızda deyil,
_target/debug/hello_cargo_ (Windows-da _target\debug\hello_cargo.exe_)
ünvanında yaradır. Defolt olaraq *debug* *build*-i yaradıldığı üçün Cargo binar
faylı _debug_ adlı direktoriyaya yerləşdirir. İcra olunan faylı bu komanda ilə
işə sala bilərsiniz:

```console
$ ./target/debug/hello_cargo # or .\target\debug\hello_cargo.exe on Windows
Hello, world!
```

Hər şey qaydasındadırsa, terminalda `Hello, world!` çap olunmalıdır. `cargo
build` komandasını ilk dəfə işə salmaq Cargo-nun kök səviyyədə yeni fayl
yaratmasına da səbəb olur: _Cargo.lock_. Bu fayl layihənizdəki asılılıqların
dəqiq versiyalarını izləyir. Bu layihənin asılılıqları yoxdur, ona görə də fayl
demək olar ki, boşdur. Bu faylı heç vaxt əl ilə dəyişməli olmayacaqsınız; Cargo
onun məzmununu sizin üçün idarə edir.

Layihəni indicə `cargo build` ilə *build* edib, `./target/debug/hello_cargo` ilə
işə saldıq. Lakin `cargo run` ilə kodu kompilyasiya edib, alınan icra olunan
faylı bir komanda ilə işə sala bilərik:

```console
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

`cargo run` istifadə etmək `cargo
build` işə salmağı, sonra isə binar faylın tam yolunu (path) yazmağı yadda
saxlamaqdan daha rahatdır, ona görə də *developer*-lərin çoxu `cargo
run` istifadə edir.

Diqqət edin ki, bu dəfə Cargo-nun `hello_cargo`-nu kompilyasiya etdiyini
göstərən çıxış görmədik. Cargo faylların dəyişmədiyini müəyyən etdi, ona görə
yenidən *build* etmədi, sadəcə binar faylı işə saldı. Mənbə kodunuzu dəyişsəydiniz,
Cargo layihəni işə salmazdan əvvəl yenidən *build* edərdi və siz bu çıxışı
görərdiniz:

```console
$ cargo run
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Cargo həmçinin `cargo check` adlı komanda da təqdim edir. Bu komanda kodunuzun
kompilyasiya olunduğuna əmin olmaq üçün onu tez yoxlayır, lakin icra olunan
fayl yaratmır:

```console
$ cargo check
   Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

Niyə icra olunan fayl istəməyəsiniz? Çox vaxt `cargo check` `cargo build`-dən
xeyli sürətlidir, çünki icra olunan faylın yaradılması addımını ötürür. Kod
yazarkən işinizi tez-tez yoxlayırsınızsa, `cargo check` layihənin hələ də
kompilyasiya olunub-olunmadığını daha tez öyrənməyə imkan verəcək! Buna görə də bir çox Rust-çı proqramını yazarkən onun
kompilyasiya olunduğuna əmin olmaq üçün vaxtaşırı `cargo check` işə salır.
Sonra icra olunan fayldan istifadə etməyə hazır olduqda `cargo build` işə
salırlar.

Gəlin Cargo haqqında indiyədək öyrəndiklərimizi xülasə edək:

- `cargo new` ilə layihə yarada bilərik.
- `cargo build` ilə layihəni *build* edə bilərik.
- `cargo run` ilə layihəni bir addımda *build* edib işə sala bilərik.
- `cargo check` ilə binar fayl yaratmadan layihəni xətalara görə yoxlaya
  bilərik.
- Cargo *build* nəticəsini kodumuzla eyni direktoriyada deyil, _target/debug_
  direktoriyasında saxlayır.

Cargo-dan istifadənin əlavə üstünlüyü ondadır ki, hansı əməliyyat sistemində
işləməyinizdən asılı olmayaraq, komandalar eynidir. Ona görə də bundan sonra
Linux və macOS üçün, Windows üçün ayrıca təlimatlar verməyəcəyik.

### Reliz üçün build

Layihəniz nəhayət reliz üçün hazır olduqda, onu optimizasiyalarla kompilyasiya etmək üçün `cargo build
--release` istifadə edə bilərsiniz. Bu komanda icra olunan faylı _target/debug_
əvəzinə _target/release_ direktoriyasında yaradacaq. Optimizasiyalar Rust
kodunuzun daha sürətli işləməsini təmin edir, lakin onları aktivləşdirmək
proqramınızın kompilyasiya müddətini uzadır. Buna görə iki
fərqli profil var. Biri inkişaf mərhələsi üçündür: burada kodu tez-tez və
sürətlə yenidən *build* etmək istəyirsiniz. Digəri isə istifadəçiyə verəcəyiniz
son proqram üçündür: o, təkrar-təkrar *build* edilməyəcək və mümkün qədər
sürətli işləməlidir. Kodunuzun icra müddətini bençmark edirsinizsə, mütləq
`cargo build --release` işə salın və _target/release_ içindəki icra olunan
fayl ilə bençmark edin.

<!-- Old headings. Do not remove or links may break. -->
<a id="cargo-as-convention"></a>

### Cargo konvensiyalarından istifadə

Sadə layihələrdə Cargo sadəcə `rustc` istifadə etməklə müqayisədə çox da
üstünlük vermir, lakin proqramlarınız mürəkkəbləşdikcə öz faydasını göstərəcək.
Proqramlar bir neçə fayldan ibarət olduqda və ya asılılığa ehtiyac duyduqda
*build* prosesini Cargo-ya həvalə etmək xeyli asandır.

`hello_cargo` layihəsi sadə olsa da, o, artıq Rust karyeranızın qalan
hissəsində istifadə edəcəyiniz real alətlərin çoxundan istifadə edir. Əslində,
istənilən mövcud layihə üzərində işləmək üçün kodu Git ilə əldə etmək, həmin
layihənin direktoriyasına keçmək və *build* etmək üçün aşağıdakı komandalardan
istifadə edə bilərsiniz:

```console
$ git clone example.org/someproject
$ cd someproject
$ cargo build
```

Cargo haqqında ətraflı məlumat üçün [onun dokumentasiyasına][cargo] baxın.

## Xülasə

Rust səyahətinizə artıq əla başlanğıc verdiniz! Bu fəsildə bunları öyrəndiniz:

- `rustup` ilə Rust-ın ən son stabil versiyasını quraşdırmaq.
- Rust-ı daha yeni versiyaya yeniləmək.
- Lokal quraşdırılmış dokumentasiyanı açmaq.
- Birbaşa `rustc` istifadə edərək, “Hello, world!” proqramı yazıb işə salmaq.
- Cargo konvensiyalarından istifadə edərək, yeni layihə yaradıb işə salmaq.

Rust kodunu oxumağa və yazmağa öyrəşmək üçün daha ciddi proqram yazmağın tam
vaxtıdır. Ona görə də 2-ci fəsildə ədəd tapma oyunu proqramı yazacağıq. Ümumi
proqramlaşdırma anlayışlarının Rust-da necə işlədiyini öyrənməklə başlamaq
istəyirsinizsə, 3-cü fəslə baxın, sonra 2-ci fəslə qayıdın.

[installation]: ch01-01-installation.html#quraşdırma
[toml]: https://toml.io
[appendix-e]: appendix-05-editions.html
[cargo]: https://doc.rust-lang.org/cargo/
