class informatika:
    def_init_(self, nama, semester, mata kuliah):
    self.nama= nama
    self.semester= semester
    self.matkul= matkul

  def __str__(self):
    return f"Nama saya adalah {self.nama} Saat ini semester {self.semester} dengan mata kuliah kesukaan {self.matkul}"

x = informatika("Amita afriyani", 3 ,"PBO")
print(x)
