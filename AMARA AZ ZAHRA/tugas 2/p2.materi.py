class informatika:
  def __init__(self, nama, semester, matkul):
    self.nama = nama
    self.semester = semester
    self.matkul = matkul

  def __str__(self):
    return f"Nama saya adalah {self.nama} saat ini saya semester {self.semester} dengan mata kuliah kesukaan {self.matkul}"
  def teman_sebelah_kanan(self,teman_kanan):
    return f"Teman di sebelah kanan saya adalah {teman_kanan}."

x = informatika("Amaraazzahra", 3, "PBO")
teman_kanan = "Darell"
print(x.__str__())
print(x.teman_sebelah_kanan(teman_kanan))
