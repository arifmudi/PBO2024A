class Informatika:
    def __init__(self, nama, semester, matakuliah):
        self.nama = nama
        self.semester = semester
        self.matakuliah = matakuliah
        self.namateman = "Ermita."

    def set_teman(self, namateman):
        self.namateman = namateman

    def myfunc(self):
        print(f"Nama Saya {self.nama} \nSaat Ini Semester {self.semester} "
              f"\nDengan Matkul {self.matakuliah}, \nMatkul Favorit Saya Adalah {self.matakuliah}. "
              f"\nNama Teman Disebelah Kanan {self.namateman}.")

# Membuat objek
variabel = Informatika("Darell Revalino", 3, "PBO")
variabel.set_teman("Ermita") 
variabel.myfunc()