class Informatika:
    def __init__(self, nama, semester, matakuliah):
        self.nama = nama
        self.semester = semester
        self.matakuliah = matakuliah
    
    def __str__(self):
        return f"Nama saya adalah {self.nama}. Saat ini saya di semester {self.semester}. Dengan matkul {self.matakuliah}"

r = Informatika("Rezky", 3, "PBO")

print(r)