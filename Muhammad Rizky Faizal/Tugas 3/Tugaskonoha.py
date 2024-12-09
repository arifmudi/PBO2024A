class Konoha:
    def __init__(self, input_string):
        if not input_string.strip():
            raise ValueError("Input string tidak boleh kosong.")
        self.input_string = input_string
        self.shift_value = 0
        self.validasi_input_string()

    def validasi_input_string(self):
        if not any(char.isdigit() for char in self.input_string):
            print("Input tidak memiliki angka untuk menentukan nilai pergeseran.")
            self.shift_value = None
        else:
            self.shift_value = self.calculate_shift()

    def calculate_shift(self):
        total = sum(int(char) for char in self.input_string if char.isdigit())
        return total

    def shift_letter(self, letter, shift):
        if letter.islower():
            start = ord('a')
            return chr((ord(letter) - start + shift) % 26 + start)
        elif letter.isupper():
            start = ord('A')
            return chr((ord(letter) - start + shift) % 26 + start)
        return letter

    def decrypt(self):
        if self.shift_value is None:
            return "Tidak ada angka, tidak dapat melakukan dekripsi."
        
        result = []
        for char in self.input_string:
            if char.isalpha():
                shifted_char = self.shift_letter(char, self.shift_value)
                result.append(shifted_char)
            else:
                result.append(char)
        return ''.join(result)


input_string = input("Masukkan teks untuk didekripsi: ")
try:
    eligma = Konoha(input_string)
    output = eligma.decrypt()
    print(f"Hasil dekripsi: {output}")
except ValueError as e:
    print(e)
