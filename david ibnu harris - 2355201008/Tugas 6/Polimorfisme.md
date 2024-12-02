## Polimorfisme
Polimorfisme adalah salah satu konsep dalam pemrograman berorientasi objek dimana suatu objek dapat memiliki banyak bentuk

## Jenis-Jenis Polimorfisme
1. **Overriding**: Menulis ulang method yang sudah ada di class parent di class child dengan implementasi yang berbeda
   
2. **Overloading**: Membuat method dengan nama yang sama tapi parameter berbeda dalam satu class

## Implementasi Polimorfisme

```python
class Item:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat
        self.durability = 100

    def gunakan(self):
        pass

    def perbaiki(self):
        self.durability = 100
        print(f"{self.nama} sudah diperbaiki. Durability: {self.durability}")

    def hitung_total(self):
        return self.berat

class Weapon(Item):
    def __init__(self, nama, berat, dmg, type_dmg):
        super().__init__(nama, berat)
        self.dmg = dmg
        self.type_dmg = type_dmg
        self.lvl = 0

    def gunakan(self):
        if self.durability <= 0:
            return f"{self.nama} rusak!"
        self.durability -= 10
        return f"Attack dengan {self.nama}! DMG: {self.dmg + (self.lvl * 5)}"

    def upgrade(self):
        if self.lvl < 10:
            self.lvl += 1
            self.dmg += 5
            return f"{self.nama} di upgrade ke +{self.lvl}! DMG: {self.dmg}"
        return f"{self.nama} udah max level!"

class Equip(Item):
    def __init__(self, nama, berat, defense, type_armor):
        super().__init__(nama, berat)
        self.defense = defense
        self.type_armor = type_armor
        self.bonus = False

    def gunakan(self):
        if self.durability <= 0:
            return f"{self.nama} rusak!"
        self.durability -= 5
        defense_total = self.defense * 1.5 if self.bonus else self.defense
        return f"Pake {self.nama}! DEF: {defense_total}"

    def aktif_bonus(self):
        self.bonus = True
        return f"Bonus {self.nama} aktif! DEF +50%"

class Potion(Item):
    def __init__(self, nama, berat, efek, time):
        super().__init__(nama, berat)
        self.efek = efek
        self.time = time
        self.jumlah = 1

    def gunakan(self):
        if self.jumlah <= 0:
            return f"Ga ada {self.nama}!"
        self.jumlah -= 1
        return f"Minum {self.nama}! Efek: {self.efek} selama {self.time} detik"

    def tambah(self, total):
        self.jumlah += total
        return f"Nambah {total} {self.nama}. Total: {self.jumlah}"

    def hitung_total(self):
        return self.berat * self.jumlah

class Tas:
    def __init__(self, max_berat):
        self.items = []
        self.max_berat = max_berat

    def tambah_item(self, item):
        total = sum(i.hitung_total() for i in self.items)
        if total + item.hitung_total() <= self.max_berat:
            self.items.append(item)
            return f"{item.nama} masuk tas"
        return f"Tas kelebihan berat buat {item.nama}"

    def pake_item(self):
        print("\nPake semua item:")
        for item in self.items:
            print(item.gunakan())

if __name__ == "__main__":
    sword = Weapon("Pedang Legend", 5, 100, "Fisik")
    armor = Equip("Baju Besi", 10, 50, "Heavy")
    hp_pot = Potion("Potion HP", 0.5, "HP +50", 30)

    tas_ku = Tas(50)

    print(tas_ku.tambah_item(sword))
    print(tas_ku.tambah_item(armor))
    print(tas_ku.tambah_item(hp_pot))

    print("\nUpgrade:")
    print(sword.upgrade())
    print(sword.upgrade())

    print("\nAktifin Bonus:")
    print(armor.aktif_bonus())

    print("\nTambah Potion:")
    print(hp_pot.tambah(3))

    tas_ku.pake_item()

    print("\nPerbaikin:")
    sword.durability = 0
    print(sword.gunakan())
    sword.perbaiki()
```


## Output 
```
Pedang Legend masuk tas
Baju Besi masuk tas
Potion HP masuk tas

Upgrade:
Pedang Legend di upgrade ke +1! DMG: 105
Pedang Legend di upgrade ke +2! DMG: 110

Aktifin Bonus:
Bonus Baju Besi aktif! DEF +50%

Tambah Potion:
Nambah 3 Potion HP. Total: 4

Pake semua item:
Attack dengan Pedang Legend! DMG: 110
Pake Baju Besi! DEF: 75.0
Minum Potion HP! Efek: HP +50 selama 30 detik

Perbaikin:
Pedang Legend rusak!
Pedang Legend sudah diperbaiki. Durability: 100
```
