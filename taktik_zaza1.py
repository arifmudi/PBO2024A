import math 

print("\n### Request Tactical Doll ###")
NamaTacticalDoll = input ("Masukkan Nama Tactical Doll= ")
firepower = int(input("Masukkan firepower= "))
rate_of_fire = int(input("Masukkan rate of fire= "))
accuracy = int(input("Masukkan Accuracy= "))
evasion = int(input("Masukkan Evasion= "))

dps= firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy+evasion)

print("\n###Succsess ###")
print(f"Nama Tactical Doll: {NamaTacticalDoll}")
print(f"Damage per Second (DPS): {dps:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")