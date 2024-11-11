class FileAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.char_counts = []
        self.min_chars = 0
        self.max_chars = 0
        self.range_chars = 0
        self.is_empty = False

    def analyze(self):
        """Membaca file dan menghitung jumlah karakter per baris."""
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
            
            # Cek apakah file kosong atau hanya berisi karakter newline
            if not lines or all(line.strip() == '' for line in lines):
                self.is_empty = True
                return
            
            # Menghitung jumlah karakter per baris tanpa newline
            self.char_counts = [len(line.rstrip('\n')) for line in lines]
            self.max_chars = max(self.char_counts)
            self.min_chars = min(self.char_counts)
            self.range_chars = self.max_chars - self.min_chars
        
        except FileNotFoundError:
            self.handle_file_not_found()
        except Exception as e:
            print(f"Terjadi error: {e}")

    def write_output(self):
        """Menuliskan hasil analisis ke dalam file yang sama atau menambahkan 'NULL' jika kosong."""
        if self.is_empty:
            with open(self.file_name, 'w') as file:
                file.write("NULL\n")
            print(f"Output berhasil ditulis pada {self.file_name}")
            return

        # Menulis hasil ke dalam file yang sama
        with open(self.file_name, 'a') as file:
            file.write("\n........\n")
            file.write("########\n")
            file.write(f"Min: {self.min_chars} karakter\n")
            file.write(f"Max: {self.max_chars} karakter\n")
            file.write(f"Range: {self.range_chars} karakter\n")
            file.write("########\n")

        print(f"Output berhasil ditulis pada {self.file_name}")

    def handle_file_not_found(self):
        """Menangani kasus file tidak ditemukan."""
        print("File tidak ditemukan :(")

# Interaksi dengan pengguna
file_name = input("Masukkan nama file input: ")
analyzer = FileAnalyzer(file_name)
analyzer.analyze()
analyzer.write_output()
input("Program selesai. Tekan enter untuk keluar...")