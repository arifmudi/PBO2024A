class EnigmaDecoder:
    def __init__(self, text):
        self.text = text

    def decode(self):
        numbers = []
        letters = []
        for char in self.text:
            if char.isdigit():
                numbers.append(int(char))
            elif char.isalpha():
                letters.append(char)
        # Jika tidak ada angka, kembalikan string kosong
        if not numbers:
            return "minimal masukkan 1 angka"

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
input_text = input("Masukkan nama: ")
decoder = EnigmaDecoder(input_text)
decoded_text = decoder.decode()
print(f"Input: {input_text}")
print(f"Output: {decoded_text}")
