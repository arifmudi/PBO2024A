print ("Nama: Zany Zafira Akmal")
print ("Nim: 2355201019")

### my tactical doll###
import math 
print("\n### My Tactical Doll ###")
myTacticalDoll = input ("Masukkan Nama Tactical Doll: ")
firepower = int(input("Masukkan firepower: "))
rate_of_fire = int(input("Masukkan rate of fire: "))
accuracy = int(input("Masukkan accuracy= "))
evasion = int(input("Masukkan evasion= "))

mydps= firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy+evasion)

### enemy tactical doll###
import math 
print("\n### Enemy Tactical Doll Data ###")
enemyTacticalDoll = input ("Masukkan Nama Tactical Doll= ")
firepower = int(input("Masukkan firepower= "))
rate_of_fire = int(input("Masukkan rate of fire= "))
accuracy = int(input("Masukkan accuracy= "))
evasion = int(input("Masukkan evasion= "))


enemydps= firepower * rate_of_fire / 60
combat_effectiveness = 30 * firepower + 40 * rate_of_fire/120 + 15 * (accuracy+evasion)

###Result###
print("\n### Result ###")
print(myTacticalDoll)
print(f"Damage per Second (DPS): {mydps:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")

print(enemyTacticalDoll )
print(f"Damage per Second (DPS): {enemydps:.2f}")
print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")

if mydps > enemydps:
    print("keputusan: gas lawan")
else:
    print("Keputusan: Kabuuur")