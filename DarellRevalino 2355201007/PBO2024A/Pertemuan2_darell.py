class informatika:
    def __init__(self, nama, semester, matkul):
        self.nama = nama
        self.semester = semester
        self.matkul = matkul

    def __str__(self):
        return f"Nama saya adalah {self.nama} saat ini saya semester {self.semester} dengan matakuliah favorite {self.matkul} dan nama teman saya adalah Ermita."
    
    k = informatika("Darell Revalino", 3, "PBO")