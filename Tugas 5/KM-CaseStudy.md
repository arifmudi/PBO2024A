# Studi Kasus: Sistem Manajemen Perpustakaan Digital

## Latar Belakang
Sebuah perpustakaan digital ingin mengembangkan sistem untuk mengelola berbagai jenis koleksi media (buku, majalah, dan media digital) serta pengguna perpustakaan (mahasiswa, dosen, dan tamu). Sistem ini harus bisa menangani peminjaman, pengembalian, dan perhitungan denda.

## Implementasi

### 1. Single Inheritance: Pengelolaan Media
```python
class Media:
    def __init__(self, id, judul, penerbit, tahun):
        self.id = id
        self.judul = judul
        self.penerbit = penerbit
        self.tahun = tahun
        self.dipinjam = False
    
    def info(self):
        return f"ID: {self.id}, Judul: {self.judul}, Penerbit: {self.penerbit}, Tahun: {self.tahun}"

class Buku(Media):
    def __init__(self, id, judul, penerbit, tahun, penulis, halaman):
        super().__init__(id, judul, penerbit, tahun)  # Penggunaan super()
        self.penulis = penulis
        self.halaman = halaman
    
    def info(self):  # Method override
        return f"{super().info()}, Penulis: {self.penulis}, Halaman: {self.halaman}"
```

### 2. Multiple Inheritance: Fitur Media Digital
```python
class Downloadable:
    def download(self):
        return "Mengunduh media..."

class Streamable:
    def stream(self):
        return "Streaming media..."

class EBook(Buku, Downloadable):
    def __init__(self, id, judul, penerbit, tahun, penulis, halaman, format_file):
        super().__init__(id, judul, penerbit, tahun, penulis, halaman)
        self.format_file = format_file
    
    def info(self):
        return f"{super().info()}, Format: {self.format_file}"
```

### 3. Hierarchical Inheritance: Pengelolaan Pengguna
```python
class Pengguna:
    def __init__(self, id, nama, email):
        self.id = id
        self.nama = nama
        self.email = email
        self.daftar_pinjaman = []
    
    def pinjam(self, media):
        if not media.dipinjam:
            self.daftar_pinjaman.append(media)
            media.dipinjam = True
            return f"{self.nama} berhasil meminjam {media.judul}"
        return "Media sedang dipinjam"

class Mahasiswa(Pengguna):
    def __init__(self, id, nama, email, nim, jurusan):
        super().__init__(id, nama, email)
        self.nim = nim
        self.jurusan = jurusan
        self.max_pinjaman = 3
    
    def pinjam(self, media):
        if len(self.daftar_pinjaman) >= self.max_pinjaman:
            return "Sudah mencapai batas maksimum peminjaman"
        return super().pinjam(media)

class Dosen(Pengguna):
    def __init__(self, id, nama, email, nip, fakultas):
        super().__init__(id, nama, email)
        self.nip = nip
        self.fakultas = fakultas
        self.max_pinjaman = 5
```

### 4. Komposisi: Sistem Perpustakaan
```python
class SistemDenda:
    def __init__(self):
        self.denda_per_hari = 1000
    
    def hitung_denda(self, hari_terlambat):
        return self.denda_per_hari * hari_terlambat

class Perpustakaan:
    def __init__(self):
        self.koleksi_media = []
        self.daftar_pengguna = []
        self.sistem_denda = SistemDenda()  # Komposisi
    
    def tambah_media(self, media):
        self.koleksi_media.append(media)
    
    def tambah_pengguna(self, pengguna):
        self.daftar_pengguna.append(pengguna)
    
    def cari_media(self, judul):
        return [media for media in self.koleksi_media if media.judul.lower() == judul.lower()]
```

## Contoh Penggunaan
```python
# Membuat instance perpustakaan
perpus = Perpustakaan()

# Membuat beberapa media
buku1 = Buku("B001", "Python Programming", "InfoTech", 2023, "John Doe", 300)
ebook1 = EBook("E001", "Data Science Basics", "TechEdu", 2023, "Jane Smith", 250, "PDF")

# Membuat pengguna
mhs1 = Mahasiswa("M001", "Budi", "budi@email.com", "12345", "Informatika")
dsn1 = Dosen("D001", "Dr. Ahmad", "ahmad@email.com", "98765", "FTIK")

# Menambahkan ke sistem
perpus.tambah_media(buku1)
perpus.tambah_media(ebook1)
perpus.tambah_pengguna(mhs1)
perpus.tambah_pengguna(dsn1)

# Contoh peminjaman
print(mhs1.pinjam(buku1))
print(dsn1.pinjam(ebook1))

# Contoh penggunaan fitur ebook
print(ebook1.download())
```

## Penjelasan Penggunaan Konsep OOP

1. **Single Inheritance**
   - Digunakan pada class `Buku` yang mewarisi `Media`
   - Memungkinkan sharing atribut dan method dasar untuk semua jenis media

2. **Super()**
   - Digunakan dalam konstruktor `Buku` untuk memanggil konstruktor `Media`
   - Memastikan inisialisasi yang proper untuk atribut parent class

3. **Multiple Inheritance**
   - `EBook` mewarisi dari `Buku` dan `Downloadable`
   - Menggabungkan fungsionalitas buku dengan kemampuan digital

4. **Method Override**
   - Method `info()` di class `Buku` meng-override method di class `Media`
   - Method `pinjam()` di class `Mahasiswa` meng-override method di class `Pengguna`

5. **Hierarchical Inheritance**
   - Class `Pengguna` sebagai parent untuk `Mahasiswa` dan `Dosen`
   - Memungkinkan sharing behavior umum dengan spesialisasi untuk masing-masing jenis pengguna

6. **Komposisi**
   - Class `Perpustakaan` menggunakan komposisi dengan `SistemDenda`
   - Memberikan fleksibilitas dalam pengelolaan sistem denda

## Keuntungan Design Ini

1. **Modular**: Setiap class memiliki tanggung jawab yang jelas
2. **Extensible**: Mudah menambahkan jenis media atau pengguna baru
3. **Maintainable**: Perubahan pada satu class tidak mempengaruhi class lain
4. **Reusable**: Code yang umum bisa digunakan kembali melalui inheritance
