# # class Mahasiswa:
# #     def __init__(self, nama, nim, prodi):
# #         self.nama = nama
# #         self.nim = nim
# #         self.prodi = prodi

# #     def perkenalan (self):
# #         print (f"halo nama saay {self.nama}, nim saya adalah {self.nim} dan saya dari prodi {self.prodi}")

# #         orangA = Mahasiswa (input (""))
        
# #         orangA.

# #         print (orangA)



# # class Mahasiswa:
# #     def _init_(self, nama, nim, prodi):
# #         self.nama = nama
# #         self.nim = nim
# #         self.prodi = prodi

# #     def perkenalan(self):
# #         print(f"Halo, nama saya {self.nama}, NIM saya adalah {self.nim}, dan saya dari prodi {self.prodi}.")

# # # Mengambil input untuk nama, nim, dan prodi
# # nama = input("Masukkan nama mahasiswa: ")
# # nim = input("Masukkan NIM mahasiswa: ")
# # prodi = input("Masukkan prodi mahasiswa: ")

# # # Membuat objek Mahasiswa
# # orangA = Mahasiswa(nama, nim, prodi)

# # # Memanggil method perkenalan
# # orangA.perkenalan()




class EligmaDecryptor:
    def __init__(self, message):
        self.message = message
        self.shift_value = 0  # Inisialisasi nilai pergeseran

    def validasi_massage(self):
        #memeriksa apakah pesan mengandung setidaknya 1 angka 
        if not any (char.isdigit () for char in self.message):
            raise ValueError("Pesan harus ada minimal 1 angka yaaa")

    def calculate_shift(self):
        # Menghitung total dari angka dalam string
        total = sum(int(char) for char in self.message if char.isdigit())
        self.shift_value = total  # Mengatur nilai pergeseran berdasarkan total

    def decrypt(self):
        # Menggeser huruf berdasarkan total yang dihitung
        decrypted_message = ""
        for char in self.message:
            if char.isalpha():  # Memeriksa apakah karakter adalah huruf
                # Menggeser karakter
                if char.islower():
                    new_char = chr((ord(char) - ord('a') + self.shift_value) % 26 + ord('a'))
                else:
                    new_char = chr((ord(char) - ord('A') + self.shift_value) % 26 + ord('A'))
                decrypted_message += new_char  # Menambahkan karakter yang telah digeser
        return decrypted_message

# Input dari pengguna
input_message = input("Masukkan pesan  (minimal 1 angka): ")

    # Membuat instance dari kelas EligmaDecryptor
decryptor = EligmaDecryptor(input_message)

try: 
    #Validasi pesan
    decryptor.validasi_massage()

    # Menghitung nilai pergeseran berdasarkan angka dalam pesan
    decryptor.calculate_shift()

    # Mendapatkan hasil dekripsi
    result = decryptor.decrypt()

    # Menampilkan hasil dekripsi
    print("Isi pesannya:", result)

except ValueError as e :
    print (e)
#--------------------------------------------------------------------------------------



# class EligmaEncryptor:
#     def _init_(self, masuk_string):
#         self.masuk_string = masuk_string

#     def _extract_digits(self):
#         return [int(char) for char in self.masuk_string if char.isdigit()]

#     def _calculate_shift(self):
#         digits = self._extract_digits()
#         return sum(digits) if digits else 0

#     def _shift_characters(self, char, shift):
#         if char.islower():
#             return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#         elif char.isupper():
#             return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#         else:
#             return ''

#     def encrypt(self):
#         shift = self._calculate_shift()
#         hasil_geser = ''.join(
#             self._shift_characters(char, shift) for char in self.masuk_string
#         )
#         return hasil_geser


# masuk_string = input("Masukkan pesan Rahasia: ")
# pengode = EligmaEncryptor(masuk_string)
# kode_string = pengode.encrypt()
# print("Kode Rahasia:", kode_string)