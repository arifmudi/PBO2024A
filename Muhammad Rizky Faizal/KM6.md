Nama: Muhammad rizky faizal
Nim : 2355201020

Polimorfisme adalah konsep dalam OOP yang memungkinkan objek dari kelas yang berbeda untuk diakses melalui antarmuka yang sama. Dengan kata lain, polimorfisme memungkinkan metode untuk memiliki nama yang sama tetapi perilaku yang berbeda tergantung pada objek yang memanggilnya. Ini membantu dalam mengurangi kompleksitas dan meningkatkan fleksibilitas kode.
Example:
class Kendaraan:
    def suara(self):
        pass

class Mobil(Kendaraan):
    def suara(self):
        return "Vroom"

class Motor(Kendaraan):
    def suara(self):
        return "Brrrm"

def cetak_suara(kendaraan):
    print(kendaraan.suara())

# Objek dari kelas Mobil dan Motor
mobil = Mobil()
motor = Motor()

# Fungsi cetak_suara untuk mencetak suara dari masing-masing kendaraan
cetak_suara(mobil)
cetak_suara(motor)

hasilnya:
Vroom
Brrrm
