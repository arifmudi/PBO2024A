# Konsep Pewarisan (Inheritance) dalam Python

## 1. Konsep Pewarisan Tunggal (Single Inheritance)

Single inheritance adalah konsep dimana sebuah class hanya mewarisi dari satu class parent saja. Ini adalah bentuk pewarisan yang paling sederhana dan umum digunakan.

### Implementasi Single Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Penggunaan
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!
```

### Kapan Menggunakan Single Inheritance
- Ketika ingin membuat hierarki class yang sederhana
- Ketika class turunan merupakan versi yang lebih spesifik dari class parent
- Ketika ingin menghindari kompleksitas dari multiple inheritance

## 2. Konsep Super()

`super()` adalah method khusus yang digunakan untuk memanggil method dari class parent.

### Manfaat Super()
1. Menghindari penggunaan nama class parent secara eksplisit
2. Mendukung multiple inheritance dengan benar
3. Memudahkan maintenance code

### Implementasi Super()
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Memanggil konstruktor parent
        self.breed = breed

# Penggunaan
dog = Dog("Buddy", "Golden Retriever")
```

### Kapan Menggunakan Super()
- Saat ingin mengakses method parent class
- Ketika melakukan override method tapi tetap ingin menjalankan fungsi parent
- Dalam konstruktor untuk menginisialisasi atribut parent class

## 3. Jenis-jenis Inheritance

| Jenis Inheritance | Deskripsi | Contoh Use Case | 
|-------------------|-----------|-----------------|
| Single Inheritance | Satu class mewarisi dari satu parent class | Vehicle -> Car |
| Multiple Inheritance | Satu class mewarisi dari beberapa parent class | Smartphone (Phone, Computer) |
| Multi-level Inheritance | Class mewarisi dari class yang juga mewarisi class lain | Animal -> Mammal -> Dog |
| Hierarchical Inheritance | Beberapa class mewarisi dari satu parent class | Animal -> (Dog, Cat, Bird) |
| Hybrid Inheritance | Kombinasi dari beberapa jenis inheritance | Complex class hierarchies |

### Contoh Multiple Inheritance
```python
class Phone:
    def call(self):
        return "Calling..."

class Computer:
    def compute(self):
        return "Computing..."

class Smartphone(Phone, Computer):
    def take_photo(self):
        return "Taking photo..."
```

### Contoh Multi-level Inheritance
```python
class Animal:
    def speak(self):
        pass

class Mammal(Animal):
    def feed_young(self):
        return "Feeding with milk"

class Dog(Mammal):
    def speak(self):
        return "Woof!"
```

### Contoh Hierarchical Inheritance
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

## 4. Override Method

Override method adalah teknik menulis ulang method yang sudah ada di class parent di class child.

### Manfaat Override
1. Menyesuaikan perilaku method sesuai kebutuhan class child
2. Memberikan implementasi yang lebih spesifik
3. Memungkinkan polymorphism

### Implementasi Override
```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):  # Override method
        return "Woof!"

class Cat(Animal):
    def make_sound(self):  # Override method
        return "Meow!"
```

### Kapan Menggunakan Override
- Ketika implementasi parent class tidak sesuai dengan kebutuhan child class
- Saat ingin menambahkan fungsionalitas baru sambil mempertahankan interface yang sama
- Untuk implementasi polymorphism

## 5. Kapan Menggunakan Pewarisan

Pewarisan sebaiknya digunakan ketika:
1. Ada hubungan "is-a" yang jelas (Dog is-a Animal)
2. Ingin membagi code yang sama di antara beberapa class
3. Membutuhkan polymorphism
4. Ada hierarki class yang jelas
5. Class child merupakan versi yang lebih spesifik dari class parent

## 6. Kapan Menggunakan Komposisi (Non-Pewarisan)

Komposisi lebih tepat digunakan ketika:
1. Ada hubungan "has-a" (Car has-a Engine)
2. Tidak ada hierarki yang jelas antar class
3. Ingin menghindari coupling yang kuat
4. Membutuhkan fleksibilitas dalam mengubah implementasi
5. Perlu menggunakan berbagai fungsi dari class lain tanpa mewarisi seluruh propertinya

### Contoh Komposisi
```python
class Engine:
    def start(self):
        return "Engine starting..."

class Car:
    def __init__(self):
        self.engine = Engine()  # Komposisi
    
    def start_car(self):
        return self.engine.start()
```
