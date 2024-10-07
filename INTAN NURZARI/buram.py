# class Manusia :
#     def__init__(self,nama,umur):
#     self.name = nama
#     self.umur = umur
#     def

class orang : 
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur 



    def perkenalan (self):
        print(f"Hallo, nama saya {self.nama} dan saya berumur {self.umur} tahun.")

OrangA = orang ("Doni",27)
OrangA.perkenalan()

OrangB = orang ("Nia")
OrangB.perkenalan()