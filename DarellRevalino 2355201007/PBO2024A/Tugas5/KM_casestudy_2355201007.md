# Studi Kasus: Pewarisan dalam Dunia Transportasi

Di dunia transportasi modern, berbagai jenis kendaraan berkembang untuk memenuhi kebutuhan manusia yang semakin beragam. Dalam studi kasus ini, kita akan melihat bagaimana konsep pewarisan dapat diterapkan untuk memodelkan hierarki dan hubungan antar-kendaraan.

## Skenario

Bayangkan sebuah perusahaan transportasi yang memiliki berbagai jenis kendaraan, mulai dari kendaraan darat, laut, hingga udara. Perusahaan ini ingin mengembangkan sistem manajemen yang efisien untuk mengelola seluruh armada kendaraannya.

## Hierarki Kendaraan

Pertama-tama, kita akan membuat hierarki kendaraan menggunakan konsep pewarisan:

1. **Kendaraan (Vehicle)**: Kelas dasar yang mewakili semua jenis kendaraan. Kelas ini akan memiliki atribut dan metode umum yang dimiliki oleh semua kendaraan.
2. **KendaraanDarat (GroundVehicle)**: Kelas turunan dari Kendaraan, mewakili kendaraan yang beroperasi di darat, seperti mobil, truk, dan sepeda motor.
3. **KendaraanLaut (WaterVehicle)**: Kelas turunan dari Kendaraan, mewakili kendaraan yang beroperasi di air, seperti kapal, perahu, dan jet ski.
4. **KendaraanUdara (AirVehicle)**: Kelas turunan dari Kendaraan, mewakili kendaraan yang beroperasi di udara, seperti pesawat terbang, helikopter, dan drone.

Dalam contoh ini, kita akan menggunakan pewarisan tunggal (single inheritance) untuk membentuk hierarki kendaraan.

```python
class Kendaraan:
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model
    
    def info(self):
        print(f"Merk: {self.merk}, Model: {self.model}")

class KendaraanDarat(Kendaraan):
    def __init__(self, merk, model, roda):
        super().__init__(merk, model)
        self.roda = roda
    
    def bergerak(self):
        print("Kendaraan darat bergerak di jalan raya.")

class KendaraanLaut(Kendaraan):
    def __init__(self, merk, model, tipe_badan):
        super().__init__(merk, model)
        self.tipe_badan = tipe_badan
    
    def bergerak(self):
        print("Kendaraan laut bergerak di air.")

class KendaraanUdara(Kendaraan):
    def __init__(self, merk, model, sayap):
        super().__init__(merk, model)
        self.sayap = sayap
    
    def bergerak(self):
        print("Kendaraan udara terbang di angkasa.")
```

Dalam contoh di atas, kelas `Kendaraan` adalah kelas dasar yang memiliki atribut umum `merk` dan `model`, serta metode `info()` untuk menampilkan informasi kendaraan. Kelas `KendaraanDarat`, `KendaraanLaut`, dan `KendaraanUdara` adalah kelas turunan yang masing-masing memiliki atribut dan metode khusus sesuai dengan jenis kendaraannya.

## Penggunaan Kode

Sekarang, mari kita coba menggunakan hierarki kendaraan yang telah kita buat:

```python
# Membuat objek kendaraan
mobil = KendaraanDarat("Toyota", "Camry", 4)
kapal = KendaraanLaut("Titanic", "Ocean Liner", "Badan Besar")
pesawat = KendaraanUdara("Boeing", "747", "Sayap Besar")

# Memanggil metode
mobil.info()
mobil.bergerak()

kapal.info()
kapal.bergerak()

pesawat.info()
pesawat.bergerak()
```

Output:
```
Merk: Toyota, Model: Camry
Kendaraan darat bergerak di jalan raya.
Merk: Titanic, Model: Ocean Liner
Kendaraan laut bergerak di air.
Merk: Boeing, Model: 747
Kendaraan udara terbang di angkasa.
```

Dalam contoh di atas, kita membuat objek untuk masing-masing jenis kendaraan dan memanggil metode `info()` serta `bergerak()` pada setiap objek. Perhatikan bagaimana masing-masing kendaraan mengimplementasikan metode `bergerak()` secara berbeda, sesuai dengan karakteristiknya.

## Pewarisan Ganda dan Hibrid

Selain pewarisan tunggal, kita juga dapat menerapkan pewarisan ganda (multiple inheritance) dan pewarisan hibrid (hybrid inheritance) untuk memodelkan kendaraan yang memiliki sifat-sifat gabungan.

Misalnya, kita dapat membuat kelas `KendaraanAmfibi` yang mewarisi dari `KendaraanDarat` dan `KendaraanLaut`, sehingga dapat bergerak di darat maupun di air.

```python
class KendaraanAmfibi(KendaraanDarat, KendaraanLaut):
    def __init__(self, merk, model, roda, tipe_badan):
        KendaraanDarat.__init__(self, merk, model, roda)
        KendaraanLaut.__init__(self, merk, model, tipe_badan)
    
    def bergerak(self):
        print("Kendaraan amfibi bergerak di darat dan air.")

# Contoh penggunaan
hovecraft = KendaraanAmfibi("Generic", "Hovercraft", 0, "Badan Datar")
hovecraft.info()
hovecraft.bergerak()
```

Output:
```
Merk: Generic, Model: Hovercraft
Kendaraan amfibi bergerak di darat dan air.
```

Dengan pendekatan pewarisan, kita dapat dengan mudah memperluas hierarki kendaraan sesuai dengan kebutuhan, serta menyediakan implementasi yang sesuai untuk setiap jenis kendaraan.

