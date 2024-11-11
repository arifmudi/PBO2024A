Muhammad Rezky Ramadhan
2355201013


KONSEP OOP

Object-oriented programming (OOP) adalah paradigma programing yang berpusat pada objek. Objek dapat berupa data dan kode, yaitu field (atribut) dan procedure 
(method)2. OOP fokus pada manipulasi objek daripada logika yang digunakan untuk memanipulasinya. Beberapa keuntungan menggunakan OOP adalah modularity, skalabilitas, 
dan efisiensi. Prinsip-prinsip OOP meliputi abstraksi, encapsulasi, warisan, dan polymorfisme.

*Abstraksi*
Abstraksi adalah kemampuan untuk menyajikan hanya informasi yang dibutuhkan dari dunia luar tanpa menampilkan detail-detail yang tidak perlu. Hal ini membantu menjawab
kompleksitas sistem dengan fokus pada ciri-cirinya yang esensial.

*Encapsulasi*
Encapsulasi berarti bahwa objek harus mengekspor perilaku tetapi menyembunyikan hampir semua datanya. Ini dilakukan melalui method-method tertentu agar internal code 
tidak bisa diakses secara langsung oleh external code.

*Warisan*
Warisan atau inheritance memungkinkan pembuatan class baru yang mewarisi atribut dan method dari class induk. Class anak juga dapat menambahkan atau mengubah attribute 
dan method milik class induk.

*Polymorfisme*
Polymorfisme adalah kemampuan suatu objek untuk mengambil bentuk yang berbeda-beda. Polymorfisme dapat dicapai melalui overriding method, yaitu ketika subclass memberikan 
implementasi spesifik untuk method yang sudah ada di superclass


CLASS & OBJECT

Class adalah blueprint atau template yang mendefinisikan sifat dan perilaku objek. Setiap class memiliki atribut (data) dan method (fungsi) yang dapat digunakan oleh objek 
yang diinstansiasi dari class tersebut. Misalnya, dalam bahasa pemrograman Python, kita dapat mendefinisikan class Car seperti berikut:

    class mobil:
        def __init__(self, merek, model, tahun):
            self.make = merek
            self.model = model
            self.year = tahun

        def start_engine(self):
            print("Tsututututututututu")

Object adalah instance dari class. Ketika kita membuat objek dari class Car, kita dapat mengakses atribut dan method yang telah didefinisikan.
Contoh :

    toyota = Car("Toyota", "Corolla", 2020)
    toyota.start_engine()  


ATRIBUT

Atribut adalah variabel yang menyimpan data terkait objek. Atribut dapat berupa nilai numerik, string, atau tipe data lainnya. Dalam contoh class Car, atributnya adalah 
make, model, dan year. Setiap objek dari class Car akan memiliki salinan sendiri dari atribut-atribut ini.
Atribut dapat dibedakan menjadi:

    1. Instance Variables: Atribut yang dimiliki oleh setiap instance (objek) dari class.
    2. Class Variables: Atribut yang dimiliki oleh class itu sendiri dan dibagikan di antara semua instance.

Atribut dalam Object-Oriented Programming (OOP) merupakan variabel yang dimiliki oleh sebuah class dan digunakan untuk menyimpan data atau informasi tentang objek. Ada 
beberapa jenis atribut, termasuk instance variable, yang dimiliki oleh setiap instance (objek) dari class, dan class variable, yang dimiliki oleh class itu sendiri dan 
dibagikan di antara semua instance. Selain itu, atribut dapat memiliki kontrol akses yang berbeda-beda, seperti private, protected, dan public, untuk membatasi akses 
datanya. Misalnya, atribut nama dalam class Manusia dapat diinisialisasi sebagai instance variable (self.nama) dan dikontrol aksesnya dengan deklarasi private (_nama). 
Fungsi utamanya adalah mendeskripsikan karakteristik objek sehingga memudahkan manipulasi dan integrasi data dalam aplikasi.


METHOD

Method adalah fungsi yang didefinisikan dalam class dan digunakan untuk melakukan operasi pada objek. Method dapat mengakses dan memodifikasi atribut objek. Dalam contoh 
di atas, start_engine() adalah method yang mencetak pesan ketika dipanggil.
Ada dua jenis method:

    1. Instance Methods: Method yang beroperasi pada instance tertentu dari class.
    2. Class Methods: Method yang beroperasi pada class itu sendiri dan biasanya didekorasi dengan @classmethod.

Method dalam Object-Oriented Programming (OOP) adalah fungsi yang dideklarasikan dalam sebuah class dan digunakan untuk melakukan tindakan atau operasi pada objek. Setiap 
method dapat mengakses dan memanipulasi atribut objek, serta berfungsi untuk mendefinisikan perilaku spesifik dari objek tersebut. Misalnya, dalam class Mobil, kita bisa 
memiliki method seperti info_mobil() yang mencetak informasi tentang mobil berdasarkan atribut yang ada, seperti merek dan tahun produksi. Method juga dapat menerima parameter 
dan mengembalikan nilai, memungkinkan interaksi yang lebih kompleks antara objek. Selain itu, method dapat memiliki modifier akses seperti public, private, atau protected, yang 
mengatur tingkat aksesibilitasnya. Dengan cara ini, method membantu mengorganisir logika program dan memfasilitasi interaksi antar objek dalam sistem yang lebih besar.


CONTOH LAINNYA

Constructor adalah method khusus yang dipanggil saat objek baru dibuat. Constructor biasanya digunakan untuk menginisialisasi atribut objek dengan nilai awal. Dalam Python, 
constructor didefinisikan dengan nama __ init__ . Contoh:
python
    class mobil:
        def __init __(self, merek, model, tahun):
            self.make = merek
            self.model = model
            self.year = tahun

Ketika kita membuat objek baru menggunakan mobil("Toyota", "Corolla", 2020), constructor ini akan dipanggil secara otomatis untuk mengatur nilai atribut merek, model, dan tahun 
sesuai dengan parameter yang diberikan.