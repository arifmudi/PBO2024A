def meong_bross():
    x, y = 0, 0
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

    print(f"Karakter Meong Brosss berada di koordinat ({x}, {y})")

if __name__ == "__main__":
    meong_bross()