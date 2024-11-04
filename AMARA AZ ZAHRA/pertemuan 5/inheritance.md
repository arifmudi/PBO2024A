**1. Konsep Pewarisan Tunggal (Single Inheritance)**
    Pewarisan tunggal adalah ketika sebuah kelas (subkelas) mewarisi dari satu kelas induk saja. Dalam pewarisan ini, subkelas memperoleh properti dan metode dari kelas induk tunggalnya.

    *Implementasi di Python*:
        class Animal:
            def speak(self):
                return "Some sound"

        class Dog(Animal):  # Dog mewarisi dari Animal
            def bark(self):
                return "Woof!"

    Pewarisan tunggal digunakan ketika subkelas hanya membutuhkan fitur dari satu kelas induk. Misalnya, kelas `Dog` hanya perlu mewarisi karakteristik dari kelas `Animal`, tidak perlu dari kelas lain.

**2. Konsep `super()` untuk Pewarisan di Konstruktor**
    Di Python, fungsi super() memungkinkan Anda mengakses metode dan atribut kelas induk dari dalam kelas anak.
    Fungsi `super()` digunakan untuk memanggil metode dari kelas induk. Biasanya digunakan di dalam konstruktor (`__init__`) agar subkelas dapat menginisialisasi atribut dari kelas induknya tanpa perlu menulis ulang seluruh kode.

    *Implementasi di Python*:
        class Animal:
            def __init__(self, name):
                self.name = name

        class Dog(Animal):
            def __init__(self, name, breed):
                super().__init__(name)  # Memanggil konstruktor kelas induk
                self.breed = breed

    `super()` digunakan untuk menyederhanakan kode ketika Anda ingin mengakses metode atau konstruktor dari kelas induk. Ini bermanfaat untuk menjaga kode tetap ringkas dan mudah dibaca.

**3. Jenis-jenis Pewarisan**   
    
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    | Jenis Inheritance |                  Deskripsi                        |        Contoh Implementasi        |                 Kapan Digunakan                 |
    |-------------------+---------------------------------------------------+-----------------------------------+-------------------------------------------------|
    | *Single*          | Mewarisi dari satu kelas induk                    | `class Dog(Animal)`               | Saat hanya butuh dari satu kelas induk          |
    | *Multiple*        | Mewarisi dari lebih dari satu kelas induk         | `class Hybrid(Dog, Cat)`          | Saat butuh fitur dari beberapa kelas induk      |
    | *Multilevel*      | Mewarisi secara berurutan dari beberapa kelas     | `class Puppy(Dog)`                | Untuk pewarisan bertingkat                      |
    | *Hierarchical*    | Beberapa subkelas mewarisi dari satu kelas induk  | `class Dog(Animal), Cat(Animal)`  | Saat beberapa kelas berbagi satu induk          |
    | *Hybrid*          | Kombinasi dari beberapa jenis pewarisan           | `class HybridDog(Dog, Robot)`     | Ketika butuh gabungan tipe pewarisan            |
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    *A.Python - Single Inheritance*
        Bentuk pewarisan paling sederhana di mana kelas anak mewarisi atribut dan metode hanya dari satu kelas induk.
    *B.Python - Multiple Inheritance*
        Membangun kelas berdasarkan lebih dari satu kelas induk. Kelas Child dengan demikian mewarisi atribut dan metode dari semua induk. Anak dapat mengganti metode yang diwarisi dari induk mana pun.
    *C.Python - Multilevel Inheritance*
        Dalam pewarisan multilevel, kelas diturunkan dari kelas turunan lainnya. Ada banyak lapisan pewarisan. Kita bisa membayangkannya sebagai hubungan kakek-nenek-tua-anak.
    *D.Python - Hierarchical Inheritance*
        Jenis pewarisan ini berisi beberapa kelas turunan yang diwarisi dari satu kelas dasar. Ini mirip dengan hierarki dalam suatu organisasi.
    *E.Python - Hybrid Inheritance*
        Kombinasi dua atau lebih jenis warisan disebut sebagai Pewarisan Hibrida. Misalnya, itu bisa berupa campuran pewarisan tunggal dan ganda.

    *Contoh Implementasi untuk Multiple Inheritance:*
        class Animal:
            def eat(self):
                return "Eating"

        class Flyable:
            def fly(self):
                return "Flying"

        class Bird(Animal, Flyable):
            pass

**4. Override Method**
    Override (penulisan ulang) memungkinkan subkelas untuk mengubah perilaku metode yang diwarisi dari kelas induk.

    *Implementasi di Python:*
        class Animal:
            def speak(self):
                return "Some sound"

        class Dog(Animal):
            def speak(self):  # Override method `speak` dari `Animal`
                return "Woof!"

    Override method digunakan saat subkelas membutuhkan perilaku yang berbeda dari kelas induknya, seperti pada kasus `Dog` yang memiliki suara berbeda dari `Animal`.

**5. Kapan Menggunakan Pewarisan**
    Pewarisan adalah salah satu fitur terpenting dari bahasa pemrograman berorientasi objek seperti Python. Ini digunakan untuk mewarisi properti dan perilaku satu kelas ke kelas lainnya. Kelas yang mewarisi kelas lain disebut kelas anak dan kelas yang diwariskan disebut kelas dasar atau kelas induk.
    Pewarisan memungkinkan kemampuan kelas yang ada untuk digunakan kembali dan jika diperlukan diperluas untuk merancang kelas baru.
    Pewarisan muncul ketika kelas baru memiliki hubungan 'IS A' dengan kelas yang ada. Misalnya, Mobil ADALAH kendaraan, Bus ADALAH kendaraan, Sepeda JUGA kendaraan. Di sini, Kendaraan adalah kelas induk, sedangkan mobil, bus, dan sepeda adalah kelas anak.
    Pewarisan memungkinkan kita untuk mendefinisikan kelas yang mewarisi semua metode dan properti dari kelas lain.
    *Parent class* adalah class yang diwariskan, juga disebut kelas dasar.
    *Child class* adalah kelas yang mewarisi dari kelas lain, juga disebut kelas turunan.
    Gunakan pewarisan ketika:
    - Terdapat hubungan “is-a” antara kelas (misalnya, `Dog` adalah `Animal`).
    - Subkelas membutuhkan fitur atau perilaku dari kelas induk yang dapat digunakan ulang tanpa perubahan signifikan.

**6. Kapan Menggunakan Non-Pewarisan (Komposisi)**
    Gunakan komposisi ketika:
    - Tidak ada hubungan “is-a” yang jelas antara kelas, namun lebih pada hubungan “has-a”.
    - Anda ingin memisahkan tanggung jawab dari dua kelas yang berbeda.
    - Lebih fleksibel daripada pewarisan dan mencegah pewarisan yang terlalu dalam.

    *Contoh Komposisi:*
        class Engine:
            def start(self):
                return "Engine started"

        class Car:
            def __init__(self):
                self.engine = Engine()  # Komposisi: Car memiliki Engine

            def start_car(self):
                return self.engine.start()

**7. Studi Kasus dan Implementasi**
    *Studi Kasus*: Sistem Manajemen Perpustakaan
    Sebuah perpustakaan ingin mengembangkan sistem manajemen untuk mengelola buku dan anggota perpustakaan. Dalam sistem ini, terdapat berbagai jenis buku, seperti buku fiksi dan buku non-fiksi. Untuk memudahkan pengelolaan data, kita akan menggunakan konsep inheritance (pewarisan) dalam pemrograman berorientasi objek (OOP) di Python.
    
    *Tujuan*
    Membuat kelas dasar Buku dan dua kelas turunan BukuFiksi dan BukuNonFiksi untuk mengelola data buku dengan cara yang lebih terstruktur dan efisien.
    
    *Deskripsi Kelas*
    1. Buku (Kelas Dasar)
    *Atribut:
        judul: Judul buku
        pengarang: Pengarang buku
        tahun_terbit: Tahun terbit buku
    *Metode:
        tampilkan_info(): Menampilkan informasi dasar buku.
    2. BukuFiksi (Kelas Turunan)
    *Atribut tambahan:
        genre: Genre buku fiksi
    *Metode:
        tampilkan_info(): Menampilkan informasi buku fiksi, termasuk genre.
    3. BukuNonFiksi (Kelas Turunan)
    *Atribut tambahan:
        topik: Topik buku non-fiksi
    *Metode:
        tampilkan_info(): Menampilkan informasi buku non-fiksi, termasuk topik.
    
    *Implementasi*
        class Buku:
            def __init__(self, judul, pengarang, tahun_terbit):
                self.judul = judul
                self.pengarang = pengarang
                self.tahun_terbit = tahun_terbit

            def tampilkan_info(self):
                print(f"Judul: {self.judul}")
                print(f"Pengarang: {self.pengarang}")
                print(f"Tahun Terbit: {self.tahun_terbit}")

        class BukuFiksi(Buku):
            def __init__(self, judul, pengarang, tahun_terbit, genre):
                super().__init__(judul, pengarang, tahun_terbit)
                self.genre = genre

            def tampilkan_info(self):
                super().tampilkan_info()
                print(f"Genre: {self.genre}")

        class BukuNonFiksi(Buku):
            def __init__(self, judul, pengarang, tahun_terbit, topik):
                super().__init__(judul, pengarang, tahun_terbit)
                self.topik = topik

            def tampilkan_info(self):
                super().tampilkan_info()
                print(f"Topik: {self.topik}")

        #  Contoh Penggunaan
        buku1 = BukuFiksi("Harry Potter dan Batu Bertuah", "J.K. Rowling", 1997, "Fantasi")
        buku1.tampilkan_info()
        print("\n" + "="*30 + "\n")
        buku2 = BukuNonFiksi("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, "Sejarah")
        buku2.tampilkan_info()

        *Penjelasan Kode*
        1. Kelas Buku: Kelas dasar yang menyimpan informasi umum tentang buku.
        2. Kelas BukuFiksi: Kelas turunan yang menambahkan atribut genre dan metode untuk menampilkan informasi buku fiksi.
        3. Kelas BukuNonFiksi: Kelas turunan yang menambahkan atribut topik dan metode untuk menampilkan informasi buku non-fiksi.
        4. Contoh Penggunaan: Membuat objek dari kedua kelas turunan dan menampilkan informasi masing-masing buku.
