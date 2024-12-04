class FileCharacterAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def analyze(self):
        """Membaca file, menghitung statistik, dan menulis hasil."""
        try:
            lines = self._read_lines()
            
            if not lines:
                print("File kosong. Menambahkan pesan 'NULL'.")
                self._write_to_file("NULL\n")
                return
            
            # Hitung statistik
            char_counts = [len(line) for line in lines]
            min_chars = min(char_counts)
            max_chars = max(char_counts)
            range_chars = max_chars - min_chars

            # Tulis hasil ke file
            self._write_stats_to_file(min_chars, max_chars, range_chars)
            print(f"Output berhasil ditulis pada {self.filename}")
        
        except FileNotFoundError:
            print("File tidak ditemukan :(")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def _read_lines(self):
        """Membaca semua baris dalam file."""
        with open(self.filename, 'r') as file:
            return file.readlines()

    def _write_stats_to_file(self, min_chars, max_chars, range_chars):
        """Menulis hasil perhitungan ke file input."""
        content = (
            "\n###########\n"
            f"Min: {min_chars} karakter\n"
            f"Max: {max_chars} karakter\n"
            f"Range: {range_chars} karakter\n"
        )
        self._write_to_file(content)

    def _write_to_file(self, content):
        """Menambahkan konten ke file."""
        with open(self.filename, 'a') as file:
            file.write(content)

# Fungsi utama untuk menjalankan program
def main():
    filename = input("Masukkan nama file input: ")
    analyzer = FileCharacterAnalyzer(filename)
    analyzer.analyze()
    input("Program selesai. Tekan enter untuk keluar...")

if __name__ == "__main__":
    main()
