def decrypt_eligma_code(input_str):
    # Inisialisasi variabel
    jumlah_angka = 0
    hasil_dekripsi = ""

    # Iterasi melalui setiap karakter dalam input
    for char in input_str:
        if char.isdigit():  # Jika karakter adalah angka
            jumlah_angka += int(char)
        elif char.isalpha():  # Jika karakter adalah alfabet
            hasil_dekripsi += char

    # Geser setiap alfabet sebanyak jumlah_angka
    output = ""
    for char in hasil_dekripsi:
        # Geser ke kanan dengan memperhatikan siklus alfabet
        geser = (ord(char.lower()) - ord('a') + jumlah_angka) % 26
        karakter_baru = chr(ord('a') + geser)
        output += karakter_baru

    return output

# Contoh penggunaan
input_str = "M13b3yni"
print(decrypt_eligma_code(input_str)) # Output: tifup