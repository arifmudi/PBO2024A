#                   CF2                             #

# Membuka dan Menutup File

# IMPORTANT 
# Mode "r" sebagai membaca
# Mode "W" sebagai Mengetik

# open ()
in_file = open("yumeko.txt", "r") #perintah untuk membuka file

isi = in_file.read() #memanggil untuk membuka file dan termasuk karakter newline/garis baru (\n)

print(isi)
in_file.close() #perintah untuk menutup file

# with open()
with open("yumeko.txt", "r") as in_file: #membuka aksen dengan with dan tidak bisa mengakses melalui in_file
    isi = in_file.readlines() #memanggil untuk membuka file dan termasuk karakter newline tetapi memunculkan karakter dan extension terminal

print(isi)
in_file.close()

# use for
with open("yumeko.txt", "r") as in_file:
    for line in in_file: 
        print(line)

# use out write
with open("WahyuMina.txt", "w") as out_file:
    out_file.write('Hello My Name WahyuMina. \n')
    out_file.write('WahyuMina is here in file Txt:3.\n')


# Exeception
try : 
 # Baris-baris kode yang berpeluang menghasilkan Exception
 raise Exception("Ini Pesan Exception")
except Exception as e:
 print("Terdapat Exception dengan pesan", e)
else : # Opsional
 print("Program berjalan tanpa exception")
finally : # Opsional
 print("Dijalankan baik dengan maupun tanpa exception")

# raise exception
try:
    nilai = int(input("Masukkan angka: "))
    if nilai < 0:
        raise Exception("Angka tidak boleh negatif")
    print("Angka yang dimasukkan adalah:", nilai)
except Exception as e:
    print(f"Error: {e}")

#Beberapa jenis exception yang terdapat di Python adalah
# 1. AssertionError: Dipanggil ketika tidak memenuhi statement assert 
# (statement assert bernilai False)
# 2. TypeError: Dipanggil ketika tipe data tidak sesuai
# 3. ValueError: Dipanggil ketika value / nilai data tidak sesuai
# 4. ZeroDivisionError: Dipanggil ketika terdapat pembagian dengan angka nol
# 5. NameError: Dipanggil ketika suatu nama variabel tidak dikenal / belum diinisialisasi



