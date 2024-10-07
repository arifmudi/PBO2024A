import math
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")

def calculate_dps(firepower, rate_of_fire):
    return firepower * rate_of_fire / 60

def calculate_combat_effectiveness(firepower, rate_of_fire, accuracy, evasion):
    return 30 * firepower + 40 * rate_of_fire / 120 + 15 * (accuracy + evasion)

def determine_action(your_dps, enemy_dps):
    if your_dps > enemy_dps:
        return "Melawan"
    else:
        return "Menghindar"

def print_tactical_doll_info(name, firepower, rate_of_fire, accuracy, evasion):
    dps = calculate_dps(firepower, rate_of_fire)
    combat_effectiveness = calculate_combat_effectiveness(firepower, rate_of_fire, accuracy, evasion)
    
    print(f"\n--- Tactical Doll: {name} ---")
    print(f"Damage per Second (DPS): {dps:.2f}")
    print(f"Combat Effectiveness: {math.floor(combat_effectiveness)}")
    return dps

print("\n--- Tactical Doll Data ---")

# Input for your Tactical Doll
print("\n--- Tactical Doll Anda ---")
your_name = input("Nama Tactical Doll Anda: ")
your_firepower = get_int_input("Input firepower: ")
your_rate_of_fire = get_int_input("Input rate of fire: ")
your_accuracy = get_int_input("Input accuracy: ")
your_evasion = get_int_input("Input evasion: ")

# Input for enemy's Tactical Doll
print("\n--- Tactical Doll Musuh ---")
enemy_name = input("Nama Tactical Doll Musuh: ")
enemy_firepower = get_int_input("Input firepower: ")
enemy_rate_of_fire = get_int_input("Input rate of fire: ")
enemy_accuracy = get_int_input("Input accuracy: ")
enemy_evasion = get_int_input("Input evasion: ")

# Print your Tactical Doll info and calculate DPS
your_dps = print_tactical_doll_info(your_name, your_firepower, your_rate_of_fire, your_accuracy, your_evasion)

# Print enemy's Tactical Doll info and calculate DPS
enemy_dps = print_tactical_doll_info(enemy_name, enemy_firepower, enemy_rate_of_fire, enemy_accuracy, enemy_evasion)

# Determine action based on DPS
action = determine_action(your_dps, enemy_dps)

# Output your name and student ID
print("\n--- Additional Information ---")
print(input("masukkan nama kamu:"))
print(input("masukkan nim kamu:"))

# Output recommended action
print(f"\nRekomendasi Tindakan: {action}")