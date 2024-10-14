def eligma_encrypt(input_string):

    digits = [int(char) for char in input_string if char.isdigit()]
    jumlah_angka = sum(digits) if digits else 0
    
    hasil_geser = ''.join(
        chr((ord(char.lower()) - ord('a') + jumlah_angka) % 26 + ord('a')) if char.islower() else
        chr((ord(char.upper()) - ord('A') + jumlah_angka) % 26 + ord('A')) if char.isupper() else
        ''
        for char in input_string
    )
    return hasil_geser

input_string = input("Masukkan pesan Rahasia: ")
kode_string = eligma_encrypt(input_string)  
print("Kode Rahasia:", kode_string)