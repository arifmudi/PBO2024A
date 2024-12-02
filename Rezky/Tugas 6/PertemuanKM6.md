Nama    : Muhammad Rezky Ramadhan
Nim     : 2355201013

===============================================================POLIMORFISME=============================================================

Apa Itu Polimorfisme?

Polimorfisme berasal dari bahasa Yunani yang berarti "banyak bentuk". Dalam pemrograman, Polimorfisme adalah konsep di mana satu antarmuka dapat digunakan untuk berbagai jenis objek. Dengan kata lain, metode atau fungsi yang sama dapat memiliki perilaku berbeda tergantung pada objek yang menggunakannya.

Kegunaan Polimorfisme

1. Kode yang Lebih Fleksibel: Memungkinkan penggunaan metode yang sama untuk berbagai tipe data.
2. Mempercepat Pengembangan: Dengan menulis metode generik yang dapat digunakan kembali untuk banyak kelas.
3. Meningkatkan Abstraksi: Mengurangi ketergantungan pada implementasi spesifik, sehingga kode lebih mudah dipelihara.
4. Mendukung Prinsip OOP: Seperti inheritance dan interface.

Kapan Digunakan?

1. Ketika ingin membuat program yang dapat menangani objek berbeda dengan cara yang seragam.
2. Saat ada hierarki kelas dengan metode yang memiliki nama sama tetapi perilaku yang berbeda.
3. Dalam desain sistem yang memanfaatkan abstract class atau interface untuk mendukung perluasan di masa depan.

Contoh Polimorfisme

class Hewan:
    def berbunyi(self):
        return "Hewan mengeluarkan suara"

class Kucing(Hewan):
    def berbunyi(self):
        return "Meong"

class Anjing(Hewan):
    def berbunyi(self):
        return "Guk guk"

def suara_hewan(hewan):
    print(hewan.berbunyi())

kucing = Kucing()
anjing = Anjing()

suara_hewan(kucing)  # Output: Meong
suara_hewan(anjing)  # Output: Guk guk


Penjelasan
Method Overriding: Subkelas seperti `Kucing` dan `Anjing` mendefinisikan ulang metode `berbunyi` dari kelas induk `Hewan`. Fungsi `suara_hewan` dapat bekerja dengan semua objek `Hewan` dan turunannya.