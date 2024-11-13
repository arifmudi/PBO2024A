class FileProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lines = []
        self.jumlahKarakter = []

    def baca_file(self):
        try:
            with open(self.file_name, "r") as file:
                self.lines = file.readlines()
            return True
        except FileNotFoundError:
            print("File NotFound : ")
            return False

    def hitung_karakter(self):
        if not self.lines:
            return False
        
        self.jumlahKarakter = [len(line.rstrip('\n')) for line in self.lines]
        return True

    def tulis_hasil(self):
        if not self.jumlahKarakter:
            with open(self.file_name, 'w') as file:
                file.write("NULL\n")
        else:

            min_karakter = min(self.jumlahKarakter)
            max_karakter = max(self.jumlahKarakter)
            rentang = max_karakter - min_karakter

            with open(self.file_name, 'a') as file:
                file.write("\n###########\n")
                file.write(f"Min: {min_karakter} karakter\n")
                file.write(f"Max: {max_karakter} karakter\n")
                file.write(f"Range: {rentang} karakter\n")
        
        print(f"Output berhasil ditulis pada {self.file_name}")

    def proses_file(self):
        if self.baca_file():
            if not self.hitung_karakter():
                with open(self.file_name, 'w') as file:
                    file.write("NULL\n")
            self.tulis_hasil()


if __name__ == "__main__":

    nama_file = input("Masukkan nama file input: ")
    processor = FileProcessor(nama_file)
    processor.proses_file()
    print("Program selesai.")
