class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

class BukuFiksi(Buku):
    def __init__(self, judul, pengarang, tahun_terbit, genre):
        super().__init__(judul, pengarang, tahun_terbit)
        self.genre = genre

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Genre: {self.genre}")

class BukuNonFiksi(Buku):
    def __init__(self, judul, pengarang, tahun_terbit, topik):
        super().__init__(judul, pengarang, tahun_terbit)
        self.topik = topik

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Topik: {self.topik}")

# Contoh Penggunaan
buku1 = BukuFiksi("Harry Potter dan Batu Bertuah", "J.K. Rowling", 1997, "Fantasi")
buku1.tampilkan_info()
print("\n" + "="*30 + "\n")
buku2 = BukuNonFiksi("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, "Sejarah")
buku2.tampilkan_info()