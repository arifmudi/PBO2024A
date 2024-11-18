class EligmaDecoder:
    def __init__(self, code):
        """
        Initialize the decoder with the encoded message.
        
        :param code: The encoded message containing at least one number indicating the total shift amount.
        """
        self.code = code
        self.total_shift = 0
        self.decrypted_message = []

    def calculate_total_shift(self):
        """Calculate the total shift by summing up all numeric characters."""
        for char in self.code:
            if char.isdigit():
                self.total_shift += int(char)
            elif char.isalpha():
                # Append lowercase version of alphabetic characters to decrypted_message
                self.decrypted_message.append(char.lower())

    def decrypt_message(self):
        """Decrypts the message based on calculated total shift."""
        for i in range(len(self.decrypted_message)):
            original_char = self.decrypted_message[i]
            # Calculate shifted character using positive shift for decryption
            shifted_char = chr((ord(original_char) - ord('a') + self.total_shift) % 26 + ord('a'))
            self.decrypted_message[i] = shifted_char 

        return ''.join(self.decrypted_message) 

    def run(self):
        """Run the decoding process, checking if there are numbers present first."""
        if not any(char.isdigit() for char in self.code):
            return "Error: Pesan harus mengandung setidaknya 1 angka."
        
        self.calculate_total_shift()
        return self.decrypt_message() 

# Contoh penggunaan
if __name__ == "__main__":
    x = input("Masukkan: ")
    decoder = EligmaDecoder(x)
    output = decoder.run()
    print(output)