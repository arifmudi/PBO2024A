# Fungsi untuk menghitung Damage Per Second (DPS) dan Combat Effectiveness (CE)
def hitung_dps_ce(firepower, rate_of_fire, accuracy, evasion):
    # Menghitung Damage Per Second (DPS)
    dps = round(firepower * rate_of_fire / 60, 2)
    # Menghitung Combat Effectiveness (CE)
    ce = int(firepower + rate_of_fire + accuracy + evasion)
    return dps, ce

# Input data dari pengguna
nama_tactical_doll = input("Masukkan nama Tactical Doll: ")
firepower = int(input("Masukkan nilai Firepower: "))
rate_of_fire = int(input("Masukkan nilai Rate of Fire: "))
accuracy = int(input("Masukkan nilai Accuracy: "))
evasion = int(input("Masukkan nilai Evasion: "))

# Menghitung DPS dan CE
dps, ce = hitung_dps_ce(firepower, rate_of_fire, accuracy, evasion)

# Mencetak hasil
print(f"{nama_tactical_doll} memiliki:")
print(f"Damage per Second (DPS): {dps}")
print(f"Combat Effectiveness (CE): {ce}")