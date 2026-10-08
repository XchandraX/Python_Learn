# Hashmaps
    HashMap, HashTable, Map, dan Associative Array merujuk pada konsep arsitektur yang sama: Struktur data yang memetakan Kunci (Key) ke Nilai (Value).

Di Python, implementasi asli dan paling dari HashMap adalah struktur data Dictionary (`dict`)

## Rahasi Kecepatan HashMap (Fungsi Hash)
Keunggulan mutlak dari HashMap dibandingkan List atau Linked List adalah kecepatannya. Watku yang dibutuhkan untuk mencari, atau menghapus data adalah O(1) (seketika), tidak peduli apakah data Kita berjumlah 10 atau 10 juta.

*Bagaimana ini bisa terjadi?*:
- Saat Kita mamasukan Key, Ptython tidak menyimpannya secara berurutan.
- Python akan menjalankan sebuah fungsi matematika khusus (fungsi hash) pada Key tersebut.
- Fungsi hash akan mengonversi teks/angka dari Key menjadi sebuah angka unik. Angka unik inilah yang langsung menjadi alamat indeks memori tempat Value disimpan.
- Saat Kita mencari data, Python cukup menghitung hash dari Key yang Kita cari dan langsung melompat ke alamat memori tersebut tanpa perlu menelusuri data satu per satu.

## Syarat Mutlak HashMap di Python
    Karena sangat bergantung pada nilai hash, dan aturan ketat yang berlaku:
- Key harus Immutable (Tidak bisa diubah): Kita hanya bisa menggunakan tipe data seperti String, Integer, Float, atau Tuple sebagai Key. Kita tidak bisa menggunakan List atau Set sebagi Key karena isinya bisa berubah (yang akan merusak nilai hash aslinya).
- Key harus Unik: Jika Kita memasukkan Key yang sama dua kali, nilai yang baru akan menimpa/menggantikan nilai yang lama.

## Penanganan Tabrakan (Hash Collision)
    Dalam kasus yang langka, fungsi hash bisa saja menghasilkan alamat memori yang persis sama untuk dua key yang berbeda (ini disebut Collision atau Tabrakan).

Python mengatasi hal ini menggunakan teknik yang disebut Open Addressing (khususnya variasi)