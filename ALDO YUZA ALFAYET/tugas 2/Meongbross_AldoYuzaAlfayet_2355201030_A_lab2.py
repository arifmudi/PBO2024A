# Program untuk memprediksi koordinat akhir Meong Bross
def meong_bross():
    # Inisialisasi posisi awal
    x, y = 0, 0
    
    # Meminta input jumlah perintah
    banyak_perintah = int(input("Banyak perintah: "))
    
    # Loop untuk meminta input perintah
    for _ in range(banyak_perintah):
        perintah = input("Masukkan perintah: ")
        
        if perintah == "U":
            y += 1  # Bergerak ke Utara (Y positif)
        elif perintah == "S":
            y -= 1  # Bergerak ke Selatan (Y negatif)
        elif perintah == "T":
            x += 1  # Bergerak ke Timur (X positif)
        elif perintah == "B":
            x -= 1  # Bergerak ke Barat (X negatif)
        elif perintah == "HOME":
            x, y = 0, 0  # Kembali ke titik asal (0,0)
    
    # Output koordinat akhir
    print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")

# Menjalankan program
meong_bross()
