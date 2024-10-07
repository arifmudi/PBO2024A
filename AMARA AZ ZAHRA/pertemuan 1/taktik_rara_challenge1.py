print (input("masukkan nama kamu: "))
print (input("masukan nim kamu: "))
### my tactical doll###
import math 
print("\n--- Tactical Doll Data ---")
NamaTacticalDoll = input ("Nama Tactical Doll= ")
firepower = int(input("input firepower= "))
rate_of_fire = int(input("input rate of fire= "))
accuracy = int(input("input accuracy= "))
evasion = int(input(" input evasion= "))

dps= firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy+evasion)

print("\n--- Succsess ---")
print(NamaTacticalDoll)
print(f"Damage per Second (DPS): {dps:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")

### enemy tactical doll###
import math 
print("\n--- Tactical Doll Data ---")
NamaTacticalDoll = input ("Nama Tactical Doll= ")
firepower = int(input("input firepower= "))
rate_of_fire = int(input("input rate of fire= "))
accuracy = int(input("input accuracy= "))
evasion = int(input(" input evasion= "))

dps= firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy+evasion)

print("\n--- Succsess ---")
print(NamaTacticalDoll)
print(f"Damage per Second (DPS): {dps:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")

print("keputusan:gas lawan")