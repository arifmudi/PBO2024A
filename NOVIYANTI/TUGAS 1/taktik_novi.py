import math

print("\n--- Tactical Doll Data ---")
NamaTacticalDoll = input ("Nama Tactical Doll= ")
firepower = int(input("input firepower= "))
rate_of_fire = int(input("input rate of fire= "))
accuracy = int(input("input accuracy= "))
evasion = int(input(" input evasion= "))

# Konversi
dps= firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy+evasion)

# Eksekusi
print("\n--- Succsess ---")
print(f"Nama Tactical Doll: {NamaTacticalDoll}")
print(f"Damage per Second (DPS): {dps:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")