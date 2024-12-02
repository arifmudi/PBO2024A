1. Polymorfisme 

Polimorfisme adalah konsep dalam pemrograman berorientasi objek yang memungkinkan satu fungsi, metode, atau objek memiliki perilaku yang berbeda-beda tergantung pada bagaimana ia digunakan. Dalam Python, polimorfisme biasanya diterapkan melalui metode dengan nama yang sama tetapi didefinisikandalam kelas yang berbeda. Polimorfisme membantu membuat kode lebih fleksibel dan mudah dikembangkan.

```python
# Parent Class
class VendingMachine:
    def _init_(self, user_name):
        self.user_name = user_name

    def select_item(self, item):
        pass

# Child Class untuk Vending Machine Minuman
class DrinkVendingMachine(VendingMachine):
    def _init_(self, user_name):
        super()._init_(user_name)
        self.drinks = {"Coke": 10, "Water": 5, "Juice": 15}

    def select_item(self, item):
        price = self.drinks.get(item, None)
        if price:
            return f"{self.user_name} memilih {item}, harganya {price} ribu rupiah."
        else:
            return f"{item} tidak tersedia di mesin minuman."

# Child Class untuk Vending Machine Makanan Ringan
class SnackVendingMachine(VendingMachine):
    def _init_(self, user_name):
        super()._init_(user_name)
        self.snacks = {"Chips": 12, "Candy

```