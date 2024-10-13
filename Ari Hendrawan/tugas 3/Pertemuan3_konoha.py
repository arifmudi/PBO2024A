import random

def eligma_encrypt(input_string):

    digits = [random.randint(0, 9) for _ in range(3)]
    jumlah_angka = sum(digits)
    hasil_geser = ''.join(
        chr((ord(char.lower()) - ord('a') + jumlah_angka) % 26 + ord('a')) if char.isalpha() else char 
        for char in input_string
    )
    kode_string = ""
    indeks_digit = 0
    for char in hasil_geser:
        kode_string += char
        if indeks_digit < len(digits) and random.random() < 0.5:
            kode_string += str(digits[indeks_digit])
            indeks_digit += 1
    kode_string += ''.join(map(str, digits[indeks_digit:]))
    
    return kode_string

def eligma_decrypt(input_string):

    jumlah_angka = sum(int(char) for char in input_string if char.isdigit())
    hasil_geser = ''.join(
        chr((ord(char.lower()) - ord('a') - jumlah_angka) % 26 + ord('a')) if char.isalpha() else char 
        for char in input_string if not char.isdigit()
    )
    
    return hasil_geser

input_string = input("Masukkan pesan Rahasia: ")
kode_string = eligma_encrypt(input_string)
print("Kode Rahasia:", kode_string)

translate_string = eligma_decrypt(kode_string)
print("Translate no Jutsu:", translate_string)
