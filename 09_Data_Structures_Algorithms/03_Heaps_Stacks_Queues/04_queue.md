# Queue (Antrean)
    Struktur data yang beroperasi dengan prinsip FIFO (First In, First Out)
Eleemen yang pertama kali dimasukkan akan dimasukkan akan menjadi elemen yang pertama kali dikeluarkan. Konsep ini persis seperti antrean pelanggan di kasir supermarket; siapa yang datang lebih dulu, dia yang akan dilayani lebih dulu.

Rerdapat empat operasi utama dalam struktur data Queue:
- Enqueue: Menambahkan elemen ke posisi paling belakang (ekor antrean).
- Dequeue: Mengambil dan menghapus elemen dari posisi paling depan (kepala antrean).
- Fornt / Peek: melihat elemen paling depan tanpa menghapusnya dari memori.
- Is_Empty: Memeriksa apakah antrean saat ini dalam keadaan kosong.

## Mengapa List Biasa Kurang Tapat?
    Kita sebenarnya bisa membuat Queue menggunakan List bawaan Python. Namun, ini dianggap sebagi praktik yang buruk untuk performa.

Pada List, mengambail data terdepan mengharuskan Kita memanggil `pop(0)`. Begitu elemen terdepan dihapus. Python harus menggeser semua elemen yg tersisa satu persatu ke depan untuk mengisis kekosongan. Proses pergeseran ini memakan waktu O(n). Jika natrean Kita memuat jutaan data. operasi ini akan sangat membebani komputer.

## Menggunakan collections.deque
cara palnig PYhonic dan efisien membuat Queue adalah memanfaatkan tipe data `deque` (Double-Ended Queue) dari modul bawaan `collections`, Struktur `deque` dioptimalkan secara khusus menggunakan arsitektur mirip Doubly Linked List, sehingga eporasi tambah di belakang(`append`) dan hapus di deapn (`popleft`) berjalan secara instan dengan kompleksitas waktu O(1).