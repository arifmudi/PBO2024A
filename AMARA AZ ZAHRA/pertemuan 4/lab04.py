class countchars:
def count_chars(filename):
    # Mencoba untuk membuka dan membaca file
    try:
        # Membuka file dalam mode baca
        with open(filename, 'r') as file:
            # Membaca semua baris dari file
            lines = file.readlines()
            
            # Memeriksa apakah file kosong
            if not lines:
                # Jika file kosong, tulis "NULL" ke dalam file
                with open(filename, 'w') as output:
                    output.write("NULL")
                print(f"Output berhasil ditulis pada {filename}")
                return
            
            # Menghitung jumlah karakter per baris (menghilangkan newline)
            char_counts = [len(line.rstrip('\n')) for line in lines]
            
            # Menghitung nilai minimum dan maksimum dari jumlah karakter
            min_chars = min(char_counts)
            max_chars = max(char_counts)
            
            # Menghitung rentang jumlah karakter
            range_chars = max_chars - min_chars
            
            # Menulis hasil perhitungan ke dalam file
            with open(filename, 'a') as output:
                output.write("\n###########\n")  # Menambahkan pemisah
                output.write(f"Min: {min_chars} karakter\n")  # Menulis nilai minimum
                output.write(f"Max: {max_chars} karakter\n")  # Menulis nilai maksimum
                output.write(f"Range: {range_chars} karakter\n")  # Menulis rentang
            
            # Menampilkan pesan bahwa output berhasil ditulis
            print(f"Output berhasil ditulis pada {filename}")
    
    # Menangani exception jika file tidak ditemukan
    except FileNotFoundError:
        print("File tidak ditemukan :(")
    
    # Menangani exception umum lainnya
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    
    # Bagian ini akan selalu dijalankan, baik ada exception atau tidak
    finally:
        print("Program selesai. Tekan enter untuk keluar...")
        input()  # Menunggu input dari pengguna sebelum keluar

# Main program
# Meminta pengguna untuk memasukkan nama file input
filename = input("Masukkan nama file input: ")
# Memanggil fungsi untuk menghitung karakter
count_chars(filename)
