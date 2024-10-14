class EligmaDecoder:
    def __init__(self, code):
        self.code = code
        self.total_shift = 0
        self.decrypted_message = []

    def calculate_total_shift(self):
        for char in self.code:
            if char.isdigit():
                self.total_shift += int(char)  
            elif char.isalpha():
                self.decrypted_message.append(char.lower())

    def decrypt_message(self):

        for i in range(len(self.decrypted_message)):
            original_char = self.decrypted_message[i]

            shifted_char = chr((ord(original_char) - ord('a') + self.total_shift) % 26 + ord('a'))

            self.decrypted_message[i] = shifted_char 

        return ''.join(self.decrypted_message) 

    def run(self):
        if not any(char.isdigit() for char in self.code): 
            return "Error: Pesan harus mengandung setidaknya 1 angka."
        self.calculate_total_shift()  
        return self.decrypt_message() 

x = input("Enter Code: ")
decoder = EligmaDecoder(x) 
output = decoder.run()  
print(output) 
