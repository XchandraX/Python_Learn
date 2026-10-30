# Context Manager (Manajemen Memori Otomatis)
Saat Kita berurusan dengan database atau membuka file, Kita wajib menutupnya setelah selesai agar memori komputer tidak bocor (memory leak).
Di Python, cara paling profesional utnuk melakukan adalah menggunakan blok with. Kita bisa membuat Class kita sendiri mendukung blok with (menjadi Context Manager) dengan menambahkan dua dunder methods (Double Underscrose):
- __enter__: Dijalankan saat memasukan blok with (Setup/Buka)
- __exit__: Dijalankan secara absolut saat keluar blok with (Teardown/Tutup), bahkan jika terjadi error/crash di tengah jalan!
