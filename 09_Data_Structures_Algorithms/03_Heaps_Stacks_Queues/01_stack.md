# Stack (Tumpukan) 
    adalah struktur data yang beroperasi dengan prinsip LIFO (Last In, First Out)
Elemen terakhir yang dimasukkan akan menjadi elemen pertama yang diambil. Bayangkan tumpukan piring; Ktia selalu menaruh piring baru di tumpukan paling atas, dan saat mengambil pirng, Kita jug mengambil dari tumpukan paling atasa.

Ada empat operasi utama dalam Stack:
- Push: Menambahkan elemen ke posisi paling atas.
- Pop: Mengambil dan menghapus elemen dari posisi paling atas.
- Peek / Top: Melihat elemen paling atas tanpa menghapusnya.
-Is_Empty: Memerika apakah stack kosong.

## Stack Menggunakan List Bawaaan (Cara Termudah)
Cara palnig sederhana membuat Stack di Python adalah menggunakan List biasa. List memiliki metode `append()` untuk menaruh data di ujung (berfungsi sebagai Push). dan metode `pop()` untuk mengambil data dari ujung (berfungsi sebagai Pop). Keduanya berjalan sangat cepat dengan kompleksitas waktu O(1).

## Stack Menggunakan Linked List (Cara Dinamis)
Kelelmahan menggunakan List biasa adalah Python secara internal perlu mengalokasikan ulang blok memori yang lebih besar jika Lish penuh, yang sesekali bisa memakana waktu O(n). 
Menggunakan Linked LIst menyelesaikan masalah ini karena dialokasikan secara dinamis per node. 

Untuk mempertahankan prinsip LIFO dengan efisiensi O(1), operasi Push dan Pop pada Linked List dilakukan tepat di posisi Head (paling depan), bukan di belakang