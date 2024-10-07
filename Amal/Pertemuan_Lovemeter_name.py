import random
print("Selamat Datang Di Lovemeter")
nama_dia = "Super Amal"
cocok = random.random()
print("Kecocokan anda" , cocok * 100, "%")
if cocok > 0.8:
    print("Anda sangat cocok dengan " + nama_dia + "!" )
elif 0.5 <= cocok <= 0.8:
    print("Anda lumayan cocok dengan " + nama_dia + "!")
else:
    print("Anda tidak cocok dengan " + nama_dia + "!")