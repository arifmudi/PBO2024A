STUDI KASUS : Sistem Manajemen Data Pelanggan Bank

Di dunia perbankan, manajemen data pelanggan sangat penting untuk memberikan layanan yang lebih baik dan personal. 
Dengan semakin banyaknya produk dan layanan yang ditawarkan bank, pengelompokan data pelanggan berdasarkan jenis akun dan layanan 
yang mereka gunakan menjadi suatu kebutuhan. Dalam studi kasus ini, kita akan menggunakan prinsip inheritance dalam 
pemrograman berorientasi objek untuk merancang sistem penyimpanan data pelanggan bank yang efisien dan terstruktur.

Sistem manajemen data pelanggan bank ini terdiri dari beberapa kelas yang merepresentasikan pelanggan dan jenis akun yang mereka miliki. 
Kita akan mengimplementasikan berbagai jenis inheritance:

1. Single Inheritance: Digunakan untuk mendefinisikan kelas dasar Customer dan kelas turunan SavingsAccount. 
Kelas ini menyimpan informasi dasar tentang pelanggan dan saldo akun tabungan mereka.

2. Multiple Inheritance: Kelas CustomerWithContact mewarisi dari Customer dan ContactInfo, 
yang memungkinkan penyimpanan informasi kontak pelanggan seperti email dan nomor telepon.

3. Multilevel Inheritance: Dalam contoh ini, CurrentAccount merupakan kelas anak dari BankAccount, 
yang juga diintegrasikan dengan kelas Customer untuk menciptakan CustomerWithCurrentAccount. 
Ini menggambarkan hubungan yang lebih kompleks di mana satu jenis akun dapat memiliki sifat tambahan.

4. Hierarchical Inheritance: Kelas PremiumAccount adalah kelas turunan dari kelas Customer, 
menunjukkan bagaimana beberapa jenis akun (seperti akun premium) dapat memiliki manfaat tambahan. 
Ini memungkinkan pengelompokan semua jenis akun di bawah kelas pelanggan yang sama.

5. Hybrid Inheritance: Kelas CustomerWithLoyalty menggabungkan BaseCustomer dan LoyaltyProgram untuk menyimpan 
data pelanggan sekaligus informasi tentang poin loyalitas. Ini memberikan fleksibilitas dalam manajemen data dan fitur baru.

Customer: Kelas dasar yang menyimpan nama dan nomor akun.
SavingsAccount: Kelas turunan yang menambahkan informasi saldo.
ContactInfo: Kelas untuk menyimpan informasi kontak.
CustomerWithContact: Kelas yang menggabungkan informasi pelanggan dan kontak.
BankAccount: Kelas dasar untuk semua jenis akun.
CurrentAccount: Kelas untuk akun giro dengan limit overdraft.
PremiumAccount: Kelas untuk akun premium dengan manfaat khusus.
BaseCustomer dan LoyaltyProgram: Kelas untuk mengelola data pelanggan dan program loyalitas dalam hybrid inheritance.

_codingan_

1. Single Inheritance

###
class Customer:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number

    def display_info(self):
        return f"Name: {self.name}, Account Number: {self.account_number}"

class SavingsAccount(Customer):
    def __init__(self, name, account_number, balance):
        super().__init__(name, account_number)
        self.balance = balance

    def display_info(self):
        return super().display_info() + f", Balance: {self.balance}"
###


2. Multiple Inheritance 

###
class ContactInfo:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

class CustomerWithContact(Customer, ContactInfo):
    def __init__(self, name, account_number, email, phone):
        Customer.__init__(self, name, account_number)
        ContactInfo.__init__(self, email, phone)

    def display_info(self):
        return super().display_info() + f", Email: {self.email}, Phone: {self.phone}"
###

3. Multi Level Inheritance

###
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number

class CurrentAccount(BankAccount):
    def __init__(self, account_number, overdraft_limit):
        super().__init__(account_number)
        self.overdraft_limit = overdraft_limit

class CustomerWithCurrentAccount(Customer, CurrentAccount):
    def __init__(self, name, account_number, overdraft_limit):
        Customer.__init__(self, name, account_number)
        CurrentAccount.__init__(self, account_number, overdraft_limit)

    def display_info(self):
        return super().display_info() + f", Overdraft Limit: {self.overdraft_limit}"
###

4. Hirarki Inheritance

###
class PremiumAccount(Customer):
    def __init__(self, name, account_number, benefits):
        super().__init__(name, account_number)
        self.benefits = benefits

    def display_info(self):
        return super().display_info() + f", Benefits: {self.benefits}"

# Penggunaan
customer1 = SavingsAccount("Alice", "12345", 1000)
customer2 = PremiumAccount("Bob", "67890", "Priority Service")

print(customer1.display_info())
print(customer2.display_info())
###

5. Hybird Inheritance 

###
class BaseCustomer:
    def __init__(self, name):
        self.name = name

class LoyaltyProgram:
    def __init__(self, points):
        self.points = points

class CustomerWithLoyalty(BaseCustomer, LoyaltyProgram):
    def __init__(self, name, points):
        BaseCustomer.__init__(self, name)
        LoyaltyProgram.__init__(self, points)

    def display_info(self):
        return f"Customer: {self.name}, Loyalty Points: {self.points}"

# Penggunaan
customer3 = CustomerWithLoyalty("Charlie", 150)
print(customer3.display_info())
###

