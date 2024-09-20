# identitas
print("Nama : Ari Hendrawan")
print("NIM : 2355201034")

# input doll kamu
print("### MY TACTICAL DOLL ###")
nama_doll_kamu = input("Masukkan Nama Doll : ")
firepower_kamu = int(input("Masukkan Firepower  : "))
rate_of_fire_kamu = int(input("Masukkan Rate Of Fire : "))
accuracy_kamu = int(input("Masukkan Accuracy : "))
evasion_kamu = int(input("Masukkan Evasion : "))

# input doll musuh
print("### MY TACTICAL DOLL ###")
nama_doll_musuh = input("Masukkan Nama Doll : ")
firepower_musuh = int(input("Masukkan Firepower  : "))
rate_of_fire_musuh = int(input("Masukkan Rate Of Fire : "))
accuracy_musuh = int(input("Masukkan Accuracy : "))
evasion_musuh = int(input("Masukkan Evasion : "))

# DPS dari kamu
my_dps= round(firepower_kamu * rate_of_fire_kamu / 60, 2)
my_combat_effectiveness = int(30 * firepower_kamu + 40 * pow(rate_of_fire_kamu,2)/120 + 15 * (accuracy_kamu+evasion_kamu))

# DPS dari musuh
enemy_dps= round(firepower_musuh * rate_of_fire_musuh / 60, 2)
enemy_combat_effectiveness = int(30 * firepower_musuh + 40 * pow(rate_of_fire_musuh,2)/120 + 15 * (accuracy_musuh+evasion_musuh))

# menentukan keputusan
if my_combat_effectiveness > enemy_combat_effectiveness:
    keputusan = "Gass Lawan lah"
else:
    keputusan = "mundur aja lah, capek"

# hasil perhitungan doll kamu
print(f"\n{nama_doll_kamu}")
print(f"Damage per Second: {my_dps}")
print(f"Combat Effectiveness: {my_combat_effectiveness}")

# hasil perhitungan doll kamu
print(f"\n{nama_doll_musuh}")
print(f"Damage per Second: {enemy_dps}")
print(f"Combat Effectiveness: {enemy_combat_effectiveness}")

print(f"\nKeputusan : {keputusan}")