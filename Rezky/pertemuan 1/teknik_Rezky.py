import math

print("\n--- TacticalDoll Data ---")
NamaTacticalDoll = input ("Masukkan Nama Tactical Doll= ")
firepower = int(input("Masukkan firepower= "))
rate_of_fire = int(input("Masukkan rate of fire= "))
accuracy = int(input("Masukkan accuracy= "))
evasion = int(input("Masukkan evasion= "))

# Konversi
dps= firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy)

# Eksekusi
print("\n--- Succsess ---")
print(f"Tactical Doll: {NamaTacticalDoll}")
print(f"Firepower: {firepower}")
print(f"Rate Of Fire: {rate_of_fire}")
print(f"Accuracy: {accuracy}")
print(f"Evasion: {evasion}")
print(f"Damage per Second (DPS): {dps:.25f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")