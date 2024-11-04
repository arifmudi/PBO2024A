class FileCharacterAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """Membaca isi file dan menghitung statistik karakter."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
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
            print("File tidak ditemuk
