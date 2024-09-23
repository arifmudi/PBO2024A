class informatika:
  def _init_(self, name, semester, matkul, teman):
    self.name = name
    self.semester = semester
    self.matkul = matkul
    self.teman = teman

  def _str_(self):
    return f"Nama saya adalah {self.name} saat ini saya semester {self.semester} dengan matkul {self.matkul}. matkul kesukaan saya {self.matkul}, dan teman sebelah kanan saya adalah {self.teman}."    

k = informatika("Ermita", 3,"pbo", "zany zafira")

print(k)