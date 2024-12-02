class FileCharacterAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.min_chars = None
        self.max_chars = None
        self.range_chars = None

    def read_file(self):
        """Membaca isi file dan menghitung statistik karakter."""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                
                if not lines:  # Jika file kosong
                    print("File kosong. Menambahkan pesan 'NULL'.")
                    self.write_result("NULL\n")
                    return

                # Hitung jumlah karakter per baris (termasuk baris kosong)
                char_counts = [len(line) for line in lines]
                self.min_chars = min(char_counts)
                self.max_chars = max(char_counts)
                self.range_chars = self.max_chars - self.min_chars

                # Tulis hasil ke file
                self.write_result_to_file()
                print(f"Output berhasil ditulis pada {self.filename}")
        
        except FileNotFoundError:
            print("File tidak ditemukan :(")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def write_result_to_file(self):
        """Menambahkan hasil perhitungan ke file input."""
        with open(self.filename, 'a') as file:
            file.write("\n###########\n")
            file.write(f"Min: {self.min_chars} karakter\n")
            file.write(f"Max: {self.max_chars} karakter\n")
            file.write(f"Range: {self.range_chars} karakter\n")

    def write_result(self, message):
        """Menulis pesan ke file, misalnya NULL untuk file kosong."""
        with open(self.filename, 'a') as file:
            file.write(message)

# Fungsi utama untuk menjalankan program
def main():
    filename = input("Masukkan nama file input: ")
    analyzer = FileCharacterAnalyzer(filename)
    analyzer.read_file()
    input("Program selesai. Tekan enter untuk keluar...")

if __name__ == "__main__":
    main()