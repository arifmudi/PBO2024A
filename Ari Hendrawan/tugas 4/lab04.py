import os

class CharacterCounter:
    def __init__(self, filename):
        self.filename = filename
        self.min_char_count = float('inf')
        self.max_char_count = float('-inf')

    def count_characters(self):
        try:
            with open(self.filename, 'r') as in_file:
                lines = in_file.readlines()
        except FileNotFoundError:
            print("File tidak ditemukan :(")
            return
        
        if not lines or all(line.strip() == "" for line in lines):
            with open(self.filename, 'w') as out_file:
                out_file.write("NULL")
            return
        
        for line in lines:
            stripped_line = line.rstrip('\n')
            char_count = len(stripped_line)
            
            if char_count < self.min_char_count:
                self.min_char_count = char_count
            if char_count > self.max_char_count:
                self.max_char_count = char_count
        
        range_value = self.max_char_count - self.min_char_count
        
        output_string = "\n... Isi dari berkas {} sebelumnya ...\n".format(os.path.basename(self.filename))
        output_string += "###########\n"
        output_string += f"Min: {self.min_char_count} karakter\n"
        output_string += f"Max: {self.max_char_count} karakter\n"
        output_string += f"Range: {range_value} karakter\n"
        
        with open(self.filename, 'a') as out_file:
            out_file.write(output_string)

    def run(self):
        while True:
            in_filename = input("Masukkan nama file input (ketik 'exit' untuk berhenti): ")
            if in_filename.lower() == 'exit':
                break
            self.filename = in_filename
            self.min_char_count = float('inf')
            self.max_char_count = float('-inf')
            self.count_characters()
            print(f"Output berhasil ditulis pada {self.filename}")
            input("Tekan enter untuk melanjutkan...")

if __name__ == "__main__":
    counter = CharacterCounter("")
    counter.run()