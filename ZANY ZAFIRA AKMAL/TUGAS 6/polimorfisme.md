**1.Apa itu Polimorfisme di Python?**
    Istilah polimorfisme mengacu pada fungsi atau metode yang mengambil bentuk yang berbeda dalam konteks yang berbeda. Karena Python adalah bahasa yang diketik secara dinamis, polimorfisme di Python sangat mudah diimplementasikan.

    Jika metode di kelas induk diganti dengan logika bisnis yang berbeda di kelas anaknya yang berbeda, metode kelas dasar adalah metode polimorfik.

**2.Cara menerapkan Polimorfisme di Python**
    Ada empat cara untuk mengimplementasikan polimorfisme di Python 

    1.Pengetikan Bebek
    2.Metode Penggantian
    3.Kelebihan Beban Operator
    4.Metode Overloading

    1.Mengetik Bebek di Python
        Pengetikan bebek adalah konsep di mana jenis atau kelas suatu objek kurang penting daripada metode yang ditentukannya. Dengan menggunakan konsep ini, Anda dapat memanggil metode apa pun pada objek tanpa memeriksa jenisnya, selama metode tersebut ada.

        Istilah ini didefinisikan oleh kutipan yang sangat terkenal yang menyatakan: Misalkan ada seekor burung yang berjalan seperti bebek, berenang seperti bebek, terlihat seperti bebek, dan berdetak seperti bebek maka itu mungkin bebek.

        Contoh
        Dalam kode yang diberikan di bawah ini, kami secara praktis mendemonstrasikan konsep pengetikan bebek.

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

            Ketika Anda menjalankan kode ini, itu akan menghasilkan output berikut:
            Quack, quack!
            I'm similar to a duck!

    2.Metode Mengganti di Python
        Dalam penggantian metode, metode yang didefinisikan di dalam subkelas memiliki nama yang sama dengan metode di superkelasnya tetapi mengimplementasikan fungsionalitas yang berbeda.

        Contoh
        ebagai contoh polimorfisme yang diberikan di bawah ini, kita memiliki bentuk yang merupakan kelas abstrak. Ini digunakan sebagai induk oleh dua kelas lingkaran dan persegi panjang. Kedua kelas mengganti metode draw() induk dengan cara yang berbeda.

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

            Ketika Anda menjalankan kode di atas, itu akan menghasilkan output berikut:
            Draw a circle
            Draw a rectangle 

            Variabel shp pertama-tama mengacu pada objek lingkaran dan memanggil metode draw() dari kelas lingkaran. Dalam iterasi berikutnya, ini mengacu pada objek persegi panjang dan memanggil metode draw() dari kelas persegi panjang. Oleh karena itu metode draw() dalam kelas shape adalah polimorfik.

    3.Operator Kelebihan Beban di Python
        Misalkan Anda telah membuat kelas Vector untuk mewakili vektor dua dimensi, apa yang terjadi ketika Anda menggunakan operator plus untuk menambahkannya? Kemungkinan besar Python akan berteriak pada Anda.

        Namun, Anda dapat mendefinisikan metode __add__ di kelas Anda untuk melakukan penambahan vektor dan kemudian operator plus akan berperilaku sesuai ekspektasi −

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

            Ketika kode di atas dieksekusi, itu menghasilkan hasil berikut:
            Vector(7,8)

    4.Metode Overloading di Python**
        Ketika kelas berisi dua atau lebih metode dengan nama yang sama tetapi jumlah parameter yang berbeda, maka skenario ini dapat disebut sebagai kelebihan metode.

        Python tidak mengizinkan kelebihan metode secara default, namun, kita dapat menggunakan teknik seperti daftar argumen panjang variabel, beberapa pengiriman dan parameter default untuk mencapai ini.

        Contoh
        Dalam contoh berikut, kita menggunakan daftar argumen panjang variabel untuk mencapai kelebihan metode.

            def add(*nums):
            return sum(nums)

            # Call the function with different number of parameters
            result1 = add(10, 25)
            result2 = add(10, 25, 35)

            print(result1)  
            print(result2) 

            Ketika kode di atas dieksekusi, itu menghasilkan hasil berikut:
            35
            70