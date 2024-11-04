

Nama : Intan Nurzari
NIM : 235201035



___Inheritance__

######
1. Single inheritance dalam Python adalah konsep di mana sebuah kelas (kelas anak) mewarisi sifat-sifat dan perilaku dari satu kelas induk. Ini adalah cara untuk mengorganisir dan mengelola kode dengan lebih efisien, mengurangi duplikasi, dan memfasilitasi pemeliharaan.

_codingan_:
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Woof!"

Dalam contoh di atas, kelas Dog mewarisi metode speak() dari kelas Animal. Ini berarti kita dapat menggunakan metode tersebut tanpa harus mendefinisikannya kembali di dalam kelas Dog.

__Kapan menggunakan single inheritance__

1. _Sederhana dan Jelas_: Ketika hierarki kelas sederhana dan hanya memerlukan satu kelas induk. Ini membuat kode lebih mudah dipahami.

2. _Reusabilitas_: Saat Anda ingin menggunakan kembali kode yang ada di kelas induk tanpa membuat kompleksitas tambahan yang mungkin timbul dari multiple inheritance.

3. _Mempermudah Pemeliharaan_: Dengan hanya satu kelas induk, jika ada perubahan di kelas induk, semua kelas anak yang mewarisi dapat langsung mendapatkan perubahan tersebut.

4. _Modeling Hubungan yang Jelas_: Ketika hubungan antara kelas induk dan anak jelas dan tidak memerlukan fitur kompleks dari multiple inheritance.

Single inheritance adalah cara yang efisien dan terstruktur untuk mendefinisikan kelas dan hubungan di antara mereka. Ini ideal digunakan ketika hubungan antara kelas cukup sederhana dan tidak memerlukan kemampuan lebih dari satu kelas induk.


######
___Super()__
2. Konsep super() dalam Python adalah cara untuk memanggil metode atau atribut dari kelas induk dalam konteks kelas anak. Ini sangat berguna dalam inheritance, terutama ketika kita ingin mewarisi konstruktor (metode __init__) dari kelas induk.

__kapan dan mengapa menggunakan super__

1. _Mewarisi Konstruktor_: Ketika kelas anak perlu menginisialisasi atribut yang didefinisikan dalam kelas induk, super() digunakan untuk memanggil konstruktor kelas induk.

2. _Multiple Inheritance_: Dalam kasus pewarisan ganda, super() membantu menghindari masalah yang dikenal sebagai "diamond problem," di mana metode yang sama dapat diwarisi dari beberapa jalur.

3. _Keterbacaan dan Pemeliharaan_: Menggunakan super() membuat kode lebih jelas dan memudahkan pemeliharaan. Jika Anda mengubah nama kelas induk, Anda hanya perlu memperbarui satu tempat.

__Manfaat menggunakan super__

_Mengurangi Duplikasi Kode_: Anda tidak perlu menulis ulang kode yang ada di kelas induk.
_Meningkatkan Keterbacaan_: Memudahkan pemahaman tentang bagaimana kelas anak berinteraksi dengan kelas induk.
_Fleksibilitas_: Memudahkan perubahan di masa depan, misalnya saat mengubah hirarki kelas.

_codingan_
class Orang:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def info(self):
        return f"Nama: {self.nama}, Usia: {self.usia}"

class Intan(Orang):
    def __init__(self, nama, usia, pekerjaan):
        super().__init__(nama, usia)  # Memanggil konstruktor dari kelas Orang
        self.pekerjaan = pekerjaan

    def info(self):
        # Menggunakan metode info dari kelas induk
        return super().info() + f", Pekerjaan: {self.pekerjaan}"

 #Contoh penggunaan
orang1 = Intan("Intan", 30, "Programmer")
print(orang1.info())

Menggunakan super() dalam inheritance di Python adalah praktik yang baik, terutama ketika Anda ingin mewarisi konstruktor dan memastikan keterhubungan yang baik antara kelas induk dan anak. Ini meningkatkan fleksibilitas dan keterbacaan kode.


######
3. Jenis-Jenis Inheritance dalam OOP

|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Single Inheritance                                                            |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Mewarisi dari satu kelas induk.                                               |
| **Contoh Implementasi**     | `class B(A): pass`                                                            |
| **Kapan Menggunakan**       | Ketika kelas turunan hanya perlu satu dasar dari kelas induk.                 |
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Multiple Inheritance                                                          |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Mewarisi dari lebih dari satu kelas induk.                                    |
| **Contoh Implementasi**     | `class C(A, B): pass`                                                         |
| **Kapan Menggunakan**       | Ketika kelas turunan membutuhkan sifat dari beberapa kelas induk.             |
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Multilevel Inheritance                                                        |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Mewarisi dalam beberapa level (kelas induk, anak, cucu).                      |
| **Contoh Implementasi**     | `class C(B): pass` dan `class B(A): pass`                                     |
| **Kapan Menggunakan**       | Ketika ingin membuat hierarki yang panjang atau rantai turunan.               |
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Hierarchical Inheritance                                                      |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Satu kelas induk diwarisi oleh beberapa kelas turunan.                        |
| **Contoh Implementasi**     | `class B(A): pass` dan `class C(A): pass`                                     |
| **Kapan Menggunakan**       | Ketika beberapa kelas perlu memiliki sifat yang sama dari satu kelas induk.   |
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Hybrid Inheritance                                                            |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Gabungan dari beberapa tipe inheritance, termasuk multiple dan multilevel.    |
| **Contoh Implementasi**     | `class C(A, B): pass` (A dan B bisa saling terkait)                           |
| **Kapan Menggunakan**       | Ketika membutuhkan kombinasi sifat dari beberapa inheritance untuk kasus      |
|                             | yang  kompleks.                                                               |
|-------------------------------------------------------------------------------------------------------------|

_codingan_

1. Single Inheritance 
    ###
        class Hewan:
    def suara(self):
        return "Suara Hewan"

class Kucing(Hewan):
    def suara(self):
        return "Meow, saya Intan."

intan_kucing = Kucing()
print(intan_kucing.suara())  # Output: Meow, saya Intan.
###

2. Multiple Inheritance
    ###
        class A:
    def metode_a(self):
        return "Metode A"

class B:
    def metode_b(self):
        return "Metode B"

class C(A, B):
    def metode_c(self):
        return "Metode C, ini adalah Intan."

intan_objek = C()
print(intan_objek.metode_a())  # Output: Metode A
print(intan_objek.metode_b())  # Output: Metode B
###

3. Multi level Inheritance 
    ###
        class Hewan:
    def suara(self):
        return "Suara Hewan"

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class KucingPersia(Kucing):
    def suara(self):
        return "Meow Persia, saya Intan."

intan_kucing_persia = KucingPersia()
print(intan_kucing_persia.suara())  # Output: Meow Persia, saya Intan.
###

4. Hirarki Inheritance 
    ###
        class Hewan:
    def suara(self):
        return "Suara Hewan"

class Kucing(Hewan):
    def suara(self):
        return "Meow, saya Intan."

class Anjing(Hewan):
    def suara(self):
        return "Bark, saya Intan."

intan_kucing = Kucing()
intan_anjing = Anjing()
print(intan_kucing.suara())  # Output: Meow, saya Intan.
print(intan_anjing.suara())  # Output: Bark, saya Intan.
###

5. Hybird Inheritance 
    
    ###
        class A:
    def metode_a(self):
        return "Metode A"

class B(A):
    def metode_b(self):
        return "Metode B"

class C(A):
    def metode_c(self):
        return "Metode C"

class D(B, C):
    def metode_d(self):
        return "Metode D, saya Intan."

intan_objek_hybrid = D()
print(intan_objek_hybrid.metode_a())  # Output: Metode A
print(intan_objek_hybrid.metode_b())  # Output: Metode B
print(intan_objek_hybrid.metode_c())  # Output: Metode C
###



3. ___overwrite method___

Overwrite Method atau method overriding adalah kemampuan dalam pemrograman berorientasi objek (OOP) di mana sebuah kelas anak dapat menyediakan implementasi yang spesifik untuk metode yang sudah didefinisikan di kelas induk. Dengan cara ini, metode di kelas anak dapat menggantikan (menimpa) perilaku metode di kelas induk, memungkinkan perilaku yang lebih sesuai dengan kebutuhan kelas anak.


___Manfaat Overwrite Method___

1. Kustomisasi Perilaku: Memberikan kemampuan untuk menyesuaikan atau memperluas fungsi dari kelas induk tanpa mengubah kelas induk itu sendiri.
2. Polimorfisme: Memungkinkan metode yang sama untuk memiliki perilaku berbeda tergantung pada objek yang memanggilnya, mendukung prinsip polimorfisme.
3. Keterbacaan dan Pemeliharaan: Kode menjadi lebih mudah dibaca dan dirawat, karena perilaku yang spesifik terletak di kelas yang relevan.

___Kapan digunakan___

1. Ketika ada kebutuhan untuk mengubah perilaku metode dari kelas induk di dalam kelas anak.
2. Ketika kita ingin menerapkan logika yang lebih spesifik di dalam subclass, sementara tetap menjaga interface yang sama dengan superclass.

___Mengapa Digunakan___

1. Untuk menghindari duplikasi kode, dengan menggunakan kembali metode di kelas induk tetapi dengan penyesuaian sesuai kebutuhan subclass.
2. Untuk meningkatkan modularitas dan fleksibilitas kode.

_Codingan_

class Induk:
    def tampilkan_nama(self):
        return "Nama dari kelas Induk"

class Intan(Induk):
    def tampilkan_nama(self):  # Overwriting method
        return "Nama dari kelas Intan"

# Penggunaan
induk = Induk()
intan = Intan()

print(induk.tampilkan_nama())  # Output: Nama dari kelas Induk
print(intan.tampilkan_nama())   # Output: Nama dari kelas Intan

Dengan cara ini, kita dapat memanfaatkan inheritance dan method overriding untuk menciptakan perilaku yang lebih spesifik dan sesuai dengan kebutuhan kelas anak.


######
5. Kapan Menggunakan Pewarisan 

1. Ketika Ada Hubungan "Is-a":
Gunakan inheritance saat ada hubungan yang jelas antara dua kelas. Misalnya, jika kita memiliki kelas Hewan, dan kelas Kucing, di mana Kucing adalah jenis dari Hewan. Ini adalah contoh hubungan "adalah".

2. ntuk Menghindari Duplikasi Kode:
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


######
6. Kapan menggunakan non pewarisan (komposisi)

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


######
