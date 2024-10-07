# #KOORDINAT MEONG BROS#
def meong_bross():
    x, y = 0, 0
    while True:
        try:
            jumlah_jalan = int(input("Masukkan jumlah perintah: "))
            if jumlah_jalan < 0:
                print("Aduhh kakak, janagn negatif atuh >_<")
            else:
                break
        except ValueError:
            print("Invalid Kck, Masukkin bilangan real ajah")
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
            print("Aduhh mager banget buat jalan, hmph")

    print(f"Karakter Meong Brosss berada di koordinat ({x}, {y})")

if __name__ == "__main__":
    meong_bross()
