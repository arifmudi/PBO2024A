# Panduan Lengkap Inheritance (Pewarisan) dalam Python

## 1\. Konsep Pewarisan Tunggal \(Single Inheritance\)

### Pengertian

Single inheritance adalah konsep dimana sebuah class
(subclass/child class) hanya mewarisi sifat dan perilaku dari satu class induk (superclass/parent class). Ini merupakan bentuk pewarisan yang paling sederhana dan umum digunakan.

### Implementasi

``` python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Penggunaan
my_cat = Cat("Whiskers")
print(my_cat.speak())  # Output: Whiskers says Meow!
```

### Kapan Menggunakan Single Inheritance

* Ketika ingin membuat hierarki class yang sederhana dan mudah dipahami
* Saat ada hubungan "is-a" yang jelas (misalnya: Kucing adalah Hewan)
* Ketika ingin menghindari kompleksitas dari multiple inheritance
* Saat ingin meminimalkan ketergantungan antar class

## 2\. Konsep Super\(\) untuk Mewarisi di Konstruktor

### Pengertian dan Manfaat

* `super()` adalah fungsi built-in Python yang memungkinkan akses ke method dan property dari class induk
* Memungkinkan penggunaan kembali kode dari class induk
* Menghindari penulisan nama class induk secara eksplisit
* Mendukung Multiple Inheritance dengan benar

### Implementasi

``` python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class ElectricCar(Vehicle):
    def __init__(self, brand, year, battery_capacity):
        super().__init__(brand, year)  # Memanggil konstruktor parent
        self.battery_capacity = battery_capacity

# Penggunaan
tesla = ElectricCar("Tesla", 2023, "100kWh")
print(f"{tesla.brand} {tesla.year} with {tesla.battery_capacity} battery")
```

### Kapan dan Mengapa Menggunakan Super

* Saat ingin mengakses method dari class induk
* Ketika perlu menambahkan fungsionalitas baru sambil mempertahankan fungsionalitas dasar
* Untuk menghindari duplikasi kode
* Saat implementasi method di class anak memerlukan implementasi method class induk

## 3\. Jenis\-jenis Inheritance

### Tabel Perbandingan

| Jenis Inheritance | Karakteristik | Penggunaan | Kompleksitas | Contoh Use Case |
| ----------------- | ------------- | ---------- | ------------ | --------------- |
| Single | Satu parent class | Sederhana dan umum | Rendah | Animal → Cat |
| Multiple | Banyak parent class | Kompleks, butuh perhatian khusus | Tinggi | Car, ElectricDevice → ElectricCar |
| Multilevel | Rantai inheritance | Hierarki bertingkat | Sedang | Animal → Mammal → Cat |
| Hierarchical | Satu parent, banyak child | Struktur pohon | Sedang | Animal → (Cat, Dog, Bird) |
| Hybrid | Kombinasi berbagai jenis | Sangat kompleks | Sangat Tinggi | Mixin patterns |

### Contoh Implementasi

#### Multiple Inheritance

``` python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return "Driving..."

class ElectricDevice:
    def __init__(self, power):
        self.power = power

    def charge(self):
        return "Charging..."

class ElectricCar(Car, ElectricDevice):
    def __init__(self, brand, power):
        Car.__init__(self, brand)
        ElectricDevice.__init__(self, power)
```

#### Multilevel Inheritance

``` python
class Animal:
    def speak(self):
        pass

class Mammal(Animal):
    def feed_young(self):
        return "Feeding with milk"

class Cat(Mammal):
    def speak(self):
        return "Meow"
```

#### Hierarchical Inheritance

``` python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Bird(Animal):
    def speak(self):
        return "Tweet"
```

## 4\. Override Method

### Pengertian dan Manfaat

* Override method adalah kemampuan class anak untuk memberikan implementasi berbeda untuk method yang sudah didefinisikan di class induk
* Memungkinkan customisasi perilaku untuk class spesifik
* Mendukung polimorfisme

### Implementasi

``` python
class Shape:
    def area(self):
        return "Area calculation not implemented"

    def describe(self):
        return "This is a shape"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Override method area()
        return 3.14 * self.radius ** 2

    def describe(self):  # Override method describe()
        return f"This is a circle with radius {self.radius}"

# Penggunaan
circle = Circle(5)
print(circle.area())  # Output: 78.5
print(circle.describe())  # Output: This is a circle with radius 5
```

### Kapan Menggunakan Override

* Ketika implementasi method parent tidak sesuai untuk child class
* Saat ingin menambahkan fungsionalitas khusus untuk child class
* Untuk implementasi polimorfisme
* Ketika perlu customisasi perilaku untuk kasus spesifik

## 5\. Kapan Menggunakan Pewarisan

### Gunakan Pewarisan Ketika:

1. Ada hubungan "is-a" yang jelas
2. Ingin membagi kode yang umum di antara beberapa class
3. Ada hierarki class yang alami
4. Perlu implementasi polimorfisme
5. Class-class memiliki banyak perilaku yang sama

### Contoh Kasus Yang Tepat:

``` python
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Developer(Employee):
    def __init__(self, name, id, programming_languages):
        super().__init__(name, id)
        self.programming_languages = programming_languages

class Designer(Employee):
    def __init__(self, name, id, design_tools):
        super().__init__(name, id)
        self.design_tools = design_tools
```

## 6\. Kapan Menggunakan Komposisi \(Non\-Pewarisan\)

### Konsep Komposisi

Komposisi adalah pendekatan dimana object dibuat dari kombinasi object lain, bukan mewarisi sifat-sifatnya.

### Implementasi Inovatif: Smart Home System

``` python
class Device:
    def __init__(self, name, power_usage):
        self.name = name
        self.power_usage = power_usage
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on

class SmartController:
    def __init__(self):
        self.devices = {}
        self.schedules = {}

    def add_device(self, device_id, device):
        self.devices[device_id] = device

    def set_schedule(self, device_id, time, action):
        if device_id not in self.schedules:
            self.schedules[device_id] = []
        self.schedules[device_id].append((time, action))

class SmartHome:
    def __init__(self):
        self.controller = SmartController()
        self.power_monitor = PowerMonitor()
        self.security_system = SecuritySystem()

    def add_device(self, device_id, device):
        self.controller.add_device(device_id, device)
        self.power_monitor.register_device(device)

class PowerMonitor:
    def __init__(self):
        self.devices = []
        self.total_usage = 0

    def register_device(self, device):
        self.devices.append(device)

    def calculate_usage(self):
        return sum(d.power_usage for d in self.devices if d.is_on)

class SecuritySystem:
    def __init__(self):
        self.is_armed = False
        self.alerts = []

    def arm(self):
        self.is_armed = True

    def disarm(self):
        self.is_armed = False

# Penggunaan
smart_home = SmartHome()
living_room_light = Device("Living Room Light", 60)
smart_home.add_device("LR_LIGHT_1", living_room_light)
smart_home.controller.set_schedule("LR_LIGHT_1", "18:00", "ON")
```

### Kapan Menggunakan Komposisi:

1. Ketika hubungan antar object adalah "has-a" bukan "is-a"
2. Saat ingin fleksibilitas dalam mengganti komponen
3. Ketika perlu menghindari coupling yang kuat
4. Saat struktur object bisa berubah saat runtime
5. Ketika ingin menghindari hierarki pewarisan yang dalam

### Keuntungan Komposisi:

* Lebih fleksibel dibanding inheritance
* Mudah dimodifikasi saat runtime
* Mengurangi coupling antar class
* Memudahkan unit testing
* Lebih mudah dimaintain dalam jangka panjang