Nama    : Arjunaidi
Nim     : 2355201040
Matkul  : PBO

                                           Konsep Interhitance
Inheritance, atau pewarisan, adalah salah satu konsep fundamental dalam pemrograman berorientasi objek (OOP). Konsep ini memungkinkan sebuah kelas (class) untuk mewarisi atribut dan metode dari kelas lain, yang dikenal sebagai kelas induk (parent class) atau superclass. Dengan menggunakan inheritance, pengembang dapat membangun hierarki kelas yang lebih terstruktur dan efisien.

Konsep Single Inheritance dalam Pemrograman
Single inheritance adalah bentuk dasar dari pewarisan dalam pemrograman berorientasi objek, di mana sebuah subclass mewarisi atribut dan metode dari satu superclass. Single Inheritance dipakai ketika hubungan antar kelas tidak kompleks dan hanya perlu satu tingkatan level pewarisan. Single Inhertance dipakai ketika ingin memanfaatkan kembali kode dari sebuah class induk tanpa adanya tambahan kompleksitas. Single Inheritance dipakai ketika sebuah subclass perlu untuk menambahkan atau mengubah sebuah perilaku dari superclass tanpa terjadinya kebingungan interaksi yang mungkin terjadi dengan multiple inheritance.

*Implmentasi single inheritance*
        #buat class induk
        class Burung:
            def bicara(self):
                print("camar bersuara")

        #class anak mewarisi class induk
        class camar(Burung):
            def berbunyi(self):
                print("berbunyi!!! berbunyi!!!")

        #Membuat objek dari class camar
        camar = camar()
        camar.bicara()  #akses metode class induk
        anjing.berbunyi()   #akses metode class anak

PENJELASAN SINGKAT :
    1. class induk 'Burung' didefinisikan dengan metode 'bicara' yang mencetak string
    2. class anak 'Camar' melakukan pewarisan dari 'Burung' dan mempunyai penambahan metode 'berbunyi'
    3. objek 'camar' dapat melakukan akses metode 'bicara' dari class induk dan metode 'berbunyi' dari class anak

    
                                                 Konsep Super
Konsepd super() dalam python adalah sebuah fungsi yang dipakai untuk melakukan akses method dan atribut dari class induk (superclass). dalam konteks inheritance, cara ini lumayan berguna jika ingin memanggil konstruktor atau method dari class induk dalam subclass, sehingga dapat memanfaatkan fungsionalitas yang telah ada sebelumnya.
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

                                                Jenis interhitance
    Multiple Inheritance
    Kelas anak mewarisi dari lebih dari satu kelas induk. Ini memungkinkan akses ke atribut dan metode dari semua kelas induk yang terlibat. Namun, dapat menyebabkan kebingungan jika ada metode dengan nama yang sama di kelas induk.

            class mamalia:
                def mamalia_info(self):
                    print("Mamalia bisa melahirkan")

            class Hewansayap:
                def info_hewan_sayap(self):
                    print("mamalia bersirip bisa berenang")

            class Bat(amal, Hewanbersirip):
                pass

            # Membuat objek dari kelas Bat
            b1 = lumba-lumba()
            b1.mamalia_info()         
            b1.info_hewan_bersirip()   

    Multilvel Inheritance
    Kelas anak mewarisi dari kelas induk yang juga merupakan turunan dari kelas lain. Ini membentuk rantai pewarisan, di mana subclass dapat mewarisi perilaku dari superclass dan juga dari kelas induk lainnya.

            class hewanlaut:
                def suara(self):
                    print("hewan bersuara")

            class ikan(hewanlaut):
                def blub(self):
                    print("Lumba-lumba klikikli ")

            class lumba(ikan):
                def berenang(self):
                    print("lumba berenang")

    Hierarchical Inheritance
    Beberapa subclass mewarisi dari satu superclass yang sama. Ini memungkinkan berbagai subclass untuk berbagi atribut dan metode dari superclass, memudahkan pengelolaan kode yang memiliki kesamaan.

                class kendaraan:
                    def start(self):
                        print("kendaraan menyala")

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

    Hybrid Inheritance
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

                                            konsep overiding method 
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

                                            Inheritance dan Non-Inheritance 
Kapan Menggunakan Pewarisan (Inheritance)
    Ketika ada beberapa kelas yang memiliki atribut dan metode yang sama, menggunakan inheritance dapat mengurangi duplikasi kode.
    jika Anda perlu membuat struktur yang mencerminkan hubungan "adalah" (misalnya, Burung adalah subclass dari Hewan), inheritance memungkinkan Anda untuk mendefinisikan hubungan ini secara jelas dalam kode.
Kapan Menggunakan Non-Pewarisan (Non-Composition)
    Ketika ada beberapa kelas yang memiliki atribut dan metode yang sama, menggunakan inheritance dapat mengurangi duplikasi kode.
    Penggunaan komposisi memungkinkan pengembang untuk menggabungkan berbagai fungsionalitas tanpa terikat pada hierarki kelas tertentu. Ini memberikan fleksibilitas yang lebih besar dalam merancang sistem dan memungkinkan reuse kode yang lebih efisien.

                                                       study kasus 
    Brodi seorang yang sangat tertarik dengan kapal perang, saat terdiam dan melamun dia memikirkan bagaimana saat kinerja sebuah kapal dalam kode python lalu dia berniat untuk membuat strukturnya dalam sebuah kode python dibawah ini

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
