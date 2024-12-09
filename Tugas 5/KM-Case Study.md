# Studi Kasus: Sistem Manajemen Sekolah Musik

## Latar Belakang
Sebuah sekolah musik membutuhkan sistem untuk mengelola kursus musik, instruktur, siswa, dan jadwal les. Sistem ini harus bisa menangani berbagai jenis instrumen musik, level pembelajaran, dan jenis kursus (private/grup).

## Implementasi

### 1. Single Inheritance: Pengelolaan Instrumen Musik
```python
class MusicalInstrument:
    def __init__(self, id, nama, jenis, tingkat_kesulitan):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.tingkat_kesulitan = tingkat_kesulitan
    
    def info(self):
        return f"Instrumen: {self.nama} ({self.jenis}), Level: {self.tingkat_kesulitan}"

class Piano(MusicalInstrument):
    def __init__(self, id, nama, jenis, tingkat_kesulitan, tipe_piano):
        super().__init__(id, nama, jenis, tingkat_kesulitan)  # Penggunaan super()
        self.tipe_piano = tipe_piano
    
    def info(self):  # Method override
        return f"{super().info()}, Tipe Piano: {self.tipe_piano}"
```

### 2. Multiple Inheritance: Kemampuan Instruktur
```python
class MusicTheory:
    def mengajar_teori(self):
        return "Mengajar teori musik dasar"

class Performer:
    def perform(self):
        return "Melakukan pertunjukan musik"

class AdvancedInstructor(MusicTheory, Performer):
    def __init__(self, nama, spesialisasi):
        self.nama = nama
        self.spesialisasi = spesialisasi
    
    def mengajar_advanced(self):
        return f"Mengajar {self.spesialisasi} tingkat lanjut"
```

### 3. Hierarchical Inheritance: Jenis Kursus
```python
class Course:
    def __init__(self, kode, nama, durasi, harga):
        self.kode = kode
        self.nama = nama
        self.durasi = durasi
        self.harga = harga
        self.siswa = []
    
    def tambah_siswa(self, siswa):
        if len(self.siswa) < self.kapasitas_maksimal:
            self.siswa.append(siswa)
            return f"Siswa {siswa.nama} berhasil ditambahkan ke kursus {self.nama}"
        return "Kursus sudah penuh"

class PrivateCourse(Course):
    def __init__(self, kode, nama, durasi, harga):
        super().__init__(kode, nama, durasi, harga)
        self.kapasitas_maksimal = 1
        self.tipe = "Private"

class GroupCourse(Course):
    def __init__(self, kode, nama, durasi, harga, kapasitas):
        super().__init__(kode, nama, durasi, harga)
        self.kapasitas_maksimal = kapasitas
        self.tipe = "Group"
```

### 4. Multilevel Inheritance: Level Pembelajaran
```python
class MusicStudent:
    def __init__(self, id, nama, umur):
        self.id = id
        self.nama = nama
        self.umur = umur
        self.level = "Beginner"
    
    def practice(self):
        return f"{self.nama} sedang berlatih musik"

class IntermediateStudent(MusicStudent):
    def __init__(self, id, nama, umur, jam_terbang):
        super().__init__(id, nama, umur)
        self.jam_terbang = jam_terbang
        self.level = "Intermediate"
    
    def perform_basic(self):
        return f"{self.nama} tampil di recital tingkat dasar"

class AdvancedStudent(IntermediateStudent):
    def __init__(self, id, nama, umur, jam_terbang, prestasi):
        super().__init__(id, nama, umur, jam_terbang)
        self.prestasi = prestasi
        self.level = "Advanced"
    
    def perform_advanced(self):
        return f"{self.nama} tampil di konser tingkat lanjut"
```

### 5. Komposisi: Manajemen Sekolah Musik
```python
class Schedule:
    def __init__(self):
        self.jadwal = {}
    
    def tambah_jadwal(self, hari, waktu, kursus, instruktur):
        if hari not in self.jadwal:
            self.jadwal[hari] = {}
        self.jadwal[hari][waktu] = (kursus, instruktur)

class MusicSchool:
    def __init__(self, nama):
        self.nama = nama
        self.instruktur = []
        self.siswa = []
        self.kursus = []
        self.schedule = Schedule()  # Komposisi
    
    def tambah_instruktur(self, instruktur):
        self.instruktur.append(instruktur)
    
    def tambah_siswa(self, siswa):
        self.siswa.append(siswa)
    
    def buat_kursus(self, kursus):
        self.kursus.append(kursus)
```

## Contoh Penggunaan
```python
# Inisialisasi sekolah musik
melody_school = MusicSchool("Melody Music School")

# Membuat instrumen
piano = Piano("P001", "Grand Piano", "Keyboard", "Advanced", "Grand")

# Membuat instruktur
instruktur1 = AdvancedInstructor("John Doe", "Piano")

# Membuat kursus
private_piano = PrivateCourse("PP001", "Private Piano", "60 mins", 500000)
group_piano = GroupCourse("GP001", "Group Piano", "90 mins", 300000, 5)

# Membuat siswa
siswa_pemula = MusicStudent("S001", "Alice", 15)
siswa_lanjut = AdvancedStudent("S002", "Bob", 17, 1000, ["Juara 1 Kompetisi Piano"])

# Mendaftarkan ke kursus
print(private_piano.tambah_siswa(siswa_pemula))
print(group_piano.tambah_siswa(siswa_lanjut))

# Menambahkan jadwal
melody_school.schedule.tambah_jadwal("Senin", "15:00", private_piano, instruktur1)
```

## Penjelasan Penggunaan Konsep OOP

1. **Single Inheritance & Super()**
   - Class `Piano` mewarisi dari `MusicalInstrument`
   - Menggunakan `super()` untuk memanggil konstruktor parent
   - Override method `info()` untuk menambahkan informasi spesifik piano

2. **Multiple Inheritance**
   - `AdvancedInstructor` mewarisi kemampuan dari `MusicTheory` dan `Performer`
   - Menggabungkan kemampuan mengajar teori dan perform

3. **Hierarchical Inheritance**
   - Class `Course` sebagai parent untuk `PrivateCourse` dan `GroupCourse`
   - Masing-masing jenis kursus memiliki karakteristik khusus

4. **Multilevel Inheritance**
   - Hierarki level siswa: `MusicStudent` -> `IntermediateStudent` -> `AdvancedStudent`
   - Setiap level menambahkan kemampuan baru

5. **Method Override**
   - Override method `info()` di class `Piano`
   - Override method untuk performance di tiap level siswa

6. **Komposisi**
   - Class `MusicSchool` menggunakan komposisi dengan `Schedule`
   - Schedule bisa dikelola secara independen

## Keunggulan Design

1. **Fleksibel**: Mudah menambahkan jenis instrumen, kursus, atau level baru
2. **Terorganisir**: Hierarki yang jelas untuk setiap komponen
3. **Reusable**: Kode dapat digunakan ulang melalui inheritance
4. **Maintainable**: Perubahan dapat dilakukan tanpa mempengaruhi komponen lain

## Use Cases

1. **Pendaftaran Siswa Baru**
   - Membuat instance siswa sesuai level
   - Mendaftarkan ke kursus yang sesuai

2. **Penjadwalan Les**
   - Menambahkan jadwal les baru
   - Mengecek ketersediaan instruktur

3. **Tracking Kemajuan**
   - Memantau level siswa
   - Mencatat prestasi dan jam terbang

4. **Manajemen Kursus**
   - Membuat kursus baru
   - Mengatur kapasitas dan jadwal

## Kesimpulan

Studi kasus ini mendemonstrasikan penggunaan berbagai jenis inheritance dan komposisi dalam konteks manajemen sekolah musik. Setiap konsep OOP digunakan sesuai kebutuhan spesifik:
- Single inheritance untuk instrumen musik
- Multiple inheritance untuk kemampuan instruktur
- Hierarchical inheritance untuk jenis kursus
- Multilevel inheritance untuk level pembelajaran
- Komposisi untuk manajemen jadwal