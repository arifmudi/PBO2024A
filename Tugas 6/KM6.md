Nama : M.Abdi Ahzani Nim : 2355201036 Matkul : PBO

-------------------------------------------------------- Polimorfisme --------------------------------------------------------- Polimorfisme adalah konsep dalam OOP yang memungkinkan objek dari kelas yang berbeda untuk diakses melalui antarmuka yang sama. Dengan kata lain, polimorfisme memungkinkan metode untuk memiliki nama yang sama tetapi perilaku yang berbeda tergantung pada objek yang memanggilnya. Ini membantu dalam mengurangi kompleksitas dan meningkatkan fleksibilitas kode.

            example: 
            class Hewan:
                def suara(self):
                    pass

            class Kucing(Hewan):
                def suara(self):
                    return "Meow"

            class Anjing(Hewan):
                def suara(self):
                    return "Bark"

            def cetak_suara(hewan):
                print(hewan.suara())

            #objek dari kelas Kucing dan Anjing
            kucing = Kucing()
            anjing = Anjing()

            #fungsi cetak_suara untuk mencetak suara dari masing-masing hewan
            cetak_suara(kucing)  
            cetak_suara(anjing)  