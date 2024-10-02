print("Nama: Ermita Sari")
print("Nim: 2355201024")

### My Tactical Doll ###
import math
print("\n---  My Tactical Doll  ---")
myTacticalDoll = input("Nama Tactical Doll: ")
firepower = int(input("Input firepower: "))
rate_of_fire = int(input("Input rate of fire: "))
accuracy = int(input("Input accuracy: "))
evasion = int(input("Input evasion: "))

mydps = firepower * rate_of_fire / 60
my_combat_effectiveness = 30 * firepower + 40 * rate_of_fire / 120 + 15 * (accuracy + evasion)

### Enemy Tactical Doll ###
import math
print("\n---  Enemy Tactical Doll  ---")
enemyTacticalDoll = input("Nama Tactical Doll: ")
firepower = int(input("Input firepower: "))
rate_of_fire = int(input("Input rate of fire: "))
accuracy = int(input("Input accuracy: "))
evasion = int(input("Input evasion: "))

enemydps = firepower * rate_of_fire / 60
enemy_combat_effectiveness = 30 * firepower + 40 * rate_of_fire / 120 + 15 * (accuracy + evasion)

### Results ###
print("\n--- Result ---")
print(myTacticalDoll)
print(f"Damage per Second (DPS): {mydps:.2f}")
print(f"Combat Effectiveness: {math.floor(my_combat_effectiveness)}")

print(enemyTacticalDoll)
print(f"Damage per Second (DPS): {enemydps:.2f}")
print(f"Combat Effectiveness: {math.floor(enemy_combat_effectiveness)}")

### Decision ###
if mydps > enemydps:
    print("Keputusan: Gas lawan")
else:
    print("Keputusan: kaburr")