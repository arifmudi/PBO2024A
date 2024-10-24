
class EligmaDecryptor:
    def __init__(self, message):
        self.message = message
        self.shift_value = 0  # Inisialisasi nilai pergeseran

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

# Validasi input
if not any(char.isdigit() for char in input_message):
    print("Pesan harus mengandung minimal satu angka.")
else:
    # Membuat instance dari kelas EligmaDecryptor
    decryptor = EligmaDecryptor(input_message)

    # Menghitung nilai pergeseran berdasarkan angka dalam pesan
    decryptor.calculate_shift()

    # Mendapatkan hasil dekripsi
    result = decryptor.decrypt()

    # Menampilkan hasil dekripsi
    print("Isi pesannya:", result)

#--------------------------------------------------------------------------------------
