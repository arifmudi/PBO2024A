Polimorfisme adalah konsep dalam pemrograman berorientasi objek (Object-Oriented Programming, OOP) yang memungkinkan objek dari kelas berbeda merespons secara berbeda terhadap metode yang sama. Polimorfisme berasal dari bahasa Yunani, "poly" berarti banyak, dan "morph" berarti bentuk. Artinya, satu antarmuka dapat memiliki banyak bentuk atau implementasi.

Jenis Polimorfisme
Polimorfisme pada waktu kompilasi (Compile-time Polymorphism): Disebut juga method overloading. Terjadi ketika ada beberapa metode dengan nama yang sama, tetapi berbeda parameter (tipe, jumlah, atau urutan parameter) dalam satu kelas.

Polimorfisme pada waktu eksekusi (Run-time Polymorphism): Disebut juga method overriding. Terjadi ketika sebuah kelas turunan (subclass) menyediakan implementasi spesifik untuk metode yang sudah didefinisikan dalam kelas induk (superclass).

Manfaat Polimorfisme
Meningkatkan fleksibilitas kode: Polimorfisme memungkinkan penggunaan metode dengan nama yang sama di berbagai kelas, sehingga mempermudah pengelolaan kode.
Mendukung abstraksi: Programmer dapat memanggil metode tanpa harus mengetahui implementasi detailnya.
Mendukung pemeliharaan kode: Dengan memisahkan logika ke berbagai kelas, kode lebih modular dan mudah diperbarui.

contoh :


# Superclass
class Animal:
    def make_sound(self):
        print("This animal makes a sound")

# Subclass 1
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

# Subclass 2
class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

# Main code
def main():
    # Polimorfisme: satu referensi untuk berbagai objek
    animals = [Dog(), Cat()]

    for animal in animals:
        animal.make_sound()  # Memanggil metode yang sesuai dengan objek

main()
