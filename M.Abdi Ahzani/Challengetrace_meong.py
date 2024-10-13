# Program untuk memprediksi jalur koordinat Meong Bross
def trace_meong_bross():
    # Inisialisasi posisi awal dan jalur
    x, y = 0, 0
    jalur = [(x, y)]  # Menyimpan jalur yang dilalui
    
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
        
        # Simpan posisi saat ini ke dalam jalur
        jalur.append((x, y))
    
    # Format output untuk jalur
    jalur_str = '-'.join([f"({a},{b})" for a, b in jalur])
    
    # Output jalur yang ditempuh
    print(f"Jalur yang ditempuh Meong Bross adalah {jalur_str}")

# Menjalankan program
trace_meong_bross()
