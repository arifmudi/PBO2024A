1. **Python-Konsep OOP**
    Di dunia nyata, kita berurusan dengan dan memproses objek, seperti siswa, karyawan, faktur, mobil, dll. Objek bukan hanya data dan bukan hanya fungsi, tetapi kombinasi keduanya. Setiap objek dunia nyata memiliki atribut dan perilaku yang terkait dengannya.

    OOP (Object-Oriented Programming) adalah singkatan dari paradigma pemrograman berorientasi objek. Ini didefinisikan sebagai model pemrograman yang menggunakan konsep objek yang mengacu pada entitas dunia nyata dengan keadaan dan perilaku.

    Misalnya, sebuah objek dapat mewakili seseorang dengan properti seperti nama, usia, dan alamat serta perilaku seperti berjalan, berbicara, bernapas, dan berlari. Atau bisa mewakili email dengan properti seperti daftar penerima, subjek, dan isi serta perilaku seperti menambahkan lampiran dan mengirim.

    Dengan kata lain, pemrograman berorientasi objek adalah pendekatan untuk memodelkan hal-hal konkret di dunia nyata, seperti mobil, serta hubungan antara hal-hal, seperti perusahaan dan karyawan atau siswa dan guru. OOP memodelkan entitas dunia nyata sebagai objek perangkat lunak yang memiliki beberapa data yang terkait dengannya dan dapat melakukan operasi tertentu.

    Prinsip Konsep OOP : Paradigma pemrograman berorientasi objek ditandai dengan prinsip-prinsip yaitu, Class, Object, Encapsulation, Inheritance, Polymorphism.

2. **Python-Class & Object**
    Class adalah prototipe yang ditentukan pengguna untuk objek yang mendefinisikan sekumpulan atribut yang mencirikan objek apa pun dari kelas tersebut. Atribut adalah anggota data (variabel kelas dan variabel instance) dan metode, diakses melalui notasi titik.

    Object mengacu pada instance dari kelas tertentu. Misalnya, objek bernama obj yang termasuk dalam kelas Circle adalah instance dari kelas tersebut. Contoh unik dari struktur data yang ditentukan oleh kelasnya. Sebuah objek terdiri dari anggota data (variabel kelas dan variabel instance) dan metode.
    
    Kelas adalah blueprint atau cetak biru untuk membuat objek. Ini mendefinisikan atribut dan metode yang akan dimiliki oleh objek yang akan dibuat dari kelas tersebut.
    # Create a Class
    To create a class, use the keyword class:
    Example
    Create a class named MyClass, with a property named x:

        class MyClass:
        x = 5

    Objek adalah instance dari kelas. Ketika Anda membuat objek, Anda membuat instansi kelas dengan atribut dan metode yang telah ditentukan oleh kelas.
    # Create Object
    Now we can use the class named MyClass to create objects:
    Example
    Create an object named p1, and print the value of x:

        p1 = MyClass()
        print(p1.x)

    *EXAMPLE:*
   
        #defining class
        class Smartphone:
            #constructor    
            def __init__(self, device, brand):
                self.device = device
                self.brand = brand
            #method of the class
            def description(self):
                return f"{self.device} of {self.brand} supports Android 14"
            #creating object of the class
            phoneObj = Smartphone("Smartphone", "Samsung")
            print(phoneObj.description())
            OUTPUT: "Smartphone of Samsung supports Android 14"

    # The __init__() Function
    Untuk memahami arti kelas kita harus memahami __init__() bawaan fungsi.
    Semua kelas memiliki fungsi yang disebut __init__(), yang selalu dieksekusi ketika Kelas sedang dimulai.
    Gunakan fungsi __init__() untuk menetapkan nilai ke properti objek, atau lainnya operasi yang perlu dilakukan ketika       objek sedang dibuat:
    *Contoh*
    Buat kelas bernama Person, gunakan fungsi __init__() untuk menetapkan nilai Untuk nama dan usia:
   
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            p1 = Person("Rara", 19)
            print(p1.name)
            print(p1.age)
            Output: "Rara"
                    19
    *Note: Fungsi ini dipanggil secara otomatis setiap kali kelas digunakan untuk membuat objek baru.__init__()*

    # The __str__() Function
    Fungsi __str__() mengontrol apa yang harus dikembalikan ketika objek kelas direpresentasikan sebagai string.
    Jika fungsi __str__() tidak diatur, representasi string dari objek dikembalikan:
    Contoh
    Representasi string dari objek DENGAN fungsi __str__():
   
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def __str__(self):
            return f"{self.name}({self.age})"
        p1 = Person("Rara", 19)
        print(p1)
        Output: "Rara(19)"

4. **Python-Attributes**
    Atribut adalah variabel yang terkait dengan objek dan digunakan untuk menyimpan data tentang objek tersebut. Atribut didefinisikan di dalam kelas.
    Setiap atribut akan memiliki nilai yang terkait dengannya. Atribut setara dengan data.
    * Name, class, subjects, marks, etc., of student
    * Name, designation, department, salary, etc., of employee
    * Invoice number, customer, product code and name, price and quantity, etc., in an invoice
    * Registration number, owner, company, brand, horsepower, speed, etc., of car

    # Atribut Kelas (Variabel)
    Atribut kelas adalah variabel yang termasuk dalam kelas dan yang nilainya dibagikan di antara semua instance kelas tersebut. Atribut class tetap sama untuk setiap instance kelas.

    Atribut kelas didefinisikan di kelas tetapi di luar metode apa pun. Mereka tidak dapat diinisialisasi di dalam konstruktor __init__(). Mereka dapat diakses dengan nama kelas selain objek. Dengan kata lain, atribut kelas tersedia untuk kelas serta objeknya.

    # Mengakses Atribut Kelas
    Nama objek diikuti dengan notasi titik (.) digunakan untuk mengakses atribut kelas.
    *Contoh*
    Contoh di bawah ini menunjukkan cara mengakses atribut kelas Python.
   
        class Employee:
            name = "Amara Az Zahra"
            age = "19"
        #instance of the class
        emp = Employee()
        #accessing class attributes
        print("Name of the Employee:", emp.name)
        print("Age of the Employee:", emp.age)
        *Hasil*
        Name of the Employee: Amara Az Zahra
        Age of the Employee: 19

    # Atribut kelas penting karena alasan berikut:
    * Mereka digunakan untuk mendefinisikan properti kelas yang harus memiliki nilai yang sama untuk setiap objek kelas tersebut.
    * Atribut kelas dapat digunakan untuk mengatur nilai default untuk objek.
    * Ini juga berguna dalam membuat singleton. Mereka adalah objek yang dibuat hanya sekali dan digunakan di berbagai bagian kode.

6. **Python-Methods**
    Metode adalah fungsi yang terkait dengan objek dan digunakan untuk melakukan tindakan atau operasi pada objek. Metode juga didefinisikan di dalam kelas.
    Objek juga dapat berisi metode. Metode dalam objek adalah fungsi yang milik objek.
    Contoh
    Masukkan fungsi yang mencetak salam, dan jalankan pada objek p1:
   
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def myfunc(self):
                print("Hello my name is " + self.name)
        p1 = Person("Rara", 19)
        p1.myfunc()
        Output: "Hello my name is Rara"
    *Nota: Parameter adalah referensi ke instance kelas saat ini, dan digunakan untuk mengakses variabel yang termasuk dalam kelas.* **self**

8. **Python-Constructors**
    Konstruktor Python adalah metode instance dalam kelas, yang secara otomatis dipanggil setiap kali objek baru dari kelas dibuat. Peran konstruktor adalah untuk menetapkan nilai ke variabel instance segera setelah objek dideklarasikan.

    Python menggunakan metode khusus yang disebut __init__() untuk menginisialisasi variabel instance untuk objek, segera setelah dideklarasikan.

    # Membuat konstruktor di Python
    Metode __init__() bertindak sebagai konstruktor. Dibutuhkan argumen wajib bernama self, yang merupakan referensi ke objek.

        def __init__(self, parameters):
        #initialize instance variables

    Metode __init__() serta metode instance apa pun dalam kelas memiliki parameter wajib, self. Namun, Anda dapat memberikan nama apa pun untuk parameter pertama, tidak harus sendiri.

    # Jenis Konstruktor di Python
    Python memiliki dua jenis konstruktor 
    * Konstruktor Default
    * Konstruktor Parameter

    # Konstruktor Default di Python
    Konstruktor Python yang tidak menerima parameter apa pun selain self disebut sebagai konstruktor default.
    *Contoh*
    Definisikan konstruktor di kelas Employee untuk menginisialisasi nama dan usia sebagai variabel instance. Kemudian dapat mengakses atribut ini melalui objeknya.

        class Employee:
            'Common base class for all employees'
            def __init__(self):
                self.name = "Bhavana"
                self.age = 24
    
        e1 = Employee()
        print ("Name: {}".format(e1.name))
        print ("age: {}".format(e1.age))
        *Output*
        Name: Bhavana
        age: 24

    Untuk kelas Employee di atas, setiap objek yang kita deklarasikan akan memiliki nilai yang sama untuk variabel instance name dan age. Untuk mendeklarasikan objek dengan atribut yang bervariasi alih-alih default, tentukan argumen untuk metode __init__().

    # Konstruktor Parameter
    Jika konstruktor didefinisikan dengan beberapa parameter bersama dengan *self* disebut sebagai konstruktor berparameter.
    *Contoh*
    Dalam contoh ini, konstruktor __init__() memiliki dua argumen formal.Mendeklarasikan objek Employee dengan nilai yang berbeda
    
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
        *Output*
        Name: Bhavana
        age: 24
        Name: Bharat
        age: 25

    Anda juga dapat menetapkan nilai default ke argumen formal dalam konstruktor sehingga objek dapat dibuat instans dengan atau tanpa meneruskan parameter.
