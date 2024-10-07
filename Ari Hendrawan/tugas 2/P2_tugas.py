class Informatika:
    def __init__(self, nama, semester, matkul):
        self.name = nama
        self.semester = semester
        self.matkul = matkul
    
    def kanan(self):
        return "David"

    def __str__(self):
        return (f"Nama saya adalah {self.name}. "
                f"\nSaat ini saya di semester {self.semester} dengan matkul {self.matkul}. "
                f"\nNama disebelah kanan saya {self.kanan()}.")


cocoklogi = Informatika("Envy", 3, "PBO")

print(str(cocoklogi))
