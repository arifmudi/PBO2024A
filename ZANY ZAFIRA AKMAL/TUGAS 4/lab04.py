def process_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
            # Cek jika file kosong
            if not lines:
                with open(filename, "a") as out_file:
                    out_file.write("\nNULL")
                print(f"Output berhasil ditulis pada {filename}")
                return
            
            # Menghitung jumlah karakter per baris
            char_counts = [len(line.strip()) for line in lines]
            min_chars = min(char_counts)
            max_chars = max(char_counts)
            range_chars = max_chars - min_chars
            
            # Menulis output ke file
            with open(filename, "a") as out_file:
                out_file.write("\n########\n")
                out_file.write(f"Min: {min_chars} karakter\n")
                out_file.write(f"Max: {max_chars} karakter\n")
                out_file.write(f"Range: {range_chars} karakter\n")
            
            print(f"Output berhasil ditulis pada {filename}")
    
    except FileNotFoundError:
        print("File tidak ditemukan :(")
    except Exception as e:
        print("Terjadi kesalahan:", e)

# Mengambil nama file dari user
filename = input("Masukkan nama file input: ")
process_file(filename)
print("Program selesai. Tekan enter untuk keluar...")
