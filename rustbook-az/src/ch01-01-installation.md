## Quraşdırma

İlk addım Rust-ı quraşdırmaqdır. Rust-ı `rustup` vasitəsilə yükləyəcəyik; bu, Rust versiyalarını və əlaqəli alətləri idarə etmək üçün
komanda sətri (command line) alətidir. Yükləmə üçün internet bağlantısı
lazımdır.

> Qeyd: Hər hansı səbəbdən `rustup`-dan istifadə etmək istəmirsinizsə, başqa
> seçimlər üçün [Rust-ın digər quraşdırma üsulları səhifəsinə][otherinstall]
> baxın.

Aşağıdakı addımlar Rust kompilyatorunun ən son stabil
versiyasını quraşdırır. Rust-ın stabillik zəmanətləri sayəsində kitabdakı kompilyasiya olunan bütün
nümunələr Rust-ın daha yeni versiyalarında da kompilyasiya olunacaq. Çıxış versiyadan
versiyaya bir qədər fərqlənə bilər, çünki Rust xəta mesajlarını
və xəbərdarlıqları tez-tez təkmilləşdirir. Başqa sözlə, bu addımlarla
quraşdırdığınız Rust-ın istənilən daha yeni, stabil versiyası bu kitabın
məzmunu ilə gözlənildiyi kimi işləməlidir.

> ### Komanda sətri notasiyası
>
> Bu fəsildə və bütün kitab boyu terminalda işlədilən bəzi komandaları
> göstərəcəyik. Terminala daxil etməli olduğunuz komandaların hamısı `$` ilə
> başlayır. `$` simvolunu yazmağa ehtiyac yoxdur; bu, hər komandanın başlanğıcını
> göstərən komanda sətri *prompt*-udur. `$` ilə başlamayanlar adətən əvvəlki
> komandanın çıxışını göstərir. Bundan əlavə, PowerShell-ə aid nümunələrdə `$`
> əvəzinə `>` işlədiləcək.

### Linux və ya macOS-da `rustup`-ın quraşdırılması

Linux və ya macOS istifadə edirsinizsə, terminal açın və aşağıdakı komandanı
daxil edin:

```console
$ curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

Komanda skript yükləyir və `rustup` alətinin quraşdırılmasına başlayır;
bu alət Rust-ın ən son stabil versiyasını quraşdırır. Sizdən parolunuz istənə
bilər. Quraşdırma uğurlu olarsa, aşağıdakı mesaj görünəcək:

```text
Rust is installed now. Great!
```

Sizə həmçinin _linker_ lazım olacaq — bu, Rust-ın kompilyasiya nəticələrini bir
faylda birləşdirmək üçün istifadə etdiyi proqramdır. Çox güman ki, o, sizdə
artıq var. *Linker* xətaları alırsınızsa, C kompilyatoru
quraşdırmalısınız; onun tərkibində adətən *linker* də olur. C kompilyatoru həm də ona
görə faydalıdır ki, bəzi geniş yayılmış Rust paketləri (packages) C kodundan
asılıdır və C kompilyatoru tələb edir.

macOS-da C kompilyatorunu bu komandanı işə salmaqla əldə edə bilərsiniz:

```console
$ xcode-select --install
```

Linux istifadəçiləri adətən öz distributivlərinin dokumentasiyasına uyğun olaraq GCC və ya Clang quraşdırmalıdırlar. Məsələn,
Ubuntu istifadə edirsinizsə, `build-essential` paketini quraşdıra bilərsiniz.

### Windows-da `rustup`-ın quraşdırılması

Windows-da [https://www.rust-lang.org/tools/install][install]<!-- ignore
--> ünvanına keçin və Rust-ın quraşdırılması üçün təlimatlara əməl edin.
Quraşdırmanın müəyyən mərhələsində sizdən Visual Studio quraşdırmaq istəniləcək.
O, proqramları kompilyasiya etmək üçün lazım olan *linker*-i və yerli
kitabxanaları təmin edir. Bu addımla bağlı əlavə köməyə ehtiyacınız
varsa,
[https://rust-lang.github.io/rustup/installation/windows-msvc.html][msvc]<!--
ignore --> səhifəsinə baxın.

Kitabın qalan hissəsində həm _cmd.exe_, həm də PowerShell-də işləyən
komandalardan istifadə olunur. Konkret fərqlər olarsa, hansından istifadə
etməli olduğunuzu izah edəcəyik.

### Problemlərin aradan qaldırılması

Rust-ın düzgün quraşdırılıb-quraşdırılmadığını yoxlamaq üçün *shell* açın və
bunu daxil edin:

```console
$ rustc --version
```

Çıxmış ən son stabil versiyanın versiya nömrəsini, commit heşini və commit tarixini aşağıdakı formatda görməlisiniz:

```text
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

Bu məlumatı görürsünüzsə, Rust-ı uğurla quraşdırmısınız! Görmürsünüzsə,
Rust-ın `%PATH%` sistem dəyişənində (system variable) olub-olmadığını aşağıdakı
kimi yoxlayın.

Windows CMD-də bunu işlədin:

```console
> echo %PATH%
```

PowerShell-də bunu işlədin:

```powershell
> echo $env:Path
```

Linux və macOS-da bunu işlədin:

```console
$ echo $PATH
```

Hər şey düzgündürsə və Rust yenə də işləmirsə, kömək ala biləcəyiniz bir sıra
yerlər var. Digər Rust-çılarla (Rustacean, özümüzə verdiyimiz zarafatyana ləqəb) necə
əlaqə saxlamağı [icma səhifəsindən][community] öyrənin.

### Yeniləmə və silmə

Rust `rustup` vasitəsilə quraşdırıldıqdan sonra onu yeni çıxmış versiyaya
yeniləmək asandır. *Shell*-inizdə aşağıdakı yeniləmə skriptini işə
salın:

```console
$ rustup update
```

Rust-ı və `rustup`-ı silmək üçün *shell*-inizdə aşağıdakı silmə
skriptini işə salın:

```console
$ rustup self uninstall
```

<!-- Old headings. Do not remove or links may break. -->
<a id="local-documentation"></a>

### Lokal dokumentasiyanın oxunması

Rust quraşdırılarkən dokumentasiyanın lokal surəti də quraşdırılır ki, onu
oflayn oxuya biləsiniz. Lokal dokumentasiyanı brauzerinizdə açmaq
üçün `rustup doc` komandasını işə salın.

Standart kitabxanadakı hər hansı tipin və ya funksiyanın nə etdiyinə, yaxud
ondan necə istifadə edəcəyinizə əmin deyilsinizsə, cavabı proqramlaşdırma
interfeysinin (Application Programming Interface, API) dokumentasiyasında tapa
bilərsiniz!

<!-- Old headings. Do not remove or links may break. -->
<a id="text-editors-and-integrated-development-environments"></a>

### Mətn redaktorları və IDE-lərdən istifadə

Rust kodu yazmaq üçün hansı alətlərdən istifadə etdiyinizin bu kitab üçün
fərqi yoxdur. Demək olar ki, istənilən mətn redaktoru işinizi
görəcək! Bununla belə, bir çox mətn redaktorlarında və inteqrasiya olunmuş
inkişaf mühitlərində (Integrated Development Environments, IDEs) daxili Rust
dəstəyi var. Bir çox redaktor və IDE-nin kifayət qədər aktual siyahısını həmişə
Rust veb saytındakı [alətlər səhifəsində][tools] tapa bilərsiniz.

### Bu kitabla oflayn işləmək

Bir neçə nümunədə standart kitabxanadan kənar Rust paketlərindən istifadə
edəcəyik. Həmin nümunələr üzərində işləmək üçün ya internet bağlantınız
olmalıdır, ya da həmin asılılıqları (dependencies) əvvəlcədən yükləməlisiniz.
Asılılıqları əvvəlcədən yükləmək üçün aşağıdakı komandaları işə sala
bilərsiniz. (`cargo`-nun nə olduğunu və bu komandaların hər birinin nə etdiyini
daha sonra ətraflı izah edəcəyik.)

<!-- When updating the version of `rand` used, also update the version of
`rand` used in these files so they all match:

* ch02-00-guessing-game-tutorial.md
* ch07-04-bringing-paths-into-scope-with-the-use-keyword.md
* ch14-03-cargo-workspaces.md
-->

```console
$ cargo new get-dependencies
$ cd get-dependencies
$ cargo add rand@0.10.1 trpl@0.2.0
```

Bu, həmin paketlərin yüklənmiş fayllarını keşləyəcək, beləliklə onları
sonra yenidən yükləməyə ehtiyac olmayacaq. Bu komandanı işə saldıqdan sonra
`get-dependencies` direktoriyasını saxlamağa ehtiyac yoxdur. Bu
komandanı işə salmısınızsa, kitabın qalan hissəsində bütün `cargo` komandaları
ilə `--offline` *flag*-indən (bayraq) istifadə edə bilərsiniz; onda şəbəkəyə qoşulmağa cəhd etmək əvəzinə bu keşlənmiş versiyalar istifadə
olunacaq.

[otherinstall]: https://forge.rust-lang.org/infra/other-installation-methods.html
[install]: https://www.rust-lang.org/tools/install
[msvc]: https://rust-lang.github.io/rustup/installation/windows-msvc.html
[community]: https://www.rust-lang.org/community
[tools]: https://www.rust-lang.org/tools
