class Informatika:
    def __init__(self, name, semester, matkul):
        self.name = name
        self.semester = semester
        self.matkul = matkul

    def tampilkan_info(self):
        return f"Nama saya adalah {self.name}, saat ini saya semester {self.semester} dengan matkul {self.matkul} matkul kesukaan saya."

def tampilkan_teman_kanan(teman_kanan):
    return f"Teman di sebelah kanan saya adalah {teman_kanan}."

k = Informatika("Ermita", 3, "PBO")
teman_kanan = "Zany Zafira"
print(k.tampilkan_info())
print(tampilkan_teman_kanan(teman_kanan))