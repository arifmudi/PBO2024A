# Konsep Pewarisan dalam Python

## 1. Konsep Pewarisan Tunggal (Single Inheritance)

Single inheritance adalah konsep dimana sebuah class hanya mewarisi dari satu class parent saja. Ini adalah bentuk pewarisan yang paling sederhana dan umum digunakan.

### Implementasi:
```python
class car:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class toyota(car):
    def speak(self):
        return f"{self.name} Hand Brake!"

# Penggunaan
toyota = toyota("Buddy")
print(toyota.speak()) 
```

### Kapan Menggunakan:
- Ketika ingin membuat hierarki class yang sederhana
- Ketika class turunan merupakan bentuk spesifik dari class parent
- Ketika ingin menghindari kompleksitas dari multiple inheritance

## 2. Konsep Super()

`super()` adalah method khusus yang memungkinkan kita untuk memanggil method dari class parent.

### Manfaat:
1. Menghindari duplikasi kode
2. Memungkinkan penggunaan method parent dan child secara bersamaan
3. Menjaga fleksibilitas kode ketika terjadi perubahan pada class parent

### Implementasi:
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)  # Memanggil konstruktor parent
        self.year = year

# Penggunaan
my_car = Car("Toyota", "Camry", 2022)
print(f"{my_car.brand} {my_car.model} {my_car.year}")
```

### Kapan Menggunakan:
- Ketika ingin mengakses method parent yang telah di-override
- Saat ingin menambahkan fungsionalitas baru sambil mempertahankan fungsionalitas parent
- Dalam konstruktor untuk menginisialisasi atribut parent

## 3. Jenis-jenis Inheritance

### Tabel Perbandingan

| Jenis Inheritance | Karakteristik | Penggunaan | Kompleksitas |
|-------------------|---------------|------------|--------------|
| Single | Satu parent -> satu child | Hierarki sederhana | Rendah |
| Multiple | Banyak parent -> satu child | Kombinasi fitur | Tinggi |
| Multilevel | Parent -> child -> grandchild | Hierarki berlapis | Sedang |
| Hierarchical | Satu parent -> banyak child | Klasifikasi umum | Sedang |
| Hybrid | Kombinasi berbagai jenis | Kasus kompleks | Sangat Tinggi |

### Contoh Implementasi:

#### Multiple Inheritance
```python
class Flying:
    def fly(self):
        return "I can fly"

class Swimming:
    def swim(self):
        return "I can swim"

class Duck(Flying, Swimming):
    pass

# Penggunaan
duck = Duck()
print(duck.fly())   # Output: I can fly
print(duck.swim())  # Output: I can swim
```

#### Multilevel Inheritance
```python
class Grandparent:
    def speak(self):
        return "Grandparent speaking"

class Parent(Grandparent):
    def walk(self):
        return "Parent walking"

class Child(Parent):
    def run(self):
        return "Child running"
```

#### Hierarchical Inheritance
```python
class car:
    def speak(self):
        pass

class toyota(car):
    def speak(self):
        return "Woof!"

class Cat(car):
    def speak(self):
        return "Meow!"
```

## 4. Override Method

Override method adalah konsep menulis ulang method yang sudah ada di class parent di class child.

### Manfaat:
1. Customisasi perilaku untuk class spesifik
2. Implementasi polimorfisme
3. Fleksibilitas dalam pengembangan

### Implementasi:
```python
class car:
    def make_sound(self):
        return "Some sound"

class toyota(car):
    def make_sound(self):  # Override method
        return "Woof!"

class Cat(car):
    def make_sound(self):  # Override method
        return "Meow!"

# Penggunaan
toyota = toyota()
cat = Cat()
print(toyota.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
```

## 5. Kapan Menggunakan Pewarisan

Pewarisan sebaiknya digunakan ketika:
1. Ada hubungan "is-a" yang jelas (Kucing adalah Hewan)
2. Ingin membagi kode yang umum di antara beberapa class
3. Ingin membuat hierarki class yang terstruktur
4. Ada kebutuhan untuk polimorfisme

## 6. Kapan Menggunakan Komposisi (Non-Pewarisan)

Komposisi lebih tepat digunakan ketika:
1. Ada hubungan "has-a" (Mobil memiliki Mesin)
2. Ingin lebih fleksibel dalam mengganti komponen
3. Menghindari hierarki yang terlalu dalam
4. Ingin mengurangi coupling antar class

### Contoh Komposisi:
```python
class Engine:
    def start(self):
        return "Engine starting"

class Car:
    def __init__(self):
        self.engine = Engine()  # Komposisi
    
    def start_car(self):
        return self.engine.start()

# Penggunaan
car = Car()
print(car.start_car())  # Output: Engine starting
```

Dalam praktik nyata, pilihan antara pewarisan dan komposisi harus didasarkan pada kebutuhan spesifik project dan prinsip design yang ingin diterapkan. Ingat prinsip "Composition over Inheritance" yang sering dianjurkan dalam pemrograman berorientasi objek modern.