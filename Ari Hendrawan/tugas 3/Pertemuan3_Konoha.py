class EligmaEncryptor:
    def __init__(self, masuk_string):
        self.masuk_string = masuk_string

    def _extract_digits(self):
        return [int(char) for char in self.masuk_string if char.isdigit()]

    def _calculate_shift(self):
        digits = self._extract_digits()
        return sum(digits) if digits else 0

    def _shift_characters(self, char, shift):
        if char.islower():
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            return ''

    def encrypt(self):
        shift = self._calculate_shift()
        hasil_geser = ''.join(
            self._shift_characters(char, shift) for char in self.masuk_string
        )
        return hasil_geser

def get_valid_input():
    while True:
        masuk_string = input("Masukkan pesan Rahasia: ")
        if any(char.isdigit() for char in masuk_string):
            return masuk_string
        else:
            print("Bikin apa sih lu? kasih angka kek.")

masuk_string = get_valid_input()
pengode = EligmaEncryptor(masuk_string)
kode_string = pengode.encrypt()
print("Kode Rahasia:", kode_string)