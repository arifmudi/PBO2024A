Nama    : Arjunaidi
Nim     : 2355201040
Matkul  : PBO
                                     Konsep OOP dalam pemograman                                           
OOP (Object-oriented programming) adalah konsep programing yang berpusat pada objek. Objek dapat berupa data dan kode, atribut dan Method. OOP fokus pada manipulasi objek daripada logika yang digunakan untuk memanipulasinya. Prinsip-prinsip OOP meliputi abstraksi, encapsulasi, warisan, dan polymorfisme.
  Abstraksi adalah kemampuan untuk menyajikan hanya informasi yang dibutuhkan dari dunia luar tanpa menampilkan detail-detail yang tidak perlu. 
  Encapsulasi berarti bahwa objek harus mengekspor perilaku tetapi menyembunyikan hampir semua datanya. Ini dilakukan melalui method-method tertentu agar internal code tidak bisa diakses secara langsung oleh external code.

Warisan dalam pemrograman, atau yang lebih dikenal dengan istilah inheritance, adalah salah satu konsep fundamental dalam paradigma pemrograman berorientasi objek (OOP). Konsep ini memungkinkan sebuah kelas (class) untuk mewarisi atribut dan metode dari kelas lain, yang dikenal sebagai kelas induk (parent class atau superclass).

Polymorfisme adalah kemampuan suatu objek untuk mengambil bentuk yang berbeda-beda. Polymorfisme dapat dicapai melalui overriding method, yaitu ketika subclass memberikan implementasi spesifik untuk method yang sudah ada di superclass


                                                Class OOP
Class adalah blueprint atau template yang mendefinisikan sifat dan perilaku objek. Setiap class memiliki atribut (data) dan method (fungsi) yang dapat digunakan oleh objek yang diinstansiasi dari class tersebut. Misalnya, dalam bahasa pemrograman Python, kita dapat mendefinisikan class Car seperti berikut:

    class mobil:
        def __init__(self, merek, model, tahun):
            self.make = merek
            self.model = model
            self.year = tahun

        def start_engine(self):
            print("brum")

Object adalah instance dari class. Ketika kita membuat objek dari class Car, kita dapat mengakses atribut dan method yang telah didefinisikan.
Contoh :

    toyota = Car("Bmw", "M4", "2002")
    toyota.start_engine()  

                                                      Atribut
Atribut adalah variabel yang menyimpan data terkait objek. Atribut dapat berupa nilai numerik, string, atau tipe data lainnya. Dalam contoh class Car, atributnya adalah make, model, dan year. Setiap objek dari class Car akan memiliki salinan sendiri dari atribut-atribut ini. Atribut dalam Object-Oriented Programming (OOP) merupakan variabel yang dimiliki oleh sebuah class dan digunakan untuk menyimpan data atau informasi tentang objek. Ada beberapa jenis atribut, termasuk instance variable, yang dimiliki oleh setiap instance (objek) dari class, dan class variable, yang dimiliki oleh class itu sendiri dan dibagikan di antara semua instance. Selain itu, atribut dapat memiliki kontrol akses yang berbeda-beda, seperti private, protected, dan public, untuk membatasi akses datanya. Misalnya, atribut nama dalam class Manusia dapat diinisialisasi sebagai instance variable (self.nama) dan dikontrol aksesnya dengan deklarasi private (_nama). Fungsi utamanya adalah mendeskripsikan karakteristik objek sehingga memudahkan manipulasi dan integrasi data dalam aplikasi. Method adalah fungsi yang didefinisikan dalam class dan digunakan untuk melakukan operasi pada objek. Method dapat mengakses dan memodifikasi atribut objek. Dalam contoh di atas, start_engine() adalah method yang mencetak pesan ketika dipanggil. Ada dua jenis method: Instance Methods dan Class Methods. Method dalam Object-Oriented Programming (OOP) adalah fungsi yang dideklarasikan dalam sebuah class dan digunakan untuk melakukan tindakan atau operasi pada objek. Setiap method dapat mengakses dan memanipulasi atribut objek, serta berfungsi untuk mendefinisikan perilaku spesifik dari objek tersebut. Misalnya, dalam class Mobil, kita bisa memiliki method seperti info_mobil() yang mencetak informasi tentang mobil berdasarkan atribut yang ada, seperti merek dan tahun produksi. Method juga dapat menerima parameter dan mengembalikan nilai, memungkinkan interaksi yang lebih kompleks antara objek. Selain itu, method dapat memiliki modifier akses seperti public, private, atau protected, yang mengatur tingkat aksesibilitasnya. Dengan cara ini, method membantu mengorganisir logika program dan memfasilitasi interaksi antar objek dalam sistem yang lebih besar.
