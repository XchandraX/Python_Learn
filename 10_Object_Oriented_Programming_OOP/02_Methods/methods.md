# Methods (Jenis-jenis Metode)

Dalam sebuah Class, tidak semua metode ditujukan untuk memanipulasi objek. Python membagi menjadi tiga jenis:

1. Instance Method: Metode standar. Menggunakan self. Bisa mengakses dan mengubah state (data) dari objek spesifik.

2. Class Method (@classmethod): Menggunakan cls (bukan self), Tidak peduli dengan objek spesifik, metode ini emngubha state dari Class itu sendri secara global. Sering digunakan sebagai pembuat objek alternatif (Factory Method).

3. Static Method (@staticmethod); Tidak menggunakan self maupun cls, ini hanyalah fungsi biasa yang diletakkan di dalam Class agar rapi karena secara logika masih berhubungan dengan Class tersebut.