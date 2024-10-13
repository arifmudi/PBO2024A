def decrypt_eligma_code(input_str):
    
    jumlah_angka = 0
    hasil_dekripsi = ""

    for char in input_str:
        if char.isdigit():  
            jumlah_angka += int(char)
        elif char.isalpha():  
            hasil_dekripsi += char

    output = ""
    for char in hasil_dekripsi:
        slide = (ord(char.lower()) - ord('a') + jumlah_angka) % 26
        newchar = chr(ord('a') + slide)
        output += newchar

    return output

# Contoh penggunaan
input_str = "M13b3yni"
print(decrypt_eligma_code(input_str))