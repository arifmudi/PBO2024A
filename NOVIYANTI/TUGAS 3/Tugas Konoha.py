class Konoha:
    # Fungsi yang dijalankan saat objek dibuat
    def __init__(self, input_string):
        if not input_string:  # Cek apakah input string kosong
            raise ValueError("Input string tidak boleh kosong.")
        self.input_string = input_string  # Simpan input string
        self.shift_value = 0  # Nilai pergeseran awal
        self.validasi_input_string()  # Validasi input string

    # Fungsi untuk validasi input string
    def validasi_input_string(self):
        if not any(char.isdigit() for char in self.input_string):
            print("Tidak memiliki angka.")  # Cetak pesan jika tidak ada angka
            self.shift_value = None  # Set nilai pergeseran menjadi None untuk menghentikan dekripsi
        else:
            self.shift_value = self.calculate_shift()  # Hitung nilai pergeseran hanya jika ada angka

    # Fungsi untuk menghitung total dari semua angka dalam string
    def calculate_shift(self):
        total = sum(int(char) for char in self.input_string if char.isdigit())  # Jumlahkan semua angka
        return total  # Kembalikan hasil jumlahnya

    # Fungsi untuk menggeser huruf sesuai jumlah shift
    def shift_letter(self, letter, shift):
        if letter.islower():  # Jika huruf kecil
            start = ord('a')  # Nilai ASCII untuk 'a'
            return chr((ord(letter) - start + shift) % 26 + start)  # Geser huruf dan jaga tetap dalam alfabet
        elif letter.isupper():  # Jika huruf besar
            start = ord('A')  # Nilai ASCII untuk 'A'
            return chr((ord(letter) - start + shift) % 26 + start)  # Geser huruf besar
        return letter  # Kembalikan huruf apa adanya jika bukan alfabet

    # Fungsi untuk mendekripsi string dengan menggeser huruf
    def decrypt(self):
        if self.shift_value is None:  # Cek jika tidak ada angka dan shift_value adalah None
            return  # Tidak melakukan apapun jika tidak ada angka
        result = []  # Tempat menyimpan hasil dekripsi
        for char in self.input_string:  # Periksa setiap karakter
            if char.isalpha():  # Jika karakter adalah huruf
                shifted_char = self.shift_letter(char, self.shift_value)  # Geser hurufnya
                result.append(shifted_char)  # Simpan hasil geseran
            # Abaikan angka dalam output hasil dekripsi
        return ''.join(result)  # Gabungkan semua huruf hasil geseran jadi string

# Contoh penggunaan
input_string = "nnnn"  # Input string tanpa angka
eligma = Konoha(input_string)  # Buat objek dengan string input
output = eligma.decrypt()  # Dekripsi string (atau tidak, jika tidak ada angka)
if output:  # Tampilkan hasil dekripsi jika ada
    print(f"Output: {output}")
