import math 
print("\n### Tactical Doll Data ###")
NamaTacticalDoll = input ("Masukkan Nama Tactical Doll= ")
firepower = int(input("Masukkan firepower= "))
rate_of_fire = int(input("Masukkan rate of fire= "))
accuracy = int(input("Masukkan accuracy= "))
evasion = int(input("Masukkan evasion= "))

dps= firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy+evasion)

print("\n### Succsess ###")
print(f"Tactical Doll: {NamaTacticalDoll}")
print(f"firepower:{firepower}")
print(f"rate of fire:{rate_of_fire}")
print(f"accuracy:{accuracy}")
print(f"evasion:{evasion}")
print(f"Damage per Second (DPS): {dps:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")