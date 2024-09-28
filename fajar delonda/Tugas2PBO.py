class Informatika:
    def __init__(self, nama, jurusan, matakuliah):
        self.nama = nama
        self.jurusan = jurusan
        self.matakuliah = matakuliah

    def str(self):
        return f"Nama: {self.nama}, Jurusan: {self.jurusan}, Matakuliah: {self.matakuliah}"

    def ubah_nama(self, nama_baru):
        self.nama = nama_baru

# Membuat objek
mahasiswa = Informatika("Fajar Delonda", "Informatika", "PBO")

# Menampilkan informasi
print(mahasiswa.str())

# Mengubah nama
mahasiswa.ubah_nama("Nama Rofdan Azzaki")

# Menampilkan informasi setelah perubahan
print(mahasiswa.str())