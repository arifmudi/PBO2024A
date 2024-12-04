**Pengertian Polimorfisme dalam Python**
Polimorfisme adalah konsep penting dalam pemrograman berorientasi objek (OOP) yang memungkinkan objek dari berbagai kelas untuk merespons metode yang sama dengan cara yang berbeda. Dalam konteks Python, polimorfisme memungkinkan fleksibilitas dalam penggunaan kode dan mempermudah pengembangan serta pemeliharaan perangkat lunak. Konsep ini berasal dari kata Yunani "poly" yang berarti banyak dan "morph" yang berarti bentuk, sehingga secara harfiah berarti "banyak bentuk".
Istilah polimorfisme mengacu pada fungsi atau metode yang mengambil bentuk yang berbeda dalam konteks yang berbeda. Karena Python adalah bahasa yang diketik secara dinamis, polimorfisme di Python sangat mudah diimplementasikan. Jika metode di kelas induk diganti dengan logika bisnis yang berbeda di kelas anaknya yang berbeda, metode kelas dasar adalah metode polimorfik.

**Tipe-Tipe Polimorfisme**
Polimorfisme dalam Python dapat dibagi menjadi dua tipe utama:
Polimorfisme Statis (Compile-Time Polymorphism):
Juga dikenal sebagai overloading, di mana beberapa metode dalam satu kelas dapat memiliki nama yang sama tetapi dengan parameter yang berbeda. Namun, Python tidak mendukung overload method secara eksplisit seperti bahasa lain seperti C++ 23.
Polimorfisme Dinamis (Runtime Polymorphism):
Dikenal sebagai overriding, di mana subclass menyediakan implementasi baru untuk metode yang ada di superclass. Ini memungkinkan metode yang sama dipanggil pada objek dari kelas yang berbeda, dan hasilnya bergantung pada jenis objek yang sebenarnya saat runtime.

**Implementasi Polimorfisme dalam Python**
Ada empat cara untuk mengimplementasikan polimorfisme di Python:
1. Duck Typing
    adalah konsep di mana jenis atau kelas suatu objek kurang penting daripada metode yang ditentukannya. Dengan menggunakan konsep ini, Anda dapat memanggil metode apa pun pada objek tanpa memeriksa jenisnya, selama metode tersebut ada.
    *example*
    
        class Duck:
            def sound(self):
                return "Quack, quack!"

        class AnotherBird:
            def sound(self):
                return "I'm similar to a duck!"

        def makeSound(duck):
            print(duck.sound())

        # creating instances
        duck = Duck()
        anotherBird = AnotherBird()
        # calling methods
        makeSound(duck)   
        makeSound(anotherBird)

2. Operator Overloading
    Misalkan Anda telah membuat kelas Vector untuk mewakili vektor dua dimensi, apa yang terjadi ketika Anda menggunakan operator plus untuk menambahkannya? Kemungkinan besar Python akan berteriak pada Anda.
    Namun, Anda dapat mendefinisikan metode __add__ di kelas Anda untuk melakukan penambahan vektor dan kemudian operator plus akan berperilaku sesuai ekspektasi −
    *example*

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

3. Method Overriding
    Dalam penggantian metode, metode yang didefinisikan di dalam subkelas memiliki nama yang sama dengan metode di superkelasnya tetapi mengimplementasikan fungsionalitas yang berbeda.
    *example*

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

    Variabel shp pertama-tama mengacu pada objek lingkaran dan memanggil metode draw() dari kelas lingkaran. Dalam iterasi berikutnya, ini mengacu pada objek persegi panjang dan memanggil metode draw() dari kelas persegi panjang. Oleh karena itu metode draw() dalam kelas shape adalah polimorfik.

4. Method Overloading
    Ketika kelas berisi dua atau lebih metode dengan nama yang sama tetapi jumlah parameter yang berbeda, maka skenario ini dapat disebut sebagai kelebihan metode.
    Python tidak mengizinkan kelebihan metode secara default, namun, kita dapat menggunakan teknik seperti daftar argumen panjang variabel, beberapa pengiriman dan parameter default untuk mencapai ini.
    *example*

        def add(*nums):
            return sum(nums)

        # Call the function with different number of parameters
        result1 = add(10, 25)
        result2 = add(10, 25, 35)

        print(result1)  
        print(result2)  

Dalam Python, polimorfisme sering kali diimplementasikan melalui metode dengan nama yang sama di kelas-kelas yang berbeda. Berikut adalah contoh implementasi polimorfisme:

        class Animal:
            def sound(self):
                pass

        class Dog(Animal):
            def sound(self):
                return "Woof!"

        class Cat(Animal):
            def sound(self):
                return "Meow!"

        def make_sound(animal):
            return animal.sound()

        # Membuat objek dari kelas yang berbeda
        dog = Dog()
        cat = Cat()

        # Memanggil metode yang sama pada objek-objek yang berbeda
        print(make_sound(dog))  # Output: Woof!
        print(make_sound(cat))  # Output: Meow!

Dalam contoh di atas, kelas Animal memiliki metode sound() yang tidak terimplementasi. Kelas Dog dan Cat mengoverride metode ini dengan implementasi mereka sendiri. Fungsi make_sound() dapat memanggil metode sound() pada objek dari kelas-kelas tersebut, dan hasilnya akan sesuai dengan jenis objek yang dipanggil.

**Class Polymorphism**
    Polimorfisme sering digunakan dalam metode Class, di mana kita dapat memiliki beberapa dengan nama metode yang sama.
    Misalnya, katakanlah kita memiliki tiga kelas: , , dan , dan semuanya memiliki metode yang disebut :CarBoatPlanemove()
    *example*

        class Car:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def move(self):
                print("Drive!")

        class Boat:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def move(self):
                print("Sail!")

        class Plane:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def move(self):
                print("Fly!")

        car1 = Car("Ford", "Mustang")       #Create a Car class
        boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
        plane1 = Plane("Boeing", "747")     #Create a Plane class

        for x in (car1, boat1, plane1):
            x.move()

**Inheritance Class Polymorphism**
    *example*

        class Vehicle:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def move(self):
                print("Move!")

        class Car(Vehicle):
            pass

        class Boat(Vehicle):
            def move(self):
                print("Sail!")

        class Plane(Vehicle):
            def move(self):
                print("Fly!")

        car1 = Car("Ford", "Mustang") #Create a Car object
        boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
        plane1 = Plane("Boeing", "747") #Create a Plane object

        for x in (car1, boat1, plane1):
            print(x.brand)
            print(x.model)
            x.move()

Kelas anak mewarisi properti dan metode dari kelas induk.
Pada contoh di atas Anda dapat melihat bahwa class kosong, tetapi itu mewarisi , , dan dari .Carbrand modelmove()Vehicle. Kelas dan juga mewarisi dan dari , tetapi keduanya mengesampingkan metode.BoatPlanebrandmodelmove()Vehiclemove(). Karena polimorfisme kita dapat mengeksekusi metode yang sama untuk semua kelas.

**Keuntungan Menggunakan Polimorfisme**
    Menggunakan polimorfisme dalam pengembangan perangkat lunak memiliki beberapa keuntungan:
    *Fleksibilitas*: Kode menjadi lebih fleksibel karena Anda dapat menggunakan metode yang sama pada berbagai objek tanpa perlu mengetahui detail implementasinya.
    *Interoperabilitas*: Berbagai objek dapat berinteraksi dengan kode yang sama, meningkatkan interoperabilitas.
    *Pengurangan Duplikasi Kode*: Polimorfisme membantu mengurangi duplikasi kode dengan memungkinkan penggunaan kembali kode dasar dalam kelas-kelas turunan 24.
    Dengan memahami dan menerapkan polimorfisme, pengembang dapat menulis kode yang lebih bersih, efisien, dan mudah dikelola.