# Rekursi adalah teknik pemrograman di mana fungsi meemanggil dirinya sendiri
  secara berulang kali untuk memecahkan masalah. Alih-alih mencoba menyelesaikan masalah besar sekaligus, fungsi rekursif akan memecah masalah tersebut menjadi sub-masalah yang lebih kecil dan identik, hingga mencapai titik di mana masalah tersebut bisa langsung diselesaikan.

## Dua Pilar Utama Fungsi Rekursif
    Agar fungsi tidak memanggil dirinya sendiri tanpa henti (yang menyebabkan infinite loop dan membuat program crash), setiap fungsi rekursif wajib memiliki dua bagian:
- Base Case (Kondisi Berhenti): Titik akhir atau kondisi paling sederhana di mana fungsi tidak perlu lagi memanggil dirinya sendiri dan langsung  mengembalikan hasil.
- Recursive Case (Langkah Rekursif): Kondisi di mana fungsi memanggil dirinya sendiri dengan argumen/data yang nilainya sudah dimodifikasi (biasanya diperkecil) agar semakin mendekati Base Case.

## Bahaya Rekursi: Batas Kedalaman (Recursion Depth)
Meskipun kode rekursif sering kali lebih elegan dan singkat daripada menggunakan Loop (seperti  `for` atau `while`), ia memiliki kelemahana dalam hal memori. 
Setiap kali fungsi memanggil dirinya sendiri. Python harus menyimpan status fungsi tersebut ke dalam memori (Call Stack).

Jika Kita luap menambahkan Base Case, atau jika Base Case tidak pernah tercapai, tumpukan memori akan penuh. Python memiliki sistem keamanan bawaan untuk mencegah komputer hang. Jika fungsi memangggil dirinya sendiri lebih dari ~1000 kali berturut-turut, Python akan menghentikan program dan memunculkan error:
`RecursionError: maximum recursion depth exceeded`.