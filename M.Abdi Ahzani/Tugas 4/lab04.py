class FileCharacterAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """Membaca isi file dan menghitung statistik karakter."""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

                if not lines:  # Jika file kosong
                    print("File kosong. Menambahkan pesan 'NULL'.")
                    self.write_result("NULL\n")
                    return

                # Hitung jumlah karakter per baris
                char_counts = [len(line) for line in lines]
                statistics = self.calculate_statistics(char_counts)

                # Tulis hasil ke file
                self.write_result_to_file(statistics)
                print(f"Output berhasil ditulis pada {self.filename}")

        except FileNotFoundError:
            print("File tidak ditemukan :(")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def calculate_statistics(self, char_counts):
        """Menghitung statistik karakter."""
        min_chars = min(char_counts)
        max_chars = max(char_counts)
        range_chars = max_chars - min_chars
        return min_chars, max_chars, range_chars

    def write_result_to_file(self, statistics):
        """Menambahkan hasil perhitungan ke file input."""
        min_chars, max_chars, range_chars = statistics
        with open(self.filename, 'a') as file:
            file.write("\n###########\n")
            file.write(f"Min: {min_chars} karakter\n")
            file.write(f"Max: {max_chars} karakter\n")
            file.write(f"Range: {range_chars} karakter\n")

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
