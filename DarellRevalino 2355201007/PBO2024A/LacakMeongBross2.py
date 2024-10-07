import sys
x, y = 0, 0
trace = [(x, y)]

print(str("Direction U, S, T, B, HOME"))

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
    while True:  
        perintah = input("Masukkan perintah: ").upper()  
        
        if perintah == "U":
            y += 1
            break  
        elif perintah == "S":
            y -= 1
            break  
        elif perintah == "T":
            x += 1
            break  
        elif perintah == "B":
            x -= 1
            break  
        elif perintah == "HOME":
            print(f"Karakter Meong Bross berada di koordinat ({x},{y})")
            break  
        elif perintah == "STOP":
            print("Program Berhenti.")
            sys.exit()  
        else:
            print("Perintah Salah!") 

trace.append((x, y))
print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")
print(f"Jejak koordinat yang dilalui: {trace}")