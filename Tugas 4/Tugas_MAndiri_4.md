
___OOP___

Paradigma Pemrograman Berorientasi Objek (OOP) adalah suatu pendekatan dalam pemrograman yang menggunakan "objek" 
sebagai dasar dari struktur dan fungsionalitas program. OOP memudahkan pengembangan perangkat lunak dengan mengorganisir 
kode menjadi bagian-bagian yang lebih terstruktur, sehingga lebih mudah dikelola dan diperluas.


___Class___
Class adalah cetak biru atau template untuk membuat objek. Class mendefinisikan atribut dan metode yang dimiliki oleh objek tersebut.
Contoh : 
_
class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna
_

___Objek___
Objek adalah instansi dari class. Setiap objek memiliki atribut dan metode yang didefinisikan oleh class.
Contoh :
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Biru")


___Atribut___
Atribut adalah variabel yang terdapat dalam class. Atribut menyimpan informasi atau keadaan objek.
Contoh : pada contoh diatas, merek dan warna adalah atribut mobil1

___Method____
Method adalah fungsi yang didefinisikan dalam class dan dapat dipanggil oleh objek dari class tersebut.
Contoh:
_class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def deskripsi(self):
        return f"{self.merek} berwarna {self.warna}"
___


___Constructor___
Constructor adalah metode khusus dalam class yang secara otomatis dipanggil saat objek dibuat. 
Dalam Python, constructor biasanya ditandai dengan __init__.
Contoh:
_
mobil1 = Mobil("Toyota", "Merah")  # __init__ dipanggil di sini
_

___Modifikasi akses___
Modifikasi akses mengacu pada cara kita mengontrol akses ke atribut dan metode dalam class. Di Python, kita dapat menggunakan:

public: Akses bebas (default)
protected: Akses terbatas pada class dan subclass
private: Akses terbatas hanya dalam class itu sendiri

contoh 
class Mobil:
_
    def __init__(self, merek, warna):
        self.merek = merek  # public
        self._warna = warna  # protected
        self.__kecepatan = 0  # private
_


____Enkapsulasi___
nkapsulasi adalah konsep menyembunyikan detail implementasi dari suatu objek dan hanya menampilkan interface yang diperlukan. 
Ini membantu menghindari akses langsung ke data dan mengurangi ketergantungan antar bagian kode.
Contoh:
-
class Mobil:
    def __init__(self, merek, warna):
        self.__kecepatan = 0  # private

    def tambah_kecepatan(self, tambah):
        self.__kecepatan += tambah

    def lihat_kecepatan(self):
        return self.__kecepatan
_




Jadi 
Paradigma OOP membantu dalam mengorganisir kode dengan cara yang lebih terstruktur dan modular. 
Dengan memanfaatkan konsep class, objek, atribut, method, constructor, modifikasi akses, dan enkapsulasi, 
pengembang dapat membuat aplikasi yang lebih mudah untuk dikelola dan dikembangkan.