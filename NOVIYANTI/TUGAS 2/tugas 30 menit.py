class Informatika:
    def __init__(self, nama, semester, matkul, teman_sebelah):
        self.nama = nama
        self.semester = semester
        self.matkul = matkul
        self.teman_sebelah = teman_sebelah

    def __str__(self):
        return (f"Nama saya adalah {self.nama}. Saat ini semester {self.semester} "
                f"dengan mata kuliah kesukaan {self.matkul}. "
                f"Teman di sebelah kanan saya adalah {self.teman_sebelah}.")

X = Informatika("Noviyanti", 3, "PBO", "Amara")
print(X)
