class EligmaEncryptor:
    def __init__(self, masuk_string):
        self.masuk_string = masuk_string

    def _get_valid_input(self):
        while True:
            self.masuk_string = input("Masukkan pesan Rahasia: ")
            if any(char.isdigit() for char in self.masuk_string):
                break
            else:
                print("Bikin apa sih lu? kasih angka kek.")

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
        self._get_valid_input()
        shift = self._calculate_shift()
        hasil_geser = ''.join(
            self._shift_characters(char, shift) for char in self.masuk_string
        )
        return hasil_geser

pengode = EligmaEncryptor("")
kode_string = pengode.encrypt()
print("Kode Rahasia:", kode_string)