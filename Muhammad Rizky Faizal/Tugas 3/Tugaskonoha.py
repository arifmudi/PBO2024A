class EligmaDecryptor:
    def __init__(self, input_str):
        self.input_str = input_str
        self.jumlah_angka = 0
        self.hasil_dekripsi = ""

    def _hitung_angka_dan_dekripsi(self):
        for char in self.input_str:
            if char.isdigit():
                self.jumlah_angka += int(char)
            elif char.isalpha():
                self.hasil_dekripsi += char

    def decrypt(self):
        self._hitung_angka_dan_dekripsi()

        output = ""
        for char in self.hasil_dekripsi:
            if char.islower():
                geser = (ord(char) - ord('a') + self.jumlah_angka) % 26
                karakter_baru = chr(ord('a') + geser)
            elif char.isupper():
                geser = (ord(char) - ord('A') + self.jumlah_angka) % 26
                karakter_baru = chr(ord('A') + geser)
            
            output += karakter_baru

        return output

input_str = "M13b3yni"
decryptor = EligmaDecryptor(input_str)
print(decryptor.decrypt())
