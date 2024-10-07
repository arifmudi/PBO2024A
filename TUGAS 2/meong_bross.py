def meong_bross():
    # Posisi awal Meongbross
    x, y = 0, 0
    
    # Input jumlah perintah
    try :
        jumlah_perintah = int(input("Masukkan jumlah perintah: "))
        
        # Identifikasi input jumlah perintah
        if jumlah_perintah < 0:
            print("Jumlah perintah adalah bilangan non negatif.")
            
    except ValueError:
        print("Tidak valid. Coba masukkan bilangan bulat!")
        

    # Proses setiap perintah
    for _ in range(jumlah_perintah):
        p = input("Masukkan perintah: ").strip()
        
        if p == 'U':
            y += 1  # Bergerak ke Utara
        elif p == 'S':
            y -= 1  # Bergerak ke Selatan
        elif p == 'T':
            x += 1  # Bergerak ke Timur
        elif p == 'B':
            x -= 1  # Bergerak ke Barat
        elif p == 'HOME':
            break  # Menghentikan eksekusi
        else:
            print("GAGAL, Meong Bross tidak bergerak.")
    
    # Output posisi akhir Meong Bross dengan format yang diminta
    print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")

# Menjalankan program
meong_bross()

