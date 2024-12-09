Nama : M.Abdi Ahzani Nim : 2355201036 Matkul : PBO

                              POLIMORFISME

Polimorfisme adalah salah satu konsep utama dalam Pemrograman Berorientasi Objek (Object-Oriented Programming / OOP). Kata polimorfisme berasal dari bahasa Yunani: poly berarti "banyak", dan morphe berarti "bentuk". Dalam konteks OOP, polimorfisme memungkinkan satu antarmuka, metode, atau kelas memiliki berbagai bentuk atau perilaku yang berbeda.


Polimorfisme adalah kemampuan untuk memanggil metode pada suatu objek tanpa mengetahui tipe spesifik dari objek tersebut. Metode yang dipanggil bergantung pada implementasi spesifik dari objek tersebut. Dengan demikian, kita dapat menulis kode yang fleksibel dan dapat digunakan kembali tanpa harus memperhatikan detail implementasi setiap tipe objek.


Polimorfisme dalam pemrograman OOP dibagi menjadi dua jenis utama:
Polimorfisme Waktu Kompilasi (Compile-Time Polymorphism):
Terjadi ketika metode yang akan dijalankan diputuskan saat kompilasi.
Dicapai melalui method overloading (metode dengan nama yang sama tetapi parameter berbeda) atau operator overloading.
Polimorfisme Waktu Eksekusi (Runtime Polymorphism):
Terjadi ketika metode yang akan dijalankan diputuskan pada saat runtime.
Dicapai melalui inheritance dan method overriding.


Manfaat Polimorfisme
Kode yang Fleksibel:
Kode dapat menangani berbagai tipe objek tanpa perlu mengetahui detail implementasinya.
Reusability (Kode yang Dapat Digunakan Ulang):
Polimorfisme memungkinkan metode yang sama digunakan untuk tipe data yang berbeda, sehingga meminimalkan pengulangan kode.
Pemeliharaan Kode yang Lebih Mudah:
Perubahan pada implementasi kelas turunan tidak memengaruhi kode yang menggunakan kelas induk.


Modularitas:
Dengan menggunakan antarmuka atau kelas abstrak, kode dapat dirancang secara modular sehingga lebih mudah dipahami dan dikembangkan.
Mengikuti Prinsip Desain OOP:
Polimorfisme mendukung Open-Closed Principle, di mana kode mudah diperluas tanpa harus dimodifikasi.


Contoh Code:
class Kalkulator {
    // Menjumlahkan dua angka
    public int jumlah(int a, int b) {
        return a + b;
    }

    // Menjumlahkan tiga angka
    public int jumlah(int a, int b, int c) {
        return a + b + c;
    }

    // Menjumlahkan array angka
    public int jumlah(int[] angka) {
        int total = 0;
        for (int num : angka) {
            total += num;
        }
        return total;
    }
}

public class CompileTimePolymorphism {
    public static void main(String[] args) {
        Kalkulator kalkulator = new Kalkulator();

        System.out.println("Jumlah dua angka: " + kalkulator.jumlah(5, 10)); // Output: 15
        System.out.println("Jumlah tiga angka: " + kalkulator.jumlah(5, 10, 15)); // Output: 30
        System.out.println("Jumlah array angka: " + kalkulator.jumlah(new int[]{1, 2, 3, 4, 5})); // Output: 15
    }
}
