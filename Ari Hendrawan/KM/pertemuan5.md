Nama    : Ari Hendrawan
Nim     : 2355201034
Matkul  : PBO

-------------------------------------------------------- Konsep Single Inheritance ---------------------------------------------------------
Single Inheritance atau Pewarisan Tunggal merupakan bentuk pewarisan dalam pemograman berorientasi objek, yang dimana sebuah class anak hanya mewarisi satu dari class induk. konsep dari single inheritance memungkinkan sub class atau class anak untuk mengakses atribut dan metode yang didefinisikan dalam class induk, sehingga nantinta dapat memudahkan kembali penggunaan kode dan memperluas fungsional tanpa harus menulis kembali kode yang sama.

Single inheritance dapat digunakan di tiap kondisi tertentu, contihnya pada ketika:

*Hierarki Kelas Sederhana*
Single Inheritance dipakai ketika hubungan antar kelas tidak kompleks dan hanya perlu satu tingkatan level pewarisan.

*Penggunaan ulang kode*
Single Inhertance dipakai ketika ingin memanfaatkan kembali kode dari sebuah class induk tanpa adanya tambahan kompleksitas.

*Spesialisasi*
Single Inheritance dipakai ketika sebuah subclass perlu untuk menambahkan atau mengubah sebuah perilaku dari superclass tanpa terjadinya kebingungan interaksi yang mungkin terjadi dengan multiple inheritance.

*Implmentasi single inheritance*
        #buat class induk
        class Hewan:
            def bicara(self):
                print("Hewan bersuara")

        #class anak mewarisi class induk
        class anjing(Hewan):
            def begokgok(self):
                print("BEGOKGOK!!! BEGOKGOK!!!")

        #Membuat objek dari class anjing
        anjing = anjing()
        anjing.bicara()  #akses metode class induk
        anjing.begokgok()   #akses metode class anak

PENJELASAN SINGKAT :
    1. class induk 'Hewan' didefinisikan dengan metode 'bicara' yang mencetak string
    2. class anak 'anjing' melakukan pewarisan dari 'hewan' dan mempunyai penambahan metode 'begokgok'
    3. objek 'anjeng' dapat melakukan akses metode 'bicara' dari class induk dan metode 'begokgok' dari class anak

    
-------------------------------------------------------- Konsep Super Inheritance ---------------------------------------------------------
Konsepd super() dalam python adalah sebuah fungsi yang dipakai untuk melakukan akses method dan atribut dari class induk (superclass). dalam konteks inheritance, cara ini lumayan berguna jika ingin memanggil konstruktor atau method dari class induk dalam subclass, sehingga dapat memanfaatkan fungsionalitas yang telah ada sebelumnya.

penggunaan super inheritance memiliki beberapa manfaat :
    1. *menghindari pengulangan kode*, penggunaan super dapat melakukan pemanggilan konstruktor class induk, sehingga menghindari penulisan kode berulang.
    2. *mendukung multiple inheritance*, suoer yang difungsikan dengan baik memastikann metode digunakan dengan benar dan sesuai demgan method.
    3. *memudahkan pemeliharaan*, sewaktu adanya perubahan pada class induk, penggunaan supe memungkinkan bahwa subclass tetap mendapatkan pembaruan tanpa harus melakukan banyak perubahan kode di banyak tempat.

penggunaan super inheritance dapat digunakan jika pada saat membuat sebuah subclass yang memrlukan konstruktor atau metode dari superclass. jika ingin memastikan semua inisial dari superclass dibutuhkan, perlu dilakukan sebelum menambahkan logic yang spesifik dari subclass. mengapa super dibutuhkan? fungsi super inheritance dibutuhkan untuk memastikan adanya perbahan superclass tercermin secara otomatis pada subclass dan juga untuk memudahkan pengelolaan dan oemeliharaan kode hierarki yang kompleks.

    #Kelas Induk
    class Kendaraan:
        def __init__(self, merek, tahun):
            self.merek = merek
            self.tahun = tahun

        def info(self):
            return f"Kendaraan laut: {self.merek}, Tahun: {self.tahun}"

    #Kelas Anak
    class kapal(Kendaraan):
        def __init__(self, merek, tahun, tipe):
            super().__init__(merek, tahun)  # Memanggil konstruktor kelas induk
            self.tipe = tipe

        def info(self):
            return f"{super().info()}, Tipe: {self.tipe}"

    #Membuat objek dari kelas kapal
    kapal_saya = kapal("Budiono Siregar", 2024, "Kapal Lawut")
    print(kapal_saya.info()) 

-------------------------------------------------------- Jenis jenis inheritance ---------------------------------------------------------
    1. *Multiple Inheritance*
    Kelas anak mewarisi dari lebih dari satu kelas induk. Ini memungkinkan akses ke atribut dan metode dari semua kelas induk yang terlibat. Namun, dapat menyebabkan kebingungan jika ada metode dengan nama yang sama di kelas induk.

            class mamal:
                def mamalia_info(self):
                    print("Mamalia bisa melahirkan")

            class Hewansayap:
                def info_hewan_sayap(self):
                    print("mamalia bersayap bisa terbang")

            class Bat(amal, Hewansayap):
                pass

            # Membuat objek dari kelas Bat
            b1 = Kelelawar()
            b1.mamalia_info()         
            b1.info_hewan_sayap()   

    2. *multilvel Inheritance*
    Kelas anak mewarisi dari kelas induk yang juga merupakan turunan dari kelas lain. Ini membentuk rantai pewarisan, di mana subclass dapat mewarisi perilaku dari superclass dan juga dari kelas induk lainnya.

            class hewanlaut:
                def suara(self):
                    print("hewan bersuara")

            class ikan(hewanlaut):
                def blub(self):
                    print("ikan blublub")

            class paus(ikan):
                def berenang(self):
                    print("paus berenang")

    3. *hierarchical Inheritance*
    Beberapa subclass mewarisi dari satu superclass yang sama. Ini memungkinkan berbagai subclass untuk berbagi atribut dan metode dari superclass, memudahkan pengelolaan kode yang memiliki kesamaan.

                class kendaraan:
                    def start(self):
                        print("kendaraan mulai")

                class mobil(kendaraan):
                    def kemudi(self):
                        print("mobil mengemudi")

                class motor(kendaraan):
                    def kendara(self):
                        print("motor mengendara")

                mobil = mobil()
                mobil.start()  
                mobil.kemudi()  

                motor = motor()
                motor.start()  
                motor.kendara()   

    4. *Hybrid Inheritance*
    Kombinasi dari dua atau lebih jenis inheritance di atas. Ini menciptakan struktur yang lebih kompleks dan fleksibel, memungkinkan pengembang untuk menggabungkan berbagai pola pewarisan sesuai kebutuhan aplikasi.

                class hewan:
                    def makan(self):
                        print("memakan")

                class mamalia(hewan):
                    def gerak(self):
                        print("berjalan")

                class hewansayap(hewan):
                    def udara(self):
                        print("terbang")

                class kelelawar(mamalia, udara):  
                    def ekolokasi(self):
                        print("menggunnakan ekolokasi")


+---------------------------+-------------------------------------------------------+---------------------------------------------------+
|   Jenis                   |   Deskripsi                                           |   Contoh Penggunaan                               |
|   Inheritance             |                                                       |                                                   |
+---------------------------+-------------------------------------------------------+---------------------------------------------------+
|                           |                                                       |                                                   |
|    Multiple               |     Kelas anak mewarisi dari lebih dari satu          |   kelas kelelawar mewarisi 'mamal' dan            |
|    Inheritance            |     kelas induk.                                      |   'hewansayap'                                    |
|                           |                                                       |                                                   |
+---------------------------+-------------------------------------------------------+---------------------------------------------------+
|                           |                                                       |                                                   |
|    Hierarchical           |     Kelas anak mewarisi dari kelas induk yang juga    |   kelas 'paus' mewarisi 'ikan' dan                |
|    Inheritance            |     merupakan turunan dari kelas lain.                |   yang mewarisi 'hewanlaut'                       |
|                           |                                                       |                                                   |
+---------------------------+-------------------------------------------------------+---------------------------------------------------+
|                           |                                                       |                                                   |
|    Hierarchical           |     Beberapa subclass mewarisi dari satu              |   kelas 'mobil' dan 'mtor' mewarisi kelas         |
|    Inheritance            |     superclass yang sama.                             |   'kendaraan'                                     |
|                           |                                                       |                                                   |
+---------------------------+-------------------------------------------------------+---------------------------------------------------+
|                           |                                                       |                                                   |
|    Hybird                 |     Kombinasi dari dua atau lebih jenis               |   kelas 'kelelawar' mewarisi kelas 'mamalia'      |
|    Inheritance            |     inheritance di atas.                              |   dan 'udara'                                     |
|                           |                                                       |                                                   |
+---------------------------+-------------------------------------------------------+---------------------------------------------------+

-------------------------------------------------------- konsep overiding method ---------------------------------------------------------
Overiding Method merupakan fitur dalam sebuah pemograman yang memungkinkan subclass untuk didefinisikan ulang metode yang telah didefinisikan dalam superclass. penggunakan motode ini dapat menberikan implementasi yang lebih spesifik dan berbeda dari metode yang diwarisi

metode ini memiliki beberapa manfaat penggunaan :
    1. *Kustomisasi perilaku*, subclass dapoat mengubah perilaku metode yang diwarisi agar dapat sesuai dengan kebutuhan spesifiknya.
    2. *Penggunaan kembali kode*, subclass yang melakukan pengubahan kode tetap dapat memanggil metode superclass sehingga dapat dimungkinkan menggunkan kembali kode yang sudah ada.
    3. *polimorfisme*, overriding mendukung polimorfisme, dimana tiap metode yang sama dapat berpelilaku berbeda tergantung pada objek yang dipanggil. 

            #Kelas Induk
            class Karyawan:
                def print_data(self):
                    print("Ini merupakan data karyawan.")

            #Kelas Anak
            class Dosen(Karyawan):
                def print_data(self):  
                    print("Ini data dosen.")

            #Membuat objek dari kelas Karyawan dan Dosen
            karyawan1 = Karyawan()
            karyawan2 = Dosen()

            karyawan1.print_data()  
            karyawan2.print_data()  

-------------------------------------------------------- Inheritance dan Non-Inheritance ---------------------------------------------------------
Kapan Menggunakan Pewarisan (Inheritance)
    1. Hubungan "Is-A": Gunakan pewarisan ketika ada hubungan yang jelas antara kelas induk dan kelas anak, di mana kelas anak merupakan spesialisasi dari kelas induk. Contohnya, Mobil adalah jenis dari Kendaraan.
    2. Penggunaan Kembali Kode: Pewarisan memungkinkan subclass untuk mewarisi metode dan atribut dari superclass, sehingga mengurangi pengulangan kode dan memudahkan pemeliharaan.
    3. Polimorfisme: Jika Anda ingin menggunakan polimorfisme, di mana objek dari subclass dapat digunakan di tempat objek dari superclass, pewarisan adalah pilihan yang tepat.
Hierarki Kelas: Ketika Anda perlu membuat hierarki kelas yang terstruktur, pewarisan membantu dalam mendefinisikan hubungan antar kelas dengan jelas.

Kapan Menggunakan Non-Pewarisan (Non-Composition)
    1. Hubungan "Has-A": Gunakan komposisi ketika ada hubungan di mana satu objek memiliki objek lain sebagai bagian dari dirinya. Misalnya, Mobil memiliki Mesin. Ini lebih fleksibel daripada pewarisan.
    2. Fleksibilitas dan Pemisahan Tanggung Jawab: Komposisi memungkinkan Anda untuk mengubah perilaku objek tanpa mengubah hierarki kelas. Ini sangat berguna dalam desain sistem yang kompleks.
    3. Menghindari Masalah Pewarisan Ganda: Dalam beberapa bahasa pemrograman, pewarisan ganda dapat menyebabkan konflik jika dua superclass memiliki metode dengan nama yang sama. Komposisi menghindari masalah ini dengan mengandalkan agregasi.
    4. Sederhana dan Mudah Dipahami: Dalam beberapa kasus, menggunakan komposisi lebih sederhana dan lebih mudah dipahami dibandingkan dengan membuat hierarki kelas yang kompleks.

    ------------------------------------------------------------------------ study kasus -----------------------------------------------------------------------------

    Budiono Siregar seorang bocah SD yang sedang bermimpi untuk menjelajahi lautan. suatu hari Budiono Siregar didapatin oleh seorang konten kreator cita cita, siregar ditanya apa cita citanya ketika menjadi dewasa kelak. dengan lantang Budiono Siregar menjawab dia ingin menjadi sebuah "kapal Lawut".

    hingga suatu hari, ketika Budiono Siregar sedang memikirkan kembali impian nya dia terpikirkan banyaknya jenis kapal laut yang di dunia yang luas ini. sehingga Budiono siregar mempunyai ide untuk membuat kode python tentang jenis jenis kapal laut yang dia suka.

    pada kode python tersebut budiono siregar mengelompok kan jenis jenis kapal laut diantaranya kapal cargo, kapal tempur, kapal ikan, kapal penumpang. isi dari kode nya berisi seputar jenis kapal, tahun dibuatnya, dan total muatannya.

    kode python :
    
            # class Kapal
            class Kapal:
                def __init__(self, jenis, tahun_dibuat, total_muatan):
                    self.jenis = jenis
                    self.tahun_dibuat = tahun_dibuat
                    self.total_muatan = total_muatan

                def info(self):
                    return f"Jenis Kapal: {self.jenis}, Tahun Dibuat: {self.tahun_dibuat}, Total Muatan: {self.total_muatan} ton"


            # class Kapal Cargo
            class KapalCargo(Kapal):
                def __init__(self, tahun_dibuat, total_muatan):
                    super().__init__("Kapal Cargo", tahun_dibuat, total_muatan)


            # class Kapal Tempur
            class KapalTempur(Kapal):
                def __init__(self, tahun_dibuat, total_muatan):
                    super().__init__("Kapal Tempur", tahun_dibuat, total_muatan)


            # class Kapal Ikan
            class KapalIkan(Kapal):
                def __init__(self, tahun_dibuat, total_muatan):
                    super().__init__("Kapal Ikan", tahun_dibuat, total_muatan)


            # class Kapal Penumpang
            class KapalPenumpang(Kapal):
                def __init__(self, tahun_dibuat, total_muatan):
                    super().__init__("Kapal Penumpang", tahun_dibuat, total_muatan)



            def main():
                kapal_cargo = KapalCargo(2010, 2000)
                kapal_tempur = KapalTempur(2015, 1500)
                kapal_ikan = KapalIkan(2018, 800)
                kapal_penumpang = KapalPenumpang(2020, 1000)

                for kapal in [kapal_cargo, kapal_tempur, kapal_ikan, kapal_penumpang]:
                    print(kapal.info())


            if __name__ == "__main__":
                main()