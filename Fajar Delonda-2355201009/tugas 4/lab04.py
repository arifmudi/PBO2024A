#                           CF2                                     #
class IOException:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
        self.char_counts = []
        self.min_chars = None
        self.max_chars = None
        self.char_range = None

        try:
            self.read_file()
            if not self.lines:
                self.write_null()
            else:
                self.calculate_stats()
                self.write_output()
        except FileNotFoundError:
            print("File tidak ditemukan :(")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
        else:
            print(f"Output berhasil ditulis pada {self.filename}")
        finally:
            input("Program selesai. Tekan enter untuk keluar...")

    def read_file(self):
        # Membaca isi file dan menyimpan setiap baris ke dalam list self.lines.
        # Menghitung jumlah karakter per baris dan menyimpannya dalam self.char_counts. 
        with open(self.filename, "r") as in_file:
            self.lines = in_file.readlines()
            self.char_counts = [len(line.rstrip('\n')) for line in self.lines]  # Menghapus \n

    def calculate_stats(self):
        # Menghitung nilai minimum, maksimum, dan rentang dari jumlah karakter per baris.
        self.min_chars = min(self.char_counts)
        self.max_chars = max(self.char_counts)
        self.char_range = self.max_chars - self.min_chars

    def write_output(self):
        # Menulis hasil perhitungan (min, max, range) ke dalam file yang sama tanpa menghilangkan isi sebelumnya.
        with open(self.filename, "a") as out_file:
            out_file.write("###########\n")
            out_file.write(f"Min: {self.min_chars} karakter\n")
            out_file.write(f"Max: {self.max_chars} karakter\n")
            out_file.write(f"Range: {self.char_range} karakter\n")

    def write_null(self):
        # Menulis 'NULL' ke dalam file jika file kosong.
        with open(self.filename, "w") as out_file:
            out_file.write("NULL\n")
        print("File tidak berisi teks. Ditulis 'NULL' ke dalam file.")

def main():
    in_filename = input("Masukkan nama file input: ")
    IOException(in_filename)

if __name__ == "__main__":
    main()
