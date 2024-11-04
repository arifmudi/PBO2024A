
### 1. Konsep Pewarisan Tunggal (Single Inheritance)
Pewarisan tunggal adalah konsep di mana satu kelas anak (subclass) mewarisi sifat atau perilaku dari satu kelas induk (superclass). Pewarisan tunggal digunakan ketika kita ingin membuat kelas yang memiliki sifat dasar dari satu kelas lain tanpa melibatkan kelas tambahan.

**Implementasi Single Inheritance dalam Python**
```python
# Cerita:
# Kita memiliki kelas `Hewan` yang memiliki atribut dasar seperti suara.
# Kelas `Anjing` mewarisi sifat dari kelas `Hewan` dan menambahkan perilaku khusus.

# Kelas induk
class Hewan:
    def __init__(self, suara):
        self.suara = suara
    
    def berbunyi(self):
        print(f"Hewan ini berbunyi: {self.suara}")

# Kelas anak
class Anjing(Hewan):
    def menggonggong(self):
        print("Anjing menggonggong: Guk guk!")

# Penggunaan
anjing = Anjing("Guk guk!")
anjing.berbunyi()        # Memanggil metode dari kelas induk
anjing.menggonggong()     # Memanggil metode dari kelas anak
```

**Kapan Menggunakan Single Inheritance**
Gunakan single inheritance ketika hanya ada satu sifat utama yang ingin diturunkan ke kelas anak. Misalnya, `Anjing` yang mewarisi sifat dari `Hewan`.

### 2. Konsep `super` untuk Mewarisi di Konstruktor
`super()` digunakan untuk memanggil metode atau konstruktor dari kelas induk. Manfaatnya adalah memungkinkan kita untuk mengakses fungsi atau atribut dari kelas induk tanpa menulis ulang kodenya di kelas anak.

**Implementasi `super` dalam Python**
```python
# Cerita:
# Kita memiliki kelas `Orang` yang menyimpan nama, lalu kelas `Mahasiswa` yang menyimpan nama dan jurusan.

# Kelas induk
class Orang:
    def __init__(self, nama):
        self.nama = nama

# Kelas anak
class Mahasiswa(Orang):
    def __init__(self, nama, jurusan):
        super().__init__(nama)  # Memanggil konstruktor dari kelas induk
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")

# Penggunaan
mahasiswa = Mahasiswa("Budi", "Teknik Informatika")
mahasiswa.info()
```

**Kapan dan Mengapa Menggunakan `super()`**
Gunakan `super()` ketika Anda perlu mewarisi konstruktor atau metode dari kelas induk untuk menghindari pengulangan kode.

### 3. Jenis-jenis Pewarisan
| Jenis Pewarisan         | Penjelasan | Contoh Kode |
|-------------------------|------------|-------------|
| **Single Inheritance**  | Pewarisan dari satu kelas induk | Sudah dijelaskan di nomor 1 |
| **Multiple Inheritance**| Pewarisan dari dua atau lebih kelas induk | Lihat contoh di bawah |
| **Multi-level Inheritance** | Pewarisan bertingkat dari beberapa level | Lihat contoh di bawah |
| **Hierarchical Inheritance** | Satu kelas induk diwarisi oleh beberapa kelas anak | Lihat contoh di bawah |
| **Hybrid Inheritance** | Kombinasi dari beberapa jenis pewarisan | Lihat contoh di bawah |

**Contoh Kode**
```python
# Multiple Inheritance
class A:
    def show(self):
        print("Ini dari kelas A")

class B:
    def show(self):
        print("Ini dari kelas B")

class C(A, B):
    pass

c = C()
c.show()  # Menampilkan metode dari kelas A karena urutan pewarisan

# Multi-level Inheritance
class X:
    def tampil(self):
        print("Ini kelas X")

class Y(X):
    pass

class Z(Y):
    pass

z = Z()
z.tampil()  # Menampilkan metode dari kelas X

# Hierarchical Inheritance
class D:
    def tampil(self):
        print("Ini dari kelas D")

class E(D):
    pass

class F(D):
    pass

e = E()
e.tampil()  # Menampilkan dari kelas D
```

### 4. Override Method
Override method adalah proses mendefinisikan ulang metode yang sama dari kelas induk ke dalam kelas anak. Manfaatnya adalah kita dapat memodifikasi perilaku metode tersebut di kelas anak.

**Implementasi Override Method dalam Python**
```python
# Cerita:
# Kelas `Kendaraan` memiliki metode `bergerak`, kelas `Mobil` mewarisi kelas `Kendaraan` dan mengganti perilaku `bergerak`.

class Kendaraan:
    def bergerak(self):
        print("Kendaraan bergerak")

class Mobil(Kendaraan):
    def bergerak(self):
        print("Mobil bergerak dengan roda")

# Penggunaan
mobil = Mobil()
mobil.bergerak()  # Menggunakan metode yang di-override di kelas Mobil
```

**Kapan dan Mengapa Menggunakan Override**
Gunakan override ketika ingin mengubah perilaku default dari metode di kelas induk pada kelas anak.

### 5. Kapan Menggunakan Pewarisan
Gunakan pewarisan ketika ada hubungan “adalah” (is-a) antara kelas induk dan kelas anak. Misalnya, `Mobil` adalah `Kendaraan`.

### 6. Kapan Menggunakan Non Pewarisan (Komposisi)
Komposisi lebih cocok digunakan ketika hubungan antar kelas adalah “memiliki” (has-a), misalnya kelas `Mobil` memiliki `Mesin`.

### 7. Studi Kasus
Cerita:
Kita memiliki sistem untuk mengelola kendaraan. Ada kelas `Kendaraan`, kelas `Mobil` yang memiliki karakteristik umum dari `Kendaraan`, dan kelas `Motor` sebagai tipe kendaraan lainnya. Dalam program ini kita mengimplementasikan pewarisan dan komposisi.

**Kode**
```python
# Kelas Induk
class Kendaraan:
    def __init__(self, warna):
        self.warna = warna
    
    def info(self):
        print(f"Kendaraan berwarna {self.warna}")

# Kelas Anak dengan Pewarisan
class Mobil(Kendaraan):
    def __init__(self, warna, roda):
        super().__init__(warna)
        self.roda = roda

    def info(self):
        print(f"Mobil berwarna {self.warna} dengan {self.roda} roda")

# Kelas dengan Komposisi
class Mesin:
    def __init__(self, jenis):
        self.jenis = jenis

    def start(self):
        print(f"Mesin {self.jenis} dinyalakan")

class Motor(Kendaraan):
    def __init__(self, warna, mesin):
        super().__init__(warna)
        self.mesin = mesin  # Komposisi
    
    def info(self):
        print(f"Motor berwarna {self.warna} dengan mesin {self.mesin.jenis}")

# Penggunaan
mobil = Mobil("merah", 4)
mobil.info()

mesin_motor = Mesin("bensin")
motor = Motor("hitam", mesin_motor)
motor.info()
motor.mesin.start()
``` 

Di sini kita menggabungkan pewarisan pada `Mobil` dan komposisi pada `Motor`