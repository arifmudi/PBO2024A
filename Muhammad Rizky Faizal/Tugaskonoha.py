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

        if not numbers:
            return "minimal masukkan 1 angka"

        total_numbers = sum(numbers)

        decoded_letters = []
        for letter in letters:
            ascii_code = ord(letter)

            if letter.islower():
                shifted_code = ascii_code + total_numbers
                if shifted_code > ord('z'):
                    shifted_code -= 26
            elif letter.isupper():
                shifted_code = ascii_code + total_numbers
                if shifted_code > ord('Z'):
                    shifted_code -= 26

            decoded_letter = chr(shifted_code)
            decoded_letters.append(decoded_letter)

        decoded_text = "".join(decoded_letters)
        return decoded_text

input_text = input("Masukkan nama: ")
decoder = EnigmaDecoder(input_text)
decoded_text = decoder.decode()
print(f"Input: {input_text}")
print(f"Output: {decoded_text}")
