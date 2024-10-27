#OOP
OOP adalah singkatan dari paradigma pemrograman berorientasi objek. Ini didefinisikan sebagai model pemrograman yang menggunakan konsep objek yang mengacu pada entitas dunia nyata dengan keadaan dan perilaku. Bab ini membantu Anda menjadi ahli dalam menggunakan dukungan pemrograman berorientasi objek dalam bahasa Python.

Python adalah bahasa pemrograman yang mendukung pemrograman berorientasi objek. Ini membuatnya mudah untuk membuat dan menggunakan kelas dan objek. Jika Anda tidak memiliki pengalaman sebelumnya dengan pemrograman berorientasi objek, Anda berada di tempat yang tepat. Mari kita mulai dengan membahas pengenalan kecil tentang Pemrograman Berorientasi Objek (OOP) untuk membantu Anda.

Python - Konsep OOP
Di dunia nyata, kita berurusan dengan dan memproses objek, seperti siswa, karyawan, faktur, mobil, dll. Objek bukan hanya data dan bukan hanya fungsi, tetapi kombinasi keduanya. Setiap objek dunia nyata memiliki atribut dan perilaku yang terkait dengannya.

Atribut
-Nama, kelas, mata pelajaran, nilai, dll.,
-Nama, jabatan, departemen, gaji, dll., karyawan
-Nomor faktur, pelanggan, kode dan nama produk, harga dan kuantitas, dll., Dalam faktur
-Nomor registrasi, pemilik, perusahaan, merek, tenaga kuda, kecepatan, dll., Mobil

Prinsip Konsep OOP
Paradigma pemrograman berorientasi objek ditandai dengan prinsip-prinsip berikut :
-Kelas
-Benda
-Enkapsulasi
-Warisan
-Polimorfisme


#CLAS AND OBJEK

Kelas adalah prototipe yang ditentukan pengguna untuk objek yang mendefinisikan sekumpulan atribut yang mencirikan objek apa pun dari kelas tersebut. Atribut adalah anggota data (variabel kelas dan variabel instance) dan metode, diakses melalui notasi titik.

Objek mengacu pada instance dari kelas tertentu. Misalnya, objek bernama obj yang termasuk dalam kelas Circle adalah instance dari kelas tersebut. Contoh unik dari struktur data yang ditentukan oleh kelasnya. Sebuah objek terdiri dari anggota data (variabel kelas dan variabel instance) dan metode.

Python adalah bahasa pemrograman berorientasi objek.
Hampir semua yang ada di Python adalah objek, dengan properti dan metodenya.
Kelas seperti konstruktor objek, atau "cetak biru" untuk membuat objek.

Untuk membuat kelas, gunakan kata kunci :class
Contoh:
Buat kelas bernama MyClass, dengan properti bernama x:

class MyClass:
  x = 5
print(MyClass)

a)Fungsi __init__()
Contoh di atas adalah kelas dan objek dalam bentuk yang paling sederhana, dan tidak terlalu berguna dalam aplikasi kehidupan nyata.

Untuk memahami arti kelas kita harus memahami __init__() bawaan fungsi.

Semua kelas memiliki fungsi yang disebut __init__(), yang selalu dieksekusi ketika Kelas sedang dimulai.

Gunakan fungsi __init__() untuk menetapkan nilai ke properti objek, atau lainnya operasi yang perlu dilakukan ketika objek sedang dibuat:

Contoh
Buat kelas bernama Person, gunakan fungsi __init__() untuk menetapkan nilai Untuk nama dan usia:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

b)Fungsi __str__()
Fungsi __str__() mengontrol apa yang harus dikembalikan ketika objek kelas direpresentasikan sebagai string.

Jika fungsi __str__() tidak diatur, representasi string dari objek dikembalikan:

c)Metode Objek
Objek juga dapat berisi metode. Metode dalam objek adalah fungsi yang milik objek.

Mari kita buat metode di kelas Person:

Contoh
Masukkan fungsi yang mencetak salam, dan jalankan pada objek p1:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

d)Parameter diri
Parameter adalah referensi ke instance kelas saat ini, dan digunakan untuk mengakses variabel yang termasuk dalam kelas.self

Tidak harus disebutkan namanya, Anda bisa sebut saja apa pun yang Anda suka, tetapi itu harus menjadi parameter pertama dari fungsi apa pun Di kelas:self

Contoh
Gunakan kata mysillyobject dan abc alih-alih self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

Contoh
Contoh di bawah ini mengilustrasikan cara membuat kelas dan objeknya di Python.
# defining class
class Smartphone:
   # constructor    
   def __init__(self, device, brand):
      self.device = device
      self.brand = brand
   
   # method of the class
   def description(self):
      return f"{self.device} of {self.brand} supports Android 14"

# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung")
print(phoneObj.description()) 


#ATRIBUT
Properti atau variabel yang didefinisikan di dalam kelas disebut sebagai Atribut. Atribut memberikan informasi tentang jenis data yang terkandung dalam kelas. Ada dua jenis atribut di Python yaitu atribut instance dan atribut class.

Atribut instance didefinisikan dalam konstruktor kelas Python dan unik untuk setiap instance kelas. Dan, atribut kelas dideklarasikan dan diinisialisasi di luar konstruktor kelas.

a)Atribut Kelas (Variabel)
Atribut kelas adalah variabel yang termasuk dalam kelas dan yang nilainya dibagikan di antara semua instance kelas tersebut. Atribut class tetap sama untuk setiap instance kelas.

Atribut kelas didefinisikan di kelas tetapi di luar metode apa pun. Mereka tidak dapat diinisialisasi di dalam konstruktor __init__(). Mereka dapat diakses dengan nama kelas selain objek. Dengan kata lain, atribut kelas tersedia untuk kelas serta objeknya.

c)Mengakses Atribut Kelas
Nama objek diikuti dengan notasi titik (.) digunakan untuk mengakses atribut kelas.

Contoh
Contoh di bawah ini menunjukkan cara mengakses atribut kelas Python.

class Employee:
   name = "Bhavesh Aggarwal"
   age = "30"

# instance of the class
emp = Employee()
# accessing class attributes
print("Name of the Employee:", emp.name)
print("Age of the Employee:", emp.age)

Output:
Name of the Employee: Bhavesh Aggarwal
Age of the Employee: 30

Memodifikasi Atribut Kelas
Untuk memodifikasi nilai atribut kelas, kita hanya perlu menetapkan nilai baru padanya menggunakan nama kelas diikuti dengan notasi titik dan nama atribut.

Contoh
Dalam contoh di bawah ini, kita menginisialisasi variabel kelas yang disebut empCount di kelas Employee. Untuk setiap objek yang dideklarasikan, metode __init__() secara otomatis dipanggil. Metode ini menginisialisasi variabel instans serta menambah empCount sebesar 1.

class Employee:
   # class attribute    
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      # modifying class attribute
      Employee.empCount += 1
      print ("Name:", self.__name, ", Age: ", self.__age)
      # accessing class attribute
      print ("Employee Count:", Employee.empCount)

e1 = Employee("Bhavana", 24)
print()
e2 = Employee("Rajesh", 26)

Output:
Kita telah mendeklarasikan dua objek. Setiap kali, empCount bertambah 1.

Name: Bhavana , Age:  24
Employee Count: 1

Name: Rajesh , Age:  26
Employee Count: 2


#METHOD

Metode milik objek kelas dan digunakan untuk melakukan operasi tertentu. Kita dapat membagi metode Python dalam tiga kategori berbeda, yaitu metode kelas, metode instance, dan metode statis.

Metode kelas Python adalah metode yang terikat ke kelas dan bukan ke instance kelas. Ini dapat dipanggil pada kelas itu sendiri, bukan pada instance kelas.

Sebagian besar dari kita sering mendapatkan metode kelas yang dikacaukan dengan metode statis. Selalu ingat, sementara keduanya dipanggil pada kelas, metode statis tidak memiliki akses ke parameter "cls" dan oleh karena itu tidak dapat memodifikasi status kelas.

Tidak seperti metode kelas, metode instance dapat mengakses variabel instance dari objek. Itu juga dapat mengakses variabel kelas karena umum untuk semua objek.

Membuat Metode Kelas di Python
Ada dua cara untuk membuat metode kelas di Python −

-Menggunakan fungsi classmethod()
-Menggunakan @classmethod Decorator

a)Menggunakan fungsi classmethod()
Python memiliki fungsi bawaan classmethod() yang mengubah metode instance menjadi metode kelas yang dapat dipanggil dengan referensi ke kelas saja dan bukan objek.

Sintaksis
classmethod(instance_method)
Contoh
Di kelas Employee, tentukan metode instance showcount() dengan argumen "self" (referensi ke memanggil objek). Ini mencetak nilai empCount. Selanjutnya, ubah metode menjadi metode kelas counter() yang dapat diakses melalui referensi kelas.

class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):
      print (self.empCount)
      
   counter = classmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount()
Employee.counter()

Output
Panggil showcount() dengan objek dan panggil count() dengan kelas, keduanya menunjukkan nilai jumlah karyawan.

3
3

b)Atribut Kelas Akses dalam Metode Kelas
Atribut kelas adalah variabel yang termasuk dalam kelas dan yang nilainya dibagikan di antara semua instance kelas tersebut.

Untuk mengakses atribut kelas dalam metode kelas, gunakan parameter cls diikuti dengan notasi titik (.) dan nama atribut.

Contoh
Dalam contoh ini, kita mengakses atribut kelas dalam metode kelas.
class Cloth:
   # Class attribute
   price = 4000

   @classmethod
   def showPrice(cls):
      return cls.price

# Accessing class attribute
print(Cloth.showPrice())  

Output:
Saat menjalankan kode di atas, itu akan menampilkan output berikut -

4000

c)Menghapus Metode Kelas Secara Dinamis
Operator del Python digunakan untuk menghapus metode kelas secara dinamis. Jika Anda mencoba mengakses metode yang dihapus, kode akan memunculkan AttributeError.

Contoh
Dalam contoh di bawah ini, kita menghapus metode kelas bernama "brandName" menggunakan operator del.

Buka Kompiler
class Cloth:
   # class method
   @classmethod
   def brandName(cls):
      print("Name of the brand is Raymond")

# deleting dynamically
del Cloth.brandName
print("Method deleted")

Saat mengeksekusi kode di atas, itu akan menampilkan output berikut −

Method deleted

#CONSTRUKTOR
Konstruktor Python adalah metode instance dalam kelas, yang secara otomatis dipanggil setiap kali objek baru dari kelas dibuat. Peran konstruktor adalah untuk menetapkan nilai ke variabel instance segera setelah objek dideklarasikan.

Python menggunakan metode khusus yang disebut __init__() untuk menginisialisasi variabel instance untuk objek, segera setelah dideklarasikan.

a)Membuat konstruktor di Python
Metode __init__() bertindak sebagai konstruktor. Dibutuhkan argumen wajib bernama self, yang merupakan referensi ke objek.

def __init__(self, parameters):
#initialize instance variables

Metode __init__() serta metode instance apa pun dalam kelas memiliki parameter wajib, self. Namun, Anda dapat memberikan nama apa pun untuk parameter pertama, tidak harus sendiri.

Jenis Konstruktor di Python
Python memiliki dua jenis konstruktor −

-Konstruktor Default
-Konstruktor Parameter

a)Konstruktor Default di Python
Konstruktor Python yang tidak menerima parameter apa pun selain self disebut sebagai konstruktor default.

Contoh
Mari kita definisikan konstruktor di kelas Employee untuk menginisialisasi nama dan usia sebagai variabel instance. Kita kemudian dapat mengakses atribut ini melalui objeknya.

class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Bhavana"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))

Ini akan menghasilkan output berikut −

Name: Bhavana
age: 24

b)Konstruktor Parameter
Jika konstruktor didefinisikan dengan beberapa parameter bersama dengan self disebut sebagai konstruktor berparameter.

Contoh
Dalam contoh ini, konstruktor __init__() memiliki dua argumen formal. Kami mendeklarasikan objek Employee dengan nilai yang berbeda −

class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

e1 = Employee("Bhavana", 24)
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

Ini akan menghasilkan output berikut −

Name: Bhavana
age: 24
Name: Bharat
age: 25

c)Python - Metode Instans
Selain konstruktor __init__(), mungkin ada satu atau lebih metode instance yang didefinisikan dalam sebuah kelas. Metode dengan self sebagai salah satu argumen formal disebut metode instance, karena dipanggil oleh objek tertentu.

Contoh
Dalam contoh berikut, metode displayEmployee() telah didefinisikan sebagai metode instance. Ini mengembalikan atribut nama dan usia objek Employee yang memanggil metode.

class Employee:
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

e1 = Employee()
e2 = Employee("Bharat", 25)

e1.displayEmployee()
e2.displayEmployee()

Ini akan menghasilkan output berikut −

Name : Bhavana , age: 24
Name : Bharat , age: 25

d)Python Beberapa Konstruktor
Seperti yang disebutkan sebelumnya, kita mendefinisikan metode __init__() untuk membuat konstruktor. Namun, tidak seperti bahasa pemrograman lain seperti C++ dan Java, Python tidak mengizinkan banyak konstruktor.

Jika Anda mencoba membuat beberapa konstruktor, Python tidak akan melemparkan kesalahan, tetapi hanya akan mempertimbangkan metode __init__() terakhir di kelas Anda. Definisi sebelumnya akan ditimpa oleh yang terakhir.

Tapi, ada cara untuk mencapai fungsionalitas serupa di Python. Kita dapat membebani konstruktor berdasarkan jenis atau jumlah argumen yang diteruskan ke metode __init__(). Ini akan memungkinkan metode konstruktor tunggal untuk menangani berbagai skenario inisialisasi berdasarkan argumen yang disediakan.

