class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """Membaca konten file."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                return lines
        except FileNotFoundError:
            print("File tidak ditemukan :(")
            return None
        except Exception as e:
            print("Terjadi kesalahan:", e)
            return None

    def write_output(self, content):
        """Menulis konten ke file."""
        try:
            with open(self.filename, "a") as out_file:
                out_file.write(content)
        except Exception as e:
            print("Terjadi kesalahan saat menulis ke file:", e)

    def process(self):
        """Memproses file sesuai dengan logika yang diberikan."""
        lines = self.read_file()
        
        if lines is None:
            return
        
        # Cek jika file kosong
        if not lines:
            self.write_output("\nNULL")
            print(f"Output berhasil ditulis pada {self.filename}")
            return

        # Menghitung jumlah karakter per baris
        char_counts = [len(line.strip()) for line in lines]
        min_chars = min(char_counts)
        max_chars = max(char_counts)
        range_chars = max_chars - min_chars

        # Menulis output ke file
        output = (
            "\n########\n"
            f"Min: {min_chars} karakter\n"
            f"Max: {max_chars} karakter\n"
            f"Range: {range_chars} karakter\n"
        )
        self.write_output(output)
        print(f"Output berhasil ditulis pada {self.filename}")


# Mengambil nama file dari user dan memprosesnya
filename = input("Masukkan nama file input: ")
processor = FileProcessor(filename)
processor.process()

print("Program selesai. Tekan enter untuk keluar...")
