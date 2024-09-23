import math

def calculate_dps(firepower, rate_of_fire):
    return firepower * rate_of_fire / 60

def calculate_combat_effectiveness(firepower, rate_of_fire, accuracy, evasion):
    return 30 * firepower + 40 * rate_of_fire / 120 + 15 * (accuracy + evasion)

def main():
    x=input("Nama Kamu ")
    y=input("Nim Kamu ")


    # 1. Menerima input untuk Tactical Doll milikmu
    print("=== Masukkan Data Tactical Doll Milikmu ===")
    nama_doll_milikmu = input("Nama Tactical Doll milikmu: ")
    firepower_milikmu = int(input("Input firepower milikmu: "))
    rate_of_fire_milikmu = int(input("Input rate of fire milikmu: "))
    accuracy_milikmu = int(input("Input accuracy milikmu: "))
    evasion_milikmu = int(input("Input evasion milikmu: "))
    
    # 2. Menerima input untuk Tactical Doll musuh
    print("\n=== Masukkan Data Tactical Doll Musuh ===")
    nama_doll_musuh = input("Nama Tactical Doll musuh: ")
    firepower_musuh = int(input("Input firepower musuh: "))
    rate_of_fire_musuh = int(input("Input rate of fire musuh: "))
    accuracy_musuh = int(input("Input accuracy musuh: "))
    evasion_musuh = int(input("Input evasion musuh: "))

    # Menghitung DPS dan Combat Effectiveness
    dps_milikmu = calculate_dps(firepower_milikmu, rate_of_fire_milikmu)
    combat_effectiveness_milikmu = calculate_combat_effectiveness(firepower_milikmu, rate_of_fire_milikmu, accuracy_milikmu, evasion_milikmu)

    dps_musuh = calculate_dps(firepower_musuh, rate_of_fire_musuh)
    combat_effectiveness_musuh = calculate_combat_effectiveness(firepower_musuh, rate_of_fire_musuh, accuracy_musuh, evasion_musuh)

    # Menentukan langkah yang harus diambil
    if combat_effectiveness_milikmu > combat_effectiveness_musuh:
        langkah = "Melawan"
    else:
        langkah = "Menghindar"

    # Mencetak output
    print("\n=== Data Tactical Doll ===")
    print(f"Nama Lengkap Anda: {x}")
    print(f"NIM Anda: {y}")
    
    print("\n--- Tactical Doll Milikmu ---")
    print(f"Nama Tactical Doll: {nama_doll_milikmu}")
    print(f"Damage per Second (DPS): {dps_milikmu:.2f}")
    print(f"Combat Effectiveness: {math.floor(combat_effectiveness_milikmu)}")

    print("\n--- Tactical Doll Musuh ---")
    print(f"Nama Tactical Doll: {nama_doll_musuh}")
    print(f"Damage per Second (DPS): {dps_musuh:.2f}")
    print(f"Combat Effectiveness: {math.floor(combat_effectiveness_musuh)}")

    print(f"\nLangkah yang harus diambil: {langkah}")

if __name__ == "__main__":
    main()
