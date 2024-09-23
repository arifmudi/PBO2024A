#TASK 2

import random
print ("SELAMAT DATANG DI LOVEMATER")
nama_dia = input ("nama doi kamu : ")

cocok = random.random()
print("kecocokan anda", cocok*100, "%")

if cocok > 0.8 :
    print ("woww kamu cocok banget sama " + nama_dia + "!!!")
elif 0.5 <= cocok <=0.8:
    print("yaaa kamu lumayan cocok lah sama " + nama_dia + ":)")
else :
    print("kamu ga cocok sama " + nama_dia + " cari yang lain aja, masih banyak ikan di laut^^")