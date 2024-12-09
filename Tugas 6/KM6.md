Nama : Khairun Fadli Nim : 2355201043 Matkul : PBO

------------------------------------------------------Polimorfisme--------------------------------------------------

**Pengertian Polimorfisme**  

Polimorfisme adalah salah satu konsep fundamental dalam pemrograman berorientasi objek (Object-Oriented Programming, OOP) yang memungkinkan suatu objek atau fungsi untuk memiliki banyak bentuk (bentuk yang berbeda-beda) tergantung pada bagaimana ia digunakan. Kata *polimorfisme* sendiri berasal dari bahasa Yunani, yaitu "poly" yang berarti banyak, dan "morph" yang berarti bentuk.  

 **Jenis-jenis Polimorfisme**  
Polimorfisme dapat dibagi menjadi dua jenis utama:  

1. **Polimorfisme pada waktu kompilasi (Compile-time Polymorphism)**  
   Polimorfisme jenis ini dikenal juga sebagai *method overloading* atau *operator overloading*. Polimorfisme ini terjadi ketika sebuah fungsi atau metode memiliki nama yang sama, tetapi parameter atau argumennya berbeda. Contohnya:  
   ```java
   class Calculator {
       // Overloading method add
       int add(int a, int b) {
           return a + b;
       }

       double add(double a, double b) {
           return a + b;
       }
   }
   ```  
   Di sini, metode `add` bisa menangani argumen dengan tipe data berbeda, tetapi nama metode tetap sama.

2. **Polimorfisme pada waktu runtime (Runtime Polymorphism)**  
   Polimorfisme ini dikenal juga sebagai *method overriding*. Ini memungkinkan subclass untuk menyediakan implementasi yang berbeda dari metode yang didefinisikan di superclass. Contohnya:  
   ```java
   class Animal {
       void sound() {
           System.out.println("Animal makes a sound");
       }
   }

   class Dog extends Animal {
       @Override
       void sound() {
           System.out.println("Dog barks");
       }
   }

   class Cat extends Animal {
       @Override
       void sound() {
           System.out.println("Cat meows");
       }
   }
   public class Main {
       public static void main(String[] args) {
           Animal animal;

           animal = new Dog();
           animal.sound(); // Output: Dog barks

           animal = new Cat();
           animal.sound(); // Output: Cat meows
       }
   }
   ```  
   Pada contoh di atas, metode `sound()` dipanggil berdasarkan tipe objek pada runtime, meskipun referensinya adalah tipe `Animal`.

**Manfaat Polimorfisme**
1. **Fleksibilitas**: Memungkinkan kode yang lebih fleksibel karena objek dapat digunakan dalam berbagai bentuk.
2. **Pemeliharaan Kode**: Dengan polimorfisme, kode dapat diperbarui atau ditingkatkan tanpa memengaruhi komponen lain secara signifikan.
3. **Reduksi Duplikasi Kode**: Menghindari penulisan kode yang berulang dengan cara mengatur fungsi atau metode yang generik.

### **Implementasi Polimorfisme**
Polimorfisme banyak digunakan dalam pemrograman OOP untuk mendukung prinsip *reusability* dan *extensibility*. Contohnya, dalam desain aplikasi, polimorfisme sering digunakan untuk membuat antarmuka (*interfaces*) atau kelas abstrak yang dapat diimplementasikan oleh berbagai kelas konkret.

Dengan memahami dan menerapkan polimorfisme, pengembang perangkat lunak dapat membuat sistem yang lebih terorganisasi, mudah dikembangkan, dan mudah dipelihara.