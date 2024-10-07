# class orang:
#     def __init__(self, nama, umur, nik):
#         self.name = nama
#         self._umur = umur
#         self.__nik = nik
    
#     def perkenalan(self):
#         print(f"halo, nama saya {self.name} dan saya berumur {self.umur} tahun. dengan nik {self.nik}.")

# orangA = orang ("doni",27,12345)
# orangB = orang ("nia", 20,54321)
# orangA.perkenalan()
# orangB.perkenalan()

class Orang:
    def __init__(self, nama, umur, nik):
        self.nama = nama          # Public attribute
        self._umur = umur         # Protected attribute
        self.__nik = nik          # Private attribute

    def perkenalan(self):
        print(f"Hallo, nama saya {self.nama} dan saya berumur {self._umur} tahun. Dengan NIK {self.__nik}.")

    def get_nik(self):
        return self.__nik

orangA = Orang("Doni", 27, 12345)
orangB = Orang("Nia", 20, 54321)

orangA.perkenalan()  
orangB.perkenalan()  