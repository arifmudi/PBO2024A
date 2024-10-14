class Konoha:
    # Fungsi yang dijalankan saat objek dibuat
    def __init__(self, input_string):
        self.input_string = input_string  # Simpan input string
    # Periksa apakah input hanya berisi huruf
        if
        self.input_string.isalpha():
            raise
        ValueError("Input Tidak Memiliki Angka.") #Jika hanya huruf 
        self.shift_value = self.calculate_shift()  # Hitung jumlah angka dalam string

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
        result = []  # Tempat menyimpan hasil dekripsi
        for char in self.input_string:  # Periksa setiap karakter
            if char.isalpha():  # Jika karakter adalah huruf
                shifted_char = self.shift_letter(char, self.shift_value)  # Geser hurufnya
                result.append(shifted_char)  # Simpan hasil geseran
        return ''.join(result)  # Gabungkan semua huruf hasil geseran jadi string

# Contoh penggunaan
input_string = "N2ov5i"  # Input string
eligma = Konoha(input_string)  # Buat objek dengan string input
output = eligma.decrypt()  # Dekripsi string
print(f"Output: {output}")  # Tampilkan hasil dekripsi
