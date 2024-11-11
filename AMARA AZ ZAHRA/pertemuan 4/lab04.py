class FileAnalyzer:
    def __init__(self, filename):
        """Inisialisasi dengan nama file."""
        self.filename = filename

    def count_chars(self):
        """Menghitung jumlah karakter per baris dan menulis hasilnya ke dalam file."""
        try:
            # Membuka file untuk membaca
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            # Memeriksa apakah file kosong
            if not lines:
                # Jika file kosong, menulis "NULL" ke dalam file
                self._write_to_file("NULL")
                print(f"Output berhasil ditulis pada {self.filename}")
                return

            # Menghitung jumlah karakter per baris (menghilangkan newline)
            char_counts = [len(line.rstrip('\n')) for line in lines]

            # Menghitung nilai minimum dan maksimum dari jumlah karakter
            min_chars = min(char_counts)
            max_chars = max(char_counts)

            # Menghitung rentang jumlah karakter
            range_chars = max_chars - min_chars

            # Menulis hasil perhitungan ke dalam file
            result = (
                "\n###########\n"
                f"Min: {min_chars} karakter\n"
                f"Max: {max_chars} karakter\n"
                f"Range: {range_chars} karakter\n"
            )
            self._write_to_file(result)

            print(f"Output berhasil ditulis pada {self.filename}")

        except FileNotFoundError:
            print("File tidak ditemukan :(")
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")
        finally:
            print("Program selesai. Tekan enter untuk keluar...")
            input()  # Menunggu input dari pengguna sebelum keluar

    def _write_to_file(self, content):
        """Menulis konten ke file, baik menambah atau mengganti isi file."""
        with open(self.filename, 'a') as file:
            file.write(content)


# Main program
if __name__ == "__main__":
    # Meminta pengguna untuk memasukkan nama file input
    filename = input("Masukkan nama file input: ")
    
    # Membuat objek dari kelas FileAnalyzer
    analyzer = FileAnalyzer(filename)
    
    # Memanggil metode count_chars untuk menghitung karakter
    analyzer.count_chars()
