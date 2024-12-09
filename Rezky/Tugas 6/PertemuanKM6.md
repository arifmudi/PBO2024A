Nama    : Muhammad Rezky Ramadhan
Nim     : 2355201013

===============================================================POLIMORFISME=============================================================

Penjelasan Polimorfisme
Polimorfisme dalam Pemrograman Berorientasi Objek adalah konsep di mana objek yang berbeda dapat merespons metode yang sama dengan cara yang berbeda. Istilah 
"polimorfisme" berasal dari bahasa Yunani yang berarti "banyak bentuk". Dalam konteks pemrograman, ini memungkinkan satu antarmuka untuk digunakan pada berbagai 
tipe data.


Kapan Polimorfisme Digunakan?
Polimorfisme digunakan dalam situasi berikut:
Ketika Ada Kebutuhan Akan Generalisasi: Misalnya, saat Anda ingin menulis kode yang dapat bekerja dengan berbagai tipe objek tanpa mengetahui jenisnya secara 
spesifik.
Untuk Mendukung Ekstensi Sistem: Polimorfisme mempermudah penambahan fitur baru tanpa mengubah kode yang sudah ada.
Meningkatkan Pemeliharaan Kode: Kode menjadi lebih modular, sehingga lebih mudah dikelola dan diperbarui.
Dalam Penggunaan Pola Desain: Beberapa pola desain seperti Factory Pattern dan Strategy Pattern sangat bergantung pada polimorfisme.


Manfaat Polimorfisme
Reusabilitas Kode: Kode yang sama dapat digunakan untuk berbagai tipe objek.
Modularitas: Mempermudah pembagian kode menjadi bagian-bagian yang terpisah.
Fleksibilitas: Dapat menangani berbagai objek yang memiliki metode dengan nama sama.
Ekstensibilitas: Kode dapat diperluas tanpa memodifikasi struktur yang sudah ada.


Contoh Kodingan
1. Polimorfisme dengan Pewarisan (Inheritance)
python
Salin kode
# Base class
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini!")

# Derived class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Fungsi yang menunjukkan polimorfisme
def animal_sound(animal):
    print(animal.speak())

# Menggunakan polimorfisme
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

2. Polimorfisme dengan Duck Typing
Dalam Python, polimorfisme tidak selalu membutuhkan pewarisan karena mendukung duck typing.

python
Salin kode
class Duck:
    def speak(self):
        return "Quack!"

class Human:
    def speak(self):
        return "Hello!"

# Fungsi yang memanfaatkan polimorfisme
def make_sound(entity):
    print(entity.speak())

duck = Duck()
human = Human()

make_sound(duck)   # Output: Quack!
make_sound(human)  # Output: Hello!

3. Polimorfisme dengan Overloading (Python Tidak Mendukung Secara Langsung)
Namun, Python dapat mensimulasikan overloading dengan argumen default atau variable-length arguments.

python
Salin kode
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))         # Output: 3
print(calc.add(1, 2, 3, 4))  # Output: 10

4. Polimorfisme dengan Method Overriding
python
Salin kode
class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child(Parent):
    def greet(self):
        return "Hello from Child!"

# Menggunakan objek
parent = Parent()
child = Child()

print(parent.greet())  # Output: Hello from Parent!
print(child.greet())   # Output: Hello from Child!


Kesimpulan
Polimorfisme adalah konsep kunci dalam Pemrograman Berorientasi Objek yang memungkinkan fleksibilitas, efisiensi, dan kemudahan dalam pengelolaan 
kode. Dengan memahami polimorfisme, Anda dapat menulis kode yang lebih bersih, terstruktur, dan dapat diperluas di masa depan.