Nama : Khairun Fadli Nim : 2355201043 Matkul : PBO

-------------------------------------------------------- Polimorfisme -------------------------------------------------------------------------------
# Polimorfisme dalam Pemrograman

## Pengertian Dasar
Polimorfisme berasal dari bahasa Yunani yang berarti "banyak bentuk".
Dalam konteks pemrograman, polimorfisme adalah kemampuan suatu objek untuk memiliki banyak bentuk atau perilaku yang berbeda berdasarkan konteks atau parameter yang diberikan.

## Jenis-Jenis Polimorfisme

### 1. Polimorfisme Compile-Time (Statis)
Polimorfisme jenis ini terjadi pada saat kompilasi dan biasa disebut method overloading. Contoh dalam Java:

```java
class Calculator {
    // Metode pertama untuk integer
    public int tambah(int a, int b) {
        return a + b;
    }

    // Metode kedua untuk double
    public double tambah(double a, double b) {
        return a + b;
    }
}
```

### 2. Polimorfisme Run-Time (Dinamis)
Polimorfisme ini terjadi melalui pewarisan dan method overriding. Contoh dalam Python:

```python
class Hewan:
    def bersuara(self):
        print("Suara hewan")

class Kucing(Hewan):
    def bersuara(self):
        print("Meong!")

class Anjing(Hewan):
    def bersuara(self):
        print("Guk guk!")

# Penggunaan polimorfisme
def tampilkan_suara(hewan):
    hewan.bersuara()

# Objek berbeda dengan metode yang sama
kucing = Kucing()
anjing = Anjing()

tampilkan_suara(kucing)   # Output: Meong!
tampilkan_suara(anjing)   # Output: Guk guk!
```

## Keuntungan Polimorfisme

1. **Fleksibilitas**: Memungkinkan kode yang lebih fleksibel dan dapat digunakan ulang.
2. **Abstraksi**: Membantu dalam membuat desain yang lebih abstrak dan modular.
3. **Kemudahan Pengembangan**: Memudahkan penambahan fungsionalitas baru tanpa mengubah kode yang sudah ada.

## Contoh Praktis dalam Bahasa Java

```java
public class PolimorfismeContoh {
    public static void main(String[] args) {
        Bentuk[] bentukArray = new Bentuk[3];
        bentukArray[0] = new Lingkaran(5);
        bentukArray[1] = new Persegi(4);
        bentukArray[2] = new Segitiga(3, 4);

        // Menghitung luas setiap bentuk
        for (Bentuk bentuk : bentukArray) {
            System.out.println("Luas: " + bentuk.hitungLuas());
        }
    }
}

abstract class Bentuk {
    abstract double hitungLuas();
}

class Lingkaran extends Bentuk {
    private double jari;

    public Lingkaran(double jari) {
        this.jari = jari;
    }

    @Override
    double hitungLuas() {
        return Math.PI * jari * jari;
    }
}

class Persegi extends Bentuk {
    private double sisi;

    public Persegi(double sisi) {
        this.sisi = sisi;
    }

    @Override
    double hitungLuas() {
        return sisi * sisi;
    }
}

class Segitiga extends Bentuk {
    private double alas;
    private double tinggi;

    public Segitiga(double alas, double tinggi) {
        this.alas = alas;
        this.tinggi = tinggi;
    }

    @Override
    double hitungLuas() {
        return 0.5 * alas * tinggi;
    }
}
```

## Praktek Terbaik

1. Gunakan polimorfisme untuk membuat kode yang lebih generic dan fleksibel.
2. Pahami perbedaan antara polimorfisme compile-time dan run-time.
3. Gunakan abstraksi dan antarmuka untuk mencapai polimorfisme yang lebih baik.

## Kesalahan Umum yang Perlu Dihindari

1. Overusing polimorfisme yang dapat membuat kode menjadi kompleks.
2. Tidak memahami perbedaan antara inheritance dan composition.
3. Membuat hierarki kelas yang terlalu dalam.

Polimorfisme adalah konsep fundamental dalam pemrograman berorientasi objek yang memungkinkan fleksibilitas dan ekstensibilitas dalam desain perangkat lunak. Dengan memahami dan menerapkan konsep ini dengan baik, Anda dapat membuat kode yang lebih bersih, modular, dan mudah dipelihara.