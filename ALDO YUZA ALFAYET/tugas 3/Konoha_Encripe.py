class KonohaDecoder:
    def __init__(self, encrypted_code):
        self.encrypted_code = encrypted_code
        self.shift_value = 0
        self.cleaned_message = []

    def extract_digits_and_chars(self):
        """
        Ekstraksi angka untuk menghitung total shift, dan huruf diubah menjadi huruf kecil.
        """
        self.shift_value = sum(int(char) for char in self.encrypted_code if char.isdigit())
        self.cleaned_message = [char.lower() for char in self.encrypted_code if char.isalpha()]

    def apply_shift(self):
        """
        Menggeser huruf berdasarkan shift yang dihitung dari angka.
        """
        return ''.join(
            chr((ord(char) - ord('a') + self.shift_value) % 26 + ord('a'))
            for char in self.cleaned_message
        )

    def decrypt(self):
        """
        Proses dekripsi: validasi, ekstraksi karakter, dan penggeseran.
        """
        if not any(char.isdigit() for char in self.encrypted_code):
            return "Error: Pesan harus mengandung setidaknya 1 angka."

        self.extract_digits_and_chars()
        return self.apply_shift()


# Input dari pengguna
input_code = input("Masukkan kode: ")

# Membuat instance dari kelas KonohaDecoder
decoder = KonohaDecoder(input_code)

# Menampilkan hasil dekripsi
output = decoder.decrypt()
print(output)
 