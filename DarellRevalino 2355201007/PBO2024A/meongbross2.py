import sys
x, y = 0, 0 
    
while True:
        try:
            n = int(input("Masukkan jumlah perintah: "))
            if n < 0:
                print("Jumlah perintah harus non-negatif.")
            else:
                break
        except ValueError:
            print("Masukkan angka yang valid.")
    
for _ in range(n):
        perintah = input("Masukkan perintah: ")
        
        if perintah == "U":
            y += 1
        elif perintah == "S":
            y -= 1
        elif perintah == "T":
            x += 1
        elif perintah == "B":
            x -= 1
        elif perintah == "HOME":
            print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")
            sys.exit()
print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")