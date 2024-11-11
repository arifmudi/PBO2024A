class FileProcessor:
    def __init__(self, filename):
        # Inisialisasi objek dengan nama file
        self.filename = filename

    def process_file(self):
        """Memproses file untuk menghitung karakter per baris dan menulis hasil analisis ke dalam file."""
        try:
            # Membuka file dalam mode baca
            with open(self.filename, 'r') as in_file:
                lines = in_file.readlines()  # Membaca semua baris dalam file

                if not lines:
                    # Jika file kosong, tulis "NULL" ke file
                    with open(self.filename, 'w') as out_file:
                        out_file.write("NULL\n")
                    print("Output berhasil ditulis pada", self.filename)
                    return

                # Menghitung jumlah karakter per baris tanpa newline di akhir
                char_counts = [len(line.rstrip('\n')) for line in lines]
                min_chars = min(char_counts)  # Karakter minimum di antara baris
                max_chars = max(char_counts)  # Karakter maksimum di antara baris
                char_range = max_chars - min_chars  # Rentang karakter

                # Menambahkan hasil analisis ke file yang sama
                with open(self.filename, 'a') as out_file:
                    out_file.write("\n###########\n")  # Menambahkan pemisah
                    out_file.write(f"Min: {min_chars} karakter\n")  # Menulis karakter minimum
                    out_file.write(f"Max: {max_chars} karakter\n")  # Menulis karakter maksimum
                    out_file.write(f"Range: {char_range} karakter\n")  # Menulis rentang karakter

                print("Output berhasil ditulis pada", self.filename)

        except FileNotFoundError:
            # Menangani kasus jika file tidak ditemukan
            print("File tidak ditemukan :(")


# Meminta nama file input dari pengguna
file_input = input("Masukkan nama file input: ")  # Input nama file dari pengguna
processor = FileProcessor(file_input)  # Membuat objek FileProcessor dengan nama file
processor.process_file()  # Memproses file sesuai dengan metode yang ditentukan
print("Program selesai. Tekan enter untuk keluar...")
input()  # Menunggu pengguna menekan enter untuk keluar
