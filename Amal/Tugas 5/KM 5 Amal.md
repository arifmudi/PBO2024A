1. *Konsep Pewarisan Tunggal (Single Inheritance)*
Pewarisan tunggal adalah konsep di mana sebuah kelas anak (child class) mewarisi atribut dan metode dari satu kelas induk (parent class). 

python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, my name is {self.name}."

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        return f"{self.name} is {self.age} years old."

# Contoh penggunaan
child = Child("Alice", 10)
print(child.greet())
print(child.display())

Gunakan ketika:  
- Relasi antar kelas bersifat sederhana (parent-child).  
- Anda ingin menambahkan atau memperluas fungsi dari kelas induk.  


2. *Konsep super untuk Konstruktor*

*Manfaat*
- Mempermudah akses ke metode atau konstruktor kelas induk.  
- Menghindari penulisan ulang kode.  
- Menjamin bahwa atribut/metode kelas induk dapat diinisialisasi dengan benar.  

 *Implementasi Python*
python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Memanggil konstruktor Parent
        self.age = age

child = Child("Bob", 15)
print(child.name, child.age)

*Kapan Menggunakan super*
- Saat Anda ingin menggabungkan perilaku kelas induk dan menambahkannya dengan fitur baru di kelas anak.

---
 3. *Jenis-Jenis Inheritance*

| *Jenis Inheritance* | *Definisi* | *Contoh Code* | *Kapan Digunakan* |
|------------------------|--------------|------------------|---------------------|
| *Single*            | Child mewarisi satu Parent | Lihat poin 1 | Struktur sederhana |
| *Multiple*          | Child mewarisi lebih dari satu Parent | Lihat di bawah | Menggabungkan sifat dari beberapa Parent |
| *Multilevel*        | Hierarki berlapis | Lihat di bawah | Membentuk rantai pewarisan |
| *Hierarchical*      | Beberapa Child dari satu Parent | Lihat di bawah | Banyak class berbagi properti dasar |
| *Hybrid*            | Gabungan berbagai jenis | Lihat di bawah | Sistem yang kompleks |

 Contoh Code
python
# Multiple Inheritance
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    pass

obj = C()
print(obj.method_a(), obj.method_b())

# Multilevel Inheritance
class Grandparent:
    def method_gp(self):
        return "Grandparent method"

class Parent(Grandparent):
    def method_p(self):
        return "Parent method"

class Child(Parent):
    pass

obj = Child()
print(obj.method_gp(), obj.method_p())

# Hierarchical Inheritance
class Parent:
    def common_method(self):
        return "Common to all"

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()
print(obj1.common_method(), obj2.common_method())

# Hybrid Inheritance
class Base:
    def base_method(self):
        return "Base method"

class A(Base):
    def method_a(self):
        return "Method A"

class B(Base):
    def method_b(self):
        return "Method B"

class C(A, B):
    pass

obj = C()
print(obj.base_method(), obj.method_a(), obj.method_b())


---
 4. *Override Method*

 *Manfaat*
- Memberikan perilaku khusus pada metode yang diwarisi.  
- Memodifikasi atau menyesuaikan perilaku sesuai kebutuhan kelas anak.  

 *Implementasi*
python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

obj = Child()
print(obj.greet())  # Menggunakan metode yang di-override


 *Kapan Digunakan*
Ketika perilaku default dari parent class tidak mencukupi untuk kelas anak.

---

 5. *Kapan Menggunakan Pewarisan*
- Ketika ada hubungan is-a antara kelas (e.g., Dog is a Animal).  
- Untuk mengurangi pengulangan kode.  
- Saat fitur harus diturunkan ke kelas lain.  

---

 6. *Kapan Menggunakan Non-Pewarisan (Komposisi)*

Gunakan komposisi ketika:
- Hubungan antar objek lebih ke has-a (e.g., Car has a Engine).  
- Anda ingin membuat kode lebih modular dan fleksibel.  

 Contoh Komposisi
python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Komposisi

    def start_car(self):
        return self.engine.start()

car = Car()
print(car.start_car())


 7. *Studi Kasus*

*Studi Kasus: Sistem Perpustakaan*
- *Kelas Parent:* Book (mewakili buku).  
- *Kelas Child:* DigitalBook dan PrintedBook.  

 Code
python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"'{self.title}' by {self.author}"

class DigitalBook(Book):
    def __init__(self, title, author, filesize):
        super().__init__(title, author)
        self.filesize = filesize

    def info(self):
        return super().info() + f" (File Size: {self.filesize} MB)"

class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def info(self):
        return super().info() + f" (Pages: {self.pages})"

# Contoh penggunaan
ebook = DigitalBook("Python Programming", "Author A", 5)
printbook = PrintedBook("Learn Python", "Author B", 300)

print(ebook.info())
print(printbook.info())