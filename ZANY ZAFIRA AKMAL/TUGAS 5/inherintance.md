Apa itu Pewarisan di Python?
Pewarisan adalah salah satu fitur terpenting dari bahasa pemrograman berorientasi objek seperti Python. Ini digunakan untuk mewarisi properti dan perilaku satu kelas ke kelas lainnya. Kelas yang mewarisi kelas lain disebut kelas anak dan kelas yang diwariskan disebut kelas dasar atau kelas induk.

1.Pewarisan Tunggal:
adalah bentuk pewarisan paling sederhana di mana kelas anak mewarisi atribut dan metode hanya dari satu kelas induk,atau konsep di mana sebuah kelas (kelas turunan) mewarisi sifat dan perilaku dari satu kelas lain (kelas induk). Ini membantu dalam mendaur ulang kode dan membuat struktur yang lebih jelas. Pada pewarisan tunggal, kelas turunan mendapatkan semua atribut dan metode dari satu kelas induk.

IMPLEMENTASINYA:
Single inheritance digunakan ketika kita ingin memperluas atau menambahkan fungsi tambahan ke kelas yang sudah ada tanpa mengubahnya. Hal ini cocok jika sifat kelas turunan sepenuhnya atau sebagian besar didasarkan pada kelas induk.

contoh:
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

# Penggunaan
dog = Dog()
print(dog.sound())  # Output: Some sound
print(dog.bark())   # Output: Woof!

2.Konsep super untuk Pewarisan di Konstruktor

Fungsi super() digunakan untuk memanggil konstruktor atau metode dari kelas induk dalam kelas turunan. Ini memungkinkan untuk menggunakan logika yang sudah ada di kelas induk tanpa menuliskannya kembali, serta menjaga kode agar lebih modular dan mudah dipelihara.

IMPLEMENTASI
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Memanggil konstruktor kelas induk
        self.breed = breed

# Penggunaan
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)   # Output: Buddy
print(dog.breed)  # Output: Golden Retriever

Kapan dan Mengapa Menggunakan:
Gunakan super() ketika Anda ingin memperluas fungsi dari konstruktor atau metode di kelas induk, terutama jika kelas induk memiliki inisialisasi data yang dibutuhkan oleh kelas turunan.

3.Jenis Jenis Inheritance:

| Jenis Inheritance           | Single Inheritance                                                            |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Mewarisi dari satu kelas induk.                                               |
| **Contoh Implementasi**     | `class B(A): pass`                                                            |
| **Kapan Menggunakan**       | Ketika kelas turunan hanya perlu satu dasar dari kelas induk.                 |

| Jenis Inheritance           | Multiple Inheritance                                                          |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Mewarisi dari lebih dari satu kelas induk.                                    |
| **Contoh Implementasi**     | `class C(A, B): pass`                                                         |
| **Kapan Menggunakan**       | Ketika kelas turunan membutuhkan sifat dari beberapa kelas induk.             |

| Jenis Inheritance           | Multilevel Inheritance                                                        |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Mewarisi dalam beberapa level (kelas induk, anak, cucu).                      |
| **Contoh Implementasi**     | `class C(B): pass` dan `class B(A): pass`                                     |
| **Kapan Menggunakan**       | Ketika ingin membuat hierarki yang panjang atau rantai turunan.               |

| Jenis Inheritance           | Hierarchical Inheritance                                                      |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Satu kelas induk diwarisi oleh beberapa kelas turunan.                        |
| **Contoh Implementasi**     | `class B(A): pass` dan `class C(A): pass`                                     |
| **Kapan Menggunakan**       | Ketika beberapa kelas perlu memiliki sifat yang sama dari satu kelas induk.   |

| Jenis Inheritance           | Hybrid Inheritance                                                            |
|-----------------------------|-------------------------------------------------------------------------------|
| **Pengertian**              | Gabungan dari beberapa tipe inheritance, termasuk multiple dan multilevel.    |
| **Contoh Implementasi**     | `class C(A, B): pass` (A dan B bisa saling terkait)                           |
| **Kapan Menggunakan**       | Ketika membutuhkan kombinasi sifat dari beberapa inheritance untuk kasus      |
|                             | yang  kompleks.                                                               |

4.Override Method (Penulisan Ulang)
**Pengertian:**
Override method adalah teknik di mana sebuah kelas turunan menyediakan implementasi baru untuk metode yang sudah didefinisikan dalam kelas induk. Dengan cara ini, kelas turunan dapat mengubah perilaku dari metode yang diwarisi sesuai dengan kebutuhan spesifiknya.

### Manfaat Override Method
1. **Kustomisasi Perilaku:** Memberikan kemampuan kepada kelas turunan untuk menyesuaikan atau memperluas perilaku metode dari kelas induk.
2. **Polymorphism:** Memungkinkan penggunaan polymorphism, di mana kita dapat menggunakan objek dari kelas turunan dengan cara yang sama seperti objek dari kelas induk. Ini memungkinkan kita untuk memanggil metode yang sama tetapi dengan perilaku yang berbeda.
3. **Pengurangan Redundansi Kode:** Dengan mengubah perilaku metode yang diwarisi daripada membuat metode baru, kita dapat menghindari duplikasi kode dan menjaga konsistensi.
4. **Keterbacaan dan Pemeliharaan:** Memudahkan pemeliharaan kode, karena perubahan pada kelas induk dapat diterapkan ke semua kelas turunan yang mengoverride metode tersebut.

### Implementasi dalam Python
contoh implementasi override method dalam Python:

```python
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):  # Override method
        return "Bark!"

class Cat(Animal):
    def sound(self):  # Override method
        return "Meow!"

# Penggunaan
def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Bark!
make_sound(cat)  # Output: Meow!
```

### Kapan dan Mengapa Menggunakan Override Method
- **Kapan Digunakan:**
  - Ketika kelas turunan perlu memperbaiki atau menyesuaikan perilaku metode yang diwarisi dari kelas induk.
  - Ketika ada kebutuhan untuk menyediakan implementasi yang lebih spesifik berdasarkan konteks di kelas turunan.

- **Mengapa Digunakan:**
  - Untuk mencapai fleksibilitas dan kekuatan dalam desain OOP, terutama saat menggunakan polimorfisme.
  - Untuk membuat kode lebih bersih dan mudah dipelihara dengan mengurangi duplikasi kode.

5.Kapan Penggunaan Pewarisan

1. **Hubungan "Is-a":**
   - Gunakan pewarisan ketika ada hubungan yang jelas antara kelas induk dan kelas turunan yang dapat digambarkan dengan frasa "is-a". Contohnya, `Dog` adalah `Animal`, dan `Car` adalah `Vehicle`.
  
2. **Penggunaan Kembali Kode:**
   - Jika Anda memiliki beberapa kelas yang memiliki fungsi atau atribut yang sama, pewarisan memungkinkan Anda untuk mendefinisikan kode tersebut sekali di kelas induk dan kemudian mewariskannya ke kelas turunan.

3. **Polymorphism:**
   - Ketika Anda ingin menerapkan polymorphism, di mana metode dari kelas induk dapat dipanggil menggunakan referensi kelas induk tetapi dapat memiliki perilaku yang berbeda tergantung pada kelas turunan.

4. **Hierarki Kelas:**
   - Jika Anda ingin membangun hierarki yang jelas, di mana kelas-kelas yang lebih spesifik dapat diperluas dari kelas yang lebih umum, pewarisan adalah pilihan yang tepat.

5. **Memanfaatkan Fungsi `super()`:**
   - Ketika Anda ingin memanggil metode atau konstruktor dari kelas induk dalam kelas turunan, menggunakan pewarisan membuatnya lebih mudah dengan fungsi `super()`.

6.Kapan Menggunakan Non-Pewarisan (Komposisi)

1. **Hubungan "Has-a":**
   - Gunakan komposisi ketika ada hubungan yang lebih baik dijelaskan dengan frasa "has-a". Misalnya, `Car` memiliki `Engine`, tetapi `Car` bukanlah `Engine`. Dalam hal ini, komposisi lebih tepat daripada pewarisan.

2. **Fleksibilitas dan Modularitas:**
   - Komposisi memungkinkan Anda untuk mengubah bagian-bagian dari objek tanpa mempengaruhi keseluruhan struktur. Ini memberikan fleksibilitas lebih besar karena Anda dapat mengganti satu bagian (komponen) tanpa mengubah kelas utama.

3. **Menghindari Kompleksitas:**
   - Pewarisan yang berlebihan dapat menyebabkan hierarki kelas yang rumit dan sulit dipahami. Komposisi membantu menyederhanakan desain dengan memecah kelas menjadi komponen yang lebih kecil dan dapat digunakan kembali.

4. **Mengurangi Ketergantungan:**
   - Dalam komposisi, kelas tidak bergantung pada implementasi spesifik kelas lain. Ini mengurangi ketergantungan antara kelas dan membuatnya lebih mudah untuk mengubah atau mengganti bagian dari objek.

5. **Mendukung Penggunaan Kembali Kode:**
   - Komposisi memungkinkan Anda untuk menggunakan kembali kode dari beberapa kelas tanpa membuat hierarki yang dalam. Anda dapat menggabungkan beberapa komponen untuk membentuk objek yang lebih kompleks.

7.Studi Kasus
Sistem Manajemen Hewan di Kebun Binatang

Di sebuah kebun binatang, manajer kebun binatang ingin mengelola berbagai jenis hewan yang ada. Setiap hewan memiliki beberapa sifat dan perilaku yang sama, tetapi setiap jenis hewan juga memiliki perilaku khusus yang berbeda.

Manajer memutuskan untuk membuat sistem yang dapat mengelola hewan-hewan ini dengan cara yang efisien. Mereka memutuskan untuk menggunakan pewarisan untuk mengelompokkan hewan ke dalam kategori umum (seperti mamalia, burung, dan reptil) dan komposisi untuk mengelola perilaku spesifik dari setiap hewan, seperti suara yang dihasilkan dan cara mereka bergerak.

Implementasi Kode:
Berikut adalah implementasi kode untuk studi kasus ini:
# Kelas induk untuk semua hewan
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Kelas turunan untuk Mamalia
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def move(self):
        return f"{self.name} is walking on four legs."

# Kelas turunan untuk Burung
class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span

    def make_sound(self):
        return "Chirp!"

    def move(self):
        return f"{self.name} is flying."

# Kelas turunan untuk Reptil
class Reptile(Animal):
    def __init__(self, name, scale_color):
        super().__init__(name)
        self.scale_color = scale_color

    def make_sound(self):
        return "Hiss!"

    def move(self):
        return f"{self.name} is slithering."

# Komposisi untuk suara hewan
class AnimalSound:
    def __init__(self, sound):
        self.sound = sound

    def produce_sound(self):
        return self.sound

# Menggunakan komposisi untuk suara hewan tertentu
class Dog(Mammal):
    def __init__(self, name, fur_color):
        super().__init__(name, fur_color)
        self.sound = AnimalSound("Bark!")

    def make_sound(self):
        return self.sound.produce_sound()

class Parrot(Bird):
    def __init__(self, name, wing_span):
        super().__init__(name, wing_span)
        self.sound = AnimalSound("Squawk!")

    def make_sound(self):
        return self.sound.produce_sound()

# Membuat objek hewan
dog = Dog("Buddy", "Golden")
parrot = Parrot("Polly", "15 inches")
snake = Reptile("Slither", "Green")

# Menggunakan objek
animals = [dog, parrot, snake]

for animal in animals:
    print(f"{animal.name}:")
    print(f"  Sound: {animal.make_sound()}")
    print(f"  Movement: {animal.move()}\n")
    
Penjelasan Kode:
-Kelas Induk (Animal): Kelas ini berfungsi sebagai kelas dasar untuk semua hewan. Ini memiliki metode make_sound dan move yang akan diimplementasikan di kelas turunan.

-Kelas Turunan (Mammal, Bird, Reptile): Kelas-kelas ini mewarisi dari kelas Animal dan mengimplementasikan metode make_sound dan move sesuai dengan perilaku masing-masing jenis hewan. Setiap kelas juga menambahkan atribut 
 spesifik (seperti fur_color untuk mamalia).

-Komposisi (AnimalSound): Kelas ini digunakan untuk mengelola suara hewan. Kelas Dog dan Parrot menggunakan komposisi untuk menentukan suara mereka dengan membuat objek AnimalSound.

-Membuat Objek: Contoh objek hewan (Dog, Parrot, dan Reptile) dibuat dan dimasukkan ke dalam daftar animals.

-Menampilkan Informasi: Kode melakukan iterasi pada daftar hewan dan menampilkan nama, suara, dan cara bergerak masing-masing hewan.



















