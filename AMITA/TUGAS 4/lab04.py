def process_file(filename):
    try:
        with open(filename, 'r') as in_file:
            lines = in_file.readlines()

            if not lines:
                # Jika file kosong, tulis "NULL" ke file
                with open(filename, 'w') as out_file:
                    out_file.write("NULL\n")
                print("Output berhasil ditulis pada", filename)
                return

            # Hitung jumlah karakter per baris
            char_counts = [len(line.rstrip('\n')) for line in lines]
            min_chars = min(char_counts)
            max_chars = max(char_counts)
            char_range = max_chars - min_chars

            # Menuliskan hasil ke dalam file, beserta isi file sebelumnya
            with open(filename, 'a') as out_file:
                out_file.write("\n###########\n")
                out_file.write(f"Min: {min_chars} karakter\n")
                out_file.write(f"Max: {max_chars} karakter\n")
                out_file.write(f"Range: {char_range} karakter\n")

            print("Output berhasil ditulis pada", filename)

    except FileNotFoundError:
        print("File tidak ditemukan :(")

# Meminta nama file input dari pengguna nama file
file_input = input("Masukkan nama file input: ")
process_file(file_input)
print("Program selesai. Tekan enter untuk keluar...")
input()