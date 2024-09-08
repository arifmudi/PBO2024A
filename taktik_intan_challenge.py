print ("Nama : Intan Nurzari")
print ("Nim : 2355201035")

#TACTICAL DOLL KITA
print ("### MY TECTICAL DOLL ###")
nama_tactical_doll = input ("Masukkan Nama Tactical Dollmu : ")
firepower = input ("Damage Firepower : ")
rate_of_fire = input ("Jumlah Rate Of fire : ")
accuracy = input ("Jumlah Accuracy : ")
evasion = input ("Masukkan Evasion : ")
damage_per_second = round (float(firepower) * float(rate_of_fire)/60,2)
combat_effectiveness = int (30 * float(firepower) +(40 * (float(rate_of_fire) ** 2) / 120) +(15 * (float(accuracy) + float(evasion))))


#TACTICAL DOLL MUSUH
print ("### ENEMY TACTICAL DOLL ###")
nama_tactical_doll_musuh = input ("Masukkan Nama Tactical Doll Musuh : ")
firepower_musuh = input ("Damage Firepower Musuh : ")
rate_of_fire_musuh = input ("Jumlah Rate Of fire Musuh : ")
accuracy_musuh = input ("Jumlah Accuracy Musuh : ")
evasion_musuh = input ("Masukkan Evasion Musuh : ")
damage_per_second_musuh = round (float(firepower_musuh) * float(rate_of_fire_musuh)/60,2)
combat_effectiveness_musuh = int (30 * float(firepower_musuh) +(40 * (float(rate_of_fire_musuh) ** 2) / 120) +(15 * (float(accuracy_musuh) + float(evasion_musuh))))

#KEPUTUSAN
power_doll = damage_per_second + combat_effectiveness
power_doll_musuh = damage_per_second_musuh + combat_effectiveness_musuh

print ("### RESULT ###")
print (nama_tactical_doll)
print ("Damage Per Second : " + str(damage_per_second))
print ("Combat Effecttiveness : " + str(combat_effectiveness))
print (nama_tactical_doll_musuh)
print ("Damage Per Second : " + str(damage_per_second_musuh))
print ("Combat Effecttiveness : " + str(combat_effectiveness_musuh))

#LANGKAH YG DIAMBIL
if power_doll > power_doll_musuh:
    print ("Keputusan : Gasssss broooo, huraaaaaaa")
elif power_doll < power_doll_musuh:
    print ("Keputusan : OP BET anjay, musuhnya udh snowball, Lariiii")