import os

# Membuat file input jika belum ada
def create_input_files():
    file_contents = {
        "in0.txt": "",
        "in1.txt": "pagi ini sangat cerah.\n",
        "in2.txt": "nama saya noviyanti.\nsaya prodi teknik informatika.\n",
        "in3.txt": "baris pertama.\nbaris kedua.\nbaris ketiga.\n"
    }

    for filename, content in file_contents.items():
        if not os.path.exists(filename):
            with open(filename, "w") as file:
                file.write(content)
    print("File in0.txt, in1.txt, in2.txt, dan in3.txt telah berhasil dibuat atau sudah ada sebelumnya.")

# Kelas IOException untuk membaca, menghitung, dan menulis statistik file
class IOException:
    def __init__(self, filename):
        # Menginisialisasi kelas IOException dengan nama file
        # dan mengatur variabel yang diperlukan untuk pemrosesan.
        self.filename = filename
        self.lines = []          # Menyimpan setiap baris dari file
        self.char_counts = []    # Menyimpan jumlah karakter di setiap baris
        self.min_chars = None    # Menyimpan jumlah karakter minimum di semua baris
        self.max_chars = None    # Menyimpan jumlah karakter maksimum di semua baris
        self.char_range = None   # Menyimpan rentang jumlah karakter

        try:
            # Mencoba membaca file dan memproses data
            self.read_file()
            
            # Mengecek apakah file kosong (tidak ada baris), tulis 'NULL' jika kosong
            if not self.lines:
                self.write_null()
            else:
                # Jika file memiliki konten, hitung statistik dan tulis output
                self.calculate_stats()
                self.write_output()
        except FileNotFoundError:
            # Jika file tidak ditemukan, menampilkan pesan kesalahan
            print("File tidak ditemukan :(")
        except Exception as e:
            # Untuk kesalahan lain yang tidak terduga, menampilkan pesan kesalahan
            print(f"Terjadi kesalahan: {e}")
        else:
            # Jika tidak ada kesalahan, mengonfirmasi bahwa output berhasil ditulis
            print(f"Output berhasil ditulis pada {self.filename}")
        finally:
            # Memastikan pesan ini selalu muncul, baik ada atau tidak ada kesalahan
            input("Program selesai. Tekan enter untuk keluar...")

    def read_file(self):
        # Membaca isi file dan menyimpan setiap baris di self.lines.
        # Menghitung jumlah karakter di setiap baris (menghilangkan karakter newline).
        with open(self.filename, "r") as in_file:
            self.lines = in_file.readlines()  # Membaca semua baris ke dalam list
            self.char_counts = [len(line.rstrip('\n')) for line in self.lines]  # Menghitung karakter di tiap baris

    def calculate_stats(self):
        # Menghitung nilai minimum, maksimum, dan rentang karakter di setiap baris.
        self.min_chars = min(self.char_counts)          # Mendapatkan jumlah karakter minimum
        self.max_chars = max(self.char_counts)          # Mendapatkan jumlah karakter maksimum
        self.char_range = self.max_chars - self.min_chars  # Menghitung rentang antara max dan min

    def write_output(self):
        # Menambahkan hasil perhitungan statistik (min, max, range) di akhir file.
        with open(self.filename, "a") as out_file:
            out_file.write("###########\n")                     # Memisahkan konten asli dengan output
            out_file.write(f"Min: {self.min_chars} karakter\n") # Menulis jumlah karakter minimum
            out_file.write(f"Max: {self.max_chars} karakter\n") # Menulis jumlah karakter maksimum
            out_file.write(f"Range: {self.char_range} karakter\n") # Menulis rentang karakter

    def write_null(self):
        # Menulis 'NULL' ke file jika file kosong.
        with open(self.filename, "w") as out_file:
            out_file.write("NULL\n")  # Menunjukkan bahwa tidak ada konten yang ditemukan
        print("File tidak berisi teks. Ditulis 'NULL' ke dalam file.")

def main():
    # Membuat file input jika belum ada
    create_input_files()

    # Meminta pengguna untuk memasukkan nama file dan menginisialisasi IOException dengan nama tersebut.
    in_filename = input("Masukkan nama file input: ")
    IOException(in_filename)

# Menjalankan fungsi main jika script dijalankan langsung.
if __name__ == "__main__":
    main()
