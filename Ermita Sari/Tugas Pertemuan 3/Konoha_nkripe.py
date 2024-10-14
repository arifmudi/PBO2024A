class EnigmaDecoder:
    def init(self, text):
        """
        Inisialisasi kelas dengan teks yang akan didekripsi.
        Args:
            text: Teks yang akan didekripsikan.
        """
        self.text = text

    def enigma_decode(self):
        """
        Fungsi untuk mendekripsikan teks dengan menggeser huruf
        berdasarkan total nilai angka dalam teks.
        Returns:
            Teks yang sudah didekripsikan, atau pesan error jika tidak ada angka dalam teks.
        """
        # Cek apakah teks mengandung setidaknya 1 angka
        if not any(char.isdigit() for char in self.text):
            return "Error: Pesan harus mengandung setidaknya 1 angka."

        total_shift = sum(int(char) for char in self.text if char.isdigit())
        decoded_text = []

        for char in self.text:
            if char.isalpha():
                # Geser huruf dengan mempertimbangkan jenis huruf
                base = ord('a') if char.islower() else ord('A')
                shifted_code = (ord(char) - base + total_shift) % 26 + base
                decoded_text.append(chr(shifted_code))

        return ''.join(decoded_text)

# Contoh penggunaan
input_text = input("Masukkan teks: ")
decoder = EnigmaDecoder(input_text)  # Membuat instance kelas EnigmaDecoder dengan input teks
decoded_text = decoder.enigma_decode()  # Memanggil metode enigma_decode
print(f"Input: {input_text}, Output: {decoded_text}")
