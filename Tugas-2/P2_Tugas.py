class Informatika:
    def __init__(self, nama, semester, matakuliah):
        self.nama = nama
        self.semester = semester
        self.matakuliah = matakuliah
        self.orangKanan = "JUNA." 

    def set_orang_kanan(self, orangKanan):
        self.orangKanan = orangKanan

    def myfunc(self):
        print(f"Nama saya {self.nama} \nsaat ini semester {self.semester} "
              f"\ndengan matkul {self.matakuliah}, \nMatkul Favorit {self.matakuliah}. "
              f"\nOrang Disebelah Kanan {self.orangKanan}.")

# Membuat objek
variabel = Informatika("AMAL", 3, "PBO")
variabel.set_orang_kanan("JUNA") 
variabel.myfunc()