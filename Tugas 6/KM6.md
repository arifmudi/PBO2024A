Nama : Amal Alfarizal
Nim : 2355201017


Pengertian Polimorfisme
Polimorfisme berasal dari kata "poly" yang berarti banyak dan "morphe" yang berarti bentuk. Dalam konteks OOP, polimorfisme berarti kemampuan objek untuk 
memiliki banyak bentuk. Dengan kata lain, polimorfisme memungkinkan objek-objek yang berbeda untuk merespons pesan yang sama dengan cara yang berbeda.

Jenis-Jenis Polimorfisme
Polimorfisme pada Waktu Kompilasi (Compile-time Polymorphism)
Juga dikenal dengan method overloading.
Terjadi ketika ada lebih dari satu metode dengan nama yang sama, tetapi dengan parameter yang berbeda (baik jumlah atau tipe).
Polimorfisme pada Waktu Eksekusi (Run-time Polymorphism)
Juga dikenal dengan method overriding.
Terjadi ketika kelas turunan (subclass) menyediakan implementasi metode yang sudah ada di kelas induk (superclass).
Contoh Polimorfisme
1. Polimorfisme pada Waktu Kompilasi (Compile-time Polymorphism) - Method Overloading
Polimorfisme jenis ini terjadi saat ada dua atau lebih metode dengan nama yang sama dalam satu kelas, namun memiliki parameter yang berbeda.

java
Copy code
class Calculator {
    // Method dengan dua parameter integer
    public int add(int a, int b) {
        return a + b;
    }

    // Method dengan tiga parameter integer
    public int add(int a, int b, int c) {
        return a + b + c;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.add(10, 20));       // Output: 30
        System.out.println(calc.add(10, 20, 30));   // Output: 60
    }
}
Pada contoh di atas, ada dua metode add dengan nama yang sama tetapi berbeda dalam jumlah parameter. Ini adalah contoh polimorfisme pada waktu kompilasi.

2. Polimorfisme pada Waktu Eksekusi (Run-time Polymorphism) - Method Overriding
Pada polimorfisme ini, kita memiliki kelas induk dengan sebuah metode, dan kelas turunan yang meng-override (menimpa) metode tersebut dengan implementasi yang berbeda.

java
Copy code
// Kelas induk
class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Kelas turunan
class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}

// Kelas turunan lainnya
class Cat extends Animal {
    @Override
    public void sound() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myAnimal = new Animal();   // Membuat objek kelas induk
        Animal myDog = new Dog();         // Membuat objek kelas turunan
        Animal myCat = new Cat();         // Membuat objek kelas turunan
        
        myAnimal.sound();   // Output: Animal makes a sound
        myDog.sound();      // Output: Dog barks
        myCat.sound();      // Output: Cat meows
    }
}
Pada contoh di atas, meskipun tipe variabel myDog dan myCat adalah Animal, metode sound() yang dipanggil adalah implementasi yang ada di kelas turunan (Dog atau Cat). 
Ini adalah contoh polimorfisme pada waktu eksekusi (runtime polymorphism) yang terjadi berkat method overriding.

Manfaat Polimorfisme
Meningkatkan Fleksibilitas dan Reusabilitas Kode

Dengan polimorfisme, Anda dapat menulis kode yang lebih umum dan fleksibel. Sebagai contoh, kita bisa mendefinisikan suatu metode yang bekerja untuk berbagai objek yang 
berbeda tanpa perlu mengetahui kelas spesifik objek tersebut.

Contoh: Program yang mengelola berbagai jenis kendaraan (Car, Bike, Truck) bisa mendefinisikan metode start() tanpa perlu menulis implementasi spesifik untuk setiap kendaraan.

Pengurangan Duplikasi Kode

Polimorfisme memungkinkan Anda mengurangi duplikasi kode dengan menggabungkan berbagai implementasi berbeda ke dalam satu antarmuka atau kelas induk yang lebih umum.
Meningkatkan Pemeliharaan Kode

Dengan menggunakan polimorfisme, perubahan pada implementasi suatu metode di kelas induk akan secara otomatis mempengaruhi kelas-kelas turunannya yang meng-override metode tersebut, 
tanpa memerlukan perubahan pada kode yang menggunakannya.
Penggunaan Interface dan Abstraksi

Polimorfisme memungkinkan Anda menggunakan interface atau kelas abstrak untuk mendefinisikan metode yang wajib diimplementasikan oleh kelas-kelas turunannya. Hal ini meningkatkan 
pemisahan antara antarmuka (interface) dan implementasi.
Penerapan Pola Desain (Design Patterns)

Polimorfisme memainkan peran penting dalam banyak pola desain (design patterns), seperti Factory Method, Strategy, dan Command Pattern, yang memanfaatkan polimorfisme untuk meningkatkan 
fleksibilitas aplikasi.
Contoh Penggunaan Polimorfisme dalam Dunia Nyata
Misalkan Anda sedang membuat aplikasi sistem pembayaran yang mendukung berbagai metode pembayaran: Kartu Kredit, Transfer Bank, dan E-wallet. Anda bisa mendefinisikan sebuah antarmuka 
(interface) atau kelas induk yang disebut PaymentMethod, kemudian masing-masing kelas pembayaran (misalnya CreditCard, BankTransfer, dan EWallet) mengimplementasikan metode pay(). Ini 
akan memungkinkan aplikasi untuk menangani pembayaran tanpa perlu tahu detail implementasi setiap metode pembayaran.

java
Copy code
// Interface PaymentMethod
interface PaymentMethod {
    void pay(int amount);
}

// Kelas yang mengimplementasikan PaymentMethod
class CreditCard implements PaymentMethod {
    public void pay(int amount) {
        System.out.println("Paying " + amount + " using Credit Card");
    }
}

class BankTransfer implements PaymentMethod {
    public void pay(int amount) {
        System.out.println("Paying " + amount + " using Bank Transfer");
    }
}

class EWallet implements PaymentMethod {
    public void pay(int amount) {
        System.out.println("Paying " + amount + " using E-Wallet");
    }
}

public class Main {
    public static void main(String[] args) {
        PaymentMethod paymentMethod = new CreditCard();
        paymentMethod.pay(1000);  // Output: Paying 1000 using Credit Card

        paymentMethod = new BankTransfer();
        paymentMethod.pay(2000);  // Output: Paying 2000 using Bank Transfer

        paymentMethod = new EWallet();
        paymentMethod.pay(3000);  // Output: Paying 3000 using E-Wallet
    }
}
Pada contoh di atas, Anda dapat mengganti metode pembayaran dengan berbagai cara (kartu kredit, transfer bank, atau e-wallet) tanpa mengubah kode yang menggunakannya.

Kesimpulan
Polimorfisme adalah konsep dasar dalam OOP yang memungkinkan objek untuk memiliki banyak bentuk, dengan tujuan meningkatkan fleksibilitas, pemeliharaan kode, dan reusabilitas. Terdapat 
dua jenis polimorfisme utama: compile-time polymorphism (method overloading) dan run-time polymorphism (method overriding). Dengan menggunakan polimorfisme, Anda dapat menulis kode yang 
lebih fleksibel dan lebih mudah dipelihara dalam jangka panjang.

