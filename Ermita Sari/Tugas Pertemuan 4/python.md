PEMROGRAMAN BERORIENTASI OBJEK
1. KONSEP OOP
    OOP adalah singkatan dari Object-oriented programming paradigm. OOP didefinisikan sebagai model pemrograman yang menggunakan konsep objek yang mengacu pada entitas dunia nyata dengan status dan perilaku.

Pendekatan Berorientasi Prosedural
    Program komputer menggambarkan prosedur pelaksanaan tugas tertentu dengan menulis serangkaian instruksi dalam urutan yang logis. Logika program yang lebih kompleks dipecah menjadi blok pernyataan yang lebih kecil namun independen dan dapat digunakan kembali yang disebut fungsi.

Masalah-masalah yang menonjol terkait dengan pendekatan prosedural adalah sebagai berikut:
    -Pendekatannya yang top-down membuat program ini sulit dipertahankan.
    -Ia menggunakan banyak item data global, yang tidak diinginkan. Terlalu banyak item data global akan meningkatkan beban memori.
    -Ia memberi perhatian lebih pada proses dan tidak menganggap data sama pentingnya serta menganggapnya biasa saja, sehingga bergerak bebas melalui program.
    -Pergerakan data antar fungsi tidak dibatasi. Dalam skenario kehidupan nyata, ada asosiasi yang jelas antara suatu fungsi dengan data yang diharapkan dapat diproses.

Prinsip Konsep OOPs
    Paradigma pemrograman berorientasi objek dicirikan oleh prinsip-prinsip berikut: Kelas,Obyek,Enkapsulasi,Warisan dan Polimorfisme

2.Kelas & Objek
    2.1 kelas
    kelas adalah entitas yang ditentukan pengguna (tipe data) yang menentukan tipe data yang dapat ditampung suatu objek dan tindakan yang dapat dilakukannya.digunakan sebagai templat untuk membuat objek. Misalnya, jika kita ingin menentukan kelas untuk Ponsel Pintar dalam program Python, kita dapat menggunakan tipe data seperti RAM, ROM, ukuran layar, dan tindakan seperti panggilan dan pesan.

    Kelas memiliki string dokumentasi, yang dapat diakses melalui ClassName.__doc__.
    Class_suite terdiri dari semua pernyataan komponen yang mendefinisikan anggota kelas, atribut data, dan fungsi.

    contoh:
    class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

    2.2 objek
    Suatu objek disebut sebagai contoh dari suatu kelas Python. Setiap objek memiliki atribut dan metodenya sendiri, yang ditentukan oleh kelasnya.

    Ketika sebuah kelas dibuat, kelas tersebut hanya menggambarkan struktur objek. Memori dialokasikan ketika sebuah objek dibuat dari sebuah kelas.

    membuat kelas:gunakan metode __init__ .
    Mengakses Atribut Objek dalam Python:Variabel kelas akan diakses menggunakan nama kelas 

    contoh gabungan kelas dan objek
    class Employee:
   "Common base class for all employees"
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# This would create first object of Employee class
emp1 = Employee("mita", 2000)
# This would create second object of Employee class
emp2 = Employee("aqil", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

3.Atribute
    3.1 atribut kelas
    Atribut kelas adalah variabel yang termasuk dalam suatu kelas dan nilainya dibagi di antara semua instansi kelas tersebut. Atribut kelas tetap sama untuk setiap instansi kelas.

    Atribut kelas didefinisikan di dalam kelas tetapi di luar metode apa pun. Atribut tersebut tidak dapat diinisialisasi di dalam konstruktor __init__() . Atribut tersebut dapat diakses melalui nama kelas selain objek. Dengan kata lain, atribut kelas tersedia untuk kelas dan juga objeknya.

    contoh:
    class employe:
   name = "ERMITA SARI"
   age = "19"

# instance of the class
emp = Employee()
# accessing class attributes
print("Name of the Employee:", emp.name)
print("Age of the Employee:", emp.age)

    Pentingnya Atribut Kelas:

    Mereka digunakan untuk mendefinisikan properti suatu kelas yang harus memiliki nilai yang sama untuk setiap objek di kelas itu.
    Atribut kelas dapat digunakan untuk menetapkan nilai default untuk objek.
    Hal ini juga berguna dalam membuat singleton. Singleton adalah objek yang hanya dibuat satu kali dan digunakan di berbagai bagian kode.

    3.2 atribut instansi
    Seperti yang telah disebutkan sebelumnya, atribut instance dalam Python adalah variabel yang khusus untuk satu objek dalam satu kelas. Variabel ini didefinisikan di dalam metode __init__() .Parameter pertama metode ini adalah self dan menggunakan parameter ini atribut instan didefinisikan.

    contoh:
    class Student:
   def __init__(self, name, grade):
      self.__name = name
      self.__grade = grade
      print ("Name:", self.__name, ", Grade:", self.__grade)

# Creating instances 
student1 = Student("Ram", "B")
student2 = Student("Shyam", "C")

4.metode
    Metode merupakan bagian dari objek kelas dan digunakan untuk melakukan operasi tertentu. Kita dapat membagi metode Python ke dalam tiga kategori berbeda, yaitu metode kelas, metode instan, dan metode statis.
    a.metode kelas
        Metode kelas Python adalah metode yang terikat pada kelas dan bukan pada instans kelas. Metode ini dapat dipanggil pada kelas itu sendiri, bukan pada instans kelas.
    b.metode statis
        metode statis tidak memiliki akses ke parameter "cls" dan oleh karena itu tidak dapat mengubah status kelas.
    c.Metode instan
        metode instan dapat mengakses variabel instan dari suatu objek. Metode ini juga dapat mengakses variabel kelas karena variabel tersebut umum untuk semua objek.

    4.1 metode kelas
    Membuat Metode Kelas di Python:
        Menggunakan Fungsi classmethod()
        Menggunakan Dekorator @classmethod
    4.2 metode statis
        metode statis adalah jenis metode yang tidak memerlukan instans apa pun untuk dipanggil. Metode ini sangat mirip dengan metode kelas, tetapi perbedaannya adalah metode statis tidak memiliki argumen wajib seperti referensi ke objek − self atau referensi ke kelas − cls .

        Metode statis digunakan untuk mengakses bidang statis dari suatu kelas tertentu. Metode tersebut tidak dapat mengubah status suatu kelas karena terikat pada kelas, bukan instansi.
    membuat metide statis di python:
        Menggunakan Fungsi staticmethod()
        Menggunakan Dekorator @staticmethod

5.constructor
    Konstruktor Python adalah metode instan dalam suatu kelas, yang secara otomatis dipanggil setiap kali objek baru dalam kelas tersebut dibuat. Peran konstruktor adalah untuk menetapkan nilai ke variabel instan segera setelah objek tersebut dideklarasikan.

    Python menggunakan metode khusus yang disebut __init__() untuk menginisialisasi variabel instan untuk objek, segera setelah dideklarasikan.

    Jenis-jenis Konstruktor:
    1.Konstruktor Default 
    Konstruktor Python yang tidak menerima parameter apa pun selain self disebut sebagai konstruktor default.
    contoh:
    class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "mita"
      self.age = 19

    e1 = Employee()
    print ("Name: {}".format(e1.name))
    print ("age: {}".format(e1.age))

    2.Konstruktor Berparameter
    Jika suatu konstruktor didefinisikan dengan beberapa parameter beserta self-nya disebut konstruktor berparameter.
    contoh:
    class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

    e1 = Employee("mita", 19)
    e2 = Employee("cantika", 25)

    print ("Name: {}".format(e1.name))
    print ("age: {}".format(e1.age))
    print ("Name: {}".format(e2.name))
    print ("age: {}".format(e2.age))
