print ("### REQUEST TACTICAL DOLL ###")
nama_tactical_doll = input ("Masukkan Nama Tactical Dollmu : ")
firepower = input ("Damage Firepower : ")
rate_of_fire = input ("Jumlah Rate Of fire : ")
accuracy = input ("Jumlah Accuracy : ")
evasion = input ("Masukkan Evasion : ")
damage_per_second = round (float(firepower) * float(rate_of_fire)/60,2)
combat_effectiveness = int (30 * float(firepower) +(40 * (float(rate_of_fire) ** 2) / 120) +(15 * (float(accuracy) + float(evasion))))
#paaak, rumusnya udh saya otak atik sejam, tapi hasilnya gabisa jadi 5215(sesuai contoh bapak) T_T 
# saya pasrah aja deh hasilnya berapa T_T


print ("### SUCCESS ###")
print ("Tactical Doll : " + str(nama_tactical_doll))
print ("Firepower : " + str(firepower))
print ("Rate Of Fire : " + str(rate_of_fire))
print ("Accurancy : " + str(accuracy))
print ("Evasion : " + str(evasion))
print ("Damage Per Second : " + str(damage_per_second))
print ("Combat Effectiveness : " + str(combat_effectiveness))

