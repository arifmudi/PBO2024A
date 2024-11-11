1. Single Inheritence
    -Ini merupakan bentuk pewarisan paling sederhana di mana kelas anak mewarisi atribut dan metode hanya dari satu kelas induk.
    -implementasi:
#parent class
class Parent: 
   def parentMethod(self):
      print ("Calling parent method")

#child class
class Child(Parent): 
   def childMethod(self):
      print ("Calling child method")

#instance of child
c = Child()  
#calling method of child class
c.childMethod() 
#calling method of parent class
c.parentMethod() 

outputnya:
Calling child method
Calling parent method

    -Digunakan ketika: Single inheritance digunakan ketika Child bisa melakukan hal-hal yang sama seperti Parent, tetapi dengan tambahan kemampuannya sendiri. 

2. Super Inheritence
    - konsep: fungsi super() memungkinkan Anda mengakses metode dan atribut kelas induk dari dalam kelas anak.
    - implementasinya:
#parent class
class ParentDemo:
   def __init__(self, msg):
      self.message = msg

   def showMessage(self):
      print(self.message)

#child class
class ChildDemo(ParentDemo):
   def __init__(self, msg):
      # use of super function
      super().__init__(msg)  

#creating instance
obj = ChildDemo("Welcome to UP!!")
obj.showMessage() 

outputnya:
Welcome to UP!!

    -when: 
        -Saat ada metode di kelas induk yang ingin kamu gunakan di kelas turunan tanpa menulisnya lagi.
        -Ketika kamu ingin memakai metode induk dan menambahkan sesuatu yang baru di metode yang sama dalam kelas turunan.
        -super() juga sangat berguna dalam multiple inheritance untuk menghindari konflik atau kebingungan dalam memanggil metode dari beberapa kelas induk.
    -why:
        -Kode lebih efisien dan tidak berulang.
        -Metode dari kelas induk bisa digunakan dan diperluas di kelas turunan.
        -Struktur pewarisan terkelola dengan baik, khususnya dalam multiple inheritance.

3. Jenis-jenis pewarisan:
    1. Multiple inheritence
    -pengertian:Pewarisan berganda dalam Python memungkinkan Anda membuat kelas berdasarkan lebih dari satu kelas induk. Kelas Anak mewarisi atribut dan metode dari semua induk. Anak dapat mengganti metode yang diwarisi dari induk mana pun.
    -when:  -Kelas membutuhkan kombinasi perilaku dari beberapa sumber.
            -Sifat dan perilaku dapat dipisahkan ke dalam beberapa kategori yang jelas.
            -Aplikasi kompleks membutuhkan kelas dengan berbagai tanggung jawab tanpa kode duplikat.
    -how:   -Deklarasikan beberapa kelas induk dalam tanda kurung saat mendefinisikan kelas turunan.
            -Akses metode atau atribut dari semua kelas induk melalui objek kelas turunan.
            -Gunakan super() untuk memanggil metode kelas induk sesuai dengan urutan pewarisan (MRO).
    -contoh code:
class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d
      
class div_mod(division,modulus):
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)
x=div_mod(10,3)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())

outputnya:
division: 3.3333333333333335
mod_division: 1
divmod: (3.3333333333333335, 1)

    2. Multilevel Inheritance
    -pengertian:Dalam pewarisan bertingkat, suatu kelas diturunkan dari kelas turunan lainnya. Terdapat beberapa lapisan pewarisan. Kita dapat membayangkannya sebagai hubungan kakek-nenek-orang tua-anak.
    -when:  -ketika ingin membangun struktur hierarkis yang kompleks.
            -ketika ingin memanfaatkan kembali kode dan menghindari duplikasi.
            -ketika ingin mengabstraksi fitur umum dan menambah spesifikasi di tingkat yang lebih rendah.
            -ketika ingin memodelkan hubungan di dunia nyata dalam cara yang terstruktur.
    -how:   -Definisikan Kelas Induk yang berisi metode dan atribut umum.
            -Definisikan Kelas Turunan yang mewarisi dari kelas induk.
            -Buat Kelas Turunan Lebih Lanjut jika diperlukan, mewarisi dari kelas turunan sebelumnya.
            -Gunakan Kelas Turunan untuk membuat objek dan mengakses metode dari semua tingkat pewarisan.
    -contoh code:
#parent class
class Universe: 
   def universeMethod(self):
      print ("I am in the Universe")

#child class
class Earth(Universe): 
   def earthMethod(self):
      print ("I am on Earth")
      
#another child class
class India(Earth): 
   def indianMethod(self):
      print ("I am in India")      

#creating instance 
person = India()  
#method calls
person.universeMethod() 
person.earthMethod() 
person.indianMethod() 

outputnya:
I am in the Universe
I am on Earth
I am in India

    3.Hierarchical Inheritance
    -pengertian:Jenis pewarisan ini berisi beberapa kelas turunan yang diwarisi dari satu kelas dasar. Hal ini mirip dengan hierarki dalam suatu organisasi.
    -when:  -ketika mengorganisir kelas-kelas yang memiliki hubungan yang sama di bawah satu kelas induk.
            -ketika ingin mendefinisikan metode dan atribut umum yang dapat digunakan kembali di beberapa kelas turunan.
            -ketika ingin memodelkan hubungan di dunia nyata dengan cara yang terstruktur dan jelas.
            -ketika ingin menciptakan struktur kode yang modular dan mudah dikelola.
            -ketika berencana menggunakan polimorfisme untuk meningkatkan fleksibilitas kode.
    -how:   -Definisikan Kelas Induk: Buat kelas yang berisi metode dan atribut umum.
            -Definisikan Kelas Turunan: Buat beberapa kelas turunan yang mewarisi dari kelas induk dan menambahkan fungsionalitas spesifik mereka sendiri.
            -Gunakan Kelas Turunan: Buat objek dari kelas turunan dan akses metode dari kelas induk dan kelas turunan.
    -contoh code:
#parent class
class Manager: 
   def managerMethod(self):
      print ("I am the Manager")

#child class
class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
#second child class
class Employee2(Manager): 
   def employee2Method(self):
      print ("I am Employee two")      

#creating instances 
emp1 = Employee1()  
emp2 = Employee2()
#method calls
emp1.managerMethod() 
emp1.employee1Method()
emp2.managerMethod() 
emp2.employee2Method()

outputnya:
I am the Manager
I am Employee one
I am the Manager
I am Employee two

    4. Hybrid Inheritance
    -pengertian:-pengertian:Jenis pewarisan ini berisi beberapa kelas turunan yang diwarisi dari satu kelas dasar. Hal ini mirip dengan hierarki dalam suatu organisasi.
    -when:  -ketika perlu menggabungkan fitur dari beberapa kelas induk untuk menciptakan kelas turunan yang lebih kaya dalam          fungsionalitas.
            -ketika ingin menjaga kode tetap modular dan terpisah, memudahkan pengembangan dan pemeliharaan.
            -ketika ingin menggambarkan hubungan kompleks di dunia nyata dengan lebih akurat.
            -ketika ingin memanfaatkan polimorfisme untuk meningkatkan fleksibilitas dalam pengelolaan objek.
            -ketika ingin menghindari duplikasi kode dengan mendefinisikan fungsionalitas umum di kelas induk.
    -how:   -Definisikan Kelas Induk: Buat satu atau lebih kelas induk yang berisi metode dan atribut yang ingin diwarisi.
            -Definisikan Kelas Turunan: Buat kelas turunan yang mewarisi dari beberapa kelas induk.
            -Definisikan Kelas Turunan Lainnya: Jika diperlukan, Anda dapat membuat kelas turunan lainnya yang mewarisi dari kelas turunan pertama.
            -Gunakan Kelas Turunan: Buat objek dari kelas turunan dan akses metode dari kelas induk dan kelas turunan sesuai kebutuhan.
    -contoh code:
#parent class
class CEO: 
   def ceoMethod(self):
      print ("I am the CEO")
      
class Manager(CEO): 
   def managerMethod(self):
      print ("I am the Manager")

class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
class Employee2(Manager, CEO): 
   def employee2Method(self):
      print ("I am Employee two")      

#creating instances 
emp = Employee2()
#method calls
emp.managerMethod() 
emp.ceoMethod()
emp.employee2Method()

outputnya:
I am the Manager
I am the CEO
I am Employee two

PERBEDAAN:
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Single Inheritance                                                            |
|-----------------------------|-------------------------------------------------------------------------------|
| Pengertian                  | Mewarisi dari satu kelas induk.                                               |
| Contoh Implementasi         | `class B(A): pass`                                                            |
| Kapan Menggunakan           | Ketika kelas turunan hanya perlu satu dasar dari kelas induk.                 |
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Multiple Inheritance                                                          |
|-----------------------------|-------------------------------------------------------------------------------|
| Pengertian                  | Mewarisi dari lebih dari satu kelas induk.                                    |
| Contoh Implementasi         | `class C(A, B): pass`                                                         |
| Kapan Menggunakan           | Ketika kelas turunan membutuhkan sifat dari beberapa kelas induk.             |
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Multilevel Inheritance                                                        |
|-----------------------------|-------------------------------------------------------------------------------|
| Pengertian                  | Mewarisi dalam beberapa level (kelas induk, anak, cucu).                      |
| Contoh Implementasi         | `class C(B): pass` dan `class B(A): pass`                                     |
| Kapan Menggunakan           | Ketika ingin membuat hierarki yang panjang atau rantai turunan.               |
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Hierarchical Inheritance                                                      |
|-----------------------------|-------------------------------------------------------------------------------|
| Pengertian                  | Satu kelas induk diwarisi oleh beberapa kelas turunan.                        |
| Contoh Implementasi         | `class B(A): pass` dan `class C(A): pass`                                     |
| Kapan Menggunakan           | Ketika beberapa kelas perlu memiliki sifat yang sama dari satu kelas induk.   |
|-------------------------------------------------------------------------------------------------------------|
| Jenis Inheritance           | Hybrid Inheritance                                                            |
|-----------------------------|-------------------------------------------------------------------------------|
| Pengertian                  | Gabungan dari beberapa tipe inheritance, termasuk multiple dan multilevel.    |
| Contoh Implementasi         | `class C(A, B): pass` (A dan B bisa saling terkait)                           |
| Kapan Menggunakan           | Ketika membutuhkan kombinasi sifat dari beberapa inheritance untuk kasus      |
|                             | yang  kompleks.                                                               |
|-------------------------------------------------------------------------------------------------------------|

4. Method Overriding
-pengertian: Overloading metode merupakan fitur pemrograman berorientasi objek di mana suatu kelas dapat memiliki beberapa metode dengan nama yang sama tetapi parameternya berbeda. Untuk melakukan overloading metode, kita harus mengubah jumlah parameter atau jenis parameter, atau keduanya.
    -when:  -Saat Anda ingin mengubah perilaku metode dari kelas induk untuk disesuaikan dengan kebutuhan kelas turunan.
            -Untuk mendukung polimorfisme, di mana metode yang sama dapat berfungsi secara berbeda di kelas yang berbeda.
            -untuk memanfaatkan kode yang ada di kelas induk dan hanya menambahkan atau mengubah bagian yang perlu.
            -Dalam konteks kelas abstrak, Anda akan melakukan overriding pada metode yang dideklarasikan sebagai abstrak di kelas induk.
    -how:   -Mendefinisikan Kelas Induk: Pertama, buat kelas induk dengan metode yang ingin di-override.
            -Mendefinisikan Kelas Turunan: Buat kelas turunan yang mewarisi dari kelas induk.
            -Override Metode: Di dalam kelas turunan, definisikan kembali metode dengan nama yang sama dan tipe parameter yang sama seperti di kelas induk.
    -contoh code:
class example:
   def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))

outputnya:
60
30

5. Penggunaan inheritence,non-inheritence,dan komposisi
-1. Inheritance
Kapan Digunakan:
    -Hierarki Kelas: Ketika ada hubungan "adalah" yang jelas antara kelas induk dan kelas turunan (misalnya, Kucing adalah Hewan).
    -Reusabilitas Kode: Saat Anda ingin menggunakan kembali kode di kelas induk dan mengubah perilakunya di kelas turunan.
    -Polimorfisme: Ketika Anda ingin mengimplementasikan polimorfisme, di mana metode yang sama dapat memiliki perilaku berbeda tergantung pada objeknya.
    -Model Konsep yang Lebih Kompleks: Jika model domain Anda memiliki konsep yang kompleks dengan hierarki, inheritance bisa membantu mengorganisasikannya dengan baik.
Contoh Penggunaan:
    Menggunakan inheritance untuk mendefinisikan berbagai jenis kendaraan seperti Mobil, Motor, Truk, yang semuanya merupakan jenis Kendaraan.

-2. Non-Inheritance (Penggunaan Kelas Mandiri)
Kapan Digunakan:
    -Simplicity: Ketika Anda tidak memerlukan hierarki kompleks dan kelas-kelas dapat berfungsi secara independen.
    -Menghindari Overhead: Jika pewarisan tidak menambah nilai dan hanya menambah kompleksitas, menggunakan kelas mandiri lebih baik.
    -Tidak Ada Hubungan "Adalah": Ketika kelas-kelas tidak memiliki hubungan logis atau semantik antara satu sama lain.
Contoh Penggunaan:
    Mendefinisikan kelas Pengguna dan Produk yang tidak saling terkait dan tidak perlu berbagi fungsionalitas.

-3.Komposisi
Kapan Digunakan:
    -Penggabungan Fungsionalitas: Ketika Anda ingin menggabungkan beberapa objek untuk membentuk satu objek yang lebih besar tanpa menggunakan pewarisan.
    -Fleksibilitas: Jika Anda ingin menciptakan sistem yang lebih fleksibel dan dapat diperluas, di mana Anda bisa mengganti atau menambahkan komponen dengan mudah.
    -Relasi "Memiliki": Ketika objek memiliki hubungan "memiliki" (misalnya, Mobil memiliki Mesin dan Roda).
Contoh Penggunaan:
    Kelas Mobil dapat memiliki komponen seperti Mesin, Roda, dan SistemAudio, dan masing-masing dari komponen tersebut bisa menjadi kelas tersendiri yang bisa dipakai di banyak konteks.

6. Studi Kasus
-Soal Cerita
Seorang pengembang game ingin membuat simulasi mobil balap. Dalam simulasi ini, ada berbagai jenis mobil balap, seperti mobil sport dan mobil F1. Semua mobil memiliki beberapa atribut dan metode dasar, tetapi setiap jenis mobil memiliki beberapa perilaku dan fitur yang berbeda. Pengembang ingin menggunakan pewarisan untuk mengorganisir kode dan memungkinkan kemudahan dalam pengelolaan serta pengembangan di masa depan.

#Kelas induk
class MobilBalap:
    def __init__(self, merek, model, kecepatan_maks):
        self.merek = merek  # Merek mobil
        self.model = model  # Model mobil
        self.kecepatan_maks = kecepatan_maks  # Kecepatan maksimum mobil

    def info(self):
        """Menampilkan informasi dasar mobil balap."""
        return f"{self.merek} {self.model} dengan kecepatan maksimum {self.kecepatan_maks} km/jam."

    def akselerasi(self):
        """Metode untuk mengakselerasi mobil."""
        return f"{self.merek} {self.model} sedang mengakselerasi!"


#Kelas turunan untuk mobil sport
class MobilSport(MobilBalap):
    def __init__(self, merek, model, kecepatan_maks, tipe_mesin):
        super().__init__(merek, model, kecepatan_maks)  # Memanggil konstruktor kelas induk
        self.tipe_mesin = tipe_mesin  # Tipe mesin mobil sport

    def info(self):
        """Override metode info untuk menambahkan informasi tentang tipe mesin."""
        return f"{super().info()} Tipe mesin: {self.tipe_mesin}."


#Kelas turunan untuk mobil F1
class MobilF1(MobilBalap):
    def __init__(self, merek, model, kecepatan_maks, tim):
        super().__init__(merek, model, kecepatan_maks)  # Memanggil konstruktor kelas induk
        self.tim = tim  # Tim mobil F1

    def info(self):
        """Override metode info untuk menambahkan informasi tentang tim."""
        return f"{super().info()} Tim: {self.tim}."

    def akselerasi(self):
        """Override metode akselerasi untuk mobil F1."""
        return f"{self.merek} {self.model} F1 sedang mengakselerasi dengan kecepatan luar biasa!"


#Membuat objek dari kelas-kelas tersebut
mobil1 = MobilSport("Ferrari", "488", 330, "V8")
mobil2 = MobilF1("Mercedes", "W12", 360, "Mercedes AMG Petronas")

#Menampilkan informasi tentang mobil
print(mobil1.info())  # Menampilkan informasi mobil sport
print(mobil1.akselerasi())  # Menggunakan metode akselerasi

print(mobil2.info())  # Menampilkan informasi mobil F1
print(mobil2.akselerasi())  # Menggunakan metode akselerasi

-Penjelasan Kode
    1.Kelas Induk MobilBalap: Kelas ini menyimpan atribut umum seperti merek, model, dan kecepatan_maks. Metode info() dan akselerasi() memberikan informasi dasar tentang mobil.

    2.Kelas Turunan MobilSport: Kelas ini mewarisi dari MobilBalap dan menambahkan atribut baru tipe_mesin. Metode info() di-overridden untuk menyertakan informasi tentang tipe mesin.

    3.Kelas Turunan MobilF1: Kelas ini juga mewarisi dari MobilBalap dan menambahkan atribut tim. Metode info() di-overridden untuk menyertakan informasi tentang tim, dan metode akselerasi() juga di-overridden untuk memberikan perilaku yang berbeda.

    4.Instansiasi dan Penggunaan: Dua objek mobil1 dan mobil2 dibuat dari kelas MobilSport dan MobilF1. Metode info() dan akselerasi() dipanggil untuk menampilkan informasi dan perilaku masing-masing mobil.

