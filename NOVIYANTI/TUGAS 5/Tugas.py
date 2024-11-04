class Orang:
    def __init__(self, nama, mata_kuliah):
        self.nama = nama
        self.mata_kuliah = mata_kuliah

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}.")

class Guru(Orang):
    def mengajar(self):
        print(f"Saya mengajar mata kuliah {self.mata_kuliah}.")

guru1 = Guru("Novi", "PBO")

guru1.perkenalan()
guru1.mengajar()
