def prediksi_koordinat():
    x, y = 0, 0
  
    try:
        banyak_perintah = int(input("Banyak perintah: "))
        if banyak_perintah < 0:
            print("Banyak perintah harus bilangan non negatif!")
            return
    except ValueError:
        print("Input harus berupa bilangan bulat!")
        return

    for i in range(banyak_perintah):
        perintah = input(f"Masukkan perintah ke-{i+1}: ").strip().upper()

        # Menentukan aksi berdasarkan perintah
        if perintah == 'U':
            y += 1
        elif perintah == 'S':
            y -= 1
        elif perintah == 'T':
            x += 1
        elif perintah == 'B':
            x -= 1
        elif perintah == 'HOME':
            break 
        else:
            print(f"Perintah '{perintah}' tidak dikenali. Posisi Meong Bross tetap.")

    print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")

prediksi_koordinat()