def meong_bross():
    x, y = 0, 0
    jejak = [(x, y)]
    while True:
        try:
            jumlah_jalan = int(input("Masukkan jumlah perintah: "))
            if jumlah_jalan < 0:
                print("Bikin apasih? jangan negatif lah.")
            else:
                break
        except ValueError:
            print("Invalid. Masukkan angka Bulat.")
    
    for _ in range(jumlah_jalan):
        jalan = input("Masukkan perintah : ").strip().upper()
        
        if jalan == "U":
            y += 1 
        elif jalan == "S":
            y -= 1  
        elif jalan == "T":
            x += 1  
        elif jalan == "B":
            x -= 1  
        elif jalan == "HOME":
            print(f"Koordinat saat ini: ({x}, {y})")
        else:
            print("Apanih Nyaong, Meong Bross Muager.")
        
        jejak.append((x, y))

    jalur = '-'.join(f"({titik[0]},{titik[1]})" for titik in jejak)
    print(f"Jalur yang ditempuh meong bross adalah {jalur}")

if __name__ == "__main__":
    meong_bross()