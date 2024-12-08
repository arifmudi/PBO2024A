class Informatika:
    def _init_(self, nama, semester, matakuliah):
        self.nama = nama
        self.semester = semester
        self.matakuliah = matakuliah
        self.orangkanan = "Aldo"

    def set_orang_kanan(self, orangkanan):
        self.orangkanan = orangkanan

    def myfunc(self):
        print(f"Nama saya {self.nama} \nsaat ini semester {self.semester} "
              f"\ndenganmatakuliah {self.matakuliah}, \nmatakuliah favorit {self.matakuliah}."
              f"\norang disebelah kanan {self.orangkanan}.")

    # Membuat Objek
        variabel = Informatika("Rofdan Azzaky Fauzi", 3, "PBO")
        variabel.set_orang_k