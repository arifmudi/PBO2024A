def eligma_encrypt(input_string):
   
    digits = [int(char) for char in input_string if char.isdigit()]
    if not digits:
        raise ValueError("Input harus mengandung minimal 1 angka.")
    
    jumlah_angka = sum(digits)  
    
    hasil_geser = ''.join(
        chr((ord(char.lower()) - ord('a') + jumlah_angka) % 26 + ord('a')) if char.isalpha() else ''
        for char in input_string
    )
    
    return hasil_geser

input_string = input("Masukkan pesan Rahasia: ")

kode_string = eligma_encrypt(input_string)  
print("Kode Rahasia:", kode_string) 
