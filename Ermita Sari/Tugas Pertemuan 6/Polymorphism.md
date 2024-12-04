#polymorphism
Istilah polimorfisme mengacu pada fungsi atau metode yang mengambil bentuk berbeda dalam konteks berbeda. Karena Python adalah bahasa bertipe dinamis, polimorfisme dalam Python sangat mudah diimplementasikan.

Jika suatu metode pada kelas induk ditimpa dengan logika bisnis yang berbeda pada berbagai kelas anaknya, metode kelas dasar adalah metode polimorfik.

#cara menerapkan Polimorfisme dalam Python

1. Duck typing
     adalah konsep yang menganggap tipe atau kelas suatu objek kurang penting dibandingkan metode yang didefinisikannya. Dengan konsep ini, Anda dapat memanggil metode apa pun pada suatu objek tanpa memeriksa tipenya, selama metode tersebut ada.

     contoh:
    class Duck:
        def sound(self):
            return "Quack, quack!"

    class AnotherBird:
        def sound(self):
            return "I'm similar to a duck!"

    def makeSound(duck):
        print(duck.sound())

    #creating instances
    duck = Duck()
    anotherBird = AnotherBird()
    #calling methods
    makeSound(duck)   
    makeSound(anotherBird)

2. Mengganti Metode dalam Python
    Dalam penggantian metode , metode yang didefinisikan di dalam subkelas memiliki nama yang sama dengan metode di superkelasnya tetapi mengimplementasikan fungsionalitas yang berbeda.

    contoh:
    from abc import ABC, abstractmethod
    class shape(ABC):
        @abstractmethod
        def draw(self):
            "Abstract method"
            return

    class circle(shape):
        def draw(self):
            super().draw()
            print ("Draw a circle")
        return

    class rectangle(shape):
        def draw(self):
        super().draw()
        print ("Draw a rectangle")
        return

    shapes = [circle(), rectangle()]
    for shp in shapes:
        shp.draw()

3. Operator Overloading di Python

    Misalkan Anda telah membuat kelas Vector untuk merepresentasikan vektor dua dimensi, apa yang terjadi ketika Anda menggunakan operator plus untuk menambahkannya? Kemungkinan besar Python akan membentak Anda.

    Namun, Anda bisa mendefinisikan metode __add__ di kelas Anda untuk melakukan penjumlahan vektor dan kemudian operator plus akan berperilaku sesuai harapan 

    contoh:

        class Vector:
            def __init__(self, a, b):
                self.a = a
                self.b = b

            def __str__(self):
                return 'Vector (%d, %d)' % (self.a, self.b)
   
            def __add__(self,other):
                return Vector(self.a + other.a, self.b + other.b)

        v1 = Vector(2,10)
        v2 = Vector(5,-2)
        print (v1 + v2)

4. Metode Overloading di Python

    Ketika suatu kelas memuat dua atau lebih metode dengan nama sama tetapi jumlah parameter berbeda maka skenario ini dapat disebut sebagai kelebihan beban metode.

    Python tidak mengizinkan kelebihan muatan metode secara default, namun, kita dapat menggunakan teknik seperti daftar argumen dengan panjang variabel, beberapa dispatch dan parameter default untuk mencapainya.

    contoh:
        def add(*nums):
            return sum(nums)

        #Call the function with different number of parameters
        result1 = add(10, 25)
        result2 = add(10, 25, 35)

        print(result1)  
        print(result2)    

5. Mengganti Metode dalam Python
   Penggantian metode Python mengacu pada pendefinisian metode dalam subkelas dengan nama yang sama dengan metode dalam superkelasnya. Dalam hal ini, interpreter Python menentukan metode mana yang akan dipanggil saat runtime berdasarkan objek aktual yang dirujuk.

   contoh:

    #define parent class
    class Parent: 
        def myMethod(self):
            print ('Calling parent method')

    #define child class
    class Child(Parent): 
        def myMethod(self):
            print ('Calling child method')

    #instance of child
    c = Child() 
    #child calls overridden method
    c.myMethod() 

#Metode Dasar yang Dapat Diabaikan

Dalam Python, kelas induk object menyediakan beberapa metode generik yang dapat diabaikan atau diganti sesuai kebutuhan dalam kelas pengguna. Metode pertama adalah __init__(self, [args...]), yang berfungsi sebagai konstruktor untuk menginisialisasi objek dengan argumen opsional dan dipanggil otomatis saat objek dibuat. Sebagai contoh, dalam kelas MyClass, Anda dapat menggunakan __init__ untuk mengatur atribut seperti name. Selain itu, terdapat metode __del__(self), yaitu destruktor yang digunakan untuk membersihkan atau menghapus objek. Metode ini dipanggil ketika sebuah objek dihapus, misalnya menggunakan perintah del.

Selanjutnya, metode __repr__(self) digunakan untuk memberikan representasi string dari objek yang dapat dievaluasi dengan eval(). Representasi ini sering digunakan untuk debugging. Sebagai perbandingan, metode __str__(self) memberikan representasi string yang lebih ramah pengguna dan biasanya digunakan ketika objek dicetak. Kedua metode ini memungkinkan pengguna untuk menentukan bagaimana objek mereka direpresentasikan dalam berbagai konteks, baik untuk tujuan debugging maupun penggunaan umum. Mengganti metode ini memberikan fleksibilitas dalam mengontrol perilaku dan tampilan objek di Python.
    
