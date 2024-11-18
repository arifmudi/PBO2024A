# Studi Kasus Pewarisan dalam Python: Sistem Manajemen Perpustakaan Digital

## Latar Belakang
Sebuah perpustakaan digital ingin mengembangkan sistem untuk mengelola berbagai jenis konten digital mereka, termasuk buku elektronik (e-book), audio book, dan video pembelajaran. Sistem ini perlu menangani berbagai fitur seperti peminjaman, pengembalian, dan pelacakan status konten.

## Analisis Kebutuhan
1. Setiap item memiliki properti dasar: judul, penulis, tahun terbit
2. Setiap jenis konten memiliki karakteristik khusus:
   - E-book: format file, jumlah halaman
   - Audio book: durasi, format audio
   - Video pembelajaran: durasi, kualitas video, instruktur
3. Sistem perlu mencatat status peminjaman dan riwayat peminjaman
4. Beberapa konten bisa memiliki fitur premium

## Implementasi Code

### 1. Single Inheritance: Konten Dasar
```python
from datetime import datetime, timedelta

class DigitalContent:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        self.borrower = None
        self.borrow_date = None
        
    def borrow(self, user):
        if self.is_available:
            self.is_available = False
            self.borrower = user
            self.borrow_date = datetime.now()
            return True
        return False
    
    def return_item(self):
        self.is_available = True
        self.borrower = None
        self.borrow_date = None
```

### 2. Multiple Inheritance: Konten Premium dengan DRM
```python
class DRMProtected:
    def __init__(self):
        self.drm_key = None
    
    def generate_drm_key(self):
        import uuid
        self.drm_key = str(uuid.uuid4())
    
    def verify_drm(self, key):
        return self.drm_key == key

class PremiumContent:
    def __init__(self):
        self.premium = True
        self.price = 0
    
    def set_price(self, price):
        self.price = price

class PremiumEbook(DigitalContent, DRMProtected, PremiumContent):
    def __init__(self, title, author, year, file_format, pages):
        DigitalContent.__init__(self, title, author, year)
        DRMProtected.__init__(self)
        PremiumContent.__init__(self)
        self.file_format = file_format
        self.pages = pages
        self.generate_drm_key()
```

### 3. Method Override: Implementasi Khusus untuk Audiobook
```python
class Audiobook(DigitalContent):
    def __init__(self, title, author, year, duration, audio_format):
        super().__init__(title, author, year)
        self.duration = duration
        self.audio_format = audio_format
        self.current_position = 0
    
    def borrow(self, user):  # Override method borrow
        success = super().borrow(user)
        if success:
            self.current_position = 0  # Reset posisi audio
            return True
        return False
    
    def save_position(self, position):
        if position <= self.duration:
            self.current_position = position
            return True
        return False
```

### 4. Hierarchical Inheritance: Video Pembelajaran
```python
class VideoContent(DigitalContent):
    def __init__(self, title, author, year, duration, resolution):
        super().__init__(title, author, year)
        self.duration = duration
        self.resolution = resolution

class CourseVideo(VideoContent):
    def __init__(self, title, author, year, duration, resolution, course_name):
        super().__init__(title, author, year, duration, resolution)
        self.course_name = course_name
        self.completed = False
    
    def mark_completed(self):
        self.completed = True

class TutorialVideo(VideoContent):
    def __init__(self, title, author, year, duration, resolution, difficulty_level):
        super().__init__(title, author, year, duration, resolution)
        self.difficulty_level = difficulty_level
```

### 5. Composition: Sistem Manajemen Perpustakaan
```python
class LibrarySystem:
    def __init__(self):
        self.catalog = {}
        self.users = {}
        self.borrowing_records = []
    
    def add_content(self, content_id, content):
        self.catalog[content_id] = content
    
    def register_user(self, user_id, user_info):
        self.users[user_id] = user_info
    
    def borrow_content(self, content_id, user_id):
        if content_id in self.catalog and user_id in self.users:
            content = self.catalog[content_id]
            user = self.users[user_id]
            
            if content.borrow(user):
                record = {
                    'content_id': content_id,
                    'user_id': user_id,
                    'borrow_date': datetime.now()
                }
                self.borrowing_records.append(record)
                return True
        return False
```

## Contoh Penggunaan

```python
# Membuat instance sistem perpustakaan
library = LibrarySystem()

# Membuat konten digital
ebook = PremiumEbook(
    "Python Programming",
    "John Doe",
    2024,
    "PDF",
    500
)
ebook.set_price(29.99)

audiobook = Audiobook(
    "Learn Python While Jogging",
    "Jane Smith",
    2024,
    180,  # durasi dalam menit
    "MP3"
)

tutorial = TutorialVideo(
    "Advanced Python Features",
    "Mike Johnson",
    2024,
    60,  # durasi dalam menit
    "1080p",
    "Advanced"
)

# Menambahkan konten ke sistem
library.add_content("PY101", ebook)
library.add_content("AUD101", audiobook)
library.add_content("VID101", tutorial)

# Mendaftarkan pengguna
library.register_user("USR001", {
    "name": "Alice",
    "membership": "premium"
})

# Meminjam konten
if library.borrow_content("PY101", "USR001"):
    print("Buku berhasil dipinjam!")
```

## Penjelasan Pola Pewarisan yang Digunakan

1. **Single Inheritance** (`DigitalContent`):
   - Digunakan sebagai base class untuk semua konten digital
   - Menyediakan fungsionalitas dasar peminjaman dan pengembalian
   - Cocok karena semua jenis konten memiliki properti dasar yang sama

2. **Multiple Inheritance** (`PremiumEbook`):
   - Menggabungkan fitur DRM dan konten premium
   - Memungkinkan e-book memiliki proteksi dan fitur berbayar
   - Memanfaatkan fungsionalitas dari beberapa parent class

3. **Method Override** (`Audiobook`):
   - Mengubah perilaku peminjaman untuk menangani posisi audio
   - Menambahkan fungsionalitas khusus untuk audio
   - Mempertahankan kontrak interface dari parent class

4. **Hierarchical Inheritance** (`VideoContent`, `CourseVideo`, `TutorialVideo`):
   - Membuat spesialisasi untuk jenis video yang berbeda
   - Memungkinkan penanganan khusus untuk setiap jenis video
   - Mempertahankan struktur yang rapi dan logis

5. **Composition** (`LibrarySystem`):
   - Menggabungkan berbagai komponen sistem
   - Lebih fleksibel daripada inheritance untuk manajemen sistem
   - Memungkinkan perubahan implementasi tanpa mempengaruhi hierarki class

## Kesimpulan

Studi kasus ini mendemonstrasikan bagaimana berbagai jenis pewarisan dapat digunakan dalam konteks nyata:
1. Single inheritance untuk fungsionalitas dasar
2. Multiple inheritance untuk menggabungkan fitur-fitur berbeda
3. Method override untuk kustomisasi perilaku
4. Hierarchical inheritance untuk spesialisasi
5. Composition untuk sistem yang lebih besar dan kompleks

Setiap pola pewarisan dipilih berdasarkan kebutuhan spesifik dan memberikan solusi yang elegant untuk masalah yang berbeda dalam sistem perpustakaan digital.
