# Konsep Dasar OOP (Object Oriented Programming)

## Daftar Isi
1. [Class](#class)
2. [Object](#object)
3. [Atribut](#atribut)
4. [Method](#method)
5. [Constructor](#constructor)
6. [Access Modifier](#access-modifier)
7. [Encapsulation](#encapsulation)

## Class
Class adalah blueprint atau template untuk membuat object. Class mendefinisikan atribut dan method yang akan dimiliki oleh object.

### Contoh Class:
```java
public class Mobil {
    // Atribut
    String merk;
    String warna;
    int tahun;
    
    // Method
    void start() {
        System.out.println("Mobil dinyalakan");
    }
}
```

## Object
Object adalah instance dari class. Object memiliki state (atribut) dan behavior (method) sesuai dengan yang didefinisikan di class.

### Contoh pembuatan Object:
```java
Mobil mobilSaya = new Mobil();
mobilSaya.merk = "Toyota";
mobilSaya.warna = "Merah";
mobilSaya.tahun = 2020;
mobilSaya.start();
```

## Atribut
Atribut adalah variabel yang ada di dalam class. Atribut merepresentasikan karakteristik atau properti dari object.

### Contoh Atribut:
```java
public class Mahasiswa {
    // Atribut
    String nama;
    String nim;
    int umur;
    double ipk;
}
```

## Method
Method adalah fungsi yang ada di dalam class. Method merepresentasikan perilaku atau aksi yang bisa dilakukan object.

### Contoh Method:
```java
public class Kalkulator {
    int tambah(int a, int b) {
        return a + b;
    }
    
    int kurang(int a, int b) {
        return a - b;
    }
    
    void tampilkanHasil(int hasil) {
        System.out.println("Hasil: " + hasil);
    }
}
```

## Constructor
Constructor adalah method khusus yang dipanggil saat object dibuat. Constructor digunakan untuk menginisialisasi atribut object.

### Contoh Constructor:
```java
public class Siswa {
    String nama;
    int umur;
    
    // Constructor
    public Siswa() {
        // Constructor default
    }
    
    // Constructor dengan parameter
    public Siswa(String nama, int umur) {
        this.nama = nama;
        this.umur = umur;
    }
}
```

## Access Modifier
Access modifier menentukan tingkat akses dari class, atribut, dan method.

### Jenis Access Modifier:
1. **public**: Bisa diakses dari mana saja
2. **private**: Hanya bisa diakses dari dalam class yang sama
3. **protected**: Bisa diakses dari class yang sama dan turunannya
4. **default**: Bisa diakses dari package yang sama

### Contoh Access Modifier:
```java
public class Pegawai {
    public String nama;        // Bisa diakses dari mana saja
    private double gaji;       // Hanya bisa diakses dalam class Pegawai
    protected String jabatan;  // Bisa diakses class turunan
    String departemen;         // Default - bisa diakses dalam package yang sama
    
    public void setGaji(double gaji) {
        this.gaji = gaji;
    }
    
    private void hitungBonus() {
        // Method private
    }
}
```

## Encapsulation
Encapsulation adalah konsep menyembunyikan data dan detail implementasi dari luar class. Ini dilakukan dengan:
1. Membuat atribut private
2. Menyediakan public getter dan setter method

### Contoh Encapsulation:
```java
public class BankAccount {
    private String accountNumber;
    private double balance;
    
    // Getter methods
    public String getAccountNumber() {
        return accountNumber;
    }
    
    public double getBalance() {
        return balance;
    }
    
    // Setter methods
    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }
    
    public void setBalance(double balance) {
        if (balance >= 0) {
            this.balance = balance;
        }
    }
    
    // Method untuk operasi
    public void deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
        }
    }
    
    public boolean withdraw(double amount) {
        if (amount <= balance && amount > 0) {
            this.balance -= amount;
            return true;
        }
        return false;
    }
}
```

### Manfaat Encapsulation:
1. Data Hiding: Menyembunyikan detail implementasi
2. Increased Flexibility: Mudah mengubah implementasi tanpa mempengaruhi code yang menggunakan class
3. Reusability: Code lebih mudah digunakan ulang
4. Testing: Lebih mudah untuk testing karena interface yang jelas