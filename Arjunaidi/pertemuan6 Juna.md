Nama    : Arjunaidi
Nim     : 2355201040
Matkul  : PBO


Polimorfisme :
adalah konsep dalam OOP yang memungkinkan objek dari kelas yang berbeda untuk diakses melalui antarmuka yang sama. 
Dengan kata lain, polimorfisme memungkinkan metode untuk memiliki nama yang sama tetapi perilaku yang berbeda tergantung pada objek yang memanggilnya. 

- Keuntungan Polimorfisme
Fleksibilitas Kode: Polimorfisme memungkinkan penggunaan kode yang lebih fleksibel dan dapat diperluas tanpa harus mengubah banyak bagian dari kode
Reusabilitas: Dengan memanfaatkan polimorfisme, kode dapat digunakan kembali tanpa perlu menulis ulang fungsi atau metode untuk setiap jenis objek.
Mengurangi Kompleksitas: Polimorfisme memungkinkan kode yang lebih sederhana dan terorganisir dengan baik, karena dapat menggunakan metode yang sama pada objek yang berbeda.
               
Contoh Polimorfisme dalam Konteks Lain
Polimorfisme tidak hanya terbatas pada bahasa pemrograman seperti Java atau C++, tetapi juga dapat diterapkan dalam konteks lain seperti sistem basis data dan API.
Dalam banyak kasus, polimorfisme memungkinkan fungsi untuk menangani berbagai jenis data atau objek dengan cara yang seragam, meskipun setiap tipe objek dapat memiliki
implementasi atau perilaku yang berbeda.
Dengan demikian, polimorfisme adalah salah satu pilar utama dari pemrograman berorientasi objek yang memungkinkan pengembangan perangkat lunak yang lebih fleksibel,
modular, dan mudah dikelola.

- Ada dua jenis polimorfisme dalam OOP
Polimorfisme pada waktu kompilasi (Compile-time Polymorphism), yang juga dikenal dengan overloading.
Polimorfisme pada waktu kompilasi terjadi ketika metode atau fungsi yang memiliki nama yang sama dapat memiliki 
implementasi yang berbeda berdasarkan parameter yang diberikan (baik itu jumlah, tipe, atau urutan parameter). 
Hal ini disebut method overloading. Proses pemilihan metode yang tepat dilakukan oleh kompiler pada saat proses 
kompilasi.

Polimorfisme pada waktu eksekusi (Run-time Polymorphism), yang juga dikenal dengan overriding.
Polimorfisme pada waktu eksekusi terjadi ketika sebuah metode yang ada di kelas induk (superclass) 
diganti implementasinya oleh kelas turunan (subclass). Ini disebut method overriding, di mana metode 
yang sama dengan nama dan parameter yang sama, tetapi implementasinya berbeda di subclass.

- Kesimpulan
Polimorfisme memungkinkan kita untuk menulis kode yang lebih modular, fleksibel, dan mudah dipelihara. 
Dengan menggunakan polimorfisme, kita dapat memperlakukan objek yang berbeda dengan cara yang sama, 
meskipun implementasinya berbeda, baik itu dalam bentuk method overloading (compile-time) atau 
method overriding (run-time). Polimorfisme membantu dalam mendesain sistem yang lebih terstruktur dan extensible.



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