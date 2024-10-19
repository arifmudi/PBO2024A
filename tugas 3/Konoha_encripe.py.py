class Konoha:
    def __init__(self, encoded_str):
        self.encoded_str = encoded_str
        self.sum_digits = 0
        self.letters = []

    def calculate_sum_of_digits(self):
        """Menghitung total dari semua angka dalam string."""
        for char in self.encoded_str:
            if char.isdigit():
                self.sum_digits += int(char)

    def collect_letters(self):
        """Mengumpulkan huruf dari string."""
        for char in self.encoded_str:
            if char.isalpha():
                self.letters.append(char)

    def decrypt(self):
        """Dekripsi string berdasarkan nilai shift dari penjumlahan digit."""
        self.calculate_sum_of_digits()

        # Pengecekan untuk jumlah digit
        if self.sum_digits == 0:
            print("Tidak memiliki angka")
            return ""

        self.collect_letters()

        shift = self.sum_digits % 26  # Menghindari pergeseran lebih dari 26
        decrypted_letters = []

        for letter in self.letters:
            # Geser huruf kecil (mengonversi semua huruf menjadi lowercase)
            lower_letter = letter.lower()
            new_char = chr((ord(lower_letter) - ord('a') + shift) % 26 + ord('a'))
            decrypted_letters.append(new_char)

        return ''.join(decrypted_letters)

# Contoh penggunaan
input_str = "M13b3yni"
decoder = Konoha(input_str)
output = decoder.decrypt()
print(output)
