Aspek Unik dan Jarang Diketahui tentang Pewarisan Python
1. Abstract Base Classes (ABC) dan Interface
Konsep Interface di Python menggunakan ABC
from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardPayment(PaymentInterface):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"
    
    def refund(self, amount):
        return f"Refunding ${amount} to Credit Card"
2. Mixin Classes - Teknik Pewarisan Canggih
Penggunaan Mixin untuk Menambah Fungsionalitas
class TimestampMixin:
    def get_current_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class LoggerMixin:
    def log(self, message):
        print(f"{self.get_current_timestamp()} - {message}")

class UserAccount(TimestampMixin, LoggerMixin):
    def __init__(self, username):
        self.username = username
    
    def login(self):
        self.log(f"User {self.username} logged in")
3. Property Inheritance dan Descriptor
Custom Descriptors dengan Inheritance
class ValidatedProperty:
    def __init__(self, minimum=None, maximum=None):
        self.minimum = minimum
        self.maximum = maximum
    
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if self.minimum is not None and value < self.minimum:
            raise ValueError(f"Value must be greater than {self.minimum}")
        if self.maximum is not None and value > self.maximum:
            raise ValueError(f"Value must be less than {self.maximum}")
        obj.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name

class Product:
    price = ValidatedProperty(minimum=0)
    quantity = ValidatedProperty(minimum=0, maximum=100)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
4. Context Manager Inheritance
Membuat Context Manager yang Dapat Diwariskan
class BaseContextManager:
    def __init__(self, resource_name):
        self.resource_name = resource_name
    
    def __enter__(self):
        print(f"Acquiring {self.resource_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing {self.resource_name}")
        return False  # Re-raise any exceptions

class DatabaseConnection(BaseContextManager):
    def __init__(self, db_name):
        super().__init__(f"Database connection to {db_name}")
        self.db_name = db_name
    
    def query(self, sql):
        return f"Executing {sql} on {self.db_name}"

# Penggunaan
with DatabaseConnection("users_db") as db:
    result = db.query("SELECT * FROM users")
5. Metaclass Inheritance
Customizing Class Creation
class ValidationMeta(type):
    def __new__(cls, name, bases, attrs):
        # Validate attributes before class creation
        for key, value in attrs.items():
            if key.startswith('price_'):
                if not isinstance(value, (int, float)):
                    raise TypeError(f"{key} must be a number")
                if value < 0:
                    raise ValueError(f"{key} cannot be negative")
        return super().__new__(cls, name, bases, attrs)

class Product(metaclass=ValidationMeta):
    price_regular = 100
    price_discount = 80

    def __init__(self, name):
        self.name = name
6. Dynamic Inheritance
Runtime Class Generation
def create_specialized_class(base_class, **attributes):
    """Membuat kelas baru dengan atribut yang ditentukan runtime"""
    return type(
        f"Specialized{base_class.__name__}",
        (base_class,),
        attributes
    )

class Animal:
    def speak(self):
        return self.sound

# Membuat kelas secara dinamis
DogClass = create_specialized_class(Animal, sound="Woof!")
CatClass = create_specialized_class(Animal, sound="Meow!")

# Penggunaan
dog = DogClass()
print(dog.speak())  # Output: Woof!
7. Slot Inheritance
Mengoptimalkan Penggunaan Memori
class BaseModel:
    __slots__ = ['id', 'created_at']
    
    def __init__(self, id):
        self.id = id
        self.created_at = datetime.now()

class User(BaseModel):
    __slots__ = ['username', 'email']
    
    def __init__(self, id, username, email):
        super().__init__(id)
        self.username = username
        self.email = email
8. Generic Programming dengan Inheritance
Type Hints dan Generic Classes
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    
    def get_item(self) -> T:
        return self.item

class StringContainer(Container[str]):
    def get_uppercase(self) -> str:
        return self.item.upper()

# Penggunaan
str_container = StringContainer("hello")
print(str_container.get_uppercase())  # Output: HELLO
9. Multi-dispatch Inheritance
Method Overloading Berbasis Tipe
from functools import singledispatchmethod

class Calculator:
    @singledispatchmethod
    def add(self, x):
        raise NotImplementedError("Unsupported type")
    
    @add.register(int)
    def _(self, x: int):
        return x + 1
    
    @add.register(str)
    def _(self, x: str):
        return x + "1"

# Penggunaan
calc = Calculator()
print(calc.add(5))      # Output: 6
print(calc.add("5"))    # Output: 51
10. Aspek-aspek Keamanan dalam Pewarisan
Protected dan Private Attributes
class SecureBase:
    def __init__(self):
        self._protected = "Can be accessed by child classes"
        self.__private = "Cannot be accessed directly by child classes"
    
    def _protected_method(self):
        return "Protected method"
    
    def __private_method(self):
        return "Private method"

class SecureChild(SecureBase):
    def access_members(self):
        print(self._protected)  # Works fine
        # print(self.__private)  # Raises AttributeError
        print(self._protected_method())  # Works fine
        # print(self.__private_method())  # Raises AttributeError
Kesimpulan dan Best Practices
Gunakan Abstract Base Classes untuk memaksakan interface
Manfaatkan Mixin untuk menambah fungsionalitas tanpa hierarki yang kompleks
Pertimbangkan penggunaan slots untuk optimasi memori
Gunakan metaclasses dengan bijak untuk kasus khusus
Manfaatkan type hints untuk keamanan tipe
Pertimbangkan protected vs private attributes dengan cermat