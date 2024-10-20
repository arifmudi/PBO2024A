class EligmaDecryptor:
    def __init__(self, message):
        self.message = message
        self.shift_value = 0

    def validate_message(self):
        if not any(char.isdigit() for char in self.message):
            raise ValueError("Bikin Apasih lu? Kasih angka kek.")

    def calculate_shift(self):
        self.shift_value = sum(int(char) for char in self.message if char.isdigit())

    def decrypt(self):
        decrypted_message = ""
        for char in self.message:
            if char.isalpha():
                shift = self.shift_value % 26
                if char.islower():
                    decrypted_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    decrypted_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif not char.isdigit(): 
                decrypted_message += char
        return decrypted_message

input_message = input("Masukkan Kode Rahasia : ")
decryptor = EligmaDecryptor(input_message)

try:
    decryptor.validate_message()
    decryptor.calculate_shift()
    result = decryptor.decrypt()
    print("Isi pesannya:", result)
except ValueError as e:
    print(e)