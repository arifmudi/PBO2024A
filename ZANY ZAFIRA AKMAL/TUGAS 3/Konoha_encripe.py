class EnigmaDecoder:
    def __init__(self, text):
        """
        Inisialisasi kelas dengan teks yang akan didekripsi.
        Args:
            text: Teks yang akan didekripsikan.
        """
        self.text = text

    def enigma_decode(self):
        """
        Fungsi untuk mendekripsikan kode enigma.
        Returns:
            Teks yang sudah didekripsikan.
        """

        numbers = []
        letters = []
        for char in self.text:
            if char.isdigit():
                numbers.append(int(char))
            elif char.isalpha():
                letters.append(char)

        # Hitung total angka
        total_numbers = sum(numbers)

        # Dekripsikan alfabet
        decoded_letters = []
        for letter in letters:
            # Konversi huruf menjadi kode ASCII
            ascii_code = ord(letter)
            # Geser huruf ke kanan sesuai total angka
            shifted_code = ascii_code + total_numbers
            # Jika huruf melewati 'z', reset ke 'a'
            if shifted_code > ord('z'):
                shifted_code -= 26
            # Konversi kode ASCII kembali menjadi huruf
            decoded_letter = chr(shifted_code)
            decoded_letters.append(decoded_letter)

        # Gabungkan huruf yang sudah didekripsikan
        decoded_text = "".join(decoded_letters)

        return decoded_text

# Contoh penggunaan
input_text = input("Masukkan teks: ")
decoder = EnigmaDecoder(input_text)  # Membuat instance kelas EnigmaDecoder dengan input teks
decoded_text = decoder.enigma_decode()  # Memanggil metode enigma_decode
print(f"Input: {input_text}, Output: {decoded_text}")
