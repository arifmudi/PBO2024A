# #KOORDINAT MEONG BROS#

# banyak_perintah = int(input("Masukkan banyak perintah : "))
# for x in range (banyak_perintah):
#     print (str(input("Masukkan ")))


# # print ("Banyak Perintah : ", + banyak_perintah)

# class informatika:
#     nama = "intan"
#     smester = 3

# p1= informatika()

# print (p1.nama)
# print (p1.smester)



# class informatika : 
#     def__init__(self,nama,semster)
#     self.name = nama
#     self.semester = semester

# p1 = informatika ("Intan",3)

# print (p1.nama)
# print (p1.)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)




class informatika: 
    def __init__(self,name,semester,matkul):
        self.name = name
        self.semester = semester 
        self.matkul = matkul

    def __str__(self):
        return f"Nama saya {self.name}. Saat ini saya di smester {self.semester} Dengan Matkul {self.matkul}.\nMatkul kesukaan saya {self.matkul}"
        +(f"\n Teman saya adalah")
    
    def teman_kanan (cls,nama_kawan):
        cls.nama_kawan = nama_kawan


me = informatika("intan", 3,"PBO")

informatika.teman_kanan("david")

print (me)



