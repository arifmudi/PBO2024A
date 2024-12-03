# Konsep Pewarisan dalam Game Development

## 1. Konsep Pewarisan Tunggal (Single Inheritance)

Single inheritance adalah konsep dimana sebuah class hanya mewarisi dari satu class parent. Dalam konteks game, ini sangat berguna untuk membuat berbagai jenis karakter atau item.

### Implementasi:
```python
class GameCharacter:
    def __init__(self, name, health, speed):
        self.name = name
        self.health = health
        self.speed = speed
        
    def move(self):
        return f"{self.name} bergerak dengan kecepatan {self.speed}"

class Warrior(GameCharacter):
    def __init__(self, name, health, speed, armor):
        self.armor = armor
        super().__init__(name, health, speed)
    
    def attack(self):
        return f"{self.name} menyerang dengan pedang!"

# Penggunaan
hero = Warrior("Hercules", 100, 5, 50)
print(hero.move())      # Output: Hercules bergerak dengan kecepatan 5
print(hero.attack())    # Output: Hercules menyerang dengan pedang!
```

### Kapan Menggunakan:
- Saat membuat variasi dari objek dasar (mis: Warrior, Archer, Mage dari GameCharacter)
- Ketika ingin menurunkan sifat-sifat umum ke class yang lebih spesifik
- Saat struktur pewarisan sederhana dan linier

## 2. Konsep Super()

Super() adalah method yang memungkinkan class anak mengakses method dan properti dari class induk.

### Manfaat:
1. Menghindari duplikasi kode
2. Mempertahankan fungsionalitas parent sambil menambah fitur baru
3. Memudahkan maintenance code

### Implementasi:
```python
class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

class MagicWeapon(Weapon):
    def __init__(self, name, damage, durability, mana_cost):
        super().__init__(name, damage, durability)  # Memanggil konstruktor parent
        self.mana_cost = mana_cost
        
    def get_stats(self):
        base_stats = super().get_stats()  # Memanggil method parent
        return f"{base_stats}, Mana Cost: {self.mana_cost}"

# Penggunaan
magic_sword = MagicWeapon("Excalibur", 100, 1000, 50)
```

### Kapan Menggunakan:
- Saat ingin menggunakan konstruktor parent
- Ketika perlu memanggil method parent yang di-override
- Saat menambah fungsionalitas baru dengan tetap mempertahankan yang lama

## 3. Jenis-jenis Inheritance

### Tabel Perbandingan

| Jenis | Contoh Penggunaan | Kelebihan | Kekurangan | Kompleksitas |
|-------|------------------|------------|------------|--------------|
| Single | Character -> Warrior | Sederhana, mudah dipahami | Terbatas pada satu parent | Rendah |
| Multiple | Flying, Combat -> FlyingWarrior | Bisa mengkombinasi fitur | Potential konflik | Tinggi |
| Multilevel | Item -> Weapon -> Sword | Hierarki yang detail | Bisa terlalu dalam | Sedang |
| Hierarchical | Character -> (Warrior, Mage, Archer) | Organisasi yang baik | Duplikasi kode | Sedang |
| Hybrid | Kombinasi dari jenis lainnya | Sangat fleksibel | Sangat kompleks | Sangat Tinggi |

### Contoh Multiple Inheritance:
```python
class Flying:
    def fly(self):
        return "Terbang di udara"

class Combat:
    def attack(self):
        return "Menyerang musuh"

class FlyingWarrior(Flying, Combat):
    def aerial_attack(self):
        return f"{self.fly()} dan {self.attack()}"
```

### Contoh Multilevel:
```python
class Item:
    def __init__(self, name):
        self.name = name

class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

class Sword(Weapon):
    def __init__(self, name, damage, swing_speed):
        super().__init__(name, damage)
        self.swing_speed = swing_speed
```

## 4. Override Method

Override method adalah teknik menulis ulang method yang sudah ada di class parent.

### Implementasi:
```python
class Enemy:
    def attack(self):
        return "Serangan dasar"

class Boss(Enemy):
    def attack(self):  # Override method
        base_attack = super().attack()
        return f"{base_attack} + Serangan spesial!"

# Penggunaan
boss = Boss()
print(boss.attack())  # Output: Serangan dasar + Serangan spesial!
```

### Manfaat:
1. Kustomisasi perilaku untuk class spesifik
2. Menambah atau memodifikasi fungsi yang ada
3. Implementasi polimorfisme

## 5. Kapan Menggunakan Pewarisan

Pewarisan tepat digunakan ketika:
1. Ada hubungan "is-a" yang jelas
   - Warrior is a Character
   - Sword is a Weapon
2. Ingin membagi fitur umum antar class
   - Semua karakter punya health dan speed
   - Semua senjata punya damage
3. Perlu implementasi polimorfisme
   - Berbagai jenis karakter dengan attack() berbeda
4. Menghindari duplikasi kode
   - Fitur dasar di parent class

## 6. Kapan Menggunakan Komposisi

Komposisi lebih tepat ketika:
1. Ada hubungan "has-a"
   - Character has a Weapon
   - Game has an Inventory
2. Komponen bisa digunakan secara independen
3. Perlu fleksibilitas dalam mengganti komponen

### Contoh Komposisi:
```python
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Inventory:
    def __init__(self):
        self.items = []

class Character:
    def __init__(self, name):
        self.name = name
        self.weapon = None        # Komposisi
        self.inventory = Inventory()  # Komposisi
    
    def equip_weapon(self, weapon):
        self.weapon = weapon

# Penggunaan
sword = Weapon("Iron Sword", 10)
hero = Character("Hero")
hero.equip_weapon(sword)
```

### Kelebihan Komposisi:
1. Lebih fleksibel daripada inheritance
2. Mudah mengganti komponen
3. Menghindari hierarki yang kompleks
4. Pemisahan concern yang lebih baik

Dalam game development, keputusan antara inheritance dan komposisi sangat penting:
- Inheritance: untuk sistem yang memiliki hierarki jelas
- Komposisi: untuk sistem yang membutuhkan fleksibilitas tinggi

Contoh praktis:
- Inheritance: jenis-jenis karakter, senjata, skill
- Komposisi: inventory system, equipment system, party system