# Kelas induk untuk semua hewan
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Kelas turunan untuk Mamalia
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def move(self):
        return f"{self.name} is walking on four legs."

# Kelas turunan untuk Burung
class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span

    def make_sound(self):
        return "Chirp!"

    def move(self):
        return f"{self.name} is flying."

# Kelas turunan untuk Reptil
class Reptile(Animal):
    def __init__(self, name, scale_color):
        super().__init__(name)
        self.scale_color = scale_color

    def make_sound(self):
        return "Hiss!"

    def move(self):
        return f"{self.name} is slithering."

# Komposisi untuk suara hewan
class AnimalSound:
    def __init__(self, sound):
        self.sound = sound

    def produce_sound(self):
        return self.sound

# Menggunakan komposisi untuk suara hewan tertentu
class Dog(Mammal):
    def __init__(self, name, fur_color):
        super().__init__(name, fur_color)
        self.sound = AnimalSound("Bark!")

    def make_sound(self):
        return self.sound.produce_sound()

class Parrot(Bird):
    def __init__(self, name, wing_span):
        super().__init__(name, wing_span)
        self.sound = AnimalSound("Squawk!")

    def make_sound(self):
        return self.sound.produce_sound()

# Membuat objek hewan
dog = Dog("Buddy", "Golden")
parrot = Parrot("Polly", "15 inches")
snake = Reptile("Slither", "Green")

# Menggunakan objek
animals = [dog, parrot, snake]

for animal in animals:
    print(f"{animal.name}:")
    print(f"  Sound: {animal.make_sound()}")
    print(f"  Movement: {animal.move()}\n")
