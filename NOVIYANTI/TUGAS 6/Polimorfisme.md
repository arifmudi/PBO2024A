# Polimorfisme
    Polimorfisme adalah salah satu konsep utama dalam pemrograman berorientasi objek. Dalam bahasa sederhana, 
polimorfisme memungkinkan kita menggunakan satu nama metode yang sama, tetapi dengan perilaku yang berbeda 
tergantung pada jenis objek yang menjalankannya. 

    Bayangkan ada seekor anjing, kucing, dan burung. Ketiganya adalah "hewan", tetapi kalau diminta bersuara, 
masing-masing akan menghasilkan suara yang berbeda: anjing menggonggong, kucing mengeong, dan burung berkicau. 
Dalam dunia pemrograman, kita bisa membuat satu metode bernama `suara` yang dapat digunakan oleh ketiga jenis 
hewan ini, tetapi mereka akan memberikan hasil berbeda sesuai jenisnya.

# Jenis Polimorfisme
 1. Polimorfisme Saat Kompilasi (Compile-time Polymorphism):
   - Metode yang namanya sama tetapi parameternya berbeda. Contohnya adalah metode dengan jumlah atau tipe 
     parameter yang berbeda.
   - Ini dikenal sebagai method overloading.
   - Python tidak mendukung method overloading secara langsung seperti Java, tetapi kita bisa mengakalinya.

2. Polimorfisme Saat Program Berjalan (Runtime Polymorphism):
   - Metode yang didefinisikan di kelas induk dapat di-override oleh kelas anak.
   - Ini dikenal sebagai method overriding, dan Python mendukungnya dengan baik.
   - Saat program dijalankan, metode yang dipanggil akan sesuai dengan jenis objek yang sedang digunakan.

# Contoh Polimorfisme
# *Cerita dalam Program*
    Ada seekor hewan, seekor anjing, dan seekor kucing. Ketiganya bisa "bersuara". Kita akan membuat satu 
metode bernama `suara`, tetapi perilaku mereka berbeda tergantung pada jenisnya.

# *Kodingan*

# Kelas induk bernama 'Hewan'
class Hewan:
    def suara(self):
        print("Hewan ini bersuara.")

# Kelas 'Anjing' mewarisi kelas 'Hewan' dan mengubah perilaku metode 'suara'
class Anjing(Hewan):
    def suara(self):
        print("Anjing menggonggong.")

# Kelas 'Kucing' juga mewarisi kelas 'Hewan' dan memberikan perilaku spesifik
class Kucing(Hewan):
    def suara(self):
        print("Kucing mengeong.")

# Membuat daftar hewan
daftar_hewan = [Hewan(), Anjing(), Kucing()]

# Semua hewan diperlakukan sama, tapi suara mereka berbeda
for hewan in daftar_hewan:
    hewan.suara()

# *Hasil Output*

Hewan ini bersuara.
Anjing menggonggong.
Kucing mengeong.


# Kenapa Polimorfisme Penting?

1. Kode Lebih Fleksibel: Kita tidak perlu membuat metode dengan nama berbeda untuk setiap jenis objek. 
   Satu metode bisa digunakan untuk banyak kelas.
2. Mudah Dikembangkan:Jika ingin menambah jenis objek baru (misalnya burung), cukup tambahkan kelas baru 
   tanpa mengubah kelas yang sudah ada.
3. Reusabilitas Tinggi: Kelas induk dan metode dasarnya bisa digunakan berulang kali oleh kelas-kelas anak 
   tanpa perlu duplikasi kode.

# Kesimpulan
    Polimorfisme membuat program lebih sederhana, efisien, dan mudah dikelola. Dengan konsep ini, kita bisa 
menggunakan satu metode untuk berbagai macam objek tanpa kehilangan fleksibilitas perilaku.