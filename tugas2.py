class informatika:
  def __init__(self, nama, semester, matkul):
    self.nama = nama
    self.semester = semester
    self.matkul = matkul

  def __str__(self):
    return f"Nama saya adalah {self.nama} saat ini saya semester {self.semester} dengan mata kuliah kesukaan {self.matkul}"

x = informatika("ZanyZafiraAkmal", 3, "PBO")

print(x)
