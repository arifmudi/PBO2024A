**Nama : Intan Nurzari**
**NIM : 235201035**



**A. INHERITANCE**

Single inheritance dalam Python adalah konsep di mana sebuah kelas (kelas anak) mewarisi sifat-sifat dan perilaku dari satu kelas induk. Ini adalah cara untuk mengorganisir dan mengelola kode dengan lebih efisien, mengurangi duplikasi, dan memfasilitasi pemeliharaan.

<b>*codingan*</b>
class Animal:
        def speak(self):
        return "Animal speaks"

class Dog(Animal):
        def bark(self):
        return "Woof!"

Dalam contoh di atas, kelas Dog mewarisi metode speak() dari kelas Animal. Ini    berarti kita dapat menggunakan metode tersebut tanpa harus mendefinisikannya    kembali di dalam kelas Dog.
<br>
> **Kapan menggunakan single inheritance**

<br>
* ***Sederhana dan Jelas*:** Ketika hierarki kelas sederhana dan hanya memerlukan satu kelas induk. Ini membuat kode lebih mudah dipahami.
* ***Reusabilitas*:** Saat Anda ingin menggunakan kembali kode yang ada di kelas induk tanpa membuat kompleksitas tambahan yang mungkin timbul dari multiple inheritance.
* ***Mempermudah Pemeliharaan*:** Dengan hanya satu kelas induk, jika ada perubahan di kelas induk, semua kelas anak yang mewarisi dapat langsung mendapatkan perubahan tersebut.
* ***Modeling Hubungan yang Jelas*:** Ketika hubungan antara kelas induk dan anak jelas dan tidak memerlukan fitur kompleks dari multiple inheritance.

Single inheritance adalah cara yang efisien dan terstruktur untuk mendefinisikan kelas dan hubungan di antara mereka. Ini ideal digunakan ketika hubungan antara kelas cukup sederhana dan tidak memerlukan kemampuan lebih dari satu kelas induk.

B.SUPER

Konsep super() dalam Python adalah cara untuk memanggil metode atau atribut dari kelas induk dalam konteks kelas anak. Ini sangat berguna dalam inheritance, terutama ketika kita ingin mewarisi konstruktor (metode **init**) dari kelas induk.
<br>
> **kapan dan mengapa menggunakan super**

* ***Mewarisi Konstruktor*:** Ketika kelas anak perlu menginisialisasi atribut yang didefinisikan dalam kelas induk, super() digunakan untuk memanggil konstruktor kelas induk.
* ***Multiple Inheritance*:** Dalam kasus pewarisan ganda, super() membantu menghindari masalah yang dikenal sebagai "diamond problem," di mana metode yang sama dapat diwarisi dari beberapa jalur.
* ***Keterbacaan dan Pemeliharaan*:** Menggunakan super() membuat kode lebih jelas dan memudahkan pemeliharaan. Jika Anda mengubah nama kelas induk, Anda hanya perlu memperbarui satu tempat.

<br>
> **Manfaat menggunakan super**

* **Mengurangi Duplikasi Kode**: Anda tidak perlu menulis ulang kode yang ada di kelas induk.
* <b>*Meningkatkan Keterbacaan:*</b> Memudahkan pemahaman tentang bagaimana kelas anak berinteraksi dengan kelas induk.
* <b>*Fleksibilitas:*</b> Memudahkan perubahan di masa depan, misalnya saat mengubah hirarki kelas.

<br>
***codingan***
class Orang:
def **init**(self, nama, usia):
self.nama = nama
self.usia = usia

```
def info(self):
    return f"Nama: {self.nama}, Usia: {self.usia}"
```

class Intan(Orang):
def **init**(self, nama, usia, pekerjaan):
super().**init**(nama, usia) # Memanggil konstruktor dari kelas Orang
self.pekerjaan = pekerjaan

```
def info(self):
    # Menggunakan metode info dari kelas induk
    return super().info() + f", Pekerjaan: {self.pekerjaan}"
```

#Contoh penggunaan
orang1 = Intan("Intan", 30, "Programmer")
print(orang1.info())

Menggunakan super() dalam inheritance di Python adalah praktik yang baik, terutama ketika Anda ingin mewarisi konstruktor dan memastikan keterhubungan yang baik antara kelas induk dan anak. Ini meningkatkan fleksibilitas dan keterbacaan kode.


3. Jenis-Jenis Inheritance dalam OOP

<br>
| **Jenis-jenis Inheritance** | **Definisi** | **Kapan Digunakan** | **Cara penggunaan** |
| ----------------------- | -------- | --------------- | --------------- |
| Multi level Inheritance | Kelas anak mewarisi kelas induk, yang kemudian diwarisi lagi oleh kelas lainnya. | Ketika ingin membuat hierarki kelas panjang. | class C(B): pass dan class B(A): pass |
| Hirarki Inheritance | Beberapa kelas anak mewarisi kelas induk yang sama. | Ketika beberapa kelas membutuhkan sifat yang sama dari satu kelas induk. | class B(A): pass dan class C(A): pass |
| Hybird Inheritance | Kombinasi dari berbagai jenis inheritance, seperti multiple dan multilevel. | Ketika membutuhkan kombinasi dari beberapa inheritance untuk kasus kompleks. | class D(B, C): pass |
| Multiple Inheritance | Kelas anak mewarisi lebih dari satu kelas induk | Ketika kelas membutuhkan sifat dari beberapa kelas induk. | class C(A, B): pass |

*codingan*

1. Single Inheritance

```
class Hewan:
```

def suara(self):
return "Suara Hewan"

class Kucing(Hewan):
def suara(self):
return "Meow, saya Intan."

intan\_kucing = Kucing()
print(intan\_kucing.suara()) # Output: Meow, saya Intan.


2. Multiple Inheritance


```
 class A:
```

def metode\_a(self):
return "Metode A"

class B:
def metode\_b(self):
return "Metode B"

class C(A, B):
def metode\_c(self):
return "Metode C, ini adalah Intan."

intan\_objek = C()
print(intan\_objek.metode\_a()) # Output: Metode A
print(intan\_objek.metode\_b()) # Output: Metode B


3. Multi level Inheritance


```
 class Hewan:
```

def suara(self):
return "Suara Hewan"

class Kucing(Hewan):
def suara(self):
return "Meow"

class KucingPersia(Kucing):
def suara(self):
return "Meow Persia, saya Intan."

intan\_kucing\_persia = KucingPersia()
print(intan\_kucing\_persia.suara()) # Output: Meow Persia, saya Intan.


4. Hirarki Inheritance


```
 class Hewan:
```

def suara(self):
return "Suara Hewan"

class Kucing(Hewan):
def suara(self):
return "Meow, saya Intan."

class Anjing(Hewan):
def suara(self):
return "Bark, saya Intan."

intan\_kucing = Kucing()
intan\_anjing = Anjing()
print(intan\_kucing.suara()) # Output: Meow, saya Intan.
print(intan\_anjing.suara()) # Output: Bark, saya Intan.

5. Hybird Inheritance

 class A:

def metode\_a(self):
return "Metode A"

class B(A):
def metode\_b(self):
return "Metode B"

class C(A):
def metode\_c(self):
return "Metode C"

class D(B, C):
def metode\_d(self):
return "Metode D, saya Intan."

intan\_objek\_hybrid = D()
print(intan\_objek\_hybrid.metode\_a()) # Output: Metode A
print(intan\_objek\_hybrid.metode\_b()) # Output: Metode B
print(intan\_objek\_hybrid.metode\_c()) # Output: Metode C


3. ***overwrite method***

Overwrite Method atau method overriding adalah kemampuan dalam pemrograman berorientasi objek (OOP) di mana sebuah kelas anak dapat menyediakan implementasi yang spesifik untuk metode yang sudah didefinisikan di kelas induk. Dengan cara ini, metode di kelas anak dapat menggantikan (menimpa) perilaku metode di kelas induk, memungkinkan perilaku yang lebih sesuai dengan kebutuhan kelas anak.
<br>
> ***Manfaat Overwrite Method***

1. Kustomisasi Perilaku: Memberikan kemampuan untuk menyesuaikan atau memperluas fungsi dari kelas induk tanpa mengubah kelas induk itu sendiri.
2. Polimorfisme: Memungkinkan metode yang sama untuk memiliki perilaku berbeda tergantung pada objek yang memanggilnya, mendukung prinsip polimorfisme.
3. Keterbacaan dan Pemeliharaan: Kode menjadi lebih mudah dibaca dan dirawat, karena perilaku yang spesifik terletak di kelas yang relevan.

> ***Kapan digunakan***

1. Ketika ada kebutuhan untuk mengubah perilaku metode dari kelas induk di dalam kelas anak.
2. Ketika kita ingin menerapkan logika yang lebih spesifik di dalam subclass, sementara tetap menjaga interface yang sama dengan superclass.

> ***Mengapa Digunakan***

1. Untuk menghindari duplikasi kode, dengan menggunakan kembali metode di kelas induk tetapi dengan penyesuaian sesuai kebutuhan subclass.
2. Untuk meningkatkan modularitas dan fleksibilitas kode.

*Codingan*

class Induk:
def tampilkan\_nama(self):
return "Nama dari kelas Induk"

class Intan(Induk):
def tampilkan\_nama(self): # Overwriting method
return "Nama dari kelas Intan"
<br>
> Penggunaan

induk = Induk()
intan = Intan()

print(induk.tampilkan\_nama()) # Output: Nama dari kelas Induk
print(intan.tampilkan\_nama()) # Output: Nama dari kelas Intan

Dengan cara ini, kita dapat memanfaatkan inheritance dan method overriding untuk menciptakan perilaku yang lebih spesifik dan sesuai dengan kebutuhan kelas anak.

> Kapan Menggunakan Pewarisan

1. Ketika Ada Hubungan "Is-a":
Gunakan inheritance saat ada hubungan yang jelas antara dua kelas. Misalnya, jika kita memiliki kelas Hewan, dan kelas Kucing, di mana Kucing adalah jenis dari Hewan. Ini adalah contoh hubungan "adalah".
2. untuk Menghindari Duplikasi Kode:
Jika beberapa kelas memiliki kode yang sama, inheritance memungkinkan untuk menulis kode tersebut di satu tempat (kelas induk). Dengan cara ini, kelas lain (kelas anak) dapat menggunakan kode yang sama tanpa menyalin ulang.
3. Ketika Perlu Menyesuaikan Perilaku:
Jika ingin mengubah cara kerja metode yang sudah ada di kelas induk, inheritance bisa digunakan. Kelas anak dapat menimpa metode tersebut dengan implementasi yang sesuai dengan kebutuhannya.
4. Untuk Mendukung Polimorfisme:
Inheritance memungkinkan objek dari kelas anak diperlakukan sebagai objek dari kelas induk. Ini membuat kode lebih fleksibel, karena metode yang sama dapat memberikan hasil yang berbeda tergantung pada objek yang digunakan.
5. Merepresentasikan Konsep Dunia Nyata:
Inheritance sangat berguna untuk menggambarkan hubungan nyata. Misalnya, kelas Kendaraan dapat memiliki subclass seperti Mobil dan Motor. Ini membantu menciptakan struktur yang mudah dipahami.
6. Mengelompokkan Kelas yang Mirip:
Jika ada beberapa kelas yang memiliki atribut dan metode serupa, inheritance memungkinkan untuk mengelompokkan kelas-kelas tersebut di bawah satu kelas induk. Hal ini mempermudah pengelolaan dan penggunaan.
7. Menjaga Konsistensi:
Dengan inheritance, semua kelas anak dapat mengikuti pola atau interface yang sama. Jika ada metode yang sama di beberapa kelas dengan implementasi yang berbeda, inheritance membantu menjaga konsistensi ini.
8. Memudahkan Pemeliharaan Kode:
Ketika ada perubahan di kelas induk, semua kelas anak yang mewarisi akan otomatis mendapatkan perubahan tersebut. Ini membuat pemeliharaan dan pembaruan kode menjadi lebih mudah.

> Kapan menggunakan non pewarisan (komposisi)

1. Ketika Hierarki Kelas Tidak Jelas:
Jika tidak ada hubungan "is-a" yang jelas antara objek, lebih baik menggunakan komposisi daripada pewarisan. Misalnya, jika Kendaraan dan Mesin tidak memiliki hubungan hierarkis yang kuat, lebih baik menggabungkannya.
2. Untuk Menghindari Masalah Dengan Pewarisan Ganda:
Jika menggunakan pewarisan ganda dapat menyebabkan kebingungan atau konflik, komposisi adalah pilihan yang lebih baik. Ini menghindari masalah seperti "diamond problem" di mana dua kelas induk memiliki metode yang sama.
3. Ketika Kelas Perlu Fleksibilitas Tinggi:
Jika ada kebutuhan untuk mengubah perilaku objek secara dinamis, komposisi memungkinkan objek untuk mengubah perilakunya dengan mengubah objek yang dimilikinya, tanpa perlu memodifikasi hierarki kelas.
4. Untuk Memisahkan Tanggung Jawab:
Jika ingin memisahkan fungsionalitas menjadi beberapa bagian yang berbeda, komposisi membantu dalam menciptakan kelas yang memiliki tanggung jawab yang lebih spesifik. Ini membuat kode lebih mudah dikelola dan dipahami.
5. Ketika Menggunakan Kelas Abstrak dan Interface:
Jika ingin mendefinisikan kontrak tanpa harus mengikatnya pada implementasi spesifik, menggunakan interface atau kelas abstrak adalah cara yang tepat. Ini memberi fleksibilitas kepada kelas lain untuk mengimplementasikan metode dengan cara mereka sendiri.
6. Saat Membutuhkan Agregasi:
Jika ada kebutuhan untuk mengelola objek yang dapat hidup secara terpisah, seperti Sekolah dan Siswa, di mana Siswa dapat ada tanpa keterikatan langsung pada Sekolah, gunakan agregasi.
7. Ketika Kode Harus Mudah Diuji:
Kode yang menggunakan komposisi dan fungsi terpisah seringkali lebih mudah untuk diuji secara unit. Dengan memisahkan fungsionalitas, setiap bagian dapat diuji secara independen.

Menggunakan non-pewarisan dengan tepat dapat meningkatkan keterbacaan, pemeliharaan, dan fleksibilitas kode.
