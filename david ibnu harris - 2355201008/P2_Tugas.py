# class Informatika:
#     def __init__(self, nama, semester, matakuliah, orangKanan):
#         self.nama = nama
#         self.semester = semester
#         self.matakuliah = matakuliah

#     def __str__(self):
#         return (f"Nama saya {self.nama} \nsaat ini semester {self.semester} "
#                 f"\ndengan matkul {self.matakuliah}, \nMatkul Favorit {self.matakuliah}. "
#                 f"\nOrang Disebelah Kanan {self.orangKanan}.")


# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc() 

class Informatika:
    def __init__(self, nama, semester, matakuliah):
        self.nama = nama
        self.semester = semester
        self.matakuliah = matakuliah
        self.orangKanan = "Intan." 

    def set_orang_kanan(self, orangKanan):
        self.orangKanan = orangKanan

    def myfunc(self):
        print(f"Nama saya {self.nama} \nsaat ini semester {self.semester} "
              f"\ndengan matkul {self.matakuliah}, \nMatkul Favorit {self.matakuliah}. "
              f"\nOrang Disebelah Kanan {self.orangKanan}.")

# Membuat objek
variabel = Informatika("David Ibnu Harris", 3, "PBO")
variabel.set_orang_kanan("Intan") 
variabel.myfunc()



